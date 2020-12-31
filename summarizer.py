from gensim.summarization.summarizer import summarize

def summarizer(text):
    summ = summarize(text, ratio=0.25)
    print(summ)
