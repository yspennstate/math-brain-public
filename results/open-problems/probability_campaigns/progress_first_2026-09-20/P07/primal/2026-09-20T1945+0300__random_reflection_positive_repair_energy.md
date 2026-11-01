Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum reasoning was requested as an owner preference, but authenticated completed-run effort telemetry is unavailable, so I do not claim otherwise.

# P07-A — random-reflection normal form and a positive-repair energy criterion

**Status:** **OPEN / PROVED PARTIAL** on Randomstrasse101 Conjecture 18.  
**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`.  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`.  
**Captured pre-write master:** `47564291654993a2f0c9eac50834ed58a51d12eb`.  
**Previous own substantive checkpoint:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1845+0300__orthogonal_core_mass_variance_bridge.md`.  
**Complementary role boundary:** P07-B owns the Fourier-dual / exceptional-frequency / quadratic-interpolation route. This report uses only the primal orthogonal-core LP and positive-orthant geometry; it does not duplicate P07-B's interpolation program.

**Outside target:** Bandeira et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18.  
**Primary partial-result paper:** A. S. Bandeira, J. Błasiok, D. Dmitriev, U. Faure, A. Kireeva, D. Kunisky, *The Lovász number of random circulant graphs*, arXiv:2502.16227.  
**Exact source model:** odd `n`; with `m=(n-1)/2`, each nonzero conjugate difference pair is selected independently with probability `1/2`.  
**Endpoint:**

`E theta(G_n) = (1+o(1)) sqrt(n)`.

A bounded source check on 20 September 2026 again found arXiv:2502.16227 stating that the exact asymptotics remain open and retaining the upper scale `O(sqrt(n log log n))`; the Randomstrasse collection still records the sharp-constant target. No later source-matching sharp-constant proof appeared in this bounded check. This is not a worldwide novelty certificate.

The fixed full-source metric remains

`alpha_LL = 1/2 -> 1/2`.

Nothing below is represented as a proof of the full conjecture.

---

## 0. Preserved predecessor handoff: SRG69 remains OPEN / PARTIAL

The reassigned predecessor remains archived under

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/SHPECTOROV-ZHAO-2026-SRG69/`

with frozen `R_SRG69=1`, status **OPEN / PARTIAL**. Preserve its no-Cayley theorem, rooted `L/B/C` feasibility system, centered spectral transfer, endpoint/cycle filters, moment and Gram reductions, low-rank residual work and star-complement handoff. Nothing in this report edits that root or calls SRG69 solved.

---

# 1. Inherited orthogonal-core reduction

Let

`M={1,...,m}`, `m=(n-1)/2`,

and

`C_ab = cos(2 pi a b/n)`.

The preceding P07-A run introduced

`Q=(2/sqrt(n)) C`,

`P=J/m`,

`rho=1-1/sqrt(n)`,

`O=Q-rho P`.

For every odd `n`,

`O^T=O`, `O^2=I`, `O 1=-1`.

For `D subset M`, define the exact core mass

`S_D = min { 1^T u : O_D u = -1_D, u>=0 }`.            (1.1)

The previous report proved

`S_D + S_{D^c}=m`,                                      (1.2)

and the exact theta scalarization

`theta_D/sqrt(n)
 = (1-lambda S_D)/(1-lambda(m-S_D))`,                   (1.3)

where

`lambda = 2/(sqrt(n)(sqrt(n)+1))`.                      (1.4)

Under the fair source mask,

`E S_D = m/2`,                                          (1.5)

and

`0 <= E theta_D/sqrt(n)-1
   <= [8/(sqrt(n)(sqrt(n)+1)^2)] Var(S_D)`.             (1.6)

Thus `Var(S_D)=o(n^(3/2))` is sufficient for Conjecture 18. The present run replaces the abstract variance target by a positive-orthant repair problem for a random signed orthogonal reflection.

---

# 2. New exact random-reflection normal form

Let

`epsilon_a = +1` if `a in D`, and `epsilon_a=-1` otherwise,

