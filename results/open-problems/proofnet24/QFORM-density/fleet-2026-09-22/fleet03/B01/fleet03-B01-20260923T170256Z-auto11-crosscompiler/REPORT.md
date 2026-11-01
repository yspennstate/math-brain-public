SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B01, 2026-09-23T17:02:56Z.
attacking: near-null leakage after scalar completion; combine the new arbitrary-rank projected-crossing theorem with an outer-square half-Riesz compiler to obtain a genuine bounded-density exit.

# fleet03/B01 — projected-crossing residual + correlated outer square

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `fleet03-B01-20260923T170256Z-auto11-crosscompiler`  
Assignment: oscillatory replacement / FOURIER  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING BOUNDED-DENSITY BRANCH; FULL QFORM OPEN; FULL CONTINUITY NOT PROVED HERE**.

The full target remains open. Throughout, all random coordinates are the original independent coordinates and have probability densities bounded by one. No moment, support, log-concavity, Gaussian, or post-rotation independence hypothesis is introduced.

The phase-aligned obstruction is preserved: at any prescribed frequency `s`, a cap-one density can be supported on finitely many components of `{x: dist(s x^2,2 pi Z)<=eta}` of total length one, forcing `Re E exp(i s X^2)>=cos eta`. Thus no law-uniform positive-power pointwise quadratic-phase decay is used below.

## 1. Sources actually used

### 1.1 fleet04/B01 near-singular star identity

The designated partner source is

`yspennstate/math-open-problems@8410ab9d8238baa40c033f83dbae6af44b0b2582`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260923T131003Z-fleet04-B01-singular-star-routing-r2/REPORT.md`.

For a physical pair `S={i,j}` with

`B=[[a,b],[b,c]]`, `a!=0`,

scalar-complete coordinate `i` and write, on `K=S^c`,

`delta=c-b^2/a`,
`ell_k=A_jk-(b/a)A_ik`,
`M_kl=A_kl-a^(-1)A_ik A_il`.

The partner proves

`W2(S)=a^2 sum_(k!=l)(delta M_kl-ell_k ell_l)^2`                 (1.1)

and therefore the leakage/curvature dichotomy. The branch used here is

`L(ell):=sum_(k!=l)ell_k^2 ell_l^2 >= W2(S)/(4a^2)`.             (1.2)

The random two-coloring computation in that report gives

`E[||ell_I||_2^2 ||ell_J||_2^2]=L(ell)/4`.                       (1.3)

A correction to the printed Corollary 4.1 is recorded in Section 5 below: (1.3) implies a PRODUCT lower bound, not the same lower bound on each factor separately.

### 1.2 newest projected-crossing theorem

The fresh interactive source is

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its one-original-hub, `ell=2` consequence is the following. Let

`R(Y,Z)=F(Y)+2Y(ell dot Z+beta)+Z^T M Z+q dot Z+r`,               (1.4)

where `Y` is one original coordinate and `Z` is its independent original-coordinate complement. Split `Z=(Z_I,Z_J)`. Assume `ell_J!=0`; set

`S_J=||ell_J||_2`,
`Pi_J=orthogonal projection in R^J onto span(ell_J)`,
`C=M[I,J](I-Pi_J)`,
`Z2=e_2(CC^T)>0`.                                                 (1.5)

For the 2-volume weights

`w_T=det(C_T C_T^T)/Z2`, `|T|=2`,
`alpha_r=sum_(T contains r)w_T`,                                  (1.6)

assume every `alpha_r<=1/2`. The theorem applies with hub rank `k=1`, `rank(M_J)=1`, singular product exactly `S_J`, and gives a continuous `C_0` density for `R` with

`||p_R||_infinity <= C_GC (S_J^2 Z2)^(-1/6)`,                    (1.7)

where

`C_GC=3*2^(7/6)*exp(1/3)=9.39913188784886...`.                    (1.8)

This is an actual application of every gate of the new result: the hub-light block on `J` has rank one, its singular product is `S_J`, the projected crossing is exactly (1.5), and the row-marginal hypothesis is (1.6). Arbitrary same-bank curvature and affine terms remain in (1.4).

## 2. New compiler: a correlated translated square over a bounded remainder

### Lemma 2.1 — `QFORM-OUTER-SQUARE-OVER-BOUNDED-REMAINDER-v1`

Let `X` be a real random variable with density at most one and independent of a random element `V`. Let `h(V)` and `R(V)` be arbitrary measurable real functions, with no independence assumed between `h(V)` and `R(V)`. Suppose the marginal law of `R` has a density bounded by `M<infinity`. For `a!=0`, define

`Q=a(X+h(V))^2+R(V)`.                                             (2.1)

Then `Q` has a density and

`boxed: ||p_Q||_infinity <= 2 sqrt(2) |a|^(-1/2) M^(1/2).`        (2.2)

Consequently every signed Fejer average obeys the same bound.

#### Proof

Conditional on `V=v`, the variable `a(X+h(v))^2` has a density `g_v` satisfying, for almost every `u`,

`g_v(u)<=|a|^(-1/2)|u|^(-1/2) 1_(a u>0)`.                        (2.3)

This is the exact two-preimage change-of-variables bound; the translation `h(v)` does not change it. Fubini therefore constructs a density for (2.1) and gives

`p_Q(y)<=|a|^(-1/2) E |R-y|^(-1/2)`.                             (2.4)

Since `p_R<=M`, for every `rho>0`,

`P(|R-y|<rho)<=min(1,2M rho)`.                                   (2.5)

Layer cake now gives the sharp cap-only half-Riesz estimate

`E|R-y|^(-1/2)`
` = int_0^infinity P(|R-y|<t^(-2)) dt`
` <= int_0^infinity min(1,2M t^(-2)) dt`
` =2 sqrt(2M)`.                                                   (2.6)

Substitute (2.6) into (2.4). QED.

This lemma is deliberately dependence-safe: `h(V)` can be a function of the same variables producing `R(V)`. It therefore applies to exact scalar completion, unlike an independent-convolution shortcut.

Continuity is not asserted in this generality. The proof gives an essentially bounded density. The residual `R` in (1.7) is continuous, but the correlated translation `h(V)` need not provide a convolution representation for the full `Q`.

## 3. Main theorem: projected-crossing payment of the near-null leakage residual

Scalar completion of coordinate `i` writes the original quadratic form exactly as

`Q=a(X_i+h(Y,Z))^2+R(Y,Z)`,                                      (3.1)

where `Y=X_j`, `Z=X_K` remain original independent coordinates and `R` has the form (1.4) with the Schur data `(delta,ell,M)` from Section 1. No random variable is rotated.

### Theorem 3.1 — `QFORM-NEARNULL-PROJECTED-CROSSING-COMPILER-v1`

Assume there is an original-coordinate split `K=I disjoint_union J` for which the gates (1.5)-(1.6) hold. Then

`boxed:`
`||p_Q||_infinity`
` <= C_* |a|^(-1/2) (||ell_J||_2^2 Z2)^(-1/12),                  (3.2)

