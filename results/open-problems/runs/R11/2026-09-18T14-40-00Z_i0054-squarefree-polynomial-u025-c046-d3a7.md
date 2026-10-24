Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested in prompt text, but the exposed scheduler/runtime still has no binding model-family selector, no reasoning-effort selector, no guaranteed-duration control, and no authenticated completed-run routing telemetry, so GPT-6 / maximum is not verified or claimed. Metric movement: `45 -> 46` distinct nontrivial discrete model classes with complete author-side proofs of the frozen CTCS(infinity) limit. Actual section-B moves: **#1, #16, #24**.

# R11 / I0054 — U025 squarefree finite-field factor compiler and C046 binary-polynomial factor fragmentation

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Track: R11, CLOSABLE OUTSIDE.  
Source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, Open Problem 18.  
Source-level campaign status after this run: **PARTIAL, not CLOSED**.  
New author-side claims: `R11-I0054-U025 = PROVED_AUTHOR_SIDE`; `R11-I0054-C046 = PROVED_AUTHOR_SIDE under frozen equivalence`.

## 1. Continuity, source, ownership, and current literature

I continued from

`runs/R11/2026-09-18T13-40-00Z_i0054-gauss-quadrature-u024-c045-a51e.md`

rather than restarting. That report proved U024/C045, moved the frozen metric `44 -> 45`, and prescribed the nonrepeating moves `#1/#16/#24`; those are the moves actually used here.

Before new research I reread or recovered the current control state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/I0054.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the current owner directive;
- the newest R11 report and prior R11 finite-field/permutation/hypergeometric/log-assembly routes needed to avoid duplication;
- the newest neighboring P13 state, which is now the distinct C0021 revealment problem and does not own or reopen I0054;
- current repository searches for I0054 ownership, prior attempts, deterministic root-degree witnesses, and the required audit identifiers.

The canonical I0054 file still assigns the provisional reservation to R11 and still says `PENDING_ADMISSION, not READY`. `POSTED.md` does not record Open Problem 18 as posted or settled. R11's old planar self-avoiding-walk route remains retired with immutable history and was not touched.

I rechecked the actual v3 source PDF. Printed page 58 states:

> **Open Problem 18.** Are there superficially different discrete models whose limit is the same CTCS(infinity)?

and immediately asks whether the source's subordinator-approximation mechanism can arise in another discrete tree model. The same source, and Aldous--Janson Part III (arXiv:2412.09655), formalize CTCS(infinity) through consistent exchangeable partition restrictions. I therefore preserve the stronger frozen target used throughout this R11 chain: convergence of the **complete partition-valued cadlag path** on every fixed restriction in Skorokhod `J_1`, followed by convergence in the summable projective finite-restriction path topology. A root split, tagged fragment, or one-time marginal is not enough.

Fresh dated searches on 2026-09-18 found the same nearby 2026 beta-splitting work as the preceding runs: Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320, on homogeneous fragmentations/subordinators and a height problem; Heng Ma, arXiv:2609.14329, resolving the distinct Aldous--Janson Open Problem 4; and Heng Ma, arXiv:2609.14325, on separation/clade dynamics. I found no announcement resolving exact Open Problem 18.

For the new algebraic category I also searched combinations of `finite field polynomial factorization`, `irreducible factors`, `random permutation cycles`, `logarithmic combinatorial structures`, `CTCS`, and `critical beta-splitting`. The polynomial/permutation analogy is classical prior art: Arratia--Barbour--Tavare studied random polynomials over finite fields and showed large irreducible factors are close to large permutation cycles; their monograph on logarithmic combinatorial structures explicitly includes finite-field polynomials, permutations, and mappings. Elboim--Gorodetsky later obtained uniform estimates for polynomial almost-prime counts and permutation-cycle comparisons. None of those classical ingredients is claimed as new. The bounded search did not locate the recursive factor-block fragmentation below or a claim that it answers Open Problem 18. This is negative evidence only, **not** a worldwide novelty certificate.

A current repository audit search still recovers only older scoped R10 passes on earlier C00x/U00x pieces. It does **not** recover a present-package `P26-AUDIT-R11-I0054` end-to-end PASS plus a second independent OTHER-track end-to-end PASS. Therefore no source-level closure is claimed.

## 2. Idea before code; counterexample-first check; the three moves

