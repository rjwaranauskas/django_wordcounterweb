from django.http import HttpResponse
from django.shortcuts import render
import operator

def index(request):
	return render(request, 'index.html',)

def count(request):
	fulltext = request.GET['fulltext']
	
	wordlist = fulltext.split()
	wordlist_dict = {}
	for word in wordlist:
		if word in wordlist_dict:
			wordlist_dict[word] += 1
		else:
			wordlist_dict[word] = 1

	sorted_words = sorted(wordlist_dict.items(), key=operator.itemgetter(1), reverse=True)
	return render(request, 'count.html',{"fulltext":fulltext, 'wordcount':len(wordlist), "sorted_words":sorted_words})

def about(request):
	return render(request, 'about.html')