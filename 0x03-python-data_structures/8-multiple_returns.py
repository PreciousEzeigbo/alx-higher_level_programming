#!/usr/bin/python3
def multitude_returns(sentence):
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
