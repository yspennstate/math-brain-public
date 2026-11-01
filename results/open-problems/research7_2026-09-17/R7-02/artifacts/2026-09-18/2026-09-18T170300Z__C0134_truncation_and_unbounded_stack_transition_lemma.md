Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding selector is exposed.

# C0134 — truncation proof for the ballistic half and a universal transition lemma for unbounded positive stacks

## 1. Source target and scope

Target C0134 is Kosygina–Zerner, *Excited random walks: results, methods, open problems*, Problem 5.3. Under `(IID)+(WEL)+(POS1)` in one dimension, write

\[
 d_i(\omega):=2\omega(0,1,i)-1\in[0,1],\qquad
 D_\infty(\omega):=\sum_{i\ge1}d_i(\omega),\qquad
 \delta:=\mathbb E D_\infty\in[0,\infty].
\]

The full source asks whether the speed threshold from the bounded-stack theorem remains

\[
 v=0\quad(\delta\le2),\qquad v>0\quad(\delta>2)
\]

when `(BD)` is replaced by `(POS1)`.

This note proves the entire `delta>2` clause, reduces every `delta<2` case to the critical `delta=2` case by an explicit monotone strengthening, and proves exact first- and second-order asymptotics plus a one-step CLT for the branching-like transition `F_m` without `(BD)`. It does **not** prove the remaining critical zero-speed assertion.

No result from the neighboring R7-05/C0130 escape-probability project is used.

## 2. B2 obstruction search: where can a counterexample still live?

The source's Theorem 3.10 already yields recurrence for `delta<=1` under the positive-cookie hypotheses (the weak-ellipticity assumption excludes the exceptional deterministic forced-right stack), and Theorem 4.1 supplies an almost-sure deterministic speed. Hence

\[
\delta\le1 \implies v=0.
\]

Section 3 below proves `delta>2 => v>0`. Therefore a counterexample to Problem 5.3, if one exists at all, must satisfy

\[
\boxed{1<\delta\le2\quad\text{and}\quad v>0.}
\]

The source-level uncertainty is thereby localized to the right-transient but purportedly sub-ballistic strip, with the critical endpoint `delta=2` singled out further in Section 4.

## 3. B19 constructive truncation: the full `delta>2` clause

### Theorem 3.1
Assume `(IID)+(WEL)+(POS1)` and `delta>2`, allowing `delta=+infinity`. Then the excited random walk has strictly positive limiting speed.

### Proof
For an integer `M>=1`, define the truncated stack law by keeping the first `M` cookies unchanged and replacing all later cookies by placebo cookies:

\[
 \omega^{(M)}(x,1,i)=
 \begin{cases}
 \omega(x,1,i),&i\le M,\\
 1/2,&i>M.
 \end{cases}
\]

This transformation is performed independently site by site, so `(IID)` is preserved. It gives `(BD)` with bound `M`. It preserves `(WEL)`: on any event on which all original left- and right-step probabilities required by `(WEL)` are positive, the post-`M` probabilities become exactly `1/2`, hence remain positive. It also preserves `(POS1)`.

Its drift parameter is

\[
 \delta_M=\mathbb E\sum_{i=1}^M d_i.
\]

Because the summands are nonnegative, monotone convergence gives `delta_M ↑ delta`, including when `delta=+infinity`. Thus some finite `M` satisfies `delta_M>2`.

The source's Theorem 5.2 applies to the truncated environment and yields a deterministic speed

\[
 v_M>0.
\]

Pathwise in the cookie environment,

\[
 \omega(x,1,i)\ge \omega^{(M)}(x,1,i)
\]

for every site and visit index, because all original cookies are positive and every discarded cookie is replaced by `1/2`. The source's monotonicity Proposition 4.2 applies once the two limiting speeds exist. The original speed exists by Theorem 4.1 under `(SE)+(POS1)` (and `(IID)` implies `(SE)`), while the truncated speed exists by the same theorem. Hence

\[
 v\ge v_M>0.
\]

This proves the complete `delta>2` source clause. ∎

### Consequence for the frozen metric
The source has two clauses. The positive-speed clause is now proved under the full source hypotheses, so the admission metric satisfies

\[
\boxed{M_{\rm clause}\ge1/2.}
\]

No statement about the second clause is included in this movement.

## 4. B19/B16 critical strengthening: all `delta<2` reduces to `delta=2`

The next lemma is useful because speed is monotone in cookie strength in the positive environment.

