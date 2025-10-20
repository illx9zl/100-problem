from typing import List, Set

def build_set() -> List[int]:
    """
    Creates a list of unique integers by continuously accepting inputs from the user
    until the list contains exactly 5 unique elements. The insertion order is preserved.

    Returns:
        List[int]: A list containing 5 unique integers in the order they were entered.
    """
    # 1. Initialize a list to store elements in order and a set to ensure uniqueness
    ordered_unique_elements: List[int] = []
    seen_elements: Set[int] = set()
    TARGET_SIZE = 5

    print("--- Ordered Unique Number Builder ---")
    print(f"Goal: Enter exactly {TARGET_SIZE} unique integer numbers. Order will be preserved.")

    # 2. Continuously accept input until the list reaches the target size
    while len(ordered_unique_elements) < TARGET_SIZE:
        required = TARGET_SIZE - len(ordered_unique_elements)
        prompt = f"\nCurrently have {len(ordered_unique_elements)} unique numbers. Enter an integer (Need {required} more): "

        try:
            # Prompt user and attempt to convert input to an integer
            user_input = input(prompt)
            number = int(user_input)

            # Check for uniqueness using the set
            if number not in seen_elements:
                # Add to both the list (for order) and the set (for uniqueness tracking)
                ordered_unique_elements.append(number)
                seen_elements.add(number)
                print(f"✅ Added {number}. Count is now {len(ordered_unique_elements)}.")
            else:
                print(f"⚠️ {number} is already entered. Try a different unique number.")

        except ValueError:
            # Handle cases where the input is not a valid integer
            print("❌ Invalid input. Please enter a whole number/integer.")

    # 3. Return the ordered list
    print("\n--------------------------")
    print(f"Success! The ordered list now contains {TARGET_SIZE} unique elements.")
    return ordered_unique_elements

# Example of how to run the function:
if __name__ == "__main__":
    final_list = build_set()
    print(f"Final Ordered List: {final_list}")
    