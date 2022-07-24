from django.shortcuts import HttpResponse
from rank_bm25 import BM25Okapi

def searchlist(mylist,query,nmb):
    tokenized_list = [doc.split(" ") for doc in mylist]
    bm25 = BM25Okapi(tokenized_list)
    tokenized_query = query.split(" ")
    doc_scores = bm25.get_scores(tokenized_query)
    print(doc_scores)
    doc = bm25.get_top_n(tokenized_query, mylist, n=nmb)
    # corpus = ["Hello there good man!","It is quite windy in London","How is the weather today?"]
    # tokenized_corpus = [doc.split(" ") for doc in corpus]
    # bm25 = BM25Okapi(tokenized_corpus)
    # print(bm25)
    # query = "windy London"
    # tokenized_query = query.split(" ")
    # doc_scores = bm25.get_scores(tokenized_query)
    # print(doc_scores)
    # doc = bm25.get_top_n(tokenized_query, corpus, n=1)
    # print(doc)
    return doc