where

`C_*=2 sqrt(2 C_GC)=8.67139291595018...`.                         (3.3)

The identical constant bounds

`sup_(T>0,y) D_T law(Q)(y)`.                                     (3.4)

#### Proof

Apply the new projected-crossing theorem to the scalar-completed residual `R`. Equation (1.7) gives the marginal density cap

`M_R=C_GC(||ell_J||_2^2 Z2)^(-1/6)`.                             (3.5)

Now apply Lemma 2.1 to the exact outer square (3.1). This yields

`||p_Q||_infinity`
` <=2sqrt(2)|a|^(-1/2) M_R^(1/2)`,                               (3.6)

which is (3.2). The fleet04/B01 signed-Fejer identity then gives (3.4). QED.

This is a genuine bounded-density exit for a near-null physical pair; it is not merely the logarithmic `q log(1/q)` interval estimate from the preceding B01 run.

## 4. Feed the fleet04/B01 leakage currency into the new theorem

From (1.2)-(1.3), some two-coloring satisfies

`||ell_I||_2 ||ell_J||_2 >= sqrt(W2(S))/(4|a|)`.                  (4.1)

Orient that partition so that `||ell_J||_2>=||ell_I||_2`. Then

`||ell_J||_2 >= W2(S)^(1/4)/(2 |a|^(1/2)).`                       (4.2)

If the projected-crossing gates (1.5)-(1.6) hold for this orientation, Theorem 3.1 gives

`boxed:`
`||p_Q||_infinity`
` <= C_leak |a|^(-5/12) W2(S)^(-1/24) Z2^(-1/12),                (4.3)

with

`C_leak=2 sqrt(2 C_GC) 2^(1/6)=9.73330945413282...`.              (4.4)

At the exact-null endpoint `det B=0`, the partner identity strengthens (1.2) to

`L(ell)=W2(S)/a^2`.

The same random partition then yields

`||ell_I|| ||ell_J|| >= sqrt(W2)/(2|a|)`,                         (4.5)

so the larger bank satisfies `||ell_J||>=W2^(1/4)/(sqrt(2)|a|^(1/2))`. Hence

`boxed:`
`||p_Q||_infinity`
` <= 9.18702077113785 |a|^(-5/12) W2(S)^(-1/24) Z2^(-1/12).      (4.6)

