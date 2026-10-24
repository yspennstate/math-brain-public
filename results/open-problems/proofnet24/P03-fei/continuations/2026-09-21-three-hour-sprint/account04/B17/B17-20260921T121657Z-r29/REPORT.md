# B17 FEI creative run — quadratic code phases hide KL from every bounded local spectral view

**Run:** `B17-20260921T121657Z-r29`  
**Status:** PARTIAL. Full uniform-cube Fourier entropy–influence (FEI) remains **OPEN / NOT PROVED**.  
**Brain label:** **WITHOUT_VERIFIED_BRAIN**. No authenticated brain retrieval or receiver-side brain context was used.  
**Fresh scientific source state:** `yspennstate/math-open-problems` master `38478ec564b732c16e302f3be7504d1d23bbdf72` at the start of the derivation.  
**Active sprint:** `FEI-PROOF-NUMERICS-SPRINT-20260921T120803Z`; account04/B17 scope is adversarial non-read-once phase constructions.  
**Named universal obstruction attacked:** the previous B17 run showed that an FEI proof based on rare-history dependence must retain **conditional KL scale**, not merely Hellinger distance. This run asks whether a fixed-order local spectral/phase payment can recover that KL. The answer is no: exact Boolean quadratic phases can hide arbitrarily much total correlation from every fixed collection of low-order spectral marginals, even after a rare selector activates the phase.

Creative moves from `FLEET_RULES.md`, deliberately different from the preceding B17 trio: **#11 dualize** (turn the spectral support into a code/cocode pair), **#21 ask who else has this shape** (use coding-theoretic k-wise independence), and **#26 hunt the sporadic case** (build and exactly test a seven-variable non-unate quadratic phase before generalizing).

No novelty or publication-priority claim is made. A bounded literature check is recorded in §9.

## 1. The previous obstruction and the new question

For a Boolean function \(f:\{0,1\}^n\to\{\pm1\}\), use normalized Walsh coefficients
\[
\widehat f(a)=2^{-n}\sum_x f(x)(-1)^{a\cdot x},
\qquad
\mu_f(a)=\widehat f(a)^2.
\]
The spectral entropy is \(H(f)=H(\mu_f)\), the coordinate marginals are
\[
p_i=\Pr_{\mu_f}(i\in S)=\operatorname{Inf}_i(f),
\]
and \(I(f)=\sum_i p_i\).

The preceding B17 run exhibited exact one-point defects for which global and even chain-additive *unweighted* Hellinger payment loses the rare-event logarithm. That leaves a natural repair: derive conditional KL on a rare activated history from local Boolean phase constraints.

The present run tests the strongest fixed-order version of that repair:

> Can bounded-order spectral marginals, perhaps evaluated only after a rare phase is activated, certify a constant fraction of the total correlation that Booleanity forces?

The answer is **no**, on an exact source-admissible Boolean family.

## 2. Quadratic phases whose spectral sample is an affine code

Let \(V=\mathbb F_2^n\). A quadratic form \(Q:V\to\mathbb F_2\) has polar form
\[
B(x,z)=Q(x+z)+Q(x)+Q(z),
\]
an alternating bilinear form. Put
\[
R=\operatorname{rad}(B)=\{z:B(x,z)=0\ \forall x\},
\qquad s=\dim R,
\qquad r=n-s.
\]
The rank \(r\) is even.

Set
\[
h_Q(x)=(-1)^{Q(x)}
\]
and write its unnormalized Walsh transform as
\[
W_Q(a)=\sum_{x\in V}(-1)^{Q(x)+a\cdot x}.
\]

### Lemma 2.1 — exact affine-code support

For every \(z\in R\),
\[
W_Q(a)=(-1)^{Q(z)+a\cdot z}W_Q(a).
\]
Hence \(W_Q(a)\ne0\) only if
\[
a\cdot z=Q(z)\qquad\forall z\in R. \tag{2.1}
\]
Because \(B\) vanishes on \(R\), the restriction \(Q|_R\) is linear. Therefore (2.1) describes either the empty set or an affine coset
\[
C=a_0+R^\perp.
\]
It is nonempty because every linear functional on \(R\) extends to \(V\).

