from pathlib import Path
from itertools import permutations
from fractions import Fraction as Q
import verify_continuum as arithmetic
import json,time,sys

RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'
EVEN=[sum(1<<x for x in range(16) if (x&S).bit_count()%2==0) for S in range(16)]
EDGE=[0x5555,0x3333,0x0f0f,0x00ff]
FACT2=[0,0,1,1,3]; FACT3=[0,0,0,1,1]

def orbit(t):
    ans=set()
    for perm in permutations(range(4)):
        for flip in range(16):
            out=0
            for x in range(16):
                if t>>x&1:
                    y=sum(((x>>j&1)^(flip>>j&1))<<perm[j] for j in range(4)); out|=1<<y
            ans.add(out); ans.add(out^65535)
    return ans

def main():
    limit=int(sys.argv[1]); start=time.monotonic(); l3,u3=arithmetic.log_bounds(Q(3)); equal=[]; strict=constants=0; smallest=None; worst=None
    for t in range(limit):
        if t%256==0: assert time.monotonic()-start<60
        ones=t.bit_count(); a=[2*ones-16]+[4*(t&M).bit_count()-2*ones for M in EVEN[1:]]
        sq=[v*v for v in a]; assert sum(sq)==256
        if limit<=256:
            direct=[sum((1 if t>>x&1 else -1)*(1 if (x&S).bit_count()%2==0 else -1) for x in range(16)) for S in range(16)]
            assert direct==a
        J=[sum(sq[S] for S in range(16) if S>>j&1) for j in range(4)]
        assert all(J[j]==32*(((t>>(1<<j))^t)&EDGE[j]).bit_count() for j in range(4))
        if not sum(J): constants+=1; continue
        J.sort(reverse=True); levels=[sum(sq[S] for S in range(16) if S.bit_count()==s) for s in range(5)]
        c2=6*(J[1]+2*J[3]-sum(levels[s]*FACT2[s] for s in range(5)))
        c3=6*(J[2]-sum(levels[s]*FACT3[s] for s in range(5)))
        den=5*sum(J); d2=43*den-80*c2; d3=19*den-80*c3
        if not d2 and not d3: equal.append(t); continue
        lower=Q(d2,80*den)+Q(d3,80*den)*(l3 if d3>=0 else u3)
        assert lower>0,(t,c2,c3,den,float(lower))
        strict+=1
        if smallest is None or lower<smallest: smallest=lower; worst=t
    if limit==65536: assert constants==2 and set(equal)==orbit(855) and len(equal)==96
    result={'truth_tables':limit,'constants':constants,'strict':strict,'equal':len(equal),'equality_masks':equal,'minimum_strict_gap_lower':str(smallest),'minimum_strict_gap_float':float(smallest),'closest_strict_truth':worst,'elapsed_seconds':time.monotonic()-start,'alpha4_coefficients':{'2':'43/80','3':'19/80'}}
    (OUT/f'raw_rank_{limit}.json').write_text(json.dumps(result,indent=2)); print({k:v for k,v in result.items() if k!='equality_masks'})

if __name__=='__main__': main()
