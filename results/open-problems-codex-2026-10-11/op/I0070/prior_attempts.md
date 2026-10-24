
FILE operations/claims/I0070.md
# I0070 — provisional exclusive reservation for R10

Owner: R10, native task 6aa7b669391081918ba308c31573a86e.
Status: PENDING_ADMISSION, not READY.
Source: Agresti and Veraar, arXiv:2501.18561v2, Problem 6.
Statement: extend Theorem 5.7 to the critical Hilbert case p=2 under the critical equality (6.1), preserving the full theorem's hypotheses and norms.
Metric: largest time-regularity exponent theta rigorously established for a fixed source-admissible critical p=2 problem, with all weights, norms and parameter restrictions frozen and reported. Restricted model results remain PARTIAL for the source's full question.
Initial moves: 2, 6, 30.
Why selected: a critical model counterexample or a complete endpoint theorem can isolate the unresolved mechanism.

Read the complete Theorem 5.7 and equation (6.1), current primary literature, all previous attempts and ownership before research. The already written Problems 4–5 package is excluded. The earlier queue listed this candidate unassigned; this create-only reservation does not certify worldwide openness or readiness. Retire R10's old square-lattice Cardy route from the slot with an immutable handoff, retaining its history.


FILE runs/R10/20260916T1753Z_i0070_compact_tail_endpoint.md
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


FILE runs/R10/20260916T1833Z_i0070_stopped_perturbation_repair.md
Model: GPT-5.6 Sol. Reasoning: UNVERIFIED — **NO NUMERIC METRIC MOVEMENT** (`theta_* = 1/2` as a supremum before and after; endpoint `theta=1/2` is not claimed). Scope/proof movement: the full-source candidate `R10-I0070-C003` is hardened by a deterministic-horizon stopped-perturbation argument that removes the two largest technical gaps in the preceding run. New Section-B methods actually used: **15 (BREAK THE SYMMETRY ON PURPOSE), 20 (FIND WHY THE ALGORITHM FAILS), 21 (ASK WHO ELSE HAS THIS SHAPE)**.

Problem/source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561v5 / NoDEA 32 (2025), Article 123, Problem 6 (“Time regularization in Hilbert spaces”). Campaign status remains **PARTIAL**. The source problem is not called closed before two independent OTHER-track audits, including P26, and prior-art clearance.

# R10 I0070 — deterministic-horizon localization repairs the compact-tail endpoint route

Run ID: `20260916T1833Z_i0070_stopped_perturbation_repair`  
Repository/branch: `yspennstate/math-open-problems` / `master`  
Dated source/status check: 2026-09-16

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler mutation, peer-file edit, or shared-root edit was performed.

## 1. Continuity, whole-repository resume, ownership, and admission

I continued from the newest immutable R10 report rather than restarting:

`runs/R10/20260916T1753Z_i0070_compact_tail_endpoint.md`.

That report retained the fixed metric

`theta_* = 1/2` as a supremum,

proved the compact-tail absorption lemma `R10-I0070-C002`, and gave the full-source endpoint candidate `R10-I0070-C003`. Its explicit audit-sensitive points were: (i) progressive/operator measurability of the rank-one perturbation, (ii) legitimate use of stochastic maximal-regularity perturbation simultaneously at `p=2` and a higher exponent, and (iii) the `r=2` conclusion.

Before new mathematics I read/recovered on current `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/I0070.md`;
- the newest complete R10 report;
- the newest neighboring Agresti–Veraar P24 report found on current master;
- the newest R11 package found by repository search;
- current exact-ID/ownership surfaces for I0070.

The connector cannot render all roughly 780 intake JSONL rows byte-for-byte in one model response. I therefore do **not** claim a manual row-by-row reread of every intake file. The exact I0070 claim, queue entry, current source, neighboring ownership, and prior attempts were rechecked directly.

The canonical claim still says `PENDING_ADMISSION, not READY`; R10 does not edit coordinator-owned claim/root files. Research-side admission evidence remains complete: the current published source still prints Problem 6; no later source resolution was found in the bounded 2026-09-16 search; I0070 is exclusively reserved to R10; P19 explicitly declined it because of that claim; P24 is on distinct Problem 3 / I0063=I0069; and the already-written Problems 4–5 package is excluded. The retired square-lattice Cardy work remains preserved in older R10 reports and is not reopened.

## 2. Exact source scope retained

The current v5/journal source states Theorem 5.7 for `p>2`, `kappa=0`. Besides the hypotheses of Theorem 4.7 it assumes the source growth bound (5.21), and it assumes

`(A,B) in SMR^bullet_{r,alpha}`

for every `r>2` and `alpha in [0,r/2-1)`. It concludes, for every `theta<1/2`, every `r>=2`, and every `0<epsilon<theta`,

`u in H^{theta,r}_loc((0,sigma);X_{1-theta}) cap C^{theta-epsilon}_loc((0,sigma);X_{1-theta})`.

Problem 6 asks whether this regularization result extends to `p=2` when `X0` is Hilbert and the critical equality occurs. At `p=2`, writing

`s_j := 2 beta_j - 1 in (0,1)`, 

the critical restriction is

`s_j(rho_j+1) <= 1`,

with equality allowed/required for at least one critical pair. I retain **all** Theorem-5.7 hypotheses, including (5.21), although the compact-tail proof below does not appear to use (5.21).

The basic p=2 solution supplied by the source has, on localizing intervals,

`u in L^2(X1) cap C(H)`,  where `H:=X_{1/2,2}`.

Since `X0` is Hilbert, `X1=D(A)` with graph norm is Hilbert, and the Hilbert interpolation space `H` is Hilbert.

## 3. Current literature screen and what is / is not new

Dated 2026-09-16 searches covered the exact Problem-6 wording, Theorem 5.7, critical p=2 Hilbert regularization, compactness/spectral-tail variants, later Agresti–Veraar papers, and recent maximal-regularity papers.

The current source is the published NoDEA article (1 September 2025) / arXiv v5 and still prints Problem 6. Lorist–van Neerven–Veraar, arXiv:2608.20266 (20 August 2026), gives sharp necessary Banach-geometry information for stochastic maximal regularity and in particular singles out Hilbert geometry at `p=2`, but it does not state the nonlinear Problem-6 regularization theorem proved below. The bounded search found no later paper resolving Problem 6. This is **not** a worldwide novelty certificate.

The perturbation step itself is not new: Agresti–Veraar Part II (J. Evol. Equ. 22 (2022), Article 56) explicitly invokes Corollary 3.15 to preserve `SMR^bullet_p` under small progressively measurable perturbations of both the deterministic and stochastic leading operators. Their continuation proof localizes on stopping events and uses the perturbation theorem after coefficient differences are made small. This run ports that architecture to the critical semilinear endpoint. The new mechanism in the R10 candidate is the source of smallness: **uniform Hilbert spectral-tail smallness of a compact solution path**, rather than smallness of a coefficient difference in the trace norm.

## 4. Retained compact-tail lemma C002

I do not re-prove the entire preceding report, but record the exact input needed below.

Let

`H=X_{1/2,2}`

and represent the Hilbert couple `(H,X1)` by a positive self-adjoint operator `L` on `H` with form domain `D(L^{1/2})=X1` and equivalent form norm. Put

`P_R = 1_[0,R](L)`.

Then `P_R -> I` strongly on `H`, `P_R` is uniformly bounded on `H` and `X1`, and

`||P_R x||_{X1} <= C R^{1/2} ||x||_H`.

Because a continuous map from a compact time interval into `H` has compact range and the `P_R` are uniformly bounded,

`sup_{t in I} ||(I-P_R)u(t)||_H -> 0`

on every compact path interval `I`.

The source reiteration at `p=2` gives, for `s_j=2beta_j-1`,

`X_{beta_j,1} = (H,X1)_{s_j,1}`

and

`||x||_{X_{beta_j,1}} <= C_j ||x||_H^(1-s_j) ||x||_{X1}^{s_j}`.

From Assumption 4.1 and `s_j(rho_j+1)<=1`, the preceding report proved:

### `R10-I0070-C002` (retained)
For every `K>0` and every `a>0` there exists `eta=eta(K,a)>0` such that for each fixed `R` there is `C=C(K,a,R)` satisfying

`||F(x)||_{X0} + ||G(x)||_{gamma(U,H)} <= a ||x||_{X1} + C`

whenever

`||x||_H<=K`,  `||(I-P_R)x||_H<=eta`.

At a critical pair the highest `X1` power is exactly one, but its coefficient contains `eta^(1-s_j)` with `1-s_j>0`; this is what can be made arbitrarily small. Strictly subcritical powers are absorbed by Young.

The exact critical-exponent arithmetic was already archived in

`artifacts/R10/20260916T1753Z_i0070_compact_tail_checker.py`

and its `.out`; this run does not manufacture a redundant checker for the same unchanged finite algebra.

## 5. Move 15 — break the symmetry: keep B nonzero and use two different SMR exponents

The most dangerous hidden strengthening in the preceding proof would have been to make `B=0`, or to use one perturbation threshold for all `p`. I therefore broke that symmetry deliberately.

Let a requested final integrability exponent be `r0>=2`, and choose one auxiliary exponent

`q > max(r0, 2, 1/epsilon)`.

The source assumptions give both

`(A,B) in SMR^bullet_{2,0}`

and

`(A,B) in SMR^bullet_{q,0}`.

Corollary 3.15 has (possibly different) deterministic/stochastic perturbation constants at exponent 2 and exponent q. Choose the scalar `a>0` in C002 smaller than **both** perturbation budgets, e.g. sufficiently small that

`Cdet_2 a + Csto_2 a < 1/2`,

`Cdet_q a + Csto_q a < 1/2`.

