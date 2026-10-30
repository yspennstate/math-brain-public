import argparse,json,time
from collections import Counter
from fractions import Fraction as Q
import search as s

def main(pilot):
    start=time.perf_counter();counts=Counter();minor=Counter();cases=0;bad=[]
    name='signature_pilot' if pilot else 'signatures'
    with (s.ROOT/('out/'+name+'.jsonl')).open('w',encoding='utf-8') as f:
        for M in ([1,2,3,4,32] if pilot else range(1,64)):
            for d in range(M%2,min(M,64-M)+1,2):
                a,b=(M+d)//2,(M-d)//2
                mask=sum(1<<(2*x) for x in range(a))+sum(1<<(2*x+1) for x in range(b))
                cs=s.fwht(s.truth(6,mask));assert cs[0]==64-2*M and cs[1]==-2*d
                p=Q(M,64);t=Q(d,32)**2;_,R=s.reserve(p,t);sig=s.sign(R)
                counts[sig]+=1
                if M<=32:minor[sig]+=1
                if sig=='negative' and M<=32:bad.append([M,d,mask])
                item={'M':M,'d':d,'actual_mask':mask,'p':str(p),'singleton_squared':str(t),'reserve_sign':sig,'reserve':s.pack(R)}
                f.write(json.dumps(item)+'\n');f.flush();cases+=1
                if time.perf_counter()-start>(55 if pilot else 600):raise RuntimeError('frozen runtime cap')
    assert cases==(25 if pilot else 559)
    result={'cases':cases,'reserve_sign_counts':dict(counts),'minority_orientation_counts':dict(minor),
            'minority_negative_examples':bad[:10],'runtime_seconds':time.perf_counter()-start,
            'helper_sha256':s.hashlib.sha256(__import__('pathlib').Path(__file__).read_bytes()).hexdigest(),
            'jsonl_sha256':s.hashlib.sha256((s.ROOT/('out/'+name+'.jsonl')).read_bytes()).hexdigest()}
    (s.ROOT/('out/'+name+'.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');main(ap.parse_args().pilot)
