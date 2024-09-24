from adafruit_circuitplayground import cp

while True:

    blue = (0, 0, 255)
    off = (0, 0, 0)

    # Prompt user for the number of LEDs
    try:
        num_leds = int(input("Enter the number of LEDs to switch on (1-10): "))
    except ValueError:
        print("Inserted value is not a number.")
        continue
    
    # Check if the number is within the valid range
    if 1 <= num_leds <= 10:

        # Set all LEDs to zero to start, in case user restarts
        for j in range(0, 10):
            cp.pixels[j] = off

        # Turn on LEDs using a for loop
        for i in range(0, num_leds):
            print("LED {} is ON".format(i))
            cp.pixels[i] = blue
    else:
        print("Number out of range. Please enter a number between 1 and 10.")
        continue
    
    # Prompt if user wants to start again
    restart = input("Do you want to start again? (n to stop, any other key to continue): ").lower()
    if restart == 'n':
        print("Program ended.")
        break