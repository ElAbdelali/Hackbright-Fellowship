english_to_spanish = {
    "hi": "hola", 
    "bye": "adios",
    "why": "porque",
    "please": "porfavor",
    "one": "uno",
    "two": "dos",
    "three": "tres",
    "four": "quatro",
    "five": "cinco",
    "six": "seis"
    }

def translate(word):
    if word in english_to_spanish:
        return english_to_spanish[word]
    else:
        print("The word you're looking for was not found.")
        
print(translate("three"))