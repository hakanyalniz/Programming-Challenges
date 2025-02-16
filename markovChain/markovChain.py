import random
import re


def main():
    with open("./assets/grimm.txt", "r", encoding="utf-8") as file:
        text = file.read()
        newText = text.lower()
    
    newText = normalize(newText)
    newText = tokenize(newText)
    markovDict = markovChain(newText)

    generatedText = generateText(markovDict)

    f = open("markovOutput.txt", "w")
    f.write(generatedText)
    f.close()


# Remove Gutenberg header
def normalize(text):
    # Added ignorecase for case insensitivity
    text = re.sub(
        r"\*The Project Gutenberg Etext Fairy Tales, by the Grimm Brothers.*?\*end the small print! for public domain etexts\*ver\.04\.29\.93\*end\*", 
        "", 
        text, 
        flags=re.DOTALL | re.IGNORECASE  
    )

    # Write the new file, edited and lowercased
    # f = open("output.txt", "w")
    # f.write(text.lower())
    # f.close()
    
    return text


# split text into list from the space
def tokenize(text):
    return text.split()


def markovChain(text):
    # take first item, make it a key, add the next item as value
    markovDict = {}
    textLength = len(text)
    
    for index in range(textLength - 1):
        current_word = text[index]
        next_word = text[index + 1]
        # if text[index] exists in markovDict, add to it
        # or else create new key list pair
        if current_word in markovDict:
            markovDict[current_word].append(next_word)
        else:
            markovDict[current_word] = [next_word]

    return markovDict


def generateText(dict, length=1000):
    # pick a random word, add it to the beginning of sentence
    currentWord = random.choice(list(dict.keys()))  
    sentence = [currentWord.capitalize()]

    # length-1 because we already have the first word
    for _ in range(length - 1):  
       # Get the list of words that can follow the current word
        possible_next_words = dict.get(currentWord, [])

        if not possible_next_words:
            # stop if no next word is found
            break  

        # Pick a random next word from the list of possible next words
        nextWord = random.choice(possible_next_words)

        # if the last character of the last item in list is a dot, 
        # capitalize the word
        if (sentence[len(sentence) - 1][-1] == "." or 
            sentence[len(sentence) - 1][-1] == "?" or 
            sentence[len(sentence) - 1][-1] == "!"):
            nextWord = nextWord.capitalize()

        # Add the next word to the sentence and update the current word
        sentence.append(nextWord)
        # if nextWord is capitalized, then it will not be found in the dict, since every key there is lowercase
        currentWord = nextWord.lower()

        # if current Word length increases by 100, add newline
        if (len(sentence)%100 == 0):
            sentence.append("\n")


    return " ".join(sentence)


if __name__ == "__main__":
    main()