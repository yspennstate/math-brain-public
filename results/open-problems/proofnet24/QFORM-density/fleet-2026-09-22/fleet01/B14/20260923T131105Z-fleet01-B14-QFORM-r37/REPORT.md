SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-23T13:11:05Z.
attacking: fractional-trace mass-homogeneity localization — preserve full fragment mass through the partner cubic-root pair-log estimate, with arbitrary fragment-dependent shifts and no support or moment bounds.

# fleet01/B14 r37 — fractional-trace mass localization and a protected-slope target theorem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T131105Z-fleet01-B14-QFORM-r37`  
Status: `NEW SUPPORTING LOCALIZATION THEOREM + TARGET-VALID PARTNER APPLICATION / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`. Continuity for the full target remains separate.

## 1. Scope and completed sources actually used

The exact owner target is unchanged: for every finite `n`, every independent real input coordinates with probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal finite essential density bound for `X^T A X`, or give a valid counterexample. No support, moment, centering, connectedness, identical-law, log-concavity, diagonal-coordinate, or post-rotation-independence hypothesis is added.


The completed designated partner used below is **fleet02/B14 r36**, canonical source

`yspennstate/math-open-problems@d2180eded43f3c299ecff739c67109d342c032b7`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260923T122915Z-fleet02-B14-QFORM-r36/REPORT.md`.

Two parts of that report are used at equations, not merely cited:

1. exact law-level full-target localization: the worst small-ball/density constant over all cap-one product laws is exactly the same when every marginal is restricted to the indicator of an arbitrary compact finite union of intervals of total measure one, with no common fragment-count/diameter/location bound;
2. the globally dominated physical-pair logarithmic estimate: for an invertible indefinite original-coordinate pair `B`,

`D=|det B|`, `kappa=sigma_min(B)`,

and a completed scalar remainder of density cap `H`,

`||p_Q||_infinity <= 6 [ H/(kappa sqrt(D)) ]^(1/3)`.          (1.1)

For the multidimensional-bank corollary I also use the completed product-projection estimate source-pinned through fleet03/B14 r26,

`yspennstate/math-open-problems@f89093b26b458e02914d99e7235268aff6ae1e40`,

which gives for independent cap-one coordinates `W=(W_j)` and every nonzero `c`,

`||p_(c^T W)||_infinity <= sqrt(2)/||c||_2`.                  (1.2)

The proof below changes mechanism from the preceding protected-smoother runs: instead of optimizing a conditional cap directly, it proves a **subprobability fractional-trace homogeneity theorem** and then feeds the exact mass power through (1.1).

## 2. Main localization lemma: fractional traces of subprobabilities

### Theorem 2.1 — `QFORM-FRACTIONAL-TRACE-SUBPROBABILITY-LOCALIZATION-v1`

Let `0<alpha<1`. Let `nu` be a finite measure on `R`, of total mass `m`, absolutely continuous with a density `g` satisfying `0<=g<=L`. Then, for every translation `a in R`,

`boxed:
 int |s-a|^(-alpha) dnu(s)
 <= C_alpha L^alpha m^(1-alpha),
 C_alpha = 2^alpha/(1-alpha).`                                (2.1)

The constant is independent of the location of `nu`, the number or separation of support components, the support diameter, all tails, and every moment.

More generally, for a finite or countable family `nu_j` with masses `m_j`, density caps `L_j`, and arbitrary fragment-dependent centers `a_j`,

`boxed:
 sum_j int |s-a_j|^(-alpha) dnu_j(s)
 <= C_alpha sum_j L_j^alpha m_j^(1-alpha).`                   (2.2)

In particular, if the **unnormalized** caps carry their masses,

`L_j <= M m_j`,                                               (2.3)

then

`boxed:
 sum_j int |s-a_j|^(-alpha) dnu_j(s)
 <= C_alpha M^alpha sum_j m_j.`                              (2.4)

Thus for a probability decomposition `sum_j m_j=1`, the whole-law constant is preserved **exactly**, regardless of fragment count, separation, translations, or support size.

### Proof

Fix `a`. The kernel `K_a(s)=|s-a|^(-alpha)` is symmetric decreasing about `a`. Among all densities bounded by `L` and of total mass `m`, the bathtub/rearrangement principle maximizes `int K_a g` by taking `g=L` on the centered interval of length `m/L`. Hence

`int |s-a|^(-alpha) dnu(s)
 <= 2L int_0^(m/(2L)) r^(-alpha) dr
 = [2L/(1-alpha)] [m/(2L)]^(1-alpha)
 = [2^alpha/(1-alpha)] L^alpha m^(1-alpha)`,                 (2.5)

which is (2.1). Applying (2.1) to every `nu_j` and summing proves (2.2); countable sums follow by Tonelli/monotone convergence. Under (2.3),

`L_j^alpha m_j^(1-alpha) <= M^alpha m_j`,                     (2.6)

which gives (2.4). QED.

For the exponent needed by the partner cubic-root estimate,

`alpha=1/3`, `C_(1/3)=3*2^(-2/3)`.                           (2.7)

The precise point of (2.4) is that the singularity can be paid **after an outside subprobability split** with no localization tax, provided the active slope law remains whole so that its cap is multiplied by the outside mass.

## 3. Partner application: cubic-root pair smoothing with exact subprobability homogeneity

Let `(U_1,U_2)` be two original independent cap-one coordinates whose quadratic block is an invertible indefinite symmetric matrix `B`; put `D=|det B|` and `kappa=sigma_min(B)`.

Let `Y` be another independent cap-one original coordinate. Let `W` denote an independent product block, and let `nu` be a finite subprobability law on that block of mass `m`. Suppose the pushforward of `nu` by a measurable slope statistic `S(W)` has a density bounded by `L`. Let `rho(W)` be arbitrary and possibly fully correlated with `S(W)`. Consider the completed remainder

`R = rho(W) + 2 S(W) Y`.                                      (3.1)

All affine terms in the outer physical pair are allowed; they are suppressed from notation because the partner estimate is uniform in them.

### Theorem 3.1 — protected-slope fractional-trace compiler

The output submeasure of the full quadratic form satisfies

`boxed:
 ||p_Q^(sub)||_infinity
 <= 9 (kappa sqrt(D))^(-1/3) L^(1/3) m^(2/3).`               (3.2)

If `L<=mM`, equivalently if the normalized protected slope law has cap at most `M`, then

`boxed:
 ||p_Q^(sub)||_infinity
 <= 9 m [ M/(kappa sqrt(D)) ]^(1/3).`                         (3.3)

This is the exact linear mass homogeneity needed for zero-loss localization.

### Proof

Condition on `W=w`. Except on the null set `S(w)=0` (null because the slope pushforward is absolutely continuous), the scalar remainder in (3.1) is a translate and rescaling of the cap-one variable `Y`, hence has density cap

`H(w) <= 1/[2|S(w)|]`.                                        (3.4)

Apply fleet02/B14 r36 equation (1.1) on that fiber:

`||p_(Q|W=w)||_infinity
 <= 6 [1/(2 kappa sqrt(D)|S(w)|)]^(1/3).`                    (3.5)

Integrating the conditional output subdensities against `nu` gives

`||p_Q^(sub)||_infinity
 <= 6(2 kappa sqrt(D))^(-1/3)
    int |S(w)|^(-1/3) dnu(w).`                               (3.6)

The pushforward measure `S_#nu` has mass `m` and density cap `L`. Apply Theorem 2.1 with `alpha=1/3`, `a=0`:

