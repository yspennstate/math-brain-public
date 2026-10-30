from pathlib import Path
from functools import lru_cache
import json,time,sys,hashlib
run=Path(__file__).resolve().parents[1]
helper=run.parents[0]/'20261012T003951Z-fleet05-A062-influence-compensator/code/check_reserve.py'
env={'__file__':str(helper)}
exec(compile(helper.read_text().split('core_rows=[]')[0],str(helper),'exec'),env)
F=env['F']; point=env['point']; plus=env['plus']; minus=env['minus']; mul=env['mul']; pos=env['pos']; measure=env['measure']; equal=env['equal']; leq=env['leq']; fmt=env['fmt']; b=env['b']
start=time.perf_counter()
@lru_cache(None)
def tree(values,labels):
    if len(set(values))==1: return point(0),point(0),F(0)
    _,H,inf=measure(values)
    i=next(i for i,d in enumerate(inf) if d)
    children=[tuple(values[x] for x in range(len(values)) if ((x>>i)&1)==bit) for bit in (0,1)]
    rest=labels[:i]+labels[i+1:]
    ch=[tree(f,rest) for f in children]
    D=minus(H,mul(plus(ch[0][1],ch[1][1]),F(1,2)))
    Q=pos(plus(minus(D,point(6*inf[i])),mul(plus(ch[0][0],ch[1][0]),F(1,2))))
    spent=inf[i]+sum(c[2] for c in ch)/2
    equal(spent,sum(inf),'complete_influence_budget')
    return Q,H,spent
pilot='--pilot' in sys.argv
rows=[]
for k in ((4,) if pilot else (2,4,6)):
    for v in range(1<<k):
        values=list(b(k)); values[v]*=-1
        Q,H,I=tree(tuple(values),tuple(range(k)))
        equal(Q,point(0),'all_single_edit_entry_zero')
        rows.append({'family':'single','k':k,'vertex':v,'Q':fmt(Q)})
for k in ((4,) if pilot else (4,6,8,10)):
    values=list(b(k)); values[0]*=-1; values[5]*=-1; values=tuple(values)
    Q,H,I=tree(values,tuple(range(k)))
    equal(Q,point(0),'two_edit_entry_zero')
    delta=F(1,1<<k)
    _,_,inf=measure(values)
    equal(inf,[F(1,2) if j in (1,3) else F(1,2)+4*delta for j in range(k)],'two_edit_label_influence')
    children=[tuple(values[x] for x in range(len(values)) if (x&1)==bit) for bit in (0,1)]
    ch=[tree(f,tuple(range(1,k))) for f in children]
    equal(ch[1][0],point(0),'expensive_odd_child_zero')
    leq(ch[0][0][1],F(2),'cheap_odd_child_cap')
    leq(max(ch[0][1][0],ch[1][1][0]),min(ch[0][1][1],ch[1][1][1]),'odd_child_entropy_invariant')
    pre=plus(minus(minus(H,mul(plus(ch[0][1],ch[1][1]),F(1,2))),point(6*inf[0])),mul(plus(ch[0][0],ch[1][0]),F(1,2)))
    leq(pre[1],F(0),'two_owned_children_paid')
    rows.append({'family':'two','k':k,'Q':fmt(Q),'preclip':fmt(pre),'child_Q':[fmt(c[0]) for c in ch],'I':str(I),'table_sha256':hashlib.sha256(bytes(v+1 for v in values)).hexdigest()})
if not pilot:
    k,r=4,8
    values=[]
    for x in range(1<<(k+r+1)):
        sel=x&1; controls=(x>>1)&((1<<r)-1); data=x>>(r+1)
        sign=b(k)[data]
        values.append(1 if controls else (-sign if sel and data in (0,5) else sign))
    values=tuple(values)
    Q,H,I=tree(values,tuple(range(k+r+1)))
    p=F(1,1<<r); delta=F(1,1<<k); alpha=F(1,1<<(k//2))
    equal(I,p*(F(k,2)+r*(1-alpha+2*delta)+(2*k-2)*delta),'selector_initial_influence')
    _,_,inf=measure(values)
    equal(inf[0],2*p*delta,'two_selector_influence')
    leq(Q[1],4*delta*I,'root_initial_influence_credit')
    ch=[tree(tuple(values[x] for x in range(len(values)) if (x&1)==bit),tuple(range(1,k+r+1))) for bit in (0,1)]
    for c in ch: equal(c[0],point(0),'activated_child_zero')
    equal(Q,pos(minus(minus(H,mul(plus(ch[0][1],ch[1][1]),F(1,2))),point(6*inf[0]))),'root_complete_tree_identity')
    rows.append({'family':'activated_selector_two','k':k,'r':r,'Q':fmt(Q),'I':str(I),'Q_over_I':fmt(mul(Q,1/I))})
elapsed=time.perf_counter()-start
assert elapsed<60,elapsed
out={'helper_version':'A062-two-edit-tree-v1','pilot':pilot,'runtime_seconds':elapsed,'root_count':len(rows),'assertions':sum(env['counts'].values()),'counts':dict(env['counts']),'failures':0,'distinct_internal_states':tree.cache_info().currsize,'rows':rows}
(run/'out'/('PILOT.json' if pilot else 'EXACT_TREES.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
