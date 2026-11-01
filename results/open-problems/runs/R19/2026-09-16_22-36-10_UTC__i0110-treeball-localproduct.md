Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed interface has no model selector, no reasoning-effort selector, and no authenticated runtime telemetry, so I do not claim otherwise. **METRIC MOVED: I0110 `M_9 = UNMEASURED -> 1/9 CERTIFIED`; Section-B moves actually used: #2 ATTACK THE NEGATION FIRST, #12 FIND WHAT IS CONSERVED, #19 MAKE IT AN ALGORITHM.**

Problem/source: **Justin Salez (2025), _Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon_, arXiv:2508.21055v1, Problem 2.1 (Derandomization), intake I0110.**

Status: **PARTIAL / SOURCE OPEN.** The previous I0084/Hasebe--Ueda target remains handed off after its mandatory six-unchanged-run rotation; this report does not reopen it.

# 1. Continuity, repository state, and why R19 is now on I0110

The immediately preceding R19 report is

`runs/R19/2026-09-16_21-40-25_UTC__i0084-rotation-i0110.md`.

It reached the controlling CLOSABLE threshold of six unchanged runs on I0084 after the fixed half-stable metric had already saturated at `2/2`, preserved the version-specific I0084 handoff, and expressly said that **no seventh unchanged I0084 research run should be produced by R19**. It then created the canonical successor claim

`operations/claims/I0110.md`

for Salez Problem 2.1. I therefore continue I0110 rather than restarting a mathematically completed-but-audit-pending I0084 argument.

The I0084 handoff remains at

`artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md`.

Its important source-version distinction remains intact: frozen arXiv v2 Conjecture 5.5 uses ordinary convolution `mu*S_t` even when `S_t` is the law of a free stable distribution; the later ALEA wording uses the classical/free `*` / `boxplus` split. Repository search this run still found no P26 audit of the **frozen arXiv ordinary-`*`** package. The P26/R18 end-to-end free audits located in the repository explicitly certify the different published ALEA `boxplus` scope. Nothing below changes that handoff or its audit status.

Before new mathematics I read/recovered the current repository surfaces required by the fleet contract:

- root `README.md`, `FLEET_RULES.md`, `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- `proofnet24/HOURLY20_PROTOCOL_2026-09-16.md`;
- `operations/FLEET_2026-09-16.md`, `operations/RFLEET_2026-09-16.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- canonical I0110 claim and exact I0110 intake hit in `probability_1000_intake_I_20260914/problems.jsonl`;
- newest complete R19 report;
- neighboring Salez tracks R01/I0113 and R16/I0112;
- newest R20/I0100 package, for the directed audit obligation.

The large intake JSONL files are connector-truncated when rendered wholesale. I used exact-ID/source searches and the canonical claims rather than falsely claiming a manual byte-for-byte rendering of all roughly 780 records.

P26 remains the shared-root ledger writer. This run edits no shared root and no peer file.

# 2. Exact source target and first baseline map

Salez's Problem 2.1 appears immediately after a paragraph listing nine random-graph cutoff references

`[80,16,14,21,13,61,22,52,62]`

and asks for

> a structural property which is almost-surely satisfied by the various random graphs considered above, and which deterministically triggers cutoff.

The canonical R19 metric is therefore

\[
M_9
=
\#\{\text{those nine cited random-graph results covered by one common proved property }P\},
\]

where a citation counts only if the **same explicit property** is

1. proved asymptotically almost surely for the cited random ensemble, and
2. proved to imply total-variation cutoff for every deterministic graph sequence in the stated deterministic domain.

The target is `9/9`. The claim-time baseline was deliberately `UNMEASURED`, not zero.

I mapped the nine source references to the following model families before choosing a candidate property.

