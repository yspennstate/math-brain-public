Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** Primary metric **no movement**: `L_6 >= 0 -> L_6 >= 0` (third consecutive unchanged run); substantive route movement: an explicit positive-first-moment profile whose **full feasible homogeneous two-replica Hessian is strictly negative** was found and certified, with stability interval `(3 sqrt(10)-8)/13 < alpha <= 1/3`; methods tried: **B3 / B12 / B15**.

# HARD7-06 run 3 — a minority-profile deformation repairs the raw-count local second-moment instability

Status: **PARTIAL / Chang--Kolhe--Sohn k=3 sharpness conjecture remains OPEN under bounded current-literature review.**

Repository / branch: `yspennstate/math-open-problems` / `master`.

Canonical ownership remains `operations/claims/CKS-2024-RREG-HYPER2COL-K3.md`, owner `HARD7-06`. I resumed the exact admitted target and the two previous checkpoints. Run 1 proved that the ordinary balanced-coloring second moment is locally unstable at independent overlap when `d=6`; run 2 classified the one-dimensional symmetric raw-count landscape and proved that the correlated saddles are global maxima. This run **does not recompute that landscape**. It changes the counted object.

Exact finite-core artifacts for this run:

- `artifacts/hard7_2026-09-18/HARD7-06/k3_profile_tilt_local_hessian_exact.py`, creation commit `f4641b044596538074842ddc7f2c58ca7392253b`;
- executed output `artifacts/hard7_2026-09-18/HARD7-06/k3_profile_tilt_local_hessian_exact.out`, creation commit `2d9f6b699bdea06373af06feee93d818890469c8`, ending `ALL_EXACT_CHECKS_PASS`.

The script uses Python `Fraction` and integer arithmetic only. It is a self-check of the finite algebraic core, not a certificate of the asymptotic source conjecture.

## 1. Continuity, ownership, exclusions, and current literature

I reread the controlling files `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; root `POSTED.md`, `RESULTS.md`, `QUEUE.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the current HARD7-06 claim; both previous HARD7-06 reports; and neighboring random-CSP material including R03's terminal F0097 handoff. Repository searches by the current title/model recover the HARD7-06 claim and reports and other tracks explicitly treating the claim as HARD7-06-owned. No release, duplicate claim, or posted/settled equivalent was found.

The initially suggested random 3-SAT threshold remains unavailable to this track: the repository's canonical F0097 history belongs to R03 and has a separate lifecycle/handoff. I therefore do not duplicate it.

The primary source remains:

Evan Chang, Neel Kolhe, Youngtak Sohn, *Upper Bounds on the 2-Colorability Threshold of Random d-Regular k-Uniform Hypergraphs for k >= 3*, APPROX/RANDOM 2024, LIPIcs 317, Article 47, DOI `10.4230/LIPIcs.APPROX/RANDOM.2024.47`, full version arXiv:2308.02075.

A fresh bounded source/current-literature check dated 2026-09-18 UTC / 2026-09-19 local reread the primary proceedings paper and searched its exact title/arXiv identifier together with `random regular hypergraph 2-colorability k=3 d=6 threshold` and `random regular NAE-SAT k=3 threshold`. The source itself states that locating the satisfiability threshold at small fixed `k>=3` remains open and that its explicit upper threshold is conjectured sharp. I found no later source in this bounded search proving the exact `k=3,d=6` lower side. This is bounded negative evidence, not proof of worldwide openness.

I also checked the nearby large-`k` cluster technology, in particular Danny Nam, Allan Sly, Youngtak Sohn, *One-Step Replica Symmetry Breaking of Random Regular NAE-SAT II*, Commun. Math. Phys. 405 (2024), article 61, DOI `10.1007/s00220-023-04868-6`. That work uses cluster-level counts, small-subgraph conditioning, Doob martingales and Fourier analysis for sufficiently large `k`; it is not a small-`k=3` hypergraph-2-coloring lower-bound theorem. Bounded searches for the exact phrases `minority incidence`, `profile random regular hypergraph 2-coloring second moment`, and `judicious random regular hypergraph 2-coloring` did not locate the exact profile/Hessian calculation below. I therefore label the calculation **new to this track under a bounded prior-art screen**, not globally novel.

The frozen source metric remains

