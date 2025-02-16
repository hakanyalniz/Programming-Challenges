# Training data from DailyDialog Dataset was used, alongside the default English ChatterBot corpus
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import sqlite3
import os


def main():
    chatbot = ChatBot('Chatbot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3'  # File to store the database
    )    

    train(chatbot)

    # chat loop
    while(True):
        userInput = input(">")
        response = chatbot.get_response(userInput)
        print(response)


def train(chatbot):
    # the first time the program is run
    if not os.path.exists("database.sqlite3"):
        # Create a new trainer for the chatbot
        trainer = ChatterBotCorpusTrainer(chatbot)

        # Train the chatbot based on the english corpus
        trainer.train("../assets/english_corpus")
    else:
        # Connect to the SQLite database to check if there is any data in it
        conn = sqlite3.connect("database.sqlite3")
        cursor = conn.cursor()

        # Query to check if there's any data in the table
        cursor.execute("SELECT COUNT(*) FROM statement")
        result = cursor.fetchone()
        
        if result[0] == 0:
            # Train with the default corpus
            print("Training the chatbot because it's empty...")
            trainer = ChatterBotCorpusTrainer(chatbot)
            trainer.train('../assets/english_corpus')  
        else:
            print("Chatbot is already trained and using the existing database.")
        conn.close()


if __name__ == "__main__":
    main()