| Salez ref. | model/result scope relevant to Problem 2.1 | immediate structural warning |
|---|---|---|
| [80] Lubetzky--Sly | simple random walk / nonbacktracking walk on random regular graphs | locally tree-like, bounded degree in the fixed-d regime |
| [16] Berestycki--Lubetzky--Peres--Sly | random walk on the giant component of sparse `G(n,lambda/n)` and related sparse degree models | dangling/tree geometry; not globally regular |
| [14] Ben-Hamou--Salez | nonbacktracking walk with prescribed random degrees | chain is nonbacktracking, so a criterion tied only to ordinary SRW is too narrow |
| [21] Bordenave--Caputo--Salez | sparse random digraphs / directed configuration model | nonreversible; symmetric-support criteria fail |
| [13] Ben-Hamou | random graphs with two-community structure, nonbacktracking cutoff threshold | bottleneck scale may vanish with `n` |
| [61] Hermon--Sly--Sousi | bounded-degree base graph plus random perfect matching | quasi-tree/random-matching geometry rather than a pure configuration model |
| [22] Bordenave--Lacoin | random walks on covered expanders; random regular / random-lift applications | already comes with an explicit deterministic covered-expander cutoff criterion |
| [52] Hermon--Olesker-Taylor | random Abelian Cayley graphs with a growing random generator set | degree grows; commuting generators create short cycles |
| [62] Hermon--Sarkovic--Sousi | finite-community configuration models | community Cheeger parameter may decay while cutoff still holds above the threshold |

This table is a source/model map, not a claim that the cited papers have identical normalizations.

# 3. Dated current-status and prior-art refresh

Search date: **16--17 September 2026 UTC window**.

Primary/current sources checked included:

- Salez, arXiv:2508.21055v1, exact Problem 2.1 paragraph and bibliography;
- Pedrotti--Salez, _The local product condition implies cutoff_, arXiv:2607.05345 (July 2026);
- Lubetzky--Sly, random regular graph cutoff;
- Berestycki--Lubetzky--Peres--Sly, sparse random graph cutoff;
- Ben-Hamou--Salez, nonbacktracking sparse random graph cutoff;
- Bordenave--Caputo--Salez, sparse random digraph cutoff;
- Ben-Hamou, two-community nonbacktracking cutoff;
- Hermon--Sly--Sousi, random-perfect-matching cutoff;
- Bordenave--Lacoin, covered-expander entropic-time cutoff;
- Hermon--Olesker-Taylor, random Abelian Cayley cutoff;
- Hermon--Sarkovic--Sousi, random graphs with community structure;
- Salez, _The varentropy criterion is sharp on expanders_;
- Hermon--Huang--Pedrotti--Salez, _Concentration of information on discrete groups_.

Queries included exact `Problem 2.1`, `Derandomization`, `random graph cutoff structural property`, `local product random regular graph`, `non-equilibrium Poincare random regular graph`, `varentropy random graph cutoff`, and later Salez cutoff papers.

I found no source explicitly claiming a resolution of Problem 2.1 across all nine ensembles. In particular Pedrotti--Salez prove a general **local-product** sufficient condition but the paper does not itself verify that condition for Salez's nine random-graph families. This is a bounded dated search miss, **not** a novelty certificate.

Two details of Pedrotti--Salez are crucial for the attack below. For a law `mu` and Markov kernel `K`, define

\[
\gamma_K(\mu)\,\operatorname{Var}_\mu(f)
\le
\int \Gamma_K f\,d\mu,
\tag{3.1}
\]

and, along a trajectory `mu_t`, the global local-product constant

\[
\gamma_*:=\inf_{t>0}\gamma_K(\mu_t).
\tag{3.2}
\]

Their theorem yields a cutoff criterion from `gamma_* t_mix -> infinity`. Their Remark 2 also introduces a **restricted mixing-window version** (call it `gamma_epsilon`) in which the infimum is taken only across the relevant mixing interval. The restricted version can be much larger than the global `gamma_*`. The distinction turns out to be essential.

# 4. Move #2 — attack the proposed common properties before trying to prove one

The first I0110 run is required to attack the negation. Several attractive one-line common criteria die immediately against the exact nine-model map.

## 4.1 Uniform bounded degree fails

Reference [52] is a random Abelian Cayley regime with a growing number of random generators. Therefore a structural property requiring a uniform maximum-degree bound cannot cover all nine cited scopes.

## 4.2 Reversibility or symmetric support fails

Reference [21] treats sparse random **digraphs** and nonreversible random walks. A property whose deterministic cutoff theorem requires reversibility cannot be a literal nine-family answer.

## 4.3 Literal local tree-likeness fails

Random Abelian Cayley graphs [52] have commuting generators and consequently systematic short commutator cycles. Thus a criterion demanding tree neighborhoods out to a diverging radius cannot be common to all nine.

## 4.4 Uniform expansion fails as a common literal property

