# Week 10

Data Cleaning and Text Cleaning

First, determine what you need from your data and how are you analyzing it. This
will be the basis for determining what you need to do to clean your data.

Example for data cleaning: Machine Learning Project (Jupyter notebook)
Go over:
Data Sources
* UCLA Behind Bars COVID-19 - prison population of each state, social distance policies (convert to dummies)
* Bureau of Justice Statistics - prison capacity
* Marshall Project - prison cases.

We updated Marshall Project to locate the date of the case. If the date is after the
date social distance policies were put in effect, update the dummies. Otherwise,
all dummies are empty.

Calculate changes in cases and death over time.

Basic Visualizations

One-hot encode the states

---

Tips for data-cleaning text. This may go more into Data Skills II or Machine Learning, so an overview:

* What is your analysis? For your analysis, do you need to extract certain words,
or do you want to use almost all the words (natural language processing)?

* Generally, you may want to do the following:
    * Remove capitalization and punctuation
    * Tokenization
    * Optional: Lemmatize/Stem Words: Transforms words to get the root of the word. If you don't do this, all words will be distinct from each other. Example: 'runs' and 'run' will be considered as two different words,
    lemmatizing and stemming would make them the same.

---
Code on cleaning the data

Example for parsing data: BeautifulSoup project in GitHub
Go over:
How BeautifulSoup parsed data, where the data was stored, what we did with it

