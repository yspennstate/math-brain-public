Model: GPT-5.6 Sol. Reasoning: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no model-family or reasoning-effort selector, so I do not claim it. **No numeric metric movement:** `theta_* = 1/2` as a supremum before and after; endpoint `theta=1/2` is not claimed. This is the fifth consecutive unchanged metric run after the metric-moving special-model run. New-method moves actually used: **#1 CHANGE THE CATEGORY, #19 MAKE IT AN ALGORITHM, #27 SWAP THE QUANTIFIERS**.

Problem/source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, historical intake locator arXiv:2501.18561v2, current arXiv v5 / NoDEA 32 (2025), Article 123, **Problem 6 (Time regularization in Hilbert spaces)**, intake `I0070`.

Status: **PARTIAL / RECOVERY2 / author-side full-source proof candidate strengthened; external closure audits still missing.**

# R10 I0070 — Hilbert reference-scale and progressive-representative repair

Run ID: `20260916T2138Z_i0070_progressive_representative`
Repository/branch: `yspennstate/math-open-problems` / `master`
Dated source/status check: 2026-09-16/17 UTC boundary

No Gmail/email, Drive, public posting, purchases, permission changes, workflow execution, shared-root edit, peer-file edit, or scheduler mutation was performed.

---

## 1. Continuity, repository state, ownership and admission

I continued from the newest complete R10 state rather than restarting:

`runs/R10/20260916T2033Z_i0070_zero_trace_delta_bypass.md`.

That report retained the frozen metric

`theta_* = 1/2` as a supremum,

and stated the full-source zero-trace compact-tail candidate `R10-I0070-C005`. The three issues most worth an adversarial source audit were (i) the mismatch between the source's complex `X_{1/2}` and real trace `X_{1/2,2}` notation, (ii) strong progressive measurability of the rank-one operator coefficients because a source strong solution is only a.e. `X_1`-valued, and (iii) whether the proof secretly needs one perturbation-smallness constant uniform in every auxiliary exponent `q>2`.

