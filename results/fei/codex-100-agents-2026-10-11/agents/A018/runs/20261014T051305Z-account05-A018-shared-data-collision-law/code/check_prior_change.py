from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'code/check_reference.py'
env={'__file__':str(SOURCE),'__name__':'definitions_only'}
exec(compile(SOURCE.read_text(encoding='utf8').split('\nfixtures=')[0],str(SOURCE),'exec'),env)
Q=env['Q'];ns=env['ns'];data=env['data'];CE=env['CE'];ck=env['ck']
start=time.perf_counter();vs=[[-1]+[1]*7,[-1]+[1]*3];ds=[data(v) for v in vs]
g=[a*b for b in vs[1] for a in vs[0]];v=[x for a in g for x in (a,1)];P,H,I,_=data(v)
R=[P[2*t]+P[2*t+1] for t in range(len(g))];rows=[]
for flavor in ('actual','uniform'):
 qs=[d[0] if flavor=='actual' else [Q(1,len(vv))]*len(vv) for d,vv in zip(ds,vs)]
 qproduct=[a*b for b in qs[1] for a in qs[0]]
 joint=[(q+int(t==0))/2 for t,q in enumerate(qproduct)]
 separate=[(q2+int(u==0))*(q1+int(t==0))/4 for u,q2 in enumerate(qs[1]) for t,q1 in enumerate(qs[0])]
 ck(sum(joint)==sum(separate)==1)
 change=ns['add'](*[(r,ns['logq'](qj/qs0)) for r,qj,qs0 in zip(R,joint,separate) if r])
 jointCE=CE(R,joint);separateCE=CE(R,separate)
 ck(change==ns['add']((1,separateCE),(-1,jointCE)))
 lo,hi=ns['grid'](change)
 costs=[CE(d[0],q) for d,q in zip(ds,qs)]
 ck(all(ns['grid'](ns['add']((5*d[2],{2:1}),(-1,c)))[0]>=0 for c,d in zip(costs,ds)))
 if flavor=='actual':ck(lo>0)
 else:ck(hi<0)
 rows.append({'flavor':flavor,'core_dimensions':[3,2],'core_means':[str(d[3]) for d in ds],'core_reference_costs_prime_log':[{str(p):str(c) for p,c in z.items()} for z in costs],'supplied_rate5_hypotheses':'PASS','I_parent':str(I),'change_CE_separate_minus_joint_prime_log':{str(p):str(c) for p,c in change.items()},'change_scaled_interval':[str(lo),str(hi)],'scale':str(ns['SCALE']),'sign':'POSITIVE_TC_REFUND' if lo>0 else 'NEGATIVE_CHANGE_NO_FREE_REFUND'})
out={'status':'PASS','checks':env['checks'],'cases':rows,'elapsed_seconds':time.perf_counter()-start}
(ROOT/'out/PRIOR_CHANGE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':'PASS','checks':env['checks'],'elapsed_seconds':out['elapsed_seconds']}))
