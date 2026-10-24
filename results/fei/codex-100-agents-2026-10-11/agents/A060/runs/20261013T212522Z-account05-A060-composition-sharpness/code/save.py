from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];TASK=R.parents[1]
BASE=Path(r'~\brain_workers\FEI100_20261011')
CAN=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
def sha(v):return hashlib.sha256(v).hexdigest()
def write(name,v):(R/name).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def statement_hash(s,h):return sha(json.dumps({'statement':s,'hypotheses':h},sort_keys=True,separators=(',',':')).encode())
protocol=json.loads((CAN/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
main=json.loads((R/'out/validation.json').read_text());repro=json.loads((R/'out/reproduction.json').read_text())
assert main['status']==repro['status']=='PASS'
data=json.loads((R/'out/census.json').read_text());assert not data['failures']
assert all(e['majority3_junta'] for e in data['extremizers'] if e['n'] in [3,5])
assert sum(e['majority3_junta'] for e in data['extremizers'] if e['n']==4)==32
assert repro['equality_cases']==224 and repro['consensus_orbit']==192
statement=('For every balanced Boolean h on n<=4 uniform bits, and every antipodally odd Boolean h on n=5, Lambda(h)<=3 ln(2)(I(h)-1). '
'The maximum ratio for non-dictators is 3 ln(2) for n=3,4 and odd n=5. All 224 n=4 equality tables form two NPN orbits: 32 Maj3 juntas and 192 variants of h that returns x3 if x3=x4, otherwise x1 when x3=+1 and x2 when x3=-1; this h has H=3, I=3/2 and singleton coefficients (1/4,1/4,1/2,1/2). '
'For every even m>=2, d=2^-m, paired quadratic bent b, D=1_(y=0), g_m=D+z(b-D), and 0<x<1, 0<B_z(g_m)-L_z(x)<=d log2(1/x). For even m>=4, L_z(x)/B_z(g_m)>=1-log2(1/x)/m. '
'Consequently for every 0<c<1 the supremum L_j(alpha^2)/B_j(g) over genuine balanced-child disjoint compositions with B_j(g)>0 and |alpha|<=1-c is 1; this also admits a sequence alpha->0. '
'The cap coefficient 1 survives disjoint outer tensor products and cannot be reduced using a fixed additive overhead. In contrast, Lambda of a product of two balanced functions is zero and is not tensor additive.')
hyp=['uniform physical input cube and Boolean sign output','Lambda is singleton-log functional in nats; H,B,L in bits; I ordinary total influence','finite singleton domains are all balanced n<=4 and all antipodally odd n=5, not all balanced n=5 or all dimensions','cap L_j(x)=sum_T phi(ahat_T^2,x bhat_T^2), phi in bits; g=a+z_j b','for coefficient-realization: disjoint input blocks, balanced actual Boolean inner, alpha its queried singleton','tensor overhead assertion requires sums over selected independent factors and a fixed additive term']
cid='A060-SINGLETON-AND-MONOTONE-CAP-SHARPNESS'
claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':statement_hash(statement,hyp),
'contributors':['A060; B12 lead supplied sharpness questions and earlier L1/L2 bounds; X009 source credited'],
'proof_source':{'path':'PROOF.md','sha256':sha((R/'PROOF.md').read_bytes()),'finite_certificate':'out/integer_certificates.json','independent_n4_reproduction':'out/reproduction.json'},
'proof_dependencies':[{'claim_id':'B12-L1-MONOTONE-ERASURE','version':1,'scope':'packet monotonicity/concavity, independently reconstructed in this run; cap counterfamily separately derived'},{'claim_id':'A057-COHERENT-ERASURE-SPLIT','version':1,'scope':'balanced physical B identity; A087 stage2 independent acceptance; explicit inner examples also derived directly'}],
'review_records':[],'status':'AUTHOR_PROVED_AT_SCOPED_DOMAINS_PENDING_INDEPENDENT_REVIEW','supersedes':[],
'refutes':['Maj3 is the unique singleton-log equality family in n=4','any universal strict multiplicative L_j(alpha^2)<=kappa(c)B_j(g), kappa(c)<1, based only on |alpha|<=1-c, 0<c<1','singleton Lambda is additive under products of balanced Boolean functions'],
'first_unproved_line':None,'next_consumers':['A056','A057','A058','A059','A019','A091','A090','B20']}
leadpath=BASE/'claude/B12/runs/20261011T225832Z-claude-B12-erasure-ledger-depth/CLAIMS.json'
lead=json.loads(leadpath.read_text(encoding='utf-8'));reviews=[]
for src,artifact in [('B12-L1-MONOTONE-ERASURE','REVIEW_L1.md'),('B12-L2-DEFICIT-LOG-BANK','REVIEW_L2.md')]:
 original=next(v for v in lead if v['claim_id']==src);entry={k:original[k] for k in protocol['required_per_run']['claim_fields']}
 oldhash=entry['statement_sha256'];entry['statement_sha256']=statement_hash(entry['exact_statement'],entry['hypotheses'])
 entry['review_records']=list(entry['review_records'])+[{'reviewer':'A060','verdict':'HOLDS_AT_STATED_SCOPE','artifact':artifact,'sha256':sha((R/artifact).read_bytes()),'source_claim_file':str(leadpath),'source_claim_file_sha256':sha(leadpath.read_bytes()),'source_recorded_statement_sha256':oldhash,'hash_convention':'canonical statement+hypotheses JSON normalized in this review record','source_report_availability':'source REPORT.md pointer absent locally; complete claim read and proof independently reconstructed','repair_contribution':False}]
 entry['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL';reviews.append(entry)
write('CLAIMS.json',[claim]+reviews)
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B12','packet_id':'A060','gap_id':'G-LOWSEL-COLLISION','attempt_id':'A060-sharpness-02',
'method':'Complete integer singleton-log census, independent direct-character equality-orbit reproduction, swapped bent-sector analytic cap saturation, tensor scope audit and L1/L2 review',
'mathematical_delta':'Sharp 3ln2 finite gate constant with a new four-bit equality orbit; all-dimensional cap coefficient 1 remains necessary even with alpha bounded away from one or alpha->0; singleton Lambda not tensor additive; original L1/L2 independently accepted at scope',
'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_SHARPNESS_PROVED_UNREVIEWED; GLOBAL_SHARP_SINGLETON_BOUND_OPEN; UNIVERSAL_C019_PAYMENT_OPEN; FULL_FEI_OPEN',
'claim_versions_used':['B12-L1-MONOTONE-ERASURE@1 (reviewed in this run)','B12-L2-DEFICIT-LOG-BANK@1 (reviewed in this run)','A057-COHERENT-ERASURE-SPLIT@1 (A087 stage2 HOLDS consumed)','A057-NONREUSING-ALPHA-LOG-PAYMENT@1 (A087 HOLDS consumed at scope)','A057-CAPPED-RECENTERED-ACTIVATION-TREE-BANK@1 (A058 HOLDS consumed, not a premise of new proof)','ERASURE_RIGIDITY X009 sections 2-3 (chi-square independently derived)'],
'claims_created_or_changed':[cid+'@1','B12-L1-MONOTONE-ERASURE@1: local independent HOLDS','B12-L2-DEFICIT-LOG-BANK@1: local independent HOLDS'],
'source_artifacts':['PROOF.md','REPORT.md','REVIEW_L1.md','REVIEW_L2.md','CONSTANT_SCOPE.json','FROZEN_SPEC.json','FROZEN_SPEC_V2.json','code/check.py','code/reproduce.py','out/validation.json','out/census.json','out/integer_certificates.json','out/reproduction.json','out/SOURCES.json'],
'next_consumers':claim['next_consumers'],
'next_action':'On the first two-core priority activation with overlapping controls, price actual biased packet imbalance from one owned reserve and retain both terminal core entropies; use saturated g_m=D+z(b-D) against any proposed relative cap saving. Reviewers A091/A090.',
'stagnant_substantive_attempts':0,'blockers':['All-dimensional sharp Lambda<=3ln2(I-1) remains unproved; even all balanced n=5 not certified','Universal biased-descendant/terminal entropy reserve unpaid','External review, supervisor adoption and mirror copies pending'],
'packet_ids':['A060']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
write('CONSTANT_SCOPE.json',{'singleton_constant':{'units':'nats','necessary_lower_bound':'3 ln2','certified_upper_bound':'3 ln2 on all balanced arity<=4 and odd arity5','general_dimension':'original 4+6/e accepted locally; proposed 3 ln2 OPEN','n4_equality_orbits':{'Maj3_juntas':32,'four_input_selector':192},'tensorization':'not additive; product of balanced factors has zero singleton Lambda'},'monotone_cap':{'coefficient':1,'sharpness':'supremum 1 for every fixed 0<c<1 with |alpha|<=1-c; also alpha->0 sequence','family':'g_m=D+z(b-D), m even','loss_bound_bits':'0<B-L<=2^-m log2(1/x)','explicit_ratio_bound':'for even m>=4, L/B>=1-log2(1/x)/m; m=100,x=1/4 gives >=49/50','outer_selector_influence':'1-2^-m; NOT the small original X009 selector influence','physical_inner_query_influence':'1 for s*v; 1/2 for Maj3','data_influence':'m(1/2+2^-m)','tensorization':'each selected B and L preserved by a disjoint Boolean spectator; sum over copies additive; fixed additive overhead erased','hypothesis_needed_for_strict_relative_gain':'control packet A_T/V_T or source-sensitive reserve; singleton gap alone insufficient'},'physical_tree':{'known':'local gate constants telescope only for certified balanced disjoint gate representations','unpaid':'biased physical descendants, current packet debt, nonempty inner decrement, terminal core entropy and common influence ownership'},'full_FEI':'OPEN'})
paths=[CAN/'EXECUTION_PROTOCOL.json',BASE/'BOARD.md',BASE/'claude/B12/STREAM_NOTES.md',BASE/'claude/B12/LEARNED.md',leadpath]
paths += [BASE/'agents/A087/runs/20261012T004155Z-account05-A087-restriction-referee/REPORT.md',BASE/'agents/A057/runs/20261012T003930Z-account05-A057-coherent-restriction-remainder/REPORT.md',BASE/'agents/A057/runs/20261012T003930Z-account05-A057-coherent-restriction-remainder/PROOF.md',BASE/'agents/A058/runs/20261012T020138Z-account05-A058-overlapping-compositions/REVIEW_A057.md',BASE/'agents/A058/runs/20261012T020138Z-account05-A058-overlapping-compositions/out/review_results.json']
paths += [SUP/'sources/ERASURE_RIGIDITY.md',BASE/'context/threshold_paper_38pp.txt',TASK/'runs/20261011T230152Z-account05-A060-composition-sharpness/PROOF.md']
write('out/SOURCES.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes()),'read_scope':'See REPORT.md; prior manuscript/source reads retained as provenance, not fresh whole-file audits.'} for p in paths])
expected={s.split(' (',1)[0] for s in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
assert all(set(v)==set(protocol['required_per_run']['claim_fields']) for v in [claim]+reviews)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
report=(R/'REPORT.md').read_text(encoding='utf-8');assert all(s in report for s in protocol['required_per_run']['report_fields'])
assert report.rstrip().endswith('singleton census would leave the universal transport cost unpaid.')
write('out/SCHEMA_CHECK.json',{'status':'PASS','claim_fields_exact':True,'progress_fields_exact':True,'packet_ids_annotation_normalized':True,'delta_byte_identical':True,'required_report_fields_present':True,'universal_bridge_at_end':True,'mathematical_assertions':main['assertions']+repro['assertions'],'independent_n4_equality_masks_agree':True})
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(TASK/'STATUS.md').write_text('STATE: A060 stage2 saved: sharp Lambda=3ln2 through balanced n4/odd n5, 192 new n4 equality variants; monotone cap coefficient 1 saturated even alpha->0; 340063 exact checks PASS; global sharp Lambda and FEI OPEN.\nNEXT: A091/A090 review; price actual two-core overlapping-control packet debt with one owned reserve and both terminal entropies; singleton gap alone cannot discount the cap.\n',encoding='utf-8')
with (TASK/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+now+' Stage 20261013T212522Z: followed B12 v2 sharpness target. Corrected singleton/influence pilot assertion; full census exposed unsupported Maj3-only classification (mask1343), not a bound failure. Exhausted 78484 frozen functions; 314298 main checks and 25765 independent checks PASS. Classified n4 equality orbits (32 Maj3,192 four-input selector), proved all-m cap saturation including alpha->0 and tensor distinction; independently accepted original L1/L2 at scope. Sharp global Lambda and universal tree reserve remain OPEN. Saved protocol artifacts; supervisor adoption/review pending.\n')
with (TASK/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('''
# Stage 2 durable facts

- All balanced n<=4 and all odd n=5 satisfy Lambda<=3ln2(I-1), exactly certified. Max ratio is 3ln2 in balanced n3/n4 and odd n5. All balanced n5 and the all-dimensional sharp bound remain OPEN.
- There are 224 equality tables at n4: 32 signed Maj3 juntas and 192 variants of h that returns x3 when x3=x4, otherwise x1 if x3=+ and x2 otherwise. This balanced h has singleton coefficients (1/4,1/4,1/2,1/2), I=3/2, H=3, Lambda=(3/2)ln2. Mask1343. Maj3 is not the unique equality example.
- Swapped bent splice g_m=D+z(b-D), d=2^-m: selected influence 1-d, data influences 1/2+d; absent-selector packet mass d^2, present packet (sign sqrt(d)-d)^2. For 0<x<1, 0<B-L(x)<=d log2(1/x). For even m>=4, B>=dm and L/B>=1-log2(1/x)/m. Thus cap coefficient1 cannot be uniformly reduced using |alpha|<=1-c,0<c<1, even for alpha->0 slowly.
- Actual inner h=s*v(w) realizes alpha=Ev and B_s(h)=0, Inf_s(h)=1. Do not identify singleton coefficient with influence. In the composite D+h(b-D), singleton is alpha(sqrt(d)-d), while query influence is (1-d)Inf_s(h).
- Outer disjoint spectators preserve each B_j and L_j, so the cap coefficient1 survives tensorization and fixed additive overhead vanishes for sums over copies. Singleton Lambda is not additive: products of two balanced functions have zero singleton spectrum. Ordinary tensor powers cannot erase additive overhead in a Lambda bound.
- Local gate-log coefficient3ln2 is certified only for balanced arity<=4/odd arity5; biased physical descendants remain outside this statement. L1 monotone cap and L2 original4+6/e lemma independently reconstructed locally; no universal C019 price inferred.
- Validation uses exact positive integer products, no floating signs; main314298 + independent25765 =340063 checks. Independent n4 enumeration filters masks rather than combinations and uses direct character sums rather than FWHT. Initial wrong equality classification was retained as a discovery record.
- Shortest next mechanism: current biased packet debt and common reserve on two distinct activated cores sharing a control, retaining both terminal core entropies. A strict relative cap discount based only on alpha is unavailable.
''')
receipts=[]
for p in list(R.rglob('*'))+[TASK/'STATUS.md',TASK/'WORKLOG.md',TASK/'LEARNED.md']:
 if p.is_file() and p.name!='PERSISTENCE.json':
  v=p.read_bytes();assert len(v)<20*1024*1024
  receipts.append({'path':str(p),'bytes':len(v),'sha256':sha(v)})
write('out/PERSISTENCE.json',{'saved_at_utc':now,'status':'LOCAL_READBACK_HASHED','external_review':'PENDING','supervisor_copy':'PENDING_NOT_CLAIMED','mirror_verification':'PENDING_NOT_CLAIMED','assertions':main['assertions']+repro['assertions'],'files':receipts})
print(json.dumps({'status':'PASS','schema':'exact','files_hashed':len(receipts),'assertions':main['assertions']+repro['assertions'],'save_time_utc':now}))
