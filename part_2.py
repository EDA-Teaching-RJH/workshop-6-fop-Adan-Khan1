# --- Task 2.1: System Status ---
print("\n--- Task 2.1: Initial System Check ---")

# 1. Create the dictionary with labels (Keys) and data (Values)
rover_status = {
    "Battery": 100,
    "Heater": "Off",
    "Camera": "Standby"
}

# 2. Print the Battery status by accessing the Key
print(f"Current Battery Level: {rover_status['Battery']}%")


# --- Task 2.2: Status Update ---
print("\n--- Task 2.2: Update ---")

# 1. Update Battery to 85
rover_status["Battery"] = 85

# 2. Update Heater to "On"
rover_status["Heater"] = "On"

# 3. Add a NEW key-value pair for Speed
rover_status["Speed"] = 5

# 4. Print the entire dictionary to verify structure
print("Updated Rover Status:", rover_status)


# --- Task 2.3: The Science Log (Nesting) ---
print("\n--- Task 2.3: Mission Log Analysis ---")

# 1. Create a List called mission_log
# 2. Store two Dictionaries inside the list
mission_log = [
    {"Site": "Crater A", "Radiation": "Low", "Water": False},
    {"Site": "Dune B", "Radiation": "High", "Water": True}
]

# 3. Challenge: 
for site in mission_log:
    name = site["Site"]
    rad_level = site["Radiation"]
    
    print(f"Site {name} has {rad_level} radiation.")