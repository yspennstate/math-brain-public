import json,hashlib,datetime
from pathlib import Path
R=Path(__file__).resolve().parents[1]; A=R.parent.parent; BASE=A.parent.parent
P=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
a34=BASE/'agents/A034/runs/20261014T055220Z-account05-A034-phase-energy-transfer'
a32=BASE/'agents/A032/runs/20261014T043539Z-account05-A032-boolean-phase-realizability'
a33=BASE/'agents/A033/runs/20261014T051927Z-account05-A033-derivative-hierarchy'
prev=A/'runs/20261014T030635Z-account05-A079-correlated-auxiliaries'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
v=read(R/'out/validation.json');b=read(R/'out/branch_boundary.json');s=read(R/'out/scalar_validation.json')
assert all(t['status']=='PASS' for t in (v,b,s))
assert v['seconds']<60 and b['seconds']<60
sources=[P,BASE/'BOARD.md',BASE/'claude/B16/STREAM_NOTES.md',a34/'PROOF.md',a34/'REPORT.md',a34/'CLAIMS.json',a32/'REVIEW_A079.md',a32/'CLAIMS.json',a33/'REPORT.md',a33/'CLAIMS.json',prev/'CLAIMS.json']
manifest=[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources]
save(R/'out/SOURCE_MANIFEST.json',manifest)
up=next(c for c in read(a34/'CLAIMS.json') if c['claim_id']=='A034-ALL-PRODUCT-ROW-PAYMENT')
assert up['statement_sha256']=='d42f5efd43a5ac7a718a413147f7d3327f3d8061d629487f7d19946f27e0be9a'
assert sha(a34/'PROOF.md')=='ec11c426f1fa4be8b0037385845ceac5e88705e212159a019a1791413449caf8'
review={'reviewer':'A079','verdict':'HOLDS_AT_STATED_SCOPE','method':'Complete all-N primitive norm and complementary convolution reconstruction, independent physical-height enumeration of3584 norm25 rows instead of author Fourier phase enumeration, symbolic norm125 signs, shared-mask and full Gibbs/address ledger; no author code import or substantive repair','source':{'path':str(R/'REVIEW_A034.md'),'sha256':sha(R/'REVIEW_A034.md')},'registry_adoption':'NOT_VERIFIED'}
up['review_records'].append(review);up['status']='INDEPENDENTLY_RECONSTRUCTED_BY_A079_PENDING_REGISTRY_ADOPTION'
old=next(c for c in read(prev/'CLAIMS.json') if c['claim_id']=='A079-CUBIC-ROW-CONDITIONAL-PAYMENT')
sourceold=next(c for c in read(a32/'CLAIMS.json') if c['claim_id']==old['claim_id'])
assert old['exact_statement']==sourceold['exact_statement']
assert old['statement_sha256']==sourceold['statement_sha256']
old['review_records']=sourceold['review_records'];old['status']='INDEPENDENTLY_RECONSTRUCTED_BY_A032_PENDING_REGISTRY_ADOPTION'
statement='For every actual Boolean g(z,y) on an independent uniform physical cube, if each positive conditional squared Fourier law of S_Y given S_z=b is a coordinate product with fair varying marginals and deterministic frequency coordinates, arbitrary Fourier signs allowed, then H(g)<=2I(g). If both frequency branches are positive their probabilities are exactly1/2, and H(g)=1+(m_0+m_1)/2, I(g)=1/2+(a_0+a_1)/2 with a_b>=m_b/2. The constant2 is attained by the nonflat nonproduct four-bit Boolean fixture in BOUNDARY.md, with H=3 and I=3/2. No nonfair branch, general height-two row or arbitrary seed tensor extension is asserted.'
claim={'claim_id':'A079-FAIR-BRANCH-NONPRODUCT-ENDPOINT','version':1,'exact_statement':statement,
 'hypotheses':['Actual Boolean signs; one singled-out physical coordinate z and arbitrary uniform independent physical Y','Positive conditional frequency branches are coordinate-product laws with only fair/deterministic marginals; zero branches omitted','Normalized Walsh, entropy bits, influence original physical degree; no Booleanity assumed of partial Fourier rows'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A079'],
 'proof_source':{'path':str(R/'BOUNDARY.md'),'sha256':sha(R/'BOUNDARY.md'),'validation':['out/branch_boundary.json','out/nonflat_truth.json','out/scalar_validation.json']},
 'proof_dependencies':[],'review_records':[],'status':'NARROW_TERMINAL_ENDPOINT_AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A032','A033','A034','A088','A094','B16','B20']}
