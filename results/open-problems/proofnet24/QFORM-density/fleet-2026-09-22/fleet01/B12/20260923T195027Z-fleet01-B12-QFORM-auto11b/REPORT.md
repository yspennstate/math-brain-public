SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B12, 2026-09-23T19:50:27Z.
attacking: a carrier-local approximation-number theorem for arbitrary signed spectral additions, replacing hard footprint rank by the best local low-rank approximation error.

# fleet01/B12 — local approximation-number stability for additional spectrum

Run: `20260923T195027Z-fleet01-B12-QFORM-auto11b`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Additional eigenvalue control  
Claim: `QFORM-LOCAL-ACTION-APPROXIMATION-NUMBER-STABILITY-v1`  
Status: **PROVED SUPPORTING STABILITY THEOREM; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED.**  
Regularity: the concrete application below yields an essentially bounded density through the designated partner's six-mode carrier theorem; continuity is **not claimed** for that theorem as a whole.

## 1. Exact target and first unpaid implication

The owner target remains: for every dimension, every product law of independent real variables whose scalar densities are bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal bound for the density of `X^T A X`, or give a valid counterexample. No moment, compact-support, log-concavity, iid, connected-support, Gaussian, or post-rotation independence assumption may be inserted.

This B12 run asks what happens when a useful original-coordinate carrier is present and arbitrary additional signed spectrum is added. The preceding B12 run proved an exact hard-footprint theorem: if `rank(E P_H)<=r`, only `r` carrier reserve directions are lost. The present theorem replaces exact rank by a **soft approximation-number charge**. A full-rank added operator can therefore be harmless when its action on the protected physical carrier is well approximated by low rank, even if its global norm and some of its eigenvalues are arbitrarily large.

The first unpaid implication for the full conjecture remains structural: derive, from bare `s_3(A)>=1`, an original-coordinate carrier or complementary grouped/ridge/hub/Schur certificate with quantitative parameters. The theorem below is a compiler once a carrier is identified; it does not assert that every target matrix has such a carrier.

## 2. Designated partner theorem actually used

The newest compatible completed `fleet02/B12` theorem used here is

`yspennstate/math-open-problems@c635fcdce6aa206c68f1f14e061cf617d72376fb`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/fleet02-B12-20260923T185321Z-r11/REPORT.md`.

Its Theorem 4.1 (`QFORM-SIX-SQUARE-MODE-PAIR-COMPILER-v2`) states: if `H` is a set of `m>=6` ORIGINAL coordinates and the **actual final symmetric matrix** `A` satisfies

`lambda_6((A^2)[H,H]) >= g^2 > 0`,                              (2.1)

then every independent cap-one product input has an essentially bounded quadratic-form density with

`||p_(X^T A X)||_infinity <= C_m/g`,                            (2.2)

where, with `N_2=binom(m,2)`,

`C_m=max{`
`  8 N_2 sqrt(6 pi m),`
`  4 pi N_2,`
`  3*400^(1/3)*(4N_2)^(5/6),`
`  10 sqrt(2e/3)`
`}.`                                                           (2.3)

That theorem combines an actual-original-coordinate D5 receiver, a projected-gradient receiver, and a physical-pair receiver. It places no restriction on the rest of the spectrum. It does not claim continuity for the hybrid theorem as a whole.

## 3. Main deterministic theorem

Let `H` be a set of `m` ORIGINAL coordinates and let `P=P_H` be the corresponding orthogonal coordinate projection. For a matrix `M`, write

`s_1(M)>=s_2(M)>=...`

for its singular values, padding by zeros as necessary.

### Theorem 3.1 — carrier-local approximation-number stability

Let `A_0=A_0^T` and `E=E^T` be arbitrary real `n x n` matrices, and put

`A=A_0+E`.

For every integer `k>=1` and every `r>=0` satisfying

`k+r<=m`,                                                       (3.1)

one has

`boxed:`
` sqrt(lambda_k((A^2)[H,H]))`
` >= [sqrt(lambda_(k+r)((A_0^2)[H,H])) - s_(r+1)(E P)]_+ .`    (3.2)

Equivalently,

`boxed:`
` s_k(A P)`
` >= [s_(k+r)(A_0 P) - s_(r+1)(E P)]_+ .`                      (3.3)

Optimizing in `r`,

`boxed:`
` sqrt(lambda_k((A^2)[H,H]))`
` >= max_(0<=r<=m-k)
`      [sqrt(lambda_(k+r)((A_0^2)[H,H]))-s_(r+1)(E P)]_+ .`    (3.4)

