SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-24T06:52:24Z.
attacking: high-leverage fixed-hub packets by promoting literal leaf coordinates into retained physical hubs, preserving the mixed Brascamp--Lieb Fourier exponent and replacing tiny scalar pivots by an exact residual-Gram volume.

# fleet01/B09 r32 — promoted-leaf retained-hub compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: B09 bilinear block mechanism  
Status: **NEW SUPPORTING THEOREM / ESSENTIAL STEP APPLIED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted conjecture is not claimed solved. The result below is a source-coordinate analytic compiler for the high-leverage branch left by fleet01/B09 r31. It works for every finite low-rank leaf completion, in particular ranks 1--4, and it uses the newest completed designated-partner theorem fleet02/B09 r18 at an actual inequality.

All random variables below are literal original independent source coordinates with one-dimensional densities bounded by one. No random-variable rotation, moment assumption, support assumption, log-concavity, iid assumption, Gaussian assumption, or deletion of a small quadratic coefficient is used.

## 1. Source results actually used

The completed designated-partner source is fleet02/B09 r18,

`QFORM-RETAINED-HUB-BRASCAMP-LIEB-v1`,

at

`yspennstate/math-open-problems@e03ae6cafb3cca423b4a2fab5c6aa0106cc319f4`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260924T055153Z-fleet02-B09-QFORM-r18/REPORT.md`.

Its exact statement is as follows. For a literal split `H union I union J`, `h=|H|`, and

`A_II=D+sum_(k=1)^r lambda_k v_k v_k^T`,

with `D` diagonal and all `lambda_k!=0`, define the mixed rows

`rho_i=((v_1)_i,...,(v_r)_i,A_(ih):h in H) in R^(r+h)`.

Choose retained hubs `S_H subset H`, add their coordinate rows to the Gram

`Gbar=sum_(i in I) rho_i rho_i^T+sum_(a in S_H)e_a e_a^T`,

put

`c_i=rho_i^T Gbar^(-1)rho_i`, `b_a=e_a^T Gbar^(-1)e_a`, `B=sum b_a`,

and `alpha=h+r/2-B`. If `Gbar>0`, every `c_i<=1/2`, and `alpha>1`, then the full ambient quadratic form, with every other block and every affine term arbitrary, has a continuous density and

`|phi_Q(t)|<=K |t|^(-alpha)`,

where

`K=[prod_a b_a^(-b_a/2)] 2^(-h+B)(4pi)^alpha [prod_k |lambda_k|]^(-1/2) det(Gbar)^(-1/2)`.

Consequently

`||p_Q||_infinity <= alpha/[pi(alpha-1)] K^(1/alpha)`,

and the identical coefficient gives `P{Q in L}<=C|L|` for every interval `L`.

The previous fleet01/B09 r31 source is

`yspennstate/math-open-problems@14ef2c833e502312b3e86d503933fa930a7f6f9e`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B09/20260924T054443Z-fleet01-B09-QFORM-auto11-r31/REPORT.md`.

It left the explicit debt `QFORM-FIXEDHUB-HIGHLEVERAGE-OR-RANK234-OMEGA1-v1`: promote high-leverage literal leaf coordinates without tiny-pivot inversion, and extend the fixed-hub analytic compiler beyond rank-one completed leaf curvature.

## 2. New theorem: promote arbitrary literal leaves at no Fourier-power cost

### Theorem 2.1 — `QFORM-PROMOTED-LEAF-RETAINED-HUB-BL-v1`

Let `h` be one literal original coordinate and `L,J` disjoint literal banks. Assume on the leaf bank

`A_LL = D + V Lambda V^T`,                                      (2.1)

where `D` is diagonal in the original source coordinates,

`Lambda=diag(lambda_1,...,lambda_r)`, `lambda_k!=0`,             (2.2)

and `V` is the physical leaf-by-mode coefficient matrix. Let

`c=A[L,h]`.                                                       (2.3)

No assumption is made on `A_hh`, on blocks involving `J`, or on affine terms.

Choose **any** set `S subset L` of literal leaf coordinates to promote to physical hubs, and put

`R=L\S`, `k=|S|`.                                                 (2.4)

For every residual literal leaf `j in R`, define the **base mixed row**

