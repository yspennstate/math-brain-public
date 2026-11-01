Model: GPT-5.6 Sol. Reasoning: UNVERIFIED. **MOVEMENT (PARTIAL):** on a restricted but source-valid bounded-degree subcritical class, the sufficient echo-amplification coefficient improves from the source's `A_echo = Delta_max` to the uniform adjacency spectral bound `A_echo = Lambda_* := sup_n ||A(G_n)||_{2->2}`; methods actually tried: **#2, #4, #8**.

# NM13-11 first run — H0003 front-Markov strong-coupling attack

Date: 2026-09-17 UTC  
Track: NM13-11 / HARD OUTSIDE  
Repository: `yspennstate/math-open-problems`, `master`  
Claim: `operations/claims/H0003.md`, creation commit `9da49e832192bc0ce72f545b40589aa9dd91acb8`, read back at that commit, blob `6842b4d7c0367422b8b2be1c9cd61e150b6491fe`.

## 1. Runtime honesty and repository continuity

The scheduler interface exposed to this run does not authenticate a model selector or a reasoning-effort selector. The actual model identity available to this report is GPT-5.6 Sol; the reasoning setting is **UNVERIFIED**. The prompt request for GPT-6/maximum is therefore not reported as an installed runtime fact.

I recovered the controlling `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, the NM13 deployment receipt, root `POSTED.md`, root `RESULTS.md`, the H-intake source/verification material, current claims, and repository searches for H0003 and its aliases. Large fleet surfaces were read in scoped form rather than represented as byte-for-byte rereads. No previous `proofnet24/NM13-11/` report and no NM13-10/NM13-12 report were recovered at run start, so this is the first own report.

The source is not in `POSTED.md`, and repository search found no prior live H0003 owner. Immediately before the claim write, `operations/claims/H0003.md` returned 404. Searches for `H0003`, `arxiv_2608_15987`, and `Front-Markov property` recovered the H intake/verification plus screening reports that call H0003 HARD, but no competing claim. This is why the create-only claim was lawful.

## 2. Source and current-status check

Source: Achyut Kumar, *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1, submitted 17 August 2026.

Direct source read: <https://arxiv.org/html/2608.15987>.

Exact target is Conjecture 11.8, Section 11.5. In the paper's notation, in the full saturated regime and without the dissipative condition

\[
\kappa=\frac{\gamma_{\max}L_\sigma\Delta_{\max}}{\alpha_{\min}}<1,
\]

prove a uniform total-variation reduction

\[
d_{\rm TV}\!\left(\mathcal L(S_n),\mathcal L({\rm GW}(M))\right)
 \le C\bigl(\varepsilon(\delta)+\eta_n\bigr),
\]

including strong coupling `kappa >= 1`, uniformly through the critical window. The source itself states that this remains open. Its unconditional Theorem 11.5 proves a subcritical version when `kappa<1` and a critical version only along a joint limit `n epsilon(delta_n) -> 0`.

Fresh bounded literature screen on 2026-09-17 used the exact arXiv id/title, `front-Markov`, and later author work. It recovered the companion Kumar–Duddala preprint arXiv:2608.21125 (21 August 2026), which treats front propagation/Bramson correction and the sensitive continuous-type regime, not Conjecture 11.8. No source-matching later resolution was recovered. This is a bounded negative search, not a claim of global novelty or bibliographic completeness.

The H intake row had no canonical `dedup_key`. I therefore recovered the source identity rather than hashing the alias `H0003`: `arxiv_2608_15987::conjecture_11.8`. Its SHA-256 is `2f736678ffd1e4a5b22f0cd7b44583c00b0e5a08c713047cabcb7cb732af1b74`, whose integer residue modulo 13 is **10**, matching this worker's shard. No prior `H0003-A*` attempt record was recovered; intake screening is the only prior H0003-specific history found.

## 3. Frozen metric

Metric: `A_echo`, the graph-amplification coefficient in a *proved* sufficient linear echo-stability condition

\[
\gamma_{\max}L_\sigma A_{\rm echo}<\alpha_{\min}
\]

that is actually carried through to a source-relevant front-decoupling statement.

- **Before:** `A_echo = Delta_max`, the coefficient used by the source's Theorem 11.5.
- **After this run (restricted class):** `A_echo = Lambda_* := sup_n ||A(G_n)||_{2->2}` under the additional hypothesis `Lambda_* < infinity` and with a strictly positive spectral gap `g_2=alpha_min-gamma_max L_sigma Lambda_*`. When `Lambda_* < Delta_max`, this is a strict sufficient-condition improvement and can include parameters that the source calls strong coupling (`kappa >= 1`).
- **Full-source status:** still OPEN. The improvement is **PARTIAL**, subcritical, bounded-degree, and assumes the uniform adjacency spectral bound. It does not give the source's full critical-window statement, nor does it remove every strong-coupling case.

No metric is reset or renamed. The comparison is in the same source parameters `alpha_min`, `gamma_max`, `L_sigma`, and graph sequence.

---

# 4. Method #2 — attack the negation first

I tried to make the full front-Markov conjecture fail by exploiting the source's own echo mechanism.

### 4.1 Minimal sibling echo does not refute the conjecture

For a failed parent `u` with two children `v,w`, if `v` fails first then `v -> u` changes the parent trajectory, and hence can alter the forcing from `u` to `w`. At finite saturation margin this creates sibling dependence. The source itself quantifies a single such effect as `O(epsilon(delta))` (Proposition 11.2), so this does **not** refute Conjecture 11.8: the conjectured right-hand side explicitly permits `C epsilon(delta)`.

This also means that statements in the source saying the Bethe reduction is "exact" should not be used here as a finite-margin zero-error premise without reconciling them with Proposition 11.2 and Section 11.3. I do **not** claim an internal contradiction: the intended reading may be the ideal saturated limit. For the present attack the safe fact is only that the finite-margin echo is small per cell, not exactly zero.

### 4.2 Resonant linear mode: a real obstruction, but not a stochastic counterexample

Let `A` be the adjacency matrix of a finite graph and linearise the true-minus-directed difference around a trajectory on which all active coupling derivatives are near the global Lipschitz bound. Ignoring the small source term, the worst comparison equation is

\[
\dot D=(-\alpha_{\min} I+\gamma_{\max}L_\sigma A)D.
\]

If `lambda_max(A)` is the Perron eigenvalue of `A`, the top mode has exponent

\[
-\alpha_{\min}+\gamma_{\max}L_\sigma\lambda_{\max}(A).
\]

Thus when

\[
\gamma_{\max}L_\sigma\lambda_{\max}(A)\ge\alpha_{\min},
\]

a proof based *only* on global Lipschitz contraction of the echo cannot contract every perturbation. This is an exact obstruction to that proof architecture.

It is **not** a counterexample to Conjecture 11.8. The actual source is localized to the failed front, the nonlinear logistic derivative is usually much smaller than `L_sigma` in the saturated basin, and the resonant Perron mode need not be excited at order one. So method #2 did not refute the source. It did identify the natural spectral boundary of the next route.

Outcome of method #2: **source refutation failed; proof-route obstruction proved.**

---

# 5. Method #4 — prove something weaker, completely

The source's weighted-sup argument inserts `Delta_max` because

\[
\sum_{u\sim v}|D_u|\le \Delta_{\max}\|D\|_\infty.
\]

The new idea is to use the Euclidean logarithmic norm of the time-dependent interaction Jacobian. This replaces the row-sum bound by the adjacency spectral norm.

## Theorem NM13-11-H0003-SPECTRAL-ECHO-01

Let `(G_n)` be finite connected undirected graphs with `deg <= Delta` and Benjamini–Schramm limit the source tree `UGW(g)`. Let `A_n` be the adjacency matrix and suppose

\[
\Lambda_*:=\sup_n\|A_n\|_{2\to2}<\infty,
\qquad
g_2:=\alpha_{\min}-\gamma_{\max}L_\sigma\Lambda_*>0.
\tag{1}
\]

Assume the saturated regime of Definition 2.3, with error `epsilon=epsilon(delta)`, and assume the ideal finite-type branching matrix `M` is strictly subcritical, `rho(M)<1`. Then, in the iterated limit `n -> infinity` followed by `delta -> infinity`, the failed-cluster law converges in total variation to the multitype Galton–Watson law of the source.

More quantitatively, for every integer cutoff `K>=1`, define `eta_{n,K}` to be the probability that the rooted portion of `G_n` exposed before `K` failed vertices have been discovered contains a cycle. For fixed `K`, `eta_{n,K}->0` by Benjamini–Schramm convergence to a tree. There are constants `C_1,C_2,c_0,C_0>0`, independent of `n,K,delta`, such that

\[
\delta_{n,K}:=d_{\rm TV}\!\left(
 \mathcal L(S_n^{\le K}),\mathcal L(S_{\rm GW}^{\le K})
\right)
\le
\eta_{n,K}
+C_1\varepsilon K
+ C_2\frac{\varepsilon}{g_2}K^{3/2},
\tag{2}
\]

and

\[
d_{\rm TV}\!\left(\mathcal L(S_n),\mathcal L(S_{\rm GW})\right)
\le 2\delta_{n,K}+2C_0e^{-c_0K}.
\tag{3}
\]

Consequently, choosing `K` of order `log(1/epsilon)` after taking `n -> infinity` gives

\[
\limsup_{n\to\infty}d_{\rm TV}
=O\!\left(
\varepsilon(\delta)\,[\log(1/\varepsilon(\delta))]^{3/2}/g_2
\right)+o_{\delta\to\infty}(1),
\tag{4}
\]

so the total-variation distance tends to zero.

This is a source-matching **partial theorem**. In any source-valid graph sequence with `Lambda_*<Delta`, condition (1) is strictly weaker than the source's global row-sum condition

\[
\alpha_{\min}>\gamma_{\max}L_\sigma\Delta.
\]

In particular the interval

\[
\gamma_{\max}L_\sigma\Lambda_*<\alpha_{\min}
\le \gamma_{\max}L_\sigma\Delta
\tag{5}
\]

is classified as `kappa>=1` by the source but is covered by the theorem whenever it is nonempty.

### Proof

We use only source ingredients that precede the `kappa<1` contraction: synchronous coupling, saturation, and first-passage stability.

#### Step 1: exact Euclidean stability estimate for the nonlinear difference

Couple the true SDE and the source's directed comparison system with the same Brownian motions. Put

\[
D_v(t)=s_v(t)-\widetilde s_v(t).
\]

By the mean-value theorem, the interaction part of the difference can be written with time-dependent edge coefficients `b_{vu}(t)` satisfying

\[
0\le b_{vu}(t)\le \gamma_{\max}L_\sigma A_n(v,u).
\]

The diagonal drift is at most `-alpha_min`. The remaining mismatch is a source vector `g(t)`. Saturation is the only input needed for the source's estimate: before the stopped cluster has reached `K` failed vertices, each component of `g` is `O(gamma_max epsilon)`, and it is supported within graph distance one of the failed set. Hence, for a constant `C_s` depending only on the fixed compact parameter bounds,

\[
\|g(t)\|_2
\le C_s\gamma_{\max}\varepsilon\sqrt{(\Delta+1)K}.
\tag{6}
\]

For the homogeneous part, let `B(t)` be the time-dependent Jacobian. Although the type-dependent matrix need not be symmetric, its symmetric part obeys, as quadratic forms,

\[
\frac{B(t)+B(t)^\top}{2}
\preceq -\alpha_{\min}I+\gamma_{\max}L_\sigma A_n.
\]

Indeed every off-diagonal entry of the symmetric part is bounded above by `gamma_max L_sigma` on an edge, and the adjacency matrix is nonnegative and symmetric. Therefore the Euclidean logarithmic norm is bounded by

\[
\mu_2(B(t))
\le -\alpha_{\min}+\gamma_{\max}L_\sigma\|A_n\|_{2\to2}
\le -g_2.
\tag{7}
\]

The Dini derivative of `z(t)=||D(t)||_2` consequently satisfies

\[
D^+z(t)\le -g_2z(t)+\|g(t)\|_2.
\]

The synchronous coupling starts from the same initial state, so `z(0)=0`. Variation of constants and (6) give, up to the stopping time at `K` failed vertices,

\[
\sup_t\|D(t)\|_2
\le \frac{C_s\gamma_{\max}}{g_2}\,
\varepsilon\sqrt{(\Delta+1)K}.
\tag{8}
\]

In particular (8) is a uniform pointwise bound for every child state because `|D_v|<=||D||_2`.

#### Step 2: convert state error to per-edge transmission error

The source's Lemma 11.3 proves first-passage stability: a uniform state/drift perturbation `eta` changes the two-barrier OU hitting probability by at most `C_stab eta`. Proposition 11.2 additionally supplies the direct cellwise saturation error `O(epsilon)`.

Thus, on the event that the explored neighborhood is a tree, the conditional transmission probability at each tested edge differs from the ideal directed probability by at most

\[
C_{\rm cell}\varepsilon
+C_{\rm stab}\frac{C_s\gamma_{\max}}{g_2}
\varepsilon\sqrt{(\Delta+1)K}.
\tag{9}
\]

A breadth-first exploration that stops at `K` failed vertices tests at most `Delta K` outward edges. Couple the Bernoulli decision at each exploration step maximally and telescope the conditional mismatch probabilities. If a cycle appears, charge that whole event to `eta_{n,K}`. Therefore

\[
\delta_{n,K}
\le \eta_{n,K}
+\Delta K C_{\rm cell}\varepsilon
+\Delta K C_{\rm stab}\frac{C_s\gamma_{\max}}{g_2}
\varepsilon\sqrt{(\Delta+1)K},
\]

which is exactly (2) after absorbing fixed factors into `C_1,C_2`.

#### Step 3: the ideal subcritical total progeny has an exponential tail

Because the graph degrees are bounded by `Delta`, the ideal finite-type GW offspring vectors have bounded support. Let `F=(F_i)` be their multivariate offspring generating polynomial and let

\[
H_i(s)=\mathbb E_i[s^{|S_{\rm GW}|}].
\]

The total-progeny pgf satisfies near `s=1`

\[
H(s)=sF(H(s)).
\tag{10}
\]

At `(s,H)=(1,1)`, the Jacobian of the map `H-sF(H)` with respect to `H` is `I-M`. Since `rho(M)<1`, `I-M` is invertible. The analytic implicit-function theorem applied to the polynomial map in (10) gives a solution with finite coordinates for all `s>1` sufficiently close to `1`. Hence for some `s_0>1` and finite `C_0`,

\[
\mathbb P(|S_{\rm GW}|\ge K)
\le C_0s_0^{-K}=C_0e^{-c_0K}.
\tag{11}
\]

No external tail theorem is needed.

#### Step 4: remove the cutoff without assuming a true-cluster tail

This is the point at which a circular argument is easy to make, so we spell it out. Couple the two stopped explorations so their mismatch probability is at most `delta_{n,K}`. If the stopped explorations match and the ideal GW tree terminates before size `K`, then the true exploration has seen the same failed/nonfailed edge decisions and also terminates before `K`. Therefore

\[
\mathbb P(|S_n|\ge K)
\le \mathbb P(|S_{\rm GW}|\ge K)+\delta_{n,K}.
\tag{12}
\]

A mismatch of the full cluster laws can occur only if the stopped coupling fails or at least one cluster reaches `K`. Combining (11)-(12),

\[
\begin{aligned}
d_{\rm TV}(\mathcal L(S_n),\mathcal L(S_{\rm GW}))
&\le \delta_{n,K}
 +\mathbb P(|S_n|\ge K)
 +\mathbb P(|S_{\rm GW}|\ge K)\\
&\le 2\delta_{n,K}+2C_0e^{-c_0K},
\end{aligned}
\]

which is (3).

For each fixed saturation error `epsilon>0`, take `K=K(epsilon)` finite and then let `n->infinity`; Benjamini–Schramm convergence to a tree gives `eta_{n,K}->0`. Then send `epsilon->0`, choosing `K` proportional to `log(1/epsilon)`. Equation (2) gives the polylogarithmic factor in (4), while (11) makes the tail vanish as a positive power of `epsilon`. This proves the theorem. ∎

### Scope audit of the theorem

- It is not a full proof of Conjecture 11.8.
- It is unconditional only after adding the explicit uniform adjacency-spectral condition (1), bounded degrees, and strict subcriticality `rho(M)<1`.
- It genuinely goes past the source's particular `kappa<1` *row-sum* criterion whenever `Lambda_*<Delta` and parameters lie in (5).
- It does not yet treat critical total progeny, where the exponential tail in Step 3 disappears.
- It does not treat unbounded degrees.
- Non-vacuous concrete UGW graph sequences with a rigorously certified uniform gap `Lambda_*<Delta` should be exhibited before presenting this as a broad practical enlargement of the phase diagram. The theorem itself is conditional on the explicit spectral bound and does not pretend that every UGW approximation has such a gap.

Outcome of method #4: **proved a theorem-sized source-relevant restricted extension; metric moved on that class.**

---

# 6. Method #8 — discretize

The proof above turns the analytic echo question into a finite-dimensional graph certificate.

For each finite `G_n`, the required geometric input is no longer the crude integer `Delta` but the largest eigenvalue of its finite adjacency matrix:

\[
\lambda_{\max}(A_n)<\frac{\alpha_{\min}}{\gamma_{\max}L_\sigma}.
\tag{13}
\]

This is an exact finite statement. For a concrete rational threshold `L`, the inequality `lambda_max(A_n)<L` can be certified without floating point, for example by an exact Sturm/sign-count for the characteristic polynomial, by an exact symmetric `LDL^T` positivity certificate for `LI-A_n` when `L` is rational and safely above the eigenvalue, or by a rigorously enclosed algebraic eigenvalue. A uniform theorem for a graph family still needs a family-level bound; checking a few finite graphs does not establish (1).

This discretization exposed the correct next finite target: find a source-valid sequence `G_n ->^BS UGW(g)` with an exact uniform spectral bound `Lambda<Delta`, and then choose parameters in the nonempty interval (5). Such a certificate would demonstrate an explicit `kappa>=1` instance covered by the new theorem. I did not manufacture that family in this run.

Outcome of method #8: **the strong-coupling subproblem is reduced, on the new route, to a finite adjacency spectral certificate plus a family-level uniform bound. No checker was created because no concrete graph family was yet justified.**

---

# 7. What moved, what did not

The source's row-sum proof uses the sufficient echo coefficient `Delta_max`. The theorem above replaces it by `Lambda_*` on a restricted graph class and propagates that replacement all the way through stopped exploration, total variation, and cutoff removal. Thus the frozen metric moves

\[
\boxed{A_{\rm echo}:\ \Delta_{\max}\ \longrightarrow\ \Lambda_*}
\]

**on the explicitly stated spectral subclass**. This is a strict improvement only when `Lambda_*<Delta_max`; that condition is not silently assumed for the entire source class.

The full source metric is not declared solved. In particular no result here supplies the conjectured `C(epsilon+eta_n)` rate uniformly through criticality, and no claim is made for all `kappa>=1`.

Unchanged-run count for the admitted target: **0** (first substantive run, and the metric moved on a restricted source-valid class).

Recovery count: **0**.

## Exact remaining obligations

1. Exhibit and rigorously certify at least one nontrivial source-valid `G_n ->^BS UGW(g)` family with `Lambda_*<Delta` and parameters satisfying (5), so the strong-coupling extension is visibly non-vacuous rather than only conditional on a spectral hypothesis.
2. Try to replace the Euclidean global mode by a front-supported norm so the relevant operator is the active-front adjacency/nonbacktracking operator rather than the full `A_n`; this is the plausible route to substantially more of `kappa>=1`.
3. At criticality, replace the subcritical exponential-progeny truncation by a front-width estimate. The source predicts `sqrt(n)` rather than bulk `n`; the current proof does not reach it.
4. Determine whether the spectral boundary `gamma L lambda_max = alpha` can produce a genuine stochastic counterexample or is only a limitation of global-Lipschitz comparison.
5. Obtain P26 plus a distinct NM13-12 end-to-end audit only if this restricted theorem is promoted as a package. No outside audit exists yet.

## Next methods

Do not repeat `2,4,8` immediately. If this target remains active next run, a genuinely different triple is appropriate: **#12 find what is conserved, #13 find what only increases, #21 ask who else has this shape**, aimed at a front-energy/Lyapunov norm localized to the active boundary rather than the entire graph.

---

# 8. Directed audit status

No independent audit is claimed. NM13-12 has no recovered report yet and P26 has not audited this theorem. Self-review only: I checked the two most likely circular points explicitly — (i) the nonlinear Euclidean norm estimate uses the symmetric part of the time-dependent Jacobian rather than assuming the type-dependent Jacobian is symmetric; (ii) cutoff removal bounds the *true* cluster tail from the stopped coupling and the ideal GW tail, rather than assuming the desired reduction in order to get the true tail.

No finite checker artifact was warranted because the new claim is theorem-sized and contains no concrete finite eigenvalue computation. Per fleet rules, the proof is on the page.

---

```yaml
ledger_delta:
  track: NM13-11
  source_id: H0003
  canonical_dedup_key: arxiv_2608_15987::conjecture_11.8
  claim_path: operations/claims/H0003.md
  claim_creation_commit: 9da49e832192bc0ce72f545b40589aa9dd91acb8
  category: HARD_OUTSIDE
  exact_source_status: OPEN
  mathematical_status: PARTIAL
  metric:
    name: A_echo
    before: Delta_max
    after: Lambda_star_on_uniform_spectral_subclass
    meaning: sufficient graph-amplification coefficient in gamma_max*L_sigma*A_echo < alpha_min carried through to front decoupling
  movement: true
  theorem_claim: NM13-11-H0003-SPECTRAL-ECHO-01
  methods_tried: [2, 4, 8]
  unchanged_runs: 0
  stuck_recoveries: 0
  audits:
    p26: MISSING
    second_other_track: MISSING
  closure: false
  next_obligation: certify a concrete source-valid UGW approximation with Lambda_star < Delta and attack critical front-width uniformity
  shared_root_edit_requested: false
```

**End of complete run report.**
