SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B11, 2026-09-24T10:55:53Z.
attacking: the determinant-only physical indefinite 3x3 closure obtained by splicing the partner L^3 indefinite-pair theorem with the pinned pair-log Schur receiver; remove the vanishing diagonal-pivot loss.

# fleet02/B11 r13 — determinant-only closure for every literal indefinite physical triple

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: indefinite signatures / complementary constructions and source-valid counterexamples  
Status: `NEW AMBIENT PHYSICAL-TRIPLE THEOREM / FULL QFORM OPEN`

The unrestricted conjecture remains OPEN / not proved / not disproved. No moment, support, log-concavity, iid, diagonal-basis, or post-rotation independence assumption is used. Continuity is kept separate.

The first unpaid implication after the theorem below is:

`QFORM-DET49-AGGREGATE-EXTRACTION-v1`: under the bare three-large-eigenvalue hypothesis, prove that either some literal original-coordinate indefinite principal triple has determinant bounded below at the target spectral scale, or one of the already-paid diffuse/cross-volume/hub receivers applies. Arbitrary additional nonseparable spectrum remains part of that structural extraction problem.

## 1. Completed inputs actually used

1. Designated partner fleet03/B11 r55, `QFORM-INDEFINITE-PAIR-L3-v1`, source `yspennstate/math-open-problems@bc05973cb71eb6707de7342cafeef36af6a99230`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260924T101550Z-fleet03-B11-QFORM-r55/REPORT.md`: for independent physical variables with cap-one densities and every invertible indefinite symmetric 2x2 matrix `P`, including arbitrary affine terms,

   `||p||_3 <= 22 |det P|^(-1/3)`.

2. Completed dependent square-smoothing lemma, fleet03/B06 r52, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260924T052046Z-fleet03-B06-qform-r52/REPORT.md`: if a base output has density `p` with `||p||_3<=M` and, conditional on the base, the translated physical scalar still has density cap one, then adding `lambda V^2` gives

   `||p_out||_infinity <= 4 |lambda|^(-1/2) M^(3/4)`.