`x_j=(V_(j,1),...,V_(j,r),c_j) in R^(r+1)`,                      (2.5)

and the residual base Gram

`G_R=sum_(j in R) x_j x_j^T`.                                    (2.6)

Assume

`G_R>0`                                                           (2.7)

and every residual normalized leverage obeys

`ell_j=x_j^T G_R^(-1)x_j <=1/2`.                                 (2.8)

Then the **full ambient quadratic form** has a continuous `C_0` density and

`boxed:`
`||p_Q||_infinity <= C_r [ det(G_R) prod_(q=1)^r |lambda_q| ]^(-1/(r+2)),`  (2.9)

where

`boxed:`
`C_r = 4(r+2)/r * 2^(-2/(r+2)).`                                 (2.10)

The identical constant controls every interval:

`boxed:`
`P{Q in I} <= C_r [ det(G_R) prod_q |lambda_q| ]^(-1/(r+2)) |I|.` (2.11)

For ranks one through four,

`C_1=7.559526299369239...`,
`C_2=5.656854249492381...`,
`C_3=5.052388555034661...`,
`C_4=4.762203155904599...`.                                     (2.12)

The striking feature is that **the number `k` of promoted literal coordinates does not appear in the Fourier exponent or in the numerical prefactor**. Promotion consumes only the residual determinant `det(G_R)`.

### Proof

After promotion the physical hub bank is

`H={h} union S`,                                                  (2.13)

while the active leaf bank is `R`. Its same-bank block remains

`A_RR=D_R+V_R Lambda V_R^T`.                                    (2.14)

For distinct `j in R`, `s in S`, the physical diagonal contributes nothing to the cross entry, so

`A_(js)=V_j Lambda V_s^T`.                                      (2.15)

Thus the mixed row required by the partner theorem is

`rho_j=(V_j,c_j,V_j Lambda V_S^T)`.                              (2.16)

Let `d_0=r+1`. Define

`B_S=[ V_S Lambda , 0 ] in R^(k x d_0)`,                         (2.17)

where the final zero column corresponds to the original hub coefficient `c_j`, and set

`M=[ I_(d_0) ; B_S ]`,
`E=[ 0 ; I_k ]`,
`N=[M,E]=[[I_(d_0),0],[B_S,I_k]].`                               (2.18)

Then

`rho_j=M x_j`,                                                   (2.19)

and `N` is block lower triangular with

`det N=1`.                                                       (2.20)

Retain **all promoted physical hub densities** `S` in the partner theorem. The augmented Gram is therefore

`Gbar=sum_(j in R)rho_jrho_j^T+EE^T`
`    =M G_R M^T+EE^T`
`    =N diag(G_R,I_k) N^T`.                                     (2.21)

This exact factorization gives immediately

`boxed: det Gbar = det G_R.`                                    (2.22)

Moreover, since

`Gbar^(-1)=N^(-T)diag(G_R^(-1),I_k)N^(-1)`,                     (2.23)

for a residual leaf row

`rho_j=N(x_j,0)`,                                                (2.24)

so

`boxed: rho_j^T Gbar^(-1)rho_j = x_j^T G_R^(-1)x_j=ell_j.`       (2.25)

For a retained promoted hub coordinate `s`, its coordinate vector is

`e_s=N(0,e_s)`,                                                  (2.26)

hence

`boxed: b_s=e_s^T Gbar^(-1)e_s=1.`                              (2.27)

Therefore the total retained-hub weight is

`B=k`.                                                          (2.28)

The partner theorem now has

`h'=1+k`                                                        (2.29)

physical hubs and the same rank `r`, so its Fourier exponent is

`alpha=h'+r/2-B`
`     =1+k+r/2-k`
`     =1+r/2`.                                                   (2.30)

This is the exact no-power-loss cancellation promised above. The partner constant becomes

`K=2^(-1)(4pi)^(1+r/2)`
`  *[det(G_R) prod_q |lambda_q|]^(-1/2)`.                       (2.31)

Since `alpha=1+r/2>1`, its direct `L^1` Fourier integration gives

`||p_Q||_infinity`
` <= alpha/[pi(alpha-1)] K^(1/alpha)`
` =4(r+2)/r 2^(-2/(r+2))`
`  *[det(G_R)prod_q|lambda_q|]^(-1/(r+2)),`                     (2.32)

