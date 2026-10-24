# P0072 — a harmonic-number martingale closes the loop-erased five-edge losange case

Status: **new restricted theorem / PROVED CANDIDATE relative to the cited source interface; full P0072 remains OPEN; publication novelty UNVERIFIED.**

This note addresses the specific five-edge non-series-parallel losange graph singled out as unresolved for the **loop-erased** ant process in Kious–Mailler–Schapira, *Annals of Applied Probability* 32 (2022), §3. It does **not** claim the general-finite-graph conjecture P0072.

## 1. Source interface and notation

Use the source's edge numbering. Edges 1 and 2 form the left two-edge geodesic from nest `N` to food `F`; edges 4 and 5 form the right geodesic; edge 3 is the horizontal bridge between the two middle vertices. Initially every edge has weight 1. After `n` ants let

\[
W(n)=(W_1(n),\dots,W_5(n)),\qquad t_n=n+2,\qquad w_i=\frac{W_i(n)}{t_n}.
\]

Every reinforced simple path is one of

\[
12,\qquad 45,\qquad 135,\qquad 432.
\]

Consequently the source state constraints (its (18)) hold for the loop-erased process as well:

\[
w_1+w_4=w_2+w_5=1,\qquad |w_1-w_2|\le w_3,
\]

plus the other inequalities in the source state space `E`. Put

\[
d:=w_1-w_2,\qquad Q:=w_3+w_1w_4+w_2w_5.
\]

The published loop-erased remark after Lemma 3.5 gives

\[
q_{135}=\frac{w_1w_3w_5}{Q},
\]

and reflection gives

\[
q_{432}=\frac{w_2w_3w_4}{Q}.
\]

The same remark says Lemma 3.5 holds for the loop-erased process, hence

\[
\boxed{w_3(n)=W_3(n)/(n+2)\longrightarrow0\quad\text{a.s.}}
\tag{S1}
\]

This is the only asymptotic input imported from the published proof. It is upstream of the unresolved convergence step, so using it is noncircular.

For an outer edge `i`, let `p_i` be the conditional probability that the next loop-erased path reinforces that edge, and put `F_i=p_i-w_i`.

## 2. B2 — attack the negation: the bridge is not a local positive-drift counterexample

Because the loop-erased reversed path starts at `F`, edge 2 is reinforced iff the last step of the raw walk into `F` uses edge 2. Therefore the source's electrical/hitting calculation behind Lemma 3.9 is rule-independent and gives

\[
p_2
=\frac{w_2w_3+w_1w_2w_5+w_1w_2w_4}{Q},
\]

hence

\[
\boxed{F_2=\frac{d\,w_2w_5}{Q}.}
\tag{2.1}
\]

Also

\[
p_1-p_2=q_{135}-q_{432}
=\frac{w_3(w_1w_5-w_2w_4)}{Q}
=\frac{dw_3}{Q}.
\]

Since `F_1-F_2=(p_1-p_2)-d`,

\[
\boxed{F_1=-\frac{d\,w_1w_4}{Q}.}
\tag{2.2}
\]

For the bridge,

\[
p_3=q_{135}+q_{432}
=\frac{w_3(w_1w_5+w_2w_4)}{Q}.
\]

Using

\[
w_1w_5+w_2w_4=w_1w_4+w_2w_5+d^2=Q-w_3+d^2,
\]

we obtain the exact loop-erased bridge drift

\[
\boxed{F_3=\frac{w_3(d^2-w_3)}{Q}.}
\tag{2.3}
\]

Because `|d|\le w_3\le1`, one has `d^2\le w_3^2\le w_3`, so

\[
F_3\le0.
\]

Thus the source's non-geodesic bridge cannot generate a counterexample through positive local normalized drift. On the symmetric face `d=0`, (2.3) becomes `F_3=-w_3^2/Q`; this explains why a proof demanding a uniform linear contraction of `w_3` is too strong. This last sentence is mechanism-level interpretation only, not an asserted asymptotic rate.

## 3. A uniform outer-edge comparability lemma

The next lemma is the key replacement for the polynomial *upper* bound on `W_3` that the published uniform-geodesic proof needed.

### Lemma 3.1

For each outer edge `i in {1,2,4,5}` and every state `w in E` of the loop-erased losange process,

\[
\boxed{\frac12 w_i\le p_i\le 2w_i.}
\tag{3.1}
\]

### Proof

For edge 2, (2.1) gives

\[
\frac{p_2}{w_2}=1+\frac{dw_5}{Q}.
\]

