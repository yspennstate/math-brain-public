# P0434 — arbitrary M-SERPT record-span coefficient and skipped-prefix scalar collapse

**Status: PROVED PARTIAL.** This is a finite-law structural lemma for Scully–Harchol-Balter–Scheller-Wolf (2020), Conjecture 8.1. It does **not** prove the full arbitrary-law factor-two conjecture.

Source: Ziv Scully, Mor Harchol-Balter, Alan Scheller-Wolf, *Simple Near-Optimal Scheduling for the M/G/1*, Proc. ACM Meas. Anal. Comput. Syst. 4(1), 2020, Conjecture 8.1, arXiv:1907.10792.

The source endpoint is

\[
E[T_{\rm MS}]\le 2E[T_G]
\]

for every source-admissible service-time distribution and every stable load, or a source-valid counterexample.

The inherited R7-04 theorem already proves factor two for every positive finite-support law with at most two strict internal M-SERPT record jumps. The first finite topology not covered by that theorem has at least three M-SERPT records and a longer prefix mismatch chain. The purpose of this note is to remove the support-cardinality dependence from one key coefficient in that longer chain.

---

## 1. Record coordinates

Write

\[
S(a)=P(X>a),\qquad N(a)=E[(X-a)^+],
\]

\[
c=1-\rho,\qquad A(a)=1-\lambda E[X\wedge a]=c+\lambda N(a).
\]

Consider any finite consecutive span of M-SERPT record ages

\[
a_0<a_1<\cdots<a_k.
\]

Put

\[
x_j=S(a_j),\qquad y_j=\lambda N(a_j),\qquad A_j=c+y_j,
\]

and

\[
p_j=x_{j-1}-x_j,\qquad P=x_0-x_k=\sum_{j=1}^k p_j.
\]

At M-SERPT records the SERPT record ratios are nondecreasing, so

\[
\frac{y_0}{x_0}\le \frac{y_1}{x_1}\le\cdots\le\frac{y_k}{x_k}.
\tag{1.1}
\]

Also `N` is nonincreasing, hence

\[
y_0\ge y_1\ge\cdots\ge y_k.
\tag{1.2}
\]

No assumption on the number of atoms inside the span is made beyond finiteness of the record chain.

---

## 2. Reciprocal-load record-span lemma

Define

\[
\Sigma_{0,k}:=
\sum_{j=1}^k\frac{p_j}{A_{j-1}A_j},
\tag{2.1}
\]

and the factor-two coarse-block coefficient

\[
K_{0,k}:=
\frac{2P}{A_0A_k}-\Sigma_{0,k}.
\tag{2.2}
\]

### Theorem 2.1 — strict positivity for an arbitrary record span

For every nonempty consecutive M-SERPT record span,

\[
\boxed{K_{0,k}>0.}
\tag{2.3}
\]

More precisely, let

\[
r_0:=\frac{y_0}{x_0},\qquad
\xi:=\frac{y_k}{r_0},\qquad
L:=x_0-\xi,\qquad R:=\xi-x_k.
\tag{2.4}
\]

Then `x_k<=xi<=x_0`, and

\[
\boxed{
\Sigma_{0,k}
\le
\frac{L}{A_0A_k}+\frac{R}{A_k^2}.
}
\tag{2.5}
\]

Consequently

\[
\boxed{
K_{0,k}
\ge
\frac{R}{A_0A_k}
+
\frac{L(c+r_0x_k)}{A_0A_k^2}
>0.
}
\tag{2.6}
\]

The terminal case `x_k=y_k=0` is included by taking `xi=R=0`.

### Proof

From (1.1),

\[
y_j\ge r_0x_j,
\]

while (1.2) gives `y_j>=y_k`. Therefore

\[
A_j\ge \phi(x_j),
\qquad
\phi(x):=c+\max\{r_0x,y_k\}.
\tag{2.7}
\]

Because `y_k/x_k>=r_0` and `y_k<=r_0x_0`, the breakpoint `xi=y_k/r_0` lies in `[x_k,x_0]`.

Replacing every denominator `A_j` by the smaller `phi(x_j)` can only increase the sum in (2.1). If the partition crosses `xi`, insert `xi` as an extra mesh point. This also increases the reciprocal-product Riemann sum: below `xi`, `phi` is already constant at `A_k`, whereas the unsplit crossing interval has the larger left denominator.

On `[xi,x_0]`,

\[
\phi(x)=c+r_0x,
\]

and each refined summand telescopes exactly:

\[
\frac{x_{j-1}-x_j}
{(c+r_0x_{j-1})(c+r_0x_j)}
=
\frac1{r_0}
\left(
\frac1{c+r_0x_j}-
\frac1{c+r_0x_{j-1}}
\right).
\tag{2.8}
\]

The total contribution of the linear part is therefore

