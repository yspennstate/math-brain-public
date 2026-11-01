SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B19, 2026-09-24T02:50:57Z.
attacking: the distinct-anchor weak-edge/large-E2 survivor — identify the exact bordered-Schur cancellation geometry, stress it inside the full target, and pay the pure-bilinear canonical model without losing product provenance.

# fleet02/B19 auto11b — exact bordered-Schur collapse and pure rank-two bilinear payment

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS / complementary constructions and source-valid counterexamples  
Status: **ESSENTIAL STRUCTURAL IDENTITY + TARGET-VALID OBSTRUCTION + PAID CANONICAL SUBBRANCH / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval is not authenticated native receiver use.  
Continuity: not claimed for the new direct bilinear theorem; unrestricted continuity remains open.

The exact target remains: arbitrary independent ORIGINAL real coordinates with one-dimensional densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moments, bounded support, log-concavity, iid hypothesis, spectral-coordinate independence, post-rotation independence, arbitrary-joint coarea premise, or coefficient-continuity argument is used.

## 1. Fresh source graph


The previous B19 result is

`yspennstate/math-open-problems@373f70551921d40dc74ac9ada67cfce1e491e432`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260924T021245Z-fleet02-B19-QFORM-r11/REPORT.md`.

For distinct physical anchors `p != q`, disjoint physical banks `R,C`,

`N=A[R,C]`, `u=A[R,p]`, `v=A[q,C]`, `b=A_qp`, `delta=||u||||v||`,

and the literal bordered physical cross block

`B=[[N,u],[v^T,b]]`,

that run proved, after the physical-E3 exit, the live dichotomy

`|b| sqrt(E2(N)) >= 2^-9`

or

`||P_u^perp N P_v^perp||_F < 9/512`,

with the stronger `<9/1024` at `b=0`. It explicitly left the first branch open because raw `E2(N)` need not survive pair completion.

The newest completed designated partner fleet03/B19 is r47:

`yspennstate/math-open-problems@1a64d8ce29d893fd99b9af8dac5a63e359a9cc08`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260924T020346Z-fleet03-B19-QFORM-r47/REPORT.md`,
brain handoff commit `d7a71d65d4c65b0fc15e485542bb25090bfbf9a1`.

Its large-leaf-curvature compiler pays a literal `E3` exit and otherwise forces an ultra-thin physical rank-two crossing. Quantitatively, one live branch has

`sigma_1(N) sigma_2(N) > gamma_0`,

where

`gamma_0 = 28159/(4194304 sqrt(2)) = 0.00474725242887306...`,

and another is giant near rank one. Its first synthesis debt is to pay these physical rank-two / giant-rank-one carriers while retaining arbitrary same-bank curvature and all nonzero tails.

The owner-pinned source was reread at exactly

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

The source-valid ingredient used below at equation level is its checked Livshyts--Paouris--Pivovarov projection bound: an orthogonal `k`-dimensional projection of a cap-one product measure has density at most `2^(k/2)` (the sharper finite-dimensional expression is also recorded there). Thus a unit one-dimensional product projection has density cap at most `sqrt(2)`, and an orthogonal two-dimensional product projection has joint density cap at most `2`. This is applied below to a literal physical-bank SVD; the two projected vectors are independent only because their source coordinate banks are disjoint.

The same owner-pinned source also supplies the physical `E3` and marginal-free `E5` receivers. The stress family below has `E3(B)=E5(B)=0` exactly, so it is a genuine obstruction to closing the live branch by simply strengthening those volume gates.

## 2. Exact identity behind the weak-edge/raw-E2 branch

Let `R,C` be finite physical index sets, `N` an `R x C` real matrix, `u in R^R`, `v in R^C`, and `b != 0`. Define

`B = [[N,u],[v^T,b]]`

and the rank-one-corrected block

`S = N - b^(-1) u v^T`.                                           (2.1)

Let `D_pq` denote the sum of squares of the `3 x 3` minors of `B` that use the appended row and appended column. Equivalently the remaining selected rows are any two rows of `R` and the remaining selected columns are any two columns of `C`.

### Theorem 2.1 — `QFORM-TWOSTAR-BORDERED-SCHUR-E2-IDENTITY-v1`

One has the exact identity

`boxed: D_pq = b^2 E2(S)`,                                        (2.2)

where

`E2(S)=e_2(S^T S)=sum_(|I|=|J|=2) det(S[I,J])^2`.

#### Proof

For each physical row pair `I subset R`, column pair `J subset C`, Schur's determinant formula for the scalar lower-right block gives

