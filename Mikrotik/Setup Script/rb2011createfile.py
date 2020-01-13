import datetime
import random
import string

def createfile():

    customername = 'testcustomer'

    date= datetime.datetime.now()

    timestampStr = date.strftime("%d-%b-%Y")#(%H:%M:%S.%f)

    #print('Current Timestamp : ', timestampStr)

    filename = customername + timestampStr + '.txt'

    print(f"file name is {filename}")

    #filename = filename.replace(" ","")

    #print(f"{filename}")

    file1 = open(filename, 'a')
    file1.write(f'#filenameis "{filename}"')
    file1.close()

    return filename

x = createfile()


