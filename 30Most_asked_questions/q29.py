#  question: reverse the sentence not the words. 

def reversed_sentence(sentence): 
    reverse_sentence=" "
    word=" "
    for char in sentence:
        if char == ' ':
            reverse_sentence=word+' '+reverse_sentence
            word=' '
        else: 
            word+=char 
    reverse_sentence=word+ ' '+ reverse_sentence
    return reverse_sentence.strip()
print(reversed_sentence("hello how are you"))