SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B01, 2026-09-24T09:18:04Z.
attacking: QFORM-DIAGRANK1-PLUS-ONEEDGE-STABILITY-v1; inherit two Schur singular directions and remove the weak-edge instability without treating the edge as a small random perturbation.

# account02/B01 — two-level half-Riesz compiler and diffuse-row certificate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T091804Z-account02-B01-qform-auto11`  
Role: oscillatory replacement / complementary constructions and source-valid obstructions  
Status: **ESSENTIAL STEP APPLIED / FULL QFORM OPEN**

## 1. Correction boundary

All variables below are ORIGINAL independent real coordinates with probability densities bounded by one. Affine terms are arbitrary. No moments, Gaussianity, log-concavity, compact/connected support, smoothness, iid assumption, diagonal-basis independence or post-rotation independence is used. Continuity is not claimed.

The phase-aligned-density obstruction remains in force: no law-uniform pointwise positive-power decay for `E exp(it X^2)` is used. The argument below instead uses a pinned small-ball estimate, a logarithmic square interface, physical-space rearrangement, and the newest partner's raw averaged-frequency row budget.

Control was refreshed from `yspennstate/math-research-brain@fa294f36e3e45d9ebe9601172e8eaa3045a5dcee`; OWNER CONTROL revision `2026-09-22.15` remained QFORM-only with no account02/B01 pause.

Required pinned source actually used:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

The two explicit pinned inputs are:

* arbitrary-rank small-ball: if a quadratic-plus-affine coefficient `T` has `||T||_op>=L`, then

`sup_s P(|Z-s|<r) <= min(1, 5 (r/L)^(1/4));`                 (1.1)

* logarithmic square interface: after a literal ORIGINAL scalar completion

`R=a(V+h)^2+Z`, `a!=0`,

`H_(1/2)(R) <= |a|^(-1/2)[8+2 sup_s E log_+(|a|/(4|s-Z|))].` (1.2)

The source's scalar Schur-persistence lemma is also used below.

Freshest designated partner consumed before publication:

