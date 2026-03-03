# Brain-wide Organization of Post-Synaptic Sites: Three Principles
After calculating predicted post-synaptic sites (PPSS), this repository provides the code to analyze ppss data. 

## Dependencies
 * Python 3.9.20
   
## Prepare the python enviroment
```bash
# Create a new environment
conda create -n ppss_analysis python=3.9.20
conda activate ppss_analysis

# Install dependencies
pip install -r req.txt

```

## Prepare the data
1) Extract all compressed files:
```bash
cd data
unzip h01_swc_rm_tiny_synapse_branch_level.csv.zip
unzip h01_1600_synapses_within_branch.csv.zip
unzip ppss_from_pacs_within_segments_branch_order_summary.csv.zip
unzip ibl_cluster_tables.csv.zip
unzip allen_ish_gene_region.csv.zip
cd ..
```

2) Download ppss_from_pacs.csv from Zenodo and move it into the data directory. It might take half hours to download it. 
```bash
wget https://zenodo.org/records/18831226/files/ppss_from_pacs.csv
cd ..
```

## PPSS analysis for figures
(1) Start Jupyter Notebook:
```bash
cd jupyter
jupyter notebook 
```
(2) Open the corresponding figure-x folder and run all cells.

## Reference
Yina Wei, Yuze Liu, Feng Xiong, Fuhui Long, Hanchuan Peng*, Brain-wide Organization of Post-Synaptic Sites: Three Principles, bioRxiv, 2026


