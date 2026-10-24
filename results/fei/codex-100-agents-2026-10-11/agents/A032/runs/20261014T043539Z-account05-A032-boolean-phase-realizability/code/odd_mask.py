import json,time,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic();old=ROOT.parent/'20261011T234647Z-account05-A032-boolean-phase-realizability'
rows=json.loads((old/'out/mixed_slices_m4.json').read_text())['records'];odd=0;norms={};checks=[]
chars=[[(-1 if (s&x).bit_count()%2 else 1) for x in range(16)] for s in range(16)]
for i,r in enumerate(rows):
    M=r['mixed_mask']
    if not M.bit_count()%2:continue
    odd+=1;W=[sum(v*c for v,c in zip(r['truth_h'],char)) for char in chars]
    assert all(v%2 for v in W)
    D=1
    for j in range(4):
        g=math.gcd(abs(W[0]),abs(W[1<<j]));a,b=abs(W[0])//g,abs(W[1<<j])//g;D*=a*b
    t=sum((-1 if x.bit_count()%2 else 1) for x in range(16) if M>>x&1)
    E=r['pure_mask'];tE=sum((-1 if x.bit_count()%2 else 1) for x in range(16) if E>>x&1)
    assert (t+4*tE)%D==0
    left=sum(W[s]*W[s^15] for s in range(16));assert left==16*(t+4*tE)
    norms[r['norm_integer']]=norms.get(r['norm_integer'],0)+1
    checks.append({'row_index':i,'D':D,'t':t,'t_E':tE,'signed_rhs':t+4*tE})
assert odd==144 and set(norms)=={1,5}
assert 4*max(norms)<64 # no four such rows can form a full Boolean cover on4data bits
out={'status':'PASS_PER_ROW_SIGNED_DIVISIBILITY','rows_scanned':len(rows),'odd_mask_rows':odd,'norm_counts':norms,'four_data_odd_mask_joint_cover_impossible':'four row norms<=5 cannot sum64','checks':checks,'seconds':time.monotonic()-start,'coupled_gcd_claim':'NOT_ACCEPTED: the cited sum of four divisible terms is0, not3t'}
(ROOT/'out/odd_mask_validation.json').write_text(json.dumps(out,indent=2))
gap={'status':'EXACT_NONIMPLICATION_FOR_THE_CITED_ARITHMETIC_STEP','t':1,'t_J':[2,2,2,-7],'D_J':[9,9,9,9],'sum_t_J':-1,'t_plus_4t_J':[9,9,9,-27],'sum_divisible_terms':0,'gcd_D':9,'three_t':3,'not_a_Boolean_counterexample':True,'scope':'satisfies only the listed divisibility and signed-partition-sum premises, not full product-row admission'}
assert sum(gap['t_J'])==-gap['t'] and all(v%9==0 for v in gap['t_plus_4t_J']) and 3%9!=0
(ROOT/'out/coupled_gap.json').write_text(json.dumps(gap,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='checks'}))
