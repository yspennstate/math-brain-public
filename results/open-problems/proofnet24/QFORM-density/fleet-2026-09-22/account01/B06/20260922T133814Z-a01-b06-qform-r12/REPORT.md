# account01/B06 — independent-bank curved aggregation and an elementary diffuse rank-three branch

**Run:** `20260922T133814Z-a01-b06-qform-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Assignment:** Curved fiber integration / GEOMETRY  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval/use occurred, but native learned-memory receiver use was not verified.

## 0. Exact target and dependency discipline

The full target remains: for every finite `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has an essentially bounded density with one universal finite constant, or give a valid counterexample. Continuity is a separate requested strengthening.

Fresh control was read from `yspennstate/math-research-brain` main at the start of this run and refreshed before publication; owner revision remained `2026-09-22.5`, with QFORM as the sole research target and no later stop for B06.

Corrections consumed include the standing failures of law-uniform pointwise quadratic-phase decay, unrestricted fiber-sup integration, independence after spectral rotation, conditional-cap replacement, single-Schur extraction, local cross-rank-three dichotomies, and the later `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`. A still newer event, `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`, was also checked before publication. The argument below uses none of these refuted interfaces: product aggregation is performed on original independent coordinate banks before any curved or cross-block conclusion.

The designated partner result actually used is **account02/B06**, run `b06-20260922T113045Z-d47192d10a82`, canonical report

`yspennstate/math-open-problems@6902eb62f21a7c833ca27dcca69f34d50e711a7d:proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T113045Z-d47192d10a82/REPORT.md`.

Its theorem `QFORM-SAMESIGN-DETERMINANT-MASS-v1` says that for an orthonormal same-sign spectral two-frame `R=[r s]`,

`w_ij=(r_i s_j-r_j s_i)^2`,  and  `sum_{i<j} w_ij=1`.

I apply these exact weights below to both halves of an independently split coordinate bank.

A second source used is the completed supporting theorem

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a:proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

Its relevant implication is: if an original-coordinate cross block `B=A[I,J]` has at least `r>2q` singular values at least `sigma`, `1<=q<2`, and the coordinate leverage of `range(B)` on one side is at most `q/2`, then `X^TAX` has a **continuous** density and

`||p_Q||_infinity <= e r / (sqrt(2q) sigma (r-2q))`.

Arbitrary self-block phases and outside couplings are retained in that theorem.

## 1. Conditional end-to-end argument and first missing implication

Choose three orthonormal eigenvectors corresponding to three eigenvalues of magnitude at least one and put them into an `n x 3` frame `U`. If their row leverages are diffuse, the new theorem below partitions the **original independent coordinates** into two banks `S,T` such that both restricted frames are quantitatively invertible. For a rank-exactly-three form, this forces three singular values of the physical cross block `A[S,T]` to stay uniformly large and simultaneously controls its range leverage. The regularized determinant theorem then gives a universal continuous density bound.

The same partition also has a direct curved-fiber interpretation: for the same-sign pair among the three eigenvectors, the account02/B06 Pluecker determinant mass is bounded below by a constant **inside each bank**, so each bank separately retains a dimension-free elliptic smoothing mechanism. This is a weighted replacement for choosing one large physical pair.

The first essential missing implication for the unrestricted target is now:

> **QFORM-CROSS-CANCELLATION-BRIDGE-v1 (OPEN).** When additional spectral components are present, prove that one can choose an original-coordinate split for which either the full cross block retains three usable singular directions with controlled range leverage, or the additional spectrum can be absorbed by another product-preserving curved estimate. The selected rank-three truncation has the required cross singular values, but arbitrary extra spectral components may cancel its cross block or enlarge its range leverage. They cannot be treated as independent noise after spectral rotation.

The theorem below closes the exact-rank-three diffuse branch and a block-diagonal perturbation branch, not the full conjecture.

## 2. Elementary two-bank splitting of a low-leverage tight frame

### Lemma 2.1 — `QFORM-TIGHT-FRAME-TWO-BANK-v1`

Let `U` be an `n x d` real matrix with `U^T U=I_d`; write its rows as `u_i^T` and assume

