SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-24T02:45:20Z.
attacking: a global spectral-window-or-physical-hub reduction and exact stability under arbitrary signed spectral completion.

# account03/B12 r47 — spectral completion either stays diffuse or creates a physical hub

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING REDUCTION / FULL QFORM OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`  

## 1. Compact end-to-end reduction

Let `A=A^T` have at least three eigenvalues of absolute value at least one. Put

`gamma=1/64`, `eta=1/32`,

and let

`P = 1_{[gamma,infinity)}(|A|)`

be the spectral projection onto **all** eigenspaces with `|lambda(A)|>=gamma`.

There are two exhaustive cases.

1. If `max_i P_ii<=eta`, the completed spectral-window theorem at
`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`, applies directly and gives a continuous `C_0` density with

`||p_(X^T A X)||_infinity <= 288 sqrt(3e)/13 = 63.26405187778285... <64.`

It retains every eigenvalue below `1/64`, however numerous, nonzero, signed, or oriented.

2. If some `P_ii>eta`, the elementary square-energy inequality proved below gives

`||A e_i||_2 > gamma sqrt(eta)=1/(256 sqrt(2)).`

Since

`||A e_i||_2^2=A_ii^2+||A[i,i^c]||_2^2`,

at least one literal ORIGINAL-coordinate coefficient certificate holds:

`|A_ii|>1/512`  or  `||A[i,i^c]||_2>1/512`.

Thus the bare three-large-eigenvalue hypothesis is reduced, with no dimension loss, to the already-paid diffuse spectral-window branch **or** a universal physical pivot/cross-row hub branch. No eigen-coordinate is declared independent.

The second branch is not yet closed here. In particular one heavy row alone must not be treated as if it absorbed arbitrary same-bank curvature; the live correction inbox contains a counterexample to that shortcut.

## 2. General square-energy lemma

For any real symmetric matrix `M` and any threshold `a>0`, let

`P_a(M)=1_{[a,infinity)}(|M|)`.

### Lemma 2.1 — high spectral leverage forces physical row energy

For every original coordinate `i`,

`||M e_i||_2^2=(M^2)_ii >= a^2 (P_a(M))_ii.`                 (2.1)

#### Proof

Write the spectral decomposition

`M=sum_j lambda_j v_j v_j^T`.

Then

`M^2-a^2 P_a(M)`
` =sum_j [lambda_j^2-a^2 1_{|lambda_j|>=a}] v_j v_j^T >=0.`   (2.2)

Taking its `i,i` entry gives (2.1). QED.

### Corollary 2.2 — spectral-window-or-hub at arbitrary parameters

If `max_i(P_a(M))_ii<=eta`, the high spectral window is `eta`-diffuse. Otherwise some original coordinate satisfies

`||M e_i||_2>a sqrt(eta).`                                    (2.3)

Moreover, for that coordinate,

`max{|M_ii|, ||M[i,i^c]||_2} > a sqrt(eta/2).`                (2.4)

For `a=1/64`, `eta=1/32`, (2.4) is exactly the `1/512` alternative in Section 1.

This implication is deterministic and uses the **final matrix**. Arbitrary added eigenvalues of either sign are already included in `P_a(M)` and `M^2`; no random perturbation is introduced.

## 3. Exact stability under arbitrary signed spectral completion

The preceding reduction has a useful completion form tailored to the B12 assignment.

Let `A_0=A_0^T`, `R=R^T`, and assume

`A_0 R=0.`                                                     (3.1)

Because the matrices are symmetric, also `R A_0=0`; their nonzero spectral supports are orthogonal. Hence for every `a>0`,

`P_a(A_0+R)=P_a(A_0)+P_a(R)`                                  (3.2)

and

`(A_0+R)^2=A_0^2+R^2 >= A_0^2.`                              (3.3)

Equation (3.2) gives an exact leverage-budget theorem. If a downstream spectral-window theorem requires

`(P_a(A))_ii<=eta`,

then the arbitrary spectral completion `R` is harmless precisely when

`(P_a(R))_ii <= eta-(P_a(A_0))_ii`                            (3.4)

for every `i` with nonnegative right side. The completion may contain arbitrarily many eigenvalues, of arbitrary sign and magnitude. Eigenvalues of `R` below `a` are completely absent from the leverage budget.

If (3.4) fails so that the final projector has a diagonal entry above `eta`, Corollary 2.2 exports that failure to a literal physical hub. Thus at the owner scale `a=1/64`, arbitrary spectral completion has the exhaustive behavior

`diffuse final window => continuous density <64`,

or

`heavy final window => |A_ii|>1/512 or ||A[i,i^c]||_2>1/512`.

This is `QFORM-SPECTRAL-COMPLETION-DIFFUSE-OR-HUB-v1`.

A useful point is that (3.3) is sign-blind. Adding a positive, negative, or mixed-sign spectral packet on an orthogonal spectral support cannot destroy any principal square-energy certificate. The statement concerns coefficient matrices only, not a claim that `X^T R X` is independent of `X^T A_0 X`.

## 4. Application of the designated account04/B12 result

The completed partner theorem is account04/B12 r8:

`yspennstate/math-open-problems@bcb9fd2641440a89d6e4967781d755618e163001`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260924T002154Z-account04-B12-multihub-shear-r8/REPORT.md`.

