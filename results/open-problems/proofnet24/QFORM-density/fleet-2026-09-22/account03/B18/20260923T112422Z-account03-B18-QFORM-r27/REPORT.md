SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-23T11:24:22Z.

attacking: a product-preserving three-disjoint-bank all-pivot closure, with the near-zero pivot strip handled by a deterministic pivot-or-indefinite-pair dichotomy rather than perturbing the zero-pivot theorem.

# QFORM account03/B18 r27 — three disjoint scalar banks, all pivots

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **new supporting implication; full QFORM remains OPEN / NOT PROVED**.  The analytic dependencies quoted below are complete supplied proofs but still carry their own pending-independent-review labels.  No claim of literature-wide novelty is made.

Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Main result

### Theorem A — QFORM-THREE-DISJOINT-BANKS-ALLPIVOTS-v1

Let `I_1,I_2,I_3` be pairwise disjoint sets of original coordinates.  For each `k`, let `u_k` be a unit vector supported on `I_k`, and put

`S_k=<u_k,X_{I_k}>`,  `S=(S_1,S_2,S_3)`.

The original coordinates are independent and have probability densities bounded by one.  Suppose that, after conditioning on any further original coordinates disjoint from the three banks, the active dependence on the banks is

`Q = S^T K S + ell^T S + c`,

where `K` is a fixed real symmetric `3x3` matrix satisfying

`sigma_min(K) >= s > 0`,

while `ell,c` may depend arbitrarily on the conditioned outside coordinates.  Then the full law of `Q` has an essentially bounded density and

`||p_Q||_infinity < 296/s`.                                      (1.1)

In particular, if the effective three-bank matrix has all three eigenvalues of absolute value at least one, then

`||p_Q||_infinity < 296`.                                        (1.2)

No diagonal-pivot lower bound is assumed.  All three diagonal entries of `K` may be arbitrarily small nonzero numbers.  All signatures are allowed.

Continuity is **not** claimed by this all-pivot argument.  The exact zero-pivot subcase below does have a continuous density by the completed account04/B18 theorem.

A useful exact-rank-three corollary is obtained when the range of the physical matrix has an orthonormal basis of three vectors with pairwise disjoint original-coordinate supports.  If `U=[u_1,u_2,u_3]` and `A=U K U^T`, then the three nonzero physical eigenvalues are exactly those of `K`, so the target normalization gives (1.2).

## 2. Primary literature transfer: every normalized bank has density cap sqrt(2)

Primary source: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949.

Their theorem applies to a product density `prod_i f_i` with each one-dimensional factor a probability density bounded by one.  Every `k`-dimensional orthogonal marginal is bounded by `2^(k/2)`.  In particular, for every unit vector `u`,

`||p_<u,X>||_infinity <= sqrt(2)`.                               (2.1)

The theorem assumes none of: Gaussianity, log-concavity, moments, compact support, connected support, identical laws, centering, or smoothness.  It is a marginal-density theorem, not a pointwise oscillatory-decay theorem.

Because the three banks use disjoint original-coordinate sets, `S_1,S_2,S_3` are genuinely independent.  Define

`T_k=sqrt(2) S_k`.

By (2.1), every `T_k` has density cap one, and the `T_k` remain independent.  Since `S=T/sqrt(2)`, the quadratic matrix in the `T` variables is

`H=K/2`,

hence

`sigma_min(H) >= s/2`.                                          (2.2)

Thus it remains only to prove a dimension-three cap-one lemma with no pivot restriction.

## 3. Cap-one dimension-three lemma

### Lemma B — pivot-or-indefinite-pair closure

Let `Z_1,Z_2,Z_3` be independent real variables with probability densities bounded by one.  Let `H=H^T` satisfy `sigma_min(H)>=tau>0`, and allow an arbitrary affine term.  Then the quadratic law has an essentially bounded density with

`||p||_infinity < 148/tau`.                                    (3.1)

The proof uses two already-completed QFORM analytic packets, each at its literal hypotheses:

1. `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1`, scientific source
   `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
   `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.
   For a three-dimensional original-coordinate block and a nonzero scalar pivot `a=H_ii`, it gives

   `||p||_infinity <= 128 (|a| |det H|)^(-1/4)`.               (3.2)

   Arbitrary affine terms are included.

2. `QFORM-RANK3-INDEFINITE-PAIR-PIVOT-v1`, scientific source
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
   If a physical principal pair `B` is invertible indefinite, with
   `D=|det B|`, `kappa=sigma_min(B)`, it gives

   `||p||_infinity <= 8 sqrt(5) (D kappa tau)^(-1/4)`.          (3.3)

   This theorem also includes arbitrary affine terms and does not divide by either diagonal of `B`.

We now show that one of these two packets always has a quantitative certificate.

Set

`alpha=9/16`.

### Case 1: a large scalar pivot exists

If some diagonal entry satisfies `|H_ii|>=alpha tau`, then

`|det H| >= tau^3`

because every singular value of `H` is at least `tau`.  Therefore (3.2) gives

`||p||_infinity`
` <=128 (alpha tau^4)^(-1/4)`
` =128 alpha^(-1/4) tau^(-1)`
` =(256/sqrt(3)) tau^(-1)`
` =147.8016689125... tau^(-1)`
` <148 tau^(-1)`.                                               (3.4)

### Case 2: every scalar pivot is small

Assume `|H_kk|<alpha tau` for all `k`.  Since `sigma_min(H)>=tau`, every column (equivalently every row) has Euclidean norm at least `tau`.  Fix a row `i`.  Its two off-diagonal entries therefore satisfy

`sum_(j!=i) H_ij^2 >= (1-alpha^2) tau^2`.

Hence one of them, write it `b=H_ij`, obeys

`|b| >= sqrt((1-alpha^2)/2) tau`
`     =sqrt(175/512) tau`.                                     (3.5)

Consider the physical principal pair

`B=[[H_ii,b],[b,H_jj]]`.

Its determinant is negative because

`|det B| = b^2-H_ii H_jj`
` >= b^2-|H_ii H_jj|`
` >= [(1-alpha^2)/2-alpha^2] tau^2`
` =[(1-3alpha^2)/2] tau^2`
` =(13/512) tau^2`.                                            (3.6)

Thus `B` is invertible indefinite.  Compare it with `[[0,b],[b,0]]`.  Weyl's singular-value perturbation inequality gives

`kappa=sigma_min(B)`
` >= |b|-max(|H_ii|,|H_jj|)`
` >= [sqrt(175/512)-9/16] tau`
` =[(5 sqrt(14)-18)/32] tau`.                                 (3.7)

Substituting (3.6)-(3.7) in (3.3) gives

`||p||_infinity <= C_pair tau^(-1)`,

where

`C_pair = 8 sqrt(5) [13(5 sqrt(14)-18)/16384]^(-1/4)`
`       =116.1827972202... <148`.                              (3.8)

Cases 1 and 2 prove Lemma B.

### Completion of Theorem A

Apply Lemma B to the independent cap-one variables `T_k` from Section 2 and to `H=K/2`.  By (2.2), `tau=s/2`, so

`||p_Q||_infinity <148/(s/2)=296/s`.

The bound is uniform in every outside conditioning because outside variables only change the affine term.  Averaging the conditional densities proves (1.1).

No spectral rotation of random coordinates is used.  The only aggregated variables declared independent are built from disjoint original-coordinate banks.

## 4. Required account04/B18 application: exact zero pivot

The designated partner result is account04/B18's completed sharp zero-pivot `1+2` transfer, scientific source

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

It states: if a cap-one scalar is genuinely independent of a two-dimensional vector of joint density cap `M`, and the active symmetric `3x3` matrix has a zero scalar pivot and is nonsingular, then

`||p||_infinity <=6 M^(2/3)|det H|^(-1/3)`,                    (4.1)

and the density is continuous.