`ell_i=||u_i||_2^2 <= delta` for all `i`.

Then there is a partition `[n]=S disjoint_union T` such that, with

`rho=sqrt(d delta)`, `m=(1-rho)/2`, `M=(1+rho)/2`,

one has

`m I_d <= U_S^T U_S <= M I_d`,

`m I_d <= U_T^T U_T <= M I_d`.

In particular this is nontrivial whenever `delta<1/d`.

### Proof

Let `epsilon_i` be independent Rademacher signs and put

`D=sum_i epsilon_i u_i u_i^T`.

Since the cross terms vanish in expectation,

`E tr(D^2)=sum_i tr((u_i u_i^T)^2)=sum_i ell_i^2 <= delta sum_i ell_i=d delta`.

Therefore some deterministic sign choice satisfies

`||D||_op^2 <= ||D||_F^2=tr(D^2)<=d delta`,

so `-rho I_d<=D<=rho I_d`. Let `S={i:epsilon_i=+1}` and `T={i:epsilon_i=-1}`. Since

`U_S^T U_S=(I_d+D)/2`,  `U_T^T U_T=(I_d-D)/2`,

the claimed inequalities follow. `QED`

This is intentionally elementary. It creates independent coordinate banks because the partition acts in the original product coordinates, not in a rotated eigenbasis.

## 3. Direct application of account02/B06 determinant mass

Take `d=3`, write the selected orthonormal frame as `U=[r s t]`, and choose `r,s` to be the same-sign pair among the three selected large eigenvectors. Let

`R=[r s]`,  `w_ij=det(R_{ij})^2`.

By account02/B06, `sum_{i<j}w_ij=1`. For any coordinate set `E`, Cauchy--Binet gives the localized identity

`sum_{i<j, i,j in E} w_ij = det(R_E^T R_E)`.                     (3.1)

Apply Lemma 2.1 to the full three-frame `U`. Since `R_S^T R_S` and `R_T^T R_T` are principal compressions of `U_S^TU_S` and `U_T^TU_T`, respectively,

`R_S^T R_S >= m I_2`,  `R_T^T R_T >= m I_2`.

Hence the partner weights obey the **two-bank determinant-mass lower bounds**

`sum_{i<j in S} w_ij >= m^2`,

`sum_{i<j in T} w_ij >= m^2`.                                  (3.2)

This is the requested actual inequality using the named partner theorem: a diffuse same-sign spectral plane cannot have all its Pluecker curvature concentrated across the bank boundary. Both independent coordinate banks retain a constant amount of same-sign determinant mass.

There is also an exact one-coordinate deletion identity, useful when one wants to avoid a heavy coordinate. If `c_i=r_i^2+s_i^2`, then the partner marginal identity gives `c_i=sum_{j!=i}w_ij`; therefore

`sum_{j<k: j,k!=i} w_jk = 1-c_i >= t_i^2`,                       (3.3)

because the three-frame row leverage satisfies `c_i+t_i^2<=1`.

## 4. Curved ellipse smoothing inside each independent bank

The previous B06 run proved a two-dimensional product projection theorem: if `V` is any matrix with two orthogonal columns after normalization and `Y=V^T X` is formed from independent cap-one coordinates, then the projected density is bounded by `e` after whitening. Applied to a non-normalized two-frame with Gram matrix `G=V^TV`, this gives

`||p_{V^T X}||_infinity <= e/sqrt(det G)`.                       (4.1)

For the partition above, (3.2) says

`det(R_S^TR_S)>=m^2`,  `det(R_T^TR_T)>=m^2`.

Thus the two same-sign spectral projections formed from each independent coordinate bank satisfy

`||p_{R_S^T X_S}||_infinity <= e/m`,

`||p_{R_T^T X_T}||_infinity <= e/m`.                            (4.2)

Let their same-sign eigenvalues be `lambda_1,lambda_2`, with `|lambda_1|,|lambda_2|>=1`. Keeping the full ellipse shell rather than a fiber supremum gives, separately for `E=S,T`,

