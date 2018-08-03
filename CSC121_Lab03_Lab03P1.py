hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))
second = int(input("Enter second: "))
am_pm = input("Enter AM or PM: ")
am_pm = am_pm.upper()
if hour == 12:
    hour = hour - 12
if am_pm == "PM":
    hour = hour + 12
seconds_midnight = hour * 3600 + minute * 60 + second
print("Seconds since midnight: ", seconds_midnight)

