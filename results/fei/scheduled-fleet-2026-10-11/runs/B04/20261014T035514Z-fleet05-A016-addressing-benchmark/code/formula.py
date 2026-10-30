from pathlib import Path
from fractions import Fraction as F
import json,time
RUN=Path(__file__).resolve().parents[1]
spec=json.loads((RUN/'FORMULA_SPEC.json').read_text());review=json.loads((RUN/'REVIEW_SPEC.json').read_text())
start=time.perf_counter();checks=0
def ck(b,label):
    global checks
    if not b:raise AssertionError(label)
    checks+=1
    if time.perf_counter()-start>60:raise RuntimeError('Frozen formula/review limit')
def energy(v):return F(sum((v[s]-v[s^(1<<i)])**2 for i in range(2) for s in range(4)),16)
review_records=[]
for core in range(16):
    g=[1-2*((core>>s)&1) for s in range(4)]
    for edit in range(16):
        inside=[bool(edit&(1<<s)) for s in range(4)]
        b=[-g[s] if inside[s] else g[s] for s in range(4)]
        D=[g[s] if inside[s] else 0 for s in range(4)]
        J=(energy(g)+energy(b))/2;kappa=energy(D)
        pin=F(sum(g[s]!=g[s^(1<<i)] and inside[s] and inside[s^(1<<i)] for i in range(2) for s in range(4)),4)
        pout=F(sum(g[s]!=g[s^(1<<i)] and not inside[s] and not inside[s^(1<<i)] for i in range(2) for s in range(4)),4)
        ck(2*kappa-J==pin-pout,'arbitrary-core partition identity')
        ck((kappa<=J/2)==(pin<=pout),'half-private iff')
        if edit.bit_count()==1:ck(kappa<=J/2,'arbitrary-core point edit')
        if pin>pout:review_records.append({'core_mask':core,'edit_mask':edit,'J':str(J),'kappa':str(kappa),'P_in':str(pin),'P_out':str(pout)})
review_count=checks
(RUN/'out/REVIEW_CHECK.json').write_text(json.dumps({'helper_version':review['helper_version'],'cases':256,'assertions':review_count,'failures':0,'positive_internal_surplus_cases':len(review_records),'positive_cases':review_records,'scope':'exact arbitrary-core edge partition only; full CE transfer reconstructed analytically in REPORT'},indent=2)+'\n')
records=[]
for a in spec['domain']:
    m=6;M=a*a;delta=F(1,1<<m);Is=a*(F(m,2)+(m+1)*delta);I=(M+Is+1)/2
    core=a*M*delta
    T=a*(M+F(1,2))*delta+F(a*a*m,2)*delta+F(a*(a-1)*(2*m+1),2)*delta**2
    CE=2+F(a*(m+1),2)
    ck(T>=core,'same-core exact contribution')
    ck(CE<=4*I,'complete gate-first reference')
    ck(m-1>4,'all reached selectors K4 bad')
    ck(2*T>=2*core,'nonnegative localized extras')
    rec={'a':a,'m':m,'M':M,'n':1+M+a*(m+1),'truth_table_constructed':False,'I':str(I),'mask_I':str(Is),'localized_K4_bill':str(T),'core_only_bill':str(core),'localized_bill_over_I':str(T/I),'core_bill_over_I':str(core/I),'localized_bill_over_aI':str(T/(a*I)),'complete_CE':str(CE),'complete_CE_over_I':str(CE/I),'gate_first_bad_bill':'0','all_K4_bad_selector_ratio_lower_bound':m-1}
    records.append(rec);(RUN/'out/FORMULA_PARTIAL.json').write_text(json.dumps({'records':records},indent=2)+'\n')
result={'helper_version':spec['helper_version'],'cases':len(records),'assertions':checks-review_count,'failures':0,'elapsed_seconds':time.perf_counter()-start,'records':records,'analytical_limits':{'localized_bill_over_I':'~ 2*2^-m*a -> infinity at M=a^2','core_only_bill_over_I':'~ 2*2^-m*a -> infinity','complete_CE_over_I':'~ (m+1)/a ->0','localized_bill_over_aI':'->2*2^-m =1/32 at m6'},'full_FEI':'OPEN'}
(RUN/'out/FORMULA_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'review_cases':256,'review_assertions':review_count,'formula_cases':len(records),'formula_assertions':checks-review_count,'failures':0,'elapsed_seconds':result['elapsed_seconds'],'largest_core_bill_over_I':records[-1]['core_bill_over_I'],'largest_complete_CE_over_I':records[-1]['complete_CE_over_I']}))
