"""Second entropy implementation for EVERY declared shared-coordinate root."""
import hashlib,itertools,json,sys,time
from pathlib import Path
from fractions import Fraction as F
from independent import entropy,ln
R=Path(__file__).resolve().parents[1]; O=R/'out'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,z):p.write_bytes((json.dumps(z,indent=2)+'\n').encode('utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def lower(d):return sum((v*ln(q)[0 if v>=0 else 1] for q,v in d.items()),F(0))
def freeze():
    save(O/'audit_spec.json',dict(helper_version='A017-all-root-direct-audit-v1',helper_sha256=sha(Path(__file__)),entropy_helper_sha256=sha(R/'code/independent.py'),
      family='EXACT SAME frozen2560 b*c descriptions, re-enumerated independently',domain='10 triples of original1..5, all256 truth tables; original query0',case_count=2560,
      symmetry='none; duplicates kept',arithmetic='Direct integer character sums for root AND BOTH children; Fraction;256-term unreduced logarithms with proved remainder',
      pilot='First16 descriptions',memory_estimate_MB=70,max_runtime_seconds=300,pilot_max_runtime_seconds=60))
    print('FROZEN direct audit:2560 roots/BOTH children;70MB;300s')
def main(pilot):
    spec=read(O/'audit_spec.json');assert spec['helper_sha256']==sha(Path(__file__)) and spec['entropy_helper_sha256']==sha(R/'code/independent.py')
    start=time.monotonic(); source=read(O/'source_b.json')['truth_table']; primary=read(O/'certificate.json')['rows']
    base={2:F(-11,4),5:F(25,32),3:F(9,8)}; rows=checks=0; noncharacters=0
    for J in itertools.combinations(range(1,6),3):
        for code in range(256):
            if pilot and rows>=16:break
            local=[-1 if code&(1<<s) else 1 for s in range(8)]
            f=[]
            for x in range(64):
                index=0
                for k,j in enumerate(J):
                    if x&(1<<j):index+=2**k
                f.append(source[x]*local[index])
            a,b=f[::2],f[1::2];delta=entropy(f)
            for child in (a,b):
                for q,c in entropy(child).items():delta[q]=delta.get(q,F(0))-c/2
            delta={q:c for q,c in delta.items() if c}
            row=primary[rows];assert row['subset']==list(J) and row['multiplier_code']==code
            assert row['delta']=={str(q):str(c) for q,c in delta.items()}
            assert sum(x!=y for x,y in zip(a,b))==4
            gap=dict(base)
            for q,c in delta.items():gap[q]=gap.get(q,F(0))-c
            assert lower(gap)>=0
            # A local character has precisely one nonzero direct Fourier coefficient.
            noncharacters+=sum(sum(v*(-1 if (s&mask).bit_count()%2 else 1) for s,v in enumerate(local))!=0 for mask in range(8))!=1
            checks+=4;rows+=1
            assert time.monotonic()-start<(60 if pilot else 300)
        if pilot:break
    # Deliberately underpriced positive control: actual base debit exceeds4p.
    small=dict(base);small[2]-=F(1,2);assert lower(small)>0;checks+=1
    assert rows==(16 if pilot else 2560)
    result=dict(status='PASS',pilot=pilot,roots=rows,full_children=2*rows,checks=checks,noncharacter_descriptions=noncharacters,
      elapsed_seconds=time.monotonic()-start,scope='Separate author direct-character reconstruction of ALL frozen overlap descriptions; external review pending')
    save(O/('audit_pilot.json' if pilot else 'independent_full.json'),result);print(json.dumps(result))
if __name__=='__main__':
    if '--freeze' in sys.argv:freeze()
    else:main('--pilot' in sys.argv)
