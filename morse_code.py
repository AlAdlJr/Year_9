# Morce Code - Ismail AlAdl

# Makeing the dictionary
def morce_code (text):
    codes = {
     "a": ".-",
     "b": "-...",
     "c": "-.-.", 
     "d": "-..",
     "e": ".",
     "f": "..-.",
     "g": "--.",
     "h": "....",
     "i": "..",
     "j": ".---",
     "k": "-.-",
     "l": ".-..",
     "m": "--",
     "n": "-.",
     "o": "---",
     "p": ".--.",
     "q": "--.-",
     "r": ".-.",
     "s": "...",
     "t": "-",
     "u": "..-",
     "v": "...-",
     "w": ".--",
     "x": "-..-",    
     "y": "-.--",
     "z": "--..",
    }   
   
   # Makeing the morce code empty varible
    
    morce_word = ""

    # Converty the word into morce code using a for loop

    for char in text:
        morce_word += codes[char]

    return morce_word

# While loop

choice = 0

while choice != 2:
    
    # Menu choice

    print("Menu choice")
    print("input your choice ")
    choice = int(input("1 - Convert a word into morce code or 2 - Quit "))
    
    if choice == 1:
        # Input a word
        text = input("User input a word " )

        # Output the word in morce code
        print(morce_code(text))
    else:
        choice == 2

