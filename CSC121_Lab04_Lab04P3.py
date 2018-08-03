initial = float(input("Enter initial height: "))
bounce_index = float(input("Enter bounciness index: "))
bounces = int(input("Enter the number of times the ball is allowed to bounce: "))
iterations = 0
while iterations < bounces:
    height = initial * (bounce_index**(iterations+1))
    iterations = iterations +1
    print("Number of bounces:", iterations, "Height: ", height)

