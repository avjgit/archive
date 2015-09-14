# Write code for the function play_game, which takes in as inputs parts_of_speech, 
# which is a list of acceptable replacement words and ml_string, which is a string that 
# can contain replacement words that are found in parts_of_speech. Your play_game function 
# should return the joined list replaced, which will have the same structure as ml_string, 
# only that replacement words are swapped out with "corgi", since this program cannot replace 
# those words with user input. 

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """Straight outta PLACE, crazy NOUN named PERSON, 
from the gang called PLURALNOUN Wit Attitude"""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
        
def play_game(ml_string, parts_of_speech):    
    replaced = []   
    for w in ml_string.split():
        replacement = word_in_pos(w, parts_of_speech)
        if replacement:
            user_input = raw_input("enter " + replacement)
            w = w.replace(replacement, "corgi")
        replaced.append(w)
    return " ".join(replaced)
    
print play_game(test_string, parts_of_speech)