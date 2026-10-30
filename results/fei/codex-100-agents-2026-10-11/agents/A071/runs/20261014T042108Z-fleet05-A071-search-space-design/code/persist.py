import copy,hashlib,json
from datetime import datetime,timezone
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
BASE=Path('~/brain_workers/FEI100_20261011')
SOURCE=BASE/'agents/A075/runs/20261014T034311Z-fleet05-A075-search-to-theorem-bridge'
PROTO=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
source_claims=json.loads((SOURCE/'CLAIMS.json').read_text())
original=next(x for x in source_claims if x['claim_id']=='A075-MIXED-EXCURSION-OUTPUT-ENTROPY-BUDGET')
assert original['version']==1 and original['statement_sha256']=='329456072857a03fe4dfc64a015a86828e01fa2929c12c481e7b8d461f85c9de'
assert hashlib.sha256(original['exact_statement'].encode()).hexdigest()==original['statement_sha256']
review=copy.deepcopy(original)
review['review_records'].append({'reviewer':'A071','decision':'ACCEPT_AT_STATED_SCOPE_WITHOUT_REPAIR',
 'independence':'Independent chain-rule information derivation of output potential; factorwise polynomial intervals instead of Bernstein bounds on all256 boxes; exact FWHT of all28 tagged two-bit-core compositions and all336 physical edges; independent existingg3 interval from own prior stage. No source code imported or executed.',
 'proof':str(ROOT/'PROOF_REVIEW.md'),'source_statement_hash_preserved':True,
 'certificates':['out/validation.json','out/boxes_partial.json','out/physical_partial.json'],
 'scope_boundary':'Accepts original64 statement only. Separate contributed48 corollary remains independently unreviewed. Prior one-flip target supplied by A071 is acknowledged; no repair of this source version supplied.'})
review['status']='INDEPENDENTLY_ACCEPTED_AT_UNCHANGED_SCOPE_A071_LOCAL_RECORD'
new_id='A071-MIXED-EXCURSION-PRICE48-REFINEMENT'
statement=('For every nonconstant actual Boolean starting core on a finite independent uniform physical cube, '
 'and every finite legal word in the exact gate/policy scope of A075-MIXED-EXCURSION-OUTPUT-ENTROPY-BUDGET@1, '
 'the absolute variation of R=H/I is at most48(Psi_start-Psi_end)<=48, where Psi=h2(p_min)/I. '
 'If p_min(start)<=1/16 the budget is at most33. The full arbitrary starting R is retained. '
 'On the existing actual core g0=h,g1=h(g0^6),g2=h((-g1)^6),g3=h(g2^6), '
 'R(g3)+48Psi(g3)<10, hence every finite legal mixed descendant has H/I<10. '
 'Here h is negative exactly on {0,1,2,4,8,16,32,6,17,40}; common steps choose minority input '
 'when minority<=7/32 and its complement otherwise, and one-flip J_j=-h(x xor(1<<j)) steps are permitted only '
 'when minority<=1/16; outputs are reoriented to minority-negative. '
 'All substitutions use six identical disjoint physical copies. Entropy is in bits. '
 'No absolute bound on unknown starting cores, nonnegative erasure-reserve theorem, or physical restriction-tree payment follows.')
