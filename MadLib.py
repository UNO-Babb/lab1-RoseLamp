#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  noun=input ("give me a noun ")
  noun2=input ("give me another noun ")
  noun3=input ("give me another noun ")
  verb=input ("give me a verb ")
  verb2=input ("give me another verb ")
  verb3=input ("give me another verb ")
  adverb=input ("give me an adverb please ")
  #Print the story with the user supplied words.
  print ("legend has it that at the end of a rainbow lies a " + noun)
  print ("they say it contains copious amounts of " + noun2)
  print ("but it's not so easy, in order to reach it one must " + verb)
  print ("and one must " + verb2)
  print ("and do so " + adverb)
  print ("of course it is also guarded by a " + noun3)
  print ("so one must " + verb3)


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
