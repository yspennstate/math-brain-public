from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from itertools import product
import json, math

P = 80
CELL_EPS_DEC = Decimal('2e-9')
CELL_EPS_RAT = F(2,10**9)
SHIFT_RAT = F(2,10**9)
OUTER_RADIUS_RAT = F(4,10**9)

def _down(fn):
    with localcontext() as c:
        c.prec=P; c.rounding=ROUND_FLOOR
        return +fn()
def _up(fn):
    with localcontext() as c:
        c.prec=P; c.rounding=ROUND_CEILING
        return +fn()
class IV:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=lo if isinstance(lo,Decimal) else Decimal(str(lo))
        self.hi=self.lo if hi is None else (hi if isinstance(hi,Decimal) else Decimal(str(hi)))
        if self.lo>self.hi: raise ValueError((self.lo,self.hi))
    def __add__(self,o):
        o=toiv(o); return IV(_down(lambda:self.lo+o.lo),_up(lambda:self.hi+o.hi))
    __radd__=__add__
    def __neg__(self): return IV(self.hi.copy_negate(),self.lo.copy_negate())
    def __sub__(self,o): return self+(-toiv(o))
    def __rsub__(self,o): return toiv(o)-self
    def __mul__(self,o):
        o=toiv(o); pairs=((self.lo,o.lo),(self.lo,o.hi),(self.hi,o.lo),(self.hi,o.hi))
        lows=[_down(lambda a=a,b=b:a*b) for a,b in pairs]
        highs=[_up(lambda a=a,b=b:a*b) for a,b in pairs]
        return IV(min(lows),max(highs))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi: raise ZeroDivisionError((self.lo,self.hi))
        vals_lo=[_down(lambda x=x:Decimal(1)/x) for x in (self.lo,self.hi)]
        vals_hi=[_up(lambda x=x:Decimal(1)/x) for x in (self.lo,self.hi)]
        return IV(min(vals_lo),max(vals_hi))
    def __truediv__(self,o): return self*toiv(o).inv()
    def __rtruediv__(self,o): return toiv(o)/self
    def contains_zero(self): return self.lo<=0<=self.hi
    def __repr__(self): return f'[{self.lo},{self.hi}]'
def toiv(x): return x if isinstance(x,IV) else IV(x)
class CIV:
    __slots__=('re','im')
    def __init__(self,re=0,im=0): self.re=toiv(re); self.im=toiv(im)
    def __add__(self,o): o=tociv(o); return CIV(self.re+o.re,self.im+o.im)
    __radd__=__add__
    def __neg__(self): return CIV(-self.re,-self.im)
    def __sub__(self,o): return self+(-tociv(o))
    def __rsub__(self,o): return tociv(o)-self
    def __mul__(self,o):
        o=tociv(o); return CIV(self.re*o.re-self.im*o.im,self.re*o.im+self.im*o.re)
    __rmul__=__mul__
    def conj(self): return CIV(self.re,-self.im)
def tociv(x):
    if isinstance(x,CIV): return x
    if isinstance(x,IV): return CIV(x,0)
    return CIV(x,0)
def det_dp(A):
    n=len(A); zero=CIV() if isinstance(A[0][0],CIV) else IV(0); one=CIV(1,0) if isinstance(A[0][0],CIV) else IV(1); dp={0:one}
    for i in range(n):
        nd={}
        for mask,val in dp.items():
            for j in range(n):
                if (mask>>j)&1: continue
                inv=(mask>>(j+1)).bit_count(); term=val*A[i][j]
                if inv&1: term=-term
                nm=mask|(1<<j); nd[nm]=nd.get(nm,zero)+term
        dp=nd
    return dp[(1<<n)-1]
def matmul(A,B):
    n=len(A); m=len(B[0]); k=len(B); iscomplex=isinstance(A[0][0],CIV) or isinstance(B[0][0],CIV); z=CIV() if iscomplex else IV(0)
    return [[sum((A[i][r]*B[r][j] for r in range(k)),z) for j in range(m)] for i in range(n)]
def trace(A):
    z=CIV() if isinstance(A[0][0],CIV) else IV(0); return sum((A[i][i] for i in range(len(A))),z)
