from pathlib import Path
import json, hashlib
from datetime import datetime, timezone

R=Path(__file__).resolve().parents[1]
B=R.parents[1]
ROOT=B.parents[1]
def read(p): return Path(p).read_text(encoding='utf-8')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,s): Path(p).write_text(s,encoding='utf-8')
def dump(p,x): write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
protocol=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
P=json.loads(read(protocol))
prior=B/'runs/20261023T110208Z-account03-A020-selector-boundary-tests'
a16=ROOT/'agents/A016/runs/20261023T112921Z-account03-A016-addressing-benchmark'
a18=ROOT/'agents/A018/runs/20261023T121958Z-account03-A018-shared-data-collision-law'
helper=B/'runs/20261022T231605Z-account03-A020-selector-boundary-tests/code/check.py'
check=json.loads(read(R/'out/CHECK.json'))
pilot=json.loads(read(R/'out/PILOT.json'))
assert check['status']==pilot['status']=='PASS'
assert check['assertions']==6808 and len(check['mixed'])==594
assert check['literal'][0]['signed_frontiers']==128
assert check['literal'][0]['actual_signed_physical_branches']==1458

report=r'''# A020 stage10: predetermined mixed exposures on an interacting source

Full FEI remains OPEN. For the original reference and old debit, the full physical frontier obtained by querying q and ANY predetermined subset of padding/source coordinates has expected reserve greater than107/64 under the projected-entropy hypothesis below. The explicit source uses overlapping point defects sharing a real physical bit, not independent factors masquerading as shared data. A016's essential-terminal obstruction and its complete-tree repair are independently reconstructed. An outcome-dependent choice of exposed set or stopping time remains outside the new theorem.

## exact target, quantifiers, hypotheses and units

Bits are uniform independent0/1; chi_z=(-1)^z; entropy and complete code costs use log base2. Let G be any finite Boolean source with original mean0<=mu<=1/2. For each predetermined erased source-coordinate set S write R_S for the frequency marginal of the ORIGINAL squared Fourier law and I_rem(S) for the sum of ORIGINAL influences of unqueried source coordinates. Assume H(R_S)<=4I_rem(S) for each set to which the result is applied (including empty S for root eligibility).

Fix k>=5, rho=2^-k, A=point_k(v)(1-G)/2, p=rho(1-mu)/2. Put h=chi_u off A and chi_q on A. Let s2=[-1,1,1,1], with mean1/2 and flat squared spectrum1/4, on two fresh mask bits. Let F=1 at a fresh gate0 and hs2 at gate1. The ORIGINAL reference is Q_h=(P_h+point_q)/2 and Q_F(e,T)=[Q_h(T_core)P_s2(T_mask)+point_empty(T)]/4 at EACH gate frequency e. Every subsequent reference is its exact frequency marginal; no reference is reset.

Query q, then any predetermined subset of the padding and source coordinates, keeping u,gate,mask unqueried and ALL physical outcomes. For EACH q sign separately, E[4I(F_leaf)-CE(P_leaf,Q_projected)]-U>107/64. Here U=L_q+E is the original already booked insertion debit, defined below; it is not rebooked or replaced by an upper bound. The original root is rate4 eligible with margin>19/8. Source influences are retired once.

An unconditional interacting realization is G=product of j>=2 disjoint copies of E(a,b,c,d,e)=g3(a,b,c)g3(a,d,e), where g3 is-1 only at000. Inside E the two tests share the SAME physical a; their Fourier interference is retained. Predetermined subsets may differ between independent E blocks and may mix padding and source bits. A set may depend on the already observed q sign, since the result holds for each sign; it may not depend on outcomes of the subsequently exposed padding/source bits. No pointwise terminal eligibility or adaptive stopping theorem is claimed.

## sources actually read, revisions and theorem locators

Read current BOARD at invocation, own STATUS and B04 STREAM_NOTES v2 (2026-10-11), including the lead's exact-boundary adaptive stopping obligation. Read A016 run20261023T112921Z REPORT derivation and claims: A016-REVIEW-A020-ALL-ADAPTIVE-TENSOR-CLEANUP@1 accepts our prior tensor theorem; A016-ESSENTIAL-MIXED-PADDING-OBSTRUCTION-AND-AVERAGED-REPAIR@1 identifies the essential mixed terminal and expected-tree repair. Read A018 run20261023T121958Z REPORT derivation and claims, especially A018-DENSITY-ONLY-SOURCE-OWNERSHIP@1. Its source-owner warning is consumed here; its numerical constants belong to a DIFFERENT one-balanced hierarchy and are not transplanted. Own stage9 full proof and stage7 exact helper were read/carried forward. Source bytes and statement hashes are saved in out/SOURCE_RECEIPTS.json.

The required initial campaign documents, registries, protocol and papers were read in previous stages of this packet; no new paper theorem or novelty priority is claimed. The full protocol was re-read this stage; revision2026-10-11-execution-v2 supplies the exact output fields. The owner's extended deadline2026-10-23 14:49UTC supersedes the old protocol endpoint. The current-session wake reported owner model99.8h, state of mind84.4h and dream35.1h stale: brain self-care is degraded/unverified, affecting freshness of owner/state/dream context, not the mathematical certificate. Those notes are not proof inputs. The compute snapshot timestamp13:57:59 LOCAL was stale at inspection and is not evidence of present admission or governor health. No shared process was restarted or stopped.

## complete derivation or exact first unsupported line

1. Original source, interference, and debit. Direct32-point Walsh/edge calculations for E give mean5/8 and physical influence vector(3/8,1/4,1/4,1/4,1/4), hence I(E)=11/8. The shared-bit influence3/8 would be lost by treating its g3 factors as disjoint. For j blocks, mu=(5/8)^j<=1/2. Every remaining source coordinate has original spectral inclusion probability at least1/4. Thus H(R_S)<=number of remaining coordinates<=4I_rem(S), regardless of correlations inside each projected E law. Independence is used ONLY across genuinely disjoint E blocks. This proves the source hypothesis in all dimensions of the stated family.

The old debit is
L_q=log((9+p^2)/8)/2+(p^2/8)log((9+p^2)/(1+p^2)),
E=(1+(p/2)^2)[1-h2((1+p/2)^2/(2(1+(p/2)^2)))]/2, U=L_q+E.
It satisfies0<=U<5/8: Bernoulli KL bounded by chi-square and ln2>1/2 give0<=E<=p^2, while L_q<1/2+p^2/2 and p<=1/64. Actual U remains in every certified profile. At k128, intersection with the proved0<=E<=p^2 enclosure avoids rounding a tiny positive debit to zero; this is not a debit reset.

2. Exact averaged law for a predetermined physical frontier. Suppose k' padding bits remain, rho'=2^-k', and R=R_S for the erased source set. Let L_k' replicate its seed measure equally over the two u frequencies and all2^k' padding frequencies, multiplying total mass by2^(k'+1). Averaging the TRUE restricted squared spectra over every physical outcome gives the complete core law

Pbar_c=(1-2p)point_u+(rho*rho'/4)L_k'[R+(1-2mu)point_empty].

To derive this, Fourier expand h=(1-A)chi_u+Achi_q, add coincident coefficient contributions, square, then use the exact identity that averaging both restrictions marginalizes squared Fourier mass over the queried frequency. Before erasure the q sector and u sector are disjoint, so querying q merely relabels its spectrum; this is true for either q sign. Further predetermined erasures marginalize the padding/source frequencies. The principal/rare split displayed above has rare mass2p. No conditional restriction law has been substituted for R. The inherited core reference is EXACTLY Qbar_c=(Pbar_c+point_empty)/2, because the ORIGINAL point_q projects toempty. Both measures have total massone.

The actual averaged full data law is(Pbar_c P_s2+point_empty)/2. Gate means/interference are averaged as the original signed mean sigma*p/2 of hs2, not as sqrt(Pbar_c(empty))/2. The latter substitution would discard physical interference and give the wrong influence. The code is uniform in gate frequency, so its expected complete cost depends linearly on the displayed full data marginal.

3. Complete coding bound and exact influence. The normalized rare seed mixture is [R+(1-2mu)point_empty]/[2(1-mu)]. It is positive because mu<=1/2. Entropy of its latent mixture is at most1+H(R)/[2(1-mu)]. Complete principal/rare coding therefore gives
H(Pbar_c)<=h2(2p)+2p(k'+2)+(rho/2)H(R).

Since Qbar_c>=Pbar_c/2, CE(Pbar_c,Qbar_c)<=H(Pbar_c)+1. Coding the complete constant/nonconstant data mixture under its supplied reference and the uniform gate gives
E CE_F<=CE(Pbar_c,Qbar_c)/2+3<=H(Pbar_c)/2+7/2.

These are latent-mixture upper bounds for entire normalized laws; no row or slice was discarded. Direct physical edge averaging gives, for q sign sigma in{-1,+1},
E[4I_F | sigma]=6+2(k'-1)p+rho I_rem(S)-sigma*p.
For clarity, the contributions are: u gives2-2p, remaining padding gives2k'p, source givesrho I_rem, two mask coordinates together give2, and gate gives2-sigma*p. Conditional event probabilities and conditional source influences average to their ORIGINAL values because the exposed set is predetermined. This also shows exactly where an outcome-dependent choice would invalidate the argument.

Subtracting complete cost and the same U yields
E[4I-CE]-U >=5/2+(k'-4-sigma)p-h2(2p)/2
 +rho[I_rem-H(R)/4]-U >107/64.

Indeed k'>=0, sigma<=1, p<=1/64, h2(2p)<=h2(1/32)<1/4 and U<5/8, so the conservative lower bound is5/2-5/64-1/8-5/8=107/64. Equality p=1/64 at mu0,k5 is allowed: strict reserve slack comes from the strict entropy/debit bounds. The entropy endpoint is an integer certificate31^31>2^152. This is a per-sign average over a FULL physical partition, not a statement about its individual leaves.

The unqueried root h is balanced; its Fourier law has the same atom magnitudes as Pbar_c before any padding/source erasure. With c=CE(P_h,Q_h)<=H(P_h)+1, the complete root code is c/2+3, and4I_root=6+2kp+rho I(G). The same entropy bound gives root margin at least5/2+(k-2)p-h2(2p)/2+rho[I(G)-H(P_G)/4]>19/8. Thus the starting source is actually eligible; no bad root is silently admitted.

4. Original-owner ledger and adaptive gap. After q, the rate4 influence retired by the predetermined padding/source exposures is exactly
4Pi=2(k-k')p+rho[I(G)-I_rem(S)].
For each actual physical query, CE_parent=average CE_child+L_i, with L_i=sum P(e,T)log[Q_marg(T)/Q(e,T)]>=0. Nonnegativity follows from Q_marg>=Q atomwise on the paired frequencies. Therefore E W_new=W_q-4Pi+sum(reach*L_i), with the ORIGINAL U and reference. CE release is a credit; influence already committed to the original supplier is retired ONCE, never added as a second unused bank. This consumes A018's ownership objection without importing constants from its other hierarchy.

First unsupported line: replacing this predetermined-set expectation by the expectation at an outcome-dependent chosen set or stopping frontier. Uniform lower bounds on the mean at each fixed set do not control an adaptive selection of rare negative terminals. The projected-entropy hypothesis also needs a universal low-influence supplier for arbitrary Boolean sources. Neither obligation is solved here.

5. Independent reconstruction of A016's full stated mixed experiment. Use its original m4 tensor source, mu=81/256 and p=rho(1-mu)/2, k>=5. Query q and three first seed bits, take their all1 history and clean the six now irrelevant seed coordinates. One live g3 remains. After all padding bits0, its actual full Boolean terminal has seven coordinates and influence vector
(7/16,1/16,1/16,1/16,1/4,1/4,1/2-sigma/32).
All seven are essential. Hence4I=13/2-sigma/8, equal51/8 or53/8. With u frequency a and live seed frequency T, the original projected core reference is
Q_c(a,T)=rho[P_g3(T)+(1-2mu)point_empty(T)]/8
 +(1-2p)point_u(a,T)/2+point_empty(a,T)/2.
It is normalized. Direct128-point tables separately check both true terminals against this full reference.

Every full atom with nonempty live-seed frequency has true mass1/1024 and reference massrho/2048. Their total true mass7/64 has selected code cost EXACTLY7(k+11)/64. Remaining rows have positive cost, so at k64 both W are STRICTLY below53/8-525/64=-101/64; both tend to minus infinity. This agrees with the source version unchanged. The true terminal functions stay fixed, so this is a code obstruction, not a Boolean FEI counterfamily. Cleanup cannot repair it: all surviving coordinates are essential.

Outside the selected mass, reference atoms are at least31/1024>1/64, giving
7(k+11)/64<=C_k<7(k+11)/64+342/64.
Condition on a q sign and its all1 seed history. Its active padding event has probabilityrho, and the reach-weighted positive deficit D_k=rho(C_k+U-4I_active)_+ obeys
D_k<=rho(7k+51)/64.
Determining this padding event spends ACTUAL influence J_pad=k*rho/16: depth d has physical reach2^-d and queried influence2^d*rho/16. Thus D_k/J_pad<=7/4+51/(4k)<=43/10<5; the complete-cost bounds show the ratio tends to7/4. Outer reaches multiply both sides equally.

Before padding, the same distinguished cleaned tensor state has W_pre>5/4 by the separately reconstructed first-bit result in our stage9 report. Follow the padding decision tree and clean irrelevant coordinates on off-event leaves. The exact signed transition gives
E W_after=W_pre-4J_pad+sum(reach*L_i)>5/4-k*rho/4>=155/128,
since k*2^-k<=5/32. No influence is recredited. Run this subtree only on the distinguished all1 tensor history and stop at the other seven cleaned tensor outcomes. The accepted all-adaptive tensor theorem pays each of those siblings by>5/8. Both q signs, all seed/padding outcomes and cleanup reaches remain. Hence the whole stated mixed policy has expected reserve>5/8. This independently reconstructs the obstruction, weighted-liability bound and complete-policy repair without modifying the source claim. It does not assert a general adaptive mixed theorem.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded searches; LITERAL_SCOPE_CLARIFICATION.json fixed the descriptive count to128 signed frontiers before the pilot. Full compressed domain: k5,8; j2,3,8; remaining padding0,1,k; each of32 uniform per-block source masks plus one alternating1/30 pattern. This is594 profiles, each with both q signs, exact old U, complete cost and influence retired once. All32 projected E laws are certified separately. The proof, rather than finite coverage, establishes arbitrary k>=5,j>=2 and arbitrary predetermined per-block subsets.

Literal validation uses original11-coordinate Boolean F at k1,j1, outside the theorem's mu/k hypotheses. It explicitly retains every physical outcome of each of128 signed frontiers (all32 source masks, both padding choices, both q signs), totaling1458 actual signed branches across these overlapping frontiers. Integer Walsh laws are compared to exact projection; direct physical edges to averaged influence; original Q to its full normalized marginal; and entropy/CE compression to the literal complete cost. These overlapping frontiers are NOT summed as one stopping partition. Independent A016 terminal checks use k5,8,16,32,64,128, both signs, seven essential influences and all128 actual truth-table entries.

The checker imports only the hash-bound read-only A020 stage7 integer-Walsh/Fraction/log helper, with bytecode disabled. Logs have100-bit outward enclosures,48 atanh terms and tail2z^97/[97(1-z^2)] after range reduction to[1,2), with separately enclosed ln2. Saved dyadic endpoints are rounded outward. Interval overlap checks numerical consistency, while exact probability identities and the analytic derivation prove equality; no floating-point sign is used. Each k/j batch is saved immediately.

Pilot: `python -X utf8 code/check.py --pilot` PASS111 assertions,3 profiles,4 signed frontiers,one A016 width,2.1936465seconds. Full: `python -X utf8 code/check.py` PASS6808 assertions,594 profiles,128 signed frontiers,six A016 widths,24.7109671seconds. out/PILOT.json and out/CHECK.json preserve all outputs. No failed assertion occurred. Frozen memory estimate125MB is below the300MB memok threshold; no job requiring admission was started. No GPU, window, detached job, compiler, automatic dimension increase or other-agent mutation occurred. No formal proof-assistant certificate is claimed.

## proof dependencies and changed downstream conclusions

The new theorem depends on the displayed original family/reference/debit algebra, exact physical marginalization, latent-mixture coding, and its explicit projected-entropy hypothesis. The E-block realization proves that hypothesis by a dimension/inclusion bound; it does not assume full FEI or independent overlapping factors. A016's acceptance of our prior tensor-only theorem is recorded with its original hash. Our independent review of A016's new version uses the unchanged first-bit/all-tensor theorem only for the specified unqueried-padding siblings; it supplies no substantive repair. The source under review is identified separately from proof dependencies, avoiding circular acceptance.

This stage replaces the failed pointwise mixed extension with a stronger fixed-frontier average on an actually interacting source. It preserves A016's negative essential terminals and A018's original-owner objection. There are two claim records: one new locally proved theorem pending independent review and one independent reconstruction of A016's unchanged stated package. No review or downstream use of the new theorem is presumed; no full FEI proof or counterexample is claimed.

## one next mathematical action and independent reviewer

Test outcome-dependent stopping on the SAME overlapping-E source with the SAME original Q/U: derive the signed continuation or an explicit rare-history failure while retaining all siblings and charging every queried physical coordinate once. A fixed-set average must not be substituted at a random selected set. A016/A019 should independently reconstruct the projected-law bound and both physical gate profiles; A018/A090/A091/A094 should challenge adaptive source ownership. This is a source-bound handoff only; no external message is sent.

## actual persistence receipts or precise save blocker

The four protocol files, both frozen specifications, checker/finalizer, pilot/full output and source receipts are local to this A020 run. STATUS has exactly two lines; WORKLOG is appended once and LEARNED records the general projected-entropy contract, shared-bit realization and adaptive gap. out/PERSISTENCE_RECEIPTS.json validates exact schemas, canonical statement hashes, identical PROGRESS/PACKET_DELTA and every run file's SHA256/size; a separate final readback checks the actual bytes. Every file is below20MB. Local artifact completion is distinct from pending independent review, supervisor adoption and remote mirror verification. No worker git, research-brain write or supervisor-copy receipt is claimed. Brain self-care remains degraded/unverified for stale owner/state/dream context.

## Universal bridge

This stage moves C019 stopping-tree payment and C024 history transfer from independent tensor cleanup to every PREDETERMINED mixed padding/source frontier of an explicit overlapping-bit source, with expected original-account reserve>107/64 after the old debit and actual root margin>19/8. It also independently confirms why pointwise mixed eligibility is impossible: A016's seven-essential-coordinate leaves have unbounded negative inherited-code reserve, though its full stated policy is paid. What remains is an outcome-dependent stopping rule funded from the original owner, plus a universal projected-entropy or equivalent low-influence supplier. NEXT attacks exactly the adaptation step on the same interacting source; that is the missing operation between a fixed-frontier average and the lead's universal boundary-payment tree, rather than another isolated selector class estimate.
'''
write(R/'REPORT.md',report)

