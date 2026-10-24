# A038 / B08: occupancy conditioning and the missing normalization account

## exact target, quantifiers, hypotheses and units

Retrieve and audit the current K_occ before using it. The original definition and archived correction chain are in OCCUPANCY_TARGET_SOURCE.md with complete source copies. For any probability law P_all on subsets with v=P_all(S nonempty)>0, write P+=P_all(.|nonempty), r_i=P+(i in S), d_i=v r_i, Q_d=product Bern(d_i), and let Q_r be the source-defined maximum-entropy nonempty law. Put
K_full=D_2(P_all||Q_d), K_occ=D_2(P+||Q_r).
Our exact cross-law audit applies to every such finite law, including genuine biased or uniform Boolean spectra when their own Fourier basis is fixed.

Frozen new payment candidate: for every genuine uniform Boolean function f, K_occ(f)>=T(f)/4-kappa I(f) for one finite fixed kappa>=0, using the unconditioned signed product-marginal collision statistic T in A036's report. Also test the more naturally weighted v K_occ. Named debt is [T/4-kappa I]_+. This proposed substitution is explicitly OUR audit target, not a claim made by A036. It is REFUTED by actual point defects, for every fixed kappa. The canonical Gamma debt is a different target and remains open.

Quantitative correction theorem: define M=(1-v)delta_empty+v Q_r and Delta=D_2(M||Q_d). Then
K_full=v K_occ+Delta,
Delta=sum_i h_2(d_i)-h_2(v)-v Hmax(r)>=0.
No fixed dimension-independent A can bound Delta<=A I on all Boolean functions. The exact reference/normalization correction is required rather than absorbed into an unspecified O(I).

All logs are base two unless ln is written. Constant Boolean functions have v=0, I=H=0 and are excluded only from conditional-law definitions. Marginals 0 or 1 force coordinates; restrict to that support before writing logarithms. The claims below have finite divergences on that support.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2. Read campaign README/CURRENT_STATUS; inspect claim/obstruction/packet registries, next actions, A038 full assignment and plan B08 contract (lines 734-764). Read BOARD.md at stage start. B08 STREAM_NOTES.md was absent. A036 and A037 current reports were read; the collision definition and no-reuse warnings determine the audit boundary. Earlier B05/B09/B19 report scope was inspected through campaign sources and neighboring reports; none is a mathematical premise.

Read the supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING, with ROUTE_MAP_CURATED Sections 1-6 and 9.1 particularly relevant. Other curated files were inventoried, not claimed as fully independently reviewed. The plan and contextual manuscripts were searched/read at relevant interfaces rather than independently audited in their entirety. Threshold current text Section 2, Gibbs inequality and Lemma 2.1, was compared with its 29-page predecessor; current spectral-level constant is log2(4+e), predecessor 3. Percolation current and other-version Section 2, Lemma 2.1, retains nonempty masks and terminal contents. Its spatial occupancy vector is not K_occ. No threshold/percolation class theorem is used as a proof premise.

Brain recall: two main-Brain recalls and one mathematical-Brain recall were executed read-only; none returned the exact definition. Instead the curated source map led to the authorized Brain repository checkpoint and original reports. The default-branch checkpoint was verified to have the same blob as the pinned checkpoint. Original definition: account02/B15, Theorem 2.1 and Section 4, blob 5ce14eaaec34f0d91f2d430dba576e19dddc6894 at 2bf247373576eb406ca91bb3ea5f3ce5e5ab8588. Exact composition source: account04/B15, Theorem 2.1, blob 1c91fc5076be85aaceca37bc8f4ce31cbaed2311 at the same commit. Balanced admission: account02/B18, Theorem 2.1 and equation (4.6), blob 05781355d8908301b764f987ea74e8547f9e506e at 7d20a4bb4067085af7c5e7c9a82aef31998a7d36. Fixed-reserve original: account01/B01, Sections 3-7, blob 748dbfcb20b3dc236200d5351b74bf3edb2f4158 at 63a1d889005602ab5ed5f15497243c70186689a1. Complete retrieved sources, URLs and local hashes are archived in out/sources and source receipts. These older mathematical controls remain current in the checked Brain checkpoint; no independent acceptance of their entire external dependency chains is asserted.

