from urllib.request import urlopen



#print(letter_to_points)
def score_word(word):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1,
              3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
    point_total = 0
    for letter in word:
        point_total += points[letters.index(letter)]
    return(point_total)


def babble():
    all_words = []

    r = urlopen("https://raw.githubusercontent.com/alex6480/BabbleSolver/main/Dictionary.txt")
    for line in r:
        all_words.append(str(line[:len(line)-1]))

    your_letters = list(input("Your Letters: "))
    start_letter = input("Starting Letter: ")
    end_letter = input("End Letter: ")
    spaces = input("Spaces apart: ")

    possible_words = []

    your_letters.extend((start_letter, end_letter))
    for word in all_words:
        list_of_letters = list(word)
        if start_letter in word:
            if end_letter in word:
                if word.find(start_letter[-1]) + int(spaces)+1 == word.find(end_letter[0]):
                    possible_word = word[2:len(word)-1]
                    possible_word_copy = list(possible_word)
                    possible_word_length = len(possible_word)
                    copy_of_your_letters = your_letters.copy()
                    if len(start_letter) > 1:
                        if start_letter in possible_word:
                            copy_of_your_letters.remove(start_letter)
                            for l in start_letter:
                                possible_word_copy.remove(l)
                            possible_word_length -= len(start_letter)
                    if len(end_letter) > 1:
                        if end_letter in possible_word:
                            copy_of_your_letters.remove(end_letter)
                            for l in end_letter:
                                possible_word_copy.remove(l)
                            possible_word_length -= len(end_letter)
                    for letter in possible_word_copy:
                        if letter in copy_of_your_letters:
                            copy_of_your_letters.remove(letter)
                            possible_word_length -= 1
                            if possible_word_length == 0:
                                possible_words.append(possible_word)
                elif word.find(start_letter[-1], word.find(start_letter[-1])+1) + int(spaces)+1 == word.find(end_letter[0]):
                    possible_word = word[2:len(word) - 1]
                    possible_word_copy = list(possible_word)
                    possible_word_length = len(possible_word)
                    copy_of_your_letters = your_letters.copy()
                    if len(start_letter) > 1:
                        if start_letter in possible_word:
                            copy_of_your_letters.remove(start_letter)
                            for l in start_letter:
                                possible_word_copy.remove(l)
                            possible_word_length -= len(start_letter)
                    if len(end_letter) > 1:
                        if end_letter in possible_word:
                            copy_of_your_letters.remove(end_letter)
                            for l in end_letter:
                                possible_word_copy.remove(l)
                            possible_word_length -= len(end_letter)
                    for letter in possible_word_copy:
                        if letter in copy_of_your_letters:
                            copy_of_your_letters.remove(letter)
                            possible_word_length -= 1
                            if possible_word_length == 0:
                                possible_words.append(possible_word)
                elif word.find(start_letter[-1]) + int(spaces)+1 == word.find(end_letter[0], word.find(end_letter[0])+1):
                    possible_word = word[2:len(word) - 1]
                    possible_word_copy = list(possible_word)
                    possible_word_length = len(possible_word)
                    copy_of_your_letters = your_letters.copy()
                    if len(start_letter) > 1:
                        if start_letter in possible_word:
                            copy_of_your_letters.remove(start_letter)
                            for l in start_letter:
                                possible_word_copy.remove(l)
                            possible_word_length -= len(start_letter)
                    if len(end_letter) > 1:
                        if end_letter in possible_word:
                            copy_of_your_letters.remove(end_letter)
                            for l in end_letter:
                                possible_word_copy.remove(l)
                            possible_word_length -= len(end_letter)
                    for letter in possible_word_copy:
                        if letter in copy_of_your_letters:
                            copy_of_your_letters.remove(letter)
                            possible_word_length -= 1
                            if possible_word_length == 0:
                                possible_words.append(possible_word)
                elif word.find(start_letter[-1], word.find(start_letter[-1])+1) + int(spaces)+1 == word.find(end_letter[0], word.find(end_letter[0])+1):
                    possible_word = word[2:len(word) - 1]
                    possible_word_copy = list(possible_word)
                    possible_word_length = len(possible_word)
                    copy_of_your_letters = your_letters.copy()
                    if len(start_letter) > 1:
                        if start_letter in possible_word:
                            copy_of_your_letters.remove(start_letter)
                            for l in start_letter:
                                possible_word_copy.remove(l)
                            possible_word_length -= len(start_letter)
                    if len(end_letter) > 1:
                        if end_letter in possible_word:
                            copy_of_your_letters.remove(end_letter)
                            for l in end_letter:
                                possible_word_copy.remove(l)
                            possible_word_length -= len(end_letter)
                    for letter in possible_word_copy:
                        if letter in copy_of_your_letters:
                            copy_of_your_letters.remove(letter)
                            possible_word_length -= 1
                            if possible_word_length == 0:
                                possible_words.append(possible_word)

    final_word_count = 0
    accepted_words = []
    for w in possible_words:
        if start_letter in w:
            if end_letter in w:
                if w.find(start_letter[-1]) + int(spaces) + 1 == w.find(end_letter[0]):
                    final_word_count += 1
                    accepted_words.append({"word": w, "score": score_word(w)})
                elif w.find(start_letter[-1], word.find(start_letter[-1]) + 1) >= 0 and w.find(start_letter[-1], w.find(start_letter[-1]) + 1) + int(spaces) + 1 == w.find(end_letter[0]):
                    final_word_count += 1
                    accepted_words.append({"word": w, "score": score_word(w)})
                elif w.find(end_letter[0], w.find(end_letter[0]) + 1) >= 0 and w.find(start_letter[-1]) + int(spaces) + 1 == w.find(end_letter[0], w.find(end_letter[0]) + 1):
                    final_word_count += 1
                    accepted_words.append({"word": w, "score": score_word(w)})
                elif word.find(start_letter[-1], word.find(start_letter[-1]) + 1) >= 0 and w.find(end_letter[0], w.find(end_letter[0]) + 1) >= 0 and w.find(start_letter[-1], w.find(start_letter[-1]) + 1) + int(spaces) + 1 == w.find(end_letter[0], w.find(end_letter[0]) + 1):
                    final_word_count += 1
                    accepted_words.append({"word": w, "score": score_word(w)})
    if final_word_count == 0:
        print("No words with that configuration found")

    def myFunc(e):
        return e['score']

    accepted_words.sort(key=myFunc, reverse=True)

    for wrd in accepted_words:
        print(wrd['word'] + ' ' + str(wrd['score']))


while True:
    babble()
    print()