3. Required pinned source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`: the completed indefinite pair-log receiver says that if an invertible indefinite physical pair `P` has determinant magnitude `D_P`, smallest singular value `sigma`, and its Schur remainder satisfies

   `sup_s P(|R-s|<=rho) <= H sqrt(rho)`,

   then

   `||p_Q||_infinity <= 4 sqrt(2H) (D_P sigma)^(-1/4)`.

The same pinned package's ruled Theorem C is used in Section 5 at a real one-sheet inequality. Its `FOURIER_ROUTE_REPORT.md` and `COUNTEREXAMPLE_SEARCH.md` were also read at the pinned commit; no counterexample was supplied there and the two-sheet side remains outside the ruled theorem.

## 2. A universal L^3 physical-pair lemma for either inertia

The partner gives the indefinite case with constant 22. The definite case is easier and lets the later pivot have either sign.

Let `P` be any invertible definite symmetric 2x2 physical coefficient matrix and let `X,Y` be independent cap-one variables. Complete arbitrary affine terms by coordinatewise constant translations. After the linear map `u=|P|^(1/2)x`, the joint density is bounded by `|det P|^(-1/2)`. The pushforward of a planar density bounded by `K` under `u -> |u|^2` has density at most `pi K`; hence

`||p||_infinity <= pi |det P|^(-1/2)`.

Interpolating with `||p||_1=1`,

`||p||_3 <= pi^(2/3) |det P|^(-1/3) < 22 |det P|^(-1/3)`.

Therefore, for every invertible symmetric physical pair, definite or indefinite,

`boxed: ||p||_3 <= 22 |det P|^(-1/3).`                    (2.1)

This extension is source-preserving: the only rotation is an analytic change of variables in the two-dimensional density integral; no independence is asserted after that rotation.

## 3. Main theorem: determinant-only physical indefinite triple

### Theorem — `QFORM-INDEFINITE-PHYSICAL-TRIPLE-DET49-v1`

Let `I={i,j,k}` be three literal original coordinates. Suppose the 3x3 principal block

`B=A_II`

is invertible and indefinite. Let `D=|det B|`. Then for arbitrary independent input densities `f_l<=1`, arbitrary coefficients and couplings involving all coordinates outside `I`, and arbitrary affine terms, the full quadratic form has an essentially bounded density satisfying

`boxed: ||p_(X^T A X)||_infinity <= 49 D^(-1/3).`          (3.1)

Thus if the literal physical triple itself has three eigenvalues of modulus at least `s`, then `D>=s^3` and

`boxed: ||p||_infinity <= 49/s.`                          (3.2)

No continuity conclusion is claimed from this argument.

### Proof

Condition on every original coordinate outside `I`. This changes the form on the three retained independent cap-one variables only by affine and constant terms, while keeping the same quadratic block `B`. It is therefore enough to prove (3.1) in dimension three, uniformly in affine terms.

Write

`B=[[a,x,y],[x,b,z],[y,z,c]]`,

and define

`r=D^(1/3)`, `m=max(|a|,|b|,|c|)`, `e=max(|x|,|y|,|z|)`.

We split according to the size of the largest physical diagonal.

### Case A: a physical diagonal is at least `r/2`

Suppose, after relabelling, `lambda=c` and

`|lambda|=m >= r/2`.                                      (3.3)

Complete the square only in the literal independent coordinate `X_k`:

`Q=lambda (X_k+mu(X_i,X_j))^2 + R(X_i,X_j)`.

The pair matrix of `R` is the Schur complement

`S = B_{ij,ij} - B_{ij,k} B_{k,ij}/lambda`,

and

`det B = lambda det S`.                                    (3.4)

Because `B` is invertible, `S` is invertible. By (2.1), irrespective of whether `S` is definite or indefinite,

`M:=||p_R||_3 <= 22 |det S|^(-1/3)
                 =22 (|lambda|/D)^(1/3).`                  (3.5)

The literal `X_k` is independent of `(X_i,X_j)`. Conditional on `R`, the translated variable `X_k+mu(X_i,X_j)` is therefore a mixture of translates of the original cap-one law and still has density cap one. The completed dependent square-smoothing lemma gives

`||p_Q||_infinity
 <=4 |lambda|^(-1/2) M^(3/4)
 <=4*22^(3/4) |lambda|^(-1/4) D^(-1/4).`                   (3.6)

Using (3.3),

`||p_Q||_infinity
 <=4*22^(3/4)*2^(1/4) D^(-1/3)
 =48.32084283629789... D^(-1/3)
 <49 D^(-1/3).`                                            (3.7)

This case removes the sign restriction on the partner r55 pivot: if the Schur pair is definite, the elementary definite-pair estimate supplies the same `L^3` scale.

### Case B: every physical diagonal is smaller than `r/2`

Assume

`m < r/2`.                                                  (3.8)

The exact determinant expansion gives

`det B = abc + 2xyz - a z^2 - b y^2 - c x^2`,

hence

`D <= m^3 + 2e^3 + 3me^2`.                                 (3.9)

If `e<=9r/16`, then (3.8)-(3.9) imply

`D < r^3 [1/8 + 2(9/16)^3 + (3/2)(9/16)^2]
   = (1957/2048) D`,                                       (3.10)

an impossibility. Therefore

`e > 9r/16`.                                                (3.11)

Choose the physical 2x2 principal block `P` containing an off-diagonal entry of magnitude `e`. It is a perturbation of `[[0,e],[e,0]]` by a diagonal matrix of operator norm at most `m`. Weyl's singular-value inequality and (3.8),(3.11) give

`boxed: sigma_min(P) >= e-m > r/16.`                        (3.12)

Moreover `e>m` implies `e^2>|ab|` for the corresponding two diagonal entries, so `P` is invertible indefinite.

Complete this literal physical pair, leaving the third original coordinate `Z`. Its scalar Schur remainder has nonzero quadratic coefficient

`kappa = det B / det P`.                                    (3.13)

After completing its affine term it is `kappa (Z-z0)^2+const`. Since `Z` has density cap one, for every `s,rho`,

`P(|kappa(Z-z0)^2-s|<=rho)
 <=2 sqrt(2rho/|kappa|).`                                   (3.14)

Thus the pinned completed pair-log theorem applies with

`H=2 sqrt(2) |kappa|^(-1/2)`.

It yields

`||p_Q||_infinity
 <=4 sqrt(2H) (|det P| sigma_min(P))^(-1/4)
 =8*2^(1/4) (D sigma_min(P))^(-1/4)`.                        (3.15)

Using (3.12),

`||p_Q||_infinity
 <16*2^(1/4) D^(-1/3)
 =19.027313840043536... D^(-1/3)
 <49 D^(-1/3).`                                             (3.16)

Cases A and B prove (3.1). Averaging the uniformly bounded conditional densities over the coordinates outside `I` proves the ambient statement. QED.

## 4. Exactly how the third direction removes the rank-two logarithm

The rank-two obstruction remains literal. For independent centered unit uniforms,

`R=2XY`

has

`p_R(t)=log(1/(2|t|)),  0<|t|<1/2`,                         (4.1)

so the density is unbounded. The partner r55 theorem records simultaneously that this logarithm lies in `L^3` (`||p_R||_3^3=6`).

The determinant-only triple proof uses two exact third-direction mechanisms, depending on the physical geometry:

* In Case A the third literal coordinate is a nonzero scalar pivot. The residual two-coordinate output may still have the logarithmic saddle, but it has uniform `L^3`; the conditionally translated square has the conjugate half-power singularity, and the dependent `L^3 -> L^infinity` square-smoothing lemma makes their combined output bounded. The rank-two saddle is never falsely declared bounded first.

* In Case B the physical diagonals are too small, so determinant currency forces a quantitatively transverse indefinite pair. Its logarithmic pair kernel is retained. The third coordinate survives through the scalar Schur coefficient `kappa`; its square small-ball law is exactly `O(rho^(1/2))`. The pinned pair-log receiver integrates that half-power against the logarithmic pair singularity and produces (3.15). Thus a vanishing diagonal pivot does not remove the third direction: determinant conservation moves it into the Schur square.

For the canonical model

`Q=2XY+Z^2`,                                                  (4.2)

the pair `2XY` has the logarithmic blow-up (4.1), while `kappa=1` and `sigma_min([[0,1],[1,0]])=1`; (3.15) already gives a finite full-line bound. The sharper source-disjoint `L^3 * L^(3/2)` theorem from partner r55 gives `||p_Q||_infinity<=44`.

## 5. Sign-specific ruled geometry: one-sheet side versus two-sheet side

For an exact physical rank-three block of signature `(2,1)` with eigenvalue magnitudes at least `s`, the required pinned source's ruled Theorem C gives the sharper one-sheet estimate, after removing affine terms by constant coordinate translations and shifting the critical value `t_*`,

`boxed: p_Q(t) <= pi sqrt(2)/s  for t>=t_*.`                  (5.1)

For signature `(1,2)`, applying the same theorem to `-Q` gives

`boxed: p_Q(t) <= pi sqrt(2)/s  for t<=t_*.`                  (5.2)

I do not transfer this ruling/X-ray estimate to the opposite two-sheet side; the live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` forbids that inference. The determinant-only theorem (3.1) pays the full line, including that opposite side, whenever the physical triple determinant is quantitative.

