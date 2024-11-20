# BioGRID

- consider this as a temporary placeholder that will likely be deleted based on more recent research

- as an initial search for synthetic lethality I recommend using the [STRING "Geneset by Pathway / Process / Disease / Publication"](https://string-db.org/cgi/input?input_page_active_form=single_term) option from the initial search screen.
  - use a search terms similar to "TP53 synthetic lethality"
  - this will return a list of publications that can then be used to generate the graph network

- in many respects when querying for synthetic lethality / negative genetic interactor genes the most valuable column is the "Publication Source" (I think this mapped to around 7 PubMed references total)

- core files for TP53
  - [biogrid-synthetic-lethality-filtered-cols.csv](./biogrid-tp53-synthetic-lethality-filtered-cols.csv)
  - [biogrid-tp53-negative-genetic-filtered-cols.csv](./biogrid-tp53-negative-genetic-filtered-cols.csv)
- core files for RB1
  - stay tuned

## CITATION:

> Oughtred R, Rust J, Chang C, Breitkreutz BJ, Stark C, Willems A, Boucher L, Leung G, Kolas N, Zhang F, Dolma S, Coulombe-Huntington J, Chatr-Aryamontri A, Dolinski K, Tyers M. The BioGRID database: A comprehensive biomedical resource of curated protein, genetic, and chemical interactions. Protein Sci. 2021 Jan;30(1):187-200. doi: 10.1002/pro.3978. Epub 2020 Nov 23. PMID: 33070389; PMCID: PMC7737760.
