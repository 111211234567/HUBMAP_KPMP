For the KPMP data, two similar variables with different names were identified in the RN and SN datasets: 'specimen' and 'library_id'. These variables were standardized to 'SpecimenID' and 'LibraryID' and subsequently combined. 

a new varible named database_source was added to clearify the source database for each case in obs

The unique variables present in the KPMP SN dataset are:
- "experiment_id"
- "percent.medulla"
- "percent.er"
- "percent.cortex"
- "specimen"
- "subclass.l2"
- "region"
- "class"
- "library_id"

  Meanwhile, the unique variables in the KPMP SC dataset are:
- "sampletype"
- "Race"
- "SpecimenID"
- "clusterClass"
- "clusterNumber"
- "SampleID"
- "author_cell_type"
- "Run"
- "LibraryID"
- "dataSource"
- "diseasetype"

For the HuBMAP data, since all variables are the same, the concat function was directly used, and the 'azimuth_label' and 'cell type' variables were combined into a single variable to align with the format in the KPMP data.

Additionally, a 'database_source' variable was added to clarify the data source for each entry in hubmap.obs. For combining KPMP and HuBMAP, the following variables were merged to represent the same concepts across datasets:
"hubmap_id": "LibraryID",
        "age": "Age",
        "race": "Race",
        "n_genes": "nFeature_RNA",
        "n_counts": "nCount_RNA",
        "predicted_label": "cell_type",
        "predicted_CLID": "cell_type_ontology_term_id"

  Here is the final output file:https://drive.google.com/file/d/1WaZuOVWEWzwJeNYzisH5ncUJ-YHw3eR1/view?usp=drive_link
