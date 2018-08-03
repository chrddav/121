Lottery = float(input('Enter the Lottery Prize Amount without commas: '))
Pre_tax_instant_payout = Lottery * 0.65
Post_tax_instant_payout = Pre_tax_instant_payout * 0.7
Pre_tax_annuity = Lottery * 0.05
Post_tax_annuity = Pre_tax_annuity * 0.7
print('Instant Payout Winnings Before Tax: $', format (Pre_tax_instant_payout, ',.2f'))
print('Instant Payout Winnings After Tax: $', format (Post_tax_instant_payout, ',.2f'))
print('20 Annual Payout Winnings Before Tax: $', format (Pre_tax_annuity, ',.2f'))
print('20 Annual Payout Winnings After Tax: $', format (Post_tax_annuity, ',.2f'))

