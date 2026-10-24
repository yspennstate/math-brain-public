from math import sqrt, exp, e

C_direct = 6*sqrt(e)
C_one_hub = 3*2**(7/6)*exp(1/3)*2**(1/6)
C_two_hub = 3*2**(5/6)*4**(1/6)
C_three_hub = 3*sqrt(2)*8**(1/6)
C = max(C_direct, C_one_hub, C_two_hub, C_three_hub)
paid_partner = C*1000/19

assert C == C_one_hub
assert C < 10.551
assert paid_partner < 556

print({
    "direct_D": C_direct,
    "one_hub_after_anchor": C_one_hub,
    "two_hub_after_anchor": C_two_hub,
    "three_hub_after_anchor": C_three_hub,
    "C3": C,
    "partner_diffuse_payment": paid_partner,
})
