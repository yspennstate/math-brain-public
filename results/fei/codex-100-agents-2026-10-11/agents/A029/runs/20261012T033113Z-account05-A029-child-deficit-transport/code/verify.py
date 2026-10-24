import json,time
from fractions import Fraction as R
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
COUNT=0
def ck(b):
    global COUNT
    COUNT+=1
    if not b:raise AssertionError(COUNT)
def factors(a):
    out={};p=2
    while p*p<=a:
        while a%p==0:out[p]=out.get(p,0)+1;a//=p
        p+=1
    if a>1:out[a]=out.get(a,0)+1
    return out
def add(a,b,weight=R(1)):
    a=a.copy()
    for p,v in b.items():a[p]=a.get(p,R(0))+weight*v
    return {p:v for p,v in a.items() if v}
def scale(a,k):return {p:v*k for p,v in a.items() if v*k}
def record(table):
    N=len(table);n=N.bit_length()-1
    w=[sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(table)) for s in range(N)]
    ck(sum(a*a for a in w)==N*N)
    H={2:R(2*n)}
    for a in w:
        if not a:continue
        for p,e in factors(abs(a)).items():H[p]=H.get(p,R(0))-R(a*a*2*e,N*N)
    H={p:v for p,v in H.items() if v}
    d=[R(sum(table[x]!=table[x^(1<<i)] for x in range(N)),N) for i in range(n)]
    ck(sum(d)==R(sum(s.bit_count()*a*a for s,a in enumerate(w)),N*N))
    return H,sum(d),d,w
def restricted(state):
    free=[i for i,b in enumerate(state) if b is None]
    table=[]
    for z in range(1<<len(free)):
        vals=list(state)
        for j,i in enumerate(free):vals[i]=(z>>j)&1
        x=vals[:3];y=vals[3:]
        g=-1 if not any(y) else 1
        table.append(g*(-1 if sum(a*b for a,b in zip(x,y))%2 else 1))
    return free,record(table)
def main():
    start=time.monotonic();root=restricted((None,)*6)[1]
    ck(root[0]=={2:R(6)} and root[1]==3 and all(abs(v)==8 for v in root[3]))
    for i in range(6):
        for b in range(2):
            s=[None]*6;s[i]=b;r=restricted(tuple(s))[1]
            ck(r[0]=={2:R(4)})
        ck(root[2][i]==R(1,2))
    leafH={};leafI=R(0);nodeH={};nodeI=R(0);leaf_count=0;node_count=0;leaf_records=[]
    def visit(state):
        nonlocal leafH,leafI,nodeH,nodeI,leaf_count,node_count
        free,r=restricted(state);H,I,d,w=r;weight=R(1,2**(6-len(free)))
        xs=[j for j in range(3) if state[j] is None]
        ys=[j for j in range(3,6) if state[j] is None]
        if not xs and (not any(state[:3]) or not ys):
            leaf_count+=1;leafH=add(leafH,H,weight);leafI+=weight*I
            leaf_records.append({'assignment':list(state),'weight':str(weight),'H':{str(p):str(v) for p,v in H.items()},'I':str(I)})
            return
        i=xs[0] if xs else ys[0];node_count+=1
        child=[]
        for b in range(2):
            s=list(state);s[i]=b;child.append(restricted(tuple(s))[1])
        delta=add(add(H,child[0][0],-R(1,2)),child[1][0],-R(1,2))
        nodeH=add(nodeH,delta,weight);nodeI+=weight*d[free.index(i)]
        ck(I-(child[0][1]+child[1][1])/2==d[free.index(i)])
        for b in range(2):
            s=list(state);s[i]=b;visit(tuple(s))
    visit((None,)*6)
    ck(leaf_count==57 and node_count==56)
    ck(leafH=={2:R(1,2),3:-R(9,64)} and leafI==R(3,32))
    ck(nodeH==add(root[0],leafH,-1));ck(nodeI==root[1]-leafI==R(93,32))
    ratio=scale(nodeH,1/nodeI)
    ck(ratio=={2:R(176,93),3:R(3,62)})
    terminal_D=add({2:2*leafI},leafH,-1)
    node_credit=add({2:2*nodeI},nodeH,-1)
    ck(add(terminal_D,node_credit)=={})
    ck(terminal_D=={2:-R(5,16),3:R(9,64)})
    ck(3**5<2**8)
    ratio_upper=ratio[2]+ratio[3]*R(8,5)
    gain_lower=4-ratio_upper
    ck(ratio_upper==R(916,465));ck(gain_lower==R(944,465)>R(203,100))
    result={'status':'PASS','assertions':COUNT,'elapsed_seconds':time.monotonic()-start,
     'root_H':6,'root_I':3,'local_ratio_each':4,'leaf_count':leaf_count,'node_count':node_count,
     'terminal_H':{str(p):str(v) for p,v in leafH.items()},'terminal_I':str(leafI),
     'Pi_H':{str(p):str(v) for p,v in nodeH.items()},'Pi_I':str(nodeI),
     'tree_ratio_prime_log_form':{str(p):str(v) for p,v in ratio.items()},
     'terminal_D2_prime_log_form':{str(p):str(v) for p,v in terminal_D.items()},
     'query_credit_prime_log_form':{str(p):str(v) for p,v in node_credit.items()},
     'strict_gain_lower':str(gain_lower),'strict_ratio_upper':str(ratio_upper),
     'sign_certificate':'3^5=243<256=2^8; log2 3<8/5',
     'independent_agent_review':False,'prime_log_convention':'coefficient p multiplies log2(p), log2(2)=1'}
    (BASE/'out'/'independent.json').write_text(json.dumps(result,indent=2))
    (BASE/'out'/'physical_leaves.json').write_text(json.dumps(leaf_records,indent=2))
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
