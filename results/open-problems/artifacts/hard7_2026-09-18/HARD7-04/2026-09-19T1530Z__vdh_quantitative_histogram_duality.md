# HARD7-04 — quantitative extinction-tilted degree-law duality after giant deletion

**Status:** theorem-sized route result / **PARTIAL pending independent audit and source-scope reconciliation**.  This note proves a stronger distributional form of the discrete-duality mechanism left open by the preceding HARD7-04 second-largest-component size candidate.  It does not assert total-variation equivalence of the entire residual graph law, and it does not satisfy the repository closure protocol by itself.

## 1. Source regime and inherited inputs

Let `d_1,...,d_n` be a deterministic degree sequence satisfying the finite-third-moment barely-supercritical regime of the active `VDH-8.3-DUALITY` claim:

\[
\nu_n:=\frac{\sum_i d_i(d_i-1)}{\sum_i d_i}=1+\varepsilon_n,
\qquad
\varepsilon_n\downarrow0,
\qquad
\varepsilon_n n^{1/3}\longrightarrow\infty,
\tag{1.1}
\]

with

\[
\frac1n\sum_i d_i^3\to \mathbb E D^3<\infty,
\qquad
\frac1n\sum_i d_i\to\mu>0,
\tag{1.2}
\]

and the source's nondegenerate critical limiting degree law.  Write

\[
n_d:=\#\{i:d_i=d\},
\qquad d_{\max}:=\max_i d_i.
\tag{1.3}
\]

Moment convergence implies uniform integrability of the empirical third moments, hence

\[
\frac{d_{\max}^3}{n}\to0,
\qquad
\sum_i(1+d_i)^2=O(n).
\tag{1.4}
\]

Let `xi_n<1` be the extinction probability of the size-biased excess branching process and put

\[
t_n^*:=-\log\xi_n.
\tag{1.5}
\]

The preceding HARD7-04 parameter calculation gives

\[
t_n^*=O(\varepsilon_n).
\tag{1.6}
\]

We use three already proved graph-level inputs from

- `2026-09-19T0855Z__vdh_random_time_weighted_residual.md`, and
- `2026-09-19T0900Z__vdh_postgiant_stopping_reduction.md`.

They are, with `tau_n` the genuine completed-component stopping boundary that identifies the unique giant with probability `1-o(1)`:

\[
\tau_n-t_n^*=o_p(\varepsilon_n),
\tag{1.7}
\]

\[
\sum_i d_i^2
\left|
\mathbf1\{i\text{ sleeping at }\tau_n\}
-\mathbf1\{E_i>\tau_n\}
\right|
=o_p(n\varepsilon_n),
\tag{1.8}
\]

where the independent clock variables satisfy

\[
E_i\sim\operatorname{Exp}(d_i),
\qquad
\mathbb P(E_i>t)=e^{-d_it},
\tag{1.9}
\]

with `E_i=infinity` for `d_i=0`, and the total half-edge volume of components completed before the giant is

\[
H_n^{pre}=o_p(n\varepsilon_n).
\tag{1.10}
\]

At the stopping boundary the still-unpaired sleeping half-edges are conditionally a uniform perfect matching, so the stopping remainder is exactly a configuration model on its random sleeping degree sequence.

The primary source is Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated 4 August 2026, Notes on Section 8.3, printed p. 245 / PDF p. 255, which asks in the barely-supercritical finite-third-moment configuration-model discussion whether the discrete duality principle still holds.  The extinction tilt itself is classical/familiar from fixed-supercritical configuration-model heuristics and generating-function calculations; **no novelty is claimed here for that formula alone**.  The point of this note is the uniform `o_p(epsilon_n)` source-window control for the whole triangular-array degree law at the actual giant deletion.

---

## 2. Main theorem: simultaneous weighted histogram duality

Let `G_n` be the unique giant component and define the literal outside-giant degree counts

\[
N_{n,d}^{out}:=\#\{i\notin G_n:d_i=d\}.
\tag{2.1}
\]

Define the deterministic extinction-tilted count vector

\[
\bar N_{n,d}:=n_d\xi_n^d.
\tag{2.2}
\]

### Theorem 2.1

Under (1.1)--(1.10),

\[
\boxed{
\sum_{d\ge0}(1+d)
\left|N_{n,d}^{out}-n_d\xi_n^d\right|
=o_p(n\varepsilon_n).
}
\tag{2.3}
\]

Equivalently, with `p_{n,d}=n_d/n`,

