from hangman import get_secret_word,hide_word,get_status_message,play
 
def test_secret_word_no_punctuation():
    with open("/tmp/words.txt","w") as f:
        for i in ["word'one", "word_two", "wordthree"]:
            f.write(i+"\n")
    selected_word = get_secret_word('/tmp/words.txt')
    assert selected_word == "wordthree"

def test_secret_word_atleast_five():
    with open("/tmp/words.txt","w") as f:
        for i in ["wo", "wor", "word", "bigword"]:
            f.write(i+"\n")
    selected_word = get_secret_word('/tmp/words.txt')
    assert selected_word == "bigword"
 
def test_secret_word_lowercase():
    with open("/tmp/words.txt","w") as f:
        for i in ["Wording", "wOrding", "WORDING", "wording"]:
            f.write(i+"\n")
    selected_word = get_secret_word('/tmp/words.txt')
    assert selected_word == "wording"
 
def test_secret_word_no_repeat():
    with open("/tmp/words.txt","w") as f:
        for i in ["disaster","recall","advise","national","infrastructure","shots","fired",
                  "federation", "duress"]:
            f.write(i+"\n")
    l = []
    for i in range(3):
        l.append(get_secret_word('/tmp/words.txt'))
    assert len(set(l)) == 3


def test_hide_word_no_guesses():
    x = "elephant"
    guess = []
    assert hide_word(x,guess) == "________"

def test_hide_single_guess():
    sw = "elephant"
    guess = "l"
    assert hide_word(sw,guess) == "_l______"

def test_hide_first_guess():
    sw = "elephant"
    guess = "e"
    assert hide_word(sw,guess) == "e_e_____"

def test_hide_wrong_guess():
    sw = "elephant"
    guess = "s"
    assert hide_word(sw,guess) == "________"
 
def test_hide_two_guess():
    sw = "elephant"
    guess = ["e","l"]
    assert hide_word(sw,guess) == "ele_____"

def test_status_message():
    sw = "baseball"
    cg = ["b","l"]
    wg = ["v"]
    turns_left = 8

    assert get_status_message(sw,cg,wg,turns_left) == """b___b_ll
    guesses: blv
    turns left: 8
"""
def test_new_guess_correct_normal_turn():
    cg,wg,turns_left,game_over,fm = play(sw = "baseball", cg = ["b","l"], wg = ["v"],
                                                       ng = "a",turns_left = 8)
    assert cg == ["b","l","a"]
    assert wg == ["v"]
    assert turns_left == 8
    assert game_over == False

def test_new_guess_win_turn():
    cg,wg,turns_left,game_over,final_message = play(sw = "baseball", cg = ["b","l","a","s"],
                                                    wg = ["v"],ng = "e",turns_left = 4)
    assert cg == ["b","l","a","s","e"]
    assert wg == ["v"]
    assert turns_left == 4
    assert game_over == True


def test_new_guess_lose_turn():
    cg,wg,turns_left,game_over,final_message = play(sw = "baseball", cg = ["b","l","a","s"],
                                                    wg = ["v"],ng = "k",turns_left = 1)
    assert cg == ["b","l","a","s",]
    assert wg == ["v","k"]
    assert turns_left == 0
    assert game_over == True

def test_new_guess_wrong_normal_turn():
    cg,wg,turns_left,game_over,fm = play(sw = "baseball", cg = ["b","l","a","s"],
                                                    wg = ["v"],ng = "k",turns_left = 5)
    assert cg == ["b","l","a","s",]
    assert wg == ["v","k"]
    assert turns_left == 4
    assert game_over == False

def test_new_guess_correct_repeat_turn():
    cg,wg,turns_left,game_over,fm = play(sw = "baseball", cg = ["b","l"], wg = ["v"],
                                                       ng = "l",turns_left = 8)
    assert cg == ["b","l"]
    assert wg == ["v"]
    assert turns_left == 8
    assert game_over == False

def test_new_guess_wrong_repeat_turn():
    cg,wg,turns_left,game_over,fm = play(sw = "baseball", cg = ["b","l"], wg = ["v"],
                                                       ng = "v",turns_left = 8)
    assert cg == ["b","l"]
    assert wg == ["v"]
    assert turns_left == 8
    assert game_over == False
