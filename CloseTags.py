import re

#Ввод текста
String = input()

#Флажок
f = 0

Tags = ''
ExitTags = ''

#Цикл для дого чтобы убрать все лишнее кроме тэгов
for i in String:
    if i == '>':
        Tags = Tags + i
        f = 0
    if f == 1:
        Tags = Tags + i
    if i == '<':
        Tags = Tags + i
        f = 1

#print(Tags)    

#Цикл для того чтобы определить каких "закрытых" тегов не хватает
while Tags != '':
    OpenTag = ''
    CloseTag = ''
    for i in Tags:
        if i == '>':
            OpenTag = OpenTag + i
            f = 0
            break
        if f == 1:
            OpenTag = OpenTag + i
        if i == '<':
            OpenTag = OpenTag + i
            f = 1
        if i == '/':
            f = 0
            OpenTag = ''
            break

    #print(OpenTag)

    for i in OpenTag:
        if i == '>':
            CloseTag = CloseTag + i
            f = 0
            break
        if f == 1:
            if i != ' ':
                CloseTag = CloseTag + i
            else:
                CloseTag = CloseTag + '>'
                f = 0
                break
        if i == '<':
            CloseTag = CloseTag + i + '/'
            f = 1

    #print(CloseTag)

    Tags = re.sub(OpenTag, '', Tags, count=1)

    if CloseTag in Tags:
        Tags = re.sub(CloseTag, '', Tags, count=1)
    else:
        #Исключения
        if CloseTag == "</br>":
            continue
        elif CloseTag == "</img>":
            continue
        else:
            ExitTags = CloseTag + ExitTags

print(ExitTags)