def minor2_det(A,rows,cols): return A[rows[0]][cols[0]]*A[rows[1]][cols[1]]-A[rows[0]][cols[1]]*A[rows[1]][cols[0]]
def adj3(A):
    out=[[CIV() for _ in range(3)] for __ in range(3)]
    for i in range(3):
        for j in range(3):
            rows=[r for r in range(3) if r!=j]; cols=[c for c in range(3) if c!=i]; cof=minor2_det(A,rows,cols)
            if (i+j)&1: cof=-cof
            out[i][j]=cof
    return out
def ln_bound(x,lower):
    with localcontext() as c:
        c.prec=P+30; y=x.ln(); guard=Decimal(1).scaleb(-(P+10)); y=y-guard if lower else y+guard
    with localcontext() as c:
        c.prec=P; c.rounding=ROUND_FLOOR if lower else ROUND_CEILING; return +y
def log_iv(x):
    x=toiv(x)
    if x.lo<=0: raise ValueError(('log domain',x))
    return IV(ln_bound(x.lo,True),ln_bound(x.hi,False))
def D(q): return Decimal(q.numerator)/Decimal(q.denominator)
def box(q):
    qd=D(q); return IV(_down(lambda:qd-CELL_EPS_DEC),_up(lambda:qd+CELL_EPS_DEC))

BASE=[
    [(F(6102,10000),F(0)), (F(2921,10000),F(1627,10000)), (F(-521,10000),F(3138,10000))],
    [(F(2921,10000),F(-1627,10000)), (F(5485,10000),F(0)), (F(975,10000),F(-809,10000))],
    [(F(-521,10000),F(-3138,10000)), (F(975,10000),F(809,10000)), (F(3343,10000),F(0))],
]
leadJ=[F(3051,5000),F(222901,10**6),F(7471243,10**12)]
leadK=[F(1949,5000),F(64201,10**6),F(11028757,10**12)]
detJ=leadJ[-1]; trJ=F(14930,10000); detK=leadK[-1]; trK=F(15070,10000)
center_lower_J=4*detJ/(trJ*trJ); center_lower_K=4*detK/(trK*trK)
assert center_lower_J > F(1,100000) and center_lower_K > F(1,100000)
assert F(1,100000)-4*OUTER_RADIUS_RAT > 0

def shifted_rat(bits):
    s=[SHIFT_RAT if b else -SHIFT_RAT for b in bits]
    R=[[tuple(x) for x in row] for row in BASE]
    for idx,i in enumerate((0,1,2)):
        re,im=R[i][i]; R[i][i]=(re+s[idx],im)
    k=3
    for i,j in ((0,1),(0,2),(1,2)):
        re,im=R[i][j]; re2=re+s[k]; im2=im+s[k+1]; k+=2
        R[i][j]=(re2,im2); R[j][i]=(re2,-im2)
    return R

