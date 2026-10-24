Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO FIXED-METRIC MOVEMENT: `W_3: 0.6565076662 -> 0.6565076662`; methods actually used: B5 / B20 / B24.**

# HARD7-06 bounded research iteration — the small cavity fixed-point branch is impossible

Status: **F0095 OPEN / HARD7-06 PARTIAL.** This run does not prove existence of the limiting ordinary Erdős--Rényi 3-colourability threshold. It makes a structural advance inside the Ayre--Coja-Oghlan--Greenhill variational route: of the two nonzero boundary-mass branches left by the previous exact cavity calculation, the entire small-positive-mass branch is impossible for any distributional cavity fixed point. Consequently every infinite-support convex-mixture local minimizer from the preceding HARD7-06 dichotomy is forced onto the single large-positive-mass branch

\[
q:=\Pr\{\Lambda>0\}\in(0.9319,0.9320),
\qquad
p_0:=\Pr\{\alpha=1\}\in(0.0680,0.0681).
\]

This is an exact theorem conditional only on the already-proved cavity fixed-point reduction; it is not finite sampling and it is not a claim of global optimality of the ACG functional.

Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity, ownership, exclusions, required reads

I resumed the admitted canonical target `F0095` and its create-only owner record `operations/claims/F0095.md`; I did not restart the original random-3-SAT candidate or the exhausted CKS predecessor. The retained external statement is Alan Frieze's ICM 2014 chromatic-number conjecture (ICM slides, PDF p. 82):

> **Conjecture.** There exists a sequence `d_k`, `k >= 2`, such that w.h.p. `chi(G_{n,d/n}) = k` for `d_{k-1} < d < d_k`.

HARD7-06 freezes the first small unresolved location case `k=3`: convergence of the ordinary sparse Erdős--Rényi 3-colourability transition to a constant average-degree location, not merely the known sharp threshold around an `n`-dependent location.