\[
\frac1{r_0}\left(\frac1{A_k}-\frac1{A_0}\right)
=
\frac{L}{A_0A_k},
\tag{2.9}
\]

because `A_0-A_k=r_0L`. On `[x_k,xi]`, `phi=A_k`, so the contribution is `R/A_k^2`. This proves (2.5).

Using `P=L+R`,

\[
K_{0,k}
\ge
\frac{2P-L}{A_0A_k}-\frac{R}{A_k^2}
=
\frac{1}{A_0A_k}
\left(P-\frac{r_0LR}{A_k}\right).
\tag{2.10}
\]

Finally,

\[
P-\frac{r_0LR}{A_k}
=R+L\left(1-\frac{r_0R}{A_k}\right)
=R+L\frac{c+r_0x_k}{A_k},
\tag{2.11}
\]

which is strictly positive for a nonempty span because `c>0`. Substitution gives (2.6). QED.

---

## 3. Exact factor-two waiting-reserve decomposition

Let

\[
V_j=E[(X\wedge a_j)^2].
\]

Suppose one Gittins valley merges the consecutive M-SERPT blocks in the span `a_0,...,a_k`. The source's Proposition 4.7 waiting surrogate for the coarse Gittins block uses endpoint `V_k`, whereas M-SERPT uses the refined endpoints `V_j`.

The exact local factor-two waiting difference is

\[
\begin{aligned}
&\frac{2P V_k}{A_0A_k}
-
\sum_{j=1}^k\frac{p_jV_j}{A_{j-1}A_j}
\\
&\qquad=
K_{0,k}V_k
+
\sum_{j=1}^{k-1}
\frac{p_j(V_k-V_j)}{A_{j-1}A_j}.
\end{aligned}
\tag{3.1}
\]

Every term on the right is nonnegative, and the first is strictly positive when `V_k>0`. Restoring the common prefactor `lambda/2`,

\[
\boxed{
2\bar Q_G(a_0,a_k)-Q_{\rm MS}(a_0,a_k)
\ge
\frac{\lambda}{2}K_{0,k}V_k>0.
}
\tag{3.2}
\]

Thus an arbitrarily long skipped M-SERPT record prefix does **not** create a sign problem on the waiting side by itself. Its factor-two waiting reserve has a strictly positive endpoint coefficient controlled solely by the M-record geometry.

This is the discrete record-chain analogue of a positive prefix charge: it is not tied to three- or four-atom support.

---

## 4. Arbitrary-length skipped-prefix collapse to one scalar quadratic

The remaining difficulty is paying M-SERPT residence, not the sign of (3.1). Here is a support-cardinality-independent reduction of that payment problem.

Assume for this subsection that the record chain starts at age zero, so `A_0=1`, and that one Gittins valley merges the first `m` M-SERPT blocks and ends at the shared record `a_m`. Put

\[
a:=A_m,\qquad \rho=1-c,\qquad
P=\sum_{j=1}^m p_j,\qquad r=1-P,
\]

\[
y:=1-a,\qquad
q_j:=\lambda E[X\mathbf 1_{\{a_{j-1}<X\le a_j\}}],
\qquad
u:=\sum_{j=1}^m q_j.
\tag{4.1}
\]

Then the scaled terminal first moment is `rho-u`, while

\[
y-u=\lambda a_m r.
\tag{4.2}
\]

Write

\[
w_j:=\frac1{A_{j-1}},\qquad
\bar w:=\frac1P\sum_{j=1}^m p_jw_j,
\]

\[
\sigma_w^2:=\sum_{j=1}^m p_j(w_j-\bar w)^2,
\tag{4.3}
\]

and

\[
K:=\frac{2P}{a}-\sum_{j=1}^m\frac{p_j}{A_{j-1}A_j}>0,
\qquad
C:=K+\frac{r}{ac}>0.
\tag{4.4}
\]

Let

\[
H:=2\bar Q_G-Q_{\rm MS}+2E[X]-R_{\rm MS}.
\tag{4.5}
\]

After dropping only the nonnegative `V_m-V_j` terms in (3.1), blockwise Cauchy gives

\[
\lambda^2V_m
\ge
\sum_{j=1}^m\frac{q_j^2}{p_j}
+
\frac{(y-u)^2}{r},
\tag{4.6}
\]

\[
\lambda^2E[X^2]
\ge
\sum_{j=1}^m\frac{q_j^2}{p_j}
+
\frac{(\rho-u)^2}{r}.
\tag{4.7}
\]

Therefore

\[
\begin{aligned}
\lambda H\ge B(q_1,\ldots,q_m)
:=&\ 2\rho-\frac\rho a+\frac ua-\sum_{j=1}^m w_jq_j\\
&+\frac K2\left[
\sum_{j=1}^m\frac{q_j^2}{p_j}+\frac{(y-u)^2}{r}
\right]\\
&+\frac{r}{2ac}\left[
\sum_{j=1}^m\frac{q_j^2}{p_j}+\frac{(\rho-u)^2}{r}
\right].
\end{aligned}
\tag{4.8}
\]