new={'claim_id':new_id,'version':1,'exact_statement':statement,
 'hypotheses':['Actual arbitrary finite uniform Boolean nonconstant starting core; entropy bits',
  'Exactly the source-named common/oneflip policy and its bias domains; arbitrary finite admissible word',
  'Identical independent copies on disjoint supports; no overlap or extra gates/sign patterns',
  'All six unequal J pivotal probabilities retained; oneflip locations matched by actual gate automorphisms',
  'Scope-preserving quantitative refinement; independent acceptance of this48 version pending'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),
 'contributors':['A075 (original output-entropy potential/payment mechanism)','A071 (independent price audit and scope-preserving quantitative refinement)'],
 'proof_source':str(ROOT/'PROOF_REVIEW.md'),
 'proof_dependencies':['A075-MIXED-EXCURSION-OUTPUT-ENTROPY-BUDGET@1 chain independently reconstructed and accepted unchanged here; source finite-word mechanism and scope retained',
  'Own stage4 actualg3 state reconstructed from Boolean seed; ordinary entropy/Fourier/edge identities',
  'Exact256-box factorwise certificate and analytic endpoint prices14,40,48 in PROOF_REVIEW.md'],
 'review_records':[],'status':'AUTHOR_PROVED_SCOPE_PRESERVING_QUANTITATIVE_REFINEMENT_REVIEW_PENDING_FEI_OPEN',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A075','A072','A074','A080','A084','A089','A092','B15','B20']}
dump(ROOT/'CLAIMS.json',[review,new])
validation=json.loads((ROOT/'out/validation.json').read_text())
refinement=json.loads((ROOT/'out/refinement48.json').read_text())
assert validation['compact_boxes']==256 and validation['physical_cases']==28
assert validation['physical_coefficient_checks']==114688 and validation['all_coordinate_edge_checks']==336
assert Q(refinement['compact_price_max'])<20<48
assert Q(refinement['g3_R_plus48Psi'][1])<10
sources=[PROTO,BASE/'BOARD.md',BASE/'claude/B15/STREAM_NOTES.md',SOURCE/'REPORT.md',SOURCE/'PROOF.md',SOURCE/'CLAIMS.json',
 SOURCE/'code/check_potential.py',SOURCE/'code/finalize.py',SOURCE/'out/COMPACT_PAYMENT_CERTIFICATE.json',
 BASE/'agents/A072/runs/20261014T020611Z-fleet05-A072-exact-walsh-engine/REPORT.md',
 AGENT/'runs/20261014T013355Z-fleet05-A071-search-space-design/out/core_partial.json',
 AGENT/'runs/20261014T013355Z-fleet05-A071-search-space-design/PROOF.md']
dump(ROOT/'out/source_manifest.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
protocol=json.loads(PROTO.read_text(encoding='utf-8-sig'))
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B15','packet_id':'A071',
 'gap_id':'B15-ARBITRARY-CORE-BIASED-ADMISSION','attempt_id':'A071-stage5-output-potential-review',
 'method':'Consume newly closed escape/repeated-word mechanisms; independently review A075 via chain-rule information, factorwise256-box certificate, all nonconstant two-bit core compositions, endpoint proofs and actual retainedg3 state; tighten existing scope price to48.',
 'mathematical_delta':'A075 original64 all-word theorem independently accepted unchanged. Scope-preserving48 corollary gives rare budget33 and existing high-E seed entire legal mixed orbit H/I<10. Arbitrary starting terminal H remains unpaid.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS_AND_SOURCE_REVIEW; new quantitative corollary independent review pending',
 'mathematical_status':'SOURCE64_HOLDS_AT_SCOPE; PRICE48_COROLLARY_AUTHOR_PROVED; UNKNOWN_STARTING_CORE_AND_FEI_OPEN',
 'claim_versions_used':['A075-MIXED-EXCURSION-OUTPUT-ENTROPY-BUDGET@1 hash329456072857a03fe4dfc64a015a86828e01fa2929c12c481e7b8d461f85c9de accepted unchanged by A071 local review',
  'A072 stage4 escape-pricing REPORT consumed for dispatch; not an unreviewed premise',
  'A071 stage4 actual g3 core certificate and independently proved composition law'],
 'claims_created_or_changed':['A075-MIXED-EXCURSION-OUTPUT-ENTROPY-BUDGET@1 local independent review only',new_id+'@1'],
 'source_artifacts':[str(p) for p in sources]+[str(ROOT/'out/validation.json'),str(ROOT/'out/refinement48.json')],
 'next_consumers':['A075','A072','A074','A080','A084','A089','A092','B15','B20'],
 'next_action':'State one actual signed-row transfer paying an exclusively owned certified portion of arbitrary rare-core terminal H from I-h2(p), with original child weights retained; test non-flat{0,1,2} and existingg3. A074/A092 audit price48 endpoint and factorwise compact coverage; no raw sign/depth search.',
 'stagnant_substantive_attempts':0,'blockers':[],'packet_ids':['A071']}
dump(ROOT/'PROGRESS.json',progress);dump(ROOT/'PACKET_DELTA.json',progress)
now=datetime.now(timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A071 stage5: A075 all-word64 theorem independently HOLDS unchanged; scope-preserving price48, rare budget33 and existingg3 all-word H/I<10 proved; corollary review pending; FEI OPEN.\nNEXT: A075/A089 source one actual signed-row/child-surplus transfer paying retained rare-core H from I-h2(p), no reuse; A074/A092 review48 endpoint and256 factorwise boxes; no sign/depth growth.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n'+now+' | Stage20261014T042108Z: read updated board/lead/status; A072 escape bill and A075 arbitrary-word bill superseded stale NEXT. Independently accepted A075@1 unchanged. Exact family28 tagged12-bit compositions,114688 Fourier coefficients,336 edges;6 rare non-flat controls and256 compact factorwise boxes;120496 checks PASS in2.319s, pilot16896/0.303s. Refinement3726 checks PASS in0.0052s, proves price48 (rare33), fixedg3 all-wordH/I<10 via9.9481922336 exact enclosure. Original64 acceptance separated from contributed48 corollary review pending. Full starting H remains unpaid; no new sign/depth circuit search or universalFEI claim. Run '+str(ROOT)+'.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n'+now+' | A075 all-word output-entropy payment independently reconstructed: D=Qh2(p)-h2(pout)>=0, DeltaPsi=D/(QI), Delta(H/I)=C/(QI), C=H_p(gate)-Qh2(4p(1-p)); retained core H never drops. Same scope supports48 rather than64: h rare price<14,J rare positive<40/negative<48, compact256 factorwise boxes max19.41842714<20. Thus arbitrary finite legal common/oneflip words have absoluteH/I variation<=48DeltaPsi; rare budget<=33. Existingg3 R+48Psi=9.9481922336<10, so all legal descendantsH/I<10. Source64 claim accepted unchanged;48 quantitativecorollary independent review pending. Exact root surplus I-h2(p)=H(X|g(X))-sum_i H(X_i|g(X),X_-i), conditional physical dependence; its positivity alone pays no Fourier entropy. A bound H<=K(I-h2(p)) on rare cores remains FEI-equivalent up toconstants. Do not restart closed fixed-seed growth.\n')
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
for claim in (review,new):assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
for key in ('claim_id','version','exact_statement','hypotheses','statement_sha256','contributors'):assert review[key]==original[key]
report=(ROOT/'REPORT.md').read_text()
for field in protocol['required_per_run']['report_fields']:assert '\n## '+field+'\n' in report
assert report.rsplit('\n## ',1)[-1].startswith('Universal bridge\n')
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
dump(ROOT/'out/schema_validation.json',{'protocol_fields_exact':True,'report_fields_present':True,'progress_delta_identical':True,
 'source_statement_version_hash_contributors_preserved':True,'new_statement_hash_valid':hashlib.sha256(statement.encode()).hexdigest()==new['statement_sha256'],
 'compact_boxes':256,'physical_coefficients':114688,'price48_checked':True,'g3_all_word10_checked':True,'full_FEI':'OPEN'})
receipts=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and p.name!='receipts.json':
  assert p.stat().st_size<20_000_000
  receipts.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(ROOT/'out/receipts.json',{'saved_at_utc':now,'files':receipts,'A075_source64_review':'ACCEPT_AT_STATED_SCOPE_A071_LOCAL',
 'price48_independent_review':'PENDING','supervisor_copy':'PENDING','mirror_verification':'PENDING','downstream_adoption':'PENDING'})
print(json.dumps({'run':str(ROOT),'files':len(receipts)+1,'schema':'PASS','source64_review':'HOLDS_UNCHANGED',
 'price48':'AUTHOR_PROVED_REVIEW_PENDING','full_FEI':'OPEN'}))
