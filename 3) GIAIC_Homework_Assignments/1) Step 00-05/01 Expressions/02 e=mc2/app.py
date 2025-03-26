# speed of light in meters per second
C = 299792458

while True:
    try:
        mass_in_kg = float(input("Enter mass in kilograms (or type 'exit' to quit): "))
        
        # Calculate energy using Einstein's formula
        energy_in_joules = mass_in_kg * C**2
        
        # Display the calculation to the user
        print("e = m * C^2...")
        print("m = " + str(mass_in_kg) + " kg")
        print("C = " + str(C) + " m/s")
        print(str(energy_in_joules) + " joules of energy!")
    except ValueError:
        print("Invalid input. Please enter a valid number for mass or type 'exit' to quit.")
    except KeyboardInterrupt:
        print("\nExiting program. Goodbye!")
        break