`account03/B01` r48, canonical mathematics
`yspennstate/math-open-problems@f98e469792a51ca58a4387cffc0c68561a24621a`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/20260924T083540Z-account03-B01-qform-auto11-r48/`.

Its pivot-free row restriction is applied in Section 6.

## 2. A general two-level pivot-to-half-Riesz compiler

### Theorem 2.1 — `QFORM-TWOLEVEL-PIVOT-HALFRIESZ-v1`

Let `R` be a quadratic-plus-affine polynomial in independent cap-one ORIGINAL coordinates with real symmetric coefficient `S`. Assume

` s_2(S) >= rho > 0,`                                         (2.1)

and suppose some physical diagonal coefficient is `a=S_ii!=0`. Then

`H_(1/2)(R)
 <= 8 |a|^(-1/2)
    + 32 sqrt(5) 4^(-1/8) rho^(-1/8) |a|^(-3/8).`             (2.2)

In particular, if `rho=1` and `|a|>=1/64`,

`H_(1/2)(R) < 350.217.`                                        (2.3)

#### Proof

Complete the literal coordinate `X_i` exactly:

`R=a(X_i+h)^2+Z`.                                              (2.4)

Scale `S` by `rho`. The pinned Schur-persistence lemma says that the Schur coefficient of `Z` has at least one eigenvalue of modulus at least `rho`; hence its operator norm is at least `rho`.

Apply (1.1). For every center `s`, with `W=|Z-s|`,

`P(W<r) <= min(1,5(r/rho)^(1/4)).`                            (2.5)

Set `beta=1/8`. The layer-cake identity gives

`E W^(-beta)=beta int_0^infty r^(-beta-1) P(W<r) dr.`          (2.6)

The two terms in (2.5) meet at `r_0=rho/625`. Splitting (2.6) there gives exactly

`H_(1/8)(Z) <= 2 sqrt(5) rho^(-1/8).`                          (2.7)

Since `log_+ u <= 8 u^(1/8)`, (1.2) and (2.7) imply

`H_(1/2)(R)
 <= |a|^(-1/2)[8+32 sqrt(5)(|a|/(4rho))^(1/8)],`              (2.8)

which is (2.2). No coefficient tending to zero elsewhere is inverted. QED.

### Full-target corollary

Suppose a full target form first has a literal outer completion

`Q=a_0(X_0+h)^2+R`, `|a_0|>=1/64`.                             (2.9)

Pinned Schur persistence gives `s_2(S_R)>=1`. If the residual has any physical diagonal of modulus at least `1/64`, then the required square peel followed by (2.3) gives

`||p_Q||_infinity
 <= |a_0|^(-1/2) H_(1/2)(R)
 < 8*350.217
 < 2801.734.`                                                  (2.10)

Thus every finite-leak survivor with a second non-small literal diagonal is paid uniformly, independently of the weak edge parameter.

## 3. Exact zero diagonal: spend the whole physical row, not one edge

### Theorem 3.1 — `QFORM-ZERODIAG-ROW-HALFRIESZ-v1`

Let `R` be any quadratic-plus-affine form in independent cap-one ORIGINAL coordinates. If for some physical coordinate `i`

`S_ii=0`,

and its off-diagonal row has Euclidean norm

`c_i=(sum_{j!=i} S_ij^2)^(1/2)>0`,                             (3.1)

then, with completely arbitrary quadratic curvature among the remaining coordinates,

`boxed: H_(1/2)(R) <= 2^(11/4) c_i^(-1/2).`                   (3.2)

#### Proof

Write, after absorbing affine coefficients,

`R-s = 2 X_i L(X_-i) + T(X_-i)-s`,                             (3.3)

where `L=sum_{j!=i} S_ij X_j + const`. Condition on `X_-i`. A cap-one scalar density and the bathtub/rearrangement bound for `|u|^(-1/2)` give, for every real `b`,

`E_{X_i}|2 L X_i+b|^(-1/2) <= 2 |L|^(-1/2).`                  (3.4)

The linear form `L` has density at most `sqrt(2)/c_i` by the Rogozin--Ball scalar projection bound. Applying the same bathtub bound to `L` yields

`E |L|^(-1/2) <= 2^(7/4) c_i^(-1/2).`                         (3.5)

Combining (3.4)-(3.5) proves (3.2). Notice that `T` disappears only as a translation in (3.4); no assumption on the leaf block is made. QED.

This strictly strengthens the earlier literal single-edge zero-diagonal estimate in the diffuse-row regime.

## 4. A spectral lemma for the diagonal-plus-rank-one weak-edge normal form

The remaining finite-leak normal form from the preceding B01 run is

`S = D + alpha q q^T + eta(e_j e_k^T+e_k e_j^T),`              (4.1)

with inherited `s_2(S)>=1`. The previous theorem paid the complementary rank-one two-hub arrowhead uniformly; (4.1) was the first unpaid implication.

Absorb the rank-one scale by writing `alpha q q^T = sigma r r^T`, `sigma in {+1,-1}`. Define the zero-diagonal weighted-complete-graph matrix

`O = sigma( r r^T - diag(r_1^2,...,r_n^2) ).`                  (4.2)

### Lemma 4.1 — second singular value is controlled by one row energy

Let `R2=sum_i r_i^2` and

`C=max_i |r_i| sqrt(R2-r_i^2).`                                (4.3)

Then

`boxed: s_2(O) <= C.`                                          (4.4)

#### Proof

The sign `sigma` does not affect singular values, so take `sigma=+1`. Put `x_i=r_i^2`, `R=sum x_i`. Since

`O = r r^T - diag(x_i)`,                                      (4.5)

it is a rank-one positive perturbation of a negative semidefinite diagonal matrix and therefore has at most one positive eigenvalue.

If `M=max_i x_i <= C`, Loewner monotonicity gives every negative eigenvalue at least `-M`, so all negative eigenvalues have modulus at most `C`; at most the single positive eigenvalue can exceed `C`, proving (4.4).

Now suppose `M>C`, attained at coordinate `h`, and put `T=R-M`. Since the `h`-row norm is `sqrt(MT)`, definition (4.3) gives `C^2>=MT`; hence

`T <= C^2/M < C`.                                               (4.6)

Write the tail vector as `r_T`, `D_T=diag(x_l:l!=h)`, and partition

`O = [[0, u^T],[u,B]],
 u=sqrt(M) r_T,
 B=r_T r_T^T-D_T.`                                             (4.7)

Because every tail `x_l<=T<C`, `B+C I = C I-D_T+r_T r_T^T` is positive definite. Let

`h_0=sum_{l!=h} x_l/(C-x_l).`                                  (4.8)

Sherman--Morrison gives

`r_T^T(B+C I)^(-1)r_T = h_0/(1+h_0).`                          (4.9)

Moreover

`h_0 <= T/(C-T) <= C/(M-C),`                                  (4.10)

where the last step is exactly `MT<=C^2`. Therefore

`u^T(B+C I)^(-1)u
 = M h_0/(1+h_0) <= C.`                                     (4.11)

The Schur complement of `B+C I` in `O+C I` is nonnegative, so `O+C I` is positive semidefinite. Hence every negative eigenvalue of `O` has modulus at most `C`; again only its single positive eigenvalue may exceed `C`. Thus `s_2(O)<=C`. Equality cases follow by continuity. QED.

A random deterministic check over 10,000 positive weight vectors for each dimension `2<=n<=14` found `max s_2(O)/C = 1+2e-16` (machine precision), consistent with the exact proof.

## 5. Weak-edge low-diagonal compiler and row certificate

Fix the stability collar

`|eta| <= 1/4`,
`max_i |S_ii| <= 1/64`.                                       (5.1)

Since the weak edge has zero diagonal,

`S = diag(S_ii) + O + eta E_jk`,                               (5.2)

where `||E_jk||_op=1`. Weyl and `s_2(S)>=1` give

`s_2(O) >= 1 - 1/64 - 1/4 = 47/64.`                           (5.3)

Lemma 4.1 therefore supplies a physical row `i` of `O` with off-diagonal norm at least `47/64`. The actual off-diagonal row of `S` differs in at most the special edge, so by the triangle inequality its norm `r_i(S)` obeys

`boxed: r_i(S) >= 47/64 - 1/4 = 31/64.`                       (5.4)

This is the promised product-preserving row-energy certificate.

### Concentrated row: a physical pair pays

If some edge on that row satisfies `|S_il|>=1/8`, then the literal two-coordinate block

`B_il=[[S_ii,S_il],[S_il,S_ll]]`                               (5.5)

has

`|det B_il| >= 1/64 - 1/4096 = 63/4096.`                      (5.6)

Condition every other ORIGINAL coordinate. The previously proved orientation-free exact-rank-two affine half-Riesz theorem gives

`H_(1/2)(R)
 <=128(63/4096)^(-1/4)
 <363.467.`                                                     (5.7)

Thus the concentrated low-diagonal row is paid uniformly in `eta`.

### Diffuse row: exact-zero endpoint is paid

If every edge on the certified row is `<1/8`, then (5.4) forces at least 16 nonzero row entries. If in addition its physical diagonal is exactly zero, Theorem 3.1 gives

`H_(1/2)(R)
 <=2^(11/4)(31/64)^(-1/2)
 <9.666.`                                                       (5.8)

In particular the entire all-zero-diagonal endpoint of the weak-edge collar is paid. The remaining gap is now genuinely punctured: the certified diffuse row has `0<|S_ii|<1/64`, not an exact zero.

## 6. Newest partner applied to the surviving diffuse row

The newest compatible designated-partner theorem is account03/B01 r48, `QFORM-DECOUPLED-AMBIGUITY-L2-THRESHOLD-v1` together with its pivot-free row addendum. For

`r_i=(sum_{l!=i}S_il^2)^(1/2)`

it proves the raw cubic row budget

`R_i(T)
 <= min{2T,
         (2 pi sqrt(2)/r_i)
         [1+log_+(T r_i/(pi sqrt(2)))]}.`                      (6.1)

Insert the actual certified inequality `r_i>=31/64` from (5.4). The right side is nonincreasing in `r_i` for fixed `T`, hence

`boxed:
R_i(T)
 <= min{2T,
         18.344807 [1+log_+(T/9.172404)]}.`                    (6.2)

This is a concrete averaged-frequency estimate on the exact remaining survivor, not a summary of the partner result.

The same r48 result also proves why a generic absolute ambiguity-cell closure cannot finish (6.2): the decoupled graph has dimension `n+1`, every cell is 2D, and every law-uniform unweighted cell exponent satisfies `q_i>=2`, so

`sum_i 2/q_i <= n < n+1.`                                     (6.3)

Its explicit fragmented-density construction proves no universal `q<2` repair exists. Therefore the next step must recover the one missing graph dimension through signed aggregation or another physical-space receiver; taking absolute values cell-by-cell is source-validly blocked.

## 7. Strict full-target stress family

For every `m>=1`, on ORIGINAL coordinates `(X_0,H,Y_1,...,Y_m)` let

`Q_m = X_0^2 + 2 H m^(-1/2) sum_{j=1}^m Y_j.`                 (7.1)

The coefficient is `[1]` direct-summed with a star whose slope vector has Euclidean norm one. Its spectrum is exactly

`{1,1,-1,0,...,0}`,                                            (7.2)

so it meets the owner target with three eigenvalues of modulus one.

The residual star has a zero hub diagonal and row energy `c_H=1`; Theorem 3.1 and the **required pinned square peel** at the outer coefficient one give

`boxed: ||p_{Q_m}||_infinity <= 2^(11/4)
       =6.727171322...`                                        (7.3)

uniformly in `m` and in all admissible input laws.

This family shows why spending aggregate row energy matters. A single-edge estimate sees only `m^(-1/2)` and deteriorates like `m^(1/4)`, while (7.3) is constant. Every disjoint physical cross block of the star has rank at most one, hence the required pinned D/D'/D5 currencies satisfy

`e_3=e_5=0`                                                     (7.4)

on every cut. Thus the row-rearrangement route contributes genuinely outside those volume receivers (although the pure star is also visible to the pinned hub theorem).

## 8. What is now paid and the first unpaid implication

For the complementary finite-leak normal form (4.1) with inherited `s_2>=1`:

* any residual physical diagonal `>=1/64` is paid by Theorem 2.1, uniformly in `eta`;
* in the weak-edge collar `|eta|<=1/4` with all residual diagonals `<=1/64`, a certified row has total off-diagonal energy at least `31/64`;
* if that row contains an edge `>=1/8`, the physical pair pays it;
* if its diagonal is exactly zero, the aggregate row half-Riesz theorem pays it, including arbitrarily diffuse rows;
* if the row is diffuse, the newest partner supplies the explicit signed/raw cubic budget (6.2).

The first unpaid implication is therefore

`QFORM-PUNCTURED-DIFFUSE-ROW-SIGNED-RECOVERY-v1`:

in the diagonal-plus-rank-one plus weak-edge normal form, convert (6.2) into a half-Riesz/direct-density estimate when a certified diffuse row has

`0<|S_ii|<1/64`, `r_i>=31/64`, and every `|S_il|<1/8`,

uniformly as `S_ii -> 0`, without treating the tiny diagonal as a small random perturbation and without normalizing ambiguity fibers. The partner's sharp L2 threshold says the missing one-dimensional gain must be signed or geometric.

Full QFORM remains OPEN. No counterexample to the conjecture was found.