`det [[N[I,J],u_I],[v_J^T,b]]
 = b det(N[I,J]-b^(-1)u_I v_J^T)
 = b det S[I,J].`                                                  (2.3)

Square (2.3) and sum over all `I,J`. No random variable is transformed and no probabilistic assertion enters the proof. QED.

This is sharper than the preceding reverse-triangle estimate. In particular, since `D_pq <= E3(B)`, every unpaid bordered state with

`E3(B) < eta`                                                       (2.4)

satisfies

`boxed: |b| sqrt(E2(S)) < sqrt(eta).`                              (2.5)

At the live threshold `eta=2^-18`,

`boxed: |b| sqrt(E2(S)) < 2^-9.`                                  (2.6)

Therefore the r11 weak-edge/raw-E2 branch

`|b| sqrt(E2(N)) >= 2^-9`                                         (2.7)

is exactly a **rank-one-update E2-collapse chamber**: the raw physical two-volume is large at the `b` scale, while after the canonical one-sided rank-one correction (2.1) its weighted two-volume is below the same threshold.

The identity also explains why the old warning that raw E2 may collapse under pair completion was not merely a loose example. The collapse can be complete.

## 3. Target-valid exact-collapse family

Fix `0<epsilon<1` and an even integer `m`. Let `R,C` be disjoint physical banks of size `m`; let `p,q` be two further distinct physical coordinates. Choose flat orthonormal pairs

`u,a in R^R`, `v,c in R^C`,                                       (3.1)

for example

`u_i=v_j=m^(-1/2)`,

and `a,c` equal to the same flat sign pattern with half plus signs and half minus signs. Thus

`u perp a`, `v perp c`, and all four vectors have norm one.

Define

`N = epsilon^(-1) u v^T + a c^T`,                                 (3.2)

and the literal bordered cross block

`B = [[N,u],[v^T,epsilon]]`,                                      (3.3)

with row bank `I=R union {q}` and column bank `J=C union {p}`. Let the full symmetric physical matrix be

`A_epsilon,m = [[0,B],[B^T,0]]`                                   (3.4)

in the `I | J` decomposition. All unlisted coefficients are exactly zero.

### Theorem 3.1 — `QFORM-WEAKEDGE-RAW-E2-COMPLETE-COLLAPSE-v1`

This family has all of the following exact properties.

First, the r11 two-star currencies are macroscopic:

`delta=||u||||v||=1`,                                              (3.5)

`P_u^perp N P_v^perp = a c^T`, so

`F:=||P_u^perp N P_v^perp||_F=1`,                                 (3.6)

and the nonzero singular values of `N` are

`epsilon^(-1), 1`.

Hence

`E2(N)=epsilon^(-2)`,                                              (3.7)

and

`boxed: |b| sqrt(E2(N)) = 1.`                                     (3.8)

Thus the construction lies very deeply in the weak-edge/large-raw-E2 branch for every small `epsilon`.

Second, the corrected block (2.1) is

`S = N-epsilon^(-1)u v^T = a c^T`,                                (3.9)

which has rank one. Consequently

`boxed: E2(S)=0, D_pq=0.`                                         (3.10)

Moreover `B` itself has rank exactly two, so

`boxed: E3(B)=E5(B)=0.`                                           (3.11)

The preceding bordered tradeoff is saturated by exact cancellation:

`delta F = 1 = |b| sqrt(E2(N))`,                                  (3.12)

while its bordered-minor vector is zero.

Third, the family belongs to the exact QFORM target. Indeed write

`x_1=[u/epsilon;1]`, `x_2=[a;0]`,

`y_1=[v;epsilon]`, `y_2=[c;0]`.                                   (3.13)

Then

`B=x_1 y_1^T+x_2 y_2^T`.                                          (3.14)

The two `x` vectors are orthogonal and the two `y` vectors are orthogonal. Therefore the two nonzero singular values of `B` are exactly

`sigma_1(B)=||x_1||||y_1||=(1+epsilon^2)/epsilon
                                  =epsilon^(-1)+epsilon`,

`sigma_2(B)=1`.                                                    (3.15)

The nonzero eigenvalues of the symmetric bipartite matrix (3.4) are therefore

`boxed: { +(epsilon^(-1)+epsilon), +1, -1, -(epsilon^(-1)+epsilon) }.` (3.16)

So there are **four** actual eigenvalues of modulus at least one. No rank-three surrogate is being inserted.

### 3.1 Arbitrarily strict local no-pivot geometry

The family can simultaneously make every physical scalar, pair and triple local pivot arbitrarily small.

Every diagonal is zero. Its nonzero individual entries are bounded by

`epsilon`, `m^(-1/2)`, and `(epsilon^(-1)+1)/m`.                    (3.17)

