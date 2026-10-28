# FEI route map: selected mathematical sections and source pins

**Full FEI remains OPEN.** Curated mathematical excerpt. Original section numbers and mathematical prose are retained; unrelated historical operating instructions and unneeded sections are omitted. This is not a complete archive or a new proof.

Original repository source: [research_pushes/2026-09-30-fei-current-route-map/REPORT.md](https://github.com/yspennstate/math-research-brain/blob/main/research_pushes/2026-09-30-fei-current-route-map/REPORT.md). Immutable Git blob: `216cb662e7b21cfe6d7c2034a6690f3c10b886fa`. See `../SOURCES.json` for exact retained line ranges, original hashes, and the packaged-file hash. Links to unbundled companion files refer to their original repository locations.

## 1. Universal target and exact accounting

For a genuine Boolean function on a finite uniform cube, let P(S)=fhat(S)^2, H=H_2(P), I=sum_S |S|P(S), d_i=Inf_i(f), j_i=min(d_i,1-d_i), B_i=H(S_i|S_-i), and B=sum_i B_i. Zero-mass terms are zero. Every logarithm below is base two unless written ln. D_2 denotes base-two Kullback–Leibler divergence, not order-two Rényi divergence.

**PROVEN, recovered September 17.**
- Delta_i H = B_i + JS(P_i^+,P_i^-), with 0 <= JS <= (2/ln 2)j_i
- I(f)=d_i+[I(f_i^+)+I(f_i^-)]/2
- B<=H, and universal B<=K I implies H<=(K+2/ln 2)I by a physically realizable restriction induction
- Thus finiteness of sup B/I is equivalent to full FEI; it is not a solved weaker estimate

Read the [complete erasure reduction](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/proofnet24/P03-fei/solo-2026-09-17/ERASURE_REDUCTION.md) before reconstructing it. Its downward-edge residual L_down satisfies L_down<=B<=L_down+I/ln 2. The blind Jensen bound L_down<=I log(n/I) discards precisely the structure needed for closure. L_down is **not** the all-shift collision L in Section 4.

## 2. Strongest retained local restriction information

### 2.1 First use the recovered September 20 mismatch/KL theorem

**PROVEN; recovered, not a September 30 discovery.** For the actual Boolean children g,h, write a_T=ghat(T), b_T=hhat(T), P_T=a_T^2, Q_T=b_T^2, q_T=(P_T+Q_T)/2, m_T=(|a_T|-|b_T|)^2/4, M=sum_T m_T, and nu_T=m_T/M when M>0. Then

    M=(1-sum_T sqrt(P_T Q_T))/2 <= j_i
    B_i=sum_T q_T h_2(m_T/q_T)
    B_i <= M[log(1/M)-D_2(nu||q)+1/ln 2]
    JS(P,Q) <= 2M/ln 2
    Delta_i H <= M[log(1/M)-D_2(nu||q)+3/ln 2]

When M=0, B_i=JS=Delta_i H=0 exactly. If the child squared spectra agree coordinatewise, the parent inherits their FEI constant with zero extra cost. An r-dimensional signed physical translation symmetry can be removed by r actual coordinate queries at zero allocation/decrement, preserving H and weakly decreasing I. A minimum-dimensional counterexample to a proposed constant may therefore be assumed to have no nontrivial signed-translation symmetry.

[Full proof, Theorems 3.1–5.1](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/proofnet24/P03-fei/runs/2026-09-20/2026-09-20T12-28-55+0300__fei-isospectral-splicing-symmetry-quotient.md). Preserve the KL rebate and recognize exact isospectral splits before replacing M by j or charging a scalar child statistic. This is stronger structural information than a blind kappa surcharge, although the different numerical upper bounds need not be pointwise ordered.

**OPEN payment.** A real stopping tree still needs a nonreusing bound on

    sum_v w_v M_v[log(1/M_v)-D_2(nu_v||q_v)] = O(I(f))

together with paid terminal entropy. Since M_v<=j_v<=d_v, the remaining 3M_v/ln 2 terms already fit the queried-influence budget. Exact M=0 splicing alone gives no universal approximate-isospectral theorem.

### 2.2 September 30 additions: useful bounds, not replacement of the rebate

**PROVEN in the new continuation; novelty unverified.** Put kappa(u)=1-max_T uhat(T)^2 and kappa_min=min(kappa(g),kappa(h)). For every physical split,

    B_i <= j_i[2+3/(2 ln 2)+log(1+kappa_min/(2j_i))]

with value zero when j_i=0. It may be minimized with the exact formula and earlier bounds; it is not everywhere better than the old additive kappa estimate. Sparse activation of a bent one-point flip proves that B_i/j_i can diverge while both child influences tend to zero. Hence no multiplier Phi(I(g),I(h)) bounded near (0,0) pays B_i uniformly; coefficient 1 on the displayed logarithm is asymptotically necessary. [Proof and precise falsifier](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/research_pushes/2026-09-30-fei-log-allocation/REPORT.md).

A second universal bound, with v=Var(f) and **actual** d_i>0, is

    B_i <= d_i[log(v/d_i)+(1+2/sqrt(e))/ln 2]
    Delta_i H <= d_i[log(v/d_i)+(3+2/sqrt(e))/ln 2]

The latter constant is 6.078162672495945.... [Variance proof](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/research_pushes/2026-09-30-fei-log-allocation/VARIANCE_LOCAL.md). Summing loses sum_i d_i log(v/d_i); it does not pay the universal aggregate erasure bound.

**PROVEN restricted applications.**
- Any restriction-closed class having at least one ordinary certificate of length <=w at every nonconstant restriction obeys H<=[w+2+7/(2 ln 2)]I. This includes arbitrary mixed-literal width-w DNF/CNF, with overlaps and no term-count bound. The monotone refinement is 2+7/(2 ln 2)+log(2^w-1). [Certificate proof](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/research_pushes/2026-09-30-fei-log-allocation/CERTIFICATE_COROLLARY.md)
- Every Boolean function with a decision tree of at most s>=2 leaves obeys H<=[log log s+6.078162672495945...]I. More generally, the hereditary expected-depth bound D gives log D plus this constant. A root-only expected-depth bound is not the hereditary hypothesis. [Decision-tree proof](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/research_pushes/2026-09-30-fei-log-allocation/VARIANCE_LOCAL.md#2-decision-tree-consequences)

These are genuine scoped progress, but w and s may grow. They do not yield one universal constant.

## 3. Do not restart finite-order Booleanity relaxations

**PROVEN obstruction, recovered September 20.** Exact Booleanity is normalization plus **all** signed convolution identities sum_S a_S a_(S xor U)=0 for U nonempty. Normalization and singleton cancellation alone were already subsumed by a much stronger no-go.

For K=4^k, disjoint control blocks of size w, and the explicit real-valued G_(K,w) in [BOOLEANITY_ORDER, Theorem 2.1](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/proofnet24/P03-fei/continuations/2026-09-20-booleanity-order/REPORT.md#theorem-21),

    E G^2=1; all square-spectrum coefficients of degrees 1,...,2w-1 vanish
    I(G)=w+3/4
    B(G)/I(G) > [3/(4w+3)] log(1+K/4) -> infinity

Its Fourier coefficients are dyadic; E G^4<3; every restriction fixing <=2w-1 physical coordinates has norm exactly one. For any prescribed fixed cancellation order r, take w=ceil((r+1)/2) and K arbitrarily large. These functions are **not Boolean**.

Sections 3–4 strengthen the obstruction: dyadic L2-near-constant functions can have vanishing energy and square defect; a distinct, not asserted dyadic, uniformly near-constant family defeats even B<=C[I+E(f^2-1)^2]. Along an explicit increasing-order sequence the square defect is o(I) while B/I diverges. Section 5 proves rigidity only for the stated block-linear/data-affine genuine-Boolean pattern; it does not classify general Boolean spectra.

**Stop condition for a retry:** state an additional consequence of full Booleanity not possessed by these examples and show where it supplies the missing high-degree payment. Merely increasing a fixed truncation order, retaining dyadic coefficients, or adding small norm defects is already ruled out. Conversely this no-go does not prohibit a finite proof using other full-Booleanity consequences.

The report's old upload-blocked wording is historical: the [delivery recovery](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/proofnet24/P03-fei/continuations/2026-09-20-booleanity-order/DELIVERY.md) records byte-preserved remote proofs/checker/output. Do not mistake an old delivery failure for an unavailable theorem.

## 4. Collision/KL route: keep the normalization and both directions separate

For the actual spectral law P, Q is the product law with its coordinate marginals. Distinguish K_full=D_2(P||Q), K_supp=-log Q(A), and K_shape=D_2(P||Q(.|A)), A=supp(P). For a normalized reference amplitude b, put C_b(U)=sum_S b_S b_(S xor U), v_U=C_b(U)^2, Z=sum_U v_U, L=sum_U v_U log(1/v_U), and T=L/Z.

**PROVEN in September 30 source.**
- T=H(v/Z)-log Z, **not** H(v/Z); T is exactly additive on amplitude tensors
- **REFUTED:** universal K>=theta L-kappa I for raw L and any fixed theta>0, finite kappa. The genuine Boolean three-bit one-point factor has Z=319/256>1, so tensor powers give exponential L and linear K,I
- **REFUTED:** universal recovery K_shape<=A T_conditioned+B I for fixed A,B. Paired-coordinate one-point lifts have T_conditioned/I->0, K_shape/I=m-3+o(1), and K_supp/I->1/ln 2. This under-recovery result does **not** refute K_shape>=T/4-kappa I
- **PROVEN restricted repair:** unconditioned Q with the specified + sign completion at zeros on that family gives T_completed/4-K_shape=o(I)
- For any Boolean source with spectral zeros in dimension >=2, one physical-point flip fills every zero and preserves every existing Fourier sign. This realizes the completion signs in the explicit paired family; reference amplitudes are not thereby Boolean Fourier coefficients, and the original marginals remain the reference

[Complete tensor, support-loss, and surgery proofs](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/research_pushes/2026-09-30-fei-normalized-convolution-0236z/REPORT.md). “+ at every zero” is not a globally tensor-compatible rule; tensor identities for completed references require product completions.

**CONDITIONAL full-FEI admission, not a proved premise.** Even only for full-support Boolean f with I(f)<=1/16, a universal

    K_full >= T/4-kappa I

would imply **full FEI** with constant kappa+2+log e. Full support removes completion ambiguity. The reduction tensors an arbitrary seed, fills zeros with one-point surgery, and sparsely activates it. [Complete admission proof](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/research_pushes/2026-09-30-fei-log-allocation/COLLISION_ADMISSION.md). Thus small influence and full support do not make this a solved or demonstrably easier problem. The raw-L falsifier does not refute normalized T. For a broader collision construction, separately prove both valid lower payment and sufficient recovery of the required deficit; these are different tests.

## 5. Mandatory older corrections and stronger benchmark floors

Read the [current FEI checkpoint](https://github.com/yspennstate/math-research-brain/blob/fc8276da09123d9f7ede195ad8ac27ed5768306f/scheduled_tasks/work/shared/fei-all-team-2026-09-22/CURRENT_RESEARCH.md), [all correction deltas](https://github.com/yspennstate/math-research-brain/blob/fc8276da09123d9f7ede195ad8ac27ed5768306f/scheduled_tasks/work/shared/fei-all-team-2026-09-22/DELTAS.json), and [still-present correction inbox](https://github.com/yspennstate/math-research-brain/blob/fc8276da09123d9f7ede195ad8ac27ed5768306f/scheduled_tasks/work/shared/fei-all-team-2026-09-22/CORRECTION_INBOX.json) before positive reuse. These are scientific sources, not current fleet assignments.

**REFUTED exact scopes; retain unaffected identities.**
- Fixed Gamma-dagger, quadratic repairs 0.337/0.34, and the old smaller shaped scale fail the stronger 18-input prime witness. A later safe direction or known-witness repair is not all-gate positivity
- Fixed positive occurrence reserve D_Gamma>=lambda v K_occ for every source fails for every lambda>0 at finite potential center. Lambda=0, nonlinear/state-dependent credit and FEI are not refuted
- Full unweighted convolution L2 payment and fixed/low-depth labelled KL extraction underpay rare logarithms
- Raw U4=O(J) from all-block terminality plus tensor primitivity is false; the counterexample does not remove full ratio-criticality hypotheses
- The global-safe-cone-to-local-selector step is **NEEDS REVALIDATION**, not a disproved conclusion: it discards child slack that need not vanish

Each correction links its complete original proof/counterexample through the checkpoint and deltas. No initial positive occurrence credit, small cell count, finite bias sweep or relabeled residual is a substitute for payment.

**Stronger recovered benchmark, not a new FEI lower bound.** The [F4 report](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/proofnet24/P03-fei/continuations/2026-09-22-opus-team/F4-proof-attempt/REPORT.md) and its [actual certificate log](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/proofnet24/P03-fei/continuations/2026-09-22-opus-team/F4-proof-attempt/logs/certify_tower.log) give, on the 104,976-variable Numaro selfcomposition,

    B/I approximately 4.5388346767
    min_i B_i/d_i approximately 4.5048788574
    min_i Delta_i H/d_i approximately 7.0518528350

Hence K=4 aggregate or existential erasure targets are stale, and potential-free one-coordinate restriction induction cannot have constant below 7.05. Conservative floors are 4.5388, 4.5048, and 7.0518 respectively. The source's outward numerical certificate assumes numpy log2/log1p accuracy within 8 ulp; this map did not replay it. Limits 4.58825, 4.55771, 7.11162 are numerical observations, not certified universal limits. None raises the lower bound on the actual FEI constant merely by measuring this proof mechanism.

## 6. Genuine universal obligations still open

1. **Restriction/erasure:** prove B<=K I for one finite universal K, or construct a physical stopping argument paying actual packet mismatch/KL charges with a nonreused influence budget and uniformly paid leaves
2. **Gate potential:** establish the exact gate inequality for every genuine Boolean gate, all required product biases and boundary contractions using one symmetric nonnegative finite-cap potential. A safety direction or repaired witness leaves this open
3. **KL:** pay K_occ>=[-B_inf^Gamma]_+ with actual source signs, bias, normalizations and reference changes retained. On the balanced slice this is already full-FEI-strength. Nonlinear/multiscale payment remains possible; fixed positive reserves and low-level truncations do not supply it
4. **Critical cores:** make full ratio-criticality yield a realizable nonreusing physical rule, including small/nonrobust rows and entropy cost. Terminality alone and a renamed curvature surplus do not close it

The [checkpoint's three-route outline](https://github.com/yspennstate/math-research-brain/blob/fc8276da09123d9f7ede195ad8ac27ed5768306f/scheduled_tasks/work/shared/fei-all-team-2026-09-22/CURRENT_RESEARCH.md#6-three-source-grounded-research-pathways) supplies the longer dependency links. This map adds no universal proof and no Boolean counterfamily with unbounded H/I.

---

### 8.2 Overlapping-product entropy subadditivity was already refuted

**REFUTED; recovered September 20 source, not a new September 30 broad theorem.** The proposed inequality H(fg)<=H(f)+H(g) for arbitrary Boolean factors sharing variables fails. The eleven-variable shared-rare-clause example in the September 30 archive is exactly the earlier [directional-compression Section 7 construction](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/proofnet24/P03-fei/continuations/2026-09-20-directional-compression/REPORT.md#7-an-explicit-obstruction-to-shared-control-subadditivity), up to complementing the common control. Its equation (7.6) already identifies the positive restriction-decrement defect with H(fg)-H(f)-H(g). The prior proof and the new attribution correction were both read; the exact finite checker was not replayed here.

Read the [explicit attribution correction](https://github.com/yspennstate/math-open-problems/blob/e894a01f20ba02694c099f903fbdf26cc39db0b3/research_pushes/2026-09-30-fei-overlapping-product-0302z/CORRECTION.md) before claiming novelty. The [amended report](https://github.com/yspennstate/math-open-problems/blob/e894a01f20ba02694c099f903fbdf26cc39db0b3/research_pushes/2026-09-30-fei-overlapping-product-0302z/REPORT.md) also supplies a distinct seven-variable single-point-multiplier witness, with source-certified excess greater than 0.1630852002095. It is a proof-route counterexample, not a classical FEI counterexample; publication priority is unverified.

**Stop before retrying:** do not use the broad entropy triangle inequality, even for a chosen one-point flip, or repair it by an absolute additive constant (tensor amplification defeats that). The amended report also rules out a fixed multiple of the actual pivotal-overlap influence loss. These failures do not refute disjoint additivity, translation-averaged subadditivity, or the valid +2k bound when at most k physical variables are shared. A useful averaged argument still needs to reconstruct the original function and pay one consistent influence ledger; choosing unrelated favorable entropy and energy translates is invalid.

Supplemental provenance: prior directional-compression blob 011865c0e85cc90c8af59bd9033173603ee5ebe0; amended product report blob 76734ba5f15292f83784573271517c61d039ffad; attribution-correction blob 0ba6bbec4662aa78e8a13f2ffc9cc3d4a4821f6e. The later two were read at math-open-problems commit e894a01f20ba02694c099f903fbdf26cc39db0b3. External preprint version is pinned to v1; this is source-backed research status, not a claim of peer review or full independent certification.

---

### 9.1 Exact product-spectrum rigidity is prior work; its stability gap remains

**PROVEN, recovered September 21.** If the squared Fourier law of a genuine Boolean function is a product law, every coordinate marginal lies in `{0,1/2,1}`, the number of fair coordinates is even, and, after removing irrelevant coordinates, the function is a character times a bent function. Consequently `H=|A|`, `I=|D|+|A|/2`, and `H<=2I` sharply. Read both [account01/B18 classification](https://github.com/yspennstate/math-open-problems/blob/933891c27be3104c3a6f6e310f2db388d193a123/proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260921T095921Z-product-spectrum/REPORT.md) and [account03/B13 rigidity proof](https://github.com/yspennstate/math-open-problems/blob/933891c27be3104c3a6f6e310f2db388d193a123/proofnet24/P03-fei/fleet-2026-09-21/account03/B13/20260921T183113Z-product-spectrum-rigidity/REPORT.md) before calling the zero-address endpoint new.

The prior [account02/B18 product-phase theorem](https://github.com/yspennstate/math-open-problems/blob/933891c27be3104c3a6f6e310f2db388d193a123/proofnet24/P03-fei/fleet-2026-09-21/account02/B18/20260921T103159Z-product-phase-kl-stability/REPORT.md) already gives quantitative information. For actual Boolean amplitudes `a`, same-sign product-reference amplitudes `b`, `t=||b-a||_2^2`, and `R_U=<b,T_U b>`,

    sum_(U nonempty) (|R_U|-t)_+^2 <= 4t,
    TC(P)=D_2(P||Q) >= t/ln 2 >= Phi(R)/ln 2,

where `Phi` is the nonnegative root of the corresponding threshold equation. The Fourier phase also has exact curl-free derivative signs. These are proved necessary constraints, but `t<=2`: Hellinger-scale separation does not itself pay the dimension-growing KL/rare-coordinate entropy deficit. Exact rational-square rigidity supplies no uniform approximate-product stability as denominators grow. **OPEN:** the required KL-scale or collective payment.

### 9.2 Independent audits pass the mathematics; old floating exports are not certificates

The [convolution/product audit](https://github.com/yspennstate/math-open-problems/blob/933891c27be3104c3a6f6e310f2db388d193a123/research_pushes/2026-09-30-fei-convolution-product-audit-0321z/AUDIT.md) independently checked the analytic tensor, support-loss, completion, surgery, product-counterexample and averaged-ledger arguments in Sections 4 and 8.2, and replayed the exact acceptance arithmetic. It does **not** prove the proposed universal normalized KL payment. Its initial treatment of floating serialization was subsequently corrected; read the [mandatory serialization addendum](https://github.com/yspennstate/math-open-problems/blob/55b0ce947fb829dbd1726655e0b407e98c3511fd/research_pushes/2026-09-30-fei-convolution-product-audit-0321z/SERIALIZATION_CORRECTION.md) alongside the original PASS.

**CORRECTION:** the old nearest-rounded JSON `*_interval` pairs in the convolution, overlapping-product, and Hadamard packages can exclude the true value. Reproducing their bytes does not certify their endpoints. The intermediate `ada352231ccb4f37bf8faa54112a07e2213bd399` repair checked binary containment only and still did not certify exact decimal tokens. Preserved audit inputs, including the old `product/witness.json` display metadata, retain their historical defect.

The final [dual-semantics repair](https://github.com/yspennstate/math-open-problems/blob/67c4459ae0e8ae85a228c7a5c2629f003910139b/research_pushes/2026-09-30-fei-output-enclosures-0335z/CORRECTION.md) at commit `67c4459ae0e8ae85a228c7a5c2629f003910139b` verifies **both** exact binary64 values and serialized JSON decimal text against the rational enclosure, stepping outward as needed. Independent replay checked all 15 convolution exports, 31 product exports, and four product witness interval fields under both interpretations, with exact regenerated-output equality. The separately audited Hadamard replay checked all 20 emitted pairs. The corrected seven-variable excess interval is `[0.16308520020956166, 0.16308520020956171]`; its exact conservative lower bound `>0.1630852002095` is unchanged.

Use the corrected [convolution output](https://github.com/yspennstate/math-open-problems/blob/67c4459ae0e8ae85a228c7a5c2629f003910139b/research_pushes/2026-09-30-fei-normalized-convolution-0236z/verification.json), [product output](https://github.com/yspennstate/math-open-problems/blob/67c4459ae0e8ae85a228c7a5c2629f003910139b/research_pushes/2026-09-30-fei-overlapping-product-0302z/verification.json), and [Hadamard output](https://github.com/yspennstate/math-open-problems/blob/67c4459ae0e8ae85a228c7a5c2629f003910139b/research_pushes/2026-09-30-fei-hadamard-rounding-0330z/verification.json) for exported bounds. The analytic proofs and internal exact rational acceptance comparisons were unaffected; earlier exported floats are not retroactively certified.

**PROVEN scoped Hadamard obstruction.** The [multilayer report](https://github.com/yspennstate/math-open-problems/blob/f1ce20b4735afbe2b0aaedf32bf2fc2cdd0f51d1/research_pushes/2026-09-30-fei-hadamard-rounding-0330z/REPORT.md) and [independent audit](https://github.com/yspennstate/math-open-problems/blob/b0997dbcf4e1e51a4ab1efeb226217ef78b951d0/research_pushes/2026-09-30-fei-hadamard-independent-audit-0333z/AUDIT.md) prove that for a flat real orthogonal final layer, an independent unit input vector, independent uniform sign data, and disjoint length-r parity controls, scalar sign-rounding incurs

    I_control >= [r/(2 sqrt(6))] sqrt(L/ln(4L)).

This is uniform over preceding layers. The unrounded linear-control function is Boolean exactly when its coefficient vector is one-hot. In the specified quantum-inspired degree split, the rounded influence grows at least as a constant times `sqrt(d) 3^(d/4)` asymptotically. Independence, flatness and disjoint controls are essential. No entropy upper bound for the entire rounded family, obstruction to every classicalization, or classical FEI theorem follows.

### 9.3 Entropy-priced spectral wringing: exact coupling retained, collective payment unpaid

**PROVEN.** For any finite bit law `X` and `0<eta<1`, the [entropy-wringing theorem](https://github.com/yspennstate/math-open-problems/blob/0add87669946788d041f3ee5e2f27ec10316c90b/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/REPORT.md) selects one deterministic spectral-coordinate set `A`, with `R=A^c`, such that

    H(X_A) <= DTC(X)/eta,
    TC(X_R|X_A) <= [eta/(1-eta)] H(X_R|X_A).

This is an averaged conditional-TC bound, not a claim for every branch or a physical restriction algorithm. On an actual ratio-critical Boolean source, the prior criticality ledger gives `DTC<=c0 I`, `c0=2/ln 2`, so the address costs at most `c0 I/eta`. The optional all-block influence estimate requires ratio maximality over **all physical descendants**, not only immediate children; the [analytic review](https://github.com/yspennstate/math-open-problems/blob/0add87669946788d041f3ee5e2f27ec10316c90b/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/AUDIT.md) records this correction.

For partial Walsh projections `g_T(x)=E_y f(y,x)chi_T(y)`, weights `w_T=||g_T||_2^2`, and normalized squared laws `q_T`, full Booleanity retains the **pointwise all-shift** identities

    sum_T g_T(x)g_(T xor U)(x)=1_(U empty).

The explicitly sufficient collective target remains **OPEN**:

    sum_T w_T H(q_T)
      <= K[I_R(f)+H(w)] + L sum_T w_T TC(q_T)

for universal finite `K,L`. The source proves that such a statement would imply full FEI. It does not prove the statement or show it easier than FEI.

**REFUTED component replacement.** The [component obstruction](https://github.com/yspennstate/math-open-problems/blob/0add87669946788d041f3ee5e2f27ec10316c90b/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/COMPONENT_OBSTRUCTION.md) constructs bounded, exactly dyadic, actual Boolean partial means with exactly product normalized spectra for which

    H(q)/[I(g)/||g||_2^2 + log(1/||g||_2^2)] -> infinity.

Adding a multiple of `TC(q)=0` does not help. The other projections and the full address entropy remain uncharged; this is neither a counterexample to the collective target nor to FEI. Product rigidity for genuine Boolean functions cannot be applied separately to these multivalued projections.

**Physical-transfer guardrail.** The exact Boolean locking transform `L_g(z,t,x)=(-1)^(zt)g(x xor t*1)` has `H=H(g)+2`, `I=I(g)+1`, and unchanged DTC, but one physical z-query increases expected DTC by `B(g)` while `Inf_z=1/2`. It refutes an unconditional O(query-influence) DTC drift bound. That query is already affordable, with `Delta_z H/Inf_z=4`; critical-only or stop-on-certified-function rules are not refuted. The clipped-potential obstruction is only for slopes admitted by the source's explicit seed criterion, not arbitrary slopes such as 100.

### 9.4 One spectral address bit is solved exactly; two bits already break constant two

**PROVEN endpoint.** The [one-bit theorem and two-bit boundary](https://github.com/yspennstate/math-open-problems/blob/2591d8acb920ca59230530761efa3113bea2167a/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/ONE_BIT_ENDPOINT.md) show that a unit dyadic amplitude vector whose remaining squared law is product after conditioning on one spectral bit satisfies `H<=2I`. In particular this holds for actual Boolean spectra. A nonzero dyadic product-amplitude vector has squared norm with reduced odd numerator congruent to 1 modulo 4. Two positive such norms summing to one must both be 1/2, forcing all nondegenerate conditional marginals to be fair. This is an exact arithmetic extension, not approximate stability.

**REFUTED extension with the same constant.** The source gives an actual six-variable Boolean function with two spectral address bits, address masses `(5/8,1/8,1/8,1/8)`, and product conditional spectra in all four components, but

    H=5, I=17/8, H/I=40/17>2.

Its influence vector is `(1/4,1/4,1/2,1/2,1/2,1/8)`. The full spectrum has eight atoms of mass 1/16 and thirty-two of mass 1/64. This refutes only the constant-two arbitrary-address extension, not another finite collective constant, address-entropy payment, or FEI.

The proof was independently reviewed; the exact finite [endpoint verification](https://github.com/yspennstate/math-open-problems/blob/2591d8acb920ca59230530761efa3113bea2167a/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/endpoint_verification.json) exhausts all 65,812 Boolean functions in dimensions 1–4 for the distinguished spectral coordinate and separately verifies the six-variable witness. These are supporting checks, not the all-dimensional proof or formal certification. The original three wringing reports are on master; this endpoint and the executable package are on **unmerged draft [PR #12](https://github.com/yspennstate/math-open-problems/pull/12)**, pinned here at `2591d8acb920ca59230530761efa3113bea2167a`. Read the pinned files; the original PR body predates the four endpoint additions.

---

### 9.6 Signed-noise positive parts are proved; spectral entropy transfer is not

The revised [signed noisy-derivative lemma](https://github.com/yspennstate/math-open-problems/blob/121f0b540e497b97e92d7ced06efd7b384bdf32a/research_pushes/2026-09-30-fei-signed-noise-0359z/REPORT.md) at `121f0b540e497b97e92d7ced06efd7b384bdf32a` uses **natural logarithms**, actual signed Boolean derivatives, `b_i=||T_r d_i f||_1`, and the source's nonnegative resolvent weights `z_i,U,Z`. For `0<r<=1`, `gamma>0`, it proves the stronger coordinatewise positive-part statement

    sum_i [z_i ln(z_i/b_i^2)]_+ <= 2(gamma+1)(U-Z).

Zero derivatives are omitted from logarithms. Coordinatewise nonnegative Dirichlet energy justifies the positive parts even though the signed logarithmic summands can be negative; the first archived limitation on positive parts was corrected. In the r=1, gamma-to-infinity limit, with `c_i=sum_(S contains i) p_S/|S|`, it gives

    sum_i [c_i ln(c_i/Inf_i(f)^2)]_+ <= 2(I(f)-Var(f)).

This is physical-space entropy/influence control. No coefficientwise spectral-entropy transfer, identification with the mismatch/KL packets of Section 2, or nonreusing multiscale payment is proved. The source credits the positive smoothing calculation of Mahdavifar–Beirami and standard Gross/Talagrand/Falik–Samorodnitsky mechanisms; it does not certify the cited paper's full Courtade–Kumar claim. Analytic proof only; no executable certificate or novelty determination is claimed.

### 9.7 Low-influence reduction credit and reuse boundary

The [low-influence source note](https://github.com/yspennstate/math-open-problems/blob/ecc6da6b0c2514fd885bd2c4de03eb6f26f13f3b/research_pushes/2026-09-30-fei-log-allocation/LOW_INFLUENCE_SOURCE_NOTE.md) credits Shalev, arXiv:1806.03646v2, Theorem 3 and Section 3.2: a universal FEI theorem on `I(f)<=2^(-s(n))`, `s(n)=o(n)`, already implies full FEI; the activation construction is attributed there to Wan–Wright–Wu. Thus neither the general low-influence hardness principle nor tensor-plus-activation is new here. Section 4's particular normalized-collision premise, constants, and exact full-support perturbation remain unchanged, with the premise still unproved.

**Before a new attempt:** retain the actual signed joint Boolean constraints, distinguish a spectral address from a physical query, apply the strongest prior product/mismatch results at their valid scope, use the final dual-semantics exports, and state the new missing implication. Independent analytic review, exact finite arithmetic, floating regression, formal verification, remote delivery, merge state and downstream use remain separate evidence tiers. All research-source links in this addendum are immutable; PR links report delivery only. Publication priority remains unverified throughout.

---

### 11.13 Direct trajectory budget and the actual biased-Boolean remainder

**PROVED, arbitrary real initial states.** The [integrated trajectory package](https://github.com/yspennstate/math-open-problems/blob/c63180b23321ce9130dbcbab825546f6c14923d0/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/INTEGRATED_INFORMATION.md) observes independent rate-one clocks on the latent occupied Fourier coordinates. Conditional amplitudes retain their actual real signs. In natural units, the zero-safe secant lemma gives T<=K<=T+3J, where T is the physical-density entropy generator. The exact active-energy decay and finite-horizon identity imply

    integral E K(h_t)dt<=3I(g)-Ent(g²).

No product-spectrum hypothesis is needed. Spectral entropy has the exact clock-information integral H(P)=integral E sum q_i ln(1/q_i)dt, credited to the checked Poisson-channel source and also derived directly. The independently derived no-click subpath bound is at most2I+Var−Ent(g²). Neither integrated statement bounds the initial/terminal K by a universal multiple of I.

**Full-scope gap is explicit.** For Boolean initial f the true integrated conditional cost C_path obeys H_nat(f)−3I<=C_path<=H_nat(f)+I. Paying it linearly is FEI-equivalent and remains open. The trajectory states are generally real multivalued wavefunctions, not Boolean physical restrictions. At fixed time their averaged physical density is identically one, but that zero-shift condition alone is insufficient.

**Retain the history refund.** [The exact history note](https://github.com/yspennstate/math-open-problems/blob/c63180b23321ce9130dbcbab825546f6c14923d0/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/BOOLEAN_HISTORY_REFUND.md) expresses C as the pivotal Jensen envelope minus conditional information in the actual record. On AND_n the envelope grows like nI while the true cost is O(I). The prephysical record refund integrates to TC(P)+an error in[0,I], but the full refund also contains actual K minus the no-history physical information Kbar. Kbar itself can be order nI and cannot be dropped. The AND leading constants and their integrable domination are recorded; this is an overcharge guard, not a new FEI bound.

**Stronger source structure, not independent sphere rows.** In [the biased-Boolean structure note](https://github.com/yspennstate/math-open-problems/blob/c63180b23321ce9130dbcbab825546f6c14923d0/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/BIASED_BOOLEAN_STRUCTURE.md), the fixed-time clicked set A is sufficient; detailed click times are ancillary given A. With theta=1−exp(−t), its unnormalized amplitude b_A(x) is exactly the biased Fourier coefficient of the actual Boolean function eta↦f(x eta), where E eta_i=sqrt(1−theta). Thus mu_theta^x(A)=b_A(x)² obeys the complete weighted biased product identities, and all x-rows are translates of one f. The exact C functional uses adjacent coefficients, or equivalently the biased transforms of actual complementary ternary pairs.

A proved sufficient reduction retains this structure:

    H_nat(f)<=(4+2ln2)I(f)+Q_bias(f),
    Q_bias=integral_0^1 E_x[sum_i H_mu_theta^x(A_i|A_-i)] dtheta/theta.

The integral is still unpaid. Its integrand is the full conditional-entropy sum of the actual biased-Boolean law, not TC or the unconditional thinning marginal. The independently checked reverse inequality now gives |Q_bias−C_path|<=(1+2ln2)I, hence H_nat−(4+2ln2)I<=Q_bias<=H_nat+(2+2ln2)I. Thus this is an FEI-equivalent bank, not an oversized proxy. Characters give Q_bias=(pi²/6)I as a normalization check. This does not establish the retired universal pointwise erasure bound.

Parent and maintainer independently reviewed the analytic notes. The16 fixed trajectory fixtures and the exhaustive exact Fraction structure checker were independently replayed byte-identically; the latter checks4,244 translated rows,33,316 weighted-shift identities and49,680 adjacent derivatives through n3 at two rational biases. Those are algebraic checks, not numerical verification of the time-integral theorem or the missing C/Q_bias payment. All files remain on unmerged draft PR12.

The [updated physical-restriction ledger](https://github.com/yspennstate/math-open-problems/blob/c63180b23321ce9130dbcbab825546f6c14923d0/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/EXTENDED_NOISE_LEDGER.md) separately retains the address-information refund: E TC_leaf+HA_root−E HA_leaf<=TC_root+c0(IR_root−E IR_leaf). This is the same actual-posterior telescope, not another independently reusable budget.


### 11.14 Adaptive correlation payment and exact lattice-noise transport

The [adaptive-minority ledger](https://github.com/yspennstate/math-open-problems/blob/9c2692e18b9e1519610467158172540a8d00247d/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/adaptive-minority/ADAPTIVE_MINORITY_LEDGER.md) uses rate-one clocks with a predictable selected minority outcome. Choices reset after clicks and on a finite mesh of spacing at most1/(100n); selected posterior probabilities stay below0.51. The exact DTC generator and a checked Bernoulli-to-Poisson comparison prove, in natural units,

    integral E[TC(P_t)+DTC(P_t)]dt<=4DTC(P_0).

The selected-energy budget and integrated K theorem survive. On the separately established admitted critical Boolean sources, this gives at most8I for the integrated posterior correlation reserve. Same-sign product references consequently have paid integrated L2/Hellinger error. They need not be Boolean or share the source's history, and no dimension-free entropy transfer follows. The averaged channel remains ordinary dephasing in the original frequency labels; the old clicked-set/product-basis description is not automatically valid under feedback. Root, peer and maintainer analytic reviews and byte-identical26 scalar/12 generator/9 channel checks are recorded. Coarse finite channel fixtures are not substitutes for the finite-mesh proof.

[Sections7–8 of the integer-norm source](https://github.com/yspennstate/math-open-problems/blob/9c2692e18b9e1519610467158172540a8d00247d/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/INTEGER_NORM_PRODUCT.md) add exact common-odds transport. If a product law satisfies H_nat<=cJ+B, then under p_i(s)=sp_i/(1−p_i+sp_i),

    H_nat(P_s)<=[c+ln(1/s)]J_s+beta_c(s)B,
    beta_c(s)=s/[1−(1−s)p_c], h(p_c)/p_c=c.

The signed threshold comparison permits negative B. With the integer-norm theorem, a lattice surcharge decays as O(s). This requires an exact-product pre-tilt ancestor and fixed-direction common attenuation; it does not cover arbitrary anisotropic feedback or approximate-product ancestors.

A genuine restricted-class consequence follows without a row-energy cutoff: if every nonzero demodulated first derivative of a Boolean f has exact product spectrum, the first-mark raw-entropy correction cancels the logarithmic-noise energy exactly. The theorem is H_bits(f)<=[12/5+4/ln2]I(f). Arbitrary Boolean derivatives need not satisfy its hypothesis. Root, peer and maintainer checked the raw/normalized ledger and endpoints;80 signed transport cases and102 qualifying Boolean cases through n3 were independently replayed with exact rational-log output.

Scoped guards at this same draft head remain explicit. The [true-history profile certificate](https://github.com/yspennstate/math-open-problems/blob/9c2692e18b9e1519610467158172540a8d00247d/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/profile-stress/PROFILE_STRESS.md) refutes coefficient1 only, not all constants; its bounded scans are diagnostic. [Parity-inflated addressing](https://github.com/yspennstate/math-open-problems/blob/9c2692e18b9e1519610467158172540a8d00247d/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/PARITY_ADDRESS_LOG_BANK.md) refutes an unmarked logarithmic bank without a TC correction, not the actual full-trajectory cost. The [near-vacuum signed-rotation reduction](https://github.com/yspennstate/math-open-problems/blob/9c2692e18b9e1519610467158172540a8d00247d/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/uniform-vacuum/EXCEPTIONAL_ROTATION_REDUCTION.md) pays its good region by17D and leaves an explicit exceptional positive bank unpaid.

The current full-scope obligation is still an actual-source entropy/history payment or a valid entropy-stable transfer spending the integrated correlation reserve once. Neither the correlation budget nor exact arithmetic transport supplies that missing implication. All additions remain on unmerged draft PR12; the latest26 changed files were exactly read back, and the local hash audit covers159 manifest entries/158 unique files.

### 11.15 Pointwise restoration limits and explicit source-aware criteria

**Pointwise Hellinger transfer needs more than the paid reserve.** The [real-state bent/spike guard](https://github.com/yspennstate/math-open-problems/blob/b1b9d08716766c3ef373de8350867ccae5314755/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/adaptive-minority/HELLINGER_TRANSFER_OBSTRUCTION.md) has common marginal energy J, bounded TC and a same-sign marginal-product reference, but C(h)−C(reference) is order J while sqrt(J TC)+TC is only order sqrt(J). Thus no fixed coefficient on that error gives a universal pointwise comparison, even with a fixed multiplier on the reference cost. An additive C J term is not refuted. The [separately reviewed optional embedding](https://github.com/yspennstate/math-open-problems/blob/b1b9d08716766c3ef373de8350867ccae5314755/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/adaptive-minority/OPTIONAL_HISTORY_EMBEDDING.md) realizes the same failure on an actual all-one no-click history of the finite-mesh minority policy. A dyadic completion near Maj17 and address parity inflation keep every selected marginal below one-half. Its original source H/I tends to zero, so neither high-ratio criticality nor integrated source-influence payment is contradicted.

**A positive inverse theorem keeps its actual prices.** The [source-aware inverse note](https://github.com/yspennstate/math-open-problems/blob/b1b9d08716766c3ef373de8350867ccae5314755/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/adaptive-minority/inverse-noise/INVERSE_NOISE_GUARD.md) proves normalized recovery error at most the undamped source tail plus kappa² TC, with kappa the exact inverse condition number. Degree-weighted recovery additionally retains the source energy tail. Grid rounding loses degree, and exact low-degree decoding restores the actual source without proving product structure. The [arithmetic criterion](https://github.com/yspennstate/math-open-problems/blob/b1b9d08716766c3ef373de8350867ccae5314755/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/adaptive-minority/inverse-noise/PRODUCT_RIGIDITY.md) supplies one severe sufficient repair: a nonproduct probability law with atoms on a 1/M grid is at TV distance at least1/(3M²) from every product law. Full inverse error below1/(36M^4) therefore forces the actual low-degree grid source's spectrum to be exactly product. This threshold explicitly requires inverse conditioning and the full inverse-reference tail; the integrated TC budget does not supply them.

**Actual Boolean controls defeat an unpriced shortcut.** For the four-bit one-point flip, every ordinary degree truncation of the full inverse product reference rounds to the constant+1 at sufficiently late no-click times, with squared source error1/4 despite TC tending to zero. Its late branch has probability at least49/64; unweighted source-reconstruction error has infinite time integral. This is distinct from the current-amplitude error. The [dimension-growing point-flip control](https://github.com/yspennstate/math-open-problems/blob/b1b9d08716766c3ef373de8350867ccae5314755/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/adaptive-minority/inverse-noise/POINT_FLIP_SURPLUS.md), with r=n^−3, has TC/J tending to zero but H/J−ln(1/r) growing as2n ln2. It refutes adding only sqrt(J TC)+TC to the common-noise log-time bound for arbitrary approximately product Boolean ancestors. The sources are actual and their paths follow minority selection, but adjusted criticality is not claimed.

**Approximate Booleanity and positivity are still insufficient.** The [compact positive-source guard](https://github.com/yspennstate/math-open-problems/blob/b1b9d08716766c3ef373de8350867ccae5314755/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/adaptive-minority/critical-source-guard/POSITIVE_PROXY_GUARD.md) reuses the earlier random-sign product component to build one positive, uniformly near-Boolean real source with DTC=o(I), squared full-convolution defect=o(I), and the paid adaptive K/correlation reserves, yet C_integral/I diverges. It is not Boolean. The [critical-source interface](https://github.com/yspennstate/math-open-problems/blob/b1b9d08716766c3ef373de8350867ccae5314755/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/adaptive-minority/critical-source-guard/CRITICAL_SOURCE_INTERFACE.md) retains the exact indicator block ledger, its immediate consequence q_i<=exp(3−rho), and an alternative proof of the already known indicator-product classification. These are scope controls and recovered consequences, not a new constructive payment.

Root, peer and maintainer analytic reviews are recorded with the precise source hypotheses. The maintainer's isolated replays matched all final outputs byte-for-byte: seven rational-log bent/spike cases; thirteen four-bit noise cases; forty-two compressed point-flip dimensions;27,540 rational-law comparisons and32,640 Boolean spacing pairs; and the exact65,536-atom positive-source fixture. Numerical entropy columns remain diagnostic where labeled. All23 files changed in this final batch were exactly read back at draft PR12 head b1b9d08716766c3ef373de8350867ccae5314755; the local manifest audit found176 entries/176 unique files and zero mismatches. The draft remains unmerged. Full FEI, actual critical-source entropy restoration and the equivalent C/Q_bias payment remain open.

### 11.16 Actual-Boolean endpoint and the source-aware interval ledger

The [near-product Boolean endpoint](https://github.com/yspennstate/math-open-problems/blob/973b5214bae8803f3351fba42b130757b348cbda/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/boolean-product-endpoint/REPORT.md) explicitly invokes the credited KKLMS Theorem1.3, after checking its indicator/sign conventions. An elementary Gibbs estimate for any binary law P and its marginal product gives E[N ln(N+1)]<=J ln(J+1)+32J+2TC(P). Consequently a genuine Boolean sign source satisfies

    H_nat(f)<=C[I(f)ln(1+I(f))+I(f)+TC(P_f)],

for a universal constant inherited from the published theorem. When I<=1, this becomes H<=C'(I+TC). This is a real stopping endpoint if an actual Boolean source with TC=O(I) can be produced. It does not apply the imported Boolean theorem to multivalued projections or trajectory fields. The primary statement and normalization were independently read; the rational checker certifies only the elementary moment constants. The recovered September23 W3-04 KKLMS barrier/reference-charge report is explicitly credited without a novelty claim.

The [full-trajectory density note](https://github.com/yspennstate/math-open-problems/blob/973b5214bae8803f3351fba42b130757b348cbda/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/integrated-density/REPORT.md) preserves a different positive fact. For bounded real g with M=||g||infinity and g_s=T_sqrt(s)g,

    integral_0^1 ||g_s||²[H(P_s)+TC(P_s)] ds/s
      <=2I(g)+Var(g)−Ent(g²)+4ln2 M TV(g).

Thus one source-aware no-click episode is paid by(3+4ln2)I for Boolean g, or(3+8ln2)I for scaled-ternary g. A nonreusing sum over clicked ancestors is not established.

The same note refutes the proposed full-trajectory TV replacement using the actual Boolean ordinary-address function x_y, with a address bits. Its minority orientation is genuinely compatible with the fixed tie-one policy. The complete trajectory's integrated squared-density TV is at least(6/5)^a/36, while I=a/2+1, integrated posterior TC<=1, integrated DTC=a ln2, and actual C is O(a). Adding either paid correlation reserve therefore does not repair that surrogate. This is a complete-history obstruction, distinguished from the older static and first-mark banks; high-ratio criticality is not asserted.

Root and maintainer independently read both arguments and replayed the checkers byte-identically. The density checker covers3 actual truth tables,9 rational-noise values and252 record fields; the endpoint checker verifies its stated rational constants rather than the imported theorem. All eight files were exactly read back at unmerged draft PR12 head 973b5214bae8803f3351fba42b130757b348cbda. The constructive gaps remain actual-Boolean entropy restoration and a nonreusing interval/history refund; no unrestricted C payment follows.

### 11.17 Common-forward-noise protocol and nonreusing global-time refunds

The [single forced-reveal protocol](https://github.com/yspennstate/math-open-problems/blob/fb2d580aae3a83e4dcf358b29525d56a569f227d/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/forced-reveal/REPORT.md) keeps rate-one observations of Fourier bit1 throughout. Whenever an active posterior marginal reaches2/3, it fully reveals that bit and removes it, including the zero outcome. Threshold cascades are finite because every event removes a coordinate. No selected label is reversed. Every positive-probability history is therefore common forward noise T_exp(−t/2) of an actual dyadic E_B D_A projection of the original Boolean source. The active field itself need not be Boolean or quantized, and physical-density flatness is not asserted for this policy.

All structural costs remain paid. In natural units, integral E(TC+DTC)<=6DTC_initial; the integrated K budget is at most3J0−F0−Q_forced; total expected removals are at most1.5J0; forced-bit entropy is at most kappa Q_forced with kappa=h(2/3)/(2/3)<1. Retaining that negative forced-energy reserve gives the same full-scope C comparison H_nat−3I<=C_integral<=H_nat+I for Boolean initial sources. Thus C payment remains FEI-equivalent and open.

The [global-time refund companion](https://github.com/yspennstate/math-open-problems/blob/fb2d580aae3a83e4dcf358b29525d56a569f227d/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/forced-reveal/GLOBAL_TIME_REFUND.md) resolves one concrete reuse issue. With a(t)=EJ_t and the forced-loss measure mu(d tau)=E sum_forced q delta_tau,

    a(t)=e^(−t)J0−integral_[0,t] e^(−(t−tau))mu(d tau),
    integral t a(t)dt=J0−integral(tau+1)mu(d tau),
    integral e^tau mu(d tau)<=J0.

It also proves the complete Laplace family and the sharper discounted-grid count integral e^(−t)E k_t dt<=J0/2+integral e^(−tau)mu(d tau). These use the one original time axis, not a fresh energy charge for each derivative ancestor. The positive-exponential forced-loss bound does not control inverse amplification of degree greater than one.

For histories with exact product spectra, the integer-norm/common-odds theorem gives the price L_t=[(12/5)ln2+t]J_t+(4/5)ln2 e^(−t)k_t. The entire integral of this price plus forced-bit entropy is at most[1+(14/5)ln2]I of the original Boolean source, with an explicit nonnegative forced-energy refund. This pays the logarithmic-time and inherited-grid terms together.

The remaining obligation is exact and still unpaid: the signed integrated arithmetic error E_arith=integral E[H(P_t)−L_t]dt. The actual entropy identity yields H(P0)<=[1+(14/5)ln2]I+6DTC(P0)+E_arith. On the admitted critical sources, the first two terms are linear in I. No bound for E_arith, no replacement by its positive part, and no generic approximate-product stability are proved. The actual point-flip no-click guard remains compatible with this protocol and still excludes the pointwise shortcut.

Root and peer independently read the complete protocol and refund proof. The maintainer replayed the corrected final structural checker byte-identically:278 Boolean tables,17,814 positive projection/noise and generator cases,19,116 forced-energy checks and121 distinct cascades. This checker does not certify continuous stopping-time entropy integrals. All five package files were exactly read back at unmerged draft PR12 head fb2d580aae3a83e4dcf358b29525d56a569f227d. The new result is the source-preserving protocol and nonreusing cost ledger, not an unrestricted FEI bound.

### 11.18 Audited ternary-source degree-log and near-product endpoint

The [scoped ternary extension](https://github.com/yspennstate/math-open-problems/blob/84b0d71fee51f9f514cf65cedada10be391c90e2/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/boolean-product-endpoint/TERNARY_SOURCE_EXTENSION.md) adapts the credited KKLMS proof to an actual source u taking values in {−1,0,1}. In natural units, for a universal finite constant,

    Hraw(u)<=C[I(u)+sum_S |S|ln(|S|+1) uhat(S)^2].

For nonzero u, writing w=||u||², P=uhat²/w and J=I(u)/w, the already proved centered-Gibbs degree-moment estimate yields

    H(P)+ln(1/w)<=C'[Jln(1+J)+J+TC(P)].

Thus J<=1 gives a dimension-free ternary-source endpoint. For scaled-ternary g=a u, retain the norm surcharge ln(a²/||g||²). Heat-smoothed fields and general many-bit Fourier projections are not thereby ternary.

The [complete independent dependency audit](https://github.com/yspennstate/math-open-problems/blob/84b0d71fee51f9f514cf65cedada10be391c90e2/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/boolean-product-endpoint/TERNARY_DEPENDENCY_AUDIT.md) checks every Boolean-specific source use through primary Sections2–6 and7.1. The intermediate half-integer alphabet is uniformly bounded and closed under restrictions and parity substitutions; its first half-differences have minimum nonzero magnitude1/4. It is used only for the positive-degree two-function estimate. A nearest-integer centering and quantized Gross bound replace the indicator variance argument, while the empty atom is paid only after returning to original ternary u. The constant intermediate source1/2 still refutes any unqualified energy-only raw-entropy claim.

The adaptation explicitly uses the conservative exponent1/32 from the primary proof, rather than the displayed1/16, and supplies a finite-small-degree base-case repair. Root read the complete corrected adaptation and dependency audit and checked their arguments; root is not represented as having independently reread every primary dependency. Both root and maintainer isolated elementary replays byte-matched25 alphabet edge pairs and6,654 ternary truth tables. These check only the stated elementary claims, not the multiscale proof. All six additive/updated package files were exactly read back at unmerged draft PR12 head 84b0d71fee51f9f514cf65cedada10be391c90e2. No arbitrary-integer, filtered-state, approximation-stability, novelty or full-FEI claim is made.

### 11.19 Decaying thresholds, signed episodes and paid amplified-correlation errors

The [separate decaying-threshold policy](https://github.com/yspennstate/math-open-problems/blob/b052f7ac40a2aef7e4768aa4f0d9836d6906b939/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/forced-reveal/DECAYING_THRESHOLD.md) keeps the same fixed outcome-one clocks, but fully reveals/removes a coordinate when q_i>=epsilon exp(−2t). It counts forced zeros and uses the one original time axis. Cascades are finite. Common forward-noise ancestry survives; the old unweighted removal-count bound and unconditional physical flatness are not asserted for this policy.

The exact forced-loss budget integral exp(tau)mu(d tau)<=J0 pays the needed discounted grid count integral exp(−t)E k_tdt<=(1/2+1/epsilon)J0. Forced-bit entropy is at most(2+ln(1/epsilon))J0; integral E(TC+DTC)<=4DTC_initial, and the integrated K bound retains its negative forced-energy term. The common-noise arithmetic time/grid price remains integrably paid, with only the signed arithmetic error left over. The inverse marginal-product reference has each source-side marginal p_i<epsilon exp(−t), which does not bound total excitation or inverse tails. An exactly product unresolved state has at most2(k−1)ln2/ln(5/2) active coordinates for k>=1 and is constant for k=0 or1. No stability of this arithmetic count is proved.

The [amplified-correlation companion](https://github.com/yspennstate/math-open-problems/blob/b052f7ac40a2aef7e4768aa4f0d9836d6906b939/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/forced-reveal/AMPLIFIED_CORRELATION_BUDGET.md) assumes epsilon<=exp(−2). Its scalar Bernoulli comparison and finite-horizon DTC integrating factor W(t)=exp(t)sqrt(ell/(ell+2t)), ell=ln(1/epsilon), yield

    integral [exp(t)/sqrt(1+t)] E TC(P_t)dt<=2DTC_initial,
    integral E sqrt[J_t TC(P_t)/s]dt<=2sqrt(J0 DTC_initial),
    integral E[TC(P_t)/sqrt(s)]dt<=2DTC_initial,  s=exp(−t).

The same bounds hold for the squared real-amplitude Hellinger error to the current marginal-product reference. These are nonreusing, full-trajectory error budgets. They do not prove a pointwise entropy comparison, bound TC/s or higher inverse-degree amplification, or restore an actual Boolean source. No terminal weighted-DTC vanishing assumption is needed.

The [signed discounted-episode identity](https://github.com/yspennstate/math-open-problems/blob/b052f7ac40a2aef7e4768aa4f0d9836d6906b939/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/forced-reveal/DISCOUNTED_SIGNED_EPISODE.md) retains the physical entropy derivative, derivative-square entropies and zero-safe secant remainder before integration. It handles all discount exponents alpha>=0 and gives exact zero cancellation on pure characters. Its coarse2I(g) bound still cannot be summed over derivative ancestors as a fresh source budget.

Root and maintainer independently read all three notes and replayed the snapshot checker byte-identically:278 Boolean tables,35,628 positive fields,2,424 cascade states,2,172 forced-energy checks and196 exact-product leaves. The checker is exact finite arithmetic, not a simulation or certification of continuous entropy integrals. All six files were exactly read back at unmerged draft PR12 head b052f7ac40a2aef7e4768aa4f0d9836d6906b939. The substantive remaining step is a source-sensitive entropy transfer compatible with these paid error budgets; full FEI remains open.

**Actual-history pointwise guard.** The reviewed [ordinary-address history construction](https://github.com/yspennstate/math-open-problems/blob/ace905b4a46723714396d75aa3d96c3f638d0fb7/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/forced-reveal/ADDRESS_HISTORY_GUARD.md) is an actual branch of the same decaying-threshold policy. Its initial forced address observations produce degree-one ancestors with H=a ln2, J=1, TC<=1, grid2^(1−a), and k=a until the data threshold. At s=a^(−1/(beta+1)), these histories refute every fixed-coefficient pointwise comparison by (1+t)J, sk and s^(−beta)[sqrt(J TC)+TC], for any fixed finite beta>=0. Actual source ancestry and degree one do not make that shortcut valid.

The aggregate source remains low-ratio and all paid budgets hold: discounted count is exactly a+1/2+1/(2epsilon), the two amplified-correlation integrals are each at most2, and the specific signed arithmetic residual is only(1/5)a ln2+O_epsilon(1)=O(I). No integrated, high-ratio-critical or separately low-cardinality target is refuted. Root and maintainer each read and checked the full analytic note. The note and updated manifest were exactly read back at draft PR12 head ace905b4a46723714396d75aa3d96c3f638d0fb7.

### 11.20 Stronger TC/s endpoint: exact remainder and paid zero-outcome dissipation

The [independently reviewed Gamma ledger](https://github.com/yspennstate/math-open-problems/blob/4002dfdd471e6130f138bfa161cda21f6ef23ccf/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/forced-reveal/GAMMA_ENDPOINT_LEDGER.md) examines the still-open stronger estimate integral E[TC(P_t)/s]dt=O(DTC_initial+J0) for the same decaying-threshold policy. With r_i=P(S_i=1|S_without_i), define Gamma=sum_i Ent(1−r_i). Then sum_i Ent(r_i)=TC+DTC−Gamma, so the exact full-horizon identity is

    integral e^t E TC(P_t)dt
      =DTC_initial+integral e^t E Gamma(P_t)dt
        −E sum_forced e^tau I(S_i;S_without_i|pre-reveal history).

The terminal term vanishes for each fixed finite source because post-cascade marginals satisfy q_i<=epsilon e^(−2t), bounding both DTC and TC by n h(epsilon e^(−2t)). The negative weighted forced-information term is retained.

A separate positive theorem pays Gamma's dissipation. For Gamma_i=(1−q_i)d_i(q_i), with d_i(q)=D(P_without_i|0 || (1−q)P_without_i|0+qP_without_i|1), its own one-click generator is −q_i(1−q_i)^2 d_i'(q_i). Convexity gives the rate-one bound up to q_i Gamma_i. Other-coordinate observations and full reveals decrease expected Gamma by KL chain rule. The note defines explicit nonnegative convexity and cross-observation losses Omega and Psi and proves

    integral e^t E(Omega+Psi)dt
      +E sum_forced e^tau Delta Gamma
       <=Gamma_initial+(epsilon/2)J0<=(1+epsilon/2)J0.

This is a nonreusing level/dissipation budget, not the weighted Gamma lifetime appearing in the exact TC endpoint. The uniform one-hot general-real law has J0=1 but lifetime Theta(log n), while DTC0=log n; it does not refute the proposed DTC0+J0 estimate. Its actual Boolean addressing realization has full original influence Theta(log n) as well. No counterexample or proof of the stronger endpoint was obtained in this bounded pass. The precise remaining obligation is the signed lifetime minus forced-DTC-information refund.

Root and trajectory researcher each read the full written proof and checked its zero-event conventions, right-continuous post-cascade states, generator and finite-horizon integration. No executable or formal certificate is claimed for this analytic note. The note and manifest were exactly read back at unmerged draft PR12 head 4002dfdd471e6130f138bfa161cda21f6ef23ccf; full FEI remains open.

### 11.21 Post-checkpoint primitive meshes: accounting with an unpaid boundary

The [reviewed primitive-source mesh note](https://github.com/yspennstate/math-open-problems/blob/942eb3d49efa16d36a1a716a846dfbae9c6bca41/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/forced-reveal/primitive-mesh/REPORT.md) is a separate exploratory continuation; it does not revise the completed 12:48 checkpoint or add a paid entropy endpoint. For the actual dyadic projection ancestor g, its primitive physical mesh delta is the gcd of its values, including odd factors. The tilted potential Phi_s=Ent((T_sqrt(s)g)^2)/||T_sqrt(s)g||²+ln(||T_sqrt(s)g||²/delta²) is tensor-additive and may be negative. Its exact full-reveal jump uses current posterior weights and includes the essential q t term from demodulation.

The ordinary generator gives C<=−G Phi+(t+2ln2)J, so the finite-horizon continuous contribution is paid by(1+2ln2)I. The signed forced-jump and terminal-potential expression remains unpaid. A no-further-click record need not have a constant undamped source; revealing every remaining label makes complete mesh increments telescope exactly to the original Fourier entropy. Calling that remainder a mesh budget would rename the unsolved obligation.

An actual ternary hole projection has zero starting primitive potential, but source-weighted mean potential creation tends to ln4 as its one-outcome probability tends to zero. Thus universal O(q) and O(h(q)) creation bounds fail. The note also checks ordinary-address calibration and exact tensor additivity, without an integrated or critical-source counterexample. Root and independent reviewer each read the complete proof and independently replayed its exact rational/logarithmic checker with byte-identical output:79 projected fields,237 snapshots,396 reveal identities,237 generator identities,669 mesh bounds,256 tensor pairs,7 hole cases and3 address cases. All four files were exactly read back at open, unmerged draft PR12 head 942eb3d49efa16d36a1a716a846dfbae9c6bca41. This is checked accounting and a failed-step guard, not full FEI or formal verification.

### 11.22 Restricted selector/parity history profile

The [reviewed heterogeneous selector/parity report](https://github.com/yspennstate/math-open-problems/blob/8558b63bfe2127873c4808da8c512814ab13b6b2/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/address-ensemble-profile/REPORT.md) proves the actual fixed-one-clock profile C_f(t)<=4ln2·e^(-t)(1+t)I(f) when every logical address bit is a parity on its own physical block and every leaf is a signed parity on a mutually disjoint nonempty data block. Arbitrary unequal lengths and finite disjoint tensor products are covered. The no-data-click ensemble pays the leaf-index surprisal once through address influence; its Jensen step uses independent parity characters with fixed odd squared amplitude.

This is a restricted continuous-history theorem, not an unrestricted profile, a new FEI class, or a novelty claim. Arbitrary Boolean leaves, overlapping blocks and the separate unreviewed clock-flux proposal are excluded. Root and an independent peer reviewed the complete proof, including the binary-entropy bound, and separately replayed the finite checker with byte-identical output:15 full/coarse histogram matches,331 coefficient identities,2 full physical tensor histories,465 positive fields and51,676 coordinate pairs. The finite entropy bounds use rational logarithm enclosures; they are not a formal or universal enumeration certificate. All four files were exactly read back at open, unmerged draft PR12 head8558b63bfe2127873c4808da8c512814ab13b6b2. The completed12:48 checkpoint is unchanged; full FEI remains open.

### 11.23 Clock-information lemma and overlapping-character selector profile

The separate [reviewed clock-flux extension](https://github.com/yspennstate/math-open-problems/blob/971fe8a485349a69914decb992000879acbc892e/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/scalar-information-remainder/integrated-trajectory/address-ensemble-profile/CLOCK_FLUX_AND_CHARACTER_SELECTORS.md) first records a general finite-vector classical lemma. With a fixed side channel Z and independent rate-one occupied-bit clocks, the information rate is a_Z(t)=E sum q_i ln(1/q_i), it is nonincreasing, and conditional thinning gives H(S|Y_t,Z)<=e^(-t)H(S|Z)+h(e^(-t))E|S|. The Poisson information-rate identity and concavity are credited to checked primary Atar–Weissman Section5.1 and its Guo–Shamai–Verdu2008 attribution; no novelty claim is made.

For actual selectors of distinct signed data characters, with disjoint parity address blocks, data-character supports may now overlap and an empty character is allowed. The explicit positive law averages all a address signs, including unused dummy signs for clicked blocks. It has H(S|Z_t)<=L ln2 min(t,1); joint concavity and orthogonality give the actual data-cost bound a_(Z_t)(t)+e^(-t)Kbar. This proves C_f(t)<=4e^(-t)(1+t)I(f), also for finite disjoint tensor products. These already-flat-spectrum sources are not claimed as a new FEI class.

The remaining full-scope difficulty is the low conditional-entropy bound together with payment by actual address influence. Positive hybrid laws on disjoint physical-address/Fourier-data factors exist more generally, but general Boolean leaves can retain large spectral entropy already at t=0. Positivity, the square-noise identity and vector orthogonality do not supply the missing influence-only estimate. Root and an independent peer reviewed the final proof and primary attribution and independently replayed the final checker byte-identically:15 exact profiles/full-coarse histograms,45 thinning checks,30 rate comparisons,271 positive fields and25,544 pairs. Rational finite certificates do not certify the universal statement by enumeration or prove full FEI. All seven files in the combined profile folder were exactly read back at open, unmerged draft PR12 head971fe8a485349a69914decb992000879acbc892e; the completed12:48 checkpoint is unchanged.
