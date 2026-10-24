SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-23T18:39:59Z.
attacking: heavy-row peeling for the transverse k=1 three-frame: either a bounded-size localized physical core or a conditioning-safe diffuse remainder to which account02/B08 r28 applies.

# account01/B08 r33 — conditioning-safe heavy-set peeling of the transverse three-frame

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** diffuse eigenvector case  
**Designated partner:** `account02/B08`  
**Classification:** `PROVED SUPPORTING GEOMETRIC/CONDITIONAL ROUTER + DESIGNATED PARTNER APPLIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The unrestricted owner target remains **OPEN**. This run does not claim a universal proof. It proves a deterministic/product-preserving peeling lemma that removes the pointwise leverage hypothesis from the completed transverse `k=1` partner theorem at the cost of an explicit bounded-cardinality localization alternative. The paid branch has a continuous `C_0` density; the localized branch is structural only.

No moment, support, iid, Gaussian, log-concavity, connected-support, or post-rotation independence assumption is used.

## 1. Exact source-pinned premises

### 1.1 Current control

Fresh control was read on `yspennstate/math-research-brain@f2268894a29f0e4796d88319211c4ae227f58dd1`. `scheduled_tasks/README.md` has OWNER CONTROL revision `2026-09-22.15`, keeps QFORM as the sole mathematical target, and has no pause for account01/B08. The current owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` asks every real invocation to sign in briefly and then publish substantive mathematics. The current release checkpoint explicitly keeps the unrestricted rough-input QFORM problem open.

### 1.2 Completed designated-partner theorem

I use the completed account02/B08 result

