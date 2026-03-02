# This is my python code:
def monthly_payment(principal, annual_rate, years):
 
    r_annual_rate = annual_rate / 100 # convert to decimal   
    r = r_annual_rate / 12  # monthly interest rate
    n = years * 12      #  total number of payments
    # handle zero loans
    if r == 0:
        return principal / n

    return principal * (r * (1 + r)**n) / ((1 + r)**n -1)

def monthly_payment_credit(principal, annual_rate, years):
    # Effective Annual Rate as figured by Credit Card Companies
    ear = (1 + annual_rate / 100 / 365.25) ** 365 - 1  # ear from google search
    r = (1 + ear) ** (1/12) - 1  # monthly rate from google search
    n = years * 12
    if r == 0:
        return principal / n
    return principal * (r * (1 + r)**n) / ((1 + r)**n - 1)

if __name__ == "__main__":
    principal = float(input("Loan principal (amount borrowed): "))
    annual_rate = float(input("Annual interest rate(e.g. 7 for 7%): "))
    years = int(input("Loan term in years (e.g. 30): "))

    payment = monthly_payment(principal, annual_rate, years)
    print(f"\nFor a ${principal:,.2f} loan at {annual_rate:.3f}% for {years} years:")
    print(f"Monthly payment (principal & interest): ${payment:,.2f}")



    payment_mortgage = monthly_payment(principal, annual_rate, years)
    payment_credit = monthly_payment_credit(principal, annual_rate, years)
    total_mortgage = payment_mortgage * years * 12
    total_credit = payment_credit * years * 12


    print(f"\n -- Standard Mortgage Calulation--")
    print(f"Monthly payment:          ${payment_mortgage:,.2f}")
    print(f"Total paid over 30 years: ${total_mortgage:,.2f}")
    print(f"\n--- Credit Card Style (Daily Compounding, 360 Payments) ---")
    print(f"Monthly payment:          ${payment_credit:,.2f}")
    print(f"Total paid over 30 years: ${total_credit:,.2f}")
    print(f"\n--- The Difference ---")
    print(f"Extra cost of daily compounding: ${total_credit - total_mortgage:,.2f}")