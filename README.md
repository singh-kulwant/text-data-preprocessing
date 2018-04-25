# text-data-preprocessing
In this project - a lengthy, unprocessesd single string data will be converted into cleaned tokens.

Tokens will be further used for text mining and/or natural language processing tasks.

File contents and description:

  # tdp_imports.py  contains all the libraries required for processing.
  
  nltk - Natural Language Toolkit is the best-known NLP library in python ecosystem.
         Generally used for tokenization, stemming, part of speech tagging etc.
  
  BeautifulSoup - used for extracting data from HTML and XML documents.
  
  Inflect - accomplishes the natural language related tasks of generating plurals, singular nouns, ordinals, indefinite articles, converting numbers to words
  
  Contractions - solely used for expanding contractions
  
  we need to define a random text for sample variable and save it in sample_text.py
  
  # Noise Removal - text specific normalization task, takes prior to tokenization.
  
  # tdp_denoise.py - it removes text file header, HTML,XML,markup and metadata and extract valueable data from other formats
