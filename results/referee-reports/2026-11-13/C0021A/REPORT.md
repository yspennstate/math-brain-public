PARTIAL

C0021: the revealment exponent of iterated ternary majority under uniform input.

Let $f_0(x)=x$, and let $f_k$ be majority of three independent copies of
$f_{k-1}$, on $n=3^k$ bits. All algorithms in this report compute the function
exactly on every input. Expectations defining revealment and average cost use
independent uniform input bits and independent algorithmic randomness.

The exact exponent is not determined here. The following bounds are proved:

\[
 \left(\frac34\right)^k\leq\delta(f_k)
 \leq K\left(\frac{2.46003}{3}\right)^k,
 \qquad K<13.385\quad(k\geq2).
\]

In particular, there is an exponent in the logarithmic sense
$\delta(f_k)=n^{-\sigma+o(1)}$, and

\[
 \boxed{\quad
 \log_3\!\left(\frac{300000}{246003}\right)
 =0.180626728576668\ldots
 \ \leq\ \sigma\ \leq\
 \log_3(4/3)=0.261859507142915\ldots .\quad}
\]

The upper bound on revealment is an explicit finite-state recursive algorithm
with an exact rational certificate and a separate verifier. It is the best
bound certified in this directory, not a claim to a new or best published
bound. A 2009 Peres lecture already records an unspecified average-cost upper
base $2.46\ldots$. No reference found determines sigma. The source search and
its limitations are recorded in [sources/LITERATURE_AUDIT.md](sources/LITERATURE_AUDIT.md).

The exact finite values are

| Height $k$ | Bits | Optimal uniform expected queries $C_k$ | Optimal revealment $\delta_k=C_k/3^k$ | Depth-first cost |
|---:|---:|---:|---:|---:|
| 1 | 3 | $5/2$ | $5/6$ | $5/2$ |
| 2 | 9 | $393/64$ | $131/192$ | $25/4$ |
| 3 | 27 | $15796051/1048576$ | $15796051/28311552$ | $125/8$ |

Thus directional, or depth-first, algorithms are already suboptimal for
revealment at height 2. This refutes that proposed simplification, but does not
resolve C0021; the status is PARTIAL.

## Source and literature result