Before new research I read/recovered the required current repository surfaces: campaign `INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; `operations/NEW_METHODS_2026-09-16.md`; the exact claim `operations/claims/I0070.md`; the newest R10 report; the newest neighboring Agresti--Veraar Problem-2 report from P19 and Problem-3 report from P24; and the newest R11 report for the directed peer audit.

The intake JSONL corpus is too large for one connector rendering. I do **not** claim a byte-for-byte visual reread of roughly 780 JSONL rows. I recovered the exact I0070 source/claim/ownership surfaces and the current queue/exclusion surfaces instead.

The canonical I0070 claim still says:

- owner `R10`, native task `6aa7b669391081918ba308c31573a86e`;
- status `PENDING_ADMISSION, not READY`;
- source Agresti--Veraar Problem 6;
- the exact metric used here.

No competing owner was found. P19 currently owns the distinct Agresti--Veraar Problem 2 / I0068; P24 owns the distinct Problem 3 / I0063=I0069. The already-written Problems 4--5 material remains excluded by the owner policy and was not reopened. The old square-lattice Cardy R10 route remains preserved in immutable history and retired from this slot.

Research-side admission evidence is now complete enough to continue the reserved target: exact source statement recovered; current published source still prints Problem 6; current literature screen refreshed; adjacent ownership is distinct; and no `POSTED.md` settlement of Problem 6 was found. I did not mutate the coordinator-owned claim, so I do not relabel its canonical state from `PENDING_ADMISSION` to `READY` myself.

---

## 2. Exact source target and current-status check

The current published survey (NoDEA 32 (2025), Article 123, published 1 September 2025, DOI `10.1007/s00030-025-01090-2`) still states:

> **Problem 6 (Time regularization in Hilbert spaces).** Let `X_0` be a Hilbert space. Does the regularization result of Theorem 5.7 extend to `p=2` in the critical case (i.e. equality in (6.1) holds for some `j`)?

The current source's Theorem 5.7 assumes the conditions of Theorem 4.7 with `p>2`, `kappa=0`, the additional growth bound

`||F(x)||_{X_0}+||G(x)||_{gamma(U,X_{1/2})}
 <= C_n sum_j (1+||x||_{X_{beta_j,1}}^{rho_j+1})`

for `||x||_{X_{1-1/p,infty}}<=n`, and `(A,B) in SMR^bullet_{r,alpha}` for all `r>2`, `0<=alpha<r/2-1`. Its conclusion is

`u in H^{theta,r}_loc((0,sigma);X_{1-theta})
     cap C^{theta-epsilon}_loc((0,sigma);X_{1-theta})`

for every `theta in [0,1/2)`, `r in [2,infty)`, `0<epsilon<theta`.

For `p=2`, Assumption 6.1 has `beta_j in (1/2,1)`, `rho_j>=0` and

`(2 beta_j-1)(rho_j+1) <= 1`.                                         (2.1)

The p=2 local theory gives paths in `L^2_loc(X_1) cap C(X_{1/2})`. Definition 3.8 is important below: for every `q>2`, `SMR^bullet_{q,0}` supplies `H^{theta,q}` time regularity for **all** `theta in (0,1/2)`; there is no exclusion at `theta=1/q`.

This corrects one sentence in the preceding R10 report: its claimed source exclusion `theta != 1/q` is not present in the current Definition 3.8. I record this as

`R10-I0070-X001 — DISPROVED (R10 bookkeeping claim, not a source claim): the current source Definition 3.8 does not exclude theta=1/q.`

The correction simplifies the quantifier bookkeeping below and does not alter any source hypothesis.

### Current-literature screen

Dated searches included:

- `Agresti Veraar Problem 6 2501.18561 time regularization Hilbert`;
- `critical Hilbert p=2 Theorem 5.7 stochastic maximal regularity`;
- `Agresti Veraar temporal regularity threshold 2026 stochastic PDE`;
- `2501.18561 Problem 6 2026`;
- the exact Part-II perturbation theorem / Corollary 3.15.

The current survey remains the primary open-problem source. Agresti--Veraar's later temporal-threshold note gives a sharp fixed-spatial-level obstruction for a linear self-adjoint problem; it does not identify the parabolic time/space tradeoff asked here. The 2022 Part-II paper remains the relevant small-perturbation source. I found no later paper in this bounded dated search explicitly resolving Problem 6. This is **not** a worldwide novelty certificate.

---

## 3. Inherited proof architecture retained, not re-proved

The following pieces from C002--C005 are retained in their exact scopes.

1. **Compact-path tail idea.** At p=2, a compact positive-time piece of the solution path is compact in the Hilbert trace space. Strongly convergent Hilbert spectral cutoffs therefore converge uniformly on that path range.
2. **Critical tail absorption.** Writing `s_j=2 beta_j-1`, the critical exponent is `s_j(rho_j+1)<=1`. On an H-bounded set with a small high-frequency H-tail, the polynomial nonlinearities satisfy an arbitrarily-small-linear `X_1` bound plus a bounded remainder.
3. **Zero-trace cutoff.** Multiplying by a deterministic cutoff which vanishes at a positive time avoids the nonzero-trace spatial-loss mechanism that appears in the known p=2 Proposition 6.8 route.
4. **Random linear perturbation.** The nonlinear value can be decomposed into a small linear leading perturbation plus a bounded inhomogeneity; the small-perturbation theorem can then be used at p=2 and a chosen exponent q>2.

This run does not count those as new metric movement. It repairs their source-space and measurability implementation.

---

# 4. Move #1 — CHANGE THE CATEGORY: use the source's Hilbert reference operator

The source distinguishes

`X_theta=[X_0,X_1]_theta`

from

`X_{theta,r}=(X_0,X_1)_{theta,r}`.

C005 used the shorthand `H=X_{1/2}` as though it were automatically the real trace `X_{1/2,2}`. In a general Banach couple that would be wrong. In **Problem 6** it can be repaired without adding a hypothesis.

Because `X_0` is Hilbert and Assumption 4.1 sets `X_1=D(A)`, the graph domain is a Hilbert space after replacing its usual graph norm by the equivalent Hilbert graph norm

`||x||_{1,h}^2 := ||x||_{X_0}^2+||Ax||_{X_0}^2`.                 (4.1)

More source-natively, the proof of source Theorem 3.13 chooses an invertible positive self-adjoint operator `A_0` on `X_0` with

`D(A_0)=X_1`                                                       (4.2)

with equivalent graph norm. This construction is already part of the source Hilbert-space maximal-regularity proof; using it is not self-adjointness of the original operator A.

Put

`H_0 := D(A_0^{1/2})`.

For a Hilbert couple one has, with equivalent norms,

`H_0 = [X_0,X_1]_{1/2} = (X_0,X_1)_{1/2,2}`.                     (4.3)

Thus the source p=2 continuity space `X_{1/2}` and the real p=2 trace space `X_{1/2,2}` coincide up to equivalent Hilbert norms. In particular

`H_0 -> X_{1/2,infty}`,                                           (4.4)

so an H_0-bound is sufficient to invoke the exact p=2 specialization of the Theorem-5.7 growth condition (5.21).

For `beta in (1/2,1)` set

`s:=2 beta-1 in (0,1)`.

Real-interpolation reiteration in this Hilbert couple gives

`X_{beta,1} = (H_0,X_1)_{s,1}`                                  (4.5)

with equivalent norms. This is also exactly the p=2 case of the interpolation mechanism used by the source around Lemma 4.3.

Now take spectral projections of the **reference** operator, not the possibly non-self-adjoint SPDE operator:

`P_R := 1_[0,R](A_0)`.

They satisfy

`P_R -> I strongly on H_0`,

`P_R X_1 subset X_1`, and

`||P_R x||_{X_1} <= C_R ||x||_{H_0}`.                            (4.6)

Since the p=2 solution is continuous into H_0, the image of each compact positive-time interval is compact in H_0, and therefore

`sup_t ||(I-P_R)u(t)||_{H_0} -> 0`.                              (4.7)

This is the exact compact-tail statement C005 needs. It assumes no compact embedding `X_1 -> H_0` and no spectral property of the original A or B.

---

## 5. Endpoint absorption with the exact critical coefficient

Fix one pair `(beta,rho)` and put `s=2 beta-1`. On

`||x||_{H_0}<=K`,

`||(I-P_R)x||_{H_0}<=eta`,

write `v=P_Rx`, `w=(I-P_R)x`. By (4.5),

`||w||_{X_{beta,1}}
 <= C ||w||_{H_0}^{1-s} ||w||_{X_1}^s
 <= C eta^{1-s} (||x||_{X_1}+C_R K)^s`.                         (5.1)

The low part `v` is bounded in `X_1`, hence also in `X_{beta,1}`, by a constant depending on K and R. Raising (5.1) to `rho+1` gives a highest `X_1` power

`s(rho+1)<=1`.                                                    (5.2)

If the inequality is strict, Young's inequality makes its linear `X_1` coefficient arbitrarily small.

At exact criticality,

`s(rho+1)=1`,                                                     (5.3)

the coefficient of the linear `||x||_{X_1}` term is proportional to

`eta^{(1-s)(rho+1)}`.

But (5.3) gives the exact identity

`(1-s)(rho+1)=rho`.                                               (5.4)

Since `s<1`, equality forces `rho>0`. Thus the critical coefficient is `O(eta^rho)` and can be made arbitrarily small. The exact checker tests (5.3)--(5.4) over 900 rational positive rho values.

After summing the finitely many source pairs and applying (5.21), we obtain the source-norm estimate:

### `R10-I0070-C006a — PROVED (deterministic endpoint absorption)`

For every H_0-bound K and every `a>0`, there exists `eta=eta(K,a)>0`, **independent of R**, such that for every finite R there is `C=C(K,a,R)` with

`||F(x)||_{X_0}+||G(x)||_{gamma(U,H_0)}
 <= a ||x||_{X_1}+C`                                             (5.5)

whenever

`||x||_{H_0}<=K`, `||(I-P_R)x||_{H_0}<=eta`.

The independence of eta from R matters: first choose the perturbation size a and H-bound K, then eta, and only afterwards use compactness of the actual path to choose R large enough. There is no circular `R -> eta(R) -> R` selection.

Equivalent Hilbert/source graph norms only change the constant multiplying a. Since a is chosen arbitrarily small, this is absorbed before applying the perturbation theorem; no new norm hypothesis is inserted.

---

# 6. Move #19 — MAKE IT AN ALGORITHM: construct an X_1-progressive representative

The strongest unresolved implementation issue in C005 was real: Definition 4.5 gives a strongly progressive X_0-valued process with a.e. `X_1` membership, whereas the operator coefficient

`R_{u(t,omega)} in L(X_1,Y)`

should be strongly progressively measurable. Saying “choose an X_1 representative” is not enough.

The reference operator A_0 gives an explicit construction.

For n>=1 define

`S_n := n(n+A_0)^{-1}: X_0 -> X_1`.                              (6.1)

Each S_n is deterministic and bounded from X_0 into X_1. Therefore `S_n u` is strongly progressively measurable as an X_1-valued process. For every x in X_1,

`S_n x -> x in X_1`                                               (6.2)

because the convergence holds simultaneously for x and A_0x by the spectral calculus / graph norm.

Define the progressive set

`E = { (t,omega): (S_n u(t,omega))_n is Cauchy in X_1 }`.          (6.3)

The Cauchy criterion shows E is progressive. Define

`u_tilde(t,omega)=lim_n S_nu(t,omega)` in X_1 on E,

and `u_tilde=0` off E.                                            (6.4)

Pointwise limits of strongly progressive X_1-valued maps are strongly progressive. Since the source solution lies in `L^2_loc(X_1)`, one has

`u_tilde=u` as X_0-valued processes for dt x dP-a.e. point.       (6.5)

This gives a canonical X_1-progressive representative for all coefficient constructions, without a separability shortcut and without assuming better path regularity than the source provides.

Now let

`Y := X_0 direct_sum_1 gamma(U,H_0)`,

`N(x):=(F(x),G(x))`.

On the localized set C006a yields

`||N(x)||_Y <= a ||x||_{X_1}+C`.                                 (6.6)

Define the bounded radial part

`b(x)=N(x)` if `||N(x)||<=C`, and

`b(x)=C N(x)/||N(x)||` otherwise,

and set `n(x)=N(x)-b(x)`. Then

`||b(x)||<=C`, `||n(x)||<=a||x||_{X_1}`.                         (6.7)

Using the equivalent Hilbert graph inner product on X_1, define for x!=0

`R_x z = <z,x>_{X_1,h}/||x||_{X_1,h}^2 * n(x)`,

and `R_0=0`.                                                       (6.8)

After absorbing the fixed graph-norm equivalence factor into a,

`||R_x||_{L(X_1,Y)}<=a`, `R_xx=n(x)`, and

`N(x)=R_xx+b(x)`.                                                 (6.9)

The map x -> R_x z is Borel for every fixed z in X_1. Composing with `u_tilde` proves the exact evaluation-wise strong progressive measurability required for the Part-II perturbation theorem. Projecting Y onto its two coordinates gives

`F(u)=C_tu+f_t`,

`G(u)=D_tu+g_t`                                                   (6.10)

for dt x dP-a.e. point on the localization, with `C_t,D_t` strongly progressively measurable,

`||C_t||+||D_t|| <= a`,

and `||f_t||+||g_t|| <= C`.                                      (6.11)

This closes the main measurability gap listed in C003--C005.

---

# 7. Move #27 — SWAP THE QUANTIFIERS: no uniform-in-q perturbation smallness

A hidden strengthening would occur if the proof required one tail parameter eta or one perturbation coefficient a that works uniformly for **all** `q>2`. It does not.

For each requested target regularity, choose only the finitely many exponents needed for that target.

- To prove `H^{theta,r}` for a fixed `r>2`, use q=r.
- To prove the r=2 member, choose any fixed q>2, obtain `H^{theta,q}` in the same spatial space, and use the standard bounded-interval embedding `H^{theta,q}(I;X_{1-theta}) -> H^{theta,2}(I;X_{1-theta})` (here `X_{1-theta}` is Hilbert up to an equivalent norm).
- To prove `C^{theta-epsilon}`, choose a separate q_H>max{2,1/epsilon}; Definition 3.8 gives `H^{theta,q_H}` for every theta<1/2, and one-dimensional Sobolev embedding gives `C^{theta-1/q_H} -> C^{theta-epsilon}`.

Thus the quantifier order is

`for every (theta,r,epsilon), there exist finitely many q's and an a>0 small for exactly those q's`,

not

`there exists one a>0 that works for every q>2`.                  (7.1)

For a fixed q, let `delta_2>0` and `delta_q>0` be the perturbation margins coming from Part-II Corollary 3.15 for the source pairs at p=2 and p=q. Choose a so small that the deterministic/stochastic operator differences in (6.11) are below both fixed thresholds. C006a then gives eta(K,a).

No uniform-in-q estimate is used.

---

# 8. Full deterministic-horizon localization compiler

I now restate the full proof in source order, incorporating the repairs above.

Fix a compact interval `[a,b] subset (0,sigma)` pathwise and choose deterministic `t_0<a` and a smooth deterministic cutoff chi with

`chi(t_0)=0`, `chi=1` on `[a,b]`.                                 (8.1)

Let `(sigma_n)` be a source localizing sequence. Fix deterministic K,R and the eta from C006a, and define the stopping time

`tau := sigma_n wedge T wedge inf{t>=t_0:
          ||u(t)||_{H_0}>=K or ||(I-P_R)u(t)||_{H_0}>=eta }`.      (8.2)

On `[t_0,tau]`, use (6.10). Extend `C_t,D_t,f_t,g_t` by zero after tau. Put `z=chi u`. Then up to tau,

`d z +(A-C_t)z dt
 = [chi f_t + chi' u]dt
   +[(B+D_t)z+chi g_t]dW`,

`z(t_0)=0`.                                                        (8.3)

For use on the deterministic horizon `[t_0,T]`, insert the stopped indicator in the inhomogeneous `chi'u` term and use the zero-extended coefficients. The H_0 stopping and bounded remainders make all inhomogeneities bounded in every finite `L^q(Omega x (t_0,T))` in the exact source spaces `X_0` and `gamma(U,X_{1/2})`.

Choose a below the Part-II perturbation thresholds at p=2 and the selected q. Corollary 3.15 then gives stochastic maximal regularity for

`(A-C_t, B+D_t)`                                                  (8.4)

at both exponents. It is important that B itself need not be small: D_t is a small perturbation of the **already assumed** source pair `(A,B)`.

Solve (8.3), with stopped/extended coefficients, at q on the deterministic horizon. The q-solution belongs to the p=2 solution class on the finite probability-time measure. On `[t_0,tau]`, `z=chi u` is a p=2 strong solution to the same random linear equation. The p=2 uniqueness supplied by stochastic maximal regularity therefore gives

`Z=chi u` on `[t_0,tau]`.                                         (8.5)

Definition 3.8 for q>2 then gives

`chi u in H^{theta,q}(t_0,T;X_{1-theta})`

up to tau for **every theta in (0,1/2)**.                          (8.6)

There is no `theta=1/q` exception.

Finally remove the stopping. On every sample path with `b<sigma`, choose n with `b<sigma_n`; continuity in H_0 makes the H_0 norm bounded on `[t_0,b]`, so choose an integer K above it. C006a then gives a deterministic eta(K,a). The path range on `[t_0,b]` is compact in H_0, so (4.7) gives an integer R large enough that the entire spectral tail is below eta. Hence tau>b on that sample. The countable union over n,K,R covers `{b<sigma}`. This proves the local path result.

### `R10-I0070-C006 — AUTHOR-SIDE PROVED / EXTERNAL AUDIT REQUIRED`

Under exactly the p=2 Hilbert specialization of Theorem 5.7's hypotheses (Assumption 4.1 / Theorem 4.7 at p=2, the p=2 critical condition `(2 beta_j-1)(rho_j+1)<=1` with equality allowed, the full growth condition (5.21), `(A,B) in SMR^bullet_{2,0}`, and the source's all-r/all-alpha hypothesis), the maximal solution satisfies a.s.

