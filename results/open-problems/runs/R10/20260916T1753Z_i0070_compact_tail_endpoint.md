Model: GPT-5.6 Sol. Reasoning: UNVERIFIED — NO METRIC MOVEMENT (`theta_* = 1/2` as a supremum before and after; endpoint `1/2` not claimed). Scope movement: one special critical model -> a full-source proof candidate under the exact p=2 Hilbert/Theorem-5.7 hypotheses. New Section-B methods actually used: **11 (DUALIZE / operator perturbation), 18 (SAY IT IN ANOTHER LANGUAGE), 24 (FIND THE EXTREMAL OBJECT)**.
Problem/source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561v5 / NoDEA 32 (2025), Article 123, Problem 6 (“Time regularization in Hilbert spaces”). Campaign status: **PARTIAL**. Claim `R10-I0070-C003` below is an author-side full-source proof candidate, but it is **not called CLOSED** before the required two independent OTHER-track audits and prior-art clearance.

# R10 I0070 — compact Hilbert tails turn the critical endpoint into a small linear perturbation

Run ID: `20260916T1753Z_i0070_compact_tail_endpoint`  
Repository/branch: `yspennstate/math-open-problems` / `master`  
Dated source/status check: 2026-09-16

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler mutation, peer-file edit, or shared-root edit was performed.

## 1. Continuity, ownership, whole-repository resume, and admission

I continued from the newest immutable R10 report rather than restarting:

`runs/R10/20260916T1636Z_i0070_critical_hilbert_special.md`.

That report established the source conclusion for one genuinely critical bounded-diffusion model and moved the fixed metric from `UNMEASURED` to

`theta_* = 1/2` as a supremum (all `theta<1/2`, endpoint not claimed).

This run does **not** reset that metric. The numeric metric is unchanged; the substantive movement is the scope of the proof.

Before research I read the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the I0070 claim, the newest R10 report, the newest neighboring Agresti–Veraar P24 report, and the current R11 report. The GitHub connector cannot literally materialize all roughly 780 JSONL intake rows into model context in one run, so full row-by-row intake traversal remains ACCESS-LIMITED; I do not pretend otherwise. I0070 itself was rechecked by claim/search/source.

`operations/claims/I0070.md` still reserves I0070 exclusively to R10 and still says `PENDING_ADMISSION, not READY`. The research-side admission evidence is now complete:

1. outside source and exact current statement recovered;
2. current v5/published source still prints Problem 6;
3. later-author and citing-paper search refreshed below;
4. no competing owner found; P19 explicitly declined I0070 because R10 owns it;
5. P24 is on distinct Agresti–Veraar Problem 3;
6. Problems 4–5 remain excluded/already packaged;
7. the retired Cardy route remains preserved in its immutable R10 history and is not reopened.

I do not mutate coordinator-owned claim/root files. The coordinator/P26 can reconcile the stale `PENDING_ADMISSION` label from this evidence.

## 2. Exact source statement — no strengthened hypotheses

The current survey v5 (dated 27/28 August 2025; NoDEA publication 1 September 2025) states in Theorem 4.7 that for `p=2`, `kappa=0`, Assumption 4.1 and

`(A,B) in SMR^bullet_{2,0}`

give a maximal solution `(u,sigma)` satisfying on every localizing interval

`u in L^2(0,sigma_n;X1) cap C([0,sigma_n];X_{1/2})` a.s.

Here `X0` is Hilbert in Problem 6, hence `X1=D(A)` with the graph norm and the trace space

`H := X_{1/2,2}`

are Hilbert; for a Hilbert couple the real `q=2` and complex midpoint spaces agree up to equivalent norms.

Theorem 5.7 assumes, in addition to Theorem 4.7:

- the growth condition (5.21), with exactly the source `X_{1-1/p,infinity}` bound and the same `X_{beta_j,1}` norms;
- `(A,B) in SMR^bullet_{r,alpha}` for every `r>2` and `alpha in [0,r/2-1)`;

and concludes