The homogeneity is correct: under `A -> lambda A`, `a`, `M`, and `ell` scale by `lambda`, `W2` scales by `lambda^6`, `Z2` by `lambda^4`, and (4.3) scales by `|lambda|^(-1)`.

The unpaid point is now explicit. The partner leakage theorem does not force the projected-crossing volume `Z2` or its row-marginal spread. If `Z2` is tiny/zero or its volume is concentrated on a heavy row, another receiver is still required. The present theorem closes the complementary spread-crossing branch without paying any reciprocal power of `det B`.

## 5. Source correction: the partner's printed individual-bank bound is too strong

The proof of fleet04/B01 Corollary 4.1 establishes (4.1). The displayed conclusion there states that both

`||ell_I||_2, ||ell_J||_2 >= sqrt(W2)/(4|a|)`.

That does **not** follow from the product bound: in general `xy>=c` does not imply `x>=c` and `y>=c`. The source-valid consequences used here are only

`||ell_I|| ||ell_J|| >= sqrt(W2)/(4|a|)`                         (5.1)

and, after naming the larger bank `J`,

`||ell_J|| >= W2^(1/4)/(2|a|^(1/2))`.                            (5.2)

This correction does not affect the partner's exact determinant identity, dichotomy, or random-coloring expectation. It only narrows the bank-extraction corollary to what its proof actually establishes.

## 6. Concrete target-valid gate check

The branch is nonempty and the projected-crossing conditions can hold at equality. Use nine original coordinates

`x,y,u1,u2,u3,u4,v0,v1,v2`

and let `epsilon=0.01`. Put

`Q=x^2 + epsilon y^2 + 2y(u1+v0) + 2 u^T C (v1,v2)`,             (6.1)

where

`C=4U`,
`U=(1/2)[[1,1],[1,-1],[-1,1],[-1,-1]]`.                         (6.2)

Take the physical pair `(x,y)`, `a=1`, and split `I={u1,...,u4}`, `J={v0,v1,v2}`. Then

`ell_J=(1,0,0)`, so `rank(M_J)=1` and `S_J=1`.                   (6.3)

Projecting the light crossing away from `ell_J` leaves the two columns `C`. Its two nonzero singular values are `4,4`, hence

`Z2=e_2(CC^T)=4^2*4^2=256`.                                      (6.4)

The nonzero two-row volume weights are four equal weights `1/4`; every row belongs to two of them, so

`alpha_1=alpha_2=alpha_3=alpha_4=1/2`.                            (6.5)

Thus every gate of the new arbitrary-rank crossing theorem is checked exactly. It gives

`||p_R||_infinity <= 3.73004796159...`,                           (6.6)

and Theorem 3.1 gives

`boxed: ||p_Q||_infinity <=5.46263523336...`.                    (6.7)

The matrix of (6.1) has eigenvalues numerically

`-4.06796718, -4, -1.19941977, 0, 0, 1, 1.20905563, 4, 4.06833132`,

so it has seven eigenvalues of modulus at least one and is a valid target instance. Here `W2=2.0064`; the coarser partner-fed bound (4.3) gives `5.95625301082...`.

These finite computations are checks only; the analytic theorem is Sections 2-4.

## 7. What changed and what remains

The previous run reached only a uniform residual square-root small-ball estimate and therefore a full-form `q log(1/q)` bound. The new mechanism first obtains a true bounded density for the scalar-completed residual from the projected-crossing theorem and then uses a translation-uniform half-Riesz compiler to reattach the correlated outer square. This removes the logarithm completely whenever the projected-crossing spread gate holds.

The remaining near-null leakage endpoint is now the complementary case: every product-certified bank orientation either has `Z2=0/tiny` or has a heavy 2-volume row marginal `>1/2`. That is a structural concentration problem, not the false scalar pointwise oscillatory-decay problem. The unrestricted three-large-eigenvalue conjecture remains open.

Continuity: `R` has a continuous `C_0` density by the projected-crossing theorem. The full `Q` is proved here only to have an essentially bounded density; continuity is not claimed because the outer square translation may be correlated with `R`.
