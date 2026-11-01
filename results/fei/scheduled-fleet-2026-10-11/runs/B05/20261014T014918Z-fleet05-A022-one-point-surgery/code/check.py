"""controller-point-switch-v1: exact formulas and terminal-inclusive stopping tree."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from itertools import product
import sys,time,json,hashlib
RUN=Path(__file__).resolve().parents[1];MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
assert MODE in ('pilot','full')
SOURCE=RUN.parent/'20261013T220954Z-fleet05-A022-one-point-surgery'/'code'/'paired_access.py'
ns={'__file__':str(SOURCE),'__name__':'kernel'}
exec(SOURCE.read_text(encoding='utf-8').split('\ncase_count=0')[0],ns)
stats=ns['stats'];split=ns['split'];add=ns['add'];interval=ns['interval'];factors=ns['factors'];canonical=ns['canonical']
START=time.perf_counter();LIMIT=60 if MODE=='pilot' else 1800;CHECKS=0;counts=Counter()
def ck(v):
    global CHECKS
    assert v
    CHECKS+=1
def guard():
    if time.perf_counter()-START>LIMIT:raise TimeoutError('frozen runtime limit')
def phi(q):
    if not q:return ()
    e=Counter()
    for p,j in factors(q.denominator):e[p]+=q*j
    for p,j in factors(q.numerator):e[p]-=q*j
    return canonical(e)
def bent(v,k):return (-1)**sum(((v>>(2*j))&1)*((v>>(2*j+1))&1) for j in range(k//2))
def data_vertex(e,o,k):return sum(((e>>j)&1)<<(2*j) | ((o>>j)&1)<<(2*j+1) for j in range(k//2))
def truth(k,t,v,mask):
    m=k//2;dm=(1<<m)-1;ans=[]
    for x in range(1<<(k+t)):
        data=data_vertex(x&dm,(x>>m)&dm,k);z=x>>k
        ans.append(bent(data,k)*(-1 if data==v and ((mask>>z)&1) else 1))
    return tuple(ans)
def walk(f,k,t,v,mask,Ha,Ia,alpha,depth=0,prefix=0):
    guard();H,inf=stats(f);m=k//2
    if depth==m:
        tau=Q(1,1<<m);exceptional=prefix==sum(((v>>(2*j))&1)<<j for j in range(m))
        if exceptional:
            w=sum(((v>>(2*j+1))&1)<<j for j in range(m))
            q=tuple(s*((-1)**((x&((1<<m)-1)&prefix).bit_count()%2)) for x,s in enumerate(f))
            expected=tuple(-1 if (x&((1<<m)-1))==w and ((mask>>(x>>m))&1) else 1 for x in range(len(f)))
            ck(q==expected)
            leaf_formula=add((1,phi((1-2*tau*alpha)**2)),((1<<m)-1,phi(4*tau*tau*alpha*alpha)),
                (tau,Ha),(-tau,phi((1-2*alpha)**2)),(8*tau*alpha*(1-alpha)*m,((2,Q(1)),)))
            ck(H==leaf_formula)
            ck(sum(inf[:m])>=2*m*tau*alpha)
            ck(sum(inf[m:])==tau*Ia)
            ck(interval(add((1,H),(-tau,Ha)))[1]<=7*sum(inf[:m]))
            counts['exceptional_leaves']+=1
        else:
            ck(not H);ck(not sum(inf[m:]));counts['character_leaves']+=1
        return Q(0),sum(inf[:m]),sum(inf[m:]),(),H
    B,JS,d=split(f)
    ck(d>=Q(1,4));counts['access_nodes']+=1
    left=walk(f[::2],k,t,v,mask,Ha,Ia,alpha,depth+1,prefix)
    right=walk(f[1::2],k,t,v,mask,Ha,Ia,alpha,depth+1,prefix|(1<<depth))
    removed=d+(left[0]+right[0])/2
    leafdata=(left[1]+right[1])/2;leafctrl=(left[2]+right[2])/2
    accessH=add((1,B),(1,JS),(Q(1,2),left[3]),(Q(1,2),right[3]))
    leafH=add((Q(1,2),left[4]),(Q(1,2),right[4]))
    ck(H==add((1,accessH),(1,leafH)))
    ck(sum(inf)==removed+leafdata+leafctrl)
    return removed,leafdata,leafctrl,accessH,leafH
cases=0
with (RUN/'out'/f'{MODE}_CASES.jsonl').open('w',encoding='utf-8') as out:
    for k in ([4] if MODE=='pilot' else [4,6,8]):
        verts=range(16) if k==4 else ([0,1,21,63] if k==6 else [0,1,85,255])
        for t in range(3 if MODE=='pilot' else 4):
            for mask in range(1<<(1<<t)):
                a=tuple(-1 if (mask>>z)&1 else 1 for z in range(1<<t));Ha,infa=stats(a);Ia=sum(infa)
                alpha=Q(mask.bit_count(),1<<t)
                for v in verts:
                    f=truth(k,t,v,mask);H,inf=stats(f);delta=Q(1,1<<k);beta=Q(1,1<<(k//2))
                    dataI=sum(inf[:k]);ctrlI=sum(inf[k:])
                    bv=bent(v,k);interaction=sum(bv*bent(v^(1<<j),k) for j in range(k))
                    ck(dataI==Q(k,2)+2*delta*alpha*interaction);ck(ctrlI==delta*Ia)
                    aligned=((1<<k)+(1<<(k//2)))//2;anti=(1<<k)-aligned
                    root_formula=add((aligned,phi((beta-2*delta*alpha)**2)),(anti,phi((beta+2*delta*alpha)**2)),
                        (delta,Ha),(-delta,phi((1-2*alpha)**2)),(8*delta*alpha*(1-alpha)*k,((2,Q(1)),)))
                    ck(H==root_formula)
                    removed,leafdata,leafctrl,accessH,leafH=walk(f,k,t,v,mask,Ha,Ia,alpha)
                    ck(dataI==removed+leafdata);ck(ctrlI==leafctrl)
                    ck(interval(add((1,H),(-delta,Ha)))[1]<=7*dataI)
                    # One-use terminal bill: exact inherited weight delta, all other leaves entropy0.
                    ck(interval(add((1,leafH),(-delta,Ha)))[1]<=7*leafdata)
                    out.write(json.dumps({'k':k,'t':t,'v':v,'controller_mask':mask,'alpha':str(alpha),
                        'I_data':str(dataI),'I_ctrl':str(ctrlI),'I_access':str(removed),
                        'I_terminal_data':str(leafdata),'I_terminal_ctrl':str(leafctrl),
                        'H_interval':[str(x) for x in interval(H)],
                        'H_controller_interval':[str(x) for x in interval(Ha)],
                        'H_minus_inherited_interval':[str(x) for x in interval(add((1,H),(-delta,Ha)))],
                        'access_bad_credit':'0'},separators=(',',':'))+'\n')
                    cases+=1
            out.flush()
result={'helper':'controller-point-switch-v1','mode':MODE,'cases':cases,'checks':CHECKS,
    'support_checks':ns['CHECKS'],'kernel_checks':ns['ns']['ASSERTIONS'],'counts':dict(counts),
    'runtime_seconds':time.perf_counter()-START,'verdict':'PASS','access_bad_credit':'0',
    'arithmetic':'integer signed Walsh, rational exact prime-log identities; 80-bit outward intervals',
    'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest()}
(RUN/'out'/f'{MODE}_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
(RUN/'out'/f'{MODE}_LOG_RECEIPTS.json').write_text(json.dumps({'scale':str(ns['SCALE']),
    'prime_intervals':ns['ns']['PRIME_RECEIPTS'],'kernel':'immutable stage2 50-term atanh proof with range reduction and outward80-bit rounding'},indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
