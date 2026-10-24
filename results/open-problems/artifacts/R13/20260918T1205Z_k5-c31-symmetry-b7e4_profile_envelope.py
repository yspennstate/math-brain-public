from fractions import Fraction as F
M=[0,5,16,29,48,61,80,101,128,133,144,157,176,189,208,229,256]
c=F(31,100)
prev_c=F(303,1000)
new_T2=1/c
old_T2=1/prev_c

def parts(total,q,lo=1):
    def rec(rem,k,mn,cur):
        if k==1:
            if rem>=mn: yield tuple(cur+[rem])
            return
        for x in range(mn, rem//k+1):
            yield from rec(rem-x,k-1,x,cur+[x])
    yield from rec(total,q,lo,[])

def energy(p): return sum(F(k*k,M[k]) for k in p)
q4=[p for p in parts(16,4) if energy(p)<5*c]
q5=[p for p in parts(16,5) if energy(p)<5*c]
q6min=min((energy(p),p) for q in range(6,17) for p in parts(16,q))
print('c=',c)
print('q4_profiles=',len(q4))
print('q4=',q4)
print('q5_profiles=',len(q5))
print('q5=',q5)
print('q_ge_6_min=',q6min)
assert q6min==(F(49,30),(1,1,1,1,4,8))
assert q6min[0]-5*c==F(1,12)
imp=[]
for n in range(5,86):
    bal=F(3*n,4)
    old=min(bal,old_T2*((n+4)//5))
    new=min(bal,new_T2*((n+4)//5))
    if new<old: imp.append(n)
print('improved_n=',imp)
print('improved_count=',len(imp))
assert imp==[5,9,10,13,14,15,18,19,20]+list(range(22,86))
assert F(1700,31) < 18*F(333,106)
assert F(1800,31) > 18*F(22,7)
assert F(3*86,4) > 18*F(22,7)
print('crossover=86 certified by 333/106 < pi < 22/7')
print('R13_K5_C31_PROFILE_ENVELOPE_EXACT_PASS')
