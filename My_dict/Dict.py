import requests
from bs4 import BeautifulSoup
import csv
import sys

def dictionary():
    FFF = 'My_dict/dict.csv'
    print('=========================')
    print('~How can I help you?~')
    print('=========================')

    print('a: Show me the word list of the dictionary')
    print('b: Let me use the dictionary')
    mode = input("a or b:")
    if mode == 'a':
        with open(FFF) as f:
            reader = csv.reader(f)
            word_list=[]
            for row in reader:
                word_list.append(row[0])
            word_list.sort()
            print('=========================')
            for i in range(len(word_list)):
                print(word_list[i])

            print('=========================')
    elif mode == 'b':
        print('What word would you like to know its meanings?')

    #検索する単語を入力
    word = input("search word:")
    

    #単語が保存されているリストファイルを開く
    try:
        with open(FFF) as f:
            reader = csv.reader(f)
            l = [row for row in reader]
    except:
        print("Listfile doesn't exist")
        exit(1)

    #すでに保存されている単語かどうかチェック
    for exist_word in l:
        if exist_word[0] == word:
            exist_word_verif = input("This word is already registered. Check mean? y/n:")
            if exist_word_verif == "n":
                sys.exit(0)
            elif exist_word_verif == "y":
                print(exist_word[1])
                sys.exit(0)
            else:
                print("Please input y or n. Start again.")
                sys.exit(1)


    #リストファイルに追加するかどうか選択
    append_or_not = input("append y/n:")


    if append_or_not == "y":
        word_mean = input("Write down the meanings:")
        data = [word, word_mean]
        with open(FFF, 'a') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(data)         