`u in H^{theta,r}_loc((0,sigma);X_{1-theta}) cap C^{theta-epsilon}_loc((0,sigma);X_{1-theta})`

for `theta in [0,1/2)`, `r in [2,infinity)`, `epsilon in (0,theta)`.

Problem 6 asks whether this result extends to `p=2` when `X0` is Hilbert and the setting is critical. At `p=2,kappa=0`, put

`s_j := 2 beta_j - 1 in (0,1)`.

The source criticality relation is exactly

`s_j (rho_j+1) <= 1`,

with equality for at least one `j` in the critical case; this is equation (6.1) in the variational notation.

**All of those hypotheses are retained below.** In fact the new argument does not use the extra growth assumption (5.21); I keep it in the theorem statement rather than silently changing the source problem.

## 3. Current source / later-literature check

Dated searches on 2026-09-16 included:

- `"Problem 6" "Agresti" "Veraar" "time regularization" Hilbert`;
- `"Theorem 5.7" "p=2" Agresti Veraar`;
- `2501.18561 Problem 6 Hilbert p=2`;
- `endpoint stochastic maximal regularity Hilbert critical semilinear spectral truncation`;
- author/follow-up searches around Agresti–Veraar's 2026 temporal-threshold note and Agresti–Germ–Veraar's 2026 reaction–diffusion preprint.

The current arXiv is v5 and still prints Problem 6. The 2026 Agresti–Veraar temporal-threshold note proves a sharp negative statement for persistence of `W^{alpha,2}` regularity at a **fixed spatial level** `D(A^{1/2})`; it does not settle the parabolic trade `X_{1-theta}` asked here. The 2026 reaction–diffusion paper gives concrete-model regularization, not the abstract Problem-6 theorem. I found no source explicitly stating the compact-tail argument below. This bounded search is **not** a novelty certificate.

A relevant older ingredient is already in Agresti–Veraar Part II (J. Evol. Equ. 2022), Corollary 3.15: stochastic maximal regularity is stable under sufficiently small progressively measurable perturbations of the deterministic and stochastic leading operators. The new route below combines that known perturbation theorem with uniform spectral-tail smallness of a compact Hilbert path.

## 4. Method 24 — extremal counterexample search: why high-frequency escape fails

I first tried to manufacture a source-admissible critical counterexample by making `u(t)` move its `H=X_{1/2}` mass to higher and higher spectral scales while keeping the critical interpolation product at order one. On one spectral scale the previous run already showed exact scale invariance at equality, so this is the natural extremal obstruction.

The attempt fails for a structural reason that is not present in the one-scale calculation:

> a continuous map from a compact time interval into a Hilbert space has compact range, and uniformly bounded strong approximations of the identity converge **uniformly on compact sets**.

Thus an `H`-continuous solution cannot retain a fixed amount of `H` mass arbitrarily far out in the spectral tail on a compact positive-time interval. This failure of the counterexample becomes the proof mechanism below.

## 5. Method 18 — rewrite the endpoint in the Hilbert-couple language

Let

`H = X_{1/2,2}`.

Since `X1` embeds densely and continuously into the Hilbert space `H`, the closed quadratic form given by the `X1` inner product has a positive self-adjoint representing operator `L` on `H` with form domain `D(L^{1/2})=X1` and an equivalent norm

`||x||_{X1} ~ ||L^{1/2}x||_H`.

For `R>=1` set

`P_R = 1_[0,R](L)`.

Then:

1. `P_R` and `I-P_R` are contractions on `H` and, up to the fixed norm equivalence, uniformly bounded on `X1`;
2. `P_R -> I` strongly on `H`;
3. `||P_R x||_{X1} <= C R^{1/2} ||x||_H`;
4. because `sup_R ||P_R||_{L(H)}<=1`, the convergence `P_R x -> x` is uniform for `x` in any compact subset of `H`.

The source's own real-interpolation reiteration formula (Lemma 4.3 specialized to `p=2,kappa=0`) is

`X_{beta_j,1} = (H,X1)_{s_j,1}`,  `s_j=2 beta_j-1`,

with

