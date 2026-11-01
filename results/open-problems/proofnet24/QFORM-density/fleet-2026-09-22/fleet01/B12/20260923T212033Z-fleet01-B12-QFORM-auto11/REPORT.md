SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B12, 2026-09-23T21:20:33Z.
attacking: carrier-relative gain decomposition — isolate the only part of arbitrary signed added spectrum that can contract an original-coordinate square-energy carrier, while making orthogonal carrier action magnitude-free.

# fleet01/B12 — carrier-relative gain stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control used before publication: revision `2026-09-22.15`; refreshed brain head `6ecfd061ab88f4ddde0ab40ad88712c2fca7af6d`.  
Claim: `QFORM-CARRIER-RELATIVE-GAIN-STABILITY-v1`.  
Status: **PROVED SUPPORTING STABILITY THEOREM; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED.**  
Continuity: **not claimed** for the final hybrid, because the designated partner's six-square-mode compiler has branches proving only an essential `L^infinity` bound.

The exact owner target remains the arbitrary independent cap-one product law and arbitrary symmetric matrix with at least three eigenvalues of modulus at least one. No moment, support, log-concavity, iid, diagonal-coordinate, or post-rotation independence assumption is used below.

## 1. First unpaid implication

The global missing step remains structural: from bare `s_3(A)>=1`, force a product-preserving original-coordinate certificate covered by one of the proved receivers. This run does not assert such a universal extraction. It proves a sharper stability theorem for the assigned additional-eigenvalue problem: a huge signed spectral packet is charged only by its **relative contraction on the active carrier**, while all carrier action orthogonal to the old range is automatically beneficial square energy.

## 2. Exact carrier decomposition

Let `H` be `m` original coordinates and let

`P: R^m -> R^n`

be their coordinate inclusion. Let `A_0,S` be arbitrary real symmetric `n x n` matrices. Define

`V=A_0 P`,
`G_0=V^T V=P^T A_0^2 P`,
`q=rank G_0`,
`E=Ran(G_0)=(ker V)^perp`.

Let `Pi=V V^dagger` be the orthogonal projection onto `Ran(V)` and put

`D=S P`,
`K=V^dagger D=G_0^dagger V^T D`,
`R=(I-Pi)D`.

Then

`D=V K+R`,
`V^T R=0`,
`Ran(K) subset E`.                                             (2.1)

Let `B=(G_0|_E)^(1/2)>0` and let `U:E->Ran(V)` be the isometry in the polar decomposition `V|_E=U B`. Write

`K_E=K|_E:E->E`

and define the **relative active gain**

`L=B(I_E+K_E)B^(-1):E->E`.                                    (2.2)

### Lemma 2.1 — only the active-to-active gain can destroy carrier reserve

For every `k<=q`,

`s_k((A_0+S)P) >= s_k(LB)`.                                   (2.3)

#### Proof

Because `V=V P_E`, the aligned part is

`V+D-R=V(P_E+K)`.

Its columns coming from the active domain `E` form

`M_E=U B(I_E+K_E)=U L B`.                                     (2.4)

The columns coming from `ker V` contribute an additional positive-semidefinite term to the **row Gram** of the aligned matrix. Therefore every nonzero singular value of the full aligned matrix is at least the corresponding singular value of `M_E`, hence at least that of `LB` because `U` is an isometry.

Next, (2.1) gives orthogonality of the output ranges:

`[V(P_E+K)]^T R=0`.

Consequently the **column Gram** of the full matrix is the exact sum

`((A_0+S)P)^T((A_0+S)P)`
` =[V(P_E+K)]^T[V(P_E+K)]+R^T R`,                              (2.5)

and `R^T R` is positive semidefinite. This proves (2.3). QED.

Thus `(I-Pi)S P` can have arbitrary rank and arbitrary norm and is **free**: it only adds square energy. Likewise, action of `SP` on baseline-null input directions cannot decrease the active singular profile. The only potentially destructive object is the `q x q` normalized gain `L`.

## 3. Adaptive bad-channel theorem

### Theorem 3.1 — carrier-relative gain reserve

Assume for some `0<=r<q` and `alpha>0` that

`s_(q-r)(L) >= alpha`.                                        (3.1)

Then for every `k` with `k+r<=q`,

`boxed: s_k((A_0+S)P) >= alpha sqrt(lambda_(k+r)(G_0))`,       (3.2)

and hence

