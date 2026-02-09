# --- Task 4.1: Implementation ---
print("--- Automated Navigation System Initialised ---")

# 1. INITIALISE: Create an empty list for the log
travel_log = []

# 2. LOOP: Start continuous monitoring
while True:
    # 3. INPUT: Ask for sensor reading
    user_input = input("\nSensor Reading (Slope Angle): ")
    
    # 4. VALIDATION (Try/Except)
    try:
        # Try to convert string input to an integer
        angle = int(user_input)
        
        # 5. SAFETY CHECK (If/Else)
        # Check for critical tilt (Logic Step 6)
        if angle > 45:
            print("CRITICAL TILT! HALTING.")
            break # STOP LOOP immediately
        
        # 6. LOGGING & OUTPUT
        travel_log.append(angle)
        print(f"Path Stable (Angle: {angle}). Moving forward.")
        
    except ValueError:
        print("Sensor Glitch: Invalid input detected. Retrying...")


# --- Task 4.2: Mission Report ---
print("\n--- Mission Report ---")
print("Mission Terminated.")

print(f"Total steps taken: {len(travel_log)}")

print(f"Full Travel Log: {travel_log}")