\[
\boxed{
\sum_{d\ge0}(1+d)
\left|\frac{N_{n,d}^{out}}n-p_{n,d}\xi_n^d\right|
=o_p(\varepsilon_n).
}
\tag{2.4}
\]

Thus the first-order degree profile removed by the giant is simultaneously

\[
N_{n,d}^{G}
=n_d(1-\xi_n^d)+r_{n,d},
\qquad
\sum_d(1+d)|r_{n,d}|=o_p(n\varepsilon_n).
\tag{2.5}
\]

This is a whole-histogram statement; no fixed degree `d` is selected before taking `n->infinity`.

---

## 3. B9 / B27 core: uniform all-degree concentration of the clock thinning

For every degree `d`, set

\[
M_{n,d}(t):=\sum_{i:d_i=d}\mathbf1\{E_i>t\},
\qquad
m_{n,d}(t):=n_de^{-dt}.
\tag{3.1}
\]

The weighted half-line maximal inequality already proved in the earlier HARD7-04 clock note gives, applied separately within the degree-`d` class,

\[
\mathbb E\sup_{t\ge0}
|M_{n,d}(t)-m_{n,d}(t)|
\le4\sqrt{n_d}.
\tag{3.2}
\]

For `d=0` the left side is actually zero, but keeping it causes no harm.  Therefore

\[
\begin{aligned}
\mathbb E\sup_{t\ge0}
\sum_{d\ge0}(1+d)|M_{n,d}(t)-m_{n,d}(t)|
&\le
4\sum_{d:n_d>0}(1+d)\sqrt{n_d}\\
&\le
4\sqrt{(d_{\max}+1)
\sum_d(1+d)^2n_d}.
\end{aligned}
\tag{3.3}
\]

By (1.4),

\[
d_{\max}=o(n^{1/3}),
\qquad
\sum_d(1+d)^2n_d=O(n),
\]

so

\[
\mathbb E\sup_{t\ge0}
\sum_d(1+d)|M_{n,d}(t)-m_{n,d}(t)|
=o(n^{2/3}).
\tag{3.4}
\]

Since

\[
\frac{n^{2/3}}{n\varepsilon_n}
=\frac1{\varepsilon_n n^{1/3}}\to0,
\tag{3.5}
\]

Markov's inequality yields

\[
\boxed{
\sup_{t\ge0}
\sum_d(1+d)|M_{n,d}(t)-m_{n,d}(t)|
=o_p(n\varepsilon_n).
}
\tag{3.6}
\]

This proves the quantifier swap promised by B27: rather than show convergence for each fixed degree and then leave a tail problem, (3.6) controls all occupied degree classes simultaneously, uniformly over every possible random clock time.

### Counterexample stress test

The apparent adversary is a degree sequence occupying as many distinct degree classes as the source moment hypotheses permit.  Equation (3.3) is already optimized for that adversary: the cost is only the square root of the number of occupied classes, at most `sqrt(d_max+1)`.  Even the extreme `d_max` scale allowed by a bounded third moment gives at most order `n^{2/3}` clock noise, while the source signal scale is `n epsilon_n >> n^{2/3}`.  Thus fragmentation of the degree support cannot refute (3.6) within the admitted window.

---

## 4. Random stopping time to deterministic extinction tilt

By (3.6), evaluation at the dependent random time `tau_n` is free:

\[
\sum_d(1+d)|M_{n,d}(\tau_n)-m_{n,d}(\tau_n)|
=o_p(n\varepsilon_n).
\tag{4.1}
\]

For any `a,b>=0`, the map `t->e^{-dt}` is `d`-Lipschitz, so

\[
|e^{-da}-e^{-db}|\le d|a-b|.
\tag{4.2}
\]

Consequently, using (1.7),

\[
\begin{aligned}
\sum_d(1+d)
|m_{n,d}(\tau_n)-m_{n,d}(t_n^*)|
&\le
|\tau_n-t_n^*|
\sum_d d(1+d)n_d\\
&=O(n)|\tau_n-t_n^*|\\
&=o_p(n\varepsilon_n),
\end{aligned}
\tag{4.3}
\]

because the empirical second moment is bounded.  Since

\[
m_{n,d}(t_n^*)=n_de^{-dt_n^*}=n_d\xi_n^d,
\tag{4.4}
\]

(4.1)--(4.4) give

\[
\boxed{
\sum_d(1+d)
|M_{n,d}(\tau_n)-n_d\xi_n^d|
=o_p(n\varepsilon_n).
}
\tag{4.5}
\]