At run start I reread/recovered:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/F0095.md`;
- the newest own checkpoint `runs/hard7_2026-09-18/HARD7-06/2026-09-19T14-55-00Z__f0095_cavity_fixed_point_dichotomy.md`;
- the F-intake source file `probability_1000_intake_F_20260908/batches/b07_kalai_frieze.json` (connector rendering is truncated because the batch is large, so the exact F0095 row was cross-checked through the canonical claim and prior admission report rather than falsely claiming a complete all-line intake read);
- the newest relevant neighbouring ownership state, including R14's explicit negative-margin-perceptron handoff/rotation and HARD7-04's current random-graph duality track.

No release, conflicting F0095 owner, posted equivalent, or settled campaign entry was recovered.

## 2. Fresh bounded status search — 19 September 2026

I reran a bounded current-literature search rather than inheriting the previous status sentence.

- Achlioptas--Friedgut, *A Sharp Threshold for k-Colorability*, Random Structures & Algorithms 14 (1999), DOI `10.1002/(SICI)1098-2418(1999010)14:1<63::AID-RSA3>3.0.CO;2-7`, proves an `n`-dependent sharp threshold for fixed `k>=3`; it does not prove convergence of the `k=3` threshold location.
- Ayre--Coja-Oghlan--Greenhill, *Lower Bounds on the Chromatic Number of Random Graphs*, Combinatorica 42 (2022), DOI `10.1007/s00493-021-4236-z`, remains the rigorous interpolation/variational engine underlying the current explicit upper endpoint.
- Mizgerd--Perkins--Wang, *On the Chromatic Number of Random Triangle-Free Graphs*, Random Structures & Algorithms 68 (2026), DOI `10.1002/rsa.70081`, first published 6 June 2026, proves scaling-window results in a triangle-free conditioned model at a different density scale, not the ordinary `G(n,d/n)` fixed-`q=3` problem.
- A 2025--2026 search also recovered Gallai edge-colouring and other differently defined colouring problems, but no theorem closing the ordinary fixed-`q=3` constant-location question.

This is bounded negative evidence only, not a worldwide openness or novelty certificate. F0095 remains **OPEN**.

## 3. Frozen source-relevant metric: second consecutive no-movement run

The campaign quantity remains

\[
W_3:=U_3-L_3.
\]

The supported endpoints are

\[
L_3=4.03,
\qquad
U_3=4.6865076662,
\qquad
W_3=0.6565076662.
\]

This run changes neither endpoint:

\[
\boxed{W_3:0.6565076662\longrightarrow0.6565076662.}
\]

This is the **second** consecutive unchanged run after the latest endpoint-moving checkpoint. Section I therefore does not yet fire; a third unchanged run with the same remaining obligation must trigger the prescribed stuck protocol rather than more routine cavity algebra.

The useful auxiliary state does move: the number of scalar nonzero atom branches compatible with a full distributional cavity fixed point changes from **2 to 1**.

## 4. Carry-in theorem from the previous run

Use the exact transformed coordinate

\[
\Lambda=\frac{1-\alpha}{2+\alpha}\in[0,1/2].
\]

For a Poisson(`d`) cloud of iid incoming transformed messages, put

\[
P=\prod_i(1-\Lambda_i),
\qquad
Q=\prod_i(1-2\Lambda_i),
\]

and define the outgoing message

\[
\boxed{T=\frac{1-2P+Q}{2-P}.}
\tag{4.1}
\]

The previous on-page first-variation/analyticity argument proved:

> every convex-mixture local minimizer of the `q=3` ACG functional is either finitely supported or, if its support is infinite, its transformed law `mu` satisfies the exact recursive distributional equation `Law(T)=mu`.

It also proved that for any such nontrivial fixed point, with

\[
q=\Pr\{\Lambda>0\},
\]

Poisson thinning yields

\[
\boxed{q=1-e^{-dq}(1+dq).}
\tag{4.2}
\]

At the current certified degree

\[
d=4.6865076662,
\tag{4.3}
\]

the previous exact certificate exhaustively bracketed the two nonzero scalar roots as

\[
q\in(0.1388,0.1389)
\quad\text{or}\quad
q\in(0.9319,0.9320).
\tag{4.4}
\]

The present run asks whether both scalar roots can actually lift to full probability-law fixed points of (4.1).

## 5. B5 — add the first moment and obtain a universal nonzero lower bound

Let

\[
m:=\mathbb E\Lambda.
\]

Because `0<=P<=1`, the denominator in (4.1) obeys `2-P>=1`. Therefore

\[
T\le 1-2P+Q.
\tag{5.1}
\]

For a marked Poisson process the generating functional gives exactly

\[
\mathbb EP
=\exp\{d(\mathbb E(1-\Lambda)-1)\}
=e^{-dm},
\tag{5.2}
\]

and similarly

\[
\mathbb EQ=e^{-2dm}.
\tag{5.3}
\]

If `Law(T)=Law(Lambda)`, then taking expectations in (5.1) yields

\[
\begin{aligned}
m
&\le 1-2e^{-dm}+e^{-2dm}\\
&=(1-e^{-dm})^2.
\end{aligned}
\tag{5.4}
\]

For a nontrivial fixed point `m>0`, and `1-e^{-x}<x` for every `x>0`. Thus

\[
m<d^2m^2,
\]

so every nontrivial fixed point satisfies the strict necessary condition

\[
\boxed{m>\frac1{d^2}.}
\tag{5.5}
\]

At (4.3),

\[
\frac1{d^2}=0.04553038644294999\ldots.
\tag{5.6}
\]

This lower bound is distribution-free; it uses no finite support or numerical sampling.

## 6. B24 — solve the extremal outgoing-message problem at fixed positive-input count

The next step is to upper-bound the same first moment using only `q`.

Fix all incoming coordinates except one. Write

\[
A:=\prod_{j\ne i}(1-\lambda_j),
\qquad
B:=\prod_{j\ne i}(1-2\lambda_j),
\]

and regard `T` as a function of the remaining coordinate `x`. Direct differentiation of (4.1) gives a denominator that is strictly positive and numerator

\[
\boxed{AB+3A-4B.}
\tag{6.1}
\]

For each `u in [0,1/2]`,

\[
1-2u\le(1-u)^2.
\]

Multiplying over the other coordinates gives

\[
0\le B\le A^2\le1.
\tag{6.2}
\]

For fixed `A<=1`, expression (6.1) decreases as `B` increases because its `B` coefficient is `A-4<0`. Hence

\[
AB+3A-4B
\ge A^3+3A-4A^2
=A(A-1)(A-3)
\ge0.
\tag{6.3}
\]

Therefore **the cavity map is coordinatewise nondecreasing**.

Condition on exactly `K=k` positive incoming messages. The largest possible output is attained by setting every positive incoming message to the endpoint `1/2`. Then

\[
P=2^{-k},\qquad Q=0\quad(k\ge1),
\]

and hence, for `k>=2`,

\[
\boxed{t_k:=\max T\mid K=k
=\frac{2^k-2}{2^{k+1}-1}.}
\tag{6.4}
\]

In particular,

\[
t_2=\frac27,
\qquad
t_3=\frac25,
\qquad
t_k<\frac12\quad(k\ge4),
\tag{6.5}
\]

while `t_0=t_1=0`.

Under a fixed point, positive incoming messages form a thinned Poisson cloud,

\[
K\sim\operatorname{Poisson}(dq).
\]

Thus

\[
\boxed{
m\le
\frac27\Pr(K=2)
+\frac25\Pr(K=3)
+\frac12\Pr(K\ge4)
=:\overline M(dq).}
\tag{6.6}
\]

The payoff in (6.6) is nondecreasing in `K`, so `\overline M(a)` is nondecreasing in the Poisson mean `a` by the standard monotone coupling `K_{a'}=K_a+K_{a'-a}` for `a' >= a`.

