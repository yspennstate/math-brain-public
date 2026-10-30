from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,datetime,math
R=Path(__file__).resolve().parents[1];A=R.parents[1];B=A.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def put(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
v=read(R/'out/validation.json');a=read(R/'out/allocation.json');i=read(R/'out/repro.json')
assert all(x['status']=='PASS' for x in [v,a,i])
total=v['exact_assertions']+a['exact_assertions']+i['exact_assertions'];assert total==56283
e4=sum(Q(1,math.factorial(j)) for j in range(5));exp15=sum(Q(11,3)**j/math.factorial(j) for j in range(16))
assert e4>Q(8,3) and exp15>38 and (2*(Q(1,3)+Q(1,3)**3/3)==Q(56,81) and Q(56,81)>Q(3,5)) and 6+Q(113,12)*Q(81,56)<20
put(R/'out/source_constants.json',{'status':'PASS','fixed_exact_checks':4,'e_taylor_lower':[e4.numerator,e4.denominator],
 'exp_11_over3_lower':[exp15.numerator,exp15.denominator],'ln2_lower':'56/81 from first two positive atanh terms',
 'upper_C0_rational':str(6+Q(113,12)*Q(81,56))})
put(R/'out/lean.json',{'rung':'SETUP_UNVERIFIED','result':'Compute admission held (hung window or under5500MB free); no new compiler process',
 'prior_memok':'exit0; physical free6.5GB and commit free23.8GB before helper call; helper rechecked admission at its later launch',
 'compiler_started':False,'retry':False,'certification':'NONE','statement_scope':'only scalar source-bank inequality; full Fourier/transfer theorem is analytic'})
src60=B/'agents/A060/runs/20261022T233802Z-fleet03-A060-composition-sharpness'
src59=B/'agents/A059/runs/20261022T224007Z-fleet03-A059-decomposition-depth'
src91=B/'agents/A091/runs/20261023T005154Z-fleet03-A091-composition-referee'
sources={}
for p in [src60/'PROOF.md',src60/'CLAIMS.json',src59/'PROOF.md',src91/'REVIEW.md',B/'BOARD.md',B/'claude/B12/STREAM_NOTES.md']:
 sources[str(p)]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
put(R/'out/SOURCES.json',sources)
upstream=[]
for p in [src60/'CLAIMS.json',src59/'CLAIMS.json']:
 x=read(p);xs=x if isinstance(x,list) else x.get('claims',[])
 for c in xs:
  if 'claim_id' in c:upstream.append(c['claim_id']+'@'+str(c.get('version',1)))
statement1=('Let even m>=4,c=2^-m,b be paired quadratic bent with b(0)=1, C=1_{x=0}, and g any independent Boolean fallback, '
 'possibly biased and nonflat after actual compatible restrictions. W_0=g and W_1=b-C+Cg use the SAME g. '
 'Its actual source influence is dX=[1-c-Eg*(sqrt(c)-c)]/2>=3/8. If DX is the complete source entropy decrement, '
 'then for any actual rare-child internal controller continuation consuming conditional influence L<=1, '
 '6dX-DX-(mc/2)L>=dX/3. The original fine reserve and both full actual terminal profiles are retained; no reserve release is used as a second subsidy.')
statement2=('Assume the stated local private-priority wrapper payments (<21 at density>=1/2, <20+log2(1/t) at density t>0) '
 'and signed fine-data payment3/ln2. In the same W geometry with g a private point-priority list of disjoint cores and constant default, '
 'allow arbitrary compatible internal histories, optional source X exposure at any stopping frontier, and arbitrary subsequent internal stopping policies, '
 'while exterior bent bits remain unqueried. The SAME original remaining ticket Qhidden=a[21 Ictrl(g)+5 Idata(g)],a=(1+c)/2, '
 'splits into Q0=20 Ictrl+5 Idata and Q1=c[(20+m)Ictrl+5 Idata], with refund[a-mc/2]Ictrl>=13Ictrl/32. '
 'Thus Hroot<=Uroot+Rroot+Qroot+6Inf_X(root)+E[Hleaf-Uleaf-Rleaf-Qleaf-6Inf_X(leaf)]. '
 'All previous debits and both actual terminal profiles are retained. A source-only KdX account cannot alone pay unrestricted density tax: '
 'the actual private priority OR family gr with2^r blocks of width r and m4 has fine U=R=0, '
 'tax=I(gr)/8>r/12 while dX<=9/16, refuting every fixed source-only rate by choosing r sufficiently large.')
def claim(cid,st,hyp,deps,proof):
 return {'claim_id':cid,'version':1,'exact_statement':st,'hypotheses':hyp,
 'statement_sha256':hashlib.sha256(st.encode('utf-8')).hexdigest(),'contributors':['A057'],'proof_source':proof,
 'proof_dependencies':deps,'review_records':[],'status':'PROVED_LOCAL_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':[],'first_unproved_line':'No unsupported line in the stated scope; arbitrary exterior exposures after the ticket split and universal inherited/terminal entropy remain unpaid.',
 'next_consumers':['A059','A060','A091','A087','A097']}
claims=[claim('A057-NONFLAT-SOURCE-DENSITY-PAYMENT',statement1,
 ['even m>=4','uniform independent exterior/core blocks; same physical g in both branches','L<=1 for source-only payment','original fine labels/actual terminals preserved'],
 ['Boolean physical split:0<=DX<=2','finite Walsh/Parseval','elementary dyadic inequalities'], 'PROOF.md Sections1-2; out/validation.json and out/repro.json'),
 claim('A057-INHERITED-TICKET-DENSITY-TRANSFER',statement2,
 ['private point-priority internal controls, disjoint fine-core data, constant default','exterior bent bits stay unqueried',
  'same unused ancestor ticket after all earlier booked costs; no new ticket supplied at X',
  'local wrapper/signed-data imports at their actual hypotheses; no shared core-data substitution'],
 upstream+['A057-NONFLAT-SOURCE-DENSITY-PAYMENT@1','physical block-influence conservation','conditional local wrapper imports documented in REVIEW_A060.md'],
 'PROOF.md Sections3-4; REVIEW_A060.md; out/allocation.json and out/repro.json')]
put(R/'CLAIMS.json',claims)
nextline='Expose one exterior bent-data coordinate after Q0/Q1 allocation and an actual old internal debit; pay its density/profile change from SAME diminished Q/U/R with both actual terminals. A091/A087 audit ticket induction first.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B12','packet_id':'A057',
 'gap_id':'G-R-SELECT/SOURCE-DEPENDENT-DENSITY-TRANSFER','attempt_id':'A057-stage18-nonflat-inherited-ticket-v1',
 'method':'Actual source mismatch plus original internal influence-ticket split; exact signed fine-profile edge certificates; source-only whole-tax falsifier',
 'mathematical_delta':'Inherited arbitrary nonflat g source paid at SAME6; unrestricted subsequent internal continuation paid by original21/5 ticket split with refund>=13Ictrl/32; source-only fixed-rate extension refuted by actual priority OR family.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_ANALYTIC_PROOFS_PENDING_REVIEW; TRANSFER_HAS_EXPLICIT_LOCAL_IMPORTS; FULL_FEI_OPEN',
 'claim_versions_used':upstream+['A091 stage18 independent acceptance of A057-LATER-PRIVATE-SHARED-Y-PAYMENT@1','A057 stage4 signed U/R ledger'],
 'claims_created_or_changed':[x['claim_id']+'@1' for x in claims],
 'source_artifacts':['PROOF.md','REVIEW_A060.md','SPEC.json','ALLOCATION_SPEC.json','REPRO_SPEC.json','LEAN_SPEC.json',
                     'out/validation.json','out/allocation.json','out/repro.json','out/lean.json','out/SOURCES.json','out/source_constants.json'],
 'next_consumers':['A059','A060','A091','A087','A097'],'next_action':nextline,'stagnant_substantive_attempts':0,
 'blockers':['independent review of new claims pending','compiler admission held; no Lean certificate',
             'local controller/signed-data imports remain explicit proof dependencies','full FEI and universal inherited/terminal entropy unpaid',
             'supervisor mirroring/adoption unverified'],'packet_ids':['A057']}