The previous run reduced one family to polynomial quadrature. Rather than make another phase rule, move #1 changes category completely: from paintboxes/quadrature to **factorization of polynomials over finite fields**.

The first, deliberately overbroad attempt was to use an unconditioned random squarefree polynomial and let its irreducible factors be the children. This is the wrong scale. The number of irreducible factors is logarithmic, and the classical polynomial/permutation analogy says the visible factor partition is Ewens/permutation-like rather than a rare binary tangent. In particular, higher-way visible factor refinements survive instead of disappearing at the CTCS first-order scale. This failed route is useful: a proof must force the factor partition into the rare-separation regime.

The repair is to condition on a **fixed number of irreducible factors**, exactly as one conditions on a fixed component count in a logarithmic assembly, and then accelerate by the exact two-label separation probability.

The actual moves were:

- **#1 — change the category.** Replace graphs, urns, permutations and Bernoulli phases by squarefree polynomial factorization over a finite field. The tree children are factor blocks.
- **#16 — compute every small case and stare at the sequence.** Exact enumeration over `F_2` gave
  `I_2(1..14) = 2,1,2,3,6,9,18,30,56,99,186,335,630,1161`.
  Conditioning on six distinct irreducible factors is impossible below degree 14; at degree 14 there are exactly three squarefree polynomials and every one has factor-degree multiset `(1,1,2,3,3,4)`. This exposed a clean finite root witness.
- **#24 — find the extremal object.** I chose the smallest field `F_2`, rather than taking `q -> infinity` where polynomial factors become visibly permutation-like. At `q=2` the arithmetic correction to the leading `q^m/m` irreducible count is largest in practical finite cases; nevertheless its generating series is analytic strictly beyond the dominant singularity. Thus the CTCS mechanism does not depend on a large-field approximation.

I first checked a more decorated Frobenius-orbit labelled assembly, then strengthened the route to the actual squarefree-polynomial factorization below. The earlier same-run Frobenius checker is retained as an exploratory supporting artifact but is **not** counted as a second model and is not needed for C046.

## 3. Finite-field input: irreducible counts have one logarithmic singularity

Let `I_q(m)` denote the number of monic irreducible polynomials of degree `m` over `F_q`. The classical formula is

\[
I_q(m)=\frac1m\sum_{d\mid m}\mu(d)q^{m/d}.
\tag{3.1}
\]

Define

\[
C_q(z)=\sum_{m\ge1}I_q(m)z^m.
\tag{3.2}
\]

The `d=1` contribution in (3.1) is `q^m/m`, so

\[
\boxed{
C_q(z)=\log\frac1{1-qz}+H_q(z),
}
\tag{3.3}
\]

where `H_q` is analytic in `|z|<q^{-1/2}`. Indeed

\[
\left|I_q(m)-\frac{q^m}{m}\right|
\le \frac1m\sum_{\substack{d\mid m\\ d\ge2}}q^{m/d}
\le q^{m/2}
\]

up to the harmless divisor-count factor, so the correction has radius strictly larger than `rho=1/q`.

For every fixed `n>=1`, put

\[
D_{q,n}(z)
:=\sum_{m\ge1}I_q(m)(m)_{\underline n}z^m
=z^n C_q^{(n)}(z).
\tag{3.4}
\]

Then as `z -> rho=1/q` in a Delta-domain,

\[
\boxed{
D_{q,n}(z)
\sim (n-1)!(1-qz)^{-n}.
}
\tag{3.5}
\]

The point of (3.3)--(3.5) is that finite-field arithmetic changes only an analytic remainder; the singular part is exactly the logarithmic component law needed for the beta kernel.

## 4. Squarefree polynomials with a fixed number of factors

Let `F_q(u,z)` be the ordinary generating function for squarefree monic polynomials, where `u` marks the number of irreducible factors:

\[
\boxed{
F_q(u,z)
=\prod_{m\ge1}(1+u z^m)^{I_q(m)}.
}
\tag{4.1}
\]

Taking logarithms,

\[
\log F_q(u,z)
=\sum_{\ell\ge1}\frac{(-1)^{\ell+1}}{\ell}
 u^\ell C_q(z^\ell).
\tag{4.2}
\]

For every `ell>=2`, `C_q(z^ell)` is analytic at `z=rho`. Hence

