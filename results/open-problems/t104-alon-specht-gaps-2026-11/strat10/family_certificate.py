"""PROVED only by exact rational Bernstein controls; explicit pressure family."""
import json,itertools,math
from pathlib import Path
from fractions import Fraction as F
import sympy as S
from cells import lower_value,vector_from_record
from face_intervals import Interval as I
from cover_face import sqrt_enclosure
s=S.symbols('s');EPS=F(1,100)

def controls(poly,eps=EPS):
    p=S.Poly(poly,s);n=p.degree();cs=[S.Rational(p.nth(j))*S.Rational(eps.numerator,eps.denominator)**j for j in range(n+1)]
    return [sum(cs[j]*S.binomial(k,j)/S.binomial(n,j)for j in range(k+1))for k in range(n+1)]

def cert(expr,label):
    num,den=S.fraction(S.cancel(expr));power=0
    while S.Poly(num,s).nth(0)==0:num=S.cancel(num/s);power+=1
    # denominator sign fixed by its value at zero.
    if den.subs(s,0)<0:num,den=-num,-den
    nn,dd=controls(num),controls(den);assert min(nn)>0 and min(dd)>0,(label,nn,dd)
    return dict(name=label,zero_power=power,numerator_coefficients=[str(v)for v in S.Poly(num,s).all_coeffs()],denominator_coefficients=[str(v)for v in S.Poly(den,s).all_coeffs()],numerator_bernstein=list(map(str,nn)),denominator_bernstein=list(map(str,dd)))

def inv(v):assert v.lo>0;return I(1/v.hi,1/v.lo)
def div(x,y):return I.wrap(x)*inv(I.wrap(y))

def exclusions(eps=EPS,boxes_file='face_boxes.json'):
    si=I(0,eps);U=[I(-4),1+si,1+si,1-si,1-si];W=[0,1,-1,-1,1]
    tu=20+4*si.square();tw=I(4);a=div(5+si.square(),5+10*si-si.square());lam=(1+a)*F(1,2)
    rad=div(a.square(),lam.square()*tu*tw);root=I(sqrt_enclosure(rad.lo,10**15)[0],sqrt_enclosure(rad.hi,10**15)[1])
    boxes=[[(F(a),F(b))for a,b in c['box']]for c in json.load(open(boxes_file))]
    proofs=[]
    for edge in ((0,1),(0,2)):
        for k,j in(edge,edge[::-1]):
            first=[5*div(a,lam)*(div(U[k]*U[i],tu)+F(W[k]*W[i],4))for i in range(5)]
            second=[5*(U[k]*W[i]-W[k]*U[i])*root for i in range(5)]
            for rest in itertools.permutations([i for i in range(5)if i not in edge]):
                for sign in(-1,1):
                    x=[first[k],first[rest[0]],sign*second[rest[0]],first[rest[1]],sign*second[rest[1]],sign*second[j]]
                    indices=[]
                    for box in boxes:
                        inds=[i for i,(v,(lo,hi))in enumerate(zip(x,box))if v.hi<lo or hi<v.lo]
                        assert inds,(edge,k,rest,sign,box)
                        indices.append(inds[0])
                    proofs.append(dict(edge=list(edge),ordered=[k,j],rest=list(rest),sign=sign,coordinate_intervals=[[str(v.lo),str(v.hi)]for v in x],separating_coordinates=indices))
    return proofs

def build():
    U=[-4,1+s,1+s,1-s,1-s];W=[0,1,-1,-1,1];tu=20+4*s*s;tw=4
    assert sum(U)==sum(W)==sum(x*y for x,y in zip(U,W))==0
    A=sum(x**4 for x in U)/tu**2;B=S.Rational(1,4);C=sum(x*x*y*y for x,y in zip(U,W))/(tu*tw)
    aa=(5+s*s)/(5+10*s-s*s);lam=(1+aa)/2
    weights=[lam/5+aa*(U[i]*U[j]/tu+S.Rational(W[i]*W[j],tw))for i in range(5)for j in range(i+1,5)]
    Q=S.Matrix([[U[i]*U[j]/tu+S.Rational(W[i]*W[j],tw)for j in range(5)]for i in range(5)])
    L0=(S.eye(5)-S.ones(5)/5-Q).subs(s,0)
    expected=S.zeros(5)
    for i,j in ((1,4),(2,3)):
        expected[i,i]+=S.Rational(1,2);expected[j,j]+=S.Rational(1,2);expected[i,j]-=S.Rational(1,2);expected[j,i]-=S.Rational(1,2)
    assert L0==expected
    K=sum(Q[i,i]**2 for i in range(5));q=S.Matrix([Q[i,i]for i in range(5)])
    R=sum(v**3 for v in Q)+2*(q.T*Q*q)[0]
    dr=sum(x**3 for x in U);er=sum(x*x*y for x,y in zip(U,W));fr=sum(x*y*y for x,y in zip(U,W));hr=sum(x**3 for x in W)
    Rmom=3*dr**2/tu**3+S.Rational(3,tw**3)*hr**2+5*er**2/(tu**2*tw)+5*fr**2/(tu*tw**2)+4*dr*fr/(tu**2*tw)+4*er*hr/(tu*tw**2)
    assert S.cancel(R-Rmom)==0
    T=S.cancel(S.Rational(9,80)+aa*(11*K-4)/8+aa**2*(S.Rational(191,80)-S.Rational(35,8)*K+R))
    assert T.subs(s,0)==0
    records=[cert(T,'T6 at endpoint'),cert(1-aa,'connected endpoint: a<lambda'),cert(aa-S.Rational(14,25),'scale >14/25')]
    for i,w in enumerate(weights):
        if S.cancel(w)==0:assert i in (0,1)
        else:records.append(cert(w,'positive edge '+str(i)))
    bank=json.load(open('moment_cells.json'))+json.load(open('allN_optimized_cells.json'))
    for i,rec in enumerate(bank):
        if F(rec['rlo'])<=1<=F(rec['rhi']):
            records.append(cert(-lower_value((A,B,C),aa,F(1),vector_from_record(rec)),'negative inherited moment '+str(i)))
            if rec in bank[:10]:records.append(cert(aa-S.Rational(rec['ahi']),'scale above saved ceiling '+str(i)))
    from padding import base_coefficients
    base=base_coefficients((A,B,C),aa,F(1));C3=sum(v**3 for v in Q)
    allN=[16*T,base[1]+8*aa**2*R+4*aa**2*C3,base[2]+aa**2*R+aa**2*C3]
    records.extend(cert(expr,'all-N numerator coefficient '+str(i))for i,expr in enumerate(allN))
    chartproofs=exclusions()
    return dict(label='PROVED',eps=str(EPS),U=list(map(str,U)),W=W,r='1',a=str(aa),limit_L5=[[str(v)for v in L0.row(i)]for i in range(5)],T6=str(S.factor(T)),certificates=records,chart_exclusions=chartproofs)
if __name__=='__main__':
    data=build();Path('pressure_family.json').write_text(json.dumps(data,indent=2)+'\n')
    print('PROVED: explicit connected residual family, r=1, 0<s<=1/100; T6=',data['T6'],'tends to zero from above.',flush=True)
    with open('LOG.md','a')as f:f.write('\nPROVED (pressure_family.json; verify_family.py): explicit one-parameter connected zero-edge family lies in every condition of inherited (11), has T6>0 and T6 tends to 0 as s tends to 0. All weight, scale and moment-filter inequalities have exact univariate Bernstein certificates; all 48 endpoint charts are interval-excluded from every old box. OPEN: this does not exclude negative points elsewhere.\n')