No common all-p estimate is needed; only the two fixed exponents `2` and `q` are used. The stochastic perturbation produced from `G` is absorbed into the existing, possibly large, nonzero operator `B`. Thus the route keeps the full nonzero-`B` source scope.

Outcome of move 15: **survives**. The proof does not need `B=0`, small `B`, or a perturbation constant uniform in `p`.

## 6. Move 20 — find why the previous algorithm could fail, then repair it

The preceding proof said “stop where the tail is small, apply the perturbation theorem, and identify by p=2 uniqueness.” Written that way, it hid two genuine obligations:

1. Corollary 3.15 is easiest to apply on a deterministic horizon, whereas the useful small-tail set is defined by a stopping time.
2. The rank-one coefficient field must be strongly progressively measurable in the sense needed by the perturbation theorem.

Both can be repaired without new assumptions.

### 6.1 A Borel rank-one decomposition

Set

`Y := X0 direct_sum_1 gamma(U,H)`,  `N(x):=(F(x),G(x))`.

On the C002 region, write `X=||x||_{X1}` and `Y0=||N(x)||_Y`, so

`Y0 <= a X + C`.

Define a scalar Borel split

- if `Y0<=C`, set `N_1(x)=0`, `N_0(x)=N(x)`;
- if `Y0>C`, set `N_0(x)= (C/Y0) N(x)` and `N_1(x)=N(x)-N_0(x)`.

Then

`||N_0(x)||_Y <= C`,  `||N_1(x)||_Y <= a||x||_{X1}`.

For `x!=0` define the rank-one operator

`R_x z = <z,x>_{X1}/||x||_{X1}^2 * N_1(x)`,

and set `R_0=0`. Then

`||R_x||_{L(X1,Y)} <= a`,  `R_x x=N_1(x)`,

so

`N(x)=R_x x + N_0(x)`.

The formula is Borel in `(x,N(x))`; projecting `Y` onto its two factors yields

`F(x)=C_x x + f_x`,

`G(x)=D_x x + g_x`,

with

`||C_x||+||D_x|| <= a`,  `||f_x||+||g_x|| <= C`.

A source strong solution is progressively measurable in `X0` and belongs to `L^2(X1)`. On the a.e. set where it is `X1`-valued, one may take the standard strongly progressively measurable `X1` representative (equivalently: on the essentially separable `X1` range, the continuous injective embedding `X1 -> X0` has a Borel inverse onto its image). Hence for each fixed `z in X1`, `C_{u(t)}z` and `D_{u(t)}z` are progressively measurable. This is precisely the strong progressive measurability required for the time-dependent perturbation pair.

This explicitly closes the measurability point left for audit in the previous report.

### 6.2 Deterministic-horizon zero extension

Fix a compact positive-time interval `[a,b] subset (0,sigma)` and choose deterministic `a0<a<T`. Let `chi` be a deterministic smooth cutoff with

`chi(a0)=0`,  `chi=1` on `[a,b]`.

Let `sigma_n` be a source localizing sequence for the p=2 maximal solution. For deterministic integers `K,R`, define the stopping time

`tau = sigma_n wedge T wedge inf{t>=a0: ||u(t)||_H >= K or ||(I-P_R)u(t)||_H >= eta}`,

where `eta=eta(K,a)` is supplied by C002 for the perturbation size fixed in Section 5.

For `t<=tau`, use the Borel decomposition above and set

`C_t=C_{u(t)}`, `D_t=D_{u(t)}`, `f_t=f_{u(t)}`, `g_t=g_{u(t)}`.

After `tau`, extend all four fields by zero. The stopped fields remain strongly progressively measurable, and

`||C_t||+||D_t||<=a`,

`||f_t||+||g_t||<=C(K,a,R)`

on the whole deterministic interval `[a0,T]`.

Now consider the **auxiliary deterministic-horizon linear equation**

`dZ + (A-C_t)Z dt = [chi f_t + 1_{t<=tau} chi' u]dt + [(B+D_t)Z + chi g_t]dW`,

`Z(a0)=0`.

All coefficient fields and forcing terms are zero-extended after `tau`. The forcing is in every finite `L^q(Omega x (a0,T))`: the remainders are deterministically bounded after localization, and `1_{t<=tau}chi'u` is bounded in `H`, hence in `X0`, by `K`.

By the choice of `a`, Corollary 3.15 gives the perturbed pair simultaneously in

`SMR^bullet_{2,0}` and `SMR^bullet_{q,0}`

on the deterministic horizon. Therefore the auxiliary equation has a unique q-solution `Z^(q)` with

`Z^(q) in H^{theta,q}(a0,T;X_{1-theta})`

for every `theta<1/2`. Since `q>2` and the underlying probability-time measure is finite, `Z^(q)` also belongs to the p=2 solution class.

On `[a0,tau]`, the cutoff process `z=chi u` satisfies **the same** auxiliary linear equation: linearity gives

`chi C_t u = C_t(chi u)=C_t z`,

`chi D_t u = D_t z`.

The p=2 uniqueness statement therefore gives

`Z^(q)=chi u`

up to `tau`.

This is the rigorous deterministic-horizon version of the localization step. It avoids applying the perturbation theorem “on a random interval” by fiat.

### 6.3 Removing the stops by compact Hilbert tails

For almost every path with `b<sigma`, choose `n` with `b<sigma_n`. Since

`u in C([a0,b];H)`, 

its range is compact and bounded. Hence there is an integer `K` with

`sup_[a0,b] ||u||_H<K`,

and, by uniform strong convergence of `P_R` on compact subsets of `H`, an integer `R` with

`sup_[a0,b] ||(I-P_R)u||_H < eta(K,a)`.

Thus `tau>b` for some triple `(n,K,R)`. The countable union over integers `n,K,R` covers `{b<sigma}`. On every event in that union,

`u = Z^(q)` on `[a,b]`,

so

`u in H^{theta,q}([a,b];X_{1-theta})`.

Since `[a,b]` was an arbitrary positive-time compact interval, this is local regularity on `(0,sigma)`.

Outcome of move 20: **the two largest implementation gaps of C003 are repaired**. The price is only a countable stopping decomposition, not a new hypothesis.

## 7. The r=2 point no longer needs a separate endpoint time theorem

The preceding report flagged `r=2` as an audit point because `SMR^bullet_{2,0}` itself has a special definition and should not be silently treated as if it already supplied every `H^{theta,2}` estimate.

The repair is simpler: for any requested `r0>=2`, choose one `q>max(r0,2)`. Section 6 yields

`u in H^{theta,q}_loc(X_{1-theta})`.

On a finite compact time interval, the standard same-smoothness embedding

`H^{theta,q} -> H^{theta,r0}`

holds for `q>=r0`. Therefore the `r0=2` conclusion follows from the higher-q estimate; no direct p=2 bullet time-regularity assertion is used. Likewise choose `q>1/epsilon` and use the one-dimensional Sobolev embedding

`H^{theta,q} -> C^{theta-1/q} -> C^{theta-epsilon}`.

Thus one large auxiliary exponent q supplies both the whole finite-r range below q and the desired Hölder exponent.

## 8. `R10-I0070-C004` — stopped compact-tail perturbation compiler

**STATUS: AUTHOR-SIDE PROVED.**

Assume exactly the p=2 Hilbert/Theorem-5.7 hypotheses recorded in Section 2 and retain C002. Fix a local p=2 solution `u`, a positive-time compact interval `[a,b]`, a target `r0>=2`, `theta<1/2`, and `0<epsilon<theta`. Choose `q>max(r0,1/epsilon,2)`. Then there exists a countable family of deterministic-horizon stopped linear perturbation problems, each satisfying the source perturbation smallness simultaneously at exponents 2 and q, whose events cover `{b<sigma}` and on which the corresponding q-solution equals `u` on `[a,b]`. Consequently

`u in H^{theta,r0}([a,b];X_{1-theta}) cap C^{theta-epsilon}([a,b];X_{1-theta})`

on `{b<sigma}`.

Dependencies: source p=2 existence/uniqueness; C002; Hilbert-couple spectral calculus; Corollary 3.15 small perturbations; the source all-r SMR hypothesis. No compact embedding, `B=0`, small-B assumption, stronger initial space, or stronger nonlinear norm is introduced.

## 9. Status of `R10-I0070-C003`

After C004, the previous full-source candidate can be restated cleanly:

> Under exactly the p=2 Hilbert specialization of the hypotheses of Theorem 5.7, with `s_j(rho_j+1)<=1` and equality allowed, the maximal solution satisfies
>
> `u in H^{theta,r}_loc((0,sigma);X_{1-theta}) cap C^{theta-epsilon}_loc((0,sigma);X_{1-theta})`
>
> for every `theta<1/2`, every `r>=2`, and every `0<epsilon<theta`.

**Author-side proof status: PROVED CANDIDATE, strengthened this run by C004. Campaign/source status: PARTIAL until the closure protocol is met.**

The fixed numeric metric remains

`theta_* = 1/2` as a supremum,

so this is the second consecutive run with no numeric metric movement after the special-model run first established that supremum. Under the owner policy the unchanged count is therefore `2`, not zero and not UNKNOWN. One more unchanged run would trigger the five-part stuck protocol unless an audit/closure event or genuine metric/scope movement changes the state.

## 10. Move 21 — who else has this shape?

The nearest source-internal analogue is Agresti–Veraar Part II itself: its continuation argument makes time/random leading-operator differences small, applies Corollary 3.15, and then removes localization. This validates the **architecture** of Section 6, but not the new compact-tail estimate C002.

The recent Lorist–van Neerven–Veraar preprint arXiv:2608.20266 proves necessary Banach-geometry conditions for stochastic maximal regularity and characterizes an endpoint `p=2` kernel condition by Hilbert geometry. It is conceptually consistent with the fact that the R10 mechanism uses Hilbert spectral calculus in an essential way. It does not state or imply C002/C004 directly.

