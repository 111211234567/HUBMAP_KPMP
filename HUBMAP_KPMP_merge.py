import scanpy as sc
import pandas as pd
import anndata as ad
import os
import json

datasets = {
    "KPMP": "D:/Git/Professor-He-Research/Second_final_combined_obs.csv",
    "HUPMAP": "D:/Git/Professor-He-Research/sub/all_data/HUPMAP_COMBINED.csv"
}
def csv_to_obs_h5ad(csv_path):
    data = pd.read_csv(csv_path, index_col=0)  
    adata = ad.AnnData(X=None, obs=data)
    return adata
hupmap_rename_dict = {
    "hubmap_id": "LibraryID",
    "age": "Age",
    "race": "Race",
    "n_genes": "nFeature_RNA",
    "n_counts": "nCount_RNA",
    "predicted_label": "cell_type",
    "predicted_CLID": "cell_type_ontology_term_id"
}

def normalize_hubmap(path,output_path):
    hubmap_data = pd.read_csv(path)
    print("Original columns:", hubmap_data.columns)
    hubmap_data.rename(columns=hupmap_rename_dict, inplace=True)
    if 'azimuth_label' in hubmap_data.columns and 'cell_type' in hubmap_data.columns:
        hubmap_data['cell_type'] = hubmap_data['azimuth_label'] + " " + hubmap_data['cell_type']
        hubmap_data.drop(columns="azimuth_label", inplace=True)
    hubmap_data.to_csv(output_path, index=False)
    print("Normalized data saved to:", output_path)
normalize_hubmap("D:/Git/Professor-He-Research/sub/all_data/HUPMAP_COMBINED.csv","sub/sdfsdfsfdsfsdfds.csv")


def final_combine():
    kpmp=pd.read_csv("D:/Git/Professor-He-Research/Second_final_combined_obs.csv")
    hupmap=pd.read_csv("sub/sdfsdfsfdsfsdfds.csv")
    combined_df = pd.DataFrame()
    combined_df=pd.concat([kpmp,hupmap])
    combined_df = combined_df.fillna("does not exist in current case")
    return combined_df
final_combine().to_csv("sub/final.csv")