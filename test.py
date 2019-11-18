def character_range(char1, char2):
	for char in range(ord(char1),ord(char2)+1):
		yield (char)

def clr():
        print('\n' * 10)
print('Welcome!')
mainxmenu = 0
mm = ('1. Tests', '2. Projects', '3. Exit program')
gp = ('1.1 Students List','1.2 Add grade','1.3 Back to main menu')
pp = ('2.1 Students List','2.2 Add Score','2.3 Back to main menu')
while(mainxmenu<1):   # main menu loop
        testxmenu = 0
        projectxmenu = 0
        for item in mm:
                print(item)      # show list
        mainmenu = input ('Select: ')    #select from list
        clr()                                                # clear screen
        if mainmenu == '1':                    # if selected 1. Tests
                while(testxmenu<1):
                        print(mm[0] + " :")
                        for item in gp:
                                print(item)
                        testmenu = input ('Select: ')
                        clr()
                        if testmenu == '1':
                                f = open('SCHOOL\students_id.txt','r')
                                studentid=f.read()
                                print(studentid)
                                f.close()
                                back = input (' Press any key to back Tests ')
                                clr()
                        if testmenu == '2':
                                sidd=0
                                while(sidd<1):
                                        sid = input ( 'Student ID: ')
                                        if sid != '1' and sid != '2':
                                                clr()
                                                print('ID doesnt exist, try again \n')
                                        else:
                                                sidd=1
                                if sid == '1':
                                        date=0
                                        while(date<1):
                                                print('Insert date: \n')
                                                day = int(input (' Day (1-31):  '))
                                                month = int(input ('Month (1-12): '))
                                                year = int(input ('Year (yyyy): '))
                                                if day in range(1,32) and month in range(1,13) and len(str(year))==4:
                                                        date=1
                                                else:
                                                        print('\n\nWrong date!\n' )
                                        testnumber = input (' Test number: ')
                                        gradee = 0
                                        check = 0
                                        while(gradee<1):
                                                grade = input ('grade (A-F): ')
                                                for letter in character_range('A','F'):
                                                        if grade == chr(letter):
                                                                check = 1
                                                                gradee = 1
                                                if check == 0:
                                                        print('Grade need to be from A to F!')

                                                
                                        a = open('SCHOOL\wynik1.txt','a+')
                                        a.write('\n' + str(day)+'-'+ str(month)+'-'+ str(year)+ '  |  ' + testnumber + '  |  ' + grade)
                                        a.close()
                                        back = input ('Data saved, press any key to continue')
                                        clr()
                                if sid == '2':
                                        date=0
                                        while(date<1):
                                                print('Insert date: \n')
                                                day = int(input (' Day (1-31):  '))
                                                month = int(input ('Month (1-12): '))
                                                year = int(input ('Year (yyyy): '))
                                                if day in range(1,32) and month in range(1,13) and len(str(year))==4:
                                                        date=1
                                                else:
                                                        print('\n\nWrong date!\n' )
                                        testnumber = input (' Test number: ')
                                        gradee = 0
                                        check = 0
                                        while(gradee<1):
                                                grade = input ('grade (A-F): ')
                                                for letter in character_range('A','F'):
                                                        if grade == chr(letter):
                                                                check = 1
                                                                gradee = 1
                                                if check == 0:
                                                        print('Grade need to be from A to F!')

                                                        
                                        a = open('SCHOOL\wynik2.txt','a+')
                                        a.write('\n' + str(day)+'-'+ str(month)+'-'+ str(year)+ '  |  ' + testnumber + '  |  ' + grade)
                                        a.close()
                                        back = input ('Data saved, press any key to continue')
                                        clr()
                        if testmenu == '3':
                                testxmenu=2
                        if testmenu != '1' and testmenu != '2' and testmenu !='3':
                                print('Select number from 1 to 3! \n\n')  # FINISH 'TESTS' MENU
        if mainmenu == '2':                    # if selected 2. Projects
                while(projectxmenu<1):
                        print(mm[1] + " :")
                        for item in pp:
                                print(item)
                        projectmenu = input ('Select: ')
                        clr()
                        if projectmenu == '1':
                                f = open('SCHOOL\students_id.txt','r')
                                studentid=f.read()
                                print(studentid)
                                f.close()
                                back = input (' Press any key to back Project')
                                clr()
                        if projectmenu == '2':
                                sidd=0
                                while(sidd<1):
                                        sid = input ( 'Student ID: ')
                                        if sid != '1' and sid != '2':
                                                clr()
                                                print('ID doesnt exist, try again \n')
                                        else:
                                                sidd=1
                                if sid == '1':
                                        date=0
                                        while(date<1):
                                                print('Insert date: \n')
                                                day = int(input (' Day (1-31):  '))
                                                month = int(input ('Month (1-12): '))
                                                year = int(input ('Year (yyyy): '))
                                                if day in range(1,32) and month in range(1,13) and len(str(year))==4:
                                                        date=1
                                                else:
                                                        print('\n\nWrong date!\n' )
                                        projectname = input (' Project name: ')
                                        check = 0
                                        while(check<1):
                                                score = int(input ('score (0-100): '))
                                                if score <101 and score >= 0:
                                                        check = 1
                                                else:
                                                        print(' Score need to be from 0 to 100!')

                                                
                                        a = open('SCHOOL\projects1.txt','a+')
                                        a.write('\n' + str(day)+'-'+ str(month)+'-'+ str(year)+ '  |  ' + projectname + '  |  ' + str(score))
                                        a.close()
                                        back = input ('Data saved, press any key to continue')
                                        clr()
                                if sid == '2':
                                        date=0
                                        while(date<1):
                                                print('Insert date: \n')
                                                day = int(input (' Day (1-31):  '))
                                                month = int(input ('Month (1-12): '))
                                                year = int(input ('Year (yyyy): '))
                                                if day in range(1,32) and month in range(1,13) and len(str(year))==4:
                                                        date=1
                                                else:
                                                        print('\n\nWrong date!\n' )
                                        projectname = input (' Project name: ')
                                        check = 0
                                        while(check<1):
                                                score = int(input ('score (0-100): '))
                                                if score <101 and score >= 0:
                                                        check = 1
                                                else:
                                                        print(' Score need to be from 0 to 100!')

                                                        
                                        a = open('SCHOOL\projects2.txt','a+')
                                        a.write('\n' + str(day)+'-'+ str(month)+'-'+ str(year)+ '  |  ' + projectname + '  |  ' + str(score))
                                        a.close()
                                        back = input ('Data saved, press any key to continue')
                                        clr()
                                if sid != '1' and sid != '2':
                                        clr()
                                        print('ID doesnt exist, try again \n \n')
                        if projectmenu == '3':
                                projectxmenu=2
                        if projectmenu != '1' and projectmenu != '2' and projectmenu !='3':
                                print('Select number from 1 to 3! \n\n')  # FINISH 'PROJECT' MENU
        if mainmenu =='3':
                mainxmenu=2
        if mainmenu != '1' and mainmenu != '2' and mainmenu !='3':
                print('Select number from 1 to 3! \n\n')

                
                                
                                        
                        
                
