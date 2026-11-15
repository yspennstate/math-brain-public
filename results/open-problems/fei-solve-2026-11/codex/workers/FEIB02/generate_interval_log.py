"""Exact tables for an integer interval logarithm at scale 2^56."""
from fractions import Fraction as F
from pathlib import Path
Q=1<<56

def ln_bounds(x,M=60):
 y=(x-1)/(x+1)
 lo=2*sum(y**(2*j+1)/(2*j+1) for j in range(M))
 hi=lo+2*y**(2*M+1)/((2*M+1)*(1-y*y))
 return lo,hi
lo2,hi2=ln_bounds(F(2))
low=[];high=[]
for m in range(256,512):
 lo,hi=ln_bounds(F(m,256));x=lo/hi2*Q;y=hi/lo2*Q
 low.append(x.numerator//x.denominator);high.append((y.numerator+y.denominator-1)//y.denominator)
invlo=(F(Q)/hi2).numerator//(F(Q)/hi2).denominator
inv=F(Q)/lo2;invhi=(inv.numerator+inv.denominator-1)//inv.denominator
Path('interval_log_table.h').write_text('#define LOG_Q (1ULL<<56)\nstatic const uint64_t ilog_lo[256]={'+','.join(str(x)+'ULL' for x in low)+'};\nstatic const uint64_t ilog_hi[256]={'+','.join(str(x)+'ULL' for x in high)+'};\n#define INV_LN2_LO '+str(invlo)+'ULL\n#define INV_LN2_HI '+str(invhi)+'ULL\n')
print('Generated exact log table at scale 2^56, using positive-series remainders.')
