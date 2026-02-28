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
   unzip den_contact_test.csv.zip
   unzip h01_1600_synapses_within_branch.csv.zip
   unzip ppss_from_pacs_within_segments_branch_order_summary.csv.zip
   cd hippo
   unzip root.vtk.zip
   cd ../..
   ```
2) Download ppss_from_pacs.csv from Zenodo and move it into the data directory.

## PPSS Analysis for Figures
(1) Start Jupyter Notebook:
```bash
jupyter notebook
```

(2) Open the corresponding figure-x folder and run all cells.

## Reference
Yina Wei, Yuze Liu, Feng Xiong, Fuhui Long, Hanchuan Peng*, Brain-wide Organization of Post-Synaptic Sites: Three Principles, bioRxiv, 2026


