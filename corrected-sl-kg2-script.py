import networkx as nx
import pandas as pd
import numpy as np
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_data(project_path, hgnc_path, sl_path):
    """Load HGNC and synthetic lethality data from parquet files."""
    try:
        hgnc_data = pd.read_parquet(os.path.join(project_path, hgnc_path))
        sl_data = pd.read_parquet(os.path.join(project_path, sl_path))
        logger.info(f"Loaded {len(hgnc_data)} HGNC records and {len(sl_data)} synthetic lethality records")
        return hgnc_data, sl_data
    except Exception as e:
        logger.error(f"Error loading data: {str(e)}")
        raise

def create_hgnc_dict(hgnc_data):
    """Create a dictionary for HGNC data lookups."""
    return hgnc_data.set_index('symbol').to_dict('index')

def add_node(G, gene, gene_type, hgnc_dict):
    if gene not in G:
        attrs = {'gene_type': gene_type}
        if gene in hgnc_dict:
            for k, v in hgnc_dict[gene].items():
                if isinstance(v, (pd.Series, pd.DataFrame)):
                    if not v.isnull().all():  # Check if the entire Series/DataFrame is not null
                        attrs[k] = v.dropna().tolist()  # Convert non-null values to a list
                elif isinstance(v, (list, tuple)):
                    non_null_values = [item for item in v if pd.notna(item)]
                    if non_null_values:  # Only add non-null values
                        attrs[k] = non_null_values
                elif isinstance(v, (np.ndarray)):
                    if pd.notna(v).any():  # Check if any non-null values exist in the array
                        attrs[k] = v[pd.notna(v)].tolist()  # Convert non-null values to a list
                elif pd.notna(v):  # For scalar values, check if it's not null
                    attrs[k] = v
        G.add_node(gene, **attrs)

def create_graph(sl_data, hgnc_dict):
    """Create a graph from synthetic lethality data and HGNC information."""
    G = nx.DiGraph()
    for _, row in sl_data.iterrows():
        sl_gene = row['SL_GENE']
        tsg_genes = row['TS_GENE'].split(',')
        for tsg_gene in tsg_genes:
            add_node(G, sl_gene, 'SL_GENE', hgnc_dict)
            add_node(G, tsg_gene, 'TS_GENE', hgnc_dict)
            G.add_edge(sl_gene, tsg_gene, relationship_type='synthetic_lethality')
    return G

def prepare_graph_for_export(G):
    """Prepare the graph for export by converting all attributes to strings."""
    for node, data in G.nodes(data=True):
        for key, value in data.items():
            if isinstance(value, (list, tuple)):
                G.nodes[node][key] = ','.join(map(str, value))
            else:
                G.nodes[node][key] = str(value)
    for u, v, data in G.edges(data=True):
        for key, value in data.items():
            G[u][v][key] = str(value)
    return G

def main():
    project_path = 'C://Users//donbr//github//nsclc-pathways//'
    hgnc_data_path = 'biogrid//crispr-paper//hgnc.parquet'
    sl_data_path = 'biogrid/crispr-paper/sl_data.parquet'
    output_path = "ts_sl_gene_graph.graphml"

    try:
        hgnc_data, sl_data = load_data(project_path, hgnc_data_path, sl_data_path)
        logger.info(f"HGNC data columns: {hgnc_data.columns.tolist()}")
        logger.info(f"SL data columns: {sl_data.columns.tolist()}")

        hgnc_dict = create_hgnc_dict(hgnc_data)
        logger.info(f"Created HGNC dictionary with {len(hgnc_dict)} entries")

        G = create_graph(sl_data, hgnc_dict)
        logger.info(f"Created graph with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")

        G = prepare_graph_for_export(G)
        nx.write_graphml(G, output_path)
        logger.info(f"Saved graph to {output_path}")

        # Validate saved graph
        G_loaded = nx.read_graphml(output_path)
        assert G.number_of_nodes() == G_loaded.number_of_nodes(), "Node count mismatch"
        assert G.number_of_edges() == G_loaded.number_of_edges(), "Edge count mismatch"
        logger.info("Graph validation successful")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)

if __name__ == "__main__":
    main()
