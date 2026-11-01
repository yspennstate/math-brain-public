"""What the published covering-code tables say about the maximum discrepancy of an n x n sign matrix,
for n up to 24.

max_A disc(A) = n - 2*min{R : some complement-closed binary code of length n and size 2n has covering
radius R}.  Writing K(n,R) for the least size of ANY binary covering code of length n and radius R, and
noting that a code together with its complements has at most twice its size:

    K_upper(n,R) <= n   ==>  radius R is achievable with 2n complement-closed codewords, so disc >= n-2R
    K_lower(n,R) >  2n  ==>  radius R is impossible, so disc < n-2R

which brackets the maximum.  K values are the published bounds (Kéri's tables, descended from Cohen,
Honkala, Litsyn and Lobstein, *Covering Codes*, 1997); a pair is a bracket, a single number is exact.

CONTROL: for n <= 11 the exact values computed directly here are 2,1,2,3,4,3,4,5,4,5, and the bracket
from the tables must contain each of them.
"""
K = {
 3:  {1:(2,2), 2:(2,2), 3:(1,1)},
 4:  {1:(4,4), 2:(2,2), 3:(2,2), 4:(1,1)},
 5:  {1:(7,7), 2:(2,2), 3:(2,2), 4:(2,2), 5:(1,1)},
 6:  {1:(12,12), 2:(4,4), 3:(2,2), 4:(2,2), 5:(2,2), 6:(1,1)},
 7:  {1:(16,16), 2:(7,7), 3:(2,2), 4:(2,2), 5:(2,2), 6:(2,2), 7:(1,1)},
 8:  {1:(32,32), 2:(12,12), 3:(4,4), 4:(2,2), 5:(2,2), 6:(2,2), 7:(2,2)},
 9:  {1:(62,62), 2:(16,16), 3:(7,7), 4:(2,2), 5:(2,2), 6:(2,2), 7:(2,2)},
 10: {1:(107,120), 2:(24,30), 3:(12,12), 4:(4,4), 5:(2,2), 6:(2,2), 7:(2,2)},
 11: {1:(180,192), 2:(37,44), 3:(15,16), 4:(7,7), 5:(2,2), 6:(2,2), 7:(2,2)},
 12: {1:(342,380), 2:(62,78), 3:(18,28), 4:(11,12), 5:(4,4), 6:(2,2), 7:(2,2)},
 13: {1:(598,704), 2:(97,128), 3:(28,42), 4:(12,16), 5:(7,7), 6:(2,2), 7:(2,2)},
 14: {1:(1172,1408), 2:(159,248), 3:(44,64), 4:(16,28), 5:(10,12), 6:(4,4), 7:(2,2)},
 15: {1:(2048,2048), 2:(310,384), 3:(70,112), 4:(22,32), 5:(12,16), 6:(7,7), 7:(2,2)},
 16: {1:(4096,4096), 2:(512,768), 3:(115,192), 4:(33,64), 5:(13,28), 6:(9,12), 7:(4,4)},
 17: {1:(7419,8192), 2:(859,1536), 3:(187,320), 4:(52,112), 5:(19,32), 6:(11,16), 7:(7,7)},
 18: {1:(14564,16384), 2:(1702,2944), 3:(316,512), 4:(83,192), 5:(27,64), 6:(12,28), 7:(9,12)},
 19: {1:(26309,31744), 2:(2898,4096), 3:(513,1024), 4:(128,256), 5:(40,64), 6:(16,32), 7:(10,16)},
 20: {1:(52618,63488), 2:(5330,8192), 3:(892,2048), 4:(208,512), 5:(62,128), 6:(24,64), 7:(12,28)},
 21: {1:(96125,122880), 2:(9900,14336), 3:(1475,3072), 4:(336,896), 5:(95,256), 6:(33,64), 7:(14,32)},
 22: {1:(190651,245760), 2:(17336,24576), 3:(2544,4096), 4:(553,1536), 5:(150,512), 6:(49,128), 7:(20,64)},
 23: {1:(352827,393216), 2:(30686,32768), 3:(4096,4096), 4:(912,2048), 5:(235,640), 6:(73,224), 7:(29,64)},
 24: {1:(699051,786432), 2:(60381,65536), 3:(8128,8192), 4:(1505,4096), 5:(376,1024), 6:(113,384), 7:(41,128)},
}
EXACT = {3:1, 4:2, 5:3, 6:4, 7:3, 8:4, 9:5, 10:4, 11:5}

import math
print(f"{'n':>3} {'disc >=':>8} {'disc <=':>8} {'ratio <=':>9} {'exact':>6} {'bracket ok':>11}")
for n in sorted(K):
    rs = sorted(K[n])
    lo = None       # largest certain discrepancy
    for R in rs:
        if K[n][R][1] <= n:
            lo = n - 2 * R; break
    hi = None       # smallest R not ruled out
    for R in rs:
        if K[n][R][0] <= 2 * n:
            hi = n - 2 * R; break
    if hi is None: hi = n - 2 * max(rs)
    ok = ''
    if n in EXACT:
        e = EXACT[n]
        ok = 'yes' if (lo is None or lo <= e) and e <= hi else 'NO'
    print(f"{n:>3} {str(lo if lo is not None else '-'):>8} {hi:>8} {hi/math.sqrt(n):>9.4f} "
          f"{str(EXACT.get(n,'-')):>6} {ok:>11}")
print("\ndisc >= column: from K_upper(n,R) <= n, which makes the radius achievable with complements")
print("disc <= column: from K_lower(n,R) > 2n, which makes every smaller radius impossible")
print("the ratio column is an upper bound on disc/sqrt(n) at that n; 5/3 = 1.6667 is what is attained at n=9")