`boxed: lambda_k(((A_0+S)^2)[H,H])`
`       >= alpha^2 lambda_(k+r)(G_0).`                         (3.3)

Here only `r` relatively contracting channels are spent, regardless of the rank, signs, or magnitudes of the added spectrum.

#### Proof

Let `G_good subset E` be the span of the right singular vectors of `L` associated with its largest `q-r` singular values. Then

`||Ly|| >= alpha ||y||` for `y in G_good`.                    (3.4)

Let `F` be the span of the top `k+r` right singular vectors of `B`. Since `B` is invertible on `E`, `B^(-1)G_good` has dimension `q-r`; hence

`dim(F intersect B^(-1)G_good) >= (k+r)+(q-r)-q=k`.            (3.5)

For every `x` in this intersection,

`||LBx|| >= alpha ||Bx|| >= alpha s_(k+r)(B)||x||`.            (3.6)

The min-max characterization of `s_k(LB)` therefore gives

`s_k(LB)>=alpha s_(k+r)(B)`.

Now use Lemma 2.1 and `s_j(B)=sqrt(lambda_j(G_0))`. QED.

This is a multiplicative stability statement, not an operator-norm perturbation bound. An added matrix may have arbitrarily large operator norm and still have `alpha>=1`.

## 4. Arbitrary further tails: only local action is charged

Let `F=F^T` be arbitrary. Singular-value Weyl on the actual original-coordinate column block gives

`boxed:
 sqrt(lambda_k(((A_0+S+F)^2)[H,H]))
 >= [alpha sqrt(lambda_(k+r)(G_0))-||F P||_op]_+ .`            (4.1)

Only the action of `F` on `H` is paid. The outside-outside block of `F` may therefore have arbitrarily large spectrum.

### Spectral-threshold corollary

For an arbitrary signed spectral addition

`E_add=sum_a theta_a v_a v_a^T`,

choose `h>=0` and split

`S_h=sum_(|theta_a|>h) theta_a v_a v_a^T`,
`W_h=sum_(|theta_a|<=h) theta_a v_a v_a^T`.

Then `||W_h||_op<=h`. Construct `L_h` from `S_h` by (2.1)-(2.2). If

`s_(q-r)(L_h)>=alpha`,                                        (4.2)

then after any further symmetric `T`,

`boxed:
 sqrt(lambda_k(((A_0+E_add+T)^2)[H,H]))
 >= [alpha sqrt(lambda_(k+r)(G_0))-h-||T P||_op]_+ .`          (4.3)

No sign, rank, multiplicity, or amplitude restriction is imposed on the large packet `S_h`; all its orthogonal carrier action is exactly free. Arbitrarily many smaller eigenmodes of either sign cost the single threshold `h`.

The active interaction is directly expressible in the literal spectral data:

`V^T S_h P`
`=P^T A_0 S_h P`
`=sum_(|theta_a|>h) theta_a (P^T A_0 v_a)(P^T v_a)^T`.         (4.4)

Thus (4.2) is an original-coordinate deterministic condition; it never declares the spectral coordinates of `X` independent.

### Useful zero-loss subcone

If the normalized active interaction

`J=B K_E B^(-1)`

is skew-symmetric, then `L=I+J` and

`L^T L=I+J^T J >= I`.                                        (4.5)

Therefore `alpha>=1` with `r=0`, no matter how large `J` is. This produces a full-rank magnitude-free class distinct from PSD/polar-monotone additions.

## 5. Required application of completed partner `fleet02/B12`

The designated completed partner report is

