from django.http import HttpResponse as hr
from django.shortcuts import render

def hithere(req):
    return render(req,'home.html')

def Count(req):
    text = req.GET['fulltext']
    wordCount = len(text.split())
    wordDict = {}
    for word in text.split():
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    words = sorted(wordDict.items(), key=lambda x: x[1], reverse=True)
    print(words)
    return render(req, 'count.html', {'txt':text, 'word_count':wordCount, 'words':words })

def about(req):
    return render(req, 'about.html')
