SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B20, 2026-09-23T17:27:57Z.
attacking: compile the newest fleet03/B20 finite-core branch and the preceding aligned E2/rank-two branch into source-preserving physical-coordinate reductions, paying every third-volume escape with the new marginal-free E3 receiver.

# fleet02/B20 — finite-core spectral exit and three-cut common-plane compressor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T172757Z-fleet02-B20-QFORM-auto11`  
Role: Proof closure and keeper / SYNTHESIS  
Status: **ESSENTIAL_STEP_APPLIED / NEWEST-PARTNER-R35-APPLIED / THREE-CUT-COMMON-PLANE-COMPRESSOR / FULL-QFORM-OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: separate; not claimed globally.

## 1. Scope and corrections

The target is unchanged. For every dimension `n`, every independent real ORIGINAL-coordinate input `X_i` with density `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential density bound for `X^T A X`, or give a valid counterexample. No moments, compact support, connected support, iid, Gaussianity, log-concavity, diagonal-basis assumption, or post-rotation independence is introduced.


- no law-uniform pointwise quadratic-phase decay;
- no dimension-free worst spectral-fiber supremum;
- no independence after spectral rotation;
- no arbitrary-joint coarea density theorem;
- no conversion of a conditional marginal cap into independence;
- no inference of one uniformly good physical minor from aggregate volume;
- no deletion of a small nonzero coefficient tail as a uniformly small random quadratic perturbation.

All coefficient-plane projectors below are deterministic matrix objects only. The random variables remain grouped by ORIGINAL coordinates.

## 2. Required historical Claude source actually used

The required source directory was reread at the latest compatible state descending from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Two exact results from it are used here.

### 2.1 Physical third-volume receiver with diffuse row-volume law

For a literal ORIGINAL-coordinate cross block `M=A[I,J]`, write

`Z_3=e_3(MM^T)`.

Theorem D gives, when the canonical three-volume row marginals are at most `1/2`,

`||p_Q||_infinity <= 6 sqrt(e) Z_3^(-1/6)`.                       (2.1)

Same-bank blocks and affine terms are not discarded.

### 2.2 Fixed-dimensional physical principal-core theorem

The same source records, for every fixed dimension `m`,

`||p_Q||_infinity <= 250 m (8+log m)`                              (2.2)

for an `m x m` symmetric quadratic part having at least three eigenvalues of modulus at least one, uniformly in linear terms. By scaling, if its third absolute eigenvalue is at least `c>0`,

`||p_Q||_infinity <= 250 m (8+log m)/c`.                           (2.3)

Conditioning ORIGINAL coordinates outside a principal block only creates affine terms, so (2.3) is a legitimate ambient receiver.

## 3. Newest completed designated partner, fleet03/B20 r35

The newest compatible completed designated-partner result available in this run is

`yspennstate/math-open-problems@ab5d7906b6ffc0ca6b07c354d912d7b5b1afccfc`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T171148Z-fleet03-B20-QFORM-r35/REPORT.md`.

It starts from a symmetric ORIGINAL-coordinate carrier

`S_0=U Lambda U^T`, `rank(S_0)=r<=5`, `U^TU=I_r`,                  (3.1)

with

`s_3(S_0)>1597/2000`,
`||A-S_0||_op<403/2000`.                                           (3.2)

The diffuse carrier-leverage branch is now paid continuously. Every surviving heavy branch supplies an ORIGINAL-coordinate set `H` and a carrier-space unit vector `v` satisfying

`|H|<=124`,
`sum_(i in H) <U(i,:),v>^2 >1/20`.                                (3.3)

In particular one physical coordinate in `H` carries more than `1/2480` of that deterministic carrier direction. No random spectral coordinate is introduced.

### Theorem 3.1 — `QFORM-R5-124CORE-PHYSICALS3-EXIT-v1`

Under (3.1)-(3.3), if the physical principal block `A[H,H]` has three eigenvalues of modulus at least `1/64`, then the FULL ambient law has an essentially bounded density with

