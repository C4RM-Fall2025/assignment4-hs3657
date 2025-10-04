

def getBondPrice_E(face, couponRate, m, yc):
    coupon_payment = face * couponRate
    bond_price = 0

    for t in range(1, m + 1): 
        if t == m: 
            cash_flow = coupon_payment + face
        else:
            cash_flow = coupon_payment

        pv_factor = 1 / (1 + yc[t - 1]) ** t
        pvcf = cash_flow * pv_factor

        bond_price += pvcf  

    return bond_price

