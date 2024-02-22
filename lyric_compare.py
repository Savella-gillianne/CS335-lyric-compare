import click
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from tabulate import tabulate

def vectorizer(input,vocab): #converts prompt/input to word count matrix
    countVec = CountVectorizer(
    lowercase=True,
    max_features=300000,
    ngram_range = (1,3),
    vocabulary=vocab
    )

    vecPrompt = countVec.transform([str(input)])

    return vecPrompt

def transformer(lyricModel): #takes in word count matrix, transforms to TF-IDF
    transform = TfidfTransformer()
    transformedMatrix = transform.fit_transform(lyricModel) 

    return transformedMatrix

def scoreSort(simScores, data, numResults):
    organizedTitles = []
    titles = data["title"] 
    artists = data["artist"]

    index = 0
    for title in titles:
        score = float(simScores[index])
        artist = artists[index]
        organizedTitles.append((score, title, artist))
        index += 1
    
    fullList = sorted(organizedTitles, reverse=True)
    sortedScores = fullList[:numResults]

    return sortedScores

@click.command
@click.option("--prompt", required=True, help="Prompt to compare lyrics against.", prompt="Give me a song about...")
@click.option("--size", "--s", default="medium", help="Size of song dataset to use: [mini|medium|large]")
@click.option("--results", "--r", default=3, help="Number of songs to return.")
def lyric_compare(prompt, size, results):
    """Compares input prompt to various song lyrics."""
    
    countName = size
    countFile = open(countName,"rb")
    countMatrix = pickle.load(countFile)
    
    vocabFile = size + "-vocab"
    vocabDict = open(vocabFile,"rb")
    vocab = pickle.load(vocabDict)

    dfFile = size + "-df"
    songs = open(dfFile,"rb")
    songInfo = pickle.load(songs)

    #TF-IDF lyric word count matrix
    lyricModel = transformer(countMatrix) 

    #vectorize and transform prompt
    vecPrompt = vectorizer(prompt, vocab)
    finPrompt = transformer(vecPrompt)

    #compare prompts and lyrics
    cosSim = cosine_similarity(lyricModel, finPrompt)

    topN = scoreSort(cosSim, songInfo, results)
    click.echo(tabulate(topN, headers=["Score", "Song Title", "Artist"])) 

    click.echo("\nDone!")

if __name__ == "__main__":
    lyric_compare()
