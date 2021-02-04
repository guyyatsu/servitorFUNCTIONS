from datetime import date
from os import system

#Environment Initialization

today = date.today().strftime('%m\%d\%y')
errorMSG = "ERROR! Please type a number"

def catLIST():
    return system("cat /var/spool/ToDoLists/'%s' | nl" % (today))

def initializer():

    try: system("mkdir /var/spool/ToDoLists")
    except: pass

    try: system("touch /var/spool/ToDoLists/%s" % (today))
    except: pass


def greeterBOT():

    printASCII()

    print()
    print('Would you like to:')
    print('    1.) Create a list for today.')
    print('    2.) Read the current list.')
    print('    3.) Add to the current list.')
    #UNDER CONSTRUCTION print('    4.) Check an item off the list.')

    try:
        selection = int(input('Type a number to make your selection: '))
        if selection == 1:
            return todoLISTER()
        elif selection == 2:
            return todoREADER()
        elif selection == 3:
            return todoADDER()
        elif selection == 4:
            return checkLISTER()
        else:
            print(errorMSG)
        return greeterBOT()

    except:
        KeyboardInterrupt


def printASCII():

    bannerEDGE = ('#' * 72)

    bannerDESCRIPTION = (str('#'*25) + "GUYYATSU'S TO-DO LIST" + str('#'*26))

    print(bannerEDGE)
    print(bannerDESCRIPTION)
    print(bannerEDGE)


def todoLISTER():
    def listCREATOR():
        return system("touch /var/spool/ToDoLists/%s" % (today))

    listCREATOR()

    with open("/var/spool/ToDoLists/%s" % (today), 'w') as lister:
        for line in iter(input, ''):
            lister.write(line + '\n')
        return


def todoADDER():
    with open("/var/spool/ToDoLists/%s" % (today), 'a') as adder:
        for line in iter(input, ''):
            adder.write(line + '\n')
        return


def todoREADER():
    return catLIST()

"""#UNDER CONSTRUCTION
def checkLISTER():
    def listCHECKER():

        with open('/var/spool/ToDoLists/%s' % (today)) as f:
            lines += f.read().splitlines()
            lineLIST = lines

        x = int(input('Type a number to make a selection: '))
        if isinstance(x, int) == True:
            lineLIST[(x-1)] += "    [CHECKED]"
            with open('/var/spool/ToDoLists/%s' % (today)), 'w' as f:
                f.write(lines)
                f.close()
                return
        else:
            print(errorMSG)
            return


    catLIST()
    checkLISTER()
"""

initializer()
greeterBOT()