Given any `tau>0`, choose

`0<epsilon<min(1,sqrt(tau)/2)`                                    (3.18)

and then choose even `m` with

`m>4/tau`,

`m>2(epsilon^(-1)+1)/sqrt(tau)`.                                  (3.19)

Then every physical coefficient has modulus `<sqrt(tau)/2`. Since the diagonal is zero, every physical `2 x 2` principal determinant is `-A_ij^2`, hence has magnitude `<tau/4<tau`.

Every physical `3 x 3` principal determinant is **exactly zero**: the full matrix is bipartite with zero same-side blocks, so every odd-order principal submatrix is bipartite with unequal part sizes and is singular.

Thus complete E2 collapse is compatible with the full spectral target and arbitrarily deep scalar/pair/triple no-pivot geometry. This refutes the structural implication

`weak edge + large raw E2 + full QFORM spectrum + strict local no-pivot`

`=> nontrivial post-correction E2 or nontrivial bordered E3`.       (3.20)

The target theorem itself is not refuted.

## 4. A direct product-safe payment for pure physical rank-two bilinear forms

The collapse family is not difficult probabilistically. The right primitive object is the entire physical rank-two bilinear packet, before arbitrary internal curvature is added.

### Theorem 4.1 — `QFORM-PURE-BILINEAR-R2-PROJECTION-PAYMENT-v1`

Let `I,J` be disjoint original-coordinate banks. Let `X_I,X_J` be the corresponding independent product vectors, each one-dimensional input density bounded by one. Let `M` be an `I x J` real matrix of rank two with singular values

`sigma_1>=sigma_2>0`.

For

`Q_0 = 2 X_I^T M X_J`,                                            (4.1)

the law has an essentially bounded density and

`boxed: ||p_(Q_0)||_infinity <= 2 sqrt(pi) (sigma_1 sigma_2)^(-1/2).` (4.2)

The same bound remains true after adding an independent random variable supported on coordinates disjoint from `I union J`, by convolution.

#### Proof

Take an SVD

`M=U diag(sigma_1,sigma_2) V^T`,                                  (4.3)

where `U,V` have orthonormal columns in their respective **physical bank coefficient spaces**. Define

`Y=U^T X_I`, `Z=V^T X_J`.                                         (4.4)

No random coordinate rotation is performed. `Y` and `Z` are independent vectors because `I` and `J` are disjoint original product banks.

The owner-pinned `e5f71...` source records the checked sharp product-projection theorem. Applied in dimension two,

`||rho_Y||_infinity <= 2`, `||rho_Z||_infinity <= 2`.              (4.5)

Applied in dimension one, every unit linear projection of `Z` has density cap at most `sqrt(2)`. Hence, conditional on `Y=y` and writing

`D=diag(sigma_1,sigma_2)`,

`Q_0=2(Dy) dot Z`,                                                 (4.6)

so for almost every `y !=0`,

`||p_(Q_0 | Y=y)||_infinity
 <= sqrt(2)/(2|Dy|)
 =1/(sqrt(2)|Dy|).`                                                (4.7)

Averaging conditional densities gives

`||p_(Q_0)||_infinity
 <=(1/sqrt(2)) int rho_Y(y)/|Dy| dy.`                              (4.8)

Put `d=det D=sigma_1 sigma_2` and change variables `z=Dy`. The transformed probability density

`q(z)=rho_Y(D^(-1)z)/d`

satisfies

`0<=q<=2/d`, `int q=1`.                                           (4.9)

Because `|z|^(-1)` is radially decreasing, the elementary bathtub/rearrangement bound puts the extremal cap-density on a centered disk. With

`M_0=2/d`,

`R=(pi M_0)^(-1/2)=sqrt(d/(2pi))`,                                (4.10)

we obtain

`int q(z)/|z| dz
 <= M_0 int_(|z|<=R) |z|^(-1) dz
 =(2/d) 2pi R
 =2 sqrt(2pi) d^(-1/2).`                                          (4.11)

Substituting (4.11) into (4.8) proves

`||p_(Q_0)||_infinity <=2 sqrt(pi) d^(-1/2)`. QED.                 (4.12)

This proof uses the e5f71 source's completed product-projection bounds at the exact equations (4.5)--(4.7). It does **not** replace `(Y,Z)` by an arbitrary joint four-dimensional density; it retains the only independence actually available, namely independence of the two original coordinate banks.

## 5. Paying the exact-collapse stress family

For the matrix `A_epsilon,m`, the full quadratic form is exactly the pure bilinear form

`Q=2 X_I^T B X_J`.                                                 (5.1)

