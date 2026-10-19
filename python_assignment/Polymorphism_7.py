# Task 1
# class InsaStory:
#     def share(self):
#         print("Sharing an image story")
# class WhatsAppStory(InsaStory):
#     def share(self):
#         print("Sharing a text status")
# i=InsaStory()
# i.share()
# w=WhatsAppStory()
# w.share()


# Task 2
# class Payment:
#     def pay(self,amount):
#         print("Paying amount:",amount)
# class UPI(Payment):
#     pass
    # def pay(self,amount):
    #     print("Paying amount via UPI:",amount)

# payment=Payment()
# upi=UPI()
# payment.pay(100)
# upi.pay(100)

# Task 3
# class ZomatoOrder:
#     def add_item(self,item,quantity=1):
#         print("Added",quantity,item)
#
# z=ZomatoOrder()
# z.add_item("Pizza")
# z.add_item("Burger",3)


# Task 4
class Content:
    def display(self,title):
        print("Title:",title)
class Movie(Content):
    def display(self,title,year):
        print("Title:",title)
        print("Year:",year)
m=Movie()
m.display("Jean",2000)

# Task 5
class Notification:
    def send(self):
        print("Sending notification")
class EmailNotification(Notification):
    def send(self):
        print("Sending email notification")
class SMSNotification(Notification):
    def send(self):
        print("Sending SMS notification")
notification=Notification()
email=EmailNotification()
sms=SMSNotification()
notification.send()
email.send()
sms.send()










