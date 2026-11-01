Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# H0024 — scale-burst compensator theorem for the exact critical shell chain

Target: `H0024`, Gustavo Oshiro de Carvalho, Fábio Prates Machado, José Hermenegildo Ramírez-González, *Extinction and Survival in an Interval-Activation Frog Model on Z with Random Survival Parameters and Symmetric Random Walks* (2026), arXiv:2607.27082v1, Theorem 3.5(ii) / Remark 3.6.

Status: **PARTIAL / SOURCE OPEN**.  Frozen source metric remains `G_crit=1`; the strict constants were already matched.  This note attacks the equality-shell gluing problem left by `2026-09-18T070124Z__H0024_exact_critical_hyperbolic_shell_recurrence.md`.

Methods: **B3 / B12 / B30**.

The central idea is stronger than a one-step drift estimate.  On any trajectory that survives forever, the total projective shell mass `sum g_k/N_k` must diverge.  Every fresh site has order `1/N_k` probability to make a prescribed multiplicative-scale cross-interval jump.  Therefore the compensator for such jumps diverges on every surviving path.  Conditional Borel-Cantelli then forces jumps of *every fixed multiplicative scale* infinitely often.  In particular the fresh-shell ratio has limsup one on survival.

This is a pathwise theorem.  It uses only the exact critical `1/n` marginal tail and independence across fresh sites; the difficult same-frog left/right dependence never enters the lower bound.

---

## 1. Exact shell notation

Use the cumulative breadth-first shell chain already proved for H0024.  At generation `k`, the activated interval has span `N_k` and the newly activated shell has left/right widths `(ell_k,r_k)`.  Put

`g_k := ell_k+r_k` and `s_k := g_k/N_k`.

If the next extension is `(U_k,V_k)`, then

`g_{k+1}=U_k+V_k`,

`N_{k+1}=N_k+g_{k+1}`.                                      (1.1)

On nonabsorption, `g_k>=1`.  Because the previous activated interval is nonempty, `0<g_k<=N_k`, hence `0<s_k<=1`.

In the exact hyperbolic equality model from the preceding artifact,

`P(L>m)=P(R>m)=1/(m+2)`, `m>=0`.                              (1.2)

Here `L,R` are the left/right maximal displacements in one fresh site mark.  Site marks are independent from site to site, although `L` and `R` at one site are dependent.

The argument below actually needs only

`P(L>m)>=c_-/m`, `P(R>m)>=c_+/m`                               (1.3)

for all sufficiently large `m`, with fixed `c_-,c_+>0`; thus it applies to any source critical law whose site-level directional tails have positive `1/n` coefficients.  The exact model has `c_-=c_+=1` asymptotically and gives fully explicit constants.

---

# 2. B12 — the conserved scale clock

The deterministic span recursion already contains a useful cumulative identity.

### Lemma 2.1 (log-span clock)

For every nonabsorbed trajectory and every `K>=1`,

`log(N_K/N_0)=sum_{k=1}^K [-log(1-s_k)]`.                      (2.1)

Consequently, on every trajectory that survives forever,

`sum_{k>=1} s_k = infinity`.                                   (2.2)

### Proof

Since `g_k=N_k-N_{k-1}` for `k>=1`,

`N_{k-1}=N_k-g_k=N_k(1-s_k)`.

Therefore

`log N_k-log N_{k-1}=-log(1-s_k)`,

and summing proves (2.1).

On eternal survival the integer spans strictly increase at every generation, so `N_K->infinity`; hence the left-hand side of (2.1) diverges.  If `sum s_k<infinity`, then `s_k->0`; eventually `s_k<=1/2`, and on `[0,1/2]`

`-log(1-s)<=2s`.

The right side of (2.1) would then converge, contradiction.  Thus (2.2) holds. QED.

### Interpretation

`sum s_k` is the natural projective time of the shell chain.  The earlier one-sided revival hazard `g/(N+2)` is exactly of order `s`; Lemma 2.1 shows that its cumulative hazard can never remain finite on an infinite trajectory.