`P_E=lambda_1 <r_E,X_E>^2+lambda_2 <s_E,X_E>^2`,

`||p_{P_E}||_infinity <= pi e/[m sqrt(|lambda_1 lambda_2|)] <= pi e/m`.  (4.3)

This is a genuine curved-fiber aggregation statement: no individual physical pair `w_ij` must be large, and the smoothing occurs inside two disjoint original-coordinate banks.

Equation (4.3) alone still does not permit convolution with the remaining spectral term inside the same bank; it is recorded as geometric structure, not falsely promoted to the full theorem.

## 5. A new rank-exactly-three diffuse theorem

### Theorem 5.1 — `QFORM-RANK3-ELEMENTARY-BANK-v1`

Let

`A=U Lambda U^T`

be a real symmetric matrix of **rank exactly three**, where `U` is `n x 3` with orthonormal columns and every eigenvalue in the invertible `3 x 3` matrix `Lambda` has absolute value at least one. Assume

`max_i ||u_i||^2 <= delta <1/3`.

Put

`rho=sqrt(3 delta)`,  `m=(1-rho)/2`.

If there exists `q in [1,3/2)` such that

`delta/m <= q/2`,                                                   (5.1)

then for every independent input with densities bounded by one, `Q=X^TAX` has a **continuous density vanishing at infinity**, and

`||p_Q||_infinity <= 3e/[sqrt(2q) m (3-2q)]`.                       (5.2)

### Proof

Use Lemma 2.1 with `d=3` to obtain `S,T` and write

`M_S=U_S^TU_S`,  `M_T=U_T^TU_T`.

Both obey `M_S,M_T>=mI_3`. Define the physical cross block

`B=A[S,T]=U_S Lambda U_T^T`.

Write the polar factorizations

`U_S=Q_S M_S^(1/2)`,  `U_T=Q_T M_T^(1/2)`,

where `Q_S,Q_T` have orthonormal columns. The three nonzero singular values of `B` therefore equal those of

`C=M_S^(1/2) Lambda M_T^(1/2)`.

Since `s_min(Lambda)>=1`,

`s_3(B)=s_min(C)>=sqrt(m)*1*sqrt(m)=m`.                            (5.3)

All three factors in `C` are invertible, so

`range(B)=range(U_S)`.

Its orthogonal projector is

`P_B=U_S M_S^(-1) U_S^T`.

For every `i in S`,

`(P_B)_{ii}=u_i^T M_S^(-1)u_i <= ||u_i||^2/m <= delta/m <= q/2`.   (5.4)

Now apply the regularized determinant cross-block theorem quoted in Section 0 with `r=3`, `sigma=m`, and this `q`. Its hypotheses are exactly (5.3)--(5.4), and `3>2q` by assumption. It yields (5.2), together with a continuous density vanishing at infinity. `QED`

No sign condition is used in Theorem 5.1. Repeated eigenvalues and mixed signatures are allowed. The theorem is source-valid because the bank split is in original coordinates and because the cross-block estimate retains all self-block phases rather than assuming rotated independence.

### Concrete constants

For `q=1`, condition (5.1) becomes `delta/m<=1/2`. Its exact threshold is

`delta <= delta_0 := (11-sqrt(57))/32 = 0.1078176738...`.

At the endpoint, `m=2 delta_0`, and (5.2) gives

`||p_Q||_infinity <= 26.742`.

A cleaner sufficient condition is `delta<=1/16`; then

`m=(1-sqrt(3)/4)/2=0.283493...`,

and

`||p_Q||_infinity <20.341`.

The theorem also reaches beyond the `q=1` region. For example, if `delta<=1/8`, choose `q=4/3`; then `m=(1-sqrt(3/8))/2=0.193813...`, `delta/m<2/3=q/2`, and

`||p_Q||_infinity <77.30`.                                        (5.5)

These are explicit supporting constants, not proposed sharp values for the full conjecture.

## 6. Block-diagonal perturbations survive for free

The same proof gives a useful non-rank-three extension. Let `A_3=U Lambda U^T` satisfy Theorem 5.1, choose the partition `S,T` supplied there, and let `C` be any symmetric matrix satisfying

