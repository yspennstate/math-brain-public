from fractions import Fraction
from math import ceil
M=[0,5,16,29,48,61,80,101,128,133,144,157,176,189,208,229,256]
c=Fraction(303,1000)

def parts(total,q,lo=1,p=()):
    if q==0:
        if total==0: yield p
        return
    for x in range(lo,total//q+1):
        yield from parts(total-x,q-1,x,p+(x,))

def energy(p): return sum((Fraction(k*k,M[k]) for k in p),Fraction())
assert 3*303 < 1000
mins={}
for q in range(1,17):
    vals=[(energy(p),p) for p in parts(16,q)]
    if vals: mins[q]=min(vals)
q6=min((e,p,q) for q,(e,p) in mins.items() if q>=6)
assert q6[0]==Fraction(49,30) and q6[1]==(1,1,1,1,4,8)
assert Fraction(49,30)-5*c==Fraction(71,600)>0
p4=[p for p in parts(16,4) if energy(p)<5*c]
p5=[p for p in parts(16,5) if energy(p)<5*c]
assert len(p4)==34
assert p5==[(1,1,1,5,8),(1,1,2,4,8),(1,2,2,3,8),(1,3,4,4,4),(2,2,2,2,8),(2,2,4,4,4)]
cold=Fraction(219,725)
newB5sq=1/c
oldB5sq=1/cold
pi_lo=Fraction(333,106); pi_hi=Fraction(22,7)
assert 17*newB5sq < 18*pi_lo
assert 18*newB5sq > 18*pi_hi
def bal_sq(n): return Fraction(3*n,4)
def block_sq(n,b5): return b5*ceil(n/5)
improved=[]
for n in range(5,86):
    old=min(bal_sq(n),block_sq(n,oldB5sq))
    new=min(bal_sq(n),block_sq(n,newB5sq))
    if new<old: improved.append(n)
expected=[5,9,10,14,15,18,19,20,23,24,25]+list(range(27,86))
assert improved==expected
print('R13_K5_C303_PROFILE_ENVELOPE_EXACT_PASS')
print('target_c =',c)
print('K5_upper_squared =',newB5sq)
print('q>=6 minimum =',q6[0],'profile',q6[1])
print('q>=6 margin =',Fraction(49,30)-5*c)
print('q4_profiles =',len(p4))
print('q5_profiles =',len(p5),p5)
print('finite block wins through n=85; universal takes over at n=86')
print('dimensions improved vs prior envelope =',len(improved))
print('improved =',improved)
