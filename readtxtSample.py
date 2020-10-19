print ("Opening and closing the file")
text_file =open(r'G:\HEDIEUHANHTHOIGIANTHUC_RTOS\Thuctap\Python\RTOS_Week4\readme.txt')

data= text_file.readlines() #read first line
#data= text_file.readable() #co the read dc hay ko (true/false)
print(data)

text_file.close()