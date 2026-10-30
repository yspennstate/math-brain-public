# B12 — Palm coding identity and a state-capacity obstruction for sequential FEI compression

**Run:** 2026-09-21T14:48:34Z, fleet02/B12  
**Role:** FEI approach 1 — spectral-sample compression / sequential prediction  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval or receiver-context use occurred.  
**Status:** PARTIAL / new exact identity plus a rigorous Boolean obstruction to a natural low-state bridge. **Full uniform-cube FEI remains OPEN / NOT PROVED.**

The direct owner order `FEI-SEVEN-TASKS-2026-09-21` controls this run over the stale provisional benchmark row in `roles.json`. I read the required read-once continuation in the owner-prescribed order (`TASKS_2026-09-21.md`, `REPORT.md`, `APPROACHES.md`), the fresh P03 README and `FLEET_RULES.md`, then the newest complete B12 selector/death-chain work and the complementary current B13 product-mixing and B14 selector work. I do **not** make a publication-priority or novelty claim here.

The three fresh `FLEET_RULES` moves are **#1 (change category: treat the selector as universal source coding with a memory-state budget), #3 (prove a stronger obstruction: arbitrary low-entropy prefix summaries, not just a particular finite window), and #25 (count the continuation-Palm joint law two ways to expose the exact influence-profile marginal).**

The current unrestricted FEI lower bound from the required task sheet remains the external `> 6.521845710923046575`; the read-once theorem `H <= 6.4573 I` is a structured-class theorem only. Nothing below changes either fact.

## 1. Starting point from the preceding B12 run

Let

\[
p_B=\widehat f(B)^2,\qquad K=|B|,\qquad \lambda=I(f)=\sum_B |B|p_B.
\]

For a prefix set `A`, `a=|A|`, define the uniform-prefix shadow

\[
v_A=\sum_{B\supseteq A}\frac{p_B}{\binom{|B|}{a}}.
\]

The preceding run proved the exact random-order continuation law

\[
\mu(A):=\frac{v_A-p_A}{\lambda},\qquad
r_A(i):=\frac{v_{A\cup\{i\}}}{(a+1)(v_A-p_A)}\quad(i\notin A),
\]

and the selector information

\[
j_A=I(B;X_{a+1}\mid A,\ B\ne A).
\]

Its selector contribution is

\[
\mathrm{Sel}(f)=\sum_A(v_A-p_A)j_A
=\lambda\,\mathbb E_{A\sim\mu}j_A.
\]

The same run gave

\[
H(f)=H_{\rm haz}(f)+\mathrm{Sel}(f),\qquad H_{\rm haz}(f)\le H(K)\le 3\lambda.
\]

Thus a dimension-free bound on the normalized selector is enough for FEI, while the sharp selector problem is itself as hard as FEI under amplification. The issue is how the *whole prefix* predicts the next spectral coordinate.

## 2. New exact continuation-Palm experiment

Assume `lambda>0`. Define one random continuation event as follows.

1. Draw a terminal spectral set `B` from the size-biased law
   \[
   \Pr(B)=\frac{|B|p_B}{\lambda}.
   \]
2. Conditional on `B`, choose `R` uniformly from `{1,...,|B|}`.
3. Choose a uniformly random ordering of `B`.
4. Let `A` be the set of the first `R-1` coordinates and let `X` be the coordinate in position `R`.

This experiment chooses a uniformly random *continuation step* along a random spectral path, with terminal sets weighted by their number of continuation steps.

### Proposition 2.1 — exact Palm law

Under this experiment,

\[
\boxed{\Pr(A)=\mu(A)=\frac{v_A-p_A}{\lambda}},
\tag{2.1}
\]

and, conditional on `A`,

\[
\boxed{\Pr(X=i\mid A)=r_A(i)}.
\tag{2.2}
\]

Moreover the **unconditional next-coordinate marginal is exactly the normalized influence profile**

\[
\boxed{
\Pr(X=i)=\pi_i:=\frac{\operatorname{Inf}_i(f)}{I(f)}.
}
\tag{2.3}
\]

#### Proof

For `a=|A|<|B|`, the probability of choosing rank `a+1` is `1/|B|`, and the first `a` unordered elements of a random permutation form a uniform `a`-subset of `B`. Hence the `B` contribution to `Pr(A)` is

\[
\frac{|B|p_B}{\lambda}\frac1{|B|}\frac1{\binom{|B|}{a}}
=\frac{p_B}{\lambda\binom{|B|}{a}}.
\]

Summing over strict supersets `B>A` gives (2.1); the already-proved child-shadow recurrence gives (2.2).