\[
F_q(u,z)=e^{uC_q(z)}G_q(u,z),
\tag{4.3}
\]

where `G_q` is analytic near `(u,z)=(0,rho)`, with `G_q(u,z)=1+O(u^2)`. For fixed `R>=2`, if

\[
Z_{N,R}^{(q)}
=[u^Rz^N]F_q(u,z),
\]

then standard logarithmic transfer gives

\[
\boxed{
Z_{N,R}^{(q)}
\sim
q^N\frac{(\log N)^{R-1}}{N(R-1)!}.
}
\tag{4.4}
\]

This is the number of squarefree monic degree-`N` polynomials over `F_q` having exactly `R` distinct irreducible factors.

## 5. The visible factor-partition law

Fix such a polynomial

\[
f=f_1\cdots f_R,
\qquad d_j=\deg f_j,
\qquad \sum_jd_j=N.
\]

After sampling `f`, assign the leaf labels `[N]` uniformly to the `R` factor boxes with capacities `d_1,...,d_R`. Equivalently, choose a uniform bijection of `[N]` to `N` abstract slots grouped into factor boxes of those sizes and then forget the slot order. This makes the induced factor partition of `[N]` exchangeable.

For a specified visible set partition

\[
\pi=\{B_1,\ldots,B_r\},
\qquad |B_a|=n_a,
\qquad b=\sum_an_a,
\]

the conditional probability given the factor degrees is exactly

\[
\boxed{
\Pr(\pi\mid d_1,\ldots,d_R)
=\frac1{(N)_{\underline b}}
\sum_{\phi:[r]\hookrightarrow[R]}
\prod_{a=1}^r(d_{\phi(a)})_{\underline{n_a}}.
}
\tag{5.1}
\]

The injection is essential: different visible blocks must lie in different irreducible factors.

### Marked-factor generating function

For each irreducible polynomial `g` let `d(g)=deg g`. Introduce marker variables `t_1,...,t_r`:

\[
\mathcal F_q(u,z;\mathbf t)
=
\prod_g
\left[
1+uz^{d(g)}
\left(1+\sum_{a=1}^r
 t_a(d(g))_{\underline{n_a}}
\right)
\right].
\tag{5.2}
\]

Then

\[
H_{N,R}(\mathbf n)
:=[u^Rz^Nt_1\cdots t_r]\mathcal F_q
\tag{5.3}
\]

is exactly the numerator obtained by summing the injection weight in (5.1) over all conditioned squarefree polynomials.

The dominant singular term in (5.3) is

\[
\boxed{
\frac{C_q(z)^{R-r}}{(R-r)!}
\prod_{a=1}^rD_{q,n_a}(z).
}
\tag{5.4}
\]

Here is the point that makes (5.4) rigorous. If two marker derivatives try to use the same irreducible factor, the resulting diagonal series contains `z^{2d(g)}` (or a higher power), for example

\[
\sum_g
(d(g))_{\underline{n_a}}
(d(g))_{\underline{n_c}}z^{2d(g)}.
\]

Such a series is analytic at `z=1/q`, because its radius is at least `q^{-1/2}>q^{-1}`. The same is true for every correction caused by excluding an already marked factor from the unmarked squarefree product. Inclusion--exclusion over equality patterns of marked factors therefore leaves (5.4) as the unique dominant singular contribution. This is exactly where squarefreeness matters and exactly why the classical polynomial/permutation analogy is strong enough here.

Using (3.3)--(3.5) and logarithmic transfer,

\[
H_{N,R}(\mathbf n)
\sim
q^N
\frac{N^{b-1}}{(b-1)!}
\frac{(\log N)^{R-r}}{(R-r)!}
\prod_{a=1}^r(n_a-1)!.
\tag{5.5}
\]

Divide (5.5) by `(N)_b Z_{N,R}^{(q)}` and use `(N)_b~N^b`. We obtain the structural restriction law

\[
\boxed{
\Pr_N(\pi)
\sim
\frac{(R-1)!}{(R-r)!}
\frac{\prod_a(n_a-1)!}{(b-1)!}
(\log N)^{1-r}.
}
\tag{5.6}
\]

This is the same rare-partition law as the labelled logarithmic-assembly compiler U015, but it is proved here for **actual squarefree polynomial factorization** rather than for an artificially labelled SET assembly.