`||p_Q||_infinity
 <=64 * 250 * |H| * (8+log |H|)
 <=64 * 250 * 124 * (8+log 124)
 <25,435,439.`                                                     (3.4)

#### Proof

Condition on every ORIGINAL coordinate outside `H`. The remaining random coordinates are still mutually independent and cap one, while every cross coupling to the conditioned coordinates becomes only a linear term. The quadratic part is exactly `A[H,H]`. Divide that conditional quadratic polynomial by `1/64` and apply (2.2), then scale the density back. The bound is uniform in the conditioned values, so averaging preserves (3.4). QED.

#### Consequence

The newest r35 finite-core survivor may therefore be sharpened without any new probabilistic assumption to

`|H|<=124`,
`sum_(i in H)<U(i,:),v>^2>1/20`,
`s_3(A[H,H])<1/64`                                                 (3.5)

where `s_3(A[H,H])` means the third largest absolute eigenvalue of this symmetric physical principal block. Thus its unpaid content is genuinely a **carrier-capture / low-physical-spectrum mismatch**, not merely finite dimensionality.

The first in-plane edge is correspondingly sharpened to

`QFORM-R5-124CORE-LOWPHYSICALS3-CARRIER-CAPTURE-PAYMENT-v1`:

> under (3.1)-(3.2), spend an ORIGINAL-coordinate set `H` with `|H|<=124`, carrier mass `>1/20` in one direction, but third absolute physical-core eigenvalue `<1/64`, while retaining the full residual `A-S_0`, all same-bank curvature, every outside coupling and every nonzero tail.

## 4. The predecessor r34 marginal-free E3 theorem

The immediate completed predecessor fleet03/B20 r34 proves

`QFORM-PHYSICAL-E3-MARGINAL-GATE-REMOVAL-v1`:

for every literal ORIGINAL-coordinate physical cross block `M=A[R,C]` with

`Z_3=e_3(MM^T)>0`,

one has the FULL ambient continuous-density estimate

`||p_Q||_infinity <= K_3 Z_3^(-1/6)`,                              (4.1)

where

`K_3=3*2^(4/3)*exp(1/3)<10.551`.                                  (4.2)

Its proof escalates concentrated determinant volume through one, two and then three actual ORIGINAL-coordinate hubs. Thus (4.1) covers both the diffuse Theorem-D branch and every concentrated row-volume branch without selecting a vanishing reciprocal minor.

## 5. New three-cut compressor for the aligned triangle

The r34 aligned survivor consists of three disjoint ORIGINAL-coordinate banks `D1,D2,K` and literal blocks

`C=A[D1,D2]`,
`N1=A[D1,K]`,
`N2=A[D2,K]`,                                                      (5.1)

with

`F:=||C||_F^2>0.05671470919622164`,                                (5.2)

and

`s_1(N_r)s_2(N_r)>Delta:=0.0014419528160955833`, `r=1,2`.          (5.3)

Define all three physical cross cuts of this triangle:

`M1=[C,N1] : D1 -> D2 union K`,
`M2=[C^T,N2] : D2 -> D1 union K`,
`M3=[N1^T,N2^T] : K -> D1 union D2`.                              (5.4)

For each `a=1,2,3`, let

`T_a^2 := sum_(j>=3) s_j(M_a)^2
       = dist_F(M_a,{rank<=2})^2`.                                 (5.5)

### Theorem 5.1 — `QFORM-R34-THREECUT-FROBENIUS-R2-COMPRESSOR-v1`

For every `tau>0`, either the full ambient law has a continuous density satisfying

`||p_Q||_infinity <= K_3 (Delta tau)^(-1/3)`,                      (5.6)

or simultaneously

`T_1<tau`, `T_2<tau`, `T_3<tau`.                                  (5.7)

#### Proof

Each `M_a` contains either `N1` or `N2` as a column subblock (up to transpose). Positive-semidefinite row-Gram monotonicity therefore gives