### Lemma 4.1 (finite-coordinate strengthening to critical drift)
Let `(IID)+(WEL)+(POS1)` hold with finite `delta<2`. There is another `(IID)+(WEL)+(POS1)` cookie law `P^+`, obtained by strengthening only finitely many cookie coordinates at each site, such that

1. `P^+` dominates `P` coordinatewise;
2. its expected total drift is exactly `delta^+=2`.

### Proof
Let

\[
 c_i:=\mathbb E(1-d_i).
\]

Since `sum_i E d_i=delta<infinity`, we have `E d_i ->0`, hence `c_i->1`. In particular, `sum_i c_i=+infinity`.

Set `r:=2-delta>0`. Because the partial sums of `c_i` diverge, choose finitely many coefficients `a_i in [0,1/2]` with finite support such that

\[
 \sum_i a_i c_i=r.
\]

For example, add terms with coefficient `1/2` until the accumulated sum would exceed `r`, and choose the final coefficient in `[0,1/2]` to hit `r` exactly.

At each site define

\[
 p_i^+:=p_i+a_i(1-p_i).
\]

Then `p_i^+>=p_i>=1/2`, and the new drift of cookie `i` is

\[
 d_i^+=2p_i^+-1=d_i+a_i(1-d_i).
\]

Thus the law is coordinatewise stronger and

\[
 \delta^+
 =\delta+\sum_i a_i\mathbb E(1-d_i)
 =\delta+r=2.
\]

The sitewise deterministic transformation preserves `(IID)`. It preserves `(WEL)` because every changed coordinate uses `a_i<=1/2<1`, so

\[
 1-p_i^+=(1-a_i)(1-p_i)>0
\]

whenever the original left-step probability was positive; unchanged coordinates are unaffected. ∎

### Corollary 4.2
If every `(IID)+(WEL)+(POS1)` law with `delta=2` has zero speed, then every such law with `delta<2` also has zero speed.

### Proof
Given `delta<2`, use Lemma 4.1. By speed monotonicity,

\[
 0\le v(P)\le v(P^+).
\]

If the critical theorem gives `v(P^+)=0`, then `v(P)=0`. ∎

Combining Theorem 3.1 and Corollary 4.2, **Problem 5.3 is reduced to the single critical assertion**

\[
\boxed{\delta=2\implies v=0.}
\]

The reduction is source-valid: it does not impose a moment assumption on the random stack length or on `D_infty` beyond the source's finite critical value `E D_infty=2`.

## 5. B16 exact transition analysis without bounded stacks

We now analyze the source's branching-like transition in a fresh positive cookie stack. This is the part of the bounded-stack proof where `(BD)` had previously been used to obtain a geometric offspring law after finitely many cookies.

Fix a fresh random stack with drifts `(d_i)_{i>=1}` and independent uniforms `(U_i)_{i>=1}`. Define signs

\[
 B_i:=\begin{cases}
 +1,&U_i\le (1+d_i)/2,\\
 -1,&U_i>(1+d_i)/2.
 \end{cases}
\]

Conditional on the stack, `E[B_i | omega]=d_i`. Let `T_m` be the trial index of the `m`-th success (`B_i=+1`), and let

\[
 F_m:=T_m-m
\]

be the number of failures before the `m`-th success. This is exactly the one-site transition used in the backward edge-crossing chain

\[
 V_{k+1}=F^{(k)}_{V_k+1}
\]

with independent copies across sites under `(IID)`.

For finite `delta=E D_infty`, define the consumed and residual drift

\[
 D_m:=\sum_{i\le T_m}d_i,
 \qquad
 R_m:=\sum_{i>T_m}d_i,
 \qquad
 r_m:=\mathbb E R_m.
\]

### Lemma 5.1 (exact mean identity)
For every `m>=1`,

\[
\boxed{\mathbb E F_m=m-\delta+r_m,}
\qquad
0\le r_m\le \mathbb E\sum_{i>m}d_i\longrightarrow0.
\]

### Proof
Let

\[
 M_n:=\sum_{i=1}^n(B_i-d_i).
\]

Conditional on the stack, this is a martingale with increments bounded by `2`. Couple to fair signs using the same uniforms: declare a fair success when `U_i<=1/2`. Since `(POS1)` gives `(1+d_i)/2>=1/2`, the actual `m`-th success occurs no later than the fair `m`-th success. Hence `T_m` is dominated by a negative-binomial total-trial variable of mean `2m`, so `E T_m<infinity`. Optional stopping is therefore valid for the bounded-increment martingale.