### U025 — squarefree finite-field factor compiler

For every fixed prime power `q` and fixed `R>=2`, sample a squarefree monic degree-`N` polynomial over `F_q` conditioned to have exactly `R` distinct irreducible factors, then uniformly allocate `[N]` to its factor boxes according to factor degrees. For every fixed visible partition `pi`, its restriction probability satisfies (5.6).

In particular, for a specified binary support of sizes `i,j`,

\[
\boxed{
\Pr_N(i|j)
\sim\frac{R-1}{\log N}B(i,j),
\qquad
B(i,j)=\frac{(i-1)!(j-1)!}{(i+j-1)!},
}
\tag{5.7}
\]

while every specified `r>=3` visible refinement is smaller by the factor `(log N)^{2-r}` after pair normalization.

This proves `R11-I0054-U025 = PROVED_AUTHOR_SIDE`. The finite-field factor-count machinery itself is classical prior art; the claim here is the complete marked restriction asymptotic in the form needed for the CTCS compiler. External novelty remains unverified.

## 6. C046 — six-factor squarefree binary-polynomial fragmentation

Now take the extremal smallest field `q=2` and fix

\[
R=6.
\]

For every `N>=14`, let `P_N` be uniform over squarefree monic degree-`N` polynomials in `F_2[x]` having exactly six irreducible factors. This conditioning class is nonempty for every `N>=14`: use the two degree-one irreducibles, the unique degree-two irreducible, the two degree-three irreducibles, and one irreducible of degree `N-10>=4`.

Given `P_N=f_1\cdots f_6`, uniformly allocate the `N` leaf labels to the six factor boxes with capacities `deg f_1,...,deg f_6`; call the resulting random six-block partition `Xi_N`.

Let

\[
p_{11,N}:=\Pr\{1,2\text{ lie in different blocks of }\Xi_N\},
\qquad
\lambda_N=p_{11,N}^{-1}.
\tag{6.1}
\]

By U025,

\[
\boxed{
p_{11,N}\sim\frac5{\log N},
\qquad
\lambda_N\sim\frac{\log N}{5}.
}
\tag{6.2}
\]

Set

\[
\delta_N
=\min\{N^{-2},p_{11,N}/2\},
\qquad
a_N=\delta_N\lambda_N\le\frac12.
\tag{6.3}
\]

C046 starts from the one-block partition `[N]`. At each raw step, independently for every current nonsingleton block `B`:

1. attempt with probability `a_N`;
2. on an attempt draw a fresh independent copy of `Xi_N`;
3. replace `B` by its nonempty intersections with the six blocks of `Xi_N`;
4. if all labels of `B` land in one factor block, the attempt is invisible;
5. process children only from the next raw step.

One raw step has physical length `delta_N`.

This is a finite discrete hierarchy. Every nonsingleton block eventually splits almost surely: choose any pair in it; in every raw step that pair separates with probability exactly `a_Np_{11,N}=delta_N>0`, independently of the past after a fresh proposal. A finite monotone refinement has at most `N-1` proper split events, so the process reaches singletons almost surely.

## 7. Exact hidden-label lumping and the full path limit

Fix `k`. Every visible block lies in one full carrier block. C046's proposal is sampled afresh from the same global-`N` law, independently of carrier size and carrier history. If a proposal refines the full carrier but all visible labels stay in one child, the visible state is unchanged and that child receives the same fresh proposal law at later attempts. Thus hidden labels lump out **exactly**: the restriction to `[k]` is itself Markov.

For a specified visible refinement `pi` into `r` blocks, its first-order accelerated rate is

\[
\lambda_N\Pr_N(\pi).
\tag{7.1}
\]

From (5.6)--(6.2):

- for a binary split `i|j`,
  \[
  \boxed{
  \lambda_N\Pr_N(i|j)\to B(i,j);
  }
  \tag{7.2}
  \]
- for every fixed `r>=3`,
  \[
  \boxed{
  \lambda_N\Pr_N(\pi)=O((\log N)^{2-r})\to0.
  }
  \tag{7.3}
  \]

Hence the finite-state one-block generator on every fixed restriction converges entrywise to the CTCS generator.

Let `Q_N^{(k)}` be the resulting fixed-`k` generator, including the vanishing multifurcating transitions. In one raw step two or more current visible blocks may attempt, but there are at most `k` of them, so this contribution is `O_k(a_N^2)`. Therefore the exact one-step kernel satisfies