`u in H^{theta,r}_loc((0,sigma);X_{1-theta})
     cap C^{theta-epsilon}_loc((0,sigma);X_{1-theta})`             (8.7)

for every

`theta in [0,1/2)`, `r in [2,infty)`, `0<epsilon<theta`.          (8.8)

At theta=0 the H-part is just the locally improved time-integrability statement; the Hölder clause is only asserted for epsilon in `(0,theta)` as in the source.

No claim is made at theta=1/2.

The argument does **not** assume the original A is self-adjoint, does **not** assume a compact embedding, does **not** set B=0, does **not** ask for better initial data, and does **not** strengthen critical inequality (6.1) to strict subcriticality. The positive self-adjoint A_0 is the source's Hilbert-couple reference operator from the proof of Theorem 3.13.

This is still not fleet closure: two independent OTHER-track audits, including P26, and a broader prior-art clearance are required by the owner protocol.

---

## 9. Adversarial checks and failures retained

1. **Old short-time endpoint absorption fails.** At exact criticality the usual time-smallness exponent is zero; this is why simply deforming the p>2 proof does not solve the endpoint.
2. **Passing spatial-loss delta down to zero is invalid.** The previous run retained the exact Hilbert-scale example showing membership in every `X_{s-delta}`, delta>0, need not imply membership in `X_s`.
3. **C005's theta-exception sentence was wrong.** Current Definition 3.8 has all theta in `(0,1/2)` for q>2. It is corrected above rather than silently inherited.
4. **A non-Hilbert graph domain would kill the rank-one implementation.** Problem 6 avoids that obstruction because X_0 is Hilbert and X_1=D(A), hence X_1 has an equivalent Hilbert graph norm. This is source structure, not an added assumption.
5. **A high-frequency counterexample must defeat more than compactness.** On a compact H_0 path range the spectral tail is uniformly small. Any genuine counterexample to C006 must therefore attack the random-linear perturbation/identification step or one of its source assumptions, not merely move mass to higher frequencies.