This is the conserved quantity sought by B12: not a state martingale, but an exact deterministic clock linking multiplicative span growth to accumulated shell ratio.

---

# 3. B3 — a stronger theorem: every surviving path has arbitrarily large multiplicative bursts

Fix an integer `M>=1`.  Call a fresh site **M-crossing** if its mark crosses the opposite old boundary and then extends at least an additional distance `M N_k` beyond that boundary.

For a left fresh site at translated position `j in {0,...,ell_k-1}`, it is enough that

`R > (M+1)N_k-j`.

Since `j>=0`, this threshold is at most `(M+1)N_k`.  Therefore in the exact model

`P(site is M-crossing | F_k) >= 1/((M+1)N_k+2)`.               (3.1)

The same bound holds for a right fresh site using `L`.  The directions differ on the two shell blocks, but the relevant site events are independent across the `g_k` fresh sites because site marks are independent.

Let `C_k^(M)` be the event that at least one of the `g_k` fresh sites is M-crossing during the transition from generation `k` to `k+1`.

### Lemma 3.1 (uniform scale-hazard lower bound)

For all sufficiently large `N_k`,

`P(C_k^(M) | F_k) >= c_M s_k`                                  (3.2)

with, for example, the explicit exact-model constant

`c_M=1/[4(M+1)]`.                                                (3.3)

### Proof

Put

`q_k=1/((M+1)N_k+2)`.

By independence across fresh sites,

`P(C_k^(M)|F_k) >= 1-(1-q_k)^(g_k) >= 1-exp(-g_k q_k)`.        (3.4)

For all sufficiently large `N_k`,

`q_k >= 1/[2(M+1)N_k]`.

Also `g_k q_k <=1/(M+1)<=1`.  For `0<=x<=1`, `1-e^{-x}>=x/2`.  Hence

`P(C_k^(M)|F_k)
 >= (g_k q_k)/2
 >= g_k/[4(M+1)N_k]
 = c_M s_k`.

QED.

### Lemma 3.2 (an M-crossing forces a macroscopic next shell)

On `C_k^(M)`,

`g_{k+1}>=M N_k`,

and therefore

`s_{k+1}=g_{k+1}/N_{k+1}
          =g_{k+1}/(N_k+g_{k+1})
          >= M/(M+1)`.                                         (3.5)

This is purely deterministic once the crossing occurs.

### Theorem 3.3 (scale-burst theorem)

In the exact hyperbolic critical H0024 model, conditional on eternal survival,

`C_k^(M)` occurs infinitely often almost surely for every fixed integer `M>=1`.  Consequently

`P( limsup_{k->infinity} g_k/N_k =1  | survival forever)=1`.    (3.6)

Equivalently, on every surviving trajectory, for every fixed multiplicative factor `A>1`, the activated span makes jumps by a factor at least `A` infinitely many times almost surely.

### Proof

On eternal survival, Lemma 2.1 gives

`sum_k s_k=infinity`.

For fixed `M`, Lemma 3.1 therefore gives

`sum_k P(C_k^(M)|F_k)=infinity`                                 (3.7)

on the survival event.  The fresh shell at generation `k` consists of sites whose marks have not yet been exposed.  Thus `C_k^(M)` is adapted to the next sigma-field and the usual Levy conditional Borel-Cantelli lemma applies: whenever the predictable sum (3.7) diverges, `C_k^(M)` occurs infinitely often almost surely.

By Lemma 3.2, every such occurrence forces

`s_{k+1}>=M/(M+1)`.

Hence for each fixed `M`,

`limsup_k s_k >= M/(M+1)`

almost surely on survival.  Intersecting these probability-one statements over the countable set `M=1,2,...` gives

`limsup_k s_k>=sup_M M/(M+1)=1`.

Since always `s_k<=1`, equality follows. QED.

### Corollary 3.4 (thin escape is impossible)

The scenario isolated in the preceding recovery run,

`g_k->infinity` and `g_k/N_k->0`,