The two-community/community-structure regimes [13] and [62] allow the macroscopic bottleneck parameter to decay with `n`; their cutoff threshold is formulated in a product such as a community-conductance/Cheeger scale times `log n`, rather than a fixed positive expansion constant. Therefore a uniform spectral-gap/Cheeger lower bound is too strong for the full source list.

The most promising new 2026 candidate is more subtle: the Pedrotti--Salez local-product condition. The next theorem shows that its **global-inf** form is also too strong even for the canonical fixed-degree random-regular member [80].

# 5. R19-I0110-C001 — early tree geometry forces a small global local-product constant

**STATUS: PROVED.** This is a deterministic theorem about the Pedrotti--Salez non-equilibrium Poincare quantity. Constants are not optimized.

Let `G` be a finite `d`-regular graph, `d>=3`. Let

\[
K(x,y)=\frac1d\mathbf 1_{\{x\sim y\}},
\qquad
L=K-I,
\]

and let `(X_t)` be the corresponding rate-one continuous-time simple random walk started at `o`. Put

\[
\mu_t=\mathcal L(X_t),
\]

and use the carré-du-champ normalization

\[
\Gamma f(x)
=
\frac12\sum_y K(x,y)(f(y)-f(x))^2.
\tag{5.1}
\]

For any probability law `mu`, define

\[
\gamma_G(\mu)
:=
\inf_{\operatorname{Var}_\mu f>0}
\frac{\int\Gamma f\,d\mu}{\operatorname{Var}_\mu f},
\tag{5.2}
\]

and

\[
\gamma_*(o):=\inf_{t>0}\gamma_G(\mu_t).
\tag{5.3}
\]

### Theorem C001

Suppose the rooted ball `B_G(o,4r)` is isomorphic to the radius-`4r` ball in the infinite `d`-regular tree. Then for all sufficiently large `r`,

\[
\boxed{
\gamma_*(o)\le \frac{16}{r}.
}
\tag{C001}
\]

### Proof

#### Step 1: a globally 1-Lipschitz extension of a tree Busemann function

Identify `B_G(o,4r)` with the corresponding tree ball and choose an end `xi` of the infinite tree. Let `b` be the associated Busemann function, normalized by `b(o)=0`. Along every tree edge,

\[
|b(x)-b(y)|=1.
\tag{5.4}
\]

Restrict `b` first to the inner ball `B_G(o,r)`. I claim this restriction is 1-Lipschitz for the **global graph metric**, not only for the intrinsic tree metric.

Indeed, if `x,y in B_G(o,r)`, the tree path between them has length at most `2r`. Any graph path from `x` to `y` that leaves `B_G(o,4r)` must travel more than `3r` from `x` before exiting and more than `3r` to return to `y`, hence has length greater than `6r`. A shortest path therefore stays inside the radius-`4r` tree ball, where its length is the tree distance. Consequently

\[
|b(x)-b(y)|\le d_G(x,y)
\qquad(x,y\in B_G(o,r)).
\tag{5.5}
\]

By the McShane extension theorem there is a function `f:V(G)->R` extending `b` on `B_G(o,r)` such that

\[
f(o)=0,
\qquad
|f(x)-f(y)|\le d_G(x,y)
\quad\text{for all }x,y.
\tag{5.6}
\]

In particular every graph-edge increment has magnitude at most 1, so

\[
\boxed{
\Gamma f(x)\le\frac12
\quad\text{for every }x.
}
\tag{5.7}
\]

#### Step 2: couple to the infinite-tree walk until the finite walk has made `r` jumps

Let `(\widetilde X_t)` be rate-one continuous-time simple random walk on the infinite `d`-regular tree, started at the root and coupled through the rooted-ball isomorphism while the path stays in the inner ball. Let

\[
N_t\sim\operatorname{Pois}(t)
\]

be the common jump count.

On the event `{N_t<r}`, every path has graph distance strictly less than `r` from the root, so the two walks can be coupled identically inside the tree ball and

\[
f(X_t)=b(\widetilde X_t).
\tag{5.8}
\]

Set

\[
F_t:=f(X_t),
\qquad
B_t:=b(\widetilde X_t).
\]

Even on the complement, both rooted Lipschitz functions are bounded by the number of jumps:

\[
|F_t|\le N_t,
\qquad
|B_t|\le N_t.
\]
Hence