The upper bound follows from `|d|\le w_3\le Q` and `w_5\le1`. If `d\ge0`, the lower bound is even `p_2\ge w_2`. Suppose `d<0`; write `a=w_1`, `b=w_2`, and `\delta=b-a>0`. Since `w_3\ge\delta`, `w_4=1-a`, and `w_5=1-b`,

\[
Q\ge \delta+a(1-a)+b(1-b)=2b-a^2-b^2.
\]

Moreover

\[
\begin{aligned}
&\bigl(2b-a^2-b^2\bigr)-2(b-a)(1-b)\\
&\qquad=2a(1-b)+(b-a)(a+b)\ge0.
\end{aligned}
\]

Hence `Q\ge2\delta(1-b)=2|d|w_5`, and therefore `p_2/w_2\ge1/2`.

For edge 1 use (2.2):

\[
\frac{p_1}{w_1}=1-\frac{dw_4}{Q},
\]

and the same argument with left/right reflected variables. Finally every reinforced path contains exactly one of edges 1,4 and exactly one of edges 2,5, so `p_4=1-p_1` and `p_5=1-p_2`; reflection gives the same bounds for 4 and 5. ∎

## 4. B16 — exact small case: every outer weight grows polynomially

The published obstruction was the lack of a polynomial *decay* estimate for the normalized bridge. Instead we prove a polynomial **lower** bound on every outer raw weight, which is enough to make a new invariant converge.

### Lemma 4.1

For every `i in {1,2,4,5}`,

\[
\boxed{
\liminf_{n\to\infty}\frac{\log W_i(n)}{\log n}\ge \frac{\log2}{2}
\quad\text{a.s.}}
\tag{4.1}
\]

Consequently, for every fixed `0<\beta<(\log2)/2`, almost surely `W_i(n)\ge n^\beta` for all sufficiently large `n`, simultaneously for the four outer edges.

### Proof

Fix an outer edge and abbreviate `X_n=W_i(n)`. Its next increment is Bernoulli with conditional parameter `p_n`, and Lemma 3.1 gives

\[
\frac{X_n}{2t_n}\le p_n\le\frac{2X_n}{t_n}.
\]

Set `L_n=\log X_n`. Then

\[
\mathbb E[\Delta L_n\mid\mathcal F_n]
=p_n\log(1+X_n^{-1})
\ge\frac{X_n}{2t_n}\log(1+X_n^{-1}).
\]

The function `x\mapsto x\log(1+1/x)` is increasing on `[1,\infty)` and equals `\log2` at 1, hence

\[
\mathbb E[\Delta L_n\mid\mathcal F_n]\ge\frac{\log2}{2t_n}.
\tag{4.2}
\]

Let `M_n` be the martingale obtained by subtracting these predictable drifts from `L_n`. Since `\log(1+1/X_n)\le1/X_n`,

\[
\mathbb E[(\Delta L_n)^2\mid\mathcal F_n]
\le p_nX_n^{-2}
\le\frac{2}{t_nX_n}\le\frac2{t_n}.
\]

Thus the predictable quadratic variation of `M` through time `n` is `O(\log n)`, while its increments are uniformly bounded. Freedman's inequality on the dyadic times `2^m`, followed by Borel–Cantelli and the maximal form of the same inequality on each dyadic block, gives

\[
M_n=o(\log n)\qquad\text{a.s.}
\]

Summing (4.2) yields (4.1). ∎

## 5. B19 — make it an algorithm: discrete antiderivatives reveal an exact martingale

The drift identities (2.1)–(2.2) suggest dividing the increment of an outer coordinate by its current raw weight. The exact discrete antiderivative of `1/m` is the harmonic number.

Let `H_0=0` and `H_m=\sum_{k=1}^m1/k`. Define

\[
\boxed{
K_n:=H_{W_1(n)-1}+H_{W_2(n)-1}
-H_{W_4(n)-1}-H_{W_5(n)-1}.}
\tag{5.1}
\]

### Lemma 5.1 — exact conservation in conditional expectation

`(K_n)` is an exact martingale for the loop-erased losange process.

### Proof

When edge `i` is reinforced, `H_{W_i-1}` changes by exactly `1/W_i`. Hence

\[
\mathbb E[\Delta K_n\mid\mathcal F_n]
=\frac{p_1}{W_1}+\frac{p_2}{W_2}
-\frac{p_4}{W_4}-\frac{p_5}{W_5}.
\]

Because `W_1+W_4=W_2+W_5=t_n` and `p_4=1-p_1`,

\[
\frac{p_1}{W_1}-\frac{p_4}{W_4}
=\frac{F_1}{t_nw_1w_4}
=-\frac{d}{t_nQ}.
\]

Likewise, using `p_5=1-p_2` and (2.1),

