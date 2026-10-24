SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-24T05:11:20Z.
attacking: the punctured same-source majority-sign collar by an exact volume-preserving LDL factorization that keeps the original product provenance and identifies where the third direction goes as the physical pivot tends to zero.

# account03/B11 r50 — volume-preserving three-square LDL normal form for the punctured indefinite collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: indefinite signatures `(2,1)` / `(1,2)`  
Status: **NEW EXACT STRUCTURAL THEOREM / FRESH DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: **not proved by this run**.

The unrestricted owner target remains OPEN / NOT PROVED / NOT DISPROVED. The theorem below is an exact-rank-three structural reduction for the genuinely rotated indefinite small-pivot collar. It does not add Gaussianity, moments, support assumptions, log-concavity, connected support, iid assumptions, or independence after spectral rotation. It does not use law-uniform pointwise quadratic-phase decay, an arbitrary-joint coarea theorem, a worst conditional-density cap, or perturbative deletion of a small coefficient.

## 1. Fresh source state actually used

Fresh `yspennstate/math-research-brain/main` was read at startup, including `AGENTS.md`, the full owner message, fleet/role/protocol files, programme MANIFEST, CURRENT_RESEARCH, CLAIMS, live CORRECTION_INBOX, MEMORY_PROTOCOL and this exact `account03/B11` assignment. OWNER CONTROL remains revision `2026-09-22.15`; QFORM is the sole research target and the full conjecture remains open.

The immediate B11 predecessor is account03/B11 r49, whose theorem `QFORM-R48-CANCELLATION-XRAY-IMPOSSIBILITY-v1` proves that the explicit nonlinear same-bank cancellation law used to preserve the rank-two logarithm cannot be a genuine orthogonal projection of a cap-one product source. That result narrows the unpaid step to a product-provenance trace estimate; it does not itself give a linear small-ball bound.

