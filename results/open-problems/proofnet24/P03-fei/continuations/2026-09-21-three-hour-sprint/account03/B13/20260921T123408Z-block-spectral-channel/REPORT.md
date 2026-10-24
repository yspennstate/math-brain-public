# B13 FEI sprint — sharp block-spectral information payment

**Status:** PARTIAL / PROVED universal auxiliary theorem. Full uniform-cube Fourier entropy-influence (FEI) remains **OPEN / NOT PROVED**.

**Execution label:** **WITHOUT_VERIFIED_BRAIN**. No authenticated mathematical/cognitive brain retrieval was used in the derivation or computation.

**Owner route:** FEI cancellation/Booleanity profile, compatible with APPROACHES routes 2, 13 and 14 and the current three-hour sprint assignment for account03/B13. This run does not recheck the read-once certificate or any settled sweep.

**No novelty claim:** the information inequality below is assembled here as a new-to-this-run proof step. Its Jensen–Shannon/Hellinger ingredient is classical in flavor; no publication-priority assertion is made.

## 1. Exact universal statement attempted

Let
\[
f:\{-1,1\}^{X\sqcup Y}\to\{-1,1\}
\]
be Boolean. For each outside assignment \(y\in\{-1,1\}^{Y}\), let \(f_y\) be the restriction to the block \(X\), and define its local spectral law
\[
P_y(A)=\widehat{f_y}(A)^2,\qquad A\subseteq X.
\]
Sample \(Y\) uniformly, then conditionally sample a label \(Z\subseteq X\) from \(P_Y\).

The first attempted strengthening was

\[
\tag{BC_2}
I(Y;Z)\le 2\sum_{j\in Y}\operatorname{Inf}_j(f).
\]

This statement is **REFUTED** below.

The replacement theorem proved in this run is the sharp universal inequality

\[
\tag{BC_*}
\boxed{
I(Y;Z)\le \frac{2}{\ln 2}\sum_{j\in Y}\operatorname{Inf}_j(f)
}
\]
with mutual information measured in bits. The constant \(2/\ln2=2.8853900817779268\ldots\) is best possible.

This is a genuine all-dimensions/all-Boolean-functions theorem, but it is an auxiliary statement, **not full FEI**.

## 2. Exact block-profile identity

For \(A\subseteq X\), write
\[
c_A(y)=\widehat{f_y}(A).
\]
Expanding in the outside variables,
\[
c_A(y)=\sum_{R\subseteq Y}\widehat f(A\cup R)\chi_R(y).
\]
Parseval in \(y\) therefore gives
\[
\mathbb E_y c_A(y)^2
 =\sum_{R\subseteq Y}\widehat f(A\cup R)^2
 =\Pr_{S\sim\widehat f^2}[S\cap X=A].
\]
Hence the marginal law of \(Z\) is **exactly** the block projection \(S\cap X\) of the global spectral sample.

Consequently
\[
\tag{2.1}
H(S\cap X)=\mathbb E_y H(P_y)+I(Y;Z).
\]
Thus \(I(Y;Z)\) measures the extra block spectral entropy produced by variation of the local Fourier-square law across outside assignments.

## 3. Pair lemma: spectral JS divergence is paid by disagreement

### Lemma 3.1

Let \(a,b\) be real unit vectors and let \(p_i=a_i^2,\ q_i=b_i^2\). Then
\[
\tag{3.1}
\operatorname{JS}_2(p,q)
 \le \frac{1}{2\ln2}\,\|\,|a|-|b|\,\|_2^2
 \le \frac{1}{2\ln2}\min\{\|a-b\|_2^2,\|a+b\|_2^2\}.
\]

#### Proof

For nonnegative \(x,y\), put \(s=x^2+y^2\) and
\[
t=\frac{x^2-y^2}{x^2+y^2}\in[-1,1]
\]
when \(s>0\). The coordinate contribution to Jensen–Shannon divergence in natural logarithms is
\[
j_e(x^2,y^2)
=\frac{s}{4}\left[(1+t)\ln(1+t)+(1-t)\ln(1-t)\right].
\]
Meanwhile
\[
(x-y)^2=s\bigl(1-\sqrt{1-t^2}\bigr).
\]
It is enough to prove
\[
\frac12[(1+t)\ln(1+t)+(1-t)\ln(1-t)]
\le 1-\sqrt{1-t^2}.
\]
Both sides are even and vanish at \(t=0\). For \(0\le t<1\), the derivatives are
\[
\operatorname{artanh}(t)
\quad\text{and}\quad
\frac{t}{\sqrt{1-t^2}}.
\]
Their derivatives are respectively
\[
\frac1{1-t^2}
\quad\text{and}\quad
\frac1{(1-t^2)^{3/2}},
\]
so the second derivative-of-the-primitive is larger. Hence the desired scalar inequality follows by integrating from \(0\).

