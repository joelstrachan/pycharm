

filename1 = 123

def createfile(filename1):
    import datetime


    customername = 'testcustomer'

    date = datetime.datetime.now()

    timestampStr = date.strftime("%d-%b-%Y")#(%H:%M:%S.%f)

    #print('Current Timestamp : ', timestampStr)

    filename1 = customername + timestampStr + '.txt'

    #print(f"file name is {filename}")

    #filename = filename.replace(" ","")

    print(f"{filename1}")

    file1 = open(filename1, 'a')
    #file1.write(f'#{filename1}')
    #file1.write(f'#test')
    file1.close()

    return filename1

#filename =
filename = createfile(filename1)

file1 = open(filename, 'a')
file1.write(f'#{filename}')
file1.write(f'#test')
file1.close()