def source_claim(path, cid):
 return next(x for x in json.loads(read(path/'CLAIMS.json')) if x['claim_id']==cid)
tensor=source_claim(prior,'A020-ALL-ADAPTIVE-TENSOR-CLEANUP')
first=source_claim(prior,'A020-REVIEW-A016-ALL-FIRST-BIT-CLEANUP')
mixed=source_claim(a16,'A016-ESSENTIAL-MIXED-PADDING-OBSTRUCTION-AND-AVERAGED-REPAIR')
accepted=source_claim(a16,'A016-REVIEW-A020-ALL-ADAPTIVE-TENSOR-CLEANUP')
owner=source_claim(a18,'A018-DENSITY-ONLY-SOURCE-OWNERSHIP')
def ident(c): return {k:c[k] for k in ['claim_id','version','statement_sha256']}
def claim(cid,statement,hyp,**extra):
 c=dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=hyp,
        statement_sha256=hashlib.sha256(json.dumps(dict(exact_statement=statement,hypotheses=hyp),sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')).hexdigest(),
        contributors=['A020'],proof_source=['REPORT.md','code/check.py','out/CHECK.json'],
        proof_dependencies=[],review_records=[],status='PROVED_LOCALLY_REVIEW_PENDING',
        supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A016','A018','A019','A090','A091','A094'])
 c.update(extra);return c
c1=claim('A020-PREDETERMINED-MIXED-EXPOSURE-AVERAGED-RESERVE',
 'For the supplied original Boolean family, reference Q and one original debit U, querying q followed by any predetermined subset of padding and source coordinates leaves, for each q sign, full physical-frontier expected reserve E[4I-CE]-U>107/64. Original root margin is>19/8 and source influence is retired exactly once. The projected-entropy hypothesis holds for every subset of G equal to a product of j>=2 disjoint overlapping-bit blocks E(a,b,c,d,e)=g3(a,b,c)g3(a,d,e); no independence is assumed between the two factors sharing a. This does not certify individual terminals or outcome-dependent exposure/stopping.',
 ['All costs use base2 and uniform physical bits; k>=5, rho=2^-k, 0<=mu=E G<=1/2, A=point_k(1-G)/2, p=rho(1-mu)/2, h=chi_u off A and chi_q on A, F=1 at gate0 and hs2 at gate1, s2=[-1,1,1,1] on fresh bits.',
  'Q_h=(P_h+point_q)/2, Q_F(e,T)=(Q_h(T_core)P_s2(T_mask)+point_empty(T))/4 at each gate frequency; all later codes are exact original frequency marginals. U=L_q+E is the single exact old debit defined in REPORT step1.',
  'For each applied predetermined source subset S, H(R_S)<=4I_rem(S), where R_S is the original spectral marginal and I_rem is the original remaining physical influence; include empty S for root eligibility.',
  'The post-q exposed subset may depend on q sign but not on subsequent padding/source outcomes. Keep all outcomes and leave u, mask and gate unqueried.'])
c2=claim('A020-REVIEW-A016-ESSENTIAL-MIXED-OBSTRUCTION',
 'Independent reconstruction holds for unchanged A016-ESSENTIAL-MIXED-PADDING-OBSTRUCTION-AND-AVERAGED-REPAIR@1: its original m4,k>=5 source has a mixed terminal with seven essential coordinates,4I=51/8 or53/8 and selected code cost7(k+11)/64. Both old-Q/U reserves at k64 are<-101/64 and diverge negatively with k. Conditional reach-weighted active-leaf deficit is<5 times actual padding influence k*2^-k/16, with ratio tending to7/4. Its full distinguished padding subtree has expected reserve>155/128; its complete stated mixed policy has expected reserve>5/8. No adaptive universal or pointwise mixed eligibility claim follows.',
 ['Exactly the original source, reference, old U, stated distinguished three-first-bits-all1/cleanup history and full physical padding policy from the reviewed source version; all siblings and both q signs retained.',
  'The other seven completed tensor histories use the unchanged accepted all-adaptive tensor theorem; the distinguished pre-padding state uses the separately reconstructed first-bit bound>5/4.'],
 status='INDEPENDENT_RECONSTRUCTION_HOLDS',
 proof_dependencies=[ident(tensor),ident(first)],
 review_records=[dict(reviewer='A020',source_under_review=ident(mixed),conclusion='HOLDS_UNCHANGED_FULL_STATED_SCOPE',method='Separate128-point terminal Walsh/edge reconstruction; exact normalized original reference; analytic complete-cost and signed physical-tree ledger.',substantive_repair=False)])
claims=[c1,c2];dump(R/'CLAIMS.json',claims)
paths=[protocol,ROOT/'BOARD.md',ROOT/'claude/B04/STREAM_NOTES.md',prior/'REPORT.md',prior/'CLAIMS.json',helper,a16/'REPORT.md',a16/'CLAIMS.json',a18/'REPORT.md',a18/'CLAIMS.json']
dump(R/'out/SOURCE_RECEIPTS.json',dict(files=[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size) for p in paths],
 claim_versions=dict(prior_tensor=ident(tensor),prior_first_bit_review=ident(first),A016_reviewed=ident(mixed),A016_acceptance_of_prior_tensor=ident(accepted),A018_ownership_lesson_only=ident(owner)),
 notes='Source versions are read-only; numerical A018 constants are not proof inputs; latest BOARD hash records the read snapshot bytes at finalization.'))
progress=dict(protocol_revision=P['revision'],run_id=R.name,stream='B04',packet_id='A020',gap_id='G-LOWSEL-COLLISION-SAME-REFERENCE-HISTORY-BANK',
 attempt_id='A020-stage10-predetermined-mixed-interacting-frontier',method='Original frequency marginal averaged over all physical outcomes; projected-entropy mixture bound; shared-bit exact Walsh; independent essential-terminal reconstruction.',
 mathematical_delta='Locally proved per-sign expected reserve>107/64 for predetermined mixed padding/source exposures under H(R)<=4I_rem; overlapping-bit E-block realization; original root margin>19/8. Independently reconstructed A016 mixed obstruction, weighted liability and full stated policy. Adaptive stopping and universal low-influence supplier remain open.',
 deliverable_status='COMPLETE_LOCAL_READBACK_PENDING_SUPERVISOR_ADOPTION',mathematical_status='SCOPED_THEOREM_PROVED_LOCALLY_REVIEW_PENDING; A016_SOURCE_INDEPENDENTLY_RECONSTRUCTED; FULL_FEI_OPEN',
 claim_versions_used=[dict(**ident(tensor),use='A016 mixed-policy unchanged siblings'),dict(**ident(first),use='distinguished pre-padding reserve'),dict(**ident(mixed),use='source independently reviewed'),dict(**ident(accepted),use='downstream acceptance of prior tensor theorem'),dict(**ident(owner),use='ownership objection consumed; different-family constants not transplanted')],
 claims_created_or_changed=[ident(c) for c in claims],source_artifacts=[str(p) for p in paths],next_consumers=['A016','A018','A019','A090','A091','A094'],
 next_action='Derive or refute expected signed continuation for outcome-dependent stopping on the same overlapping-E source, retaining original Q/U, all siblings and original source ownership; do not substitute a fixed-set average at a random chosen set.',
 stagnant_substantive_attempts=0,blockers=['Universal adaptive boundary-payment bridge unpaid.','Universal initial/projected-entropy supplier for arbitrary low-influence Boolean cores unpaid.','New theorem awaits independent review; supervisor mirror/adoption not verified.','Brain self-care context stale/unverified; stale governor snapshot not used for resource admission.'],packet_ids=['A020'])
dump(R/'PROGRESS.json',progress);write(R/'PACKET_DELTA.json',read(R/'PROGRESS.json'))
write(B/'STATUS.md','STATE: A020 stage10 COMPLETE locally: predetermined mixed padding/shared-source frontiers have expected SAME-Q/U reserve>107/64; A016 essential-terminal obstruction and full stated repair independently hold; FEI OPEN.\nNEXT: Test outcome-dependent stopping on the SAME overlapping-E source with original-owner signed ledger; fixed-set averages cannot certify adaptive rare terminals; new theorem awaits A016/A019 review.\n')
marker='20261023T132008Z-account03-A020-selector-boundary-tests'
for name,entry in [
 ('WORKLOG.md',f'\n### 2026-10-23 UTC / {marker}\nConsumed BOARD, A016 mixed obstruction/repair and A018 original-owner objection. New analytic fixed-frontier theorem gives expected SAME-Q/U reserve>107/64 after any predetermined mixed exposure under H(R)<=4I_rem; explicit genuinely overlapping-bit source meets this in all block counts j>=2. Root margin>19/8. Pilot PASS111 assertions2.194s; full PASS6808 assertions24.711s,594 profiles,128 signed frontiers,1458 actual signed branches,six A016 widths. Independent128-point reconstruction accepts unchanged A016 essential mixed terminal/weighted deficit/full stated policy. No failed assertion. Saved all protocol artifacts and exact certificates locally. Adaptive stopping and universal supplier remain open; no new-theorem review or supervisor mirror presumed. Brain self-care stale/unverified; stale compute snapshot not treated as admission.\n'),
 ('LEARNED.md',f'\n### {marker}: predetermined mixed averages and essential negative leaves\nFor original mu in[0,1/2], k>=5 and H(R_S)<=4I_rem(S), any predetermined post-q padding/source exposure has per-sign E[4I-CE]-oldU>107/64, original root margin>19/8. Its averaged core law is(1-2p)delta_u+(rho*rho_remaining/4)L[R_S+(1-2mu)delta_0], and inherited Qcore=(Pbar+delta_0)/2. All complete gate/mask/empty rows remain; gate influence uses signed original p, not sqrt(Pbar_empty). Source E=g3(a,b,c)g3(a,d,e) shares a physical bit: mean5/8, influences(3/8,1/4,1/4,1/4,1/4). Products of j>=2 disjoint E blocks meet the source hypothesis for every subset by H<=remaining dimension<=4I_rem. Independence inside E would be wrong. The theorem averages a fixed physical partition; adaptive selection of a rare set is UNPAID. A016 seven-essential-coordinate mixed terminals retain selected cost7(k+11)/64 and unbounded negative old-code reserve, though their actual full padding policy is paid. Retire original influence once; CE release is a credit, not fresh unused bank.\n')]:
 p=B/name;s=read(p) if p.exists() else ''
 if marker not in s: write(p,s+entry)

fields=P['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in fields['progress_fields']}
for c in claims:
 assert set(c)==set(fields['claim_fields'])
 assert c['statement_sha256']==hashlib.sha256(json.dumps({k:c[k] for k in ['exact_statement','hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')).hexdigest()
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all('## '+x+'\n' in report for x in fields['report_fields'])
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert len(read(B/'STATUS.md').splitlines())==2
files=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  assert p.stat().st_size<20_000_000
  if p.suffix=='.json':json.loads(read(p))
  files.append(dict(path=str(p.relative_to(R)),sha256=sha(p),bytes=p.stat().st_size))
dump(R/'out/PERSISTENCE_RECEIPTS.json',dict(status='PASS',utc=datetime.now(timezone.utc).isoformat(),checks=['Exact report/claim/progress field sets','Canonical statement hashes','All JSON parsed UTF8','Identical progress/delta','Two-line STATUS','All files below20MB'],files=files,remote_mirror='NOT_VERIFIED',new_theorem_independent_review='PENDING'))
print(json.dumps(dict(status='PASS',files=len(files),claims=len(claims),assertions=check['assertions'],stage=R.name)))
