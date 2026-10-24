Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# C0031 — stretched-exponential hard-edge localization and sparse exceptional dimensions

## Source and cumulative input

Target: Charles Bordenave and Djalil Chafaï, *Around the circular law*, Probability Surveys 9 (2012), Section 6.6 after Theorem 6.2.  Under the general `0<alpha<2` stable-domain hypotheses, the source proves convergence in probability of the eigenvalue ESD and proves almost-sure convergence under an additional bounded-density assumption.  C0031 asks for the same almost-sure conclusion without that additional density hypothesis.

Write

`A_n(z)=a_n^{-1} X_n-zI`

in the source normalization, let `s_1,...,s_n` denote its singular values without imposing an ordering, and set

`F_{n,z}(t)=n^{-1} #{i:s_i<=t}`.

The previous R7-05 run proved, using the source intermediate-small-singular-value estimate plus bounded-variation concentration, that for constants `gamma>0`, `kappa=2alpha/(alpha+2)>0`, and

`c_* = gamma/kappa`,

one has for every fixed `z`, almost surely eventually,

`F_{n,z}(exp(-M_n)) <= C n^{-gamma}+C sqrt(log n/n)+o(1)`,      (1)

where `M_n=floor(c_* log n)`, and also the mesoscopic logarithmic-energy theorem

`lim_{J->infinity} limsup_{n->infinity}
 sum_{m=J}^{M_n} F_{n,z}(e^{-m}) = 0`                         (2)

almost surely.  Equivalently, the negative logarithm is already uniformly integrable from every fixed lower cutoff down to the polynomial scale `e^{-M_n} asymp n^{-c_*}`.

This artifact attacks only the remaining extreme hard edge.  The methods are B3 (prove a stronger scale-localized statement), B14 (identify the symmetry/arithmetic profile behind the source loss), and B29 (add the missing boundary point by testing square-vs-rectangular and three-step comparison routes).

## B3 — a stronger theorem: all logarithmic mass above a stretched-exponential floor is controlled

Define

`q_* = min(gamma,1/2)`.

### Theorem 1 (stretched-exponential hard-edge localization)

For every fixed `z` and every fixed `q` satisfying

`0<q<q_*`,

almost surely,

`lim_{J->infinity} limsup_{n->infinity}
 (1/n) sum_i log(1/s_i)
  1_{ e^{-n^q} <= s_i < e^{-J} } = 0`.                      (3)

Here the indicator automatically restricts to `s_i<1`, so every displayed logarithm is nonnegative.

### Proof

Split the interval in (3) at the already-controlled polynomial scale `t_n=e^{-M_n}`.

**Mesoscopic part.**  For `t_n<=s_i<e^{-J}`, the layer-cake/dyadic identity used in the preceding run bounds the normalized negative-log mass by the dyadic energy in (2), up to at most one endpoint bin.  Hence

`lim_{J->infinity} limsup_n
 (1/n) sum_i log(1/s_i) 1_{t_n<=s_i<e^{-J}}=0`               (4)

almost surely.

**Extreme-but-not-ultra-extreme part.**  If

`e^{-n^q}<=s_i<t_n`,

then `log(1/s_i)<=n^q`.  The number of such singular values is at most `n F_{n,z}(t_n)`.  Therefore

`0 <= (1/n) sum_i log(1/s_i)1_{e^{-n^q}<=s_i<t_n}
   <= n^q F_{n,z}(t_n)`.

Using (1),

`n^q F_{n,z}(t_n)
 <= C n^{q-gamma}
    + C n^{q-1/2} sqrt(log n)
    + o(n^q)`.

The first two displayed terms tend to zero because `q<gamma` and `q<1/2`; the `o(1)` in (1) comes from the exponentially small source good-event error and can be taken smaller than every fixed negative power after the same concentration construction, so its product with `n^q` also tends to zero.  Thus

`(1/n) sum_i log(1/s_i)1_{e^{-n^q}<=s_i<t_n} -> 0`           (5)

almost surely.  Combining (4) and (5) proves (3).  QED.

### Exact residual quantity

Define the ultra-hard-edge logarithmic defect

`U_{n,q}(z)
 = (1/n) sum_i log(1/s_i) 1_{s_i<e^{-n^q}}`.                (6)

Theorem 1 proves that **all remaining lower-log uniform-integrability difficulty is concentrated in `U_{n,q}(z)`**.  In particular, for any fixed `q<q_*`, the source endpoint follows through its existing Hermitization argument if, on one probability-one event, for Lebesgue-a.e. `z`,

`U_{n,q}(z) -> 0`.                                          (7)

A stronger but very concrete sufficient condition is the eventual stretched-exponential floor

`s_min(A_n(z)) >= e^{-n^q}`                                 (8)