\[
|F_t-B_t|\le2N_t\mathbf 1_{\{N_t\ge r\}},
\]
so

\[
\|F_t-B_t\|_2^2
\le
4\,\mathbb E[N_t^2\mathbf 1_{\{N_t\ge r\}}].
\tag{5.9}
\]

#### Step 3: the tree Busemann coordinate has exact variance `t`

At every tree jump, the Busemann increment is `+1` in one oriented direction and `-1` in the other `d-1` directions (or the opposite sign convention). Thus the jump increments are iid random variables `xi_j` satisfying

\[
\xi_j^2=1.
\]

The Busemann process is a compound Poisson sum

\[
B_t=\sum_{j=1}^{N_t}\xi_j.
\]

For a compound Poisson process,

\[
\operatorname{Var}(B_t)
=t\,\mathbb E[\xi_1^2]
=t.
\tag{5.10}
\]

The nonzero drift does not alter (5.10).

#### Step 4: the exit-error is exponentially small at `t=r/8`

Take

\[
t=\frac r8.
\tag{5.11}
\]

Using `1_{N>=r}<=2^{N-r}` and the exact Poisson identity

\[
\mathbb E[N^2z^N]
=(tz+t^2z^2)e^{t(z-1)},
\tag{5.12}
\]

we obtain at `z=2`

\[
\mathbb E[N_t^2\mathbf 1_{\{N_t\ge r\}}]
\le
2^{-r}(2t+4t^2)e^t
=
(2t+4t^2)e^{-(8\log2-1)t}
=o(t).
\tag{5.13}
\]

Therefore for all sufficiently large `r`, (5.9) gives

\[
\|F_t-B_t\|_2\le\frac{\sqrt t}{4}.
\tag{5.14}
\]

Centering can enlarge an `L^2` difference by at most a factor two:

\[
\left\|(F_t-\mathbb EF_t)-(B_t-\mathbb EB_t)\right\|_2
\le2\|F_t-B_t\|_2
\le\frac{\sqrt t}{2}.
\tag{5.15}
\]

Since `sd(B_t)=sqrt(t)`, the reverse triangle inequality yields

\[
\operatorname{sd}(F_t)\ge\frac{\sqrt t}{2},
\qquad
\boxed{\operatorname{Var}(F_t)\ge\frac t4.}
\tag{5.16}
\]

#### Step 5: test the non-equilibrium Poincare quotient

From (5.7),

\[
\int\Gamma f\,d\mu_t\le\frac12.
\]
Combining with (5.16),

\[
\gamma_G(\mu_t)
\le
\frac{1/2}{t/4}
=
\frac2t
=
\frac{16}{r}.
\tag{5.17}
\]

Finally `gamma_*(o)<=gamma_G(mu_t)`. This proves C001. QED.

### Scope

C001 is a deterministic upper bound on the **global-inf** local-product constant. It does not say the chain lacks cutoff; in fact the random-regular application below has cutoff. It therefore tests whether Pedrotti--Salez's sufficient condition can be the universal derandomizing property, not whether their theorem is correct.

# 6. R19-I0110-C002 — the global local-product criterion already misses fixed-degree random regular graphs

**STATUS: PROVED relative to the standard local-tree exploration estimate and the Lubetzky--Sly random-regular cutoff theorem.**

Fix `d>=3` and let `G_n` be a uniform simple `d`-regular graph on `n` vertices. Fix a labelled root `o`. Choose any

\[
0<c<\frac12,
\qquad
R_n=\left\lfloor c\log_{d-1}n\right\rfloor,
\qquad
r_n=\left\lfloor\frac{R_n}{4}\right\rfloor.
\tag{6.1}
\]

The standard configuration-model breadth-first exploration of `B(o,R_n)` exposes

\[
O((d-1)^{R_n})=O(n^c)
\]

half-edges. The probability of an exploration collision is therefore

\[
O\!\left(\frac{(d-1)^{2R_n}}n\right)
=O(n^{2c-1})
=o(1).
\tag{6.2}
\]

For fixed `d`, conditioning on simplicity preserves this high-probability local-tree event. Hence

\[
B_{G_n}(o,4r_n)
\]

is a tree with probability tending to one. C001 then gives

\[
\boxed{
\gamma_*(o)
=O_{\mathbb P}\!\left(\frac1{\log n}\right).
}
\tag{6.3}
\]