\[
\frac{p_2}{W_2}-\frac{p_5}{W_5}
=\frac{F_2}{t_nw_2w_5}
=\frac{d}{t_nQ}.
\]

They cancel exactly. ∎

### Lemma 5.2 — almost-sure convergence of the invariant

`K_n` converges almost surely to a finite random variable `K_\infty`.

### Proof

Every selected path uses exactly two outer edges. Therefore

\[
(\Delta K_n)^2
\le2\sum_{i\in\{1,2,4,5\}}
\frac{\mathbf1_{\{i\text{ reinforced at }n+1\}}}{W_i(n)^2}.
\]

Taking conditional expectation and using the upper half of (3.1),

\[
\mathbb E[(\Delta K_n)^2\mid\mathcal F_n]
\le \frac4{t_n}\sum_{i\in\{1,2,4,5\}}\frac1{W_i(n)}.
\tag{5.2}
\]

Choose any `\beta<(\log2)/2`. By Lemma 4.1, almost surely all four denominators eventually exceed `n^\beta`, so the right-hand side of (5.2) is summable. The martingale has bounded increments; localizing at the partial quadratic variation and applying the martingale convergence theorem yields finite almost-sure convergence. ∎

## 6. The five-edge loop-erased losange theorem

### Theorem 6.1

For the loop-erased ant process on the five-edge losange with unit initial weights, there exists a random `\chi\in(0,1)` such that almost surely

\[
\boxed{
\frac{W_1(n)}n,\frac{W_2(n)}n\to\chi,
\qquad
\frac{W_4(n)}n,\frac{W_5(n)}n\to1-\chi,
\qquad
\frac{W_3(n)}n\to0.}
\tag{6.1}
\]

In particular the stronger Kious–Mailler–Schapira Conjecture 1.1 holds on this graph for the loop-erased rule: the bridge is the unique non-geodesic edge and has zero limiting normalized weight, while every edge on either geodesic has positive limiting normalized weight.

### Proof

By (S1), `w_3(n)\to0`. Since `|w_1-w_2|\le w_3`,

\[
w_1(n)-w_2(n)\to0.
\tag{6.2}
\]

Lemma 4.1 gives `W_i(n)\to\infty` for all four outer edges. Hence

\[
H_{W_i(n)-1}=\log W_i(n)+\gamma+o(1).
\]

The two positive and two negative Euler constants cancel in (5.1), and the common normalization `t_n` cancels from the ratio, so Lemma 5.2 implies

\[
\log\frac{w_1(n)w_2(n)}{w_4(n)w_5(n)}\longrightarrow K_\infty.
\tag{6.3}
\]

Take any convergent subsequence of `w_1(n)`. By (6.2), `w_2` has the same subsequential limit `r`, while `w_4,w_5` tend to `1-r`. If `r=0`, the left side of (6.3) tends to `-\infty`; if `r=1`, it tends to `+\infty`. Both contradict finite `K_\infty`. Thus every subsequential limit lies in `(0,1)` and must solve

\[
2\log\frac r{1-r}=K_\infty.
\]

This equation has the unique solution

\[
\boxed{\chi=\frac{e^{K_\infty/2}}{1+e^{K_\infty/2}}\in(0,1).}
\]

Therefore every subsequence has the same limit, proving convergence of the whole sequence. Replacing `n+2` by `n` does not change the limits, and (S1) gives the bridge conclusion. ∎

## 7. What moved and what did not

This proves a source-relevant **restricted theorem that the 2022 parent paper explicitly left open**: the loop-erased five-edge losange converges, and its limit has exactly the required geodesic support. The mechanism is the exact harmonic-number martingale (5.1), not a polynomial upper rate for the bridge.

It does **not** resolve canonical P0072, whose 2025 source asks for all finite graphs and both reinforcement rules. The frozen full-source metric therefore remains

`C_P0072: 0 -> 0 (NO MOVEMENT)`.

A separate finite milestone moves from unresolved to proved candidate:

`loop-erased five-edge losange: 0 -> 1`.

No novelty claim is made from the bounded literature search. Independent audit is still absent.

## 8. Next mathematical attack

The martingale comes from pairing the two cut identities `W_1+W_4=t` and `W_2+W_5=t` with exact drift ratios. The next useful question is whether a general finite graph admits an analogous cycle/cut harmonic potential: assign signs/cochains `s_e` so that

\[
\sum_e s_e\frac{p_e}{W_e}=0
\]

exactly or up to a summable error. If such potentials can be generated from the cycle space, one can try to combine them with known decay of non-geodesic flow. If not, the first graph where the linear system is inconsistent is a concrete counterexample-search target.