for Lebesgue-a.e. `z` and some fixed `q<q_*`.

This is a genuine sharpening of the preceding polynomial-floor formulation.  A proof no longer needs to control the lower logarithm throughout all polynomial scales: the existing source machinery plus the previous R7-05 theorem automatically handles every singular value down to the much smaller scale `e^{-n^q}`.  Only singular values *below* that stretched-exponential scale remain.

### Corollary 1 (general deterministic subsequences)

Let `(n_j)` be any deterministic increasing sequence satisfying

`sum_j sqrt(log n_j/n_j) < infinity`.                        (9)

Then, under the full source hypotheses and without bounded density, the empirical eigenvalue measures converge almost surely to `mu_alpha` along `(n_j)`.

Indeed, the source weak-invertibility polynomial-floor failure bound is summable under (9), so Borel-Cantelli supplies the polynomial floor eventually on the subsequence; the preceding mesoscopic theorem then gives complete lower-log uniform integrability and the source Hermitization proof applies.  The earlier `n_j=ceil(j^p)`, `p>2`, theorem is the special case of (9).

## B14 — the nonsummable source loss is sparse in dimension even without independence

Let `E_n(z)` be the failure event for the fixed polynomial lower bound on `s_min(A_n(z))` furnished by the source weak-invertibility lemma in the normalization used above.  The source gives, for fixed `z`,

`P(E_n(z)) <= C sqrt(log n/n)`.                              (10)

The events may be strongly dependent across `n`; no independence is used below.

### Theorem 2 (dyadic sparsity of polynomial-floor failures)

For every fixed `z` and every `epsilon>0`, almost surely, for all sufficiently large integers `k`,

`#{n in [2^k,2^{k+1}): E_n(z)}
 <= C_epsilon 2^{k(1/2+epsilon)} sqrt(k)`.                   (11)

Consequently,

`#{n<=N:E_n(z)}
 = O_epsilon(N^{1/2+epsilon} sqrt(log N))`                   (12)

almost surely.

### Proof

Put

`K_k(z)=sum_{n=2^k}^{2^{k+1}-1} 1_{E_n(z)}`.

By (10),

`E K_k(z)
 <= C sum_{n=2^k}^{2^{k+1}-1} sqrt(log n/n)
 <= C' 2^{k/2} sqrt(k)`.

Markov's inequality therefore gives

`P(K_k(z)>2^{k(1/2+epsilon)}sqrt(k))
 <= C' 2^{-k epsilon}`.

The right side is summable in `k`, so Borel-Cantelli proves (11).  Summing the resulting dyadic estimates up to `log_2 N` proves (12), since the final dyadic scale dominates the geometric sum.  QED.

### What this does and does not prove

The source's nonsummable `sqrt(log n/n)` estimate therefore does **not** permit bad polynomial-floor dimensions to occupy a positive density of dimensions along a typical nested realization; they have zero density and satisfy the quantitative bound (12).  This uses no cross-dimension independence.

However, this still does not close C0031.  Even a single exceptional dimension can in principle contain a singular value with enormous logarithmic depth, for example far below `e^{-n^q}`.  Since the target is full-sequence almost-sure convergence rather than density-one convergence, sparsity of exceptional dimensions alone cannot replace a bound on `U_{n,q}(z)`.

### Arithmetic-profile diagnosis

The source Appendix-A weak invertibility argument contains a `n^{-1/2}`-scale loss originating in a Berry-Esseen concentration step.  Such a plateau is real for highly structured coefficient vectors: lattice sums with nearly equal coefficients may have point masses of order `n^{-1/2}`.  But the coefficient vector relevant to invertibility is a random normal vector to a random span, and modern least-singular-value arguments exploit arithmetic unstructure of that random normal through LCD/RLCD-type parameters.

The dated literature check shows why importing that technology is not automatic here.  Sharp square estimates such as Rebrova-Tikhomirov and Livshyts-Tikhomirov-Vershynin are built under finite-variance or Hilbert-Schmidt second-moment budgets, while C0031 allows fixed `alpha<2` stable-domain laws.  Random-rounding results weaken moment assumptions substantially, but their readily applicable fixed-law corollaries still do not simply cover a fixed infinite-variance stable-domain law at this normalization.

Theorem 1 turns this into a precise arithmetic milestone rather than a vague request for a better Berry-Esseen theorem: it is enough to prove a tail-robust random-normal anti-structure statement strong enough to rule out singular values below `e^{-n^q}` for one `q<q_*`, or more weakly to force the averaged defect (6) to vanish.  A route based on an LCD-like denominator would therefore need to show that the relevant random normals are overwhelmingly outside the structured set at denominator scale roughly `e^{n^q}`.  No such source-matching stable-domain theorem is proved here.

