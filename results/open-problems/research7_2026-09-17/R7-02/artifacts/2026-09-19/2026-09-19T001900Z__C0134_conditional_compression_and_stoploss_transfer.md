Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# C0134 — conditional compression, stop-loss duality, and hostile-tail stress test

Date: 2026-09-19 UTC  
Slot: `R7-02 Finite Certificate Research`  
Native ID: `6aabe797a39081919acc889f29f4c556`  
Target: `C0134` — Kosygina–Zerner, *Excited random walks: results, methods, open problems*, Problem 5.3  
Run-start master: `6c7513beb44088fffa157f558b670f7aefbd8e75`  
Fresh master before delivery work: `6c246a0dabaf517ebfa34111d7d95d0bc2842efd`  
Previous report: `research7_2026-09-17/R7-02/runs/2026-09-18/2026-09-18T232500Z__report.md` @ `9eb0d677e3cc985db458d3dec3bcd612a14fc6f7`

Frozen source metric remains

\[
\boxed{M_{\rm clause}:2/2\to2/2\quad\text{NO MOVEMENT}.}
\]

This note executes the prescribed nonrepeating methods **B11 / B23 / B30**.  The point is not to add a fictitious third source clause.  It attacks the last material mathematical verification risk from the previous report: the transfer from an arbitrary integrable emigration law to a bounded source-valid comparator.

## 1. Scalar object inherited from the cumulative reduction

For a nonnegative integer-valued emigration variable `N`, define the front-loaded branching-like chain

\[
Z^{N}_{n+1}=S_{(Z^N_n+1-N_n)_+},
\qquad
S_r=\xi_1+\cdots+\xi_r,
\]

where `N_n` are iid copies of `N` and

\[
\mathbb P(\xi=j)=2^{-(j+1)},\qquad j\ge0,
\qquad E\xi=1.
\]

For the positive-cookie source problem at finite drift, Bernoulliization gives

\[
\mu:=EN=\delta<\infty,
\qquad
p_0:=P(N=0)>0.
\]

The second assertion follows from `(WEL)` in the left direction together with finite total positive drift: on the positive-probability event that every left transition is positive, all Bernoulliization parameters are strictly below one; because their sum is finite almost surely, the product of their failure probabilities is positive.

The cumulative proof already established a stackwise coupling under which the original backward chain dominates `Z^N` generation by generation.  Thus, in the transient range `1<delta<=2`, it suffices to show that the first-cycle area of `Z^N` has infinite mean.

## 2. B30 — one-block tail compression gives a universal bounded comparator

The earlier proof used hand-built comparators on `{0,1,2}` and `{0,2,3}`.  They are unnecessary.  There is a canonical bounded comparator for every integrable `N` that preserves both the mean and the exact zero mass.

### Lemma 2.1 (conditional two-point compression)

Let `N` be nonnegative integer-valued with finite mean `mu>0` and

\[
p_0=P(N=0)<1,
\qquad q=1-p_0.
\]

Set

\[
m:=E[N\mid N>0]=\frac{\mu}{q},
\qquad k:=\lfloor m\rfloor,
\qquad \theta:=m-k\in[0,1).
\]

Define the bounded integer-valued law `L` by

\[
P(L=0)=p_0,
\]

and, conditionally on `L>0`,

\[
P(L=k\mid L>0)=1-\theta,
\qquad
P(L=k+1\mid L>0)=\theta.
\]

Then

\[
P(L=0)=P(N=0),
\qquad EL=EN=\mu,
\qquad \boxed{L\le_{\rm cx}N}.
\]

#### Proof

The mean is immediate:

\[
EL=q\bigl((1-\theta)k+\theta(k+1)\bigr)=qm=\mu.
\]

Let `phi` be any convex function on the nonnegative integers for which the expectations below are defined.  Let `\bar\phi` be its piecewise-linear interpolation on `[0,\infty)`.  Discrete convexity means the slopes `phi(j+1)-phi(j)` are nondecreasing, hence `\bar\phi` is convex on the real line.

Condition on positivity.  Since `N\mid\{N>0\}` is integer-valued with mean `m`, Jensen gives

\[
E[\phi(N)\mid N>0]
=E[\bar\phi(N)\mid N>0]
\ge \bar\phi(m)
=(1-\theta)\phi(k)+\theta\phi(k+1)
=E[\phi(L)\mid L>0].
\]

The two laws place exactly the same mass `p_0` at zero, so after adding the common term `p_0\phi(0)` we obtain

\[
E\phi(L)\le E\phi(N).
\]

Together with equality of means, this is exactly `L<=cx N`.  Equivalently, one may restrict to the stop-loss generators `(x-t)_+`, whose expectations are finite because `EN<infinity`.  `square`

### Why this is source-valid

For the cookie model whose first `L` cookies are deterministic right cookies and all later cookies are fair:

- site stacks are iid;
- the stack depth is bounded by `k+1`;
- every cookie is positive;
- the drift parameter is `EL=mu`;
- `(WEL)` holds: right probabilities are always positive, while on the event `L=0` (probability exactly `p_0>0`) every left probability is `1/2`.

