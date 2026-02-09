# --- Task 1.1: The Storage Bay ---
# Creating the initial list of samples
sample_bay = ["Basalt", "Silica", "Iron", "Dust"]

# Accessing items via indexing
print(f"First item: {sample_bay[0]}")
print(f"Last item: {sample_bay[-1]}")
print(f"Total samples in bay: {len(sample_bay)}")


# --- Task 1.2: Analysing Samples (Iteration) ---
print("\n--- Starting Transmission ---")
# Direct iteration over the list items as per the Tip
for rock in sample_bay:
    print(f"Transmitting data for: {rock}")


# --- Task 1.3: Collection Duty (Appending) ---
print("\n--- Rover Collection Sequence ---")
new_findings = []

# Loop 3 times to gather new data
for i in range(3):
    rock_type = input("Enter rock type found by robotic arm: ")
    new_findings.append(rock_type)

# Output the result of the collection
print(f"New findings stored: {new_findings}")


# --- Task 1.4: Jettisoning Waste (Extension) ---
print("\n--- Cleaning Storage Bay ---")
# Logical check before removal to prevent errors
if "Dust" in sample_bay:
    sample_bay.remove("Dust")
    print("Waste jettisoned: 'Dust' removed from memory.")

# Verification of final list
print(f"Cleaned Sample Bay: {sample_bay}")