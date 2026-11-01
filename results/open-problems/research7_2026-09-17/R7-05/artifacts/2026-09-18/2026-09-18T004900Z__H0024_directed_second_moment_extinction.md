Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding model/effort selector is exposed.

# H0024 — a dependence-robust directed-interval extinction theorem at the sharp coefficient 1

Status: **PARTIAL / OPEN for the full source phase diagram**, but this note closes the source's factor-four **strict-constant gap**: under the source hypotheses on the critical line, the sufficient extinction constant improves from `1/4` (source) and `1/2` (previous R7-05 work) to `1`, matching the source's sufficient survival constant. Equality and oscillatory cases crossing the threshold remain unresolved.

Target: Gustavo Oshiro de Carvalho, Fábio Prates Machado, José Hermenegildo Ramírez-González, *Extinction and Survival in an Interval-Activation Frog Model on Z with Random Survival Parameters and Symmetric Random Walks*, arXiv:2607.27082v1 (2026), Theorem 3.5(ii) / Remark 3.6 in the repository's numbering convention (Theorem 5 / Remark 6 in arXiv HTML).

Canonical claim: `operations/claims/H0024.md`.

Previous R7-05 structural result: `research7_2026-09-17/R7-05/artifacts/2026-09-17/2026-09-17T235600Z__H0024_directional_closure_structure.md` plus its immutable correction note.

The mathematical idea comes first: do **not** try to make a single candidate trap likely. Instead count a two-parameter rectangle of possible left/right trap boundaries. A first moment gives order `N^2 A_N^2`; a dependence-aware pair bound factorizes the two boundary displacements, giving a matching second moment. Paley-Zygmund then gives a scale-uniform positive probability of a trap; a tail 0-1 argument upgrades this to traps at arbitrarily large scales almost surely.

---

## 1. Abstract directed-interval model

Let `(L_x,R_x)_{x in Z}` be iid copies of a pair `(L,R)` of almost surely finite nonnegative integer-valued random variables. Dependence between `L` and `R` at the same site is arbitrary. Assume the two marginals agree,

`P(L>n)=P(R>n)=q_n`, `n>=0`,

and assume

`P(L=0,R=0)>0`.

Site `x` carries the interval

`J_x=[x-L_x,x+R_x] cap Z`.

Starting from the origin, repeatedly adjoin `J_x` whenever `x` has been reached. By the deterministic closure lemma proved in the preceding R7-05 run, the activated cluster is finite if and only if there exists a finite **closed interval** containing zero, where `[a,b]` is closed when `J_x subseteq [a,b]` for every integer `x in [a,b]`.

Define

`f_n:=1-q_n=P(R<=n)=P(L<=n)`

and the one-sided barrier product

`A_n:=prod_{k=0}^n f_k`, with `A_{-1}:=1`.

Because `P(R=0)>=P(L=0,R=0)>0`, we have `f_0>0`; hence every `A_n` is positive.

### Theorem 1 (directed second-moment extinction theorem)

If

`limsup_{n->infinity} n q_n < 1`,

then almost surely there exist arbitrarily large closed intervals containing the origin. In particular, the activated cluster from the origin is finite almost surely.

This theorem uses only iid sites, finite marks, equal left/right marginal tails, and the displayed strict tail condition. No independence between `L` and `R` at one site is assumed.

---

## 2. Closed-interval probability is comparable to `A_n^2`

Let

`p_n:=P([0,n] is closed)`.

Writing

`F(u,v):=P(L<=u,R<=v)`,

site independence gives exactly

`p_n=prod_{k=0}^n F(k,n-k)`.

Choose a constant `c` satisfying

`limsup n q_n < c < 1`.

Then for all sufficiently large `n`,

`q_n <= c/n`.

We prove that there are constants `0<c_1<=C_1<infinity` such that for all sufficiently large `n`,

`c_1 A_n^2 <= p_n <= C_1 A_n^2`.    (2.1)

### Upper bound

