
def getBondPrice_E(face, couponRate, yc):
    couponPayment = face * couponRate
    bondPrice = 0.0
    n = len(yc)

    for i, r in enumerate(yc, start=1):
        if i == n:
            cash_flow = couponPayment + face
        else:
            cash_flow = couponPayment

        pv_factor = 1 / (1 + r) ** i
        bondPrice += cash_flow * pv_factor

    return bondPrice
