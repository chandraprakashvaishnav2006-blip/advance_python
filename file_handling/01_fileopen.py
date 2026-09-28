# try:
#     f=open("abczy.txt",'r')
#     content=f.read()
#     print(content)
#     f.close()
# except FileNotFoundError:
#     print("File not found.")





# Reading line by line
j=0
try:
    f = open("abcz.txt", "r")
    for line in f: # Efficient for large files
        print(line.strip()) # Remove newline characters
        j+=1
    print(f"Total lines read: {j}")    
    f.close()
except FileNotFoundError:
    print("File not found.")
 