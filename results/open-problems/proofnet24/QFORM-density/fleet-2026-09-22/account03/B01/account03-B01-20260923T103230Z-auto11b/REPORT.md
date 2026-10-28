SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B01, 2026-09-23T10:32:30Z.
attacking: derive an L2 bounded-remainder compiler for a rank-two physical cross bicore, then apply account04/B01 grouped-square innovations to an actual hybrid QFORM inequality and signed-Fejer bound.

# account03/B01 — rank-two cross + bounded independent remainder: an L2 oscillatory compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `account03-B01-20260923T103230Z-auto11b`  
Classification: `PROVED SUPPORTING ANALYTIC THEOREM / ESSENTIAL STEP APPLIED / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: proved on the new branch (`C_0(R)`); full-target continuity remains open.

## 1. Target, controls, and correction boundary

The unrestricted target is still open: for every dimension, every family of independent real inputs with probability densities at most one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal `L^infinity` bound for the density of `X^T A X`, or give a target-valid counterexample.


The phase-aligned correction remains binding. For any prescribed `s>0` and small `delta>0`, choose a finite union `E` of total length one inside

`{x : dist(s x^2, 2 pi Z) <= delta}`

and let `f=1_E`. Then

`Re int exp(i s x^2) f(x) dx >= cos(delta)`.

Thus no positive-power, law-uniform pointwise scalar Fresnel decay follows from `f<=1`. The new theorem below does not use one. It uses a **joint rank-two physical cross estimate in L2 time** and a second L2 resource supplied by an independent bounded-density remainder.

Source-pinned inputs actually used:

1. account03/B01 source-disjoint square Lp/log report, `yspennstate/math-open-problems@86cf72d34382ec4456beddd12b7ed9a579d830fd`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T100010Z-auto11/REPORT.md`. Section 3 there proves the joint rank-two cross envelope recalled below, allowing arbitrary same-bank phases on both active banks.
2. Designated partner account04/B01 grouped innovation theorem, `yspennstate/math-open-problems@88003dc06af684cc4bc178a7dfe8e7cbebb0f987`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T234537Z-account04-B01-grouped-square-fejer-r2/REPORT.md`. It proves the conditional grouped-square density cap and applies account04/B01's signed-Fejer identity.
3. Designated partner account04/B01 signed-Fejer theorem, canonical bundle `yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`, proving `||p_mu||_infinity = sup_(T>0,y) D_T mu(y)` with the extended-value convention.

A repository source search before publication found many related rank-two receivers, but no source-matching completed theorem with the exact `rank-two cross + arbitrary independent bounded-density remainder -> L2 x L2` scope and the constant below. This is a duplication check, not a novelty claim.

## 2. The bicore L2 resource

Partition ORIGINAL independent coordinates into disjoint banks `I,J,D,W`. Condition on `X_W=w`. Let `K` be the physical `I x J` cross matrix and suppose it has exact rank two, with nonzero singular values

`kappa_1 >= kappa_2 > 0`,

and define

`Delta = kappa_1 kappa_2`.                                      (2.1)

Allow completely arbitrary measurable same-bank phases `F_w(X_I)` and `G_w(X_J)`. Define the bicore

`B_w = F_w(X_I) + G_w(X_J) + 2 X_I^T K X_J`.                    (2.2)

The source-pinned projected-Plancherel theorem gives, uniformly in `w`,

`|psi_w(t)| := |E exp(i t B_w)|
 <= min(1, 2 pi/(|t| sqrt(Delta))).`                             (2.3)

This estimate is joint in the two ORIGINAL product banks. It is not obtained by multiplying scalar quadratic-phase bounds.

Put

`A_Delta = 2 pi / sqrt(Delta)`.                                  (2.4)

Then the exact L2 integral of the envelope is

`int_R min(1,A_Delta/|t|)^2 dt
 = 2 int_0^A_Delta 1 dt + 2 int_A_Delta^infinity A_Delta^2 t^(-2) dt
 = 4 A_Delta
 = 8 pi / sqrt(Delta).`                                         (2.5)

Therefore

`boxed:
 ||psi_w||_2 <= 2 sqrt(2 pi) Delta^(-1/4).`                      (2.6)

The important point is that the borderline pointwise `1/|t|` bicore envelope is square-integrable even though it need not itself be integrable.

## 3. Independent bounded remainder supplies the second L2 factor

Let `R_w=R_w(X_D)` be an arbitrary real random variable generated only by the disjoint original-coordinate bank `D`. Assume its conditional law (given `X_W=w`) has a probability density `r_w` satisfying

`||r_w||_infinity <= M(w) < infinity`.                           (3.1)

No shape, moment, support, unimodality, log-concavity, or quadratic representation is required in this theorem.

Let

`g_w(t)=E_D exp(i t R_w)`.

Because `r_w` is a probability density,

`||r_w||_2^2 <= ||r_w||_infinity ||r_w||_1 <= M(w)`.             (3.2)

With the Fourier convention used in the fleet, Plancherel gives

`||g_w||_2^2 = 2 pi ||r_w||_2^2 <= 2 pi M(w)`,                  (3.3)

hence

`boxed:
 ||g_w||_2 <= sqrt(2 pi M(w)).`                                  (3.4)

Given `w`, the banks `(I,J)` and `D` are genuinely independent original-coordinate banks. Hence for

`Q_w = B_w + R_w + c(w)`                                        (3.5)

the conditional characteristic function factors, up to the harmless phase `exp(i t c(w))`, as

`phi_w(t)=psi_w(t) g_w(t) exp(i t c(w)).`                        (3.6)

Cauchy-Schwarz in time and (2.6),(3.4) yield the central estimate

`int_R |phi_w(t)| dt
 <= ||psi_w||_2 ||g_w||_2
 <= 4 pi sqrt(M(w)) Delta^(-1/4).`                               (3.7)

## 4. Main theorem

### Theorem 4.1 — `QFORM-RANK2-CROSS-BOUNDED-REMAINDER-L2-v1`

Under the setup above, if

`E_W sqrt(M(W)) < infinity`,                                    (4.1)

then the unconditional characteristic function is in `L1(R)`, the law of `Q` has a continuous density vanishing at infinity, and

`boxed:
 ||p_Q||_infinity
 <= 2 Delta^(-1/4) E_W sqrt(M(W)).`                              (4.2)

In particular, if `M(w)<=M` almost surely, then

`boxed:
 ||p_Q||_infinity <= 2 sqrt(M) Delta^(-1/4).`                    (4.3)

#### Proof

By conditional expectation,

`phi_Q(t)=E_W phi_W(t)`.

Thus `|phi_Q(t)| <= E_W |phi_W(t)|`. Tonelli and (3.7) give

`||phi_Q||_1
 <= E_W ||phi_W||_1
 <= 4 pi Delta^(-1/4) E_W sqrt(M(W)).`                           (4.4)

Assumption (4.1) makes the right side finite. Fourier inversion therefore gives a `C_0(R)` density and

`||p_Q||_infinity <= (2 pi)^(-1)||phi_Q||_1`,

which is (4.2). Equation (4.3) is immediate. QED.

### Scaling check

If the entire quadratic form is multiplied by `c!=0`, then `K -> cK`, hence `Delta -> c^2 Delta`; a density cap for the remainder scales as `M -> M/|c|`. The right side of (4.3) therefore becomes

`2 sqrt(M/|c|) (c^2 Delta)^(-1/4)
 = |c|^(-1) 2 sqrt(M) Delta^(-1/4)`,

which is the exact density scaling.

## 5. Required partner application: grouped squares as the bounded remainder

Now apply the completed account04/B01 theorem to an actual inequality, not merely as a citation.

Further partition `D` into pairwise disjoint original-coordinate banks

`D = C disjoint_union B_1 disjoint_union B_2 disjoint_union B_3`.

For `ell=1,2,3`, let

`L_ell = a_ell^T X_(B_ell)`, `sigma_ell=||a_ell||_2>0`,           (5.1)

and suppose the remainder has, conditional on `W=w`, the exact grouped-square form

`R_w = R_0,w(X_C)
      + sum_(ell=1)^3 lambda_ell
          (L_ell + h_ell,w(X_C))^2`,                              (5.2)

where all `lambda_ell !=0` and `R_0,w,h_ell,w` are arbitrary measurable functions.

Account04/B01 proves that for every same-sign pair `j!=k`, the conditional density of `R_w` satisfies, uniformly in `w`,

`M(w) <= 2 pi /
 [sigma_j sigma_k sqrt(|lambda_j lambda_k|)].`                   (5.3)

Substituting (5.3) into the new compiler (4.3) gives the hybrid inequality

`boxed:
 ||p_Q||_infinity
 <= 2 sqrt(2 pi) Delta^(-1/4)
    (sigma_j sigma_k)^(-1/2)
    |lambda_j lambda_k|^(-1/4).`                                 (5.4)

Since three nonzero real `lambda_ell` always contain a same-sign pair, one may minimize (5.4) over all same-sign pairs.

This application retains arbitrary same-bank curvature in the rank-two bicore, arbitrary conditioning-generated shifts in the three grouped squares, and arbitrary functions of the conditioned `W` bank. The only independence used is the explicit disjoint ORIGINAL-coordinate bank decomposition.

### Signed-Fejer consequence

The designated account04/B01 signed-Fejer identity now applies directly to the density bound (5.4): for every `T>0` and `y in R`,

`boxed:
 D_T law(Q)(y)
 <= 2 sqrt(2 pi) Delta^(-1/4)
    (sigma_j sigma_k)^(-1/2)
    |lambda_j lambda_k|^(-1/4).`                                 (5.5)

This is an averaged-frequency statement. It makes no claim that `|phi_Q(t)|` obeys a law-uniform scalar stationary-phase envelope.

## 6. Target-valid normalized control

Take seven independent cap-one inputs and

`Q_0 = 2 X_1 Y_1 + 2 X_2 Y_2 + Z_1^2 + Z_2^2 + Z_3^2.`          (6.1)

Here the rank-two cross matrix is `K=I_2`, so `Delta=1`. The three square innovation banks are singleton original-coordinate banks with `sigma_1=sigma_2=sigma_3=1` and `lambda_1=lambda_2=lambda_3=1`. The associated symmetric matrix has spectrum

`{-1,-1,1,1,1,1,1}`.                                            (6.2)

Hence it satisfies the exact owner spectral hypothesis. Applying the **partner theorem as stated**, (5.3) gives `M<=2pi`, and (5.4) gives

`boxed:
 ||p_(Q_0)||_infinity <= 2 sqrt(2 pi)
 = 5.013256549262... < 5.014,`                                   (6.3)

with a continuous `C_0` density. The same constant bounds all signed-Fejer averages.

For this singleton control only, one can sharpen the grouped-square density cap directly from `sqrt(2)` projection caps to the actual coordinate caps `1`, obtaining `M<=pi` and hence `2 sqrt(pi)<3.545`. That refinement is not needed for the partner application and is not claimed for general grouped projections.

## 7. What this does and does not close

This theorem supplies a modular bridge that was absent from the preceding B01 run: **any source-disjoint remainder with a bounded density can be spent as an L2-time factor against a rank-two cross bicore**. One no longer needs the remainder itself to be a single square with a separately optimized `L^p` transform. In particular, a whole grouped-square packet from account04/B01 can be compiled into the bicore in one line.

The full QFORM conjecture nevertheless remains OPEN. The bare three-large-eigenvalue condition does not automatically expose a source-disjoint decomposition containing both

1. a rank-two physical cross block with `Delta` bounded below, and
2. an independent remainder with a dimension-free density cap.

The current structural corrections explicitly rule out demanding one uniformly good fixed physical triple/minor. The next B01 implication is therefore:

**`QFORM-RANK2-BICORE-BOUNDED-REMAINDER-ROUTING-v1`.** From the remaining strict-N3 / high-leverage / low-cross-rank states, either route a quantitatively strong rank-two bicore to a source-disjoint already-paid bounded-density remainder (grouped squares, pair-log output, ridge/diffuse packet, or another completed branch), or retain overlap and use one of the already-proved transverse/overlap-safe receivers. Reciprocal payment must occur after aggregation, not by choosing a microscopic physical coefficient.

No counterexample to the full conjecture is produced. The phase-aligned scalar counterexample remains a counterexample only to uniform pointwise Fresnel decay.

## 8. Verification status

A deterministic checker in this bundle verifies:

- `int min(1,2pi/|t|)^2 dt = 8pi` at `Delta=1`;
- the normalized partner-compiled constant `2sqrt(2pi)=5.013256549262...`;
- the spectrum in (6.2);
- exact homogeneity of (4.3) under common scaling.

These checks are regression diagnostics. The universal inequalities are proved analytically above.
