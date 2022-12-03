#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return len(sentence), None
    return len(sentence), sentence[0]

sentence = "At school, I learnt C!"
sentence1 = ""
length, first = multiple_returns(sentence)
length1, first1 = multiple_returns(sentence1)

print("Length: {:d} - First character: {}".format(length, first))
print("Length: {:d} - First character: {}".format(length1, first1))