\[
L_6:=\sup\left\{L\in[0,1]:
\liminf_{n\to\infty}
\Pr(H_{n,6,3}\ {\rm is\ 2\!-\!colorable})\ge L\right\},
\]

with the source's uniformly random simple 6-regular 3-uniform model and admissible `n` fixed. No source-model probability lower bound is proved below, hence

\[
\boxed{L_6\ge0\quad\longrightarrow\quad L_6\ge0.}
\]

## 2. B12 — the conserved quantity kills every linear minority weight

Fix a proper 2-coloring `sigma` of a 6-regular 3-uniform hypergraph. For a vertex `v`, define

\[
R_v(\sigma):=\#\{e\ni v:\ v \text{ is the unique minority color on }e\}.
\]

Every proper 3-edge has color pattern `2+1`, hence contributes **exactly one** minority incidence. Since the number of edges is `nd/3=2n`,

\[
\boxed{\sum_v R_v(\sigma)=2n.}\tag{2.1}
\]

Thus any linear exponential reweighting
\[
\exp\{\lambda\sum_v R_v\}
\]
is the constant `exp(2 lambda n)` on the set of proper colorings. It cannot alter the overlap landscape at all. This disposes of the most obvious one-parameter repair before spending a run optimizing it.

The conservation law instead suggests changing category from a scalar weight to a **profile-conditioned count**.

## 3. B15 — break the raw ensemble by conditioning the minority-incidence profile

For a balanced coloring, let `p=(p_0,...,p_6)` be the empirical law of `R_v`, taken identically in the two color classes. Equation (2.1) imposes

\[
\sum_{r=0}^6p_r=1,\qquad \sum_{r=0}^6r p_r=2.\tag{3.1}
\]

In the ordinary first-moment saddle the role profile is

\[
q_r=\binom6r\left(\frac13\right)^r
\left(\frac23\right)^{6-r}
=\frac{(64,192,240,160,60,12,1)_r}{729},\tag{3.2}
\]
with mean `2` and variance `4/3`.

Consider the mean-preserving deformation

\[
\boxed{p_\alpha=(1-\alpha)q+\alpha\delta_2,\qquad 0\le\alpha<1.}\tag{3.3}
\]

It preserves color symmetry and the source constraints, but reduces local minority-role fluctuations:

\[
\operatorname{Var}_{p_\alpha}(R)
=(1-\alpha)\frac43.\tag{3.4}
\]

This is not a change of the random hypergraph model. It changes only the subset of proper colorings that is counted.

### 3.1 Exact first-moment exponent

Work first in the standard 6-regular configuration model. For a fixed balanced coloring and a fixed profile, mark at each vertex the `R_v` incident half-edges on which that vertex is to be the minority. There are `n` minority `+` half-edges, `n` minority `-` half-edges, and `2n` majority half-edges of each color. A role-compatible proper edge partition is obtained by pairing the `2n` majority half-edges of each sign and bijecting the opposite-sign minority half-edges to those pairs. Therefore the matching contribution has exponential rate `log(1/81)`, while the balanced color choice contributes `log 2`.

For an exact type `p`, Stirling's formula gives

\[
\frac1n\log \mathbb E Z_p
\longrightarrow
s_1(p):=
H(p)+\sum_{r=0}^6p_r\log\binom6r+\log\frac2{81}.\tag{3.5}
\]

Using `(3.1)` and `(3.2)`,

\[
\boxed{s_1(p)=\log\frac98-D(p\|q).}\tag{3.6}
\]

In particular the raw profile `q` has rate `log(9/8)>0`.

Along `(3.3)`, relative entropy is convex in `alpha`, has value `0` and derivative `0` at `alpha=0`, hence is nondecreasing for `alpha>=0`. It is therefore enough to certify positivity at one right endpoint.

At `alpha=1/3`,

\[
p_{1/3}=
\frac{(128,384,1209,320,120,24,2)}{2187}.\tag{3.7}
\]

Multiplying `(3.5)` by `2187`, positivity is exactly equivalent to the integer inequality

\[
54^{2187}\prod_{r=0}^6\binom6r^{n_r}
>
\prod_{r=0}^6 n_r^{\,n_r},
\qquad
(n_0,\ldots,n_6)=(128,384,1209,320,120,24,2).\tag{3.8}
\]

The archived checker evaluates this inequality with exact integers and returns PASS. Hence

\[
\boxed{s_1(p_\alpha)>0\qquad(0\le\alpha\le1/3).}\tag{3.9}
\]

