SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-24T04:03:28Z.
attacking: transverse-vertex subprobability localization — make the newest partner random-slope receiver mass-homogeneous across arbitrary positive fragments, and isolate the exact whole-anchor condition that removes the square-root fragment tax.

# account02/B14 — subprobability transverse-vertex localization and the active-slope fragment barrier

Run: `20260924T040328Z-account02-B14-QFORM-auto11`.

Status: **NEW SUPPORTING LOCALIZATION THEOREM + EXACT-TARGET PROOF-INTERFACE OBSTRUCTION / FULL QFORM OPEN / CONTINUITY SEPARATE**.

The unrestricted owner target remains: independent original-coordinate real laws with densities at most one, arbitrary real symmetric matrix with at least three eigenvalues of modulus at least one, and one universal essential-density bound. No moment, support, connectedness, bounded-diameter, fixed-fragment, log-concavity, Gaussian, iid, or post-rotation-independence assumption is introduced below.

## 1. First unpaid implication

`QFORM-WHOLE-RANDOM-SLOPE-BEFORE-LOCALIZATION-v1`:

In every surviving Schur/hub configuration using a random-slope receiver, before localizing the variables that generate the slope one must force at least one of the following:

1. the whole random slope is aggregated before the reciprocal half-Riesz payment;
2. an undecomposed original-coordinate/product-bank slope anchor remains whose convolution makes every localized slope submeasure carry a density cap proportional to its mass;
3. another whole-law D'/D5/projected-crossing/ridge/pair/hub receiver fires first.

The latest account03/B14 theorem supplies the receiver once such a transverse square + random slope representation exists, but `s_3(A)>=1` does not yet force that representation and an additional `U`-dependent residual curvature is still outside its scope. The calculation below shows that normalizing/localizing the slope source first is not a harmless substitute: the resulting certificate can grow like `sqrt(N)`, or become infinite for a countable unbounded comb, while the unchanged exact-target law has a uniform density bound.

## 2. Input theorem from the designated partner

The newest compatible account03/B14 result is `QFORM-TRANSVERSE-VERTEX-RANDOM-SLOPE-LOCALIZATION-v1`, canonical report

`yspennstate/math-open-problems@eac495331ac51a64b786478b490564b25a06c233`
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260924T033822Z-account03-B14-QFORM-auto11/REPORT.md`.

It proves: if `W,U,Z` are mutually independent, `||p_W||_inf<=K_W`, `||p_U||_inf<=K_U`, `D=D(Z)` has probability-density cap `M`, `Phi(U,Z)` is arbitrary measurable, `R(Z)` arbitrary, and `a!=0`, then

`Q = a(W+Phi(U,Z))^2 + D(Z)U + R(Z)`

has an absolutely continuous law with

`||p_Q||_inf,ess <= 4 sqrt(2) K_W sqrt(K_U M/|a|)`.          (2.1)

Equivalently, for `D=2S`, `||p_S||_inf<=M_S`,

`||p_Q||_inf,ess <= 4 K_W sqrt(K_U M_S/|a|)`.                (2.2)

The square vertex may overlap arbitrarily with the transverse hub `U`; the additive residual must remain `Z`-measurable so it cannot cancel the affine resource `D(Z)U`.

## 3. New theorem: the exact subprobability homogeneity

### Theorem `QFORM-TRANSVERSE-VERTEX-SUBPROBABILITY-COMPILER-v1`

Let `W,U` be independent probability laws with density caps `K_W,K_U`. Let `tau` be a finite positive measure on a measurable `Z`-space, independent of `W,U`, of total mass

`m = tau(Z) <= 1`.

Let `D=D(z)` be measurable and assume the pushforward `D_# tau` is absolutely continuous with an **unnormalized** density `h_D` satisfying

`0 <= h_D <= L`,    `integral h_D = m`.                     (3.1)

Let `Phi(U,z)` be arbitrary finite measurable, `R(z)` arbitrary finite measurable, and `a!=0`. Define the output positive submeasure `eta` by pushing forward `P_W x P_U x tau` under

