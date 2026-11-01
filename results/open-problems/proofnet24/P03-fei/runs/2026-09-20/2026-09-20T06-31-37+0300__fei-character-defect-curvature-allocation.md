Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.

# P03 FEI — character-defect allocation and a telescoping square-curvature payment

## Status / before-after

**Parent problem.** Friedgut--Kalai Fourier entropy--influence (FEI): prove one finite universal constant \(C\) such that
\[
H(\widehat f^{\,2})\le C I(f)
\]
for every Boolean \(f\) on every finite uniform cube.

**Source-level status before -> after:** **OPEN/PARTIAL -> OPEN/PARTIAL.** No universal FEI constant is proved here. The source-level finite universal upper bound remains **UNKNOWN -> UNKNOWN**. P03's inherited native finite-dimensional atlas remains **6 -> 6**.

**Mechanism-level advance.** This run produces two all-dimensional, fresh-variable-free hereditary estimates and one decisive obstruction.

1. The newest P03 minor-child theorem is strengthened by replacing the smaller child's **total influence** with its **spectral character defect**
   \[
   \kappa(g):=1-\max_A \widehat g(A)^2.
   \]
   For every split coordinate \(i\),
   \[
   \boxed{
   B_i(f):=H(Z_i\mid Z_{-i})
   \le C_\chi j_i(f)+
   \min\{\kappa(f^+),\kappa(f^-)\},
   }
   \tag{A}
   \]
   where
   \[
   C_\chi=2+\frac1{\sqrt e\,\ln2}=2.8750387749\ldots,\qquad
   j_i=\min\{\operatorname{Inf}_i,1-\operatorname{Inf}_i\}.
   \]
   Moreover \(\kappa(g)\le J(g)\le I(g)\), so (A) pointwise strengthens the previous arbitrary-child theorem.

2. Odd majority is a decisive obstruction to turning (A) into a universal nodewise selector: for \(n=2m+1\), every coordinate has \(B_i=0\), but
   \[
   \frac{\min\{\kappa(f^+),\kappa(f^-)\}}{j_i(f)}
   \ge \frac{1-\delta_n}{\delta_n}\to\infty,
   \quad
   \delta_n=\frac{\binom{2m}{m}}{2^{2m}}.
   \]
   Thus "find \(i\) with small child character defect relative to \(j_i\)" is false even on a known FEI-positive symmetric family.

3. A different route succeeds: use the **physical multiplicative derivative**
   \[
   D_i f(x_{-i})=f(+1,x_{-i})f(-1,x_{-i}).
   \]
   Every coordinate obeys the all-dimensional local bound
   \[
   \boxed{
   B_i(f)\le \frac12 I(D_i f)+\frac1{\ln2}j_i(f).
   }
   \tag{B}
   \]
   The first term telescopes *exactly* on every adaptive physical restriction tree into a root second-order square-curvature. For
   \[
   \mathcal C_2(f):=
   \sum_{i<k}
   \Pr\!\left[
   f(x)f(x^{(i)})f(x^{(k)})f(x^{(i,k)})=-1
   \right],
   \]
   every full adaptive tree satisfies
   \[
   \sum_{v\ {\rm internal}}w_v I(D_{i(v)}f_v)=\mathcal C_2(f).
   \]
   Combining this with P03's already-proved dependent-branch recombination payment gives the universal auxiliary inequality
   \[
   \boxed{
   H(f)\le \frac12\mathcal C_2(f)+\frac3{\ln2}J(f).
   }
   \tag{C}
   \]
   More usefully for stopping trees, if the **consumed curvature**
   \[
   \mathcal C_{\mathcal T}
   :=\sum_{v\ {\rm internal}}w_v I(D_{i(v)}f_v)
   \]
   satisfies \(\mathcal C_{\mathcal T}\le KQ_{\mathcal T}\) and every stopping leaf has FEI constant \(C_0\), then
   \[
   \boxed{
   H(f)\le
   \max\!\left\{
   C_0,\frac K2+\frac3{\ln2}
   \right\}I(f).
   }
   \tag{D}
   \]
   This is a new source-facing reduction: pay entropy by *square curvature consumed before reaching certified leaves*. It does not require fresh variables or branch independence.

The global curvature itself is not universally \(O(I)\): the complete quadratic phase
\[
(-1)^{\sum_{i<j}x_ix_j}
\]
has \(I=n/2\) and \(\mathcal C_2=\binom n2\). Hence (C) alone is not FEI. The stopping version (D) is the live route: dense quadratic pieces should be stopped at the already-certified quadratic leaf class rather than expanded until their curvature is paid.