This is an annealed exponential-count statement in the configuration model. It is **not** a second-moment bound and not a source probability bound.

## 4. B3 — prove a stronger local statement than the color-overlap curvature

Run 1 only tested one color-overlap direction and found the raw count unstable. A useful reweighted object needs to survive **every homogeneous feasible pair perturbation**, including coupled role and color modes. I therefore ask for the stronger local property: strict negative definiteness of the full two-replica Bethe Hessian on the feasible tangent space.

### 4.1 One-replica port Hilbert space

At a half-edge, let

- `s in {+1,-1}` be the vertex color,
- `m in {0,1}` indicate whether this endpoint is the unique minority endpoint of its edge.

For the single-replica port law, `s` is uniform, `P(m=1)=1/3`, and they are independent. A centered basis is

\[
e=3m-1,\qquad b=s,\qquad c=s(3m-1),\tag{4.1}
\]
with Gram matrix

\[
G=\operatorname{diag}(2,1,2).\tag{4.2}
\]

For a vertex with profile `p_alpha`, two distinct incident ports have role correlation

\[
\kappa_\alpha
=
\frac{\operatorname{Cov}(m_i,m_j)}{\operatorname{Var}(m_i)}
=
\frac{3\operatorname{Var}(R)-4}{20}
=
-\frac{\alpha}{5}.\tag{4.3}
\]

Color is identical on all six ports of the same vertex. Consequently the port-to-port conditional operator on the centered space is

\[
\boxed{T_v=\operatorname{diag}(\kappa_\alpha,1,\kappa_\alpha).}\tag{4.4}
\]

For a proper 3-edge, the six nonmonochromatic sign triples are equiprobable. Exact enumeration in the checker gives

\[
\boxed{
T_f=
\begin{pmatrix}
-\frac12&0&0\\
0&-\frac13&-\frac23\\
0&-\frac13&\frac56
\end{pmatrix},
}\tag{4.5}
\]
which is self-adjoint in the `G` inner product: `G T_f=(G T_f)^T`.

### 4.2 The lift lemma

Let a single-replica node have `r` exchangeable ports with centered port conditional operator `T`. Let `K` be a first-order two-replica coupling kernel at one port, with each replica marginal fixed. If the same `K` is prescribed at every port, the minimum quadratic `chi^2` norm of a node-level lift is

\[
\boxed{
r\,\langle K,\,[I+(r-1)T\otimes T]^{-1}K\rangle,
}\tag{4.6}
\]
whenever the inverse is taken on the range if necessary.

Proof: for a port kernel `u`, the symmetric node tangent is the sum of its `r` port copies. The covariance between two different copies is exactly
`<u,(T\otimes T)u>`. Hence its squared norm is

\[
r\langle u,[I+(r-1)T\otimes T]u\rangle.
\]

Its one-port conditional expectation is
`[I+(r-1)T\otimes T]u`. Solving this equal to `K` gives `(4.6)`. Orthogonal projection shows this symmetric lift is the minimum-norm lift. This is the entire local linear algebra used below.

### 4.3 Pair entropy and the feasible Hessian

For the regular factor graph with variable degree `d=6` and factor degree `k=3`, the pair Bethe entropy excess over two independent replicas is

\[
\Delta=6I_e-I_v-2I_f,\tag{4.7}
\]
where `I_e,I_v,I_f` are the mutual informations of the pair edge-, variable-, and factor-local laws.

For a perturbation `epsilon K`, mutual information is
`epsilon^2 ||K||^2/2+O(epsilon^3)`. Applying `(4.6)` at variables and factors, the sign of the second-order term is the sign of

\[
\langle K,\,[I-L_v^{-1}-L_f^{-1}]K\rangle,\tag{4.8}
\]
where

\[
L_v=I+5T_v\otimes T_v,\qquad
L_f=I+2T_f\otimes T_f.\tag{4.9}
\]

The omitted prefactor is the positive number `d/2=3`.

The factor hard constraint makes `L_f` singular. Exact row reduction gives

\[
\operatorname{rank}L_f=5,\tag{4.10}
\]
so a feasible homogeneous tangent must lie in `Ran L_f`; this is why testing only the old color direction was insufficient.

Choose the five pivot columns `(0,1,3,4,5)` of `L_f` as a rational range basis `R`. Let `X` be the corresponding five coordinate columns, so `L_f X=R`. In these range coordinates the sign-relevant quadratic matrix is