A bounded search for “critical maximal regularity + compact spectral tail / compact path + small perturbation” found general compactness-rigidity paradigms in critical PDE, but no direct source-equivalent theorem. I therefore record the mechanism as **prior-art not cleared**, not as novel.

Outcome of move 21: the perturbation/localization half is demonstrably standard in the authors’ own toolkit; the specific tail-smallness bridge remains the part requiring independent scrutiny.

## 11. Adversarial checks of the strongest claim

I specifically tried to break C003/C004 in the following ways.

1. **Nonzero B.** Survives: the stochastic rank-one part perturbs `B` and Corollary 3.15 treats both leading operators.
2. **Different perturbation radii at p=2 and q.** Survives: choose `a` below the minimum of the two fixed budgets; no uniform-in-p constant is required.
3. **Random stopping interval.** Repaired: zero-extend coefficients/forcing and solve on a deterministic horizon.
4. **Measurability of rank-one operators.** Repaired by the explicit Borel split and Hilbert Riesz functional; use the standard `X1` progressive representative of the strong solution.
5. **r=2 conclusion.** Repaired by first proving a q>2 estimate and embedding at unchanged smoothness.
6. **Noncompact X1->H embedding.** Not needed: uniform tail convergence is on the compact path range, using strong convergence of bounded spectral projections, not compactness of the embedding.
7. **Pathwise choice of R.** Repaired by countable deterministic integers `(n,K,R)` and event decomposition; no random spectral projector is introduced.

The remaining audit-sensitive point I would ask an independent reader to check first is the exact source formulation of Corollary 3.15 at `p=2` and its bullet/time-regularity convention. The Part-II application explicitly uses that perturbation result in an `SMR^bullet_p` continuation argument, which is strong supporting evidence, but source-level closure should include a line-by-line verification of the constants/interval convention.

## 12. R11 audit status

The newest R11 package found in this run is still

`runs/R11/2026-09-16T17-42-08Z_i0054-ncrp-tangent-8b6e.md`.

The preceding R10 run already independently audited its generator/projective-convergence core and recorded a PASS at that restricted scope. No newer R11 theorem package was found on current master, so I do **not** spend the research budget duplicating the same audit. This run creates no peer-file edit.

## 13. Model/runtime and denied-task controls

The actual runtime here identifies the model as GPT-5.6 Sol; reasoning effort is not exposed, hence `UNVERIFIED`. The scheduler interface exposed to this environment offers task title/prompt, schedule, enablement, and timing-mode controls. It exposes **no model-family selector and no reasoning-effort selector**. Therefore GPT-6/maximum can be requested in prompt text but cannot be set or verified from this interface.

Repository operations records clarify the historical P26 permission issue: one native context returned `You cannot modify this task`, while a later authorized context successfully updated P26. Thus the denial is context/ownership-specific, not proof of global immutability. The legitimate repair is to use the authorized workspace/task-owner context that owns the existing task, or platform support to repair/expose that ownership. Duplicating the job or bypassing permissions is not an acceptable workaround. No scheduler mutation was attempted in this run.

## 14. Structured ledger_delta

```yaml
ledger_delta:
  source: "Agresti-Veraar, Nonlinear SPDEs and Maximal Regularity: An Extended Survey, NoDEA 32 (2025), Problem 6; arXiv:2501.18561v5"
  target: "Extend Theorem 5.7 to p=2 when X0 is Hilbert in the critical case, preserving all theorem hypotheses/norms/parameter ranges"
  metric: "largest rigorously established time-regularity exponent theta for the fixed source-admissible critical p=2 problem"
  before: "theta_* = 1/2 as supremum; endpoint 1/2 not claimed; full-source proof candidate C003 with localization/measurability audit gaps"
  after: "theta_* = 1/2 as supremum; endpoint 1/2 not claimed; C004 repairs deterministic-horizon localization, progressive rank-one measurability, nonzero-B/two-exponent perturbation, and r=2 reduction"
  numeric_movement: false
  unchanged_count: 2
  status: PARTIAL
  exact_evidence:
    - "retained exact algebra: artifacts/R10/20260916T1753Z_i0070_compact_tail_checker.py and .out"
    - "new theorem-sized proof: this immutable report, Sections 5-9"
  audit_ids: []
  closure_blockers:
    - "P26 end-to-end audit of source statement and Corollary 3.15 conventions"
    - "second independent OTHER-track end-to-end audit"
    - "prior-art clearance for compact-tail absorption mechanism"
```

## 15. Next attack if another run occurs

Do **not** re-prove C002/C004 and do not repeat methods 15/20/21. The highest-value next run is an independent-failure hunt aimed at one of two outcomes:

1. find a source-valid counterexample to the compact-tail rank-one perturbation step, especially a measurability/interval-convention failure invisible to the algebra; or
2. if none survives, turn C002+C004+C003 into the minimal self-contained source-matching paper folder **only after** the two required OTHER-track audits exist.

If the numeric metric remains unchanged for that next run, it will be the third consecutive unchanged run and the owner’s five-part stuck protocol must be triggered unless closure/audit progress genuinely changes the tracked state.

No closure claim is made in this report.


FILE runs/R10/20260916T2033Z_i0070_zero_trace_delta_bypass.md
Model: GPT-5.6 Sol. Reasoning: UNVERIFIED — **no movement** in the fixed numeric metric (`theta_* = 1/2` as a supremum before and after; endpoint `theta=1/2` is not claimed). This is the first recovery run after STUCK1. New Section-B moves actually used: **#3 PROVE SOMETHING STRONGER, #7 TAKE THE LIMIT, #22 READ THE FAILURES**.

Problem/source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, NoDEA 32 (2025), article 123, arXiv:2501.18561 (historical intake locator v2; current source v5), **Problem 6 (Time regularization in Hilbert spaces)**, intake `I0070`.

# R10 I0070 recovery1 — zero initial trace removes the Proposition-6.8 spatial-loss mechanism

Run ID: `20260916T2033Z_i0070_zero_trace_delta_bypass`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Dated source/status check: 2026-09-16  
Status: **PARTIAL / author-side full-source proof candidate; no campaign closure claim**.

No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, scheduler mutation, shared-root edit, claim-file edit, or peer-file edit was performed.

---

## 1. Continuity, admission evidence, exclusions, and neighboring work

I continued from the newest complete R10 report rather than restarting:

`runs/R10/20260916T1935Z_i0070_stuck1_endpoint_verification.md`.

That report was the mandatory STUCK1 thinking run after three consecutive unchanged metric runs. It chose exactly one recovery route: port Agresti--Veraar Part II Proposition 6.8 line-by-line, identify every place where the spatial loss `delta>0` is spent, and test whether the compact-Hilbert-tail mechanism can replace that expenditure at `delta=0`. It prescribed the present method triple **3, 7, 22**. I followed that route rather than adding another unrelated endpoint lemma.

Before new mathematics I read/recovered current `master` state for:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the current new-methods owner policy;
- canonical reservation `operations/claims/I0070.md`;
- the exact I0070 intake/ownership search surfaces under `probability_1000_intake_I_20260914/problems.jsonl` and its mirror;
- newest own R10 report;
- newest neighboring Agresti--Veraar P19 Problem-2 report `proofnet24/P19-closure-smr-optimal/runs/2026-09-16/2026-09-16T19-57-17Z__run-report.md`;
- newest neighboring P24 Problem-3 report `proofnet24/P24-probability-semigroup/runs/2026-09-16/2026-09-16T19-48-00Z__run-report.md`;
- newest R11 package `runs/R11/2026-09-16T19-40-00Z_i0054-pitman-yor-tangent-a4c2.md` for the directed independent audit below.

The connector truncates very large JSONL files if fetched wholesale. I therefore used exact-ID/source searches plus the canonical queue/claim surfaces; I do **not** claim a byte-for-byte model-visible reread of all roughly 780 intake rows.

### Admission evidence refreshed

The mathematical admission evidence is complete again on 2026-09-16:

1. the outside source is current and primary;
2. the current published survey still states Problem 6 as open;
3. `POSTED.md` excludes Agresti--Veraar Problems 4--5, not Problem 6;
4. P24 owns the distinct Problem 3 and P19 owns the distinct Problem 2;
5. exact-ID repository searches show no competing I0070 owner;
6. the live canonical reservation names R10 as owner.

The canonical file nevertheless still literally says `PENDING_ADMISSION, not READY`. Under the current fleet rule attacking workers do not rewrite coordinator-owned shared claim/ledger state. I therefore record **ADMISSION-EVIDENCE COMPLETE / CANONICAL FLAG STILL PENDING** rather than silently changing that file. The present research is continued under the owner's explicit R10 assignment and reservation; this report is not a coordinator READY mutation.

The old R10 square-lattice Cardy work remains preserved in its immutable reports and handoff and is not reopened.

---

## 2. Source target and exact hypotheses retained

The current journal source states Theorem 5.7 for `p>2`, `kappa=0`. Besides the conditions of Theorem 4.7 it assumes the local growth estimate

\[
 \|F(x)\|_{X_0}+\|G(x)\|_{\gamma(\mathcal U,X_{1/2})}
 \le C_n\sum_{j=1}^m \bigl(1+\|x\|_{X_{\beta_j,1}}^{\rho_j+1}\bigr)
\tag{2.1}
\]

for `||x||_{X_{1-1/p,infty}}<=n`, and assumes

\[
(A,B)\in \mathcal{SMR}_{r,\alpha}^{\bullet}
\quad\text{for all }r>2,
\quad 0\le\alpha<r/2-1.
\tag{2.2}
\]

Its conclusion is

\[
u\in H^{\theta,r}_{\rm loc}((0,\sigma);X_{1-\theta})
\cap C^{\theta-\varepsilon}_{\rm loc}((0,\sigma);X_{1-\theta})
\tag{2.3}
\]