## complete derivation or exact first unsupported line

### 1. Source I-projection and exact change of account

For mu=sum r_i=1 every mass is on a singleton, and that law is uniquely fixed by r. For mu>1, the source equation 1-c=prod(1-c r_i) makes independent Bernoulli(c r_i) nonempty with probability c. Conditioning yields marginals r. On nonempty subsets log Q_r is affine in the coordinate indicators, after deleting forced coordinates. Therefore E_P+ log Q_r=E_Q_r log Q_r. Gibbs gives Hmax(r)-H(P+)=D(P+||Q_r)>=0. This justifies the exact source formula; no arbitrary sign-free law is assumed Boolean.

P_all and M have identical empty mass 1-v and coordinate marginals d_i=v r_i. On nonempty sets,
log(M/Q_d)=log v+log Q_r-log Q_d,
an affine function of the coordinate indicators plus a constant. On the empty atom its expectation is fixed by 1-v. Consequently
E_P_all log(M/Q_d)=E_M log(M/Q_d).
Expanding relative entropy gives
D(P_all||Q_d)=D(P_all||M)+D(M||Q_d).
The first term is v D(P+||Q_r)=v K_occ. The second is Delta>=0.

Equivalently, cross entropy against Q_d is sum_i h_2(d_i), while
H(M)=h_2(v)+v Hmax(r).
This proves the displayed explicit Delta formula. It is the additional entropy gap of the full-law product reference after the nonempty maximum-entropy step; it is not conditional occupancy KL.

Let c_d=Q_d(nonempty) and Q_d+=Q_d(.|nonempty). KL chain rule on the empty/nonempty event gives the additional exact formula
Delta=D_2(Bern(v)||Bern(c_d))+v D_2(Q_r||Q_d+).
The inner Pythagorean identity follows because log(Q_r/Q_d+) is affine on nonempty subsets. This separates event normalization from nonempty-reference tilt. Both terms are nonnegative and may be large. Zero-probability endpoints use the forced support without infinity subtraction.

### 2. Actual point defects have K_occ exactly zero

For every integer m>=2 on m uniform physical bits, take
f_m(x)=1-2*1_{x=0}, d=2^(1-m), N=2^m.
The Walsh amplitudes are 1-d at empty and -d at every nonempty set. Thus
P_all(empty)=(1-d)^2, P_all(S)=d^2 for S nonempty,
v=2d-d^2, d_i=d, I=md,
P+(S)=1/(N-1), r_i=d/v=1/(2-d).

Take c=1-1/N=1-d/2. Then c r_i=1/2 and 1-c=(1/2)^m. The source I-projection Q_r is the uniform law on all nonempty subsets, exactly P+. Therefore
K_occ(f_m)=0 for every m>=2,
M=P_all, Delta=K_full.

A direct entropy estimate gives H(f_m)<=4I. Indeed the empty contribution
-2(1-d)^2 log2(1-d)<=2d/ln2<4d,
using -ln(1-d)<=d/(1-d) and ln2>1/2. The nonempty contribution equals
4d(1-d/2)(m-1)<=4d(m-1).
Hence
Delta=K_full=m h_2(d)-H(f_m)>=(m-5)I,
because h_2(d)>=d log2(1/d)=d(m-1).
This proves that Delta/I diverges, despite K_occ=0 and I->0. A036's full-support and low-influence hypotheses do not remove this distinction. This is a normalization audit, not a Shannon FEI counterexample: the family still has H/I<=4.

### 3. The proposed normalized collision substitution fails for every fixed coefficient

Use precisely A036's full-support phase convention:
Q_d(S)=d^|S|(1-d)^(m-|S|),
b_empty=+sqrt(Q_d(empty)), b_S=-sqrt(Q_d(S)) for S nonempty.
Let C_b(U)=sum_S b_S b_(S xor U), w_U=C_b(U)^2,
Z=sum_U w_U, T=Z^(-1)sum_U w_U log2(1/w_U).
The temporary symbol w here avoids confusing collision masses with spectral variance v.