save(R/'CLAIMS.json',[up,old,claim])
next_action='Derive or refute full unequal-mass nonproduct frequency-branch payment when one branch has nonfair product marginals: retain h2(q), both actual partial-row norms/heights and complete spectra, signed address/Renyi gap, inherited terminal debts and one unused physical reserve. A032/A034 consume; A088/A094 review.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B16','packet_id':'A079','gap_id':'G-PHASE-COND','attempt_id':'A079-phase-5',
 'method':'Consume A032 review; independently reconstruct A034 all-product extension using physical-height norm endpoints; exact targeted nonproduct two-frequency-branch census; close fair-branch endpoint by dyadic partial-row norms.',
 'mathematical_delta':{'review':'A034-ALL-PRODUCT-ROW-PAYMENT@1 independently HOLDS; no repair or withdrawn gcd inference','prior_review_consumed':'A032 accepts A079-CUBIC-ROW-CONDITIONAL-PAYMENT@1 without repair','new_endpoint':'Actual Boolean fair-product frequency branches have masses1/2 and H<=2I in every data dimension; sharp nonflat nonproduct example H3,I3/2','finite_boundary':{'gates_mod_global_sign':32768,'admitted_gate_branch_pairs':2112,'nonflat_pairs':1536,'sharp_pairs':384},'signed_gap_fixture':'Two unused addresses: H(w)-E R=-2log2(3), full conditional entropy3','first_unsupported_line':'Nonfair branch norms need not be dyadic; h2(q) and both full conditional spectra require paid unequal-mass transfer with actual partial-row heights'},
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'ALL_PRODUCT_TERMINAL_INDEPENDENTLY_ACCEPTED; FAIR_BRANCH_ENDPOINT_AUTHOR_PROVED; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':up['claim_id'],'version':1,'use':'Independent full-chain review; not a premise of the new self-contained endpoint'},{'claim_id':old['claim_id'],'version':1,'use':'A032 independent acceptance consumed; exact statement unchanged'},{'claim_id':'A034-SIGNED-ODD-MASK-ADMISSION','version':2,'use':'Correction noted; withdrawn version1 coupled inference not used'},{'claim_id':'A033-TWO-NONFAIR-TERMINAL-PAYMENT','version':1,'use':'Frontier source read; no proof premise'}],
 'claims_created_or_changed':[{'claim_id':up['claim_id'],'version':1,'change':'Independent A079 HOLDS review appended; source statement/proof unchanged'},{'claim_id':old['claim_id'],'version':1,'change':'A032 acceptance consumed without statement change'},{'claim_id':claim['claim_id'],'version':1,'change':'Narrow endpoint refinement of the existing conditional-row mechanism, not a broad universal candidate'}],
 'source_artifacts':manifest,'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Unequal-mass/nonfair and general height-two partial-row nonproduct payment remains open','Independent review of new endpoint and registry/mirror adoption unverified'], 'packet_ids':['A079']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