No restriction is imposed on the sign, rank, norm, inertia, eigenspaces, or commutation properties of `E`.

### Proof

Because `A` is symmetric,

`(A P)^T(A P)=P A^2 P`.                                        (3.5)

Restricted to `Ran P`, this is precisely the principal compression `(A^2)[H,H]`. Therefore

`s_k(A P)^2=lambda_k((A^2)[H,H])`.                             (3.6)

Similarly,

`s_j(A_0 P)^2=lambda_j((A_0^2)[H,H])`.                         (3.7)

Take a rank-`r` truncated singular-value decomposition of the **carrier action** `E P`:

`E P=L_r+R_r`,                                                  (3.8)

with

`rank L_r<=r`,
`||R_r||_op=s_(r+1)(E P)`.                                     (3.9)

This is exactly the Eckart--Young best rank-`r` approximation in operator norm. Importantly, `L_r` is used only as a rectangular deterministic decomposition of the action on the original-coordinate carrier; it is not interpreted as a quadratic random term and need not itself be symmetric.

Rank-`r` singular-value interlacing gives

`s_k(A_0P+L_r)>=s_(k+r)(A_0P)`.                                (3.10)

One quick derivation uses the standard inequality

`s_(k+r)(X)<=s_k(X+Y)+s_(r+1)(Y)`                               (3.11)

with `X=A_0P`, `Y=-L_r`, for which `s_(r+1)(L_r)=0`.

Now add the residual `R_r`. Ordinary singular-value Weyl gives

`s_k(A P)`
` =s_k(A_0P+L_r+R_r)`
` >=s_k(A_0P+L_r)-||R_r||_op`                                  (3.12)
` >=s_(k+r)(A_0P)-s_(r+1)(E P).`                               (3.13)

Taking the positive part and applying (3.6)-(3.7) proves (3.2)-(3.3), and maximizing over `r` proves (3.4). QED.

### Interpretation

The theorem charges the added matrix only through the approximation numbers of its action on the protected **physical** coordinate carrier. It is therefore strictly softer than a hard local-rank hypothesis. If `rank(E P)<=r`, then `s_(r+1)(EP)=0` and the preceding exact local-footprint theorem is recovered. But if `EP` has full rank with a rapidly decaying singular profile, only its tail singular value is paid.

Nothing in the proof rotates the random vector, conditions on dependent spectral coordinates, or treats `X^T E X` as a convolution factor.

## 4. A dense tail is charged only by its carrier action

Let

`A=A_0+E+T`,                                                     (4.1)

where `T=T^T` is arbitrary. Applying Theorem 3.1 to `E+T` and the singular-value perturbation inequality

`s_(r+1)((E+T)P)<=s_(r+1)(EP)+||TP||_op`                       (4.2)

gives

`boxed:`
` sqrt(lambda_k((A^2)[H,H]))`
` >= [sqrt(lambda_(k+r)((A_0^2)[H,H]))`
`     -s_(r+1)(EP)-||TP||_op]_+ .`                             (4.3)

This is stronger than paying the global norm `||T||_op`: the entire outside-outside block of `T` may have arbitrary magnitude, rank, signs and eigenvalues. Only the columns of `T` incident to the carrier are charged.

Again this is a deterministic matrix estimate. There is no assertion that `X^T T X` is a small random variable; such an assertion would be invalid for arbitrary unbounded cap-one input laws.

## 5. Multi-packet reserve allocation

The same argument allows different reserve budgets for different spectral packets.

### Corollary 5.1

Let

`A=A_0+E_1+...+E_J+T`                                         (5.1)

with all full matrices symmetric. Choose integers `r_j>=0` and let

`R=r_1+...+r_J`, `k+R<=m`.                                     (5.2)

Then

`boxed:`
` sqrt(lambda_k((A^2)[H,H]))`
` >= [sqrt(lambda_(k+R)((A_0^2)[H,H]))`
`     -sum_j s_(r_j+1)(E_jP)-||TP||_op]_+ .`                  (5.3)

### Proof

For each `j`, truncate `E_jP=L_j+R_j` with `rank L_j<=r_j` and `||R_j||=s_(r_j+1)(E_jP)`. Then `rank(sum_j L_j)<=R`. Apply rank-`R` interlacing once, followed by operator-norm Weyl to `sum_j R_j+TP`. QED.

This gives an explicit optimization problem: spend reserve dimensions only on those added packets whose large singular directions are expensive; pay the rest through approximation-number tails.

## 6. Literal additional eigenvalues of arbitrary signs and magnitudes

Suppose the added symmetric matrix is written spectrally as