Suppose in Theorem A that `K_11=0`.  Scale all three banks by `sqrt(2)` as above.  Then the three scaled variables have cap one and remain mutually independent, so the pair `(T_2,T_3)` has joint density cap `M<=1`.  The scaled matrix is `H=K/2`, hence `det H=det K/8`.  Applying (4.1) literally gives

`||p_Q||_infinity`
` <=6 (|det K|/8)^(-1/3)`
` =12 |det K|^(-1/3)`.                                        (4.2)

This is an actual partner inequality, not merely a citation.  Under `sigma_min(K)>=1`, it gives the much sharper

`||p_Q||_infinity <=12`,                                      (4.3)

and a continuous density.

Thus the new all-pivot theorem genuinely bridges the partner-paid exact-zero slice to nonzero pivots in the same three-disjoint-bank geometry; it does not obtain the bridge by treating a small nonzero pivot as zero.

## 5. Concrete near-zero target family

Let the three banks be any disjoint unit banks and, for `0<=delta<1`, set

`K_delta=(1/(1-delta))*[[delta,1,1],[1,delta,1],[1,1,delta]]`.

The eigenvalues are exactly

`(delta+2)/(1-delta), -1, -1`,

so every `K_delta` is target-normalized.  For every `delta>0`, all three diagonal pivots are nonzero, while they tend to zero as `delta->0`.

Theorem A gives, for every admissible original product law,

`||p_Q||_infinity <296`                                       (5.1)

uniformly all the way down the nonzero-pivot collar.

For the explicit collar `0<delta<9/25`, after the `sqrt(2)` bank scaling all three pivots fall into Case 2 of Lemma B, so the sharper pair branch gives

`||p_Q||_infinity <2*C_pair <232.366`.                         (5.2)

At the exact corner `delta=0`, the designated account04/B18 theorem gives

`||p_Q||_infinity <=12*2^(-1/3)=9.5244063118...`,              (5.3)

with continuity.  Equation (5.2) is deliberately not called a perturbative consequence of (5.3): it is a separate all-pivot proof valid for every nonzero `delta` in the stated interval.

## 6. Hypothesis audit and relation to live corrections

This proof uses no Gaussian, log-concavity, moment, bounded-support, connected-support, centering, identical-law, or smoothness assumptions.

It respects every relevant live correction:

- no independence is asserted after a general spectral rotation;
- a bounded projection density alone is never used as a nonlinear quadratic pushforward theorem;
- the arbitrary-joint 3D coarea lemma is not used;
- conditional density caps are not substituted for independence;
- no fixed physical good-minor extraction is claimed from the bare target;
- no pointwise law-uniform quadratic-phase decay is used;
- no near-zero coefficient is replaced by zero;
- no Monte Carlo or interval-extremality claim enters the proof.

The source transfer is specifically the LPP marginal-density theorem applied *before* the nonlinear step and only to disjoint original-coordinate banks.  The nonlinear payment is supplied by the complete rank-three pivot/pair packets in Section 3, with the exact-zero branch sharpened by account04/B18 in Section 4.

## 7. What this does and does not solve

Theorem A closes the **entire all-pivot problem once a product-preserving representation by three disjoint scalar banks with a uniformly nonsingular effective `3x3` matrix has been obtained**.  Therefore a structural compiler may use such a certificate without separately treating zero, near-zero, and large diagonal pivots.

It does **not** prove that the bare hypothesis `s_3(A)>=1` always supplies such three banks.  The live families with diffuse rank-two cross structure, plane-plus-one geometry, and extra spectrum show why that extraction cannot be asserted from a fixed minor or arbitrary rotation.  In particular, the current account03/B19 small-pivot star residue is not discharged merely from its star-energy lower bound; an additional product-preserving grouped-coordinate certificate is still required.

Full QFORM remains `OPEN / NOT PROVED`.  Full-target continuity also remains open.  Continuity is proved here only on the exact zero-pivot partner subcase.

## 8. Source pins

Primary published transfer:
- Livshyts, Paouris, Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949.

Internal complete analytic dependencies:
- `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.
- `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
- designated partner: `yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061:proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

