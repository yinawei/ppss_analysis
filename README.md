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
```

2) Download ppss_from_pacs.csv from Zenodo and move it into the data directory.
```bash
wget https://zenodo.org/records/18831226/files/ppss_from_pacs.csv
cd ..
```

## PPSS analysis for figures
(1) To get started, launch either Jupyter Notebook or your preferred Python IDE.
```bash
cd jupyter
jupyter notebook 
```
(2) Open the corresponding figure-x folder and run all cells.

## Figures plotted using paraview
(1). Installation
Visit https://www.paraview.org/download/ to download the paraview installer for your operating system and follow the installation instructions.

(2). Figures requiring paraview rendering
The following figures require rendering using paraview:
1) Main Figure 1 A
2) Main Figure 5 C, D
3) Supplementary Figure 6 B

(3). Basic paraview visualization workflow
  1) Launch paraview (For Linux system, open the folder bin, in the terminal: ./paraview)
  2) Right-click on builtin in the Pipeline Browser, then import /data/hippo/root.vtk or /data/hippo/CA1.vtk
  3) Click the eye icon next to the imported VTK object in the Pipeline Browser to display it. 
Then, in the Properties panel below, go to the Coloring section, change the coloring mode to Solid Color, 
and adjust the Opacity to your preference. In the Background section of the Properties panel, 
uncheck Use Color Palette For Background and select white as the background color.
  4) Click the View button in the toolbar and check Python Shell to display the script dialog
  5) Click Run Script in the bottom-right corner and select the corresponding Python script file in the file explorer
Note: You must modify all relative paths to data files in the code to absolute paths
Wait for the rendering to complete (~5 minutes).

(4). Figure-specific Instructions
  1) Main Figure 1 A
Prerequisite: Run ./jupyter/figure1/bouton_dendritic_contact_branching_level_region_ave.ipynb
Script: /jupyter/figure1/load_ppss.py

  2) Main Figure 5 C
Prerequisite: Run /jupyter/figure5/morph_feature-hippo-usingLM.ipynb and utils.ipynb
Script: /jupyter/figure5/load_soma.py

  3) Main Figure 5 D
Prerequisite: Run /jupyter/figure5/morph_feature-hippo-usingLM.ipynb and utils.ipynb
Script: /jupyter/figure5/draw_swc.py

  4) Supplementary Figure 6 B
Prerequisite: Run /jupyter/figure5/morph_feature-hippo-usingLM.ipynb and utils.ipynb
Script: /jupyter/figure5/load_soma.py
Modification: Replace the data file with /output/CA1_hippo_data_random.csv

## Reference
Yina Wei, Yuze Liu, Feng Xiong, Fuhui Long, Hanchuan Peng*, Brain-wide Organization of Post-Synaptic Sites: Three Principles, bioRxiv, 2026


