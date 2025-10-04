

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

        print(f"t={t}, y={y:.3%}, cash_flow={cash_flow:,.2f}, "
              f"pv_factor={pv_factor:.6f}, pvcf={pvcf:,.2f}")

    return bond_price

