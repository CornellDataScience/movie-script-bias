file = "practice.txt"

characters = ['Elsa','Anna', 'Olaf', 'Kristoff', 'Sven', 'Hans', 'Oaken', 'Duke']
f = open("scene1.txt","w")

# with open(file, "r") as txtFile:
#     lines = txtFile.readlines()
#     for line in txtFile:
#         if "EXT." in line or "INT." in line:
#             f.write(line)
#             print(line)

reader = open('practice.txt')
content = reader.readlines()


#print("length: ", len(content)-5)
for i in range(0,len(content)-2):
    print(content[i])
    if "EXT." in content[i] or "INT." in content[i]:
        print("inside if")
        f.write(content[i])
        i=i+1
    print(i)
    while("EXT." not in content[i] and "INT." not in content[i]):
        print("in while")
        f.write(content[i+1])
        i=i+1
    break
        #f.write(content[i]) # WRITE TO SCENE 1 TEXT FILE
          


# with open(file, "r+") as txtFile:
#     for line in txtFile:
#         if "EXT." in line or "INT." in line:
#             #f.write(txtFile.readline()())
#             print(txtFile.readline())
            
        # while("EXT." not in line and "INT." not in line):
        #     f.write(line)
        #     print(line)    