Lubetzky--Sly prove cutoff for fixed-degree random regular graphs at a mixing-time scale `Theta(log n)` (with the sharper entropic center and `sqrt(log n)`-order window in the SRW statement). Therefore for each fixed accuracy,

\[
t_{\rm mix}^{(n)}(o,\varepsilon)=O_{\mathbb P}(\log n),
\]
so

\[
\boxed{
\gamma_*(o)\,t_{\rm mix}^{(n)}(o,\varepsilon)
=O_{\mathbb P}(1),
}
\tag{C002}
\]

and in particular the product does **not** tend to infinity in probability.

Thus the **global-inf** local-product condition of Pedrotti--Salez is not the single common property answering Salez Problem 2.1: it already fails, with high probability, in the canonical random-regular family [80].

There is no contradiction. Pedrotti--Salez give a sufficient condition, not a necessary one.

## The important escape hatch

Their Remark 2 is now more compelling, not less. It proposes restricting the non-equilibrium Poincare infimum to the actual mixing interval. C001 exploits an **early tree-like epoch** at time `t≈r/8≈c log n`, with `c` arbitrarily small compared with the true mixing center. A restricted mixing-window constant can discard this obstruction.

So this run kills

\[
\gamma_*\,t_{\rm mix}\to\infty
\]

as the nine-family answer, but it does **not** kill a criterion based on

\[
\gamma_\varepsilon
:=
\inf_{t\in[t_{\rm mix}(1-\varepsilon),\,t_{\rm mix}(\varepsilon)]}
\gamma_G(\mu_t).
\tag{6.4}
\]

That is the sharpest new route produced by this run.

# 7. Move #12 — what appears to be conserved is information growth, not geometry

The nine models are structurally too different for the obvious graph-geometric properties above, but their cutoff proofs repeatedly expose the same **information/entropy clock**:

- [80]: escape speed / entropy on the regular tree;
- [16]: speed times harmonic-measure dimension on the Poisson--Galton--Watson local limit;
- [14]: nonbacktracking path information built from the degree sequence;
- [21]: directed path weights / row-entropy concentration;
- [13] and [62]: community-modulated information accumulation and a Gaussian-profile threshold;
- [61]: quasi-tree / random-matching entropy growth;
- [22]: entropy rate of a transitive infinite cover;
- [52]: entropy of the corresponding walk on `Z^k`.

This list is a research diagnosis, not a theorem that one common entropy condition has already been verified.

The C001 obstruction explains why a **global-in-time** curvature/local-product minimum loses the common signal: early-time tree geometry can drive `gamma_*` down even though the chain later exhibits a sharp entropic transition.

The candidate that survives is therefore a **mixing-window information condition**. Two precise versions deserve the next attack:

1. the restricted Pedrotti--Salez quantity `gamma_epsilon` in (6.4);
2. an integrated non-equilibrium Poincare mass, because the core local-product contraction proof naturally contains an exponent of the form
   \[
   \int \gamma_G(\mu_s)\,ds
   \tag{7.1}
   \]
   before replacing it by a global infimum.

The second formulation may tolerate an early `gamma(mu_t)≈1/t` tree phase: its integral grows logarithmically instead of being destroyed by the smallest early-time value.

**OPEN obligation:** derive a deterministic cutoff theorem directly from a mixing-window or integrated information quantity, then verify that quantity without using the already-known cutoff theorem for each random ensemble. Using known cutoff to infer the needed information concentration would be circular for Problem 2.1.

# 8. Move #19 — exact finite algorithm for the local Poincare quantity

The same non-equilibrium quantity admits a completely explicit finite-dimensional representation. This turns the surviving route into a concrete spectral object rather than a verbal condition.

Let `K` be any finite Markov kernel and let `mu` be a strictly positive probability vector. Define

\[
B_\mu:=\operatorname{Diag}(\mu)-\mu\mu^T
\tag{8.1}
\]

and

\[
A_{\mu,K}
:=
\frac12\sum_{x,y}\mu_xK_{xy}
(e_y-e_x)(e_y-e_x)^T.
\tag{8.2}
\]

Then for every real column vector `f`,

\[
\operatorname{Var}_\mu(f)=f^TB_\mu f,
\tag{8.3}
\]

while

