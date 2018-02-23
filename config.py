import os


class Config():
    # Name the dataset
    set_name = 'Cardiology'
    # Enter your own email address
    myemail = 'adam.day@sagepub.co.uk'
    # Journal of interest (must match the WoS name for the journal)
    joi = 'BRAIN' 
    # which years' data will we use?  Edit to shrink your data to a smaller size for testing
    years = ['2012','2013', '2014','2015','2016','2017'] # 2012-2017 available

    # SETTINGS
    # sampling - take every nth article from the dataset.  If you don't want to sample, set equal to 1
    every_nth = 1
    # kmeans
    n_clusters = 32
    
    # tsne settings.  Set all to None for defaults
    n_iter = 1500
    n_iter_without_progress = 50
    perplexity = 400 # recommendation is 5-7% of dataset size.
    learning_rate = 150

    
    # GLOBAL VARIABLES - probably won't need to edit these
    wos_word_data_p = 'data/wos_word_data.csv'    
    # paths to metadata
    dim_data_p = 'data/Dimensions_data.csv'
    dim_json_p = 'data/dimensions_metrics.json'
    dim_failures_p = 'data/dimensions_failures.json'
    cr_data_p = 'data/crossref_cit_data.json'
    cr_failures_p = 'data/crossref_cit_failures.json'
    
    
    dois_pkl = os.path.abspath(r'data/dois.p')
    all_dois_pkl = os.path.abspath(r'data/all_dois.pkl')
    filepaths_pkl = os.path.abspath(r'data/filepaths.pkl')
    jnl_data_filepaths_pkl = os.path.abspath(r'data/jnl_data_filepaths.pkl')
    labels_path = os.path.abspath(r'data/labels.pkl')
    working_data = os.path.abspath(r'data/working_data.csv')
    # search engine
    vocab_p = os.path.abspath(r'data/vocabulary.p')
    idf_p = os.path.abspath(r'data/idf.p')

    # input data

    # word data
    word_datapath = os.path.abspath(r'data/word_data.p')

    # tfidf data
    tfidf_datapath = os.path.abspath(r'data/tfidf_data.pkl')
    cosine_sims_datapath = os.path.abspath(r'data/cosine_sims.pkl')
    vectorizer_datapath = os.path.abspath(r'data/vectorizer.pkl')

    # kmeans data
    kmeans_out = os.path.abspath(r'data/data_2.csv')
    kmeans_out_xl = os.path.abspath(r'data/kmeans_data.xlsx')
    kmeans_out_csv = os.path.abspath(r'data/cluster_data.csv')

    # tsne data
    tsne_data = os.path.abspath(r'data/data_3.csv')

    # Visualisation
    # visualisation data (?)



    # visualisations
    tfidf_filename = "outputs\\{3}_bokeh_tfidf_k{0}_L{1}_p{2}_0.html".format(n_clusters,learning_rate,perplexity,set_name)
    title = "TF-IDF visualisation of {}".format(set_name)
    bar_filename = "outputs\\{3}_bokeh_bar_k{0}_L{1}_p{2}_0.html".format(n_clusters,learning_rate,perplexity,set_name)

