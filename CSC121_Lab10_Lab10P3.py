time = input("Enter time [hh:mm:ss]: ")
time = time.strip()
if time.count(":") != 2:
    print("Must separate hour, minute and second with colons.")
else:
    time_list = time.split(":")
    if time_list[0].isdigit() == False or len(time_list[0]) != 2:
        print("Hour Must be a 2-digit number.")
    elif time_list[1].isdigit() == False or len(time_list[1]) != 2:
        print("Minute must be a 2-digit number.")
    elif time_list[2].isdigit() == False or len(time_list[2]) != 2:
        print("Second must be a 2-digit number.")
    elif int(time_list[0]) < 0 or int(time_list[0]) > 23:
        print("Hour must be a 2-digit number between 0 and 23.")
    elif int(time_list[1]) < 0 or int(time_list[1]) > 59:
        print("Minute must be a 2-digit number between 0 and 59.")
    elif int(time_list[2]) < 0 or int(time_list[2]) > 59:
        print("Second must be a 2-digit number between 0 and 59.")
    else:
        time = time.replace(":", "")
        print("Time with colons removed:", time)