so `epsilon in {+1,-1}^m` is an iid Rademacher vector under the exact source law. Let

`E_D = diag(1_D)`

and define

`boxed( R_epsilon := O diag(epsilon) O. )`              (2.1)

Because `O` is symmetric orthogonal and `diag(epsilon)^2=I`,

`boxed( R_epsilon^T=R_epsilon,   R_epsilon^2=I. )`      (2.2)

Define the row-space projections

`Pi_D := O E_D O`,

`Pi_A := O(I-E_D)O`, where `A=D^c`.                     (2.3)

Since `E_D=(I+diag(epsilon))/2`, one gets the exact reflection splitting

`boxed( Pi_D=(I+R_epsilon)/2,   Pi_A=(I-R_epsilon)/2. )` (2.4)

Thus the random source mask does not merely select rows: after conjugation by the deterministic cosine core it produces a **random symmetric involution**, whose `+1` and `-1` eigenspaces are exactly the selected and unselected row spans.

Now put

`boxed( p_D := Pi_D 1. )`                               (2.5)

Using `O1=-1` and `epsilon=2 1_D-1`,

`O epsilon = 2 O1_D + 1`,

hence

`boxed( p_D = (1-O epsilon)/2. )`                       (2.6)

Similarly

`boxed( p_A = Pi_A1 = 1-p_D = (1+O epsilon)/2. )`       (2.7)

The radial data of the two complementary masks therefore come from one near-flat orthogonal Rademacher transform `O epsilon`.

## Theorem P07-A.45 — the signed minimum-norm solution is explicit

For every odd `n` and every mask `D`, `p_D` is the unique minimum-Euclidean-norm signed solution of

`O_D u = -1_D`.                                         (2.8)

Moreover

`boxed( ||p_D||_2^2=d,   1^T p_D=d, )`                  (2.9)

where `d=|D|`.

### Proof

The rows of `O_D` are orthonormal. Therefore the minimum-norm solution to `O_Du=-1_D` is

`-O_D^T 1_D`.

But

`Pi_D1=O_D^TO_D1=-O_D^T1_D`,

because `O_D1=-1_D`. Hence the minimum-norm solution is `p_D`.

Since `Pi_D` is an orthogonal projection,

`||p_D||^2 = 1^T Pi_D1 = ||O_D1||^2 = d`,

and the same displayed scalar is `1^Tp_D=d`. QED.

This theorem is exact for every odd `n`; no prime assumption or probabilistic approximation enters.

---

# 3. New exact orthant-repair form of the theta LP

The equality constraints in the core LP fix only the selected-row projection.

## Theorem P07-A.46 — every positive feasible point is a repair of `p_D`

A vector `u` satisfies

`O_Du=-1_D`

if and only if

`boxed( u=p_D+h,   h in range(Pi_A). )`                 (3.1)

Consequently

`boxed(
S_D
 = d + min { 1^T h : h in range(Pi_A), p_D+h>=0 }.
)`                                                       (3.2)

### Proof

The equality `O_Du=-1_D` is equivalent, after multiplying by `O_D^T`, to

`Pi_Du=p_D`.

Hence `u-p_D` belongs to `ker(Pi_D)=range(Pi_A)`. The converse is immediate. Finally `1^Tp_D=d` by (2.9). QED.

This is the structural point of the run. The full positive LP is now:

1. start from the explicit signed point `p_D=(1-O epsilon)/2`;
2. move only in the complementary eigenspace of `R_epsilon`;
3. enter the nonnegative orthant;
4. minimize the radial mass of that repair.

The complement problem is the same geometry with `epsilon -> -epsilon`.

---

# 4. Least-energy positive repair and an exact two-sided sandwich

Define the **least-energy positive repair**

`boxed(
mathcal E_D
 := min { ||h||_2^2 : h in range(Pi_A), p_D+h>=0 }.
)`                                                       (4.1)

This quantity is always finite because `h=p_A` is feasible:

`p_D+p_A=1>0`.

Hence

`0 <= mathcal E_D <= ||p_A||^2 = m-d`.                  (4.2)

