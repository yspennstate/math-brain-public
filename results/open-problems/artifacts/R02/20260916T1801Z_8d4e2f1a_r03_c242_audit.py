#!/usr/bin/env python3
# Independent R02 audit of R03-C242 finite scalar core.
# For k<=8 enumerate every F3 coefficient vector a and every Boolean u,
# excluding the special forms 0 and coordinate projections, and verify
# that at most 3/4 of Boolean inputs yield a.u in {0,1} mod 3.
for k in range(1,9):
    worst=-1
    arg=None
    for idx in range(3**k):
        t=idx
        a=[]
        for _ in range(k):
            a.append(t%3); t//=3
        special = (all(x==0 for x in a) or
                   (a.count(1)==1 and a.count(2)==0 and a.count(0)==k-1))
        if special:
            continue
        good=0
        for mask in range(1<<k):
            v=sum(a[i] for i in range(k) if (mask>>i)&1)%3
            if v in (0,1):
                good+=1
        if good>worst:
            worst=good;arg=a[:]
    assert 4*worst <= 3*(1<<k), (k,worst,arg)
    print(k, worst, 1<<k, arg)
print("R02 INDEPENDENT AUDIT R03-C242 FINITE CORE PASS")