Since

`F(k,n-k) <= min(f_k,f_{n-k})`,

splitting the product at `n/2` yields

`p_n <= A_{floor(n/2)}^2`

(up to deleting at most one extra factor, which only weakens the upper bound). Moreover,

`log(A_{floor(n/2)}/A_n)
 = -sum_{r=floor(n/2)+1}^n log(1-q_r)`.

For large `r`, `q_r<=c/r` and therefore `-log(1-q_r)<=q_r+Cq_r^2`. Hence the last display is bounded uniformly in `n`. Thus

`p_n <= C_1 A_n^2`.

### Lower bound

Put

`j_{u,v}:=P(L>u,R>v)`.

Then

`F(u,v)=1-q_u-q_v+j_{u,v}`

and

`f_u f_v=1-q_u-q_v+q_u q_v`.

Since `j_{u,v}>=0`,

`F(u,v) >= f_u f_v-q_u q_v`.

Because `f_u,f_v>=f_0>0`,

`F(u,v)/(f_u f_v) >= 1 - q_u q_v/f_0^2`.    (2.2)

For `u=k`, `v=n-k`, at least one of `u,v` is at least `n/2`, so the maximum of the error term in (2.2) is `O(1/n)`. Also

`sum_{k=0}^n q_k q_{n-k}=O((log n)/n)`.    (2.3)

Indeed, for `k<=n/2`, `q_{n-k}=O(1/n)` and `sum_{k<=n/2}q_k=O(log n)`; the other half is symmetric.

For all large `n`, every error in (2.2) is at most `1/2`, so `log(1-x)>=-2x` gives

`prod_{k=0}^n F(k,n-k)/(f_k f_{n-k}) >= exp(-O((log n)/n))`.

But

`prod_{k=0}^n f_k f_{n-k}=A_n^2`.

Thus the ratio is bounded below by a positive constant, proving the lower half of (2.1). Notice that the within-site joint law contributes only a favorable term `j_{u,v}` to this estimate.

---

## 3. A regular-variation-free summation lemma

The proof needs no existence of `n q_n -> c_0`; only the strict upper bound `q_n<=c/n` with `c<1` eventually.

### Lemma 2

There is a constant `C` such that for every sufficiently large `N` and every `0<=d<=N`,

`A_{d-1} <= C A_N (N/(d+1))^c`,    (3.1)

where `A_{-1}=1`. Consequently,

`sum_{d=0}^N A_{d-1} <= C N A_N`.    (3.2)

Also, uniformly for `m in [N,4N]`,

`A_m >= C^{-1} A_N`.    (3.3)

### Proof

For large `d<N`,

`log(A_d/A_N)
 = -sum_{k=d+1}^N log(1-q_k)
 <= C_0 + c sum_{k=d+1}^N 1/k
 <= C_1+c log(N/d)`,

where the convergent `sum q_k^2` contribution is absorbed in `C_0`. Enlarging the constant handles finitely many small `d` and the shift from `A_d` to `A_{d-1}`. This proves (3.1).

Summing (3.1) and using `c<1`,

`sum_{d=0}^N A_{d-1}
 <= C A_N N^c sum_{d=1}^{N+1} d^{-c}
 <= C' N A_N`,

which is (3.2).

Finally,

`log(A_N/A_{4N})
 = -sum_{k=N+1}^{4N} log(1-q_k)
 <= C_2+c log 4`,

so `A_{4N}>=C^{-1}A_N`; monotonicity of `A_m` gives (3.3).

---

## 4. B3/B19 core: a two-parameter trap finder

For an integer `N>=1`, consider all intervals

`I_{i,j}:=[-i,j]`, `N<=i,j<=2N`,

and let

`Z_N:=sum_{i=N}^{2N} sum_{j=N}^{2N} 1_{ {I_{i,j} closed} }`.

This is the constructive search object: inspect all candidate left/right boundary pairs in the `N by N` square. The theorem will show that this search succeeds with probability bounded away from zero uniformly in scale.

