# # Mortgage calculator
# def monthly_payment(principal, annual_rate, years):

#     # convert to decimal    
#     r_annual_rate = annual_rate / 100
#     # monthly interest rate
#     r = r_annual_rate / 12
#     #  total number of payments
#     n = years * 12
#     # handle zero loans
#     if r == 0:
#         return principal / n

#     return principal * (r * (1 + r)**n) / ((1 + r)**n -1)

# if __name__ == "__main__":
#     principal = float(input("Loan principal (amount borrowed): "))
#     annual_rate = float(input("Annual interest rate(e.g. 7 for 7%): "))
#     years = int(input("Loan term in years (e.g. 30): "))

#     payment = monthly_payment(principal, annual_rate, years)
#     print(f"\nFor a ${principal:,.2f} loan at {annual_rate:.3f}% for {years} years:")
#     print(f"Monthly payment (principal & interest): ${payment:,.2f}")
# Mortgage calculator
# def monthly_payment(principal, annual_rate, years, decimal_places):

#     # convert to decimal    
#     r_annual_rate = annual_rate / 100
#     # monthly interest rate
#     r = round (r_annual_rate / 12, decimal_places)
#     #  total number of payments
#     n = years * 12
#     # handle zero loans
#     if r == 0:
#         return principal / n

#     return principal * (r * (1 + r)**n) / ((1 + r)**n -1)

# def monthly_payment_credit(principal, annual_rate, years):
#     # convert apr to EAR using monthly compounding
#     apr = annual_rate / 100
#     # r = (1 + apr / 365) ** 30.4375 - 1 # months days average or 365.25/12 (365.25 because of leap year)
#     daily_rate = apr / 365
#     days_per_month = 365.25 / 12
#     r = (1 + daily_rate) ** days_per_month -1 
#     n = years * 12 
#     print(f"DEBUG: r={r:.8f}, n={n}, principal={principal}") 

#     if r == 0:
#         return principal / n
    
#     return principal * (r *(1 + r)**n) / ((1+r)**n - 1)
                                          
# if __name__ == "__main__":
#     principal = float(input("Loan principal (amount borrowed): "))
#     annual_rate = float(input("Annual interest rate(e.g. 7 for 7%): "))
#     years = int(input("Loan term in years (e.g. 30): "))

#     payment_mortgage = monthly_payment(principal, annual_rate, years, decimal_places = 2)
#     payment_credit = monthly_payment_credit(principal, annual_rate, years)

#     print(f"\nFor a ${principal:,.2f} loan at {annual_rate:.3f}% for {years} years:")
#     print(f"Monthly payment- mortgage method : ${payment_mortgage:,.2f}")
#     print(f"Monthly payment -credit card method : ${payment_credit:,.2f}")




# def monthly_payment(principal, annual_rate, years):

#     # convert to decimal    
#     r_annual_rate = annual_rate / 100
#     # monthly interest rate
#     r = r_annual_rate / 12
#     #  total number of payments
#     n = years * 12
#     # handle zero loans
#     if r == 0:
#         return principal / n

#     return principal * (r * (1 + r)**n) / ((1 + r)**n -1)

# if __name__ == "__main__":
#     principal = float(input("Loan principal (amount borrowed): "))
#     annual_rate = float(input("Annual interest rate(e.g. 7 for 7%): "))
#     years = int(input("Loan term in years (e.g. 30): "))

#     payment = monthly_payment(principal, annual_rate, years)
#     print(f"\nFor a ${principal:,.2f} loan at {annual_rate:.3f}% for {years} years:")
#     print(f"Monthly payment (principal & interest): ${payment:,.2f}")
   


#     print(f"DEBUG: daily_rate={daily_rate:.10f}, days_per_month={days_per_month:.6f}")
#     print(f"DEBUG: r={r:.8f}, n={n}, principal={principal}")
#     return principal * numerator / denominator
#     if r == 0:
#         return principal / n

#     numerator = r * (1 + r)**n
#     denominator = (1 + r)**n - 1

