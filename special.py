def check_year(year):
    a = int(str(year)[:2])
    b = int(str(year)[2:4])

    if a ** 2 + 2*a*b + b**2 == year:
        return True
    return False    
if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False
