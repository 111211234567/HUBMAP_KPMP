import anndata as ad
import pandas as pd
import os

def concat_h5ad_files_with_column_mapping(file1_path, file2_path,rename_arr):
    # Load the two h5ad files
    data1 = ad.read_h5ad(file1_path)
    data2 = ad.read_h5ad(file2_path)

    # Extract the .obs DataFrames from both files
    obs1 = data1.obs
    obs2 = data2.obs
    obs1['database_source']=os.path.splitext(os.path.basename(file1_path))[0]
    obs2['database_source']=os.path.splitext(os.path.basename(file2_path))[0]
    # Rename column 'e' to 'c' in obs2 if they represent the same data
    obs2.rename(columns={'specimen': 'SpecimenID'}, inplace=True)
    obs2.rename(columns={'library_id': 'LibraryID'}, inplace=True)
    # for original_name,changed_name in rename_arr.items():
    #     obs2.rename(columns={original_name: changed_name}, inplace=True)

    # Concatenate the obs DataFrames, this will automatically align on columns
    concatenated_obs = pd.concat([obs1, obs2], axis=0, join='outer', ignore_index=True)
    for column in concatenated_obs.select_dtypes(include=['category']).columns:
        concatenated_obs[column] = concatenated_obs[column].cat.add_categories("unknown in current database")

    # Replace NaN values with "unknown in current database"
    concatenated_obs.fillna("unknown in current database", inplace=True)
    return concatenated_obs

# Example usage
file1 = "E:/Git/ProfessorHe's research/kpmp-sc-rnaseq.h5ad"
file2 = "E:/Git/ProfessorHe's research/kpmp-sn-rnaseq.h5ad"
rename_list={
    "libraryid":"LibraryID",
    "specimen":"SpecimenID"
}
# Call the function to concatenate the obs DataFrames
combined_obs = concat_h5ad_files_with_column_mapping(file1, file2,rename_list)

# Optionally, save the combined obs DataFrame to a CSV file
combined_obs.to_csv('Second_final_combined_obs.csv', index=False)

# Print the resulting DataFrame
print(combined_obs)
