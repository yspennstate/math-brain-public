Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but authenticated runtime metadata does not establish GPT-6/maximum, so I do not claim it. **NO SOURCE-METRIC MOVEMENT:** Salez Problem 2.3 remains OPEN and historical `W_exp` remains `1/2 provisional`; this run instead proves a new source-admissible obstruction family for the Sarnak–Xue / endpoint-collision route.

# PROB10-08 — affine high-multiplicity stress test for transitive-expander cutoff

Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / OPEN / obstruction proved / cutoff for the stress-test family not proved / independent validation pending**.

## 0. Contract recovery and nonduplication

Before research I read/recovered the controlling and ownership state required by the PROB10 contract:

- `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md` (the posted Abelian Cayley/product-condition target remains excluded);
- `operations/claims/I0112.md`;
- newest own PROB10-08 report `runs/prob10_2026-09-20/PROB10-08/2026-09-20T01-48-49Z_pre-entropic-lre-cutoff_4f2a.md`, together with the preceding vanishing-LRE and large-LRE-quotient reports;
- R16 handoff `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`, preserving the H0002 successor and its all-prefix isotonic/KKT obstruction;
- historical I0112 reports beginning with `runs/R16/2026-09-16T18-48-00Z_i0112-product-varentropy.md` and including the synchronous-tensor, moving-window/Poincare, Hecke/information-curvature and tree-subcommutation failures;
- newest related P26 report `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_05-01-42__graph-square-shell-entropy-transfer.md`.

Accordingly I did not repeat finite-fiber, line-graph, graph-square, truncation/replacement-product, product-varentropy, synchronous-tensor, moving-Poincare, Hecke/curvature or tree-subcommutation routes.

## 1. Fresh primary-source check

The exact source remains Justin Salez, arXiv:2508.21055v1, Problem 2.3: prove cutoff for every bounded-degree vertex-transitive expander sequence under his rate-one continuous-time SRW convention.

Dylan Altschuler, arXiv:2609.14945, is still v1, submitted 14 September 2026; a bounded fresh search found no v2, erratum or correction. I reread the proof segment where LRE is consumed: Lemma 3.2 transfers tree-rate set growth to the oriented-edge NBRW graph, Lemma 3.3 turns that growth into near-maximal endpoint Shannon entropy by the forest/departure decomposition, and Proposition 3.1 feeds that entropy into the cutoff proof. This stronger LRE hypothesis is not inferred from transitivity plus spectral expansion.

The comparison theorem used below is Golubev–Kamber, arXiv:1905.11165v3: their Sarnak–Xue density property with parameter `A=1`, plus expansion, yields cutoff. That is an important positive baseline, not a new result of this run.

A bounded search also checked the exact affine family of Haiman–Schildkraut–Zhang–Zhao, BLMS 2022 / arXiv:2109.13131. I found no current paper proving cutoff for that exact family and no source explicitly recording the uniform full-graph gap estimate below. This negative search is not a novelty certificate.

## 2. Idea written before computation

The prior PROB10-08 run showed that maximal ambient tree growth cannot follow from transitivity plus a gap. The natural next replacement is a **Green-function / collision estimate** for the NBRW endpoint, because unlike the oriented-edge NBRW operator, the vertex endpoint kernel is a self-adjoint polynomial of adjacency.

Before trying to prove such an estimate universally, I looked for a source-admissible transitive expander with unusually large positive spectral multiplicity. Haiman et al.'s affine Cayley construction is exactly such a stress test. The decisive question was first whether their 18-regular family can itself be certified to have a uniform one-sided gap; their paper proves large second-eigenvalue multiplicity but does not state the uniform bound needed here. The new representation calculation below supplies that gap and then shows that the Sarnak–Xue / collision route fails polynomially on this admissible family.

## 3. Approach 1 — affine representation theory: SUCCESS AS AN OBSTRUCTION FAMILY

Take the Haiman et al. family on

`Gamma_q = SL(2,q) semidirect F_q^2`,

along an infinite odd-q LPS subfamily. Their lifted subgroup generating set `S subset Pi=SL(2,q)` has `|S|=16` and adjacency gap at least 4. Specialize the added generator to a pure nonzero translation `t=(I,e)` and form

`G_q = Cay(Gamma_q, S union {t,t^{-1}})`.

The detailed proof in the matching artifact establishes

`lambda_2(A_Gq) <= 15+sqrt(3)`

and therefore

`gap(P_Gq) >= (3-sqrt(3))/18`.

The mechanism is a two-dimensional compression inside the unique nontrivial irreducible `phi` occurring in `Ind_Pi^Gamma(1)`. On `phi`, the `S`-operator has one 16-eigenvector `u` and is at most 12 on `u^perp`. In the affine permutation model,

`<u,(R_t+R_t^{-1})u> = -2/(q^2-1)`

and the off-axis component has norm `< sqrt(2)`. The worst Rayleigh quotient is therefore at most the top eigenvalue of

`[[16,sqrt(2)],[sqrt(2),14]]`,

namely `15+sqrt(3)`. Every other irreducible block is at most 14 by the subgroup gap plus `||R_t+R_t^{-1}||<=2`.

Thus this is a genuine bounded-degree vertex-transitive **spectral expander** sequence and is admissible for Salez Problem 2.3.

Haiman et al. also give a second adjacency eigenvalue at least 14 with multiplicity

`m_q >= q^2-1 >= n_q^(2/5)-1`,  `n_q=q^3(q^2-1)`.

For degree 18 the nonbacktracking branching number is 17. At normalized eigenvalue `7/9`, the large nonbacktracking root is

`theta_0=7+4sqrt(2)`.

