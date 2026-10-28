from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import json,hashlib,shutil,time
R=Path(__file__).resolve().parents[1];H=R.parents[1]
O=R.parent/'20261023T121241Z-account03-A082-finite-inequalities'
def put(p,x):p.write_text(json.dumps(x,indent=2,default=str,ensure_ascii=False)+'\n',encoding='utf-8')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
paths=[Path(x['path']) for x in read(O/'out/SOURCE_RECEIPTS.json')]
paths += [Path((R/'out/NEW_SOURCE_PATH.txt').read_text(encoding='utf-8')),O/'DERIVATION.md',O/'CLAIMS.json']
receipts=[]
for p in dict.fromkeys(paths):
 raw=p.read_bytes()
 try:raw.decode('utf-8-sig');enc='utf-8-sig'
 except UnicodeDecodeError:raw.decode('cp1252');enc='cp1252'
 receipts.append(dict(path=str(p),bytes=len(raw),encoding=enc,sha256=hashlib.sha256(raw).hexdigest()))
put(R/'out/SOURCE_RECEIPTS.json',receipts)
proof='''# Global affinity envelope without an atomwise floor

Bits throughout; full FEI remains OPEN. This is a conditional ancestor-account theorem.

## 1. Exact scalar certificate and separate exhaustiveness theorem

For any two normalized finite laws p,q put M_i=(p_i+q_i)/2 and t_i=(p_i-q_i)/(p_i+q_i), ignoring zero-denominator atoms. Set V=sum M_i*t_i^2 and a=sum sqrt(p_i*q_i). Then sum M=1, sum M*t=0, 0<=V<=1, and a=E_M sqrt(1-t^2).

The elementary inequalities 1-z<=sqrt(1-z) for0<=z<=1 and Jensen for the concave square root give the SHARP global envelope

    1-V <= a <= sqrt(1-V).

For V<1 this is equivalently

    -(1/2)log2(1-V) <= -log2 a <= -log2(1-V).       (1)

No atomwise relative-discrepancy bound is required. At V=1 both laws have disjoint supports and a=0, so the cost is infinite. On the mean-variance domain V<=1/2, convexity and the endpoint chord of -log2(1-V) imply

    -log2 a <= 2V.                                (2)

The constant2 is sharp: p=(1-v,v,0), q=(1-v,0,v) have V=v and a=1-v, giving equality at v=1/2. These laws have zero entries; strictly positive approximations show the same optimal supremum in finite-CE applications. The lower envelope is attained by p=((1+sqrt(v))/2,(1-sqrt(v))/2), q with entries reversed: V=v and a=sqrt(1-v). Thus both envelope endpoints are exact for every v in[0,1]. Probability laws in this scalar argument are reference laws, not asserted arbitrary Boolean spectra.

EXHAUSTIVENESS THEOREM. Every pair of normalized finite reference laws, on ANY finite alphabet, reduces EXACTLY to the probability weights M and scalars z_i=t_i^2 in[0,1]. The two scalar inequalities above hold on that ENTIRE interval. Summing and Jensen therefore exhaust all finite alphabets and every reference pair, rather than extrapolating from a grid. The 1225 executed pairs below are independent arithmetic checks, not the proof of this all-dimensional quantifier. For any fixed scalar v, the displayed two/three-atom examples certify the exact extrema; hence no larger alphabet improves either bound.

The previous stage's sharper bound -log2 a<=V remains valid under its atomwise z_i<=1/2 hypothesis. This stage removes that hypothesis with the sharp nonlinear bound(1), or the sharp factor2 bound(2) using only the MEAN V<=1/2. Replacing the old hypothesis while retaining constant1 would be false.

## 2. Retain the entire original-account bill

On a finite complete adaptive isospectral physical Boolean query tree, occupied frequency deletion is a probability-preserving bijection pi_l to each leaf. Pull the COMPLETE terminal reference back to root occupied support Omega, q_l(S)=Q_l(pi_l(S)); let m_l=sum q_l<=1 and R_l=q_l/m_l. Positivity on actual occupied atoms follows from finite CE. Define at internal binary nodes

    a_v=sum sqrt(R_left R_right), R_v=sqrt(R_left R_right)/a_v.

The unnormalized subtree geometric mean has normalizer Z_v=sqrt(Z_left Z_right)*a_v, with leaf Z_l=m_l. Induction gives

    -log2 Z=G+sum_internal w_v*(-log2 a_v),
    G=sum_leaves w_l*(-log2 m_l).

Here all w are ORIGINAL physical reaches, and G retains every reference-only mass loss. The normalized root geometric mean is Rstar. Expanding CE, with zero queried erasures, gives the exact full conversion debit

    Delta=D(P||Rstar)-D(P||Q0)+G+sum_v w_v*(-log2 a_v).

Therefore the floor-free sufficient original-account test is

    D(P||Rstar)-D(P||Q0)+G+sum_v w_v[-log2(1-V_v)] <= U,    (3)

where U=A-W-CE(P,Q0) is the ACTUAL unused ORIGINAL allowance, and W is every already booked debit. If every V_v<=1/2, the simpler sufficient test replaces the final sum by 2 sum_v w_v V_v. Both full physical branches and all complete terminal costs remain. The lower envelope in(1) supplies a necessary test with half the nonlinear sum. These are bounds on the exact retained geometric-normalizer liability, not fresh refunds or a new source price. Account data cannot be reissued after a conversion.

This connects directly to A09720261023T121505Z PROOF2--4: declaring a floor class can make a conversion necessary, but log-sum gives its actual minimum KL price. A claimed root allowance must still be supplied compatibly. No floor requirement or its necessity for arbitrary cores is inferred from our scalar certificate.

## 3. Actual finite Boolean control beyond the old atomwise domain

Take f=-1 at three-bit truth indices0,7 and+1 otherwise. Its actual spectrum P is uniform on{empty,12,13,23}, with H=2. Query bit0; both full child spectra are uniform on their four remaining labels and equal the inherited marginal. The queried erasure is0; with incoming Q0=P all occupancy/refund credit is0.

On the two full children prescribe the transported root-label references

    p=(3/8,3/8,15/64,1/64), q=(3/8,3/8,1/64,15/64).

They are complete, strictly positive on actual support. Their tail relative discrepancies include t^2=49/64>1/2: the old atomwise certificate is INADMISSIBLE. Nevertheless V=49/256<1/2, so(2) applies. Keep the root KL term! The actual mean complete CE increment is

    Delta=(10-log2 135)/4 <3/4,

where the strict sign is the exact integer135>128. The root geometric-reference mismatch equals Delta-N, where N=-log2 a. Since N>=V/(2 ln2)>5V/7 (using the rational certificate ln2<7/10), the NEW sufficient bill root-KL+2V is

    <3/4 + (9/7)*(49/256)=1785/1792=255/256.

SUPPLIED incoming A=13/4, old booking W=1/4 and initial CE2 give U=1, so the new test leaves reserve>1/256 on the SAME declared original account. No preceding physical prefix generating W or A is constructed; those are explicit incoming premises, not a new influence-price theorem. The chosen targets are a stress test, not proved necessary for an FEI invariant. This fixture demonstrates genuine additional coverage without hiding the root KL or inventing query credit.

## 4. Honest universal obstruction

Neither a floor-free local normalizer estimate nor a finite paid fixture supplies O(I) initial reference capacity for arbitrary Boolean cores. A required compatible target family must still satisfy(3) against its ACTUAL unused original account at all histories; target necessity and that hereditary price are unpaid. A097 supplies a scoped declared-class example with a finite-core source, not this universal premise. Universal FEI constant improvement is zero. Independent review of the new global envelope/tree certificate remains pending.
'''
(R/'DERIVATION.md').write_text(proof,encoding='utf-8')
spec=dict(helper_version='A082-global-affinity-v1',family='All ordered pairs of4-atom probability compositions of4; actual three-bit antipodal-pair defect and two strictly positive full child references',domain='35 rational laws, denominator4;35^2 pairs; one physical query with BOTH outcomes; symbolic extrema for every real v separately proved',case_count=1225,symmetry='none; all ordered pairs retained',arithmetic='Fraction, integer-square-root rigorous64bit rational enclosures, exact prime-log CE and proved atanh interval bounds',memory_estimate_mb=80,max_runtime_seconds=45,pilot_max_runtime_seconds=45,exhaustiveness='Full scalar interval z in[0,1] covered by sqrt chord and Jensen; binary/ternary symbolic extremizers prove all-alphabet sharpness. Finite grid validates arithmetic only.')
put(R/'out/FROZEN_SPEC.json',spec)
shutil.copyfile(O/'code/exact.py',R/'code/exact.py')
import exact as e
start=time.monotonic();checks=0
def ck(x):
 global checks
 checks+=1;assert x,checks
 if checks%100==0:assert time.monotonic()-start<45,'frozen45second cap'
