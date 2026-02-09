# --- Part 5: Rover OS ---
print("--- Booting Rover OS v1.0 ---")

# 1. INITIALISE (Memory)
rover_status = {"Power": 100, "Samples": 0}

# List for storage
inventory = []

# 2. MAIN LOOP (The "Game Loop")
while True:
    print("\n---------------------------")
    print("ROVER MENU:")
    print("1. Dig for Sample")
    print("2. Report Status")
    print("3. Emergency Stop")
    print("---------------------------")
    
    # Get user choice
    user_choice = input("Select Option (1-3): ")
    
    # 3. LOGIC & ERROR HANDLING
    if user_choice == "1":
        # --- Option 1: Dig for Sample ---
        if rover_status["Power"] >= 10:
            sample_name = input("Enter sample name: ")
            
            inventory.append(sample_name)
            
            rover_status["Samples"] += 1       # Increase count
            rover_status["Power"] -= 10        # Decrease power
            
            print(f"Success! {sample_name} collected. Power consumed.")
        else:
            print("WARNING: Insufficient Power to dig.")
            
    elif user_choice == "2":
        print("\n--- SYSTEM REPORT ---")
        print(f"Status: {rover_status}")
        print(f"Inventory: {inventory}")
        
    elif user_choice == "3":
        print("Shutting down Rover OS...")
        break  
        
    else:
        print("ERROR: Invalid selection. Please enter 1, 2, or 3.")

print("Mission Complete.")