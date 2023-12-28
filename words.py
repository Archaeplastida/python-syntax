def print_upper_words(words, must_start_with):
    """This will print words in all UPPERCASE as long as they start with the given letters
    
    ex: print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with=["h", "y"])
                   
        should print out 'HELLO', 'HEY', 'YO', 'YES'"""
    for x in words:
        if x[0].lower() in must_start_with or x[0].upper() in must_start_with:
            print(x.upper())

print_upper_words(must_start_with=["e", "f", "r"],
                  words=["Electric", "empty", "full", "party", "shark", "Remilia", "Eirin", "USF", "Python", "Excel", "exactly", "racecar", "vroom", "Flandre", "Donkey", "Zebra", "floppy", "Xtreme"])