from pathlib import Path
from fractions import Fraction as F
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
# Direct exact certificate, not a parameter search: both half-cube masks have
# squared Fourier weights(1/4,1/4), entropy1; mixture masses(1/2,1/2) have entropy1.
outside=(F(0),F(1));event=(F(1),F(0))
for mask in (outside,event):
    c=((mask[0]+mask[1])/2,(mask[0]-mask[1])/2)
    assert tuple(a*a for a in c)==(F(1,4),F(1,4))
assert F(1)+2*(F(1)+F(1))==5
save(R/'out/RAW_MASK_PAYMENT_OBSTRUCTION.json',{'status':'EXACT_CERTIFICATE','n_shared':1,'h':[1,1],'event_indicator':[1,0],'private_profile':[1],'F':[1,1],'H':0,'I':0,'U':0,'N':0,'partition_masses':['1/2','1/2'],'mask_squared_coefficients':[['1/4','1/4'],['1/4','1/4']],'mask_entropies':[1,1],'H_partition':1,'raw_mask_bill':5,'upper_certificate_with_offset':6,'refuted_statement':'A universal K with H(p)+(t+1)sum Ji<=K I(F) for arbitrary partition/profile representations','regenerate':'python -X utf8 code/final_scope.py (from run root; script resolves its own output root)'})
obstruction='The raw mask payment is NOT universally influence-controlled: on one shared bit let h=+1, A1 be one half cube and V1=+1. Then F=+1,H=I=U=N=0, each of the two mask squared spectra is(1/4,1/4) with Ji1, and H(p)=1. Thus H(p)+2sum Ji=5>0 and its bound with offset is6, despite I(F)=0. This exact certificate refutes payment of the raw mask upper bound by arbitrary output influence; it does NOT refute FEI or the proved bank inequality. A general bridge needs an activation/cancellation-aware certificate or a necessary admissible representation paid by its actual unused original owner. The threshold-class admission above is unaffected because its original majority pivots remain present.'
proof=R/'DISJOINT_MASK_PROOF.md';txt=proof.read_text(encoding='utf-8');txt+='\n\n## 5. Exact obstruction to raw universal mask payment\n\n'+obstruction+'\n';proof.write_text(txt,encoding='utf-8')
next_action='Construct an ACTIVATION/CANCELLATION-AWARE conditional-spectrum certificate, or a NECESSARY admissible mask representation, paid from actual unused ORIGINAL influence. Raw mask entropy alone is refuted by the constant-output certificate. Retain explicit source240, actual frozen R/K, old debits and full input/terminal bills; A077/A078/A092/A094 review equations1-10 and the exact obstruction first.'
claims=read(R/'CLAIMS.json')
for c in claims:
    c['exact_statement']+=' Stage11 exact obstruction: '+obstruction
    c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest();c['proof_source']['stage11_raw_payment_obstruction']=str(R/'out/RAW_MASK_PAYMENT_OBSTRUCTION.json')
save(R/'CLAIMS.json',claims)
p=read(R/'PROGRESS.json');p['next_action']=next_action;p['mathematical_delta']+=' Exact constant-output certificate refutes raw mask-bill<=K I(F), forcing activation/cancellation-aware admission.'
p['blockers'].insert(0,'Raw universal mask-entropy payment is REFUTED, not merely unproved: exact constant F has I0 but raw mask bill5. Need activation/cancellation-aware or necessary-representation source payment.')
p['blockers'].append('Administrative checklist done update failed: RuntimeError checklist lock held too long. Local research persistence passed; shared checklist was not forcibly unlocked.')
p['source_artifacts']+=['code/final_scope.py','out/RAW_MASK_PAYMENT_OBSTRUCTION.json'];save(R/'PROGRESS.json',p);save(R/'PACKET_DELTA.json',p)
report=R/'REPORT.md';txt=report.read_text(encoding='utf-8');heading='# one next mathematical action and independent reviewer';a,b=txt.split(heading+'\n\n',1);oldnext,tail=b.split('\n\n# ',1);txt=a+heading+'\n\n'+next_action+'\n\n# '+tail
needle='# executed validation with domain, arithmetic, commands and outputs';txt=txt.replace(needle,'Exact universal obstruction: '+obstruction+'\n\n'+needle)
txt=txt.replace('Administrative wake/checklist receipts are separate.','Administrative wake/checklist receipts are separate. The checklist done call failed because its lock was held too long; no shared lock was removed. Local artifact verification passed independently.')
txt=txt.replace('Exactly remaining is original-influence admission of the hereditary mask-entropy bill or a sharper certificate controlling growing profile count; arbitrary-mask eligibility is not proved.','Exactly remaining is activation/cancellation-aware source admission or a necessary admissible representation: raw universal mask payment is REFUTED by the exact constant-output bill5 versus influence0 certificate. Growing profile-count interference and arbitrary-mask eligibility remain unpaid.')
report.write_text(txt,encoding='utf-8')
lines=(A/'STATUS.md').read_text(encoding='utf-8').splitlines();lines[1]='NEXT: '+next_action;(A/'STATUS.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
for name in ('WORKLOG.md','LEARNED.md'):
    with (A/name).open('a',encoding='utf-8') as f:f.write('\n'+now+' stage11 final scope: '+obstruction+' Administrative checklist done lock timed out; no shared lock removed; local research artifacts verified.\n')
print(json.dumps({'status':'FINAL_SCOPE_SAVED','raw_bill':5,'actual_influence':0,'checklist':'LOCK_BLOCKED'}))
