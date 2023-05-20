#Write a function named right_justify that takes a string named s as a parameter. Using string concatenation and repetition 

def right_justify(s):
    spaces = " "*(70-len(s)) #70 spaces and substracting of string length 
    justify_right= spaces + s #add the string length 
    print(justify_right)

right_justify('Samantha')
            