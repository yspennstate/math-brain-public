SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-24T00:22:22.352142Z.
attacking: QFORM-DOUBLEZERO-COORDINATE-HYPERBOLA-SCHUR-SQUARE-v1 — retain the exact coordinate hyperbola in the two scalar banks and average its true logarithmic/tail kernel against the Schur square before any fiber supremum or conditional projection cap.

# account02/B05 — scale-invariant coordinate-hyperbola / Schur-square interval theorem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: quadratic coarea bound / complementary source-valid constructions  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING ROUGH-INPUT INTERVAL THEOREM / EXACT DOUBLE-ZERO SCALAR-PAIR FACE PAID / FULL QFORM OPEN**  
Continuity: **not claimed**; the theorem gives absolute continuity and an essential density bound by an interval estimate.

The first unpaid implication after this run is

`QFORM-DOUBLEZERO-TO-PUNCTURED-GENERAL-HYPERBOLA-v1`:

> extend the exact coordinate-product receiver proved below from the physical scalar pair `[[0,c],[c,0]]` to an indefinite pair with small nonzero diagonals, uniformly through the double-zero limit, while retaining the original two scalar product banks. Equivalently, obtain the source-valid interpolation for the product of two **general** linear forms of a two-scalar product law before taking absolute fiber suprema.

This is precisely the bounded-dimensional `R2` interpolation identified as open in the pinned Fourier report. The present theorem pays its exact coordinate endpoint with the correct determinant scale and with arbitrary same-bank overlap translations preserved.

## 1. Fresh sources and corrections actually used

Fresh designated partner:

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T234035Z-account03-B05-QFORM-r35/REPORT.md`.

Its new theorem `QFORM-SCALAR-HEAVY-PIVOT-CROSSING-v1` proves an asymmetric original-bank rank-three crossing and isolates as a genuine survivor the double-heavy scalar / collapsed-currency chamber; in the exact literal-literal endpoint `q_Y=q_Z=1` both of its one-tail currencies vanish. The result below supplies a different receiver on the exact double-zero scalar-pair face and does not split either scalar bank.

Required pinned source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Two completed facts are applied to the live obstruction:

1. Theorem F gives, for every exact-rank-three target frame whose physical spectral leverages are all at most `1/2`,

`||p_Q||_infinity <= 12`.

Hence the scalar-pair endpoint below is needed only after the genuine physical diffuse gate has failed; no spectral rotation is declared probabilistically independent.

2. The ruled one-sheet theorem gives, in target normalization and signature `(2,1)`,

`p_Q(s) <= pi*sqrt(2),  s>=0`.

The new theorem is a full-line interval estimate on the exact double-zero scalar-pair packet, so in the `(2,1)` case it supplies a source-valid receiver on the complementary convex/two-sheet side as well. The pinned counterexample search still reports no target-valid counterexample.

Live corrections remain binding: no arbitrary-joint quadratic coarea theorem, no conditional cap for conjugate projections, no interval-to-Borel promotion, no unrestricted curved-fiber supremum, no deletion of small coefficient tails, and no perturbative claim that a small quadratic coefficient is a small random error.

## 2. A sharp enough product kernel for arbitrary rough scalar densities

Let `U,V` be independent real random variables with probability densities bounded by one. Their product `W=UV` has, for `w!=0`,

`p_W(w)=int f_U(u) f_V(w/u) du/|u|`.                               (2.1)

Two elementary bounds will be used **together**.

### Lemma 2.1 — logarithmic core and inverse-square-root tail

For every `w!=0`,

`boxed:
 p_W(w) <= 2[1+log_+(1/|w|)],
 p_W(w) <= 2 |w|^(-1/2).
`                                                                      (2.2)

Proof of the logarithmic bound. If `0<|w|<1`, split the `u` integral into

`|u|>1`, `|u|<=|w|`, and `|w|<|u|<=1`.

The first part is at most one. In the second use `v=w/u`; then `|v|>=1` and the part is at most one. On the middle annulus use both caps `<=1`, obtaining

`int_(|w|<|u|<=1) du/|u| =2 log(1/|w|)`.

For `|w|>=1`, the same split at `|u|=1` gives at most two. This proves the first estimate.

For the second estimate split at `|u|=sqrt(|w|)`. The outer part is at most `|w|^(-1/2)` by the mass of `f_U`; after `v=w/u`, the inner part is at most the same quantity by the mass of `f_V`. QED.

Consequently, for `c!=0`, the density of `2cUV` obeys

`boxed:
 k_c(r)
 <= |c|^(-1)[1+log_+(2|c|/|r|)],
 k_c(r)
 <= sqrt(2)/(sqrt(|c| |r|)).
