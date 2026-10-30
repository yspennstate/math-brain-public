from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];HOME=ROOT.parents[1]
PROTO=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTO.read_text(encoding='utf-8'))
def write(p,s):p.write_text(s,encoding='utf-8')
def js(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
prior=HOME/'runs/20261014T063752Z-fleet05-A050-repair-with-scope'
peer=HOME.parent/'A047/runs/20261014T124731Z-fleet05-A047-boundary-search'
statement=('For any uniform Boolean core h let t=Pr(h=-1), and F_h=(-1)^a at x=0, h at x=b=1, and +1 otherwise. '
 'Let Q be its complete canonical nonempty occupancy reference with matched empty mass and every Fourier marginal. '
 'A unique positive occupancy normalizer exists; the telescoping product argument needs no sum-of-squares restriction. '
 'Set G(h)=h2(t/2)+sum_j h2(Inf_j(h)/4). Query b first, then any finite adaptive fresh data-only stopping continuation in b1, retaining b0 and keeping x,a unqueried. '
 'If every terminal data core g has a supplied certificate H(g)<=4I(g), and its actual rate4 mean terminal surplus S is unused, '
 'then Hroot,Hterminal>=2,S>=2 and the whole fixed-reference liability L=KL(P||Q)+[Hroot-EHleaf-4(Iroot-EIleaf)]_+<=G(h). '
 'The same inherited kernels, fair fallback on source-zero rows, and full reference-only support retain all erasure/outcome and terminal KL in that one source account. '
 'Thus G(h)<2 gives complete payment once; previously booked conservative overpayments require their own additional omega from the same owner. '
 'For h the product of m disjoint width-r point-defect signs, all terminal certificates persist under data restriction. '
 'For every r>=8 and2<=m<=r, G(h)<189/128, leaving more than67/128 bit of that same owner through any such continuation. '
 'The first data query in b1 has two nonconstant core children. This is a scoped sufficient repair, not globally weakest; arbitrary mixed histories, fresh resets and full FEI remain open.')
own={
 'claim_id':'A050-NONPOINT-CANONICAL-GAP-REPAIR','version':1,'exact_statement':statement,
 'hypotheses':['Finite uniform Boolean signs; Shannon and KL bits',
 'Root F_h and complete matched-marginal canonical occupancy Q exactly as in PROOF sections2-3; dummy coordinates contracted',
 'Same inherited normalized actual coherent channel throughout, fair source-zero fallback and all reference-only rows retained; no fresh reference reset',
 'Query b first, then only fresh data in b1; x,a unqueried, b0 and every full terminal retained',
 'Actual terminal core certificates H(g)<=4I(g) and their mean terminal surplus is genuinely previously unused',
 'G(h)<2 for claimed full payment; previously booked overpayment omega additionally reserved; unpaid earlier ancestor exposures are excluded',
 'Explicit all-dimensional family has disjoint point-defect blocks, integer r>=8 and2<=m<=r'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A050'],
 'proof_source':['PROOF.md','code/check.py','out/CHECK.json','code/payment.lean','out/LEAN.json'],
 'proof_dependencies':[], 'review_records':[],
 'status':'ANALYTIC_PROOF_WITH_EXACT_CHECKS_INDEPENDENT_REVIEW_PENDING_LEAN_RUNTIME_UNVERIFIED',
 'supersedes':[],'refutes':[],
 'first_unproved_line':'For arbitrary cores/mixed histories, supply enough genuinely unused certified surplus to pay the actual full canonical CE gap and fresh resets after earlier booked debts.',
 'next_consumers':['A047','A039','A038','A083','A085','A092','A087','A095','B10','B20']}
source=next(c for c in json.loads((peer/'CLAIMS.json').read_text(encoding='utf-8')) if c['claim_id']=='A047-COMPLETE-CANONICAL-FRONTIER-PAYMENT')
review=dict(source)
review['proof_source']=[str(peer/'PROOF.md'),str(peer/'code/check.py'),str(peer/'out/CHECK.json')]
review['review_records']=list(source['review_records'])+[{'reviewer':'A050','verdict':'ACCEPT_AT_STATED_SCOPE','source_statement_sha256':source['statement_sha256'],'reconstruction':'PROOF sections1,2,4,5 reconstruct full source chain, signed payment, occupancy normalization, point-defect hereditary certificate and balanced conservative overpayment. New independent exact physical transport on non-point continuation; source code not replayed. Strict rational signs in out/REVIEW_CERTIFICATE.json.','source_changes':'NONE; non-point extension is a separate A050 claim'}]
review['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A050'
js(ROOT/'CLAIMS.json',[own,review])
check=json.loads((ROOT/'out/CHECK.json').read_text(encoding='utf-8'))
assert check['status']=='PASS' and check['cases']==8
assert 3**12>2**19 and 2209**8<2*2040**8 and 60**8<8*47**8
js(ROOT/'out/REVIEW_CERTIFICATE.json',{'status':'PASS','integer_signs':['3^12>2^19','2209^8<2*2040^8','60^8<8*47^8'],'source_statement_sha256':source['statement_sha256'],'source_unchanged':True,'proof_reconstruction':'PROOF sections1-5','independent_source_replay':False})
next_action='A047/A039/A092 review; replace the marginal-subadditivity gap by the exact canonical gap on a supplied core with G>=2, preserving one original unused owner and all source/terminal debts after an active data query.'
progress={
 'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B10','packet_id':'A050',
 'gap_id':'C024-SAME-REFERENCE-CERTIFIED-UNUSED-FRONTIER','attempt_id':'A050-stage6-nonpoint-gap-v1',
 'method':'Independent source review, analytic fixed-reference payment and hereditary non-point eligibility; exact rational physical reconstruction',
 'mathematical_delta':'Accepted A047 complete canonical payment unchanged; general normalizer existence without square-sum condition; non-point all-r family L<189/128 from same S>=2 through arbitrary data continuations, leaving>67/128. No universal FEI constant improves.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_ANALYTIC_PROOF_EXACT_CHECKS_REVIEW_PENDING_FULL_FEI_OPEN',
 'claim_versions_used':['A047-COMPLETE-CANONICAL-FRONTIER-PAYMENT@1','A050-CONDITIONAL-LIKELIHOOD-ENVELOPE-REPAIR@1'],
 'claims_created_or_changed':[own['claim_id']+'@1',source['claim_id']+'@1: independent acceptance'],
 'source_artifacts':[str(peer/'PROOF.md'),str(prior/'PROOF.md'),'PROOF.md','out/CHECK.json','out/LEAN.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':own['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal unused-surplus and mixed-history eligibility open; no fresh-reference reset payment','Named Lean scalar check RUNTIME_UNVERIFIED after55s; no formal certification','Independent review, supervisor copying and remote mirror verification pending'],
 'packet_ids':['A050']}
js(ROOT/'PROGRESS.json',progress);js(ROOT/'PACKET_DELTA.json',progress)
report='''# exact target, quantifiers, hypotheses and units

A050/B10 stage6 resumes repair-with-scope. Pay the whole inherited canonical source, including quotient/conditional terminal KL and positive query deficit, on a weak non-point core with two nonconstant data children. Uniform Boolean signs, entropy/KL bits. The changed sufficient hypothesis is an explicit marginal gap G(h)<2 together with actual previously unused certified frontier surplus. No globally weakest hypothesis or full FEI theorem is claimed. Current user deadline2026-10-23T14:49Z supersedes the older protocol date.

# sources actually read, revisions and theorem locators

Read execution-v2 protocol in full; board snapshot2026-10-21T17:03Z, B10 lead v2, own STATUS/LEARNED and actual completed prior reports. Later resume directories have no REPORT; last completed A050 proof is20261014T063752. Read campaign README/status and relevant registry/packet/plan entries, supplemental campaign/claims/counterexamples/seeds/mapping, source inventory, and relevant composition/percolation text excerpts (explicit legacy cp1252 decoding). These are background; no literature theorem is a new proof premise. Source receipts pin observed bytes. The new primary dependency is A04720261014T124731 PROOF sections1-6 and CLAIMS, with A08520261014T074749 full proof clarifying child-only versus full-source ownership. Previous A050 exact primitives are copied into this run so its checker is self-contained. No brain result is used as a theorem; read-only recall returned the known Booleanity and marginal-entropy obstructions.

# complete derivation or exact first unsupported line

PROOF.md gives a self-contained proof. For a fixed inherited reference, one source KL equals all erasure/outcome plus final inherited KL. Its complete conservative liability L=A+[D-4R]_+ is at most CE minus the lower root/terminal entropy floor. The canonical normalizer exists uniquely by a decreasing telescoping-product polynomial, without the former square-sum sufficient restriction. For F_h, canonical CE<=2+G(h), all root/terminal entropies>=2, and certified terminal H(g)<=4I(g) gives genuine unused S>=2. Therefore L<=G(h), preserving all terminal/reference-only rows and one original bank through arbitrary data-only stopping continuations.

For m disjoint width-r point-defect factors, hereditary terminal certificates are proved by exact tensor identities and the elementary point-defect spectrum. All integer r>=8,2<=m<=r have G<189/128, hence complete liability<189/128 and more than67/128 remains. The first queried core bit has two nonconstant children. The report distinguishes this all-r analytic result from finite checks. Prior matching, the conditional moment-envelope and complete marginal-gap repairs are explicitly compared without asserting a false global ordering. Arbitrary cores with many parity bits fail the new hypothesis. Earlier arbitrary tilted-reference and marginal-coordinate obstructions remain intact.

A047 complete payment is independently accepted unchanged, including the balanced already-booked total<21/32 from final2. A085's reported larger remainder excludes earlier source/outcome costs; A047 includes them. This is a scope difference, not numerical drift. FIRST UNSUPPORTED UNIVERSAL LINE: enough genuinely unused certified terminal surplus pays the actual canonical gap and fresh resets for arbitrary supplied cores/mixed histories after earlier bookings. No universal constant improves.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes search. Command: python -X utf8 runs/20261021T171109Z-fleet03-A050-repair-with-scope/code/check.py --pilot, then without --pilot. Final pilot PASS:2 cases,487 ledger+920 primitive assertions,2.945s. Main PASS:8 cases,10126 ledger+18200 primitive assertions,29.200s; maximum11 physical variables. Fixtures(m,r)=(2,2),(2,3),(2,4),(3,2), each at two sign-bracketed32-step rational normalizer endpoints, normalized as complete perturbations. These are NOT the algebraic canonical law. No symmetry reduction or automatic dimension increase. Integer Walsh/direct physical edges, Fraction full channel transport and atomwise multiplicative likelihood products verify normalization, reference-only rows, exact influence telescope, nonconstant children, full source ledger and terminal surplus. Rational atanh tails and outward dyadic log endpoints certify strict inequalities; exact atom identities, not interval overlap, prove the KL chain. Small algebraic boundary certificates support the analytic proof rather than extending finite scope.

Two checker defects were corrected before acceptance: expected removed influence used delta/4 instead of delta/2; the auxiliary identity interval requested150bits from a32-term logarithm routine giving about100bits, and was changed to80bits while preserving exact product certificates. Failed runs are logged, not counted. No theorem conclusion rests on either failure. Lightweight job estimate100MB, frozen runtime55s. memok passed before Lean. The named scalar Lean check, source/compiler/Mathlib receipt in out/LEAN.json, timed out55s; result RUNTIME_UNVERIFIED, no axioms or target identity certified. An earlier inline attempt also timed out. Rung: analytic proof with exact checks, NOT Lean-checked. Dependency bytes are not independently verified. No further retry is pending.

# proof dependencies and changed downstream conclusions

The new scoped proof reconstructs its premises and uses no unproved FEI claim. A047@1 receives independent acceptance with unchanged exact statement/hypotheses/hash; the non-point extension is separate. A050 prior conditional repair is accepted by A047 at its scope. Consumers may carry the fixed canonical source through this supplied non-point class, without renewing Q or discarding the b0 terminal. Earlier ancestor payment and arbitrary-core eligibility remain separate. The stream's original essential-tax packet is already complete; consuming the new A047 objection/payment follows protocol dispatch and does not contradict the lead.

# one next mathematical action and independent reviewer

NEXT: replace the loose marginal-subadditivity gap by the exact canonical gap on one supplied non-point core with G>=2, keeping the same original unused frontier owner, old booked debits and all source/terminal bills after an active data query. Reviewers A047/A039 primary, A092/A087 for ghost support and ownership. This targets the failing eligibility condition rather than adding a census or renewing a bank.

# actual persistence receipts or precise save blocker

REPORT.md, exact-schema CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json, PROOF, frozen specification, self-contained code, per-case certificates, source receipts and Lean timeout receipt are saved in A050 only. STATUS is two lines; WORKLOG/LEARNED append. out/PERSISTENCE.json pins bytes and hashes and checks schema fields, statement hashes, progress compatibility and sizes<20MB. Required wake/checklist infrastructure calls are separate from research output ownership. No git, messages, other-agent writes, trading-path access, deletion, remote publication or detached job. Local save is complete; independent acceptance of the new theorem, supervisor copying, mirrors and downstream use are pending.

Universal bridge: This stage moves C024 history transfer and C019 stopping-tree payment by accepting the complete canonical source ledger and proving hereditary non-point eligibility at unchanged rate4, including two nonconstant core children and arbitrary finite data-only continuations: total reference-plus-positive-edge liability<189/128 is paid once from actual unused frontier surplus>=2. The universal improvement is zero; arbitrary-core certified unused surplus, mixed queries and fresh resets remain open. NEXT attacks the exact canonical gap where marginal subadditivity stops working, the shortest identified route to the missing universal eligibility theorem rather than another isolated class certificate.
'''
write(ROOT/'REPORT.md',report)
write(HOME/'STATUS.md','STATE: A050 stage6 complete locally: A047 full source payment independently HOLDS; non-point hereditary canonical liability<189/128 from SAME terminal>=2;8 cases/28326 exact checks PASS; Lean timeout; FEI OPEN.\nNEXT: '+next_action+'\n')
for name,text in [('WORKLOG.md','2026-10-21 stage6 complete: independent A047 full-source acceptance; proved general normalizer uniqueness without square-sum hypothesis and explicit non-point hereditary gap repair. Main8cases/28326checks PASS29.2s. Scalar Lean attempts timed out; no formal status claimed. Source/quotient/full-terminal ownership retained; no universal FEI improvement.'),('LEARNED.md','Stage6: For F_h selecting independent character or h/constant, canonical CE<=2+G, G=h2(Pr(h=-1)/2)+sum h2(Inf_j(h)/4). Root/leaf H>=2; terminal H(g)<=4I(g) yields unused S>=2, so full fixed-reference liability A+[D-4R]+<=G. Disjoint products of m width-r point defects, r>=8,2<=m<=r, satisfy hereditary G<189/128, leaving>67/128; first active data query has two nonconstant children. Canonical normalizer uniqueness follows from strict decrease of sum_i r_i product_{j<i}(1-c r_j), no sum r_i^2 assumption. Preserve source/quotient costs and ghost rows. A047 full-source versus A085 child-only remaining margins differ by earlier source/outcome costs. Lean timed out: analytic/exact, not formal. Correct root removed influence for b then data is t/2+delta/2.32-term atanh is about100bits before dyadic rounding; rounding to256bits does not create150bit accuracy.')]:
 with (HOME/name).open('a',encoding='utf-8') as f:f.write('\n'+text+'\n')
paths=[PROTO,HOME/'LEARNED.md',HOME.parent.parent/'BOARD.md',HOME.parent.parent/'claude/B10/STREAM_NOTES.md',peer/'REPORT.md',peer/'PROOF.md',peer/'CLAIMS.json',prior/'REPORT.md',prior/'PROOF.md',HOME.parent/'A085/runs/20261014T074749Z-fleet05-A085-certificate-adversary/PROOF.md']
receipts=[]
for p in paths:
 if p.exists():receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
js(ROOT/'out/SOURCE_RECEIPTS.json',receipts)
fields=protocol['required_per_run']
for c in json.loads((ROOT/'CLAIMS.json').read_text(encoding='utf-8')):
 assert set(c)==set(fields['claim_fields'])
 assert c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode()).hexdigest()
expected={x.split(' (')[0] for x in fields['progress_fields']}
assert set(progress)==expected
assert json.loads((ROOT/'PROGRESS.json').read_text(encoding='utf-8'))==json.loads((ROOT/'PACKET_DELTA.json').read_text(encoding='utf-8'))
assert all('# '+x in report for x in fields['report_fields'])
assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
manifest=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20*1024*1024
  manifest.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
js(ROOT/'out/PERSISTENCE.json',{'status':'PASS','local_only':True,'files':manifest,'protocol_schema_validated':True,'full_FEI':'OPEN','new_claim_independent_review':'PENDING','mirror_verification':'NOT_PERFORMED'})
print(json.dumps({'status':'PASS','files':len(manifest),'protocol_claims':2,'main_cases':check['cases'],'total_main_assertions':check['assertions']+check['primitive_assertions'],'local_run':str(ROOT)}))
