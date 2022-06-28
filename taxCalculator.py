while True:
    profit = float(input(f'Enter chargeable income profit: '))
    
    
    if profit <= 100000:
        row1 = profit * 0.0425
        row2=0
        row3=0
        grossTax = row1
        netTax = row1
        print(f'4.25% on above $100,000: {row1}\n8.5% on next $100,000: {row2}\n17% on income above $200,000: {row3}\nGross Tax Payable: {grossTax}\nNet Tax Payable: {netTax}')
        
    elif 200000 >= profit > 100000:
        row1 = 100000 * 0.0425
        row2 = (profit - 100000) * 0.085
        row3=0
        grossTax = row1 + row2
        netTax = row1 + row2
        print(f'4.25% on above $100,000: {row1}\n8.5% on next $100,000: {row2}\n17% on income above $200,000: {row3}\nGross Tax Payable: {grossTax}\nNet Tax Payable: {netTax}')
    
    elif profit > 200000:
        row1 = 100000 * 0.0425
        row2 = 100000 * 0.085
        row3 = (profit - 200000) * 0.17
        grossTax = row1 + row2 + row3
        netTax = row1 + row2 + row3
        print(f'4.25% on above $100,000: {row1}\n8.5% on next $100,000: {row2}\n17% on income above $200,000: {row3}\nGross Tax Payable: {grossTax}\nNet Tax Payable: {netTax}')
        
    elif profit == 0:
        break