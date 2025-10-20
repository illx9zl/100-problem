from typing import List
import math

def calculate_investment_growth(principal: float, annual_rate: float, years: int) -> List[float]:
    """
    Calculates the accumulated amount of an investment for each year up to 5 years
    using compound interest.

    Args:
        principal (float): The initial investment amount (P).
        annual_rate (float): The annual interest rate (r) as a percentage.
        years (int): The total number of years (only first 5 years are calculated).

    Returns:
        List[float]: A list of accumulated amounts for years 1 through 5.
    """
    # Constraint: Only the first 5 years are considered for output, regardless of the input 'years'.
    MAX_OUTPUT_YEARS = 5 
    
    # Convert annual rate percentage to decimal (e.g., 5% becomes 0.05)
    rate_decimal = annual_rate / 100.0
    
    accumulated_amounts: List[float] = []
    
    # Iterate from year 1 up to the maximum required output year (5)
    for n in range(1, MAX_OUTPUT_YEARS + 1):
        # Compound Interest Formula: A = P * (1 + r)^n
        # A = accumulated amount
        accumulated_amount = principal * (1 + rate_decimal) ** n
        
        # Round the result to two decimal places for financial precision, matching the example output.
        rounded_amount = round(accumulated_amount, 2)
        accumulated_amounts.append(rounded_amount)
        
    return accumulated_amounts

# Example Usage to demonstrate the function
if __name__ == "__main__":
    # Example Input: principal = 1000, annual_rate = 5, years = 5
    principal = 1000
    annual_rate = 5
    years = 5
    
    # Perform the calculation
    result = calculate_investment_growth(principal, annual_rate, years)
    
    # Output: [1050.0, 1102.5, 1157.63, 1215.51, 1276.28]
    print(result)