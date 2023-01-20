#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    idx = 0
    list = dir(hidden_4)
    word = ""
    for i in range(len(list)):
        word = list[idx]
        if word[0] != "_":
            print(word)
        idx += 1
