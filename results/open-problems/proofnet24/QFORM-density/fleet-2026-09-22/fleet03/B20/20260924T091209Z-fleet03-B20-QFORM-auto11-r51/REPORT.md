SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B20, 2026-09-24T09:12:09Z.
attacking: the fleet04/B20 r13 strong-edge punctured-rank-two survivor; pass to the exact physical-pair Schur complement and prove that every still-unpaid survivor is an ultra-thin additive rank-six carrier with the nonzero tail retained.

# fleet03/B20 r51 — strong-edge Schur compression to rank six with an ultra-thin retained tail

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW TARGET-RELEVANT STRUCTURAL CLOSURE / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Authenticated repository access/writeback is not native learned-memory ingestion.

Regularity: the paid branches below give an essentially bounded density. Continuity is not proved by these pair-log/random-slope branches. Full-target continuity remains **OPEN**.

Every coordinate set below is a literal ORIGINAL-coordinate set. No random variable is rotated. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, arbitrary-joint coarea, fiber-supremum, or law-uniform pointwise quadratic-phase decay hypothesis is introduced. No nonzero coefficient tail is deleted.

## 1. Source-pinned live inputs


The designated partner is fleet04/B20 r13:

`yspennstate/math-open-problems@d2560a041fd91c05d7fddf50f5b5414ecd2680a2`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260924T051424Z-fleet04-B20-QFORM-r13/REPORT.md`.

On its localized child-window strong-edge leaf, after the scalar-pivot exit has failed, there are literal original coordinates `i,j` with

`|A_ij| >= 1/1024`, `|A_jj| < a_0`,

where

`a_0=4.2146684313588616e-8`.

The already-paid large-diagonal branch lets the current unpaid chamber assume `|A_ii|<=1/64`. Fleet03/B20 r48 then proved that the physical pair

`P=A[{i,j},{i,j}]`

is invertible and indefinite, with

`D:=|det P|>=D_0=9.530157744638501e-7`,

`kappa:=s_min(P)>=kappa_0=6.075614261408114e-5`.

Source:

`yspennstate/math-open-problems@67a9144806e9371e3ecb9b93d29e9aff915cb9f3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260924T054542Z-fleet03-B20-QFORM-auto11-r48/REPORT.md`.

The completed pair+third-cross receiver used there actually works at every positive threshold `sigma`: if, after deleting the pair, a literal disjoint cross block has `s_3>=sigma`, then

`||p_Q||_infinity <= C_pc D^(-1/3) kappa^(-1/6) sigma^(-1/6)`,

with `C_pc=35.72978950364268...`.

The second analytic input is the pair-log theorem

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

Its general form says that, after completing a fixed indefinite physical pair, if the scalar Schur remainder `R` satisfies

`sup_t P(|R-t|<rho) <= H sqrt(rho)`,

then

`||p_Q||_infinity <= 4 sqrt(2H) (D kappa)^(-1/4)`.

The transition-stable random-slope theorem and the quantitative near-null identities are recorded in fleet03/B06 r55:

`yspennstate/math-open-problems@3f8fe4c0920f41353374c50693ccdc741e245008`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260924T082141Z-fleet03-B06-qform-r55/REPORT.md`.

Finally, the two-part MSS frame partition with lower Gram constant

`delta=1-(1/sqrt(2)+sqrt(epsilon))^2`

was already used source-validly in fleet03/B20 r50.

## 2. Exact Schur coordinates for the strong pair

Put the strong physical pair first and write the full coefficient matrix as

`A=[[P,M],[M^T,C]]`,

where `P` is the `2 x 2` indefinite pair and the tail bank is the complement of `{i,j}`. Define its exact Schur complement

`S=C-M^T P^(-1) M`.                                               (2.1)

For a literal tail coordinate `k`, isolate it from the other tail coordinates. In the notation of the B06 pair-pivot compiler,

`s_k = S_kk`,

`m_k = S[k,T\{k}]`.                                               (2.2)

Indeed, if `r=M e_k`, `a=C_kk`, and `h` is the physical `k`-to-other-tail row, then

`s_k=a-r^T P^(-1)r`,

`m_k=h-M_rest^T P^(-1)r`.

Thus the entire family of third-coordinate pair-pivot currencies is exactly the diagonal and off-diagonal row geometry of one symmetric matrix `S`. This observation lets the local B06 transition theorem be aggregated without any dimension-dependent union bound.

## 3. A small extension of the pair-log square branch

The B06 report stated its scalar-square branch after setting `m=0`, but its proof is actually uniform in the post-pair star. The needed extension is elementary and is recorded here because it is used below.

### Lemma 3.1 — `QFORM-PAIRLOG-SCHUR-SQUARE-ARBITRARY-STAR-v1`

After completing an invertible indefinite physical pair, suppose the remainder can be written

`R=s X^2+2X(m^T Y+beta)+R_0(Y)`,

