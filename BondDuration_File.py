
def getBondDuration(y, face, couponRate, m, ppy = 1):
    coupon_payment = (couponRate * face) / ppy
    periods = m * ppy
    period_rate = y / ppy

    bond_price = 0
    weighted_sum = 0

    for t in range(1, periods + 1):
        if t == periods:
            cash_flow = coupon_payment + face
        else:
            cash_flow = coupon_payment

        pv_factor = 1 / (1 + period_rate) ** t
        pvcf = cash_flow * pv_factor

        bond_price += pvcf
        weighted_sum += pvcf * t / ppy

    bondDuration = weighted_sum / bond_price
    return bondDuration
