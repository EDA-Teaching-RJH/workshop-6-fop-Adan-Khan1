# --- Task 1.1: The Storage Bay ---
print("\n--- Task 1.1: Storage Bay Status ---")

# 1. Create the list
sample_bay = ["Basalt", "Silica", "Iron", "Dust"]

# 2. Print first item (Index 0)
print("First item:", sample_bay[0])

# 3. Print last item (using negative indexing)
print("Last item:", sample_bay[-1])

# 4. Print total number of samples
print("Total samples:", len(sample_bay))


# --- Task 1.2: Analysing Samples (Iteration) ---
print("\n--- Task 1.2: Transmitting Data ---")

# 1. Loop through sample_bay without a counter
for rock in sample_bay:
    # 2. Print the transmission phrase
    print(f"Transmitting data for: {rock}")


# --- Task 1.3: Collection Duty (Appending) ---
print("\n--- Task 1.3: New Findings Collection ---")

# 1. Create empty list
new_findings = []

# 2. Loop 3 times for input
for i in range(3):
    user_input = input("Enter new rock type: ")
    
    # 3. Append input to the list
    new_findings.append(user_input)

# 4. Print the full list
print("New findings list:", new_findings)


# --- Task 1.4: Jettisoning Waste (Extension) ---
print("\n--- Task 1.4: Cleaning Storage ---")

# 1. Check if "Dust" is in the list
if "Dust" in sample_bay:
    # 2. Remove it
    sample_bay.remove("Dust")
    print("Item 'Dust' has been removed.")
else:
    print("'Dust' not found in sample bay.")

# 3. Print cleaned list
print("Final Sample Bay:", sample_bay)