for every `theta<1/2`, `r>=2`, and `0<epsilon<theta`.

For `p=2`, Assumption 3.1 of the source Hilbert theory requires `X_0` and `X_1` to be Hilbert spaces and identifies

\[
H:=X_{1/2}=(X_0,X_1)_{1/2,2}.
\tag{2.4}
\]

Theorem 4.7 gives the source p=2 maximal solution with

\[
u\in L^2_{\rm loc}((0,\sigma);X_1)
\cap C((0,\sigma);H).
\tag{2.5}
\]

For `p=2,kappa=0`, criticality of a pair `(beta_j,rho_j)` is equivalent, with

\[
s_j:=2\beta_j-1\in(0,1),
\tag{2.6}
\]

to

\[
s_j(\rho_j+1)=1,
\tag{2.7}
\]

and the source inequality gives `s_j(rho_j+1)<=1` in general.

Problem 6 asks whether the Theorem-5.7 conclusion extends to this p=2 Hilbert critical case. I retain every Theorem-5.7 hypothesis. In fact, the argument below uses the weaker growth estimate already supplied by Assumption 4.1 on bounded p=2 trace balls; I do **not** remove (2.1) from the source-matching statement.

Primary source URLs checked this run:

- current survey: https://doi.org/10.1007/s00030-025-01090-2;
- Part II: https://doi.org/10.1007/s00028-022-00786-7.

---

# 3. Move #22 — READ THE FAILURE: every place Proposition 6.8 spends `delta>0`

The nearest source-native solved theorem is Agresti--Veraar Part II, Proposition 6.8. Its `p=2` route obtains time regularity only after moving to an extrapolated spatial scale. The proposition imposes

\[
Y_\delta=X_0,\qquad Y_1=X_{1-\delta},\qquad
\frac1p=\frac{1+\alpha}{r}+\delta.
\tag{3.1}
\]

The paper explicitly says that when `p=2`, `delta=0` is impossible because

\[
\frac12>\frac{1+\alpha}{r}
\qquad
(0\le\alpha<r/2-1),
\tag{3.2}
\]

so (3.1) can hold only for `delta>0`.

I traced the proof line-by-line. The spatial loss is spent in four linked places.

### 3.1 Startup at a nonzero trace

Their first decisive step is

\[
X_p^{\rm Tr}\hookrightarrow Y_{\alpha,r}^{\rm Tr},
\tag{3.3}
\]

which lets them start a new nonlinear `L^r_alpha` solution `v` at the nonzero random state `u(epsilon)`. The identity (3.1) is exactly what makes this trace embedding available.

### 3.2 Compatibility / uniqueness between the two nonlinear solutions

For `delta>0`, strict inequality

\[
\frac{1+\alpha}{r}=\frac1p-\delta<\frac1p
\tag{3.4}
\]

gives the weighted-to-unweighted embedding needed to compare the `Y`-scale solution with the original `X`-scale solution. In the `delta=0,p>2` branch they instead choose an intermediate `q in (2,p)`. At `p=2` there is no such q below p.

### 3.3 Continuation

In their p=2 Step 2, the standard interpolation

\[
C([a,b];X_{1/2})\cap L^2(a,b;X_1)
\hookrightarrow
L^{2/\vartheta}(a,b;X_{(1+\vartheta)/2})
\tag{3.5}
\]

is matched to the shifted scale through

\[
\vartheta=1-2(\alpha/r+\delta)=2/r.
\tag{3.6}
\]

Again the `Y` scale already contains the spatial loss.

### 3.4 Nonlinear class embedding

Their final nonlinear estimate repeatedly uses

\[
Y_{\phi+\delta}=X_\phi.
\tag{3.7}
\]

Thus `delta` is not a cosmetic parameter that can simply be set to zero at the final line; it is woven through the startup trace, uniqueness comparison, continuation, and nonlinear embedding.

**Outcome of Move #22:** the source proof fails at `p=2,delta=0` first because it insists on starting a *new nonlinear higher-integrability solution from the nonzero trace* `u(epsilon)`. This identifies a different possible entry point: create a zero-trace problem on the desired positive-time interval and never construct that second nonlinear solution.

---

# 4. Move #7 — TAKE THE LIMIT: the naive `delta downarrow 0` route is invalid

A tempting argument would be to apply Proposition 6.8 for every `delta>0` and pass to `delta=0`. That is not valid abstractly.

On the standard Hilbert sequence scale

\[
\ell^2_s:=\Bigl\{x=(x_n):\sum_{n\ge2} n^{2s}|x_n|^2<\infty\Bigr\},
\]

take

\[
x_n=n^{-s-1/2}.
\]

Then for every `delta>0`,

\[
\sum_{n\ge2} n^{2(s-\delta)}|x_n|^2
=
\sum_{n\ge2}n^{-1-2\delta}<\infty,
\]

whereas

\[
\sum_{n\ge2} n^{2s}|x_n|^2
=
\sum_{n\ge2}n^{-1}=\infty.
\]

Therefore

\[
\bigcap_{\delta>0} X_{s-\delta}
\not\subseteq X_s
\tag{4.1}
\]

in general. A family of `delta>0` regularity statements with constants allowed to diverge as `delta downarrow0` cannot identify the zero-loss endpoint.

**Outcome of Move #7:** the spatial-loss limit route is rejected. Any valid proof must produce an estimate directly in the original `X` scale (or a uniform endpoint compactness principle stronger than Proposition 6.8 supplies).

---

# 5. Move #3 — PROVE SOMETHING STRONGER: a zero-trace, one-q endpoint bootstrap

The new result is a sharper formulation of the compact-tail idea from C004. It uses the source's original p=2 trace path and one auxiliary exponent `q>2`; it never constructs a second nonlinear q-solution with nonzero initial trace and never introduces a `Y_delta` scale.

## `R10-I0070-C005` — zero-trace compact-tail bootstrap

**STATUS: AUTHOR-SIDE PROVED / EXTERNAL AUDIT REQUIRED.**  
This is a theorem-sized source-matching proof candidate, not campaign closure.

### Statement

Assume the p=2, kappa=0 Hilbert specialization of Assumption 4.1 and Theorem 4.7, with

\[
(A,B)\in\mathcal{SMR}_{2,0}^{\bullet},
\]

and let `(u,sigma)` be its maximal p=2 solution. Assume the source critical condition

\[
(2\beta_j-1)(\rho_j+1)\le1
\quad (j=1,\ldots,m).
\tag{5.1}
\]

Fix one `q>2` and assume

\[
(A,B)\in\mathcal{SMR}_{q,0}^{\bullet}.
\tag{5.2}
\]

