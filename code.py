import random
from typing import List
import easygui as gui

file1 = open("movie_list.txt", 'a')
option = gui.buttonbox("                 Welcome to Movie-Tron. What would you like to do? ", "", ['Add Movies', '  Get Movie  ', '       Exit       '])
add_more = '1'

if option == 'Add Movies':
    while add_more == '1':
        file1 = open("movie_list.txt", 'a')
        movie_add = gui.enterbox('Movie Title: ')
        file1.writelines(movie_add + "\n")
        if movie_add == 'cancel':
            exit()
    file1.close()

elif option == '  Get Movie  ':
    file1 = open("movie_list.txt", 'r')
    reading = file1.readlines()
    content: List[str] = []
    for x in reading:
        content.append(x.strip())

    fname = "movie_list.txt"
    count = 0
    with open(fname, 'r') as f:
        line: str
        for line in f:
            count += 1
    rand_movie_choice = random.randint(0, count - 1)

    if rand_movie_choice == 'Marmaduke':
        rand_movie_choice = random.randint(0, count - 1)
        # Chooses other movie is the movie is Marmaduke
    movie_give = gui.msgbox('The Chosen Movie is:' + content[rand_movie_choice])
    file1.close()

elif option == '       Exit       ': # This Does Stuff
    exit()