`C[S,T]=0`.

Then the full matrix

`A=A_3+C`

has exactly the same cross block `A[S,T]=A_3[S,T]`. The regularized determinant theorem permits arbitrary within-bank quadratic phases, so the full quadratic form still satisfies the same continuous-density bound (5.2), with no spectral restriction on the block-diagonal perturbation `C`.

This illustrates precisely what the current mechanism can absorb: arbitrary extra curvature living within banks is harmless. The hard case is genuinely **cross-bank cancellation or range inflation** by the additional spectrum.

## 7. Why small coefficient overlap alone is not a safe perturbative bridge

One might try to use a third eigenvector `t` whose coordinate overlap with the same-sign two-plane is small. The exact overlap identity is

`eta=sum_i (r_i^2+s_i^2)t_i^2
    =sum_{i<j} w_ij (t_i^2+t_j^2)`.

Since `r,s,t` are orthonormal, `r_i^2+s_i^2+t_i^2<=1`, so

`eta<=1-sum_i t_i^4`.

However, under only the density cap there is no scale control converting small coefficient overlap into probabilistic near-independence. For example, for small `epsilon`, take

`t=(sqrt(1-epsilon^2), epsilon,0)`,

`r=(epsilon,-sqrt(1-epsilon^2),0)`,

`s=(0,0,1)`.

Then `eta=2epsilon^2(1-epsilon^2)->0`. But let `X_1` be uniform on a centered interval of length `1/epsilon` (density `epsilon<=1`) and `X_2` uniform on a centered interval of length one. The covariance between `<r,X>` and `<t,X>` remains order one, and their correlation tends to a nonzero constant (indeed magnitude `1/sqrt(2)` at leading order). Thus a scale-free argument of the form “small coefficient overlap implies near independence” cannot be used without an additional invariant that pays for arbitrarily broad input supports.

This does not refute the QFORM target. It rules out a tempting perturbative shortcut for `QFORM-CROSS-CANCELLATION-BRIDGE-v1`.

## 8. Status and next exact implication

**PROVED / supporting:**

1. `QFORM-TIGHT-FRAME-TWO-BANK-v1`, an elementary quantitative original-coordinate partition for a diffuse `d`-frame.
2. The partner-applied determinant-mass bounds (3.2), showing constant same-sign Pluecker curvature in **both** independent banks.
3. The bankwise curved ellipse bounds (4.3).
4. `QFORM-RANK3-ELEMENTARY-BANK-v1`: a continuous density theorem for rank-exactly-three diffuse frames under the explicit condition (5.1), including the clean `delta<=1/8` constant `<77.30`.
5. The block-diagonal perturbation extension of Section 6.

**REFUTED LOCAL SHORTCUT:** coefficient-level near-orthogonality/overlap by itself does not imply probabilistic near-independence under arbitrary cap-one laws with unbounded support scale.

**OPEN:** the unrestricted three-large-eigenvalue theorem. The first exact missing implication on this route is `QFORM-CROSS-CANCELLATION-BRIDGE-v1`: prevent or absorb cancellation/range inflation of the rank-three bank cross block by arbitrary additional spectral components while preserving the original product structure. The owner-requested continuous-density conclusion is proved only in Theorem 5.1 and Section 6, not in full generality.

## 9. Publication-time correction check

Before publication, fresh `math-research-brain` main had advanced to `026692a030fc864d59bccb110245e7f5491482c3`; owner control was still revision `2026-09-22.5`, QFORM-only, with no B06 stop. The live correction set included `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`, and the head itself added `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`. Neither challenges the present argument: this proof performs original-coordinate bank aggregation before curved/cross-block estimates and does not invoke an absolute spectral-Wiener norm.

**Privacy/provenance check:** changed-file content was manually restricted to the mathematical statements, source pins, run identifier, and nonsecret operational status. No credentials, scheduler identifiers, machine paths, private unrelated data, email, Drive data, paid API use, remote workflow, or public-release action is present. An automated repository secret scanner was not exposed through the connector in this run.
