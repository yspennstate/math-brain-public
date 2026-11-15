"""Symbolic family identities and high-precision spectral checks."""
import sympy as s
import mpmath as mp
from exact_core import calculate, lump, leaf_family, save_json


def main():
    t,m = s.symbols('t m',positive=True)
    total = t**6+m*(t+1)**2
    A = t+1+1/t
    C = t+2+1/t
    mu = m*(t*(t+1)*A+C)/total
    tx = (t+1)*(t**5*(t+1)+m*(2*t+1))/total
    ty = t*(2*t**6+m*(t+1)*(t+2))/total
    muy = m*t*t*(t+1)/total
    assert s.simplify(C-mu-tx) == 0
    assert s.simplify(2*t-muy-ty) == 0
    print('W =',total)
    print('tmix(X) =',tx)
    print('tmix(hX) =',ty)
    print('tau0(hX) =',m*t-muy)
    print('Condition for original maximizing pair hub/heavy: t^6 >= m*t*(t^2-1).')
    records = []
    mp.mp.dps = 80
    for mm in (2,3,4,5):
        for tt in (2,10,100,1000,1000000):
            w = leaf_family(mm,tt)
            x = calculate(w)
            hw,_ = lump(w,(mm,mm+1))
            y = calculate(hw)
            assert x['tmix'] == tx.subs({m:mm,t:tt})
            assert y['tmix'] == ty.subs({m:mm,t:tt})
            assert y['tau0'] == (m*t-muy).subs({m:mm,t:tt})
            rr = mp.mpf(mm)/(mp.mpf(tt)**5+mm)
            S = 1+mp.mpf(1)/tt+rr
            Q = mp.mpf(1)/(tt+1)+rr*(1+mp.mpf(1)/(tt*(tt+1)))
            slowgap = 2*Q/(S+mp.sqrt(S*S-4*Q))
            tau2x = max(mp.mpf(tt),1/slowgap)
            cv = lambda z: mp.mpf(z.numerator)/z.denominator
            factors = [cv(y['tmix'])/cv(y['tau0']),
                       cv(y['tau0'])/(mm*tt),
                       mp.mpf(tt)/tau2x,
                       tau2x/cv(x['tmix'])]
            row = dict(n=mm+2,t=tt,tau2_original=mp.nstr(tau2x,30),
                       tau2_quotient=tt,
                       upper_bound_factors=[mp.nstr(v,30) for v in factors])
            records.append(row)
            print(f"n={mm+2} t={tt}: tau2X={mp.nstr(tau2x,14)} "
                  f"chain factors={[mp.nstr(v,12) for v in factors]}")
    save_json('family_spectral.json',records)


if __name__ == '__main__':
    main()
