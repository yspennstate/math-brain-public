from pathlib import Path
from fractions import Fraction as F
import hashlib,json,re

R=Path(__file__).resolve().parents[1];A=R.parents[1];ROOT=A.parents[1]
def put(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False),encoding='utf-8')
def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def get(p):return json.loads(p.read_text(encoding='utf-8'))
protocol_path=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=get(protocol_path)
batches=[get(R/'out'/('BATCH_'+str(j)+'.json')) for j in range(4)]
assert all(x['status']=='PASS' and x['runtime_seconds']<55 for x in batches)
records=[y for x in batches for y in x['records']]
expected={(w,m,d,str(e)) for w in (4,5) for m in (2,3) for d in range(w+1) for e in (F(0),F(1,4))}
actual={(x['w'],x['m'],x['d'],x['eta']) for x in records}
assert actual==expected and len(records)==len(actual)==44
assert get(R/'out/PILOT.json')['status']=='PASS'
result={'status':'PASS','histories':44,'assertions':sum(x['assertions'] for x in batches),'frontiers':sum(x['frontiers'] for x in batches),'resets':sum(x['resets'] for x in batches),'runtime_seconds_sum':sum(x['runtime_seconds'] for x in batches),'maximum_helper_seconds':max(x['runtime_seconds'] for x in batches),'batches':[{'id':j,**{k:x[k] for k in ['histories','assertions','frontiers','resets','runtime_seconds']}} for j,x in enumerate(batches)],'excluded_counts':'all v1 and pilot counts excluded','checker_sha256':sh(R/'code/check.py'),'records':records}
put(R/'out/EXACT_RESULTS.json',result)
root_coeff=(31-8)-F(31+15,8)
final_coeff=root_coeff-F(69,8)-F(11,4)
assert root_coeff==F(69,4) and final_coeff==F(47,8)
for t in range(65):
    assert sum((4*F(1,2**(j+2)) for j in range(1,t+1)),F(0))==1-F(1,2**t)
fixtures=[x for x in records if x['d']==0 and x['eta']=='1/4']
assert len(fixtures)==4
for x in fixtures:assert F(x['actual_charges'][0]['actual_signed_charge'][0])>0
fixture=next(x for x in fixtures if x['w']==4 and x['m']==2)
e0=fixture['actual_charges'][0]['actual_signed_charge']
put(R/'out/COEFFICIENT_CERTIFICATE.json',{'status':'PASS','root_source_coefficient':str(root_coeff),'old_U_coefficient':'69/8','fresh_chain_upper':'11/4','remaining_source_coefficient':str(final_coeff),'remaining_creation_coefficient':16,'geometric_checks_t0_to64':65,'first_actual_floor_handoff_positive_fixtures':4,'w4m2_eta_quarter_actual_first_charge_interval':e0,'infinite_extension':'DERIVATION geometric identity and source/core inequalities; finite sequence checks not extrapolated'})

