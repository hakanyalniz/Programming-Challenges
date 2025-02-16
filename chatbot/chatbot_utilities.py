import json
import yaml

def loadJsonl():
    yaml_data = {
        "categories": ["movie-dialogues"],
        "conversations": [
            ["Hello, how are you?", "I'm fine, thank you."],
            ["What's your favorite movie?", "I love Inception!"],
        ],
    }

    tempConvoList = []
    # Load the jsonl conversation file
    with open('./assets/movie-corpus/cleaned_corpus.jsonl', 'r') as file:
        conversations = [json.loads(line) for line in file]
        # check conversation_id, if not null, put in list, if null, that is root

        # loop through the conversations dataset
        for i in range(len(conversations) - 1, -1, -1):
            # add the texts into a list
            tempConvoList.append(conversations[i]["text"])
            # if the current text has reply to null, it is the root
            # add it to the greater data dictionary
            # and purge the tempConvoList to empty, so it can be filled again
            # this will allow us to append full conversations to the data variable
            # check i - 1, to see if the next loop will have none, if so, add all current ones to list
            # this is done because we go from end to beginning and the Null is at the end
            if (conversations[i - 1]["reply-to"] is None):
                yaml_data["conversations"].append(tempConvoList)
                tempConvoList = []

    with open("movie_dialogues.yml", "w") as yaml_file:
        yaml.dump(yaml_data, yaml_file, default_flow_style=False, sort_keys=False)


def loadTxt():
    yaml_data = {
        "categories": ["movie-dialogues"],
        "conversations": [
            ["Hello, how are you?", "I'm fine, thank you."],
            ["What's your favorite movie?", "I love Inception!"],
        ],
    }
        
    # for txt files with eou
    tempList = []
    tempSentence = ""
    # Load the jsonl conversation file
    with open('../assets/dialogues_train.txt', 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()  # Split the line into words
            for word in words:
                if word == '__eou__':
                    tempList.append(tempSentence)
                    tempSentence = ""
                else:
                    tempSentence += word + " " 
            # when we have dealt with this line, append it to data
            yaml_data["conversations"].append(tempList)
            tempList = []