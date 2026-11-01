from pathlib import Path
from fractions import Fraction as F
import json
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'
spec={'helper':'A100-support-conditioning-v1','family':'one actual parity3 core activated by one fair control; seed dictator plus two parity bits',
      'domain':'n=4, m=k=1, ell=2','case_count':1,'symmetry':'none','arithmetic':'integer character sums and Fraction; all logs are exact log2(2)=1 or log2(1)=0',
      'memory_estimate_MB':5,'max_runtime_seconds':10,'automatic_dimension_escalation':False}
(RUN/'MUTATION_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
table=[(-1 if (x&7).bit_count()%2 else 1) if x>>3==0 else 1 for x in range(16)]
a=[F(sum(table[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(16)),16) for s in range(16)]
p=[v*v for v in a]; eps=F(sum(table[x]!=table[x^1] for x in range(16)),16)
r={t:p[t]+p[t|1] for t in range(0,16,2)}
mu={t:p[t|1]/eps for t in r if p[t|1]}
assert sum(p)==1 and sum(r.values())==1 and sum(mu.values())==1 and eps==F(1,2)
support_mass=sum((r[t] for t in mu),F(0)); assert support_mass==F(1,2)
assert all(mu[t]/r[t]==2 for t in mu)
assert all(mu[t]/(r[t]/support_mass)==1 for t in mu)
assert all(r[t]==p[t|1] for t in mu)
record={'status':'PASS','family':spec['family'],'p':{str(t):str(v) for t,v in enumerate(p) if v},
        'complete_reference_mass':'1','reference_mass_on_derivative_support':str(support_mass),
        'physical_influence':str(eps),'D_complete_bits':1,'D_support_conditioned_bits':0,
        'actual_M_bits':0,'incorrect_conditioned_substitution_M_bits':'1/2',
        'lost_reference_mass_log_correction_bits':1,
        'scope':'Reject substituting a support-conditioned reference into the complete retained-KL identity. No error in A096 source; no FEI refutation.',
        'checked_predicates':8}
(OUT/'SUPPORT_CONDITIONING_CERTIFICATE.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print('PASS: exact four-bit support-conditioning negative control; lost refund is one bit.')