For \(a\in C\), \(Q(x)+a\cdot x\) is constant on cosets of \(R\) and descends to a nondegenerate quadratic form on \(V/R\). A symplectic-pair Gauss-sum calculation gives
\[
|W_Q(a)|=2^s\,2^{r/2}=2^{n-r/2}.
\]
Thus the normalized Fourier coefficients satisfy
\[
|\widehat h_Q(a)|=
\begin{cases}
2^{-r/2},&a\in C,\\
0,&a\notin C,
\end{cases} \tag{2.2}
\]
and the spectral sample is **uniform on the affine code \(C\)** of size \(2^r\).

If \(Q|_R\ne0\), then \(0\notin C\), so \(W_Q(0)=0\): \(h_Q\) is balanced.

This is a proof, not a finite inference.

## 3. Coding theory turns local spectral invisibility into an arbitrarily large exact gap

For a linear code \(R\le\mathbb F_2^n\), let
\[
\delta(R)=\min\{|z|:z\in R\setminus\{0\}\}
\]
be its minimum distance. The direction space of \(C\) in §2 is \(R^\perp\), whose dual is \(R\).

### Lemma 3.1 — \(k\)-wise spectral independence

If \(k<\delta(R)\), the uniform law on any affine coset \(a_0+R^\perp\) is \(k\)-wise independent with fair one-bit marginals.

**Proof.** A projection to a coordinate set \(J\) fails to be surjective exactly when some nonzero linear functional supported in \(J\) vanishes on \(R^\perp\), equivalently when \(R\) contains a nonzero codeword supported in \(J\). No such word exists when \(|J|<\delta(R)\). Every fibre of the surjective projection has the same size, so the projected law is uniform. \(\square\)

Since every one-bit marginal is \(1/2\), the matched product law is the uniform law \(U_n\). From (2.2),
\[
H(\mu_{h_Q})=r,
\qquad
\operatorname{TC}(\mu_{h_Q})
=D_2(\mu_{h_Q}\|U_n)
=n-r=s. \tag{3.1}
\]

Thus \(s\) bits of dependence can be present while every marginal of order \(<\delta(R)\) is **exactly indistinguishable** from an independent fair product.

### Theorem 3.2 — bounded-order local payment cannot recover Boolean spectral KL

For every fixed integer \(k\ge1\) and every \(L>0\), there is a balanced Boolean function \(h\) whose spectral sample:

1. is exactly \(k\)-wise independent with fair marginals;
2. has total correlation \(>L\).

**Construction.** Choose an odd \(s\) so large that \(s>L\) and \(2^{s-1}>k\). Let \(R_s\) be the binary simplex code of dimension \(s\) and length
\[
n=2^s-1.
\]
Its coordinates are indexed by nonzero \(u\in\mathbb F_2^s\), and a codeword indexed by \(c\in\mathbb F_2^s\) has entries \(c\cdot u\). Every nonzero codeword has weight exactly
\[
\delta(R_s)=2^{s-1}.
\]
Because \(s\) is odd,
\[
r=n-s=2^s-1-s
\]
is even. Choose an alternating form on \(V/R_s\) that is nondegenerate and pull it back to \(V\); its radical is \(R_s\). Choose a quadratic refinement \(Q\), then add a linear form so that \(Q|_{R_s}\) is a prescribed nonzero linear functional. Lemmas 2.1 and 3.1 apply. The spectral sample is \(k\)-wise independent, while by (3.1)
\[
\operatorname{TC}=s>L.
\]
\(\square\)

### Exact no-go scope

Let \(\Phi_k\) be any statistic determined solely by the complete collection of spectral marginals on coordinate sets of size at most \(k\), and suppose \(\Phi_k(U_n)=0\). There is **no** \(c_k>0\) such that
\[
\Phi_k(\mu_f)\ge c_k\,\operatorname{TC}(\mu_f)
\]
for every Boolean spectral law \(\mu_f\). The functions above have exactly the same \(\le k\)-coordinate marginals as \(U_n\), hence \(\Phi_k=0\), while \(\operatorname{TC}>0\).

This does **not** refute a global signed-phase or growing-block proof. It precisely kills the stronger intermediate claim that a fixed-order local marginal deviation can certify a constant fraction of the KL payment.

## 4. An explicit seven-variable non-read-once witness