`int |S(w)|^(-1/3) dnu(w)
 <= 3*2^(-2/3) L^(1/3)m^(2/3).`                              (3.7)

Multiplying (3.6) and (3.7) gives `18*2^(-1)=9`, proving (3.2). If `L<=mM`, then `L^(1/3)m^(2/3)<=M^(1/3)m`, proving (3.3). QED.

### Corollary 3.2 — arbitrary outside fragmentation has zero tax

Suppose an independent outside environment is decomposed into arbitrary finite/countable pieces of masses `m_j`, and on piece `j` the same protected slope law is merely translated by an arbitrary amount `beta_j`. Its unnormalized slope pushforward then has cap

`L_j <= m_j M`;                                               (3.8)

translation does not alter the cap. Applying (3.3) on every outside piece and summing gives

`sum_j 9m_j[M/(kappa sqrt(D))]^(1/3)
 = 9[M/(kappa sqrt(D))]^(1/3).`                              (3.9)

Thus fragment-dependent translations, remote outside pieces, unbounded support and missing moments cost **exactly zero**. The statement is unchanged for countably many pieces.

The more general budget when proportionality is nonuniform is

`||p_Q||_infinity
 <= 9(kappa sqrt(D))^(-1/3)
    sum_j L_j^(1/3)m_j^(2/3).`                               (3.10)

