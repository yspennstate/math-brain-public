#!/usr/bin/env python3
from fractions import Fraction as F
from math import factorial

# T05 exact self-check: enlarge the Hermite min-max compression from degree 10
# to degree 20 and combine it with the already certified corrected fourth-trace
# cap and degree-48 Perron quasimode. All promoted comparisons use exact
# Fraction/integer arithmetic.

r=F(7,8)
s=F(24861,25000)
c=s*F(1+r,2)
trace4=F(54959,50000)  # corrected scale-safe soft-edge cap
mu_lo=F(91219830,100000000)
mu_hi=F(91219831,100000000)
eps2_hi=F(25851,1000000000)

# Rationalized columns, selected before certification from the first ten
# numerical eigenvectors of the degree-20 normalized-Hermite compression.
# Coordinates are in the unnormalized He_0,...,He_20 basis.
Q=[[10000000000,5047567073,10000000000,10000000000,10000000000,10000000000,10000000000,10000000000,10000000000,10000000000],[-9686988669,3569964747,5466055692,4952966535,4663902726,4442995290,4229885843,3977458907,3610694317,2915730498],[2180917990,-10000000000,-7707827066,-6255580491,-5739679471,-5518512957,-5445828598,-5486671403,-5667472558,-6141366819],[602319955,5497753006,-6184962278,-3758732264,-3084265038,-2754739654,-2543553368,-2374087298,-2197578075,-1933284998],[-174991124,-748565915,9123364396,2453038046,1814844529,1604701579,1530649897,1534260552,1617189786,1853124519],[-75056353,-243171502,-3637049512,2215606059,1189370032,923639114,801081615,728816083,677273546,628672344],[14415587,42546152,339409253,-2288838247,-483079324,-343433087,-302565959,-295244657,-312784819,-371604781],[7948897,20953186,127174145,731082714,-483880139,-241225192,-181821437,-155940664,-142460481,-135887937],[-1005662,-2648502,-14998816,-50095139,394439689,70040150,49635136,45001354,46792084,56490156],[-702009,-1694041,-8434832,-21284783,-106924454,75732646,36175228,27004752,23402480,22303790],[57910,146766,750628,1821896,5691560,-52200025,-8321829,-6087452,-5918421,-7065249],[52655,121177,553514,1153183,2670794,12501507,-9286037,-4365703,-3306568,-3023216],[-2702,-6905,-34519,-76766,-177833,-550324,5682863,880835,693839,778176],[-3420,-7651,-33361,-63889,-122740,-272831,-1242165,946698,452247,364214],[97,265,1377,3055,6587,15367,48999,-536132,-89834,-81923],[196,430,1823,3336,5900,10914,23924,110304,-84197,-43224],[-2,-8,-46,-109,-239,-526,-1276,-4335,46123,9755],[-10,-22,-90,-161,-272,-464,-848,-1878,-9269,6879],[0,0,1,3,8,19,43,112,421,-3900],[0,1,4,7,12,19,32,60,137,822],[0,0,0,0,0,-1,-2,-5,-13,-61]]

tau_lo=F(38519,100000)
tau_hi=F(38521,100000)
pi_lo=F(333,106)
pi_hi=F(355,113)
assert tau_lo*tau_lo < c/(2*pi_hi)
assert tau_hi*tau_hi > c/(2*pi_lo)

def mhe(i,j,tau):
    if (i+j)%2==0:
        return F(factorial(i))*r**i/2 if i==j else F(0)
    out=F(0)
    for k in range(min(i,j)+1):
        n=i+j-2*k
        m=(n-1)//2
        half_over_phi0=-F(((-1)**m)*factorial(2*m),2**m*factorial(m))
        coeff=F(factorial(i)*factorial(j),factorial(k)*factorial(i-k)*factorial(j-k))
        out += coeff*r**k*c**m*half_over_phi0
    return tau*out