The sprint asks account04/B17 for adversarial **non-read-once phase constructions**, so I instantiated the general mechanism before relying on the abstract family.

Take \(n=7\) and let \(R\) be generated by
\[
\begin{aligned}
g_1&=(0,0,0,1,1,1,1),\\
g_2&=(0,1,1,0,0,1,1),\\
g_3&=(1,0,1,0,1,0,1).
\end{aligned}
\]
Every nonzero vector of \(R\) has Hamming weight \(4\).

Define
\[
Q(x)=
x_1x_2+x_1x_5+x_1x_7+
x_2x_6+x_2x_7+
x_3x_4+x_3x_5+x_3x_6+x_3x_7+
x_4x_5+x_4x_6+x_5x_6
\pmod2, \tag{4.1}
\]
and \(h(x)=(-1)^{Q(x)}\).

The exact checker verifies:

- the radical of the polar form of (4.1) is **exactly** \(R\);
- the Walsh support has \(16\) points, every nonzero Walsh coefficient has unnormalized magnitude \(32\), so \(|\widehat h|=1/4\) on the support;
- the support is the affine syndrome class
  \[
  g_1\cdot a=1,\qquad g_2\cdot a=0,\qquad g_3\cdot a=0; \tag{4.2}
  \]
- \(h\) is balanced;
- every 1-, 2-, and 3-coordinate projection of the spectral support is exactly uniform;
- \(H(h)=4\) bits and \(\operatorname{TC}=3\) bits.

The checker also tests unateness exactly. For every input coordinate, among the \(0\to1\) edge differences of \(h\) one finds both \(+2\) and \(-2\) (as well as \(0\)). Hence \(h\) is **not unate**.

Every read-once formula over AND/OR/NOT is unate after pushing negations to its leaves: each variable occurs with one fixed polarity in a monotone AND/OR formula. Therefore this explicit \(h\) is not a read-once AND/OR/NOT function.

This makes the witness genuinely outside the read-once class rather than merely a repackaging of the already certified read-once mechanism.

## 5. Rare-selector lift: the hidden code KL survives on an activated history

The preceding run's obstruction was specifically about **rare histories**, so embed the quadratic phase behind a rare selector.

Let \(x\in\{0,1\}^d\), \(y\in\{0,1\}^n\), let \(h\) be a balanced code-phase function from §2, and set
\[
\varepsilon=2^{-d},
\qquad
F_{d,h}(x,y)=
\begin{cases}
h(y),&x=0^d,\\
1,&x\ne0^d.
\end{cases} \tag{5.1}
\]

Using
\[
1_{\{x=0^d\}}=2^{-d}\sum_{T\subseteq[d]}\chi_T(x),
\]
the Fourier coefficients are exact:
\[
\widehat F(\varnothing,\varnothing)=1-\varepsilon, \tag{5.2}
\]
\[
\widehat F(T,\varnothing)=-\varepsilon
\quad(T\ne\varnothing), \tag{5.3}
\]
and for \(U\ne\varnothing\),
\[
\widehat F(T,U)=\varepsilon\,\widehat h(U)
\quad\text{for every }T. \tag{5.4}
\]

If \(\mu_h\) is uniform on \(C=a_0+R^\perp\) of dimension \(r\), the phase-coordinate block \(Y\) of the spectral sample therefore has law
\[
\Pr(Y=0)=1-\varepsilon,\qquad
\Pr(Y=u)=\varepsilon\,2^{-r}\quad(u\in C). \tag{5.5}
\]

So, **conditioned on the rare event \(A=\{Y\ne0\}\)**,
\[
Y\mid A\sim\operatorname{Unif}(C). \tag{5.6}
\]
All \(|J|<\delta(R)\) conditional marginals are fair and independent, yet
\[
\operatorname{TC}(Y\mid A)=s. \tag{5.7}
\]

The unconditional phase marginals are
\[
\Pr(j\in Y)=\varepsilon/2.
\]
Its phase-block entropy and total correlation are
\[
H(Y)=h_2(\varepsilon)+\varepsilon r, \tag{5.8}
\]
\[
\operatorname{TC}(Y)
=n\,h_2(\varepsilon/2)-h_2(\varepsilon)-\varepsilon r. \tag{5.9}
\]
Using \(r=n-s\),
\[
\boxed{
\operatorname{TC}(Y)
=
\underbrace{n\,h_2(\varepsilon/2)-h_2(\varepsilon)-\varepsilon n}_{\text{activation/marginal term}}
+\underbrace{\varepsilon s}_{\text{hidden code-syndrome term}}.
} \tag{5.10}
\]