`yspennstate/math-open-problems@66582bd87d50634f3525a57c87acffdbde97aea1`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T153836Z-account02-B08-qform-r28/REPORT.md`.

Its theorem `QFORM-K1-MACROSCOPIC-3FRAME-HALFCUT-v1` has the following relevant scope. On original-coordinate banks `I,J`, let

`C0=lambda r r^T + U H U^T + D`,
`B0=U Sigma V^T`,

where `U,V` have two orthonormal columns, `D` is diagonal in the original coordinates, `H` is arbitrary symmetric `2 x 2`,

`|lambda| >= c L`, `s_2(Sigma) >= beta L`,

and with

`d = dist(r,range(U)) >0`,
`q=(I-UU^T)r/d`,
`W=[q,U]`,
`nu=max_i ||W_i||^2`.

If `nu<=1/48`, and the actual blocks are `C=C0+E_C`, `B=B0+E_B`, then with

`kappa(c,beta,d) = c beta d^2 / [2 sqrt(c^2 d^2 + 4 beta^2)]`,

its proof gives a continuous `C_0` density bound

`||p_Q||_infinity < 23/[kappa(c,beta,d)L]`

provided

`sqrt(||E_C||op^2+||E_B||op^2) <= kappa(c,beta,d)L/16`.

The theorem applies to the full ambient form, retains arbitrary outside couplings and same-bank phases allowed by its source, and permits conditioning-generated affine terms.

For the source-exact `k=1` gate constants I use

`c=sqrt(3/20)=0.3872983346207417...`,
`beta=(3/16)sqrt(3/5)=0.1452368754827781...`.

The stronger B08 energy ledger cross scale `3/sqrt(40)` can improve the numerical constant slightly, but is not needed for the theorem below.

## 2. New geometric lemma: peel all heavy physical rows at once

Let `W` be an `m x 3` matrix with orthonormal columns. For a parameter `g in (0,1)`, define

`tau=g/48`,
`H_g={i: ||W_i||^2>tau}`, `T=I\H_g`,
`G=W_T^T W_T`.

### Lemma 2.1 — `QFORM-3FRAME-HEAVY-PEEL-v1`

Exactly one of the following alternatives holds.

**Localized alternative.**

There is a unit vector `z in R^3` such that

`||W_{H_g} z||^2 > 1-g`,

and

`|H_g| < 144/g`.

Thus an actual direction of the physical three-frame puts more than `1-g` of its squared mass on fewer than `144/g` original coordinates.

**Diffuse-after-conditioning alternative.**

`G>=g I_3`. After conditioning the original coordinates in `H_g`, the orthogonal projector onto the restricted frame `range(W_T)` has every physical diagonal at most `1/48`:

`max_{i in T} (P_{range(W_T)})_{ii} <=1/48`.

#### Proof

Since `W^T W=I_3`,

`sum_i ||W_i||^2=3`.

Every `i in H_g` contributes strictly more than `g/48`, hence

`|H_g| (g/48)<3`,

so

`|H_g|<144/g`.                                                   (2.1)

Also

`W_{H_g}^T W_{H_g}=I_3-G`.                                      (2.2)

If `lambda_min(G)<g`, then

`lambda_max(I-G)>1-g`,

so a unit top eigenvector `z` satisfies

`||W_{H_g}z||^2=z^T(I-G)z>1-g`,

which is the localized alternative.

Otherwise `G>=g I_3`. The projector onto `range(W_T)` is

`P_T=W_T G^{-1}W_T^T`.

For every `i in T`, by definition `||W_i||^2<=g/48`, hence

`(P_T)_{ii}=W_i G^{-1} W_i^T
 <= ||W_i||^2/g
 <=1/48`.                                                        (2.3)

This proves the second alternative. QED.

The point is that the conditioning set is finite with a bound independent of dimension and of the input laws. Conditioning is on ORIGINAL independent coordinates, so the remaining coordinates stay independent and cap-one; only affine terms are generated.

## 3. Restricted child/cross geometry survives the peel quantitatively

Return to the partner setup. Thus

`r=Ua+dq`, `||a||^2+d^2=1`, `W=[q,U]`,

with `W^T W=I_3`. Assume the diffuse-after-conditioning alternative of Lemma 2.1, so

`G=W_T^T W_T>=g I_3`.                                            (3.1)

Write `G_U=U_T^T U_T`. Since it is a principal compression of `G`,

`G_U>=g I_2`.                                                     (3.2)

### Lemma 3.1 — exact degradation factors

After restricting to `T`:

1. `||r_T||^2>=g`;
2. `dist(r_T,range(U_T))>=d sqrt(g)`;
3. after normalizing `r_T`, its sine-angle from `range(U_T)` is at least `d sqrt(g)`;
4. after orthonormalizing the cross frame by

   `U_tilde=U_T G_U^{-1/2}`,

   the cross coefficient has

   `s_2(G_U^{1/2} Sigma)>=sqrt(g) s_2(Sigma)`;
5. the augmented orthonormal three-frame spanning `range(W_T)` has physical leverage at most `1/48`.

#### Proof

Let `z=(d,a_1,a_2)^T`, so `||z||=1` and `r_T=W_T z`. Then (3.1) gives

`||r_T||^2=z^T G z>=g`.                                          (3.3)

For the transverse distance, write `G` in the coefficient split `q | U`. The squared distance from `q_T` to `range(U_T)` is the Schur complement

`s = q_T^T q_T-q_T^T U_T G_U^{-1}U_T^T q_T
   = 1/(G^{-1})_{qq}`.                                           (3.4)

Because `G>=gI`, one has `G^{-1}<=g^{-1}I`, hence

`s>=g`.                                                           (3.5)

Since `r_T=U_T a+d q_T`,

`dist(r_T,range(U_T))=d sqrt(s)>=d sqrt(g)`.                      (3.6)

Also restriction can only decrease norm, so `||r_T||<=1`. Therefore the sine-angle of `r_T/||r_T||` from `range(U_T)` is at least `d sqrt(g)`.

Equation (3.2) gives

`s_2(G_U^{1/2}Sigma)>=s_2(G_U^{1/2})s_2(Sigma)
 >=sqrt(g)s_2(Sigma)`.                                           (3.7)

Finally item 5 is exactly (2.3). QED.

## 4. Main theorem: transverse branch is either finitely localized or paid

### Theorem 4.1 — `QFORM-K1-TRANSVERSE-HEAVY-PEEL-v1`

Assume the source-exact partner setup on original-coordinate banks `I,J`:

`C0=lambda r r^T+UHU^T+D`,
`B0=U Sigma V^T`,
`C=C0+E_C`, `B=B0+E_B`,

with `D` original-coordinate diagonal, `H` arbitrary symmetric, `U,V` orthonormal two-frames,

`|lambda|>=cL`, `s_2(Sigma)>=beta L`,
`d=dist(r,range(U))>=d0>0`.

Fix `g in (0,1)` and form the heavy set from `W=[q,U]` at threshold `g/48`.

Then either

`boxed: exists unit z in R^3 with ||W_{H_g}z||^2>1-g and |H_g|<144/g`,       (4.1)

or, if

`sqrt(||E_C||op^2+||E_B||op^2) <= kappa_g L/16`,                (4.2)

where

`boxed:
 kappa_g = c beta d0^2 g^2 /
           [2 sqrt(c^2 d0^2 g^2+4 beta^2)],
