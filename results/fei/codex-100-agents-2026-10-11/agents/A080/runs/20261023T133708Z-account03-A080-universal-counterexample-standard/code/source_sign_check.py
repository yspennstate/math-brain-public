"""One frozen exact witness to a written sign convention, not to FEI."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import time
import itertools

t=time.monotonic()
r=Path(__file__).resolve().parents[1]
s=Path('agents/A089/runs/20261023T130925Z-account03-A089-repair-specialist')
proof=r/'out'/'A089_SOURCE_PROOF.md'
if not proof.exists():
    b=(s/'PROOF.md').read_bytes()
    assert hashlib.sha256(b).hexdigest()=='ce30bbf231302d8f5004ed6794e59591d81b44e1f926345f18d5bb4bbf07af00'
    proof.write_bytes(b)
assert 'With S_b=H(F_b)-K I(F_b)' in proof.read_text(encoding='utf-8')
f=(1,-1,-1,1)
children=[tuple(f[x] for x in range(4) if x%2==b) for b in (0,1)]
def influence(g):
    return sum((Q(sum(g[x]!=g[x^(1<<i)] for x in range(len(g))),len(g)) for i in range(len(g).bit_length()-1)),Q(0))
for g in [f]+children:
    w=[sum(g[x]*(-1 if (x&z).bit_count()%2 else 1) for x in range(len(g))) for z in range(len(g))]
    assert sum(v!=0 for v in w)==1 and sum(v*v for v in w)==len(g)**2
K,kappa=Q(10),Q(9,2)
parent_I=influence(f)
child_I=[influence(g) for g in children]
parent_bank=kappa*parent_I
child_bank=[kappa*x for x in child_I]
allocated=[a+parent_bank-sum(child_bank)/2 for a in child_bank]
wrong=[-K*x+a for x,a in zip(child_I,allocated)]
right=[K*x+a for x,a in zip(child_I,allocated)]
assert (parent_I,child_I,allocated,wrong,right)==(Q(2),[Q(1),Q(1)],[Q(9),Q(9)],[Q(-1),Q(-1)],[Q(19),Q(19)])
assert time.monotonic()-t<10
result={'status':'PASS','scope':'Written A089 PROOF section5 sign assertion only; source claim and FEI not refuted','function':list(f),'full_children':[list(g) for g in children],'K':str(K),'kappa':str(kappa),'parent_influence':str(parent_I),'child_influences':list(map(str,child_I)),'parent_bank':str(parent_bank),'allocated_child_credit':list(map(str,allocated)),'source_written_S':'H-KI','source_written_child_debits':list(map(str,wrong)),'corrected_S':'KI-H','corrected_child_debits':list(map(str,right)),'source_proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'source_claims_sha256':hashlib.sha256((r/'out'/'A089_SOURCE_CLAIMS.json').read_bytes()).hexdigest(),'source_owner_correction':'PENDING_A089','elapsed_seconds':time.monotonic()-t}
guard=(1,1,1,-1,1,-1,1,1)
def exact_dyadic_entropy(g):
    N=len(g)
    ws=[sum(g[x]*(-1 if (x&z).bit_count()%2 else 1) for x in range(N)) for z in range(N)]
    nonzero=[w for w in ws if w]
    assert sum(w*w for w in ws)==N*N
    if len(nonzero)==1:
        return Q(0)
    assert len(nonzero)==4 and all(abs(w)*2==N for w in nonzero)
    return Q(2)
restriction_rows=[]
for pattern in itertools.product((-1,0,1),repeat=3):
    g=tuple(guard[x] for x in range(8) if all(b==-1 or ((x>>i)&1)==b for i,b in enumerate(pattern)))
    h,ii=exact_dyadic_entropy(g),influence(g)
    assert h<=2*ii and h<=K*ii
    restriction_rows.append({'pattern':list(pattern),'H':str(h),'I':str(ii)})
H,Ip=exact_dyadic_entropy(guard),influence(guard)
assert (H,Ip)==(Q(2),Q(3,2))
kids=[tuple(guard[x] for x in range(8) if x%2==b) for b in (0,1)]
His=[exact_dyadic_entropy(g) for g in kids]
Iis=[influence(g) for g in kids]
supplied=Q(13)
assert supplied>=kappa*Ip and H-K*Ip+supplied==0
Ac=[kappa*x for x in Iis]
credits=[a+supplied-sum(Ac)/2 for a in Ac]
bad=[h-K*i+a for h,i,a in zip(His,Iis,credits)]
good=[K*i-h+a for h,i,a in zip(His,Iis,credits)]
assert bad==[Q(17,2),Q(-5,2)] and min(good)>=0
result['nonnegative_parent_debit_witness']={'function':list(guard),'full_children':[list(g) for g in kids],'parent_H':str(H),'parent_I':str(Ip),'parent_bank':str(kappa*Ip),'supplied_credit':str(supplied),'source_written_parent_debit':'0','allocated_child_credit':list(map(str,credits)),'source_written_child_debits':list(map(str,bad)),'corrected_child_debits':list(map(str,good)),'all_restrictions':restriction_rows,'true_inner_hulls':'0 at every state; every restriction has H<=2I<=10I'}
assert time.monotonic()-t<10
result['elapsed_seconds']=time.monotonic()-t
(r/'out'/'SOURCE_SIGN_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result),flush=True)