The final term is exactly the rare-event probability times the conditional code deficit \(s\). It is invisible to **every** conditional spectral marginal of order \(<\delta(R)\).

This is the new mechanism obstruction: the rare-history KL demanded by the previous B17 run can sit in a global code syndrome while all bounded local faces of the activated spectral law look perfectly product-like.

A successful phase/curl-free route therefore needs at least one of:

1. block order growing with the relevant dual distance;
2. a global code/correlation invariant;
3. a genuinely signed global constraint that is not reducible to bounded-order spectral marginals.

## 6. Entropy and influence of the selector family — boundary check

The full spectral law of \(F_{d,h}\) has:

- one atom of mass \((1-\varepsilon)^2\);
- \(2^d-1\) gate-only atoms of mass \(\varepsilon^2\);
- \(2^d2^r\) phase-layer atoms of mass \(\varepsilon^2 2^{-r}\).

Hence
\[
H(F_{d,h})
=
\phi((1-\varepsilon)^2)
+2d(\varepsilon-\varepsilon^2)
+\varepsilon(2d+r), \tag{6.1}
\]
where \(\phi(t)=t\log_2(1/t)\), i.e.
\[
H(F_{d,h})
=
\phi((1-\varepsilon)^2)
+4d\varepsilon-2d\varepsilon^2+\varepsilon r. \tag{6.2}
\]

Every gate spectral coordinate has marginal \(\varepsilon\). Every phase coordinate has marginal \(\varepsilon/2\). Thus
\[
I(F_{d,h})=\varepsilon\left(d+\frac n2\right). \tag{6.3}
\]

This family is **not an FEI counterexample**. In particular, for fixed phase block and \(d\to\infty\), the leading gate contribution gives a ratio tending to at most the familiar constant \(4\); in the opposite phase-dominated regime the ratio is small. The construction is an obstruction to a *proof mechanism*, not to FEI.

Moreover, if the seed \(h\) is the non-read-once witness from §4, then restricting the gate variables of \(F_{d,h}\) to zero recovers \(h\). Restrictions of a read-once formula are read-once, so \(F_{d,h}\) is also non-read-once.

## 7. Exact finite stress test

`verify_quadratic_code_phase.py` is a standard-library exact checker. It performs integer Walsh transforms and rational marginal calculations.

For the seven-variable phase it verifies the radical, simplex distance, exact affine syndrome, support size, Walsh magnitude, balance, exact 3-wise independence, \(3\) bits of total correlation, and non-unateness.

For the rare selector it uses \(d=4\), hence \(\varepsilon=1/16\), on \(11\) total variables. The exact Walsh histogram is
\[
|W|=1920\ (1\text{ coefficient}),\quad
128\ (15),\quad
32\ (256),\quad
0\ (1776).
\]
Equivalently, the normalized coefficient classes are \(15/16\), \(1/16\), and \(1/64\), exactly as (5.2)–(5.4) predict.

It verifies exactly:
\[
\operatorname{Inf}_{x_i}=1/16,\qquad
\operatorname{Inf}_{y_j}=1/32,\qquad
I(F)=15/32.
\]
Numerically from exact probabilities,
\[
H(F)=1.382418874906901,
\]
and the closed form (6.2) agrees to the displayed precision.

For the phase block,
\[
H(Y)=0.5872900666170139,
\]
\[
\operatorname{TC}(Y)=0.8170662035719888,
\]
with decomposition
\[
0.8170662035719888
=
0.6295662035719888
+
0.1875.
\]
The last number is exactly
\[
\varepsilon s=(1/16)\cdot3=3/16.
\]
Conditioned on activation, the 16-point phase support is exactly the same affine code from §4 and remains 3-wise independent.

Checker SHA-256:
`ad9b2baac61b6a6c4f2b83117700ef6107961b75ee84a2722d1cb6f52c721f23`.

Verification-output SHA-256:
`c9efec39b2fafaf668bf3a78ea6f73d5ef1666626e65cbc20a642029ce8644a5`.

