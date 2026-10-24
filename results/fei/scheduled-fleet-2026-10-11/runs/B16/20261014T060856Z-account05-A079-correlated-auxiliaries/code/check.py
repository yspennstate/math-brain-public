"""Independent physical-height endpoint and nonproduct boundary checks; no author imports."""
import itertools, json, math, time
from pathlib import Path
from fractions import Fraction as Q

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out'; OUT.mkdir(exist_ok=True)

def walsh(a):
    a=list(a); stride=1
    while stride<len(a):
        for j in range(0,len(a),2*stride):
            for i in range(j,j+stride):
                u,v=a[i],a[i+stride]; a[i],a[i+stride]=u+v,u-v
        stride*=2
    return a

def product_info(W):
    n=(len(W)-1).bit_length(); sq=[v*v for v in W]; tot=sum(sq)
    if not tot: return None
    margins=[sum(v for s,v in enumerate(sq) if (s>>i)&1) for i in range(n)]
    for s,v in enumerate(sq):
        num=math.prod(margins[i] if (s>>i)&1 else tot-margins[i] for i in range(n))
        if v*tot**(n-1)!=num: return None
    fair=sum(2*b==tot for b in margins)
    nonfair=sum(b not in (0,tot) and 2*b!=tot for b in margins)
    return fair,nonfair,margins,tot

assertions=0
def ck(test):
    global assertions
    assertions+=1
    assert test

def endpoints():
    count=0; product=0; norms={}
    # P=8,k=25: enumerate ALL physical supports/signs modulo global negation.
    # Sign at the unique modulus-one point is fixed positive; no other symmetry.
    for mixed in range(8):
        for zero in range(8):
            if mixed==zero: continue
            pure=[j for j in range(8) if j not in (mixed,zero)]
            for signs in itertools.product((-1,1),repeat=6):
                h=[0]*8; h[mixed]=1
                for j,s in zip(pure,signs): h[j]=2*s
                W=walsh(h); count+=1
                ck(sum(v*v for v in h)==25)
                A=sum(v*v*(-1)**j.bit_count() for j,v in enumerate(h))
                ck(A in (-7,-1,1,7))
                ck(sum(W[s]*W[s^7] for s in range(8))==8*A)
                info=product_info(W)
                if info is not None:
                    product+=1
                    ck(not (info[0]==1 and info[1]==2))
                norms[A]=norms.get(A,0)+1
    ck(count==3584); ck(product==0)
    # Entire remaining N=3,m=2 endpoint, symbolic signs disappear in squares.
    for mixed in range(32):
        hsq=[4]*32; hsq[mixed]=1
        A=sum(v*(-1)**j.bit_count() for j,v in enumerate(hsq))
        ck(A==-3*(-1)**mixed.bit_count())
        ck((32*A)%27!=0)
    # All-N induction, finite arithmetic only verifies the base and multiplier.
    ck(5**4>2*4**4); ck(5*4>4*4)
    ck(5**3>4*2**4); ck(5**2>4*2**2)
    # Exhaust reduced one-coordinate physical height pairs, arbitrary scaling.
    exceptions=[]
    for h in itertools.product(range(-2,3),repeat=2):
        W=walsh(h); info=product_info(W)
        if info and info[1]:
            a,b=sorted(map(abs,W)); g=math.gcd(a,b)
            ck((a//g,b//g)==(1,3))
            ck(sorted(map(abs,h))==[1,2])
            exceptions.append(h)
    return {'physical_norm25_cases_mod_global_sign':count,'product_rows':product,
            'signed_square_moments':norms,'norm125_mixed_locations':32,
            'one_coordinate_exception_pairs':len(exceptions)}

def actual_fixture(F,addr=2):
    N=len(F); n=(N-1).bit_length(); P=N>>addr
    rows=[]
    for j in range(1<<addr):
        h=[sum(F[(y<<addr)|x]*(-1)**(x&j).bit_count() for x in range(1<<addr))//2 for y in range(P)]
        W=walsh(h); rows.append((h,W))
    for y in range(P):
        absrow=sorted(abs(h[y]) for h,W in rows)
        ck(absrow in ([0,0,0,2],[1,1,1,1]))
    full=walsh(F)
    for j,(h,W) in enumerate(rows):
        for s,v in enumerate(W): ck(full[(s<<addr)|j]==2*v)
    specI=Q(sum(v*v*s.bit_count() for s,v in enumerate(full)),N*N)
    edges=Q(sum(F[x]!=F[x^(1<<i)] for x in range(N) for i in range(n)),N)
    ck(specI==edges)
    return rows,specI

def boundary():
    # Search ONLY actual Boolean 3-bit data gates for genuine nonproduct law
    # whose two branches in at least one physical coordinate are both product.
    candidates=[]
    for code in range(128):  # global output sign fixed F(0)=+1
        g=[1]+[1 if (code>>(x-1))&1 else -1 for x in range(1,8)]
        W=walsh(g)
        if product_info(W) is not None: continue
        for bit in range(3):
            branches=[[W[s] for s in range(8) if ((s>>bit)&1)==b] for b in (0,1)]
            if all(product_info(a) is not None for a in branches):
                candidates.append((code,bit,g,W,branches))
    ck(bool(candidates))
    code,bit,g,W,branches=candidates[0]
    F=[g[x>>2] for x in range(32)]
    rows,I=actual_fixture(F)
    ck(product_info(rows[0][1]) is None)
    ck(all(all(v==0 for v in h) for h,w in rows[1:]))
    return {'candidate_count':len(candidates),'data_code':code,'branch_coordinate':bit,
            'data_truth':g,'raw_data_Walsh':W,'frequency_branch_coefficients':branches,
            'I':str(I),'address_masses':['1','0','0','0'],
            'purpose':'Actual nonproduct two-product-branch terminal; no new all-dimensional payment claimed.'}

def main():
    start=time.perf_counter()
    result={'endpoints':endpoints(),'nonproduct_boundary':boundary()}
    result.update(assertions=assertions,seconds=time.perf_counter()-start,status='PASS')
    (OUT/'validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
