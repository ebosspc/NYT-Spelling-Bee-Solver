letter_1 = str(input("Please enter the first letter: "))
letter_2 = str(input("Please enter the second letter: "))
letter_3 = str(input("Please enter the third letter: "))
letter_4 = str(input("Please enter the fourth letter: "))
letter_5 = str(input("Please enter the fifth letter: "))
letter_6 = str(input("Please enter the sixth letter: "))
letter_7 = str(input("Please enter the seventh letter: "))

alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                ,'n','o','p','q','r','s','t','u','v','w','x','y','z']

alphabet_list.remove(letter_1)
alphabet_list.remove(letter_2)
alphabet_list.remove(letter_3)
alphabet_list.remove(letter_4)
alphabet_list.remove(letter_5)
alphabet_list.remove(letter_6)
alphabet_list.remove(letter_7)

unusable_letters_list = alphabet_list



words_database = open("Words_English.txt", 'r')
words_list = []
for line in words_database:
    word = line.strip()
    if letter_1 in word:
        valid_word = 1
        for unusable_letter in unusable_letters_list:
            if unusable_letter not in word:
                continue
            else:
                valid_word = 0
        if valid_word == 1:
            words_list.append(word)
            continue
    if letter_2 in word:
        valid_word = 1
        for unusable_letter in unusable_letters_list:
            if unusable_letter not in word:
                continue
            else:
                valid_word = 0
        if valid_word == 1:
            words_list.append(word)
            continue
    if letter_3 in word:
        valid_word = 1
        for unusable_letter in unusable_letters_list:
            if unusable_letter not in word:
                continue
            else:
                valid_word = 0
        if valid_word == 1:
            words_list.append(word)
            continue
    if letter_4 in word:
        valid_word = 1
        for unusable_letter in unusable_letters_list:
            if unusable_letter not in word:
                continue
            else:
                valid_word = 0
        if valid_word == 1:
            words_list.append(word)
            continue
    if letter_5 in word:
        valid_word = 1
        for unusable_letter in unusable_letters_list:
            if unusable_letter not in word:
                continue
            else:
                valid_word = 0
        if valid_word == 1:
            words_list.append(word)
            continue
    if letter_6 in word:
        valid_word = 1
        for unusable_letter in unusable_letters_list:
            if unusable_letter not in word:
                continue
            else:
                valid_word = 0
        if valid_word == 1:
            words_list.append(word)
            continue
    if letter_7 in word:
        valid_word = 1
        for unusable_letter in unusable_letters_list:
            if unusable_letter not in word:
                continue
            else:
                valid_word = 0
        if valid_word == 1:
            words_list.append(word)
            continue
    

words_list.sort(key = len)
words_list.reverse()
print(words_list)