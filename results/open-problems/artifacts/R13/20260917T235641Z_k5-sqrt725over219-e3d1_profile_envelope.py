from fractions import Fraction
from math import ceil
M=[0,5,16,29,48,61,80,101,128,133,144,157,176,189,208,229,256]
c=Fraction(219,725)

def parts(total,q,lo=1,prefix=()):
    if q==0:
        if total==0: yield prefix
        return
    for k in range(lo,total+1):
        if total-k<k*(q-1): break
        yield from parts(total-k,q-1,k,prefix+(k,))

def energy(p): return sum(Fraction(k*k,M[k]) for k in p)
mins={}
for q in range(4,17):
    arr=[(energy(p),p) for p in parts(16,q)]
    mins[q]=min(arr)
print('target_c=',c,'five_c=',5*c)
for q in range(4,17): print('q',q,'min',mins[q][0],'profile',mins[q][1])
assert mins[6][0]==Fraction(49,30)
assert mins[6][0] > 5*c
q5_sur=[(energy(p),p) for p in parts(16,5) if energy(p)<5*c]
q5_eq=[(energy(p),p) for p in parts(16,5) if energy(p)==5*c]
print('q5_strict_survivors=',q5_sur)
print('q5_equal_profiles=',q5_eq)
assert [p for e,p in q5_sur]==[(1,1,1,5,8),(1,1,2,4,8),(2,2,2,2,8),(2,2,4,4,4)]
assert sorted(p for e,p in q5_eq)==[(1,2,2,3,8),(1,3,4,4,4)]
assert Fraction(725,219) < Fraction(300,89)
# q=17 five-block square beats 18*pi using pi>333/106.
assert Fraction(17*725,219) < Fraction(18*333,106)
# q=18 five-block square is already worse than 18*pi using pi<22/7.
assert Fraction(18*725,219) > Fraction(18*22,7)
improved=[]
for n in range(5,86):
    bal=Fraction(3*n,4)
    old5=Fraction(300,89)*ceil(n/5)
    new5=Fraction(725,219)*ceil(n/5)
    if n<=80:
        old=min(bal,old5)
        new=min(bal,new5)
        if new<old: improved.append(n)
    else:
        improved.append(n)
print('improved_count=',len(improved))
print('improved=',improved)
assert improved==[5,9,10,14,15,18,19,20,23,24,25]+list(range(27,86))
print('R13_PROFILE_ENVELOPE_EXACT_PASS')
