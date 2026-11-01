#!/usr/bin/env python3
"""Exact-rational verifier for B17's partial-branch shared-core FEI witness.

Consumes source-certified intervals for the 18-bit host, the 162-bit balanced
monotone shared graft F, and K(ell^4), then checks the exact one-branch
composition recurrence and the final shared-core ledger. It does not re-prove
inherited source certificates and is not a proof of FEI.
"""
from fractions import Fraction
import json

I0 = Fraction(261,128)
H0_LO = Fraction("6.776605309005978082519790221891882314787235038")
H0_HI = Fraction("6.776605309005978082519790221891882314787235039")
I1 = Fraction(68013,32768)
H1_LO = Fraction("7.014850042680291613033104756310658624299893163")
H1_HI = Fraction("7.014850042680291613033104756310658624299893164")
ELL = Fraction(14593,65536)
K_LO = Fraction("0.000005669659456255203780880696514165710505627614411852309871367271610481643")
K_HI = Fraction("0.000005669659456255203780880696514165710505627614411852309871367271610481643")
ALPHA = Fraction(9,256)
R6_HI = Fraction("6.5218509495504481848824149770395541197961122790612205924109263953322714")

def dec(x,digits=80):
    sign="-" if x<0 else ""
    x=abs(x); q,r=divmod(x.numerator,x.denominator)
    out=[sign+str(q),"."]
    for _ in range(digits):
        r*=10; a,r=divmod(r,x.denominator); out.append(str(a))
    return "".join(out)

def main():
    # h_1=F; h_{m+1}=F with only the distinguished core input replaced by
    # h_m and all other F-inputs kept as fresh characters. Since F is balanced
    # monotone and its distinguished singleton coefficient is ELL, that input's
    # influence equals ELL.
    Ih=I1
    Hh_lo=H1_LO
    Hh_hi=H1_HI
    n_h=162
    for _m in range(2,5):
        Ih = I1 + ELL*(Ih-1)
        Hh_lo = H1_LO + ELL*Hh_lo
        Hh_hi = H1_HI + ELL*Hh_hi
        n_h += 161

    assert n_h == 645
    b = ELL**4

    # Endpoint-for-endpoint preservation of balanced-excess ratio.
    assert Hh_lo*(I1-1) == H1_LO*(Ih-1)
    assert Hh_hi*(I1-1) == H1_HI*(Ih-1)

    # Apply the exact nine-host shared-core operator T to h_4.
    Istar = 1 + (I0-1) + ALPHA*(Ih-1)
    Hstar_lo = H0_LO + ALPHA*Hh_lo + K_LO
    Hstar_hi = H0_HI + ALPHA*Hh_hi + K_HI
    Rstar_lo = Hstar_lo/(Istar-1)
    Rstar_hi = Hstar_hi/(Istar-1)
    nstar = 9 + 9*(n_h-1)
    assert nstar == 5805

    gain = Rstar_lo - R6_HI
    assert gain > 0

    out = {
      "partial_chain_depth": 4,
      "partial_chain_dimension": n_h,
      "partial_chain_influence_exact": str(Ih),
      "partial_chain_entropy_lower": dec(Hh_lo,70),
      "partial_chain_entropy_upper": dec(Hh_hi,70),
      "distinguished_coefficient_exact": str(b),
      "final_dimension": nstar,
      "final_influence_exact": str(Istar),
      "final_entropy_lower": dec(Hstar_lo,70),
      "final_entropy_upper": dec(Hstar_hi,70),
      "final_balanced_excess_lower": dec(Rstar_lo,75),
      "final_balanced_excess_upper": dec(Rstar_hi,75),
      "peer_R6_upper": dec(R6_HI,75),
      "certified_gain_over_peer_R6_upper": dec(gain,75),
      "checks": [
        "one-branch balanced composition recurrence evaluated exactly",
        "one-branch chain preserves H/(I-1) endpoint-for-endpoint",
        "distinguished singleton coefficient is ell^4",
        "source-certified K(ell^4) inserted into exact T ledger",
        "5805-variable balanced-excess lower endpoint exceeds peer R6 upper endpoint"
      ]
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