\[
P_N^{(k)}
=I+\delta_NQ_N^{(k)}+R_N^{(k)},
\qquad
\|R_N^{(k)}\|_{\rm row,1}
=O_k(\delta_N^2\lambda_N^2).
\tag{7.4}
\]

Eventually `delta_N=N^{-2}` by (6.2), and therefore on every bounded time interval

\[
\frac1{\delta_N}
O_k(\delta_N^2\lambda_N^2)
=O_k(\delta_N\lambda_N^2)
=O_k\left(\frac{(\log N)^2}{N^2}\right)
\longrightarrow0.
\tag{7.5}
\]

The grid mesh also tends to zero. Finite-state Euler/uniformization coupling gives

\[
\boxed{
\Pi_{N,046}^{[k]}
\Longrightarrow
\Pi_{\rm CTCS}^{[k]}
\quad\text{in Skorokhod }J_1
}
\tag{7.6}
\]

for every fixed `k` and bounded time horizon. The restrictions are consistent, so with

\[
d_{\rm proj}(\omega,\eta)
=\sum_{k\ge2}2^{-k}
(1\wedge d_{J_1,k}(\omega^{[k]},\eta^{[k]})),
\]

the usual finite-coordinate/tail argument gives

\[
\boxed{
\Pi_{N,046}
\Longrightarrow
\Pi_{\operatorname{CTCS}(\infty)}.
}
\tag{7.7}
\]

This is the complete partition-valued genealogy limit, not a root or tagged-fragment limit.

## 8. Exact finite witness and frozen non-equivalence

Every conditioned polynomial has exactly six distinct irreducible factors, all of positive degree. Therefore the first effective full-root proposal in C046 has

\[
\boxed{\deg(\text{root})=6\quad\text{almost surely}.}
\tag{8.1}
\]

At the minimum size `N=14`, exact enumeration is especially rigid. There are exactly

\[
\boxed{3}
\]

squarefree monic degree-14 binary polynomials with six irreducible factors, and every one has degree multiset

\[
\boxed{(4,3,3,2,1,1).}
\tag{8.2}
\]

The exact two-label separation probability is

\[
\boxed{p_{11,14}=6/7.}
\tag{8.3}
\]

At `N=15` there are exactly 12 conditioned polynomials, split evenly between profiles `(5,3,3,2,1,1)` and `(4,4,3,2,1,1)`, and `p_{11,15}=59/70`.

A deterministic leaf relabeling or global time/branch-length rescaling cannot alter the root outdegree law or the root size-multiset support. Repository recovery of the retained classes shows: the retained binary classes have degree two at a single-block root; C034/C035 have deterministic degree three; C036 has deterministic degree four; C038 has deterministic degree five; C037 has deterministic degree diverging with `N`; C039 has a genuinely random growing root-degree law; and the common-shock/quadrature classes C040--C045 still split a single root block binary. Earlier variable-arity classes have nondegenerate arity laws rather than a point mass at six. Targeted repository searches found no earlier R11 class with deterministic degree-six root law.

Thus C046 is distinct from C001--C045 under the frozen equivalence convention, which identifies only deterministic relabelings and global rescalings.

## 9. Exact finite self-checks

Only after the algebraic route and the path proof were established did I write finite checkers.

### Final C046 checker

`artifacts/R11/2026-09-18T14-40-00Z_c046_squarefree_polynomial_checker.py`

Creation commit: `acbcb1509528505d623643bf648fae48eadaedef`.

Archived output:

`artifacts/R11/2026-09-18T14-40-00Z_c046_squarefree_polynomial_checker.out`

Creation commit: `84178515abf7ef03000dd795100452ec34a169d7`.

The checker was executed locally before upload and records

`ASSERTIONS=187107`

followed by `ALL_EXACT_CHECKS_PASS`. It verifies:

1. direct brute-force irreducibility counts over `F_2` through degree 8 against (3.1);
2. finite coefficient bounds behind analyticity of the correction in (3.3);
3. exact squarefree six-factor counts by both degree-profile enumeration and the product generating function;
4. direct enumeration of all monic binary polynomials in degrees 14 and 15, recovering exactly `Z_14=3` and `Z_15=12`;
5. the exact `N=14` and `N=15` factor-degree profiles;
6. exact normalization of every visible set-partition law through five visible labels over the tested finite range;
7. `p_{11,14}=6/7`, `p_{11,15}=59/70`, `p_{11,16}=4889/5880`;
8. deterministic root degree six under the conditioning;
9. legality of the exact attempt probability in (6.3).