The most important remaining adversarial audit is to check (8.3)--(8.5) line-by-line against Corollary 3.15 and the source strong-solution uniqueness convention.

---

## 10. Independent R11 audit

Newest package actually read:

`runs/R11/2026-09-16T20-40-00Z_i0054-rrt-multicut-e71c.md`.

It proposes a fifth discrete model class for Aldous--Janson Open Problem 18: an exchangeably relabelled random recursive tree with an edge weight depending on descendant fringe size.

I independently audited the exact finite hazard core.

### Audit ID

`R10-AUDIT-R11-I0054-C005-RRT-HAZARD-20260916 — PASS for the finite fringe/hazard generator core only.`

Let `Z_{m,s}` be the number of RRT edges with descendant fringe size s. The report claims

`E Z_{m,s}=m/[s(s+1)]`.                                           (10.1)

The recursion is correct: for s=1 the leaf recurrence gives `m/2`; for s>=2,

`E Z_{n+1,s}=(1-s/n)E Z_{n,s}+((s-1)/n)E Z_{n,s-1}`,

and substitution gives `(n+1)/[s(s+1)]` exactly.

With

`w_m(s)=(s+1)/[2(m-s)]`,                                         (10.2)

and a particular sampled subset A of size i among b labels, exchangeable relabelling gives