`                                                                      (2.3)

The same bounds hold after **arbitrary translations** of `U` and `V`; translations preserve both probability mass and the density cap.

The simultaneous use of both bounds in (2.3) is essential. Keeping only the logarithmic envelope leaves a spurious `|c|^(-1)` loss; keeping only the half-Riesz envelope is singular at the Schur-square critical value. Their exact crossover is what removes the pair scale.

## 3. Schur-square small balls

Let `S` have density cap `M`. For any `L!=0`, shift `s_0`, center `t`, and `rho>0`,

`boxed:
 P(|L(S-s_0)^2-t|<rho)
 <= min{1, K sqrt(rho)},
 K=2 sqrt(2) M / sqrt(|L|).
`                                                                      (3.1)

Indeed the inverse image under `s -> L(s-s_0)^2` of an interval of radius `rho` has total length at most

`2 sqrt(2 rho/|L|)`.

This is a rough-law statement and uses only the one-dimensional density cap.

## 4. Main theorem — coordinate hyperbola averaged before maximalisation

### Theorem `QFORM-COORD-HYPERBOLA-SCHUR-SQUARE-v1`

Let `S` be any real random variable with density cap `M_S`. Let `(S,E)` be an arbitrary joint environment. Let `Y,Z` be independent of `(S,E)`, independent of each other, with density caps `M_Y,M_Z`. Let `F(S,E),G(S,E)` be arbitrary measurable real functions. For `L,c!=0`, put

`Q=L(S-s_0)^2+2c [Y+F(S,E)][Z+G(S,E)]+q_0`.                        (4.1)

Then every finite interval `I` satisfies

`boxed:
 P(Q in I)
 <= C_H (M_S M_Y M_Z)^(2/3)
       (|c|^2 |L|)^(-1/3) |I|,
`                                                                      (4.2)

where

`C_H=3(1+exp(-2/3)) 4^(2/3)
   =11.4407165132... .`                                               (4.3)

Hence `Q` is absolutely continuous and

`boxed:
 ||p_Q||_(infinity,ess)
 <= C_H (M_S M_Y M_Z)^(2/3)
       (|c|^2 |L|)^(-1/3).
`                                                                      (4.4)

No continuity of the output density is asserted.

### Proof

Scale `S,Y,Z` by their density caps. It is enough to prove the result for `M_Y=M_Z=1` and a general cap `M=M_S`; the final scaling multiplies the right side by `(M_S M_Y M_Z)^(2/3)`.

Condition on `(S,E)`. The two bracketed factors in (4.1) are independent translated cap-one variables. By (2.3), for `r=|t-L(S-s_0)^2|`, their conditional output density is bounded by

`|c|^(-1)[1+log_+(2|c|/r)]`                                         (4.5)

and by

`sqrt(2) |c|^(-1/2) r^(-1/2)`.                                      (4.6)

Set `a=|c|`, `tau=a^2 |L|`, and

`x=K sqrt(2a)=4 M a^(3/2)/sqrt(tau)`,                               (4.7)

where `K` is from (3.1).

Use (4.5) on the near-critical region `r<=2a`. Layer cake and (3.1) give

`E log_+(2a/r)
 <= J(x),`

where

`J(x)=2x` for `x<=1`, and `J(x)=2+2 log x` for `x>=1`.              (4.8)

Therefore the near contribution is

`N <= a^(-1)[min(1,x)+J(x)].`                                       (4.9)

If `x<=1`,

`N<=3x/a
 =3 (4M)^(2/3) tau^(-1/3) x^(1/3)
 <=3 (4M)^(2/3) tau^(-1/3).`                                       (4.10)

If `x>=1`, use

`a^(-1)=(4M)^(2/3) tau^(-1/3) x^(-2/3)`                            (4.11)

and the elementary monotonicity

`x^(-2/3)(3+2 log x)<=3, x>=1`,                                    (4.12)

to obtain the same bound.

On the far region `r>2a`, use (4.6). From (3.1),

`E[r^(-1/2) 1_(r>h)]
 <= h^(-1/2),                         if K sqrt(h)>=1,
 <= K[1+log(1/(K sqrt(h)))],          if K sqrt(h)<1.`              (4.13)

This follows by layer cake for `r^(-1/2) 1_(r>h)` and the bound `P(r<u^(-2))<=min(1,K/u)`. Taking `h=2a` yields

`F <= (4M)^(2/3) tau^(-1/3)` for `x>=1`,                            (4.14)

while for `x<1`,

`F <= (4M)^(2/3) tau^(-1/3)
      x^(1/3)[1+log(1/x)].`                                         (4.15)

The scalar function on the last line has maximum

`sup_(0<x<=1) x^(1/3)(1+log(1/x))=3 exp(-2/3).`                     (4.16)

Combining (4.10)-(4.16),

`sup_t p_Q(t)
 <= [3+3 exp(-2/3)](4M)^(2/3) tau^(-1/3),`                          (4.17)

which is (4.4) for `M_Y=M_Z=1`. Fubini gives the corresponding interval domination directly, so no output continuity or interval-to-Borel upgrade is being assumed. QED.

## 5. Exact double-zero scalar-pair face of the ratio packet

Use the fresh account03/B05 ratio notation. The first product bank supplies an orthonormal two-dimensional projection

`(S,R)=Gamma^T X`, `Gamma^T Gamma=I_2`,

and two disjoint scalar banks supply normalized independent projections `Y,Z`. The Schur factorization is

`H=K^T D K`,
`D=diag(L,B)`,
`L=lambda m`,
`mu=|det B| |lambda|`.

On the exact double-zero scalar-pair face

`B=[[0,c],[c,0]], c!=0`,                                            (5.1)

so the homogeneous packet is exactly

`Q=L S^2
  +2c [Y+A11 S+A12 R][Z+A21 S+A22 R].`                             (5.2)

The overlap coefficients `A11,A12,A21,A22` are left untouched. In particular the same-bank residual coordinate `R` is **not conditioned**, and no assertion is made that `S` and `R` are independent.

The one-dimensional product-projection theorem gives

`||p_S||_infinity,
 ||p_Y||_infinity,
 ||p_Z||_infinity <=sqrt(2).`                                       (5.3)

The three source banks are mutually independent, so Theorem 4 applies with

`M_S M_Y M_Z <=(sqrt(2))^3=2 sqrt(2)`,

whose `2/3` power is exactly `2`. Since

`|c|^2 |L|
 =|det B| |lambda| m
 =mu m`,                                                            (5.4)

we obtain the full rough-input interval theorem

`boxed:
 P(Q in I)
 <= 2 C_H (mu m)^(-1/3) |I|
 <22.882 (mu m)^(-1/3)|I|,
