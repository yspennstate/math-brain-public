# FOREST / fleet01 B01 — rank-homogeneous spectral budget plus a source-safe triangle-free Simpson gate

**Run:** `20260922T050946Z-b01-forest-auto11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Candidate:** `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`  
**Brain context:** `WITHOUT_VERIFIED_BRAIN`  
**Fresh owner control at entry:** revision `2026-09-22.2`, commit `00144d7b67dd3e19eba85f41997ef28c7206718e`; a later freshness read reached `9866823882d19977fa85858e7563a7a92d984922` with the same protected-control blobs and the same FOREST allocation.

## 1. Exact source scope and inherited state

The source target is unchanged. For a finite simple graph `G=(V,E)`, let `F` be uniform over **all** acyclic edge subsets, including the empty forest, disconnected forests and every possible forest size. For distinct present edges `e,f`, prove

`P(e,f in F) <= P(e in F) P(f in F)`.

No rooted law, fixed-size law, spanning-tree law or arbitrary positive external field is substituted for the source statement.

The latest complete lead version consumed before new mathematics is fleet01/B01 run `20260922T043718Z-b01-forest-auto11`, report blob `adc332e97b112525d92cf601ad1493f2e1745987`. It correctly withdrew the previous `FOREST-KN-COCKS-RECONCILED-v3` candidate: the fixed-graph reading `unit-good G => weighted I-Rayleigh M(G)` is not source-secure. The surviving exact replacement is that all-positive-weight `K_n` is already equivalent to the whole source conjecture via the simple path-bundle gadget and epsilon deletion specialization. Therefore weighted `K_n` cannot be treated as a small globalization lemma.

The older P14 handoff `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md` preserves exact unit source coverage through nine vertices and block factorization. Its claimed 3-connected minimal-counterexample reduction, however, explicitly used the same fixed-graph Cocks implication in the two-separator step. After the lead's source correction that 3-connected reduction is not used here as an unconditional fact.

The P0001/R02 lineage was recovered exactly. R02 run `20260918T0024Z_8c7d1e52.md` proves, without the fixed-graph Cocks step, the partial theorem that p-NC holds whenever every nontrivial 2-connected block has cyclomatic number at most six; its exact endpoint is the 19 connected cubic 10-vertex graphs. R02's subsequent `r_block:6->7` handoff `20260918T0102Z_61f4a9c7.md` uses the now-disputed fixed-graph Cocks upgrade to transfer from cubic 12-vertex supergraphs to their contraction minors. I therefore preserve `r_block>=6` as source-secure and treat the claimed `r_block>=7` movement as conditional pending an independent contraction argument. Historical files are not rewritten.

## 2. Named OTHER-account result consumed and strengthened

I consumed the named partner fleet02/B02 run `20260922T041021Z-fleet02-B02-forest-r13`, report blob `d0ed896c51a038ac352aa45c3e9c40513e237dfb`. Its source-valid core is the homogeneous log-concavity/Hessian method: augment the edge indicators by the homogenizing exponent and use `- Hess log g >= 0` to obtain an edge-row correlation budget, a size-susceptibility budget and a 3-by-3 pair comparison. I do **not** use its Cocks-dependent minimal-counterexample consequences.

There is a useful strengthening that the partner report did not exploit. Let `R=r(M(G))=|V|-kappa(G)` be the graphic-matroid rank, rather than `m=|E|`. For a matroid, the canonical homogenized independent-set polynomial

`g(y,z)= sum_{F forest} y^(R-|F|) prod_{h in F} z_h`

is completely log-concave. The public source is Anari--Liu--Oveis Gharan--Vinzant, *Log-Concave Polynomials II: High-Dimensional Walks and an FPRAS for Counting Bases of a Matroid*, arXiv:1811.01816; the partner report had a mistyped arXiv number. The rank-degree homogenization is the natural stronger choice. The partner's degree-`m` homogenization is obtained by multiplying by `y^(m-R)` and gives a weaker denominator.

At the all-ones point every forest has coefficient one, so the induced law is exactly the source uniform law.

## 3. New theorem A: the rank-homogeneous augmented budget

Write

- `X_h = 1[h in F]`,
- `K=|F|`,
- `p_h=E X_h`,
- `mu=E K`,
- `v=Var(K)`,
- `c_h=Cov(X_h,K)`,
- `C_hj=Cov(X_h,X_j)`,
- `rho_hj=C_hj/sqrt(p_h(1-p_h)p_j(1-p_j))`.

Every present edge has `0<p_h<=1/2`: the singleton forest gives positive inclusion probability, and deleting `h` is an injection from forests containing `h` into forests omitting it.

For a monomial of `g`, let the exponent vector be

`U=(R-K, X_1,...,X_m)`.

For any positive-coefficient generating polynomial at the all-ones point,

`- Hess log g(1) = diag(E U) - Cov(U)`.

Log-concavity therefore gives `A-Sigma >=0`, where `A=diag(EU)` and `Sigma=Cov(U)`. Since `Sigma>=0`,

`N=A^(-1/2) Sigma A^(-1/2)` satisfies `0<=N<=I`, hence `N^2<=N`.

Taking the diagonal entry corresponding to an edge `e` and subtracting the square of `N_ee=1-p_e` yields

**(A1)**

`c_e^2 / ((R-mu)p_e(1-p_e)) + sum_{h!=e} (1-p_h) rho_eh^2 <= p_e`.

Equivalently,

`c_e^2/(R-mu) + sum_{h!=e} C_eh^2/p_h <= p_e^2(1-p_e)`.

This is strictly at least as strong as the partner's degree-`m` version because `R<=m`, so `R-mu<=m-mu`.

The slack-coordinate diagonal of `N^2<=N` similarly gives

**(A2)**

`v^2/(R-mu) + sum_h c_h^2/p_h <= v`.

Since `sum_h c_h=Cov(K,K)=v`, Cauchy--Schwarz implies `sum c_h^2/p_h >= v^2/mu`, and hence

`v <= mu(R-mu)/R`.

Finally put

`q = R-mu-v >=0`,

`d_ef = p_e p_f - P(e,f in F) = -C_ef`.

The `(slack,e,f)` principal block of `-Hess log g(1)` is

`[[q,c_e,c_f],[c_e,p_e^2,d_ef],[c_f,d_ef,p_f^2]]`.

Its determinant is nonnegative:

**(A3)**

`q p_e^2 p_f^2 + 2 c_e c_f d_ef - q d_ef^2 - p_f^2 c_e^2 - p_e^2 c_f^2 >=0`.

When `q>0`, equivalently

`|d_ef-c_e c_f/q| <= sqrt((p_e^2-c_e^2/q)(p_f^2-c_f^2/q))`.

As in the partner report, this is an interval comparison and does not by itself force `d_ef>=0`. The gain here is that every occurrence of `m-mu` has been replaced by the smaller, canonical `R-mu`.

## 4. New theorem B: source-safe Simpson conditioning on triangle-free edges

Assume for contradiction that the source conjecture fails, and choose a counterexample `G` with the **minimum number of edges**. Fix a violating pair `e,f`, and put

`a=rho_ef>0`.

Let `T(G)` be the set of physical edges of `G` contained in no triangle. Fix `g in T(G)\{e,f}`.

Conditioning on `X_g=0` is exactly the uniform forest law on `G\g`, a smaller simple graph. Conditioning on `X_g=1`, removing the compulsory edge and contracting it is exactly the uniform forest law on `G/g`. Because `g` is in no triangle, contracting `g=uv` creates neither a parallel pair nor a second copy of a marked edge: a parallel pair after contraction would come from a common neighbor of `u,v`, which is precisely a triangle through `g`. Thus `G/g` is again simple and has fewer edges. By edge-minimality,

`Cov(X_e,X_f | X_g=0) <=0`,

`Cov(X_e,X_f | X_g=1) <=0`.

The binary law of total covariance is exact:

`C_ef = (1-p_g) C_ef|0 + p_g C_ef|1 + C_eg C_fg / Var(X_g)`.

Therefore for **every triangle-free conditioner** `g`,

**(B1)**

`C_eg C_fg / Var(X_g) >= C_ef >0`,

or after standardization,

**(B2)**

`rho_eg rho_fg >= a`.

This recovers the old Simpson inequality on exactly the source-secure conditioning edges, without any weighted Cocks theorem.

## 5. New combined obstruction: rank slack + triangle-free Simpson

Let

`S=T(G)\{e,f}`, `s=|S|`,

`T_e = c_e^2/((R-mu)p_e(1-p_e))`, and similarly `T_f`.

Add (A1) for `e` and `f`, retain only the nonnegative terms indexed by `S`, and use (B2):

`T_e+T_f +(2-p_e-p_f)a^2 + sum_{g in S}(1-p_g)(rho_eg^2+rho_fg^2) <= p_e+p_f`.

For each `g in S`, `rho_eg rho_fg>=a>0`, so

`rho_eg^2+rho_fg^2 >= 2a`.

Also `p_h<=1/2` for every edge. Hence

**(C1)**

`boxed:  T_e + T_f + a^2 + s a <= 1.`

In particular,

**(C2)**

`a <= (sqrt(s^2+4(1-T_e-T_f))-s)/2 <= (sqrt(s^2+4)-s)/2`.

This is a source-valid replacement for the earlier all-edge obstruction. It becomes stronger when either marked edge has appreciable covariance with forest size, and it automatically strengthens the partner's `m-mu` susceptibility term to the rank denominator `R-mu`.

### Triangle-free positive-correlation matching

There is a second structural consequence that survives the Cocks correction. Restrict attention to the physical edge set `T(G)`. If `i,j,k` are distinct triangle-free edges and `C_ij>0`, then using `k` as conditioner gives `rho_ik rho_jk>=rho_ij>0`. Thus if also `C_jk>0`, then `C_ik>0`: positive correlation is transitive on `T(G)`.

A positive triangle of correlations is impossible. If

`x=rho_ij>0`, `y=rho_ik>0`, `z=rho_jk>0`,

then applying (B2) cyclically (all three conditioners are triangle-free) gives

`x<=yz`, `y<=xz`, `z<=xy`.

Multiplying gives `xyz<=(xyz)^2`, impossible because distinct edge indicators are not almost surely identical and hence `0<xyz<1`.

Therefore:

**(C3)** the graph of positive covariance pairs **restricted to triangle-free physical edges** is a matching.

If the violating pair `e,f` itself lies in `T(G)`, then every other `g in T(G)` is strictly negatively correlated with both `e` and `f`: (B2) says the two signs agree and (C3) rules out both being positive.

This restores the useful part of the older `FOREST-SIMPSON-MATCHING-v1` geometry on a rigorously source-safe domain.

## 6. Exact localization of the remaining contraction debt

The preceding theorem identifies exactly why triangle edges are different. Let `g=uv` lie in one or more triangles, and contract it. For every common neighbor `w` of `u` and `v`, the two simple edges `uw` and `vw` become a parallel class of multiplicity two. After simplifying the contracted multigraph, the conditional uniform law is the independent-set law of a smaller simple graph `H` with **weight 2** on each edge `xw` corresponding to a common neighbor and weight 1 on every other edge. All doubled edges lie on the single star centered at the contracted vertex `x`.

Thus the first missing comparison needed to extend (B1) from triangle-free conditioners to all conditioners is not arbitrary external fields. It is the much narrower source-generated statement:

> **STAR-2 contraction comparison.** For the specific smaller simple graph obtained by contracting one edge of an edge-minimal source counterexample, prove the marked pair is nonpositively correlated when exactly the contracted-vertex star edges arising from common neighbors have weight 2 and all other edges have weight 1.

This is an exact identity of the conditional source law, not a replacement conjecture asserted without payment. It localizes the only obstruction to the total-covariance step. Proving arbitrary weighted `K_n` would be equivalent to the whole parent conjecture; proving this source-generated star-doubling comparison would be strictly more targeted.

No proof of STAR-2 is claimed here. A one-edge or one-triangle special case would be auxiliary unless it yields a mechanism uniform in the size of the doubled star.

## 7. Correction to inherited structural claims

Two inherited claims must be kept separate after the source audit:

1. P14's complete unit source coverage through nine vertices remains usable.
2. P14's **3-connected** minimal-counterexample reduction is not used here because its two-separator transfer invoked the same fixed-graph weighted upgrade now rejected by the lead.
3. R02's `r_block<=6` theorem remains source-secure from its Huang simplification plus exact finite endpoint.
4. R02's `r_block<=7` handoff is presently conditional: its cubic-completion lemma is valid, but the transfer from a unit-good cubic 12-vertex graph to an arbitrary contraction minor used fixed-graph Cocks/minor closure.

The present argument needs only edge-minimality among simple counterexamples and therefore does not inherit either disputed weighted step.

## 8. Compact conditional end-to-end argument and first missing implication

The current source-safe chain is:

1. choose an edge-minimal simple counterexample and a violating pair;
2. for every triangle-free third edge, deletion and contraction are smaller **simple** source instances, so exact total covariance gives (B2);
3. the canonical rank-homogeneous completely-log-concave polynomial gives the stronger spectral/susceptibility budget (A1)--(A3);
4. combining them yields the quantitative obstruction (C1)--(C2) and matching structure (C3) on all triangle-free physical edges;
5. for a triangle conditioner, the only failure of the induction gate is the exactly described `{1,2}`-weighted star in the contracted simple graph.

The **first essential missing implication** is therefore the source-generated STAR-2 comparison above, or an alternative direct argument that makes its conditional covariance nonpositive. Solving that implication would restore the Simpson inequality for every conditioner; it would not by itself be advertised as a full proof until the resulting global minimal-counterexample constraints are shown inconsistent.

## 9. Failure evidence and computation policy

No finite census is used to support the new theorem. The proof is algebraic once the complete-log-concavity theorem and edge-minimality are admitted. I performed exploratory searches for a fixed-graph weighted counterexample during derivation, but they are omitted from the mathematical evidence because they did not produce a counterexample and would only repeat known small-graph information.

The failed routes are preserved rather than hidden:

- the fixed-graph Cocks globalization remains rejected fail-closed;
- all-positive-weight `K_n` is parent-equivalent and is not used as a bridge;
- complete log-concavity alone still gives an interval/spectral constraint rather than the desired entrywise sign;
- the triangle-edge contraction strata still require STAR-2 or another genuinely new mechanism.

## 10. Status

**Outcome: `ESSENTIAL_STEP_APPLIED`.**

The parent Grimmett--Winkler conjecture remains open in this report. The substantive movement is:

- partner B02's augmented Hessian method is strengthened from ground-size denominator `m-mu` to the canonical matroid-rank denominator `R-mu`;
- the previously Cocks-dependent universal Simpson argument is repaired on every triangle-free conditioning edge using only simple-minor minimality;
- these two ingredients combine to the new quantitative source-safe bound (C1);
- the positive-correlation graph on triangle-free physical edges is proved to be a matching;
- the remaining weighted debt is localized exactly to weight-2 edges on one contracted-vertex star.

No full-proof candidate is claimed and no novelty/priority claim is inferred from repository or web search misses.

## 11. Provenance / runtime truth

Named OTHER-account result actually consumed: fleet02/B02 `20260922T041021Z-fleet02-B02-forest-r13`, blob `d0ed896c51a038ac352aa45c3e9c40513e237dfb`.

Historical dependencies actually read: P14 mandatory handoff blob `bed2241d948b8a20b854efc248ccf5b46b4325cd`; P0001 claim blob `da1ca9681a08f0abc657e043af0dc19d594c9940`; R02 beta-6 report blob `968967909df972f84700eae10ea676cccc648dc6`; R02 beta-7 ownership/handoff report as preserved historical evidence; latest lead report blob `adc332e97b112525d92cf601ad1493f2e1745987`.

No installation/benchmark work, email, Drive operation, public posting, paid model/API/Codex execution, remote workflow, permission change, production-population mutation or cross-account authentication occurred. The current-account inventory was inspected only from the authorized fleet01 snapshot; it reported 20/20 managed slots enabled/hourly-valid with exposed task email/notification flags false. No scheduler mutation was made.

Model self-report: `GPT-5.6 Sol`. Requested effort: `maximum actually supported`. Configured reasoning effort: `UNKNOWN_NOT_EXPOSED`. Provider reasoning-token/time counters: `NOT_EXPOSED`. Elapsed execution is reported separately in the finish record and includes tool/network/runtime time, not pure thinking.
