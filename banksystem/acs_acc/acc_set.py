from settings import chng_name,chng_mob,chng_pass


def setting(act_no):
    set_opt = 0
    while set_opt != 4:
        print(
            'Following Settings Are Available For Your Account:\n1.Change Name\n2.Change Mobile No.\n3.Change Passowrd\n4.Go Back')
        set_opt = int(input('Your Selection >> '))
        if set_opt == 1:
            chng_name.name_change(act_no)
            #break
        elif set_opt == 2:
            chng_mob.mobile_change(act_no)
            #break
        elif set_opt == 3:
            chng_pass.password_change(act_no)
            #break
        elif set_opt == 4:
            print('Thanks')
        else:
            print('Wrong choice')
            break


