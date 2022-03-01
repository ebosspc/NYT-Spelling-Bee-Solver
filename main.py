# Get letter inputs
ring_letter_1 = str(input("Please enter the first ring letter: "))
ring_letter_2 = str(input("Please enter the second ring letter: "))
ring_letter_3 = str(input("Please enter the third ring letter: "))
ring_letter_4 = str(input("Please enter the fourth ring letter: "))
ring_letter_5 = str(input("Please enter the fifth ring letter: "))
ring_letter_6 = str(input("Please enter the sixth ring letter: "))
center_letter = str(input("Please enter the center, required letter: "))

# Create a list of unusable letters
alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_list.remove(ring_letter_1)
alphabet_list.remove(ring_letter_2)
alphabet_list.remove(ring_letter_3)
alphabet_list.remove(ring_letter_4)
alphabet_list.remove(ring_letter_5)
alphabet_list.remove(ring_letter_6)
alphabet_list.remove(center_letter)
unusable_letters_list = alphabet_list

# Search for words that meet the requirements
words_database = open("Words_English.txt", 'r')
words_list = []
for line in words_database:
    word = line.strip()
    if ring_letter_1 in word:
        valid_word = 1
        for unusable_letter in unusable_letters_list:
            if unusable_letter not in word:
                continue
            else:
                valid_word = 0
        if valid_word == 1:
            words_list.append(word)
            continue
    if ring_letter_2 in word:
        valid_word = 1
        for unusable_letter in unusable_letters_list:
            if unusable_letter not in word:
                continue
            else:
                valid_word = 0
        if valid_word == 1:
            words_list.append(word)
            continue
    if ring_letter_3 in word:
        valid_word = 1
        for unusable_letter in unusable_letters_list:
            if unusable_letter not in word:
                continue
            else:
                valid_word = 0
        if valid_word == 1:
            words_list.append(word)
            continue
    if ring_letter_4 in word:
        valid_word = 1
        for unusable_letter in unusable_letters_list:
            if unusable_letter not in word:
                continue
            else:
                valid_word = 0
        if valid_word == 1:
            words_list.append(word)
            continue
    if ring_letter_5 in word:
        valid_word = 1
        for unusable_letter in unusable_letters_list:
            if unusable_letter not in word:
                continue
            else:
                valid_word = 0
        if valid_word == 1:
            words_list.append(word)
            continue
    if ring_letter_6 in word:
        valid_word = 1
        for unusable_letter in unusable_letters_list:
            if unusable_letter not in word:
                continue
            else:
                valid_word = 0
        if valid_word == 1:
            words_list.append(word)
            continue
    if center_letter in word:
        valid_word = 1
        for unusable_letter in unusable_letters_list:
            if unusable_letter not in word:
                continue
            else:
                valid_word = 0
        if valid_word == 1:
            words_list.append(word)
            continue
    
# Remove words without the center letter
words_list.sort(key = len)
words_list.reverse()
for i in range(20):
    for word in words_list:
        if center_letter in word:
            continue
        else:
            words_list.remove(word)

# Output the answer key
print(words_list)