SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T23:37:51Z.
attacking: mu-weighted cancellation to a finite physical center or a genuinely diffuse transverse bank in the exact-rank-two survivor.

# account03/B13 r38 — sharp rank-two DPP disjointness and a 48-center / diffuse-bank compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T233751Z-account03-B13-qform-r38`  
Role: extremal product laws / quantitative geometry  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW PROVED DETERMINISTIC THEOREMS + NEW TARGET-LEVEL STRUCTURAL APPLICATION / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

No Gaussian, log-concavity, moment, compact-support, connected-support, post-rotation independence, single-interval extremality, bounded support diameter, fixed fragment count, or deletion of a coefficient-small quadratic tail is used. The only rotation below is a two-dimensional deterministic coefficient-basis rotation inside a rank-two matrix factorization; it does not rotate the independent random coordinates.

## 1. Source-pinned premises

Final prepublication owner refresh used

`yspennstate/math-research-brain@f828b8110e4a4752425ade69bda5e8da4cd54082`,

OWNER CONTROL revision `2026-09-22.15`, QFORM-only, fleet enabled, no pause on account03/B13. The live correction inbox was reread at that source. In particular, this report does not use the refuted pointwise quadratic-phase decay, arbitrary-joint coarea cap, near-zero half-Riesz shortcut, or deletion of a small matrix tail on rough unbounded inputs.

The designated partner actually applied is account04/B13:

`yspennstate/math-open-problems@d1764f29884bf14ce505d36668105edfcaf8315e`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260923T201653Z-account04-B13-extremal-slab-dichotomy-r1/REPORT.md`.

It proves both:

1. the optimizer-free product-law identity

`sup_{0<=f_i<=1, int f_i=1} int K prod_i f_i
 = sup_{|E_i|=1} int_{prod_i E_i} K`                               (1.1)

for every nonnegative measurable kernel `K`, with bounded finite-union epsilon-witnesses but no attained interval optimizer, uniform support diameter, or fixed fragment count; and

2. in the diffuse exact-rank-two chamber

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i c_i<=1/3`,
`c_i=||u_i||^2`, `s_3(A)>=1`,                                    (1.2)

there is a physical coordinate `k` with `|d_k|>=1` such that every slab ratio

`rho=P{X^T A X in J}/|J|`                                        (1.3)

obeys

`|A_kk det Lambda| <=1536 e^2 rho^(-4)`.                          (1.4)

Put

`H0=sqrt(1536 e^2)=106.53445530886934...`.                        (1.5)

Thus either

`dist_op(U Lambda U^T, SymRank_{<=1})
 <=10.321552950446426 rho^(-1)`,                                  (1.6)

or the non-rank-one branch satisfies

`|det Lambda|>H0 rho^(-2)`, `|A_kk|<=H0 rho^(-2)`.                (1.7)

The grouped three-leaf input is account01/B13:

`yspennstate/math-open-problems@38a8a2ae1cb319211ab4be60f6f8d6f7f03f85f9`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260923T223205Z-account01-B13-qform-auto11/REPORT.md`.

For `L={r,s,t}`, with complement `I`, write

`q_ab=det(u_a,u_b)^2`,
`Delta_L=det(U_I^T U_I)`,
`tau_L=d_r q_st+d_s q_rt+d_t q_rs`.                              (1.8)

Its completed supporting theorem gives

`Delta_L (det Lambda)^2 |tau_L| <= C_T rho^(-5)`,
`C_T=759375/2=379687.5`.                                          (1.9)

My preceding r34/r36 reports are

`math-open-problems@7ebaff80e4d6d1c5c45a561d1ff17a87cfd7a052`
and
`math-open-problems@a558625206539a6eaee5aa6b2c6d851ccd2f1990`.

The present report strictly improves r34's crude `1/512` DPP disjointness floor in the actual rank-two Parseval scope and therefore improves r36's `mu_k` normalization and all ensuing cancellation constants. The older inequalities remain true; they are merely nonsharp.

## 2. Sharp rank-two Parseval DPP disjointness

### Theorem 2.1 — `QFORM-RANK2-DPP-FOURIER-DISJOINTNESS-v1`

Let `W` be a finite real `m x 2` Parseval frame,

`W^T W=I_2`,                                                      (2.1)

with rows `w_i` and leverages

`ell_i=||w_i||^2`.                                                 (2.2)

For `i<j` put

`q_ij=det(w_i,w_j)^2`.                                             (2.3)

Cauchy-Binet gives `sum_{i<j}q_ij=1`, so `q` is a probability law on physical pairs. Let `E,F` be independent `q`-pairs and

`delta=P(E cap F=empty)`.                                          (2.4)

If

`max_i ell_i<=q0<=2/3`,                                           (2.5)

then

`boxed: delta >= 1-2 q0+(3/4)q0^2.`                               (2.6)

In particular,

`boxed: max_i ell_i<=1/2  =>  delta>=3/16.`                        (2.7)

The constant `3/16` is sharp.

#### Proof

For a fixed pair `{i,j}`, the total DPP pair mass on its complement is

`Delta_ij=det(I_2-w_i w_i^T-w_j w_j^T)`
`        =1-ell_i-ell_j+q_ij`.                                    (2.8)

Therefore

`delta=sum_{i<j}q_ij Delta_ij
      =1-sum_i ell_i^2+sum_{i<j}q_ij^2`.                           (2.9)

Write, for nonzero rows,

`w_i=sqrt(ell_i)(cos theta_i, sin theta_i)`.                       (2.10)

Parseval gives

`sum_i ell_i=2`,
`sum_i ell_i exp(2 i theta_i)=0`.                                 (2.11)

Put

`S2=sum_i ell_i^2`,
`A2=sum_i ell_i^2 exp(2 i theta_i)`,
`B2=sum_i ell_i^2 exp(4 i theta_i)`.                              (2.12)

Using

`sin^4 x=(3-4 cos 2x+cos 4x)/8`,                                  (2.13)

a direct expansion over unordered pairs gives the exact identity

`sum_{i<j}q_ij^2
 = (3/16) S2^2 -(1/4)|A2|^2 +(1/16)|B2|^2`.                       (2.14)

Because (2.11) vanishes,

`A2=sum_i ell_i(ell_i-q0) exp(2 i theta_i)`.                       (2.15)

Since `0<=ell_i<=q0`,

`|A2| <= sum_i ell_i(q0-ell_i)=2q0-S2`.                            (2.16)

Also

`S2<=q0 sum_i ell_i=2q0`.                                         (2.17)

Substitute (2.14)-(2.16) in (2.9) and discard the nonnegative `|B2|^2/16` term:

`delta
 >=1-S2+(3/16)S2^2-(1/4)(2q0-S2)^2`.                         (2.18)

For `q0<=1`, the right side is strictly decreasing in `S2>=0`, because its derivative is

`q0-1-S2/8<=0`.                                                    (2.19)

Using `S2<=2q0` therefore gives

`delta >= 1-2q0+(3/4)q0^2`,                                      (2.20)

proving (2.6).

For `q0=1/2`, this is `3/16`. Equality is attained by the four-row Parseval frame

`w_j=2^(-1/2)(cos(j pi/4), sin(j pi/4))`, `j=0,1,2,3`,            (2.21)

for which every leverage is `1/2`, `S2=1`, `A2=B2=0`, and hence `delta=3/16`. QED.

### Why this is materially stronger than r34

The earlier weighted-graph stability argument was valid for arbitrary pair laws and therefore gave only `delta>=1/512` under the same leverage cap. Theorem 2.1 uses the extra Pluecker/Parseval structure of the actual rank-two DPP and improves the floor by a factor `96`:

`3/16 = 96/512`.                                                   (2.22)

No probabilistic input law is involved in Theorem 2.1; it is a deterministic frame theorem.

## 3. The intrinsic `mu_k` normalization improves from `1/1152` to `1/12`

Return to (1.2) and the partner-selected `k`. Put

`Q_k=sum_{r<s; r,s!=k}q_rs=1-c_k`.                                (3.1)

The normalized leave-one-out frame from the completed Schur-DPP construction has pair law

`q'_rs=q_rs/Q_k`.                                                  (3.2)

Its row leverages satisfy

`tilde c_i<=c_i/(1-c_k)<=1/2`                                     (3.3)

because every `c_i,c_k<=1/3`. Hence Theorem 2.1 gives

`delta_k>=3/16`.                                                   (3.4)

For `E={r,s}`, define

`Delta_E=det(U_{[n]\{k,r,s}}^T U_{[n]\{k,r,s}})`.                (3.5)

Exactly as in r36,

`W_k:=sum_E q_E Delta_E=Q_k^2 delta_k`.                            (3.6)

Since `Q_k>=2/3`,

`boxed: W_k>=1/12.`                                                (3.7)

More importantly for normalized averages,

`boxed: Q_k/W_k=1/(Q_k delta_k)<=8.`                               (3.8)

Define the intrinsic physical-pair probability law

`mu_k(E)=q_E Delta_E/W_k`.                                        (3.9)

This is the same law as r36, but with a much stronger exact normalization certificate.

## 4. Improved grouped transverse cancellation

### Theorem 4.1 — `QFORM-DPP-WEIGHTED-TRANSVERSE-L1-SHARPENED-v1`