The checker is a self-check of the explicit finite witness. The general statements in §§2–6 are proved algebraically on the page.

## 8. What this changes in the full-FEI attack

The previous B17 report concluded that rare-history payment must preserve a \(\log(q/p)\)-scale likelihood ratio instead of collapsing to unweighted Hellinger distance.

This run adds a second restriction:

> **Rare-history KL cannot, in general, be extracted from any fixed order of conditional spectral marginals.**

Quadratic code phases can make the activated law \(k\)-wise exactly product for arbitrarily large prescribed \(k\), while retaining arbitrarily large conditional total correlation. The missing dependence is a **global syndrome**.

That sharply narrows the phase/curl-free route. A local-to-global argument must either prove that the relevant block order automatically grows at a rate whose cost is paid by influence, or discover a global invariant whose KL contribution is summable. Merely adding more fixed-size faces cannot close FEI.

A concrete next lemma is therefore:

> **Growing-block syndrome payment target.** Given a Boolean spectral sample and a rare activated history, find a block \(J\) whose size is itself charged to influence and for which the block correlation/phase constraint reveals a fixed fraction of the remaining conditional KL. The block size may grow with the local dual distance; a fixed universal order is impossible by Theorem 3.2.

This target is distinct from the account02/B13 block-parity cap: that result supplies valid blockwise caps/KL lower bounds, whereas the present construction identifies why **bounded block size cannot be sufficient** and what scale a block selection theorem has to reach.

## 9. Bounded primary-literature comparison

No novelty claim is made.

- Xiao Han, *A New Bound for the Fourier-Entropy-Influence Conjecture*, Combinatorica 45 (2025), proves an upper bound of the form
  \[
  O\!\left(I+\sum_i I_i\log(1/I_i)\right),
  \]
  consistent with the rare-coordinate logarithm that the previous B17 run found necessary.
- Peijie Li and Guangyue Han, arXiv:2512.03117 (2025), give an information-theoretic strengthening with sharp coefficient normalization in their formulation.
- Vladimir N. Potapov, arXiv:2609.21563 (18 September 2026), proves FEI for Boolean plateaued functions with sharp class constant \(4\), and for partially bent functions with sharp class constant \(2\). The quadratic phases in §§2–4 are plateaued, so this report does **not** present their FEI validity as new; it uses them as exact adversarial examples against a bounded-locality proof mechanism.

The full universal FEI conjecture remains open in the fresh repository state and in the checked current sources.

## 10. Claim ledger

**PROVED in this report**

1. Quadratic Boolean phases with radical \(R\) have spectral sample uniform on an affine coset of \(R^\perp\).
2. If \(\delta(R)>k\), that spectral sample is exactly \(k\)-wise independent.
3. Simplex radicals give, for every fixed \(k\) and \(L\), balanced Boolean functions whose spectral sample is \(k\)-wise independent but has total correlation \(>L\).
4. Therefore bounded-order spectral marginals cannot universally certify a positive constant fraction of Boolean spectral total correlation.
5. The explicit seven-variable quadratic phase (4.1) is balanced, 3-wise spectrally independent, has \(3\) hidden correlation bits, and is non-unate, hence not a read-once AND/OR/NOT formula.
6. The rare-selector formulas (5.2)–(6.3) are exact. Conditional on phase activation, the hidden code total correlation survives while every local marginal below the code distance remains product.
7. The explicit \(d=4\) rare selector passes the exact integer-Walsh checker.

**REFUTED INTERMEDIATE CLAIM**

Any universal FEI closure that requires a fixed-order local spectral-marginal payment to recover a constant fraction of conditional KL is false, even on exact Boolean functions and even on rare activated histories.

**NOT PROVED**

- full FEI;
- that every signed phase/curl-free mechanism is local in this sense;
- a growing-block payment theorem;
- publication novelty or priority.

## 11. Next attack

Use the peer block-parity KL bridge together with the obstruction above, but optimize over **growing blocks** rather than coordinates or fixed-size faces. The precise target is to prove an influence-budgeted block selection lemma: either a small block already exposes enough KL, or large dual distance itself forces enough influence/entropy payment to terminate the recursion.

That is a genuinely new branch from the preceding Hellinger calculation and directly addresses the current sprint's account04/B17 assignment.
