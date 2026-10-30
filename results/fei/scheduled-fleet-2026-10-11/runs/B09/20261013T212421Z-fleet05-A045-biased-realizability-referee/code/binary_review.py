from pathlib import Path
import json,itertools,time
from fractions import Fraction as Q
ROOT=Path(__file__).resolve().parents[1]
# Load only common exact definitions, not the gate-tax search driver.
text=(ROOT/'code/check.py').read_text(encoding='utf-8').split('\nms=')[0]
namespace={'__file__':str(ROOT/'code/check.py')}
exec(compile(text,'A045 shared exact definitions','exec'),namespace)
spectrum=namespace['spectrum'];product=namespace['product'];check=namespace['check']
def prime_ln(x):
    out={}
    for n,sign in [(x.numerator,1),(x.denominator,-1)]:
        d=2
        while d*d<=n:
            while n%d==0:out[d]=out.get(d,Q(0))+sign;n//=d
            d+=1
        if n>1:out[n]=out.get(n,Q(0))+sign
    return {p:c for p,c in out.items() if c}
def plus(a,b,s=Q(1)):
    z=dict(a)
    for p,c in b.items():z[p]=z.get(p,Q(0))+s*c
    return {p:c for p,c in z.items() if c}
def hp_exact(sp):
    _,ms,vs=sp;form={}
    for s,a in enumerate(ms):
        if s and a:form=plus(form,prime_ln(product(vs[i] for i in range(2) if s>>i&1)/a),a)
    return form
start=time.perf_counter();counts={'corner':0,'parity':0,'constant_or_literal':0}
bs=[Q(1,8),Q(1,3),Q(1,2),Q(2,3),Q(7,8)]
for table_id in range(16):
    table=[1 if table_id>>x&1 else -1 for x in range(4)]
    positives=[x for x in range(4) if table[x]==1]
    for p,q in itertools.product(bs,repeat=2):
        sp=spectrum(table,[p,q]);cs,ms,vs=sp;D=ms[3];actual=hp_exact(sp)
        if len(positives) in [1,3]:
            corner=positives[0] if len(positives)==1 else next(x for x in range(4) if x not in positives)
            u=p if corner&1 else 1-p;v=q if corner&2 else 1-q
            expected=plus({},prime_ln(Q(2)),2*D)
            expected=plus(expected,prime_ln(1/u),2*D*u/(1-u))
            expected=plus(expected,prime_ln(1/v),2*D*v/(1-v))
            check(D==4*u*(1-u)*v*(1-v));check(actual==expected);counts['corner']+=1
        elif len(positives)==2 and set(positives) in [{0,3},{1,2}]:
            a,b=vs;expected={}
            for w in [a,b]:
                if w!=1:expected=plus(expected,prime_ln(1/(1-w)),D*(1-w)/w)
            check(D==a*b);check(actual==expected);counts['parity']+=1
        else:
            check(D==0);check(actual=={});counts['constant_or_literal']+=1
out={'target':'A042-SHARP-BINARY-PRIME-ENDPOINT@1','verdict':'HOLDS_AT_STATED_SCOPE','cases':sum(counts.values()),'class_counts':counts,'assertions':namespace['ASSERTIONS'],'arithmetic':'Fraction spectra and exact prime-log coefficient equality','runtime_seconds':time.perf_counter()-start,'source_checker_not_used':True}
(ROOT/'out/BINARY_REVIEW_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