Summing coordinates and converting nats to bits gives the first inequality in (3.1). Pointwise
\[
||a_i|-|b_i||\le |a_i-b_i|,\qquad
||a_i|-|b_i||\le |a_i+b_i|,
\]
which gives the second. ∎

### Corollary 3.2

Let \(h_0,h_1:\{-1,1\}^{X}\to\{-1,1\}\) be Boolean, with local spectral laws \(P_0,P_1\), and let
\[
\delta=\Pr_x[h_0(x)\ne h_1(x)].
\]
Then
\[
\tag{3.2}
\operatorname{JS}_2(P_0,P_1)
 \le \frac{2}{\ln2}\min\{\delta,1-\delta\}
 \le \frac{2}{\ln2}\delta.
\]

Indeed Parseval gives
\[
\|\widehat h_0-\widehat h_1\|_2^2
 =\mathbb E(h_0-h_1)^2=4\delta
\]
and
\[
\|\widehat h_0+\widehat h_1\|_2^2
 =4(1-\delta).
\]

This is where Booleanity enters: neighboring restrictions are sign-valued vectors whose Fourier transforms have exactly controlled Euclidean distance.

## 4. Proof of the sharp block-channel theorem

Order the outside coordinates as \(Y_1,\ldots,Y_m\). By the mutual-information chain rule,
\[
I(Y;Z)=\sum_{t=1}^m I(Y_t;Z\mid Y_1,\ldots,Y_{t-1}).
\]

Fix a prefix \(Y_{<t}=u\). Conditioned on \(Y_t=b\), the law of \(Z\) is the uniform mixture, over all suffix assignments \(v\), of the local spectral laws \(P_{u,b,v}\). Since Jensen–Shannon divergence is jointly convex (equivalently, apply joint convexity of relative entropy to its two KL terms),
\[
I(Y_t;Z\mid Y_{<t}=u)
\le \mathbb E_v\,\operatorname{JS}_2(P_{u,0,v},P_{u,1,v}).
\]
By Corollary 3.2 this is at most
\[
\frac{2}{\ln2}\,
\mathbb E_v\Pr_{x_X}[f_{u,0,v}(x_X)\ne f_{u,1,v}(x_X)].
\]
Averaging over prefixes \(u\), the last expectation is exactly
\(\operatorname{Inf}_{Y_t}(f)\). Summing in \(t\) proves (BC_*).

No induction hypothesis, FEI assumption, read-once structure, monotonicity, or finite-dimensional enumeration is used.

## 5. Sharpness and decisive refutation of coefficient 2

