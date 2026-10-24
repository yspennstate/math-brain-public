from itertools import product

SIGNS = (-1, 1)
UNITS = ((1,0), (-1,0), (0,1), (0,-1))

def ga(x): return (x,0)
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
ZERO=(0,0)

def local_terminal_ok(a,b,c,d,tau):
    # c + tau(d-a) - b tau^2 = 0 in Z[i]
    v = sub(add(ga(c), mul(tau,ga(d-a))), mul(ga(b),mul(tau,tau)))
    return v == ZERO

def blocks(vals,p,q):
    n=p+q
    M=[list(vals[i*n:(i+1)*n]) for i in range(n)]
    A=[row[:p] for row in M[:p]]
    B=[row[p:] for row in M[:p]]
    C=[row[:p] for row in M[p:]]
    D=[row[p:] for row in M[p:]]
    return A,B,C,D

def membership(vals,p,q,r):
    A,B,C,D=blocks(vals,p,q)
    # R is q x p diagonal in its first p rows, with Gaussian-integer
    # diagonal entries r.  Test X upper, Y=0, Z lower exactly in Z[i].
    for i in range(p):
        for j in range(p):
            x=add(ga(A[i][j]), mul(ga(B[i][j]),r[j]))
            if i>j and x != ZERO:
                return False
    for i in range(q):
        for j in range(q):
            rb = mul(r[i],ga(B[i][j])) if i<p else ZERO
            z = sub(ga(D[i][j]),rb)
            if i<j and z != ZERO:
                return False
    for i in range(q):
        for j in range(p):
            dri = mul(ga(D[i][j]),r[j])
            ra = mul(r[i],ga(A[i][j])) if i<p else ZERO
            rbr = mul(mul(r[i],ga(B[i][j])),r[j]) if i<p else ZERO
            y = sub(sub(add(ga(C[i][j]),dri),ra),rbr)
            if y != ZERO:
                return False
    return True

def params_for_n(n):
    if n%2==0:
        m=n//2
        out=[]
        for pref in product(((1,0),(-1,0)), repeat=max(0,m-1)):
            for tau in UNITS:
                out.append(pref+(tau,))
        return m,m,out
    m=(n-1)//2
    return m,m+1,list(product(((1,0),(-1,0)), repeat=m))

def formula(n):
    if n%2==0:
        m=n//2
        return (2**(2*m*m))*(3**m)
    m=(n-1)//2
    return (2**(2*m*m+2*m+1))*(3**m)

plus={q for q in product(SIGNS, repeat=4) if local_terminal_ok(*q,(1,0))}
minus={q for q in product(SIGNS, repeat=4) if local_terminal_ok(*q,(-1,0))}
imagp={q for q in product(SIGNS, repeat=4) if local_terminal_ok(*q,(0,1))}
imagn={q for q in product(SIGNS, repeat=4) if local_terminal_ok(*q,(0,-1))}
print("terminal_real_plus:",len(plus))
print("terminal_real_minus:",len(minus))
print("terminal_real_intersection:",len(plus & minus))
print("terminal_imag_plus:",len(imagp))
print("terminal_imag_minus:",len(imagn))
print("terminal_imag_equal:",imagp==imagn)
print("terminal_real_imag_disjoint:",len((plus|minus)&imagp)==0)
print("terminal_unit_union:",len(plus|minus|imagp|imagn))
assert (len(plus),len(minus),len(plus&minus))==(6,6,4)
assert imagp==imagn and len(imagp)==4
assert not ((plus|minus)&imagp)
assert len(plus|minus|imagp|imagn)==12

for n in (2,3,4):
    p,q,params=params_for_n(n)
    union=0
    mult={}
    for vals in product(SIGNS, repeat=n*n):
        c=sum(1 for r in params if membership(vals,p,q,r))
        if c:
            union += 1
            mult[c]=mult.get(c,0)+1
    f=formula(n)
    print(f"n={n}: exact_union={union}, formula={f}, multiplicities={dict(sorted(mult.items()))}")
    assert union==f
print("SIGNED_SHEAR_ALL_SMALL_CASES_PASS")
