"""Recompute the numerical assertions printed in Section 6 independently."""
from fractions import Fraction
import itertools
from collections import Counter
import math
import mpmath as mp
from referee_numeric import determinant, enumeration, lis_profile, num

mp.mp.dps = 40
LOG = []


def say(s):
    print(s, flush=True)
    LOG.append(s)


def main():
    profiles = [Counter(lis_profile(p) for p in itertools.permutations(range(n))) for n in range(10)]
    raw = [[('.7',1)], [('.8',2)], [('1',3)], [('1',4)],
           [('.3',1),('1',2)], [('.4',2),('1',3)],
           [('.2',1),('.6',2),('1',3)], [('.3',2),('.5',3),('.9',4)],
           [('.25',1),('.5',3),('1',4)], [('.5',3),('1',2)],
           [('.6',3),('.6',2),('1',4)],
           [('.1',1),('.2',2),('.3',3),('.4',4),('1',5)]]
    max_diff, max_tail = mp.mpf(0), mp.mpf(0)
    for row in raw:
        obs = [(Fraction(t), k) for t,k in row]
        by_time = {}
        for t,k in obs:
            by_time[t] = min(by_time.get(t,k),k)
        reduced = sorted(by_time.items())
        for a in range(len(reduced)-2,-1,-1):
            reduced[a] = (reduced[a][0],min(reduced[a][1],reduced[a+1][1]))
        result, size = determinant(reduced)
        lower, bound = enumeration(obs, profiles)
        difference = result-lower
        assert -mp.mpf('1e-35') <= difference <= bound
        max_diff, max_tail = max(max_diff,difference), max(max_tail,bound)
        say(f'{row}: size={size}, value={mp.nstr(result,16)}, enum_difference={mp.nstr(difference,8)}')
    say(f'Largest enumeration deficit={mp.nstr(max_diff,12)}; all Poisson tails<={mp.nstr(max_tail,12)}')
    for T in [Fraction(1,2),Fraction(1),Fraction(2),Fraction(7,2)]:
        for s in [Fraction(0),T/4,T/2]:
            result = determinant([(s,1),(T,2)])[0]
            closed = mp.exp(-num(T))*mp.besseli(0,2*mp.sqrt(num(T-s)))
            assert abs(result-closed) < mp.mpf('1e-35')
            say(f'closed s={s},T={T}: {mp.nstr(closed,23)}')
    for i in range(1,5):
        tail = min(mp.binomial(m,m-i+1)*mp.exp(-mp.mpf(m-i+1)*400/m**2)*m**2/(m-i+1)
                   for m in range(i,40))
        say(f'Integral tail beyond 400, i={i}: <= {mp.nstr(tail,12)}')
    c3 = mp.fsum(mp.mpf(math.comb(2*n,n)//(n+1)-1)/mp.factorial(n) for n in range(1,181))
    say('Catalan c(3) series through n=180: '+mp.nstr(c3,38))
    with open('referee_reported.txt','w') as out:
        out.write('\n'.join(LOG)+'\n')


if __name__ == '__main__':
    main()
