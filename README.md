# AUTO_FILL_THE_BLANKS_GENERATOR
this is a program which takes a .txt file and generates fill in the blanks from it.
CREDITS   go to cloudxlab for the main algorithm and solution
the algorithms basic steps are explained below:
1: load the text file into pyhton.
2:convert it into TextBlob
3:THIS IS THE MOST CRUCIAL STEP 
we have used two python dictionaries , 
sent and parts
sent contains the seperate sentences of the file as keys,
the values are all parts of speech(i.e. nouns and propernouns etc) in that sentence.
parts contains all the various parts of speech in the document as keys and the words as values.
3-1:for each sentence in the file
3-2:     for each tag in the sentence
          parts[tag].append(word)(i.e. the word in the sentence for the tag)
3-3:sent[sentence]=parts
4: now we have the sent and parts dicitonaries as described above.
5: now we will implement a function for placing a blank in the sentence.
6: implement a function for taking a given sentence and return a fill in the blank form sentence.


