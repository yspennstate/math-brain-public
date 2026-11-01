"""Essential exact checks for X054; no numerical search enters the proof."""
import json
from pathlib import Path
import sympy as s

checks = 0
def eq(a, b=0):
    global checks
    assert s.simplify(a-b) == 0, (a,b)
    checks += 1

l,m = s.symbols('l m', positive=True)
x=(1-l)*(1-m); w=l*m; u=l+m-2*l*m
g11=(1-m)**2/x+m*m/w+(1-2*m)**2/u
g22=(1-l)**2/x+l*l/w+(1-2*l)**2/u
g12=(1-l)*(1-m)/x+l*m/w+(1-2*l)*(1-2*m)/u
eq(g12,1/u)
eq(g11*g22-g12*g12,(l-m)**2/(x*w*u))
eq((l-m)**2,u*u-4*x*w)
U,R=s.symbols('U R',positive=True)
eq(1+U*(U*U-4*R*R)/(R*R)-(2*U+U*U/R-1)**2,
   U*U*(2*R+U)*(1-U-2*R)/(R*R))

a,b,c,d,r,zeta=s.symbols('a b c d r zeta',real=True)
# With zeta=2(b+sqrt(ac)), the diagonal part is one exact square.
eq(a*d*d+2*b*d*r+c*r*r-2*(b+s.sqrt(a*c))*d*r,
   a*d*d-2*s.sqrt(a*c)*d*r+c*r*r)
y,z,dy,dz=s.symbols('y z dy dz',positive=True)
eq(dy*dy/y+dz*dz/z,
   (dy+dz)**2/(y+z)+y*z/(y+z)*(dy/y-dz/z)**2)

I=s.I
K=s.Matrix([[s.Rational(1,5),s.Rational(1,10),I/20],
            [s.Rational(1,10),s.Rational(3,5),s.Rational(1,10)],
            [-I/20,s.Rational(1,10),s.Rational(4,5)]])
A=s.Matrix([[0,200,s.Rational(799,2)-400*I],
            [200,0,I],[s.Rational(799,2)+400*I,-I,0]])
p=[];q=[]
for mask in range(8):
    Q=K-s.diag(*[int(not(mask>>i&1)) for i in range(3)])
    sign=(-1)**(3-mask.bit_count())
    p.append(sign*Q.det())
    q.append(s.simplify(sign*s.trace(Q.adjugate()*A)))
    assert p[-1]>0; checks+=1
eq(sum(p),1);eq(sum(q));eq(A[0,0])
for j in [0,1,6,7]:eq(q[j])
eq(A.adjugate()[0,0],-1)
eq(s.re((K*A.adjugate())[0,0]),-s.Rational(151,5))
eq(p[2]*p[4]/(p[0]*p[6]),s.Rational(209,159))
eq(p[0]*p[3]*p[5]*p[6]/(p[1]*p[2]*p[4]*p[7]),
   s.Rational(34821,35321))
lower=s.Rational(15100,35321)-s.Rational(50,159)
assert lower>0;checks+=1
for B in [K,s.eye(3)-K]:
    for j in range(1,4):
        assert B[:j,:j].det()>0;checks+=1

# Check the three-pivot count aggregation versus the two triangle energies.
score=[q[i]/p[i] for i in range(8)]
FI=sum(q[i]**2/p[i] for i in range(8))
countsum=0
for k in range(3):
    for bit in [0,1]:
        for n in range(4):
            atoms=[j for j in range(8) if (j>>k&1)==bit and j.bit_count()==n]
            if atoms:
                mass=sum(p[j] for j in atoms)
                jet=sum(q[j] for j in atoms)
                countsum+=jet*jet/mass
triangle=0
for n in [1,2]:
    atoms=[j for j in range(8) if j.bit_count()==n]
    for aidx,j in enumerate(atoms):
        for h in atoms[:aidx]:
            triangle+=p[j]*p[h]/(p[j]+p[h])*(score[j]-score[h])**2
eq(3*FI,countsum+triangle)

out={'status':'PASS','exact_assertions':checks,
     'atoms_mask_order':[str(a) for a in p],
     'local_logarithmic_lower_bound':str(lower),
     'local_count_fisher':0,
     'local_curvature_positive':True,
     'full_concavity_claim':False}
Path(__file__).with_name('certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