`P(S_e cap [b]=A | |S_e|=s)=C(m-b,s-i)/C(m,s)`.                  (10.3)

Therefore the one-orientation visible hazard is

`sum_s [m/(s(s+1))]*[(s+1)/(2(m-s))]
       *C(m-b,s-i)/C(m,s)`

`= (1/2) sum_s C(m-b,s-i) B(s,m-s)`

`= (1/2) B(i,b-i)`,                                               (10.4)

where the last identity follows from the beta integral and the binomial theorem. The opposite orientation gives the other half, so the unordered split hazard is exactly `B(i,b-i)`. Summing over unordered sampled splits yields `H_{b-1}`, the CTCS total block-split rate.

The exact checker verifies the recurrence through n=50, the one-orientation identity for all 4,495 triples `2<=m<=30`, `2<=b<=m`, `1<=i<b`, and the total-rate identity through b=30.

This audit **does not** certify R11's full hidden-state multicut Markov/projective-limit construction, its source-intent claim “superficially different”, or novelty. It certifies only the finite fringe expectation and visible CTCS hazard identity on which that construction is based.

---

## 11. Exact checker / self-check

Checker:

`artifacts/R10/20260916T2138Z_i0070_progressive_representative_checker.py`

creation/readback commit:

`230307eb7b976273106a49cda7655f10a99314aa`.