`E=sum_a theta_a v_a v_a^T`,                                   (6.1)

with orthonormal `v_a` and completely arbitrary real `theta_a`. Choose any subset `L` of modes and write

`E=E_L+E_R`.                                                    (6.2)

Put

`r_L=rank(E_LP)`.                                               (6.3)

Because `E_LP` has rank at most `r_L`, Corollary 5.1 gives

`boxed:`
` sqrt(lambda_k((A^2)[H,H]))`
` >= [sqrt(lambda_(k+r_L)((A_0^2)[H,H]))`
`     -||E_RP||_op-||TP||_op]_+ .`                            (6.4)

The remainder admits two simple deterministic bounds:

`||E_RP||_op <= ||E_R||_op = max_(a notin L)|theta_a|`,        (6.5)

and

`||E_RP||_op <= ||E_RP||_F`
` = [sum_(a notin L) theta_a^2 ||P v_a||^2]^(1/2).`             (6.6)

Hence

`||E_RP||_op`
` <= min{ max_(a notin L)|theta_a|,`
`         [sum_(a notin L)theta_a^2||Pv_a||^2]^(1/2) }.`       (6.7)

For the threshold choice

`L={a:|theta_a|>h}`,                                            (6.8)

all eigenvalues larger than `h` may have arbitrary signs and arbitrarily large magnitudes; those amplitudes disappear entirely from the estimate and are charged only by the dimension of their carrier action. Every remaining eigenvalue, however numerous and of either sign, costs at most `h`, with the potentially sharper local-energy alternative in (6.6).

Even the high packet need not have exact low carrier rank: Theorem 3.1 permits choosing any `r` and paying the single soft tail `s_(r+1)(E_{>h}P)`. This is the genuinely new feature relative to the preceding hard-footprint theorem.

## 7. Exact target-class application of the designated partner theorem

We now apply the `fleet02/B12` theorem at an actual final-matrix inequality. The example is deliberately chosen so that the added operator is generally **full rank on the carrier** and does not commute with the baseline; the previous exact-rank compiler does not obtain the six-mode conclusion with the same reserve budget.

Let `H={1,...,8}` be eight ORIGINAL coordinates. On `H` set

`A_0[H,H]`
` =diag(2,9/4,5/2,11/4,3,13/4,7/2,15/4)`,                     (7.1)

and take `A_0` zero outside `H` for definiteness. Thus

`s_8(A_0P_H)=2`,                                                (7.2)

or equivalently

`lambda_8((A_0^2)[H,H])=4`.                                   (7.3)

Define the orthonormal vectors

`u_1=(e_1+e_2)/sqrt(2)`,
`u_2=(e_3+e_4)/sqrt(2)`,                                       (7.4)

and fix

`epsilon=1/8`.                                                  (7.5)

For arbitrary amplitudes

`tau_1,tau_2 in R`                                              (7.6)

of completely unrestricted sign and magnitude, define the spectral addition

`E_tau`
` =epsilon P_H`
`  +(tau_1-epsilon)u_1u_1^T`
`  +(tau_2-epsilon)u_2u_2^T`.                                  (7.7)

On the eight-dimensional carrier its eigenvalues are

`tau_1, tau_2, epsilon, epsilon, epsilon, epsilon, epsilon, epsilon`.  (7.8)

Therefore, regardless of `tau_1,tau_2`,

`boxed: s_3(E_tau P_H)=epsilon=1/8.`                            (7.9)

When `tau_1 tau_2 !=0`, `E_tauP_H` is full rank. Moreover `E_tau` generally does **not** commute with `A_0`: each `u_j u_j^T` mixes two unequal diagonal entries of `A_0`. Thus this is not the commuting replacement branch and not an exact low-rank carrier action.

Now let `T=T^T` be any further matrix satisfying only the local condition

`||T P_H||_op<=1/8`.                                           (7.10)

There is **no bound at all** on `T[H^c,H^c]`: outside the carrier it may have arbitrary rank, signs and eigenvalue magnitudes. Set

`A=A_0+E_tau+T`.                                                (7.11)

Apply (4.3) with

`k=6`, `r=2`.                                                   (7.12)

Using (7.2), (7.9), and (7.10),

`sqrt(lambda_6((A^2)[H,H]))`
` =s_6(A P_H)`
` >=s_8(A_0P_H)-s_3(E_tauP_H)-||TP_H||`                       (7.13)
` >=2-1/8-1/8`
` =7/4.`                                                        (7.14)

Hence the actual final matrix obeys

`boxed: lambda_6((A^2)[H,H])>=49/16.`                          (7.15)

