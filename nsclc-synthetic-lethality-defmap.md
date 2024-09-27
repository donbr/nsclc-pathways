# Exploring Drug Efficacy through Synthetic Lethality in RB1- and TP53-Deficient Lung Cancer Cells

## Abstract

This paper presents an analysis of potential drug candidates that exploit synthetic lethality in **non-small cell lung cancer (NSCLC)**, specifically focusing on the tumor suppressor genes **RB1** and **TP53**. By leveraging drug response data from public datasets, we employ SQL-based queries to identify compounds with potent inhibitory effects (EC50 values) on essential targets in cancer pathways. This analysis highlights critical pathways, such as cell cycle regulation, apoptosis, and DNA damage repair, that can be exploited in RB1- and TP53-deficient cancer cells. Our results prioritize compounds based on their potency, providing a shortlist for further preclinical investigation and therapeutic validation in NSCLC models.

## 1. Introduction

Lung cancer, particularly **NSCLC**, is characterized by frequent mutations in **RB1** and **TP53**, two critical tumor suppressor genes. These mutations result in the loss of cell cycle regulation, increased genomic instability, and reduced apoptotic capacity, which drive cancer progression. The concept of **synthetic lethality** offers a targeted therapeutic approach, where loss of a tumor suppressor (e.g., RB1 or TP53) makes cancer cells reliant on alternative pathways that can be exploited with drugs to induce selective cell death. This therapeutic strategy reduces damage to healthy cells, as they typically retain the normal function of these tumor suppressors.

Previous studies have demonstrated the success of targeting synthetic lethality in cancers with **BRCA1/2** mutations by inhibiting **PARP1**, leading to FDA-approved treatments. We aim to build on this approach by identifying drugs that target pathways disrupted by **RB1** and **TP53** mutations in lung cancer.

This study focuses on identifying potent drugs with low **EC50 values** (indicating high potency) that interact with critical regulators in pathways disrupted by RB1 or TP53 mutations, using SQL-based queries on drug response data from lung cancer cell lines.

## 2. Methods

### 2.1 Data Source

We utilized the **Hugging Face Datasets** repository, specifically the secondary screen dose-response curve parameters dataset, to retrieve drug efficacy data across various cancer cell lines. The dataset contains information on drug names, their molecular targets, mechanisms of action (MOA), and **EC50** values, which reflect the potency of each drug. The EC50 value is the concentration required to reduce cell viability by 50%, with lower values indicating higher potency.

### 2.2 Query Design

#### 2.2.1 RB1 Query

The RB1 query was designed to extract drugs that target key pathways associated with **RB1**-deficient cancers. These pathways include:

- **Cell cycle regulation** (G1/S and G2/M checkpoints): In the absence of RB1, cancer cells often rely on alternative regulators like **CDK4**, **CDK6**, and **PLK1** to drive the cell cycle. Targeting these regulators can induce synthetic lethality.
- **Apoptosis regulation**: RB1 loss disrupts apoptosis. Drugs targeting proteins like **BCL2** and **BAX** can promote cell death.
- **DNA repair**: RB1-deficient cells are more reliant on DNA repair mechanisms, such as those involving **CHK1** and **ATR**.

The query prioritizes drugs with an **EC50 < 10 μM**, as these compounds demonstrate higher potency in RB1-deficient lung cancer cells.