`s_1(M_a)s_2(M_a) >= Delta`.                                       (5.8)

Writing the squared singular values of `M_a` as `lambda_j=s_j(M_a)^2`, the terms of `e_3` containing indices `1,2,k` give

`e_3(M_aM_a^T)
 >=lambda_1 lambda_2 sum_(k>=3)lambda_k
 =[s_1(M_a)s_2(M_a)]^2 T_a^2
 >=Delta^2 T_a^2`.                                                 (5.9)

If some `T_a>=tau`, (4.1) applied to this **literal physical cut** gives (5.6). Otherwise (5.7) holds. QED.

### Concrete scale

Take

`tau=sqrt(F)/256
    =0.0009302675875070436...`.                                    (5.10)

Then

`Delta^2 tau^2=1.7993592384885958e-12`,                            (5.11)

and the marginal-free partner theorem pays any failed collar by

`||p_Q||_infinity<956.621`.                                        (5.12)

This also supplies the requested equation-level use of the pinned historical source. On the subbranch where the canonical physical three-volume row marginals of that same `M_a` are at most `1/2`, Theorem D (2.1) gives the sharper actual inequality

`||p_Q||_infinity
 <=6 sqrt(e) (Delta^2 tau^2)^(-1/6)
 <896.972`.                                                        (5.13)

When the marginal gate fails, r34's ORIGINAL-hub concentration cascade pays it; no projected-coordinate independence is invoked.

## 6. Common `2+2+2` coefficient-plane geometry of every remaining aligned state

Assume the paid exit in Theorem 5.1 does not occur at the scale (5.10). Let `P1,P2,P3` be the top-two left-singular projectors of `M1,M2,M3`, acting on the physical banks `D1,D2,K`, respectively.

Because the column banks in each concatenation are disjoint, (5.7) gives

`||(I-P1)C||_F^2+||(I-P1)N1||_F^2<tau^2`,                         (6.1)

`||C(I-P2)||_F^2+||(I-P2)N2||_F^2<tau^2`,                         (6.2)

`||N1(I-P3)||_F^2+||N2(I-P3)||_F^2<tau^2`.                        (6.3)

Consequently

`||C-P1 C P2||_F<2tau`,                                            (6.4)

`||N1-P1 N1 P3||_F<2tau`,                                         (6.5)

`||N2-P2 N2 P3||_F<2tau`.                                         (6.6)

Moreover the central edge retains fixed mass:

`||P1 C P2||_F
 >sqrt(F)-2tau
 =(127/128)sqrt(F)
 >0.2362879672.`                                                    (6.7)

Thus every unpaid aligned state is now a **common three-bank `2+2+2` coefficient-plane triangle** with all three literal cross tails Frobenius-small at once. This is stronger than controlling only `M1` and `M2` separately: the third cut `M3` aligns the two K-side row spaces into one common two-plane.

Nothing probabilistic is inferred from `P1,P2,P3`. In particular, the projected random vectors `P_aX_{D_a}` are not declared to have independent coordinates. The actual original banks `D1,D2,K` remain independent of one another, and every nonzero cross tail remains in the quadratic form.

### Exact zero-tail normal form

At the exact endpoint `T_1=T_2=T_3=0`, choose orthonormal two-column physical coefficient frames `U_a` spanning `P_a`. Then there exist real `2x2` matrices `B12,B13,B23` such that

`C =U1 B12 U2^T`,
`N1=U1 B13 U3^T`,
`N2=U2 B23 U3^T`.                                                  (6.8)

This is only deterministic coefficient geometry. If one pushes the within-bank complex phases onto

`Z_a=U_a^T X_{D_a}`,                                               (6.9)

the three bank images are mutually independent because their ORIGINAL source banks are disjoint, while the two coordinates inside each `Z_a` may be arbitrarily dependent. Product-projection bounds give a two-dimensional density cap for each `Z_a`; they do not give coordinatewise independence. Arbitrary same-bank quadratic phases survive inside the corresponding complex pushforwards.