It is important that `mathcal E_D` does **not** minimize the theta objective. It is an auxiliary geometric quantity used to construct an objective sandwich from both a mask and its complement.

## Theorem P07-A.47 — repair-energy sandwich

For every odd `n` and every mask `D`, writing `A=D^c`,

`boxed(
 -sqrt(d mathcal E_A)
 <= S_D-d
 <= sqrt((m-d) mathcal E_D).
)`                                                       (4.3)

Consequently

`boxed(
(S_D-d)^2
 <= (m-d) mathcal E_D + d mathcal E_A.
)`                                                       (4.4)

### Proof

Let `h_D` attain (4.1). Then `p_D+h_D` is core-feasible, so by (3.2),

`S_D-d <= 1^T h_D`.

Because `h_D in range(Pi_A)`,

`1^T h_D = <Pi_A1,h_D> = <p_A,h_D>`.

Cauchy-Schwarz and `||p_A||^2=m-d` give

`S_D-d <= sqrt((m-d) mathcal E_D)`.

Apply the same inequality to the complementary mask `A`:

`S_A-(m-d) <= sqrt(d mathcal E_A)`.

Using `S_A=m-S_D`, this becomes

`d-S_D <= sqrt(d mathcal E_A)`,

which is the lower side of (4.3). If a scalar lies in `[-a,b]`, then its square is at most `a^2+b^2`; this gives (4.4). QED.

This is a genuine gain over using an arbitrary primal repair alone: complement conservation converts two one-sided feasible constructions into a two-sided estimate for the **optimal** core mass.

---

# 5. Main new probability reduction: only sub-square-root mean repair energy is needed

Under the fair source law, `A=D^c` has the same distribution as `D`. Averaging (4.4) and changing `D <-> A` in the second term gives

`E (S_D-d)^2
 <= 2 E[(m-d) mathcal E_D]
 <= 2m E mathcal E_D`.                                  (5.1)

Since `d~Bin(m,1/2)`,

`E(d-m/2)^2=m/4`.                                       (5.2)

By `(x+y)^2 <= 2x^2+2y^2`,

`Var(S_D)
 = E(S_D-m/2)^2
 <= m/2 + 4m E mathcal E_D`.                            (5.3)

Combining with the exact expectation bridge (1.6) yields the main criterion of this run.

## Theorem P07-A.48 — positive-repair energy criterion for Conjecture 18

For every odd `n` in the exact fair random-circulant source model,

`boxed(
0 <= E theta(G_n)/sqrt(n)-1
 <= [(sqrt(n)-1)/(sqrt(n)(sqrt(n)+1))]
    [2 + 16 E mathcal E_D].
)`                                                       (5.4)

In particular,

`boxed(
E mathcal E_D = o(sqrt(n))
  => E theta(G_n)=(1+o(1))sqrt(n).
)`                                                       (5.5)

A uniform or expected `O(1)` repair-energy theorem would give the much stronger quantitative gap `O(n^(-1/2))` in the normalized expectation.

### Proof

Insert (5.3) into (1.6). Since `m=(n-1)/2`,

`[8/(sqrt(n)(sqrt(n)+1)^2)]*(m/2)
 = 2(sqrt(n)-1)/(sqrt(n)(sqrt(n)+1))`,

and

`[8/(sqrt(n)(sqrt(n)+1)^2)]*(4m E mathcal E_D)
 = 16(sqrt(n)-1)/(sqrt(n)(sqrt(n)+1)) E mathcal E_D`.

This is (5.4); (5.5) follows. QED.

The threshold `o(sqrt(n))` is deliberately weak. The new obligation is no longer concentration of theta, an RIP theorem, or even `O(1)` conditioning of every adaptive submatrix. It is only an **average squared distance needed to repair one explicit signed point into the orthant along the complementary random eigenspace**.

---

# 6. New exact dual formula: repair energy is a positive-cone transversality quotient

The quadratic program (4.1) has a useful exact dual. Write `p=p_D`, `P=Pi_A`.

