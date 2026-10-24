# H0024 — directional closure structure, stable-envelope obstruction, and scale count

Status: **PARTIAL / OPEN**. This note does not settle the full critical-line phase diagram. It gives three new exact structural results for the admitted outside target H0024 and identifies why the full-source metric cannot improve by sharpening only the symmetric-radius comparison.

Target: Gustavo Oshiro de Carvalho, Fábio Prates Machado, José Hermenegildo Ramírez-González, *Extinction and Survival in an Interval-Activation Frog Model on Z with Random Survival Parameters and Symmetric Random Walks*, arXiv:2607.27082v1 (2026), Theorem 3.5(ii) and Remark 3.6.

Canonical claim: `operations/claims/H0024.md`.

Previous R7-05 result: `research7_2026-09-17/R7-05/artifacts/2026-09-17/2026-09-17T225126Z__H0024_factor_two_barrier_theorem.md`.

Throughout, `m=E[eta_0]`. On the critical line in the stable or finite-variance regimes, the source writes

`n P(D^-> >= n) / ell(n^r) -> kappa`.

The frozen full-source metric after the previous run is `G_crit=2`: universal survival constant `1` versus proved universal extinction constant `1/2` in the normalization `m kappa ell`.

## 1. Method B1 — change category: the exact model is an iid directed interval-closure process

For a site `x`, after all frogs initially at `x` are eventually activated, define

`R_x = max_{1<=i<=eta_x} D^->_{x,i}`,

`L_x = max_{1<=i<=eta_x} D^<-_{x,i}`,

with the maximum over the empty set equal to zero. The source's interval-activation convention implies that the entire contribution of site `x` is the integer interval

`J_x=[x-L_x,x+R_x] cap Z`.

The pairs `(L_x,R_x)` are iid over sites. They are generally *not* products within a site: left and right extremes of the same frog are dependent, and the site maxima may also be coupled through the random number of frogs. This matters because the older H0024 synthetic two-front script samples the two frontier growths independently and therefore cannot certify the actual frog process.

Define a finite integer interval `I=[a,b] cap Z` to be **closed** if

`J_x subseteq I` for every `x in I`,

or equivalently

`L_x <= x-a` and `R_x <= b-x` for every `x in I`.

### Proposition 1.1 — exact closure representation

Let `C(0)` be the set activated from the origin. Then:

1. `C(0)` is always an interval (possibly infinite).
2. `C(0)` is the smallest interval containing `0` that is closed under `x -> J_x`.
3. `C(0)` is finite if and only if there exists a finite closed interval containing `0`.
4. On the extinction event, `C(0)` is itself the unique minimal closed interval containing `0`.
5. The intersection of any two closed intervals with nonempty intersection is closed; the union of any two overlapping closed intervals is closed.

### Proof

Start from `C_0={0}` and recursively put

`C_{k+1}= union_{x in C_k} J_x`.

Because every `J_x` is an integer interval containing `x`, and because `C_k` is an interval by induction, the union is again an interval. Thus every `C_k` and `C(0)=union_k C_k` are intervals.

If `I` is a closed interval containing `0`, induction gives `C_k subseteq I` for all `k`, hence `C(0) subseteq I`. Conversely, if `C(0)` is finite, every site in it has already had its entire `J_x` exposed inside the iterative closure, so `J_x subseteq C(0)` for all `x in C(0)`; therefore `C(0)` is closed. This proves 1--4.

For 5, if `I,J` are closed and overlap, then for `x in I cap J`, `J_x` lies in both and hence in the intersection. Thus `I cap J` is closed. For `x in I union J`, it lies in at least one of the two intervals, so `J_x` lies in that interval and hence in the union. QED.

This reformulation is exact, not a comparison. It removes the deliberately lossy symmetric radius `D^*` and exposes the true object that must be controlled to close the source gap: an iid directed interval closure with a nontrivial within-site joint law `(L,R)`.

## 2. Stable-envelope obstruction: no uniform improvement can come from `D^*` alone

The previous run proved universal extinction whenever

`limsup ell(n^r) < 1/(2 m kappa)`

by upper-coupling to the symmetric site radius and using `P(D^*>=n)<=2P(D^->=n)` in tail form. One might hope simply to sharpen the factor `2` in the stable regime. The next theorem shows that this cannot improve the **uniform full-source constant**, because the factor approaches two as the stable index approaches one.