Its concrete `m=6,p=2,ell=4` family has

`s_2(Lambda)>=4`, `s_4(R_perp)=2`,
`||Lambda^(-1)W^T||op<=1`,
`||P_H T||op<=1/100`,

and proves for the actual pre-completion matrix `A_*`

`sqrt(lambda_6((A_*^2)[H,H]))`
` >= sqrt(5)-1-1/100`
` = 1.2260679774997898... =: g.`                            (4.1)

Now append **any** symmetric signed spectral completion `S` satisfying

`A_* S=0.`                                                     (4.2)

No bound is imposed on the number, signs, magnitudes, rank, or original-coordinate localization of the new eigenvalues. By (3.3),

`(A_*+S)^2=A_*^2+S^2 >= A_*^2`,

so at the actual partner carrier

`sqrt(lambda_6(((A_*+S)^2)[H,H])) >= g.`                      (4.3)

Applying the completed six-square-mode receiver already used by account04/B12 gives the unchanged essential-density estimate

`||p_(X^T(A_*+S)X)||_(infinity,ess)`
` <= 720 sqrt(pi)/g`
` = 1040.86135195729... <1040.862.`                            (4.4)

Thus an arbitrary orthogonal spectral completion is **zero-cost** for this physical square-energy certificate, despite generally being dense in the original independent coordinates. This is an actual equation-level use of the designated partner result. Continuity is not claimed for this six-mode receiver.

The square-energy monotonicity in (3.3) is an elementary mechanism already used in earlier B12 work; the new contribution of this run is the global spectral-projector leverage budget and the target-level diffuse-or-physical-hub reduction of Sections 1–3.

## 5. Deterministic checks

A seeded finite checker generated 10,000 random symmetric matrices of dimensions 6 through 39, each with at least three eigenvalues of modulus at least one and with the remaining spectrum spread over magnitudes from `10^-3` to `10^2` with mixed signs.

It checked:

- `A^2-gamma^2 P >=0` numerically;
- every heavy projector coordinate obeyed the row-energy lower bound;
- every heavy row obeyed the scalar-pivot/cross-row split;
- for an exact orthogonal spectral split, `P_gamma(A)=P_gamma(A_0)+P_gamma(R)`.

Results:

`trials=10000`
`heavy_coordinate_tests=225168`
`violations_psd=0`
`violations_heavy_row=0`
`violations_pivot_cross_split=0`
`violations_projector_additivity=0`
`minimum_numeric_psd_eigenvalue=7.356506509635007e-08`
`maximum_projector_additivity_operator_error=6.027571495244749e-16`.

These are sanity checks only. The proof is the spectral identity (2.2) and orthogonal-support identities (3.2)–(3.3).

## 6. Scope and next missing implication

The full conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

The new reduction makes the remaining B12 obstruction concrete. Outside the already-proved continuous `<64` spectral-window branch, there is an original coordinate with a universal physical certificate

`|A_ii|>1/512` or `||A[i,i^c]||_2>1/512`.

The next step is to combine this hub with the two remaining large spectral resources in a dependence-safe way: either obtain a quantitatively invertible physical pair / Schur residual, or show that diffuse mass of the cross row forces a grouped/ridge/projected-crossing receiver. One must preserve the full same-bank quadratic curvature; the known one-heavy-row absorption shortcut is false.

No Gaussian, log-concavity, moment, support, diagonal-basis, or post-rotation independence assumption is used. The diffuse branch establishes a continuous `C_0` density; the unrestricted target and the partner six-mode completion branch currently assert only the stated essential-boundedness conclusions.
