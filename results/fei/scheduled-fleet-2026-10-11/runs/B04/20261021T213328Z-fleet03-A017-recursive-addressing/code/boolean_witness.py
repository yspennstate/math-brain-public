"""Independent direct-character reconstruction; frozen exact finite domain."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,time,hashlib
R=Path(__file__).resolve().parents[1]
def direct(v):
    return [sum(a*(-1 if (s&x).bit_count()%2 else 1) for x,a in enumerate(v)) for s in range(len(v))]
def ratio(pairs):
    p=q=1
    for a,b in pairs:
        t,u=a*a,b*b
        if t+u:p*= (t+u)**(t+u)
        if t:q*=t**t
        if u:q*=u**u
    return p,q
def build(words):
    # Child coordinates u=t+4*z; selector is the lowest parent bit.
    child=[(-1 if t==3 else 1) if z==0 else words[z][t] for z in range(8) for t in range(4)]
    return [child[u]*(-1 if s and u//4==0 else 1) for u in range(32) for s in range(2)]
def ledger(f):
    w=direct(f)
    assert all(a%4==0 for a in w)
    pairs=[(w[j]//4,w[j+1]//4) for j in range(0,64,2)]
    inf=[Fraction(sum(f[x]!=f[x^(1<<i)] for x in range(64)),64) for i in range(6)]
    assert [sum(w[s]**2 for s in range(64) if s>>i&1) for i in range(6)]==[v*4096 for v in inf]
    return w,pairs,inf,ratio(pairs)
def main():
    start=time.perf_counter();sigma=[1,1,1,-1]; words={}
    for z in range(1,8):
        row=z if z<4 else 0
        sign=1 if z<4 else (-1 if (z&3)==3 else 1)
        words[z]=[sigma[row]*sign*(-1 if (row&t).bit_count()%2 else 1) for t in range(4)]
    f=build(words);w,pairs,inf,(p,q)=ledger(f)
    assert inf[0]==Fraction(1,8)
    assert Counter(a*a for a,b in pairs)=={4:24,16:8}
    assert all(b*b==1 for a,b in pairs)
    assert p>q<<128 and 17**136*5**120>2**832
    # Query a maximum physical influence; five-control descendants fall under
    # the separately proved generic five-control good-coordinate policy.
    pivot=max(range(6),key=lambda i:inf[i]);pairs2=[]
    for s in range(64):
        if s>>pivot&1:continue
        pairs2.append((w[s]//4,w[s|1<<pivot]//4))
    pp,qq=ratio(pairs2)
    threshold=1024*inf[pivot]
    assert threshold.denominator==1 and pp<=qq<<threshold.numerator
    out={'status':'ACTUAL_BOOLEAN_LOCAL_COUNTEREXAMPLE','truth_table':f,'negative_vertices':[i for i,v in enumerate(f) if v<0],
         'child_affine_words':words,'influences':[str(v) for v in inf],
         'selected_B_exact':'(136 log2(17)+120 log2(5)-704)/256',
         'selected_B_greater_than_4Inf_integer_slack':str(17**136*5**120-2**832),
         'selected_entropy_integer_ratio':{'P':str(p),'Q':str(q)},
         'maximum_influence_pivot':pivot,'repair_B_at_most_4Inf':True,
         'repair_integer_slack':str((qq<<threshold.numerator)-pp),
         'elapsed_seconds':time.perf_counter()-start}
    (R/'out/boolean_counterexample.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in out.items() if k in ['status','influences','selected_B_exact','maximum_influence_pivot','elapsed_seconds']}))
if __name__=='__main__': main()