The [Garban–Steif author-hosted draft](https://math.univ-lyon1.fr/~garban/Fichiers/book.pdf)
was retrieved as text in [sources/garban_steif_book.txt](sources/garban_steif_book.txt).
In this version, Chapter VIII occupies printed pages 89–100, and Exercise VIII.5
is on p. 100; its bracketed note is the problem in the question. The problem
appears again as XIII.1 on p. 187. Pagination and some theorem/exercise numbers
vary across drafts. Definition VIII.1 uses the maximum, over coordinates, of
the probability of being queried, averaging over both the uniform input and
the algorithm. The algorithm must stop only when all completions have the same
output. Definition VIII.7 defines uniform expected cost. The relevant results
are VIII.2, VIII.8, and VIII.9. Their consequences are derived below.

The main model distinction is essential. Write
\[
 C_k=\min_A\mathbb E_{X\sim U,\,A}|J_A(X)|,
 \qquad R_0(f_k)=\min_A\max_x\mathbb E_A|J_A(x)|.
\]
Then $C_k\le R_0(f_k)$. A worst-case upper bound transfers to $C_k$; a
worst-case lower bound does not. Transitivity on coordinates does not make all
input configurations equivalent.

The requested and subsequent literature gives the following picture:

| Reference | Relevant result | What it implies here |
|---|---|---|
| Jayram–Kumar–Sivakumar, STOC 2003, 673–682, DOI 10.1145/780542.780640 | Worst-case bounded-error lower base $7/3$; zero-error upper base about 2.65622 | Upper bound transfers, but is weaker than the uniform $2.5^k$ algorithm. The lower bound does not transfer. |
| Leonardos, ICALP 2013, LNCS 7965, 696–708 | Worst-case lower base 2.55 | Does not lower-bound $C_k$. The corrected ECCC version replaces an erroneous earlier 2.6 claim. |
| Magniez–Nayak–Santha–Sherman–Tardos–Xiao, *RSA* 48(3) (2016), 612–638, Theorem 1.1 | $(1/2-\epsilon)2.57143^k\le R_\epsilon(f_k)\le1.007\,2.64944^k$ | Its hard distribution is not uniform on all strings. The algorithms can instead be analyzed directly under uniform input. |
| Göös–Jayram, CCC 2016, Theorem 2.2 and its discussion | Worst-case base $(35/2)^{1/3}=2.596\ldots$, with a polynomial-in-height loss for constant error | Also does not lower-bound $C_k$. |
| Leonardos, arXiv:2203.17168v4, 2023 | General threshold-formula bounds | “Uniform” refers to tree shape, not the input law. No determination of this revealment exponent. |
| Al-Dhalaan–Ben-David, arXiv:2601.08073, 2026, Theorem 1 | $R_0^*(f)=\max\{R^*(f),C_{\rm certificate}^*(f)\}$ | Equates two worst-case composition bases for MAJ3; does not identify their value or the uniform-average base. |

The [2016 paper](https://www.irif.fr/~magniez/PAPIERS/mnsstx-rsa16.pdf)
defines its hard inputs by requiring non-unanimity at every internal gate.
The [2026 paper](https://arxiv.org/abs/2601.08073) explicitly leaves its
worst-case composition base unknown, between 2.596 and 2.650. Neither statement
settles the uniform-input problem. Full text extracts of both are saved.
For JKS, only the IBM abstract was retrieved; the numerical algorithm bound and
the warning about its Appendix B recurrence were checked in the later paper.

[Peres–Schramm–Sheffield–Wilson](https://arxiv.org/abs/math/0508580),
*American Mathematical Monthly* 114(5) (2007), 373–387, Lemma 3.1, identifies
game-optimal moves with maximum conditional pivotal probability. Its recursive
majority paragraph and final section leave expected game duration and query
optimality open. Winning the random-turn game optimally does not prove minimal
expected query count. No greedy-pivotal optimality assumption is used here.

## Revealment equals normalized average cost

For a tree $A$, put $q_i(A)=\mathbb P(i\in J_A)$. Repeated queries can be
removed. Then
\[
 \mathbb E|J_A|=\sum_iq_i(A)\le n\max_iq_i(A),
\]
so $delta(f_k)\ge C_k/n$. Conversely, choose a minimum-average-cost
deterministic tree and conjugate it by a uniformly random automorphism of the
complete ternary tree. These automorphisms preserve both the function and
uniform input and act transitively on leaves. Every coordinate is then queried
with probability exactly $C_k/n$. Consequently
\[
                         \delta(f_k)=C_k/3^k.                 \tag{1}
\]
Randomization does not reduce minimum average cost: it forms convex
combinations of deterministic-tree costs. It is needed in (1) to equalize
coordinate query probabilities. The minima exist because a finite function
has finitely many non-repeating decision trees.

Evaluating an optimal height-(a) tree on height-(b) block outputs gives
$C_{a+b}\le C_a C_b$. The block outputs are independent unbiased bits. The
decision to start an untouched block is independent of its contents, so each
such block costs $C_b$ in expectation, even if that cost correlates with the
block's eventual output. Fekete's lemma gives
\[
 \lambda_*:=\lim_k C_k^{1/k}=\inf_{k\ge1}C_k^{1/k},\qquad
 \sigma=1-\log_3\lambda_* .                                  \tag{2}
\]
This proves existence of a logarithmic exponent, not constant-factor
equivalence to a pure power.

## Lower bounds on revealment

Use sign-valued output, so $\mathbb Ef_k=0$ and $\operatorname{Var}(f_k)=1$.
A leaf is pivotal exactly when, at each of its $k$ ancestor gates, the two
off-path child outputs disagree. These are independent events, each of
probability $1/2$, on disjoint uniform subtrees. Thus
\[
 \operatorname{Inf}_i(f_k)=2^{-k},\qquad I_k=3^k2^{-k}=(3/2)^k. \tag{3}
\]
As a second derivation, the probability of a one under bias $p$ is iterated
application of $\Phi(p)=3p^2-2p^3$. Since $\Phi(1/2)=1/2$ and
$\Phi'(1/2)=3/2$, Russo's derivative formula also gives (3). Direct truth-table
checks at heights 1 and 2 agree with both derivations.

The [OSSS inequality, Theorem 1.1](https://www.cs.columbia.edu/~rocco/Public/focs05osss.pdf),
in this sign-valued uniform normalization, is
\[
 1\le\sum_i q_i(A)\operatorname{Inf}_i(f_k)\le\delta_A I_k.
\]
It gives
\[
 \delta_k\ge(2/3)^k=n^{-\log_3(3/2)},
 \qquad \sigma\le\log_3(3/2)=0.3690702464\ldots .
\]

The stronger bound here is Garban–Steif VIII.8, attributed to O'Donnell–Servedio.
Here is the proof specialized to this setting. For any exact algorithm let
$S_A=\sum_{i\in J_A}X_i$. Monotonicity gives
$\mathbb E[f_kX_i]=\operatorname{Inf}_i(f_k)$. On stopping, $f_k$ is
determined, so contributions from unqueried unbiased bits have expectation
zero. Hence $\mathbb E[f_k S_A]=I_k$. The successive queried signs are
martingale differences, so $\mathbb E S_A^2=\mathbb E|J_A|$. Cauchy–Schwarz
therefore gives $C(A)\ge I_k^2$, and consequently
\[
 C_k\ge(9/4)^k,\qquad
 \delta_k\ge(3/4)^k=n^{-\log_3(4/3)}.                         \tag{4}
\]
No hard-distribution query lower bound is substituted for (4).

## Explicit algorithmic upper bounds

The depth-first algorithm evaluates two children, and evaluates the third
only if their values disagree. Under uniform input this happens with
probability $1/2$, so its cost is $(5/2)^k$, giving
\[
 \delta_k\le(5/6)^k=n^{-\log_3(6/5)},\qquad
 \log_3(6/5)=0.165956232853530\ldots .
\]
Every depth-first algorithm has this same minimum average cost. Each newly
visited child subtree is independent and unbiased, even conditional on the
completed previous subtrees. Two child values are always necessary; their
disagreement requires a third with probability $1/2$. Induction proves the
claim, allowing adaptive choices of the next child and randomized mixtures.

A stronger, short explicit recursion is Algorithms 1–2 of the 2016 paper.
Write $E_h$ for its Evaluate cost and $D_h$ for its Complete cost, with one
child value already known. To evaluate a fresh node of height at least 2,
Evaluate first evaluates one grandchild in each of two children. If these
opinions disagree, it evaluates the untouched third child and completes the
child whose opinion agrees with that result, completing the other only if
necessary. If the opinions agree, it completes the first child, then chooses
between completing the second and evaluating the third according to agreement.
Complete similarly probes one grandchild of an unknown child before choosing
between finishing that child and evaluating its sibling.

Under uniform input, a child's output agrees with one observed child of its
own with probability $3/4$. Independence and this probability give the exact
average recurrences
\[
 \begin{aligned}
 E_h&=2E_{h-2}+\frac{23}{32}E_{h-1}+\frac{25}{16}D_{h-1},\\
 D_h&=E_{h-2}+\frac58E_{h-1}+\frac34D_{h-1},
 \end{aligned}                                                \tag{5}
\]
with $E_0=1,E_1=5/2,D_1=3/2$. For example, conditioned on differing first
opinions, Evaluate uses one fresh-child evaluation and $5/4$ completions on
average; conditioned on equal opinions these numbers are $7/16$ and $15/8$.
These give the first line of (5). The two cases in Complete give $5/8$ fresh
evaluations and $3/4$ completions, in addition to its initial probe.
All calls start before seeing any still-unknown contents of the called subtree;
its average cost can therefore be multiplied by its invocation probability.

The nonnegative recurrence matrix for $(E_h,E_{h-1},D_h)$ has characteristic
polynomial
\[
                   32z^3-47z^2-78z-2.
\]
Its positive Perron root is $r=2.4670436373267\ldots$. Thus
$\delta_k=O((r/3)^k)$, proving
$sigma\ge\log_3(3/r)=0.1780352949598\ldots$.
At height 2, (5) gives exactly $393/64$. A literal implementation checked on
all 512 inputs has query-count histogram
$\{4:64,5:128,6:128,7:88,8:72,9:32\}$, independently confirming that mean and
correctness. Since $393/64<25/4$, this also supplies a concrete directional
counterexample.

### Certified finite-state improvement

The final upper bound uses a larger explicit recursive family, rather than an
unjustified extrapolation of finite-height costs. Its complete policy is in
[data/recursive_bound_246003_100000.json](data/recursive_bound_246003_100000.json).

A *type* is a restriction of a complete depth-2 ternary majority tree. Collapse
only determined subtrees to 0 or 1; retain projection gates such as
$\mathrm{MAJ}(0,1,u)$. Sort children, interpreting repeated subtree symbols
as independent copies on distinct variables. There are 46 types, including the
two constants. For a type $t$ and $h\ge2$, let $F_{h,t}$ replace each
remaining unknown bottom leaf of $t$ by a fresh $f_{h-2}$. The full type
$t_*$ gives $F_{h,t_*}=f_h$.

Expand each unknown bottom leaf of $t$ into one more majority gate. The
result is a restricted depth-3 skeleton (G(t)), with independent unbiased
macro-bits $f_{h-3}$. There are 17,206 possible states. At a state $s$, the
policy selects a proper unresolved descendant at depth $j=1,2,$ or (3)
and evaluates it recursively:

- At depth 1, its remaining depth-2 skeleton is the called type.
- At depth 2, expand the descendant's bottom unknowns once to pad its type to
  depth 2. This describes the same function at height (h-2).
- At depth 3, call the full type, computing the macro-bit $f_{h-3}$.

The call is at smaller height (h-j). Replace that descendant by its returned
value and continue until the root is determined. The certificate records every
chosen action, its called type (u), depth (j), exact output probability
$p$, and successor states $s_0,s_1$. For any skeleton with child one-
probabilities (a,b,c), its one-probability is (ab+ac+bc-2abc).

Set $\lambda=246003/100000$. The certificate supplies positive rational
weights $w_t$ for all nonconstant types, with $w_{t_*}=1$, and zero weights
for constant types. For the recorded policy compute rational normalized costs
\[
 V(0)=V(1)=0,\qquad
 V(s)=\lambda^{-j}w_u+(1-p)V(s_0)+pV(s_1).                    \tag{6}
\]
Every action strictly decreases the number of unknown macro-bits, so (6) is
acyclic. The exact certificate check establishes, for every type,
\[
                             V(G(t))\le w_t.                 \tag{7}
\]
The minimum nonconstant slack in (7) is the positive rational
\[
             \frac{185008634992727}{605174760090000000000}.
\]

For completeness, (7) proves an actual recursive algorithm bound as follows.
At heights 2, 3, and 4, query all remaining original bits. Choose
\[
 K=\frac{(3/\lambda)^4}{\min_{t\ne0,1}w_t}
   =13.3845387291493\ldots .
\]
Then all these base costs are at most $K\lambda^h w_t$. At height $h\ge5$,
every descendant call is to a height at least 2, so strong induction bounds
its cost by $K\lambda^{h-j}w_u$. The remaining macro-bits are independent
and unbiased conditional on the state. Applying (6) and (7) bounds the whole
call by $K\lambda^h w_t$. In particular $C_h\le K\lambda^h$. Symmetrize
this algorithm on leaves and apply (1) to obtain the stated revealment bound.

[code/verify_recursive_bound.py](code/verify_recursive_bound.py) independently
decodes the trees into nested tuples, enumerates actual descendant paths,
checks legality and output probabilities of all 17,204 recorded actions, and
evaluates (6) using only exact fractions. It imports no search code and uses no
search-time cost values. It verifies all 46 inequalities (7), the positive
weights, normalization, and the base-case prefactor. Its result and certificate
hash are in [data/recursive_verification.json](data/recursive_verification.json).
Floating-point iteration was used only to find weights and policies. Trials
at 2.46 and 2.460025 failed and are not claimed as bounds.

## Exact optimization at small heights

There is a finite LP over deterministic exact decision trees $T$: minimize
$d$, subject to $\sum_Tp_Tq_i(T)\le d$ for each $i$,
$\sum_Tp_T=1$, and $p_T\ge0$. Its dual chooses nonnegative coordinate weights
summing to 1 and maximizes the minimum weighted tree-query cost. By the
transitive symmetrization proof, uniform coordinate weights are dual-optimal,
and this LP's value is $C_k/3^k$.

An equivalent, much smaller LP uses restricted-function states. For each
nonconstant state $s$, every possible next relevant leaf $i$ imposes
\[
       v_s\le1+\frac12(v_{s|i=0}+v_{s|i=1}),\qquad
       v_{\rm constant}=0.
\]
Maximizing the initial state's value gives $C_k$. Backward induction makes
the maximal feasible solution the Bellman recursion
\[
       v_s=\min_i\left[1+\frac12(v_{s|i=0}+v_{s|i=1})\right]. \tag{8}
\]
This includes all adaptive interleavings; it is not a minimax restricted to
directional trees. Randomizing an action cannot improve (8).

[code/exact_majority.py](code/exact_majority.py) implements (8) with exact
fractions, quotienting only by valid read-once formula symmetries and constant
simplifications. Unqueried bits remain independent uniform bits conditional
on a transcript, so forgetting the order of previous queries is valid. Two
histories with isomorphic residual formulas have identical future query
problems. Each leaf occurrence, including a repeated subtree shape, remains a
separate input variable. The height-3 certificate contains 13,986 states and
66,680 query inequalities; every permitted next-query action was regenerated
and checked, together with equality for a chosen minimizing action.

The separate verifier also computes height 1 and 2 by labelled partial
assignments without symmetry reduction. A third formulation keeps the
original ternary gates, does not eliminate projections or convert to AND/OR,
and uses scaled integer costs. It agrees at all three heights. The certificates
and results are in [data/bellman_certificate.json](data/bellman_certificate.json),
[data/exact_results.json](data/exact_results.json), and
[data/verification.json](data/verification.json).

For the fixed-tree representation, the number of restriction states obeys
\[
 S_0=3,\qquad S_{h+1}=\binom{S_h+2}{3}-2S_h+2.
\]
The subtraction collapses the two sets of triples having two equal constant
children. This gives $S_1=6,S_2=46,S_3=17206$, and
$S_4=849110490846$. A full height-4 search by this method cannot fit the
4 GB budget. This is a limitation of the exhaustive representation, not a
proof that every possible height-4 method is infeasible. No exact height-4
optimum is reported; the recursive bound's base case queries all 81 bits.

The finite effective exponents $-\log_3\delta_k/k$ are
$0.1659562329,0.1739913402,0.1770445477$. Each supplies a lower bound on sigma
by (2). A three-point log-linear fit with a free intercept gives
$0.1825887051$. That fit is descriptive only; three heights cannot identify
the limiting exponent or a convergence rate. It is compatible with the proved
interval.

## How Schramm–Steif uses revealment

Garban–Steif VIII.2 gives, for Fourier level $r\ge1$,
\[
 W_r(f)=\sum_{|S|=r}\widehat f(S)^2\le r\delta(f)\|f\|_2^2.
\]
For the centered sign-valued $f_k$, independently resampling each bit with
probability $\epsilon$ therefore gives
\[
 \operatorname{Cov}(f_k(X),f_k(X^\epsilon))
 \le\delta_k\sum_{r\ge1}r(1-\epsilon)^r
 =\delta_k\frac{1-\epsilon}{\epsilon^2}.
\]
Thus $\delta_k\to0$ implies qualitative noise sensitivity. If
$\delta_k=O(n^{-a})$, it proves decorrelation for
$\epsilon=n^{-\gamma}$ whenever $\gamma<a/2$, as in Corollary VIII.6.
The certified algorithm gives the sufficient range
$\gamma<0.0903133642883\ldots$. This is a consequence of the revealment
method, not a claim that its sufficient noise exponent is sharp.

## Reproduction, checks, and remaining problem

All computations used a single Python process with one thread, inherited nice
15, and numerical-library thread limits set to 1. The largest measured peak RSS
among the mathematical runs was under 80 MB. No subagents, simulations of large
input tables, pushes, publication, or paper page images were used. Source PDFs
were converted from memory to text. Their URLs and hashes are saved in
[sources/manifest.json](sources/manifest.json).

From this directory, run sequentially:

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
export PYTHONDONTWRITEBYTECODE=1
python3 code/exact_majority.py --max-depth 3
python3 code/verify_exact.py
python3 code/recursive_bound.py --lambda 246003/100000 --iterations 40
python3 code/verify_recursive_bound.py
python3 code/summarize.py
```

The scripts check exact finite optima, all Bellman actions, the recursive
certificate, direct influences at heights 1 and 2, independent high-precision
logarithm conversions, and a rational isolating interval for the root in (5).
Source retrieval can be repeated with `python3 code/fetch_sources.py`, which
requires `pdftotext` and saves text only.

What remains is to determine $\lambda_*=\inf_k C_k^{1/k}$, equivalently sigma.
There is no lower bound here matching the $2.46003$ algorithmic base, no proof
that the 46-type recursive family is optimal among all algorithms, and no exact
height-4 computation. The gap between $9/4$ and $2.46003$ is genuine in the
arguments presented. Neither the finite data nor the worst-case query
literature closes it.

Task: “Open problem C0021.” Received 2026-11-13, approximately 06:05 +04
(Asia/Tbilisi, from the session start clock).