Minimizing `(1/2)||h||^2` over `h in range(P)` subject to `h+p>=0`, with multiplier `q>=0`, gives the dual

`max_{q>=0} { -q^Tp - (1/2)||Pq||^2 }`.                (6.1)

Strict feasibility holds because `p+p_A=1>0`, so strong duality applies. Optimizing the scale of a fixed nonnegative direction `q` gives:

## Theorem P07-A.49 — exact cone quotient

`boxed(
mathcal E_D
 = sup_{q>=0, Pi_A q != 0}
   [(-q^T p_D)_+]^2 / ||Pi_A q||_2^2.
)`                                                       (6.2)

The convention is that a zero numerator contributes zero. There is no problematic positive-numerator / zero-denominator direction: if `Pi_Aq=0`, then `q in range(Pi_D)` and

`q^Tp_D=<q,Pi_D1>=q^T1>=0`

for `q>=0`.

Substituting the reflection identities (2.4) and (2.6), all factors of `2` cancel and (6.2) becomes

`boxed(
mathcal E_D
 = sup_{q>=0}
   [ <q,O epsilon-1>_+ ]^2
   / ||(I-R_epsilon)q||_2^2.
)`                                                       (6.3)

Thus the remaining primal problem is a **positive-cone restricted transversality problem for the random involution** `R_epsilon=O diag(epsilon)O`.

This is substantially narrower than controlling the smallest singular value of a general subsampled Fourier matrix. Only nonnegative vectors matter, and among them only vectors whose selected-space projection points against the explicit radial vector `p_D` matter.

---

# 7. New exact alignment-minus-spread formula

The cone quotient admits an even sharper geometric form. Since

`p_D + p_A = 1`,

for every `q>=0`,

`-q^Tp_D
 = q^Tp_A - ||q||_1
 = <Pi_Aq,p_A> - ||q||_1`.                              (7.1)

Also

`||p_A||_2=sqrt(m-d)`.                                  (7.2)

For `Pi_Aq != 0`, let `phi_A(q)` be the angle between `Pi_Aq` and `p_A`. Dividing (7.1) by `||Pi_Aq||` and using (6.2) gives:

## Theorem P07-A.50 — radial alignment versus positive-vector spread

`boxed(
sqrt(mathcal E_D)
 = sup_{q>=0, Pi_Aq != 0}
   [
      sqrt(m-d) cos(phi_A(q))
      - ||q||_1/||Pi_Aq||_2
   ]_+.
)`                                                       (7.3)

This formula isolates the only dangerous geometry. A large repair cost requires **simultaneously**:

1. `Pi_Aq` nearly aligned with the single radial direction `p_A`; and
2. `q` unusually concentrated in `l1/l2` relative to its complementary projection.

Generic transverse near-kernel vectors do not enter (7.3).

Define the effective support

`k_eff(q):=(||q||_1/||q||_2)^2`.                        (7.4)

Because `||Pi_Aq||_2 <= ||q||_2` and `cos(phi)<=1`, any witness to

`mathcal E_D >= L^2`                                    (7.5)

must satisfy

`boxed(
k_eff(q) <= (sqrt(m-d)-L)^2.
)`                                                       (7.6)

So a large repair-energy tail is automatically a **positive-vector localization event**. For example, repair energy of order `sqrt(n)` would require an effective-support deficit of order `n^(3/4)` from the critical complement dimension. This is not yet a probability bound, but it is a deterministic localization theorem that narrows the next source-specific estimate.

---

# 8. Why this is different from the earlier square-basis / hinge route

The preceding prime-order work tried to repair explicit hinge supports through square or slightly rectangular cosine systems. That asked for quantitative inverse control on an adaptively selected coordinate set.

The present reduction does not choose a support and does not require a uniform inverse. It allows the entire positive orthant and asks only for

`E mathcal E_D=o(sqrt(n))`,                              (8.1)

where `mathcal E_D` is the one-point orthant-repair energy in the complementary eigenspace. The exact dual (7.3) shows why this can be much weaker than RIP: only radially aligned positive cone directions can make the repair expensive.