`||x||_{X_{beta_j,1}} <= C_j ||x||_H^{1-s_j} ||x||_{X1}^{s_j}`.        (5.1)

Criticality becomes the one-line exponent statement

`s_j(rho_j+1)<=1`.                                                     (5.2)

That translation is the key: at equality the `X1` exponent is exactly one, but the high-frequency factor still carries the positive power `||tail||_H^{1-s_j}`.

## 6. `R10-I0070-C002` — compact-tail absorption lemma

**STATUS: PROVED (author-side); exact exponent algebra independently self-checked.**

Let

`N(x) := (F(x),G(x))`

with target Banach space

`Y := X0 direct_sum_1 gamma(U,H)`.

Fix `K>0` and an arbitrary `a>0`. Then there exists `eta=eta(K,a)>0` such that for every fixed spectral cutoff `P_R` there is a finite constant `C=C(K,a,R)` with the following property:

if `x in X1`,

`||x||_H <= K`,  `||(I-P_R)x||_H <= eta`,

then

`||N(x)||_Y <= a ||x||_{X1} + C`.                                    (6.1)

### Proof

Put `v=P_R x`, `w=(I-P_R)x`, and `Y1=||x||_{X1}`. The spectral bounds give

`||v||_H <= K`, `||v||_{X1} <= M_R K`,

and

`||w||_H <= eta`, `||w||_{X1} <= C(Y1+M_R K)`.

For one source pair `(beta,rho)`, write `s=2beta-1` and `q=s(rho+1)<=1`. From (5.1),

`||x||_{X_beta,1} <= C K^{1-s} Y1^s`,

`||v||_{X_beta,1} <= C_{K,R}`,

`||w||_{X_beta,1} <= C eta^{1-s}(Y1+M_R K)^s`.                       (6.2)

Assumption 4.1 therefore bounds the corresponding part of `||N(x)-N(v)||_Y` by a constant times

`eta^{1-s} [1+Y1^{s rho}+C_{K,R}] (Y1+M_R K)^s`.                    (6.3)

Since `0<s<1`, `(Y1+c)^s <= Y1^s+c^s`. Every power of `Y1` in (6.3) is strictly below one except possibly

`Y1^{s(rho+1)} = Y1^q`.

- If `q<1`, Young's inequality makes every such term at most `(a/m)Y1+C` for an arbitrary prescribed coefficient.
- If `q=1`, its coefficient contains the strictly positive tail factor `eta^{1-s}`. Choose `eta` so small that the sum of all finitely many critical coefficients is below `a/2`; all remaining powers are `<1` and are again handled by Young.

Thus

`||N(x)-N(v)||_Y <= a||x||_{X1}+C_{K,a,R}`.                         (6.4)

Finally, `N(v)` is bounded on this set: compare `v` with `0` in Assumption 4.1, use the `H` bound `K` and the `X1` bound `M_R K`, and absorb `N(0)` into the constant. This proves (6.1).

### Rank-one linearization

The scalar estimate (6.1) can be converted into an actual small operator perturbation. If `y=N(x)` satisfies

`||y||_Y <= a||x||_{X1}+C`,

split `y=y_1+y_0` with `||y_1||_Y<=a||x||_{X1}` and `||y_0||_Y<=C`: if `||y||<=C`, take `y_1=0`; otherwise take `y_0=C y/||y||`.

Because `X1` is Hilbert, for `x!=0` define

`phi_x(z)=<z,x>_{X1}/||x||_{X1}^2`,  `R_x z=phi_x(z)y_1`.

Then

`||R_x||_{L(X1,Y)}<=a`,  `R_x x=y_1`,  `N(x)=R_x x+y_0`.             (6.5)

For `x=0`, take `R_x=0`. The construction is Borel in `(x,N(x))`; along a progressively measurable `X1`-valued version of a solution (defined a.e. in time), it yields strongly progressively measurable coefficient actions. Writing the two components of `R_x` gives

`C_x in L(X1,X0)`, `D_x in L(X1,gamma(U,H))`,

