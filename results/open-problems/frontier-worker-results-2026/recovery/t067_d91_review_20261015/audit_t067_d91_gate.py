"""Independent exact compensated gate using only independently rebuilt integrals."""
from pathlib import Path
from datetime import datetime
from fractions import Fraction as F
import hashlib,json
HERE=Path(__file__).resolve().parent;W=Path('~/brain_workers/w682')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
fmap=HERE/'T067_OWN_ENDPOINT_MAP.json'
assert sha(fmap)=='3e2da056f21fdadb6c7b4be7e4e453935dde996dc932705c52bb7862ea2840fb'
fdata=json.loads(fmap.read_text(encoding='utf-8'));gu={F(k):F(v) for k,v in fdata['endpoint_g_upper'].items()}
summary_path=HERE/'T067_GAUSSIAN_FOURTH_OWN_SUMMARY.json'
data=json.loads(summary_path.read_text(encoding='utf-8'));assert data['completed']==86
assert data['status'].startswith('PASS')
qu={}
for name,digest in data['source_files'].items():
    path=HERE/'t067_gaussian_fourth_own'/name;assert sha(path)==digest
    row=json.loads(path.read_text(encoding='utf-8'));qu[F(row['s'])]=F(row['UG_upper'])
points=[F(10,100-i) for i in range(86)];assert set(gu)==set(qu)==set(points)
D=91;L=F(209657,2000000);beta=F(49,4)
assert D*L*L>=1 and L<F(39,250)
B4=F(25,288)+F(49,100)*L/(1-L)
B3=F(1,6)+F(49,20)*L*B4;B1=F(5,24)+F(49,20)*L*B3
def ledger(g1,c2,c3,c31,c4):
    cu=g1*(F(1,6)+F(49,20)*L*B4)
    cu+=c2/2*(F(1,24)+B3*(1/(1-L)+1+L/2)+F(1,6))
    cu+=c31*B1/(2*(1-L)**2)+c3/6+c4/(24*(1-L)**4)
    cm=c2/12+5*c31/24+5*c3*L*L/72+c4*(2+4*L*L+L**4)/24
    return cu,cm
fu,fm=ledger(*map(F,['1/8','1/5','2/5','1/2','3/5']))
quc,qm=ledger(*map(F,['8','20','38','38','99']))
den=D-quc-9*beta*fu;mono=qm-quc*fm/fu
assert den>0 and mono>0 and D-quc>0 and fu>0
alpha=(D-quc)/fu;B=81*((1-quc/D)*fm/fu+qm/D)
assert alpha>0 and B>0
# Generator^2(Q) <=270+1282.5+2004.75=14229/4<3600,
# using ||Pe1||<=5/6 and the independently certified derivative bounds.
assert F(14229,4)<3600
curvature=32*alpha+2*B+3600
endpoint={s:alpha*(s-gu[s])-B*s*s-qu[s] for s in points}
rows=[]
for a,b in zip(points,points[1:]):
    margin=min(endpoint[a],endpoint[b])-curvature*(b-a)**2/8
    assert margin>F(3,200),(str(a),str(b),str(margin))
    rows.append({'a':str(a),'b':str(b),'certified_margin':str(margin)})
author=W/'checks/compensated91_gate.json'
assert sha(author)=='b6f43d3d4d6781abec45f78fbc4b500d97ddfb5e8d70de7fbbd401ec25615f18'
saved=json.loads(author.read_text(encoding='utf-8'))
assert [fu,fm]==list(map(F,saved['F_constants']))
assert [quc,qm]==list(map(F,saved['Q_constants']))
assert alpha==F(saved['alpha']) and B==F(saved['B']) and curvature==F(saved['curvature_upper'])
main=W/'proofs/T067-COMPENSATED-D91-001_v1.md'
assert sha(main)=='3f41f2986e611f38d248077ab2da3352d70634fec300ae91cb40e83655ceb9bd'
out={'at':datetime.now().astimezone().isoformat(),'status':'PASS independent exact91 continuous gate using own86 F and own86 Q enclosures',
     'proof_sha256':sha(main),'script_sha256':sha(Path(__file__)),
     'own_F_map_sha256':sha(fmap),'own_Q_summary_sha256':sha(summary_path),
     'D':D,'L':str(L),'F_constants':list(map(str,[fu,fm])),'Q_constants':list(map(str,[quc,qm])),
     'positive_denominator':str(den),'positive_d_monotonicity':str(mono),
     'alpha':str(alpha),'B':str(B),'curvature':str(curvature),
     'minimum_margin':str(min(F(row['certified_margin']) for row in rows)),
     'intervals':rows,'author_gate_sha256':sha(author),
     'scope':'Finite and continuous comparison only, conditional on analytic compensated replacement and canonical-limit arguments. Does not supply distinct-account admission. No D90 rescan.'}
(HERE/'T067_D91_OWN_GATE_RECEIPT.json').write_bytes((json.dumps(out,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'status':out['status'],'minimum_margin_float':float(F(out['minimum_margin'])),'intervals':len(rows)}))
