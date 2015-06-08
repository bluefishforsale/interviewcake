#!/usr/bin/env python

import  itertools

end = 'STOP'

def flatten(data):
  return list(itertools.chain.from_iterable(data))


def make_trie(*words):
  steps = 0
  root = {}
  for word in words:
    current_dict = root
    for letter in word:
      current_dict = current_dict.setdefault(letter, {})
      steps +=1
    current_dict = current_dict.setdefault(end, end)
  print("Insert Length / Operations = [%s / %s]" % (len(flatten(words)), steps))
  return root


def in_trie(trie, word):
  steps = 0
  current_dict = trie
  for letter in word:
    steps +=1
    if letter in current_dict:
      current_dict = current_dict[letter]
    else:
      print("%d steps for" % steps),
      return False
  else:
    if end in current_dict:
      print("%d steps for" % steps),
      return True
    else:
      print("%d steps for" % steps),
      return False


words = ('www.google.com',
         'www.apple.com',
         'www.google.org',
         'facebook.com',
         'gargle.com',
         'aples.com')

trie = make_trie(*words)

print(trie)
print(in_trie(trie, 'www.google.com'))
print(in_trie(trie, 'www.gogle.com'))
