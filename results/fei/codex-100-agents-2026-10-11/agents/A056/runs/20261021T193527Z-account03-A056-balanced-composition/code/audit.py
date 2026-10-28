import shared as sh
from prior import *

u,v=table(3,1),table(3,16)
s=State(u,v,phase_ref(u,True),phase_ref(v,True),1,1)
rec,cs=sh.shared(s,0)
raw=sh.pull(s.P,s.Q,[c.P for c in cs],0)
failures=[]
for t,(c,q) in enumerate(zip(cs,raw)):
 coarse,z=sh.calibrate(c.P,q,[c.label(j) for j in range(len(c.P))])
 mismatch=[{'atom':j,'old_coarse':str(a),'prescribed':str(b)} for j,(a,b) in enumerate(zip(coarse,c.Q)) if a!=b]
 failures.append({'outcome':t,'normalizer':str(z),'mismatches':mismatch})
assert any(x['mismatches'] for x in failures)
# Independent character sums check the exact source and root coefficients,
# rather than trusting the FWHT on the critical fixture.
def direct(f):
 return tuple(Q(sum(a*(-1 if (x&t).bit_count()%2 else 1) for x,a in enumerate(f)),len(f)) for t in range(len(f)))
for f in [u,v,s.f]+[c.f for c in cs]:assert direct(f)==spectrum(f)
out={'status':'PASS','coarse_category_counterexample':{'u':1,'v':16,'shared_query':0,'private_widths':[1,1],'index_weighted':True,'outcomes':failures},'direct_character_sum_comparisons':5,'source4I_counterexample':{'function':'three-bit balanced dictator on lowest-index bit','I':'1','reference_atom':'2/35','cost':'log2(35/2)','exact_sign':'35>32 implies cost>4'},'critical_example':rec}
(R/'out/adversarial_audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','coarse_partition_mismatching_atoms':[len(x['mismatches']) for x in failures],'direct_character_sum_comparisons':5}))
