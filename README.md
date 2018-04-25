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
  
  regular expression to remove brackets etc.
  
  we need to define a random text for sample variable and save it in sample_text.py
  
  # Noise Removal - text specific normalization task, takes prior to tokenization.
  
  # tdp_denoise.py - it removes text file header, HTML,XML,markup and metadata and extract valueable data from other formats
  denoising tasks need to implemented prior to tokenization
  
  # tdp_contractions.pyy - replaces contractions with their expansions
  not mandatory to do at this stage prior to tokenization, doing do makes our task easier and straightforward
  
  # Tokenizations - splits longer pieces of string into smaller pieces, also refered as text segmentation or lexical analysis
  
  # tdp_tokenize.py - will tokenize our sample text into a list of words, using NLTKs word_tokenize() method
  