\[
\int\Gamma_Kf\,d\mu=f^TA_{\mu,K}f.
\tag{8.4}
\]

Therefore

\[
\boxed{
\gamma_K(\mu)
=
\inf_{f:\,f^TB_\mu f>0}
\frac{f^TA_{\mu,K}f}{f^TB_\mu f},
}
\tag{C003}
\]

namely the smallest positive generalized eigenvalue of the pencil `(A_{mu,K},B_mu)` after quotienting the constant direction.

For a deterministic start `x`,

\[
\mu_t=\delta_x e^{t(K-I)},
\tag{8.5}
\]

so the global and restricted local-product constants are exactly

\[
\gamma_*(x)=\inf_{t>0}\lambda_{\min}^+(A_{\mu_t,K},B_{\mu_t}),
\tag{8.6}
\]

and

\[
\gamma_\varepsilon(x)
=
\inf_{t\in I_\varepsilon}
\lambda_{\min}^+(A_{\mu_t,K},B_{\mu_t}),
\tag{8.7}
\]

where `I_epsilon` is the specified mixing interval.

This is an exact algorithmic reduction. The research difficulty is no longer defining the quantity; it is proving a random-graph lower bound near the mixing window without circularly invoking cutoff.

# 9. Fixed metric: first certified value `M_9=1/9`

To assign a first honest baseline I selected a property already present in one of the nine primary references rather than inventing a post-hoc condition.

Let `P_BL` denote the **covered-expander entropic spectral hypothesis in Bordenave--Lacoin [22]**, i.e. the deterministic hypotheses under which their theorem proves that the lower entropic bound is sharp and yields cutoff at the entropy time for a finite graph covered by the specified infinite transitive graph.

For the random covered-expander / random-lift application actually developed in [22], the paper proves the needed structural hypotheses with high probability and supplies the deterministic cutoff implication. Thus [22] itself counts under one explicit common candidate property.

I do **not** automatically count [80] or any other reference under `P_BL`: matching a random-regular special case informally is not enough because [80] includes scopes and chain types not yet checked against every `P_BL` hypothesis. Nor do I count varentropy concentration inferred from a known cutoff theorem, because that would be circular for the derandomization target.

Hence the first audited-from-source lower baseline is

\[
\boxed{M_9=1/9.}
\tag{9.1}
\]

The other eight remain **UNKNOWN under this same candidate property**, not zero forever. This is genuine movement from the claim-time `UNMEASURED` state.

# 10. Exact finite self-check

I wrote the finite checker only after the route above produced a theorem worth checking.

Checker:

`artifacts/R19/2026-09-16_22-36-10_UTC__i0110_treeball_localproduct_checker.py`

creation commit:

`9e10ea0ff7c4b0c7a8ee074dfeec11c843c50c42`.

Executed output:

`artifacts/R19/2026-09-16_22-36-10_UTC__i0110_treeball_localproduct_checker.out`

creation commit:

`2f4598501a4242e7a65296db5148a59c3bb6848f`.

The output ends `PASS` and exactly verifies:

1. the nine source reference labels are distinct;
2. the C001 quotient normalization
   \[
   \frac{1/2}{r/32}=\frac{16}{r};
   \]
3. the symbolic Poisson identity
   \[
   \mathbb E[N^2z^N]=(tz+t^2z^2)e^{t(z-1)};
   \]
4. on a rational three-state example, direct variance/energy exactly equal the quadratic forms (8.3)--(8.4):
   \[
   \operatorname{Var}=\frac{601}{400},
   \qquad
   \mathcal E=\frac{109}{40}.
   \]

This is a **self-check of the finite algebra only**. It is not an independent audit and does not certify the random-regular asymptotic exploration theorem by computation.

# 11. Directed R19 -> R20 audit

The newest ready R20 package I found is

`runs/R20/2026-09-16T22-18-29Z_i0100_projected_simplex_minor_7c4f2a.md`.

I independently checked the algebraic core against the preceding exact positive-cone formulation in

`runs/R20/2026-09-16T20-47-17Z_i0100_p421_projection_cone_b3e921.md`.

The earlier formula is

\[
T_p
=
\min\{\mathbf1^Tq:q\ge0,\ q_0=1,\ K_pq=q\}.
\tag{11.1}
\]

Normalize a feasible point by