`F(w,u,z)=a(w+Phi(u,z))^2+D(z)u+R(z)`.                     (3.2)

Then `eta` has a Lebesgue density and

`boxed: ||p_eta||_inf,ess
 <= 4 sqrt(2) K_W sqrt(K_U/|a|) sqrt(m L).`                 (3.3)

If `D=2S` and the unnormalized pushforward `S_#tau` has density cap `L_S`, then

`boxed: ||p_eta||_inf,ess
 <= 4 K_W sqrt(K_U/|a|) sqrt(m L_S).`                       (3.4)

#### Proof

For fixed `(u,z)`, translation of `W` does not change its density cap. Exactly as in the partner proof, the conditional square

`V=a(W+Phi(u,z))^2`

has the one-sided density envelope

`p_{V|u,z}(v) <= K_W |a|^{-1/2}|v|^{-1/2} 1_{av>0}`       (3.5)

for almost every `v`. Fix `z` with `d=D(z)!=0`; this holds for `tau`-almost every `z` because (3.1) has no atom at zero. The density of `dU` has total mass one and cap `K_U/|d|`. The one-sided bathtub inequality gives, uniformly in the output target and in `Phi,R`,

`||p_{F(W,U,z)}||_inf
 <= 2 K_W sqrt(K_U/(|a| |D(z)|)).`                         (3.6)

Integrating (3.6) against the **unnormalized** measure `tau` reduces the problem to

`I = integral |D(z)|^{-1/2} tau(dz)
   = integral_R |d|^{-1/2} h_D(d) dd`.                    (3.7)

Among nonnegative densities of total mass `m` capped by `L`, the symmetric decreasing bathtub maximizer for the kernel `|d|^{-1/2}` is `L` on the centered interval of length `m/L`. Hence

`I <= L integral_{-m/(2L)}^{m/(2L)} |d|^{-1/2} dd
   = 2 sqrt(2mL).`                                        (3.8)

Combining (3.6)-(3.8) proves (3.3). If `D=2S`, scaling gives `L=L_S/2`, so (3.4) follows. QED.

The exponent is the important feature: the exact localization cost is

`boxed: sqrt(m L_S).`                                     (3.9)

It is homogeneous of degree one in mass precisely when the unnormalized slope cap itself carries one full mass factor.

## 4. Countable positive-mixture compiler

Let a probability environment measure be decomposed into arbitrary positive pieces

`tau = sum_j tau_j`,    `m_j=tau_j(Z)`,    `sum_j m_j=1`.  (4.1)

Suppose the unnormalized `S`-pushforward of `tau_j` has cap `L_j`. By positivity and (3.4), the total output density satisfies

`boxed: ||p_Q||_inf,ess
 <= 4 K_W sqrt(K_U/|a|) sum_j sqrt(m_j L_j).`               (4.2)

Therefore the exact zero-tax criterion is

`L_j <= M_0 m_j  for every j`.                            (4.3)

Under (4.3),

`sum_j sqrt(m_j L_j) <= sqrt(M_0) sum_j m_j = sqrt(M_0)`,

and hence

`boxed: ||p_Q||_inf,ess
 <= 4 K_W sqrt(K_U M_0/|a|).`                             (4.4)

There is no count, location, separation, support-radius, tail or moment term. The decomposition may be countably infinite.

## 5. Whole-slope-anchor theorem: arbitrary complementary fragmentation is free

### Theorem `QFORM-TRANSVERSE-VERTEX-WHOLE-SLOPE-ANCHOR-v1`

Suppose the environment splits as independent `Z=(H,C)` and the random slope is

`S=S_H(H)+S_C(C)`.                                        (5.1)

Assume only that `S_H` has a probability density capped by `M_H`. Decompose the law of `C` into **arbitrary** positive submeasures `tau_j^C` of masses `m_j`; no density, support, moment or regularity of the individual `S_C`-pushforwards is required.