`                                                                    (4.3)

the full ambient quadratic form has a continuous `C_0` density satisfying

`boxed: ||p_Q||_infinity <23/(kappa_g L).`                       (4.4)

#### Proof

If (4.1) holds we are done. Otherwise Lemma 2.1 gives `G>=gI` and permits conditioning on the original coordinates in `H_g` while retaining a cap-one product law on the remaining coordinates.

On every conditioned fiber, the restricted structured blocks retain the same algebraic form. Namely

`lambda r_T r_T^T
 = [lambda ||r_T||^2] r_hat r_hat^T`,

where `r_hat=r_T/||r_T||`; and

`U_T H U_T^T
 = U_tilde [G_U^{1/2} H G_U^{1/2}] U_tilde^T`,

while

`B0[T,J]
 =U_tilde [G_U^{1/2}Sigma] V^T`.                                (4.5)

The diagonal term remains diagonal after restriction. The coefficient-matrix errors can only decrease under taking subblocks:

`||E_C[T,T]||op<=||E_C||op`,
`||E_B[T,J]||op<=||E_B||op`.                                    (4.6)

By Lemma 3.1, the normalized restricted partner parameters satisfy

`c_restricted >= c g`,
`beta_restricted >= beta sqrt(g)`,
`d_restricted >= d0 sqrt(g)`,
`nu_restricted <=1/48`.                                          (4.7)

Substituting the lower bounds (4.7) into the partner formula gives

`kappa(cg,beta sqrt(g),d0 sqrt(g))`
` = [c beta d0^2 g^2]/[2 sqrt(c^2 d0^2 g^2+4 beta^2)]`
` =kappa_g`.                                                      (4.8)

Thus assumption (4.2) verifies the partner theorem on **every** conditioned fiber, with the same uniform bound (4.4), regardless of the values of the conditioned variables. The conditioning-generated terms are affine and are allowed by the partner receiver.

Averaging the conditional densities preserves the same `L^infinity` bound. Since each conditional representative is continuous and tends to zero at infinity and all are bounded by the same constant `23/(kappa_gL)`, dominated convergence in the probability law of `X_{H_g}` gives a continuous `C_0` representative for the unconditional density. QED.

This argument uses no moments: the conditioned coordinates may be arbitrarily large because their values only enter affine parameters in a theorem that is uniform in those affine terms.

## 5. Clean numerical specialization

Take the partner's source-exact gate constants

`c=sqrt(3/20)`,
`beta=(3/16)sqrt(3/5)`,

take the transverse threshold

`d0=1/2`,

and choose

`g=1/2`.

Then

`H={i: ||W_i||^2>1/96}`,
`|H|<288`,

so in the localized alternative one may say `|H|<=287`, and some unit three-frame direction has more than half of its squared mass on those at most 287 original coordinates.

The constant (4.3) simplifies exactly. Since

`c beta=9/160`,
`c^2 d0^2 g^2=3/320`,
`4 beta^2=27/320`,

one obtains

`boxed: kappa_g=9/(640 sqrt(6))
 =0.005740991584648075...`.                                      (5.1)

Therefore

`boxed:
 sqrt(||E_C||op^2+||E_B||op^2)
 <= 9/[10240 sqrt(6)] L
 =0.0003588119740405047... L
