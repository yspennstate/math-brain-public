from fractions import Fraction as Q
from itertools import permutations

# Exact Gaussian rational arithmetic: z=(Re z, Im z).
def add(z,w): return (z[0]+w[0], z[1]+w[1])
def sub(z,w): return (z[0]-w[0], z[1]-w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def scale(q,z): return (q*z[0], q*z[1])

a=[(10,-13),(-18,17),(-20,5),(-20,11)]
b=[(17,-18),(-22,3),(-19,-7),(2,7)]
(c1,s1)=(Q(3,5),Q(4,5))
(c2,s2)=(Q(7,25),Q(24,25))
(c3,s3)=(Q(7,25),Q(24,25))
# Common separating functional L(z)=3 Re(z)-8 Im(z).
def L(z): return 3*z[0]-8*z[1]

P=list(permutations(range(4)))
def name(p): return ''.join(str(j+1) for j in p)
def vertex(p):
    z=(Q(1),Q(0))
    for i,j in enumerate(p):
        z=mul(z,(Q(a[i][0]+b[j][0]),Q(a[i][1]+b[j][1])))
    return z
V={name(p):vertex(p) for p in P}

w0={
'1234':c1*c1*c2*c2*c3*c3,
'1243':c1*c1*c2*c2*s3*s3,
'1324':c1*c1*c3*c3*s2*s2,
'1423':c1*c1*s2*s2*s3*s3,
'2134':c2*c2*c3*c3*s1*s1,
'2143':c2*c2*s1*s1*s3*s3,
'3124':c3*c3*s1*s1*s2*s2,
'4123':s1*s1*s2*s2*s3*s3,
}
w1={
'1423':s1*s1*s2*s2*s3*s3,
'2413':c2*c2*s1*s1*s3*s3,
'2431':c2*c2*c3*c3*s1*s1,
'3421':c3*c3*s1*s1*s2*s2,
'4123':c1*c1*s2*s2*s3*s3,
'4213':c1*c1*c2*c2*s3*s3,
'4231':c1*c1*c2*c2*c3*c3,
'4321':c1*c1*c3*c3*s2*s2,
}
assert all(q>=0 for q in w0.values()) and sum(w0.values())==1
assert all(q>=0 for q in w1.values()) and sum(w1.values())==1

def combo(w):
    z=(Q(0),Q(0))
    for k,q in w.items(): z=add(z,scale(q,V[k]))
    return z
D0=combo(w0); D1=combo(w1)
alpha=c1*s1*s2*s3
K=scale(alpha,sub(V['4123'],V['1423']))

values={k:L(z) for k,z in V.items()}
M=max(values.values())
tops=[k for k,v in values.items() if v==M]
A=L(D0); B=L(D1); C=L(K)
delta0=M-A; delta1=M-B
payment=delta0*delta1-C*C
ratio2=C*C/(delta0*delta1)

assert len(set(a))==4 and len(set(b))==4
assert all((a[i][0]+b[j][0],a[i][1]+b[j][1])!=(0,0) for i in range(4) for j in range(4))
assert tops==['2143']
assert delta0>0 and delta1>0 and payment>0
assert ratio2<1

# A rational real closing rotation near the support-maximizing angle.
c4,s4=Q(2849,3649),Q(2280,3649)
assert c4*c4+s4*s4==1
h4=c4*c4*A+s4*s4*B+2*c4*s4*C
gap4=M-h4
assert gap4>0

print('spectra_a =', a)
print('spectra_b =', b)
print('all_spectra_distinct = True')
print('all_16_pair_sums_nonzero = True')
print('support_L = 3*Re - 8*Im')
print('unique_vertex_max =', tops[0])
print('M =', M)
print('D0 =', D0)
print('D1 =', D1)
print('K =', K)
print('A=L(D0) =', A)
print('B=L(D1) =', B)
print('C=L(K) =', C)
print('delta0 =', delta0)
print('delta1 =', delta1)
print('delta0*delta1-C^2 =', payment)
print('C^2/(delta0*delta1) =', ratio2)
print('rational_final_rotation =', (c4,s4))
print('exact_gap_for_that_rotation =', gap4)
print('PASS')
