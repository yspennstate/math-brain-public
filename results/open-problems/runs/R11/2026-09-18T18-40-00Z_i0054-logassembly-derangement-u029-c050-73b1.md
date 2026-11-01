Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested in prompt text, but the exposed runtime/task-control surface still has no binding model-family selector, no reasoning-effort selector, no guaranteed-duration control, and no authenticated completed-run routing receipt, so GPT-6 / maximum is not verified or claimed. Metric movement: `49 -> 50` distinct nontrivial discrete model classes with complete author-side proofs of the frozen CTCS(infinity) limit. Actual section-B moves: **#7, #17, #23**.

# R11 / I0054 — U029 logarithmic-assembly obstruction and C050 derangement-cycle hierarchy

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Track: R11, CLOSABLE OUTSIDE.  
Source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, Open Problem 18.  
Source-level campaign status after this run: **PARTIAL, not CLOSED**.  
New author-side claims: `R11-I0054-U029 = PROVED_AUTHOR_SIDE`; `R11-I0054-C050 = PROVED_AUTHOR_SIDE under frozen equivalence`.

## 1. Continuity, ownership, exclusions, source, and topology

I continued from

`runs/R11/2026-09-18T17-40-00Z_i0054-uniform-first-factor-u028-c049-51af.md`

rather than restarting. That report proved U028/C049, moved the frozen metric `48 -> 49`, and prescribed the nonrepeating moves `#7/#17/#23`; those are the three moves actually used here.

