def calculate_bmi(weight, height):
    """
    Calculate BMI and classify into categories based on predefined ranges.
    """
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category


def main():
    """
    Main function to get user input and display BMI result and category.
    """
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("Invalid input. Please enter numerical values for weight and height.")
        return

    if weight <= 0 or height <= 0:
        print("Invalid input. Weight and height must be positive values.")
        return

    bmi, category = calculate_bmi(weight, height)
    
    print(f"\nBMI Result: {bmi:.2f}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
