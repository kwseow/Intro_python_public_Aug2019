sentence = "You are so close , - but I am thinking of the problem"
word_list=sentence.split()

def longest_word(word_list):
    longest_word = ""
    for word in word_list:
        print("Prevous longest word ->%s"%(longest_word))
        print("Current word ->%s"%(word))
        if (len(longest_word) < len(word)):
            longest_word = word
        print("Current longest word ->%s"%(longest_word))
        input("Press enter to continue...")
    return longest_word

print("Longest word is : %s"%(longest_word(word_list)))



