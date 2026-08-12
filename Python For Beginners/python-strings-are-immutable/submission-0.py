def remove_fourth_character(word: str) -> str:
    return word[0:3] + word[4:len(word)]


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