Fix `alpha in (1,2)`. Let `X=(X_t)` be the symmetric strictly `alpha`-stable Levy process appearing in the source functional limit, and put

`S_alpha = sup_{0<=t<=1} X_t`,

`T_alpha = -inf_{0<=t<=1} X_t`,

`M_alpha = sup_{0<=t<=1} |X_t| = max(S_alpha,T_alpha)`.

Let

`tau_+ = inf{t>=0:X_t>=1}`,

`tau_* = inf{t>=0:|X_t|>=1}`.

Self-similarity gives the distributional identities

`tau_+^(-1/alpha) =_d S_alpha`,

`tau_*^(-1/alpha) =_d M_alpha`.

Indeed, for `y>0`,

`P(tau_+^(-1/alpha) <= y)=P(tau_+ >= y^(-alpha))`

`=P(sup_{t<=y^(-alpha)}X_t <1)`

`=P(y^(-1) S_alpha <1)=P(S_alpha<y)`, up to null boundary events; the absolute version is identical.

The source's Proposition 3.4 proves for the one-sided displacement at `beta=1/alpha` that the critical coefficient is proportional to

`Gamma(1/alpha) E[tau_+^(-1/alpha)]`.

For the two-sided displacement, define the discrete exit time

`tau^* _n = inf{k>=0: |S_k|>=n}`.

Conditioning on the survival parameter gives the exact analogue

`P(D^*>=n | pi=p)=E[p^(tau^*_n)]`.

Repeating the source's regular-variation integral argument with `tau_n^*` is legitimate: functional convergence gives the two-sided exit-time limit, while the source's small-time domination transfers because

`e^{-s tau_n^*}=max(e^{-s tau_n^+},e^{-s tau_n^-}) <= e^{-s tau_n^+}+e^{-s tau_n^-}`

and symmetry makes the two terms identically distributed. Hence

`n P(D^*>=n)/ell(n^alpha) -> Gamma(1/alpha) E[tau_*^(-1/alpha)]`.

Therefore the exact stable-limit ratio is

`R_alpha := lim P(D^*>=n)/P(D^->=n) = E[M_alpha]/E[S_alpha]`.

(The equality is about the critical mixed tail constants, not the unconditioned fixed-time walk.)

### Proposition 2.1 — sharp uniform obstruction

For every `1<alpha<2`,

`2/alpha <= R_alpha <= 2`,

and consequently

`lim_{alpha downarrow 1} R_alpha = 2`.

Thus

`sup_{1<alpha<2} R_alpha = 2`.

### Proof

The upper bound is pathwise:

`M_alpha=max(S_alpha,T_alpha) <= S_alpha+T_alpha`.

By symmetry `E T_alpha=E S_alpha`, so `E M_alpha <=2E S_alpha`.

For the lower bound, `M_alpha>=|X_1|`. The continuous-time Spitzer identity for an integrable Levy process gives

`E S_alpha = integral_0^1 E[(X_t)^+]/t dt`.

The stable process is integrable for `alpha>1`; symmetry and self-similarity give

`E[(X_t)^+] = t^(1/alpha) E[(X_1)^+] = (1/2)t^(1/alpha)E|X_1|`.

Therefore

`E S_alpha = (alpha/2)E|X_1|`.

Combining `E M_alpha>=E|X_1|` with this identity yields

`R_alpha>=2/alpha`.

As `alpha downarrow1`, the lower bound tends to `2` and the universal upper bound is `2`, so the squeeze theorem gives `R_alpha->2`. QED.

### Consequence 2.2

For each fixed stable index, a source-style symmetric-radius extinction comparison can be written with its exact coefficient `R_alpha`, namely at least formally

`m kappa R_alpha * limsup ell(n^alpha) < 1`

is sufficient for extinction once the bidirectional radius barrier criterion is applied. But **uniformly over the source's full stable family `1<alpha<2`, no replacement of the union bound by an exact `D^*` asymptotic can push the full-source extinction constant above `1/2`**, because `R_alpha` approaches `2` as `alpha downarrow1`.

So the frozen metric `G_crit=2` can move only by exploiting the directional pair `(L,R)` or some equally source-specific structure. More polishing of the symmetric envelope is provably the wrong route for the full source.

