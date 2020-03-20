**EDIT:** This is quite an old repo. 
- Recommend switching TFIDF for Doc2Vec/SciSpaCy if you only have titles and abstracts - or a BERT variant if you have a GPU handy. 
- Also switch t-SNE for uMap

# TFIDF visualisations

This is a project folder for creating interactive textual visualisations of Web of Science data.

There are a number of potential updates and forks to this code which can develop it and improve its utility.

These instructions assume that you have the latest Python 3 version of Anaconda from Continuum.io.

### To test the code:
1. Install requirements.  Open a terminal (Mac/Linux) or command window (PC)
```
> pip install -r requirements.txt
```
1b. If you've never used nltk before, open the GUI
```
> ipython
> import nltk
> nltk.download()   # opens the GUI
```
Then download snowball stemmer and English language stopwords
```
>>> quit()
```
2. Create a folder called 'wos' and fill it with Web of Science data in tsv format. WoS data should, at a minimum include the following columns:
```python
['DI','PY','TI','AB','DE','ID','AU','AF','SO','SC','SN','EI','TC','Z9']
```

3. run the code
```
> python run.py
```
3b.  You can alternatively open a jupyter notebook
```
> jupyter notebook # or jupyter lab
```
... and then step through the code, one piece at a time in the .ipynb files

### Notes

Following the above instructions should produce a visualisation.  However, it's unlikely that your first visualisation will give you what you want to see.  This is mostly down to step 2: ‘t-SNE’ which has a couple of inherent problems.
i) T-SNE is quite slow.  You may find that, for large datasets (say 10,000+ files) t-SNE can take several hours, or even need to run overnight.  
ii) T-SNE has a number of parameters, which have to be ‘tuned’ (by editing config.py) according to the particular dataset.  I’m not aware of an automatable way of tuning these parameters, so you may have to run the analysis repeatedly in order to get the parameters right.  My best advice for tuning t-SNE is:
 - Start with ‘perplexity’ set to 5-7% of the number of papers in your dataset.
 - Pick some numbers for the other settings based on: https://distill.pub/2016/misread-tsne/
 - Run it once and take a look at what you’ve got.  
  - If you see clusters forming up in lines, or squiggles, then it’s likely that ‘number of iterations’ is too low.
  - Ideally, clusters look like fat blobs and are well separated from each other.  If blobs look too small and scattered, it's possible perplexity is too low.
  - If you can’t see any features in the data, just one big homogeneous blob, then learning rate is likely too high, (but this will happen when any parameter is too high).

One nice thing is that the scripts tend to work independently, so if tsne is a problem, you can just re-run the tsne notebook with jupyter without having to run steps 0,1 again.  Once you have all the data processed, you can just tweak step 5 to get the data exactly as you want it.  Also, tsne is only required for the visualisation, so other useful outputs like the search-engine don't require this step.

=======

TFIDF visualisations
====================================================================

This is a project folder for creating interactive textual visualisations of Web of Science data.

There are a number of potential updates and forks to this code which can develop it and improve its utility.

These instructions assume that you have the latest Python 3 version of Anaconda from Continuum.io.

To test the code:
1. Install requirements.  Open a terminal (Mac/Linux) or command window (PC)
```
> pip install -r requirements.txt
```
1b. If you've never used nltk before, open the GUI
```
> ipython
> import nltk
> nltk.download()   # opens the GUI
```
Then download snowball stemmer and English language stopwords
```
>>> quit()
```
2. Create a folder called 'wos' and fill it with Web of Science data in tsv format. WoS data should, at a minimum include the following columns:
```python
['DI','PY','TI','AB','DE','ID','AU','AF','SO','SC','SN','EI','TC','Z9']
```

3. run the code
```
> python run.py
```
3b.  You can alternatively open a jupyter notebook
```
> jupyter notebook # or jupyter lab
```
... and then step through the code, one piece at a time in the .ipynb files

Following the above instructions should produce a visualisation.  However, it's unlikely that your first visualisation will give you what you want to see.  This is mostly down to step 2: ‘t-SNE’ which has a couple of inherent problems.
i) T-SNE is quite slow.  You may find that, for large datasets (say 10,000+ files) t-SNE can take several hours, or even need to run overnight.  
ii) T-SNE has a number of parameters, which have to be ‘tuned’ (by editing config.py) according to the particular dataset.  I’m not aware of an automatable way of tuning these parameters, so you may have to run the analysis repeatedly in order to get the parameters right.  My best advice for tuning t-SNE is:
 - Start with ‘perplexity’ set to 5-7% of the number of papers in your dataset.
 - Pick some numbers for the other settings based on: https://distill.pub/2016/misread-tsne/
 - Run it once and take a look at what you’ve got.  
  - If you see clusters forming up in lines, or squiggles, then it’s likely that ‘number of iterations’ is too low.
  - Ideally, clusters look like fat blobs and are well separated from each other.  If blobs look too small and scattered, it's possible perplexity is too low.
  - If you can’t see any features in the data, just one big homogeneous blob, then learning rate is likely too high, (but this will happen when any parameter is too high).

One nice thing is that the scripts tend to work independently, so if tsne is a problem, you can just re-run the tsne notebook with jupyter without having to run steps 0,1 again.  Once you have all the data processed, you can just tweak step 5 to get the data exactly as you want it.  Also, tsne is only required for the visualisation, so other useful outputs like the search-engine don't require this step.