Before new mathematics I reread or recovered the required control state: `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; `operations/claims/I0054.md`; `operations/NEW_METHODS_2026-09-16.md`; the newest complete R11 report; the current P13/I0051 ownership surface; targeted I0054 history; current audit searches; and intake/ownership search hits. The canonical claim still literally says `PENDING_ADMISSION, not READY`, and still names R11 as the provisional exclusive owner. No competing current I0054 owner was recovered. P13's Aldous--Janson clade-count problem is distinct and was not reassigned. The old planar self-avoiding-walk route remains retired and untouched.

The current primary source was checked again on 2026-09-18. The current arXiv PDF is v3, dated 17 April 2025 / posted as v3 on 18 April 2025. Printed page 58 still states:

> Open Problem 18. Are there superficially different discrete models whose limit is the same CTCS(infinity)?

and immediately asks whether the source model's subordinator approximation can arise in some other discrete tree model. The same source says that CTCS(infinity) is formalized by the consistent exchangeable-partition process. I therefore retain the stronger frozen convergence target used by the recent R11 reports: for every fixed `k`, convergence of the complete partition-valued cadlag genealogy on `[k]` in Skorokhod `J_1`, followed by convergence in the summable projective finite-restriction path metric

\[
d_{\rm proj}(\omega,\eta)
=\sum_{k\ge1}2^{-k}
\bigl(1\wedge d_{J_1,k}(\omega^{[k]},\eta^{[k]})\bigr).
\tag{1.1}
\]

This is stronger than matching the root split, a tagged fragment, or fixed-time marginals.

For a visible block of size `b=i+j` and a specified unordered split `A|A^c`, `|A|=i`, the CTCS finite-restriction generator rate is

\[
q_b(A\mid A^c)
=B(i,j)
=\frac{(i-1)!(j-1)!}{(b-1)!},
\tag{1.2}
\]

and the total exit rate of a size-`b` block is `H_{b-1}`.

### Current literature and prior attempts

Fresh dated searches on 2026-09-18 covered:

- the current Aldous--Janson v3 source and Part III;
- `critical beta splitting`, `CTCS`, `different discrete models`, `fragmentation`, and `subordinator`;
- `logarithmic combinatorial structures`, `assemblies`, `uniform random component`, `derangements`, and `random permutation cycles`;
- current 2026 beta-splitting followups.

The nearby current papers found were Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320, on the beta-splitting family through homogeneous fragmentations/subordinators and a height problem, and Heng Ma, arXiv:2609.14325, on extremal separation/clade-count dynamics. They do not announce a solution of exact Open Problem 18.

The closest structural prior art is classical Arratia--Barbour--Tavare logarithmic-combinatorial-structure theory: assemblies, multisets, selections, Poisson--Dirichlet limits, and logarithmic component counts. Derangement cycle enumeration and the EGF `exp(-z)/(1-z)` are classical. I make no novelty claim for those ingredients, for transfer theorems, or for the usual cycle decomposition of permutations. The potentially new item is the uniform-component **binary tangent theorem U029**, especially the sharp `theta=1` obstruction, and its recursive CTCS application C050. The bounded search did not find this theorem/construction; that is negative evidence only, not a novelty certificate.

Repository recovery also found several earlier R11 permutation classes, including C011's two-cycle-sector/common-refinement construction and C034's conditioned-three-cycle model. C050 below is not a relabeling or time-rescaling of those models: it samples a full derangement first, then a uniformly chosen cycle, and its finite root support has a new exact witness recorded in section 7.

A fresh exact repository search for `P26-AUDIT-R11-I0054` still returned older R11 reports saying a current-package audit is absent; it did not recover a present-package P26 end-to-end PASS plus a second complete independent OTHER-track PASS. Thus no source closure is asserted.

## 2. Idea before code: the attempted universality statement is false

The previous three arithmetic runs C047--C049 suggested a broader conjecture:

> perhaps any logarithmic component structure, after choosing the object first and then one of its components uniformly, has the same beta binary tangent after a scalar time renormalization.

This run **attacked that claim first**. It is false. The failure is not a technical endpoint effect; it is already visible in the balanced four-label split.

Move **#17** supplied the correct general language. In a labelled logarithmic assembly the component EGF has the singular form

\[
A(z)=\theta\log\frac1{1-z}+H(z),
\tag{2.1}
\]

where `theta` is the logarithmic component-intensity parameter and `H` is regular at `1`.

Move **#7** asks for the scaling limit after first sampling the whole assembly and then a component uniformly. The resulting selected-component law can be derived exactly by pointing a component and integrating over the number of unpointed components.

Move **#23** is the surprise: `theta` does **not** disappear into time scaling. After pair normalization the limiting balanced `2|2` rate is

\[
\frac{\theta+1}{(\theta+2)(\theta+3)}.
\tag{2.2}
\]

CTCS requires `1/6`. For `theta>0` these agree if and only if

\[
6(\theta+1)=(\theta+2)(\theta+3)
\iff \theta(\theta-1)=0
\iff \boxed{\theta=1}.
\tag{2.3}
\]

So the natural "all logarithmic structures are CTCS after rescaling" route is refuted. The critical intensity `theta=1` is singled out sharply.

This obstruction is the new way in. Once it was identified, I specialized to the simplest genuinely different `theta=1` assembly that is not the uniform-permutation model itself: **uniform derangements**.

No checker was written until U029 and the whole-path C050 proof below were complete.

## 3. U029 — uniform-component tangent of a logarithmic labelled assembly

### 3.1 Setup

Let

\[
A(z)=\sum_{m\ge1}c_m z^m
=\theta L(z)+H(z),
\qquad
L(z):=\log\frac1{1-z},
\tag{3.1}
\]

where:

1. `theta>0`;
2. `c_m>=0`;
3. `H` is analytic in `|z|<R` for some `R>1`.

Let

\[
F(z)=e^{A(z)}=\sum_{n\ge0} f_n z^n.
\tag{3.2}
\]

Interpret this as the usual weighted labelled assembly: after conditioning on total label size `N`, a component count vector `(K_m)` has weight proportional to

\[
\prod_{m\ge1}\frac{c_m^{K_m}}{K_m!},
\qquad \sum_m mK_m=N.
\tag{3.3}
\]

Sample such an `N`-object, and then choose one of its `K=\sum_m K_m` components uniformly. Let `M_N` be the size of the selected component.

Because the assembly is labelled and exchangeable, conditional on `M_N=m`, the label set of that component is a uniform `m`-subset of `[N]`.

### 3.2 Exact reciprocal-component duality

Define

\[
B_A(z):=\int_0^1 e^{tA(z)}\,dt
=\frac{e^{A(z)}-1}{A(z)}
=\sum_{n\ge0} b_n z^n.
\tag{3.4}
\]

Then the selected-component size law is exactly

\[
\boxed{
p_{N,m}:=\Pr(M_N=m)
=c_m\,\frac{b_{N-m}}{f_N}.
}
\tag{3.5}
\]

**Proof.** Point the selected size-`m` component. If the remaining assembly has `K'` components, the original object has `K'+1`, so the uniform-component choice contributes `1/(K'+1)`. Since

\[
\frac1{K'+1}=\int_0^1 t^{K'}\,dt,
\]

summing all remainder assemblies with `t` marking each component gives `B_A(z)`. Multiplication by the pointed-component weight `c_m` and extraction of total size `N` yields (3.5). `QED`.

This is the exact labelled-assembly analogue of the inverse-factor-count duality from U028.

### 3.3 Singularity transfer

Since

\[
F(z)=e^{H(z)}(1-z)^{-\theta},
\tag{3.6}
\]

standard algebraic singularity transfer gives

\[
\boxed{
f_n\sim \frac{e^{H(1)}}{\Gamma(\theta)}\,n^{\theta-1}.
}
\tag{3.7}
\]

Moreover,

\[
B_A(z)
=
\frac{e^{H(z)}(1-z)^{-\theta}-1}
{\theta L(z)+H(z)}
\sim
\frac{e^{H(1)}}{\theta}
\frac{(1-z)^{-\theta}}{L(z)}.
\tag{3.8}
\]

The standard transfer theorem for an algebraic singularity times the slowly varying factor `1/L` yields

\[
\boxed{
b_n
\sim
\frac{e^{H(1)}}{\theta\Gamma(\theta)}
\frac{n^{\theta-1}}{\log n}.
}
\tag{3.9}
\]

For completeness, the only coefficient bounds needed below follow from the same transfer plus a finite adjustment:

\[
f_n\asymp (n+1)^{\theta-1},
\qquad
0\le b_n\le
C\frac{(n+1)^{\theta-1}}{\log(n+2)}.
\tag{3.10}
\]

Finally, analyticity of `H` beyond the unit circle gives

\[
c_m=\frac{\theta}{m}+h_m,
\qquad |h_m|\le C R_0^{-m}
\quad\text{for some }R_0>1,
\tag{3.11}
\]

and therefore `c_m<=C/m`.

### 3.4 Bulk selected-component law

Fix `epsilon in (0,1/2)`. Uniformly for

\[
\epsilon N\le m\le(1-\epsilon)N,
\]

equations (3.5), (3.7), (3.9), and (3.11) give

\[
\boxed{
p_{N,m}
=
\frac{1+o(1)}{m\log N}
\left(1-\frac mN\right)^{\theta-1}.
}
\tag{3.12}
\]

Thus the `theta=1` case has the same macroscopic harmonic `1/(m log N)` selected-component intensity that appeared in C049, but here it comes from a general combinatorial singularity rather than finite-field arithmetic.

### 3.5 Visible binary split law

For a fixed specified visible split with sizes `i,j>=1`, `b=i+j`, conditional on `M_N=m` the exact probability that the chosen component separates the two visible sides is

\[
s_{N,m}(i,j)
=
\frac{
(m)_{\underline i}(N-m)_{\underline j}
+
(m)_{\underline j}(N-m)_{\underline i}
}
{(N)_{\underline{i+j}}}.
\tag{3.13}
\]

Put

\[
P_N^{(\theta)}(i,j)
=\sum_{m=1}^N p_{N,m}s_{N,m}(i,j).
\tag{3.14}
\]

On the bulk, (3.12)--(3.13) form a Riemann sum and give

\[
(\log N)P_N^{(\theta)}(i,j)
\longrightarrow
R_\theta(i,j),
\tag{3.15}
\]

where

\[
\boxed{
R_\theta(i,j)
=
B(i,j+\theta)+B(j,i+\theta).
}
\tag{3.16}
\]

Here the beta function is understood by gamma functions for noninteger `theta`.

The endpoint justification is explicit. From (3.10)--(3.11), for `m<=epsilon N`,

\[
p_{N,m}\le \frac{C}{m\log N},
\tag{3.17}
\]

and the falling-factorial bound in (3.13) makes its contribution after multiplication by `log N` at most

\[
C(\epsilon^i+\epsilon^j).
\tag{3.18}
\]

At the other endpoint put `r=N-m`. For `m>=(1-\epsilon)N`,

\[
p_{N,N-r}
\le
C N^{-\theta}
\frac{(r+1)^{\theta-1}}{\log(r+2)}.
\tag{3.19}
\]

Let `s=min(i,j)`. The contribution of `r<=sqrt(N)`, after multiplication by `log N`, is

\[
O\!\left(
\log N\,N^{-\theta-s}
\sum_{r\le\sqrt N}(r+1)^{\theta+s-1}
\right)
=
O\!\left(\log N\,N^{-(\theta+s)/2}\right)
\to0.
\tag{3.20}
\]

For `sqrt(N)<r<=epsilon N`, `log(r+2)>=(1/2)\log N`, so the contribution is

\[
O(\epsilon^{\theta+s}).
\tag{3.21}
\]

Letting `N->infinity` and then `epsilon->0` proves (3.15)--(3.16) with no hidden endpoint assumption.

### 3.6 Sharp `theta=1` obstruction

For a pair,

\[
R_\theta(1,1)=\frac{2}{\theta+1}.
\tag{3.22}
\]

Normalize the proposal so the two-label split rate is one:

\[
\lambda_N:=\frac1{P_N^{(\theta)}(1,1)}
\sim
\frac{\theta+1}{2}\log N.
\tag{3.23}
\]

Then every fixed specified split has limiting normalized rate

\[
\boxed{
Q_\theta(i,j)
=
\frac{\theta+1}{2}
\left[B(i,j+\theta)+B(j,i+\theta)\right].
}
\tag{3.24}
\]

At `i=j=2`,

\[
Q_\theta(2,2)
=
\frac{\theta+1}{(\theta+2)(\theta+3)}.
\tag{3.25}
\]

As shown in (2.3), this equals the CTCS value `B(2,2)=1/6` iff `theta=1`.

Conversely, at `theta=1`,

\[
\begin{aligned}
Q_1(i,j)
&=B(i,j+1)+B(j,i+1)\\
&=\frac{j}{i+j}B(i,j)
+\frac{i}{i+j}B(i,j)\\
&=\boxed{B(i,j)}.
\end{aligned}
\tag{3.26}
\]

Therefore:

\[
\boxed{
\text{Within the regular labelled-logarithmic assembly class (3.1),}
\quad
\text{the pair-normalized binary tangent is CTCS iff }\theta=1.
}
\tag{U029}
\]

This proves

\[
\boxed{\texttt{R11-I0054-U029 = PROVED\_AUTHOR\_SIDE}.}
\]

The theorem also explains why C049 worked: it is another `theta=1` logarithmic structure after the appropriate pointing/debiasing. But it shows that the apparent universality does **not** extend to arbitrary logarithmic intensity.

## 4. A concrete `theta=1` model not used before: derangements

Take a uniform random derangement of `[N]`. Its cycle assembly has

\[
c_1=0,\qquad c_m=\frac1m\quad(m\ge2),
\tag{4.1}
\]

and therefore

\[
A_{\rm der}(z)
=\sum_{m\ge2}\frac{z^m}{m}
=
\log\frac1{1-z}-z.
\tag{4.2}
\]

Thus it is exactly U029 with

\[
\theta=1,\qquad H(z)=-z.
\tag{4.3}
\]

Let `D_{n,k}` be the number of derangements of `[n]` having exactly `k` cycles, and let

\[
D_n=\sum_kD_{n,k},
\qquad
J_n=\sum_k\frac{D_{n,k}}{k+1}.
\tag{4.4}
\]

If one first samples a uniform derangement of `[N]` and then chooses one of its cycles uniformly, the exact selected-cycle size law is

\[
\boxed{
p_{N,m}
=
\frac{\binom Nm(m-1)!\,J_{N-m}}{D_N},
\qquad 2\le m\le N.
}
\tag{4.5}
\]

This is (3.5) specialized to derangements. It also has a direct combinatorial proof: point the selected `m`-cycle; the remainder is a derangement with `k` cycles and receives the factor `1/(k+1)`.

By U029,

\[
\boxed{
(\log N)P_N(i,j)\longrightarrow B(i,j)
}
\tag{4.6}
\]

for every fixed specified unordered visible split.

## 5. C050 — uniform derangement first, then uniform cycle

For each `N>=4`, define the following finite discrete hierarchy on `[N]`.

A **C050 proposal** is:

1. sample a uniform derangement `sigma` of `[N]`;
2. list its cycles;
3. choose one cycle uniformly among those cycles;
4. let `A` be its support.

Define

\[
P_N(i,j)
\]

as the probability that a fresh proposal induces a specified visible `i|j` split, and put

\[
\lambda_N:=P_N(1,1)^{-1}.
\tag{5.1}
\]

By (4.6),

\[
\lambda_N\sim\log N,
\qquad
\lambda_NP_N(i,j)\to B(i,j).
\tag{5.2}
\]

Take

\[
\delta_N
=
\min\{N^{-2},P_N(1,1)/2\},
\qquad
a_N=\delta_N\lambda_N\le\frac12.
\tag{5.3}
\]

At each raw generation, every current nonsingleton full block `B` independently:

1. attempts with probability `a_N`;
2. on an attempt, draws a fresh independent C050 proposal `A`;
3. replaces `B` by the nonempty sets `B cap A` and `B\A`;
4. if one side is empty, the attempt is a no-change step;
5. children first act at the next raw generation.

One raw generation has physical duration `delta_N`.

This is a finite, explicit, binary, discrete random-tree model. The finite proposal mechanism is not the original critical beta-splitting rule: it samples a global fixed-point-free permutation and then selects one of that permutation's cycles uniformly.

### 5.1 Exact hidden-label lumping

Fix a visible set `[k]` and condition on its complete visible history. Every visible block `C` lies in a unique current hidden carrier `B`.

The attempt probability `a_N` is independent of `|B|`. On an attempt, the ambient derangement and selected cycle are sampled fresh from `[N]`, independently of `B` and the past. Therefore the restriction of the proposal to `C` depends only on the labels of `C`, not on the size or history of its hidden carrier.

If a proposal splits `B` but all labels of `C` fall on one side, then the visible block does not change and simply passes into one child carrier. At the next raw step that child again has the same attempt probability and receives a completely fresh ambient proposal. Thus an invisible hidden split leaves no residual visible state.

Different current visible blocks lie in different full carriers and use independent attempt coins/proposals. Hence the `[k]` restriction is itself Markov, and its one-block particular-split proposal probabilities are exactly the `P_N(i,j)` in (5.2).

### 5.2 Finite hierarchy completes almost surely

For every `N>=4` and every nonsingleton block `B`, a fresh C050 proposal has strictly positive probability to separate some two labels of `B`. For the root one may choose a derangement having a proper cycle; for a proper block one may choose a cycle whose support intersects `B` nontrivially but does not contain all of `B`. Such derangements exist for every `N>=4`.

Since attempts and proposals are fresh and independent, each nonsingleton current block eventually experiences a proper split almost surely. Every proper split increases the number of blocks, so at most `N-1` proper splits are needed before singletons. The finite hierarchy therefore completes almost surely.

### 5.3 Whole-path finite-restriction convergence

Fix `k`. Let `Q_N^{(k)}` be the generator obtained by assigning each specified binary split the rate

\[
\lambda_NP_N(i,j).
\tag{5.4}
\]

Equation (5.2) gives, entrywise on the finite partition state space,

\[
\boxed{
Q_N^{(k)}\longrightarrow Q_{\rm CTCS}^{(k)}.
}
\tag{5.5}
\]

In one raw step, one visible block has a prescribed split with probability

\[
a_NP_N(i,j)
=
\delta_N\lambda_NP_N(i,j).
\tag{5.6}
\]

Two distinct visible blocks can both change in the same raw generation only if both attempt. Since there are at most `k` visible blocks,

\[
\Pr(\text{two or more visible blocks change in one raw step})
=O_k(a_N^2)
=O_k(\delta_N^2\lambda_N^2).
\tag{5.7}
\]

Consequently the finite-state one-step kernel satisfies, uniformly in the visible state,

\[
\boxed{
\mathsf P_N^{(k)}
=
I+\delta_NQ_N^{(k)}
+O_k(\delta_N^2\lambda_N^2).
}
\tag{5.8}
\]

Because eventually `delta_N=N^{-2}` and `lambda_N~log N`,

\[
\boxed{
\delta_N\lambda_N^2
=
O\!\left(\frac{(\log N)^2}{N^2}\right)
\longrightarrow0.
}
\tag{5.9}
\]

Over a fixed physical interval `[0,T]` there are `O(T/delta_N)` raw steps. Step-by-step maximal coupling therefore couples the actual `[k]` restriction to the Euler chain with kernel `I+delta_N Q_N^{(k)}` with total failure probability

\[
O_{k,T}(\delta_N\lambda_N^2)
+O_{k,T}(\|Q_N^{(k)}-Q_{\rm CTCS}^{(k)}\|)
\to0.
\tag{5.10}
\]

The Euler chain converges to the CTCS continuous-time chain: its geometric holding time in state `rho`, multiplied by `delta_N`, tends to `Exp(-Q_{\rm CTCS}^{(k)}(rho,rho))`, and its conditional next-state probabilities converge to the CTCS jump probabilities. A fragmentation of `k` labels has at most `k-1` proper visible jumps, so this convergence of the finite jump sequence yields

\[
\boxed{
\Pi_{N,050}^{[k]}
\Longrightarrow
\Pi_{\rm CTCS}^{[k]}
\quad\text{in Skorokhod }J_1.
}
\tag{5.11}
\]

Finally, for any finite `K`, the `[K]` restriction simultaneously determines all coordinates `[k]`, `k<=K`, while the tail of (1.1) is at most `2^{-K}`. Therefore (5.11) for each `K` implies

\[
\boxed{
\Pi_{N,050}
\Longrightarrow
\Pi_{\operatorname{CTCS}(\infty)}
}
\tag{5.12}
\]

in the frozen summable projective finite-restriction path topology.

Thus C050 has the complete required limit argument, not merely a marginal calculation.

## 6. Exact finite arithmetic and the new finite witness

The derangement cycle-count recurrence used by the exact checker is

\[
D_{n,k}
=
\sum_{m=2}^{n}
\frac{(n-1)!}{(n-m)!}\,
D_{n-m,k-1},
\qquad
D_{0,0}=1.
\tag{6.1}
\]

It is simply the decomposition according to the cycle containing label `1`.

At `N=4`, there are nine derangements: six are single `4`-cycles and three have cycle type `2+2`. Therefore under "uniform derangement first, then uniform cycle",

\[
\boxed{
p_{4,2}=\frac13,\qquad
p_{4,4}=\frac23.
}
\tag{6.2}
\]

For specified visible splits,

\[
\boxed{
P_4(1,1)=\frac29,\qquad
P_4(2,2)=\frac19,\qquad
P_4(1,3)=0.
}
\tag{6.3}
\]

Hence the global-time-rescaling invariant pair is

\[
\boxed{
\left(
\frac{P_4(2,2)}{P_4(1,1)},
\frac{P_4(1,3)}{P_4(1,1)}
\right)
=
\left(\frac12,0\right).
}
\tag{6.4}
\]

This is especially useful because the zero is a support invariant: no deterministic leaf relabeling or positive global branch/time rescaling can create a `1|3` root split at `N=4`.

The nearest preceding arithmetic class C049 instead has invariant pair

\[
\left(\frac4{41},\frac{33}{82}\right),
\tag{6.5}
\]

while C048 has both entries positive as well. C011's two-cycle-sector permutation model allows `1|3` at `N=4`, and C034 has a deterministic three-child full-root proposal on every successful root attempt. A targeted repository search found no retained R11 class using uniform derangements or carrying the exact C050 support/rate witness (6.4). Under the frozen equivalence convention, C050 is therefore counted as a new class.

This proves

\[
\boxed{\texttt{R11-I0054-C050 = PROVED\_AUTHOR\_SIDE}.}
\]

## 7. Exact self-check

Only after the proof route was established did I write the finite checker

`artifacts/R11/2026-09-18T18-40-00Z_i0054-logassembly-derangement-u029-c050-73b1_checker.py`

Creation/readback commit:

`92a27c490e1259fd710d324397b073da14066fa6`

Local source SHA-256 before upload:

`63d86854b115f9d40eaba004b3cb29b3f0dee20c8270b9fee38e096ec9a41c1d`

The checker was actually executed with exact integer / `fractions.Fraction` arithmetic. It:

- checks (6.1) against the derangement inclusion--exclusion formula through `N=60`;
- verifies normalization of the exact selected-cycle law (4.5) through `N=60`;
- brute-enumerates all derangements through `N=8` and compares the selected-cycle distribution to (4.5);
- independently brute-checks specified visible split probabilities for all tested `N<=8` and visible sizes through five;
- verifies the exact `N=4` witness (6.2)--(6.4);
- compares the C050 invariant pair with C049's archived pair;
- checks the `theta` balanced-split obstruction for integer `theta=1,...,500` while the written algebra (2.3) proves it for every real `theta>0`;
- checks the exact `theta=1` beta identity through `i,j<=30`;
- checks the total CTCS exit-rate identity through block size `35`.

The run produced

`ASSERTIONS=3418`

and ends

`ALL_EXACT_CHECKS_PASS`.

Archived stdout:

`artifacts/R11/2026-09-18T18-40-00Z_i0054-logassembly-derangement-u029-c050-73b1_checker.out`

Creation/readback commit:

`d91f658da43c7b6fbdbcb25f4b03c643d97344c4`

Archived stdout SHA-256 before upload:

`7ded8e8589126b2bae5bea19490129fe0ecfae687a48865a0c9748200a54f69f`

The checker is a **self-check**. It does not count as either required independent audit.

## 8. What the three methods actually did

- **#7 — TAKE THE LIMIT.** Passing from the exact uniform-component duality (3.5) to the singular limit exposed a universal one-parameter kernel `Q_theta`, making it possible to test the entire logarithmic-assembly class rather than one finite model at a time.
- **#17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE.** Classical logarithmic-combinatorial-structure theory supplied the right representation `A(z)=theta log(1/(1-z))+H(z)`. That framework unifies permutations, derangements, finite-field factor structures and many other component models.
- **#23 — DO WHAT THE PROPOSER DID NOT EXPECT.** Instead of trying to prove unrestricted universality, I tried to refute it. The four-label balanced split proves a sharp obstruction: after pair normalization, CTCS occurs in this regular labelled-assembly class exactly at `theta=1`.

So this run did not merely create C050; it also identified a mechanism that explains why the recent arithmetic classes worked and where that mechanism fails.

## 9. Status, closure discipline, and model-control issue

The stable author-side state after this run is

\[
\boxed{\texttt{R11-I0054-U029 = PROVED\_AUTHOR\_SIDE}},
\qquad
\boxed{\texttt{R11-I0054-C050 = PROVED\_AUTHOR\_SIDE}},
\qquad
\boxed{49\to50}.
\tag{9.1}
\]

I do **not** call Aldous--Janson Open Problem 18 closed. The canonical claim remains `PENDING_ADMISSION, not READY`; external novelty of U029/C050 is unverified; and the required present-package P26 end-to-end PASS plus a second complete independent OTHER-track PASS were not recovered. The honest source-level campaign status remains **PARTIAL**.

The model-control limitation is still the one recorded in current repository policy and `RESULTS.md`. The exposed task-control schema offers prompt/title, schedule, enablement, and timing mode, but not a model-family selector, reasoning-effort selector, guaranteed execution duration, or authenticated per-run routing attestation. Thus `GPT-6 / maximum` remains a prompt request rather than an enforceable setting here. Making it binding requires the authorized product/workspace/platform to expose model/reasoning controls and completed-run routing telemetry. The historical P26 `You cannot modify this task` result was context-dependent: `RESULTS.md` records a later successful P26 prompt update in another authorized context, while all R-series edits were denied in another reconciled context. The legitimate remedy for a currently denied task is its authorized owning context or platform support, not cloning or bypassing. No scheduler change was attempted in this run.

## 10. Next route

Next nonrepeating section-B moves: **#5, #16, #29**.

The strongest next mathematical target is the boundary of U029 rather than another easy `theta=1` example. Replace the analytic correction `H` by a **quasi-logarithmic slowly varying perturbation**

\[
c_m=\frac{1+\varepsilon_m}{m},
\]

where `epsilon_m` need not be summable. The question is whether CTCS is controlled by a logarithmic Cesaro condition on `epsilon_m`, or whether an oscillatory/sparse boundary perturbation can preserve all pair rates while changing a higher split rate. The three next moves will (5) introduce a perturbation parameter and differentiate the limiting kernel, (16) enumerate exact periodic/sparse perturbations, and (29) treat the missing boundary mass at `0` and `1` as part of the compactified limiting component measure rather than discarding it as an endpoint error.

```yaml
ledger_delta:
  track: R11
  lane: CLOSABLE_OUTSIDE
  source: "Aldous--Janson arXiv:2303.02529v3 Open Problem 18 / I0054"
  metric_name: "number of distinct nontrivial discrete model classes with complete author-side full CTCS(infinity) limit proofs under frozen equivalence"
  before: 49
  after: 50
  movement: "+1"
  status: PARTIAL
  new_claims:
    - "R11-I0054-U029 = PROVED_AUTHOR_SIDE"
    - "R11-I0054-C050 = PROVED_AUTHOR_SIDE under frozen equivalence"
  actual_methods: [7, 17, 23]
  exact_self_check: "3418 exact assertions; ALL_EXACT_CHECKS_PASS"
  audit_state: "required present-package P26 + second independent OTHER-track end-to-end PASS not recovered"
  ownership: "R11 provisional exclusive reservation; canonical status PENDING_ADMISSION, not READY"
  next_methods: [5, 16, 29]
```
