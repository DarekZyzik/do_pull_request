from funkcje import *
path = '//home//daro//Python//git3//do_pull_request//rolling_stones.txt'
with open (path, 'r') as file:
  content = file.readlines()
  content2 = file.read()

#funkcja usuwająca puste linie   "usun_puste"
content_bez_pustych = usun_puste(content)
print(content_bez_pustych)

# #funkcja licząca ilość wystapień litery "a"     "ile_a"
print('Litera "a" wystepuje ', ile_a(content),' razy')
#
#funkcja licząca ilość wystapień wskazanej litery     "ile"
x = input('podaj liczbe do policzenia: ')
print('Litera ' ,x, ' wystepuje ', ile(content, x),' razy')
#
#funkcja biorąca "content" i zapisująca wszystkie linie w jednej liście     "razem"
content_razem = razem(content)
print(content_razem)