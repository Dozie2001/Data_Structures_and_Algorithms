#!/usr/bin/python3
"""To solve Tower of Hanoi based on user input"""
from hanoi import hanoi

n = int(input('Enter the number of discs: '))
source = int(input('Enter source pole: '))
spare = int(input('Enter spare pole: '))
target = int(input('Enter target pole: '))
hanoi(n, source, spare, target)