Therefore for every `1<mu<=2` this is a bounded source-valid model lying exactly inside Kosygina–Zerner Theorem 5.2 at the **same drift value** as the arbitrary law `N`.

**B30 outcome: SUCCESS.**  A single conditional mean-preserving compression replaces all special comparator formulas and works for every integrable emigration law with positive zero mass.

## 3. B11 — stop-loss duality proves the finite-time transfer exactly

The remaining issue is whether `L<=cx N` is in the correct direction for the clipped random-sum branching kernel.  Instead of relying on a generic composition statement, we prove the order on the stop-loss generators that characterize increasing-convex order.

For an integer threshold `t>=0`, let

\[
\varphi_t(x)=(x-t)_+,
\qquad
H_t(r):=E\,(S_r-t)_+.
\]

### Lemma 3.1 (exact increment formula)

For every `r>=0`,

\[
H_t(r+1)-H_t(r)=E\,q_t(S_r),
\]

where

\[
q_t(s)=
\begin{cases}
2^{s-t},&s<t,\\
1,&s\ge t.
\end{cases}
\]

In particular, `H_t` is increasing and convex in `r`.

#### Proof

Condition on `S_r=s`.  If `s>=t`, then

\[
E[(s+\xi-t)_+-(s-t)_+]=E\xi=1.
\]

If `s<t`, put `d=t-s>=1`.  Then

\[
E[(s+\xi-t)_+]=E(\xi-d)_+
=\sum_{j=d+1}^{\infty}P(\xi\ge j)
=\sum_{j=d+1}^{\infty}2^{-j}
=2^{-d}=2^{s-t}.
\]

Thus the displayed increment formula holds.  The function `q_t` is increasing in `s`, while `S_{r+1}>=S_r` under the natural coupling.  Hence `E q_t(S_r)` is nondecreasing in `r`, proving convexity.  Monotonicity is obvious from nonnegative increments.  `square`

For an emigration law `M`, write

\[
(K_M\varphi_t)(x)
:=E\,\varphi_t\!\left(S_{(x+1-M)_+}\right)
=E\,H_t((x+1-M)_+).
\]

Because `H_t` is convex and nondecreasing, both maps

\[
m\mapsto H_t((x+1-m)_+)
\quad\text{and}\quad
x\mapsto H_t((x+1-m)_+)
\]

are convex; the second is also increasing.  Therefore `L<=cx N` gives pointwise

\[
\boxed{K_L\varphi_t(x)\le K_N\varphi_t(x)}
\qquad\forall x,t\in\mathbb Z_+,
\]

and each kernel sends a stop-loss generator to an increasing convex function of the current population.

Every increasing convex function on `Z_+` with finite expectations is an affine increasing term plus a nonnegative combination/monotone limit of these stop-loss generators.  Consequently each kernel preserves increasing convexity, and the pointwise inequality extends to all increasing convex test functions.

Starting both chains from zero, induction therefore yields the exact finite-time order

\[
\boxed{Z_n^L\le_{\rm icx}Z_n^N\qquad\forall n\ge0.}
\]

In particular,

\[
\boxed{E_0Z_n^L\le E_0Z_n^N\qquad\forall n.}
\]

No moment assumption on `N` beyond `EN<infinity` enters this argument.  The clipping makes every one-step test as a function of `N` bounded above at fixed current state, while finite-time first moments remain finite from a zero start.

**B11 outcome: SUCCESS.**  The universal transfer is now reduced to exact stop-loss generators with an explicit geometric-offspring increment formula.  This independently confirms the direction of every convex-order inequality used in the cumulative proof.

## 4. B23 — hostile rare-tail family and failure of ordinary stochastic order

To try to break the transfer, consider for every integer `K>=5`

\[
P(N_K=0)=\frac12,
\qquad
P(N_K=1)=\frac{K-4}{2(K-1)},
\qquad
P(N_K=K)=\frac{3}{2(K-1)}.
\]

These probabilities sum to one and

\[
EN_K
=\frac{K-4+3K}{2(K-1)}=2.
\]

As `K` grows, the last atom becomes rarer and farther away, so this is a finite exact stress family for the kind of very long emigration tail that could have invalidated an argument silently relying on boundedness.

The conditional positive mean is

\[
E[N_K\mid N_K>0]=4.
\]

Hence Lemma 2.1 gives the same comparator for every `K`:

\[
P(L=0)=P(L=4)=\frac12.
\]

The comparison is genuinely not pathwise.  At current population `x=K-1`, the number of offspring families before reproduction is

\[
R_L=(K-L)_+
=\begin{cases}K,&1/2,\\K-4,&1/2,
\end{cases}
\]

whereas

\[
R_{N_K}=(K-N_K)_+
=\begin{cases}
K,&1/2,\\
K-1,&(K-4)/(2(K-1)),\\
0,&3/(2(K-1)).
\end{cases}
\]

Thus

\[
P(R_L\ge1)=1>P(R_{N_K}\ge1),
\]

