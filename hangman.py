import random
 
def get_secret_word(word_file="/usr/share/dict/words"):
    good_words = []
    with open(word_file) as f:
        for word in f:
            word = word.strip()
            if not word.isalpha():
                continue
            if len(word) < 5:
                continue
            if word[0].isupper():
                continue
            good_words.append(word)
 
    word = random.choice(good_words)
    return word.lower()

def hide_word(sw,guess):
    secretword = list(sw)
    #guess = list(guess)
    display =[]
    for i in secretword:
        if i in guess:
            display.append(i)
        else:
            display.append("_")
    return(''.join(display))
     
def get_status_message(sw,cg,wg,turns_left):
    masked_word = hide_word(sw, cg + wg)
    guesses = "".join(cg + wg)
    status_message = """{}
    guesses: {}
    turns left: {}
""".format(masked_word,guesses,turns_left)
    return status_message


def play(sw, cg, wg, ng, turns_left): 
    if ng in cg + wg:
        fm = "already guessed"
        return(cg,wg,turns_left,False,fm)
    if ng in sw:
        cg.append(ng)
        fm = "next word"
    else:
        turns_left -=1
        wg.append(ng)
        fm = "wrong guess"
        
    guessed = "_" not in hide_word(sw, cg + wg)
    if guessed:
        return (cg,wg,turns_left,True,"You won!")
    elif turns_left == 0:
        return(cg,wg,turns_left,True,"You lost. The word was {}".format(sw))
    return (cg,wg,turns_left,False,fm)

def main():
    secret_word = get_secret_word()
    print(secret_word)
    cg = []
    wg = []
    turns_left = 7
    game_over = False
    while not game_over:
        status = get_status_message(secret_word,cg,wg,turns_left)
        print(status)
        ip = input("enter a letter: ")
        cg,wg,turns_left,game_over, message = play(secret_word, cg, wg, ip, turns_left) 
        print(message)
main()




