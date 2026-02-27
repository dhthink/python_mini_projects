# Mortgage calculator
def monthly_payment(principal, annual_rate, years):

    # convert to decimal    
    r_annual_rate = annual_rate / 100
    # monthly interest rate
    r = r_annual_rate / 12
    #  total number of payments
    n = years * 12
    # handle zero loans
    if r == 0:
        return principal / n

    return principal * (r * (1 + r)**n) / ((1 + r)**n -1)

if __name__ == "__main__":
    principal = float(input("Loan principal (amount borrowed): "))
    annual_rate = float(input("Annual interest rate(e.g. 7 for 7%): "))
    years = int(input("Loan term in years (e.g. 30): "))

    payment = monthly_payment(principal, annual_rate, years)
    print(f"\nFor a ${principal:,.2f} loan at {annual_rate:.3f}% for {years} years:")
    print(f"Monthly payment (principal & interest): ${payment:,.2f}")