For (2.3), conditional on `B`, the coordinate occupying a uniformly random rank of a uniformly random permutation is uniform in `B`. Therefore

\[
\Pr(X=i)
=\sum_{B\ni i}\frac{|B|p_B}{\lambda}\frac1{|B|}
=\frac{\sum_{B\ni i}p_B}{\lambda}
=\frac{\operatorname{Inf}_i(f)}{\lambda}.
\]
QED.

This is the useful double count: the complicated random prefix disappears from the one-coordinate marginal.

## 3. Exact selector = profile entropy - stored-prefix information - factorial refund

Let

\[
H(\pi)=-\sum_i\pi_i\log_2\pi_i.
\]

### Theorem 3.1 — Palm coding identity

For every nonconstant Boolean `f` (indeed for every probability law on subsets),

\[
\boxed{
\frac{\mathrm{Sel}(f)}{I(f)}
=H(\pi)-I(A;X)
-\frac{\mathbb E_p\log_2(K!)}{I(f)}.
}
\tag{3.1}
\]

#### Proof

The Palm experiment is exactly the continuation law, so

\[
\frac{\mathrm{Sel}(f)}{\lambda}=I(B;X\mid A).
\]

Given `(A,B)`, the next coordinate is uniform in `B\setminus A`, hence

\[
H(X\mid A,B)=\mathbb E\log_2(K-|A|).
\]

Also, by (2.3),

\[
H(X\mid A)=H(X)-I(A;X)=H(\pi)-I(A;X).
\]

It remains to evaluate the oracle permutation entropy. Conditional on a terminal set of size `K=k`, the random rank is uniform, so the residual count `k-R+1` is uniform on `{1,...,k}`. Thus

\[
\mathbb E[\log_2(K-|A|)\mid B]
=\frac1K\log_2(K!).
\]

The Palm law size-biases `B` by `K/\lambda`, so after averaging,

\[
\mathbb E\log_2(K-|A|)
=\frac{\mathbb E_p\log_2(K!)}{\lambda}.
\]
Subtracting gives (3.1). QED.

### Interpretation

There are now three exact pieces in the average continuation code:

- `H(pi)`: raw uncertainty of the next coordinate under the normalized influence profile;
- `I(A;X)`: information about that coordinate stored in the **entire already-revealed prefix**;
- `E log(K!)/I`: the unavoidable permutation entropy the oracle also pays.

So the sequential FEI problem is not merely “find a good one-step marginal.” A proof must show that Booleanity forces the full prefix to store almost all of the dangerous coordinate-label entropy whenever `H(pi)` is large.

## 4. Stronger obstruction: any low-entropy prefix summary loses the needed refund

Let `Z` be any (possibly randomized) summary generated from `A`, with no access to the hidden terminal set beyond the information already in `A`. The optimal predictor based only on `Z` has expected continuation excess code length

\[
\mathcal L(Z)
:=H(X\mid Z)-\frac{\mathbb E_p\log_2(K!)}{\lambda}.
\tag{4.1}
\]

For the full prefix, `Z=A`, Theorem 3.1 says

\[
\mathcal L(A)=\frac{\mathrm{Sel}(f)}{\lambda}.
\tag{4.2}
\]

Because `Z` is a degradation of `A`, `H(X|Z)>=H(X|A)`, so `L(Z)>=L(A)`.

### Theorem 4.1 — state-capacity lower bound

If `H(Z)<=b`, then

\[
\boxed{
\mathcal L(Z)
\ge H(\pi)-b-
\frac{\mathbb E_p\log_2(K!)}{\lambda}.
}
\tag{4.3}
\]

#### Proof

`I(Z;X)<=H(Z)<=b`, hence

\[
H(X\mid Z)=H(X)-I(Z;X)\ge H(\pi)-b.
\]
Insert this in (4.1). QED.

This is stronger than killing a fixed sliding window: `Z` may be **any** compressed state or statistic of the whole prefix. The obstruction is information-theoretic, not tied to a particular data structure.

For a sequential algorithm that receives the rank/step number for free, one may condition throughout on `R`. On the transitive tribes family below, coordinate symmetry gives `H(X|R)=log_2 n` at every admissible rank, so the same argument holds with the charged state capacity `H(Z|R)<=b`. Thus the theorem is not an artifact of charging `O(log K)` bits for the clock.

## 5. Boolean witness: balanced tribes forces linear-in-width prefix state

The obstruction in Theorem 4.1 is genuine on a standard Boolean FEI family, not on a relaxed subset law.

Take `m` disjoint blocks of width `w`. Put