At fixed `u`, the entire `m`-dimensional dependence is quadratic. Completing squares gives the exact unconstrained minimizer

\[
q_j^*=p_j\left[
\frac uP+\frac{w_j-\bar w}{C}
\right]
\tag{4.9}
\]

and the identity

\[
B(q)=B_*(u)
+\frac C2\sum_{j=1}^m\frac{(q_j-q_j^*)^2}{p_j},
\tag{4.10}
\]

where

\[
\boxed{
\begin{aligned}
B_*(u)=&\ 2\rho-\frac\rho a
+u\left(\frac1a-\bar w\right)
-\frac{\sigma_w^2}{2C}
+\frac{Cu^2}{2P}\\
&+\frac{K(y-u)^2}{2r}
+\frac{(\rho-u)^2}{2ac}.
\end{aligned}
}
\tag{4.11}
\]

Thus **an arbitrary number of skipped M-SERPT records collapses to one scalar convex quadratic** plus an explicit nonnegative square. No atom-by-atom response expression remains.

For `m=2`, this is the same real-line minimization architecture used in the already-proved two-record theorem. For `m>=3`, (4.11) is the first genuinely new unresolved prefix object.

### A second structural constraint

Because `w_{j+1}>=w_j`,

\[
\sum_{j=1}^m p_jw_j^2
\le
\sum_{j=1}^m p_jw_jw_{j+1}
=
\frac{2P}{a}-K,
\tag{4.12}
\]

where `w_{m+1}=1/a`. Therefore

\[
\boxed{
\sigma_w^2
\le
\frac{2P}{a}-K-P\bar w^2.
}
\tag{4.13}
\]

This couples the only negative term in (4.11) directly to the positive record-span coefficient `K`.

The final-record property also forces

\[
\frac{a-c}{r}\ge \rho,
\qquad\text{equivalently}\qquad
\rho P\ge 1-a.
\tag{4.14}
\]

If `t=(1-a)/rho` and `R=P-t`, then Theorem 2.1 specializes to

\[
\boxed{
K\ge
\frac{R}{a}
+
\frac{t(c+\rho r)}{a^2}
=
\frac Pa-\frac{(1-a)R}{a^2}.
}
\tag{4.15}
\]

Equations (4.11), (4.13), and (4.15) are the candidate induction-free interface for a general prefix proof.

---

## 5. What is and is not solved

The new proved facts are:

1. `K_{0,k}>0` for **every** finite consecutive M-SERPT record span, with the explicit lower bound (2.6).
2. Every Gittins valley that merges arbitrarily many M-SERPT blocks has the exact nonnegative factor-two waiting reserve (3.1).
3. The combined waiting/residence target for an arbitrarily long skipped initial prefix reduces exactly to the one-variable quadratic (4.11), with the variance constraint (4.13) and endpoint coefficient bound (4.15).

What is **not** proved is `B_*(u)>=0` for every physically admissible multi-record chain. That is now the finite-law bottleneck. It must not be replaced by numerical evidence or by treating another support family as a general theorem.

A useful easy subcase is `a>=1/2`: then `R_MS<=E[X]/a<=2E[X]`, while (3.2) already pays the waiting difference. Hence the genuinely difficult part of (4.11) lies in the high-load suffix `a<1/2`, exactly where the source's original all-load gap lives.

---

## 6. Handoff to P01-B

P01-B's newest endpoint primitive expresses the retained `D1+D3` reserve of an arbitrary M-SERPT valley using only endpoint values and shows that local valley payment must be replaced by a prefix potential. The present result supplies the complementary discrete ingredient:

- the factor-two waiting coefficient of **any length** record span is strictly positive;
- the entire skipped-prefix moment geometry compresses to `(K, wbar, sigma_w^2, a, c, P, r, u)`;
- `sigma_w^2` is itself bounded by `K` through (4.13).

The next useful shared target is therefore not another atom family. It is to prove or refute (4.11) on the admissible endpoint domain using P01-B's prefix potential / endpoint primitive. In a Stieltjes limit, (4.12) is the natural discrete quadratic-variation term that should accompany the endpoint primitive.

---

## 7. Exact checks

The exact rational checker

`research7_2026-09-17/R7-04/artifacts/2026-09-20/2026-09-20T180000Z__P0434_record_span_coefficient_checker.py`

verifies:

- the envelope/telescoping bound (2.5) and strict margin (2.6) on two independent rational record chains;
- the exact waiting decomposition (3.1);
- the exact square completion (4.10) on a three-record rational chain.

The archived output ends with `ALL_EXACT_CHECKS_PASS`. These are self-checks, not an independent publication audit.
