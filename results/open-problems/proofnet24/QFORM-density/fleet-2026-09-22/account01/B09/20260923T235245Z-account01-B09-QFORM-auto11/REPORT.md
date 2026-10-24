SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T23:52:45Z.
attacking: the remaining overlap-one/overlap-two third-compound sectors by exact physical Schur-numerator identities and literal-cut extraction, with special attention to the singular-pair collar.

# account01/B09 — overlap-1/2 Schur-numerator compiler

Run: `20260923T235245Z-account01-B09-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Fresh owner control at startup: `f7f7e3636d5557de2cf1d957e5fe1f8f864a20a9`, revision `2026-09-22.15`  
Status: **NEW STRUCTURAL THEOREM / ESSENTIAL STEP APPLIED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The full conjecture and the full-target continuity conclusion remain open. This run addresses the B09 frontier left by `QFORM-C3-OFFDIAGONAL-OPERATOR-GAP-v1`: after the already-paid overlap-zero and principal-triple alternatives, an unpaid target matrix must have macroscopic overlap-one or overlap-two third-compound mass. The point here is to convert those overlapping physical minors into exact disjoint-coordinate bilinear currencies without rotating the independent variables and without a square-root decoupling argument.

## 1. Overlap notation

For a real symmetric `n x n` matrix `A`, write

`Omega_r(A)=sum_{|S|=|T|=3, |S intersect T|=r} det A[S,T]^2`.

The previous B09 operator-gap theorem reduces the still-unpaid global target to `Omega_1>=1/4` or `Omega_2>=1/4`. This report does not claim that the aggregate sum automatically contains one constant-size physical pivot packet; instead it derives the exact packet currencies and identifies the remaining aggregation obstruction.

## 2. The overlap-two identity: a denominator-free pair Schur numerator

Fix a literal physical pair `H={a,b}` and put `L=H^c`. In the ORIGINAL coordinate order write

`A = [[B, U^T], [U, D]]`,

where `B=A[H,H]` is `2 x 2`, `U=A[L,H]`, and `D=A[L,L]`. Let

`delta = det B`,

`N_H = delta D - U adj(B) U^T`.                                      (2.1)

For distinct `i,j in L`, the unique overlap-two third minor with shared pair `H` is the bordered determinant

`d_(H;i,j) = det A[H union {i}, H union {j}]`.

Expanding the bordered determinant gives the exact identity

`boxed: d_(H;i,j) = (N_H)_(ij).`                                  (2.2)

No invertibility is assumed. Consequently the full fixed-pair overlap-two currency is

`Omega_(2,H)
 := sum_(i!=j, i,j in L) d_(H;i,j)^2
 = ||offdiag N_H||_F^2.`                                           (2.3)

Summing over physical pairs gives exactly

`boxed: Omega_2(A) = sum_(|H|=2) ||offdiag N_H||_F^2.`             (2.4)

Every overlap-two ordered pair `(S,T)` has one and only one shared physical pair, so there is no combinatorial multiplicity hidden in (2.4).

### Invertible pair

If `delta!=0`, let

`S_H = D - U B^(-1) U^T`

be the exact physical-pair Schur complement. Since `B^(-1)=adj(B)/delta`, (2.1) becomes

`N_H = delta S_H`,

and therefore

`boxed: Omega_(2,H)=delta^2 ||offdiag S_H||_F^2.`                  (2.5)

Now make a literal Bernoulli split `L=R disjoint_union C`, each leaf independently sent to either side with probability `1/2`. Then

`E ||S_H[R,C]||_F^2
 = (1/4)||offdiag S_H||_F^2`.

Hence some literal source-coordinate cut obeys

`boxed:
 ||S_H[R,C]||_F^2 >= Omega_(2,H)/(4 delta^2).`                    (2.6)

This is a direct conversion of overlap-two compound mass into a genuinely disjoint bilinear block. It uses neither spectral coordinates nor probabilistic decoupling of `Q`.

## 3. Density corollary for an invertible indefinite shared pair

The earlier completed B09 theorem `QFORM-INDEFINITE-PAIR-PLUS-ONECROSS-v1`, source

`yspennstate/math-open-problems@4b3c7fd28ec13d4d0c926affe670109c0738d816`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260923T141440Z-account01-B09-QFORM-auto11/REPORT.md`,

