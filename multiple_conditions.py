has_sufficent_funds = True
account_active = False

if has_sufficent_funds and account_active:
    print("TX approved")

if has_sufficent_funds or account_active:
    print("one thing was true!")