Set a=4d(1-d). For a nonempty shift of size k,
C_b(U)=(2 sqrt(d(1-d)))^k [1-2^(2-k)(1-d)^(m-k)],
w_k=a^k [1-2^(2-k)(1-d)^(m-k)]^2.
Proof: the all-positive product amplitude has autocorrelation (2 sqrt(d(1-d)))^k. Changing the sign only at the empty coefficient subtracts 4 sqrt(Q_d(empty)Q_d(U)), giving the formula. This independently reconstructs A036's formula.

For k=1 the bracket lies in [-1,1]; for k>=2 it lies in [0,1]. Thus 0<=w_k<=a^k<=1, so every entropy summand is nonnegative, w_0=1 and 1<=Z<=(1+a)^m. For m>=8 put s=2(1-d)^(m-1)-1>0. Bernoulli gives s>=1-2(m-1)d, and the singleton mass is w_1=a s^2. Keeping only the m singleton contributions yields
T/(4I)>=(1-d)s^2/Z * log2(1/a).
The prefactor W=(1-d)s^2/Z satisfies
W>=(1-d)[1-4(m-1)d]e^(-ma)
 >=(1-d)[1-4(m-1)d][1-4md]
 >=1-(8m-3)d.
Every factor used here is nonnegative for m>=8. Also log2(1/a)>=m-3. The sequence (8m-3)(m-1)2^(1-m) decreases on m>=8: its next-term ratio is (8m+5)m/[2(8m-3)(m-1)]<1 since 8m^2-27m+6>0. At m=8 it is 427/128<4. Therefore
T/(4I)>=(m-3)-(8m-3)d(m-3)
 >=m-3-427/128>m-7.

For every fixed finite kappa choose integer m>=8 with m>kappa+7. Then T/4-kappa I>0, whereas K_occ=v K_occ=0. This is an all-dimensional analytic counterfamily to the explicitly frozen cross-law payment candidate. No tensor amplification, floating-point sign or automated dimension escalation is needed.

The m=16 finite certificate has I=1/2048, v=65535/1073741824,
12.953250698869 <= T/(4I) <= 12.953250698870,
12.512401622344 <= K_full/I <= 12.512401622345.
Thus the substituted kappa=8 payment fails by more than 4.95325 I, while the original A036 K_full payment is unaffected.

### 4. A controlled balanced lift explains why balanced debt is different

Let F_m(z,x)=z f_m(x) with a fresh physical character z. Its spectrum is the spectrum of f_m with z appended to every set; F_m is balanced, H(F_m)=H(f_m), I(F_m)=1+md. The occupancy marginal for z is 1. Hence the source I-projection is simply z appended to Q_d and
K_occ(F_m)=K_full(f_m), Delta(F_m)=0.
Indeed the root variance is now 1, all reference sets contain z and the nonempty conditioning disappears. The same underlying defect can therefore have zero K_occ before balancing and large K_occ after balancing. Neither normalization may be silently carried across an actual transformation.

On this specific lifted family the already established H(f_m)<=4md gives the explicit canonical balanced debt payment
K_occ(F_m)>= [Hmax(r(F_m))-4(I(F_m)-1)]_+.
This is an audit application of the known point-defect entropy estimate, not a new class FEI theorem. It does not justify the same inequality for arbitrary balanced seeds.

### 5. Surviving gap and correction scope

The imported antipodal two-flip dictator reserve no-go concerns D_Gamma-lambda v K_occ with positive fixed lambda; our no-substitution obstruction concerns the opposite task of making conditional K_occ pay an unconditioned collision debt. They are distinct failures. The exact correction Delta neither proposes such a reserve nor solves the canonical debt. No new estimate is asserted for arbitrary prime gates, physical-child reference resets, or overlapping composition.

First unsupported universal line: proving
K_occ>=[Hmax(r)+a_q-sum r_i a_i]_+
for arbitrary source-realizable prime gates at all required biases, or proving a nonreusing physical transfer of the exact state-dependent Delta together with this occupancy debt. Positivity of Delta and K_occ does not pay either. The balanced slice remains FEI-strength.

## executed validation with domain, arithmetic, commands and outputs

