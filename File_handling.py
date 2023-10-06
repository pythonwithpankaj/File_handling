## File Handling


# files -- data collection and can be stored with memory drive
# types of files:
                    # text file -- content in the form of text
                                   # notepad,word,excel,pdf.....etc
                    # binary files -- content in the form of numeric data 
                                      # image,videos,audios.....etc


## File Handling modes
                   # Read     --  'r'
                   # Write    --  'w'
                   # append   --  'a'
                   # create   --  'x'


# open("c:\\Users\\AI\\Desktop\\data1.txt")                          ## 1st 
# open("c:/Users/AI/Desktop/data1.txt")                              ## 2nd 
# f=open(r"C:\pankaj kumar")                                         ## 3rd
# print(f.read())
# print(f.readline())
# print(f.readlines())

# f=open("c:/pankaj kumar/data1.txt",mode='w')
# f.write("this is data sending from file handling file" )
# f.writelines()

# f=open("c:/pankaj kumar/data1.txt",mode='a')
# f.write("\nthis is data sending from file handling file" )

# f=open("c:/pankaj kumar/data1.txt",mode='wb')
# print(f.read())
# f.write(b'python')


# f=open("new.py")
# print(f.read())



# import os

#  os.mkdir("Ducat")
#  os.rmdir("Ducat")
#  print(os.path.exists("strings.py")         ## true and false