# if __name__ == "__main__":
#     principal = float(input("Loan principal (amount borrowed): "))
#     annual_rate = float(input("Annual interest rate(e.g. 7 for 7%): "))
#     years = int(input("Loan term in years (e.g. 30): "))

#     payment_mortgage = monthly_payment(principal, annual_rate, years, decimal_places = 2)
#     payment_credit = monthly_payment_credit(principal, annual_rate, years)

#     print(f"\nFor a ${principal:,.2f} loan at {annual_rate:.3f}% for {years} years:")
#     print(f"Monthly payment- mortgage method : ${payment_mortgage:,.2f}")
#     print(f"Monthly payment -credit card method : ${payment_credit:,.2f}")
#     print(f"DEBUG: numerator={numerator:.8f}, denominator={denominator:.8f}")

# def monthly_payment(principal, annual_rate, years, decimal_places):
#     r_annual_rate = annual_rate / 100
#     100000
#     r = round(r_annual_rate / 12, decimal_places)
#     n = years * 12
#     if r == 0:
#         return principal / n
#     return principal * (r * (1 + r)**n) / ((1 + r)**n - 1)

#     print(f"DEBUG: daily_rate={daily_rate:.10f}, days_per_month={days_per_month:.6f}")
#     print(f"DEBUG: r={r:.8f}, n={n}, principal={principal}")

#     if r == 0:
#         return principal / n

#     numerator = r * (1 + r)**n
#     denominator = (1 + r)**n - 1

#     print(f"DEBUG: numerator={numerator:.8f}, denominator={denominator:.8f}")

#     return principal * numerator / denominator

# # --- this block must be at column 0, outside both functions ---
# if __name__ == "__main__":
#     principal = float(input("Loan principal (amount borrowed): "))
#     annual_rate = float(input("Annual interest rate(e.g. 7 for 7%): "))
#     years = int(input("Loan term in years (e.g. 30): "))

#     payment_mortgage = monthly_payment(principal, annual_rate, years, decimal_places=2)
#     payment_credit = monthly_payment_credit(principal, annual_rate, years)

#     print(f"\nFor a ${principal:,.2f} loan at {annual_rate:.3f}% for {years} years:")
#     print(f"Monthly payment- mortgage method : ${payment_mortgage:,.2f}")
#     print(f"Monthly payment- credit card method : ${payment_credit:,.2f}")

def monthly_payment_mortgage(principal, annual_rate, years):
    r = annual_rate / 100 / 12
    n = years * 12
    if r == 0:
        return principal / n
    return principal * (r * (1 + r)**n) / ((1 + r)**n - 1)

def monthly_payment_credit(principal, annual_rate, years):
    ear = (1 + annual_rate / 100 / 365) ** 365 - 1
    r = (1 + ear) ** (1/12) - 1
    n = years * 12
    if r == 0:
        return principal / n
    return principal * (r * (1 + r)**n) / ((1 + r)**n - 1)

if __name__ == "__main__":
    principal = 100000.0
    annual_rate = 8.25
    years = 30

    payment_mortgage = monthly_payment_mortgage(principal, annual_rate, years)
    payment_credit = monthly_payment_credit(principal, annual_rate, years)

    total_mortgage = payment_mortgage * years * 12
    total_credit = payment_credit * years * 12

    print(f"\nFor a ${principal:,.2f} loan at {annual_rate:.2f}% for {years} years:")
    print(f"\n--- Standard Mortgage (Monthly Compounding) ---")
    print(f"Monthly payment:          ${payment_mortgage:,.2f}")
    print(f"Total paid over 30 years: ${total_mortgage:,.2f}")
    print(f"\n--- Credit Card Style (Daily Compounding, 360 Payments) ---")
    print(f"Monthly payment:          ${payment_credit:,.2f}")
    print(f"Total paid over 30 years: ${total_credit:,.2f}")
    print(f"\n--- The Difference ---")
    print(f"Extra cost of daily compounding: ${total_credit - total_mortgage:,.2f}")