where `X` and the coordinates of `Y` are original independent coordinates with density caps one, and `s!=0`. Then

`sup_t P(|R-t|<rho) <= 2 sqrt(2) |s|^(-1/2) rho^(1/2)`             (3.1)

for every `rho>0`, with no restriction on `m`, `beta`, or `R_0`. Consequently

`boxed: ||p_Q||_infinity <= 2^(13/4) [D kappa |s|]^(-1/4).`       (3.2)

#### Proof

Condition on all original coordinates in `Y`. The conditional polynomial in the single original coordinate `X` has the form

`sX^2+bX+c`.

Completing its scalar square shows that the inverse image of any output interval of radius `rho` has total Lebesgue length at most

`2 sqrt(2 rho/|s|)`.

The density cap on `X` gives the same conditional probability bound, uniformly in the conditioned value of `Y`; averaging proves (3.1). Insert

`H=2 sqrt(2)|s|^(-1/2)`

into the general pair-log estimate. QED.

This does not invoke a conditional projection-density moment and does not discard the star `m`.

## 4. A universal microscopic gate

Fix once and for all

`tau=2^-20=9.5367431640625e-7`,                                  (4.1)

`nu=tau/18=5.2981906467013886e-8`.                               (4.2)

There are now three terminal exits from the partner strong-edge leaf.

### 4.1 A disjoint post-puncture third cross singular

If there are disjoint literal tail sets `L,R` with

`s_3(C[L,R])>=nu`,                                                (4.3)

then fleet03/B20 r47 applied to the partner pair gives

`||p_Q||_infinity`
` <= C_pc D_0^(-1/3) kappa_0^(-1/6) nu^(-1/6)`
` =298797.848139... <298800.`                                    (4.4)

Thus every survivor of this exit satisfies

`boxed: s_3(C[L,R])<nu for every disjoint tail L,R.`              (4.5)

### 4.2 A Schur diagonal currency

If some tail coordinate satisfies

`|S_kk|>=tau`,                                                    (4.6)

Lemma 3.1 and the pair constants give

`||p_Q||_infinity`
` <=2^(13/4)(D_0 kappa_0 tau)^(-1/4)`
` =110363.354831... <110364.`                                    (4.7)

### 4.3 A Schur off-diagonal row currency

If some tail coordinate satisfies

`||S[k,T\{k}]||_2>=tau`,                                         (4.8)

apply the transition-stable random-slope theorem from B06 r55. It gives

`||p_Q||_infinity`
` <12.714 D_0^(-1/3) kappa_0^(-1/6) tau^(-1/6)`
` =65677.578286... <65678.`                                      (4.9)

Therefore, if none of (4.3), (4.6), (4.8) pays, then every literal Schur column obeys the dimension-free bound

`boxed: ||S e_k||_2 < sqrt(2) tau.`                              (4.10)

No summation over coordinates is used.

## 5. The first new closure: the Schur complement has only four macroscopic singular modes

### Theorem 5.1 — `QFORM-R13-SCHUR-RANK4-ULTRATHIN-v1`

Under the unpaid alternatives (4.5) and (4.10),

`boxed: s_5(S)<36 tau=9/262144=3.4332275390625e-5.`               (5.1)

#### Proof

Assume instead that `s_5(S)>=36 tau`. Put

`t_0=9 tau`                                                       (5.2)

and let

`Pi=1_{|S|>=t_0}`

be the coefficient-space spectral projection. By (4.10), for every physical tail coordinate `k`,

`(Pi)_kk <= ||S e_k||_2^2/t_0^2`
`         < 2 tau^2/(81 tau^2)=2/81=:epsilon.`                  (5.3)

Let `U` be an orthonormal frame for `range(Pi)`. The two-part MSS frame partition gives a literal original-coordinate partition of the tail

`T=I disjoint_union J`

such that

`U_I^T U_I >= delta I`, `U_J^T U_J >= delta I`,                  (5.4)

with

`delta=1-(1/sqrt(2)+sqrt(2/81))^2`
`     =1-(11 sqrt(2)/18)^2`
`     =41/162.`                                                   (5.5)

Write

`S_H=Pi S Pi`, `F=S-S_H`.

Then `||F||op<t_0=9 tau`. Thin QR on `U_I,U_J` and the singular-value product inequality give

`s_5(S_H[I,J]) >= delta s_5(S) >= (41/162)(36 tau)=82 tau/9.`    (5.6)

Restriction cannot increase operator norm, so Weyl gives

`s_5(S[I,J]) > 82 tau/9-9 tau = tau/9.`                          (5.7)

On the other hand, from (2.1),

`S[I,J]=C[I,J]-M_I^T P^(-1) M_J`,                                (5.8)

and the second term has rank at most two. The rank-two perturbation inequality therefore gives

`s_5(S[I,J]) <= s_3(C[I,J]) < nu=tau/18`,                        (5.9)

contradicting (5.7). Hence (5.1) holds. QED.

