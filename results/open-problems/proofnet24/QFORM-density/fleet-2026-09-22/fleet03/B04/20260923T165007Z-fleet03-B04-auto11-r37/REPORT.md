SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-23T16:50:07Z.
attacking: entropy-reweight the new arbitrary-rank projected-crossing Fourier lemma so concentrated canonical compound marginals can be diluted without rotating the product law.

# fleet03/B04 r37 — arbitrary-weight projected-crossing Fourier rearrangement

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: `NEW SUPPORTING THEOREM / EXPLICIT ROTATED INDEFINITE ESTIMATE / FULL TARGET OPEN`  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is not proved here. The result below gives a continuous `C_0` density in its stated grouped-hub/projected-crossing scope. It preserves independent original coordinates and does not use law-uniform pointwise quadratic-phase decay.

## 1. Source boundary and corrections


The immediate analytic source is

`yspennstate/math-open-problems@f6f7e407aea4977e9b061d90eefd8e692d3191ed:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`

(blob `dc7e29c3ee746ebf2856aaa6866b4b16b9a04b9f`). Its weighted-subset Fourier lemma (WS) and grouped-hub theorem (GC) are complete written supporting arguments at their stated scope. The source uses canonical squared-minor weights. This run keeps the exact weighted geometric mean instead of imposing the canonical law.

Consumed corrections: no law-uniform pointwise Fresnel/van-der-Corput decay; no independence after an arbitrary rotation; no arbitrary-joint coarea density cap; no positive conditional projection-density moment shortcut; no naive fiber-supremum bound. None is used below.

## 2. Exact arbitrary-weight projected-crossing lemma

Let `D=(D_j)` have independent scalar coordinates with densities bounded by one. Let `M` be a `k x m` full-row-rank matrix, with singular-value product

`S_M = product_(a=1)^k s_a(M)>0`.

Let `A` have physical rows `a_i`, let `Pi` be orthogonal projection in `R^m` onto `row(M)`, and put

`c_i=a_i(I-Pi)`, `C` = the matrix with rows `c_i`.

Fix an integer `ell>=1`. Let `w=(w_S)` be ANY probability distribution on `ell`-subsets of the physical row indices such that

`D_S := det(C_S C_S^T)>0`

whenever `w_S>0`. Define inclusion marginals

`alpha_i = sum_(S containing i) w_S`.

Assume

`alpha_i<=1/2` for every i.

Rows with `alpha_i=0` may be dropped from the product estimate because every characteristic-function factor has modulus at most one; unlike the canonical case, no claim that `c_i=0` is needed.

Define the exact determinant/marginal currency

`Gamma(w;C)
 := exp( sum_S w_S log D_S - sum_i alpha_i log alpha_i ),`       (2.1)

with `0 log 0=0`.

### Theorem `QFORM-ARBITRARY-WEIGHT-PROJECTED-CROSSING-v1`

If `kappa` is any nonnegative probability density on `R^k` and `psi_i` are characteristic functions of independent scalar laws with densities bounded by one, then for every `t!=0`,

`E[ kappa(MD) product_i |psi_i(2t<a_i,D>)| ]
 <= 2^((k+ell)/2) (2pi)^ell
    / [ S_M sqrt(Gamma(w;C)) |t|^ell ].`                       (2.2)

The product on the left can include rows with `alpha_i=0`; discarding those factors only enlarges it.

### Proof

Set `mu(dD)=kappa(MD)dP_D(D)`, a finite positive measure. For every active row (`alpha_i>0`), weighted Holder over the finite subset law `w` gives

`int product_i |psi_i(2t<a_i,D>)| dmu
 <= product_S I_S^(w_S),`                                     (2.3)

where

`I_S = E[kappa(MD) product_(i in S)
                  |psi_i(2t<a_i,D>)|^(1/alpha_i)].`           (2.4)

Indeed, the exponent of the i-th characteristic-function factor in the weighted product is

`sum_(S containing i) w_S/alpha_i=1`.

For a fixed supported `S`, write `a_i=c_i+lambda_i M`. The linear map

`D -> (MD,(<c_i,D>)_(i in S))`

has Gram determinant

`S_M^2 D_S`,

because every `c_i` is perpendicular to `row(M)`. Factoring this map into an orthogonal `(k+ell)`-dimensional projection and an invertible map, and using the cap-one product projection bound, its joint density is at most

`2^((k+ell)/2)/(S_M sqrt(D_S)).`                               (2.5)

Translate the last `ell` variables by the deterministic shifts `lambda_i MD`. Since `alpha_i<=1/2`, the exponents `1/alpha_i` are at least two, so the sharp scalar Hausdorff-Young estimate used in the source WS proof gives

