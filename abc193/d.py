#!/usr/bin/python3
import numpy

num_card = int(input())
takahashi = list(input())  # Takahashi
aoki = list(input()).sort()  # Aoki

numlist=list(range(9))
unique_takahashi, count_takahashi = numpy.unique(takahashi, return_counts=True)
unique_aoki, count_aoki = numpy.unique(aoki, return_counts=True)

score_takahashi=0
score_aoki=0

for i in range(1,len(unique_takahashi)):
    score_takahashi = sum()