states that for an invertible indefinite physical pair `B`, with

`D0=|det B|`, `kappa=sigma_min(B)`,

and any nonzero literal cross block `C0` of the exact Schur complement,

`||p_Q||_infinity
 <= 11.463 D0^(-2/5) kappa^(-1/10) ||C0||_F^(-1/10),`             (3.1)

with the same coefficient times interval length. Arbitrary same-bank quadratic curvature is retained; continuity is not claimed.

Apply (3.1) to the literal cut supplied by (2.6). With `omega=Omega_(2,H)>0`,

`||C0||_F >= omega^(1/2)/(2D0)`.

Therefore

`boxed:
 ||p_Q||_infinity
 <= 11.463*2^(1/10)
    D0^(-3/10) kappa^(-1/10) omega^(-1/20)
 < 12.286 D0^(-3/10) kappa^(-1/10) omega^(-1/20).`               (3.2)

Thus every interval `I` satisfies

`boxed:
 P{Q in I}
 < 12.286 D0^(-3/10) kappa^(-1/10) omega^(-1/20)|I|.`            (3.3)

This is a direct `O(|I|)` conclusion with no square-root small-ball conversion. Under the full target, the later `QFORM-INDEFINITE-PAIR-THIRD-SPECTRAL-SMOOTHING-v1` can be stronger because it spends `sigma_3(A)` directly; (3.2) is nevertheless the exact bridge from the overlap-two ledger to the B09 bilinear receiver and remains useful in overlap-local arguments.

## 4. Exact singular/near-singular pair decomposition

The denominator-free numerator (2.1) also identifies the singular collar precisely. Diagonalize only the **two-dimensional coefficient matrix** `B` for algebraic bookkeeping,

`B = tau e e^T + sigma k k^T`,

with `e,k` orthonormal in the two-dimensional hub coefficient space. This is NOT a change of random coordinates and no independence is asserted after it. Define physical leaf coupling vectors

`p=Ue`, `q=Uk`.

Because

`adj(B)=sigma e e^T + tau k k^T`, `delta=tau sigma`,

we have the exact identity

`boxed:
 N_H
 = tau sigma D - sigma p p^T - tau q q^T
 = delta (D-p p^T/tau) - tau q q^T`                              (4.1)

when `tau!=0`.

Taking off-diagonal Frobenius norms and writing

`omega=Omega_(2,H)=||offdiag N_H||_F^2`,

one obtains the deterministic two-arm alternative

`boxed:
 max{
   |tau| ||offdiag(q q^T)||_F,
   |delta| ||offdiag(D-p p^T/tau)||_F
 } >= sqrt(omega)/2.`                                             (4.2)

Indeed (4.1) and the triangle inequality imply that if both displayed terms were `<sqrt(omega)/2`, then `||offdiag N_H||_F<sqrt(omega)`.

At the exact rank-one endpoint `sigma=0`, (4.1) collapses to

`N_H=-tau q q^T`,

so

`boxed:
 Omega_(2,H)
 = tau^2[(sum_i q_i^2)^2 - sum_i q_i^4].`                        (4.3)

This exactly matches the account02/B09 rank-one-pair ledger. A useful negative structural consequence is also immediate:

**At an exactly singular rank-one physical pair, `Omega_(2,H)` is completely blind to the leaf block `D`.**