which is (2.9). The characteristic function is integrable, hence the density is continuous and vanishes at infinity. The same coefficient gives (2.11). No Cauchy--Schwarz decoupling, probability squaring, or square-root conversion of the final small-ball probability occurs. QED.

## 3. Exact leverage-peeling identity

The theorem suggests a literal-coordinate peeling procedure. Suppose at some stage the residual Gram is

`G=sum_(j in R)x_jx_j^T>0`,                                    (3.1)

and a physical row `i in R` has leverage

`ell_i=x_i^T G^(-1)x_i`.                                       (3.2)

Since

`G-x_ix_i^T=sum_(j in R\{i})x_jx_j^T >=0`,                     (3.3)

one has `0<=ell_i<=1`. If `ell_i<1`, matrix determinant lemma gives the exact promotion cost

`boxed:`
`det(G-x_ix_i^T)=det(G)(1-ell_i).`                              (3.4)

Thus a greedy rule may repeatedly promote a literal row with leverage above `1/2`. Each promotion:

1. keeps the Fourier exponent exactly `1+r/2` by Theorem 2.1;
2. creates no reciprocal scalar-pivot factor;
3. changes the entire determinant currency by exactly the multiplicative factor `1-ell_i`.

If the process reaches `ell_i=1`, then the residual Gram loses rank after removing that one literal coordinate. In whitened feature coordinates `y_i=G^(-1/2)x_i`, `||y_i||=1` and

`I-y_iy_i^T=sum_(j!=i)y_jy_j^T`,                                (3.5)

so every remaining row is orthogonal to `y_i`. Hence `ell_i=1` is an **exact physical coloop certificate** in the mixed frame, not an unexplained failure of the analytic bound.

This isolates the next structural debt sharply: either peeling reaches a residual frame with every leverage at most `1/2` while retaining enough determinant currency, or it produces a near/exact coloop state that must be routed by a lower-dimensional literal packet. There is no longer a separate analytic penalty for the count of promoted coordinates.

## 4. Rank-one specialization and DPP avoidance currency

The r31 packet has rank-one completed leaf curvature. Normalize its two-dimensional mixed frame as follows. Let `v,z` be orthonormal physical leaf vectors and write

`c=mu v+theta z`, `theta!=0`.                                  (4.1)

For `u_j=(v_j,z_j)` and a promoted set `S`, put

`H_S=sum_(j notin S)u_ju_j^T`
`   =I_2-sum_(i in S)u_iu_i^T`.                                (4.2)

Because `[v,c]=[v,z][[1,mu],[0,theta]]`,

`boxed: det G_R = theta^2 det H_S.`                             (4.3)

By Cauchy--Binet,

`det H_S=sum_{I subset L\S, |I|=2} det([v,z]_I)^2`.            (4.4)

Thus `det H_S` is exactly the total Pluecker two-basis mass avoiding the promoted physical set `S`.

For `r=1`, Theorem 2.1 becomes

`boxed:`
`||p_Q||_infinity`
` <=3*2^(4/3) [ |lambda| theta^2 det H_S ]^(-1/3),`            (4.5)

with a continuous density and the same interval coefficient.

If `rho` is the two-basis disjointness probability from r31, then

`Omega_(1,h)^dis=lambda^2 theta^4 rho`,                         (4.6)

so (4.5) can also be written

`||p_Q||_infinity`
` <=3*2^(4/3) [Omega_(1,h)^dis]^(-1/6)`
`   * rho^(1/6) [det H_S]^(-1/3).`                              (4.7)

This shows exactly what the high-leverage promotion branch still owes combinatorially: preserve enough **avoidance mass** while peeling, or identify the resulting coloop/localized endpoint. The old vague “tiny promoted pivot” is replaced by the canonical determinant/avoidance quantity (4.4).

## 5. Exact rank-r fixed-hub Pluecker decomposition

The rank-one factorization of r31 has a useful finite-rank extension. Let the leaf non-diagonal block be

`S=V Lambda V^T`                                                (5.1)

and let `a=A_hh`. For disjoint leaf pairs

`I={i,j}`, `J={k,l}`, `I cap J=empty`,                           (5.2)

