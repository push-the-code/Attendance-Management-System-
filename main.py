class Details:
    
    def attendance (self):
        name = input("Enter the attendees name:")
        gender = input("Enter the gender:")
        phone = int(input("Enter the phone number:"))
        email = input("Enter the email address:")
        self.attendance = float(input("Enter the attendance:"))
        
class Attendance (Details):
    
    def receive_attnd (self):
        if (self.attendance < 75):
            print ("The attendance is low!")
        else:
            print ("Attendance is up to date!")

adtc = Attendance()
adtc.attendance()
adtc.receive_attnd()