Let \(k\) be even and \(N=2^k\). Take the explicit quadratic bent function
\[
h(x)=(-1)^{x_1x_2\oplus x_3x_4\oplus\cdots\oplus x_{k-1}x_k}
\]
on \(\mathbb F_2^k\). Every Walsh coefficient has magnitude \(N^{-1/2}\). Let \(h'\) be obtained by flipping the value of \(h\) at one input, and define a Boolean function with one outside bit \(y\):
\[
f(x,y)=
\begin{cases}
h(x),&y=0,\\
h'(x),&y=1.
\end{cases}
\]
Then
\[
\operatorname{Inf}_y(f)=\frac1N,\qquad
I(y;Z)=\operatorname{JS}_2(P_h,P_{h'}).
\]

Writing \(s=\sqrt N\), after the one-point flip the spectral probabilities are
\[
\frac1N(1+2/s)^2
\quad\text{on }(N-s)/2\text{ atoms},
\]
and
\[
\frac1N(1-2/s)^2
\quad\text{on }(N+s)/2\text{ atoms},
\]
up to exchanging the two classes. The first-order perturbations cancel and a second-order expansion of binary Jensen–Shannon divergence gives
\[
\operatorname{JS}_2(P_h,P_{h'})
=\frac{2}{N\ln2}+O(N^{-3/2}).
\]
Therefore
\[
\frac{I(y;Z)}{\operatorname{Inf}_y(f)}
\longrightarrow \frac2{\ln2}.
\]
So the constant in (BC_*) is sharp.

In particular the stronger coefficient-2 claim (BC_2) is **REFUTED** by this finite Boolean family, not by an abstract random-set relaxation.

The attached standard-library reproducer gives:

| \(k\) | \(N=2^k\) | \(I(y;Z)/\operatorname{Inf}_y(f)\) |
|---:|---:|---:|
| 2 | 4 | 2.195179762781594 |
| 4 | 16 | 2.805655914813947 |
| 6 | 64 | 2.869211287837658 |
| 8 | 256 | 2.881562254420601 |
| 10 | 1024 | 2.884446418752305 |
| 12 | 4096 | 2.885154992869502 |

The limit is \(2/\ln2=2.885390081777927\ldots\).

## 6. Independent finite counterexample search

The same script exhausts all Boolean functions through \(n=4\), quotienting global negation, and every nontrivial coordinate block \(X\). The largest observed ratios \(I(Y;Z)/I_Y(f)\) are:

- \(n=2:\ 2.000000000000000\);
- \(n=3:\ 2.195179762781594\);
- \(n=4:\ 2.398671813459046\).

At \(n=4\), the recorded maximizer has
\[
I(Y;Z)=0.29983397668238077,\qquad I_Y(f)=0.125.
\]

These finite extrema are **computational evidence only**. The universal upper bound and its sharpness come from the analytic argument above.

## 7. Relation to cancellation entropy and exact remaining obstruction

The current FEI cancellation route uses
\[
p_A=\widehat f(A)^2,\qquad
u_A=\sum_{B\supseteq A}p_B
=\mathbb E_y c_A(y)^2,
\]
and
\[
B_{\rm can}(f)=\sum_A p_A\log_2\frac{u_A}{p_A},
\qquad p_A=(\mathbb E_y c_A(y))^2.
\]

The new theorem controls variation of the **magnitudes squared**
\(c_A(y)^2\) as a block spectral channel. It does **not** by itself control the cancellation between positive and negative values of \(c_A(y)\) that creates the ratio
\[
\frac{\mathbb E c_A^2}{(\mathbb E c_A)^2}.
\]
Thus it does not prove a dimension-free bound for \(B_{\rm can}/I\), and it does not overcome the certified lower obstruction
\(B_{\rm can}/I\ge 2.323994990262646786\ldots\) supplied by the current balanced-composition handoff.

A useful exact corollary of (2.1) and (BC_*) is:
if a constant \(C_X\) is known for every Boolean restriction on block \(X\), then
\[
H(S\cap X)
\le C_X\sum_{i\in X}\operatorname{Inf}_i(f)
+\frac2{\ln2}\sum_{j\in Y}\operatorname{Inf}_j(f).
\]
Naively summing this over many blocks overcharges the outside influences, so this alone is not a dimension-free FEI proof.

## 8. Dead route and next attack

**REFUTED:** a coefficient-2 universal block-channel payment. The bent one-point-flip family forces the exact larger coefficient \(2/\ln2\).

**PROVED:** the sharp universal block-spectral information inequality (BC_*), including an explicit asymptotically sharp Boolean family.

**OPEN:** a dimension-independent cancellation-entropy upper bound; full FEI.

**Next attack:** add the missing sign/phase information to the block channel. For each block coefficient \(c_A(y)\), split the cancellation quantity
\[
\log\frac{\mathbb E c_A^2}{(\mathbb E c_A)^2}
\]
into a magnitude-profile contribution and a signed phase contribution. The magnitude channel is now paid sharply by \(2/\ln2\) times outside influence. The next lemma should construct a phase-aware stopping/random-chain channel whose signed contribution is charged to strict supersets without counting a Fourier atom once for every ancestor. The circulant autocorrelation/Sidon constraints from the previous B13 run are a natural mechanism for preventing arbitrary phase cancellation.

## 9. Classification

- **PROVED (universal auxiliary theorem):** (BC_*) with optimal constant \(2/\ln2\).
- **REFUTED (stronger auxiliary statement):** coefficient \(2\) in place of \(2/\ln2\).
- **COMPUTATIONAL EVIDENCE ONLY:** exhaustive maxima through \(n=4\) and the numerical convergence table.
- **OPEN:** universal \(B_{\rm can}\le cI\) for some dimension-independent \(c\).
- **OPEN:** full uniform-cube FEI.
- **NOT CLAIMED:** novelty/publication priority for the auxiliary theorem or its classical information-theoretic ingredient.