with `||C_x||+||D_x||<=a`, and bounded remainders `f_x,g_x`.

This is exactly the format of the stochastic maximal-regularity perturbation theorem (Agresti–Veraar Part II, Corollary 3.15).

## 7. Method 11 — dualize the nonlinear endpoint into a small linear-operator problem

The previous paragraph turns the critical nonlinear forcing, **along the actual solution path**, into

`F(u)=C_t u+f_t`,  `G(u)=D_t u+g_t`,                              (7.1)

where `(C_t,D_t)` has arbitrarily small operator norm and `(f_t,g_t)` is bounded, provided the `H`-norm is localized and the `H`-spectral tail is small. This moves the endpoint problem from nonlinear interpolation to a linear stochastic perturbation problem, where the source authors already have a stable maximal-regularity theorem.

The one remaining question is whether the tail-smallness condition can cover every positive-time compact interval. Hilbert path compactness answers it exactly.

## 8. `R10-I0070-C003` — full p=2 Hilbert regularization theorem candidate

**STATUS: AUTHOR-SIDE PROVED; NOT FLEET-CLOSED. Two independent OTHER-track audits are still required before this is labelled a closed solution of Problem 6.**

### Theorem

Assume exactly the p=2, kappa=0 specialization of Theorem 5.7:

1. `X0` is Hilbert, `X1=D(A)` has its graph norm, and Assumption 4.1 holds with `s_j=2 beta_j-1` satisfying `s_j(rho_j+1)<=1` for all `j` (with equality for at least one `j` allowed);
2. `(A,B) in SMR^bullet_{2,0}`, so Theorem 4.7 gives the maximal p=2 solution `(u,sigma)`;
3. the additional growth condition (5.21) is retained;
4. `(A,B) in SMR^bullet_{r,alpha}` for every `r>2` and `alpha in [0,r/2-1)`.

Then, almost surely,

`u in H^{theta,r}_loc((0,sigma);X_{1-theta}) cap C^{theta-epsilon}_loc((0,sigma);X_{1-theta})`

for every `theta in [0,1/2)`, `r in [2,infinity)`, `epsilon in (0,theta)`.

Thus the source conclusion of Theorem 5.7 extends to the critical Hilbert case p=2 without a spatial loss and without strengthening the stated hypotheses.

### Proof

Fix deterministic `0<a<b<infinity`; we prove the assertion on `{b<sigma}`. Choose `a0 in (0,a)` and a deterministic smooth cutoff `chi` satisfying

`chi(a0)=0`, `0<=chi<=1`, and `chi=1` on `[a,b]`.

Set

`z=chi u`.

On every interval on which `u` is a strong solution,

`dz + A z dt = [chi F(u)+chi' u]dt + [Bz+chi G(u)]dW`,  `z(a0)=0`. (8.1)

Fix first one `r>2` and `theta<1/2`. Let `M_2,M_r` denote fixed maximal-regularity perturbation constants for `(A,B)` on the finite interval containing `[a0,b]`. Choose `a_*>0` so small that the Agresti–Veraar small-perturbation criterion holds simultaneously at exponents `2` and `r` (for example make the deterministic-plus-stochastic perturbation size less than one half of both reciprocal constants).

For an integer `K`, apply C002 with `a=a_*` and obtain `eta(K,a_*)>0`. For a deterministic spectral cutoff `P_R`, let `tau_{n,K,R}` be the minimum of `b`, the nth source localizing time, and the first time after `a0` at which either

`||u(t)||_H > K`

or

`||(I-P_R)u(t)||_H > eta(K,a_*)`.

Both are stopping conditions because `u` is `H`-continuous and `P_R` is bounded on `H`.

On `[a0,tau_{n,K,R}]`, C002 and its rank-one linearization give progressively measurable operators `C_t,D_t` and remainders `f_t,g_t` such that

`F(u)=C_t u+f_t`, `G(u)=D_t u+g_t`,

`||C_t||+||D_t||<=a_*`,

`||f_t||_{X0}+||g_t||_{gamma(U,H)}<=C_{K,R}`.                       (8.2)