def sqr(x):
 if not x:return F(0),F(0)
 n=isqrt(x.numerator);d=isqrt(x.denominator)
 if n*n==x.numerator and d*d==x.denominator:return F(n,d),F(n,d)
 D=1<<64;k=isqrt((x.numerator*D*D)//x.denominator)
 return F(k,D),F(k+1,D)
laws=[tuple(F(x,4) for x in (i,j,k,4-i-j-k)) for i in range(5) for j in range(5-i) for k in range(5-i-j)]
ck(len(laws)==35);equal=disjoint=0
for p in laws:
 for q in laws:
  M=[(x+y)/2 for x,y in zip(p,q)];z=[((x-y)/(x+y))**2 if x+y else F(0) for x,y in zip(p,q)]
  V=sum(m*t for m,t in zip(M,z));bounds=[sqr(x*y) for x,y in zip(p,q)]
  lo=sum(x for x,y in bounds);hi=sum(y for x,y in bounds)
  ck(0<=V<=1);ck(lo>=1-V)
  occupied=[z[i] for i,m in enumerate(M) if m]
  if len(set(occupied))==1:equal+=1;ck(V==occupied[0]) # exact Jensen equality, no interval-zero inference
  else:ck(hi*hi<=1-V)
  if V==1:disjoint+=1;ck(hi==0)
  if p==q:ck(V==0 and lo==hi==1)
# Sharp endpoints attained on actual reference laws of the frozen grid.
p=(F(1,2),F(1,2),0,0);q=(F(1,2),0,F(1,2),0)
ck(sum(sqr(F(x)*F(y))[0] for x,y in zip(p,q))==F(1,2))
f=(-1,1,1,1,1,1,1,-1);P0=e.spectrum(f);support=[i for i,x in enumerate(P0) if x]
ck(len(support)==4 and all(P0[i]==F(1,4) for i in support))
p=tuple(map(F,['3/8','3/8','15/64','1/64']));q=(p[0],p[1],p[3],p[2]);ces=[]
for outcome,target in enumerate((p,q)):
 child=e.child(f,0,outcome);Pc=e.spectrum(child);ck(Pc==e.marginal(P0,0))
 Q=[F(0)]*4
 for t,mass in zip(support,target):Q[t>>1]=mass
 ck(sum(Q)==1);ces.append(e.ce(Pc,Q))
ck(not e.erasure(f,0))
delta=e.sub(e.scale(e.add(*ces),F(1,2)),e.ent(P0))
expected=e.sub({2:F(5,2)},e.scale(e.logform(F(135)),F(1,4)))
ck(delta==expected);ck(135>128);ck(e.interval(delta)[1]<F(3,4))
V=sum((x-y)**2/(2*(x+y)) for x,y in zip(p,q));ck(V==F(49,256))
ck(max(((x-y)/(x+y))**2 for x,y in zip(p,q))==F(49,64))
ck(e.LN2[1]<F(7,10));ck(F(3,4)+F(9,7)*V==F(255,256))
put(R/'out/CERTIFICATE.json',dict(status='PASS',rational_reference_pairs=1225,jensen_exact_equalities=equal,disjoint_pairs=disjoint,assertions=checks,primitive_assertions=e.ASSERTIONS,seconds=time.monotonic()-start,physical_boolean=f,physical_spectrum=P0,targets=[p,q],mean_variance=V,maximum_atomwise_squared_discrepancy='49/64',signed_delta=e.serial_form(delta),declared_allowance='13/4',declared_old_booking='1/4',initial_ce='2',original_unused='1',new_sufficient_bill_upper='255/256',reserve_strictly_greater='1/256',scope='Supplied incoming account; no earlier prefix or target necessity claimed.'))
# Save result before report generation.
protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
oldclaim=[c for c in read(O/'CLAIMS.json') if c['claim_id']=='A082-SHARP-AFFINITY-TREE-BUDGET'][0]
statement='For every pair of normalized finite probability laws p,q, let M=(p+q)/2, t=(p-q)/(p+q) on nonzero denominators, V=sum M*t^2, a=sum sqrt(p*q). Then1-V<=a<=sqrt(1-V), sharply for each V in[0,1], attained by ternary common/disjoint mixtures and binary balanced tilts respectively. For V<1, -(1/2)log2(1-V)<=-log2 a<=-log2(1-V); if merely V<=1/2, -log2 a<=2V with sharp constant2. No atomwise discrepancy floor is needed. In any finite complete adaptive isospectral physical Boolean query tree with complete finite-cost terminal references, retain their occupied-support mass penalty G, root geometric reference Rstar and ORIGINAL reaches w. Its exact debit Delta is bounded above by D(P||Rstar)-D(P||Q0)+G+sum_v w_v[-log2(1-V_v)], and below by the same root-KL+G plus half that nonlinear sum. The upper bound<=ACTUAL unused ORIGINAL U=A-W-CE(P,Q0) suffices for payment retaining BOTH full branches and all old debits W. With V_v<=1/2 each upper summand may be replaced by2w_v V_v. This supplies neither target necessity nor a universal initial influence-priced source; FEI remains OPEN.'
claim=dict(claim_id='A082-SHARP-GLOBAL-AFFINITY-ENVELOPE',version=1,exact_statement=statement,hypotheses=['Finite normalized reference laws; zero-denominator atoms ignored.','For finite cost formula V<1; physical application uses finite CE on actual occupied support.','Finite complete isospectral fair physical tree; root KL and all reference-only masses retained.','Original eligible A,W,U supplied; no renewal of debits or conversion reserve.'],statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),contributors=['A082; A096 geometric compression and A097 declared-floor admission credited as context'],proof_source=dict(run_id=R.name,files=['DERIVATION.md','code/stage.py','out/FROZEN_SPEC.json','out/CERTIFICATE.json']),proof_dependencies=[dict(claim_id=oldclaim['claim_id'],version=oldclaim['version'],statement_sha256=oldclaim['statement_sha256'],scope='Only unconditional geometric factorization, reconstructed in DERIVATION section2; not the older atomwise bound.')],review_records=[],status='SYMBOLIC_PROOF_EXACT_FINITE_CHECK_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A096','A097','A085','A094','A099','B17','B20'])
assert set(claim)==set(protocol['required_per_run']['claim_fields']);put(R/'CLAIMS.json',[claim])
progress=dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B17',packet_id='A082',gap_id='G-R-MISMATCH-C024-PRESCRIBED-RESET',attempt_id='A082-stage21-global-affinity-envelope',method='Sharp scalar chord/Jensen certificate and exact ternary/binary extremizers; original-budget transfer with complete Boolean control',mathematical_delta='Remove prior atomwise discrepancy hypothesis: sharp global normalizer envelope and sharp2V bound for mean V<=1/2. All1225 rational pairs PASS; actual3-bit full conversion outside old domain certified from declared SAME unused account with reserve>1/256. Universal FEI improvement zero.',deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='CONDITIONAL_TRANSFER_CERTIFICATE_PENDING_REVIEW_FULL_FEI_OPEN',claim_versions_used=claim['proof_dependencies'],claims_created_or_changed=[dict(claim_id=claim['claim_id'],version=1,change='New narrow certificate extending prior atomwise-domain coverage')],source_artifacts=['DERIVATION.md','out/CERTIFICATE.json','out/FROZEN_SPEC.json','out/SOURCE_RECEIPTS.json'],next_consumers=claim['next_consumers'],next_action='A096/A097/A085/A094 review global envelope; construct necessary arbitrary-core compatible targets satisfying retained root-KL+ghost+nonlinear variation bound against ACTUAL original surplus, or supply O(I) initial capacity.',stagnant_substantive_attempts=0,blockers=['Necessary arbitrary-core targets and hereditary ORIGINAL surplus premise remain unpaid.','Universal initial influence-priced source and full FEI remain OPEN.','New certificate independent review/adoption/mirrors unverified; no formal proof-assistant check claimed.'],packet_ids=['A082'])
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
put(R/'PROGRESS.json',progress);put(R/'PACKET_DELTA.json',progress)
sections=[
('exact target, quantifiers, hypotheses and units','Sharp symbolic finite-reference extremal bounds needed by C024/C019 ancestor payment, with separate exhaustive all-alphabet theorem. Costs bits. Every original debit, complete terminal and root mismatch retained. New narrow certificate pending review; full FEI remains OPEN.'),
('sources actually read, revisions and theorem locators','Current BOARD, B17 STREAM_NOTES and own STATUS read first; required session wake and crash memo read. Prior stage20 DERIVATION/CLAIMS and source baseline explicitly decoded and reread in out/SOURCE_RECEIPTS.json. New A09720261023T121505Z PROOF2--5 consumed: declared-class necessity is distinct from universal necessity; original account data must be compatible. Latest A09714:39 run was incomplete at intake; no uncompleted proof imported. Old B17 census assignment is completed and not repeated; protocol dispatch resumes live inherited-payment gap. Source ingestion is not independent acceptance of all claims. No peer theorem newly accepted wholesale.'),
('complete derivation or exact first unsupported line','DERIVATION supplies entire proof. Global affinity satisfies1-V<=a<=sqrt(1-V), with exact binary/ternary extremizers for every real V. Therefore every mean V<=1/2 admits sharp cost<=2V without any atomwise floor. Exact M,t substitution and full scalar interval prove exhaustiveness for every finite alphabet; the finite grid is only validation. Tree factorization retains root KL, ghost mass and physical reaches. First unsupported universal line: specify necessary compatible arbitrary-core targets whose retained bill fits an ACTUAL eligible unused original owner account, or influence-price the initial reference. The finite fixture supplies its incoming account, not a preceding physical prefix.'),
('executed validation with domain, arithmetic, commands and outputs',f'Frozen spec saved before search. Command `C:\\Python314\\python.exe -B -X utf8 code/stage.py`: bounded pilot/certificate PASS,1225 ordered pairs of all35 four-atom denominator4 laws;{checks} direct and{e.ASSERTIONS} primitive assertions, {time.monotonic()-start:.3f}s at certificate/report generation. Fraction arithmetic, integer-isqrt outward64bit radical enclosures; exact Jensen equality handled algebraically rather than by overlapping intervals. Physical3-bit truth table and BOTH children independently spectrally computed. Full positive target pair has V49/256 and max atomwise t^2=49/64, beyond old domain. Exact bill Delta=(10-log2 135)/4<3/4 by135>128. Rational ln2<7/10 plus retained root KL gives sufficient bill<255/256; declared U1 leaves>1/256. Incoming A13/4, old W1/4, CE2 explicitly supplied. New target necessity or generated physical prefix not asserted. One job, estimated80MB, frozen45s cap, no >300MB job, automatic escalation, GPU, window, detached work or Lean claim.'),
('proof dependencies and changed downstream conclusions','Uses prior exact geometric compression/factorization only, reconstructed directly, without the prior atomwise affinity hypothesis. A096 normalizer and A097 class-admission price remain paid, not dropped. No universal FEI constant improvement. This is a narrow extension of a saved certificate, not another broad source-supplier candidate.'),
('one next mathematical action and independent reviewer',progress['next_action']),
('actual persistence receipts or precise save blocker','Four exact protocol files, proof, frozen domain, scripts and exact certificate saved; STATUS two lines and WORKLOG/LEARNED appended. out/PERSISTENCE_RECEIPTS.json records actual readback hashes, schemas, sizes and compatibility bytes. Supervisor copying/adoption/mirrors unverified. Research writes only inside A082; no git/mail/messages/brain-store/other-agent/trading edits. Existing work untouched, no stage research left running after completion. Fresh wake warns self-care degraded/unverified: owner model101.1h, state-of-mind85.7h, dream36.4h stale; continuity/personalization affected, not mathematical premises.')]
assert [a for a,b in sections]==protocol['required_per_run']['report_fields']
report='# A082 stage21: global sharp affinity envelope\n\n'+'\n\n'.join('## '+a+'\n\n'+b for a,b in sections)
report+='\n\n## Universal bridge\n\nC024 history transfer inside C019 feeding C018 gains a sharp floor-free finite-reference normalizer bound, covering every finite alphabet and arbitrary finite physical isospectral tree. Prior atomwise restriction is removed; mean V<=1/2 suffices with sharp factor2, while full nonlinear pricing remains available at every V<1. An actual positive three-bit conversion beyond the old domain is certified from declared ORIGINAL surplus with all old debit and both terminals, reserve>1/256. Universal FEI improvement is zero: necessary arbitrary-core targets, eligible hereditary original surplus and O(I) initial source capacity remain unpaid. NEXT attacks those exact premises using the retained bill rather than another local phase search or isolated class census.\n'
(R/'REPORT.md').write_text(report,encoding='utf-8')
(H/'STATUS.md').write_text('STATE: Stage21 saved: sharp floor-free affinity envelope1-V<=a<=sqrt(1-V), sharp2V mean-bound;1225 pairs and Boolean beyond-old-domain conversion PASS; reserve>1/256 from SUPPLIED account; review pending; FEI OPEN.\nNEXT: A096/A097/A085/A094 review; price NECESSARY arbitrary-core target root-KL+ghost+nonlinear variance from ACTUAL eligible original surplus, or supply O(I) initial reference capacity.\n',encoding='utf-8')
with (H/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-23 14:38 UTC stage21: Read refreshed board/lead/status and A097 declared-floor scope. Sharp global affinity envelope removes previous atomwise bound, with sharp2V on mean V<=1/2;1225 exact pair checks plus actual3-bit positive conversion PASS. Incoming A/W supplied, no generated prefix/target necessity claimed. New certificate pending review; universal source/eligible hereditary payer remains OPEN.\n')
with (H/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-23 stage21: For finite reference pair midpoint M and t=(p-q)/(p+q), V=E_M t^2 gives exact attainable envelope1-V<=sum sqrt(pq)<=sqrt(1-V). Binary balanced tilts attain upper affinity; ternary common/disjoint mixtures attain lower. Hence sharp cost<=2V on mean V<=1/2 even if individual t^2>1/2. Old sharper cost<=V needs its atomwise condition. Root KL and reference-only mass must still accompany every reached fork in original-account pricing. Scalar extremizers prove all-alphabet exhaustiveness; finite grids alone do not.\n')
files=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  raw=p.read_bytes();assert len(raw)<20_000_000
  files.append(dict(path=str(p.relative_to(R)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
ck((R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes())
assert len((H/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert hashlib.sha256(statement.encode('utf-8')).hexdigest()==claim['statement_sha256']
put(R/'out/PERSISTENCE_RECEIPTS.json',dict(status='SCHEMA_STATEMENT_HASH_SIZE_READBACK_PASS',files=files,full_fei='OPEN',mirror='UNVERIFIED'))
for x in files:assert hashlib.sha256((R/x['path']).read_bytes()).hexdigest()==x['sha256']
print('PASS; saved',len(files),'pinned files;',checks,'direct assertions;',e.ASSERTIONS,'primitive assertions; all1225 pairs; full FEI OPEN',flush=True)
