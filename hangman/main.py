from words import word
import random
import os
print("Welcome To Hangman Game")
print("""Rules:
1.The Word to be guessed is randomly generated
2.The total attempts to guess the letter are 6.
3.Every time you guess wrong your one attempt will be deducted""")
ch = 1
while ch == 1:
    atmpt = 6
    w_mn = word()
    #w_mn = "aapple"
    ps = ""
    ges_lst = [" "]
    for i in range(len(w_mn)):
        ps += "_"
    lst_wrd = list(w_mn)
    lst_dash = list(ps)
    #print(w_mn)
    while atmpt >0:
        print(" ")
        wrd = ""
        for f in lst_dash:
            wrd += " "+f
        print("""Word: {}
No. of attempts left: {}
Previous Guess: {}""".format(wrd,atmpt,ges_lst[-1]))
        ges = input("Enter Letter: ")
        if ges in ges_lst:
            print(ges,"is already guessed")
            atmpt -= 1
        else:
            cnt = lst_wrd.count(ges) 
            if cnt>1:
                lst_wrd2 = list(w_mn)
                atoz=["a","b","c"]
                lst2=[]
                co=[]
                h=lst_wrd2.index(ges)
                co.append(h)
                lst2.append(ges)
                while True:
                    if ges in lst_wrd2 and ges in lst2: 
                        yy=lst_wrd2.index(ges)
                        lst_wrd2[yy]=random.choice(atoz)
                        if ges in lst_wrd2:
                            b=lst_wrd2.index(ges)
                            co.append(b)
                        else:
                            break
                for z in co:
                    lst_dash[z] = ges     
            else:
                if ges in lst_wrd:
                    z = lst_wrd.index(ges)
                    lst_dash[z] = ges
                else:
                    print(ges,"is not in word")
                    atmpt-=1
        ges_lst.append(ges)
        #print(lst_dash,lst_wrd)
        if lst_dash==lst_wrd:
            print("You Guessed The Write Word")
            break
        else:
            continue
    else:
        print("Better luck next time!!")
        print("The word was :{}".format(w_mn))
    ch = int(input("\n\nWanna Play Again? Press 1 for Yes and 0 For No: "))
os.system("ls")
