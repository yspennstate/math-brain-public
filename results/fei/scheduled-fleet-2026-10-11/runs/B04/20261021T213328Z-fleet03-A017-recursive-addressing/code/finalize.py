"""Write and validate the stage's protocol package; never writes outside A017."""
from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]
A=R.parents[1]
OLD=A/'runs/20261014T102650Z-fleet05-A017-recursive-addressing'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def save(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
protocol=read(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
for f in ['reconstruction.json','critical12_certificate.json','distance_bitset.json','quadratic_distance.json']:
    assert read(R/'out'/f)['status']=='PASS'
pos=read(R/'out/position_certificate.json')
assert pos['scalar_cases']==pos['spike_partition_cases']==78125
assert all(pos['by_intrusions'][str(k)]['bad_sets']==0 for k in range(7))
assert pos['by_intrusions']['7']['bad_partitions']==168
assert 17**170*5**80<2**896 and 17**136*5**120>2**832
assert read(R/'out/critical12_certificate.json')['actual_twelve_edit_parents']==4096
wit=read(R/'out/boolean_counterexample.json')
assert wit['status']=='ACTUAL_BOOLEAN_LOCAL_COUNTEREXAMPLE'
assert wit['influences']==['1/8','5/16','5/16','1/2','1/2','1/2']
wit.update({'spectral_entropy_bits':'21/4','total_influence':'9/4','H_over_I':'7/3','independent_data_y_total_influence':'13/4'})
save(R/'out/boolean_counterexample.json',wit)
statement=('On the uniform six-dimensional Boolean cube, let a selected physical coordinate have four pivotal pairs whose five-dimensional child locations form an affine two-plane. '
 'If the child sign on this plane is bent, and zero through six of the other seven parallel slices are affine (the rest bent), then its spectral erasure satisfies B_i<=4 Inf_i=1/2. '
 'For seven affine slices this assertion fails: the saved actual Boolean truth table has B_i=(136 log2(17)+120 log2(5)-704)/256>1/2, H=21/4 and I=9/4, with a K4-good alternative physical coordinate. '
 'Its exact nearest quadratic distances are 12 without a polar constraint and 14 when the selected quadratic polar row is nonzero. '
 'For any quadratic phase on six physical controls edited at at most twelve vertices, a nonzero polar coordinate with four pivotal pairs is K4-good whenever the surviving pivotal child set is an affine two-plane. '
 'All affine-phase mask terminals with at most twelve edits on D>=6 controls retain the unchanged K=4+2/ln(2) payment. '
 'Consequently the inherited physical stopping policy extends at the same K through twelve coherent same-fiber edits conditional on every reached four-pair critical node having planar surviving pivotal set; the general affine-span-three critical case remains open.')
claim={
 'claim_id':'A017-FOUR-EDGE-COMPATIBILITY','version':1,'exact_statement':statement,
 'hypotheses':['Boolean signs on a uniform physical cube; entropy and erasure in bits; exact Fourier probabilities.',
 'Affine changes of unqueried coordinates are used solely to preserve the selected coordinate erasure and influence, never to transport another physical influence.',
 'The twelve-edit node lemma requires a nonzero selected quadratic polar row and an affine two-plane surviving pivotal set.',
 'The twelve-edit stopping consequence is conditional on planar critical nodes at every reached restriction and uses the complete inherited five-control, JS and terminal proofs.'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A017'],
 'proof_source':['PROOF.md','out/position_certificate.json','out/boolean_counterexample.json','out/quadratic_distance.json','out/distance_bitset.json','out/critical12_certificate.json','INHERITED_STAGE6_PROOF.md'],
 'proof_dependencies':[{'claim_id':'A017-TWO-EDIT-SHARED-ADDRESS-STOPPING','version':4,'status':'AUTHOR_CHECKED_PENDING_INDEPENDENT_REVIEW','used_scope':'affine-on-plane quinary certificate; generic five-control good query; odd five-edge certificate; JS and sparse-terminal inequalities'}],
 'review_records':[], 'status':'AUTHOR_CHECKED_PROOF_AND_EXACT_CERTIFICATES_PENDING_REVIEW',
 'supersedes':[],
 'refutes':[{'statement':'Every six-variable physical coordinate with four pivotal edges satisfies B_i<=4 Inf_i.','scope':'unproved stage6 frontier helper, even for affine-plane disagreement with bent phase and seven affine parallel slices','witness':'out/boolean_counterexample.json'}],
 'first_unproved_line':None,'next_consumers':['A018','A020','A030','A090','A091','B04']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save(R/'CLAIMS.json',[claim])
next_action='Pay or adaptively repair a six-control nonzero-polar twelve-edit node whose four surviving pivotal child vertices have affine span three, retaining the same full terminal/data budget; A091/A090 reconstruct the planar reduction and A018/A020 the row certificate.'
oldp=read(OLD/'PROGRESS.json')
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B04','packet_id':'A017',
 'gap_id':oldp['gap_id'],'attempt_id':'A017-stage17-position-coupled-four-edge-repair',
 'method':'Exact scalar-row envelopes, location-coupled affine-spike partitions, actual Boolean counterexample, independent distance reconstruction, twelve-edit pivotal-edge rigidity.',
 'mathematical_delta':'Closed mixed affine intrusions k=0..6; refuted generic four-edge K4 with an actual seven-intrusion Boolean parent; proved selected-polar distance14; paid every twelve-edit planar four-edge critical node and all <=12 affine terminals at the same K. Only affine-span-three critical geometry remains for this twelve-edit route.',
 'deliverable_status':'LOCAL_COMPLETE_REVIEW_AND_SUPERVISOR_TRANSFER_PENDING',
 'mathematical_status':'RESTRICTED_PROOF_AND_EXACT_LOCAL_REFUTATION;FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A017-TWO-EDIT-SHARED-ADDRESS-STOPPING','version':4}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['REPORT.md','PROOF.md','CLAIMS.json','INHERITED_STAGE6_PROOF.md','code/','out/'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,
 'stagnant_substantive_attempts':0,
 'blockers':['Independent proof review pending.','Full FEI and the affine-span-three twelve-edit node remain open.','Core Lean sign check returned RUNTIME_UNVERIFIED; no Lean certification.','Supervisor adoption and remote mirror verification are pending.'],
 'packet_ids':['A017']}
assert set(progress)=={f.split(' (')[0] for f in protocol['required_per_run']['progress_fields']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
report='''# A017: Boolean-compatible four-edge payment and a real local obstruction

## exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. This stage repairs the saved C019 four-edge bottleneck rather than redoing the recursive addressing baseline. For every six-control Boolean phase, quantify over a selected physical coordinate with four pivotal pairs. For affine-plane child disagreement with bent restricted phase, prove B_i<=4 Inf_i when at most six other parallel slices are affine; refute the unrestricted local helper with an actual Boolean parent. For a nonzero quadratic polar row with at most twelve coherent edits, prove this payment for every planar surviving pivotal set. Entropy is in bits; probabilities use the uniform cube. K=4+2/ln(2) is unchanged. The twelve-edit stopping consequence is explicitly conditional on planar critical nodes; it is not a full twelve-edit or full-FEI theorem.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full (fei-execution-protocol/2, 2026-10-11-execution-v2), the campaign README/current status, registry/packet/stream entries and B04 parts of the campaign TeX; supplemental CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and sources inventory. Read the live BOARD A017/B04 and relevant peer entries, and Claude B04 STREAM_NOTES v2 (11 October, 23:25 UTC). The current user endpoint, 23 October 14:49 UTC, supersedes the older campaign-file endpoint; no schedules were altered.

The substantive recovered checkpoint is stage6, runs/20261014T102650Z-fleet05-A017-recursive-addressing: PROOF.md, NEXT_DERIVATION.md and critical/quinary/ternary code. Later ten stage directories contain only .final markers; they supply no mathematical continuation. Stage6's v4 eleven-edit result remains the inherited pending candidate. Its proof and affine-phase-on-plane certificate are copied byte-for-byte locally. The two current papers and their earlier versions were read through focused source excerpts; exact hashes, locations and source encodings appear in out/paper_source_notes.json. Threshold Proposition 8.6 (75) is the shared-data baseline; Corollary 8.2 is the affine-selector baseline. No percolation geometric theorem is imported into a uniform-cube payment. The text files contain cp1252 bytes; an initial UTF-8 read failed, then an explicit decoding fallback preserved the source bytes. No paper was modified.

Math recall used three wordings once. Its results were generic pivotality and unrelated/earlier bent-splice notes; none is used as a proof premise. Wake warned of stale personal-context notes, which were disclosed and not relied upon.

## complete derivation or exact first unsupported line

PROOF.md supplies the derivation, side conditions and counterexample. Write each selected Fourier row as (A,1)/16, where A=Walsh(H)-1, H(0)=1. Every bent parallel slice gives four unit signs; every affine slice gives one signed two and three zeros. Then 256 B_i=sum Phi(A^2,1). The 192 one-intrusion scalar patterns have maxima yielding 10 Phi(16,1)+16 Phi(4,1)<128, certified by 17^170*5^80<2^896.

The general scalar count envelope covers 78125 profiles and pays intrusion counts 0,1,2,3,5,6. At four intrusions its scalar maxima require incompatible spike ownership. Retaining the exact affine-column set S and its ordered partition among the four spike owners closes that failure: another 78125 partitions pay every S with |S|<=6. All comparisons use integer entropy products and exact cross multiplication. No independence between rows or preservation of other physical influences is assumed.

At seven affine slices, compatible columns realize absent squares 4 in 24 rows and 16 in eight rows, with present square one in all 32 rows, denominator 256. Thus B_i=(136 log2(17)+120 log2(5)-704)/256>1/2, certified by 17^136*5^120>2^832. The actual truth table has influences (1/8,5/16,5/16,1/2,1/2,1/2), H=21/4 and I=9/4. Physical coordinate 3 instead satisfies B_3<=4 Inf_3; its five-control descendants retain the inherited good-coordinate policy and complete terminals. The witness refutes a local helper, not FEI. Its nearest quadratic distance is 12, or 14 with a nonzero selected polar row, independently certified two ways.

The useful twelve-edit implication is sharper than the generic helper. A nonzero quadratic polar row starts with 16 pivotal selected pairs. Four surviving pairs require R-A=12, while the edit count is R+A+2D<=12. Hence precisely twelve pairs are removed, none added or doubly edited. If the four survivors form a plane W, they lie in the original derivative hyperplane P. Four parallel W-slices outside P are untouched and bent whenever W is bent; W itself is bent. Only three slices can be affine, so the new certificate pays this node. The inherited affine-sign-on-W certificate pays the other phase type.

Affine-mask terminals with <=12 edits are paid at the same K: the remaining endpoint inequality reduces to 2 ln(2)+log2(3)<3, following from ln(2)<7/10 and 3^5<2^8. Actual denominators are positive, s=0 is handled separately, and multiplying by a character cannot reduce influence since each mask influence is <1/2. Higher-dimensional polar queries and <=5-dimensional queries retain their inherited payments. The first unsupported line is a paid query or adaptive repair when a six-control critical four-point surviving set has affine span THREE. No universal reserve or unconditional twelve-edit conclusion is claimed.

## executed validation with domain, arithmetic, commands and outputs

All scripts are under code/ and commands below use python -X utf8 code/<name> from this run directory. Each search had a saved frozen spec before execution. Pilots were <60 seconds; all searches were sequential, fixed-dimension and estimated 20-40 MB, with no GPU or detached work. Core Lean was estimated 100 MB. No job was expected to exceed 300 MB, so memok was not required. Actual peak RAM was not measured. The compute monitor reported ok; no other work was stopped.

- row_pilot.py: all 192 scalar patterns, 576 checks, 0.002 seconds; exact one-intrusion maximum certificate.
- envelope.py --pilot / envelope.py: 1000 / 78125 scalar profiles; full 2.902 seconds; exact count-only envelope and honest failed relaxations.
- position.py --pilot / position.py: 1000 pilot profiles; full 78125 profiles and 78125 spike partitions, 6.394 seconds. Zero bad sets for k=0..6; seven-intrusion relaxation has 168 bad partitions.
- boolean_witness.py: independent direct character sums, exact physical influences and local/repair product signs on one actual 64-value Boolean function, 0.001 seconds.
- reconstruct.py: 192 direct scalar cases, 512 actual parents and all 168 GL(3,2) z maps, 872 total cases / 3819 assertions, 0.839 seconds. Exact projected/actual ratio identities pass.
- quadratic_distance.py --pilot / quadratic_distance.py: 256 / 32768 quadratic parts; all linear terms and both constants minimized by exact Walsh correlation; full 2.751 seconds. Minima 12 and 14 with actual edit lists. Independent XOR/bit_count check: all 2097152 quadratic/linear pairs, same minima. That check ran inline; code/distance_bitset.py preserves the same independent calculation for reproduction.
- critical12.py --pilot / critical12.py: 32 / 4096 actual twelve-edit endpoint choices; full 32768 assertions, 1.102 seconds. Every selected erasure paid; at most three affine intrusions. Exact pair-count arithmetic has one feasible triple (12,0,0); terminal integer sign has slack 13.
- Core Lean was attempted on the named two-sign theorem A017_integer_signs, source SHA256 050bf9a478b72775f9d4dfac20ba2f615b952a7dd8dd0cd9c065738afbb2242c, reviewed source, timeout 30 seconds. Result: RUNTIME_UNVERIFIED after 32.7 seconds. This certifies no Lean theorem or axioms. The integer signs are checked separately by exact Python arithmetic. No mathematical sign uses a floating approximation.

The original source text-decoding failure and the count-only envelope failures are retained as disclosed limitations; neither is a Boolean counterexample. The seven-intrusion actual truth table meets every hypothesis of the explicitly refuted local helper. The eleven-edit theorem survives; the nearest twelve-edit representation has a zero selected polar row.

## proof dependencies and changed downstream conclusions

The inherited A017-TWO-EDIT-SHARED-ADDRESS-STOPPING@4 remains author-checked and independently unreviewed. Its quinary, generic five-control, odd five-edge, JS and sparse-terminal interfaces are used at their exact scopes. New A017-FOUR-EDGE-COMPATIBILITY@1 is one continuation/repair package, not another broad universal candidate. No acceptance by A090/A091 is asserted. The generic six-control every-coordinate K4 helper is now refuted by an actual Boolean witness; its proposed use must be replaced by the planar twelve-edit rigidity argument or an actual adaptive physical query. Earlier eleven-edit conclusions are unaffected. Affine coordinate changes preserve selected erasure only, so no transformed derivative budget is transferred back to physical axes.

## one next mathematical action and independent reviewer

Treat ONE actual twelve-edit nonzero-polar four-pair node with affine-span-three disagreement: either pay its exact row compatibility or choose a paid alternative physical coordinate while keeping all inherited terminal entropy and the same data owner. This is the remaining critical geometry after the planar payment, rather than another edit-count census. A091/A090 should independently reconstruct the planar rigidity and unchanged terminal constant; A018/A020 should reconstruct the position-coupled certificate. These are intended handoffs in the saved package; no messages or writes to other agents were made.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, PROOF.md, inherited source copies, frozen specifications, code and exact outputs are saved under the assigned A017 run. code/finalize.py checks protocol field sets, claim hash, output status/case counts, compatibility identity, copied source hashes, frozen helper hashes and every file's 20 MB limit, and writes out/PERSISTENCE_RECEIPTS.json. STATUS.md is exactly two lines; WORKLOG.md and LEARNED.md contain dated updates. There is no local save blocker. Independent review, supervisor adoption, GitHub copying and mirror verification remain pending. No git command, brain write, external message, trading access, detached job or other-agent mutation was used for research persistence.

## Universal bridge

This stage advances C019 stopping-tree payment and the C018 good-coordinate interface by proving Boolean-compatible mixed-column payments, producing an actual obstruction to the generic four-edge K4 shortcut, and replacing that shortcut with a twelve-edit planar rigidity theorem plus a complete terminal payment at the unchanged K=4+2/ln(2). Every paid query retains the original physical/data owner, and full terminal entropy is kept. The twelve-edit extension now lacks only the affine-span-three critical-node payment or adaptive repair; full FEI still requires a count-independent physical selection/reserve theorem. NEXT targets that remaining geometry because it can produce a reusable Boolean compatibility or alternate-query mechanism, while another unrestricted local bound is already false.
'''
write(R/'REPORT.md',report)
for field in protocol['required_per_run']['report_fields']:
    assert '## '+field in report
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
write(A/'STATUS.md','STATE: A017 stage17 saved: mixed-slice k<=6 paid; actual seven-intrusion K4 counterexample; twelve-edit planar polar nodes/full terminals paid at same K; FEI OPEN, review pending.\nNEXT: A091/A090 review; pay or adaptively repair affine-span-three four-pair twelve-edit nodes using the same physical/data owner.\n')
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:
    f.write('\n'+now+' stage17 '+R.name+': recovered substantive stage6 after ten marker-only stages. Exact position-coupled rows pay k<=6; actual Boolean k7 has B>4Inf with H=21/4,I=9/4, alternate physical query paid. Nearest quadratic distances12/14 independently agree (32768 Walsh parts/2097152 bitset pairs). Pivotal-pair rigidity pays all twelve-edit planar critical nodes; unchanged-K affine terminals through12 proved. Row78125+partition78125, independent872/3819, canonical twelve-edit4096/32768 PASS. Core Lean RUNTIME_UNVERIFIED, not a certificate. Initial paper UTF8 decode repaired with explicit cp1252 source decoding. Full FEI and affine-span3 critical geometry remain open; review/supervisor transfer pending.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:
    f.write('''

Stage17 durable facts (2026-10-21, fleet03): For six-control four-pair affine-plane disagreement with bent phase, scalar row H0=1 has absent amplitude (Walsh H-1)/16 and present amplitude1/16. One affine intrusion costs at most [170log2(17)+80log2(5)-768]/256<1/2; 192 exact row patterns suffice. Count-only envelopes pay k=0,1,2,3,5,6. Retaining each affine-spike location across the four rows pays k=4 too: all78125 row profiles and78125 ordered spike partitions certify every k<=6. This avoids millions of parent truth tables without claiming row independence.

The seven-intrusion fully affine complement DOES admit an actual Boolean bad selected coordinate: absent-square histogram {4:24,16:8}, present squares1 in32 rows, denominator256; B=[136log2(17)+120log2(5)-704]/256>1/2=4Inf. Physical influences(1/8,5/16,5/16,1/2,1/2,1/2), H=21/4,I=9/4. Coordinate3 is paid. Nearest quadratic distance12 has selected polar row zero; nearest selected-polar distance14, independently exact. This refutes generic every-coordinate four-edge K4, not FEI or adaptive good-query existence.

Twelve-edit planar rigidity: a nonzero six-control quadratic polar row starts with16 pivotal pairs. Four survivors and <=12 edits force exactly12 removals,0 additions,0 doubled pairs. Surviving planar W lies in the derivative hyperplane P; four parallel W-slices outside P are untouched. If W has bent phase, those four plus W remain bent, so at most3 affine intrusions; if W is affine use prior quinary certificate. Hence every planar critical twelve-edit polar node is K4-good. Affine terminals<=12 pay unchanged K=4+2/ln2 because the endpoint reduces to2ln2+log2(3)<3, from ln2<.7 and3^5<2^8. The unconditional twelve-edit gap is now affine-span-three surviving pivotal sets. No count-independent reserve is proved. All normalizations preserve ONLY the selected physical B/Inf, not other physical influence budgets. Core Lean attempt was runtime-unverified; exact arithmetic/written proof pending independent review is the attained rung.
''')
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for src,dst in [('PROOF.md','INHERITED_STAGE6_PROOF.md'),('code/quinary.py','code/inherited_quinary.py'),('out/quinary_certificate.json','out/inherited_quinary_certificate.json')]:
    assert sha(OLD/src)==sha(R/dst)
for spec,helper in [('row_pilot_spec.json','row_pilot.py'),('envelope_spec.json','envelope.py'),('position_spec.json','position.py'),('boolean_witness_spec.json','boolean_witness.py'),('quadratic_distance_spec.json','quadratic_distance.py'),('reconstruction_spec.json','reconstruct.py'),('critical12_spec.json','critical12.py')]:
    assert read(R/'out'/spec)['helper_sha256']==sha(R/'code'/helper)
files=[]
for p in sorted(R.rglob('*')):
    if not p.is_file() or p.name=='PERSISTENCE_RECEIPTS.json':continue
    assert p.stat().st_size<20*1024*1024
    if p.suffix=='.json':read(p)
    files.append({'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
save(R/'out/PERSISTENCE_RECEIPTS.json',{'status':'LOCAL_FILES_VALIDATED','checked_at_utc':now,'protocol_fields_exact':True,'claim_statement_sha256':claim['statement_sha256'],'compatibility_copy_identical':True,'full_fei_status':'OPEN','independent_review':'PENDING','remote_copy':'SUPERVISOR_PENDING','files':files})
print(json.dumps({'status':'LOCAL_FILES_VALIDATED','files':len(files),'run':R.name,'claim':claim['claim_id'],'full_fei':'OPEN','next':next_action}))