For every such `(i,j)`, the length `i+j` lies in `[2N,4N]`. By (2.1) and (3.3),

`P(I_{i,j} closed)=p_{i+j} >= c_2 A_N^2`.

Therefore

`E Z_N >= c_3 N^2 A_N^2`.    (4.1)

The crucial point is to prove a matching second moment without assuming left/right independence at a site.

---

## 5. B21 core: intersection plus two independent wings

Take two candidates `I_{i,j}` and `I_{i',j'}`. Write

`i_0=min(i,i')`, `j_0=min(j,j')`,

`d=|i-i'|`, `e=|j-j'|`.

If both intervals are closed, then their intersection

`[-i_0,j_0]`

is closed: every site mark in the intersection lies in both original intervals and therefore in their intersection.

Suppose, for example, that `i>=i'`. The left wing consists of the sites

`-i,-i+1,...,-i'-1`.

For the larger interval to be closed, the successive left reaches on these `d` sites must satisfy

`L_{-i+t}<=t`, `t=0,...,d-1`.

Ignoring all other constraints can only increase probability, so the left wing contributes at most

`prod_{t=0}^{d-1}P(L<=t)=A_{d-1}`.

The same statement holds whichever interval has the longer left side. Analogously, the right wing contributes at most `A_{e-1}`. The core, left wing, and right wing use disjoint sets of sites, hence are independent across those site sets. Therefore

`P(I_{i,j} and I_{i',j'} both closed)
 <= p_{i_0+j_0} A_{d-1} A_{e-1}`.    (5.1)

Because `i_0+j_0>=2N`, the elementary half-product upper bound from Section 2 gives

`p_{i_0+j_0} <= C A_N^2`.

Thus

`P(I_{i,j}, I_{i',j'} closed)
 <= C A_N^2 A_{d-1}A_{e-1}`.    (5.2)

Now

`sum_{i,i'=N}^{2N} A_{|i-i'|-1}
 <= C N sum_{d=0}^{N}A_{d-1}
 <= C N^2 A_N`

by Lemma 2. The same estimate holds for the `j,j'` sum. Summing (5.2),

`E Z_N^2 <= C A_N^2 (N^2 A_N)^2
 = C N^4 A_N^4`.    (5.3)

Combining (4.1) and (5.3), Paley-Zygmund yields a constant `delta>0`, independent of `N`, such that

`P(Z_N>0)>=delta`    (5.4)

for all sufficiently large `N`.

This is the key gluing theorem that the preceding run was missing. The extra free choice of **both** boundaries is exactly what recovers the power lost by looking at one fixed interval.

---

## 6. Positive probability at every scale becomes almost sure trapping

Set `N_m=2^m` and let

`E_infty={Z_{N_m}>0 for infinitely many m}`.

From (5.4),

`P(E_infty)>=limsup_m P(Z_{N_m}>0)>=delta>0`.

We claim `E_infty` is a tail event of the iid site environment. Change arbitrarily the marks at finitely many sites, keeping them finite. Any closed interval counted by `Z_{N_m}` has both boundary distances at least `N_m`. For each modified site, once `m` is large enough, both boundaries lie farther away than the old and new finite left/right reaches at that site. Thus changing finitely many coordinates cannot change whether closed intervals occur for infinitely many dyadic scales. Hence `E_infty` is measurable with respect to the tail sigma-field.

Kolmogorov's zero-one law now gives

`P(E_infty)=1`.

Therefore almost surely there are arbitrarily large closed intervals containing zero. In particular, at least one finite closed interval contains zero, and the deterministic closure lemma implies that the activated cluster from zero is finite. This completes the proof of Theorem 1.

---

## 7. Application to H0024

For H0024, define the site extrema

`R_x=max_{1<=i<=eta_x} D^->_{x,i}`,

`L_x=max_{1<=i<=eta_x} D^<-_{x,i}`,

