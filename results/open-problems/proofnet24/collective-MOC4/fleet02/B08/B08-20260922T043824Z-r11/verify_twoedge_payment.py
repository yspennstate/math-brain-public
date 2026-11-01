from fractions import Fraction as Q
from itertools import permutations

# Exact Gaussian rationals z=(re,im).
def add(z,w): return (z[0]+w[0], z[1]+w[1])
def sub(z,w): return (z[0]-w[0], z[1]-w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def scale(q,z): return (q*z[0], q*z[1])
def prod(xs):
    z=(Q(1),Q(0))
    for w in xs: z=mul(z,w)
    return z

def fmt(z):
    x,y=z
    if y==0: return str(x)
    return f"{x}{'+' if y>=0 else ''}{y}i"

# Previous B08 exposed 2+2 common-block witness:
# -a=(-3,-2,1-3i,1-2i), b=(-1,0,1,1+i), U0=diag(H,H).
a=[(Q(3),Q(0)),(Q(2),Q(0)),(Q(-1),Q(3)),(Q(-1),Q(2))]
b=[(Q(-1),Q(0)),(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1))]

def vertex(p):
    return prod(add(a[i],b[p[i]]) for i in range(4))

V={p:vertex(p) for p in permutations(range(4))}
assert max(z[1] for z in V.values()) == 0
assert sum(z[1] == 0 for z in V.values()) == 4
assert sum(z[1] < 0 for z in V.values()) == 20

# H has squared entries 1/2, so each 2x2 block determinant is the
# arithmetic mean of its two permutation products.
def block_det(rows, cols):
    i,j=rows; p,q=cols
    x=mul(add(a[i],b[p]),add(a[j],b[q]))
    y=mul(add(a[i],b[q]),add(a[j],b[p]))
    return scale(Q(1,2),add(x,y))

def endpoint(swaps):
    c=[0,1,2,3]
    for p,q in swaps:
        c[p],c[q]=c[q],c[p]
    return mul(block_det((0,1),(c[0],c[1])), block_det((2,3),(c[2],c[3])))

D00=endpoint([])
D13=endpoint([(0,2)])
D24=endpoint([(1,3)])
D1324=endpoint([(0,2),(1,3)])
D14=endpoint([(0,3)])
D23=endpoint([(1,2)])
D1423=endpoint([(0,3),(1,2)])

assert D00==(Q(-119,4),Q(0))
assert D13==(Q(-289,4),Q(-119,2))
assert D24==(Q(-105,4),Q(-43,2))
assert D1324==(Q(-87,4),Q(-104))
assert D14==(Q(-77,2),Q(-115,2))
assert D23==(Q(-85,2),Q(-35,2))
assert D1423==D1324

F13_24=prod([sub(a[0],a[1]),sub(a[2],a[3]),sub(b[2],b[0]),sub(b[3],b[1])])
F14_23=prod([sub(a[0],a[1]),sub(a[2],a[3]),sub(b[3],b[0]),sub(b[2],b[1])])
assert F13_24==(Q(-2),Q(2))
assert F14_23==(Q(-1),Q(2))

# For V=W=H, |kappa|=|v11*v21*w11*w21|=1/4.
kappa=Q(1,4)
# Support L=Im and M=0.
d13=-D13[1]; d24=-D24[1]; c13=kappa*abs(F13_24[1])
d14=-D14[1]; d23=-D23[1]; c14=kappa*abs(F14_23[1])
assert d13*d24-c13*c13 == Q(1279)
assert d14*d23-c14*c14 == Q(1006)

print('PASS MOC4-2PLUS2-TWOEDGE-PAYMENT-v1 finite witness check')
print('max_endpoint_imag = 0')
print('support_line_vertices = 4; strict_offblock_vertices = 20')
print('D00 =',fmt(D00))
print('D13 =',fmt(D13),'D24 =',fmt(D24),'D1324 =',fmt(D1324))
print('F13_24 =',fmt(F13_24),'delta13*delta24 =',d13*d24,'C^2 =',c13*c13,'margin =',d13*d24-c13*c13)
print('D14 =',fmt(D14),'D23 =',fmt(D23),'D1423 =',fmt(D1423))
print('F14_23 =',fmt(F14_23),'delta14*delta23 =',d14*d23,'C^2 =',c14*c14,'margin =',d14*d23-c14*c14)
