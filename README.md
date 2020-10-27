# ArabicStopWords-Cleaner
This work is supported by the Ministry of Higher Education and Scientific Research in Algeria (Project C00L07UN100120180002)
Conception & Supervision : L. Ouahrani & D. Bennouar /  Contributor : Abdennour BenHamida.

This code allows the user to clean his arabic text by removing stopwords using two methods:
- Clean from list: a static list of stopwords is used to compare with the text's words, if a words matches with another from the list, it will be removed from the input text
- Clean from appearence: i f a word appears more than "n" time, it'll be considered as stopword and removed from the input text.
The output file is a json file containing:
- New Text: new text without any stopword.
- Stops in: A list of all the stopwords found in the input text.

1- Requirments: 
- You may need to enable these two commandes if your punkt isn't installed, once dowloaded and installed nltk will work perfectly fine:
  #1- import nltk
  #2- nltk.download('punkt')
- Python 2.7 or later
- "Stopwords.txt"

2- Libraries used:
- word_tokenize: we use to tokenize (split) our texts into a list of words
- json: files management and saving results

3- How to use:
  - If your input is a".txt" file, you need to read it with the "fromTxt(Path)" function included in the "Arabic_Stopwords.py" file and then start working with one of the two methods, for exemple: Stopwords(fromTxt("C:/....../ArabicText.txt"))
  - If not, directly launch the function you need with your string.
 
 For further questions or inquiries about this code, you can contact: 
 - abdennourbenhamida09@gmail.com
