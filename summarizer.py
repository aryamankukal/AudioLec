from gensim.summarization.summarizer import summarize

def summarizer(text):
    wordCount = len(text.split(" "))
    summ = summarize(text, word_count =wordCount / 4)
    return summ