In particular, for the canonical `2XY+Z^2`, whose coefficient matrix has spectrum `{1,1,-1}`, the pinned ruled theorem gives `p_Q(t)<=pi sqrt(2)` for `t>=0`, while (3.1) pays all `t` by `49`; the two-sheet side `t<0` is not obtained from ruling geometry.

## 6. Consequence for the designated partner frontier

Partner r55 left `QFORM-INDEFINITE-PAIR-L3-NULLPIVOT-COMPILER-v1`: remove the `|lambda|^(-1/4)` loss as usable majority-sign physical pivots vanish. The theorem above resolves that issue whenever the same literal physical triple retains determinant currency: if a diagonal pivot is large, Case A pays it; if all diagonal pivots are small, determinant expansion forces a transverse indefinite pair and the pinned pair-log Schur receiver pays Case B.

What remains is no longer an analytic null-pivot problem for a fixed determinant-localized physical triple. It is the global structural extraction problem stated at the top: show that the bare three-large-eigenvalue hypothesis forces a quantitative determinant-localized triple or one of the already-paid aggregate/diffuse exits. The full arbitrary-matrix conjecture remains open.

## 7. Deterministic checks

The two constants are

`4*22^(3/4)*2^(1/4) = 48.32084283629789... < 49`,

`16*2^(1/4) = 19.027313840043536... < 49`.

The rational determinant contradiction is exact:

`1/8 + 2(9/16)^3 + (3/2)(9/16)^2 = 1957/2048 < 1`.

No numerical experiment is used as evidence for the universal theorem; these arithmetic evaluations only check the displayed constants.