`                                                                      (5.5)

and therefore

`boxed:
 ||p_Q||_(infinity,ess)
 <22.882 (mu m)^(-1/3).
`                                                                      (5.6)

For the standard ratio packet `m>=3/20`,

`boxed:
 ||p_Q||_(infinity,ess)
 <43.065 mu^(-1/3).
`                                                                      (5.7)

Thus on the hard subbranch `mu>=1`, the **entire exact double-zero scalar-pair face** has a universal bound `<43.065`.

This payment does not require `q_Y,q_Z` to be diffuse or heavy, does not require `q_xi<1/4`, does not split either scalar bank, and is uniform in every overlap coefficient in (5.2). In particular it pays the exact literal-literal endpoint `q_Y=q_Z=1` that the fresh account03/B05 r35 crossing correctly leaves unresolved.

## 6. Range-affine terms in the exact-rank-three application

The theorem above is stated in the homogeneous form relevant to `X^TAX`. A useful exact-rank-three conditioning observation prevents an artificial affine objection.

If a retained principal block `H` has the full rank three of a global exact-rank-three matrix and conditioning outside it creates an affine vector `b`, then `b` lies in `Ran(H)`: writing the global matrix as `R Lambda R^T`, full column rank of the retained `R_I` gives

`Ran(A_II)=Ran(R_I)`, while `A_IJ x_J=R_I Lambda R_J^T x_J` lies in that same range. Therefore there is a deterministic `h` with `2Hh=b`. The coordinatewise translation `x -> x+h` removes the affine term and preserves independence and every density cap. In (5.2) this merely translates `S,Y,Z` and the two bracketed factors, all already allowed by Theorem 4.

This observation is scoped to the exact-rank-three retained block. No claim is made that arbitrary affine terms outside `Ran(H)` can be discarded in a higher-rank problem.

## 7. What remains and why it is the right obstruction

The exact face `a=d=0` in

`B=[[a,c],[c,d]]`

is now paid uniformly even as `c->0` and `|lambda|->infinity` with `|det B||lambda|` fixed. The cancellation is not perturbative: the logarithmic product kernel is averaged against the Schur square at the true scale before any supremum.

For `a,d` nonzero, an indefinite pair factors into the product of two **general** linear forms of `(Y,Z)`. Those two factors share both scalar variables, so the independent-coordinate product kernel Lemma 2.1 no longer applies. This is exactly the pinned Fourier report's open `R2` interpolation. Existing nonzero-pivot theorems pay quantitative collars but deteriorate as `a,d->0`, while the live correction `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` forbids filling the puncture by a naive small-diagonal argument.

So the first unpaid implication is genuinely the punctured general-hyperbola bridge, not the exact coordinate endpoint and not a missing scalar-tail split.

## 8. Status

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN**.  
New theorem: **proved rough-input interval bound and essential density bound; continuity not claimed**.  
Native brain status: `WITHOUT_VERIFIED_BRAIN`.  
Configured/effective reasoning effort: `UNKNOWN`; provider reasoning tokens/time: `null / not exposed`.

No moment, support, log-concavity, diagonal-basis, post-rotation independence, arbitrary-joint coarea, conditional projection cap, unrestricted curved-fiber supremum, or small-random-error assumption is used.
