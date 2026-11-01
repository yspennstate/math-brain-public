"""Independent direct Walsh sums and exact source/physical-kernel audit."""
from fractions import Fraction as F
from pathlib import Path
import json, time
R=Path(__file__).resolve().parents[1]
start=time.monotonic()
checks=0
def ck(b):
    global checks
    checks+=1
    if not b: raise AssertionError(checks)

# Direct character sums; no FWHT or imported certificate values.
v=[]
for x in range(256):
    z=1-2*((x>>2)&1)
    y=1-2*((x>>3)&1)
    b=1-2*((((x>>4)&1)*((x>>5)&1)+((x>>6)&1)*((x>>7)&1))%2)
    v.append(y*b if x&3==0 else z)
a={s:F(sum(v[x]*(-1)**((x&s).bit_count()%2) for x in range(256)),256) for s in range(256)}
a={s:t for s,t in a.items() if t}
p={s:t*t for s,t in a.items()}
ck(len(p)==68)
ck(sum(p.values())==1)
qref={s:(F(1,2) if s==4 else F(1,12) if s&4 else F(1,256)) for s in p}
ck(sum(qref.values())==1)
ck(set(qref)==set(p))
# Exact macro CE<=7/2: clear all weights by 256 and exponentiate.
prod=1
for s,w in p.items():
    e=w*256
    ck(e.denominator==1)
    ck(qref[s].numerator==1)
    prod*=qref[s].denominator**int(e)
ck(prod<=2**896)

# q=1/2 reference uses absolute Walsh coefficients, hence all rational.
Z=sum(abs(t) for t in a.values())
rq={s:abs(t)/Z for s,t in a.items()}
ck(Z==F(11,2))
ck(Z>=4)  # exact normalizer lower exponent E_2=2
ck(sum(rq.values())==1)
for child_ref in [qref,rq]:
    raw={1:{},-1:{}}
    for s,t in a.items():
        # X Fourier pair (t/2,t/2), Y pair (t/2,-t/2).
        for owner,aa,bb in [('X',t/2,t/2),('Y',t/2,-t/2)]:
            true_pair=aa*aa+bb*bb
            ref_pair=child_ref[s]/2
            for e in [-1,1]:
                kap=(aa+e*bb)**2/(2*true_pair)
                raw[e][(owner,s)]=ref_pair*kap
                ck(kap in [0,1])
    for e,owner in [(1,'X'),(-1,'Y')]:
        zq=sum(raw[e].values())
        ck(zq==F(1,2))
        for s in a:
            ck(raw[e][(owner,s)]/zq==child_ref[s])
            other='Y' if owner=='X' else 'X'
            ck(raw[e][(other,s)]==0)

for k in range(2,21):
    d=F(1,1<<k);m=2*((1<<k)-k)
    upper=3+2*d-(k+1)*d*d
    ck(upper<=F(7,2))
    ck(upper+2<=F(11,2))
    # General remaining-guard source bound; never used as a free reset.
    for r in range(1,k+1):
        dr=F(1,1<<r);I=1+dr*(F(m,2)+r)
        ceupper=1+2*dr-(r+1)*dr*dr+dr*m+2*r*dr
        ck(ceupper==2*I-1+2*dr-(r+1)*dr*dr)
        ck(ceupper<=2*I)

data={'status':'PASS','checks':checks,'seconds':time.monotonic()-start,
      'method':'direct 256x256 Walsh matrix; independent rational physical pair kernels; integer CE inequality',
      'normalizer_q_half':'11/2','macro_CE_certificate':'product(1/Q)^(256P)<=2^896',
      'selector_outcomes':'1/2,1/2, exact inherited children, for macro and q=1/2 references',
      'scope':'k=2 full spectrum; k=2..20 scalar/macro bounds; general proof is in DERIVATION.md'}
(R/'out/AUDIT_RESULTS.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps(data))
