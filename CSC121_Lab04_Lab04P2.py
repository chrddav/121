hour = int(input("Enter hour: "))
while hour > 12 or hour < 1:
    print('Error: hour mst be a number from 1 to 12.')
    hour = int(input('Enter hour: '))
minute = int(input("Enter minute: "))
while minute > 59 or minute < 0:
    print('Error: minute must be a number from 0 to 59.')
    minute = int(input('Enter minute: '))
second = int(input("Enter second: "))
while second > 59 or second < 0:
    print('Error: seconds mst be a number from 0 to 59.')
    second = int(input('Enter second: '))
am_pm = input("Enter AM or PM: ")
while am_pm not in ('AM', 'PM'):
    print("Error: Must be AM or PM")
    am_pm = input("Enter AM or PM:")
am_pm = am_pm.upper()
if hour == 12:
    hour = hour - 12
if am_pm == "PM":
    hour = hour + 12
seconds_midnight = hour * 3600 + minute * 60 + second
print("Seconds since midnight: ", seconds_midnight)