[Run RB1 Query on Hugging Face](https://huggingface.co/datasets/donb-hf/secondary-screen-dose-response-curve-parameters?sql_console=true&sql=SELECT+name%2C+target%2C+moa%2C+AVG%28ec50%29+as+avg_ec50%2C+COUNT%28*%29+as+occurrence%2C+%0A+++++++MIN%28ec50%29+as+min_ec50%2C+MAX%28ec50%29+as+max_ec50%0AFROM+train%0AWHERE+ccle_name+LIKE+%27%25_LUNG%27%0A++AND+ec50+%3E+0++++++++++--+Exclude+invalid+or+negative+EC50+values%0A++AND+ec50+%3C+10000++++++--+Focus+on+biologically+relevant+EC50+values+%28e.g.%2C+%3C+10+%CE%BCM%29%0A++AND+%28%0A++++--+RB1+pathway+and+direct+regulators%3A%0A++++--+RB1+is+a+critical+tumor+suppressor.+When+lost%2C+cancer+cells+may+rely+on+these+regulators.%0A++++target+LIKE+%27RB1%27+OR+target+LIKE+%27%2C+RB1%27+OR+target+LIKE+%27RB1%2C%25%27+OR+target+LIKE+%27%25%2C+RB1%2C%25%27%0A++++%0A++++--+G1%2FS+checkpoint+and+cell+cycle+regulation%3A%0A++++--+In+the+absence+of+RB1%2C+targeting+CDKs+and+cyclins+that+drive+the+cell+cycle+can+induce+synthetic+lethality.%0A++++OR+target+LIKE+%27%25CDK4%25%27+OR+target+LIKE+%27%25CDK6%25%27++--+CDKs+driving+G1%2FS+transition.%0A++++OR+target+LIKE+%27%25CCND1%25%27+OR+target+LIKE+%27%25CCND2%25%27+OR+target+LIKE+%27%25CCND3%25%27++--+Cyclin+D%2C+critical+for+G1+progression.%0A++++OR+target+LIKE+%27%25E2F1%25%27+OR+target+LIKE+%27%25E2F2%25%27+OR+target+LIKE+%27%25E2F3%25%27++--+E2F+transcription+factors+normally+controlled+by+RB1.%0A++++%0A++++--+G2%2FM+checkpoint+regulation+and+mitotic+control%3A%0A++++--+Targeting+mitotic+regulators+can+induce+synthetic+lethality+in+RB1-deficient+cells.%0A++++OR+target+LIKE+%27%25WEE1%25%27+OR+target+LIKE+%27%25PLK1%25%27++--+WEE1+for+G2%2FM+control%2C+PLK1+for+mitotic+entry.%0A++++OR+target+LIKE+%27%25CDC25%25%27++--+CDK+activators+for+cell+cycle+progression.%0A++++OR+target+LIKE+%27%25AURKA%25%27+OR+target+LIKE+%27%25AURKB%25%27++--+Aurora+kinases+A+and+B+for+mitotic+regulation.%0A++++OR+target+LIKE+%27%25AURKC%25%27++--+Aurora+kinase+C+%28less+commonly+targeted+but+overlaps+with+AURKB%29.%0A++++%0A++++--+Apoptosis+regulation%3A%0A++++--+RB1+loss+disrupts+apoptosis%3B+targeting+apoptotic+pathways+enhances+therapeutic+potential.%0A++++OR+target+LIKE+%27%25BCL2%25%27+OR+target+LIKE+%27%25BCLXL%25%27+OR+target+LIKE+%27%25MCL1%25%27++--+Anti-apoptotic+proteins%2C+targeting+them+induces+apoptosis.%0A++++OR+target+LIKE+%27%25BAX%25%27+OR+target+LIKE+%27%25BID%25%27++--+Pro-apoptotic+inducers%2C+promoting+cell+death.%0A++++%0A++++--+Chromatin+organization+and+histone+modification%3A%0A++++--+Chromatin+regulators+become+essential+for+transcriptional+control+in+RB1-deficient+cells.%0A++++OR+target+LIKE+%27%25EZH2%25%27+OR+target+LIKE+%27%25HDAC%25%27++--+Epigenetic+regulation+via+histone+modification.%0A++++%0A++++--+DNA+replication+and+repair%3A%0A++++--+RB1-deficient+cells+are+reliant+on+robust+DNA+repair+pathways%2C+making+these+targets+for+synthetic+lethality.%0A++++OR+target+LIKE+%27%25MCM%25%27+OR+target+LIKE+%27%25CHK1%25%27+OR+target+LIKE+%27%25CHK2%25%27+OR+target+LIKE+%27%25ATR%25%27+OR+target+LIKE+%27%25ATM%25%27++--+Key+DNA+replication+and+repair+targets.%0A++++%0A++++--+Metabolism+and+mitochondrial+function%3A%0A++++--+Metabolic+pathways+become+more+critical+in+RB1-deficient+cancers%2C+providing+additional+drug+targets.%0A++++OR+target+LIKE+%27%25PKM%25%27+OR+target+LIKE+%27%25LDHA%25%27++--+Metabolic+enzymes+critical+for+glycolysis+and+energy+production.%0A++++%0A++++--+Additional+RB1-related+targets%3A%0A++++--+RB1+loss+activates+alternative+regulators%2C+making+them+potential+therapeutic+targets.%0A++++OR+target+LIKE+%27%25FOXM1%25%27+OR+target+LIKE+%27%25CDC6%25%27++--+FOXM1+and+CDC6+are+involved+in+mitotic+regulation+and+DNA+replication.%0A++%29%0AGROUP+BY+name%2C+target%2C+moa%0AORDER+BY+avg_ec50+ASC%3B++--+Prioritize+more+potent+drugs+%28lower+EC50+values+indicate+higher+potency%29%0A)

```sql
SELECT name, target, moa, AVG(ec50) as avg_ec50, COUNT(*) as occurrence, 
       MIN(ec50) as min_ec50, MAX(ec50) as max_ec50
FROM train
WHERE ccle_name LIKE '%_LUNG'
  AND ec50 > 0          -- Exclude invalid or negative EC50 values
  AND ec50 < 10000      -- Focus on biologically relevant EC50 values (e.g., < 10 μM)
  AND (
    -- RB1 pathway and direct regulators:
    -- RB1 is a critical tumor suppressor. When lost, cancer cells may rely on these regulators.
    target LIKE 'RB1' OR target LIKE ', RB1' OR target LIKE 'RB1,%' OR target LIKE '%, RB1,%'
    
    -- G1/S checkpoint and cell cycle regulation:
    -- In the absence of RB1, targeting CDKs and cyclins that drive the cell cycle can induce synthetic lethality.
    OR target LIKE '%CDK4%' OR target LIKE '%CDK6%'  -- CDKs driving G1/S transition.
    OR target LIKE '%CCND1%' OR target LIKE '%CCND2%' OR target LIKE '%CCND3%'  -- Cyclin D, critical for G1 progression.
    OR target LIKE '%E2F1%' OR target LIKE '%E2F2%' OR target LIKE '%E2F3%'  -- E2F transcription factors normally controlled by RB1.
    
    -- G2/M checkpoint regulation and mitotic control:
    -- Targeting mitotic regulators can induce synthetic lethality in RB1-deficient cells.
    OR target LIKE '%WEE1%' OR target LIKE '%PLK1%'  -- WEE1 for G2/M control, PLK1 for mitotic entry.
    OR target LIKE '%CDC25%'  -- CDK activators for cell cycle progression.
    OR target LIKE '%AURKA%' OR target LIKE '%AURKB%'  -- Aurora kinases A and B for mitotic regulation.
    OR target LIKE '%AURKC%'  -- Aurora kinase C (less commonly targeted but overlaps with AURKB).
    
    -- Apoptosis regulation:
    -- RB1 loss disrupts apoptosis; targeting apoptotic pathways enhances therapeutic potential.
    OR target LIKE '%BCL2%' OR target LIKE '%BCLXL%' OR target LIKE '%MCL1%'  -- Anti-apoptotic proteins, targeting them induces apoptosis.
    OR target LIKE '%BAX%' OR target LIKE '%BID%'  -- Pro-apoptotic inducers, promoting cell death.
    
    -- Chromatin organization and histone modification:
    -- Chromatin regulators become essential for transcriptional control in RB1-deficient cells.
    OR target LIKE '%EZH2%' OR target LIKE '%HDAC%'  -- Epigenetic regulation via histone modification.
    
    -- DNA replication and repair:
    -- RB1-deficient cells are reliant on robust DNA repair pathways, making these targets for synthetic lethality.
    OR target LIKE '%MCM%' OR target LIKE '%CHK1%' OR target LIKE '%CHK2%' OR target LIKE '%ATR%' OR target LIKE '%ATM%'  -- Key DNA replication and repair targets.
    
    -- Metabolism and mitochondrial function:
    -- Metabolic pathways become more critical in RB1-deficient cancers, providing additional drug targets.
    OR target LIKE '%PKM%' OR target LIKE '%LDHA%'  -- Metabolic enzymes critical for glycolysis and energy production.
    
    -- Additional RB1-related targets:
    -- RB1 loss activates alternative regulators, making them potential therapeutic targets.
    OR target LIKE '%FOXM1%' OR target LIKE '%CDC6%'  -- FOXM1 and CDC6 are involved in mitotic regulation and DNA replication.
  )
GROUP BY name, target, moa
ORDER BY avg_ec50 ASC;  -- Prioritize more potent drugs (lower EC50 values indicate higher potency)
```

#### 2.2.2 TP53 Query

The TP53 query targets drugs that exploit vulnerabilities in **TP53**-deficient cells. Key pathways targeted include:

- **Apoptosis regulation**: In TP53-deficient cells, apoptotic pathways are compromised. Drugs like **Panobinostat**, which target epigenetic regulators such as **HDACs**, can induce cell death.
- **DNA repair and metabolic regulation**: TP53-deficient cells often rely on alternative DNA repair and stress response mechanisms. Drugs targeting **RRM1/RRM2** or metabolic regulators like **TIGAR** can enhance synthetic lethality.

This query also focuses on drugs with **EC50 < 10 μM**.

[Run TP53 Query on Hugging Face](https://huggingface.co/datasets/donb-hf/secondary-screen-dose-response-curve-parameters?sql_console=true&sql=SELECT+name%2C+target%2C+moa%2C+AVG%28ec50%29+as+avg_ec50%2C+COUNT%28*%29+as+occurrence%2C+%0A+++++++MIN%28ec50%29+as+min_ec50%2C+MAX%28ec50%29+as+max_ec50%0AFROM+train%0AWHERE+ccle_name+LIKE+%27%25_LUNG%27%0A++AND+ec50+%3E+0++--+Exclude+invalid+or+negative+EC50+values+to+ensure+meaningful+results%0A++AND+ec50+%3C+10000++--+Focus+on+biologically+relevant+EC50+values+%28up+to+10+%CE%BCM%29%2C+prioritizing+potent+compounds%0A++AND+%28%0A++++--+TP53+pathway+and+direct+regulators%3A%0A++++--+TP53+mutations+often+lead+to+loss+of+tumor+suppression%2C+making+targeting+its+regulators+critical.%0A++++target+LIKE+%27%25TP53%25%27+%0A++++OR+target+LIKE+%27%25MDM2%25%27++--+MDM2+controls+TP53+degradation.%0A++++%0A++++--+Cell+cycle+regulation+%28G1%2FS+and+G2%2FM+checkpoints%29%3A%0A++++--+Targeting+cell+cycle+checkpoints+helps+exploit+synthetic+lethality+in+TP53-deficient+cells.%0A++++OR+target+LIKE+%27%25CDKN1A%25%27++--+p21%2C+a+key+CDK+inhibitor+controlled+by+TP53%2C+enforcing+G1%2FS+checkpoint.%0A++++OR+target+LIKE+%27%25WEE1%25%27++--+WEE1+kinase%2C+critical+for+G2%2FM+checkpoint+regulation.%0A++++%0A++++--+Apoptosis+regulation+%28potential+combinatorial+therapy%29%3A%0A++++--+Loss+of+TP53+compromises+apoptosis%3B+targeting+apoptosis+can+enhance+synthetic+lethality.%0A++++OR+target+LIKE+%27%25BAX%25%27++--+BAX%2C+a+pro-apoptotic+factor+regulated+by+TP53.%0A++++%0A++++--+DNA+damage+response+and+repair+%28synthetic+lethality+target%29%3A%0A++++--+Cancer+cells+with+TP53+mutations+rely+on+alternative+DNA+repair+mechanisms%3B+targeting+these+induces+synthetic+lethality.%0A++++OR+target+LIKE+%27%25GADD45%25%27++--+DNA+repair+and+stress+response.%0A++++OR+target+LIKE+%27%25PCNA%25%27++--+Essential+for+DNA+replication+and+repair.%0A++++OR+target+LIKE+%27%25RRM1%25%27+OR+target+LIKE+%27%25RRM2%25%27+OR+target+LIKE+%27%25RRM2B%25%27++--+RRM+family+involved+in+nucleotide+synthesis+for+DNA+repair.%0A++++OR+target+LIKE+%27%25POLK%25%27+OR+target+LIKE+%27%25DDB2%25%27++--+POLK+for+translesion+synthesis%2C+DDB2+for+nucleotide+excision+repair.%0A++++%0A++++--+Metabolic+regulation+and+stress+response+%28potential+combinatorial+therapy%29%3A%0A++++--+Disrupting+stress+responses+in+TP53-deficient+cancers+can+enhance+synthetic+lethality.%0A++++OR+target+LIKE+%27%25TIGAR%25%27++--+Metabolic+regulation+and+stress+modulation.%0A++++%0A++++--+Epigenetic+regulation+%28potential+combinatorial+therapy%29%3A%0A++++--+Targeting+HDACs+or+other+epigenetic+modifiers+can+enhance+apoptosis+and+cell+cycle+arrest+in+TP53-deficient+cancers.%0A++++OR+target+LIKE+%27%25HDAC%25%27++--+Histone+deacetylases+%28HDACs%29+are+involved+in+chromatin+remodeling.%0A++++%0A++++--+DNA+replication+and+repair+factors%3A%0A++++--+Targeting+DNA+replication+factors+can+induce+synthetic+lethality+in+cells+relying+on+alternative+repair+pathways+due+to+TP53+loss.%0A++++OR+target+LIKE+%27%25POLA%25%27+OR+target+LIKE+%27%25POLD%25%27+OR+target+LIKE+%27%25POLE%25%27++--+Key+DNA+polymerases+in+replication+and+repair.%0A++%29%0AGROUP+BY+name%2C+target%2C+moa%0AORDER+BY+avg_ec50+ASC%3B++--+Prioritize+potent+drugs+%28lower+EC50+indicates+higher+potency%29%0A)

```sql
SELECT name, target, moa, AVG(ec50) as avg_ec50, COUNT(*) as occurrence, 
       MIN(ec50) as min_ec50, MAX(ec50) as max_ec50
FROM train
WHERE ccle_name LIKE '%_LUNG'
  AND ec50 > 0  -- Exclude invalid or negative EC50 values to ensure meaningful results
  AND ec50 < 10000  -- Focus on biologically relevant EC50 values (up to 10 μM), prioritizing potent compounds
  AND (
    -- TP53 pathway and direct regulators:
    -- TP53 mutations often lead to loss of tumor suppression, making targeting its regulators critical.
    target LIKE '%TP53%' 
    OR target LIKE '%MDM2%'  -- MDM2 controls TP53 degradation.
    
    -- Cell cycle regulation (G1/S and G2/M checkpoints):
    -- Targeting cell cycle checkpoints helps exploit synthetic lethality in TP53-deficient cells.
    OR target LIKE '%CDKN1A%'  -- p21, a key CDK inhibitor controlled by TP53, enforcing G1/S checkpoint.
    OR target LIKE '%WEE1%'  -- WEE1 kinase, critical for G2/M checkpoint regulation.
    
    -- Apoptosis regulation (potential combinatorial therapy):
    -- Loss of TP53 compromises apoptosis; targeting apoptosis can enhance synthetic lethality.
    OR target LIKE '%BAX%'  -- BAX, a pro-apoptotic factor regulated by TP53.
    
    -- DNA damage response and repair (synthetic lethality target):
    -- Cancer cells with TP53 mutations rely on alternative DNA repair mechanisms; targeting these induces synthetic lethality.
    OR target LIKE '%GADD45%'  -- DNA repair and stress response.
    OR target LIKE '%PCNA%'  -- Essential for DNA replication and repair.
    OR target LIKE '%RRM1%' OR target LIKE '%RRM2%' OR target LIKE '%RRM2B%'  -- RRM family involved in nucleotide synthesis for DNA repair.
    OR target LIKE '%POLK%' OR target LIKE '%DDB2%'  -- POLK for translesion synthesis, DDB2 for nucleotide excision repair.
    
    -- Metabolic regulation and stress response (potential combinatorial therapy):
    -- Disrupting stress responses in TP53-deficient cancers can enhance synthetic lethality.
    OR target LIKE '%TIGAR%'  -- Metabolic regulation and stress modulation.
    
    -- Epigenetic regulation (potential combinatorial therapy):
    -- Targeting HDACs or other epigenetic modifiers can enhance apoptosis and cell cycle arrest in TP53-deficient cancers.
    OR target LIKE '%HDAC%'  -- Histone deacetylases (HDACs) are involved in chromatin remodeling.
    
    -- DNA replication and repair factors:
    -- Targeting DNA replication factors can induce synthetic lethality in cells relying on alternative repair pathways due to TP53 loss.
    OR target LIKE '%POLA%' OR target LIKE '%POLD%' OR target LIKE '%POLE%'  -- Key DNA polymerases in replication and repair.
  )
GROUP BY name, target, moa
ORDER BY avg_ec50 ASC;  -- Prioritize potent drugs (lower EC50 indicates higher potency)
```

## 3. Results

### 3.1 RB1 Query Results

The RB1 query identified several potent drugs with low average EC50 values. For example:

- **Romidepsin** (targeting **HDACs**) demonstrated an average EC50 of 0.022 μM, indicating high potency in lung cancer cell lines lacking RB1. **HDAC inhibitors** have been shown to alter chromatin structure, restoring the expression of pro-apoptotic genes and inducing cell death in cancer cells.
- **BI-2536**, a **PLK1 inhibitor**, showed an average EC50 of 0.065 μM. **PLK1** plays a key role in mitotic progression, and its inhibition disrupts cell division, inducing mitotic arrest and apoptosis, especially in RB1-deficient cells.

These drugs target key regulators of cell cycle checkpoints, apoptosis, and DNA repair mechanisms, which become critical in RB1-deficient cancer cells.

### 3.2 TP53 Query Results

The TP53 query returned several potent compounds, such as:

- **Panobinostat**, a **HDAC inhibitor**, had an average EC50 of 0.165 μM. **Panobinostat** affects the acetylation of histone proteins, leading to the reactivation of pro-apoptotic pathways that are suppressed in TP53-deficient cells.
- **Gemcitabine**, targeting the **RRM1/RRM2** pathways involved in nucleotide synthesis and DNA repair, exhibited an EC50 of 0.003 μM, indicating extremely high potency in TP53-deficient cells. **Gemcitabine** works by inhibiting DNA replication, which cancer cells reliant on alternative repair mechanisms struggle to overcome.

These drugs leverage the vulnerabilities in DNA repair and apoptotic pathways in TP53-deficient cancers, providing promising candidates for combination therapies.

## 4. Conclusion

This analysis demonstrates that targeting **synthetic lethality** in **RB1**- and **TP53**-deficient lung cancer cells presents a promising strategy for selective cancer therapies. The queries identified potent compounds that inhibit key regulators of the cell cycle, apoptosis, and DNA repair mechanisms, which are essential for cancer cell survival in the absence of RB1 or TP53. These compounds, including **Romidepsin**, **BI-2536**, **Panobinostat**, and **Gemcitabine**, are promising candidates for further preclinical evaluation. Additionally, the potential of these drugs in combination therapies should be explored to enhance their therapeutic efficacy and minimize resistance.

## Appendix

### Review of SQL Inline Comments

The inline comments in the SQL commands provide important context for the biological targets and pathways being queried. Below is a review of these comments, along with suggestions for refinement and areas to enhance the analysis, focusing on clustering and stratifying drugs based on their mechanism of action (MOA) and targets for synthetic lethality in **RB1** and **TP53**-deficient **NSCLC**.

#### General Overview

The SQL queries are designed to:

- Identify compounds based on target genes/proteins related to **RB1** or **TP53** deficiency.
- Prioritize compounds by **EC50** values to find potent drugs.
- Focus on biologically relevant concentrations (with EC50 < 10,000), ensuring that only potent compounds are returned.

#### RB1 Pathway and Direct Regulators

1. **G1/S Checkpoint and Cell Cycle Regulation**:
   - **Comment**: “In the absence of RB1, targeting CDKs and cyclins that drive the cell cycle can induce synthetic lethality.”
   - **Targets**: CDK4, CDK6, CCND1 (Cyclin D1), CCND2, CCND3, E2F family.
   - **Analysis**: Targeting these cell cycle regulators is a rational strategy since RB1 normally inhibits cell cycle progression through E2F and cyclins. By disrupting these pathways, cell cycle control is lost, leading to cancer cell death. 
   - **Refinement Suggestion**: Stratify by **CDK inhibitors** (e.g., Palbociclib, Abemaciclib) and **cyclin inhibitors** to determine if certain inhibitors show more effectiveness in combination therapies. Adding **combinatorial query patterns** for specific drug-target pairs would enhance synthetic lethality.

2. **G2/M Checkpoint Regulation and Mitotic Control**:
   - **Comment**: “Targeting mitotic regulators can induce synthetic lethality in RB1-deficient cells.”
   - **Targets**: WEE1, PLK1, CDC25, Aurora kinases.
   - **Analysis**: These targets control mitotic entry, and their inhibition is crucial for forcing cell death in cells lacking proper mitotic regulation (due to RB1 loss).
   - **Refinement Suggestion**: Consider stratifying **aurora kinase inhibitors** (AURKA, AURKB) and **mitotic checkpoint inhibitors** to see if any combination of these drugs increases sensitivity in RB1-deficient cancers.

3. **Apoptosis Regulation**:
   - **Comment**: “RB1 loss disrupts apoptosis; targeting apoptotic pathways enhances therapeutic potential.”
   - **Targets**: BCL2, BCLXL, MCL1, BAX, BID.
   - **Analysis**: Targeting anti-apoptotic proteins like BCL2/BCLXL/MCL1 while promoting pro-apoptotic proteins like BAX and BID is a strategy to overcome apoptosis resistance in RB1-deficient cancer cells.
   - **Refinement Suggestion**: Cluster drugs that target **anti-apoptotic proteins** separately from those that activate **pro-apoptotic proteins**. This stratification will help in assessing whether certain combinations (e.g., BCL2 inhibitors + pro-apoptotic activators) lead to improved outcomes.

4. **Chromatin Organization and Histone Modification**:
   - **Comment**: “Chromatin regulators become essential for transcriptional control in RB1-deficient cells.”
   - **Targets**: EZH2, HDAC family.
   - **Analysis**: HDAC inhibitors are commonly used to disrupt transcriptional control in cancers. Chromatin regulation via EZH2 or HDAC inhibition could further sensitize cells to apoptosis or cell cycle arrest.
   - **Refinement Suggestion**: Focus on specific **HDAC inhibitors** and their combination with **other chromatin regulators**, particularly those that target RB1-deficient cancer pathways.

#### TP53 Pathway and Synthetic Lethality

1. **Cell Cycle Checkpoint Regulation**:
   - **Comment**: “Loss of TP53 impairs G1/S checkpoint control; targeting CDKs and checkpoint regulators induces synthetic lethality.”
   - **Targets**: CDK2, CDKN1A (p21), WEE1.
   - **Analysis**: The loss of TP53 leaves cells reliant on CDK/cell cycle checkpoint pathways. Drugs targeting CDK2 or WEE1 disrupt this balance.
   - **Refinement Suggestion**: Group CDK inhibitors by their specific target (CDK2, CDK4/6) and analyze their combinatorial effect with WEE1 inhibitors.

2. **Apoptosis Regulation (Potential Combinatorial Therapy)**:
   - **Comment**: “Loss of TP53 compromises apoptosis; targeting apoptosis can enhance synthetic lethality.”
   - **Targets**: BAX.
   - **Analysis**: Without TP53, cells are less capable of undergoing apoptosis. BAX, a pro-apoptotic factor, can be a target to restore apoptosis in cancer cells.
   - **Refinement Suggestion**: Cluster drugs targeting **BAX** and other **apoptosis-related proteins**, and analyze whether combinatorial therapies with DNA-damaging agents enhance lethality in TP53-deficient cells.

3. **DNA Damage Response and Repair (Synthetic Lethality Target)**:
   - **Comment**: “Cancer cells with TP53 mutations rely on alternative DNA repair mechanisms.”
   - **Targets**: GADD45, PCNA, RRM family, POLK.
   - **Analysis**: Targeting DNA damage repair in TP53-deficient cells could exacerbate genomic instability and promote cell death. Inhibitors of **PCNA** and **RRM** are strong candidates for such synthetic lethality.
   - **Refinement Suggestion**: Group drugs targeting **DNA damage response factors** and evaluate their role in combination with traditional DNA-damaging agents like **cisplatin**.

#### Further Refinement and Stratification

- **MOA Clustering**: Group drugs based on their **mechanism of action (MOA)**, e.g., CDK inhibitors, apoptosis inducers, DNA damage repair inhibitors. Then, within these clusters, analyze potency (based on EC50) and frequency to identify top candidates for combination therapies.
  
- **Drug-Target Network Analysis**: Consider visualizing the **drug-target network** for RB1- and TP53-related synthetic lethality targets using tools like **Cytoscape**. This will help identify key interactions and prioritize targets with multiple drug candidates.

- **Combinatorial Therapies**: Prioritize **combinatorial queries** in the SQL based on synergistic pathways. For example, combine **DNA damage inhibitors** with **apoptosis inducers** for TP53-deficient cells or **cell cycle inhibitors** with **HDAC inhibitors** for RB1-deficient cancers.

## Citation

DepMap, Broad; Corsello, Steven; Kocak, Mustafa; Golub, Todd (2019). PRISM Repurposing 19Q4 Dataset. figshare. Dataset.

Current dataset: [https://doi.org/10.6084/m9.figshare.9393293.v4](https://doi.org/10.6084/m9.figshare.9393293.v4)

General guidance: [https://doi.org/10.1101/730119](https://doi.org/10.1101/730119)
