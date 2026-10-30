"""Write protocol-exact handoff records and local readback receipts; no shared mutations."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
REPORTS=Path('~/mop_fei100/reports/fei-2026-10-11')
SUPP=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
CONTEXT=Path('~/brain_workers/FEI100_20261011/context')
TEAM=Path('~/brain_workers/FEI100_20261011')
stamp=datetime.now(timezone.utc).isoformat()
def digest(b): return hashlib.sha256(b).hexdigest()
def save(name,obj): (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
protocol=json.loads((REPORTS/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
check=json.loads((ROOT/'out/CHECK.json').read_text(encoding='utf8'))

sources=[]
def receipt(path,scope):
    if path.exists():
        b=path.read_bytes()
        sources.append({'path':str(path),'sha256':digest(b),'bytes':len(b),'scope':scope})
    else:
        sources.append({'path':str(path),'status':'ABSENT','scope':scope})

for name in ('EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex'):
    receipt(REPORTS/name,'Protocol full; navigation/state and B04 acceptance/bridge sections as described in REPORT.md. Hash records file revision, not independent audit.')
for name in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md'):
    receipt(SUPP/name,'Campaign scope, controls and crosswalk; decisive locators in REPORT.md.')
for path in sorted((SUPP/'sources').glob('*')):
    receipt(path,'Source inventory; mathematical use only for the specific locators named in REPORT.md. Inventory hashing is not a claim of full proof audit.')
for path in sorted(CONTEXT.glob('*.txt')):
    receipt(path,'Text version consulted for stated scope/locators; no percolation theorem or earlier-version theorem is a proof premise.')
receipt(TEAM/'BOARD.md','Read at stage start')
receipt(TEAM/'claude/B04/STREAM_NOTES.md','Lead direction lookup at stage start')
for name in ('A017','A091'):
    receipt(TEAM/'agents'/name/'LEARNED.md','Read-only downstream context')
for path in sorted((REPORTS/'runs').rglob('REPORT.md')):
    receipt(path,'Earlier-run inventory; B05 and B19 no-go scope consulted; B09 not accepted as a premise')
save('out/SOURCE_RECEIPTS.json',{'recorded_at_utc':stamp,'sources':sources,'mirror_verified':False})

statement=('For all fresh uniform physical selector blocks W of a bits and arbitrary Boolean branches g_b on one common uniform data cube, define R_T=E_b hat(g_b)(T)^2, r_T(b)=hat(g_b)(T)^2/(2^a R_T), nu_T(A)=hat(F)(A,T)^2/R_T, omitting R_T=0. Then Delta_W H=B_W+M_W, where B_W=sum_T R_T H(nu_T)=H(S_W|S_data), M_W=a-sum_T R_T H(r_T), and 0<=M_W<=(2/ln 2) I_W. M_W=0 iff all branch squared spectra coincide. Delta_W H=0 iff each nonzero coefficient row is a scalar Walsh character. For even m>=2 the bent/one-point-flip Boolean splice has I_W=2^{-m} and B_W>=2^{-m}(m-1), so a universal selector-only linear payment is false. These are source-complete reconstructions/characterizations, not a proof of full FEI.')
consumers=['A017','A019','A020','A026','A027','A037','A057','A058','A061','A063','A091','A090']
claim={
 'claim_id':'A018-COLLISION-BLOCK-INTERFACE','version':1,
 'exact_statement':statement,
 'hypotheses':['All g_b Boolean on the same uniform finite data cube','Selector coordinates fresh from data and uniform independent','Entropy in bits; physical influence; zero-mass rows omitted'],
 'statement_sha256':digest(statement.encode()),'contributors':['A018 (reconstruction and characterization; inherited baseline attribution in REPORT.md)'],
 'proof_source':'REPORT.md, complete derivation sections 1-5; COLLISION_BLOCK_INTERFACE.tex; code/check_collision.py; out/CHECK.json',
 'proof_dependencies':[],
 'review_records':[{'status':'AUTHOR_EXACT_VERIFICATION_ONLY','assertions':check['assertions'],'independent_reviewers_requested':['A091','A090']}],
 'status':'SOURCE_COMPLETE_BASELINE_RECONSTRUCTION_INDEPENDENT_REVIEW_PENDING',
 'supersedes':None,'refutes':[],
 'first_unproved_line':None,'next_consumers':consumers
}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save('CLAIMS.json',{'claims':[claim]})

next_action=('A019: test the unpaid B_W on common-spectrum quadratic selector phases using physical row influence, then a nonlinear input-translation class with I_W/a tending to zero; avoid repeating A017 address-rank census. A091/A090 reconstruct posterior tensorization and cancellation classification. Universal stopping-tree B_W/terminal payment remains open.')
progress={
 'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B04','packet_id':'A018',
 'gap_id':'G-LOWSEL-COLLISION','attempt_id':'A018-stage1-interface-reconstruction',
 'method':'Exact normalized Walsh row ledger; auxiliary probability law; elementary two-point/product entropy proof; exhaustive integer/Fraction and prime-log certification',
 'mathematical_delta':'Posterior M_W is paid by (2/ln2)I_W; all unpaid collision entropy is B_W. Complete cancellation requires Walsh-character coefficient rows, stronger than common squared spectra for a>=2. Bent-splice local-payment failure reconstructed with explicit m-1 lower bound.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT_PERSISTED',
 'mathematical_status':'A018_INTERFACE_RESOLVED_LOCALLY; INDEPENDENT_REVIEW_PENDING; UNIVERSAL_FEI_OPEN',
 'claim_versions_used':[],
 'claims_created_or_changed':['A018-COLLISION-BLOCK-INTERFACE@1 (baseline reconstruction, not a new broad candidate)'],
 'source_artifacts':['REPORT.md','COLLISION_BLOCK_INTERFACE.tex','COLLISION_CONTROLS.json','code/check_collision.py','out/FROZEN_SPEC.json','out/CHECK.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':consumers,'next_action':next_action,
 'stagnant_substantive_attempts':0,
 'blockers':['B04 STREAM_NOTES.md absent; independent lead direction unavailable','Independent review and supervisor copy/mirror verification pending; these do not block the local proof'],
 'packet_ids':['A018']
}
# Protocol's packet_ids entry includes a prose parenthetical, not part of the key.
expected_progress={field.split(' (')[0] for field in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected_progress
save('PROGRESS.json',progress); save('PACKET_DELTA.json',progress)
save('COLLISION_CONTROLS.json',{
 'identity':'Delta_W H=B_W+M_W','posterior_payment':'0<=M_W<=(2/ln2) I_W',
 'identical_branches':{'M_W':0,'B_W':0,'I_W':0},
 'common_spectrum_is_not_full_cancellation':{'F':'(-1)^(b1*b2) y','a':2,'M_W':0,'B_W':2,'I_W':1,'I_data':1},
 'bent_splice':{'domain':'even m>=2','I_W':'2^-m','B_W_lower_bound':'(m-1) 2^-m','status':'Inherited no-go reconstructed; not FEI disproof','executed_cases':check['bent_splices']},
 'exact_validation':{'assertions':check['assertions'],'block_cases':check['block_cases'],'signed_literal_cases':check['signed_literal_cases'],'elapsed_seconds':check['elapsed_seconds'],'phase_histograms':check['phase_histograms']},
 'unpaid':'B_W and stopping-tree terminal entropy','full_fei_status':'OPEN'
})

(AGENT/'STATUS.md').write_text('STATE: A018 packet complete locally: normalized collision B_W+M_W, posterior <=(2/ln2)I_W, exact cancellation classification and bent-splice guard; 31,794 exact assertions PASS; review pending; full FEI OPEN.\nNEXT: A091/A090 reconstruct; A019 pay common-spectrum quadratic phase B_W with physical influence and test low selector energy; A027 retain B_W/terminal stopping-tree debt.\n',encoding='utf8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf8') as f:
    f.write(f'\n{stamp} | Stage 1 A018/B04. Read protocol, board and B04 acceptance contract; lead notes absent. Reconstructed arbitrary-branch row ledger and elementary posterior payment. Distinguished common-spectrum posterior cancellation from full Walsh-row cancellation; a=2 signed bent literal witnesses positive coherent entropy. Replayed even-m bent one-point splices: B_W/I_W>=m-1. Frozen <=60-second pilot passed 31,794 exact assertions in {check["elapsed_seconds"]:.3f}s on 1,082 exhaustive block cases, 276 literal phases and six bent splices. No independent review, mirror receipt or full-FEI solution claimed. Persisted run handoff.\n')
(AGENT/'LEARNED.md').write_text('''# Durable A018 facts (stage 1)

All entropy is in bits. For F(b,y)=g_b(y), fresh uniform a-bit selector b, arbitrary overlapping Boolean branches on common data, c_T(b)=hat(g_b)(T), R_T=E_b c_T^2, r_T(b)=c_T(b)^2/(2^a R_T), nu_T(A)=hat(F)(A,T)^2/R_T. Omit only R_T=0; include empty data T when present.

Delta_W H=B_W+M_W, B_W=sum R_T H(nu_T)=H(S_W|S_data), M_W=a-sum R_T H(r_T). I_W=sum R_T E_nu |A| and I_data=average branch influence. M_W is a mutual information in the auxiliary branch/data-label law and satisfies 0<=M_W<=(2/ln2) I_W by two-point/product entropy tensorization. Do not spend it again or drop B_W.

M_W=0 exactly when all branch squared spectra coincide. B_W=0 exactly when every nonzero coefficient row c_T(b) is one scalar Walsh character. B_W=0 forces M_W=0, so whole increment zero has precisely this row-character criterion. Common spectra imply whole cancellation for a<=1 only; for a>=2 sign phases can add entropy. Identical branches have M=B=I_W=0.

Common-spectrum branches c_T=alpha_T h_T(b), h_T Boolean, have B_W=sum alpha_T^2 H(h_T), I_W=sum alpha_T^2 I(h_T), and M_W=0. Example F=(-1)^(b1*b2)y has M=0, B=2, I_W=1. General F=h(b)y embeds arbitrary FEI into the sign-phase remainder (source guard X005). Avoid calling common spectra an easy terminal.

Bent source b on even m>=2 data bits and b'=b-2*1_{y=0}, selected by one fresh bit, has I_W=delta=2^-m. Every parent fiber has masses (c_T-delta)^2 and delta^2, c_T=+/-sqrt(delta). R_T/delta^2>=1/(2delta), hence B_W>=delta(m-1). No universal selector-only bound on B or Delta H can hold. This is an inherited intermediate no-go, not FEI disproof.

For a finite physical block stopping tree, entropy telescopes into weighted B_W+M_W plus leaf H, and influence decomposes into weighted queried I_W plus leaf I. The M_W sum is paid at 2/ln2 by the queried budget without reuse. B_W and arbitrary terminal entropy remain unpaid. C018/C019 are the universal bridge; a class-level posterior improvement alone is insufficient.

Exact checker v1: 31,794 assertions; 1,082 all-table block cases n<=3, 276 signed literal controls a<=3, six bent splices m<=12; 7.109s. Entropy equalities use exact rational prime-log vectors; inequalities use outward rational atanh-series bounds with sign-aware division. Direct character sums and physical edges independently cross-check the fast transform and spectral influence. Author checks are not independent-agent acceptance. Source-complete run is runs/20261011T221538Z-fleet05-A018-shared-data-collision-law.

Next mechanism: A019 can test common-spectrum quadratic selector phases (including nonlinear input translations of arbitrary shared data), paying B via actual selector phase influence. A017 already treated quadratic addressing; do not repeat that census or use oblique influence. This is a proposed next test, not a new proved class in this stage. B04 lead notes were absent; baseline identity and positive-energy closure are already proved. Retire this baseline after review unless a specific correction arrives.
''',encoding='utf8')

receipts=[]
for path in sorted(ROOT.rglob('*')):
    if path.is_file() and path.name!='PERSISTENCE_RECEIPTS.json':
        b=path.read_bytes(); assert len(b)<20*1024*1024
        if path.suffix=='.json': json.loads(b.decode('utf-8-sig'))
        receipts.append({'path':str(path.relative_to(ROOT)),'bytes':len(b),'sha256':digest(b),'readback':'OK'})
for name in ('STATUS.md','WORKLOG.md','LEARNED.md'):
    path=AGENT/name; b=path.read_bytes(); receipts.append({'path':str(path),'bytes':len(b),'sha256':digest(b),'readback':'OK'})
assert len((AGENT/'STATUS.md').read_text(encoding='utf8').splitlines())==2
assert json.loads((ROOT/'PROGRESS.json').read_text())==json.loads((ROOT/'PACKET_DELTA.json').read_text())
save('out/PERSISTENCE_RECEIPTS.json',{'recorded_at_utc':stamp,'schema_validation':'PASS: exact claim/progress fields from protocol, stripping the prose parenthetical from packet_ids; packet delta equals progress; all JSON parse; STATUS two lines; all files <20MB','artifacts':receipts,'local_persistence':'VERIFIED_READBACK','independent_acceptance':False,'mirror_verified':False,'supervisor_copy_claimed':False})
print(json.dumps({'status':'PERSISTED','artifact_count':len(receipts),'schema':'PASS','full_fei':'OPEN'},indent=2))