\[
B_\alpha
=R^TG^{\otimes2}
\left(R-L_v^{-1}R-X\right).\tag{4.11}
\]

Since `kappa_alpha=-alpha/5`, direct rational reduction gives a diagonal `3+2` block form. The first three entries are

\[
B_{00}=\frac{3(\alpha^2-10)}{\alpha^2+5},\tag{4.12}
\]

\[
B_{11}=B_{22}
=
\frac{4(3\alpha^3+5\alpha^2+10\alpha+30)}
{9(\alpha-1)(\alpha^2+5)}.\tag{4.13}
\]

For the final `2x2` block,

\[
B_{33}=
\frac{203\alpha^3-107\alpha^2+535\alpha-55}
{486(\alpha-1)(\alpha^2+5)},\tag{4.14}
\]

\[
B_{34}=B_{43}
=
-\frac{2(11\alpha^3-59\alpha^2-245\alpha+5)}
{243(\alpha-1)(\alpha^2+5)},\tag{4.15}
\]

\[
B_{44}=
\frac{4(79\alpha^3-31\alpha^2+20\alpha+220)}
{243(\alpha-1)(\alpha^2+5)}.\tag{4.16}
\]

The determinant of this final block collapses to

\[
\boxed{
\det B_{\{3,4\}}
=
\frac{10(13\alpha^2+16\alpha-2)}
{243(\alpha^2+5)}.
}\tag{4.17}
\]

For `0<=alpha<=1/3`, `(4.12)` is negative, `(4.13)` is negative, and `(4.16)` is negative. Thus the final block, and hence all of `B_alpha`, is strictly negative definite exactly when

\[
13\alpha^2+16\alpha-2>0.
\]

The positive root is

\[
\boxed{\alpha_c=\frac{3\sqrt{10}-8}{13}.}\tag{4.18}
\]

Therefore

\[
\boxed{
\alpha_c<\alpha\le\frac13
\quad\Longrightarrow\quad
s_1(p_\alpha)>0
\ \text{and}\ 
B_\alpha\prec0.
}\tag{4.19}
\]

This is the main route result of the run: there is a nonempty interval of profile-conditioned counts with positive annealed exponential rate and a strict local maximum at independent coupling in the **entire five-dimensional feasible homogeneous pair tangent space**.

### 4.4 An exact rational witness

Take `alpha=1/4`. Then

\[
p_{1/4}
=\frac{(64,192,483,160,60,12,1)}{972},\qquad
\operatorname{Var}(R)=1,\qquad
\kappa=-\frac1{20}.\tag{4.20}
\]

For `n` divisible by `1944`, this profile is an exact balanced color-class type. The first-moment positivity becomes the exact integer inequality

\[
24^{972}\prod_{r=0}^6\binom6r^{n_r}
>
\prod_{r=0}^6 n_r^{\,n_r},
\quad
(n_r)=(64,192,483,160,60,12,1),\tag{4.21}
\]
which the checker verifies exactly.

The full feasible Hessian matrix is

\[
B_{1/4}=
\begin{pmatrix}
-\frac{53}{9}&0&0&0&0\\
0&-\frac{2804}{729}&0&0&0\\
0&0&-\frac{2804}{729}&0&0\\
0&0&0&-\frac{535}{13122}&-\frac{850}{6561}\\
0&0&0&-\frac{850}{6561}&-\frac{6380}{6561}
\end{pmatrix}.
\tag{4.22}
\]

The leading principal minors of `-B_{1/4}` are exactly

\[
\frac{53}{9},\quad
\frac{148612}{6561},\quad
\frac{416708048}{4782969},\quad
\frac{111469402840}{31381059609},\quad
\frac{20835402400}{10460353203},
\tag{4.23}
\]
all positive. Sylvester's criterion therefore gives an exact finite certificate that `B_{1/4}` is negative definite. No floating-point sample is used for this claim.

## 5. What the three method moves taught us

### B12 — FIND WHAT IS CONSERVED

Success. Equation `(2.1)` proves that every linear exponential minority-incidence weighting is a fake deformation: it is constant on proper colorings. This prevents a whole class of wasted reweighting attempts and identifies the empirical distribution of `R_v`, not its sum, as the first nontrivial variable.