def full_BG(tau):
    nrow=len(Q); ncol=len(Q[0])
    M=[[mhe(i,j,tau) for j in range(nrow)] for i in range(nrow)]
    B=[[F(0)]*ncol for _ in range(ncol)]
    G=[[F(0)]*ncol for _ in range(ncol)]
    for a in range(ncol):
        for b in range(ncol):
            G[a][b]=sum(F(Q[i][a]*Q[i][b]*factorial(i)) for i in range(nrow))
            B[a][b]=sum(F(Q[i][a]*Q[j][b])*M[i][j] for i in range(nrow) for j in range(nrow))
    return B,G

def ldlt_pivots(A):
    n=len(A); L=[[F(0)]*n for _ in range(n)]; D=[F(0)]*n
    for i in range(n):
        L[i][i]=F(1)
        z=A[i][i]-sum(L[i][k]*L[i][k]*D[k] for k in range(i))
        assert z>0
        D[i]=z
        for j in range(i+1,n):
            z=A[j][i]-sum(L[j][k]*L[i][k]*D[k] for k in range(i))
            L[j][i]=z/D[i]
    return D

# If B-aG is positive definite on a k-dimensional trial subspace, min-max gives lambda_k>a.
targets=[(3,F(553,1000)),(4,F(107,250)),(5,F(33,100)),(6,F(127,500)),
         (7,F(39,200)),(8,F(149,1000)),(9,F(113,1000)),(10,F(43,500))]
mins=[]
for tau in (tau_lo,tau_hi):
    B,G=full_BG(tau)
    for k,a in targets:
        C=[[B[i][j]-a*G[i][j] for j in range(k)] for i in range(k)]
        piv=ldlt_pivots(C)
        mins.append((tau,k,min(piv)))

# Even-Hermite compression gives lambda_j >= r^(2(j-1))/2. After stronger j=3..10
# bounds, retain this infinite tail from j=11 onward.
positive_tail=sum(a**4 for _,a in targets)+r**80/(F(16)*(1-r**8))

# New source threshold theta*=0.171784.
theta=F(21473,125000)
x=F(45616467,50000000)   # 0.91232934
beta=F(7148463,10000000) # 0.7148463
# 4 theta = 21473/31250, hence x < r^(4 theta) iff x^31250 < r^21473.
assert x**31250 < r**21473
assert x>mu_hi and mu_lo>beta
trace_margin=beta**4-(trace4-x**4-positive_tail)
assert trace_margin>0
temple_margin=(x-mu_hi)*(mu_lo-beta)-eps2_hi
assert temple_margin>0

# Exact finite-lag covariance comparison for the source Lamperti covariance.
cov_margins=[]
for k in range(1,6):
    u=r**k
    tk=c*r**(k-1)
    AA=6*u**5*tk+2*u**10-5*u**6-5*u**4+2
    margin=AA*AA-4*(1-u**4)**5
    assert AA>0 and margin>0
    cov_margins.append(margin)
# Tail k>=6: z=u^2<=1/4 and Q(z)>=4-7z-20z^2>=1, hence R(u)<=u<c r^(k-1).
assert c/r>1
assert F(4)-F(7,4)-F(20,16)==F(1)

old=F(85887,500000)
source_upper=F(1,4)
assert theta>old
assert source_upper-theta < source_upper-old

print('degree = 20; certified positive modes j=3..10')
for tau,k,p in mins:
    print('positive LDL min pivot',float(tau),'k',k,'=',float(p))
print('positive-mode fourth tail L =',positive_tail,float(positive_tail))
print('trace4 cap =',trace4,float(trace4))
print('covariance finite margins =',[float(z) for z in cov_margins])
print('theta old/new =',old,theta,float(old),float(theta))
print('x,beta =',x,beta,float(x),float(beta))
print('trace-budget margin =',trace_margin,float(trace_margin))
print('Temple margin =',temple_margin,float(temple_margin))
print('old/new widths =',float(source_upper-old),float(source_upper-theta))
print('source gain =',theta-old,float(theta-old))
print('ALL_EXACT_CHECKS_PASS = True')
