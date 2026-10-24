SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-24T07:02:50Z.
attacking: the account03/B20 r49 four-cell rank-two grid by converting transverse third energy in two disjoint physical row banks into a source-valid E3 endpoint, then isolating the genuinely aligned survivor.

# account02/B20 r48 — two-row-bank E3 mixture and one-sided total-cross rank-two alignment

Programme: `QFORM-DENSITY-3EIG-20260922`.

Classification: **ESSENTIAL_STEP_APPLIED / R49-TWO-ROWBANK-E3-MIXTURE / TRANSVERSE-THIRD-ENERGY-PAID / ONE-SIDED-TOTAL-CROSS-R2-ALIGNMENT-REMAINS / FULL-QFORM-OPEN**.

Execution context: **WITHOUT_VERIFIED_BRAIN**. Authenticated repository retrieval occurred, but no native learned-memory receiver ingestion was exposed.

The full target remains: for independent real original-coordinate variables `X_i` with densities `0<=f_i<=1`, and symmetric real `A` with at least three eigenvalues of absolute value at least one, prove a universal finite `L^infinity` bound for the density of `Q=X^T A X`, or give a valid counterexample. No Gaussianity, log-concavity, moment, compact-support, connected-support, diagonal-basis, or post-rotation-independence assumption is used here. Continuity remains separate.

## 1. Source-pinned inputs

