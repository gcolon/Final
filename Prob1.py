def credit_card_penalty(balance,days):

    if days < 15:
        return 0.05 * balance
    elif days >= 15 and days <= 30:
        return 0.10 * balance
    elif days >= 31 and days <= 60:
        return 0.15 * balance
    else:
        return balance * 0.20



print "Penalty 1:", credit_card_penalty(15000, 18)
print "Penalty 2:", credit_card_penalty(7000, 31)
print "Penalty 3:", credit_card_penalty(300, 70)
print "Penalty 4:", credit_card_penalty(1000, 3)
