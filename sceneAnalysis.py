file = "movie-scripts/practice.txt"

characters = ['Elsa','Anna', 'Olaf', 'Kristoff', 'Sven', 'Hans', 'Oaken', 'Duke']
f = open("movie-scripts/scene1.txt","w")

reader = open('movie-scripts/practice.txt')
content = reader.readlines()

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