`I_S <= [2^((k+ell)/2)(2pi)^ell]/[S_M |t|^ell]
          * product_(i in S) sqrt(alpha_i) / sqrt(D_S).`       (2.6)

Take the weighted geometric mean. The common first factor survives, while the remaining logarithm is

`(1/2) sum_i alpha_i log alpha_i
 -(1/2) sum_S w_S log D_S
 = -(1/2) log Gamma(w;C).`                                    (2.7)

This is exactly (2.2). QED.

### Relation to the canonical source theorem

For the canonical law `w_S=D_S/Z_ell`, `Z_ell=sum_S D_S`,

`sum_S w_S log D_S = log Z_ell - H(w)`.

Hence

`Gamma=Z_ell exp[-H(w)-sum_i alpha_i log alpha_i].`            (2.8)

Entropy subadditivity and `-(1-a)log(1-a)<=a` give

`Gamma>=Z_ell e^(-ell)`,                                      (2.9)

which recovers the source factor `e^(ell/2)/sqrt(Z_ell)` in (WS). Thus (2.2) is the exact-weight refinement of that argument; more importantly, it permits a noncanonical `w` when the canonical row marginals exceed `1/2`.

## 3. Grouped-hub consequence

Use the source grouped-hub notation

`Q=F(X_H)+2<W,MX'+beta>+R(X')`,

where `W=U^T X_H` has density bounded by `M_H`, `M_J` has rank `k` and singular-value product `S`, and

`C=(A_R)_(I,J)(I-Pi_row(M_J)).`

Let `w` be any feasible `ell`-minor law for this `C` as in Section 2 and put `d=k+ell>2`. Replacing source (WS) by (2.2) in its unchanged Plancherel/approximate-identity proof gives

`|phi_Q(t)| <= min(1,K |t|^(-d/2)),`                           (3.1)

where

`K=M_H^(1/2) 2^((k+3ell)/4) pi^(d/2)
      S^(-1/2) Gamma(w;C)^(-1/4).`                             (3.2)

Exact integration of the minimum and Fourier inversion give

`boxed:
 ||p_Q||_infinity
 <= [d/(d-2)] 2^((k+3ell)/(2d))
    M_H^(1/d) S^(-1/d) Gamma(w;C)^(-1/(2d)).`                  (3.3)

Moreover `phi_Q in L^1(R)`, so the density has a continuous representative in `C_0(R)`.

For one physical hub (`k=1`) and `ell=2`, if `C` has two DISJOINT physical row pairs `S,T` with

`D_S=det(C_S C_S^T)>0`, `D_T>0`,

choose `w_S=w_T=1/2`. The four active row marginals are exactly `1/2`, and

`Gamma=4 sqrt(D_S D_T).`                                      (3.4)

Thus

`boxed:
 ||p_Q||_infinity
 <= 3*2^(5/6) M_H^(1/3) S^(-1/3)
       (D_S D_T)^(-1/12).`                                    (3.5)

This pays an aggregate pair-of-pairs crossing certificate without requiring the canonical second-volume marginal law to be diffuse.

## 4. Genuinely rotated indefinite family where canonical crossing weights fail

Fix `L>0` and `0<epsilon<=1`. Take one original hub coordinate, five left light coordinates, and four right light coordinates. Let the hub-to-right coefficient row be

`m=(1,0,0,0)`.

Let the left-to-right crossing block be

`C_(L,epsilon)=
 [ 0  L  0  0
   0  0  1  0
   0  1  1  0
   0  1 -1  0
   0  0  0  epsilon ].`                                      (4.1)

Because every row in (4.1) is perpendicular to `m`, it is already the projected crossing matrix in (3.3). Put

`B_(L,epsilon)= [m; C_(L,epsilon)]`                            (4.2)

and define the symmetric `10 x 10` matrix

`A_(L,epsilon)= [[0_6,B],[B^T,0_4]].`                          (4.3)

This is non-diagonal in the independent physical coordinates and indefinite. Directly,

`B^T B = diag(1,L^2+2,3,epsilon^2)`,                          (4.4)

so

`spec_nonzero(A_(L,epsilon))
 = {+-1,+-sqrt(L^2+2),+-sqrt(3),+-epsilon}.`                  (4.5)

Therefore, for every `L>0` and `0<epsilon<1`, the matrix has SIX eigenvalues of modulus at least one, uniformly as the extra fourth cross singular direction `epsilon` tends to zero.

The positive squared two-row volumes of `C` are

`D_12=D_13=D_14=L^2`,
`D_15=L^2 epsilon^2`,
`D_23=D_24=1`,
`D_25=epsilon^2`,
`D_34=4`,
`D_35=D_45=2 epsilon^2`.                                     (4.6)