## 7. B20 — the small scalar atom root fails the full fixed-point consistency test

The small scalar branch in (4.4) obeys

\[
q<0.1389<0.14.
\tag{7.1}
\]

By monotonicity of (6.6), it therefore suffices to evaluate the upper envelope at

\[
q_{\rm cap}=0.14,
\qquad
a_{\rm cap}=dq_{\rm cap}=0.656111073268.
\tag{7.2}
\]

Writing `a=a_cap`, (6.6) simplifies to

\[
\overline M(a)
=\frac12-e^{-a}C(a),
\tag{7.3}
\]

where

\[
C(a)
=
\frac12\left(1+a+\frac{a^2}{2}+\frac{a^3}{6}\right)
-\frac27\frac{a^2}{2}
-\frac25\frac{a^3}{6}.
\tag{7.4}
\]

The exact checker described below proves, using rational arithmetic and a rigorous lower enclosure for `e^{-a_cap}`,

\[
\boxed{
\overline M(a_{\rm cap})
<0.04397661203447906
<0.04553038644294999
=\frac1{d^2}.}
\tag{7.5}
\]

Now suppose a full cavity fixed point belonged to the small branch. Equations (6.6)--(7.5) would give

\[
m<\frac1{d^2},
\]

whereas the universal fixed-point condition (5.5) gives

\[
m>\frac1{d^2}.
\]

Contradiction.

### Theorem 7.1 — small-branch exclusion

At `d=4.6865076662`, there is **no nontrivial probability law on `[0,1/2]`** satisfying the cavity RDE (4.1) with

\[
q=\Pr\{\Lambda>0\}\in(0.1388,0.1389).
\]

Therefore every nontrivial cavity fixed point at this degree must satisfy

\[
\boxed{q\in(0.9319,0.9320).}
\tag{7.6}
\]

Equivalently, in the original `alpha` coordinate,

\[
\boxed{
\Pr\{\alpha=1\}=1-q\in(0.0680,0.0681).}
\tag{7.7}
\]

Combining this with the previous finite-support/fixed-point dichotomy gives the source-relevant structural consequence:

> every **infinite-support convex-mixture local minimizer** of the `q=3` ACG functional at the current certified degree has its `alpha=1` boundary atom in the single interval `(0.0680,0.0681)`.

No assertion is made that such an infinite-support minimizer exists, that a cavity fixed point is second-order stable, or that the global minimizer cannot be finitely supported.

## 8. Exact checker and idea-before-code ordering

