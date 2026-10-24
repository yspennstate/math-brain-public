# FOREST account02/B02 r13 — augmented homogenized log-concavity comparison

**Outcome:** `ESSENTIAL_STEP_APPLIED`. The team already has an internal `FULL_PROOF_CANDIDATE`, but this report does **not** promote the parent statement to a public theorem, novelty claim, or priority claim. Context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh control and exact scope

Run: `20260922T041021Z-account02-B02-forest-r13`.

Fresh main at entry was `a936d6403a2075cb1ad721a7fa8eaab8b8b9f360`; a later freshness read reached `0fb11f77f79ccfa96c5474eb67b386307f3406dd`. Comparing those revisions showed only run/status/work additions and no change to the protected control files. Active OWNER CONTROL remains revision `2026-09-22.2`, directive `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, and account02/B02 remains FOREST research. The protected blobs read at invocation are:

- `AGENTS.md`: `94387098453b9f4a9b10179183f6f6ec780fd987`
- `scheduled_tasks/README.md`: `3d4a9372c87802ab734141a3374d04c8823372e3`
- `scheduled_tasks/fleet.json`: `e647d5d2479749f80ce7bb4862bee0f28513c7d9`
- `scheduled_tasks/roles.json`: `ed17ecc94f76720c0345b3e32249b791b20ec611`
- `scheduled_tasks/PROTOCOL.md`: `83a9268bf5287ca203e4be69a79e25382397bca7`
- collective `ORDER.md`: `a70e03208ae00795ca7c6cdf9b7dbce854347138`
- `TARGETS.md`: `a8cafa98cdb074ed15d0e214f8f54ee514c500df`
- `ASSIGNMENTS.json`: `fe144a4be3522d57f8cb2dc40b1fc57df7c7fda`

Whole-file README SHA-256 and isolated OWNER MESSAGE SHA-256 are `NOT_RECOMPUTED_CONNECTOR_BYTE_HASH_PIPELINE_NOT_EXPOSED`; no cached hash is being presented as fresh byte verification.

Exact target: for a finite simple graph `G`, choose uniformly from **all** acyclic edge subsets `F`, including the empty forest, disconnected forests, and every possible forest size. For distinct edges `e,f`, prove

`P(e,f in F) <= P(e in F) P(f in F)`.

No rooted-forest, fixed-size, spanning-tree, or weighted surrogate is substituted for the source law.

## 2. Lead candidate and named OTHER-account result consumed

The latest complete lead version consumed is account01/B01 `FOREST-KN-COCKS-RECONCILED-v3`, handoff commit `0509904b9b699563a2b6fe60b6226948886a6b86`. Its conditional/end-to-end chain is:

`unit FOREST theorem on every K_n`
`-> Cocks fixed-graph weighted upgrade for M(K_n)`
`-> Semple--Welsh Proposition 3.5 minor closure`
`-> every finite simple G is a deletion minor of K_n`
`-> specialize surviving edge weights to 1`.

The lead records two independent existing-worker end-to-end reviews of that same chain. The original Cocks article body was not directly accessible in the lead run, so external/public use still requires ordinary source/expert scrutiny; the fixed-graph statement is source-bound through the final published Semple--Welsh Note.

The assigned named OTHER-account result actually used here is account03/B03 run `20260922T025738Z-account03-B03-forest-r11`, report blob `64b8971de058ea3f9dba14e92ee5899252c1b1c3`, candidate `FOREST-KN-HERMITE-JENSEN-v1`. It independently proves the hardest complete-graph sign by the Hermite logarithmic-derivative identity and Jensen:

`s >= J_n=(n-4)(n+1)/(n^2+n+6)`,

with

`G_n(J_n)=(3n^4+40n^3-59n^2+488n-280)/(n^2+n+6)^2>0`.

Thus the complete-graph module has an analytic route independent of the lead's earlier root-moment estimate. I use that result as a source-compatible independent support for the `K_n` input; the new work below instead attacks the assigned polynomial/log-concavity comparison directly.

## 3. Why complete log-concavity applies to the exact unrooted law

Let `E(G)` have `m` edges and let `M(G)` be the graphic matroid. Its independent sets are exactly the acyclic edge subsets of `G`. Hence the Anari--Liu--Oveis Gharan--Vinzant homogenized independent-set polynomial is, in this graphic case,

`g(y,z)=sum_{F acyclic} y^(m-|F|) prod_{e in F} z_e`.

At `(y,z)=(1,1,...,1)`, every forest monomial has weight exactly one. Therefore the probability distribution encoded there is **precisely the source uniform law on all unrooted forests**, including disconnected forests and every size. No affine conditioning or rooted weighting is needed for this identification.

Source: Anari, Liu, Oveis Gharan, Vinzant, *Log-concave polynomials II: high-dimensional walks and an FPRAS for counting bases of a matroid*, arXiv:1811.01600, theorem on complete log-concavity of the homogenized independent-set polynomial. The same source explicitly distinguishes the resulting spectral negative dependence from entrywise negative correlation: complete log-concavity by itself does not imply all off-diagonal covariance signs.

For the all-graphs transfer in the existing candidate, the source scope is different: Semple--Welsh, *Negative Correlation in Graphs and Matroids*, CPC 17 (2008), defines independence correlation using all positive real element weights, proves minor closure in Proposition 3.5, and its final Section 5 Note records Cocks's fixed-graph theorem that if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated. This is not the older class-level parallel-copy argument.

## 4. New augmented homogeneous covariance inequality

Let

- `X_e = 1[e in F]`,
- `K=|F|`,
- `p_e=E X_e`,
- `mu=E K`,
- `v=Var(K)`,
- `c_e=Cov(X_e,K)`,
- `C_ef=Cov(X_e,X_f)`.

Under the monomial law of `g` at all ones, define the exponent vector

`U=(m-K, X_1,...,X_m)`.

For any homogeneous multiaffine generating polynomial at the all-ones point, direct differentiation gives

`- Hess log g(1) = diag(E U) - Cov(U)`.

Complete log-concavity therefore yields

`A-Sigma >= 0`,

where `A=diag(E U)` and `Sigma=Cov(U)`. Of course `Sigma>=0` as a covariance matrix. Consequently

`N=A^(-1/2) Sigma A^(-1/2)`

satisfies `0<=N<=I`, hence `N^2<=N`.

For an edge `e`, the relevant normalized entries are

`N_ee=1-p_e`,

`N_e0=-c_e/sqrt(p_e(m-mu))`,

`N_ef=C_ef/sqrt(p_e p_f)`.

Taking the `e` diagonal entry of `N^2<=N` gives the exact **augmented edge-row budget**

**(A)**

`c_e^2/((m-mu)p_e(1-p_e)) + sum_{f!=e} (1-p_f) rho_ef^2 <= p_e`,

where `rho_ef=C_ef/sqrt(p_e(1-p_e)p_f(1-p_f))`.

Equivalently,

`c_e^2/(m-mu) + sum_{f!=e} C_ef^2/p_f <= p_e^2(1-p_e)`.

This strictly strengthens B02's earlier dehomogenized row budget

`sum_{f!=e}(1-p_f)rho_ef^2 <= p_e`

by retaining a nonnegative **size-susceptibility payment**. This is the run's principal before/after advance.

## 5. New slack/global susceptibility budget

Taking the homogenizing/slack coordinate diagonal of `N^2<=N` gives

**(B)**

`v^2/(m-mu) + sum_e c_e^2/p_e <= v`.

Because `sum_e c_e=Cov(K,K)=v`, Cauchy--Schwarz gives

`sum_e c_e^2/p_e >= v^2/mu`.

Combining with (B) recovers directly

`v <= mu(m-mu)/m`.

Thus the homogeneous spectral inequality simultaneously controls edge-edge correlations and edge-size susceptibilities, and it recovers the ultra-log-concave variance bound without invoking a separate size-mixture argument.

## 6. A new 3-by-3 comparison for one edge pair

Write

`r=m-mu-v >= 0`

and

`d_ef=p_e p_f - P(e,f in F) = -C_ef`.

The `(slack,e,f)` principal block of `-Hess log g(1)` is

`[[r, c_e, c_f], [c_e, p_e^2, d_ef], [c_f, d_ef, p_f^2]]`.

Its determinant is nonnegative, giving the source-valid polynomial comparison

**(C)**

`r p_e^2 p_f^2 + 2 c_e c_f d_ef - r d_ef^2 - p_f^2 c_e^2 - p_e^2 c_f^2 >= 0`.

When `r>0`, the equivalent Schur-complement form is

`|d_ef - c_e c_f/r| <= sqrt((p_e^2-c_e^2/r)(p_f^2-c_f^2/r))`.

This is a genuine comparison for the desired Rayleigh gap `d_ef`, but it is an interval bound, not a sign theorem. In particular, complete log-concavity remains spectral rather than entrywise Rayleigh. If additionally `c_e,c_f>=0`, the explicit sufficient condition

`(c_e/p_e)^2 + (c_f/p_f)^2 >= r`

forces the lower endpoint of that interval to be nonnegative and hence proves the desired pair inequality. No claim is made that this sufficient condition always holds.

Therefore the first essential missing implication for a **log-concavity-only** proof is now sharply isolated: one must force the Schur interval in (C) to lie in `d_ef>=0`, or supply an additional graphic/forest structure theorem doing so. Merely citing complete log-concavity is not enough.

## 7. Sharpened obstruction to a hypothetical minimal counterexample

The same augmented row budget strengthens B02's previous normalized-correlation obstruction.

Suppose a hypothetical bad pair `(e,f)` has `rho_ef=c>0`, and suppose the usual minimal-counterexample deletion/contraction endpoint has been paid so that for every third edge `g` both `g`-conditioned `e,f` covariances are nonpositive. The exact binary total-covariance identity then yields

`rho_eg rho_fg >= c`.

Define

`T_i = c_i^2/((m-mu)p_i(1-p_i)) >= 0`.

Adding (A) for `e` and `f`, then using `rho_eg^2+rho_fg^2 >= 2 rho_eg rho_fg`, gives

**(D)**

`(2-p_e-p_f)c^2 + 2c sum_{g notin {e,f}} (1-p_g) + T_e+T_f <= p_e+p_f`.

Under the source unit law, downward closure gives `p_i<=1/2` by the injection `F -> F-{i}` from forests containing `i` into forests omitting it. Therefore any such bad pair must satisfy

**(E)**

`c^2 + (m-2)c + T_e+T_f <= 1`.

This strictly sharpens the earlier B02 obstruction `c^2+(m-2)c<=1`: a bad pair with appreciable correlation to forest size is even more constrained. The conditional-minor hypothesis is essential for this application and is not silently dropped.

## 8. Exact regression

A standard-library exact `Fraction` checker enumerated every labelled simple graph on 2--5 vertices and every forest exactly. It tested the new inequalities on:

- 1,098 labelled graphs,
- 5,325 edge-row instances,
- 11,766 present edge pairs.

Results:

- augmented edge-row budget failures: 0,
- slack/global budget failures: 0,
- 3-by-3 principal-minor failures: 0,
- ULC variance failures: 0,
- source target positive covariances in this finite range: 0.

The exact checker is Git blob `e7bce77621c3667b3437219a6009ad2818542976`, native SHA-256 `1e390e30f194b8eabead337007526b26c0e845839bc83386c63801fe5ba36dd9`. Exact output is Git blob `0ae3b91b5ca40efb077064942185ae49eaddc24d`, native SHA-256 `5641d12bc8cccf4cdf87d361ce9f9378d8ce56e3488f02056ef1f19b6bac558e`, ending `STATUS=ALL_EXACT_CHECKS_PASS`.

This finite computation is regression evidence only. The all-graph validity of (A)--(C) is the analytic consequence of complete log-concavity above; the finite search is not used to extrapolate the target theorem.

## 9. Status and next implication

**Target-level status:** the campaign retains the lead's internal full candidate with two independent end-to-end reviews. This run neither refutes it nor elevates it to a public solution.

**Mechanism-level movement:** `ESSENTIAL_STEP_APPLIED`. B02 has upgraded its source-valid log-concavity input from a dehomogenized edge-only spectral budget to the full homogenized edge+size matrix, obtaining (A), (B), (C), and the sharpened minimal-counterexample constraint (D)--(E).

**Compact conditional end-to-end argument:** the named partner supplies a clean all-`n` complete-graph sign; if the final published Semple--Welsh attribution of Cocks's fixed-graph theorem is accepted exactly as stated, weighted minor closure transfers the `K_n` result to every finite simple graph, and unit specialization is exactly the source uniform unrooted-forest law. Independently, ALOV complete log-concavity applies directly to that same source law and supplies the new spectral inequalities above.

**First missing implication for the assigned polynomial route:** force `d_ef>=0` from the augmented homogeneous PSD system plus graphic structure. Equation (C) is the sharpest local source-valid comparison produced here; complete log-concavity alone cannot supply the missing entrywise sign.

## 10. Operations, provenance, and runtime truth

The own-account managed inventory was inspected only for account02: all twenty managed B01--B20 registrations were enabled, unique/hourly-valid and role-aligned; B20 was enabled; exposed email/notification flags remained off. B02 made zero scheduler mutations and observed no deficit requiring B20 repair.

Actual-hour login and unique run start were created before substantive work. No brain installation, benchmark work, email, Drive, public posting, paid model/API/Codex execution, remote workflow, permission change, credential handling, machine-path disclosure, raw private transcript, or benchmark-gold access occurred.

Model self-report: `GPT-5.6 Sol`. Requested effort: `maximum actually supported`. Configured/known effort: `UNKNOWN_NOT_EXPOSED`. Provider reasoning/token/time counters: `null / NOT_EXPOSED`. Brain context: `WITHOUT_VERIFIED_BRAIN`.