but

\[
P(R_L\ge K-1)=\frac12
<\frac12+\frac{K-4}{2(K-1)}
=P(R_{N_K}\ge K-1).
\]

So neither parent-count law stochastically dominates the other.  This hostile family defeats any attempted proof based on ordinary stochastic domination or a monotone coupling at fixed equal drift.

It does **not** defeat the increasing-convex transfer: Lemma 3.1 proves the stop-loss inequalities at every threshold and every generation, uniformly in `K`.  In particular the rare huge emigration atom cannot reverse the only order actually used by the proof.

**B23 outcome: COUNTEREXAMPLE SEARCH FAILED AGAINST THE CLAIM, BUT FOUND A REAL OBSTRUCTION TO A STRONGER ROUTE.**  The transfer survives an explicit arbitrarily long-tail family, while ordinary stochastic domination provably fails.

## 5. Direct consequence for the zero-speed branch

Let `1<mu=EN<=2`, `p_0>0`, and let `L` be the conditional two-point compression from Lemma 2.1.  The bounded cookie environment generated by `L` has the same drift `mu` and satisfies `(IID)+(BD)+(WEL)+(POS1)`.  Kosygina–Zerner's bounded theorem gives zero speed in this range; the source backward-branching/regeneration identity therefore gives

\[
E_0\sigma_L<\infty,
\qquad
E_0A_L=\infty,
\qquad
A_L:=\sum_{n<\sigma_L}Z_n^L.
\]

The previous R7-02 Abel first-return identity converts this cycle divergence into

\[
(1-s)\sum_{n\ge0}E_0Z_n^L s^n\longrightarrow\infty
\qquad(s\uparrow1).
\]

By the finite-time order just reproved,

\[
(1-s)\sum_{n\ge0}E_0Z_n^N s^n
\ge
(1-s)\sum_{n\ge0}E_0Z_n^L s^n,
\]

so the Abel mean for `N` also diverges.  If the first-cycle area `A_N` had finite expectation, then `A_N>=sigma_N-1` would imply `E sigma_N<infinity`, and the same exact first-return transform would instead give the finite limit

\[
\lim_{s\uparrow1}(1-s)\sum_{n\ge0}E_0Z_n^N s^n
=\frac{E_0A_N}{E_0\sigma_N}<\infty,
\]

a contradiction.  Hence

\[
\boxed{E_0A_N=\infty\qquad(1<EN\le2,\ P(N=0)>0).}
\]

Combined with the already established stackwise front-loading domination, this supplies the difficult `1<delta<=2` zero-speed branch for the original positive-cookie environment.  The source handles `delta<=1`, and finite-depth truncation plus monotonicity handles `delta>2`, including `delta=infinity`.

Thus this run finds **no new mathematical gap** in the candidate source-level proof.  It instead removes a proof-complexity risk: the arbitrary-`N` transfer can be presented with one canonical bounded compression and an exact stop-loss calculation.

## 6. Dated source/prior-art check — 2026-09-19 UTC

Fresh checks made in this run:

1. Original source: Kosygina–Zerner, *Excited random walks: results, methods, open problems*, arXiv:1204.1895 / Bull. Inst. Math. Acad. Sin. 8 (2013).  The printed source has Theorem 5.2 under `(IID)+(BD)+(WEL)` and immediately asks in Problem 5.3 whether `(BD)` can be replaced by `(POS1)`.
2. Omar Chakhtoun, *One-Dimensional Excited Random Walk with Unboundedly Many Excitations Per Site* (PhD dissertation, 2019).  The current CUNY record explicitly says the theory requires a tail-decay estimate on the number of excitations per site.  This public description does not state the unrestricted theorem here.
3. Nicholas Travers, *Excited random walk in a Markovian environment* (EJP 23 (2018), article 43) treats a structured Markovian environment class; its abstract does not state the unrestricted iid arbitrary positive-stack theorem of Problem 5.3.
4. Bounded current searches through 2026-09-19 did not locate a paper explicitly advertising resolution of literal Problem 5.3.  This is negative evidence only and is **not** a novelty certificate.

No novelty claim is made.  The classical branching-with-migration literature and the inaccessible/full Chakhtoun theorem text remain prior-art risks for the unrestricted random-emigration transfer, even though the bounded comparator mechanism itself is classical-shaped.

## 7. Status and remaining obligations

Mathematical status remains **CANDIDATE SOURCE-LEVEL COMPLETE**.  Operational status remains **PARTIAL** because closure still requires:

- theorem-level prior-art reconciliation, especially the full Chakhtoun dissertation and the classical random-migration literature;
- synchronization of the self-contained paper package to the cleaner conditional-compression/stop-loss proof;
- an actual independent P26 audit;
- one distinct OTHER-track independent audit.

The frozen metric is already saturated and therefore does not move.  This is the fifth ordinary no-movement research run in the current streak (`4 -> 5`).  Under the owner protocol, one further unchanged ordinary run reaches the six-run CLOSABLE retirement threshold.
