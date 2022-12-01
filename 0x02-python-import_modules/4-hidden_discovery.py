#!/usr/bin/python3
import hidden_4

for func in dir(hidden_4):
    if func[0] != "_":
        print(func)
