import psutil, sys, subprocess
psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
import rec
for kind,lo in (('adj',31),('dis',31)):
    for n in range(lo,41):
        N=rec.Npoly(n,kind); d,b=rec.bern(N)
        neg=sum(1 for bj in b for c in bj.coeffs() if c<0)
        zero=[j for j,bj in enumerate(b) if bj==0]
        print(kind,n,'deg',d,'neg',neg,'zero',zero,'b0!=0',b[0]!=0,flush=True)