Multiplying by `chi` and using `z=chi u`, equation (8.1) becomes

`dz + (A-C_t)z dt = [chi f_t+chi' u]dt + [(B+D_t)z+chi g_t]dW`.     (8.3)

The inhomogeneities on the right are in every finite `L^r(Omega x time)` on the stopped interval: `f_t,g_t` are uniformly bounded, while `||u||_H<=K` and the embedding `H -> X0` controls `chi'u`.

By the small-perturbation theorem applied at exponent `r`, the linear equation (8.3) has a unique `L^r_t X1` strong solution `z_r`. Since the interval has finite measure and `r>2`, `z_r` is also an `L^2_t X1` solution. Applying the same perturbation theorem at exponent `2`, equation (8.3) has a unique `L^2_t X1` solution. The original cutoff process `z=chi u` is such an `L^2` solution by Theorem 4.7. Hence

`z=z_r` a.e., and therefore

`z in L^r(a0,tau_{n,K,R};X1)`.                                    (8.4)

Now rewrite (8.3) with the original pair `(A,B)`:

`dz+A z dt = [C_t z+chi f_t+chi'u]dt + [Bz+D_tz+chi g_t]dW`.

By (8.4), both displayed inhomogeneities lie in `L^r`; Definition 3.8 / `SMR^bullet_{r,0}` therefore gives

`z in H^{theta,r}(a0,tau_{n,K,R};X_{1-theta})`                    (8.5)

for every `theta<1/2`.

It remains to remove the spectral-tail stopping. On `{b<sigma}`, choose `n` with `sigma_n>b`. The image

`K_omega={u(t,omega): t in [a0,b]}`

is compact in `H`, because the p=2 solution is `H`-continuous. The contractions `P_R` converge strongly to `I` on `H`, hence uniformly on this compact set:

`sup_{t in [a0,b]}||(I-P_R)u(t,omega)||_H ->0`.                    (8.6)

Choose an integer `K` above the path supremum and then an integer cutoff `R` so large that (8.6) is below `eta(K,a_*)`. Therefore

`{b<sigma}` is the countable union, over `n,K,R`, of events on which `tau_{n,K,R}=b`.

On each such event, `chi=1` on `[a,b]`, so (8.5) yields

`u in H^{theta,r}([a,b];X_{1-theta})`.

Since `[a,b]` was arbitrary, this proves

`u in H^{theta,r}_loc((0,sigma);X_{1-theta})`

for every fixed `r>2`, `theta<1/2`. The case `r=2` follows on compact intervals from any `q>2` version (or directly by the finite-measure embedding for Bessel-potential time spaces).

Finally, given `0<epsilon<theta`, choose `q>max(2,1/epsilon)`. The already proved `H^{theta,q}` regularity and the one-dimensional Sobolev embedding yield

`H^{theta,q} -> C^{theta-1/q} -> C^{theta-epsilon}`.

A countable exhaustion of positive-time compact intervals finishes the proof.

### Why this is genuinely an endpoint mechanism

At criticality the standard Lemma-4.3 estimate has no small time factor and has exactly one power of the `L^2_tX1` norm; that is why the source bootstrap stops. The new gain does **not** come from shortening time. It comes from the compactness of the **actual Hilbert-valued path range**: the high-frequency `H` tail becomes uniformly small, and the exact critical exponent leaves a positive power `eta^{1-s}` multiplying the otherwise linear `X1` term. This turns the critical nonlinearity into an arbitrarily small perturbation of `(A,B)` plus bounded forcing.

## 9. Adversarial checks / limitations

I tried to break C003 at the points where endpoint arguments typically hide stronger assumptions.