Retain the source growth hypothesis (5.21) (although the proof below already follows from Assumption 4.1's trace-ball growth bound).

Then for every compact interval `[a,b] subset (0,sigma)` and every

\[
0\le\theta<1/2,
\qquad \theta\ne1/q,
\tag{5.3}
\]

one has almost surely

\[
u\in H^{\theta,q}([a,b];X_{1-\theta}).
\tag{5.4}
\]

Consequently, if (5.2) holds for every q>2 as in Theorem 5.7, then for every `r>=2`, `theta<1/2`, and `0<epsilon<theta`,

\[
\boxed{
 u\in H^{\theta,r}_{\rm loc}((0,\sigma);X_{1-\theta})
 \cap C^{\theta-\varepsilon}_{\rm loc}((0,\sigma);X_{1-\theta}).
}
\tag{5.5}
\]

The exceptional value `theta=1/q` in (5.3) is exactly the value omitted by the source definition of `SMR^bullet_{q,0}` at q>2. It causes no gap in (5.5): for each requested `(theta,r,epsilon)`, choose an auxiliary `q>max{2,r,1/epsilon}` with `q != 1/theta` (if theta>0). There are infinitely many such q. On bounded time intervals, the standard same-smoothness integrability embedding passes `H^{theta,q}` to `H^{theta,r}`; and `q>1/epsilon` gives the desired Hölder embedding.

---

## 6. Proof of C005

### Step 1. Hilbert scale and compact spectral tails

Put

\[
H:=X_{1/2}=(X_0,X_1)_{1/2,2}.
\]

Because `(H,X_1)` is a densely embedded Hilbert couple, there is a positive self-adjoint scale operator `L` on H whose form domain is X1, with an equivalent norm

\[
\|x\|_{X_1}^2\simeq \|x\|_H^2+\|L^{1/2}x\|_H^2.
\]

Let

\[
P_R=\mathbf1_{[0,R]}(L).
\]

Then `P_R -> I` strongly on H, `P_R` is uniformly bounded on H and X1, and

\[
\|P_Rx\|_{X_1}\le C_R\|x\|_H.
\tag{6.1}
\]

On every compact positive-time interval `[a_0,T] subset (0,sigma)`, the source p=2 solution has a continuous H-valued path. Its path range is therefore compact in H. Strong convergence of a uniformly bounded operator family is uniform on compact sets, so pathwise

\[
\sup_{t\in[a_0,T]}
\|(I-P_R)u(t)\|_H\longrightarrow0.
\tag{6.2}
\]

No compact embedding `X_1 -> H` is assumed or used.

### Step 2. Critical interpolation with a small tail coefficient

For one source pair `(beta,rho)`, set

\[
s=2\beta-1\in(0,1).
\]

Hilbert reiteration and the source's real-interpolation convention give

\[
X_{\beta,1}=(H,X_1)_{s,1},
\tag{6.3}
\]

and hence, for `y in X1`,

\[
\|y\|_{X_{\beta,1}}
\le C\|y\|_H^{1-s}\|y\|_{X_1}^{s}.
\tag{6.4}
\]

Fix an H-bound K. Write

\[
x=v+w,
\qquad v=P_Rx,
\qquad w=(I-P_R)x.
\]

If

\[
\|x\|_H\le K,
\qquad
\|w\|_H\le\eta,
\tag{6.5}
\]

then by (6.1)--(6.4),

\[
\|v\|_{X_{\beta,1}}\le C_{R,\beta}K,
\]

and

\[
\|w\|_{X_{\beta,1}}
\le C\eta^{1-s}
       (\|x\|_{X_1}+C_RK)^s.
\tag{6.6}
\]

Raising to `rho+1` and using the triangle inequality yields

\[
\|x\|_{X_{\beta,1}}^{\rho+1}
\le C_{K,R}
 +C_K\eta^{(1-s)(\rho+1)}
       (\|x\|_{X_1}+C_{K,R})^{s(\rho+1)}.
\tag{6.7}
\]

By source criticality,

\[
a:=s(\rho+1)\le1.
\]

If `a<1`, Young's inequality gives, for every `eps0>0`,

\[
z^a\le \varepsilon_0 z+C_{a,\varepsilon_0}.
\]

If `a=1`, the coefficient in front of the linear X1 term in (6.7) is

\[
C_K\eta^{(1-s)(\rho+1)},
\]

and the exponent of eta is strictly positive because `s<1`.

Summing over the finitely many source pairs and using Assumption 4.1's growth bound on the H-trace ball therefore gives the endpoint absorption estimate:

> for every K and every `a0>0` there is `eta=eta(K,a0)>0` such that for every fixed R there is `C=C(K,R,a0)` for which
>
> \[
> \boxed{
> \|F(x)\|_{X_0}
> +\|G(x)\|_{\gamma(\mathcal U,H)}
> \le a_0\|x\|_{X_1}+C
> }
> \tag{6.8}
> \]
>
> whenever (6.5) holds.

This is the exact endpoint replacement for the small-time factor that disappears in the source's critical interpolation Lemma 4.3. At criticality the X1 power is exactly one, but compact Hilbert-tail smallness makes its coefficient small.

### Step 3. Borel rank-one linearization

Let

\[
Y:=X_0\oplus_1\gamma(\mathcal U,H),
\qquad N(x):=(F(x),G(x)).
\]

On the localized set, (6.8) says

\[
\|N(x)\|_Y\le a_0\|x\|_{X_1}+C.
\]

Define

\[
N_0(x)=
\begin{cases}
N(x),&\|N(x)\|\le C,\\
\frac{C}{\|N(x)\|}N(x),&\|N(x)\|>C,
\end{cases}
\qquad
N_1(x)=N(x)-N_0(x).
\tag{6.9}
\]

Then

\[
\|N_0(x)\|\le C,
\qquad
\|N_1(x)\|\le a_0\|x\|_{X_1}.
\tag{6.10}
\]

Since X1 is Hilbert at p=2, define for `x !=0`

\[
R_x z=
\frac{\langle z,x\rangle_{X_1}}
     {\|x\|_{X_1}^2}N_1(x),
\qquad R_0=0.
\tag{6.11}
\]

Then

\[
\|R_x\|_{\mathcal L(X_1,Y)}\le a_0,
\qquad
N(x)=R_xx+N_0(x).
\tag{6.12}
\]

Projecting onto the two components of Y gives

\[
F(x)=C_xx+f_x,
\qquad
G(x)=D_xx+g_x,
\tag{6.13}
\]

with

\[
\|C_x\|+\|D_x\|\le a_0,
\qquad
\|f_x\|+\|g_x\|\le C.
\tag{6.14}
\]

There is no differentiability assumption here: the linearization is rank one and is constructed only from the value of the nonlinearity.

### Step 4. Measurability of the random operator fields

In the survey, F and G in Assumption 4.1 are deterministic locally Lipschitz maps; in particular `x -> N(x)` is Borel on X1. For every fixed `z in X1`, the map

\[
x\mapsto R_x z
\]

is Borel. Thus it is enough to know that the a.e. X1-valued representative of the source solution can be chosen progressively measurable.

This follows from the source solution convention and a standard measurable-inverse argument. The solution is strongly progressive as an X0-valued process and belongs to `L^2_P(X_1)` a.e. On the separable closed X1-subspace generated by its essential range, the continuous injection into X0 is a Borel isomorphism onto its image (Lusin--Souslin). Pulling the X0-progressive representative back through that inverse gives an X1-valued strongly progressive representative after modification on a product-null set. Equivalently, this is the representative implicit in the source's `L^2_P` convention.

Consequently, for each fixed z,

\[
(t,\omega)\mapsto C_{u(t,\omega)}z,
\qquad
(t,\omega)\mapsto D_{u(t,\omega)}z
\tag{6.15}
\]

are strongly progressive. This is exactly the strong-operator progressive measurability required by the Part-II perturbation theorem. The same conclusion is immediate in the source's basic deterministic F,G setting; Remark 4.4's progressively `(t,omega)`-dependent extension can be handled by the same Caratheodory argument under its uniform hypotheses.

This measurability point was one of the explicit audit obligations in C004; it is now written as part of the proof rather than hidden under “routine”. It remains a priority for an external auditor.

### Step 5. The decisive zero-trace cutoff

Fix a compact target interval

\[
0<a<b<\sigma.
\]

Choose deterministic `a_0<a` and `T>b` and a smooth deterministic cutoff chi with

\[
\chi(a_0)=0,
\qquad
\chi=1\text{ on }[a,b].
\]

Set

\[
z=\chi u.
\]

Then z has **zero initial trace** at `a_0`. This is the point that removes the first and decisive use of `delta>0` in Proposition 6.8: zero belongs to every q-trace space, so no embedding of the nonzero state `u(epsilon)` into a stronger trace space is needed.

For deterministic integers `n,K,R`, let `sigma_n` be a source localizer and stop at

\[
\tau=
\sigma_n\wedge T\wedge
\inf\Bigl\{t\ge a_0:
 \|u(t)\|_H\ge K
 \text{ or }
 \|(I-P_R)u(t)\|_H\ge\eta
\Bigr\}.
\tag{6.16}
\]

On `[a_0,tau]`, (6.13)--(6.14) apply with the perturbation norm at most `a_0`.

Because C_x and D_x are linear,

\[
\chi C_u u=C_u(\chi u)=C_u z,
\qquad
\chi D_u u=D_u z.
\]

Therefore on `[a_0,tau]`, z solves

\[
\begin{aligned}
 dz+(A-C_t)z\,dt
 &= [\chi f_t+\chi' u]dt\\
 &\quad+[(B+D_t)z+\chi g_t]dW,
 \qquad z(a_0)=0,
\end{aligned}
\tag{6.17}
\]

where `C_t=C_{u(t)}`, etc.

### Step 6. Work on a deterministic horizon; no random-interval shortcut

Extend `C_t,D_t,f_t,g_t` by zero after tau and replace `chi'u` by `1_{t<=tau}chi'u`. We obtain a linear problem on the deterministic interval `[a_0,T]`.

Choose `a_0` in the absorption estimate (6.8) small enough that the Part-II perturbation criterion

\[
C^{\det}_{(A,B),q}\|C_t\|
+C^{\rm sto}_{(A,B),q}\|D_t\|<1
\tag{6.18}
\]

holds. If needed, choose it simultaneously below the p=2 perturbation threshold as well. Corollary 3.15 then gives

\[
(A-C_t,B+D_t)\in\mathcal{SMR}_{q,0}^{\bullet}
\]

on the deterministic horizon.

All inhomogeneities are bounded after localization: `f_t,g_t` by (6.14), while `u` in the cutoff term is H-bounded and `H -> X0`. Hence they lie in every finite Lq required by the linear theory. Let Z be the unique q-solution of the deterministic-horizon perturbed problem.

On a finite probability-time measure, the q-solution is also in the p=2 strong-solution class. On `[a_0,tau]`, z solves the same equation. The p=2 uniqueness supplied by perturbed stochastic maximal regularity therefore gives

\[
Z=z=\chi u
\qquad\text{on }[a_0,\tau].
\tag{6.19}
\]

This replaces all three later compatibility/continuation steps of Proposition 6.8: there is no second nonlinear solution and no `Y_delta` scale to compare back to X.

### Step 7. Linear q-regularity on the original X scale

Because the perturbed pair is in `SMR^bullet_{q,0}`, the zero-trace solution has

\[
Z\in H^{\theta,q}(a_0,T;X_{1-\theta})
\tag{6.20}
\]

for each `theta<1/2` except the source-definition exceptional `theta=1/q`. By (6.19) and `chi=1` on `[a,b]`, this gives (5.4) whenever `tau>b`.

### Step 8. Remove the spectral-tail stopping

Fix a sample path with `b<sigma`. Choose n with `b<sigma_n`, then K larger than

\[
\sup_{t\in[a_0,b]}\|u(t)\|_H.
\]

For that K and the already fixed perturbation smallness, choose eta from Step 2. By uniform compact-range convergence (6.2), choose an integer R so large that

\[
\sup_{t\in[a_0,b]}\|(I-P_R)u(t)\|_H<\eta.
\]

Then tau>b. The countable union over integers `(n,K,R)` covers the event `{b<sigma}`. Therefore (5.4) holds a.s. on every compact positive-time interval.

### Step 9. Recover the full Theorem-5.7 range

For a requested `r>2` and `theta<1/2`, use q=r unless `theta=1/r`; in that exceptional case choose any q>r with `q != 1/theta`. For r=2 choose q>2. The bounded-interval integrability embedding yields the desired `H^{theta,r}` result.

For Hölder regularity, given `0<epsilon<theta`, choose additionally `q>1/epsilon` and `q != 1/theta`. Then

\[
H^{\theta,q}([a,b];X_{1-\theta})
\hookrightarrow
C^{\theta-1/q}([a,b];X_{1-\theta})
\hookrightarrow
C^{\theta-\varepsilon}([a,b];X_{1-\theta}).
\]

This proves (5.5), subject only to the stated source hypotheses.

---

## 7. What is stronger than C004, and what is not claimed

C005 does not increase the frozen numeric metric: the largest proved exponent remains `theta_*=1/2` as a **supremum**, never the endpoint itself.

It strengthens the proof architecture in four ways:

1. it is source-native: the compact-tail estimate is derived directly from the p=2 Hilbert trace scale and Assumption 4.1's growth bound;
2. it isolates why Part II needs `delta>0` and bypasses that need by zero initial trace rather than by a formal `delta ->0` limit;
3. for a fixed q, it needs only `SMR^bullet_{2,0}` and `SMR^bullet_{q,0}`, not the whole all-r family; the all-r source assumption is used only to obtain every requested output exponent;
4. it explicitly handles the source-definition hole `theta=1/q` by choosing a different auxiliary q, rather than incorrectly claiming bullet-q regularity at the excluded value.

I do **not** claim:

- regularity at `theta=1/2`;
- a proof for assumptions weaker than the p=2 Hilbert source setting unless separately stated;
- closure before the required external audits;
- that the compact-tail/rank-one mechanism is novel in the literature.

Campaign label remains **PARTIAL / author-side proof candidate**.

---

## 8. Prior art and status screen — 2026-09-16

The current NoDEA survey still prints Problem 6. The direct text says that Theorems 5.6--5.7 bootstrap parabolic time regularity only for p>2, that p=2 is available in the subcritical case, and that Part-II Proposition 6.8 handles the critical p=2 case only under further restrictions with spatial loss.

The closest older proof is precisely Part-II Proposition 6.8, audited above line-by-line.

I also refreshed bounded searches around:

- `Agresti Veraar Problem 6 Hilbert p=2 critical time regularization`;
- `Theorem 5.7 p=2 Hilbert stochastic maximal regularity`;
- `critical stochastic maximal regularity compact spectral tail`;
- `endpoint Hilbert stochastic parabolic regularity compact path spectral cutoff`;
- later Agresti/Veraar papers and citing papers.

The most relevant later author paper found remains Agresti--Veraar, *A note on a threshold for temporal regularity of stochastic PDEs*, Comptes Rendus Math. 364 (2026), 371--379, DOI `10.5802/crmath.833`. It proves a sharp fixed-spatial-level temporal-regularity obstruction for a linear additive-noise model. It does not settle the parabolic time/space tradeoff in Problem 6.

I found no direct published resolution of Problem 6 and no direct statement of the zero-trace compact-tail/rank-one endpoint mechanism in this bounded search. This is **not a novelty certificate**; external prior-art review remains a closure obligation.

---

# 9. Independent audit of newest R11 package

Newest package read:

`runs/R11/2026-09-16T19-40-00Z_i0054-pitman-yor-tangent-a4c2.md`.

R11 claims `R11-I0054-C004`: a recursive positive-discount Pitman--Yor hierarchy with parameters `alpha_N,theta_N>=0`, `delta_N=alpha_N+theta_N ->0`, raw level length `delta_N`, converges on every fixed finite restriction and in the stated projective J1 topology to CTCS(infinity).

### Audit ID

`R10-AUDIT-R11-I0054-C004-PY-TANGENT-20260916`

### Verdict

**PASS for the finite-restriction generator and projective-convergence core.**  
**NOT an audit of source-intent / “superficially different” interpretation or worldwide prior art.**

### Independent derivation

For a particular Pitman--Yor partition with block sizes `n_1,...,n_r`,

\[
p_{\alpha,\theta}(n_1,\ldots,n_r)
=
\frac{\prod_{j=1}^{r-1}(\theta+j\alpha)}
     {(\theta+1)_{m-1}}
\prod_{\ell=1}^r(1-\alpha)_{n_\ell-1}.
\tag{9.1}
\]

Let `delta=alpha+theta` with alpha,theta nonnegative.

For no split,

\[
\frac{(1-\alpha)_{m-1}}{(1+\theta)_{m-1}}
=
\prod_{j=1}^{m-1}\frac{j-\alpha}{j+\theta}
=
1-\delta H_{m-1}+O_m(\delta^2).
\tag{9.2}
\]

For one particular binary split `A|A^c`, `|A|=i`,

\[
p_{\alpha,\theta}(A|A^c)
=(\theta+\alpha)
\frac{(1-\alpha)_{i-1}(1-\alpha)_{m-i-1}}
     {(1+\theta)_{m-1}}
=
\delta B(i,m-i)+O_m(\delta^2).
\tag{9.3}
\]

For r>=3, the EPPF contains both `(theta+alpha)` and `(theta+2alpha)`, hence each particular multifurcation is `O_m(delta^2)`.

The total binary rate is consistent with the diagonal term because

\[
\frac12\sum_{i=1}^{m-1}{m\choose i}B(i,m-i)
=
\frac12\sum_{i=1}^{m-1}\frac{m}{i(m-i)}
=H_{m-1}.
\tag{9.4}
\]

If the current finite partition has several nonsingleton blocks, independent block refinements imply that two distinct blocks both split in one raw step with probability `O(delta^2)`. Therefore, on every fixed finite partition state space,

\[
P_\delta=I+\delta Q+O(\delta^2),
\tag{9.5}
\]

where Q is exactly the CTCS binary-splitting generator. Standard finite-state rare-event convergence gives CTMC convergence under time acceleration `1/delta`.

For the projective topology, convergence of the first K labels controls the first K terms of the projective metric, while the remaining tail is at most `sum_{k>K}2^{-k}`. First let N tend to infinity at fixed K, then K tend to infinity. This yields the stated projective convergence.

Thus the mathematical tangent/generator core of R11-C004 survives an independent derivation. I do not certify that the positive-discount hierarchy satisfies the source's intended semantic threshold for a “superficially different” discrete model, nor do I certify novelty.

---

## 10. Metric / stuck state

The frozen metric did not move:

\[
\boxed{\theta_*=1/2\text{ as a supremum before and after}.}
\]

The endpoint `theta=1/2` remains unproved and is not part of Theorem 5.7's conclusion.

The supported unchanged count is now **4** after the metric-moving special-model run. This run is not another empty STUCK report: it executed the STUCK1 recovery route, rejected the naive delta-limit, mapped the source's exact loss mechanism, and replaced C004 by the more source-native zero-trace compiler C005. Nevertheless the owner-defined numeric metric itself did not move, so the unchanged count is not reset.

If the metric remains unchanged through six supported runs, the closable-track rotation rule applies.

The remaining mathematical obligations are now narrower than in STUCK1:

1. external audit of the strong-progressive measurability step in Section 6.4;
2. external audit that Corollary 3.15 plus zero-trace uniqueness is being used with exactly the source `SMR^bullet` norms and no hidden q-trace assumption;
3. independent prior-art search for compact-tail / rank-one absorption in endpoint stochastic maximal regularity;
4. the two required OTHER-track closure audits, including P26.

I do not create a paper folder before those gates are satisfied.

---

## 11. Checker / finite-evidence policy

This run introduces no new finite-enumeration claim. The new contribution is theorem-sized and its complete proof is written above. I therefore did not spend the run manufacturing a redundant checker. The exact critical-exponent arithmetic used here was already exercised by the earlier R10 I0070 checker; the new content is the functional-analytic zero-trace and perturbation argument, for which a finite arithmetic script would not certify the hard step.

The R11 audit was proved algebraically on the page; equation (9.4) is exact for arbitrary m, not a finite numerical experiment.

---

## 12. Model / scheduler control status

Actual runtime reported to this worker: **GPT-5.6 Sol**. Reasoning level is not exposed and is therefore **UNVERIFIED**.

The task interface available in this environment exposes task prompt/title, schedule, enablement, and timing mode. It exposes **no model-family selector and no reasoning-effort selector**. Therefore `GPT-6 / maximum` can be requested in prompt text but cannot be installed or verified by this worker.

Changing that requires either:

- an authorized product/task-owner interface that actually exposes model and reasoning fields for the existing task; or
- platform support / workspace administration to expose or repair those controls.

The historical `You cannot modify this task` result for one P26 task is permission/context-specific. Repository state records that another authorized context later succeeded for P26, so the denial is not proof that the task is globally immutable. The allowed workaround is to use the authorized owning context or platform support; cloning the task or bypassing permissions is not an acceptable workaround.

No scheduler mutation was attempted.

---

## 13. Next attack

Do **not** re-prove C005 next run. The highest-value next run is adversarial verification of the two remaining functional-analytic interfaces:

1. replace the measurable-inverse paragraph by a source-native lemma formulated directly in `L^2_\mathscr P(X_1)` and check every sigma-algebra/representative step;
2. challenge the same-smoothness `H^{theta,q}->H^{theta,r}` reduction at the source's Bessel-potential conventions and avoid it entirely where possible by choosing q=r;
3. search deterministic critical maximal-regularity / endpoint bootstrapping literature for the exact “zero initial trace + compact spectral tail + rank-one absorption” combination.

New Section-B moves reserved for that run: **#8 DISCRETIZE (operator-measurability finite/simple-process approximation), #19 MAKE IT AN ALGORITHM (construct the progressive coefficient approximation explicitly), #26 HUNT THE SPORADIC CASE (the exceptional theta=1/q and nonseparable Hilbert edge cases)**.

---

```yaml
ledger_delta:
  worker: R10
  source: "Agresti--Veraar, Nonlinear SPDEs and Maximal Regularity: An Extended Survey, NoDEA 32 (2025), Problem 6; arXiv:2501.18561 current v5"
  intake: I0070
  target: "Extend Theorem 5.7 to p=2, X0 Hilbert, under critical equality in (6.1), with source norms and restrictions unchanged"
  metric: "largest time-regularity exponent theta rigorously established for the frozen source-admissible critical p=2 target"
  before: "theta_* = 1/2 as supremum; endpoint not claimed"
  after: "theta_* = 1/2 as supremum; endpoint not claimed"
  movement: "no numeric movement; source-proof architecture strengthened C004 -> C005"
  unchanged_count: 4
  status: "PARTIAL / RECOVERY1 / author-side full-source proof candidate; external audits pending"
  methods: [3, 7, 22]
  exact_evidence:
    - "complete written proof R10-I0070-C005 in this immutable report"
    - "source Part-II Proposition 6.8 delta-use map, Sections 3-4"
    - "analytic counterexample showing intersection_{delta>0} X_{s-delta} need not imply X_s"
  own_claim_audits: []
  outgoing_audits:
    - "R10-AUDIT-R11-I0054-C004-PY-TANGENT-20260916 = PASS for generator/projective core only"
  admission: "research-side evidence complete; canonical operations/claims/I0070.md still PENDING_ADMISSION and was not edited"
  blockers:
    - "outside audit of progressive operator-valued measurability"
    - "outside audit of stopped perturbation/uniqueness source fit"
    - "second independent full audit including P26 gate"
    - "prior-art clearance"
```


FILE runs/R10/20260916T2236Z_i0070_sixrun_handoff_gate.md
Model actually running: GPT-5.6 Sol. Reasoning: UNVERIFIED — NO MOVEMENT in the frozen metric (`theta_* = 1/2` as a supremum before and after; endpoint `theta=1/2` not claimed). Problem/source: Antonio Agresti and Mark Veraar (2025), *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, Problem 6. Section-B moves used this run: **#10 DERANDOMIZE, #13 FIND WHAT ONLY INCREASES, #29 ADD THE POINTS AT INFINITY**. This is the **sixth consecutive unchanged I0070 run**, so under `NEW-METHODS-2026-09-16` the R10 attack is now **RETIRED-HANDOFF / PARTIAL**, not closed.

# R10 — I0070 six-run handoff: critical p=2 Hilbert regularity

Repository/branch: `yspennstate/math-open-problems` / `master`.
Outside source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 (historical intake locator v2; current source v5), NoDEA 32 (2025), Article 123, Problem 6.
Status after this run: **SOURCE OPEN in the current paper; R10 PARTIAL / author-side full-source proof candidate C006 preserved; 0/2 required external closure audits recovered; R10 attack retired after six unchanged metric runs.**

No email, Drive, public posting, purchases, permission changes, workflow execution, scheduler mutation, shared-ledger edit, or peer-file edit was performed.

---

## 1. Continuity recovered before mathematics

I continued from the newest immutable R10 state rather than restarting:

`runs/R10/20260916T2138Z_i0070_progressive_representative.md`.

That report retained

`theta_* = 1/2` as a supremum,

with endpoint `theta=1/2` not claimed, and promoted the compact-tail route to `R10-I0070-C006`, an author-side full-source proof candidate. Its campaign label remained PARTIAL because the required P26 audit and a second independent OTHER-track full audit were absent.

Before the present handoff I read/recovered the current control state including:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and current `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- canonical `operations/claims/I0070.md`;
- the newest R10 I0070 report and the previous I0070 proof-chain reports;
- current claim/ownership surfaces for the known CLOSABLE reserve;
- the newest task-health/admission reports;
- the available intake exact-ID/source records relevant to I0070 and successor screening.

The intake JSONL corpus is too large for one connector rendering, so I used the control files plus exact-ID/source retrieval rather than falsely claiming a byte-for-byte visual reread of all roughly 780 rows.

The canonical I0070 claim still literally says `PENDING_ADMISSION, not READY`; I did not mutate that coordinator-owned file. Research-side source/open-status/ownership work is preserved in the prior reports, but PENDING is not silently relabeled READY.

The old square-lattice Cardy line remains retired from this slot with all prior reports preserved. It was not reopened.

---

## 2. Fresh source/status check — 2026-09-17 Asia/Jerusalem

The current published source was checked again directly.

Primary URLs checked:

- https://doi.org/10.1007/s00030-025-01090-2
- https://arxiv.org/abs/2501.18561
- Agresti–Veraar Part II perturbation source: https://doi.org/10.1007/s00028-022-00786-7

The current published survey still states Problem 6 verbatim in substance:

> Let `X_0` be a Hilbert space. Does the regularization result of Theorem 5.7 extend to `p=2` in the critical case, i.e. equality in (6.1) for some `j`?

Theorem 5.7 retains the local growth condition (5.21), the all-`r>2`, all-admissible-`alpha` `SMR^bullet` assumption, and concludes

\[
u\in H^{\theta,r}_{\rm loc}((0,\sigma);X_{1-\theta})
\cap C^{\theta-\varepsilon}_{\rm loc}((0,\sigma);X_{1-\theta}),
\qquad 0\le \theta<\tfrac12,\ r\ge2,\ 0<\varepsilon<\theta.
\]

The current source explicitly says the known p=2 critical workaround is the older Part-II Proposition 6.8 under further restrictions; Problem 6 asks for the zero-loss Theorem-5.7 regularization.

Fresh dated searches used exact combinations of:

- `"Time regularization in Hilbert spaces" p=2 stochastic maximal regularity`;
- `Agresti Veraar Problem 6 time regularization`;
- `critical p=2 Theorem 5.7 Agresti Veraar`;
- `2501.18561 regularization Hilbert critical`.

I found recent adjacent work (including discrete stochastic maximal regularity and the Agresti–Veraar temporal-regularity counterexample note), but no later source explicitly announcing a resolution of Problem 6. This is bounded dated screening evidence, **not** proof of worldwide openness or novelty.

---

## 3. Retained C006 proof candidate — exact handoff statement

The proof candidate to preserve is:

### R10-I0070-C006 — AUTHOR-SIDE PROVED / EXTERNAL AUDIT REQUIRED

Assume the exact p=2 Hilbert specialization of the Theorem-5.7 framework, including:

1. Assumption 4.1 / the p=2 critical relation, equivalently `(2 beta_j - 1)(rho_j+1) <= 1` with equality allowed;
2. the source p=2 local solution / `(A,B) in SMR^bullet_{2,0}`;
3. the Theorem-5.7 local growth condition (5.21) with the exact `X_{1/2,infinity}` localization;
4. `(A,B) in SMR^bullet_{r,alpha}` for all `r>2` and all `0<=alpha<r/2-1` as in Theorem 5.7.

Then the candidate conclusion is exactly the Theorem-5.7 conclusion for p=2:

\[
\boxed{
u\in H^{\theta,r}_{\rm loc}((0,\sigma);X_{1-\theta})
\cap C^{\theta-\varepsilon}_{\rm loc}((0,\sigma);X_{1-\theta})}
\]

for every

\[
0\le\theta<\frac12,\qquad r\ge2,\qquad 0<\varepsilon<\theta.
\]

No endpoint `theta=1/2` is claimed.

The retained mechanism is:

- because `X_0` is Hilbert and `X_1=D(A)` with graph norm, the source's Hilbert proof supplies an invertible positive self-adjoint reference operator `A_0` with `D(A_0)=X_1`;
- set `H_0=D(A_0^{1/2})`, which agrees up to equivalent norms with both `[X_0,X_1]_{1/2}` and `(X_0,X_1)_{1/2,2}`;
- for `s=2 beta-1`, reiteration gives `X_{beta,1}=(H_0,X_1)_{s,1}`;
- spectral cutoffs `P_R=1_[0,R](A_0)` converge strongly on `H_0`, and uniformly on every compact positive-time path range;
- on an `H_0`-bounded tube with sufficiently small high-frequency `H_0` tail, the critical source growth becomes an arbitrarily small linear `X_1` coefficient plus a bounded remainder; at equality the small coefficient carries the exact power `eta^rho`;
- the nonlinear pair `(F,G)` is decomposed into a small rank-one leading-operator perturbation `(C_t,D_t)` plus bounded inhomogeneities;
- after a positive-time deterministic cutoff with zero trace and deterministic-horizon stopping/extension, Part-II Corollary 3.15 gives stochastic maximal regularity for `(A-C_t,B+D_t)` at p=2 and at a selected q>2;
- p=2 uniqueness identifies the q-regular linear solution with the stopped cutoff of the original nonlinear solution;
- path compactness removes the spectral-tail stopping, and a suitable q gives the requested `H^{theta,r}` and Hölder conclusions.

The newest exact algebra artifact retained from C006 checks the critical tail exponent identity and ends PASS; this handoff does not create a redundant new checker.

---

## 4. Method #10 — DERANDOMIZE: repair the remaining pointwise representative ambiguity

The most useful new proof audit this run concerns a subtle phrase in C006. Corollary 3.15 requires coefficient bounds in the strong pointwise/progressive sense, whereas the earlier report stated only that the constructed `X_1` representative agrees with `u` `dt dP`-a.e.

This can be repaired canonically, without an extra hypothesis.

Let

\[
S_n=n(n+A_0)^{-1}:X_0\to X_1.
\]

For every `x in X_0`, the spectral theorem gives

\[
S_nx\to x\quad\text{in }X_0.
\tag{4.1}
\]

For every `x in X_1`, one additionally has

\[
S_nx\to x\quad\text{in }X_1.
\tag{4.2}
\]

For the strongly progressive `X_0`-valued solution process `u`, define the progressive set

\[
E:=\{(t,\omega):(S_nu(t,\omega))_n\text{ is Cauchy in }X_1\}.
\]

Since each `S_nu` is strongly progressive as an `X_1`-valued process, `E` is progressive. Define

\[
\widetilde u(t,\omega)=
\begin{cases}
\lim_n S_nu(t,\omega),&(t,\omega)\in E,\\
0,&(t,\omega)\notin E.
\end{cases}
\tag{4.3}
\]

Then `tilde u` is strongly progressive into `X_1`.

The stronger pointwise fact is

\[
\boxed{E=\{(t,\omega):u(t,\omega)\in X_1\},\qquad \widetilde u=u\text{ pointwise on }E.}
\tag{4.4}
\]

Proof: if `u(t,omega) in X_1`, (4.2) gives membership in `E` and the limit is `u`. Conversely, if `(t,omega) in E`, the `X_1` limit `y` also converges in `X_0`; by (4.1) the same sequence converges in `X_0` to `u(t,omega)`, hence `u(t,omega)=y in X_1` by injectivity of the embedding.

This matters for the stopped compact-tail tube. Before the tube stopping time, on `E` we have `tilde u=u`, so every `H_0` and spectral-tail bound used in the critical absorption estimate holds pointwise. On `E^c`, `tilde u=0`, so the same bounds hold trivially. Therefore the small operator-norm bound for `(C_t,D_t)` can be imposed **for all times on the stopped interval outside a single omega-null exceptional set**, as required by the perturbation theorem; it is not merely an `dt dP`-a.e. estimate.

The nonlinear identity with the original solution is only needed at `X_1`-valued times. Since `u in L^2_{loc}(X_1)`, those times have full Lebesgue measure pathwise. Hence changing the coefficients/inhomogeneity on `E^c` does not alter the integral equation.

This is a proof-hardening result, not metric movement and not an independent closure audit.

---

## 5. Method #13 — FIND WHAT ONLY INCREASES: deterministic spectral-tail exhaustion

A second possible hidden selection issue is the pathwise choice of the cutoff `R`.

Because `P_R` is a nested spectral family for `A_0`, for every fixed `x in H_0`,

\[
R\mapsto \|(I-P_R)x\|_{H_0}
\]

is nonincreasing. For a compact path range `K subset H_0`, define

\[
q_K(R):=\sup_{x\in K}\|(I-P_R)x\|_{H_0}.
\]

Then `q_K(R)` is nonincreasing and, by strong convergence plus uniform convergence on compact sets,

\[
q_K(R)\downarrow0.
\tag{5.1}
\]

Thus no measurable choice of a random spectral scale is required. One can use deterministic integer cutoffs `R=m` and the countable events

\[
\{q_{K(\omega)}(m)<\eta\},\qquad m\in\mathbb N,
\]

whose union exhausts every path with compact positive-time `H_0` range. This is exactly compatible with the countable localization step in C006.

Again, this repairs a possible implementation concern but does not move `theta_*`.

---

## 6. Method #29 — ADD THE POINTS AT INFINITY: endpoint `theta=1/2` is not the source target

The only numerical way to increase the frozen metric after `theta_*=1/2` as a supremum would be to reinterpret the endpoint as an attained maximum. That would be the wrong target.

Theorem 5.7 itself states `theta in [0,1/2)`, not `theta=1/2`. This is consistent with the stochastic half-derivative barrier already visible in the survey's linear theory. The recent Agresti–Veraar note on failure of temporal regularity provides additional warning that temporal endpoint statements require extra spatial regularity even for linear Hilbert-space SPDEs.

Therefore I did **not** relabel endpoint attainment as the next R10 metric goal and did not claim `theta=1/2`. The frozen source-exact metric has genuinely saturated at its correct supremum, which is why the six-run rotation rule now applies.

---

## 7. Adversarial status of C006 after this run

I rechecked the following source-sensitive points rather than assuming them:

- the current survey explicitly identifies `X_{1/2}=(X_0,X_1)_{1/2,2}` in the p=2 Hilbert case;
- Theorem 3.13 explicitly constructs a positive self-adjoint reference `A_0` with `D(A_0)=X_1`;
- current Definition 3.8 gives the higher-p bullet time-regularity estimate for every `theta in (0,1/2)` on deterministic intervals;
- Part-II Corollary 3.15 allows small strongly progressively measurable perturbations of both deterministic and stochastic leading operators;
- the older Part-II random-initial-time bullet definition has a technical exceptional time exponent in one formulation, but the present C006 argument deliberately starts the cutoff at a deterministic positive time. The fixed-time case is the one where the source notes the exceptional exponent can be recovered by interpolation.

I did not find a new source-exact counterexample to C006 in this run. That is **not** an independent audit: it is an author-side self-check.

The remaining closure obligations are external:

1. P26 full source/proof audit of C006 with the pointwise representative repair above;
2. one second full independent audit from another track;
3. independent prior-art clearance strong enough to distinguish a genuinely new endpoint compact-tail argument from an already known abstract perturbative regularization lemma.

Until those exist, Problem 6 is not called closed and no paper folder is created.

---

## 8. Six-run rotation and successor gate

The fixed metric history is preserved exactly:

- first source-admissible critical special-model run: `UNMEASURED -> theta_*=1/2` as a supremum;
- subsequent C002/C003/C004/C005/C006 proof-generalization runs: no numerical change;
- present run: no numerical change.

Therefore the unchanged count is now **6**.

Per `NEW-METHODS-2026-09-16`, a CLOSABLE target retires after six unchanged runs. Accordingly:

\[
\boxed{\text{R10/I0070 is now RETIRED-HANDOFF from active R10 attacking research.}}
\]

This means only that R10 stops spending hourly research runs on new I0070 lemmas. It does **not** mean the source is solved, refuted, known, or abandoned. C006 plus the present representative repair remain available for independent audit and later reassignment.

I then screened the current same-category reserve before attempting a create-only successor claim. The currently verified CLOSABLE candidates visible in the latest admission/claim surfaces are already consumed by exclusive claims (including the admitted complete-mixability cluster and the admitted I0004/I0075 successors), while the newest coordinator/task-health status explicitly reports no newly admitted READY/CLOSABLE/unassigned successor. Other queue entries remain PENDING current-status/scope/ownership or are HARD rather than CLOSABLE. I therefore did **not** fabricate readiness and did not create a conflicting claim.

Current successor state for R10:

\[
\boxed{\text{SUCCESSOR GATE — no currently certified READY / CLOSABLE / UNASSIGNED target found.}}
\]

The next R10 research run should first consume a newly admitted same-category candidate if one appears; it must not restart I0070 merely because the scheduler prompt is stale.

---

## 9. R11 directed-audit status

Repository search found no newer R11 run at `2026-09-16T21*` or `T22*`. The newest located R11 theorem package remains the `20:40Z` I0054 random-recursive-tree package, whose finite hazard/generator core was already independently audited by R10 in the preceding run. I did not duplicate that audit merely to manufacture activity.

---

## 10. Model/runtime escalation state

The interface exposed to this worker still has no model-family selector and no reasoning-effort selector. It exposes task prompt/title, schedule/timing, and enablement-type controls, but cannot set or verify GPT-6/maximum. Thus GPT-6/maximum remains requested prompt text only; the actual model for this report is GPT-5.6 Sol and reasoning is UNVERIFIED.

Changing this requires either an authorized product/workspace scheduler interface that actually exposes model and reasoning fields or platform support changing the scheduler/runtime capability. A native `You cannot modify this task` result, such as the historical P26 denial, is a permission/context issue: the legitimate workaround is an authorized task-owner/workspace context or platform support, not cloning the task or bypassing permissions. No scheduler mutation was attempted in this run.

---

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R10
  deployment: NEW-METHODS-2026-09-16
  source:
    authors: "Antonio Agresti and Mark Veraar"
    title: "Nonlinear SPDEs and Maximal Regularity: An Extended Survey"
    locator: "Problem 6; historical intake arXiv:2501.18561v2; current v5 / NoDEA 32 (2025), Article 123"
    intake_id: I0070
    checked_current_source: true
    source_status: "OPEN in current published survey; bounded 2026-09-17 search found no explicit later resolution"
  target: "Extend Theorem 5.7 to critical p=2 Hilbert case without strengthening source hypotheses"
  metric:
    name: "largest source-valid time regularity exponent theta"
    before: "theta_* = 1/2 as supremum; endpoint not claimed"
    after: "theta_* = 1/2 as supremum; endpoint not claimed"
    movement: "NO MOVEMENT"
    unchanged_count: 6
  methods_this_run: [10, 13, 29]
  new_handoff_repair:
    statement: "Yosida representative can be chosen pointwise so E={u in X1}; stopped perturbation bounds hold pointwise in time, while nonlinear equality is needed only a.e."
    status: "AUTHOR-SIDE PROVED / self-check only"
  retained_main_claim:
    id: "R10-I0070-C006"
    status: "AUTHOR-SIDE PROVED / EXTERNAL AUDIT REQUIRED"
    campaign_status: PARTIAL
    external_audits_found: 0
    required_external_audits: 2
  rotation:
    triggered: true
    reason: "six consecutive unchanged metric runs on a CLOSABLE target"
    i0070_active_attack: "RETIRED-HANDOFF"
    successor_claim_created: false
    successor_reason: "no currently certified READY / CLOSABLE / UNASSIGNED target found; latest coordinator state is a successor gate"
  exact_evidence:
    retained:
      - "artifacts/R10/20260916T2138Z_i0070_progressive_representative_checker.py"
      - "artifacts/R10/20260916T2138Z_i0070_progressive_representative_checker.out (ALL_EXACT_CHECKS_PASS)"
    new_finite_claim_this_run: false
    new_checker_this_run: false
  peer_audit:
    r11_new_package_found: false
    action: "no duplicate audit"
  closure_blockers:
    - "P26 full source/proof audit"
    - "second independent OTHER-track full audit"
    - "independent prior-art clearance"
  delivery:
    github_report: "runs/R10/20260916T2236Z_i0070_sixrun_handoff_gate.md"
    email: "not used"
    drive: "not used"
```