src17=A/'runs/20261022T235414Z-fleet03-A095-restricted-result-extraction'
src16=A/'runs/20261021T180853Z-fleet03-A095-restricted-result-extraction'
dep17=next(x for x in get(src17/'CLAIMS.json') if x['claim_id']=='A095-TWO-NARROW-RESETS-SAME-RATE4-BANK')
dep16=next(x for x in get(src16/'CLAIMS.json') if x['claim_id']=='A095-UNBOUNDED-WIDTH-SIGNED-PROFILE-HISTORY')
statement='For every w>=4,m>=2, source g=h_w*h_2, h_j=1-2 indicator(all j inputs zero), source R=P_g and one fair-selector full-zero point edit F, start from the actual normalized A011 data floor (P_g padded+3delta U)/(1+3delta), lifted by the true selector-frequency kernel, delta=2^(-w-m-2). Fix original C0=4,K=31 and retain any external prior debit0<=U<=69I_g/8. Under actual normalized physical-posterior inheritance, any finite adaptive wide-only query tree may be followed on its zero leaf by the two prescribed narrow-zero resets: first to (1-eta)Qcan(h_t*h_1)+eta full-uniform, eta in[0,1/4], then to Qcan(-h_t), followed by resets at any subset of the remaining-wide zero queries to their actual Qcan(-h_(t-j)). Selector and padding are unqueried until the chain ends. Every intermediate full signed ledger L=H(F)+sum reached terminal D obeys31I(F)-U-L>47I_g/8+16(m+1)delta>0, retaining every full sibling terminal and all old debits. The STRONGER bill B_full, retaining every reached complete CE query release plus all full current terminal CE, obeys the SAME reserve bound; B_full=CEroot+sum actual signed reset e and L<=B_full, so no physical-divergence credit need be reclaimed. All positive reset debits sum to less than11/4; the number of resets is unbounded as w grows. Later inherited queries without resets preserve the bound. This is an explicit source/family single-path transfer theorem, not a universal FEI result or new-edit iteration.'
hypotheses=['Uniform Boolean cube, normalized Walsh spectrum, physical uniform query reach and ideal base2 complete-reference costs','Exact initial floor/control lift, original source R=P_g and K31; no identification with the earlier canonical-root rate4 account','Actual current inherited references and mass normalizers, full complementary terminals and external U remain; negative reset credits need not be reclaimed','Only the zero path is reset; one-child complements keep their complete inherited models; no padding/selector query before the reset chain ends','Qcan uses the true old source support and its actual point-selector completion; h_0=-1 and constant/character boundaries retained']
claim={'claim_id':'A095-FLOOR-HANDOFF-UNBOUNDED-NESTED-CANONICAL-CHAIN','version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':hashlib.sha256(json.dumps({'exact_statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest(),'contributors':['A095/fleet03'],'proof_source':{'path':str(R/'DERIVATION.md'),'sha256':sh(R/'DERIVATION.md'),'sections':'1-4; exact scope and universal gap in5'},'proof_dependencies':[{'claim_id':dep17['claim_id'],'version':dep17['version'],'statement_sha256':dep17['statement_sha256'],'scope':'ONLY all-t/all-m complete fresh canonical cost bounds; original canonical-root model and rate4 account not transplanted'},{'claim_id':dep16['claim_id'],'version':dep16['version'],'statement_sha256':dep16['statement_sha256'],'scope':'source entropy formula, independently rederived here; no canonical incoming model used'}],'review_records':[],'status':'ANALYTIC_AUTHOR_PROOF_EXACT_CASES_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':'None within stated single-path transfer theorem. Branching/new Boolean edits at fixed original source/rate, and arbitrary initial influence-paid source supply, remain open.','next_consumers':['A094','A086','A011','A081','A096','A097','A099']}
put(R/'CLAIMS.json',[claim])
next_action='A094/A086 independently reconstruct actual floor handoff and geometric complete-terminal payment. A011 test actual two-edit/multiple-active-path conversion at fixed original C0,K, full old U and both terminals; no renewed source supplier.'
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B19','packet_id':'A095','gap_id':'C020-C024-SAME-OWNER-SIGNED-PROFILE','attempt_id':'A095-stage19-floor-handoff-unbounded-nested-chain','method':'Independent fair-selector floor-envelope derivation; actual complete posterior KL ledger; source-complete fresh canonical costs and geometric ORIGINAL reach; exact Boolean/terminal reconstruction','mathematical_delta':'Actual floor-to-canonical handoff plus dimension-unbounded nested canonical-reset chain at ONE original K31, external U<=69Ig/8, full positive reset total<11/4, all-frontier reserve>47Ig/8+16G. No new FEI Boolean class or universal constant advance.','deliverable_status':'COMPLETE_LOCAL_REVIEW_PENDING','mathematical_status':'RESTRICTED_HISTORY_TRANSFER_PROVED_BY_AUTHOR_FULL_FEI_OPEN','claim_versions_used':[dep17['claim_id']+'@1 canonical fresh costs only',dep16['claim_id']+'@1 source entropy only'],'claims_created_or_changed':[claim['claim_id']+'@1'],'source_artifacts':['DERIVATION.md','out/EXACT_RESULTS.json','out/COEFFICIENT_CERTIFICATE.json','out/SOURCE_RECEIPTS.json','out/FAILURE_V1.json','out/SPEC_AMENDMENT_V2.json'],'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Independent review of new scoped theorem pending','Branching/new-edit aggregation at fixed original source/rate remains open','Universal initial source-reference supply remains open','Supervisor mirror/adoption unverified','Brain wake attachment rendering failed; owner model/state/dream stale; these notes excluded from proof premises'],'packet_ids':['A095']}
put(R/'PROGRESS.json',progress);put(R/'PACKET_DELTA.json',progress)
src94=ROOT/'agents/A094/runs/20261023T110024Z-fleet03-A094-proof-chain-challenger'
src86=ROOT/'agents/A086/runs/20261023T053719Z-fleet03-A086-joint-code-referee'
src11=ROOT/'agents/A011/runs/20261023T000841Z-fleet03-A011-representation-existence'
sources=[protocol_path,ROOT/'BOARD.md',ROOT/'claude/B19/STREAM_NOTES.md',src94/'REPORT.md',src94/'DERIVATION.md',src86/'REPORT.md',src11/'DERIVATION.md',src17/'DERIVATION.md',src17/'CLAIMS.json',src16/'CLAIMS.json',src16/'code/check.py']
put(R/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sh(p),'bytes':p.stat().st_size,'scope':'proof text or exact dependency metadata actually consumed; shared source unchanged; board hash is final local read, not an immutable initial snapshot'} for p in sources])
rp=R/'REPORT.md';txt=rp.read_text(encoding='utf-8')
txt=re.sub(r'Final v[23] PASS:.*? Initial pilot','Validation totals will be inserted from authoritative saved receipts. Initial pilot',txt,flags=re.S)
txt=txt.replace('Validation totals will be inserted from authoritative saved receipts.',f"Final v3 PASS: {result['histories']} histories, {result['frontiers']} frontiers, {result['resets']} actual resets, {result['assertions']} exact assertions. Four disjoint helpers total{result['runtime_seconds_sum']:.3f}s, maximum{result['maximum_helper_seconds']:.3f}s. Pilot and previous-version counts excluded. BOTH entropy-release ledger L and stronger complete-query-release bill B_full are reconstructed separately with the SAME reserve. For w4,m2,d0,eta1/4 the ACTUAL floor-inherited first handoff is strictly positive, certified in interval [{e0[0]},{e0[1]}]; this is a paid conversion, not a reference renaming.")
rp.write_text(txt,encoding='utf-8')
(A/'STATUS.md').write_text(f"STATE: Stage19 saved: ACTUAL floor-to-canonical handoff plus UNBOUNDED nested reset chain paid SAME original K31, full old U<=69Ig/8, both terminals; reserve>47Ig/8+16G; {result['assertions']} exact checks PASS; review pending; FEI OPEN.\nNEXT: A094/A086 review actual inherited handoff/geometric payment; A011 test TWO-edit/multiple-active-path fixed-C0/K aggregation with full old U and BOTH complete terminals; no renewed source.\n",encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f"\n2026-10-23 stage19 final audit ({R.name}): strengthened to retain EVERY complete CE query release. B_full=CEroot+sum actual signed reset e, L=Hroot+E terminal D<=B_full; SAME reserve for BOTH, no physical-divergence credit reclaimed. Unchanged44-history v3 replay: {result['assertions']} assertions/{result['frontiers']} frontiers/{result['resets']} resets PASS. v2 receipts preserved and excluded from final counts. New proof review pending; FEI OPEN.\n")
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-23 stage19 final audit: Distinguish physical entropy-release ledger L=Hroot+E terminal D from stronger B_full=sum COMPLETE CE query releases+sum full terminal CE. Exact B_full=CEroot+sum reset e, while B_full-L is accumulated nonnegative physical divergence release. The floor-handoff/unbounded-chain reserve47Ig/8+16G holds even for B_full and with all positive reset debits booked, so no transport credit is required. Both identities independently reconstructed in v3 replay; do not equate L and B_full.\n')

pf=set(protocol['required_per_run']['progress_fields']);pf.remove('packet_ids (one primary ID, for compatibility)');pf.add('packet_ids')
assert set(progress)==pf
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all(h in txt for h in protocol['required_per_run']['report_fields'])
assert txt.rstrip().split('## Universal bridge')[-1].strip()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
put(R/'out/SCHEMA_VALIDATION.json',{'status':'PASS','exact_field_sets':True,'progress_delta_identical':True,'new_statement_hash_verified':True,'histories':44,'assertions':result['assertions'],'all_main_domains_distinct':True,'all_helpers_below55s':True,'all_full_frontiers_checked':result['frontiers'],'all_old_debits_and_both_terminals_retained':True,'full_fei':'OPEN','independent_review':'PENDING','external_mirror':'UNVERIFIED'})
manifest=[]
for p in list(R.rglob('*'))+[A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']:
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20_000_000
        manifest.append({'path':str(p),'sha256':sh(p),'bytes':p.stat().st_size})
put(R/'out/PERSISTENCE_RECEIPTS.json',manifest)
assert all(sh(Path(x['path']))==x['sha256'] for x in manifest)
print(json.dumps({'status':'PASS','histories':44,'assertions':result['assertions'],'frontiers':result['frontiers'],'resets':result['resets'],'files_hashed':len(manifest),'FEI':'OPEN','review':'PENDING'}))