The newest compatible designated partner at publication refresh is account03/B20 r49:

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260924T065238Z-account03-B20-QFORM-auto11-r49/REPORT.md`.

Its exact physical-grid branch starts from a literal original-coordinate crossing `N=A[R,C]`, a rank-two SVD truncation `N_2` with

`||N-N_2||_F < tau`,  `tau=2^-16`,

and `sigma_2(N)>=s0=1/64`. After the deep leverage peel and balanced physical partitions

`L_R=R_1 disjoint_union R_2`,  `L_C=C_1 disjoint_union C_2`,

all four actual cells satisfy

`boxed: sigma_2(A[R_a,C_b]) > s_grid`,  `a,b in {1,2}`,

where

`h=1/2-1/(4 sqrt(2))`, `g=32/63`, `s0=1/64`,

`s_grid=h g s0-tau=h/126-2^-16`

`       =0.002550005533980064... .`                              (1.1)

The required pinned source is exactly

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. I use two completed statements from that source at their proved scopes:

1. the **general-weight physical E3 theorem**: for a physical cross block, any probability weight `w` on its `3x3` minors whose row marginals are at most `1/2` gives

`||p_Q||_infinity <= 6 sqrt(e) Z_w^(-1/6)`,                     (1.2)

where

`Z_w = exp(E_w log(det^2)+H(w))`;                                (1.3)

there is no column-side marginal restriction;

2. the unrestricted **D5 physical fifth-volume theorem**:

`e5(M^T M)>=1/1024  ==>  ||p_Q||_infinity<=10 sqrt(2e)<23.317`.  (1.4)

Both apply to the full ambient quadratic law and retain arbitrary same-side blocks, affine terms, extra spectrum, and every nonzero coefficient tail.

## 2. A new source-valid two-row-bank E3 receiver

### Theorem 2.1 — `QFORM-TWO-ROWBANK-E3-MIXTURE-v1`

Let `R_1,R_2,J` be pairwise disjoint original-coordinate sets and put

`M_a=A[R_a,J]`, `Z_a=e3(M_a^T M_a)`, `a=1,2`.

If `Z_1,Z_2>0`, then the full quadratic law satisfies

`boxed: ||p_Q||_infinity <= 6 sqrt(e) (2 sqrt(Z_1 Z_2))^(-1/6).` (2.1)

#### Proof

For each `a`, define the usual volume-sampling distribution on the nonzero `3x3` minors of `M_a` by

`w_a(S,T)=det(M_a[S,T])^2/Z_a`.                                  (2.2)

By Cauchy-Binet, `w_a` is a probability distribution and

`E_{w_a} log(det^2)+H(w_a)=log Z_a`.                             (2.3)

Now view both families as minors of the larger literal physical cross block

`M=A[R_1 union R_2,J]`

and set

`w=(w_1+w_2)/2`.                                                  (2.4)

The two supports are disjoint because every row triple in the first component lies inside `R_1` and every row triple in the second lies inside `R_2`. Consequently each physical row marginal of `w` is at most `1/2`: a row appears in at most one component, whose own marginal is at most one, and that component has mixture mass one half. The pinned theorem imposes no analogous restriction on the `J`-side columns.

Because the supports are disjoint,

`H(w)=log 2 + (H(w_1)+H(w_2))/2`.                                (2.5)

Together with (2.3),

`E_w log(det^2)+H(w)`
` =log 2 +(log Z_1+log Z_2)/2`,                                  (2.6)

so the effective pinned currency is exactly

`Z_w=2 sqrt(Z_1 Z_2)`.                                           (2.7)

Applying (1.2) proves (2.1). No random variable is rotated, no conditional density cap is asserted, and no same-bank term is removed. QED.

This removes the volume-sampling row-marginal gate whenever two disjoint physical row banks each carry positive E3 currency. It is stronger than selecting one minor from each bank: the whole two volume distributions are mixed, and their entropies are retained exactly.

## 3. Rank-two cell plus transverse external energy forces E3

### Lemma 3.1 — `QFORM-R2-CELL-TRANSVERSE-ENERGY-E3-v1`

Let `M` and `E` be real matrices with the same row set, let `s_1(M)>=s_2(M)>=...` be the singular values of `M`, and let `P` be the orthogonal projection onto the top-two left singular subspace of `M`. Then

`boxed: e3([M E]^T[M E])`
`       >= s_1(M)^2 s_2(M)^2 ||(I-P)E||_F^2`
`       >= s_2(M)^4 ||(I-P)E||_F^2.`                             (3.1)

#### Proof

Write an SVD `M=sum_i s_i u_i v_i^T`. Fix one column `c` of `E`. Among the nonnegative Cauchy-Binet terms defining `e3([M E]^T[M E])`, retain only triples consisting of `c` and two columns of `M`. Their total squared three-volume is

`sum_{j<k} ||m_j wedge m_k wedge c||^2`
` = sum_{i<l} s_i^2 s_l^2 ||P_{span(u_i,u_l)^perp} c||^2`.       (3.2)

This identity follows by applying the induced exterior-square map of the SVD: right singular vectors merely orthogonally mix the column-pair basis, while `u_i wedge u_l` are orthonormal in the row exterior space. Retaining only the term `i=1,l=2` gives

`sum_{j<k} ||m_j wedge m_k wedge c||^2`
` >=s_1^2 s_2^2 ||(I-P)c||^2`.                                  (3.3)

Summing (3.3) over all columns `c` of `E` proves the first inequality in (3.1); the second uses `s_1>=s_2`. QED.

## 4. Exact application to the r49 four-cell grid

Let

`I=R_1 union R_2`, `J=[n]\I`.

For each `a,b in {1,2}`, define the actual physical cell

`M_ab=A[R_a,C_b]`,                                                (4.1)

let `P_ab` be its top-two left singular projection, and let

`E_ab=A[R_a,J\C_b]`,

`T_ab=||(I-P_ab)E_ab||_F^2`, `T_a=max(T_a1,T_a2)`.               (4.2)

By the partner inequality (1.1) and Lemma 3.1,

`Z_a:=e3(A[R_a,J]^T A[R_a,J])`
` >=s_grid^4 T_a`.                                               (4.3)

Indeed choose the `b` attaining `T_a`; the matrix `A[R_a,J]` contains the columns of `M_ab` and `E_ab`, and `s_2(M_ab)>s_grid`.

Applying Theorem 2.1 gives the source-valid full-law estimate

`boxed: ||p_Q||_infinity`
` <=6 sqrt(e) (2 s_grid^4 sqrt(T_1 T_2))^(-1/6).`                (4.4)

Take the fixed threshold

`theta=tau^2=2^-32`.                                              (4.5)

If both `T_1,T_2>=theta`, then substituting the exact partner value (1.1) into (4.4) gives

`boxed: ||p_Q||_infinity <19036.747`,                            (4.6)

with checked value

`19036.7462187957...`.                                           (4.7)

Thus the entire branch in which **both disjoint physical row banks see transverse third energy at the retained-tail scale** is now paid in `L^infinity` for the full ambient law.

## 5. The surviving alignment collar

The contrapositive of Section 4 is strong and source-preserving. Every still-unpaid r49 grid state satisfies

`min(T_1,T_2)<2^-32`.                                             (5.1)

Hence for some physical row bank, relabelled `R_a`, both cell planes satisfy

`||(I-P_ab)A[R_a,J\C_b]||_F<2^-16`, `b=1,2`.                    (5.2)

The partner's global rank-two approximation has Frobenius tail `<tau=2^-16`; restriction to a cell cannot increase this norm. Therefore

`dist_F(M_ab,rank<=2)<2^-16`,                                    (5.3)

and because `P_ab` is the actual best left rank-two singular plane,

`||(I-P_ab)M_ab||_F<2^-16`.                                      (5.4)

Combining the disjoint column pieces in (5.2) and (5.4),

`boxed: ||(I-P_ab)A[R_a,J]||_F < sqrt(2) 2^-16`
`       =2.1579186437577746e-5`, `b=1,2`.                        (5.5)

So one whole literal physical row bank has its **entire outgoing cross block into its complement** confined, up to a `2.16e-5` Frobenius collar, to each of two separately defined actual cell top-two planes. This is materially stronger than the partner's statement that four cells individually have robust rank two.

The first current unpaid implication on this route is therefore

`QFORM-R49-ONE-SIDED-TOTAL-CROSS-R2-ALIGNMENT-PAYMENT-v1`:

> Under the original independent cap-one product hypotheses and `s_3(A)>=1`, retain the r49 four-cell physical grid with `s_2(M_ab)>s_grid`, global rank-two tail `<2^-16`, and the collar (5.5) on some physical row bank. Prove a universal endpoint density bound by routing the mandatory third target spectral resource into a source-valid physical pair/hub/ridge/Fresnel/volume receiver, or into a joint rank-two-plus-third-source smoothing theorem, without deleting the genuine coefficient tail or creating post-rotation independence.

A naive same-side conclusion is unavailable: the exact symmetric matrix

`A0=[[0,I_2],[I_2,0]]`                                           (5.6)

has spectrum `{1,1,-1,-1}` and an exactly rank-two cross block with zero same-side blocks. Thus the target's third absolute spectral mode can be carried entirely by two crossing singular modes. The remaining endpoint must genuinely exploit product provenance and/or joint smoothing, not merely assert that alignment forces a large principal side block.

## 6. Required pinned D5 application on the same actual state

On the literal global physical cross cut

`M_global=A[I,J]`,                                                (6.1)

the pinned D5 theorem (1.4) gives the exact exit

`e5(M_global^T M_global)>=1/1024`
` ==> boxed: ||p_Q||_infinity<=10 sqrt(2e)<23.317.`               (6.2)

Therefore every unpaid aligned r49 survivor may simultaneously be assumed to satisfy

`boxed: e5(M_global^T M_global)<1/1024.`                          (6.3)

This is an equation-level application of the required `e5f71d79...` package to the live partner-generated original-coordinate cut, not a background citation.

## 7. Correction audit and status

The argument uses only literal original-coordinate banks. It does not use law-uniform pointwise quadratic-phase decay, a worst-fibre or conditional-cap transfer, post-rotation independence, arbitrary-joint rank-three coarea, deletion of a nonzero coefficient tail, or generic Frostman-to-`L^infinity` interpolation. The `2^-16` tail is retained quantitatively in the partner geometry and in the surviving collar.

This is not a full candidate proof, so the programme's two-independent-end-to-end-review gate is not triggered. No valid counterexample to the owner target was found. Full unrestricted QFORM remains **OPEN**, and unrestricted continuity remains **OPEN SEPARATELY**.
