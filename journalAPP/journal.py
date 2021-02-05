import datetime

autoday = datetime.date.today().strftime('%m\%d\%y::')
autotime = datetime.datetime.now().strftime('%I:%M:%f') [:-2]



print("                             <|--Journal Entry--|>")

with open("./journalENTRIES/%s %s.txt" % (autoday, autotime),"x") as journal:
    for line in iter(input, ''):
        journal.write(line + '\n')

journal.close()