### B15 — BREAK THE SYMMETRY ON PURPOSE

Success at the route level. Conditioning on `p_alpha` breaks the raw solution ensemble while preserving the source's color symmetry and the exact mean constraint. It induces a **negative** role-port correlation `kappa=-alpha/5`, which is precisely the lever absent from the raw count.

### B3 — PROVE SOMETHING STRONGER

Success locally. Instead of only asking whether the old color-overlap curvature can be flipped, I required negativity on every homogeneous pair perturbation consistent with the factor constraint. The exact five-dimensional calculation produces `(4.19)`.

## 6. Why this is still not movement of `L_6`

The result above is local and annealed. Four major obligations remain before any source-probability lower bound is justified:

1. **Global pair variational control.** `B_alpha\prec0` proves only local dominance of independent coupling. A distant overlap/profile saddle could still make the second moment exponentially larger.
2. **Subexponential prefactors and lattice types.** One must control the exact type sums, not only their exponential rate.
3. **Small-subgraph fluctuations / conditioning.** Even a bounded second-moment ratio in the configuration model would naturally lead to only positive probability unless cycle fluctuations are treated; a source `L_6=1` result needs substantially more.
4. **Transfer to the source simple model.** The source is the uniformly random simple regular hypergraph. The configuration model is a proof vehicle; any final probability statement must condition on simplicity correctly.

Accordingly I do **not** claim `L_6>0`, do not call the source solved, and do not call a finite profile witness a proof of asymptotic 2-colorability.

The honest frozen metric remains

\[
\boxed{L_6\ge0\to L_6\ge0.}
\]

## 7. Stagnation trigger and next-run obligation

This is the **third consecutive HARD7-06 run with no movement in the frozen source metric**:

- run 1: `L_6>=0 -> L_6>=0`;
- run 2: `L_6>=0 -> L_6>=0`;
- run 3: `L_6>=0 -> L_6>=0`.

Therefore the controlling section-I rule triggers **on the next invocation**. The next run must be a thinking/stuck report rather than another theorem claim. It must record:

- the exact blocking statement;
- every route tried and its precise failure point;
- what a source proof needs that no route yet provides;
- the simplest unproved special case;
- the nearest solved analogue and the ingredient it has that this target lacks;

and then choose exactly one permitted recovery action and a fresh section-B triple. The most natural simplest special case exposed by this run is the global two-replica variational problem for the single exact witness `p_{1/4}`: prove independent coupling is the unique global maximizer, or find an exact counter-saddle.

No target rotation occurs in this run because this is the first section-I trigger, not a third stuck-recovery cycle.

## 8. Model / scheduler capability statement

The requested `GPT-6 / maximum` setting remains prompt text only. The exposed scheduler controls title, prompt, schedule, timing mode and enablement; it exposes no model-family selector, no reasoning-effort selector and no guaranteed execution duration. The actual model visible to this run is **GPT-5.6 Sol**; reasoning effort is **UNVERIFIED**. I do not claim GPT-6 maximum ran.

Repository policy records that modification permissions can differ by native task/context. Historical probes for P26/P01/P03 returned `You cannot modify this task`, while later repository reconciliation records successful updates for some IDs from a different authorized context. The lawful workaround for any still-denied task is its owning/authorized task-management context or platform support, not a duplicate schedule, permission bypass, or repository edit masquerading as a native scheduler setting.

No schedule, email, Drive, permission, public-posting, shared-root, or peer-track state was changed in this run.

## 9. Structured ledger delta for the designated shared maintainer

```yaml
ledger_delta:
  worker: HARD7-06
  canonical_claim: CKS-2024-RREG-HYPER2COL-K3
  status: PARTIAL
  frozen_metric: L_6
  before: ">= 0"
  after: ">= 0"
  movement: "no movement; third consecutive"
  methods: [B3, B12, B15]
  auxiliary_result:
    profile_family: "p_alpha=(1-alpha)Bin(6,1/3)+alpha delta_2"
    positive_first_moment: "0 <= alpha <= 1/3"
    full_feasible_local_pair_stability: "(3 sqrt(10)-8)/13 < alpha <= 1/3"
    exact_witness: "alpha=1/4"
  next_action: "section-I stuck/thinking run; simplest case = global pair variational problem for p_{1/4}"
```

Shared root ledgers were not edited by HARD7-06; this delta is for the designated reconciler.