def eval_cell(bits):
    Jrat=shifted_rat(bits)
    J=[[None]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            re,im=Jrat[i][j]
            if i==j: J[i][j]=CIV(box(re),IV(0))
            elif i<j: J[i][j]=CIV(box(re),box(im))
            else: J[i][j]=J[j][i].conj()
    for i,j in ((0,1),(0,2),(1,2)):
        assert not (J[i][j].re.contains_zero() and J[i][j].im.contains_zero())
    def shifted(mask):
        Q=[[CIV(J[i][j].re,J[i][j].im) for j in range(3)] for i in range(3)]
        for i in range(3):
            if not ((mask>>i)&1): Q[i][i]=Q[i][i]-1
        return Q
    atoms=[]; Qs=[]
    for mask in range(8):
        Q=shifted(mask); Qs.append(Q); z=det_dp(Q)
        if (3-mask.bit_count())&1: z=-z
        assert z.im.contains_zero(); atoms.append(z.re)
    min_atom_lower=min(x.lo for x in atoms)
    if not min_atom_lower>0: return {'ok':False,'reason':'atom','min_atom':str(min_atom_lower)}
    p=atoms
    c=[log_iv(p[2]*p[4]/(p[0]*p[6])), log_iv(p[1]*p[4]/(p[0]*p[5])), log_iv(p[1]*p[2]/(p[0]*p[3]))]
    tau=log_iv(p[0]*p[3]*p[5]*p[6]/(p[1]*p[2]*p[4]*p[7]))
    M=[[J[i][j]*tau for j in range(3)] for i in range(3)]
    for i in range(3): M[i][i]=M[i][i]+c[i]
    dz=det_dp(M); assert dz.im.contains_zero(); d=dz.re
    if not d.lo>0: return {'ok':False,'reason':'detM','detM':repr(d)}
    Es=[]
    for mask in range(1,8):
        E=adj3(Qs[mask])
        if (3-mask.bit_count())&1: E=[[-x for x in row] for row in E]
        Es.append(E)
    pp=p[1:]
    V=[[(pp[i] if i==j else IV(0))-pp[i]*pp[j] for j in range(7)] for i in range(7)]
    ME=[matmul(M,E) for E in Es]
    v=[]
    for a in range(7): z=trace(ME[a]); assert z.im.contains_zero(); v.append(z.re)
    T=[[None]*7 for _ in range(7)]
    for a in range(7):
        for b in range(7):
            z=trace(matmul(ME[a],ME[b])); assert z.im.contains_zero(); T[a][b]=z.re
    C=[[T[i][j]+d*V[i][j] for j in range(7)] for i in range(7)]
    detC=det_dp(C)
    if not detC.lo>0: return {'ok':False,'reason':'detC','detC':repr(detC)}
    Aug=[[None]*8 for _ in range(8)]
    for i in range(7):
        for j in range(7): Aug[i][j]=C[i][j]
        Aug[i][7]=v[i]
    for j in range(7): Aug[7][j]=v[j]
    Aug[7][7]=IV(2)
    phi=-det_dp(Aug)
    return {'ok':phi.lo>0,'reason':'phi' if phi.lo<=0 else 'ok','phi_lo':str(phi.lo),'phi_hi':str(phi.hi),'min_atom':str(min_atom_lower),'tau_lo':str(tau.lo),'tau_hi':str(tau.hi)}

def main():
    from multiprocessing import Pool
    x=Decimal('1.'+'1234567890'*12)
    primitive_tests=0
    for precision in (9,28,80):
        with localcontext() as ctx:
            ctx.prec=precision; iv=-IV(x)
        assert F(iv.lo)<=-F(x)<=F(iv.hi); primitive_tests+=1
    pairs=[('1.234567890123456789','1.333333333333333333','2.123456789','2.987654321'),('-3.125','-0.03125','0.125','8.0')]
    for precision in (9,28,80):
        for lo,hi,blo,bhi in pairs:
            a,b=IV(lo,hi),IV(blo,bhi); aa=[F(a.lo),F(a.hi)]; bb=[F(b.lo),F(b.hi)]
            with localcontext() as ctx:
                ctx.prec=precision
                cases=[(a+b,[u+v for u in aa for v in bb]),(a-b,[u-v for u in aa for v in bb]),(a*b,[u*v for u in aa for v in bb]),(a/b,[u/v for u in aa for v in bb])]
            for got,ex in cases:
                assert F(got.lo)<=min(ex) and F(got.hi)>=max(ex); primitive_tests+=1
    assert primitive_tests==27

    bitlist=list(product((0,1),repeat=9))
    with Pool(processes=8) as pool:
        results=pool.map(eval_cell,bitlist,chunksize=4)
    mins=[]; failures=[]; min_atom=None; worst_bits=None; worst_val=None
    for bits,r in zip(bitlist,results):
        if not r['ok']:
            failures.append({'bits':bits,**r})
        else:
            val=Decimal(r['phi_lo']); mins.append(val)
            if worst_val is None or val<worst_val:
                worst_val=val; worst_bits=bits
            ma=Decimal(r['min_atom']); min_atom=ma if min_atom is None else min(min_atom,ma)
    result={
        'status':'PASS' if not failures else 'FAIL',
        'primitive_tests':primitive_tests,
        'outer_coordinate_radius':'4e-9',
        'subdivision':'2 per coordinate, 512 closed cells, each radius 2e-9',
        'cells_total':512,
        'cells_certified':len(mins),
        'failures':failures[:5],
        'uniform_outer_spectral_margin_gt':str(F(1,100000)-4*OUTER_RADIUS_RAT),
        'union_min_atom_lower':str(min_atom) if min_atom is not None else None,
        'union_phi_lower':str(min(mins)) if mins and not failures else None,
        'worst_cell_bits':worst_bits,
        'global_phi_lower_bound':'UNMEASURED',
        'scope':'Local 9D cube only; not a global X095 certificate.'
    }
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