with empty maximum zero. The pairs `(L_x,R_x)` are iid across sites and have equal marginals by symmetry. Their within-site dependence is irrelevant to Theorem 1.

Let

`s_n:=P(D^-> >= n)`.

For integer `n>=0`,

`q_n:=P(R_0>n)=1-E[(1-s_{n+1})^{eta_0}]`.

Since `s_n->0` and

`0 <= [1-(1-s)^eta]/s <= eta`,

while the quotient converges pointwise to `eta` as `s downarrow0`, dominated convergence and `m:=E[eta_0]<infinity` give

`q_n/s_{n+1} -> m`.    (7.1)

The source's Proposition 3.4 / Theorem 3.5 critical asymptotic is

`n s_n / ell(n^r) -> kappa`.    (7.2)

Slow variation absorbs the unit shift. Combining (7.1)-(7.2),

`n q_n / ell(n^r) -> m kappa`.    (7.3)

The boundary atom required above also holds. Conditional on any finite `eta_0=k`, there is strictly positive probability that all `k` frogs die before taking a first step, because every survival parameter lies in `(0,1)`. Since `eta_0<infinity` almost surely, averaging yields

`P(L_0=0,R_0=0)>0`.

Hence, if

`limsup_{n->infinity} ell(n^r) < 1/(m kappa)`,

then (7.3) implies

`limsup n q_n <1`,

and Theorem 1 proves almost-sure extinction.

The source already proves survival with positive probability under

`liminf ell(n^r) > 1/(m kappa)`.

Therefore the strict constants now match exactly:

**extinction:** `limsup ell(n^r) < 1/(m kappa)`;

**survival:** `liminf ell(n^r) > 1/(m kappa)`.

For the frozen R7-05 metric

`G_crit=C_surv/C_ext`,

this moves

`G_crit: 2 -> 1`.

For a convergent critical coefficient `ell(n^r)->lambda`, this gives a sharp threshold away from equality:

- `lambda<1/(m kappa)` => extinction almost surely;
- `lambda>1/(m kappa)` => survival with positive probability.

The equality case and general oscillatory slowly varying functions that repeatedly cross the threshold are not determined here, so the full source problem remains **PARTIAL / OPEN**.

---

## 8. Relation to the analogous rumour model and novelty caution

Roy and Saha, *How Fast do Rumours Spread?*, Journal of Statistical Physics 191 (2024), Proposition 3.1, give a product-series criterion for a symmetric one-radius rumour process on `Z`. Its barrier product `a_n=prod_{i=0}^n P(I_0<=i)` is the direct analogue of `A_n` above. Their proof uses an iid time-layer construction to obtain independent barrier trials.

The H0024 site law is different: it is a directed pair `(L_x,R_x)` with potentially strong within-site dependence inherited from a common collection of frog trajectories. The argument above does not replace that law by independent sides or a symmetric envelope. Instead, it obtains independence only from **disjoint spatial wings**, after intersecting two candidate closed intervals.

A bounded search dated 2026-09-18 found the current H0024 primary version still at arXiv:2607.27082v1 and found no later explicit resolution of Remark 3.6 or this exact directed-pair theorem. This is negative evidence only; publication novelty is **UNVERIFIED**.

---

## 9. What remains

This run materially moves the frozen constant metric, so stagnation resets. It does not satisfy source-level closure, because the source admission deliberately requires the entire critical-line phase diagram, including equality and nonconvergent slowly varying factors.

Natural next questions, with a different Section-B triple, are:

1. decide the exact equality case `lim ell(n^r)=1/(m kappa)` using second-order behavior of the barrier product;
2. determine whether oscillatory slowly varying factors can produce survival/extinction behavior not classified by liminf/limsup separation;
3. seek an exact necessary-and-sufficient directed-pair product/renewal criterion generalizing Roy-Saha Proposition 3.1.

No independent closure audit is claimed. Current audit count remains `P26 0/1`, distinct OTHER-track `0/1`.