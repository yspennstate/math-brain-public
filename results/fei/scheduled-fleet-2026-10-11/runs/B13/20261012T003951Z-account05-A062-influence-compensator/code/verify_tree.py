"""Actual complete-tree oracle, independent of the compressed state formulas."""
from pathlib import Path
import json,time
run=Path(__file__).resolve().parents[1]
helper=run/'code/check_reserve.py'
# Reuse only the certified arithmetic/Boolean transform definitions, not its case loop.
env={'__file__':str(helper)}
exec(compile(helper.read_text().split('core_rows=[]')[0],str(helper),'exec'),env)
F=env['F']; point=env['point']; plus=env['plus']; minus=env['minus']; mul=env['mul']; pos=env['pos']
measure=env['measure']; equal=env['equal']; leq=env['leq']; fmt=env['fmt']
start=time.perf_counter()
k,r=4,8
values=[]
for x in range(1<<(1+k+r)):
    selector=x&1
    controls=(x>>1)&((1<<r)-1)
    data=x>>(r+1)
    bent=(-1)**sum(((data>>(2*j))&1)*((data>>(2*j+1))&1) for j in range(k//2))
    values.append(1 if controls else (-1 if selector and data==0 else bent))
memo={}
def recurse(f,labels):
    key=(f,labels)
    if key in memo: return memo[key]
    if all(v==f[0] for v in f):
        return (point(0),point(0),F(0),point(0),F(0))
    coeff,H,inf=measure(f)
    chosen=next(i for i,d in enumerate(inf) if d>0)
    children=[tuple(f[x] for x in range(len(f)) if ((x>>chosen)&1)==bit) for bit in (0,1)]
    remaining=labels[:chosen]+labels[chosen+1:]
    z0,z1=[recurse(g,remaining) for g in children]
    childH=mul(plus(z0[3],z1[3]),F(1,2))
    D=minus(H,childH)
    Q=pos(plus(minus(D,point(6*inf[chosen])),mul(plus(z0[0],z1[0]),F(1,2))))
    Qlead=pos(plus(minus(D,point(F(32609,5000)*inf[chosen])),mul(plus(z0[1],z1[1]),F(1,2))))
    spent=inf[chosen]+(z0[2]+z1[2])/2
    equal(spent,sum(inf),'actual_tree_budget')
    # The proof predicts that no control or even-core entry propagates debt upward.
    if labels[chosen] in range(1,r+1):
        equal(Q,point(0),'actual_control_reserve_zero')
    if labels[chosen]>r and (labels[chosen]-(r+1))%2==0:
        equal(Q,point(0),'actual_paired_entry_reserve_zero')
    mu=F(sum(v==-1 for v in f),len(f)); mu=min(mu,1-mu)
    leq(Q[1],4*env['psi'](mu)[0],'actual_all_node_rarity_domination')
    out=(Q,Qlead,spent,H,inf[chosen])
    memo[key]=out
    return out
result=recurse(tuple(values),tuple(range(1+k+r)))
cert=json.loads((run/'out/CERTIFICATES.json').read_text())['selector_roots'][0]
expected=(F(cert['Qstar']['lower']),F(cert['Qstar']['upper']))
expected_lead=(F(cert['Qstar_at_lead_price']['lower']),F(cert['Qstar_at_lead_price']['upper']))
leq(max(result[0][0],expected[0]),min(result[0][1],expected[1]),'actual_compressed_Q_interval_overlap')
leq(max(result[1][0],expected_lead[0]),min(result[1][1],expected_lead[1]),'actual_compressed_lead_Q_interval_overlap')
elapsed=time.perf_counter()-start
assert elapsed<60,elapsed
out={'helper_version':'A062-tree-oracle-v1','assertions':sum(env['counts'].values()),
     'counts':dict(env['counts']),'failures':0,'runtime_seconds':elapsed,
     'dimension':13,'distinct_internal_nodes':len(memo),'Qstar':fmt(result[0]),
     'Qstar_at_lead_price':fmt(result[1]),'I':str(result[2]),
     'method':'complete actual physical truth-table recursion; no compressed family transition assumed'}
(run/'out/TREE_ORACLE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key:val for key,val in out.items() if key not in ('Qstar','Qstar_at_lead_price')},indent=2))