the physical leaf diagonal `D` contributes no entry to `A[I,J]`. Define

`Delta_I^(pq)=v_(ip)v_(jq)-v_(iq)v_(jp)`,                       (5.3)

`W_I^p=c_i v_(jp)-c_j v_(ip)`.                                 (5.4)

Then direct expansion plus Cauchy--Binet gives the exact identity

`boxed:`
`det A[{h} union I,{h} union J]`
` = a sum_(p<q) lambda_p lambda_q Delta_I^(pq) Delta_J^(pq)`
`   - sum_p lambda_p W_I^p W_J^p.`                             (5.5)

Indeed,

`det [[a,c_J^T],[c_I,S_(I,J)]]`
`=a det S_(I,J)-c_J^T adj(S_(I,J))c_I`;                         (5.6)

Cauchy--Binet yields the first sum in (5.5), while expanding the second term mode by mode yields

`c_J^T adj(S_(I,J))c_I=sum_p lambda_p W_I^p W_J^p`.            (5.7)

Therefore the matrix of fixed-hub disjoint-pair third minors is a signed Gram combination of at most

`r+binom(r,2)=r(r+1)/2`                                         (5.8)

pair-space feature vectors. For `r<=4`, this feature rank is at most ten. This does **not** by itself prove a density bound—indefinite signed Gram structure and pair collisions still matter—but it removes any mystery about ranks two through four and gives a finite-dimensional structural object for the next aggregation step.

## 6. Actual target-valid application of the designated partner theorem

This is not a toy outside the owner's quantifiers. Take a literal hub variable `U`, a literal leaf `X_0`, and a literal bank `X_T` of size `m=8`. Choose three flat orthonormal Walsh vectors `d_1,d_2,d_3 in R^8`. Define literal physical coefficient vectors

`v_1=sqrt(3/5)e_0+sqrt(2/5)d_1`,
`v_2=d_2`,
`z=d_3`,                                                        (6.1)

where `d_q` are supported on `T` and `e_0` is the `X_0` coordinate. Then `v_1,v_2,z` are orthonormal in the physical leaf space.

Consider the quadratic form

`boxed:`
`Q=(v_1^T X_L)^2+(v_2^T X_L)^2+2U(z^T X_L).`                   (6.2)

In the orthonormal deterministic coefficient basis `(v_1,v_2,z,U)`, the active matrix is

`[1] direct_sum [1] direct_sum [[0,1],[1,0]]`,                 (6.3)

so

`spec_nonzero(A)={1,1,1,-1}`.                                  (6.4)

Thus (6.2) satisfies the owner's full three-large-eigenvalue hypothesis.

Before promotion, the one-hub/rank-two mixed rows are

`x_j=((v_1)_j,(v_2)_j,z_j)`,                                   (6.5)

and their Gram is `I_3`. The literal row `j=0` has leverage

`ell_0=3/5>1/2`,                                                (6.6)

so the unaugmented pinned mixed-frame gate fails.

Now promote **the actual source coordinate `X_0`** to a second physical hub and retain its density, exactly as fleet02/B09 r18 permits. On the eight residual leaves,

`G_R=diag(2/5,1,1)`,
`det G_R=2/5`.                                                   (6.7)

Every residual Walsh row has normalized leverage

`(1/8)+(1/8)+(1/8)=3/8<1/2`.                                  (6.8)

Take `r=2`, `lambda_1=lambda_2=1`. Theorem 2.1, which is a direct specialization of the completed partner theorem, gives

`boxed:`
`||p_Q||_infinity`
` <=4sqrt(2)(2/5)^(-1/4)`
` =7.113117640155692... <7.114,`                                (6.9)

and

`boxed:`
`P{Q in I}<7.114 |I|`                                          (6.10)

for every interval `I`. The density is continuous.

This is the required completed-partner application to a real target-valid inequality. It also demonstrates the exact point of the new compiler: one literal row violates the old `<=1/2` leverage gate, but promoting that same source coordinate and retaining its density restores the gate without losing a Fourier power.

### Uniform rank-one-through-four regression family

The same construction works for every `1<=r<=4`. Take mutually orthonormal flat Walsh vectors `d_1,...,d_(r+1)` on a sufficiently large bank `T`, put

