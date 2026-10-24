#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

checks=0
for n in range(2,6):
    N=1<<n
    for c in range(1,n+1):
        for F in combinations(range(n),c):
            for bits in range(1<<c):
                for u in range(N):
                    for v in range(N):
                        ru=sum(((u>>i)&1)<<j for j,i in enumerate(F))
                        rv=sum(((v>>i)&1)<<j for j,i in enumerate(F))
                        rank=0 if ru==0 and rv==0 else (1 if (ru==0 or rv==0 or ru==rv) else 2)
                        bad=0
                        for z in range(1<<c):
                            num=(z==bits)+((z^ru)==bits)+((z^rv)==bits)+((z^ru^rv)==bits)
                            if num%2:
                                bad+=1
                        observed=Fraction(bad,1<<c)
                        predicted=Fraction(4,1<<c) if rank==2 else Fraction(0)
                        assert observed==predicted
                        checks+=1
print("PASS")
print("exact_subcube_face_checks",checks)
