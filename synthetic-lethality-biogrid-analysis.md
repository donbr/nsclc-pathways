# Introduction to BioGRID Synthetic Lethality Analysis

This document presents an initial analysis of synthetic lethality and negative genetic interactions associated with the TP53 gene, a crucial tumor suppressor often mutated in various cancers. The analysis utilizes data from BioGRID (Biological General Repository for Interaction Datasets) and visualizations from STRING-DB (Search Tool for the Retrieval of Interacting Genes/Proteins Database).

## Purpose of the Analysis

1. **Identify Synthetic Lethal Interactions**: To discover genes that, when inhibited or mutated, cause cell death specifically in TP53-deficient cancer cells. This information is valuable for developing targeted cancer therapies.

2. **Explore Negative Genetic Interactions**: To understand genetic interactions where the combined effect of mutations in two genes is more severe than expected, providing insights into genetic networks and potential drug targets.

3. **Visualize Protein Interaction Networks**: Using STRING-DB to create visual representations of how the identified genes interact, helping to elucidate functional relationships and potential pathways for intervention.

4. **Cluster Analysis**: To group genes with similar functions or interactions, facilitating the identification of key pathways and processes affected by TP53 mutations.

This analysis aims to provide researchers and clinicians with valuable insights for developing new therapeutic strategies for cancers with TP53 mutations, particularly in the context of personalized medicine and targeted therapies.

## Synthetic Lethality

[Gene Information from BioGrid](biogrid\biogrid-tp53-synthetic-lethality-filtered-cols.csv)

![synthetic-lethality](biogrid\string-analysis\string-biogrid-p53-synthetic-lethality.png)

### Cluster Description

| Cluster | Color | Hex Color | Gene Count | Primary Description | Secondary Description | Tertiary Description | Protein Names |
|---------|-------|-----------|------------|---------------------|----------------------|----------------------|---------------|
| 1 | Red | #ff0000 | 20 | ErbB signaling pathway | Regulation of signaling by CBL | Mixed, incl. Signaling by Erythropoietin, and Insulin receptor complex | PIK3R2, SH2D2A, FLT4, CRKL, GAB1, KDR, PTK2, MTOR, EGFR, PIK3R3, PIK3CB, PIK3CD, ID1, EFNA4, SHC4, GJA5, ANXA11, UMOD, TPCN2, STEAP4 |
| 2 | Brown | #ffc165 | 8 | Blood group antigen | Hemoglobin complex, and Ammonium Transporter Family | - | GYPC, RHAG, BSG, CD47, RHD, RHCE, GYPA, GYPB |
| 3 | Olive | #8eb200 | 4 | TP53 regulates transcription of several additional cell death genes whose specific roles in p53-dependent apoptosis remain uncertain | - | - | TP53, FBXO22, CCT6B, BCL2L14 |
| 4 | Green | #84ff65 | 4 | Platelet Adhesion to exposed collagen | Integrin | - | GP6, ITGA2, CD69, ITGB7 |
| 5 | Lime Green | #00b247 | 4 | Congenital myasthenic syndrome | Acetylcholine-gated channel complex, and Myasthenia gravis | - | PRIMA1, RAPSN, COLQ, DOK7 |
| 6 | Cyan | #65feff | 3 | - | - | - | GFPT2, SATL1, EIF2B3 |
| 7 | Blue | #0047b2 | 3 | Fanconi Anemia Pathway | - | - | CDC7, ATRIP, FAAP24 |
| 8 | Purple | #8465ff | 2 | - | - | - | UBA6, UFM1 |



[Cluster Detail](biogrid\string-analysis\string-biogrid-p53-sl-MCL-clusters.tsv)

## Negative Genetic

[Gene Information from BioGrid](biogrid\biogrid-tp53-negative-genetic-filtered-cols.csv)

![negative-genetic](biogrid\string-analysis\string-biogrid-p53-negative-genetic.png)

### Cluster Descriptions

| Cluster | Color | Hex Color | Gene Count | Primary Description | Secondary Description | Tertiary Description | Protein Names |
|---------|-------|-----------|------------|---------------------|----------------------|----------------------|---------------|
| 1 | Red | #ff0000 | 25 | - | - | - | NFKBIA, CDK4, TP53, IKBKG, KMT2D, CDK9, MAD2L2, KRT5, LGR6, ERBB3, GATA2, TYMS, RCC1, USP4, OTULIN, ATP2C1, TRIM3, WNT4, ATN1, GATAD2B, WRAP53, PRIMA1, DYRK2, KDM1A, SLC2A1 |
| 2 | Salmon | #ff8c65 | 6 | Peptide ligand-binding receptors | - | - | BDKRB1, NTSR2, SST, GPER1, OPRD1, GNAS |
| 3 | Brown | #b25a00 | 5 | Calcium-ion regulated exocytosis | Schizophrenia | - | SYN2, SYT5, ERI3, SYT12, DAOA |
| 4 | Yellow | #ffd965 | 4 | - | - | - | IGF2BP1, THRB, PUM2, TRIP12 |
| 5 | Dark Golden Rod | #b0b200 | 3 | - | - | - | UNC13D, CD8A, PVRIG |
| 6 | Khaki | #d6ff65 | 3 | SWI/SNF complex | - | - | SMARCD3, BICRAL, BRD7 |
| 7 | Olive Drab | #56b200 | 3 | - | - | - | ZMAT2, ZNF207, BPTF |
| 8 | Light Green 2 | #89ff65 | 3 | Guanylate kinase activity | - | - | LIN7C, MAGI3, MPP1 |
| 9 | Green | #00b203 | 3 | - | - | - | PSMC3, TXNL1, POMP |
| 10 | Light Green | #65ff8f | 2 | - | - | - | POLR2C, RPRD1B |
| 11 | Blue | #7596ef | 2 | - | - | - | NKG7, FCRL6 |
| 12 | Medium Slate Blue | #7577ef | 2 | Eye lens protein, and Gap junction-mediated intercellular transport | - | - | TRNT1, CRYGC |
| 13 | Medium Purple | #9175ef | 2 | - | - | - | KCNA5, CSN3 |
| 14 | Medium Purple 2 | #b075ef | 2 | Mixed, incl. Uncharacterized protein CXorf65-like, and SHC SH2 domain-binding protein 1-like | - | - | CCDC54, TMCO2 |
| 15 | Orchid 2 | #cf75ef | 2 | - | - | - | CHRFAM7A, GLRA1 |
| 16 | Purple | #ee75ef | 2 | - | - | - | FUBP3, KHDC4 |
| 17 | Orchid | #ef75d2 | 2 | - | - | - | OGN, COL14A1 |
| 18 | Hot Pink | #ef75b3 | 2 | - | - | - | NABP1, RPUSD4 |
| 19 | Pink | #ef7594 | 2 | - | - | - | TAF1C, EDC4 |

[Cluster Detail](biogrid\string-analysis\string-biogrid-p53-ng-MCL-clusters.tsv)