For the product submeasure `P_H x tau_j^C`, the slope pushforward is the convolution of `p_{S_H}` with a positive measure of mass `m_j`. Therefore its unnormalized density satisfies

`L_j <= M_H m_j`.                                        (5.2)

Applying (4.4) gives

`boxed: ||p_Q||_inf,ess
 <= 4 K_W sqrt(K_U M_H/|a|),`                             (5.3)

with **zero loss under arbitrary finite or countable fragmentation of the entire complementary bank `C`**.

This is the desired localization mechanism for distant fragments: leave one genuine original/product-bank slope anchor whole, localize everything else, and pay the half-Riesz singularity only after the anchor convolution has restored the full mass factor.

If `S_H=v dot X_H` is a nonzero projection of an undecomposed original-coordinate product bank with coordinate density caps one, the usual one-dimensional product-projection estimate supplies, for example,

`M_H <= sqrt(2)/||v||_2`,                                 (5.4)

so (5.3) is completely support- and translation-free. The theorem does not require a bounded number of fragments or a bounded support diameter.

## 6. Exact-target active-slope fragmentation barrier

The same calculation shows why the order of localization matters.

Let `W,U,S_N` be independent cap-one variables. For the finite version, take

`E_N = union_{j=1}^N [4^j,4^j+1/N]`,
`p_{S_N}=1_{E_N}`.                                        (6.1)

Consider

`Q_N = 2(W+U)^2 + 4 U S_N`.                              (6.2)

The homogeneous matrix, in order `(W,U,S_N)`, is

`A_* = [[2,2,0],[2,2,2],[0,2,0]]`,                       (6.3)

with characteristic polynomial

`chi(lambda)=lambda^3-4lambda^2-4lambda+8`.               (6.4)

Its three roots lie in `(-2,-1)`, `(1,2)`, `(4,5)`, respectively. Thus **all three eigenvalues have modulus greater than one**, so (6.2) is inside the exact owner target.

Keeping `S_N` whole, the partner theorem has `a=2`, `D=4S_N`, and `||p_D||_inf=1/4`; therefore

`boxed: ||p_{Q_N}||_inf,ess <= 2`                         (6.5)

uniformly in `N` and in the exponentially growing fragment separation.

Now change no probability law and only split `S_N` into its `N` tooth submeasures. Each tooth has mass

`m_j=1/N`,

while its unnormalized `D=4S_N` pushforward has the exact density cap

`L_{D,j}=1/4`,                                            (6.6)

independent of `m_j`. Formula (3.3) therefore evaluates to

`2/sqrt(N)`                                               (6.7)

for every tooth, and the positive cellwise compiler becomes

`boxed: 2 sqrt(N).`                                       (6.8)

Thus active slope fragmentation **before** the reciprocal half-Riesz payment creates a square-root fragment tax although the underlying law and matrix are unchanged.

There is a stronger countable, unbounded-support version. Put

`m_j = 6/(pi^2 j^2)`,
`E = union_{j>=1} [4^j,4^j+m_j]`,
`p_S=1_E`.                                                 (6.9)

Then `p_S` is a cap-one probability density on an unbounded, countably fragmented support, and the whole-slope certificate is still (6.5). But splitting by teeth gives cellwise cost `2 sqrt(m_j)`, so

`sum_j 2 sqrt(m_j)
 = (2 sqrt(6)/pi) sum_j 1/j
 = infinity.`                                             (6.10)

This is a **proof-interface obstruction only**, not a lower bound on the true density and not a QFORM counterexample.

## 7. Exact-target anchor rescue on the same remote comb

Let `H` be another independent cap-one variable and let `C` have the comb law (6.9). Consider

`Q_anchor = 2(W+U)^2 + 4U(H+C)`.                          (7.1)

Its four-coordinate matrix is

`A_anchor = [[2,2,0,0],
             [2,2,2,2],
             [0,2,0,0],
             [0,2,0,0]]`.                                (7.2)

