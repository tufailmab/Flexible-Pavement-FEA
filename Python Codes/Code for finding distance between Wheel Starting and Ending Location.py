# Make sure if you are using the scalled time you must scale the values in the Excel sheet of repititive cycles (Code is in the current section in next few lines)

def calculate_time(speed=203.166, distance=230):
    """Calculate the time taken to cover a given distance at a given speed."""
    time = distance / speed
    return time

while True:
    # Ask if the user wants to input new values or use defaults
    # Once the results are generated, then you can edit the protocols of loading in post processing as well
    user_input = input("Do you want to use the default values (Speed = 203.166 mm/sec, Distance = 230 mm)? (yes/no): ").strip().lower()

    if user_input == 'no':
        try:
            # Get user inputs
            speed = float(input("Enter speed in mm/sec (default is 203.166): ") or 203.166)
            distance = float(input("Enter distance in mm (default is 230): ") or 230)
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            continue
    else:
        speed = 203.166 #These are the default values, so don't worry about these values
        distance = 230  #These are the default values, so don't worry about these values

    # Calculate and display original and scaled-down time
    # Incase if you have a powerful computer, you don't need to scale down the speed and simulate it
    # You can do original speed as well (Apologies for gramatical mistakes)
    
    time = calculate_time(speed, distance)
    scaled_time = time / 10  # Time divided by 10

    print(f"Original time taken to cover {distance} mm at a speed of {speed} mm/sec is approximately {time:.3f} seconds.")
    print(f"Scaled time (divided by 10) is approximately {scaled_time:.3f} seconds.")

    # Ask if the user wants to repeat
    repeat = input("Do you want to calculate again? (yes/no): ").strip().lower()
    if repeat != 'yes':
        break

print("Thank you for using the calculator!")
