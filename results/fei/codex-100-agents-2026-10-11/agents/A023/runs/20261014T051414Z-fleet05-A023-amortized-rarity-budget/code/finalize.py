"""Metadata/persistence only; no further Boolean search."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,copy
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1];TEAM=ROOT.parents[1]
PREV=ROOT/'runs/20261014T022245Z-fleet05-A023-amortized-rarity-budget'
SRC29=TEAM/'agents/A029/runs/20261014T025327Z-fleet05-A029-child-deficit-transport'
SRC25=TEAM/'agents/A025/runs/20261014T032227Z-fleet05-A025-rare-event-counterfamily'
PROTO=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def receipt(p):
    data=p.read_bytes();return {'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
protocol=read(PROTO);v=read(RUN/'out/validation.json');rate=read(RUN/'out/sharp_rate.json')
assert v['status']=='PASS' and v['cases']==10648 and v['checks']==106481
assert rate['cases']==10648 and rate['rational_upper']=='4' and rate['ties']==64
assert rate['exact_ratio_vector']=={'5':'-25/8','2':'33/2','3':'-27/8'}
rows=read(RUN/'out/results.json');assert len(rows)==10648
assert len((RUN/'out/rows.jsonl').read_text().splitlines())==10648
for row in rows:
    a,b=Q(1,1<<row['r']),Q(1,1<<row['s']);pi=[1-a,a*(1-b),a*b]
    assert [Q(x) for x in row['pi']]==pi
    assert Q(row['R_data'])==Q(row['R_star'])+Q(row['grouping_surcharge'])
    assert Q(row['grouping_surcharge'])==2*a*(1-a)*b*(1-b)*Q(row['I12'])
    assert Q(row['R_star'])<=2*Q(row['terminal_I']) and row['gap_sign']<=0
count=0
for name in ['sign_certificates.json','rate_certificates.json']:
    for item in read(RUN/'out'/name):
        count+=1
        if item.get('exact_zero'):assert item['sign']==0 and not item['vector']
        else:
            lo,hi=Q(item['lower']),Q(item['upper']);assert lo<=hi
            assert lo>0 if item['sign']==1 else hi<0
assert count==706
consumers=['A025','A029','A021','A027','A064','A087','A094','B05','B06','B20']
old=next(c for c in read(PREV/'CLAIMS.json') if c['claim_id'].startswith('A023-OVERLAP'))
claim=copy.deepcopy(old)
claim.update(version=4,proof_source=str(RUN/'PROOF.md'),review_records=[],
    status='EXACT_FINITE_CERTIFICATE_COMPLETE_PENDING_INDEPENDENT_REVIEW; PRIOR_SCOPES_PRESERVED',
    supersedes=[{'claim_id':old['claim_id'],'version':3}],next_consumers=consumers,
    proof_dependencies=[{'claim_id':old['claim_id'],'version':3,'source':str(PREV/'PROOF.md'),
        'status':'Whole-block additional scope independently accepted by A025/A029 at stated scopes; older bundled portions retain prior review status',
        'role':'Preserve previous scope and use reviewed constant-child activation corollary; new finite refund is direct exact certificate.'}])
claim['exact_statement'] += (
    ' Additional EXACT FINITE three-core refund theorem: g0,g1,g2 are labeled '
    'Boolean signs on the same two-bit uniform cube, A_r,B_s fresh point blocks, '
    'a=2^-r,b=2^-s, h=g1+B_s(g2-g1), f=g0+A_r(h-g0), '
    'pi=(1-a,a(1-b),ab), H_T=sum pi_j H(gj), I_T=sum pi_j I(gj). '
    'Let I_C=2r a[(1-b)P(g0!=g1)+bP(g0!=g2)]+2s abP(g1!=g2), '
    'R_star=2sum_{i<j}pi_i pi_j I(gi gj). For every ordered triple at r=s=1 '
    '(4096 cases), and every ordered pairwise-distinct nonconstant triple at '
    '(r,s)=(1,2),(2,1),(2,2) (6552 cases), H(f)-H_T<=4I_C+R_star, '
    'R_star<=2I_T, I(f)=I_C+I_T, and H(f)<=4I(f). '
    'The exact maximum (H-H_T-R_star)/I_C over the10632 positive-control cases '
    'is33/2-(25/8)log2(5)-(27/8)log2(3)<4, with64 ties. '
    'The16 zero-control cases satisfy the endpoint exactly. Fresh point '
    'activation of any nonconstant declared seed has H<6I and influence '
    '2^-t[I(f)+t(1-Ef)] tending to zero as t grows. '
    'No arbitrary-dimensional three-core refund, omitted widths/cores, '
    'localized odd-face bound or nested universal reserve is inferred.')
claim['hypotheses']=old['hypotheses']+[
    'The new refund subtheorem is restricted to exactly the10648 labeled two-bit shared-core/point-width cases listed; previous subtheorems retain their own distinct hypotheses.',
    'All terminal probabilities and entropies are physical and retained; exact prime-log/rational interval certificates constitute the finite proof.',
    'Fresh activation of finite seeds uses a separate independent point block; nonconstant seeds have positive influence.'
]
canon=json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':'))
claim['statement_sha256']=hashlib.sha256(canon.encode()).hexdigest()
save(RUN/'CLAIMS.json',[claim])
save(RUN/'out/REVIEW_A029.json',{'reviewer':'A023','source':str(SRC29/'DERIVATION.md'),
    'source_sha256':receipt(SRC29/'DERIVATION.md')['sha256'],
    'verdict':'HOLDS_NESTED_PHYSICAL_PARTITION_SIGNED_CONDITION_OWNER_AND_SURCHARGE_ALGEBRA',
    'scope':'All-dimensional two-block three-core formulas and exact grouping diagnostic only',
    'excluded':'General order-free refund, entire source computation acceptance and constant-chain grouping scope',
    'repair_supplied':False,'review_record':str(RUN/'REVIEW_A029.md')})
save(RUN/'out/CONSUMED_REVIEWS.json',{'claim_id':old['claim_id'],'version':3,
    'statement_sha256':old['statement_sha256'],
    'sources':[receipt(SRC25/'REVIEW_A023.md'),receipt(SRC29/'REVIEW_A023.md')],
    'scope':'A025 accepts entire v3 addition including class/activation; A029 accepts whole-block interface only; earlier bundled clauses not expanded'})
sources=[PROTO,TEAM/'BOARD.md',TEAM/'claude/B05/STREAM_NOTES.md',
    SRC25/'PROOF.md',SRC25/'CLAIMS.json',SRC25/'REVIEW_A023.md',
    SRC29/'DERIVATION.md',SRC29/'CLAIMS.json',SRC29/'REPORT.md',SRC29/'REVIEW_A023.md',
    PREV/'CLAIMS.json',PREV/'code/check_block.py']
save(RUN/'out/source_receipts.json',{'scope':'Read scope specified in REPORT; exact bytes, not blanket acceptance',
    'files':[receipt(p) for p in sources]})
artifacts=['REPORT.md','PROOF.md','REVIEW_A029.md','code/check_three.py','code/sharp_rate.py','code/finalize.py',
    'out/FROZEN_SPEC.json','out/POSTPROCESS_SPEC.json','out/rows.jsonl','out/results.json',
    'out/sign_certificates.json','out/rate_certificates.json','out/sharp_rate.json','out/validation.json',
    'out/REVIEW_A029.json','out/CONSUMED_REVIEWS.json','out/source_receipts.json']
progress=dict(protocol_revision=protocol['revision'],run_id=RUN.name,stream='B05',packet_id='A023',
    gap_id='G-R-MISMATCH-FIRST-REVELATION',attempt_id='A023-5-three-core-order-free-refund',
    method='Consume renewed-bank obstruction and nested reserve diagnostic; independent physical-algebra review; exact direct three-core entropy certificates and sharp saved-domain comparison',
    mathematical_delta='Nested owner/signed-condition/grouping algebra independently HOLDS. Actual three-core order-free reserve pays all10648 finite cases at control rate4; full H<=4I, exact maximum33/2-25log2(5)/8-27log2(3)/8<4 with64 ties. Primary106481 assertions and sharp10631 comparisons PASS. Arbitrary-dimensional refund not proved.',
    deliverable_status='COMPLETE_LOCAL_ARTIFACT',
    mathematical_status='DECLARED_FINITE_DOMAIN_EXACTLY_CLOSED; GENERAL_REFUND_OPEN; NEW_CERTIFICATE_REVIEW_PENDING; FULL_FEI_OPEN',
    claim_versions_used=claim['proof_dependencies'],claims_created_or_changed=[{'claim_id':claim['claim_id'],'version':4}],
    source_artifacts=artifacts,next_consumers=consumers,
    next_action='Derive actual coherent three-core excess for one balanced bent seed and two distinct vertex flips, as core dimension/point widths vary, preserving original pi weights and one R_star owner; prove refund or certify positive/growing deficit.',
    stagnant_substantive_attempts=0,
    blockers=['No analytic arbitrary-dimensional three-core order-free refund or universal terminal certificate.',
        'Actual entropy certificates do not imply general localized odd-face payment.',
        'New finite certificate awaits independent replay; remote adoption unverified.'],packet_ids=['A023'])
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected and set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
for heading in protocol['required_per_run']['report_fields']:assert '\n# '+heading+'\n' in '\n'+report
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
(ROOT/'STATUS.md').write_text(
    'STATE: A023 stage5 complete: one symmetric data reserve pays actual three-core entropy at rate4 on10648 declared cases; full H<=4I, sharp exact control ratio<4;106481 assertions and10631 comparisons PASS; general refund/FEI OPEN, independent review pending.\n'
    'NEXT: Test coherent three-core high contrast using one balanced bent seed and two distinct vertex flips, with original pi weights and a single R_star owner; A025/A029/A087/A094 replay finite certificate and sharp maximum.\n',encoding='utf-8')
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-14 05:14 UTC '+RUN.name+': Read new B05/A025/A029 results; unchanged nested coordinate renewal already refuted, three-core hierarchy identities already derived. Independently reconstructed physical/control owner formulas and signed sufficient condition (no repair). Tested actual order-free entropy rather than deleting source surcharges. Frozen10648 cases passed106481 assertions in38.5813392s. Separately frozen exact saved-vector maximum passed10631 comparisons in3.5333953s, maximum33/2-25log2(5)/8-27log2(3)/8<4,64 ties. All declared cases H<=4I with full terminals; fresh activation H<6I at vanishing influence. Extended existing claimv4; no arbitrary-dimensional refund inferred. Removed an unused discarded construction after successful run; evaluated correct truth tables/decisions unchanged. Saved all protocol/certificate/rolling artifacts locally.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-14 stage5: For nested point blocks and three shared cores, the actual source outer product includes inner-control influence I_B. Nested reserves are R_data=2a(1-a)[(1-b)I01+bI02]+2ab(1-b)I12 and R_control=2a(1-a)I_B. R_star=2sum pi_i pi_j Iij differs by grouping surcharge2a(1-a)b(1-b)I12 and has per-terminal owner2(1-pi_j), hence<=2I_T. Removing that surcharge analytically is still unsupported; however actual H-H_T<=4I_C+R_star is exactly certified on10648 declared two-bit-core cases, max ratio33/2-25log2(5)/8-27log2(3)/8<4 with64 ties. Repeated-core extremizers matter; wider domain used distinct nonconstant cores. Full H<=4I follows since every nonconstant two-bit core has H<=2I. This is a finite refund proof, NOT arbitrary-dimensional/nested localized payment. Three bent/edit cores with two distinct vertices are the next coherent high-contrast test. A025/A029 independently accepted the prior v3 whole-block scope, with their exclusions preserved.\n')
assert len((ROOT/'STATUS.md').read_text().splitlines())==2
files=[p for p in RUN.rglob('*') if p.is_file()];assert all(p.stat().st_size<20*1024*1024 for p in files)
save(RUN/'out/artifact_check.json',{'status':'PASS','cases':10648,'certificate_endpoints':706,
    'protocol_fields':'PASS','report_headings':'PASS','compatibility_copy_identical':True,
    'file_size_limit':'PASS','rolling_status_lines':2,'local_persistence':'SAVED',
    'remote_or_independent_new_review':'UNVERIFIED'})
save(RUN/'out/artifact_receipts.json',{'scope':'Local persistence only; no remote/adoption/review receipt',
    'files':[receipt(p) for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='artifact_receipts.json'],
    'rolling':[receipt(ROOT/p) for p in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
print(json.dumps({'status':'PASS','claim_version':4,'cases':10648,'schemas':'PASS','persistence':'SAVED','general_FEI':'OPEN'}))
