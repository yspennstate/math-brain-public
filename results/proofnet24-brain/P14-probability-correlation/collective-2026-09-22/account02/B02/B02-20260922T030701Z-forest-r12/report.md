# FOREST B02 — spectral row budget for the actual unrooted forest law

Run: `B02-20260922T030701Z-forest-r12`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Parent status: **internal FULL_PROOF_CANDIDATE already exists; this report is an independent structural module, not a public solved-problem/novelty claim**  
Context: `WITHOUT_VERIFIED_BRAIN`

## 1. Control and scope


The canonical actual-hour login path write was attempted and denied by the platform safety layer, so no login success is claimed. The unique run start was written successfully before substantive work.

## 2. Exact peer artifacts consumed

Lead: `account01/B01`, `FOREST-KN-HERMITE-REDUCTION-v1`, shared handoff blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`. Its chain is: exact labelled EGF/Hermite proof for unit `K_n` -> Cocks fixed-graph upgrade -> Semple-Welsh minor closure -> every finite simple graph by edge deletion.

Named partner: `account03/B03`, `FOREST-KN-HERMITE-JENSEN-v1`, shared handoff blob `d0008c96cc9d1c37e67c931d5d34d14fda798ec8`. I applied its shorter lower bound

`J_n=(n-4)(n+1)/(n^2+n+6)`

for the Hermite logarithmic derivative, yielding

`G_n(J_n)=(3n^4+40n^3-59n^2+488n-280)/(n^2+n+6)^2 > 0`

for `n>=6`, plus exact small cases. This independently supports the lead's hardest complete-graph sign without changing the source transfer step.

## 3. Source-valid log-concavity for the exact target law

For a finite simple graph `G=(V,E)`, define

`P_G(z)=sum_{F acyclic} prod_{e in F} z_e`.

This is exactly the independent-set generating polynomial of the graphic matroid. Its monomials are all unrooted forests: disconnected forests are present, every forest size is present, and no rooting factor is introduced.

Anari--Liu--Oveis Gharan--Vinzant, *Log-Concave Polynomials III*, Theorem 4.1 proves complete log-concavity of the homogenized independent-set polynomial of every matroid. Their affine-specialization closure permits setting the homogenizing variable to `1`, so `P_G` itself is log-concave on the positive orthant. Evaluating at `z=1` is therefore exactly the source unit forest law.

Write `X_e=1_{e in F}`, `p_e=E X_e`, `v_e=p_e(1-p_e)`, and let `C=(rho_ef)` be the Pearson correlation matrix (`C_ee=1`). Multiaffinity gives at `z=1`

`partial_ee log P_G = -p_e^2`,

`partial_ef log P_G = Cov(X_e,X_f)` for `e != f`.

Since `-nabla^2 log P_G` is positive semidefinite, after congruence by `diag(v_e^{-1/2})` we obtain

`D-C >= 0`, where `D=diag(1/(1-p_e))`.

As every correlation matrix satisfies `C>=0`,

`0 <= C <= D`.

The unit forest law is downward closed. Deletion of a present edge injects forests containing `e` into forests omitting `e`, so `p_e<=1/2`; hence `D<=2I`. This rederives `0<=C<=2I` for the exact unrooted source measure. It is a spectral statement only; the ALOV paper itself warns that complete log-concavity does not imply entrywise negative correlation.

## 4. New exact row-budget inequality

The stronger consequence is obtained before replacing `D` by `2I`. Put

`N=D^{-1/2} C D^{-1/2}`.

Then `0<=N<=I`, so `N^2<=N`. Its entries are

`N_ee=1-p_e`,

`N_ef=rho_ef sqrt((1-p_e)(1-p_f))` for `e!=f`.

Taking the `e,e` entry of `N^2<=N` gives

`(1-p_e)^2 + (1-p_e) sum_{f!=e} (1-p_f) rho_ef^2 <= 1-p_e`.

Therefore, for every finite simple graph and every edge `e` under the exact unit all-forest law,

**ROW BUDGET**

`sum_{f!=e} (1-p_f) rho_ef^2 <= p_e`.      (RB)

Since every `p_f<=1/2`, this also gives

`sum_{f!=e} rho_ef^2 <= 2 p_e <= 1`.

This is an unconditional source-valid comparison. It does not assume the desired signs and does not replace them with a spectral surrogate.

## 5. Application to a hypothetical minimal counterexample

Assume, only for this paragraph, that `G` is a smallest simple-graph counterexample by edge count and that `rho_ef=c>0` for a bad pair `e,f`.

For every third edge `g`, conditioning on `X_g=0` is the uniform forest law of `G\g`, so minimality gives nonpositive conditional `e,f` covariance. Conditioning on `X_g=1` is the unit independent-set law of the graphic contraction `M(G)/g`. The contraction may create parallel classes. Simplify it to a smaller simple graph `H`; minimality gives unit pNC on `H`, Cocks's fixed-graph theorem upgrades `M(H)` to independence correlation for all positive weights, and Semple--Welsh Proposition 3.7 preserves independence correlation under parallel extension. Loops, if present, never enter independent sets and are harmless. Thus the `X_g=1` conditional covariance is also nonpositive.

The exact Bernoulli total-covariance identity is

`Cov(e,f)=E[Cov(e,f|X_g)] + Cov(e,g)Cov(f,g)/Var(X_g)`.

Hence for every third edge `g`, if `a_g=rho_eg` and `b_g=rho_fg`,

`a_g b_g >= c > 0`,

so `a_g^2+b_g^2 >= 2c`.

Adding the two row budgets (RB), while retaining the mutual `e,f` term, yields the new necessary condition

`(2-p_e-p_f)c^2 + 2 c S <= p_e+p_f`,

where

`S=sum_{g notin {e,f}} (1-p_g)`.      (MC)

At unit weights, `p_i<=1/2`. If `m=|E(G)|`, then `S>=(m-2)/2`, so every hypothetical minimal violation must satisfy

`c^2 + (m-2)c <= 1`,

and therefore

`c <= (sqrt((m-2)^2+4)-(m-2))/2`

`  = 2/(sqrt((m-2)^2+4)+(m-2))`.      (SEVERITY)

Thus a minimal counterexample, if one exists, has normalized positive correlation `O(1/m)`. For `m>=5`, this is already stricter than the earlier single-conditioning `1/3` cap. This is not a proof of the target by itself; it is a quantitative obstruction that any counterexample must survive.

The source transfer used in the conditioning step is the final Semple--Welsh paper's Section 5 Note (Cocks: unit Conjecture 1.1 for a fixed graph `G` implies `M(G)` is independence correlated), together with Semple--Welsh Proposition 3.5 (minor closure) and Proposition 3.7 (parallel-extension closure). Their definition of independence correlation quantifies over all positive weights, which is exactly what makes the contraction/parallel-class step valid.

## 6. Exact finite regression

A standard-library exact-arithmetic checker enumerated all `1,098` labelled simple graphs on `2..5` vertices, all `5,325` edge rows, and `46,563` ordered total-covariance triple checks. It found:

- `P_HALF_FAILURES=0`;
- `ROW_BUDGET_FAILURES=0`;
- `TOTAL_COVARIANCE_IDENTITY_FAILURES=0`;
- maximum observed exact row-budget ratio `47506/327701`;
- `ALL_EXACT_CHECKS_PASS`.

The checker is regression evidence only; (RB) and (MC) are proved algebraically above. Exact checker SHA-256 `801c455d52254148a669721a8c576c25ae12485d69bb51832aa06ebb2e4ad598`; exact output SHA-256 `8ce472f3b34cfa75b7445773c9f7a878b2fbeae8028e71d6050fcc0c00714df0`. Repository readback blobs are checker `0248b041322ff3a80cc6b13bf5284c63bc141e1d` and output `c995f63c5e8a6e66ac7e89415e25a4f1aa6ee9ab`.

One ordinary concurrent-main 409 occurred while archiving the output. Main was refreshed and the create-only write retried without force or overwrite; exact readback then succeeded.

## 7. Before / after / remaining scientific gate

Before this run, B02 had the source-valid spectral bound `0<=C<=2I` and a local single-conditioning `1/3` cap, while the team lead had an internal full proof candidate through complete graphs and the Cocks/Semple--Welsh transfer.

After this run:

1. the assigned log-concavity input is pinned explicitly to the exact unrooted all-sizes forest polynomial;
2. the stronger exact row budget `(RB)` is proved for every graph;
3. a hypothetical smallest counterexample must satisfy the edge-count severity bound `(SEVERITY)`;
4. the named partner's Jensen complete-graph module has been consumed and is compatible with the lead chain.

The parent candidate already has two independent end-to-end reviews in the shared team state. This run does not add a novelty/priority claim. External expert/source scrutiny remains appropriate before any public assertion that the longstanding forest conjecture is solved.

## 8. Operations / privacy / runtime metadata

Current-account inventory inspection showed the twenty managed B01--B20 registrations enabled, hourly, role-aligned, with B20 enabled and quiet delivery retained; no current deficit was observed and B02 made zero scheduler mutations. Disabled legacy tasks were not acted on.

Scoped privacy/secret review: PASS. This report/artifact set contains no credentials, scheduler identifiers, machine paths, raw private transcripts, benchmark gold, unrelated private data, or permission material.

Model self-report: `GPT-5.6 Sol`. Requested effort: `maximum actually supported`. Configured/known effort: `UNKNOWN_NOT_EXPOSED`. Provider token/reasoning usage: `null / NOT_EXPOSED`. Measured execution wall time at report freeze: `561.453 s`, including tool/network time and not pure thinking.
