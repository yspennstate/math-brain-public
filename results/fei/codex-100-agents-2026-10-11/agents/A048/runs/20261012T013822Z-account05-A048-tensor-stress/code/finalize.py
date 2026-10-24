from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parents[1]
BASE=Path('~/mop_fei100/reports/fei-2026-10-11')
TEAM=Path('~/brain_workers/FEI100_20261011')
protocol=json.loads((BASE/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
check=json.loads((ROOT/'out/CHECK.json').read_text(encoding='utf-8'))
assert check['status']=='PASS' and sum(check['counts'].values())==6939 and check['runtime_seconds']<60
def dump(p,obj):p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
statement='For tau*(p)=h2(p)-min_t[h2(sin^2 t)+h2(sin^2(t-b))], sin^2 b=min(p,1-p), tau*(1/2)=0 and tau*(1/8)>1195/10000. On actual q=1/8 product-biased r-bit point-defect signs every optimal essential computing tree has tax bill tau*(q)(1-q^r)/(1-q), whose ratio to both physical influence and spectral energy is unbounded. On arbitrary-product-biased point-defect short-circuit trees and finite disjoint tensors, sum_v w_v[J_v-M_v]_+<=4 I_phys, retaining D_v=tau*(p_i)-(J_v-M_v)>=0. On the fair 13-bit point defect with a three-fair-bit mask collapsed to one p=1/8 coordinate, its scalar tax exceeds K_KL+8I although actual physical taxes are zero. These are payment scope tests, not a refutation of the uncertainty or A036 collision inequalities.'
hypotheses=['Actual Boolean sign point defects and independent product input laws','Entropy in bits, empty coefficients retained','Essential singleton computing trees, no coordinate reuse along a path','Physical influence and biased spectral energy distinguished','Disjoint factors only for tensor extension; arbitrary terminal factors remain unpaid','No half-tax upper theorem or block additivity assumed']
claim={'claim_id':'A048-SHARP-TAX-PAYMENT-SCOPE','version':1,'exact_statement':statement,'hypotheses':hypotheses,
 'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['A048'],'proof_source':{'run':ROOT.name,'files':['REPORT.md','TAX_PAYMENT_LEDGER.tex','code/check.py','out/CHECK.json']},
 'proof_dependencies':[],'review_records':[],'status':'SCOPED_EXISTING_PAYMENT_VERIFICATION_PROVED_LOCALLY_PENDING_REVIEW',
 'supersedes':[],'refutes':['Universal influence payment of the current sharp scalar tax on all essential product-biased revealed bits','Universal extra collapsed-mask scalar tax payment by fixed a*K_KL+b*I on uniform point-defect activations'],
 'first_unproved_line':None,'next_consumers':['A050','A064','A047','A040','A092','A087','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields']);dump(ROOT/'CLAIMS.json',[claim])
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B10','packet_id':'A048','gap_id':'G-BIASED-TAX','attempt_id':'A048-sharp-tax-payment-2',
 'method':'Lead-directed existing tax payment verification; exact essential Boolean trees, angular reserve cancellation, channel erasure coupling and rational witnesses.',
 'mathematical_delta':'Essential sharp-tax payment refuted on optimal biased point-defect trees; actual fair tax zero on A036 class; collapsed-mask overcharge certified at N=13 even against K_KL+8I; positive reserve-corrected debt paid <=4I_phys on biased point-defect tensors; reserve cancels asymptotically all scalar overcharge.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_PAYMENT_RESOLVED; GENERAL_RESERVE_TRANSPORT_AND_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'B10 sharp singleton angular tax','version':'lead v2 2026-10-11 23:31Z','role':'definition and elementary identity independently reconstructed; half-tax proof not assumed'},{'claim_id':'A036 normalized collision payment','version':1,'role':'uniform class/hypotheses only; inequality not assumed'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'role':'existing-payment verification and refutation; no new broad potential'}],
 'source_artifacts':['REPORT.md','TAX_PAYMENT_LEDGER.tex','PAYMENT_GUARDS.md','FROZEN_SPEC.json','code/check.py','out/CHECK.json','out/SOURCE_MANIFEST.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Derive actual positive-debt/uncertainty-defect ownership for two overlapping activation events sharing a core, with one physical influence account per control and arbitrary terminal entropy retained.',
 'stagnant_substantive_attempts':0,'blockers':['Independent review and supervisor mirror unverified; no mathematical or save blocker.'],'packet_ids':['A048']}
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
dump(ROOT/'PROGRESS.json',progress);dump(ROOT/'PACKET_DELTA.json',progress)
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '# '+field in report
assert report.rstrip().split('\n\n')[-2]=='# Universal bridge'
sources=[(TEAM/'BOARD.md','Start-stage snapshot inspected'),(TEAM/'claude/B10/STREAM_NOTES.md','v2 full lead directions'),(BASE/'EXECUTION_PROTOCOL.json','Protocol inherited in full from stage 1 and schema reread')]
sources.extend([(TEAM/'claude/B10/runs/20261011T230400Z-claude-B10-onebit-half-tax/REPORT.md','Tax definition, angular reduction and payment target; no half-tax certificate acceptance'),(TEAM/'agents/A036/runs/20261011T214139Z-account05-A036-reference-law-divergence/REPORT.md','Uniform product-reference hypotheses and exact K identity'),(TEAM/'agents/A050/runs/20261011T230000Z-account05-A050-repair-with-scope/REPORT.md','OI repair and actual-tree terminal scope'),(TEAM/'agents/A100/runs/20261011T231552Z-account05-A100-release-and-continuation-ledger/REPORT.md','Earlier positive uniform-tax obstruction; current zero-fair tax excluded by that source'),(AGENT/'runs/20261011T221822Z-account05-A048-tensor-stress/REPORT.md','Prior own tensor and general-mean activation proof'),(AGENT/'runs/20261011T221822Z-account05-A048-tensor-stress/code/check.py','Exact prime-log and rational interval primitives reused')])
dump(ROOT/'out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'scope':scope} for p,scope in sources])
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A048 stage 2 complete: essential sharp-tax payment refuted, fair tax zero, positive retained defect-tree debt <=4I_phys; 6,939 cases/32,888 assertions PASS; FEI OPEN, review pending.\nNEXT: A092/A087 review; A050/A064 derive uncertainty-defect ownership for two overlapping controls sharing a core, preserving conditional M and all terminal entropy.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'{now}: Stage 2 followed B10 v2 sharp-tax payment target. Read A100 and avoided repeating its obsolete positive uniform-tax diagnostic. Derived essential biased and collapsed-mask obstructions, arbitrary-bias erasure-coupling payment of actual positive debt, and asymptotically full uncertainty-defect cancellation. Frozen 6,939 cases passed 32,888 exact assertions in {check["runtime_seconds"]:.4f}s. No half-tax proof, block additivity, or biased extension of A036 assumed. Required local artifacts saved; review/mirroring pending.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('Stage 2: The angular sharp tax tau*(1/2)=0, while tau*(1/8)>1195/10000 by an actual AND debt certificate. For q=1/8 defects, every essential computing tree has expected scalar tax tau*(q)(1-q^r)/(1-q) and I_phys=rq^(r-1), so essentiality does not pay blanket tax. The actual reserve D=tau*-(J-M) cancels asymptotically all overcharge. For any product-biased point-defect tree and disjoint factors, sum w[J-M]_+<=sum wJ<=4I_phys by an independent erasure flag. A fixed three-fair-bit logical mask on a growing fair defect has positive collapsed tax but physical tax zero; even K_KL+8I<143/2048 at N=13 cannot pay tau*(1/8). Actual transcript entropy also has unbounded influence ratio. Keep physical and logical coordinates, the D reserve, conditional M and terminal entropy distinct.\n')
receipts=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.name not in ('RECEIPTS.json','VALIDATION.json'):
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
dump(ROOT/'out/RECEIPTS.json',receipts)
dump(ROOT/'out/VALIDATION.json',{'status':'PASS','at_utc':now,'exact_protocol_fields':True,'progress_copies_identical':True,'claim_hash':claim['statement_sha256'],'all_files_under_20MB':True,'cases':6939,'assertions':32888,'candidate_cap':'existing lead-directed payment verification; no new broad potential','independent_review':'UNVERIFIED','mirror':'UNVERIFIED'})
print(json.dumps({'status':'PASS','cases':6939,'assertions':32888,'receipt_count':len(receipts)}))