This is exactly the hypothesis (2.1) of the designated partner theorem with

`m=8`, `g=7/4`.                                                 (7.16)

For `m=8`, `N_2=28`, the four constants in (2.3) are

`8N_2 sqrt(6 pi m)                  =2750.7021909601613...`,
`4 pi N_2                           =351.8583772020568...`,
`3*400^(1/3)*(4N_2)^(5/6)           =1127.6031248207917...`,
`10 sqrt(2e/3)                      =13.4617528042947...`.      (7.17)

Therefore

`C_8=2750.7021909601613...`,                                   (7.18)

and the partner theorem gives the actual density inequality

`boxed:`
` ||p_(X^T A X)||_infinity`
` <= C_8/(7/4)`
` =1571.8298234058063... <1572.`                                (7.19)

This is uniform in dimension, in both arbitrary signed amplitudes `tau_1,tau_2`, in every symmetric `T` satisfying only (7.10), and in every independent cap-one input law.

### Verification of the owner's three-large-eigenvalue hypothesis

Since `P_H` is a contraction on the right,

`s_j(A P_H)<=s_j(A)`                                            (7.20)

for every `j`. Combining with (7.14),

`s_6(A)>=s_6(A P_H)>=7/4`.                                     (7.21)

In particular

`boxed: s_3(A)>=7/4>1.`                                        (7.22)

Thus every member of this family is literally in the exact owner target class. The verification does not rely on spectator eigenvalues or on diagonalizing the input law.

## 8. Comparison with earlier B12 mechanisms

The new theorem subsumes several earlier safe stability patterns at the carrier level:

1. **Exact local footprint:** if `rank(EP)<=r`, the tail `s_(r+1)(EP)` vanishes.
2. **Dense small tail:** choosing `r=0` gives ordinary local operator-norm stability.
3. **Large/small spectral threshold:** high modes spend carrier rank; small modes cost at most their threshold.
4. **Approximately low-rank high spectrum:** unlike the prior hard-footprint theorem, high modes may have full carrier rank; only `s_(r+1)(E_{>h}P)` is paid after spending `r` reserve directions.
5. **Outside spectrum:** arbitrary additions acting only in `H^c` have `EP=0` and are exactly free, regardless of norm and sign.

The theorem is not a probabilistic convolution statement. It works because the final receiver sees the actual original-coordinate square carrier `(A^2)[H,H]`, and singular values of `AP_H` can be compared deterministically before any random-law argument is invoked.

## 9. Exact remaining gap

This run does **not** prove the unrestricted conjecture. Bare `s_3(A)>=1` supplies three large global singular directions, whereas the partner compiler used here requires a six-mode square carrier on some finite original-coordinate set. The live programme contains exact families showing that one cannot simply assert a uniformly good small principal block or a rank-three cross cut from the spectral hypothesis.

The remaining full-target implication is therefore still a product-preserving structural dichotomy. One must prove that every `A` with `s_3(A)>=1` either:

- admits an original-coordinate carrier `H` and reserve budget `r` for which the baseline carrier profile dominates the local approximation number of the additional spectrum as in (3.2), **or**
- satisfies one of the already-paid ridge, grouped-bank/hub, projected-crossing, physical-core/pair, rank-two-half-Riesz, or Schur certificates.

The theorem proved here makes the first alternative strictly more flexible by replacing exact local low rank with a quantitative singular-tail condition. It does not prove that one of those alternatives must occur.

Full target status: **OPEN**. Full-target continuity status: **OPEN**. The concrete family in Section 7 has an essentially bounded density by the partner hybrid; continuity is not asserted from that theorem as a whole.

## 10. Corrections and integrity checks

The proof uses none of the refuted interfaces in the live correction inbox: no uniform pointwise quadratic-phase decay, no arbitrary-joint coarea cap, no conditional projection-density positive moment, no independence after rotation, no fiberwise density supremum, no uniformly good small principal block, and no Monte Carlo inference.

Changed-file allowlist for this mathematical repository run is confined to this run directory. The content contains only pure mathematical statements and public/internal repository source pins; no credentials, personal data, financial material, signed URLs, or unrelated private data are present. No repository visibility, permissions, workflow, scheduler, email, notification, or task state was modified.

## 11. Sources consumed


Designated partner theorem actually applied at (7.19):

`yspennstate/math-open-problems@c635fcdce6aa206c68f1f14e061cf617d72376fb`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/fleet02-B12-20260923T185321Z-r11/REPORT.md`.

Execution state: `WITHOUT_VERIFIED_BRAIN`; repository retrieval and publication are not treated as native learned-memory ingestion.