1. **No compact embedding assumed.** `X1 -> H` need not be compact. Only strong spectral convergence on `H`, uniform on the compact **path range**, is used.
2. **No commutation with A or B.** `P_R` is built from the Hilbert couple `(H,X1)` and is used only to split the nonlinear forcing; it never needs to commute with `A` or `B`.
3. **Nonzero B retained.** The perturbation is `(A-C_t,B+D_t)`, exactly within the source small-perturbation framework.
4. **No p>2 initial moment.** Identification uses p=2 uniqueness after constructing the `L^r` solution of the random linear perturbation; the cutoff has zero initial value.
5. **All original interpolation norms retained.** The source `X_{beta_j,1}` appears unchanged via reiteration `(H,X1)_{s_j,1}`.
6. **Endpoint theta=1/2 not claimed.** The conclusion remains exactly `theta<1/2`.
7. **Measurability.** The rank-one coefficient is an explicit Borel function of the progressively measurable pair `(u,N(u))` on the a.e. `X1` set; it may be defined arbitrarily on the null complement.
8. **(5.21) not used.** This weakens, rather than strengthens, the assumptions actually needed by the argument; the source statement nevertheless retains (5.21).

The highest-risk points for independent audit are: (i) the operator-valued measurability in the rank-one linearization; (ii) applying the Part-II small-perturbation theorem simultaneously at p=2 and p=r on the stopped interval; (iii) the `r=2` same-smoothness embedding from a `q>2` time-Bessel space. These are explicitly flagged for peer review rather than hidden.

## 10. Exact self-check artifact

Only after obtaining the new route did I build a finite checker. It verifies with exact rational arithmetic:

- the critical identity `s(rho+1)=1`, the positive tail exponent `1-s`, and `s rho=1-s` for `rho=1,...,30`;
- representative strict-subcritical exponents;
- the scalar bounded-remainder compiler used before the rank-one map (100,000 cases);
- the Neumann small-perturbation contraction algebra (100,000 cases);
- the independent R11 generator-rate identity below.

Checker:
`artifacts/R10/20260916T1753Z_i0070_compact_tail_checker.py`
created/read back at commit `167c1662bea82d8e7653d9681aee1cb8494a47b2`.

Executed output:
`artifacts/R10/20260916T1753Z_i0070_compact_tail_checker.out`
created/read back at commit `a014683d92e968e92fc8b1ab40df65ddbb6cfcf9`.

Output SHA-256:
`1a7fcf44d006c4c6a7ff68690b980ef17ebceb23a5ce394393749b4a18ba4807`.

This checker is a **self-check**, not an independent audit of the theorem-sized functional-analytic argument.

## 11. Independent R11 audit — package now ready enough for a core audit

Newest R11 package actually read:

`runs/R11/2026-09-16T17-42-08Z_i0054-ncrp-tangent-8b6e.md`

claim `R11-I0054-C002`: small-concentration nested Chinese restaurant trees converge to CTCS(infinity).

Audit ID:

`R10-AUDIT-R11-I0054-C002-GENERATOR-20260916`

**RESULT: PASS for the mathematical generator/convergence core; prior-art/source-intent clearance is not audited here.**

Independent derivation:

For a particular labelled binary partition `A | A^c` of an `m`-set, `|A|=i`, the Ewens EPPF is

`p_theta(A|A^c) = theta (i-1)!(m-i-1)! / prod_{j=1}^{m-1}(j+theta)`.

Therefore

`p_theta(A|A^c)/theta -> (i-1)!(m-i-1)!/(m-1)! = B(i,m-i)`.

The no-split probability has derivative `-H_{m-1}` at zero, and the total binary rate is exactly

`(1/2) sum_{i=1}^{m-1} C(m,i) B(i,m-i) = H_{m-1}`,

because

`C(m,i)B(i,m-i)=m/[i(m-i)]`

and

`1/[i(m-i)] = (1/i+1/(m-i))/m`.

Every >=3-way refinement and every simultaneous split of two current blocks is `O(theta^2)`. Hence on each fixed finite partition state space

`P_theta = I + theta Q + O(theta^2)`

uniformly entrywise. With `theta_N=1/N`, geometric waiting times rescaled by `1/N` converge to the exponential holding times of `Q`, jump-type probabilities converge to `q/rate`, and the probability of an `O(theta^2)` exceptional transition before any fixed time is `O(theta)`. This gives Skorokhod `J_1` convergence for every fixed `k` restriction.

