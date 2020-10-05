import os
from first_run import firstRun

def main():
    print('------Welcome To Library Management System------')
    if os.path.exists('AppDetails') and os.path.exists('adminArea') and os.path.exists('booksArea') and os.path.exists('membersZone') and os.path.exists('bookIssue'):
        print("W")
    else:
        print("It seems that you are using this app for the first time so you have to start setup by pressing 'f' or \nyour Library Management System requires a repair so press 'F' to repair.\nNote:This repair will delete all data and reset settings to default.")
        stp_ch = input('>> ').lower()
        if stp_ch=='f':
            firstRun()
if __name__ == "__main__":
    main()