Its characteristic polynomial is

`lambda (lambda^3-4lambda^2-8lambda+16)`.                 (7.3)

The three nonzero roots lie in `(-3,-2)`, `(1,2)`, `(4,5)`. Hence `A_anchor` also has at least three eigenvalues of modulus greater than one.

Decompose **all of the unbounded comb `C`** into its teeth but keep `H` whole. On tooth `j`, the slope submeasure `H+C_j` is a convolution with the whole cap-one law of `H`, so its unnormalized density cap is at most `m_j`. After scaling by four, the `D`-cap is at most `m_j/4`. Formula (3.3) then gives the cell bound

`2 m_j`.                                                   (7.4)

Summing over all countably many teeth gives exactly the same whole-law constant:

`boxed: ||p_{Q_anchor}||_inf,ess <= 2 sum_j m_j = 2.`     (7.5)

Thus arbitrary countable, unbounded, exponentially separated localization is genuinely zero-tax when a whole slope anchor is retained. No bounded-diameter or fixed-fragment surrogate is hiding in the statement.

## 8. Required fixed-source theorem applied to the same obstruction

The required fixed source was freshly read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Its completed Theorem A in `COUNTEREXAMPLE_SEARCH.md` states: in dimension three, if every eigenvalue of the quadratic matrix has modulus at least `sigma`, arbitrary linear terms are allowed and

`||p_Q||_inf <= 6 sqrt(pi)/sigma`.                         (8.1)

Apply this to the **same matrix and same fragmented laws** in (6.2). Let

`sigma_* = min{|lambda|: lambda eigenvalue of A_*}`.

From (6.4), `sigma_*>1` (numerically `sigma_*=1.109916264...`). Therefore the completed source theorem gives

`boxed: ||p_{Q_N}||_inf <= 6 sqrt(pi)/sigma_* < 6 sqrt(pi)` (8.2)

for every finite comb, and the identical inequality for the countably fragmented unbounded comb (6.9). Numerically the source certificate is about `9.58156`.

Hence a source-valid whole-law theorem stays uniformly finite on exactly the family for which the artificial fragment-first transverse-vertex compiler grows like `sqrt(N)` and becomes infinite in the countable version. This confirms that the obstruction is the proof order, not the QFORM target.

For context, the same fixed source's `FOURIER_ROUTE_REPORT.md` also proves the D5 no-marginal fifth-volume estimate

`||p_Q||_inf <= 5 sqrt(2e) e_5(A_IJ^T A_IJ)^(-1/10)`,

showing again that whole-law volume exits are legitimate alternatives before fragment normalization.

## 9. Localization rule and remaining gap

The new principle is exact:

**Aggregate the random slope before the reciprocal half-Riesz payment. If some complementary variables must be localized first, retain a whole independent slope anchor so convolution makes each unnormalized slope cap proportional to that fragment's mass.**

The mass-cap quantity `sqrt(mL)` is the correct compiler invariant for the newest transverse-vertex receiver. Pure active fragmentation has `L` essentially independent of `m` and therefore pays a square-root tax; anchored fragmentation has `L=O(m)` and is zero-tax.

What remains unpaid for the full conjecture is not translations or remote fragments. It is structural/overlap control: starting only from `s_3(A)>=1`, force a transverse square + random-slope representation with either a whole slope anchor or an existing whole-law volume/ridge/pair exit, while controlling the extra `U`-dependent quadratic residual that can otherwise cancel the affine slope resource.

## 10. Continuity and scope ledger

Everything above concerns absolute continuity and essential `L^infinity` bounds. No full-target continuity statement is claimed. The latest partner theorem itself separates continuity in the genuinely overlapping `Phi(U,Z)` branch. The localization arguments here preserve that distinction.

No independence after spectral rotation is used: every independence statement is between retained original-coordinate/product-bank factors. No moments are taken. No support radius, diameter, fragment count, fragment separation, compactness, or tail decay is assumed.
