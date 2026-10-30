"""Run two frozen scalar fixtures, then persist and re-read stage20 records."""
import hashlib,json,runpy
from pathlib import Path
R=Path(__file__).resolve().parents[1];A=R.parent.parent;O=R/'out'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_bytes((json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
main=read(O/'certificate.json');assert main['status']=='PASS' and main['query_rows']==14
assert main['actual_entropy_rate_checks']['K']['passes']
assert sha(R/'code/check.py')==read(O/'spec.json')['helper_sha256']
runpy.run_path(str(R/'code/scalar_certificate.py'),run_name='__main__')
runpy.run_path(str(R/'code/overlap.py'),run_name='__main__')
assert read(O/'scalar_certificate.json')['status']==read(O/'overlap_counterexample.json')['status']=='PASS'
proto_path=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
proto=read(proto_path)
previous=A/'runs/20261023T053924Z-fleet03-A017-recursive-addressing'
source=A/'runs/20261021T213328Z-fleet03-A017-recursive-addressing/out/boolean_counterexample.json'
(O/'source_b.json').write_bytes(source.read_bytes())
(R/'INHERITED_STAGE19_PROOF.md').write_bytes((previous/'PROOF.md').read_bytes())
save(O/'source_receipts.json',[{'path':str(p),'sha256':sha(p)} for p in [source,previous/'PROOF.md',proto_path,
 Path('BOARD.md'),
 Path('claude/B04/STREAM_NOTES.md')]])
consumers=['A018','A019','A020','A024','A030','A090','A091','B04','C019']
statement=('Prior conclusions of A017-FOUR-EDGE-COMPATIBILITY@3 remain at their stated scopes. '
 'For arbitrary Boolean b,c on disjoint original physical supports, selected i in b, '
 'p=Inf_i(b),e=I(D_i b), Delta_i(bc)=Delta_i(b),B_i(bc)=B_i(b),Inf_i(bc)=p '
 'and I(D_i(bc))=e+p I(c). For the SAME fresh shared gate A_h=1 on p0=0 '
 'and (-1)^z h on p0=1, Delta_i(A_(bc))=Delta_i(b)/2, '
 'B_i(A_(bc))=B_i(b)/2,Inf_i(A_(bc))=p/2, '
 '2I(D_i(A_(bc)))=e+p I(c)+3p/2. The saved six-bit b has '
 'p=1/8,e=5/16,H=21/4,I=9/4,B_i>4p, but '
 'delta=Delta_i(b)=-11/4+(25/32)log2(5)+(9/8)log2(3)<(4+2/ln(2))/8. '
 'For every t>=1 and every adaptive stopped prefix querying each prescribed selected factor '
 'bit at most once in A_(b^tensor(t)), actual entropy debit equals delta*E N/2 '
 'and queried original influence equals E N/16, so the SAME K pays all prefixes with '
 'both full terminals retained. Every complete adaptive permutation has bad-filtered '
 'raw boundary bill (35t^2+29t)/128, versus original influence 1+9t/8; '
 'the spectator-subtracted bill is t/2. The raw-bill ratio diverges, not H/I. '
 'Disjoint support is essential: b=(-1)^(i*x),c=(-1)^x gives Delta_i(bc)=2, '
 'I(D_i(bc))=1/4,p=1/2,I(c)=1, refuting unconditional subtraction under overlap.')
deps=[{'claim_id':'A017-FOUR-EDGE-COMPATIBILITY','version':3,'status':'AUTHOR_CHECKED_PENDING_INDEPENDENT_REVIEW',
 'used_for':'Prior conclusions and exact stage19 residual-core target; new formulas proved independently in this stage.'},
 {'claim_id':'A017-FOUR-EDGE-COMPATIBILITY','version':1,'status':'ACTUAL_BOOLEAN_FIXTURE_REVERIFIED_THIS_STAGE',
 'used_for':'Source six-bit truth table only; all entropy, influence and derivative facts used here rechecked.'}]
claim=dict(claim_id='A017-FOUR-EDGE-COMPATIBILITY',version=4,exact_statement=statement,
 hypotheses=['Uniform physical cube, Boolean signs, entropy in bits; real derivative influence is full Fourier energy.',
 'Spectator cancellation requires actual disjoint physical supports, not inferred spectral independence.',
 'Shared gate p0,z remains fresh/unqueried throughout core-only histories and its physical influence is kept once.',
 'Adaptive permutation observes previously queried selected bits only; stopped-prefix theorem retains every full terminal.',
 'No claim that all adaptive policies fail, that H/I diverges, or that arbitrary overlapping residual cores are paid.'],
 statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),contributors=['A017'],
 proof_source=['PROOF.md','code/check.py','code/scalar_certificate.py','code/overlap.py','out/certificate.json','out/source_b.json'],
 proof_dependencies=deps,review_records=[],status='AUTHOR_CHECKED_PROOF_AND_EXACT_CERTIFICATES_PENDING_REVIEW',
 supersedes=['A017-FOUR-EDGE-COMPATIBILITY@3'],refutes=[],first_unproved_line=None,next_consumers=consumers)
next_action=('Price the actual noncharacter overlap correction after a paid residual-core query from ONLY unused original influence, '
 'retaining signed physical-edge correlations, prior debits and BOTH full terminals. Compare A024 overlap credit; '
 'A090/A091 review all-width adaptive-permutation proof and the false-overlap witness.')
progress=dict(protocol_revision=proto['revision'],run_id=R.name,stream='B04',packet_id='A017',
 gap_id='C019-LOCALIZED-BAD-NODE-BOUNDARY-OWNERSHIP',attempt_id='A017-stage20-spectator-subtraction-and-real-core-payment',
 method='Exact disjoint-context derivative tensor identity, shared-gate Fourier expansion, actual entropy debit versus bad-filtered boundary bill, all-width adaptive-permutation expectation proof, physical-overlap falsifier.',
mathematical_delta='Paid arbitrary stopped prefixes of the actual tensor residual core at SAME K from queried influence only. Raw B-bad boundary bill grows quadratically, exact spectator subtraction is linear, and the coupled actual-Delta bad predicate has zero charge here. Refuted overlap extension on two physical bits; recorded signed edge correction.',
 deliverable_status='LOCAL_COMPLETE_REVIEW_AND_SUPERVISOR_TRANSFER_PENDING',mathematical_status='RESTRICTED_HISTORY_PAYMENT_AND_PROXY_OBSTRUCTION;FULL_FEI_OPEN',
 claim_versions_used=[{'claim_id':d['claim_id'],'version':d['version']} for d in deps],
 claims_created_or_changed=[{'claim_id':claim['claim_id'],'version':4}],
 source_artifacts=['REPORT.md','PROOF.md','CLAIMS.json','code/','out/'],next_consumers=consumers,next_action=next_action,
 stagnant_substantive_attempts=0,blockers=['Independent reconstruction of new proof and inherited chain pending.',
 'Noncharacter shared-physical overlap refund and universal core/terminal selection remain unproved.',
 'Supervisor adoption and remote-copy verification pending; full FEI OPEN.'],packet_ids=['A017'])
assert set(claim)==set(proto['required_per_run']['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in proto['required_per_run']['progress_fields']}
save(R/'CLAIMS.json',[claim]);save(R/'PROGRESS.json',progress)
(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
sections=[
'''Author-checked all-width result, independent review pending. In arbitrary disjoint Boolean physical context, identify and remove the spectator contribution to the selected derivative boundary. The correction survives one shared tagged-half gate with the SAME original labels. For the actual six-bit bad-query fixture, every adaptive stopped prefix of prescribed selected factor queries is paid at K=4+2/ln(2), using ONLY actual queried influence and retaining all full terminals. All t>=1 are proved analytically. The raw bad-filtered boundary proxy diverges relative to total influence for complete selected-factor adaptive permutations; the actual entropy/influence ratio does not. Full FEI is OPEN.''',
'''Read current BOARD.md including B04/A017-A020 and cross-route overlap/referee status; B04 STREAM_NOTES v2; own STATUS/LEARNED; stage19 proof; execution-protocol field/review/compute instructions. The saved six-bit truth table was read and reverified. The lead's universal boundary inequality is used only as existing context; the new identities and actual-rate proof are explicit in PROOF.md sections1-4. Prior threshold/percolation reading is inherited, not freshly claimed. Source receipts bind the consumed files. The exact-session brain wake completed with stale-source warnings; no affected owner/state/dream note was used as a mathematical premise. Current campaign deadline is the owner's2026-10-23 14:49 UTC.''',
'''PROOF.md is the full derivation. Disjoint b,c give I(D_i(bc))=e+pI(c) while selected entropy debit and erasure are independent of c. With one shared tagged-half gate, 2I(D_i A_(bc))=e+pI(c)+3p/2 and actual selected debit halves. The source b has genuinely bad B_i>4p, yet delta=-11/4+(25/32)log2(5)+(9/8)log2(3)<K/8. An independent integer certificate proves the strict margin via a degree16 positive Taylor lower bound for exp(8).

For any adaptive stopped selected-factor prefix, actual debit=delta E[N]/2 and spent influence=E[N]/16. Thus SAME K pays from the queried original coordinate, with no guard refund, spectator influence or terminal FEI allowance borrowed. For full adaptive permutations, conditional expectation gives raw bad-node boundary bill(35t^2+29t)/128 while I=1+9t/8. Removing the exact spectator term leaves t/2. Testing the coupled ACTUAL Delta>K*Inf predicate first leaves ZERO adverse boundary charge here, via the universally valid elementary refined telescope in PROOF.md. No universal coordinate selection is asserted. All tagged full terminals have influence1+17t/16 and entropy2+t(H(b)-delta)/2 on average.

The tempting overlap extension is FALSE already for b=(-1)^(i*x),c=(-1)^x. The actual debit is2, while the invalidly subtracted bound is below7/4. The correct edge-energy correction is the signed sum E[1_(c flips)*D(x)D(x^j)]. First unpaid universal line: price noncharacter shared-physical overlap and its entropy change from unused original influence, or select a valid physical factorization. No arbitrary-core or terminal FEI estimate is assumed.''',
f'''Frozen specifications precede checks: out/spec.json, scalar_spec.json and overlap_spec.json. Pilot:2 roots/2 actual query nodes,25 assertions,PASS in0.162 s. Full fixed domain:t=1,2,tag=0,1, all factor-query permutations and both full children at every reached node;4 distinct roots/14 actual query rows,{main['assertions']} assertions,PASS in{main['elapsed_seconds']:.3f} s. This is a deliberately small exact validation of an all-width proof, not an exhaustive Boolean census or an automated dimension increase. Integer Walsh spectra, exact Fraction influences and real derivative physical-edge energies are cross-checked. Base entropy is independently recomputed by direct character sums. All entropy signs use rational logarithm intervals or positive integer comparisons; floats only time the checks.

The separate scalar certificate cross-multiplies integers after bounding exp(8) below by its positive series through degree16. The two-bit overlap fixture verifies both full children, exact entropy2, influence1/2 and derivative energy1/4, including its signed edge correction. Commands: python -X utf8 code/check.py --freeze; --pilot; full without flags; then code/finish.py executes the two fixed scalar fixtures and persistence checks. Peak memory was not measured; estimates70 MB and20 MB, below the300 MB admission threshold. All mathematical jobs are bounded under60 s, no GPU, no detached job and no Lean certification. No claim of external-agent review follows from the two representations.''',
'''Version4 evolves the existing candidate rather than opening another broad unreviewed candidate. Version3 is retained for its earlier scoped results/residual target; version1 supplies only an actual truth table reverified here. The prior twelve-edit theorem is unchanged. New evidence narrows C019's payment problem: the crude proxy can repeatedly bill untouched factor influence even when exact physical entropy payment succeeds. The overlap counterexample refutes only the unproved extension of spectator subtraction to shared supports. It does not refute the disjoint identity, prior adaptive existential targets or FEI.''',
next_action+''' This targets the actual obstruction to extending the reusable primitive rather than another isolated finite-size class. Consumers include A018/A019/A020 for source ownership and A024 for physical overlap; no message was sent.''',
'''The four required protocol files, proof, scripts, frozen specifications and outputs are saved under A017; STATUS, WORKLOG and LEARNED are current. Every file is below20 MB. PACKET_DELTA equals PROGRESS byte-for-byte and has packet_ids=["A017"]. out/PERSISTENCE_RECEIPTS.json records byte sizes and SHA256; the persistence pass re-reads every bound file and exact schema. Remote transfer and independent acceptance have no receipt and remain supervisor/reviewer work. Brain self-care is degraded/unverified: owner-model98.4h, state-of-mind83.0h and latest dream33.7h stale at this wake; personalization from those notes is unverified. No process was stopped and no mathematical job was left running.'''
]
report='# A017 stage20: pay actual residual entropy, remove repeated spectator bills\n\n'
report+='\n\n'.join('## '+h+'\n\n'+s for h,s in zip(proto['required_per_run']['report_fields'],sections))
report+='''\n\n## Universal bridge

This stage moves C019 and C024 by paying actual residual-core queries through the SAME shared gate at unchanged K for every adaptive stopped selected-factor prefix, while retaining all full terminals and allocating only queried original influence. It quantifies why the raw bad-node proxy can be misleading: its bill is(35t^2+29t)/128, whereas exact spectator subtraction leaves t/2. The remaining universal bridge is a justified correction for overlapping physical cores or a policy selecting valid factorizations; the two-bit counterexample makes the first unsupported extension explicit. NEXT attacks that overlap liability using signed actual-edge correlations and the same unused source, rather than another class census. Full FEI remains OPEN.
'''
(R/'REPORT.md').write_bytes(report.encode('utf-8'))
(A/'STATUS.md').write_bytes(('STATE: A017 stage20 saved: actual tensor-core bad-query prefixes paid SAME K from queried influence; raw bad-filtered bill quadratic, exact spectator bill linear; overlap extension refuted on2 bits; FEI OPEN/review pending.\n'
 'NEXT: Price noncharacter physical-overlap entropy/edge correction from ONLY unused original influence, old debits/BOTH full terminals retained; A024 overlap credit and A090/A091 review v4.\n').encode('utf-8'))
marker='2026-10-23 stage20 (20261023T115918Z)'
note=('Disjoint b,c: selected Delta,B,Inf ignore c, but I(D_i(bc))=I(D_i b)+Inf_i(b)I(c). In shared gate A_(bc), actual debit and Inf halve;2I(D)=e+pI(c)+3p/2. Saved b has p1/8,e5/16, delta=-11/4+25log2(5)/32+9log2(3)/8<K/8 (independent exp8 integer certificate). ALL adaptive stopped selected-factor prefixes are paid SAME K from actual queried influence, full terminals retained. ALL complete adaptive permutations have raw bad-filtered bill(35t^2+29t)/128,I=1+9t/8; spectator-free bill t/2. Not a FEI disproof. Overlap cannot be assumed: b=(-1)^(ix),c=(-1)^x gives debit2 but false-refund bound<7/4. Correct energy shift is signed sum E[1_(c flips)D D_prime].')
for name in ['WORKLOG.md','LEARNED.md']:
    p=A/name;b=p.read_bytes() if p.exists() else b''
    if marker.encode('utf-8') not in b:p.write_bytes(b+('\n\n'+marker+': '+note+'\n').encode('utf-8'))
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
for h in proto['required_per_run']['report_fields']:assert '## '+h+'\n' in report
assert report.rsplit('## ',1)[1].startswith('Universal bridge\n')
files=[]
for p in sorted(R.rglob('*')):
    if not p.is_file() or p.name=='PERSISTENCE_RECEIPTS.json':continue
    assert p.stat().st_size<20*1024*1024
    if p.suffix=='.json':read(p)
    files.append({'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
receipt=dict(status='LOCAL_FILES_VALIDATED',review='PENDING',remote='SUPERVISOR_PENDING',full_fei='OPEN',files=files,
 rolling=[{'path':n,'sha256':sha(A/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']])
save(O/'PERSISTENCE_RECEIPTS.json',receipt)
for item in read(O/'PERSISTENCE_RECEIPTS.json')['files']:
    p=R/item['path'];assert p.stat().st_size==item['bytes'] and sha(p)==item['sha256']
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
print(json.dumps({'status':'LOCAL_FILES_VALIDATED','files':len(files),'full_fei':'OPEN','review':'PENDING'}))