\[
a_b(x)=\prod_{j=1}^w\frac{1+x_{b,j}}2,
\qquad
h(x)=\prod_{b=1}^m(1-a_b(x)),
\qquad
f_{w,m}=2h-1.
\]

Let

\[
\delta=2^{-w},\qquad q_0=1-\delta,\qquad q=q_0^m.
\]

Choose the balanced scaling

\[
m=m_w=\operatorname{round}((\ln2)2^w),
\tag{5.1}
\]

so `q -> 1/2`.

### 5.1 Exact block spectral law

For one block `g=1-a_b`,

\[
\widehat g(\varnothing)=q_0,
\qquad
\widehat g(T)=-\delta\quad(T\ne\varnothing).
\]

After normalizing squared Fourier masses of `g` by `E[g^2]=q_0`, the block spectral sample is

\[
\Pr(T=\varnothing)=q_0,
\qquad
\Pr(T=U)=\frac{\delta^2}{q_0}\quad(U\ne\varnothing).
\tag{5.2}
\]

Equivalently, a block is active with probability `delta`, and conditional on activity its spectral subset is uniform over the `2^w-1` nonempty subsets.

Because `h` is a disjoint product, its normalized spectral law is the product of (5.2). For `f=2h-1`, the conditional law given a nonempty spectral set is exactly this product law conditioned not all blocks empty. This gives an exact probabilistic model for the witness.

### 5.2 Exact influence and entropy calibration

All coordinates are equivalent, and

\[
\boxed{
I(f_{w,m})
=mw\,2^{1-w}(1-2^{-w})^{m-1}.
}
\tag{5.3}
\]

With `kappa=ln 2` and (5.1),

\[
I(f_{w,m_w})=\kappa w+o(w).
\tag{5.4}
\]

For the normalized one-block spectral law define

\[
H_{\rm loc}=h_2(\delta)+\delta\log_2(2^w-1).
\]

The product law has entropy `m H_loc` and all-empty probability `q`. If `V=4q(1-q)` is the nonconstant spectral mass of `f`, then

\[
\boxed{
H(f)=h_2(V)
+V\frac{mH_{\rm loc}-h_2(q)}{1-q}.
}
\tag{5.5}
\]

Since

\[
H_{\rm loc}=\delta(2w+\log_2 e)+o(\delta),
\]

(5.1) gives

\[
H(f_{w,m_w})=4\kappa w+O(1),
\qquad
\boxed{\frac{H}{I}\to4.}
\tag{5.6}
\]

So tribes itself is very far from a counterexample to FEI; it is a **counterexample to low-state sequential proofs**.

### 5.3 Influence-profile entropy is exponentially large in the block label

Coordinate transitivity gives a uniform normalized influence profile, hence

\[
\boxed{
H(\pi)=\log_2(mw)
=w+\log_2w+\log_2(\ln2)+o(1).
}
\tag{5.7}
\]

The raw next-coordinate label therefore carries about `w+log w` bits.

### 5.4 The factorial refund is only `log w + O(1)`

Let `L` be the number of active blocks in the normalized product spectral law. Then

\[
L\sim\operatorname{Bin}(m,\delta),
\qquad \mathbb EL=m\delta=\ln2+o(1).
\]

Since every active block contributes at most `w` coordinates,

\[
K\le wL.
\]

Also, conditional on `L`, the mean of `K` is a fixed constant times `L`; therefore

\[
\begin{aligned}
\frac{\mathbb E_p\log_2(K!)}{I}
&\le \frac{\mathbb E_p[K\log_2K]}{I}\\
&\le \log_2w+
\frac{\mathbb E[L\log_2L]}{\mathbb EL}\\
&\le \log_2w+
\frac{\mathbb E[L^2]}{\mathbb EL}\\
&=\log_2w+1-\delta+m\delta.
\end{aligned}
\tag{5.8}
\]

The scalar factor by which the positive spectral masses of `f` differ from the normalized `h` law cancels in this ratio. Since `m delta -> ln 2`,

\[
\boxed{
\frac{\mathbb E_p\log_2(K!)}{I}
\le \log_2w+1+\ln2+o(1).
}
\tag{5.9}
\]

### 5.5 Main no-go consequence

Combine (4.3), (5.7), and (5.9). Any prefix summary `Z` with entropy at most `b` satisfies

\[
\boxed{
\mathcal L(Z)
\ge w-b+\log_2(\ln2)-1-\ln2-o(1)
= w-b-2.222\ldots-o(1).
}
\tag{5.10}
\]

Therefore:

> **For every `b_w=o(w)`, the optimal continuation code based on a `b_w`-bit summary of the full prefix has excess log loss tending to infinity on balanced tribes.**

Equivalently, any sequential FEI bridge that first compresses the prefix to a state of `o(w)` bits and then tries to prove a dimension-independent next-coordinate regret bound is impossible. To keep `L(Z)=O(1)`, one needs

\[
H(Z)\ge w-O(1).
\tag{5.11}
\]

This remains true when the step number is supplied free, using `H(Z|R)` in place of `H(Z)`.

In contrast, the **full prefix** does amortize the block label. From (4.2),

\[
\mathcal L(A)=\frac{\mathrm{Sel}}I\le\frac HI\to4,
\]

while (5.7)-(5.9) imply

\[
I(A;X)
=H(\pi)-H(X|A)
\ge w-O(1).
\tag{5.12}
\]

Thus on tribes the already-revealed prefix really contains linearly many bits about the next spectral coordinate. Throwing that history into a low-capacity statistic destroys precisely the refund that makes the family harmless for FEI.

## 6. What this kills and what it suggests

### Killed bridge

A natural route after the death-chain selector identity was:

> replace the large prefix `A` by a fixed-dimensional/fixed-state statistic, bound the next-coordinate entropy from that statistic, and amortize a constant amount per spectral coordinate.

Theorem 4.1 plus balanced tribes kills this in the only invariant formulation that matters: **low information capacity**. A finite-state, bounded-bit, or `o(w)`-bit summary cannot retain enough of the old prefix, even if it is chosen adaptively from the entire history and even if the rank is free. A “few real numbers” is not ruled out unless their information content is controlled; arbitrary real numbers can encode unbounded information, so the correct obstruction is entropy capacity, not Euclidean dimension.

### Positive lesson

The full-prefix refund has the exact size

\[
I(A;X).
\]

On tribes it stores the identity of rare active blocks and reuses that information over many future coordinates. This is compatible with the current B13 product decomposition: B13 pays coarse product-block mixing globally rather than once per depth, while the present result says any universal sequential proof must likewise **retain and reuse high-entropy block/cluster identity across many reveals**. This is deliberately complementary to B14's restriction-selector recursion and B16's signed transport work.

A viable next bridge therefore cannot be a constant-size potential. It should be an **information-debt / dictionary argument** in which the state is allowed to carry `Theta(I)` bits, but acquiring a high-entropy label is charged only once and the label is reused across the many subsequent spectral coordinates it predicts. The universal Booleanity question becomes:

\[
\boxed{
H(\pi)-I(A;X)
\stackrel{?}{\le}
\frac{\mathbb E\log_2(K!)}I+C.
}
\tag{6.1}
\]

Equation (6.1) is exactly the selector target, not a solved lemma. The next substantive attack should lower-bound the full-history term `I(A;X)` from Boolean constraints such as the signed autocorrelation identities coming from `f^2=1`, while explicitly passing three tests:

1. **uniform fixed-size relaxed subset laws**, where (6.1) can fail and Booleanity is absent;
2. **balanced tribes**, where the proof must preserve about `w` bits of block identity;
3. **amplified high-ratio Boolean seeds**, where no constant below the true FEI lower bound can survive.

## 7. Executed verification

`verify_palm_state_capacity.py` was executed with the standard Python interpreter and compiled with `py_compile`. It checks:

- exact rational normalization of the continuation-Palm law;
- exact rational equality `Pr(X=i)=Inf_i/I`;
- the entropy identity (3.1) on `Maj_3` (observed discrepancy `0.0` at floating evaluation precision);
- direct Walsh enumeration of the tiny tribes case `w=2,m=3`, recovering exactly `I=27/16` and the closed-form entropy;
- balanced-tribes formula rows for `w=4,6,8,10,12,16,20`.

The final diagnostic row (`w=20`, `m=726817`) gives

\[
H/I=3.9999958800727846,
\]

and the rigorous finite-width lower bound obtained from (5.8)

\[
H(\pi)-\text{refund upper bound}
=17.778086886591858.
\]

These finite checks support the algebra and catch normalization errors; they are not evidence of full FEI closure.

## 8. Status

**PROVED in this report:** the Palm marginal identity (2.3), exact selector coding identity (3.1), general state-capacity bound (4.3), exact tribes formulas (5.2)-(5.5), the refund bound (5.8), and the balanced-tribes low-state obstruction (5.10).

**NOT PROVED:** any universal constant in (6.1), full FEI, or a Booleanity theorem that forces the needed full-history information refund.

The universal target remains open.