No independence between `tau_n` and the clocks is used.

---

## 5. From the clock thinning to the exact stopping remainder

Let `S_{n,d}` be the number of degree-`d` vertices sleeping at `tau_n`.  The earlier root-mismatch theorem (1.8) is stronger than what is needed here.  Vertices of degree zero satisfy both sleeping indicators identically.  For every `d>=1`,

\[
1+d\le2d^2.
\tag{5.1}
\]

Therefore

\[
\begin{aligned}
\sum_d(1+d)|S_{n,d}-M_{n,d}(\tau_n)|
&\le
\sum_i(1+d_i)
\left|
\mathbf1\{i\text{ sleeping at }\tau_n\}
-\mathbf1\{E_i>\tau_n\}
\right|\\
&\le
2\sum_i d_i^2
\left|
\mathbf1\{i\text{ sleeping at }\tau_n\}
-\mathbf1\{E_i>\tau_n\}
\right|\\
&=o_p(n\varepsilon_n).
\end{aligned}
\tag{5.2}
\]

Combining (5.2) with (4.5),

\[
\boxed{
\sum_d(1+d)|S_{n,d}-n_d\xi_n^d|
=o_p(n\varepsilon_n).
}
\tag{5.3}
\]

Conditional on the stopping history, these `S_{n,d}` are the degree counts of an **exact** configuration-model remainder.  Thus (5.3) is already a quantitative discrete-duality statement for the lawful post-giant stopping remainder.

---

## 6. Add back the pre-giant components: literal complement of the giant

On the event, of probability `1-o(1)`, that the stopping component is the unique giant, the literal complement `V\setminus G_n` consists of

1. the sleeping vertices at `tau_n`, and
2. vertices in components completed before the giant.

Degree-zero vertices are never selected by a sleeping half-edge and create no discrepancy.  Every positive-degree vertex `v` in a pre-giant component satisfies

\[
1+d_v\le2d_v.
\tag{6.1}
\]

Hence, if `P_n` is the set of vertices in components completed before the giant,

\[
\sum_{v\in P_n}(1+d_v)
\le2\sum_{v\in P_n}d_v
=2H_n^{pre}
=o_p(n\varepsilon_n)
\tag{6.2}
\]

by the published/previously archived exploration estimate (1.10).  Therefore

\[
\sum_d(1+d)|N_{n,d}^{out}-S_{n,d}|
=o_p(n\varepsilon_n).
\tag{6.3}
\]

Combining (6.3) with (5.3) proves Theorem 2.1.

---

## 7. B23 consequence: total-variation duality of the empirical degree laws

Put

\[
\bar N_n:=\sum_d n_d\xi_n^d,
\qquad
N_n^{out}:=\sum_dN_{n,d}^{out}.
\tag{7.1}
\]

Since `1-xi_n=O(epsilon_n)` and `1-xi_n^d<=d(1-xi_n)`,

\[
n-\bar N_n
\le(1-\xi_n)\sum_ddn_d
=O(n\varepsilon_n),
\tag{7.2}
\]

so `bar N_n=Theta(n)`.  Theorem 2.1 also gives

\[
|N_n^{out}-\bar N_n|=o_p(n\varepsilon_n),
\tag{7.3}
\]

hence `N_n^{out}=Theta_p(n)`.

Define the normalized extinction-tilted vertex law and the actual empirical outside-giant law by

\[
\pi_{n,d}^{\dagger}
:=\frac{n_d\xi_n^d}{\bar N_n},
\qquad
\widehat\pi_{n,d}^{out}
:=\frac{N_{n,d}^{out}}{N_n^{out}}.
\tag{7.4}
\]

For any nonnegative vectors `a,b` with totals `A,B`,

\[
\sum_j\left|\frac{a_j}{A}-\frac{b_j}{B}\right|
\le \frac{2\sum_j|a_j-b_j|}{A}.
\tag{7.5}
\]

Indeed the first denominator replacement costs `sum|a-b|/A`, and the normalization replacement costs `|A-B|/A`, which is no larger.  Applying (7.5) with (2.3) gives

\[
\boxed{
\|\widehat\pi_n^{out}-\pi_n^{\dagger}\|_{TV}
=o_p(\varepsilon_n).
}
\tag{7.6}
\]

Thus the entire empirical vertex-degree law outside the giant is, at a scale strictly smaller than the distance from criticality, the extinction tilt of the original degree law.

There is an equally useful half-edge version.  Put