Executed output:

`artifacts/R10/20260916T2138Z_i0070_progressive_representative_checker.out`

creation/readback commit:

`2b48cc3288619fdfc6b7591d6dff42b213cfe043`.

Output SHA-256:

`8471a0a9ddb95751cecf0e7a8249cd74d68d7206e744b19b53e7cb0da573fa92`.

The output ends `ALL_EXACT_CHECKS_PASS`.

This is a self-check of finite algebra only. It is not an independent audit of C006.

---

## 12. Model/runtime and denied-task status

The scheduler/runtime limitation is unchanged. The exposed task-update interface has fields for title/prompt, schedule, enabled state and timing mode. It has **no model-family selector and no reasoning-effort selector**. Therefore GPT-6/maximum can be requested in task text but cannot be installed or verified by this worker. Changing that would require an authorized product/workspace interface which actually exposes those selectors, or platform support adding/fixing that capability.

The fleet policy records native `You cannot modify this task` failures for P26/P01/P03 in some contexts. The legitimate workaround is to use an authorized task/account/workspace-owner context for the existing task, or platform support to repair its ownership/permissions. Cloning the task or bypassing the permission boundary is not authorized. No scheduler mutation was attempted in this run.

---

## 13. Fixed metric and next action

The fixed metric remains numerically saturated at the source target:

`theta_* = 1/2` as a supremum; endpoint 1/2 not claimed.

This is **no metric movement**, so the unchanged count is now 5. The scope/proof integrity did improve: the complex/real Hilbert trace mismatch is closed source-natively, the X_1-progressive representative is constructed explicitly, and the perturbation smallness is shown to be per-target rather than uniform in q.

The owner policy says a closable track rotates after six unchanged runs. Therefore the next R10 run cannot simply add another endpoint lemma. It has two legitimate outcomes:

1. obtain/locate the required independent audits and, if they genuinely validate the source-matching proof plus prior-art gate, move to closure packaging; or
2. if the metric remains unchanged and closure is not independently verified, write an immutable I0070 handoff and rotate to the next eligible unowned READY/fully-admitted closable outside queue item.

A useful final adversarial audit before rotation is to attack exactly the deterministic-horizon random-linear identification (8.3)--(8.5), especially strong progressive operator measurability and p=2 uniqueness after zero extension. Suggested next methods if one more I0070 run is protocol-legal: **#4 PROVE SOMETHING WEAKER COMPLETELY, #10 DERANDOMIZE, #26 HUNT THE SPORADIC CASE**.

---

## 14. Structured ledger_delta

```yaml
ledger_delta:
  worker: R10
  source: "Agresti--Veraar, arXiv:2501.18561 (historical v2 intake; current v5 / NoDEA 32 (2025)), Problem 6"
  target: "Extend Theorem 5.7 to p=2 with X0 Hilbert in the critical equality case of (6.1), preserving source hypotheses/norms"
  metric: "largest time-regularity exponent theta rigorously established for a fixed source-admissible critical p=2 problem"
  before: "theta_* = 1/2 as supremum; endpoint not claimed"
  after: "theta_* = 1/2 as supremum; endpoint not claimed"
  movement: "none"
  unchanged_count: 5
  status: "PARTIAL / RECOVERY2 / R10-I0070-C006 author-side full-source proof candidate; independent closure audits missing"
  methods: [1, 19, 27]
  exact_evidence:
    - "R10-I0070-C006a deterministic compact-tail endpoint absorption with source Hilbert reference A0"
    - "R10-I0070-C006 full deterministic-horizon proof written in this report"
    - "explicit A0-Yosida construction of an X1-strongly-progressive representative"
    - "artifacts/R10/20260916T2138Z_i0070_progressive_representative_checker.py @ 230307eb7b976273106a49cda7655f10a99314aa"
    - "artifacts/R10/20260916T2138Z_i0070_progressive_representative_checker.out @ 2b48cc3288619fdfc6b7591d6dff42b213cfe043; ALL_EXACT_CHECKS_PASS"
  corrections:
    - "R10-I0070-X001: prior C005 sentence excluding theta=1/q is false; current Definition 3.8 has every theta in (0,1/2)"
  audit_ids:
    - "R10-AUDIT-R11-I0054-C005-RRT-HAZARD-20260916 (PASS finite hazard core only)"
  own_claim_external_audits: []
  remaining_obligations:
    - "P26 full source-exact audit of C006"
    - "second independent OTHER-track audit of C006"
    - "bounded prior-art search must be broadened/independently checked before novelty or closure"
    - "if sixth unchanged run occurs without closure, immutable handoff and rotate per closable-track rule"
```
