'''
you will have to install pywhatkit python package using cmd
wih this command pip install pywhatkit
Make sure python is added to the path (environment variables)
'''
import pywhatkit as pwk
import pyautogui as pag

class Details:

    def attendance (self):
        self.name = input("Enter the attendees name:")
        self.gender = input("Enter the gender:")
        self.phone = input("Enter the phone number(along with ISD code):")
        self.email = input("Enter the email address:")
        self.attendance = float(input("Enter the attendance:"))

class Attendance (Details):

    def receive_attnd (self):

        det = [
            "Name: %s"%(self.name), "Gender: %s"%(self.gender), "Phone: %s"%(self.phone), "Email: %s"%(self.email), "Attendance: %.2f"%(self.attendance)
        ]
        self.message = "\n".join(det)

        if (self.attendance < 75):
            self.msg = self.message + "\n\nThe attendance is low!"
        else:
            atnd_msg = "Your attendance is up to date!"
            self.msg = self.message + "\n\nThe attendance is up to date!"

        print("\n%s" %self.msg)


    def send_message (self):
        pwk.sendwhatmsg_instantly(self.phone, "Attendance Report:\n%s"%self.msg)
        for i in range(1):
            pag.press('enter')


adtc = Attendance()
adtc.attendance()
adtc.receive_attnd()
adtc.send_message()
