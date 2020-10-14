import adminMaster,bookMaster,memberMaster

def MasterMain(admin_logged):
    """
    Main Master Head
    """
    print(f'\n\nWelcome To Master {admin_logged}')
    while True:
        mas_ch = ''
        while type(mas_ch) != int:
            try:
                mas_ch = int(input('''\n\nPress
                1 for Book Master
                2 for Member Master
                3 for Admin Master
                4 to exit\n>> '''))
            except Exception:
                print('\nInvalid Choice!!\n')
        if mas_ch == 1:
            bookMaster.Master(admin_logged)
            continue
        elif mas_ch == 2:
            memberMaster.Master(admin_logged)
            continue
        elif mas_ch == 3:
            adminMaster.Master(admin_logged)
            continue
        elif mas_ch == 4:
            break
        else:
            print('\nInvalid Choice!!\n')


if __name__ == "__main__":
    MasterMain('abbas')