The source's random bit vector enters only through

`g_D := O epsilon`,                                     (8.2)

with

`p_D=(1-g_D)/2`,

and through the conjugated sign reflection

`R_epsilon=O diag(epsilon)O`.                           (8.3)

The entries of `O` satisfy the inherited near-flat bound

`max_ab |O_ab| <= 2/sqrt(n)+2/n`,                       (8.4)

so each coordinate of `g_D` is a unit-variance Rademacher sum with vanishing maximal coefficient. This is the correct setting for a source-specific invariance / positive-cone comparison, but the adaptive supremum in (7.3) still has to be controlled. I do **not** replace that missing step by a Gaussian heuristic.

---

# 9. Self-checks and a rejected shortcut

The identities (2.4)--(2.9), the repair sandwich (4.3)--(4.4), and strong-duality formula (6.2) were checked numerically on all masks for small odd orders and against independent primal/dual quadratic programs. The primal and dual repair energies agreed to numerical tolerance.

A tempting shortcut would be to assert that `S_D` is uniformly `O(1)`-Lipschitz in one source bit and apply bounded differences. That statement is false: small exact instances already exhibit one-row core-mass jumps larger than `1` (and, for composite small order, larger than `3`). No such Lipschitz claim is used here. The repair-energy criterion avoids that false route.

These computations are only self-checks; no finite numerical value is represented as an arbitrary-`n` theorem.

---

# 10. Remaining gap and next concrete attack

The strongest new exact reduction is

`E mathcal E_D=o(sqrt(n))`                              (10.1)

with

`mathcal E_D
 = sup_{q>=0}
   [<q,O epsilon-1>_+]^2 / ||(I-O diag(epsilon)O)q||^2`. (10.2)

The next primal attack is to prove (10.1) directly by splitting the positive directions in (7.3) according to effective support.

**Localized sector.** Use the deterministic implication (7.6). A large repair cost forces a positive vector with effective support substantially below `m-d`. On prime orders, combine the existing Chebotarev/uncertainty support obstruction with a quantitative small-ball estimate for `Pi_Aq` on this localized positive cone. The desired statement is much weaker than a global restricted-isometry theorem because the numerator additionally enforces radial anti-alignment.

**Diffuse sector.** If `k_eff(q)` is close to `m-d`, then (7.3) already leaves little room for a large value. Quantify this by a radial alignment net rather than an all-directions net. The source-specific target is an `L^2` tail estimate for the supremum in (7.3), not operator-norm control of the full random Fourier restriction.

A sufficient next lemma is:

`boxed(
E [ sup_{q>=0, Pi_Aq!=0}
    ( sqrt(m-d) cos(phi_A(q))
      - ||q||_1/||Pi_Aq|| )_+^2 ]
 = O(polylog(n)).
)`                                                       (10.3)

Even `o(sqrt(n))`, rather than `O(1)`, closes the expectation conjecture through Theorem P07-A.48.

This remains a primal/structural task. P07-B should continue independently on its Fourier-dual / interpolation bottleneck and may use Theorems P07-A.45--P07-A.50 as exact shared lemmas without duplicating this positive-cone program.

---

## Ledger delta

- full-source status: **OPEN / PROVED PARTIAL**;
- fixed headline metric: `alpha_LL: 1/2 -> 1/2`;
- new exact all-odd-`n` structure: random reflection `R_epsilon=O diag(epsilon)O` and signed point `p_D=(1-Oepsilon)/2`;
- new exact orthant form: every feasible core primal is `p_D+h` with `h` in the complementary eigenspace;
- new source-valid sufficient condition: `E mathcal E_D=o(sqrt(n))`;
- new exact dual: `mathcal E_D` is a positive-cone transversality quotient;
- new localization: large repair energy forces low effective support plus radial alignment;
- remaining gap: prove the source-random positive-cone tail estimate (10.3), then feed it into the exact expectation bridge;
- SRG69 preserved **OPEN / PARTIAL**, no historical overwrite.