Equation (3.10) is useful because it identifies exactly what must be preserved by a future structural decomposition.

## 4. Actual full-target family: arbitrary dense bank curvature

Split original coordinates as

`X=(U_1,U_2,Y,W,Z)`,

where every coordinate is independent and cap-one. Assume the active principal block on `(U_1,U_2,Y,W)` is

`A_I = B direct_sum [[0,c^T],[c,H]]`,                         (4.1)

where

- `B` is an invertible indefinite `2x2` block;
- `c!=0` is arbitrary;
- `H=H^T` is an entirely arbitrary bank matrix: dense, high rank, indefinite and arbitrarily large.

All coefficients involving the outside original-coordinate block `Z` are arbitrary. Condition on `Z=z`. This preserves the product law of the active original coordinates and gives

`Q_z = U^T B U + affine_z(U)
      + 2Y[c^T W+beta(z)]
      + W^T H W + ell_z^T W + const_z.`                       (4.2)

Thus Theorem 3.1 applies with

`S_z(W)=c^T W+beta(z)`, `rho_z(W)=W^T H W+ell_z^T W+const_z`.(4.3)

The completed product-projection theorem (1.2) gives, uniformly in `z`,

`M <= sqrt(2)/||c||_2`.                                      (4.4)

Therefore

`boxed:
 ||p_(X^T A X)||_infinity
 <= 9 [ sqrt(2)/(kappa sqrt(D) ||c||_2) ]^(1/3).`             (4.5)

No parameter depending on `H`, dimension, outside couplings, translations, support diameter, fragment count/separation, tails, or moments appears.

This is a new quantitative variant of the earlier zero-self hub theorem. It is especially useful for a strong collective bank coupling because it has no additive `2/sqrt(D)` floor.

### Target validity

If both eigenvalues of `B` have modulus at least one and `||c||_2>=1`, the active principal block (4.1) already has at least three eigenvalues of modulus at least one. Indeed `B` supplies two. For

`S=[[0,c^T],[c,H]]`,

`||S||_op >= ||S e_0||_2 = ||c||_2 >=1`,                     (4.6)

so `S` has an eigenvalue of modulus at least one. If arbitrary outside coordinates/couplings are restored, Cauchy interlacing preserves separately the positive and negative threshold eigenvalue counts, hence the full matrix remains inside the exact owner target.

For the normalized physical pair

`B=[[0,1],[1,0]]`, so `D=kappa=1`,                            (4.7)

equation (4.5) becomes

`boxed:
 ||p_Q||_infinity <= 9*2^(1/6) ||c||_2^(-1/3).`              (4.8)

At `||c||=1` this is `10.102...`; its importance is the collective-coupling scaling. The previous r34 random-slope certificate was

`8/[2^(1/4)sqrt(||c||_2)] +2`,                               (4.9)

which can never go below `2`. In contrast (4.8) is below `2` whenever

`||c||_2 > 729 sqrt(2)/8 = 128.8702108...`.                  (4.10)

Thus the new fractional-trace compiler is strictly stronger in the sufficiently strong-bank regime, rather than a restatement of the preceding theorem.

## 5. Fragmentation stress test: why the active slope must be recoalesced

The homogeneity in (2.4) is also a precise proof-order test. Take the exact-target four-variable form

`Q_N = 2U_1U_2 + 2YW_N`,                                     (5.1)

where `U_1,U_2,Y` are arbitrary independent cap-one variables and `W_N` has density `1_(E_N)` with

`E_N = union_(j=1)^N [4^j,4^j+1/N]`.                         (5.2)

