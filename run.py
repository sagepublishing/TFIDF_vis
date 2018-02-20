# run.py

import os

files = [
    'Step_0_create_word_data',
    'Step_1_data_processing_TF-IDF',
    'Step_2_reduce_dims_TSNE',
    'Step_3_Add_citation_data',
    'Step_4_clustering_KMeans',
    'Step_5_Visualisation_Bokeh'
]

to_run = [0,1,2,3,4,5]

# to_run = [3,4] # select which you want to run

# convert to python
for file in [files[i] for i in to_run]:
    print('--- Converting .ipynb to .py ---')
    os.system('jupyter nbconvert --to python {}.ipynb'.format(file))
    print('--- Executing .py file ---')
    os.system('python {}.py'.format(file))
    print('--- Deleting .py file ---')
    os.system('del {}.py'.format(file))

## Notes:
"""
# convert ALL
jupyter nbconvert --to python Step_1_data_processing_TF-IDF.ipynb Step_2_reduce_dims_TSNE.ipynb Step_3_Add_citation_data.ipynb Step_4_clustering_KMeans.ipynb Step_5_Visualisation_Bokeh.ipynb

# run all
python Step_0_create_dataframe-multiple_sources.py && python Step_1_data_processing_TF-IDF_multiple_sources.py && python Step_2_clustering_KMeans-multiple_sources.py && python Step_3_reduce_dims_TSNE-multiple_sources.py && python Step_4_Visualisation_Bokeh-multiple_sources.py


# run step 0
python Step_0_create_dataframe-multiple_sources.py

# run step 1
python Step_1_data_processing_TF-IDF_multiple_sources.py

# run step 2
python Step_2_clustering_KMeans-multiple_sources.py

# run step 3
python Step_3_reduce_dims_TSNE-multiple_sources.py

# run step 4
python Step_4_Visualisation_Bokeh-multiple_sources.py"""