Under (1.2), for the partner-selected `k`,

`boxed:
 E_{E~mu_k}|tau_E|
 <=3037500 |det Lambda|^(-2) rho^(-5).}`                           (4.1)

#### Proof

For every pair with `q_E Delta_E>0`, apply the grouped three-leaf inequality (1.9) to `L={k,r,s}`:

`Delta_E (det Lambda)^2 |tau_E|<=C_T rho^(-5)`.                   (4.2)

Multiply by `q_E` and sum:

`sum_E q_E Delta_E |tau_E|
 <=C_T |det Lambda|^(-2) rho^(-5) Q_k`.                           (4.3)

Divide by `W_k`. By (3.8),

`E_mu|tau|
 <=8 C_T |det Lambda|^(-2) rho^(-5)`
` =3037500 |det Lambda|^(-2) rho^(-5)`.                           (4.4)

QED.

### Actual equation-level application of account04/B13

Apply the partner dichotomy (1.6)-(1.7). Either the rank-two carrier already satisfies

`dist_op(U Lambda U^T,SymRank_{<=1})
 <=10.321552951 rho^(-1)`,                                       (4.5)

or

`|det Lambda|>106.534455309 rho^(-2)`,
`|A_kk|<=106.534455309 rho^(-2)`.                                 (4.6)

In the second branch, (4.1) becomes

`boxed:
 E_mu|tau_E|
 < [3037500/(1536e^2)] rho^(-1)
 =267.630809135 rho^(-1).}`                                       (4.7)

Consequently

`boxed:
 mu_k{|tau_E|<=535.261618270 rho^(-1)}>=1/2.}`                    (4.8)

This improves r36's `38538.837 rho^-1` mean bound by a factor `144` and its half-mass threshold by the same factor.

The use of account04/B13 here is essential and explicit: its slab inequality supplies the determinant lower bound in the non-rank-one branch that converts the `rho^-5 |det Lambda|^-2` grouped estimate into the `rho^-1` cancellation scale.

## 5. From `mu_k` cancellation to a finite center or a diffuse bank

The r36 four-point theorem required pointwise lower bounds on one `q_ki` packet and one complement determinant. The next theorem removes that selection requirement entirely.

Rotate only the latent coefficient basis so

`u_k=(sqrt(c),0)`, `c=c_k>0`,                                    (5.1)

and write

`u_i=(x_i,y_i)`,
`s_i=y_i^2=q_ki/c`.                                                (5.2)

Because `U^T U=I_2` and `y_k=0`,

`boxed: sum_{i!=k}s_i=1.`                                         (5.3)

### Theorem 5.1 — `QFORM-MU-FINITECENTER-OR-DIFFUSE-BANK-v1`

Assume the non-rank-one branch (4.6). Fix any real `R>=1` and put

`theta=1/(24R)`,
`H_R={i!=k:s_i>=theta}`,
`L_R=([n]\{k})\H_R`.                                              (5.4)

Then `|H_R|<=24R`, and at least one of the following two alternatives holds.

#### A. Finite physical center / intrinsic star

There is a physical `h in H_R` such that

`boxed: mu_k{E:h in E}>=1/(48R).}`                                (5.5)

For the star-conditional law,

`boxed:
 E(|tau_E| | h in E)
 <12846.2788385 R rho^(-1).}`                                     (5.6)

Hence at least half of that star law satisfies

`boxed:
 |tau_E|<25692.5576770 R rho^(-1).}`                              (5.7)

#### B. Genuinely diffuse transverse physical bank

The physical bank `L_R` obeys

`boxed:
 det(U_{L_R}^T U_{L_R})>=1/24,
 sqrt(det(U_{L_R}^T U_{L_R}))>=1/sqrt(24).}`                       (5.8)

Its transverse coefficient energy

`S_R=sum_{i in L_R}s_i`                                           (5.9)

satisfies

`boxed: S_R>=1/24}`,                                               (5.10)

and every physical row has normalized transverse mass

`boxed: s_i/S_R<=1/R, i in L_R.}`                                 (5.11)

Moreover the `mu_k`-conditional pair law inside this bank satisfies

`boxed:
 E(|tau_E| | E subset L_R)
 <535.261618270 rho^(-1),}`                                       (5.12)

and at least half of that conditional law has

`boxed:
 |tau_E|<1070.52323654 rho^(-1).}`                                (5.13)

#### Proof

Equation (5.3) gives immediately

`|H_R| theta<=1`, hence `|H_R|<=24R`.                             (5.14)

Let

`m_R=mu_k{E:E cap H_R != empty}`.                                 (5.15)

If `m_R>=1/2`, then

`sum_{h in H_R}mu_k{E:h in E}
 =E_mu |E cap H_R|
 >=m_R>=1/2`.                                                      (5.16)