\[
L_n^{out}:=\sum_ddN_{n,d}^{out},
\qquad
\bar L_n:=\sum_ddn_d\xi_n^d,
\tag{7.7}
\]

and

\[
\widehat q_{n,d}^{out}:=
\frac{dN_{n,d}^{out}}{L_n^{out}},
\qquad
q_{n,d}^{\dagger}:=
\frac{dn_d\xi_n^d}{\bar L_n}.
\tag{7.8}
\]

Because `sum d^2n_d=O(n)` and `1-xi_n=O(epsilon_n)`,

\[
\sum_ddn_d(1-\xi_n^d)
\le(1-\xi_n)\sum_dd^2n_d
=O(n\varepsilon_n),
\tag{7.9}
\]

so `bar L_n=Theta(n)`.  The weighted part of (2.3) gives

\[
\sum_dd|N_{n,d}^{out}-n_d\xi_n^d|
=o_p(n\varepsilon_n),
\tag{7.10}
\]

and another application of (7.5) yields

\[
\boxed{
\|\widehat q_n^{out}-q_n^{\dagger}\|_{TV}
=o_p(\varepsilon_n).
}
\tag{7.11}
\]

Equations (7.6) and (7.11) are the promised quantitative empirical-law form of discrete duality.

---

## 8. Relation to the already proved reflected drift

The ideal size-biased tilt has excess mean

\[
\frac{\sum_dd(d-1)n_d\xi_n^d}
     {\sum_ddn_d\xi_n^d}
=g_n'(\xi_n)
=1-\varepsilon_n+o(\varepsilon_n).
\tag{8.1}
\]

The earlier HARD7-04 weighted degree-square theorem separately proves that the **actual** post-giant remainder satisfies the same reflected criticality parameter to `o_p(epsilon_n)`.  It is important not to deduce (8.1) for the actual law from total variation (7.11) alone, because the test function `d-1` is unbounded.  The two results are complementary:

- (7.6)--(7.11) give whole-law total-variation duality for bounded observables of the degree and size-biased degree laws;
- the earlier degree-square control gives the required unbounded first moment of the size-biased law.

Together they provide substantially more of the source's “discrete duality” picture than a single reflected scalar drift.

---

## 9. Source consequence and honest boundary

The previous HARD7-04 recovery candidate proved, under the same source hypotheses and its inherited exponential collar,

\[
|C_{2,n}|
=(1+o_p(1))
\frac{2R_*}{\varepsilon_n^2}\log(n\varepsilon_n^3).
\tag{9.1}
\]

The present theorem adds that the empirical degree law of the literal complement of the giant is `o_p(epsilon_n)` in total variation from the extinction tilt, both at the vertex and half-edge levels.  The lawful stopping remainder is moreover conditionally an exact configuration model.

This is a stronger source-level proof candidate for the intended discrete-duality mechanism, but the target remains **PARTIAL / OPEN in the repository** for three reasons.

1. The source wording can still be interpreted as a statement about the **full random graph law** after deleting the giant, not merely its degree law, criticality parameter, and second-largest-component scaling.  The literal complement includes a negligible but already exposed pre-giant part, so no full graph-law total-variation equivalence is asserted here.
2. The new theorem and the preceding size theorem have only this track's proof/self-check history, not the two independent OTHER-track audits required for closure.
3. The extinction tilt is classical in fixed-supercritical configuration-model theory.  The bounded 19 September 2026 literature search did not surface an explicit theorem with the present shrinking-window weighted-`ell^1` error, but that negative search is not a novelty certificate.  Any paper claim must separate the classical tilt mechanism from the source-specific quantitative near-critical upgrade.

No finite exhaustive claim is introduced in this note, so no new checker is manufactured merely for bookkeeping.  The proof is analytic and all theorem-sized steps are written on the page.

## 10. Method outcomes

- **B9 RANDOMIZE — success.** Independent exponential clocks realize the extinction tilt as a product thinning, uniformly robust at the dependent giant stopping time.
- **B23 DO WHAT THE PROPOSER DID NOT EXPECT — success.** The route proves a full empirical degree-law duality statement rather than another component-size estimate.
- **B27 SWAP THE QUANTIFIERS — success.** The classwise maximal inequalities sum to a single weighted `ell^1` estimate over all degree classes; no fixed-degree-before-limit loophole remains.

The frozen admission metric `lim Delta_dual,n` was already `0` and cannot improve numerically; it remains `0 -> 0`.  The progress in this note is therefore a source-scope strengthening rather than movement of a quantity already at its mathematical floor.