Local SHA-256 values of the uploaded payloads were:

- checker: `b2851f8759f158be5750d33674f45ab1a64458c0ebab6263e0c56a3f294a257d`;
- output: `1a997fd0914556396662b872cb793e85812cf7e8827b2bdd86ede41edd28d113`.

### Exploratory same-run checker, not separately counted

Before strengthening to actual squarefree polynomials, I checked a labelled Frobenius-orbit assembly with component EGF `sum I_2(m)z^m`. Those artifacts are:

- `artifacts/R11/2026-09-18T14-40-00Z_c046_frobenius_assembly_checker.py`, commit `730921ff89c2dc499dae21733c9dcc28549eec55`;
- `artifacts/R11/2026-09-18T14-40-00Z_c046_frobenius_assembly_checker.out`, commit `b642b608f4121b53794a5cde229acb8bc60f9574`.

They record `ASSERTIONS=18039` and `ALL_EXACT_CHECKS_PASS`. This exploratory decorated assembly is superseded by the stronger squarefree-polynomial C046 and does **not** increment the metric.

## 10. Status, model controls, and next route

The stable author-side claims after this run are

\[
\boxed{\texttt{R11-I0054-U025 = PROVED\_AUTHOR\_SIDE}},
\qquad
\boxed{\texttt{R11-I0054-C046 = PROVED\_AUTHOR\_SIDE under frozen equivalence}}.
\]

Therefore the frozen metric moves

\[
\boxed{45\to46.}
\]

I am **not calling Open Problem 18 closed**. The reasons are explicit:

1. `operations/claims/I0054.md` remains `PENDING_ADMISSION, not READY`;
2. no present-package P26 end-to-end PASS was recovered;
3. no second complete independent OTHER-track end-to-end PASS was recovered;
4. the source's informal phrase “superficially different” and publication novelty still require independent external judgment.

The honest source-level campaign status is **PARTIAL**.

The model-control limitation is also still unchanged in the actually exposed interface. It offers prompt/title, schedule, enabled state and timing mode, but no model-family selector, no reasoning-effort selector, no guaranteed hour-long execution field and no authenticated per-run model receipt. Making GPT-6/maximum enforceable would require those controls plus runtime attestation to be exposed by the authorized product/workspace/platform. The repository now records that the historical P26 `You cannot modify this task` response was context-dependent and that P26 was later editable from another authorized context; for any task still denied, the legitimate route is its authorized owning context or platform support, not cloning or bypass. No scheduler modification was attempted in this run.

### ledger_delta

```yaml
track: R11
target: I0054 / Aldous-Janson Open Problem 18
metric: distinct nontrivial discrete model classes with complete frozen-limit proofs
before: 45
after: 46
movement: +1
new_theorem: R11-I0054-U025
new_model: R11-I0054-C046
model_description: squarefree binary-polynomial six-factor fragmentation with uniform label allocation to irreducible-factor degree boxes
proof_scope: full fixed-k Skorokhod J1 path convergence plus projective CTCS(infinity) convergence
finite_checker: artifacts/R11/2026-09-18T14-40-00Z_c046_squarefree_polynomial_checker.py
finite_checker_output: artifacts/R11/2026-09-18T14-40-00Z_c046_squarefree_polynomial_checker.out
status: PARTIAL at source level; PROVED_AUTHOR_SIDE for U025/C046
stagnation_before: UNKNOWN
stagnation_after: 0 because the frozen metric moved
```

The next nonrepeating methods recorded are **#8, #20, #25**. The strongest next question is to remove the fixed-six conditioning or replace it by a natural local conditioning while retaining a rare binary tangent. Concretely: start from an ordinary random squarefree polynomial or another arithmetic factorization object, identify exactly why its Ewens-like higher-way refinements survive, and ask whether a finite deterministic thinning/conditioning of factor degrees can force the CTCS beta generator without introducing an artificial fixed component count. A complete answer would either produce a more natural class 47 or identify a genuine obstruction to arithmetic CTCS universality.
