
def instrument_add(portfolio):
    print('''enter the instrument properties in following format
    id,amount,currency,int_rate,int_type,maturity_months''')
    instrument_id = input("Enter instrument id")
    amount = float(input("enter amount"))
    currency = input("Enter currency")
    int_rate = float(input("enter interest rate"))
    int_type = input("Enter interest type")
    maturity_months = int(input("Enter maturity in months"))

    instrument = {"id":instrument_id,
                  "amount":amount,
                  "currency":currency,
                  "int_rate":int_rate,
                  "int_type":int_type,
                  "maturity_months":maturity_months}

                
    portfolio.append(instrument)

def portfolio_view(portfolio):
    for instrument in portfolio:
        print(instrument)