The constants were deliberately selected so the gap is exact:

`tau/9 > tau/18`.

The proof uses the aggregate fifth singular value; it does not choose one minor from an aggregate sum.

## 6. Additive rank-six compression of the FULL coefficient matrix

Let `S_4` be the symmetric top-four singular/eigenmode truncation of `S`, and put

`R=S-S_4`.

Theorem 5.1 gives

`rank(S_4)<=4`,

`||R||op=s_5(S)<36 tau=9/262144.`                                (6.1)

Moreover the spectral pieces are orthogonal in each physical column, so

`||R e_k||_2 <= ||S e_k||_2 < sqrt(2) tau`                       (6.2)

for every tail coordinate `k`.

Now define the exact pair-shear carrier

`K_P=[[P,M],[M^T,M^T P^(-1)M]]`.

If

`L=[I_2, P^(-1)M]`,

then

`K_P=L^T P L`,                                                    (6.3)

so

`rank(K_P)<=2`.                                                   (6.4)

Using `C=M^T P^(-1)M+S`, the original matrix decomposes **exactly** as

`A=K_6+R_tilde`,                                                  (6.5)

where

`K_6=K_P+diag(0,S_4)`,

`R_tilde=diag(0,R)`.

Therefore

`boxed: rank(K_6)<=6,`                                           (6.6)

`boxed: ||R_tilde||op<9/262144=3.4332275390625e-5,`              (6.7)

and every physical column of the retained tail satisfies

`boxed: ||R_tilde e_k||_2 < sqrt(2) 2^-20`
`       =1.3486991523486091e-6`                                  (6.8)

(with zero columns on the two pair coordinates).

Because the full target hypothesis is `s_3(A)>=1`, singular-value Lipschitz continuity under operator perturbations gives

`boxed: s_3(K_6)>1-9/262144`
`       =0.999965667724609375.`                                  (6.9)

Thus the designated partner's strong-edge survivor is no longer merely a punctured-rank-two cross system. It is either paid with the full-law essential-density bound

`boxed: ||p_Q||_infinity<300000,`                                (6.10)

or the **entire physical coefficient matrix** is an ultra-thin retained perturbation of a rank-at-most-six symmetric carrier whose third singular value is within `3.44e-5` of the target scale.

The tail `R_tilde` remains inside the quadratic form. No probabilistic smallness is inferred from (6.7)-(6.8).

## 7. Designated fleet04/B20 result applied at an actual inequality

This run uses fleet04/B20 r13 at its literal strong-anchor edge

`|A_ij|>=beta_0/sqrt(2)=1/1024`.

Together with the already-live all-small-diagonal gate and the partner's failed child pivot `|A_jj|<a_0`, this is exactly the hypothesis that supplies the quantitative indefinite pair `(D_0,kappa_0)`. The new Schur argument then spends that actual pair three times: at the disjoint third-cross receiver (4.4), at the pair-log square inequality (4.7), and at the random-slope star inequality (4.9). The survivor is the rank-six statement (6.5)-(6.9).

This is not an application of the partner theorem to a projected joint-density surrogate; all conditioning and Schur completion keep the original product coordinates.

## 8. Relation to the freshest global r52 route

The freshest fleet03/B19 route still has the separate retained-residual endpoint from r52, and fleet03/B20 r50 narrowed that branch to a rank-at-most-12 carrier (rank at most 11 on determinant collapse) plus a much larger retained operator tail. The present theorem does **not** claim that every r52 state contains the r13 strong-edge geometry.

What it does close is one live physical-hub exit that feeds that global proof graph: whenever the r13 strong edge is reached, its former punctured-rank-two debt is replaced by the far sharper finite-dimensional normal form (6.5).

The first remaining implication on this branch is now

`QFORM-R13-ULTRATHIN-R6-CARRIER-RETAINED-TAIL-ENDPOINT-v1`:

> pay a rank-at-most-six symmetric physical carrier with `s_3>0.9999656` in the presence of the retained tail `||R||op<3.44e-5`, `max_j||Re_j||<1.35e-6`, or force a completed physical-pair / physical-E3 / hub+square / ridge-window receiver. The retained tail may not be discarded.

The separate global r52 low-residual rank-12/rank-11 endpoint remains open.

## 9. Quantifier and correction boundaries

All signs are allowed; the selected pair is proved indefinite rather than assumed. Repeated eigenvalues are harmless. Every physical partition is in original coordinates. Coefficient-space spectral projections are used only to prove deterministic matrix inequalities; no independence is asserted after them.

The run does not use the refuted pointwise van-der-Corput claim, arbitrary-joint coarea, projection-density control of an indefinite quadratic pushforward, worst-fiber integration, interval extremality, Monte Carlo proof, or deletion of a small coefficient tail.

Full unrestricted QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.

Full universal continuous-density conclusion: **OPEN**.

New paid strong-edge subbranches: **essentially bounded density, uniform bound `<300000`; continuity not established here**.