By (3.15),

`sigma_1(B) sigma_2(B)=epsilon^(-1)+epsilon`.                      (5.2)

Theorem 4.1 therefore gives

`boxed:
 ||p_Q||_infinity
 <=2 sqrt(pi) sqrt(epsilon/(1+epsilon^2))
 <2 sqrt(pi epsilon).
}`                                                                  (5.3)

Thus the density bound actually **improves to zero at the scale of this estimate** as the edge `epsilon` tends to zero and the raw E2 packet tends to infinity. The exact cancellation is a failure of the bordered-volume proof currency, not a counterexample to bounded density.

A useful finite checkpoint is

`epsilon=1/64`, `m=2048`.

Then

`sigma(B)={64.015625,1}`,

`E2(N)=4096`, `epsilon sqrt(E2(N))=1`,

`E2(S)=E3(B)=E5(B)=0`,

maximum physical coefficient `<=65/2048=0.03173828125`,

maximum physical pair determinant `<=0.0010073185<1/256`,

and

`||p_Q||_infinity <=0.443059382`.                                 (5.4)

## 6. Equation-level application to the newest designated partner

Partner r47's strong multiplicative-rank-two branch has

`sigma_1(N)sigma_2(N)>gamma_0=0.00474725242887306...`.             (6.1)

Whenever that output state is in the **pure bilinear physical subchamber**, meaning after conditioning on coordinates disjoint from the two physical banks its remaining dependence on the live banks is exactly

`2 X_R^T N X_C`

(and any additional term is independent of those banks), Theorem 4.1 pays the complete ambient law by

`||p_Q||_infinity
 <2 sqrt(pi) gamma_0^(-1/2)
 =51.449809294... .`                                               (6.2)

Thus a nontrivial part of partner r47's ultra-thin physical rank-two frontier is now a finished density branch. The obstruction family in Section 3 shows simultaneously why **bordered E3** is not the missing mechanism for the rest of that frontier.

What remains is exactly the feature excluded from Theorem 4.1: arbitrary same-bank curvature, opposite anchor-to-leaf couplings, and other live terms using the same `R` or `C` variables. Those terms cannot be convolved away and cannot be replaced by an arbitrary bounded joint law.

## 7. Updated proof graph and first unpaid implication

The source-pinned full proof graph remains conditional but is sharper.

1. Principal physical triples, sufficiently large literal physical `E3`, and literal `E5` exits are paid by existing source-valid receivers.
2. One-anchor and two-star compilers reduce the unpaid geometry to ultra-thin physical rank two, giant near rank one, one-sided moving-ridge collars, or the distinct-anchor weak-edge/raw-E2 branch.
3. The exact identity (2.2) identifies the distinct-anchor branch as a rank-one-update E2-collapse problem; Section 3 proves that complete collapse `E2(S)=0` is compatible with four actual large eigenvalues and arbitrarily strict local no-pivot geometry.
4. The pure-bilinear part of the resulting rank-two frontier is paid by Theorem 4.1. In particular, partner r47's strong-rank-two output is paid by `<51.45` whenever no same-bank live curvature remains on the two crossing banks.
5. The e5f71 physical `E3`/`E5` volume receivers cannot by themselves close the exact-collapse family because those volumes vanish identically; the e5f71 product-projection theorem instead pays the whole pure rank-two packet directly.

The first compatible unpaid synthesis implication is therefore

`QFORM-R2-SCHUR-COLLAPSE-WITH-INTERNAL-CURVATURE-PAYMENT-v1`:

> In the full arbitrary rough-product target, after the scalar/pair, literal E3/E5, Fresnel/hub, ridge/window and existing grouped exits have failed, pay the physical rank-two / giant-rank-one chamber when the live rank-two crossing has the cancellation geometry
>
> `N = b^(-1) u v^T + S`,
>
> with `|b| sqrt(E2(N))` macroscopic but `|b| sqrt(E2(S))` small, **while retaining arbitrary quadratic curvature inside both physical banks and all opposite anchor-to-bank couplings**; or force an already-paid grouped/source-valid exit.

The pure-bilinear case `A_RR=A_CC=0` and no same-variable extra terms is now removed. Any next proof must spend the internal curvature jointly with the rank-two packet; a stronger bordered-minor lower bound, a guaranteed post-pair E2 lower bound, or a new E3/D5 gate is impossible in general because Section 3 has all of those quantities equal to zero at the exact target.

Arbitrary-extra-spectrum closure is still part of the global proof graph; unrestricted continuity remains open. No full theorem or counterexample to QFORM is claimed, and the required two independent end-to-end reviews do not exist.
