from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1];SOURCE=ROOT/'code/check_reference.py'
env={'__file__':str(SOURCE),'__name__':'definitions_only'}
exec(compile(SOURCE.read_text(encoding='utf8').split('\nfixtures=')[0],str(SOURCE),'exec'),env)
Q=env['Q'];ns=env['ns'];data=env['data'];CE=env['CE'];ck=env['ck'];start=time.perf_counter()
g=[-1]+[1]*31;p,Hg,Ig,mu=data(g);prod=[a*b for b in g for a in g]
v=[x for a in prod for x in (a,1)];P,H,I,_=data(v)
R=[P[2*t]+P[2*t+1] for t in range(1024)]
Rj=[(x+int(t==0))/2 for t,x in enumerate(p)]
qseparate=[a*b for b in Rj for a in Rj]
qjoint=[(a*b+int(t==0 and u==0))/2 for u,b in enumerate(p) for t,a in enumerate(p)]
ck(qjoint==R)
B=ns['add']((1,H),(-1,ns['ent'](R)))
sep=ns['add']((1,CE(R,qseparate)),(1,B));joint=ns['add']((1,CE(R,qjoint)),(1,B))
TC=ns['add']((2,ns['ent'](Rj)),(-1,ns['ent'](R)))
ck(joint==H);ck(ns['add']((1,sep),(-1,joint))==TC);ck(ns['grid'](TC)[0]>0)
Hm=data([x for a in g for x in (a,1)])[1];gap=ns['add']((1,H),(-2,Hm));ck(ns['grid'](gap)[0]>0)
ck(ns['grid'](ns['add']((5*Ig,{2:1}),(-1,Hg)))[0]>=0)
ck(ns['grid'](ns['add']((5*I,{2:1}),(-1,joint)))[0]>=0)
out={'status':'PASS','checks':env['checks'],'dimension':11,'private_dimensions':[5,5],'I':str(I),'supplied_core_rate5':'PASS','positive_entropy_excess_preserved':True,'new_CE':'H(parent)','old_CE':'H(parent)+TC','exact_TC_refund_prime_log':{str(p):str(c) for p,c in TC.items()},'normalization':'Both1','elapsed_seconds':time.perf_counter()-start}
(ROOT/'out/CONTROL_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':'PASS','checks':env['checks'],'elapsed_seconds':out['elapsed_seconds']}))