Frozen target and search-free specification are out/FROZEN_TARGET.md and out/FROZEN_SPEC.json, written before execution. Command from A038:
python -X utf8 runs/20261011T221733Z-account05-A038-occupancy-term-audit/code/check.py

Compressed exact formulas were checked for m=2,...,16. Independent integer Walsh and physical edge-influence reconstruction, exact conditioning, cross-law and event/reference corrections were checked for m=2,...,8. Balanced-lift Walsh laws were independently checked for the same seven dimensions. Direct signed autocorrelation was reconstructed by summing rational factors over actual subsets for m=2,...,7, without irrational numerical amplitudes. A pinned OR(literal,AND) Walsh table supplies a source control. This is deterministic family validation, not an exhaustive search or optimality claim.

Entropy/KL identities use exact rational coefficients of formal logarithms. Small factors are extracted and any residual composite is retained as an exact log symbol; complete cancellation is a sufficient exact identity certificate. Numerical signs use range-reduced ln x=2 sum_{j=0}^{19} t^(2j+1)/(2j+1), t=(x-1)/(x+1) in [0,1/3), with tail at most 2 t^41/[41(1-t^2)]. The ln2 denominator is positive; all returned intervals use the correct division endpoints and are rounded outward to multiples of 10^-12. No floating-point comparison establishes a mathematical sign.

Final output: PASS, 4,323 exact assertions; observed runtime 10.0806618 seconds, in out/VALIDATION.json. The first version passed the same domain but took 117.6119154 seconds because unrestricted factorization of normalization numerators was unexpectedly expensive. This violated the frozen 60-second pilot cap; it is recorded in out/INITIAL_CHECK_RECEIPT.json. The bounded-factor change repaired runtime, with no enlarged domain or claim. There was no heavy job, GPU, automatic dimension increase or external reviewer replay. The analytic arguments supply all-m quantifiers.

## proof dependencies and changed downstream conclusions

The correction and counterfamily are self-contained using Walsh character orthogonality, Gibbs inequality, the binomial theorem, Bernoulli's inequality and elementary entropy bounds. The exact K_occ definition is source-pinned; A036's collision formula is independently reconstructed rather than assumed from its unreviewed theorem. A037's ledger is an orientation input and not a proof premise.

This is a scoped audit/obstruction handoff rather than another broad universal positive candidate while B08 has source-complete positive results awaiting review. No existing A036 or A037 result is refuted. A036/A040 must keep K_full and K_occ separate. A039/A057 must retain both the event probability and conditional reference tilt when transporting them. A088/A094 should independently reconstruct the all-m no-go and deterministic-coordinate endpoints. B20 should register only the newly refuted substitution, with no change to FEI status or the original normalized K_full target. No downstream use is claimed.

## one next mathematical action and independent reviewer

Next: A039 should compute the signed physical-child change of Delta=h-sum minus h(v) minus v Hmax on the sparse activated bent-defect control and combine it with its actual child-reference reset correction. Test whether the entire weighted transfer, retaining child deficits, has a nonreused physical influence payment. A088 is primary reviewer; A094 is the alternate. Retire the false K_occ-for-K_full substitution rather than adjust its fixed coefficient.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, OCCUPANCY_TARGET_SOURCE.md, OCCUPANCY_PAYMENT.tex, code/check.py, frozen target/specification, source copies and validation outputs are saved within the authorized A038 run only. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated. out/ARTIFACT_SHA256.json and out/SOURCE_RECEIPTS.json give local readback hashes and source metadata. No shared index, another agent folder, git command, brain write or external publication was performed. Supervisor copying, mirror verification, native Brain ingestion and independent review are not observed.

Universal bridge: This stage protects C024 history transfer and the C020 whole-set normalization interface by identifying the exact missing Delta account and proving it cannot be absorbed into O(I) or replaced by conditional occupancy credit, even for full-support Boolean sources with I tending to zero. It contributes no new universal FEI constant and leaves C018/C019/C020/C024 open. The remaining task is a genuinely source-compatible nonreusing payment of the complete occupancy/reference debt; the shortest next step is the physical transfer of the explicit Delta on the existing sparse-defect tree, because this tests the exact normalization obstacle before any further class result or KL positivity claim can be used universally.