put(R/'PROGRESS.json',progress);put(R/'PACKET_DELTA.json',progress)
report=f'''# Inherited nonflat fallback through a density-lowering exposure

## exact target, quantifiers, hypotheses and units

Advance A057's SAME-account physical restriction payment after a source exposure lowers exterior density. Entropy is in bits. For every even m>=4, c=2^-m, paired quadratic bent b and C=1 at its zero input, define the actual source children W0=g and W1=b-C+Cg, using one physical independent Boolean g. Arbitrary inherited biased/nonflat g and compatible internal restrictions are allowed. The self-contained source theorem pays actual DX plus a density-tax continuation of consumed influence L<=1 from the SAME6dX account, retaining at least dX/3.

The stronger source-dependent stopped theorem uses the original remaining internal influence ticket21/5, with the source local wrapper imports explicit. It permits arbitrary internal histories, optional X exposure at any stopping frontier and arbitrary subsequent internal continuation while exterior bent bits remain unqueried. Both full actual terminals and their unused tickets remain. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

BOARD snapshot2026-10-23 01:52 UTC, B12 STREAM_NOTES v2 and own STATUS were read first. The lead's original balanced-log target is advanced through the already-paid signed U/R hierarchy; retired baseline identities were not repeated. Protocol revision2026-10-11-execution-v2 field schemas were reread. Earlier campaign sources/papers remain previously read background, not new dependencies. No new literature or primary-paper claim is made.

Read A059 stage17 PROOF Sections1-4, A060 stage6 PROOF Sections1-5/scalar channel check, their rolling learned/status, and A091 stage18 REVIEW. Hashes and byte lengths are in out/SOURCES.json. A059 and A091 already close the saved frequent-exterior fallback NEXT. A091 independently accepts A057's prior local later-B theorem, preserving its original authorship/statement hash. Its acceptance does not certify every earlier stopped import. REVIEW_A060.md reconstructs the fair-source payment and all-c bound at their actual dependencies; the new nonflat/ticket results here are not called independently accepted.

Brain wake flagged stale owner-model/state notes (88.3h/72.9h at wake); self-care is degraded/unverified. Explicit current instructions and source files direct this stage. Initial saved machine probe showed low RAM/disk contention; later memok exited0 at6.5GB free, but the formal helper's subsequent admission held. Those are different measurement windows. No running work was stopped, no heavy numerical job was launched, and the compiler did not start.

## complete derivation or exact first unsupported line

PROOF.md gives the complete derivation. Source mismatch is dX=[1-c-mu(sqrt(c)-c)]/2, not the fair-g value(1-c)/2. For all mu in[-1,1], 3/8<=dX<=9/16. The complete Boolean source decrement satisfies0<=DX<=2. For consumed rare-child controller influence L<=1, the actual root-weighted density tax is(mc/2)L<=1/8. Thus6dX-DX-tax>=dX/3. Original fine release[phi((1+c)/2)-phi(c)/2]Vbar is nonnegative but is not counted as a second subsidy. Arbitrary inherited nonflat core variance is retained.

For an unrestricted continuation the source-only account fails. Actual private priority OR gr on2^r independent width-r point blocks has fine U=R=0 and I(gr)=2r(1-2^-r)^(2^r-1)>2r/3. At fixed c=1/16 its complete density tax=I(gr)/8>r/12, whereas6dX<=27/8. This already fails for every r>=48, before old DX is spent. The family refutes the source-only helper, not FEI; its total original internal influence grows with r.

The useful repair is the SAME unused inherited internal ticket. At hidden X it is Q=a[21Ictrl+5Idata], a=(1+c)/2. Allocate Q0=20Ictrl+5Idata and Q1=c[(20+m)Ictrl+5Idata] to the actual children. The difference Q-(Q0+Q1)/2=[a-mc/2]Ictrl>=13Ictrl/32 is an exact refund. This pays arbitrary subsequent internal logarithmic bills from original unused controller capacity; that tax is not also charged to the source cash account. Before and after exposure, exact physical block-influence drift pays the actual local controller/data prices. The same fine U/R telescope with Q and source ticket6InfX, including their unused terminal balances. Both actual child H-U-R profiles remain intact. This is a conditional use of stated local wrapper/data inputs, not a universal ticket theorem.

First unsupported line: one exterior bent-data query after the split and an already booked internal debit changes the actual C/K0 profiles and child densities; its new charges/ticket rates have not been carried through the SAME diminished account. Generic overlapping core data and universal inherited U/full terminal entropy also remain unpaid. No terminal bill is declared zero because a density is rare.

## executed validation with domain, arithmetic, commands and outputs

Each search has a frozen spec, no symmetry reduction, <=55s runtime guard and <=40MB estimated memory. No dimension was escalated automatically. Commands are python -X utf8 runs/{R.name}/code/check_nonflat.py, check_allocation.py and independent_repro.py. The first frozen root count was corrected to300 before execution. The allocation checker initially stopped at a missing space in an else expression before any mathematical assertion; that syntax error was fixed and the full frozen domain replayed.

Nonflat-source replay:300 actual Boolean roots (m4/all g up to3 bits; m6/all g up to2 bits),840 queried core coordinates,200 biased nonconstant core roots; {v['exact_assertions']} exact assertions PASS in{v['elapsed_seconds']:.3f}s. It checks actual full source entropy, mismatch, same-bank margin and fine reserve scaling. Entropy uses integer Walsh/Fraction prime-log expressions and rigorous36-term atanh enclosures with an explicit tail, never floating signs.

Fine-profile/ticket replay:5184 source cylinders,15552 phase states and20736 internal query edges, including1238 positive controller-ticket refunds; {a['exact_assertions']} exact assertions PASS in{a['elapsed_seconds']:.3f}s. Every local signed fine U/R debit and remaining ticket difference is checked; induction in the proof yields adaptive stopping policies, not an asserted exhaustive policy enumeration. The64 finite fixtures include32 constant-default representations within the imported theorem and32 nonconstant-default stress controls beyond its universal stated scope; no default-core generalization is inferred from those finite passes.

Independent reproduction:16 full source spectra/decrements from direct character sums with a separate factorization path; five actual small priority-OR controls checked by physical edges and spectral influence;253 dyadic allocation cases. {i['exact_assertions']} exact assertions PASS in{i['elapsed_seconds']:.3f}s. Final total:{total} exact assertions, plus four fixed rational/Taylor comparisons for imported constants. The huge all-r OR family is proved analytically; no giant table was built or claimed enumerated.

Lean admission returned SETUP_UNVERIFIED (hung window or below5500MB free); no compiler process started and no retry was launched. Rung: analytic proof with exact finite certificates and explicit local imports, pending independent review; not Lean-checked.

## proof dependencies and changed downstream conclusions

Source-budget theorem uses only Boolean Parseval, the exact physical two-child entropy identity, dyadic bounds and actual independence. The stopped transfer additionally uses A059's accepted frequent-wrapper/last-frequency and signed-data inputs, and A060's all-c local controller bound, with the review limits in REVIEW_A060.md. Real source claim IDs/versions are recorded in PROGRESS/CLAIMS. The local all-c logarithm is retained; no O(alpha^2) replacement of the inherited coherent logarithm or new whole-subformula recharge is introduced.

A059/A060/A091 can replace the fair-g density-lowering example by arbitrary inherited nonflat g. For unrestricted continuation they must use the unused original INTERNAL ticket as well as source cash; the OR family certifies why source-only funding cannot suffice. Original rate21/5 capacity pays its two actual descendant allocations, with old costs and both full terminals protected. No independent acceptance of the new transfer is claimed.

## one next mathematical action and independent reviewer

{nextline} This is the nearest unpaid actual query after the newly paid exposure, rather than another gate-class entropy bound. A090 should audit ancestor-ticket ownership and the exact terminal/source balance; A060 should check the source-only obstruction and density constants.

## actual persistence receipts or precise save blocker

All four required protocol files, proof/review, frozen specs, code and exact outputs are inside the assigned A057 run. STATUS is exactly two lines and WORKLOG/LEARNED carry the new theorem, obstruction and NEXT. out/PERSISTENCE.json records exact field validation and readback hashes. No shared research index, other agent folder, research Brain store, repository, mail or trading file was written. Required wake/checklist bookkeeping ran separately. Supervisor copying, adoption and independent review are unverified. Every artifact is below20MB.

## Universal bridge

This stage moves C019 stopping-tree payment through an actual density-lowering source with arbitrary inherited nonflat fallback: source cash rate6 preserves a positive old-debit margin, and the SAME original internal21/5 ticket funds unlimited subsequent internal continuations with refund>=13Ictrl/32 and both full terminal profiles retained. The actual OR family rules out paying that whole continuation from a source-only fixed-rate account. Exterior-query transfer after a booked internal cost and universal inherited/terminal entropy remain open. NEXT carries the diminished ticket through that first exterior query, the shortest extension of this physical-tree account toward full FEI rather than a separate class result.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A057 stage18 nonflat density exposure paid SAME6; original21/5 ticket funds all later internal policies with refund>=13Ictrl/32;56283 exact assertions PASS; review pending; FEI OPEN.\nNEXT: Expose exterior bent-data bit after actual internal debit; retain SAME diminished Q/U/R and both full terminals; A091/A087 review source/ticket transfer.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n[{stamp}] {R.name}: consumed A091 independent acceptance of stage17 and A059 wrapper closure. Extended fair source to arbitrary inherited nonflat g: SAME6 source account leaves>=dX/3 for L<=1. Whole source-only continuation refuted by actual priority OR family. Derived original21/5 internal ticket split for arbitrary subsequent internal policies, refund>=13Ictrl/32 with full U/R/Q/source terminals. All56283 exact assertions PASS; allocation syntax typo fixed before mathematical execution; formal admission held, no compiler. New claims pending A091/A087 review; full FEI OPEN.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('''\nStage18 durable facts: A091 stage18 independently accepts A057 later-B@1; A059 already paid frequent exterior fallback. In W0=g,W1=b-C+Cg with even bent m>=4 and c=2^-m, actual dX=[1-c-Eg(sqrt(c)-c)]/2 is in[3/8,9/16], not the fair-g formula. Full DX<=2 and tax(mc/2)L<=1/8 for L<=1 give SAME6dX-DX-tax>=dX/3 with arbitrary inherited nonflat g. Fine R release[phi((1+c)/2)-phi(c)/2]Vbar>=0 is not extra cash. Original hidden ticket a[21Ictrl+5Idata] splits into20Ictrl+5Idata and c[(20+m)Ictrl+5Idata], refund[a-mc/2]Ictrl>=13Ictrl/32. Physical block influence induction carries old bookings and ALL subsequent internal stopping policies; return full H-U-R-Q-6InfX at actual terminals. Imports: A059 local frequent/signed-data and A060 all-c bounds. Do not also charge that same tax to source cash. Source-only whole-tax helper fails for actual priority OR with2^r width-r blocks: I>2r/3, tax=I/8>r/12, fine U=R=0, source6dX<=27/8; r>=48 suffices, no FEI disproof.56283 exact assertions PASS; formal SETUP_UNVERIFIED, no compiler. Next exterior query after a booked internal cost must use SAME diminished ticket.\n''')
protocol=read(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
pf={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']};cf=set(protocol['required_per_run']['claim_fields'])
assert set(progress)==pf and all(set(c)==cf for c in claims)
assert read(R/'PACKET_DELTA.json')==read(R/'PROGRESS.json')
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipts={}
for p in R.rglob('*'):
 if p.is_file():
  raw=p.read_bytes();assert len(raw)<20_000_000
  receipts[str(p.relative_to(R))]={'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
put(R/'out/PERSISTENCE.json',{'schema_fields':'PASS','packet_delta_matches':True,'rolling_status_two_lines':True,'files':receipts,'mirroring':'NOT_VERIFIED'})
print(json.dumps({'status':'COMPLETE_LOCAL','exact_assertions':total,'fixed_constant_checks':4,'schema_fields':'PASS','files':len(receipts),'full_fei':'OPEN'}))
