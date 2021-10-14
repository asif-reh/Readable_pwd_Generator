import random

word_list=[]
special_char=['@','#','$','&','^']

with open("wikipedia-text.txt", 'r') as file:
    data = file.readlines()
    
    for line in data:
        words=line.split()

        for item in words:
            if len(item) > 5:
                word_list.append(item.capitalize())

word=random.choice(word_list)
schar=random.choice(special_char)
num=str(random.randint(10,99))
password=word+schar+num
print(password)