has probability zero on eternal survival.  More strongly, *no* eventually thin-shell trajectory can survive forever in the exact equality model.

This closes the specific two-coordinate escape channel that remained after the negative projective-drift theorem.

### Corollary 3.5 (same-frog dependence is irrelevant for this obstruction)

The proof of Theorem 3.3 never factors the joint law of `(L,R)` at one site.  It uses one directional coordinate per site and only independence between different fresh sites.  Therefore any same-frog dependence allowed by the source cannot rescue an eventually thin surviving path.

---

# 4. B30 — dyadic localization and gluing across every projective scale

Theorem 3.3 may be restated as an annulus-by-annulus gluing theorem.

For `j>=1`, let

`A_j={2^{-(j+1)}<s<=2^{-j}}`.

Whenever the shell visits `A_j`, an M-crossing has conditional probability at least

`c_M 2^{-(j+1)}`                                                     (4.1)

for all sufficiently large spans.  Thus if the accumulated occupation

`T_j:=sum_k 1_{s_k in A_j}`

satisfies

`sum_j 2^{-j} T_j=infinity`,                                       (4.2)

then the total M-crossing compensator diverges.

But the log-span clock gives more directly

`sum_k s_k=infinity`,

and on `A_j`, `s_k` is comparable to `2^{-j}`.  Therefore (4.2) is exactly the scale-localized form of Lemma 2.1 up to universal constants.  No projective annulus can collectively hide enough occupation mass to keep every macroscopic-revival compensator finite.

This is the requested B30 gluing step: the local `O(s)` crossing hazard and the local shell-ratio clock glue across all dyadic scales with no loss of logarithms.  The earlier failure was not a missing constant in the one-sided drift; it was the absence of this pathwise occupation identity.

---

# 5. What this does and does not settle

The new theorem removes the exact blocker stated at the end of the preceding recovery run.  Eternal survival cannot occur through

`g_k->infinity`, `g_k/N_k->0`.

Instead, survival would have to display the much stronger burst behavior

`limsup g_k/N_k=1`.                                                (5.1)

Combined with the immediately preceding exact-equality artifact, the cumulative special-case picture is now:

1. the exact source-valid law `pi=sech(Exp(1))` has `P(D^+>=n)=1/(n+1)`;
2. the pure one-sided marginal shell chain is critical and absorbed almost surely;
3. the ideal two-log interior thin-shell limit is recurrent, not radially transient;
4. bounded shells cannot recur forever on survival;
5. eventually thin shells cannot survive forever (Theorem 3.3 here);
6. therefore every hypothetical surviving path must make arbitrarily large multiplicative span bursts infinitely often.

This is substantial structural progress, but it does **not** yet decide whether such a burst path has positive probability.  The remaining equality question has moved from a thin-shell Lamperti problem to a **burst-renewal problem**: decide whether the repeated span-scale explosions forced by (5.1) have a positive probability of renewing forever, or whether the cumulative chance of failure between explosions is one.

The full admitted source is broader still: random occupancy, stable walks, and nonconvergent slowly varying factors remain outside this exact special case.

No source-level closure, refutation, or novelty claim is made.

---

# 6. Metric / stagnation consequence

Frozen source metric:

`G_crit=C_surv/C_ext`.

Before: `1`.

After: `1`.

**NO MOVEMENT.**

The mathematical obstruction changed, but the source-matching first-order constant metric was already saturated.  This is the sixth ordinary no-movement H0024 iteration in the current CLOSABLE cycle when the immediately preceding `B7/B24/B28` artifact is counted as ordinary run five.  Therefore the owner protocol now requires an immutable H0024 handoff and rotation rather than another equivalent H0024 research run.

Useful carry-forward statement for any future independent work:

> In the exact source-valid hyperbolic equality model, every eternal-growth trajectory has `limsup g_k/N_k=1` almost surely.  The unresolved special-case question is purely whether the resulting forced burst-renewal mechanism survives with positive probability or dies almost surely.
