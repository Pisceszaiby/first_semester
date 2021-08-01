def conversion(dictionary,phrase):#Function for conversion of characters in the string(phrase)
    for i in phrase: #Each character in the string will be assessed
        if i in dictionary.keys():#Likewise if i which is character in string matches any key 
            print(dictionary[i],end='')   # then the value of key will be printed            
        else:
            print(i,end='') #if it does not match then the original character will be printed
def freq_table(dictionary,key,phrase):#For frequency/rule table
    frequency=0
    print("\nRULE\tFREQUENCY")
    for i in key: #i starts from the first element to the last element of the key list
        for j in phrase:# j starts from the first character to the last character in the string phrase
            if i==j:#if j matches I (ascending order)
                frequency+=1#frequency is added by 1
        if frequency>0:#will count frequency only greater than 0
            print(i,"→",dictionary[i],"\t  ",frequency) # i (key) will points to its value for showing rule, and frequency will be printed too
        frequency=0#for other characters
def encryption(dictionary,phrase,key):
    print("Encrypted Text: ",end="")
    conversion(dictionary,phrase)
    freq_table(dictionary,key,phrase) #Function encryption will use both frequency table and conversion functions
def decryption(dictionary,phrase,key):
    print("Decrypted Text: ",end="")
    conversion(dictionary,phrase)
    freq_table(dictionary,key,phrase) #Function decryption will use both frequency table and conversion functions  
enc_dict={'1':'5','3':'7','5':'9','7':'1','9':'3','a':'i','b':'m','d':'t','e':'o','g':'b','i':'u','m':'d','o':'a','t':'g','u':'e'}
dec_dict={'1':'7','3':'9','5':'1','7':'3','9':'5','a':'o','b':'g','d':'m','e':'u','g':'t','i':'a','m':'b','o':'e','t':'d','u':'i'}
#enc_dict and dec_dict are the dictionaries for ecrytion, decryption respectively
#dec_dict is organized from key 1 to 9 and a to u by inverting keys into values of enc_dict
keys1=enc_dict.keys() #keys of enc_dict will be stored in the list keys1
keys2=dec_dict.keys() #keys of dec_dict will be stored in the list keys2
text=input("Enter Any Phrase: ")
print("Original Text: ",text)
print("Select any option:\ne-ENCRYPTION\nd-DECRYPTION\nx-EXIT") #Menu
option=input("Your Selection: ")
if option=='e':
    print("\tENCRYPTION") 
    encryption(enc_dict,text,keys1)#encryption function will be called
elif option=='d':
    print("\tDECRYPTION")
    decryption(dec_dict,text,keys2) #decryption function will be called
elif option=='x':
    print("\tEXIT")
    exit()
    

    
   