The coefficient matrix is the direct sum of two hyperbolic blocks, hence its spectrum is `{1,-1,1,-1}`. The whole `W_N` law has density cap `M=1`, so fleet02/B14 r36 plus Theorem 3.1 gives simply

`boxed: ||p_(Q_N)||_infinity <=9`,                            (5.3)

independently of `N` and despite exponentially separated fragments and diverging moments.

Now split the **active slope law itself** into its `N` unnormalized interval pieces. Each piece has mass `m_j=1/N` but density cap `L_j=1`, not `m_j`. The general fragment budget (3.10) then becomes

`9 sum_(j=1)^N 1^(1/3)(1/N)^(2/3)
 = 9 N^(1/3).`                                                (5.4)

Thus normalizing/paying active fragments first creates a genuine `N^(1/3)` certificate loss on a family whose whole-law bound stays `9`. This is a proof-interface obstruction, **not** a counterexample to QFORM. It exactly matches the principle established by the designated partner: whole-active smoothing must be paid before active fragment normalization.

Outside fragments are different. If an independent outside piece of mass `m_j` multiplies the whole `W_N` law, its unnormalized slope density cap is `m_j`, so (3.3) contributes `9m_j`; summing gives exactly `9`. This is the concrete distinction between safe outside localization and unsafe active normalization.

## 6. Relation to the partner's exact full-target extreme localization

Fleet02/B14 r36 already proves the target-level identity

`sup_(all cap-one product laws) Lambda(P,mu)
 = sup_(compact finite-fragment extreme product laws) Lambda(P,mu)`             (6.1)

for every fixed measurable `P`, and hence after the further suprema over every target quadratic form. Therefore arbitrary unbounded supports and tails may be removed **at the law-level worst-case problem with zero change in the optimal universal constant**.

Theorem 2.1 and Sections 3-5 explain how to preserve this zero-loss feature after entering a singular reciprocal/fractional-trace argument:

1. localization to extreme product laws is safe at the whole-law level;
2. active separated components must remain recoalesced while the product-projection/slope certificate is formed;
3. an independent outside decomposition is safe because its unnormalized cap carries the full mass factor `m_j`;
4. arbitrary fragment-dependent translations are harmless because the fractional kernel estimate (2.1) is translation-uniform;
5. no support radius or moment appears anywhere.

So the localization issue for this branch is fully explicit and quantitative rather than hidden inside a normalized conditional density.

## 7. What remains unpaid

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`.

The missing implication is now matrix-structural. From the bare condition `s_3(A)>=1`, before active normalization one must force either

- an invertible indefinite original-coordinate physical pair plus a protected slope statistic with a controlled whole-law density cap, to which (3.2)-(4.5) apply;
- or one of the existing whole-law ridge/volume/mixed-hub/grouped-bank exits;
- or a new positive-copy/fractional-trace estimate whose subprobability exponents sum to a full mass power in the sense of (2.2)-(2.4).

The present theorem does not force such a protected slope from `s_3(A)>=1`, and therefore is not a proof of the unrestricted conjecture. It also does not authorize pointwise quadratic Fourier decay, fixed support diameter, fixed fragment count, or post-rotation independence.

A useful next structural target is: in the surviving no-good-pivot/high-leverage states, prove a product-preserving dichotomy that either exposes a protected slope with `L<=mM` **before** conditioning on its active fragments, or exposes a whole-law volume/ridge certificate. Equation (3.10) is the exact quantitative ledger for any proposed decomposition.

## 8. Integrity/status

- Full QFORM: `OPEN`.
- New theorem: `QFORM-FRACTIONAL-TRACE-SUBPROBABILITY-LOCALIZATION-v1`, proved in Section 2.
- New partner-derived theorem: protected-slope cubic-root compiler (3.2)-(3.3), using completed fleet02/B14 r36 at an actual inequality.
- New target-valid corollary: arbitrary dense bank-curvature family (4.1) with bound (4.5).
- New proof-order stress test: exact-target remote-fragment family (5.1)-(5.4), whole-law constant `9` versus fragment-first certificate `9N^(1/3)`.
- No new counterexample to QFORM is claimed.
- Essential boundedness is what is established in these supporting branches; full-target continuity is not claimed.