\[
\nu=\frac q{\mathbf1^Tq}.
\]

Then `nu` is a probability vector, remains in `Ran(K_p)`, and

\[
\nu_0=\frac1{\mathbf1^Tq}.
\]
Conversely any probability vector in the same Fourier subspace with `nu_0>0` rescales to a feasible `q=nu/nu_0`. Therefore

\[
T_p^{-1}
=
\max\{\nu_0:\nu\in\Delta,\ K_p\nu=\nu\},
\tag{11.2}
\]

which is exactly R20's moment-measure formulation after expressing `K_p\nu=\nu` as annihilation of the forbidden Fourier moments. The projected-simplex radial identity follows from writing

\[
0=\nu_0v_0+(1-\nu_0)y,
\qquad y\in\operatorname{conv}\{v_m:m\ne0\},
\]
so the radial parameter is

\[
t=\frac{\nu_0}{1-\nu_0}
\]
and hence

\[
T_p=1+\frac1t.
\]
Finally, with `d=n/2-1`, the real moment equality system has rank at most `d+1`, so standard LP extreme-point theory gives an optimum supported on at most

\[
d+1=\frac n2
\]
frequencies.

Verdict:

`R19-AUDIT-R20-I0100-PROJECTED-SIMPLEX-01 = PASS_ALGEBRAIC_CORE`.

**Scope:** this certifies the algebraic equivalence from R20's already-established cone LP to its probability-measure/projected-simplex formulation and the `<=n/2` basic-support bound. It does **not** independently reexecute the p=421 cyclotomic interval certificate and does **not** audit the asymptotic Paley theta conjecture.

# 12. Failed/closed routes and exact obstructions

- **Uniform bounded degree:** impossible as a nine-family property because [52] has growing random generator count.
- **Reversibility/symmetric support:** impossible because [21] is directed/nonreversible.
- **Diverging tree-like radius:** impossible because [52] has systematic short Abelian relations.
- **Uniform expansion:** too strong for the community regimes [13],[62].
- **Global local-product criterion `gamma_* t_mix -> infinity`:** disproved as a common property by C001--C002 already on [80].
- **Curvature-only route:** neighboring R16 independently found a negative Bakry--Emery test direction on locally tree-like transitive graphs; this agrees with the present diagnosis that early local geometry is the wrong universal invariant.
- **Circular varentropy route:** knowing a random model has cutoff and then invoking an expander theorem to infer information concentration does not derandomize that cutoff proof.

The surviving route is deliberately narrower: remove the early-time contamination and attack a **mixing-window / integrated information criterion**.

# 13. Model/reasoning interface and the historical P26 permission issue

The exposed task/scheduler control surface still provides prompt/title/schedule/timing/enabled controls but **no model selector, no reasoning/thinking-effort selector, and no authenticated runtime-model field**. Therefore `GPT-6 / maximum` remains a requested prompt setting rather than an enforceable or verified runtime configuration here.

To make it enforceable, the product/backend must expose model and reasoning-effort fields in the task schema/update API and return authenticated applied-runtime metadata on runs, or an authorized owner/platform-support control with those fields must migrate/configure the task.

The repository also records the historical P26 error `You cannot modify this task` from one context and later successful P26 edits from an appropriately authorized P/C context. The legitimate workaround is therefore an **authorized owner/admin/platform context that actually has permission**, not task duplication or permission bypass. R19 made no schedule change in this run.

# 14. Claim ledger

## PROVED / VERIFIED

- `R19-I0110-C001`: tree ball of radius `4r` implies `gamma_*(o)<=16/r` for the global local-product constant.
- `R19-I0110-C002`: on fixed-degree random regular graphs, `gamma_*(o)t_mix(o,epsilon)=O_P(1)`; hence the Pedrotti--Salez global-inf criterion is not the common Problem 2.1 property.
- `R19-I0110-C003`: exact generalized-eigenvalue representation (8.1)--(8.7) for the local Poincare constant.
- `M_9=1/9` under the explicit Bordenave--Lacoin covered-expander candidate `P_BL`.
- `R19-AUDIT-R20-I0100-PROJECTED-SIMPLEX-01 = PASS_ALGEBRAIC_CORE` at the stated limited scope.
- exact finite self-check PASS.

## CONDITIONAL / ROUTE