Since `theta_0>12` and `12^6>17^5`, its Golubev–Kamber p-value is strictly greater than 6. Hence the family has at least `n^(2/5)-1` eigenvalues with p-value greater than 6. Sarnak–Xue density with `A=1` would require, at `p=6`, at most `O(n^(1/3+epsilon))` such eigenvalues. Taking `epsilon=1/30` gives a contradiction.

**Conclusion:** a proof of Salez 2.3 cannot proceed by showing that transitivity plus a fixed gap automatically implies the `A=1` Sarnak–Xue density property.

This does **not** show that the affine family lacks cutoff.

## 4. Approach 2 — self-adjoint NBRW endpoint Green function: SUCCESS AS A PRECISE BARRIER

Let `K_k` be the length-k NBRW endpoint kernel. On an undirected regular graph it is symmetric (reverse every nonbacktracking path), hence a polynomial in adjacency. Vertex transitivity makes the diagonal of `K_k^2` constant, so exactly

`sum_y K_k(x,y)^2 = (1/n) sum_i kappa_k(lambda_i)^2`.

For a positive normalized eigenvalue with nonbacktracking root `theta`, the exact Golubev–Kamber formula gives

`kappa_k(lambda) >= (17/18)(theta/17)^k`.

For the high-multiplicity affine eigenvalue, `p(lambda)>6`, hence `theta/17>17^(-1/6)`. At

`k=floor(log_17 n)`

this yields

`sum_y K_k(x,y)^2 >= c n^(-14/15)`

uniformly in `x`. Uniform measure has collision `1/n`, so

`n sum_y K_k(x,y)^2 >= c n^(1/15)`.

**Conclusion:** even inside the exact source class, transitivity plus a spectral gap does not force near-uniform NBRW collision at the ambient tree-entropic radius. The earlier oriented-edge nonnormality problem can be removed by passing to the endpoint kernel, but the desired Green-function estimate is then simply false.

This statement is deliberately only in chi-square/collision scale. It is **not** a TV lower bound and does not imply a linear Shannon-entropy deficit.

## 5. Approach 3 — semidirect Fourier/Feynman–Kac route: PARTIAL, RETAINED AS THE NEXT NON-LRE DIRECTION

The same affine family has an exact Markov-additive decomposition that is not one of the exhausted R16 product routes. With semidirect multiplication

`(M,x)(N,y)=(MN,x+My)`,

Poisson thinning of the rate-one 18-generator walk gives subgroup moves at total rate `8/9` and translation moves at total rate `1/9`. The subgroup coordinate `M_t` is therefore an `S`-walk on `SL(2,q)` run at rate `8/9`; a translation event at time `tau` adds `+M_tau e` or `-M_tau e` to the additive coordinate.

For every nontrivial additive character `chi_xi` of `F_q^2`, conditional on the subgroup path,

`E[chi_xi(X_t) | (M_s)_(s<=t)]`

` = exp{ (1/9) integral_0^t [Re chi_xi(M_s e)-1] ds }`.

Under uniform `M`, `Me` is uniform on `F_q^2\{0}`, so

`E[Re chi_xi(Me)] = -1/(q^2-1)`.

This gives a concrete Feynman–Kac target for the affine cutoff question. I did not turn it into a cutoff theorem: direct Parseval summation pays for all `q^2-1` characters and does not capture the TV effect of a single well-randomized translation, while the joint `(M_t,X_t)` law—not only the additive marginal—must be controlled. A regeneration or conditional-entropy estimate is still missing.

## 6. Source-level before / after and metric accounting

**Before:** Salez Problem 2.3 OPEN. Historical R16 metric `W_exp=1/2 provisional`; the three preceding PROB10-08 runs enlarged Altschuler-style sufficient classes but did not solve the source.

**After:** Salez Problem 2.3 remains **OPEN**. No cutoff theorem for the affine stress-test family is claimed, so the graph-class/window metric does not move and `W_exp` remains `1/2 provisional`.

**Auxiliary mechanism movement, proved this run:**

1. the Haiman affine Cayley family can be specialized to a bounded-degree vertex-transitive expander with explicit normalized one-sided gap at least `(3-sqrt(3))/18`;
2. this source-admissible family violates Sarnak–Xue density with parameter `A=1`;
3. its NBRW endpoint collision at `floor(log_17 n)` is at least `c n^(-14/15)`, a polynomial factor above uniform collision;
4. the exact semidirect Feynman–Kac identity isolates a new non-LRE route for a future run.

Under the PROB10 contract this is recorded as an **obstruction/different-method run**, not falsely promoted to source progress.

## 7. Artifact, checks, and remaining obligation

Matching proof artifact:

`artifacts/prob10_2026-09-20/PROB10-08/2026-09-20T03-00-00Z_affine-sx-green-obstruction_9c21.md`

created at commit

`fc3da4d53e673f0f2bdedb01f74c7df18a8164bf`

and read back at that exact commit.

No finite mixing plots were run or used. No asymptotic conclusion comes from numerics. The proof is analytic. A private numerical sanity check of the exact p-value was used only to orient the inequality; the archived proof relies instead on the exact elementary comparison `12^6>17^5`.

The remaining source-level obligation is unchanged in nature but sharper in form: one needs an entropy/TV mechanism that tolerates polynomial NBRW collision excess and high spectral multiplicity. The most concrete next target is the affine Feynman–Kac identity above: prove a regeneration/conditional-entropy statement strong enough to establish or refute cutoff for this source-admissible family.

No scheduler setting, cadence, enabled state, email, Drive object, public posting, permission, workflow, shared root ledger, peer-track file, or R16 handoff file was modified.