SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T11:05:46Z.
attacking: aggregate a disjoint fresh source bank before the curved pushforward, then use a quantitative cross-volume cut to recover continuity while preserving the partner's sharp essential bound.

# account01/B16 — fresh-bank Schur closure and continuity upgrade for the latest partner family

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T110546Z-account01-B16-QFORM-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING IMPLICATION / FULL QFORM OPEN`  
**Regularity:** continuity is proved below for the stated partner family with `m>=16`; global continuity remains open.  
**Native-memory status:** `WITHOUT_VERIFIED_BRAIN`.

The full theorem is not claimed. The purpose of this note is to close an analytic interaction that occurs once a disjoint rank-one product bank has been extracted, and to apply both the newest designated-partner result and the newest volume-stability result to actual inequalities.

## 1. Sources actually used


The rank-two fractional input is the completed supporting theorem

`QFORM-RANK2-AFFINE-HALF-RIESZ-v1`

at

`math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For an orthonormal two-dimensional product projection `P` and invertible symmetric `B`, it gives, in the row-span affine case,

`sup_t E |P^T B P + ell^T P + c-t|^(-1/2) <=16 sqrt(30)|det B|^(-1/4)`.       (1.1)

The scalar product-projection theorem used with it is the genuine original-product statement: if `V=n^T X` and `||n||_2=1`, then

`||p_V||_infinity <=sqrt(2)`.                                                          (1.2)

The latest designated partner account02/B16 result is

`QFORM-BANK-AGGREGATED-FRESH-SQUARE-N3-v1`

at

`math-open-problems@ade5cfe51d454341667779f7d9da714e4de99ed9:proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T103259Z-account02-B16-078f791ea823/REPORT.md`.

For its strict target-valid family it proves `||p_Q||_infinity<=4`; absolute continuity is proved but continuity was not claimed there.

The owner-required newest volume input is

