'''
write a function that reads a text file containing a sequence of words on multiple lines, separated by any number of spaces and returns the size of the longest word.
note that a word can be split on more than one line. for example, if you read in the content of the file in the following list (with readlines):

["abacus     bearing  colorf\n",
"ul    dedication entertain\n",
"ment  future  gamification"]

the function will return 13, as the longest word is "entertainment".
'''


def readTextInFile(filepath):
  file_ref = open(filepath, 'r', encoding='utf8')
  txt = file_ref.read()
  return txt


def removeNewLines(txt):
  txt.replace('\n', '')
  return None


def LongestWordInFile(filepath):
  # your code goes here
  pass


if __name__ == "__main__":
  print(readTextInFile("testfile.txt"))
  print(LongestWordInFile("testfile.txt"))
