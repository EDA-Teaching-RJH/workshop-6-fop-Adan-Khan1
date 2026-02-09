def main():
    # ==========================================
    # Task 3.1: The Motor Controller (Try/Except)
    # ==========================================
    print("\n--- Task 3.1: Motor Controller ---")
    
    user_input = input("Enter Motor Speed (0-100): ")
    
    try:
        speed = int(user_input)
        print(f"Speed set to {speed}")
        
    except ValueError:
        print("Error: Corrupted Signal. Maintaining current speed.")


    # ==========================================
    # Task 3.2 & 3.3: The Persistent Receiver
    # ==========================================
    print("\n--- Task 3.2 & 3.3: Persistent Receiver ---")
    
    # calling the function defined below to test it
    valid_coordinate = get_coordinate()
    print(f"SUCCESS: Rover moving to X-Coordinate: {valid_coordinate}")


def get_coordinate():
    """
    Prompts user for a coordinate until a valid integer 
    within the safe range (-100 to 100) is entered.
    """
    while True:
        try:
            user_input = input("Enter X-coordinate (-100 to 100): ")
            
            number = int(user_input)
            
            # --- Task 3.3: Range Checks ---
            if number > 100 or number < -100:
                print("Coordinate out of range! Please try again.")
            
            else:
                return number

        except ValueError:
            print("Invalid coordinate. Please enter a number.")

if __name__ == "__main__":
    main()