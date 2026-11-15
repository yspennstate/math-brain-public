"""Exact quadratic certificates, arithmetic in Q, Q(sqrt(5)), Q(2cos(2pi/7))."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import itertools
import time
import sympy as s

START=time.monotonic()

def run(n,top):
    m=n//2
    K=s.QQ if n==6 else s.QQ.algebraic_field(s.sqrt(5) if n==5 else 2*s.cos(2*s.pi/7))
    def F(x):return K.from_sympy(s.sympify(x))
    Z,O=F(0),F(1)
    def rat(a,b=1):return F(s.Rational(a,b))
    def sign(x):
        # Exact real algebraic comparison, no floating-point sign decisions.
        expr=K.to_sympy(x)
        if x==Z:return 0
        if expr.is_positive is True:return 1
        if expr.is_negative is True:return -1
        return 1 if s.polys.numberfields.to_number_field(expr).to_root().is_positive else -1
    def dot(a,b):return sum((x*y for x,y in zip(a,b)),Z)
    def show(x):return str(s.simplify(K.to_sympy(x)))
    def poly(x):
        if n==6:return K.to_sympy(x)
        coeffs=[s.Rational(c.numerator,c.denominator) for c in x.to_list()]
        return s.Poly.from_list(coeffs,s.Symbol('t')).as_expr() if coeffs else s.Integer(0)
    def lower(x):
        if n==6:return K.to_sympy(x)
        lo,hi=(s.Rational(2236,1000),s.Rational(2237,1000)) if n==5 else (s.Rational(1246,1000),s.Rational(1247,1000))
        p=s.Poly(poly(x),s.Symbol('t'))
        return sum(c*(lo**e[0] if c>=0 else hi**e[0]) for e,c in p.terms())
    co={r:F(s.cos(2*s.pi*r/n).expand(trig=True)) for r in range(n)}
    eig={k:[rat(2,n)*(O-co[(k*r)%n]) for r in range(1,m+1)] for k in range(1,m+1)}
    dims={k:1 if 2*k==n else 2 for k in range(1,m+1)}
    D=sum(dims[k] for k in top)
    a=top[0]
    eqs=[([O]*m,O)]
    for k in top[1:]:eqs.append(([x-y for x,y in zip(eig[a],eig[k])],Z))
    inequalities=[]
    for r in range(m):inequalities.append([O if j==r else Z for j in range(m)])
    for k in range(1,m+1):
        if k not in top:inequalities.append([x-y for x,y in zip(eig[a],eig[k])])
    def solve(rows):
        A=[list(row)+[rhs] for row,rhs in rows]
        for j in range(m):
            piv=next((i for i in range(j,m) if A[i][j]!=Z),None)
            if piv is None:return None
            A[j],A[piv]=A[piv],A[j]
            v=A[j][j];A[j]=[x/v for x in A[j]]
            for i in range(m):
                if i!=j:
                    v=A[i][j];A[i]=[x-v*y for x,y in zip(A[i],A[j])]
        return tuple(row[-1] for row in A)
    vertices=[]
    for inds in itertools.combinations(range(len(inequalities)),m-len(eqs)):
        v=solve(eqs+[(inequalities[i],Z) for i in inds])
        if v is not None and all(sign(dot(row,v))>=0 for row in inequalities) and v not in vertices:
            vertices.append(v)
    def T(x):
        lam=dot(eig[a],x);h=(n-1)*lam-F(2)
        p=[sum((rat(dims[k],n)*co[(k*r)%n] for k in top),Z) for r in range(1,m+1)]
        w=[x[r-1]*rat(2 if 2*r==n else 1,n) for r in range(1,m+1)]
        S1=F(D)*(F(2)*lam-rat(4,n)-F(2)*dot(x,w))
        S2=rat(D,n)*h
        S3=sum((x[r]*(rat(2*D,n*n)*h-F(2)*p[r]*(w[r]-lam/F(n))) for r in range(m)),Z)
        S5=sum((x[r]*(rat(2*D,n)-F(2)*p[r])*(F(2)*lam-rat(4,n)-F(2)*w[r]) for r in range(m)),Z)
        c=rat(2*n,n-2)
        return S1+c*(lam*S2-S3)+(O-lam)/F(n-2)*(F(D)*h-c*S2)-F(2)*S5
    values=[T(v) for v in vertices]
    q=[]
    for i in range(len(vertices)):
        row=[]
        for j in range(len(vertices)):
            mid=tuple((x+y)/F(2) for x,y in zip(vertices[i],vertices[j]))
            row.append(F(2)*T(mid)-(values[i]+values[j])/F(2))
        q.append(row)
    print('n',n,'top',top,'D',D,'vertices',len(vertices),flush=True)
    for i,v in enumerate(vertices):print('v',i,[show(x) for x in v],flush=True)
    print('coefficient signs',[[sign(x) for x in row] for row in q],flush=True)
    print('coefficient approximate',[[round(float(K.to_sympy(x).evalf()),12) for x in row] for row in q],flush=True)
    assert all(lower(x)>=0 for row in q for x in row), 'Rational interval certificate failed'
    with open('circulant_certificate.txt','a') as f:
        f.write(f'\nn={n}, top={top}, D={D}\n')
        for i,v in enumerate(vertices):f.write(f'v{i} = '+str([show(x) for x in v])+'\n')
        for i,row in enumerate(q):f.write('q'+str(i)+' = '+str([show(x) for x in row])+'\n')
        f.write('EXACT SIGNS '+str([[sign(x) for x in row] for row in q])+'\n')
    with open('circulant_polynomial_certificate.txt','a') as f:
        f.write(f'\nn={n}, top={top}, D={D}\n')
        for i,v in enumerate(vertices):f.write(f'v{i} = '+str([str(poly(x)) for x in v])+'\n')
        for i,row in enumerate(q):f.write('q'+str(i)+' = '+str([str(poly(x)) for x in row])+'\n')
        if any(x!=Z for row in q for x in row):
            f.write('Smallest rational interval lower bound for nonzero coefficients: '+str(min(lower(x) for row in q for x in row if x!=Z))+'\n')
    return dict(certified=all(sign(x)>=0 for row in q for x in row),
                field=K,vertices=vertices,T=T,top=top,n=n)

if __name__=='__main__':
    checks=[run(n,top) for n,top in [(5,(1,)),(6,(1,)),(6,(2,)),(6,(1,3)),(6,(2,3)),(7,(1,))]]
    flags=[r['certified'] for r in checks]
    print('ALL CERTIFIED:',all(flags),'runtime',time.monotonic()-START,flush=True)
    with open('LOG.md','a') as f:f.write('\n## 4. Exact small-circulant certificates\n\n'+str(flags)+'; runtime '+str(time.monotonic()-START)+' seconds. Exact coefficients saved in circulant_certificate.txt.\n')