## Dependencies actually consumed

The progress-first policy was followed: only the dependencies needed for the live FEI mechanism were read, not the whole archive.

- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`: P03 remains T01 owner; new derivation takes priority over routine audit.
- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`: the fresh-control theorem `L(Gamma_c f)<=12 Delta_aff(Gamma_c f)` assumes appended controls and `2^{-c}M_0(f)<=1`; it is explicitly not full FEI.
- `proofnet24/P03-fei/README.md`, blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`: full FEI remains open; the shifted-threshold Han-overlap obstruction, all-fixed-coefficient drift warning, and retired resolvent/erasure shortcuts remain in force.
- Newest own substantive report `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T05-32-22+0300__fei-minor-child-allocation.md`, blob `7e12f35a9c2fae61f3c63e8434a493762a0e8081`: supplies the arbitrary-child bound with residual `min{I(f+),I(f-)}` and the influence-heavy-spine theorem.
- P03 recombination report `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T02-31-19__fei-hereditary-recombination-refinement.md`, blob `8ffb9da5bc03c30e6ed5f62adc17640d1570878c`: supplies the exact tree identities and
  \[
  S_{\mathcal T}\le(2/\ln2)J_{\mathcal T}.
  \]
- Companion NM13-02 report `proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T06-10-00+0300__quadratic-one-defect-hereditary.md`, blob `c46f7d38885d6cdf98a80e54d629e5660908a01e`: independently sharpens the minor-child residual by truncating it at the marginal-entropy residual and proves one-point perturbations of arbitrary quadratics have bounded hereditary allocation. The present run takes complementary scope: replace child influence by largest-atom defect, falsify its universal selector, then switch to a physical derivative-curvature payment.
- `proofnet24/P03-fei/continuations/2026-09-20-entropy-continuity/ERASURE_RIGIDITY.md`, blob `52a0834a88d957d0331da95aa444406530741f7f`: shows an individual `B_i/Inf_i` can diverge on a bent-background one-point defect. The curvature payment below explains where that logarithm can be charged: the physical boundary of the disagreement set of `D_i f`.
- `proofnet24/P03-fei/continuations/2026-09-20-quadratic-symmetry/REPORT.md`: arbitrary quadratic twists of symmetric cores are a certified stopping class, not full FEI.
- `POSTED.md` was checked for exact-scope exclusions. No posted unrestricted FEI theorem is claimed or duplicated.

The historical companion label P11 is superseded by the current LIVE20 pairing with NM13-02. No peer file or peer claim was edited.

## Current public-source scope

A fresh source check on 20 September 2026 recovered González--MacManus--Pereyra, arXiv:2606.00246v2, last revised 9 June 2026. It still states universal FEI as the Friedgut--Kalai conjecture and develops a coordinate-splitting/stopping-tree sufficient condition plus restricted classes (`delta`-tribes and separation classes). It does not prove universal FEI.

The paper's local induction asks to pay the full entropy decrement at branching nodes. P03's earlier tree theorem already paid the dependent-branch recombination remainder universally, leaving hereditary `B_i` allocation. The curvature theorem below gives a new way to pay that hereditary term and is therefore directly aligned with the source stopping-tree architecture, but its curvature/influence condition is not proved universally.

The Friedgut--Kalai 1996 source attribution is preserved. A bounded source check is not a publication-priority certificate for the new lemmas below; priority remains UNVERIFIED.

## 1. Notation

Let \(f:\{-1,1\}^V\to\{-1,1\}\). Its squared Fourier law is
\[
\Pr(Z=S)=\widehat f(S)^2.
\]
For \(i\in V\), define
\[
B_i(f)=H(Z_i\mid Z_{V\setminus\{i\}}),
\qquad
\alpha_i(f)=\operatorname{Inf}_i(f),
\qquad
j_i(f)=\min\{\alpha_i(f),1-\alpha_i(f)\}.
\]
Also
\[
J(f)=\sum_i j_i(f).
\]

For the two physical restrictions at coordinate \(i\), write
\[
g=f^+,\qquad h=f^-,
\]
and their Fourier coefficients on \(V\setminus\{i\}\) as
\[
a_T=\widehat g(T),\qquad b_T=\widehat h(T).
\]
The parent coefficients in the \(i\)-fiber are
\[
\widehat f(T)=\frac{a_T+b_T}{2},
\qquad
\widehat f(T\cup\{i\})=\frac{a_T-b_T}{2}.
\]
Thus with
\[
q_T=\frac{a_T^2+b_T^2}{2},
\qquad
e_T=\frac{(a_T-b_T)^2}{4},
\]
one has the exact fiber formula
\[
B_i(f)=\sum_T q_T h_2(e_T/q_T),
\tag{1.1}
\]
with zero-mass terms interpreted as zero.

Define the **spectral character defect**
\[
\kappa(u):=1-\max_A\widehat u(A)^2.
\tag{1.2}
\]
It is zero exactly for signed characters.

## 2. Character-defect refinement of the minor-child theorem

### Theorem 2.1

For every Boolean \(f\) and every physical coordinate \(i\),
\[
\boxed{
B_i(f)
\le
C_\chi j_i(f)+
\min\{\kappa(f^+),\kappa(f^-)\}.
}
\tag{2.1}
\]

Moreover, for every Boolean \(u\),
\[
\boxed{\kappa(u)\le J(u)\le I(u).}
\tag{2.2}
\]
Therefore (2.1) pointwise strengthens the preceding P03 arbitrary-child theorem.

### Proof

Multiplying the parent by the physical character \(x_i\) swaps the two spectral masses in every \(i\)-fiber. It leaves \(B_i\), both child character defects, and both child total influences unchanged, while replacing \(\alpha_i\) by \(1-\alpha_i\). We may therefore arrange
\[
\varepsilon:=\alpha_i(f)=j_i(f)\le\frac12.
\tag{2.3}
\]
Exchange the two children so that
\[
\kappa(g)=\min\{\kappa(f^+),\kappa(f^-)\}.
\tag{2.4}
\]

Choose a Fourier label \(A\) of \(g\) with
\[
\widehat g(A)^2=1-\kappa(g).
\]
Multiplying both children by the same residual character translates every residual Fourier label and therefore leaves the parent fiber entropies in (1.1) unchanged. A common sign also changes no squared Fourier quantity. Hence we may assume that the maximizing coefficient is the constant coefficient and is nonnegative:
\[
\widehat g(\varnothing)=\sqrt{1-\kappa(g)}\ge0.
\tag{2.5}
\]

Write
\[
\eta=\Pr(g=-1),\qquad \beta=\Pr(h=-1).
\]
Then
\[
\widehat g(\varnothing)=1-2\eta,\qquad
\widehat h(\varnothing)=1-2\beta,
\]
so (2.5) gives \(\eta\le1/2\), and
\[
\operatorname{Var}(g)=4\eta(1-\eta)=\kappa(g).
\tag{2.6}
\]
Because \(g\) and \(h\) differ on an \(\varepsilon\)-fraction of inputs,
\[
|\beta-\eta|\le\varepsilon.
\tag{2.7}
\]

For every nonconstant Fourier fiber \(T\ne\varnothing\), binary entropy is at most one. Therefore
\[
\begin{aligned}
\sum_{T\ne\varnothing}q_T h_2(e_T/q_T)
&\le \sum_{T\ne\varnothing}q_T\\
&=\frac12(\operatorname{Var}(g)+\operatorname{Var}(h)).
\end{aligned}
\tag{2.8}
\]
We claim
\[
\beta(1-\beta)\le
\eta(1-\eta)+\varepsilon(1-\varepsilon).
\tag{2.9}
\]
Put \(t=\beta-\eta\). If \(t\le0\), then
\[
\beta(1-\beta)-\eta(1-\eta)
=t(1-2\eta)-t^2\le0.
\]
If \(t\ge0\), then \(0\le t\le\varepsilon\le1/2\), and
\[
t(1-2\eta)-t^2
\le t(1-t)
\le\varepsilon(1-\varepsilon).
\]
This proves (2.9). Using (2.6),
\[
\sum_{T\ne\varnothing}q_T h_2(e_T/q_T)
\le
\kappa(g)+2\varepsilon(1-\varepsilon).
\tag{2.10}
\]

For the constant fiber,
\[
e_\varnothing
=\frac{(\widehat g(\varnothing)-\widehat h(\varnothing))^2}{4}
=(\beta-\eta)^2
\le\varepsilon^2.
\tag{2.11}
\]
For fixed \(0\le e\le q\le1\), the function
\[
q\mapsto qh_2(e/q)
\]
is increasing, because its derivative is
\[
\log_2\frac{q}{q-e}\ge0.
\]
Hence the constant-fiber contribution is at most \(h_2(e_\varnothing)\). The elementary bound
\[
h_2(x)\le x\log_2(e/x),\qquad 0\le x\le1,
\]
and monotonicity of \(x\log_2(e/x)\) on \([0,1]\) give
\[
q_\varnothing h_2(e_\varnothing/q_\varnothing)
\le
\varepsilon^2\log_2(e/\varepsilon^2).
\tag{2.12}
\]

Combining (2.10)--(2.12),
\[
B_i(f)\le
\kappa(g)+\varepsilon U(\varepsilon),
\]
where
\[
U(\varepsilon)
=
2(1-\varepsilon)
+
\varepsilon\log_2(e/\varepsilon^2).
\tag{2.13}
\]
On \(0<\varepsilon\le1/2\),
\[
U''(\varepsilon)=-\frac{2}{\varepsilon\ln2}<0,
\]
and the unique critical point is
\[
\varepsilon_0=\frac1{2\sqrt e}.
\]
At this point
\[
U(\varepsilon_0)
=
2+\frac1{\sqrt e\,\ln2}
=C_\chi.
\]
The endpoint limit is smaller, so \(U(\varepsilon)\le C_\chi\). This proves (2.1).

It remains to prove (2.2). Let \(Z\) have the squared Fourier law of \(u\). Choose the coordinatewise modal atom \(A_0\), i.e. put \(i\in A_0\) iff
\[
\Pr(i\in Z)>1/2.
\]
Then
\[
\mathbb E|Z\triangle A_0|
=
\sum_i\min\{\Pr(i\in Z),1-\Pr(i\in Z)\}
=J(u).
\]
If \(J(u)\ge1\), then \(\kappa(u)\le1\le J(u)\). If \(J(u)<1\), Markov's inequality for the nonnegative integer \(|Z\triangle A_0|\) gives
\[
\Pr(Z\ne A_0)\le J(u),
\]
so
\[
\max_A\Pr(Z=A)\ge \Pr(Z=A_0)\ge1-J(u).
\]
Thus \(\kappa(u)\le J(u)\). Finally \(J(u)\le I(u)\) term by term. QED.

### Corollary 2.2 — truncated character-defect residual

Since always
\[
B_i(f)\le H(Z_i)=h_2(j_i(f)),
\]
Theorem 2.1 also gives
\[
\boxed{
B_i(f)\le C_\chi j_i(f)+
\min\!\left\{
\kappa_i^{\min},
[h_2(j_i)-C_\chi j_i]_+
\right\},
}
\tag{2.14}
\]
where
\[
\kappa_i^{\min}
=
\min\{\kappa(f^+),\kappa(f^-)\}.
\]
This pointwise dominates the companion NM13-02 truncated minor-child theorem because \(\kappa(u)\le J(u)\le I(u)\).

On a restriction tree,
\[
R_{\mathcal T}
\le
C_\chi J_{\mathcal T}
+
K_{\mathcal T},
\qquad
K_{\mathcal T}
:=
\sum_vw_v\kappa_{i(v)}^{\min}.
\tag{2.15}
\]
Thus character-near children are cheap without needing their total influence to be small.

## 3. Decisive obstruction: odd majority kills a universal character-defect selector

The natural next hope after Theorem 2.1 would be:

> there is a universal \(K\) such that every nonconstant Boolean function has some coordinate \(i\) with
> \[
> \min\{\kappa(f^+),\kappa(f^-)\}\le K j_i(f).
> \tag{3.1}
> \]

This is false.

### Theorem 3.1

Let \(n=2m+1\) and let \(M_n\) be odd majority. For every coordinate \(i\),
\[
B_i(M_n)=0,
\tag{3.2}
\]
\[
j_i(M_n)=\delta_n
=
\frac{\binom{2m}{m}}{2^{2m}},
\tag{3.3}
\]
and
\[
\min\{\kappa(M_n^+),\kappa(M_n^-)\}
\ge1-\delta_n.
\tag{3.4}
\]
Consequently
\[
\frac{\min\{\kappa(M_n^+),\kappa(M_n^-)\}}
     {j_i(M_n)}
\ge
\frac{1-\delta_n}{\delta_n}
\sim\sqrt{\pi m}\to\infty.
\tag{3.5}
\]

### Proof

The influence formula (3.3) is the standard pivotal-slice count: the other \(2m\) bits must contain exactly \(m\) pluses and \(m\) minuses.

Odd majority satisfies
\[
M_n(-x)=-M_n(x).
\]
Therefore its Fourier coefficients vanish on every even level. Under the squared Fourier law the random spectral set \(Z\) has odd cardinality almost surely. Given \(Z_{-i}\), the bit \(Z_i\) is forced by the parity condition
\[
|Z_{-i}|+Z_i\equiv1\pmod2.
\]
Hence \(B_i=0\), proving (3.2).

Consider one child \(g=M_n^+\) on \(2m\) variables. Its mean is \(\delta_n\), so its constant Fourier mass is \(\delta_n^2\le\delta_n\). By symmetry, every residual coordinate \(k\) has
\[
\operatorname{Inf}_k(g)=\delta_n.
\tag{3.6}
\]
If \(S\ne\varnothing\) and \(k\in S\), then
\[
\widehat g(S)^2
\le
\sum_{T\ni k}\widehat g(T)^2
=
\operatorname{Inf}_k(g)
=
\delta_n.
\tag{3.7}
\]
Thus every squared Fourier atom of \(g\) has mass at most \(\delta_n\). The same holds for the other child by complement symmetry. Therefore each child has
\[
\kappa\ge1-\delta_n,
\]
which is (3.4). Stirling's formula gives
\[
\delta_n\sim(\pi m)^{-1/2},
\]
proving (3.5). QED.

This is not an FEI obstruction: majority is a known FEI-positive symmetric family. It is specifically an obstruction to replacing the hereditary problem by a character-proximity selector. The striking feature is that the *true* local allocation is zero while the proposed surrogate tends to its maximal value.

This failed recovery route is retained rather than hidden. It motivates a different method in the remainder of this report.

## 4. A local physical-derivative payment

Define the multiplicative derivative
\[
D_i f(x_{-i})
=
f(+1,x_{-i})f(-1,x_{-i}).
\tag{4.1}
\]
Its value is \(-1\) precisely on the \(i\)-edges where \(f\) changes, so
\[
\Pr(D_i f=-1)=\alpha_i(f).
\tag{4.2}
\]
Multiplying \(D_i f\) by \(-1\) does not change its total influence. Hence the minority density of \(D_i f\) is exactly \(j_i(f)\).

### Lemma 4.1 — cube edge isoperimetry in influence normalization

If \(u:\{-1,1\}^d\to\{-1,1\}\) has minority density \(p\le1/2\), then
\[
\boxed{
I(u)\ge2p\log_2(1/p).
}
\tag{4.3}
\]

#### Proof

Let \(A\) be the minority set, \(|A|=p2^d\), and let \(\partial A\) be its undirected cube edge boundary. We prove by induction on \(d\) that
\[
|\partial A|
\ge
|A|\log_2\frac{2^d}{|A|}.
\tag{4.4}
\]

Split the cube by the last coordinate, writing section sizes \(a,b\) and, without loss, \(a\ge b\). By induction, the within-section boundary contributes at least
\[
a\log_2\frac{2^{d-1}}a
+
b\log_2\frac{2^{d-1}}b.
\]
The matching edges between the two sections contribute at least \(|a-b|\). Put \(s=a+b\) and \(q=b/s\in[0,1/2]\). The difference between this lower bound and
\[
s\log_2\frac{2^d}s
\]
equals
\[
s\,[h_2(q)-2q].
\]
Binary entropy is concave and lies above the chord joining \((0,0)\) and \((1/2,1)\), so
\[
h_2(q)\ge2q.
\]
This proves (4.4).

Each boundary edge is seen from both endpoints in the influence normalization, so
\[
I(u)=\frac{2|\partial A|}{2^d}.
\]
Substituting \(|A|=p2^d\) into (4.4) proves (4.3). QED.

### Theorem 4.2 — local curvature payment

For every Boolean \(f\) and coordinate \(i\),
\[
\boxed{
B_i(f)
\le
\frac12 I(D_i f)+\frac1{\ln2}j_i(f).
}
\tag{4.5}
\]

### Proof

Conditioning cannot increase entropy, so
\[
B_i(f)\le H(Z_i)=h_2(\alpha_i)=h_2(j_i).
\tag{4.6}
\]
For \(0\le p\le1/2\),
\[
h_2(p)
=
p\log_2(1/p)
+
(1-p)\log_2(1/(1-p)).
\]
The second term satisfies
\[
-(1-p)\ln(1-p)\le p,
\]
hence
\[
h_2(p)
\le
p\log_2(1/p)+\frac p{\ln2}.
\tag{4.7}
\]
Apply Lemma 4.1 to \(D_i f\), whose minority density is \(p=j_i(f)\):
\[
p\log_2(1/p)\le\frac12 I(D_i f).
\tag{4.8}
\]
Combining (4.6)--(4.8) gives (4.5). The endpoint \(p=0\) follows by continuity. QED.

### Why this pays the preceding rare-coordinate obstruction

In the bent-background one-point-defect family from the entropy-continuity continuation, the queried coordinate has \(j_i=\delta\) and \(B_i\asymp\delta\log(1/\delta)\). Its derivative \(D_i f\) is itself a one-point defect, whose edge boundary has total influence of order \(\delta\log_2(1/\delta)\). Thus (4.5) puts the logarithmic loss on an actual physical boundary rather than on a scalar marginal or derivative degree.

## 5. Exact square-curvature telescope

For distinct physical coordinates \(i,k\), define
\[
c_{ik}(f)
:=
\Pr_x\!\left[
f(x)f(x^{(i)})f(x^{(k)})f(x^{(i,k)})=-1\right].
\tag{5.1}
\]
This is symmetric in \(i,k\). It is exactly the \(k\)-influence of the multiplicative derivative:
\[
c_{ik}(f)=\operatorname{Inf}_k(D_i f).
\tag{5.2}
\]
Define
\[
\mathcal C_2(f)=\sum_{i<k}c_{ik}(f).
\tag{5.3}
\]
Then
\[
I(D_i f)=\sum_{k\ne i}c_{ik}(f).
\tag{5.4}
\]

### Lemma 5.1 — one-step curvature decomposition

For every split coordinate \(i\),
\[
\boxed{
\mathcal C_2(f)
=
I(D_i f)
+
\frac{\mathcal C_2(f^+)+\mathcal C_2(f^-)}2.
}
\tag{5.5}
\]

### Proof

The pairs involving \(i\) contribute
\[
\sum_{k\ne i}c_{ik}(f)=I(D_i f)
\]
by (5.4).

For a pair \(j,k\ne i\), the square defining \(c_{jk}(f)\) lies wholly in one of the two \(i\)-slices. Averaging over the uniform value of \(x_i\) therefore gives
\[
c_{jk}(f)
=
\frac{c_{jk}(f^+)+c_{jk}(f^-)}2.
\]
Summing over all pairs not involving \(i\) gives (5.5). QED.

### Theorem 5.2 — adaptive tree curvature identity

Let \(\mathcal T\) be any adaptive physical restriction tree, with node weights \(w_v=2^{-\mathrm{depth}(v)}\). Define
\[
\mathcal C_{\mathcal T}
:=
\sum_{v\ {\rm internal}}
w_v I(D_{i(v)}f_v),
\]
and
\[
\mathcal C_L
:=
\sum_{\ell\ {\rm leaf}}
w_\ell \mathcal C_2(f_\ell).
\]
Then
\[
\boxed{
\mathcal C_2(f)=\mathcal C_{\mathcal T}+\mathcal C_L.
}
\tag{5.6}
\]
In particular, for a full tree ending at constants,
\[
\boxed{
\mathcal C_{\mathcal T}=\mathcal C_2(f).
}
\tag{5.7}
\]

### Proof

Multiply (5.5) at each internal node by its weight and sum. Every nonroot internal curvature appears once positively and once negatively because each child has half the parent weight. The surviving terms are the root curvature, the local derivative-influence charges, and the weighted leaf curvatures. Rearranging gives (5.6). Constants have zero curvature, giving (5.7). QED.

## 6. Folded influence is also a tree budget

For every split coordinate \(i\), ordinary influence satisfies
\[
\operatorname{Inf}_k(f)
=
\frac{\operatorname{Inf}_k(f^+)+\operatorname{Inf}_k(f^-)}2
\qquad(k\ne i).
\tag{6.1}
\]
The function \(t\mapsto\min\{t,1-t\}\) is concave. Therefore
\[
\boxed{
J(f)
\ge
j_i(f)+\frac{J(f^+)+J(f^-)}2.
}
\tag{6.2}
\]
Telescoping on a restriction tree gives
\[
\boxed{
J_{\mathcal T}+J_L\le J(f),
}
\tag{6.3}
\]
where
\[
J_{\mathcal T}=\sum_{v\ {\rm internal}}w_vj_{i(v)}(f_v),
\qquad
J_L=\sum_{\ell}w_\ell J(f_\ell).
\]
In particular \(J_{\mathcal T}\le J(f)\).

## 7. Global and stopping-tree consequences

P03's earlier paid recombination theorem gives, for every restriction tree,
\[
H(f)-H_L=R_{\mathcal T}+S_{\mathcal T},
\tag{7.1}
\]
\[
I(f)-I_L=Q_{\mathcal T},
\tag{7.2}
\]
and
\[
0\le S_{\mathcal T}
\le\frac2{\ln2}J_{\mathcal T}.
\tag{7.3}
\]

Summing Theorem 4.2 over the internal nodes gives
\[
R_{\mathcal T}
\le
\frac12\mathcal C_{\mathcal T}
+
\frac1{\ln2}J_{\mathcal T}.
\tag{7.4}
\]
Combining with (7.3),
\[
\boxed{
H(f)
\le
H_L+
\frac12\mathcal C_{\mathcal T}
+
\frac3{\ln2}J_{\mathcal T}.
}
\tag{7.5}
\]

### Corollary 7.1 — universal root-static second-order bound

Take any full tree to constants. Then \(H_L=0\), Theorem 5.2 gives \(\mathcal C_{\mathcal T}=\mathcal C_2(f)\), and (6.3) gives \(J_{\mathcal T}\le J(f)\). Thus
\[
\boxed{
H(f)
\le
\frac12\mathcal C_2(f)
+
\frac3{\ln2}J(f).
}
\tag{7.6}
\]

No fresh controls, branch independence, bounded degree, symmetry, or monotonicity is assumed.

### Corollary 7.2 — curvature-paid stopping theorem

Suppose a stopping tree has
\[
\mathcal C_{\mathcal T}\le K Q_{\mathcal T}
\tag{7.7}
\]
and every leaf satisfies
\[
H(f_\ell)\le C_0 I(f_\ell).
\tag{7.8}
\]
Then
\[
\boxed{
H(f)
\le
\max\!\left\{
C_0,\frac K2+\frac3{\ln2}
\right\}I(f).
}
\tag{7.9}
\]

### Proof

By (7.5), \(J_{\mathcal T}\le Q_{\mathcal T}\), (7.7), and (7.8),
\[
H(f)
\le
C_0 I_L
+
\left(\frac K2+\frac3{\ln2}\right)Q_{\mathcal T}.
\]
Use the exact influence budget
\[
I_L+Q_{\mathcal T}=I(f)
\]
from (7.2), and bound the convex combination by the larger coefficient. QED.

This is the main source-facing theorem of the run. It weakens a local entropy-decrement requirement into an aggregate, exactly telescoping second-order physical payment. It can stop before paying curvature inside any already-certified FEI leaf class.

## 8. Why root curvature alone cannot close FEI

Let
\[
q_n(x)=\sum_{1\le i<j\le n}x_ix_j\pmod2,
\qquad
f_n=(-1)^{q_n}.
\]
For every coordinate \(i\),
\[
D_i f_n(x_{-i})
=
(-1)^{\sum_{j\ne i}x_j}
\]
up to an irrelevant constant sign. It is a nonconstant character, so
\[
\operatorname{Inf}_i(f_n)=\frac12,
\qquad
I(f_n)=\frac n2.
\tag{8.1}
\]
For every \(k\ne i\),
\[
\operatorname{Inf}_k(D_i f_n)=1.
\]
Hence
\[
\mathcal C_2(f_n)=\binom n2,
\qquad
\frac{\mathcal C_2(f_n)}{I(f_n)}=n-1\to\infty.
\tag{8.2}
\]

Therefore a universal estimate \(\mathcal C_2\le KI\) is false. This is not an FEI counterexample: quadratic phases already have a separate hereditary rank certificate. It shows why Corollary 7.2 must be used as a stopping theorem rather than by fully expanding every function.

## 9. Methods compared and failure accounting

Three materially different mechanisms were considered in this run.

1. **Largest-child Fourier atom / character defect.** Successful local strengthening: Theorem 2.1 replaces child total influence by the smaller spectral defect \(\kappa\). It strictly improves the inherited local theorem on many functions and recovers zero residual for character children. However, odd majority proves that no universal coordinate selector of the form \(\kappa_{\min}\le K j_i\) exists.

2. **Affine/parity prediction of the spectral bit.** Majority's \(B_i=0\) comes from an exact parity constraint on the Fourier support. This suggests replacing character proximity by general affine spectral constraints. I did not promote this to a theorem because no source-influence payment for arbitrary affine predictors was obtained in this run. This remains a possible later route, not claimed progress.

3. **Physical multiplicative derivative and square curvature.** Successful and genuinely different. Cube edge isoperimetry converts the dangerous \(j\log(1/j)\) local entropy into the physical boundary \(I(D_i f)\), and the resulting second-order quantity has an exact adaptive restriction-tree telescope. This yields Theorem 7.2.

The prior derivative-degree/marginal-envelope route remains refuted by the one-defect family; fixed-coefficient affine drift remains refuted; Han's absolute-overlap selector remains refuted; the false pointwise erasure shortcut and resolvent claims remain retired. None is revived here.

## 10. Executed sanity checks

A new self-checker was executed before persistence and then preserved:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T06-31-37+0300__check_character_curvature_allocation.py`

