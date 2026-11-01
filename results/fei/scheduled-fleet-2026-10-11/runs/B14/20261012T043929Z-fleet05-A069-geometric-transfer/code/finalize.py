from pathlib import Path
import hashlib,json

RUN=Path(__file__).resolve().parents[1]
AGENT=RUN.parents[1]
ROOT=Path('~/brain_workers/FEI100_20261011')
PROTOCOL=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
OLD=RUN.parent/'20261011T224507Z-fleet05-A069-geometric-transfer'
REVIEW=ROOT/'agents/A070/runs/20261011T230551Z-fleet05-A070-analytic-route-referee'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
p=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'))
result=json.loads((RUN/'out/CHECK.json').read_text())
assert result['result']=='PASS' and result['target_cases']==5338 and result['seconds']<60
old_claim=json.loads((OLD/'CLAIMS.json').read_text())[0]
review_progress=json.loads((REVIEW/'PROGRESS.json').read_text())
review_ref=next(c for c in review_progress['claim_versions_used'] if c['claim_id']==old_claim['claim_id'])
assert review_ref['original_statement_sha256']==old_claim['statement_sha256']
dependency={'claim_id':old_claim['claim_id'],'version':1,'statement_sha256':old_claim['statement_sha256'],'acceptance':'A070 independent ACCEPT_AT_STATED_SCOPE without repair','review_source':str(REVIEW/'REPORT.md'),'review_source_sha256':digest(REVIEW/'REPORT.md')}
write(RUN/'out/REVIEW_RECEIPT.json',dependency)

statement=(
    'For a-bit addressing A_a, a>=1, padded to N>=a+2^a, the fixed binary selector/data/padding '
    'hierarchy all-subset prefix code has Gamma_T(A_a)=3+2a+2R(a)+2*1{N>a+2^a}, '
    'where R(1)=0 and R(k)=1-2^{-k}+R(floor(k/2))+R(ceil(k/2)), and Gamma_T(A_a)<=8I(A_a)-5. '
    'Every Boolean truth-table edit f of density rho obeys '
    'H(f)<=Gamma_T(f)<=16I(f)-10+48N*rho-8rho. Thus N*rho<=1/8 gives <=16I(f), '
    'and every one-point edit gives <=25I(f), with <=16I(f) for N>=6. '
    'For any Boolean g on a split cube Z union Y with r=|Z|>=1 and |Y|>=1, join fixed binary '
    'singleton-leaf trees on Z,Y, put W_Z,W_Y for their internal-mask costs, and flip g on z=z*. '
    'Writing rho=2^{-r}, h=g(z*,.), m_h=Eh and U_Z=sum_v 2(1-2^{-|C_v|}), '
    'the exact difference-spectrum cost is E_delta=4rho[1+2(1-rho*m_h^2)+U_Z+E_{S_h}W_Y]. '
    'Partial restriction Parseval gives rho*E_{S_h}W_Y<=E_{S_g}W_Y, hence '
    'E_delta<=4E_{S_g}W_Y+4rho(2r+1) and '
    'Gamma_T(f)<=2Gamma_T(g)+8E_{S_g}W_Y+8rho(2r+1). '
    'Free-coordinate influences are unchanged, and I_Z(f)+I_Z(g)>=2r*rho.'
)
hyp=[
    'Actual Boolean signs on the uniform finite cube; entropy and code lengths in bits.',
    'I is total physical pivotal influence, equal to sum_S |S| fhat(S)^2.',
    'Trees and child coordinate order are fixed before the Fourier subset is sampled.',
    'L_T(S)=1+sum internal b_v*1{S meets C_v}; all masks and the root/empty bit are retained.',
    'Addressing family has distinct physical data coordinates, a>=1; arbitrary edits flip inherited values.',
    'Subcube energy identities require the tree root to separate nonempty Z,Y; h is retained without a universal core-cost assumption.',
    'No universal FEI or Gamma<=C I conclusion is asserted for arbitrary subcube edits.'
]
canonical=json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':'))
claim={
    'claim_id':'A069-ALIGNED-EDIT-ENERGY-ADDRESSING','version':1,
    'exact_statement':statement,'hypotheses':hyp,
    'statement_sha256':hashlib.sha256(canonical.encode()).hexdigest(),
    'contributors':['fleet05/A069'],
    'proof_source':{'path':str(RUN/'DERIVATION.md'),'sha256':digest(RUN/'DERIVATION.md'),'locators':'(A1)-(A4), (S1)-(S5)'},
    'proof_dependencies':[dependency],
    'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
    'supersedes':[],'refutes':[],'first_unproved_line':None,
    'next_consumers':['A070','A067','A068','A088','A094','B14','B20']
}
assert set(claim)==set(p['required_per_run']['claim_fields'])
write(RUN/'CLAIMS.json',[claim])
progress={
    'protocol_revision':p['revision'],'run_id':RUN.name,'stream':'B14','packet_id':'A069',
    'gap_id':'G-A069-STABLE-ENCODING','attempt_id':'A069-stage2-aligned-edit-energy',
    'method':'source-bound A070 review intake; all-set binary addressing code; exact subcube difference-spectrum factorization and restriction Parseval; integer Walsh and physical edge verification',
    'mathematical_delta':'C020: complete addressing-edit code <=16I at N*rho<=1/8 and <=25I for every padded one-point edit; exact retained-core subcube energy removes blind ambient-dimension charge; g2 Gamma=21/2 at N=10..12 with prior N9 certificate reused.',
    'deliverable_status':'COMPLETE_LOCAL_ARTIFACT; SUPERVISOR_COPY_AND_NEW_REVIEW_PENDING',
    'mathematical_status':'SCOPED_EXTENSION_AUTHOR_PROVED; PRIOR_A069_V1_INDEPENDENTLY_ACCEPTED_BY_A070; FULL_FEI_OPEN',
    'claim_versions_used':[dependency],
    'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
    'source_artifacts':['REPORT.md','DERIVATION.md','FROZEN_SPEC.json','code/check.py','out/CHECK.json','out/REUSED_CERTIFICATES.json','out/REVIEW_RECEIPT.json','out/SOURCE_MANIFEST.json'],
    'next_consumers':claim['next_consumers'],
    'next_action':'Derive exact signed cross-energy for two overlapping-control subcube edits in one complete reference, retaining both restricted-core costs and testing first-exposure ownership.',
    'stagnant_substantive_attempts':0,'blockers':[],'packet_ids':['A069']
}
assert set(progress)=={x.split(' (',1)[0] for x in p['required_per_run']['progress_fields']}
write(RUN/'PROGRESS.json',progress);write(RUN/'PACKET_DELTA.json',progress)