At time `T_m` there have been `m` successes and `F_m` failures, so

\[
 m-F_m=\sum_{i\le T_m}B_i=D_m+M_{T_m}.
\]

Taking expectations and using `E M_{T_m}=0` gives

\[
 \mathbb E F_m=m-\mathbb E D_m.
\]

Since `D_m+R_m=D_infty`, Tonelli gives `E D_m=delta-r_m`, proving the exact identity. Also `T_m>=m`, hence pathwise

\[
 0\le R_m\le\sum_{i>m}d_i.
\]

The expected right side tends to zero because `sum_i E d_i=delta<infinity`. ∎

Thus the branching transition drift is exactly

\[
\boxed{
\mathbb E[V_{k+1}-V_k\mid V_k=x]
=1-\delta+r_{x+1},
\qquad r_m\to0.
}
\]

At the unresolved critical point `delta=2`, this becomes

\[
\boxed{
\mathbb E[V_{k+1}-V_k\mid V_k=x]
=-1+r_{x+1}\to-1.
}
\]

So **boundedness is not needed even for the exact asymptotic drift**.

## 6. A new integrability lemma: finite mean total drift is enough for second-order control

The historical intake attempt left open whether an unbounded migration term can destroy the bounded-stack branching asymptotics. The following lemma rules out that obstruction at the one-step variance scale.

### Lemma 6.1
Assume `delta=E D_infty<infinity`. Then

\[
\boxed{\mathbb E D_m^2=o(m).}
\]

### Proof
In the fair coupling above, let `G_m` be the total number of fair trials needed for `m` fair successes. Then

\[
 T_m\le G_m,
\qquad
 D_m\le D_\infty,
\qquad
 D_m\le T_m,
\]

so

\[
 D_m\le\min(D_\infty,G_m).
\]

The stack `D_infty` is independent of `G_m`, since `G_m` depends only on the auxiliary uniforms through the threshold `1/2`.

For `t>0` define

\[
 h(t):=\mathbb E[\min(D_\infty,t)^2].
\]

Because `E D_infty<infinity`,

\[
\frac{h(t)}t\longrightarrow0.
\]

Indeed, for any fixed `A<t`,

\[
 h(t)
\le A^2+t\,\mathbb E[D_\infty\mathbf1_{\{D_\infty>A\}}],
\]

and divide by `t`, then let `t->infinity` followed by `A->infinity`. Also `h(t)/t<=E D_infty` because `min(X,t)^2<=tX`.

Now `G_m/m` has mean `2` and bounded second moments (`Var(G_m)=2m`), hence it is uniformly integrable; moreover `G_m->infinity` in probability. Therefore

\[
 \frac1m\mathbb E h(G_m)
 =\mathbb E\left[
 \frac{h(G_m)}{G_m}\frac{G_m}{m}
 \right]\longrightarrow0,
\]

by uniform integrability and the bounded factor `h(G_m)/G_m ->0` in probability. Since `D_m^2<=min(D_infty,G_m)^2`, the result follows. ∎

This point is important: **no second moment of the random total stack drift is required**.

## 7. Universal mean/variance asymptotics

### Theorem 7.1
Under `(IID)+(POS1)` with finite `delta`,

\[
\boxed{
\mathbb E F_m=m-\delta+o(1),
\qquad
\operatorname{Var}(F_m)=2m+o(m).
}
\]

### Proof
The mean is Lemma 5.1. For the variance, the stopped martingale square-isometry gives

\[
 \mathbb E M_{T_m}^2
 =\mathbb E\sum_{i\le T_m}(1-d_i^2).
\]

Since

\[
 \mathbb E T_m=m+\mathbb E F_m
 =2m-\delta+r_m
\]

and `d_i^2<=d_i`,

\[
0\le
\mathbb E\sum_{i\le T_m}d_i^2
\le\mathbb E D_\infty=\delta.
\]

Hence

\[
\mathbb E M_{T_m}^2=2m+O(1).
\]

From `F_m=m-D_m-M_{T_m}` and `E M_{T_m}=0`,

\[
\operatorname{Var}(F_m)
=\operatorname{Var}(D_m)+\mathbb E M_{T_m}^2
+2\operatorname{Cov}(D_m,M_{T_m}).
\]

Lemma 6.1 gives `Var(D_m)<=E D_m^2=o(m)`. Cauchy-Schwarz then gives

\[
 |\operatorname{Cov}(D_m,M_{T_m})|
 \le
 \sqrt{o(m)\,O(m)}=o(m).
\]