## 3. Method B12 — a conserved leading closure exponent independent of left/right dependence

The exact directed closure representation admits a clean static theorem. Let

`q_n = P(R_0>n)=P(L_0>n)`

and

`j_{u,v}=P(L_0>u, R_0>v)`.

For `I_n=[0,n] cap Z`, independence across sites gives the exact product

`P(I_n is closed) = prod_{k=0}^n F(k,n-k)`,

where

`F(u,v)=P(L_0<=u,R_0<=v)=1-q_u-q_v+j_{u,v}`.

Assume only that

`q_n = O(1/n)`.

This is exactly the bounded critical-coefficient regime relevant to the unresolved constant window.

### Proposition 3.1 — logarithmic closure mass

Under `q_n=O(1/n)`,

`log P(I_n is closed) = -2 sum_{k=1}^n q_k + O(1)`.

The `O(1)` term may depend on the law but not on `n`. In particular, the within-site dependence between `L` and `R` changes the closure probability only by a bounded multiplicative factor on the logarithmic scale.

If moreover

`n q_n -> c in (0,infinity)`, then

`P(I_n is closed)=n^(-2c+o(1))`.

For the frog model in a convergent critical-line subcase `ell(n^r)->lambda`,

`c = m kappa lambda`.

### Proof

Write

`u_{k,n}=q_k+q_{n-k}-j_{k,n-k}`,

so the `k`th factor is `1-u_{k,n}`. First control the joint correction. Since an intersection is bounded by either marginal,

`j_{k,n-k} <= min(q_k,q_{n-k})`.

For all sufficiently large indices `q_s<=C/s`. Along `k+(n-k)=n`,

`min(q_k,q_{n-k}) <= C/max(k,n-k) <= 2C/n`

whenever both indices are in the tail; the finitely many boundary terms satisfy the same `O(1/n)` estimate using the large opposite index. Hence

`sum_{k=0}^n j_{k,n-k}=O(1)`.

Also

`sum_{k=0}^n (q_k+q_{n-k})^2 <=4 sum_{k=0}^n q_k^2=O(1)`.

Choose a fixed `K` such that `q_s` is small for `s>=K`. The finitely many factors with `k<K` or `n-k<K` have logarithms converging to finite constants (under the source model there is positive probability of no outward excursion across any fixed boundary). On the remaining factors, `u_{k,n}` is uniformly bounded away from one and

`log(1-u_{k,n})=-u_{k,n}+O(u_{k,n}^2)`.

Summing gives

`log P(I_n closed)`

`= -sum_k(q_k+q_{n-k}) + sum_k j_{k,n-k}+O(sum_k(q_k+q_{n-k})^2)+O(1)`

`= -2 sum_{k=1}^n q_k + O(1)`.

If `n q_n->c`, the harmonic-sum asymptotic is

`sum_{k<=n}q_k=c log n+o(log n)`,

which gives the power law. Finally, finite mean `eta_0` and the single-frog source asymptotic imply

`P(R_0>n)=E[1-(1-P(D^->n))^(eta_0)] ~ m P(D^->n)`,

so at `ell(n^r)->lambda`, `nq_n->m kappa lambda`. QED.

### Why this matters

The older H0024 memo guessed the exponent `2c` from synthetic and special-dependence calculations. Proposition 3.1 proves that exponent for the actual directed site law under the constant critical regime and, more generally, gives an `O(1)`-accurate logarithmic formula whenever `q_n=O(1/n)`. It does not assume left/right independence, asymptotic independence, finite second moment of `eta_0`, or the false relation `P(D^*)~2P(D^->)`.

The mechanism is simple but important: along a candidate interval of length `n`, every joint left/right correction has one threshold at least `n/2`, so its probability is `O(1/n)`; summing over the `n` sites costs only `O(1)`. The two marginal harmonic sums are the only logarithmically divergent terms.

## 4. Method B25 — count the same closed intervals in translation and scale

For each `n>=1`, let

`Z_n = # {a in {-n,...,0}: [a,a+n] is closed}`.

These are exactly the length-`n` closed intervals that contain the origin. Translation invariance and Proposition 3.1 give

`E Z_n = (n+1) P(I_n is closed)`.