The fresh designated partner result used at an actual equation below is account04/B11 r1,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260924T041708Z-account04-B11-schur-pseudodet-r1/REPORT.md`,

theorem `QFORM-SPECTRAL-SCHUR-PSEUDODET-v1`. For an exact-rank-three matrix and a nonzero literal physical pivot `alpha=A_hh` of spectral leverage `q_h`, it gives

`Delta_2(S)=q_h Delta_3(A)/|alpha|`,

where `S` is the physical Schur complement.

## 2. Exact heavy-row coordinates

Let

`A = R M R^T`, `R^T R=I_3`,

with `M` real symmetric invertible. Let

`sigma = min |lambda_j(M)| >0`, `D=|det M|`.

Fix an ORIGINAL physical coordinate `h` with spectral leverage

`q=||R^T e_h||^2 in (0,1)`.

After an orthogonal change only in the deterministic three-dimensional spectral coefficient space, not in the random inputs, write the physical spectral row as

`R^T e_h = sqrt(q) e_1`.

Choose `e_2` parallel to the transverse component of `M e_1` (if that component is zero, choose any transverse `e_2`). Complete by `e_3`. Then

`M = [[a,r,0],
      [r,b,c],
      [0,c,d]].`                                                   (2.1)

Let `R_-` be `R` with physical row `h` removed, and define residual coefficient vectors

`t=R_- e_1`, `y=R_- e_2`, `w=R_- e_3`.

Since

`R_-^T R_- = I_3 - q e_1 e_1^T`,

we have the exact Parseval relations

`||t||^2=1-q`, `||y||=||w||=1`,
`<t,y>=<t,w>=<y,w>=0`.                                           (2.2)

For the ORIGINAL independent inputs put

`H=X_h`, `T=<t,X_->`, `Y=<y,X_->`, `W=<w,X_->`.

No independence is asserted among `(T,Y,W)`. The only literal source separation is that `H` is independent of the entire residual product bank. The form is exactly

`Q = a(sqrt(q)H+T)^2
    +2r(sqrt(q)H+T)Y
    +bY^2+2cYW+dW^2`.                                           (2.3)

The physical pivot is

`alpha=A_hh=q a`.                                                 (2.4)

## 3. New theorem: volume-preserving three-square LDL factorization

### Theorem `QFORM-PUNCTURED-VOLUME1-LDL-v1`

Assume `a!=0` and `d!=0`. Define

`U = sqrt(q)H + T + (r/a)Y`,
`V = W + (c/d)Y`,
`gamma = det(M)/(a d)`.                                           (3.1)

Then the entire quadratic form has the exact identity

`boxed: Q = a U^2 + gamma Y^2 + d V^2.`                           (3.2)

Let `u,y_bar,v` be the three coefficient vectors of `(U,Y,V)` in the ORIGINAL physical-coordinate space. Then

`boxed: det Gram(u,y_bar,v)=1`,                                  (3.3)

and

`boxed: a gamma d = det M.`                                      (3.4)

Moreover

`boxed: det Gram(y_bar,v)=1`,                                    (3.5)

so `(Y,V)` is a determinant-one shear of the orthonormal product projection `(Y,W)`.

#### Proof

Complete the first and third squares in (2.3):

`a(sqrt(q)H+T)^2+2r(sqrt(q)H+T)Y
 = a(sqrt(q)H+T+(r/a)Y)^2 - (r^2/a)Y^2`,

and

`dW^2+2cYW=d(W+(c/d)Y)^2-(c^2/d)Y^2`.

Therefore the remaining `Y^2` coefficient is

`b-r^2/a-c^2/d
 = [a(bd-c^2)-r^2 d]/(ad)
 = det(M)/(ad)=gamma`,

which proves (3.2) and immediately (3.4).

For the volume statement, introduce the normalized residual direction `t_0=t/sqrt(1-q)` when `q<1`. In the orthonormal physical coefficient frame `(e_h,t_0,y,w)`, the three coefficient vectors are

`u=(sqrt(q),sqrt(1-q),r/a,0)`,
`y_bar=(0,0,1,0)`,
`v=(0,0,c/d,1)`.                                                  (3.6)

The span of `(y_bar,v)` is exactly `span(y,w)` and has parallelogram area one because the shear has determinant one. The component of `u` perpendicular to that plane is

`(sqrt(q),sqrt(1-q),0,0)`,

whose norm is exactly one. Hence the three-dimensional volume is one, proving (3.3); (3.5) is the two-dimensional part of the same calculation. The `q=1` endpoint follows by deleting the zero `t_0` component. QED.

### Product provenance retained exactly

Let `C=[u,y_bar,v]`. Because `det(C^T C)=1`, orthonormalizing the columns of `C` has Jacobian one. The standard three-dimensional product-projection density theorem therefore gives the source-valid marginal cap

`||p_(U,Y,V)||_infinity <= 2^(3/2)`,                              (3.7)

and similarly

`||p_(Y,V)||_infinity <=2`.                                      (3.8)

These are not independence statements. More importantly, the full characteristic function keeps the original coordinate factorization

`E exp(i<xi,(U,Y,V)>) = product_j hat f_j(xi_1 u_j+xi_2 y_j+xi_3 v_j)`.   (3.9)

Thus (3.2) diagonalizes the *quadratic polynomial* without diagonalizing the random law.

The live correction that an arbitrary bounded three-dimensional joint density does not control an indefinite quadratic pushforward remains binding, so (3.7) alone is deliberately not promoted to a density theorem.

## 4. Fresh account04/B11 Schur identity becomes an exact coefficient identity

Let `S_h` be the physical Schur complement at the literal coordinate `h`. The designated account04/B11 theorem gives

`Delta_2(S_h)=q D/|A_hh|`.

Using `A_hh=q a`, this becomes

`boxed: Delta_2(S_h)=D/|a|.`                                     (4.1)

But the new factorization gives

`|gamma d| = D/|a|`.                                             (4.2)

Hence the fresh partner theorem is applied at the exact equality

`boxed: |gamma d| = Delta_2(S_h).`                               (4.3)

This is more than a bookkeeping match: the entire physical rank-two Schur pseudodeterminant is realized as the product of the two completed residual square coefficients in the source-valid determinant-one shear `(Y,V)`.

In the live near-coloop/small-physical-pivot collar

`q>=63/64`, `0<|A_hh|<=sigma/64`,                                (4.4)

one has

`|a|=|A_hh|/q <= sigma/63`,

and therefore

`boxed: |gamma d|=Delta_2(S_h)>=63 sigma^2.`                      (4.5)

Thus the residual opposite-sign pair does not become weak when the physical pivot tends to zero; its two-volume blows up at exactly the reciprocal rate forced by the partner Schur budget.

A second quantitative identity shows that the completion is always legal in this live collar. Put `C_11=bd-c^2`. Since `||M^{-1}||<=1/sigma`,

`|C_11| <= D/sigma`.

From

`det M = a C_11-r^2 d`,

we obtain

`r^2 |d| >= D(1-|a|/sigma) >= (62/63)D >0`.                      (4.6)

Hence `r!=0` and `d!=0`, so the factorization (3.1) is valid throughout the punctured live collar.

## 5. Signature and the mandatory rank-two logarithmic control

For inertia `(2,1)`, `det M<0`; for inertia `(1,2)`, `det M>0`. In either case a **majority-sign** pivot `a` has the opposite sign from `det M`, and therefore

`gamma d = det M/a <0`.                                         (5.1)

So the completed residual pair in (3.2) is genuinely indefinite. A **minority-sign** pivot gives `gamma d>0`, hence a definite completed pair.

The rank-two control remains the exact logarithmic benchmark: for independent centered unit uniforms,

`p_(2XY)(z)=log(1/(2|z|))`, `0<|z|<1/2`.                         (5.2)

The new normal form shows precisely what happens to the third direction near a majority-sign puncture. It does **not** disappear. Instead:

1. the two opposite-sign residual curvatures satisfy `|gamma d|=Delta_2(S_h)>=63 sigma^2` in the live collar;
2. the small coefficient `a` is attached to the heavily sheared observable `U=sqrt(q)H+T+(r/a)Y`;
3. the three observable coefficient vectors keep exact unit three-volume, `det Gram=1`;
4. the coefficient product remains `a gamma d=det M`, so no curvature determinant is lost.

Thus the punctured singularity is a dependence/interpolation problem, not a curvature-loss problem. The third direction is transferred into a large source shear while the complete linear-product volume stays fixed.

For reference, the unconditional scalar projection theorem gives

`||p_U||_infinity <= sqrt(2)/sqrt(1+r^2/a^2)`,                    (5.3)

because `||u||^2=1+r^2/a^2`. This cap can become very small as the shear grows. It cannot be naively convolved with the residual indefinite pair, because `U` shares the same original source bank with `Y,V`; the live conditional-cap and arbitrary-joint corrections forbid exactly that shortcut.

## 6. What is newly reduced and what remains unpaid

The first B11 gap can now be stated without the earlier coordinate clutter.

`QFORM-VOLUME1-LDL-MAJORITY-COLLAR-v1`:

> Let `(U,Y,V)` be the volume-one linear image of the original product source produced by Theorem 3, with a literal fresh-hub component `sqrt(q)H` inside `U`, `q>=63/64`. Prove a universal density bound for
>
> `aU^2+gamma Y^2+dV^2`
>
> uniformly as `a->0` in the majority-sign branch, under
>
> `gamma d<0`, `|gamma d|>=63 sigma^2`, `|a gamma d|=D>=sigma^3`,
>
> while retaining the exact product characteristic-function factorization (3.9).

A proof based only on the joint cap (3.7), only on X-ray caps, or only on the positive discriminant denominator is insufficient by the live corrections and the r49/r41 barriers. The root numerator/product factorization has to participate before a worst-fiber or absolute-value step.

This is a genuine mechanism change from r46-r49: instead of another dependence-blind `L^p` closure, the entire punctured form has been put into a source-preserving LDL coordinate system whose three-volume and Schur budget are exact.

Arbitrary additional nonseparable spectrum beyond exact rank three remains a separate full-target bridge. Full-target continuity remains open.

## 7. Verification

A deterministic checker generated 20,000 random indefinite invertible `3x3` matrices, aligned the transverse basis so the `(1,3)` entry vanished, and checked:

- the full four-observable quadratic identity (3.2);
- `det Gram(u,y_bar,v)=1`;
- `a gamma d=det M`;
- the live-collar numerical implications `|gamma d|/sigma^2>=63` and the partner Schur budget.

The recorded maximum floating errors were below `3.1e-8`, with the algebraic factorization itself below `3.2e-11`. The checker ends

`QFORM_B11_R50_VOLUME_PRESERVING_LDL_CHECK_PASS`.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full continuous-density conclusion: **OPEN**.