## B29 — test the boundary: square versus rectangular regularization and three-step comparison

### 1. Naive rectangular augmentation has the wrong monotonicity

A tempting idea is to append one or several independent rows and invoke a strong rectangular least-singular-value theorem.  This cannot by itself give a square lower bound.

If

`A_tilde = [ A ; r^* ]`,

then

`A_tilde^* A_tilde = A^*A + r r^* >= A^*A`

in the positive-semidefinite order.  Hence

`s_min(A_tilde) >= s_min(A)`.                               (13)

Thus a lower bound for the augmented rectangular matrix says only that the added row repaired every nearly-null square direction; it gives no lower bound on the original square matrix.  The inequality points in the wrong direction.  The same obstruction applies to direct attempts to import strict-aspect-ratio results by row augmentation.

This explains why Yi Han's very-high-confidence Lévy estimates for `N/n -> a>1`, even with deterministic rectangular deformation, and the almost-square estimates of Dabagia-Fernandez do not mechanically close the square endpoint.

### 2. Louvaris is close in scale but not in source scope

Louvaris proves square least-singular-value universality for exact symmetric stable-law matrices, for all tail exponents outside a countable exceptional set: after the source stable normalization, the least singular value is of order `N^{-1}` and has the Gaussian limiting law.  That scale is vastly larger than `e^{-N^q}`.  Therefore a source-matching extension of the relevant least-singular comparison to shifted matrices `D_N-zI` and to the full stable-domain class would be much more than enough for (8).

But the final least-singular theorem in that work is for the unshifted exact-stable model, not the arbitrary fixed shifts and general stable-domain distributions required by C0031.  I therefore do not import it as a solution.

### 3. The correct comparison target is now only the ultra-hard edge

Theorem 1 shows that a future three-step argument need not transport the entire singular-value process, nor even prove optimal least-singular universality.  It is enough to establish, for some `q<q_*` and for Lebesgue-a.e. fixed `z`, a summable tail such as

`sum_n P(s_min(A_n(z))<e^{-n^q}) < infinity`,                (14)

or an aggregate version that directly implies `U_{n,q}(z)->0`.  Under (14), Borel-Cantelli gives (8), Theorem 1 supplies the rest of lower-log uniform integrability, and the source Hermitization argument yields the full almost-sure ESD theorem.

This is a materially weaker comparison objective than proving exact hard-edge universality.  It is the most focused way found so far to use Louvaris-style three-step technology without re-solving the already-controlled mesoscopic spectrum.

## Literature/status check dated 2026-09-18 UTC

- Bordenave-Chafaï, arXiv:1109.3343 / Probability Surveys 9 (2012): source endpoint; general heavy-tail ESD convergence in probability, a.s. under bounded density, with small-singular-value control identified as the obstruction.
- Michail Louvaris, arXiv:2204.06399, later AIHP publication: square exact-stable unshifted least-singular universality (outside a countable exceptional set of alpha), plus small-energy singular-vector delocalization and Gaussian-perturbation local-law machinery.  This is relevant but narrower than C0031.
- Yi Han, arXiv:2412.06246: high-confidence least-singular bounds at the correct heavy-tail scale for strict rectangular aspect ratio `N/n -> a>1`, including fixed deterministic rectangular deformation; not the square hard edge.
- Max Dabagia and Manuel Fernandez, arXiv:2408.14389: strong rectangular/almost-square lower-tail estimates under moment or anti-concentration assumptions; not a direct square fixed-alpha-stable-domain solution.

A bounded fresh search did not expose a theorem that settles the full no-bounded-density Bordenave-Chafaï almost-sure endpoint.  This is negative evidence only, not a novelty or openness certificate.

## Metric and failure boundary

Frozen metric: `BC_AS`.

Before: `0`.

After: `0` (**NO MOVEMENT**).

The new results are strict partial progress: they reduce the unresolved lower logarithm from an unspecified sub-polynomial hard edge to the explicit ultra-hard-edge defect (6), prove that every scale above `e^{-n^q}` is harmless for any `q<min(gamma,1/2)`, and prove that the source polynomial-floor failures occur only on a quantitatively sparse set of dimensions almost surely.  They do not prove `U_{n,q}(z)->0`, do not prove a stretched-exponential floor for the full source class, and do not provide the required independent P26 plus OTHER-track audits.

This is the third consecutive ordinary C0031 run with the binary metric unchanged.  Per the owner protocol, the **next R7-05 run must be a thinking-only Section-I STUCK diagnosis**, not another ordinary lemma run.  That diagnosis must isolate the exact blocking formula `U_{n,q}`, list the failed routes and missing ingredient, identify the simplest unresolved source-valid case and nearest solved analogue, and select exactly one recovery action plus the next three B methods.