The mathematical route was written before checker code at

`artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T15-47-00Z__f0095_small_branch_exclusion_idea.md`

creation commit

`7b5a6c841e438b731b63ea0c247cc3bc7e935585`.

Only after that was the finite/transcendental sign check written at

`artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T15-47-00Z__f0095_small_branch_exclusion_exact.py`

creation commit

`3d98cf8f0ed2055748f251a92f0824db0f07339b`.

The checker uses `fractions.Fraction`. To upper-bound (7.3), it upper-bounds `e^{a_cap}` by its positive Taylor series through order 8 plus a geometric tail bound and then reciprocates, giving a rigorous lower bound on `e^{-a_cap}`. Every deciding comparison is rational. The archived output is

`artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T15-47-00Z__f0095_small_branch_exclusion_exact.out`

creation commit

`39436450f31c1775dc3b7b5dafa04f642e38fab4`.

It records

```text
Mbar_upper_decimal = 0.04397661203447906
1/d^2_decimal = 0.04553038644294999
strict_margin_decimal = 0.0015537744084709276
small_root_upper_0.1389_lt_qcap = True
ALL_EXACT_CHECKS_PASS = True
```

This is a **self-check**, not an independent audit. The theorem-sized argument is written on the page above.

## 9. What the three new methods actually accomplished

**B5 — ADD A PARAMETER AND DIFFERENTIATE / track it.** The first moment `m=E Lambda` gives a new scalar consistency condition. Every nonzero RDE solution must have `m>1/d^2`; this is the lower half of the contradiction.

**B24 — FIND THE EXTREMAL OBJECT.** The exact derivative (6.1) proves that, at fixed number of positive inputs, the outgoing message is maximized by putting every positive input at `1/2`. This turns an arbitrary probability-law problem into the explicit Poisson envelope (6.6).

**B20 — FIND WHY THE ALGORITHM FAILS.** The smaller root of the atom-only recursion is a scalar false positive: it solves the positivity-count equation but cannot satisfy the full message-distribution recursion because its maximum possible first moment lies below the universal fixed-point minimum. This explains precisely why atom-count iteration alone is insufficient.

The natural remaining mathematical obligation is now narrower: determine whether the surviving large-q RDE branch can satisfy the **second-variation/local-minimum condition**, or else prove a global finite-support theorem for the ACG minimizer. The next run must use a different triple; a natural candidate is **B6 / B13 / B15** (deform from the surviving branch, search for a monotone stability quantity, and break the symmetric/fixed-point ansatz deliberately).

## 10. Capability honesty

The runtime identifies the model as **GPT-5.6 Sol**. The reasoning-effort level is **UNVERIFIED**. I therefore do not claim GPT-6 maximum.

The exposed automation interface still provides title/prompt, schedule/timing mode and enabled state, but no authenticated model-family selector, reasoning-effort selector, or guaranteed execution duration. GPT-6/maximum remains prompt-requested only. Changing this requires the platform to expose such controls or an authorized product/support path; a repository edit cannot do it.

Historical `You cannot modify this task` failures must not be bypassed. The current root ledger records that P26 was later editable from another authorized native context, so the compliant workaround for a denied task is the owning/authorized context or platform support, not creating a duplicate schedule. This run does not modify any schedule.

## 11. Ledger delta for the designated shared-root maintainer

```yaml
track: HARD7-06
canonical_target: F0095
status: PARTIAL
source_status: OPEN
metric: W_3
before: 0.6565076662
after: 0.6565076662
movement: none
unchanged_streak_after_latest_movement: 2
methods: [B5, B20, B24]
auxiliary_structural_quantity: full_cavity_nonzero_q_branches
auxiliary_before: 2
auxiliary_after: 1
new_result: >-
  At d=4.6865076662 the small scalar atom branch q in
  (0.1388,0.1389) cannot lift to a probability-law fixed point of the exact
  q=3 cavity RDE. Every nontrivial cavity fixed point must instead have
  q in (0.9319,0.9320), equivalently alpha=1 boundary mass in
  (0.0680,0.0681).
closure: false
independent_audits: 0
```