Creation commit:
`3b2d93818cf64568983189211bdc4b3460daee9b`

Blob after readback:
`2932fb284b1757a5eedb7f58b4f567694c1b42a1`

Actual output:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T06-31-37+0300__character_curvature_check.json`

Creation commit:
`5776e69d31fd376808f259db52bf7daee6270f96`

Blob after readback:
`ab442498a627e9b37bad5f8fe4f823387a15423f`

The checker exhausts all Boolean truth tables through dimension four: **262,948 coordinate cases**. It verifies:

- Theorem 2.1;
- Corollary 2.2;
- \(\kappa\le J\);
- the local curvature payment (4.5);
- the global bound (7.6);
- exact curvature telescoping on a function-dependent adaptive full tree;
- the folded tree budget \(J_{\mathcal T}\le J(f)\).

Every recorded maximum violation is `0.0` at floating tolerance. It also tests 9,400 fixed-seed random coordinate cases in dimensions 5--7; all pass. Odd majority is checked by complete Walsh transforms through dimension 15, giving exactly `B_i=0`; the reported lower ratio grows from `1.5` at \(n=3\) to `4.5644...` at \(n=15\). The analytic \(n=101\) lower ratio is already `11.5645...`.

These computations are sanity checks, not independent audits. The theorem claims rest on the proofs above.

## 11. Remaining full-scope obstruction and next attack

The new stopping criterion isolates a concrete universal question:

> Can every Boolean function be given a physical stopping tree whose leaves lie in already-certified FEI classes and whose **consumed square curvature** satisfies
> \[
> \mathcal C_{\mathcal T}=O(Q_{\mathcal T})?
> \]

A blind full tree cannot satisfy this: dense quadratic phases have curvature/influence ratio \(n-1\), but they should be stopped immediately because they already possess a hereditary quadratic certificate. The next nonredundant attack should therefore test **curvature-aware max-splicing**: at each node, either stop when one of the current certified hereditary classes applies (quadratic, symmetric/quadratic-twist, character-canalizing, one-point quadratic perturbation), or query a coordinate for which derivative boundary is cheap relative to influence consumed. A counterfamily forcing large curvature before every certified stopping class is reached would decisively refute this route.

A second, complementary route is the affine spectral-predictor idea suggested by majority, but it should not be pursued unless an ordinary-influence payment for the chosen affine predictor is proved.

Full FEI remains open.

## ledger_delta

```yaml
track: P03
parent: T01_FOURIER_ENTROPY_INFLUENCE
source_status_before: OPEN_PARTIAL
source_status_after: OPEN_PARTIAL
universal_finite_C_before: UNKNOWN
universal_finite_C_after: UNKNOWN
native_finite_atlas_before: 6
native_finite_atlas_after: 6
mechanism_add:
  - CHARACTER_DEFECT_LOCAL_PAYMENT:
      status: PROVED_SELF_CHECKED
      statement: "B_i <= C_chi j_i + min(kappa(f+),kappa(f-)); kappa<=J<=I"
  - MAJORITY_CHARACTER_SELECTOR_OBSTRUCTION:
      status: PROVED_SELF_CHECKED
      statement: "odd majority has B_i=0 but kappa_min/j_i -> infinity for every coordinate"
  - SQUARE_CURVATURE_LOCAL_PAYMENT:
      status: PROVED_SELF_CHECKED
      statement: "B_i <= (1/2) I(D_i f) + j_i/ln2"
  - ADAPTIVE_CURVATURE_TELESCOPE:
      status: PROVED_SELF_CHECKED
      statement: "C2(root)=sum_internal w I(D_i f_v)+sum_leaf w C2(f_leaf)"
  - CURVATURE_PAID_STOPPING_THEOREM:
      status: PROVED_SELF_CHECKED
      statement: "if C_T<=K Q_T and leaves FEI(C0), root FEI(max(C0,K/2+3/ln2))"
route_refuted:
  - "universal nodewise child-character-defect selector kappa_min <= K j_i"
  - "universal root curvature bound C2 <= K I"
preserve_failed:
  - fixed_coefficient_affine_drift
  - pointwise_erasure_shortcut
  - resolvent_interpolation
  - Han_absolute_overlap_selector
  - derivative_degree_scalar_payment
fresh_controls_used: false
peer_files_modified: false
publication_priority: UNVERIFIED
remaining_obligation: "curvature-aware stopping/max-splicing with C_T=O(Q_T), or decisive counterfamily"
```

**End of complete run report.**
