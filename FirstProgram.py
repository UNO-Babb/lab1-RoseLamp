#FirstProgram.py
#Name:
#Date:
#Assignment:

def main():
  print("First Program")
  #Say hello
  print ("Hello")
  #Ask for the user's name
  name=input ("what is your name? ")
  #Use the user's name in the program.
  print("hello " + name)
  #Ask the user for their age.
  age=int(input ("How young are you? ")) 
  #Tell the user what year they were born in.
  year=2024
  birth_year= (year-age)
  print ("you were born in " + str(birth_year))
  #Assume that they have not had their birthday yet this year.


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