If `nq_n->c`, then

`E Z_n = n^(1-2c+o(1))`.

Now count across scales as well:

`Z_{<=N}=sum_{n=1}^N Z_n`.

### Proposition 4.1 — the scale-summed first-moment transition is exactly `c=1`

If `nq_n->c`, then:

- for `c<1`, `E Z_{<=N}` diverges polynomially, with exponent `2-2c+o(1)`;
- for `c>1`, `E Z_{<infinity}<infinity`;
- at `c=1`, first-order information is insufficient and the second-order tail decides the sum.

In the refined boundary model

`q_n = 1/n + b/(n log n) + O(1/[n(log n)^(1+delta)] + 1/n^2)`,

Proposition 3.1 gives

`P(I_n closed) asymp 1/[n^2 (log n)^(2b)]`,

hence

`E Z_n asymp 1/[n (log n)^(2b)]`,

so

`sum_n E Z_n` converges exactly for `b>1/2` and diverges for `b<=1/2`.

### Proof

There are `n+1` translates of a length-`n` interval containing zero, so the first identity is immediate. If `p_n=n^{-2c+o(1)}`, then for every `epsilon>0` and all large `n`,

`n^{1-2c-epsilon} <= E Z_n <= n^{1-2c+epsilon}`.

The p-series test yields the first two statements and the growth exponent for `c<1`. For the second-order formula,

`sum_{k<=n} q_k = log n + b log log n + O(1)`,

and Proposition 3.1 supplies the displayed asymptotic; another integral test gives the `b=1/2` boundary. QED.

### Interpretation and exact failure

This is the first static calculation in the R7-05 line that naturally singles out the source's conjectural normalized threshold `c=1` **without assuming independent left/right reaches**. A fixed scale by itself misleadingly produces the exponent boundary `c=1/2`; summing over the `n` translations and then all scales supplies the missing scale dimension and moves the first-moment transition to `c=1`.

But this is **not yet an extinction theorem**. `E sum_n Z_n=infinity` does not imply that a closed interval containing the origin exists almost surely, because the events are strongly nested/correlated. This is the exact gluing failure. The full dynamic source problem has been reduced to converting scale-summed closed-interval abundance into an almost-sure trapping statement for the directed closure process. Any claim that the expectation divergence alone settles extinction would repeat the flaw in the old memo.

## 5. Additional deterministic structure for the next attack

The closed intervals form a useful lattice:

- overlapping closed intervals have closed union;
- intersecting closed intervals have closed intersection;
- on extinction, the activated cluster is the unique minimal closed interval containing the origin.

Therefore a successful next proof can target a renewal or conditional Borel-Cantelli theorem for *minimal* or *fresh-shell* closed intervals rather than trying to decorrelate arbitrary interval events. The strongest plausible route is to expose sites only when a frontier reaches them and prove that, for normalized coefficient `<1`, fresh annular shells supply enough conditional trapping mass across scales despite far-end revivals.

## 6. What is proved, what is not

Proved here:

1. An exact iid directed-interval closure formulation of the actual frog process.
2. In the stable critical limit, an exact symmetric-envelope ratio `R_alpha=E M_alpha/E S_alpha`, with `2/alpha<=R_alpha<=2` and `R_alpha->2` as `alpha downarrow1`; hence the full-source factor `2` cannot be improved uniformly by studying `D^*` alone.
3. For any symmetric directed site law with marginal `q_n=O(1/n)`, the exact leading closure formula `log P([0,n] closed)=-2 sum_{k<=n}q_k+O(1)`, independent of within-site left/right dependence at logarithmic order.
4. In the constant critical regime `nq_n->c`, the closure exponent is `2c`, and the expected number of closed intervals containing the origin, summed over scales, has its first-moment transition exactly at `c=1`.

Not proved:

- extinction for the actual frog process throughout `c<1`;
- survival/extinction at the equality line `c=1`;
- a full criterion for oscillatory slowly varying `ell`;
- any independent audit or publication-level novelty claim.

The frozen universal metric therefore remains

`G_crit: 2 -> 2` (**no movement**).

This run nevertheless rules out an entire class of metric-improvement attempts and identifies the precise remaining bridge: a scale-renewal/trapping theorem for the exact directed interval closure.