The matrix `D` is multiplied by `delta=0` in (2.1). Therefore no argument using fixed-pair overlap-two mass alone can claim that arbitrary same-bank leaf curvature has been controlled. This explains why the partner's remaining `QFORM-RANKONE-OMEGA2-ENTANGLED-LEAFCURVATURE-v1` is a real analytic debt rather than bookkeeping slack.

## 5. The overlap-one identity: a scalar Schur numerator and a second cross-volume

Fix one literal physical coordinate `h`, put `L=h^c`, and write

`a=A_hh`, `v=A[L,h]`, `D=A[L,L]`.

Assume first `a!=0` and define

`N_h = aD-vv^T`,
`S_h = D-vv^T/a = N_h/a`.                                      (5.1)

For disjoint physical two-subsets `I,J subset L`, the overlap-one third minor is

`d_(h;I,J)=det A[{h} union I, {h} union J]`.

The block determinant formula gives

`boxed:
 d_(h;I,J)=a det S_h[I,J]
          = a^(-1) det N_h[I,J].`                               (5.2)

Define

`Omega_(1,h)=sum_(|I|=|J|=2, I intersect J=empty) d_(h;I,J)^2`.

Then

`boxed:
 Omega_(1,h)
 = a^2 sum_(I intersect J=empty) det S_h[I,J]^2.`                (5.3)

and globally

`Omega_1(A)=sum_h Omega_(1,h)`.

Now split the literal leaves independently into `R` and `C` with probability `1/2`. For a fixed ordered disjoint pair `(I,J)` with `|I|=|J|=2`, the event `I subset R, J subset C` has probability `1/16`. Therefore some physical cut satisfies

`sum_(I subset R, J subset C, |I|=|J|=2)
 det S_h[I,J]^2
 >= Omega_(1,h)/(16a^2).`                                       (5.4)

By Cauchy-Binet, the left side is exactly

`e_2(S_h[R,C] S_h[R,C]^T)`.

Hence

`boxed:
 e_2(S_h[R,C] S_h[R,C]^T)
 >= Omega_(1,h)/(16a^2).`                                       (5.5)

Thus a nonzero scalar physical pivot converts overlap-one mass into an exact **disjoint rank-two cross-volume** of its Schur complement. The only missing analytic/global step is to spend this currency without first selecting a pivot whose reciprocal scale loses dimension. The zero-pivot endpoint `a=0` is correctly left separate; (5.2) is not used there.

## 6. What the two identities accomplish globally

The previous third-compound operator-gap theorem says every still-unpaid target matrix has `Omega_1>=1/4` or `Omega_2>=1/4`. Equations (2.4) and (5.3) now show exactly where these two masses live:

- overlap two is the sum, over literal physical pairs, of off-diagonal Frobenius energies of denominator-free pair Schur numerators;
- overlap one, away from zero scalar pivots, is the sum, over literal physical pivots, of disjoint second-compound energies of scalar Schur complements.

For a **fixed** quantitative pivot, the literal-cut extraction is dimension free: `1/4` in the pair case and `1/16` in the scalar case. The unresolved issue is aggregation **before reciprocal pivot payment** when the global `Omega_1` or `Omega_2` is spread over many weak physical pivots. This report therefore avoids the false inference that a macroscopic global compound sum forces one universally good pivot.

The exact rank-one formula (4.3) further shows that the singular overlap-two collar has only two possible sources after the pair core collapses: a kernel-star currency visible in `q`, and leaf curvature that the overlap-two ledger itself cannot see. Any complete proof must retain that curvature analytically or route it into another paid sector.

## 7. Required designated partner result applied to an actual target inequality

Newest completed account02/B09 result consumed in this run:

`QFORM-RANKONE-PHYSICAL-PAIR-COLLINEAR-STAR-v1`,
source handoff `scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account02/B09/20260923T224553Z-account02-B09-QFORM-r15.md`,
canonical mathematics
`yspennstate/math-open-problems@57b57dc6fa114b1c782a91599bdfbe94a358b2cb`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T224553Z-account02-B09-QFORM-r15/REPORT.md`.

Its exact-rank-one collinear-star theorem states, in its homogeneous zero-leaf-block scope,

`||p_Q||_infinity
 <= 6 |tau|^(-1/3) ||A[I,H]k||_2^(-2/3)`.                     (7.1)

Take `m=8`, a physical pair `H={1,2}` with

`B=diag(8,0)`,

and eight leaves with zero leaf block and couplings only to the kernel hub coordinate,

`A[i,1]=0`, `A[i,2]=2/sqrt(8)` for every leaf `i`.

Then the active spectrum is exactly

`{8,2,-2}` plus zeros,

so the owner's three-large-eigenvalue hypothesis is satisfied. Here `tau=8`, `||A[I,H]k||_2=2`, and the designated partner theorem gives the actual target inequality

`boxed:
 ||p_Q||_infinity
 <= 6*8^(-1/3)*2^(-2/3)
 = 1.8898815748... < 1.890.`                                    (7.2)

Hence

`boxed: P{Q in J}<1.890 |J|}`                                  (7.3)

for every interval `J`. Continuity is **not claimed here** because the cited partner statement used in (7.1) reports essential boundedness in this branch but does not separately state a continuity conclusion.

The new identity checks the same example exactly:

`Omega_(2,H)
 = 8^2[(2^2)^2 - 8*(2/sqrt(8))^4]
 = 896.`                                                        (7.4)

Thus the partner receiver is being applied to precisely the singular-pair overlap-two currency isolated by (2.3)-(4.3).

## 8. Deterministic verification

Independent numerical checks were run on random symmetric matrices:

- for random `8 x 8` matrices and several physical pairs, the direct sum of squared overlap-two bordered determinants agreed with `||offdiag N_H||_F^2` to floating error;
- for random `8 x 8` matrices and a nonzero scalar pivot, the direct overlap-one sum agreed with `a^2` times the disjoint `2 x 2` Schur-minor sum to floating error;
- the scaled partner regression has eigenvalues `{-2,0,...,0,2,8}`, `Omega_(2,H)=896`, and bound `1.8898815748423097`.

These checks are regression evidence only; the proofs above are algebraic.

## 9. Remaining implication

The next B09 frontier is

`QFORM-OMEGA12-AGGREGATE-BEFORE-PIVOT-INVERSION-v1`:

> Starting from the guaranteed `Omega_1>=1/4` or `Omega_2>=1/4`, aggregate the scalar/pair Schur-numerator currencies across physical pivots before paying inverse pivot scales. If the mass concentrates on zero/near-zero pivots, route it to the literal kernel-star / zero-pivot / finite-collar receivers while retaining arbitrary same-bank curvature. Do not infer a constant-size individual pivot from a global compound sum.

For overlap two, (4.1)-(4.3) identify the exact singular endpoint and prove that arbitrary leaf curvature is invisible at `det B=0`; therefore the next analytic advance must genuinely retain that curvature rather than discard it as a small perturbation. For overlap one, (5.5) shows that every nonzero scalar packet already contains the desired disjoint rank-two bilinear currency; only the global reciprocal-pivot aggregation and zero-pivot collar remain.

## 10. Correction audit and status

No Gaussian, log-concavity, moment, support, centering, or post-rotation independence assumption is used. The argument does not use law-uniform pointwise van-der-Corput decay, arbitrary-joint coarea, fiber-sup integration, Monte Carlo extremality, or probability-squaring. The only 2D diagonalization in Section 4 is an algebraic identity inside the deterministic pair coefficient space; all analytic statements remain tied to literal original coordinates.

**Conclusion:** `QFORM-OVERLAP12-SCHUR-NUMERATOR-COMPILER-v1` is proved at the stated deterministic scope, and the fixed indefinite-pair corollary (3.2)-(3.3) is a genuine density/interval consequence. The full target remains OPEN / not proved / not disproved. Full-target continuity remains OPEN.
