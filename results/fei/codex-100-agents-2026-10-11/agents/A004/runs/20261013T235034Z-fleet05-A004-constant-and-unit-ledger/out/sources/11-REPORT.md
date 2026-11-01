# A004 split and erasure convention extension, stage 2

## exact target, quantifiers, hypotheses and units

This stage follows the B01 lead's explicit A004 target: extend the completed normalization baseline to B_i, L_i, Delta_i, JS_i, DTC, D_char, and the physical split f=psi+x_i phi; supply exact constant, dictator, parity, point-defect, bent, AND_n and Maj3 endpoints and check B_i<=h2(I_i). Uniform product measure, Boolean signs, normalized Walsh coefficients, full spectral law including the empty atom, and bits are the default. Natural-unit conversions remain explicit. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-12 03:13 UTC, B01 STREAM_NOTES.md v1 (2026-10-11 22:40Z), and A004 STATUS.md at stage start; source snapshotting also captured the 03:24 board revision. The B01 lead notes were absent in stage 1 and are now available. The explicit A004 direction takes precedence over the earlier suggested posterior application. Source-bound imports and exact SHA256 revisions are in out/source_manifest.json. The execution protocol remains 2026-10-11-execution-v2.

Mathematical source locators: supplement sources/ERASURE_REDUCTION.md Sections 1--5 for B, JS, Delta and the downward L; A003 stage-1 REPORT.md definitions lines 7--11 and implication/edge decomposition lines 30--54 (it already explicitly warns that its L is not B05's L); B05 canonical accepted no-go report for q,e,L_mismatch; B01 lead run 20261011T225200Z CLAIMS.json for the full-law DTC endpoint; ERASURE_RIGIDITY.md Section 1 for already-proved exact coordinate independence. A002 stage 2 already reconstructed that rigidity theorem and noted the stale OPEN lead label; this stage cites that correction rather than recreating its proof. A038 stage-2 reset report uses different occupancy information and does not provide the erasure-conditioning identity below. A086/A094 reports were checked for an A004 acceptance; no independent acceptance of this ledger was found. B20's root-payment and activation claims are read as downstream context, not assumed universal FEI payment. Local source copies do not certify mathematical claims outside these inspected locators.

## complete derivation or exact first unsupported line

### 1. Physical split and the three different charges

Let g=f|x_i=+1, h=f|x_i=-1, psi=(g+h)/2, phi=(g-h)/2. Then

    f=psi+x_i phi,
    psi,phi take values in {-1,0,1},
    psi phi=0 and psi^2+phi^2=1 pointwise,
    I_i=E phi^2, E psi^2=1-I_i.

The disjointness is on physical inputs, not on Fourier supports. With u_T=psihat(T), w_T=phihat(T), T excluding i,

    fhat(T)=u_T, fhat(T+i)=w_T,
    ghat(T)=u_T+w_T, hhat(T)=u_T-w_T.

Put a=u_T^2, b=w_T^2, m=a+b and Phi(a,b)=(a+b)h2(b/(a+b)), with zero-mass terms omitted. Define

    B_i=sum_T Phi(a,b)=H(S_i|S_without_i),
    L_down,i=sum_T b log2(1+a/b),
    C_up,i=sum_T a log2(1+b/a),
    B_i=L_down,i+C_up,i.

Zero numerator/denominator boundary values are zero for the corresponding weighted summand. Since ln(1+t)<=t, 0<=C_up,i<=I_i/ln2. Thus L_down,i<=B_i<=L_down,i+I_i/ln2. A003 and C018 Section 5 use this downward L. It is not B05's L_mismatch.

Indeed B05's child packet has q_T=(ghat(T)^2+hhat(T)^2)/2=m and e_T=(ghat(T)-hhat(T))^2/4=b. Therefore its L_mismatch,i=sum q_T h2(e_T/q_T) is exactly B_i. The two source meanings coincide only accidentally in degenerate cases. Already on AND2, B_i=L_mismatch,i=1 but L_down,i=1/2.

Let Q_plus,Q_minus be the normalized squared child spectra. Their average is m, and

    JS_i=H(m)-[H(Q_plus)+H(Q_minus)]/2,
    Delta_i=H(P)-[H(Q_plus)+H(Q_minus)]/2=B_i+JS_i.

The equal physical split weights 1/2 are essential. Here JS_i is information in bits and Delta_i is a full physical entropy decrement; neither is the spectral deficit I-Var. The source bound is 0<=JS_i<=(2/ln2)min(I_i,1-I_i). Stage 1 already reconstructed it; its proof is reused without claiming a new result.

In natural units all B,L_down,C_up,JS,Delta multiply by ln2. Consequently C_up,nat<=I_i and JS_nat<=2min(I_i,1-I_i). A universal downward price L_nat<=k I would give B_nat<=(k+1)I and FEI_nat<=(k+3)I. A universal mismatch/erasure price L_mismatch,nat<=k I instead gives FEI_nat<=(k+2)I. Equating the two L symbols loses one paid influence term in the proof ledger. These implications were already sourced in A003; the delta here is a machine-readable common convention with endpoint regressions.

### 2. The exact slack in B_i<=h2(I_i)

The spectral bit S_i is Bernoulli(I_i), so conditioning immediately gives

    B_i<=h2(I_i),
    h2(I_i)-B_i=MI(S_i;S_without_i)>=0.

An equivalent packet proof uses concavity of h2: sum m_T=1 and sum b_T=I_i, giving sum m_T h2(b_T/m_T)<=h2(I_i). Equality means the spectral bit is independent of the remaining spectrum. For an actual Boolean sign the source's exact dyadic rigidity then forces I_i in {0,1/2,1}. This is a reuse of a proved source endpoint, not a new approximation theorem. The source's bent-splice example already shows that arbitrarily small mutual-information slack does not imply a fixed local B_i/I_i price.

Summing this marginal bound is not a new FEI proof. For point defects, sum_i h2(I_i)/I grows like n, while B/I tends to 2. The joint conditional information must remain in the ledger.

### 3. DTC, TC, character influence and invariances

For the full normalized spectral law define

    B=sum_i B_i,
    DTC=H(P)-B=sum_i H(S_without_i)-(n-1)H(P),
    TC=sum_i h2(I_i)-H(P),
    sum_i MI(S_i;S_without_i)=TC+DTC.

For n=0 both information quantities are zero. DTC>=0 follows from the chain rule: for any order, DTC=sum_i MI(S_i;S_after_i | S_before_i). DTC=0 is equivalent to a product law; exact Boolean product rigidity is already closed by ERASURE_RIGIDITY Section 1 and the A002 correction. The B01 lead's exact-product OPEN label is stale, while its quantitative low-influence DTC target remains OPEN.

Use the distinct symbol D_char=sum_i min(I_i,1-I_i)=min_U I(chi_U f), a log-free influence quantity. Under uniform character translation P_S -> P_{S xor U}, H, B_i, DTC, TC, Delta_i, JS_i and D_char are invariant. If i belongs to U, L_down,i and C_up,i swap; otherwise they merely reindex and are individually invariant. Hence L_down is generally not invariant, even though B is. The physical psi/phi likewise swap at a queried bit in U, with a common remaining character factor. Conditioning on a nonempty spectral set is not character invariant because the removed atom changes from P_empty to P_U. These are full-law statements, not biased-basis translation claims.

### 4. Exact empty-atom correction for erasure and DTC

For any probability law P on subsets, let a=P_empty, v=1-a>0, R(S)=P(S)/v for S nonempty, R(empty)=0. Define the empty-row correction

    T0(P)=sum_i Phi(P_empty,P_{i}).

Split each erasure sum into its T=empty pair and the other pairs. Phi is homogeneous: Phi(vr,vs)=v Phi(r,s). The conditional R's empty pair is (0,R_{i}) and has zero erasure. Therefore, exactly,

    B_i(P)=v B_i(R)+Phi(P_empty,P_{i}),
    B(P)=v B(R)+T0(P),
    DTC(P)=h2(v)+v DTC(R)-T0(P).

The downward law separately obeys

    L_down,i(P)=v L_down,i(R)+P_{i} log2(1+P_empty/P_{i}).

Its complementary correction is P_empty log2(1+P_{i}/P_empty). Their sum is the erasure correction. At v=0 omit R and all full-law quantities are zero. This exact algebra holds for all finite set laws; R is not asserted to be a Boolean spectrum, so Boolean rigidity cannot be applied to R alone.

Actual Boolean counterexample to discarding the correction: AND2 has all four spectral atoms 1/4, v=3/4, H(P)=B(P)=2, DTC(P)=0. Its nonempty law is uniform on three subsets, H(R)=log2 3 and B(R)=4/3, so DTC(R)=log2 3-4/3>0. The sign is certified by 3^3=27>16=2^4. Here T0=1 and h2(v)+vDTC(R)=1, which cancel exactly. This is a normalization counterexample, not a refutation of the properly defined C018 or FEI.

### 5. Actual Boolean all-dimensional stress family

For the point defect f_n=1-2*1_{x=x0}, n>=2, put p=2^-n. P_empty=(1-2p)^2 and every nonempty atom is 4p^2. R_n is uniform on 2^n-1 nonempty subsets. Therefore

    B_i(R_n)=(1-2p)/(1-p),
    DTC(R_n)=log2(2^n-1)-n(1-2p)/(1-p)
            =n p/(1-p)+log2(1-p).

Let ell=log2(e). The convergent logarithm series gives explicit all-n bounds

    p(n-ell)+(n-ell/2)p^2/(1-p)
      <=DTC(R_n)<=p(n-ell)+n p^2/(1-p).

Indeed the difference from p(n-ell) is n p^2/(1-p)-ell sum_{k>=2}p^k/k, and 0<=sum<=p^2/[2(1-p)]. Thus DTC(R_n)~n p while H(R_n)~n.

For the full law write m0=(1-2p)^2+4p^2 and b0=Phi((1-2p)^2,4p^2). Exact erasure and downward formulas are

    B_i(P_n)=b0+4p(1-2p),
    L_down,i(P_n)=4p^2 log2(m0/(4p^2))+2p(1-2p),
    T0(P_n)=n b0,
    H(P_n)=E0+8p(1-p)(n-1), I(P_n)=2np.

The binary-entropy estimate gives 0<=b0<=4p^2(2n-2+ell), since m0<=1. Stage 1's exact E0 formula has E0=4p ell+O(p^2). Consequently H(P_n)~8np, B(P_n)~4np, DTC(P_n)~4np, vDTC(R_n)~4np^2 and T0=O(n^2p^2). In particular

    DTC(P_n)/H(P_n)->1/2,
    vDTC(R_n)/H(P_n)->0,
    DTC(P_n)/(vDTC(R_n))~2^n.

An unweighted near-product claim for the nonempty law is thus not a replacement for the full-law DTC endpoint, even on genuine Boolean signs with I->0. Conversely AND2 shows conditional DTC positive while full DTC vanishes. This settles the normalization question in both directions; it does not bound the unpaid nonempty adjacent spectral pairs by influence.

### 6. First unsupported line

The complete erasure-fraction target still requires constants c>0,K,tau with full-law DTC(P_f)>=cH(P_f)-KI(f) on the source-specified low-influence/minimal-violator regime. The identities above do not prove this. Substituting DTC(R_f) without h2(v)-T0 is invalid. The equivalent C018 edge obligation at nonempty lower endpoint |S|>=1 remains unpaid; the B20 root correction is already a paid component and is not claimed as new progress here. The C019 stopping route still requires a single-use payment at actual descendants plus full terminal H. Maj3's B=0,H=2 is an immediate terminal regression.

## executed validation with domain, arithmetic, commands and outputs

Frozen domain/specification saved first in out/FROZEN_SPEC.json. Fixed domain: all 278 labelled signs on n=0..3, plus 53 endpoints (six families at n=1..8, quadratic bent at n=2,4,6,8 and Maj3). Integer FWHT spectra are compared with direct character sums; Fraction arithmetic checks the ternary split and exact coefficient identities; entropy equalities use rational prime-log forms. Named nonnegativity and payment inequalities use the reused stage-1 rational atanh-series logarithm bounds, with no floating values as premises. Equality witnesses additionally use integer comparisons. Memory estimate 40 MB; no job expected over 300 MB, GPU, adaptive dimension increase or heavy search.

Commands: python -X utf8 runs\20261012T030039Z-fleet05-A004-constant-and-unit-ledger\code\read_sources.py; python -X utf8 runs\20261012T030039Z-fleet05-A004-constant-and-unit-ledger\code\check_split.py. Final result: PASS, 26,220 exact assertions, all 278 exhaustive functions plus 53 endpoints, measured computation 1.6457144999876618 seconds. Exact records are in out/validation.json; endpoints were saved as they finished in out/endpoint_records.jsonl. The first split pilot exposed reversed physical slice labels against the reused FWHT convention x_i=(-1)^bit_i; out/PILOT_CORRECTION.json records the fix. A subsequent command stalled and was stopped, and the next command hit its 58-second guard. Memoizing repeated exact log/entropy/bound calculations and integer ternary transforms made the full identical domain pass; out/HOST_DELAY.json and out/TIME_LIMIT_RECEIPT.json preserve those attempts. Failed/incomplete commands are not certificates. Helper v2.1 retains every acceptance assertion and adds no domain. The final checker uses a 58-second guard. The all-n identity and stress-family limits are analytic proofs above; finite checks are implementation validation, not their substitute.

## proof dependencies and changed downstream conclusions

The first-stage unit ledger and certified log arithmetic are reused, not rebuilt. Dependencies are Parseval, entropy chain rule/conditioning, homogeneous binary-entropy packets, and the stated source identities. There is no open FEI premise. The extension is one bundled convention/interface claim, not another broad unreviewed FEI candidate. A003 already warns about the L collision; this ledger makes that warning machine readable. A002 already corrects exact product rigidity; no redundant theorem is opened.

Changed downstream substitutions: B05 L_mismatch equals B; A003 L_down needs its +I/ln2 complement before invoking the erasure bridge; full-law B/DTC are character invariant whereas L_down alone is not. Full/nonempty erasure conversion uses +T0 for B and -T0 for DTC. The actual AND2 and point-defect family certificates refute only omitted-correction readings. They do not refute FEI or a correctly stated near-erasure endpoint. Information quantities scale by ln2; D_char and influence do not.

## one next mathematical action and independent reviewer

A086 primary independent reviewer; A094 alternate. Reconstruct the full/nonempty erasure identity and the L_down character-orientation rule, then check the independent integer witness and all-n point-defect series bounds. After acceptance retire the convention baseline. The next mathematical application is A003's weak-influence majority-encoder descendant: measure its actual full-law DTC via h2(v)+vDTC(R)-T0 and retain terminal entropy, rather than attempt continuity from the already solved exact-product endpoint. The nonempty signed edge payment is the remaining universal obligation.

## actual persistence receipts or precise save blocker

All writes are confined to the assigned A004 run and rolling files. Source copies, exact helper snapshot, derivation, frozen specification, correction record and successful certificate are local. Final CONVENTIONS.json, ENDPOINT_CHECKS.md, CLAIMS.json, PROGRESS.json and matching PACKET_DELTA.json are generated with protocol field checks; out/persistence_receipt.json records SHA256 and sizes after completion. Independent acceptance, supervisor adoption and remote mirrors are not implied by local saves. No shared source/index, another agent's output, brain, git, mail or forbidden project is modified.

## Universal bridge

This stage advances the C018/C019 normalization interface by closing the lead's split/erasure ledger and proving the exact conversion B(P)=vB(R)+T0 and DTC(P)=h2(v)+vDTC(R)-T0. Actual Boolean endpoints expose the factor-two L-name collision, the noninvariance of the downward orientation, and an all-dimensional omitted-correction error growing like 2^n on point defects. It contributes no new universal paid influence estimate: nonempty signed adjacency, hereditary child payment and terminal entropy remain open. NEXT is the actual full-law DTC/child reserve after A003's weak-influence majority-encoder split, because it consumes the live B01 localization work and preserves exactly the normalization terms needed by the universal endpoint; another isolated class FEI bound or repeat exact-product classification would leave that endpoint unchanged.