`v_1=sqrt(3/5)e_0+sqrt(2/5)d_1`,
`v_q=d_q`, `2<=q<=r`,
`z=d_(r+1)`,                                                      (6.11)

and

`Q_r=sum_(q=1)^r(v_q^T X)^2+2U(z^T X)`.                        (6.12)

Its nonzero spectrum is `r` copies of `+1` together with `+1,-1`. If `|T|>=2(r+1)`, promotion of `X_0` leaves every normalized residual leverage at most `1/2`. With `det G_R=2/5`, the bounds from (2.9) are respectively

`r=1: 10.2598556801`,
`r=2:  7.1131176402`,
`r=3:  6.0685473434`,
`r=4:  5.5479335829`.                                           (6.13)

Hence the analytic promotion mechanism genuinely covers ranks two through four, not only the previous rank-one Pluecker factorization.

## 7. What has and has not been closed

The r31 debt splits into an analytic and a structural part.

**Closed analytically in this run.** Once a set of literal high-leverage leaves has been chosen for promotion and the residual base mixed frame has positive Gram with leverages at most `1/2`, all promoted coordinates can be retained simultaneously. There is no loss depending on how many were promoted, and the result works for every rank `r>=1`; ranks `2,3,4` therefore need no new Fourier mechanism. The output density is continuous and the interval estimate is linear.

**Still open structurally.** Under only the owner's three-large-eigenvalue hypothesis and the aggregate nonprincipal third-compound currency inherited from the singular-pair route, force one of:

1. a promoted set `S` for which the residual determinant currency `det(G_R) prod|lambda_q|` is universally large enough for (2.9);
2. an exact/near coloop or low-dimensional localized packet that is paid by an existing physical-pair/triple/grouped-crossing receiver;
3. an already-paid disjoint-volume/carrier exit.

For the rank-one fixed-hub packet the missing quantity is now particularly explicit: preserve enough two-basis avoidance mass `det H_S` during leverage peeling. No reciprocal selected physical minor is needed.

A concise name for the next implication is

`QFORM-PROMOTION-DETERMINANT-OR-COLOOP-EXIT-v1`.

## 8. Compatibility with live corrections

This proof does not use any corrected-away interface:

- no law-uniform pointwise van-der-Corput decay;
- no arbitrary-joint coarea claim;
- no independence after an orthogonal rotation of the random variables;
- no conditional density cap after sum/difference conditioning;
- no dimension-free worst fiber supremum;
- no assertion that one physical minor/pair is uniformly good;
- no treatment of a small matrix norm as a small random quadratic error;
- no Monte Carlo histogram as evidence of a universal theorem.

The only deterministic coordinate changes occur in the finite-dimensional **coefficient/Gram algebra** (2.18); the random variables remain literal independent source coordinates throughout.

## 9. Deterministic checks

Independent numerical checks for random physical data at `r=1,2,3,4`, with three promoted leaves, verified

`det Gbar=det G_R`

to at worst `8.9e-16`, residual leverage equality (2.25) to at worst `3.4e-16`, and every retained promoted-hub weight `b_s=1` to floating error.

The rank-r Pluecker identity (5.5) was checked on random disjoint physical leaf quadruples. Maximum absolute discrepancies were approximately

`8.9e-16, 1.3e-16, 5.4e-15, 8.9e-15`

for `r=1,2,3,4` respectively.

For the target-valid rank-two family (6.2), direct numerical eigendecomposition gives nonzero spectrum `{-1,1,1,1}` up to roundoff; the promoted residual Gram is `diag(0.4,1,1)`, each of its eight normalized leaf leverages is exactly `3/8`, and (6.9) evaluates to `7.113117640155692...`.

These finite checks are regressions for the exact algebra, not evidence for the full conjecture.

## 10. Status

**Full QFORM:** OPEN / not proved / not disproved.  
**New theorem:** proved conditional on the completed fleet02/B09 r18 theorem in its stated scope.  
**Continuity:** proved in the new promoted-leaf branches because the resulting characteristic function is `L^1`; not claimed for the unrestricted target.  
**Next B09 step:** `QFORM-PROMOTION-DETERMINANT-OR-COLOOP-EXIT-v1`.
