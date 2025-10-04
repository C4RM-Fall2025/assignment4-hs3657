

def getBondPrice_E(face, couponRate, m, yc):
    coupon_payment = face * couponRate
    bond_price = 0
    
    for t, y in enumerate(yc, start=1):
        if t == m: 
            cash_flow = coupon_payment + face
        else:
            cash_flow = coupon_payment
        
        pv_factor = 1 / (1 + y) ** t
        pvcf = cash_flow * pv_factor
        
        bond_price += pvcf
    
    return bond_price