Thus `Var(F_m)=2m+o(m)`. ∎

For the branching chain this becomes, uniformly along `x->infinity` in the scalar asymptotic sense,

\[
\boxed{
\mathbb E[V_{k+1}-V_k\mid V_k=x]=1-\delta+o(1),
\qquad
\operatorname{Var}(V_{k+1}\mid V_k=x)=2x+o(x).
}
\]

At `delta=2`, the Lamperti coefficients are therefore exactly the same as in the bounded-stack model at first and second order.

## 8. One-step Gaussian limit

### Theorem 8.1
Under `(POS1)` with finite `delta`,

\[
\boxed{
\frac{F_m-(m-\delta+r_m)}{\sqrt{2m}}
\Longrightarrow N(0,1).
}
\]

Equivalently, since `r_m->0`, the same holds with centering `m-delta`.

### Proof
Let the predictable quadratic variation of the stopped martingale be

\[
 Q_m:=\sum_{i\le T_m}(1-d_i^2).
\]

Theorem 7.1 implies `F_m/m->1` in probability, hence `T_m/(2m)->1` in probability. Also

\[
 0\le T_m-Q_m
 =\sum_{i\le T_m}d_i^2
 \le D_\infty,
\]

and `D_infty/m->0` in probability (indeed in `L^1` after division by `m`). Therefore

\[
\frac{Q_m}{2m}\longrightarrow1
\]

in probability. The martingale increments are bounded by `2`, so the Lindeberg condition at scale `sqrt(2m)` is automatic. The martingale central limit theorem yields

\[
\frac{M_{T_m}}{\sqrt{2m}}\Longrightarrow N(0,1).
\]

By Lemma 6.1,

\[
\frac{D_m-\mathbb E D_m}{\sqrt m}\longrightarrow0
\]

in `L^2`. Using

\[
F_m-\mathbb EF_m
=-(M_{T_m}+D_m-\mathbb E D_m)
\]

and the symmetry of the standard normal gives the conclusion. ∎

## 9. What this does and does not close

The source-level metric moves because the entire `delta>2` clause is proved. The negative clause remains open only at the critical endpoint after Lemma 4.1.

The transition theorem removes a major candidate obstruction: arbitrary positive unbounded stacks with finite mean total drift have the **same critical one-step drift, variance scale, and Gaussian transition limit** as the bounded-stack branching chain. In particular, a counterexample at `delta=2` cannot arise merely because the unbounded stack changes the first two Lamperti coefficients.

What is still missing is a source-valid theorem converting these transition asymptotics, under only the source assumptions, into the required infinite mean regeneration/life-cycle time at `delta=2`. In the bounded case this is encoded by the total-progeny tail theorem for the branching process with migration. The exact remaining mathematical target can be stated as follows:

> For the Markov chain `V_{k+1}=F^{(k)}_{V_k+1}` induced by an i.i.d. positive stack with `E D_infty=2`, prove that the relevant life-cycle total progeny has infinite mean (equivalently, prove the critical zero-speed implication after checking the regeneration identity in this unbounded setting).

A numerical fit, a guessed Bessel approximation, or a theorem requiring an unrecorded higher stack moment would not close Problem 5.3.

## 10. Next nonrepeating methods

The next ordinary run should not reuse B2/B16/B19. The proposed triple is:

1. **B11 (dualize):** characterize finite mean life-cycle progeny via the invariant/excessive measure of the branching-like kernel and seek a contradiction at the critical Lamperti coefficients.
2. **B24 (find the extremal object):** among positive stacks with fixed `E D_infty=2`, identify whether front-loaded bounded stacks minimize the critical life-cycle tail; a valid stochastic extremizer would transfer the known infinite-mean result.
3. **B5 (add a parameter and differentiate):** strengthen all cookies by a scalar `theta`, compare stationary/progeny susceptibility as `delta(theta) downarrow 2`, and test whether monotonic divergence at the threshold can be proved without a tail theorem.

## 11. Source / literature check dated 2026-09-18

Primary source: Kosygina–Zerner, arXiv:1204.1895 / 2013 journal survey, Problem 5.3. Later nearby works checked include Travers (EJP 2018) on spatial Markov environments and Letterhos (2021) on deterministic identical infinite finite-drift stacks. Those results do not, in the bounded search performed for this run, state the arbitrary i.i.d. `(POS1)` ballisticity theorem posed in Problem 5.3. Search failure is not treated as a novelty certificate.
