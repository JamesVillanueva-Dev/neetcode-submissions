from typing import List

def contains_duplicate(words: List[str]) -> bool:
    words_set = set()

    for word in words:
        words_set.add(word)
    return len(words_set) != len(words)

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
