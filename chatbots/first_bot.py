
from nltk.chat.util import Chat
import reflections,pairs 

def chatty():
        # default message at the start
    print("Hi, I'm Chatty and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ")
    chat = Chat(pairs.pairs, reflections.reflections)
    chat.converse()
if __name__ == "__main__":
    chatty()
