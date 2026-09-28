try:
    with open("abczz.txt",'x') as f:
        f.write("Hello, World!\n")
except FileNotFoundError:
    print("File not found.")        