For the projective metric, convergence of the `K`-label restriction jointly controls all restrictions `k<=K`, while the metric tail is deterministically at most `sum_{k>K}2^{-k}`. Letting first `N->infinity` and then `K->infinity` gives the stated projective convergence.

The R10 exact checker independently verifies the binary-rate identity for every `m=2,...,30`.

Thus the core scaling theorem passes this audit. Whether the known nCRP model satisfies Aldous–Janson's intended phrase “superficially different discrete models” and whether the exact scaling statement is already implicit in the Ewens-fragmentation literature remain separate prior-art/source-interpretation questions.

## 12. Metric and closure ledger

Fixed metric:

`theta_* := sup { theta : source-exact X_{1-theta} time regularization has been rigorously established for the frozen R10 critical p=2 target }`.

Before: `1/2` as a supremum for one fixed special model.  
After: `1/2` as a supremum; **no numeric movement**.  
Endpoint `theta=1/2`: not claimed.

Substantive scope change: special-model theorem -> full-source theorem candidate C003.

Outside-source status remains **PARTIAL** rather than CLOSED because the fleet closure rule requires two independent OTHER-track audits (one P26 and one distinct track) plus completed prior-art clearance. No such audits of C003 exist yet.

`ledger_delta`:

```yaml
ledger_delta:
  worker: R10
  source: "Agresti--Veraar, arXiv:2501.18561v5 / NoDEA 32 (2025), Problem 6"
  target: "extend Theorem 5.7 to p=2, kappa=0, X0 Hilbert, critical equality allowed, without changing source norms/hypotheses"
  metric: "theta_* = supremum of source-exact time regularity exponents established for the frozen R10 critical p=2 target"
  before: "1/2 (supremum), special model only"
  after: "1/2 (supremum), author-side full-source proof candidate C003"
  movement: "NO NUMERIC MOVEMENT; major scope movement"
  status: PARTIAL
  unchanged_count: 1
  exact_evidence:
    - "artifacts/R10/20260916T1753Z_i0070_compact_tail_checker.py @ 167c1662bea82d8e7653d9681aee1cb8494a47b2"
    - "artifacts/R10/20260916T1753Z_i0070_compact_tail_checker.out @ a014683d92e968e92fc8b1ab40df65ddbb6cfcf9"
  audit_ids:
    - "R10-AUDIT-R11-I0054-C002-GENERATOR-20260916 (outgoing audit of R11, not an audit of R10)"
  r10_required_external_audits: []
```

## 13. Model/runtime control escalation status

The limitation is still real. The scheduler interface exposed to this worker has controls for prompt/title, schedule, enabled state, and timing mode, but **no model-family field and no reasoning-effort field**. Therefore prompt text can request `GPT-6 / maximum`, but cannot set or verify it. This run actually reports GPT-5.6 Sol and reasoning `UNVERIFIED`.

Repository policy also records native task-update denials such as `You cannot modify this task` for some P26/P01/P03 contexts. Newer peer reports clarify that such denial is permission/context-specific rather than proof of global immutability. The legitimate fix is to use the authorized task/account/workspace-owner interface that owns the existing native task, or platform support to repair/transfer that permission. The forbidden workaround is to clone the job, bypass permission, or pretend a repository prompt edit changed runtime metadata. No scheduler mutation was attempted here.

## 14. Next run

Do **not** re-prove C002/C003 and do not repeat methods 11/18/24 immediately.

Highest-value next work is adversarial verification of C003:

1. try to break the measurable rank-one perturbation on a genuinely time-dependent `B!=0` Hilbert pair;
2. replace the same-smoothness `r=2` embedding by a direct source-space argument if an auditor dislikes that step;
3. search specifically for this compact-tail absorption mechanism in Prüss–Simonett–Wilke / critical deterministic maximal-regularity and Agresti–Veraar follow-up literature;
4. obtain the required OTHER-track audits before any closure/paper package is created.

If an audit finds a gap, preserve the exact counterexample/obstruction rather than patching silently.
