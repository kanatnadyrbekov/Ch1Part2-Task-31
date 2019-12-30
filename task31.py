# Напишите функцию которая подсчитает количество строк, слов и букв в текстовом
# файле.
text = """Hello my name is Kanat, and I study in Maker's course
mjdbvzjk zkjvasukz ksbvzu ubvu jbvab ajbvuzb """
string = text.count("\n")
print(f"Text has: {string + 1} string")
words = ' '
a = text.count(words)+1
print(f"Text has: {a} words")
letter = len(text)-a +1
print(f"Text has: {letter} letters")