Since `|H_R|<=24R`, some `h` has star mass at least `1/(48R)`, proving (5.5). Divide the global mean bound (4.7) by that star mass to get (5.6), and apply Markov at twice the conditional mean to get (5.7).

Assume now `m_R<1/2`. Then

`mu_k{E subset L_R}>1/2`.                                         (5.17)

By definition of `mu_k` and (3.7),

`sum_{E subset L_R} q_E Delta_E
 =W_k mu_k{E subset L_R}
 >W_k/2
 >=1/24`.                                                         (5.18)

Each complement Gram determinant satisfies `0<=Delta_E<=1`; therefore

`sum_{E subset L_R} q_E>=1/24`.                                   (5.19)

Cauchy-Binet identifies the left side exactly as

`det(U_{L_R}^T U_{L_R})`,                                         (5.20)

proving (5.8).

In the coefficient basis (5.1), let

`G_R=U_{L_R}^T U_{L_R}`.                                          (5.21)

Then `(G_R)_{22}=S_R`, while `0<=G_R<=I_2`, hence `(G_R)_{11}<=1`. Thus

`det G_R=(G_R)_{11}(G_R)_{22}-(G_R)_{12}^2<=S_R`.                 (5.22)

Together with (5.8), this proves `S_R>=1/24`. For `i in L_R`, `s_i<theta=1/(24R)<=S_R/R`, proving (5.11).

Finally condition (4.7) on the event `E subset L_R`, whose `mu_k` probability exceeds `1/2`, to get (5.12); Markov gives (5.13). QED.

### Concrete `R=2` form

Taking `R=2` gives a particularly useful quantitative fork:

* either a center of at most **48 original physical coordinates** contains a row `h` with intrinsic star mass at least `1/96`, and the star-conditional mean satisfies

  `E(|tau| | h in E)<25692.557677 rho^-1`,                         (5.23)

  with at least half the star mass below `51385.115354 rho^-1`; or

* the complementary physical bank has

  `sqrt(det(U_L^T U_L))>=1/sqrt(24)=0.2041241452...`,              (5.24)

  and the transverse coefficient direction has physical row marginals at most `1/2`, exactly the diffuseness gate that recurs in the grouped projected-crossing receivers. The bank-conditional mean is below `535.261619 rho^-1`, with half below `1070.523237 rho^-1`.

The theorem does **not** yet identify the transverse coefficient vector with the projected crossing in those receivers while retaining the near-null physical pivot and arbitrary diagonal curvature. That identification is the next analytic glue step; it is not silently assumed here.

## 6. Extremal product-law interpretation

The designated account04/B13 theorem (1.1) means every slab statement above has an exact geometric unit-product-set formulation. A strict cap-one product-law witness can be transferred, with arbitrarily small loss, to bounded finite-union unit-measure sets and the loss sent to zero. Therefore none of (2.6), (4.1), or the finite-center/diffuse-bank compiler depends on an interval optimizer or a support regularity assumption.

The useful point for the extremal-product programme is now sharper than the earlier r36 statement: after purification, a high slab ratio in the diffuse exact-rank-two endpoint cannot hide its pair-volume currency among arbitrarily many tiny physical minors. The actual Parseval DPP has a sharp fixed disjointness floor, and the resulting intrinsic pair law either puts positive mass through a bounded physical center or exposes a physical rank-two bank with a uniformly diffuse transverse direction.

## 7. What remains

**Full QFORM remains OPEN / not proved / not disproved. Global continuity remains OPEN.** The present structural theorem does not itself prove a density bound in either branch of Theorem 5.1.

The next precise B13 implication is

`QFORM-48CENTER-OR-DIFFUSE-TRANSVERSE-RECEIVER-v1`:

1. in the finite-center branch, group the `mu_k` star around the selected physical center `h` into a product-preserving finite-center receiver, retaining all arbitrary same-bank curvature rather than using a frozen-slice supremum; and
2. in the diffuse-bank branch, realize the transverse coefficient direction from (5.11) as an actual projected physical crossing (or an equivalent dependence-safe square resource) while retaining the near-null pivot (4.6).

The live correction `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` forbids replacing step 2 by a near-null half-Riesz argument that sees only the cross-row norm. The genuine third curvature encoded by `tau` must remain.

## 8. Computation

The sibling `CHECK.py` verifies the exact Fourier-moment identity (2.14), the sharp four-row equality example, the constants above, and 8,653 randomly generated Parseval frames satisfying `max leverage<=1/2`. It terminates

`QFORM_B13_R38_SHARP_DPP_CHECK_PASS`.

The random sample is a sanity check only; all displayed inequalities are proved analytically above.