report=f'''# A079 stage5: all-product review and a paid nonproduct endpoint

## exact target, quantifiers, hypotheses and units

Resume G-PHASE-COND for actual Boolean F on two independent uniform physical
addresses and arbitrarily many physical data bits; entropy in bits and original
coordinate influence. Independently audit A034's new ALL coordinate-product
conditional-row theorem, arbitrary odds/signs/nonfair count, which gives sharp
Kcond=3/2+(5/2)h2(1/10), joint Kall=6+2log2(65/64)<7, and sharp
Q<=5I_Y/2. Then move to a genuinely nonproduct spectrum whose two positive
frequency branches are product. The new all-dimensional fair-branch endpoint
for actual Boolean g(z,y) proves H<=2I sharply. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read BOARD snapshot2026-10-14 06:02UTC in bounded sections, B16 STREAM_NOTES
v2 dated2026-10-11 23:25Z in full, own STATUS and prior CLAIMS, and complete
EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2. The lead's original
bent target was already closed by hardness transport; its do-not-repeat and
full-terminal requirements govern this productive continuation.

Read A034 stage5 REPORT/CLAIMS and PROOF.md (run20261014T055220Z), especially
the norm endpoints and complete conditional ledger. Read A032 stage5 CLAIMS
and REVIEW_A079.md in full (run20261014T043539Z): our prior single-nonfair
theorem independently HOLDS, and the coupled-gcd objection was correctly
isolated. Read A033 stage5 REPORT/CLAIMS (run20261014T051927Z), the two-nonfair
endpoint precursor. Source paths, hashes and sizes are in
out/SOURCE_MANIFEST.json. Earlier campaign/paper reads remain background;
no new external paper, web search or brain query was used or needed.

## complete derivation or exact first unsupported line

REVIEW_A034.md reconstructs the full proof without author code or a repair.
Primitive raw product magnitudes have integer power-of-two common scale;
the physical height-two norm forces 5^N<=oddpart(k)<=4*2^(N+m). The all-N
induction leaves only two endpoints beyond the accepted single-coordinate
exception. We reject N=2,m=1 analytically by the full-complement convolution,
and independently enumerate every3584 forced physical norm25 pattern modulo
global sign. N=3,m=2 forces one unit point and31 height-two points; the
complement modulus27 cannot divide96. Shared halfcube companions, exact
Gibbs constants, complete conditional entropy and the address ledger are all
reconstructed. Verdict: HOLDS at the stated scope. We do not use or accept
the withdrawn coupled assertion in odd-mask version1; corrected version2 is
compatible. A034's stronger theorem supersedes the multiple-nonfair frontier
in our previous NEXT, so we do not open a competing product-row candidate.

BOUNDARY.md proves a narrow nonproduct endpoint: for actual Boolean g, its
two partial Fourier rows are integer0,+/-1 on disjoint physical supports.
If each positive conditional spectrum is fair product, constant raw Walsh
magnitude has no odd divisor, so each branch norm is dyadic. Their norms sum
to1, hence both equal1/2. The full entropy is1+(m0+m1)/2 and physical
influence at least1/2+(m0+m1)/4, yielding H<=2I. This includes arbitrary
Fourier signs and deterministic frequency characters in every dimension.

The actual nonflat four-bit data fixture has H=3,I=3/2, attaining equality,
and is outside the coordinate-product whole-row hypothesis. Embedded with
two unused addresses it retains conditional entropy3 and signed address gap
-2log2(3); the whole-row Renyi bill is not silently discarded. This diagnostic
fixture is not claimed to evade every possible decomposition or disprove FEI.

The exact first unsupported extension is unequal branch-mass payment when a
nonfair product branch destroys dyadic norm rigidity: pay h2(q) PLUS both
complete branch entropies from actual physical q and an unused conditional
reserve, preserving the signed address/Renyi gap and inherited terminals.
General address partial rows may additionally be half-integral and have
different scaled height. No universal Renyi/I theorem or Boolean-terminal
substitution is assumed. No unrestricted tensor or physical-restriction
closure is asserted.

## executed validation with domain, arithmetic, commands and outputs

All commands run as python -X utf8 from A079, with run-relative code paths.
Every domain was frozen in out/ before execution. Independent helpers import
no author implementation. Estimated memory<=40MB; no >300MB job was begun,
so memok was not required. Each pilot/search finished in<60s; no dimension
loop, GPU, background task, git, external message or outside write occurred.

- code/check.py:3584 physical norm25 rows,32 symbolic norm125 singleton
  patterns,25 one-coordinate height pairs and128 actual three-bit Boolean
  gates modulo output sign. PASS:{v['assertions']} exact assertions,
  {v['seconds']:.4f}s; no norm25 product row. The symbolic norm125 test does
  not assert a finite phase enumeration.
- code/branch_boundary.py v1:explicit fixed four-bit32768-gate census,
  all4 branch choices, integer full product identities;12.2915s discovery.
  The v2 repeat is justified by the new dyadic-norm lemma and was separately
  frozen before execution. Final PASS:{b['assertions']} exact assertions,
  {b['seconds']:.4f}s,2112 admitted pairs,1536 nonflat pairs,384 exact
  H=2I equalities. Every admitted branch in THIS domain is fair product;
  larger domains are not claimed classified.
- code/scalars.py:15 exact integer/Fraction certificate comparisons PASS.
  Constant inequalities are reduced analytically to integer powers; no
  floating-point sign or interval-overlap equality is used. The nonflat
  witness entropy3, influence3/2 and sqrt-probability sum3 are exact.

Actual32-/64-sign embedded witnesses are reconstructed from truth tables;
spectral influence matches physical-edge influence. Output JSON and truth
are in out/validation.json, branch_boundary.json, scalar_validation.json
and nonflat_truth.json. No exhaustive six-bit truth-table search is implied.

## proof dependencies and changed downstream conclusions

The review of A034-ALL-PRODUCT-ROW-PAYMENT@1 independently reconstructs all
premises. The new fair-branch lemma is self-contained and has no proof
dependency on a pending theorem. A032's review of our prior claim is consumed
unchanged. A034 supplies the stronger accepted product terminal, so A032/A033/
A079 can retire unbounded nonfair-count admission as an unpaid product line.
The odd-mask version1 coupled assertion remains withdrawn, not implicitly
restored. The address-only Q inequality, nonfair/nonproduct transfer and
unrestricted FEI remain open. One new narrow terminal endpoint is recorded;
no broad universal candidate or schedule was opened. Registry adoption,
second independent acceptance of the new endpoint and mirrors are unverified.

## one next mathematical action and independent reviewer

{next_action}
The first target is the norm/height-normalized unequal-mass partial-row
interface, rather than another finite census or flat-padding test. Saved
source-bound handoffs are the only communication to other agents.

## actual persistence receipts or precise save blocker

All four required protocol files, independent review, endpoint proof, code,
frozen specs, exact outputs and witness are saved inside this run. STATUS.md
has exactly two lines; WORKLOG.md and LEARNED.md are current. The finalizer
checks exact protocol keys, unchanged upstream statement hashes, source
proof hash, output PASS flags and byte-identical PROGRESS/PACKET_DELTA with
packet_ids[A079]. out/PERSISTENCE_RECEIPT.json records source/local SHA256s,
file sizes and actual validation totals. Each file is below20MB. Local
persistence is verified; no remote copy or publication receipt is claimed.

**Universal bridge:** This stage moves the lead's G-PHASE-COND bridge toward
C018/C020 by independently accepting the entire all-product conditional
terminal class and closing the first fair-branch nonproduct endpoint with
its full conditional entropy and one physical branch account at sharp rate2.
It establishes no universal erasure or stopping-tree constant. Unequal
nonfair branch masses, general partial-row heights, signed address/Renyi
conversion and inherited terminal payment remain unpaid. NEXT attacks this
precise loss of dyadic norm rigidity with both branch spectra retained,
because that is the immediate missing transfer from already paid product
terminals to general Boolean rows, rather than another isolated flat class.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: Stage5 complete: A034 all-product conditional theorem independently HOLDS; A032 acceptance consumed; nonproduct fair-branch endpoint H<=2I proved, sharp H3/I1.5; exact checks PASS; FEI OPEN.\nNEXT: Unequal-mass nonfair frequency-branch transfer with actual partial-row norms/heights, h2(q), both full spectra, signed address gap and one unused physical reserve; A032/A034 consume, A088/A094 review.\n',encoding='utf-8')
entry='\n2026-10-14 stage5 (run '+R.name+'): Read new board/lead/status. A034 had already closed all-product rows, so independently reconstructed its full norm/endpoint/shared-mask/Gibbs/address proof without author code; HOLDS, no repair. A032 accepted our earlier single-nonfair theorem. Independent physical norm25 enumeration3584 cases and norm125 parity certificates PASS. Targeted32768 four-bit data gates found2112 nonproduct two-product-branch pairs,1536 nonflat; all branches fair. Proved dyadic partial-row rigidity and sharp all-dimensional H<=2I endpoint, exact nonflat witness H3/I1.5. Validation10882+6336+15 assertions PASS. Unequal/nonfair partial-row entropy payment, address-only Q and full FEI remain open.\n'
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(entry)
learn='''
2026-10-14 stage5 durable facts:
- A034-ALL-PRODUCT-ROW-PAYMENT@1 independently reconstructed by A079: primitive odd norm factors>=5 force m>=N except ratio3 endpoint; norm25 complement products16/9 contradict square moments+/-1,+/-7; norm125 complement27 cannot divide96. The full all-N shared-mask/address entropy theorem HOLDS without the withdrawn coupled-gcd line. Do not repeat a bounded nonfair class.
- A032 independently accepts A079-CUBIC-ROW-CONDITIONAL-PAYMENT@1 at its exact arbitrary-odds/phase scope; registry/mirror adoption not verified.
- For ACTUAL Boolean g(z,y), fair-product positive frequency branches yield0,+/-1 partial rows, raw magnitudes powers2 and dyadic branch norms. Both positive norms must be1/2. H=1+(m0+m1)/2<=2I, arbitrary signs/deterministic frequency bits, every dimension. These partial rows are not Boolean terminal restrictions.
- Exact four-bit nonflat nonproduct witness raw Walsh[-8,0,0,0,4,4,-4,4,8,0,0,0,4,4,-4,4], frequency bit2 branches fair counts1 and3, masses1/2, H3,I3/2. Two-unused-address embedding has conditional entropy3, whole-row Renyi2log2(3), signed address gap-2log2(3). This is a paid endpoint, not a counterfamily or unrestricted tensor certificate.
- First unpaid step: a nonfair branch has an odd norm factor, so probability need not be1/2; preserve h2(q), both whole conditional spectra, actual partial-row heights, signed address gap and one unused physical reserve. General height-two address-row frequency children may be half-integral. Do not apply the Boolean terminal theorem to them merely because their normalized spectra are product.
'''
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write(learn)
protocol=read(P)
required=set(protocol['required_per_run']['progress_fields']);required.remove('packet_ids (one primary ID, for compatibility)');required.add('packet_ids')
assert set(progress)==required
for c in read(R/'CLAIMS.json'):
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    assert c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode()).hexdigest()
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']+[A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']
assert all(p.stat().st_size<20*1024*1024 for p in files)
receipt={'status':'PASS_LOCAL_PERSISTENCE','checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'protocol_keys_checked':True,'claim_statement_hashes_checked':True,'progress_delta_identical':True,
 'actual_assertions':v['assertions']+b['assertions']+s['assertions'],
 'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],
 'upstream_sources':manifest,'remote_mirror':'NOT_VERIFIED','independent_review_of_new_endpoint':'PENDING'}
save(R/'out/PERSISTENCE_RECEIPT.json',receipt)
print(json.dumps({'status':receipt['status'],'files':len(files),'assertions':receipt['actual_assertions'],'run':str(R)},indent=2))