Hence the canonical second-volume currency is

`Z_2=L^2(3+epsilon^2)+6+5epsilon^2`,                          (4.7)

and its first-row inclusion marginal is

`alpha_1^can
 = L^2(3+epsilon^2)/Z_2`.                                  (4.8)

For large `L` this is arbitrarily close to one, so the canonical-marginal hypothesis `alpha_i<=1/2` in the source (WS)/(GC) theorem fails badly.

Now ignore, only in the modulus upper bound, the unused characteristic-function factors and choose the noncanonical physical pair law

`w_{12}=w_{34}=1/2`.                                          (4.9)

The pairs are disjoint. All four active row marginals equal `1/2`, and

`Gamma=4 sqrt(L^2*4)=8L`.                                     (4.10)

Here the hub is one original cap-one coordinate, so `M_H<=1`; `S=||m||=1`; `k=1`, `ell=2`, `d=3`. Equation (3.3) yields

`boxed:
 ||p_(X^T A_(L,epsilon) X)||_infinity
 <= 3*2^(2/3) L^(-1/6),`                                     (4.11)

uniformly for every `0<epsilon<=1` and every admissible independent product input law. The density is continuous and vanishes at infinity.

At the explicit values

`L=64`, `epsilon=1/64`,                                       (4.12)

we have

`spec_nonzero(A)=
 {+-sqrt(4098), +-sqrt(3), +-1, +-1/64}`,                     (4.13)

so exactly six nonzero eigenvalues in the displayed list have modulus at least one, while the fourth cross singular direction is tiny. The canonical row-one second-volume marginal is

`alpha_1^can=12289/(50360325/4096)
             =0.9995118975105899... >1/2`,                    (4.14)

but the reweighted estimate gives

`boxed:
 ||p_Q||_infinity
 <= (3/2) 2^(2/3)
 =2.381101577952299... .`                                     (4.15)

This is a concrete rotated indefinite estimate with explicit constant. It also shows a useful stability feature: the new certificate does not pay a reciprocal power of the unused tiny singular direction `epsilon`.

## 5. Completed peer result applied at an actual inequality

The designated partner is `fleet04/B04`. Fresh direct repository lookups found its current-QFORM canonical report path and shared handoff path absent, consistent with the latest owner continuation's explicit reconciliation note. I therefore do not fabricate a designated-partner theorem.

I did apply the completed fleet03/B16 physical-bank projection calculation from

`yspennstate/math-open-problems@e073f14465e781bf78996438d9c267750d90728c:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260923T162348Z-fleet03-B16-QFORM-r30/REPORT.md`.

That report's equation (4.2) states for a two-dimensional coefficient bank with Gram matrix `G_B` that the physical product projection density obeys

`||p_Z||_infinity <=2/sqrt(det G_B)`.

Apply it to the two disjoint active row pairs in (4.9), viewed in the projected two-dimensional coordinates `(right_2,right_3)`. Their Gram matrices are

`G_12=diag(L^2,1)`, `G_34=2 I_2`.

Hence, at the actual inequality,

`boxed: ||p_(Z_12)||_infinity <=2/L,`
`boxed: ||p_(Z_34)||_infinity <=1.`                            (5.1)

At `L=64`, the first cap is `1/32`. Since the two row pairs use disjoint original variables, these two projected banks are genuinely independent. This peer calculation is not needed to justify (4.15), but it independently certifies the product-space quality of exactly the two physical pair packets used by the new Fourier weighting.

## 6. Scope and remaining implication

The theorem proved here does NOT show that the bare hypothesis `s_3(A)>=1` forces a grouped-hub split with `S` and `Gamma` bounded below. It is therefore not a proof of the full QFORM conjecture.

What it removes is a narrower obstruction: in the newest arbitrary-rank projected-crossing theorem, a concentrated CANONICAL compound-volume law is not by itself a reason to abandon the Fourier branch. One may reweight physical minors and pay the exact currency `Gamma(w;C)`. Failure of the optimized certificate must therefore mean that every feasible marginal-balanced minor law has small determinant/marginal currency, a stronger structural obstruction than failure of the canonical marginal test.

The next B04 target is

`QFORM-OPTIMIZED-PROJECTED-CROSSING-DUAL-OR-HUB-v1`:

derive a convex/Gibbs dual for

`Gamma_(ell,1/2)(C)=sup{Gamma(w;C): w probability on positive ell-minors, alpha_i(w)<=1/2}`,

and prove that small optimized currency forces a bounded physical hitting set / compound hub that can be routed into an already-paid pair, star, ridge, or grouped-bank endpoint.

Full QFORM remains OPEN. Full-target continuity remains OPEN separately.