Hence the exact endpoint is a genuine three-block two-dimensional oscillatory problem, not a six-independent-scalar model. The nonzero-tail problem cannot be replaced by (6.8), because the live small-random-quadratic-perturbation correction forbids simply deleting (6.4)-(6.6).

## 7. Interaction with the newest averaged-frequency receivers

Several new same-hour theorems show why the remaining geometry is much narrower but not yet paid:

- the two-ORIGINAL-hub entangled-scalar `L^4` receiver can close a rank-two hub-leaf packet when one physical scalar curvature remains, even if its affine coefficient depends on the same leaf bank;
- the rank-two crossing overlap-square theorem can close a third square that is another projection of one crossing source bank, without asserting independence inside the projected triple;
- the critical grouped-crossing theorem supplies half-Riesz credit at `k+ell=2`, but a bare half-Riesz bound still does not imply `L^infinity` output density.

The common-plane theorem above does **not** yet force the exact structural hypotheses of either `L^4` receiver. In particular, arbitrary same-bank curvature on each of `D1,D2,K` may contain components outside the six-dimensional coefficient carrier, and a nonzero cross tail cannot be discarded.

A useful next target is therefore

`QFORM-R37-THREECUT-COMMONPLANE-WITH-RETAINED-TAILS-PAYMENT-v1`:

> under (5.1)-(5.3) and the simultaneous collars (6.4)-(6.7), retain all same-bank quadratic blocks, all nonzero cross tails and all extra spectrum, and either (i) extract one source-valid overlap-square / entangled-scalar averaged-frequency receiver at fixed scale, or (ii) prove a direct three-block `2+2+2` complex-pushforward estimate that is stable under the retained coefficient tails.

This is the first remaining transverse aligned edge after the new compressor.

## 8. Strongest current conditional proof graph

The source-pinned graph now has the following paid exits relevant to this B20 synthesis:

1. every literal physical cross block with nonzero third volume is paid by r34 with `K_3 Z_3^-1/6`, with no marginal gate;
2. in the rank-`<=5` in-plane carrier, diffuse leverage is paid by `<555.273`, and the heavy branch is reduced by r35 to a physical set `H` of size at most 124 carrying `>1/20` of a carrier direction;
3. this run pays every such finite core having third absolute physical eigenvalue at least `1/64`, by `<25,435,439`, so that branch may be assumed to satisfy (3.5);
4. in the aligned triangle, this run pays any third singular tail of any of its three literal cuts above `tau=sqrt(F)/256`, by `<956.621`, leaving the common `2+2+2` physical-plane geometry (6.4)-(6.7).

Thus there are presently two explicit first-edge obligations in the synthesized graph rather than one falsely merged gap:

- **in-plane finite core:** `QFORM-R5-124CORE-LOWPHYSICALS3-CARRIER-CAPTURE-PAYMENT-v1`;
- **transverse aligned triangle:** `QFORM-R37-THREECUT-COMMONPLANE-WITH-RETAINED-TAILS-PAYMENT-v1`.

Neither is a restatement of the full conjecture: each has fixed quantitative source-pinned hypotheses and retains the arbitrary residual terms that prior corrections require.

## 9. Status

No valid target counterexample was found. The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. No full candidate is claimed, so two independent end-to-end full-proof reviews are not triggered. Global continuity remains separate and open; continuity is available only on the cited branches that prove an integrable Fourier envelope.

The numerical values in this report are deterministic evaluations of displayed exact inequalities. They are not simulation evidence.

Execution remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository retrieval and publication occurred, but no authenticated learned-memory receiver ingestion/firing was exposed and used. Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: `maximum actually supported`. Configured reasoning effort: `UNKNOWN_NOT_EXPOSED`. Known actual reasoning effort: `UNKNOWN`. Provider reasoning-token counter: `null`. Provider pure-thinking-time counter: `null`. Elapsed wall-clock execution, when recorded in the finish receipt, includes source reads, tool calls, publication and readback and is not pure thinking.