`math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Its stability theorem says that, for an ORIGINAL-coordinate cross block `M=M0+E`, if

`s_3(M0)>=a>0`, `max_i (P_range(M0))_ii<=1/2`, `||E||op<=a/16`,               (1.3)

then the full ambient quadratic-plus-affine form has a continuous density vanishing at infinity and

`||p||_infinity <23/a`.                                                          (1.4)

All self blocks and outside couplings are retained. The source marks this theorem as a complete supporting proof with independent review pending.

## 2. A dependence-safe fresh-bank Schur theorem

### Theorem 2.1 — `QFORM-FRESH-BANK-SCHUR-HALFRIESZ-v1`

Let `S,J` be disjoint sets of ORIGINAL input coordinates. Let

`P=M X_S in R^2`, `MM^T=I_2`,

be an orthonormal two-dimensional projection of the `S`-bank, and let

`V=n^T X_J`, `||n||_2=1`,

be a normalized scalar projection of the disjoint `J`-bank. The coordinates of `P` may be arbitrarily dependent; only the original source banks `S,J` are independent.

Let `B` be any invertible symmetric `2 x 2` matrix, `gamma!=0`, `ell in R^2`, `c in R`, and let `h(X_S)` be an arbitrary measurable function. Define

`Q_h=P^T B P+ell^T P+c+gamma(V+h(X_S))^2`.                         (2.1)

Then `Q_h` has an essentially bounded density and

`||p_(Q_h)||_infinity <=16 sqrt(60)|gamma|^(-1/2)|det B|^(-1/4)`.     (2.2)

No conditional density of `P` is used, and no independence between its two coordinates is asserted.

#### Proof

Condition on the genuine original source bank `X_S`. Then `P`, `h`, and the first three terms in (2.1) are fixed, while `V` remains independent and has unconditional density cap `K<=sqrt(2)` by (1.2).

For every real translation `a`, the variable `gamma(V+a)^2` has, on its supported half-line, density bounded by

`K |gamma|^(-1/2)|y|^(-1/2)`.                                      (2.3)

Indeed the two inverse branches each contribute a Jacobian `1/(2 sqrt(|gamma y|))`, and the two source-density values are each at most `K`. Therefore, for every `t`,

`p_(Q_h)(t)
 <=K |gamma|^(-1/2)
    E |t-(P^T B P+ell^T P+c)|^(-1/2)`.                            (2.4)

Apply (1.1) and `K<=sqrt(2)`. This gives (2.2). The arbitrary same-source shift `h(X_S)` has disappeared before any projection-density or curved-level-set estimate is invoked. QED.

### Corollary 2.2 — full cross mixing with a fresh scalar bank

Let

`Gamma=[[C,b],[b^T,gamma]]`

be an invertible symmetric `3 x 3` matrix with `gamma!=0`. For

`Q=(P,V)^T Gamma(P,V)+ell^T P+c`,                                 (2.5)

completion of the fresh square gives

`Q=P^T(C-bb^T/gamma)P+ell^T P+c
   +gamma[V+gamma^(-1)b^T P]^2`.                                 (2.6)

Since

`det(C-bb^T/gamma)=det Gamma/gamma`,                              (2.7)

Theorem 2.1 yields

`boxed: ||p_Q||_infinity <=16 sqrt(60)(|gamma det Gamma|)^(-1/4).` (2.8)

Thus once a genuinely disjoint normalized scalar product bank has been extracted, arbitrary linear mixing of that bank with the dependent two-dimensional product projection is already paid whenever the fresh Rayleigh coefficient `gamma` and the Schur determinant are nonzero. The analytic obstruction is not the source-dependent translation created by square completion.

The remaining endpoint of this mechanism is `gamma=0` (or a structural situation in which no such disjoint scalar bank can be extracted). That endpoint cannot be obtained by dividing by `gamma` or by replacing original-product provenance with a joint density cap.

## 3. Actual application to the newest account02/B16 family

The partner family uses `m` divisible by four and balanced signs `eps,tau`. With arbitrary independent cap-one variables, define

`L=m^(-1/2) sum X_j`,
`U=m^(-1/2) sum eps_j X_j`,
`T=m^(-1/2) sum tau_j X_j`,
`V=m^(-1/2) sum Z_j`,

`H=eta(L+rho T)`, `Y=X_0+H`,

where `0<=rho<=1`, `eta>0`,

`theta:=eta^2(1+rho^2)<1/63`, `s^2:=1+theta`,

and `0<delta<=1/16`. The quadratic form is

`Q=4 delta Y^2+8YU+4V^2`.                                       (3.1)

The coefficient vectors of `Y` and `U` are orthogonal because

`sum eps_j=sum eps_j tau_j=0`; they have norms `s` and `1`. Hence

`P=(Y/s,U)`                                                        (3.2)

is an orthonormal two-dimensional projection of the whole original `(X_0,X_1,...,X_m)` product bank. The scalar `V` comes from a disjoint original bank and is normalized. In coordinates `(P_1,P_2,V)`,

`Gamma= [[4 delta s^2,4s,0],
         [4s,0,0],
         [0,0,4]]`,                                               (3.3)

so

`det Gamma=-64s^2`, `gamma=4`.                                    (3.4)

Corollary 2.2 therefore gives the explicit source-valid inequality

`||p_Q||_infinity <=4 sqrt(60)/sqrt(s) <=4 sqrt(60)
                   =30.9838667697...`.                            (3.5)

This is weaker than the partner's specialized bound `4`, but it proves a stronger robustness statement. For **every measurable function** `h=h(X_0,X_1,...,X_m)`,

`Q_h=4 delta Y^2+8YU+4(V+h)^2`                                    (3.6)

still satisfies exactly the same estimate (3.5). Thus an arbitrary nonlinear translation of the aggregated fresh square by the entire opposite source bank does not destroy dimension-free boundedness. This is the projection-product interaction promised by the assignment: aggregation occurs first, and the curved singularity is paid afterward by the rank-two half-Riesz estimate.

## 4. New continuity upgrade for the partner's sharp bound

The partner proved the **essential** bound `4` but did not claim continuity. The new volume-stability theorem can be applied to the same matrix, and its continuity conclusion can be combined with the partner's sharper essential estimate.

Assume here `m>=16` and `4|m`. Put `q=m/4` and

`k=floor(q/2)`, `r=k/q`.

If `q` is even, `r=1/2`; if `q` is odd then `q>=5` and

`2/5<=r<1/2`.                                                     (4.1)

Choose exactly `k` physical rows from each of the four `(eps,tau)` sign classes for a diffuse side `J`, and choose exactly `m/2` rows of the fresh `V` bank for `J`. Put the hub `X_0` and every remaining row in `I`.

Normalize the partner spectral frame as

`R=[p,u,v]`, `p=y/s`,                                            (4.2)

so `R^T R=I_3`. Because each of the four shared sign classes contributes equally to `J`, all mixed Gram entries vanish and

`S_J:=R_J^T R_J
     =diag(r theta/s^2,r,1/2)`,                                  (4.3)

`S_I:=R_I^T R_I
     =diag(1-r theta/s^2,1-r,1/2)`.                              (4.4)

Both are positive definite because `eta>0`.

### 4.1 The row-leverage gate is uniformly satisfied

The cross block will be oriented as

`M=A[J,I]=R_J Gamma R_I^T`,                                      (4.5)

so its row space is on the hub-free diffuse side `J`.

Since `Gamma` and `S_I` are invertible, `range(M)=range(R_J)`. Thus

`P_range(M)=R_J S_J^(-1) R_J^T`.                                (4.6)

For a selected shared row with signs `(eps_j,tau_j)`, its leverage equals

`l_j
 =1/(m r) [ (1+rho tau_j)^2/(1+rho^2)+1 ]
 <=3/(m r)`.                                                     (4.7)

If `q` is even, `mr=m/2>=8`, so `l_j<=3/8`. If `q` is odd, `mr=2(q-1)>=8`, again `l_j<=3/8`. A fresh selected row has leverage

`l_k=2/m<=1/8`.                                                   (4.8)

Hence

`boxed: max_i (P_range(M))_ii <=3/8<1/2.`                        (4.9)

This is an exact product-source calculation, not a statement about conditional projection densities.

### 4.2 Quantitative third singular value

Take polar factorizations

`R_J=U_J S_J^(1/2)`, `R_I=U_I S_I^(1/2)`,                       (4.10)

where `U_J,U_I` have orthonormal columns. Therefore the three nonzero singular values of `M` are exactly those of

`S_J^(1/2) Gamma S_I^(1/2)`.                                    (4.11)

The partner's exact eigenvalue computation for the upper `2 x 2` block in (3.3) gives

`s_min(Gamma)>=4s/(1+delta s)`.                                  (4.12)

Also

`lambda_min(S_J)=r theta/s^2`,
`lambda_min(S_I)=1/2`.                                           (4.13)

Consequently

`s_3(M)
 >= [sqrt(r theta)/s] [4s/(1+delta s)] [1/sqrt(2)]
 = 2 sqrt(2r) eta sqrt(1+rho^2)/(1+delta s)
 >= 4 eta sqrt(1+rho^2)/(sqrt(5)(1+delta s))`.                  (4.14)

Set

`a:=4 eta sqrt(1+rho^2)/(sqrt(5)(1+delta s))`.                   (4.15)

Apply the newest volume-stability theorem with `M0=M`, `E=0`. Equations (4.9) and (4.14) verify every matrix gate. Therefore the partner law has a continuous density `p_c` vanishing at infinity and, separately,

`||p_c||_infinity
 < (23 sqrt(5)/4)(1+delta s)/(eta sqrt(1+rho^2))`.               (4.16)

This bound is not uniform as `eta->0`; it is used only to establish continuity.

### 4.3 Combine continuity with the partner's sharp essential bound

The latest account02/B16 theorem supplies a density `p` with

`ess sup p<=4`.                                                   (4.17)

The continuous density `p_c` in (4.16) represents the same probability law, so `p_c=p` almost everywhere. If `p_c(t_0)>4` at any point, continuity would make `p_c>4` on an interval of positive Lebesgue measure, contradicting (4.17). Hence

`boxed: sup_t p_c(t)<=4`.                                        (4.18)

Thus, for every partner-family parameter choice with `4|m`, `m>=16`, `eta>0`, the law in (3.1) has a **continuous density vanishing at infinity with pointwise supremum at most 4**.

This is a genuine new synthesis: the sharp constant comes from the completed designated partner, while continuity comes from the owner-required volume-stability theorem. Neither input alone states (4.18).

## 5. Direct higher-rank inequality from the completed partner result

Let `W` be any real random variable generated by additional ORIGINAL coordinates disjoint from all sources in (3.1); no density or moment assumption on `W` is needed. Then `W` is independent of `Q`, so

`p_(Q+W)=p_Q * law(W)`.                                          (5.1)

Young's elementary probability-convolution inequality gives

`boxed: ||p_(Q+W)||_infinity <=||p_Q||_infinity<=4.`             (5.2)

For `m>=16`, use the continuous representative from (4.18). Since it belongs to `C_0(R)` and is therefore uniformly continuous, convolution with an arbitrary probability measure remains continuous and still has supremum at most `4`.

In particular, take any extra independent product block `X_K` and any symmetric matrix `C` of arbitrary dimension, signs and norm, and set

`W=X_K^T C X_K`.                                                 (5.3)

Then the block-direct-sum quadratic form

`Q_total=Q+X_K^T C X_K`                                         (5.4)

is an arbitrary-higher-rank target-valid family (it retains the partner's three large eigenvalues) and satisfies

`||p_(Q_total)||_infinity<=4`;                                   (5.5)

for `m>=16` its density has a continuous representative with the same pointwise bound. This is the requested actual inequality obtained by applying a completed account02/B16 result, rather than merely citing it.

## 6. What this pays, and what remains

The new analytic conclusion is:

> A disjoint normalized rank-one product bank with a quantitatively nonzero quadratic coefficient can be aggregated **before** nonlinear integration. After aggregation, arbitrary linear cross mixing with a dependent two-dimensional product projection becomes only a source-dependent translation of the fresh square, and Theorem 2.1 pays that translation uniformly.

The newest partner family demonstrates why the bank must be aggregated before reciprocal minor payment: its individual physical fresh-square certificates deteriorate like `m^(3/4)`, while the aggregate certificate is constant. The present theorem shows that after this aggregation one also need not demand exact spectral decoupling of the fresh scalar from the opposite pair.

The first unpaid structural implication is therefore sharpened to

`QFORM-NEAR-COLOOP-FRESH-NONISOTROPIC-BANK-OR-SHARED-NULL-v1`:

starting from a general surviving near-coloop/no-pivot configuration, prove that either

1. a disjoint original-coordinate scalar bank can be aggregated so that its normalized quadratic Rayleigh coefficient `|gamma|` and the corresponding two-dimensional Schur determinant furnish a quantitative version of `(2.8)`; or
2. a diffuse original-coordinate cross block enters the volume-stability exit; or
3. one reaches the genuinely shared-bank / null-fresh-Rayleigh endpoint and proves a source-first transducer there.

Neither the three-large-eigenvalue hypothesis by itself nor a bounded two-dimensional projected density currently proves this trichotomy. The live counterexamples forbid replacing item 3 by a normalized conditional cap, arbitrary-joint coarea, or a uniformly good single physical minor. Arbitrary higher-rank cross-coupled forms remain part of the global open problem.

## 7. Status

`QFORM-FRESH-BANK-SCHUR-HALFRIESZ-v1`: complete supporting derivation from the pinned rank-two theorem and the genuine scalar product-projection bound; independent review not performed in this run.

Partner continuity synthesis (4.18): complete conditional application of the supplied volume-stability theorem and the completed account02/B16 bound; the volume-stability source itself records independent review as pending.

Full QFORM theorem: `OPEN / NOT PROVED`.

Global continuous-density theorem: `OPEN / NOT PROVED`.
