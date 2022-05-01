from nltk.corpus import names 
# print("\nNumber of male names:")
# print (len(names.words('male.txt')))
# print("\nNumber of female names:")
# print (len(names.words('female.txt')))
male_names = names.words('male.txt')
female_names = names.words('female.txt')
# print("\nFirst 10 male names:")
# print (male_names[0:15])
# print("\nFirst 10 female names:")
# print (female_names[0:15])

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
    #print(content[i])
    # for word in content[i].split():
    #     print(word)
    #     if word in male_names:
    #         print("MALE"+word)
    #     if word in female_names:
    #         print("FEMALE" + word)
    #print(content[i])
    if "EXT." in content[i] or "INT." in content[i]:
        #print("inside if")
        f.write(content[i])
        i=i+1
    #print(i)
    male_count=0
    female_count=0
    while("EXT." not in content[i] and "INT." not in content[i]):
        #print("in while")
        for word in content[i].split():
            #print(word)
            if word in male_names:
                #print("MALE: "+word)
                male_count+=1
                # print("male name counter:")
                # print(m)
            if word in female_names:
                #print("FEMALE: " + word)
                female_count+=1
                # print("female name counter")
                # print(f)
        f.write(content[i+1])
        i=i+1
    break
total = male_count+female_count
print("Male proportion: ",male_count/total)
print('Female proportion: ',female_count/total)
        #f.write(content[i]) # WRITE TO SCENE 1 TEXT FILE
          


# with open(file, "r+") as txtFile:
#     for line in txtFile:
#         if "EXT." in line or "INT." in line:
#             #f.write(txtFile.readline()())
#             print(txtFile.readline())
            
        # while("EXT." not in line and "INT." not in line):
        #     f.write(line)
        #     print(line)    



