sec = int(input('Enter the number of seconds since midnight: '))
if sec < 3600:
    mins = sec // 60
    secs = sec - mins*60
    print ('The time is: 12:', mins, ":", secs, 'AM')
elif sec < 43200:
    hrs = sec // 3600
    mins = sec // 60 - hrs*60
    secs = sec - hrs*3600 - mins*60
    print('The time is:',hrs,":",mins,":",secs,'AM')
elif sec < 46800:
    hrs = sec // 3600
    mins = sec // 60 - hrs*60
    secs = sec - hrs*3600 - mins*60
    print('The time is:',hrs,":",mins,":",secs,'PM')
elif sec > 46800:
    sec = sec - 43200
    hrs = sec // 3600
    mins = sec // 60 - hrs*60
    secs = sec - hrs*3600 - mins*60
    print('The time is:',hrs,":",mins,":",secs,'PM')