sources=[PROTOCOL,ROOT/'BOARD.md',ROOT/'claude/B14/STREAM_NOTES.md',OLD/'REPORT.md',OLD/'CLAIMS.json',OLD/'out/validation.json',OLD/'out/receipts.json',REVIEW/'REPORT.md',REVIEW/'PROGRESS.json',ROOT/'context/percolation_spectral_pivotal_entropy_30pp.txt',ROOT/'context/threshold_paper_38pp.txt']
write(RUN/'out/SOURCE_MANIFEST.json',[{'path':str(s),'bytes':s.stat().st_size,'sha256':digest(s)} for s in sources])
report=(RUN/'REPORT.md').read_text()
for k in p['required_per_run']['report_fields']:assert '## '+k in report
assert report.rstrip().split('\n')[-1].startswith('This stage moves C020')
write(RUN/'out/SCHEMA_CHECK.json',{'claim_fields':'PASS','progress_fields':'PASS (protocol parenthetical on packet_ids is annotation)','report_fields':'PASS','compatibility_copy':'IDENTICAL','statement_sha256':'PASS','parent_review_digest':'MATCH','target_cases':result['target_cases'],'exact_assertions':result['assertions']})

(AGENT/'STATUS.md').write_text('STATE: A069 stage 2 complete: addressing edit code <=16I/25I and exact retained-core subcube energy; 5,338 cases / 374,529 exact checks PASS; v1 accepted by A070; new review pending; FEI OPEN.\nNEXT: A088/A094 review; derive one-reference signed cross-energy for two overlapping-control subcube edits with first-exposure ownership and both terminal cores retained.\n',encoding='utf-8')
marker='2026-10-12 04:39 UTC stage 2:'
log=AGENT/'WORKLOG.md'
if marker not in log.read_text():
    with log.open('a',encoding='utf-8') as out:
        out.write(marker+' Read new board/B14 v2, consumed A070 independent acceptance of v1. Reused g2 N9/N10 certificates; new N11/N12 Gamma=21/2. Proved complete addressing-edit 16I/25I payment and exact single-subcube difference-spectrum/retained-core identity. Frozen 5,338 cases and 374,529 exact checks PASS in 0.571 s, 32 MB estimate. Universal separating-reference and influence cancellation remain open; new scoped review/mirror pending.\n')
learned=AGENT/'LEARNED.md'
fact='Stage 2 aligned subcube energy:'
if fact not in learned.read_text():
    with learned.open('a',encoding='utf-8') as out:
        out.write('Stage 2 addressing code: Gamma=3+2a+2R(a)+2*padding, R(1)=0, R(k)=1-2^{-k}+R(floor k/2)+R(ceil k/2); Gamma<=8I-5. Binary all-set code yields Gamma(edited)<=16I-10+48N*rho-8rho; hence 16I for N*rho<=1/8 and 25I for all one-point edits. This is a paid complete reference where pure influence-code cost/I=log2(a)+2+o(1).\n')
        out.write(fact+' For D={z=z*}, rho=2^{-r}, h=g_z*, E_delta=4rho[1+2(1-rho*(Eh)^2)+U_Z+E_h W_Y]. Partial Parseval averages W_Y over restrictions, so rho E_h W_Y<=E_g W_Y. Core term must not be discarded. Free influences unchanged; control influence sum for edited/base >=2r*rho. Universal Gamma/I transport is not implied, since cancellation can make the edited function constant.\n')
        out.write('A070 independently accepted A069-STABLE-HIERARCHY-EDIT-PAYMENT v1 without repair. g2 Gamma at N9=17/2 and at every padded N>9=21/2. Previously certified cases should be reused with hashes rather than rerun.\n')
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
files=sorted(s for s in RUN.rglob('*') if s.is_file() and s.name!='RECEIPTS.json')+[AGENT/s for s in ['STATUS.md','WORKLOG.md','LEARNED.md']]
for s in files:assert s.stat().st_size<20_000_000
write(RUN/'out/RECEIPTS.json',{'scope':'LOCAL_ONLY; supervisor copy, mirrors and new independent review pending','files':[{'path':str(s),'bytes':s.stat().st_size,'sha256':digest(s)} for s in files]})
print(json.dumps({'required_schema_checks':'PASS','new_cases':result['target_cases'],'exact_assertions':result['assertions'],'receipts_files':len(files),'receipts_sha256':digest(RUN/'out/RECEIPTS.json')},indent=2))