- Restricted mixing-window `gamma_epsilon` may survive across the nine source families; not proved.
- An integrated local-Poincare mass may be the correct deterministic invariant; not yet turned into a cutoff theorem here.
- The common mechanism appears entropic/path-information based; this is diagnosis, not closure.

## DISPROVED AS COMMON-PROPERTY ROUTES

- uniform bounded degree;
- universal reversibility;
- diverging-radius local tree-likeness;
- fixed positive global expansion;
- Pedrotti--Salez global-inf local-product product condition.

## OPEN

- Salez Problem 2.1 itself.
- `M_9`: 1/9 certified, target 9/9.
- deterministic cutoff theorem from a restricted/integrated non-equilibrium Poincare quantity.
- source-by-source verification of that same quantity without circular use of known cutoff.
- P26 plus distinct OTHER-track audits of any future source-closing I0110 theorem.

# 15. Next attack

Do **not** return to the killed global-inf `gamma_*` route.

The next run should keep the common information mechanism but localize it to the actual cutoff window:

1. derive directly from the Pedrotti--Salez contraction argument a deterministic theorem in terms of either
   \[
   \inf_{t\in I_\varepsilon}\gamma_G(\mu_t)
   \]
   or
   \[
   \int_{I_\varepsilon}\gamma_G(\mu_t)\,dt;
   \]
2. test that theorem first on the two structurally opposite source families [80] random regular and [52] random Abelian Cayley;
3. use the generalized-eigenvalue formula C003 to identify what a local weak-limit or Fourier argument must actually bound;
4. only if one **single** property survives both ends should the metric be extended beyond `1/9`.

The conceptual target is to prove that early-time tree geometry can be bad while the **mixing-window information geometry** is uniformly sharp.

# 16. Structured ledger delta

```yaml
ledger_delta:
  track: R19
  source: "Justin Salez, Modern aspects of Markov chains, arXiv:2508.21055v1 (2025), Problem 2.1 / I0110"
  target: "one structural property a.s. satisfied by the nine cited random graph models and deterministically implying cutoff"
  metric: "M_9 = number among Salez refs [80,16,14,21,13,61,22,52,62] covered by one common explicitly proved property"
  before: "UNMEASURED"
  after: "1/9 CERTIFIED"
  status: "PARTIAL / SOURCE OPEN"
  unchanged_count_before: "UNKNOWN (first I0110 research run)"
  unchanged_count_after: 0
  tried_moves: [2, 12, 19]
  exact_evidence:
    report: "runs/R19/2026-09-16_22-36-10_UTC__i0110-treeball-localproduct.md"
    checker: "artifacts/R19/2026-09-16_22-36-10_UTC__i0110_treeball_localproduct_checker.py"
    checker_commit: "9e10ea0ff7c4b0c7a8ee074dfeec11c843c50c42"
    checker_output: "artifacts/R19/2026-09-16_22-36-10_UTC__i0110_treeball_localproduct_checker.out"
    checker_output_commit: "2f4598501a4242e7a65296db5148a59c3bb6848f"
  new_claims:
    - "R19-I0110-C001 PROVED: tree-ball upper bound gamma_* <= 16/r"
    - "R19-I0110-C002 PROVED: global local-product criterion fails w.h.p. on fixed-d random regular graphs"
    - "R19-I0110-C003 PROVED: exact generalized-eigenvalue formula for gamma_K(mu)"
  common_property_baseline:
    property: "Bordenave-Lacoin covered-expander entropic spectral hypothesis P_BL"
    counted_refs: [22]
    unresolved_under_same_property: [80,16,14,21,13,61,52,62]
  failed_routes:
    - "uniform bounded degree"
    - "reversibility"
    - "diverging tree-like radius"
    - "uniform expansion"
    - "global-inf local product gamma_* t_mix -> infinity"
  audit_ids:
    p26: "NONE for I0110"
    other: "NONE for I0110"
    directed_peer_audit: "R19-AUDIT-R20-I0100-PROJECTED-SIMPLEX-01=PASS_ALGEBRAIC_CORE (limited scope)"
  remaining_obligation: "prove a restricted/integrated mixing-window information cutoff criterion and verify the SAME property noncircularly across the nine ensembles"
  prior_target_handoff: "I0084 preserved; no seventh unchanged I0084 run"
```

**NO SOURCE CLOSURE CLAIM.**