`yspennstate/math-open-problems@c635fcdce6aa206c68f1f14e061cf617d72376fb`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/fleet02-B12-20260923T185321Z-r11/REPORT.md`.

Its theorem `QFORM-SIX-SQUARE-MODE-PAIR-COMPILER-v2` says: if `H` has `m>=6` original coordinates and the **actual final matrix** `A` obeys

`lambda_6((A^2)[H,H])>=g^2>0`,                                (5.1)

then every independent cap-one product source has an essentially bounded quadratic-form density with

`||p_(X^T A X)||_infinity <= C_m/g`,                           (5.2)

where, with `N_2=binom(m,2)`,

`C_m=max{8N_2 sqrt(6 pi m), 4 pi N_2,`
`        3*400^(1/3)*(4N_2)^(5/6), 10 sqrt(2e/3)}.`            (5.3)

Combining (4.3) with the partner theorem gives an end-to-end supporting compiler: if `q>=6+r` and

`g=alpha sqrt(lambda_(6+r)(G_0))-h-||T P||_op>0`,              (5.4)

then

`boxed: ||p_(X^T(A_0+E_add+T)X)||_infinity <= C_m/g.`          (5.5)

This is the required equation-level use of a completed partner result on the actual final matrix. No added quadratic remainder is treated as an independent convolution.

## 6. Exact noncommuting target-class family

Take two original-coordinate banks `H,J` of size eight and

`D_0=diag(2,3,4,5,6,7,8,9)`,
`A_0=[[0,D_0],[D_0,0]].`                                      (6.1)

Let `J_0` be block diagonal with four copies of

`[[0,-1],[1,0]]`,

so `J_0^T=-J_0` and `J_0^T J_0=I_8`. For arbitrary `t in R`, define the symmetric full-rank addition

`S_t=[[0,(t J_0 D_0)^T],[t J_0 D_0,0]].`                      (6.2)

On the carrier `H`,

`G_0=D_0^2`,
`K=t D_0^(-1) J_0 D_0`,
`L=D_0(I+K)D_0^(-1)=I+tJ_0`.                                  (6.3)

Therefore every singular value of `L` is exactly

`sqrt(1+t^2)`,                                                  (6.4)

because `(I+tJ_0)^T(I+tJ_0)=(1+t^2)I`.

The symmetric packet `S_t` itself has the sixteen eigenvalues

`+-2|t|,+-3|t|,...,+-9|t|`,                                   (6.5)

so this is an arbitrary-magnitude, both-sign, full-rank spectral addition. Because the entries of `D_0` are unequal, it is not a commuting spectral perturbation of the baseline in the physical basis.

Now add any symmetric `W` with

`||W||_op<=1/4`,                                               (6.6)

and any symmetric `T` satisfying only

`||T P_H||_op<=1/4`;                                          (6.7)

the outside-outside spectrum of `T` is unrestricted. Set

`A=A_0+S_t+W+T`.

Since the sixth largest eigenvalue of `G_0=D_0^2` is `16`, Theorem 3.1 and (4.1) give, uniformly for every `t`,

`boxed:
 sqrt(lambda_6((A^2)[H,H]))
 >=4 sqrt(1+t^2)-1/2
 >=7/2.`                                                       (6.8)

This is the actual inequality passed to the partner theorem. For `m=8`, `N_2=28` and

`C_8=8*28*sqrt(48 pi)=2750.7021909601613...`                  (6.9)

(the other three terms in (5.3) are smaller). Hence

`boxed:
 ||p_(X^T A X)||_infinity
 <= C_8/(7/2)
 =785.9149117029032... .`                                     (6.10)

This bound is uniform in the unbounded parameter `t`, in every admissible low packet `W`, and in every dense `T` satisfying only the carrier-action bound (6.7).

Finally, `s_6(A P_H)>=7/2`, so `s_6(A)>=7/2`; therefore every matrix in this family satisfies the owner's exact global target hypothesis `s_3(A)>=1`.

## 7. Scope and remaining gap

This theorem materially strengthens the additional-eigenvalue bookkeeping: it does not charge a large signed packet by its norm, rank, or total spectral mass. It charges only the number and severity of **relative active contraction channels**. Orthogonal carrier action and baseline-null carrier action are automatically positive resources.

It does **not** prove that a matrix satisfying only `s_3(A)>=1` must admit a carrier/baseline/threshold split for which `q>=6+r` and (5.4) is positive. Exact rank-three and aggregate-bank examples in the correction record show why a universal six-mode physical carrier cannot simply be asserted. The remaining structural task is to prove an exhaustive dichotomy: either such a relative-gain carrier exists, or failure forces one of the already-paid projected-crossing, grouped-bank/hub, ridge, physical-pair, half-Riesz, or Schur branches.

Full QFORM status: **OPEN**. Full continuity status: **OPEN**. The present partner-based branch proves essential boundedness only.

## 8. Source/correction discipline

Fresh controls and the live correction inbox were reread before publication. In particular this proof does not use: uniform pointwise quadratic-phase decay, arbitrary-joint coarea, post-rotation independence, a naive fiber supremum, a universal good 3x3 minor, or the claim that a small matrix tail makes `X^T T X` a small random variable. The tail enters only through the deterministic local singular-value inequality (4.1).

Execution context remains `WITHOUT_VERIFIED_BRAIN`: repository retrieval and publication occurred, but no separate authenticated native learned-memory receiver use was established.
