#การเขียนโปรแกรมแบบทำซ้ำโดยการถามตอบ
yesno = "y"
while (yesno =="y") :
    w = int(input("ป้อนความกว้าง ? "))
    h = int(input("ป้อนความยาว ? "))
    print("พื้นที่ = "+str(w*h))
    yesno = input("คำนวณต่อหรือไม่ ? [y/n]")
    