`                                                                    (5.2)

implies, unless the bounded-cardinality localization alternative occurs,

`boxed:
 ||p_Q||_infinity
 < (14720 sqrt(6)/9) L^{-1}
 =4006.276557085... L^{-1},
`                                                                    (5.3)

with a continuous `C_0` density.

Using the stronger B08 r30 cross scale `beta=3/sqrt(40)` in the same proved partner formula improves (5.1) to

`kappa_g=0.006020262178761896...`,

hence leakage allowance `0.0003762663861726185...L` and density constant `<3820.432/L`. I keep (5.2)-(5.3) as the source-exact partner specialization.

## 6. What this changes in the B08 proof tree

The preceding B08/partner transverse branch had a hard split at

`max_i ||W_i||^2 <=1/48`.

The present theorem removes that pointwise diffuseness hypothesis as an endpoint. Under the same transverse geometry and sufficiently small child/cross leakage, **every state now does one of two things**:

1. it is paid by a uniform continuous density estimate after conditioning a finite set of original coordinates; or
2. it supplies a quantitative localized-core certificate: a direction in the actual child-plus-cross three-frame has `>1/2` of its mass on at most 287 original coordinates.

This is a genuine diffuse/localized compiler. It is conditioning-safe because the finite set is chosen from original coordinates, not from rotated spectral coordinates.

The theorem also explains exactly what still has to be done. A bounded set of 287 coordinates is not yet a uniformly conditioned three-coordinate principal block, and it does not by itself provide a scalar pivot or a rank-three cross block. Thus the next missing implication is

`QFORM-TRANSVERSE-287CORE-LOCALIZED-RECEIVER-v1`:

> Starting from a transverse `k=1` three-frame direction carrying more than half of its mass on at most 287 original coordinates, either extract a source-valid localized density receiver with a universal constant or route to another already-paid physical cross/pivot configuration, while retaining arbitrary complementary spectrum and conditioning-generated affine terms.

Separately, if the child/cross leakage exceeds (5.2), this run makes no density claim; that is the large-leakage/next-direction branch already explicit in the B08 tree.

## 7. Sanity check

A deterministic-seed numerical check was run only to test the finite-dimensional linear-algebra inequalities, not the probability theorem. It generated random orthonormal three-frames, formed `H` at threshold `1/96`, and checked:

- if `lambda_min(G)<1/2`, then `lambda_max(W_H^T W_H)>1/2`;
- if `G>=I/2`, then every whitened restricted row leverage is at most `1/48`;
- for random `d>=1/2`, the restricted transverse distance is at least `d/sqrt(2)`;
- `||r_T||^2>=1/2` on the diffuse-after-conditioning branch.

Across 1500 random frames with dimensions 300, 500 and 1000, there were zero violations; 504 instances took the localization branch and 996 the diffuse-after-conditioning branch. The smallest observed localization margin was `3.861018805840777e-4`; the largest observed restricted leverage was `0.019947764629434088<1/48`; the smallest observed transverse-distance ratio to the proved lower bound was `1.0341648651851392`. This computation is a sanity check only; the proof is Sections 2-4.

## 8. Status

- Full universal QFORM theorem: **OPEN**.
- Full universal continuity: **OPEN**.
- The paid branch of Theorem 4.1: continuous `C_0` density proved.
- The localized alternative (4.1): structural certificate only; no density conclusion claimed there.
- No correction in the current live inbox used as a premise contradicts this argument; a final correction refresh is required immediately before publication.
- Repository transport is not native learned-memory ingestion: execution remains `WITHOUT_VERIFIED_BRAIN`.
