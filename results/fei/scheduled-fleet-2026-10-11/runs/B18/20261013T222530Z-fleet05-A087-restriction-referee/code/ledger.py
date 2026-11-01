"""Exact stopped interleaved entropy-ledger certificate on one fixed gate."""
import json,hashlib
from fractions import Fraction as Q
import check as c
u=v=(1,1,1,-1);f=c.priority(u,v,0);qs=(Q(1,4),Q(1,8));order=(0,2,1,3)
def nonempty(h):return c.add(c.entropy(h),c.scale(c.phi(c.walsh(h)[0]**2),-1))
rootinner=c.add(*(c.scale(nonempty(h),q) for h,q in zip((u,v),qs)))
current=[(u,v,Q(1))];remaining=[[0,1],[2,3]];spent=();outer=();rows=[]
for depth in range(5):
    leaves=c.add(*(c.scale(c.entropy(c.priority(a,b,0)),w) for a,b,w in current))
    leafinner=c.add(*(c.scale(c.add(c.scale(nonempty(a),qs[0]),c.scale(nonempty(b),qs[1])),w) for a,b,w in current))
    rhs=c.add(leaves,rootinner,c.scale(leafinner,-1),c.scale(spent,-1),outer)
    assert rhs==c.entropy(f)
    rows.append({'depth':depth,'leaf_count':len(current),'terminal_entropy_bits':c.serial(leaves),'signed_inner_bits':c.serial(c.add(rootinner,c.scale(leafinner,-1),c.scale(spent,-1))),'outer_M_plus_J_bits':c.serial(outer)})
    if depth==4:break
    label=order[depth];j=int(label>=2);i=remaining[j].index(label);nxt=[]
    for a,b,w in current:
        h=(a,b)[j];beta=c.walsh(h)[1<<i];m=c.walsh(h)[0];C,W=c.selector(a,b,0,j);cc=c.walsh(C);ww=c.walsh(W)
        aa=tuple(x+m*y for x,y in zip(ww,cc))
        # M+J equals the signed two-amplitude entropy packet, exactly.
        outer=c.add(outer,c.scale(c.add(*(c.dpacket(x,beta*y) for x,y in zip(aa,cc))),w))
        spent=c.add(spent,c.scale(c.phi(beta*beta),w*qs[j]))
        for bit in (0,1):
            nh=c.child(h,i,bit);nxt.append((nh,b,w/2) if j==0 else (a,nh,w/2))
    remaining[j].remove(label);current=nxt
out={'status':'PASS','exact_prefix_identities':5,'physical_order':['u0','v0','u1','v1'],'rows':rows,'helper_sha256':hashlib.sha256(c.Path(__file__).read_bytes()).hexdigest()}
(c.ROOT/'out/LEDGER.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('PASS: all 5 actual stopped interleaved entropy ledgers.')
