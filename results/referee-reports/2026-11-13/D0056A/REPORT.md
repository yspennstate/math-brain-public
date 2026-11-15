COUNTEREXAMPLE

# The survival constant in the critical Derrida–Retaux recursion

For every integer \(m\ge2\), there are nonconstant critical laws with
\(\mathbb P(X_0\ge2)>0\) for which
\[
 n^2\mathbb P(X_n>0)\not\longrightarrow \frac4{(m-1)^2}.
\]
There is an elementary family for which \(\limsup n^2\mathbb P(X_n>0)=\infty\), even with a finite tilted moment of any prescribed order strictly below two. A second family with regular tilted power tails has a different necessary asymptotic constant, by published product estimates and an elementary comparison lemma. Under a finite third tilted moment, existence of the proposed limit remains unresolved by this report.

## 1. Statements

Write
\[
 q_n=\mathbb P(X_n>0),\qquad G_n(s)=\mathbb E[s^{X_n}],\qquad
 u_n=G_n(m)-1,\qquad
 \Pi_n=\prod_{j=0}^{n-1}G_j(m)^{m-1}.
\]

**Theorem A (elementary sparse-tail counterexamples).** Fix \(1\le\rho<2\), and set
\[
 k_j=2^j,\qquad a_j=\frac1{j^2k_j^\rho},\qquad
 A=\sum_{j\ge1}\big((m-1)k_j-1\big)a_j,\qquad
 T=\sum_{j\ge1}m^{-k_j}a_j,\qquad c=(A+T)^{-1}.
\]
The probability law
\[
 p_0=cA,\qquad p_{k_j}=c m^{-k_j}a_j\quad(j\ge1),\qquad
 p_k=0\quad\text{otherwise}
 \tag{A1}
\]
is nonconstant and critical. Its tilted moment of order \(r>0\) is finite if and only if \(r\le\rho\). For \(n_j=k_j-1\),
\[
 q_{n_j}\ge1-\exp\left(-\frac{c}{m j^2k_j^\rho}\right).
 \tag{A2}
\]
Consequently
\[
 \lim_{j\to\infty}n_j^2q_{n_j}=\infty,
 \qquad
 \limsup_{n\to\infty}n^2q_n=\infty.
 \tag{A3}
\]
For \(\rho=1\), this also rules out the exponent assertion \(q_n=n^{-2+o(1)}\) under bare criticality: along this subsequence,
\[
 q_{n_j}\ge\frac{c+o(1)}{m n_j(\log_2(n_j+1))^2}.
 \tag{A4}
\]
Here \(A=(m-1)\zeta(2)-\operatorname{Li}_2(1/2)\), and the series defining \(T\) converges doubly exponentially. No external asymptotic result is needed for this theorem.

**Theorem 1 (a constraint on survival probabilities).** Suppose that a critical integer-valued Derrida–Retaux system satisfies
\[
 G_n(m)\longrightarrow1,\qquad
 \frac{\log\Pi_n}{\log n}\longrightarrow\beta\in(0,\infty).
 \tag{1}
\]
Then
\[
 \liminf_{n\to\infty}n^2q_n
 \ \le\ \frac{\beta(\beta+2)}{2(m-1)^2}
 \ \le\ \limsup_{n\to\infty}n^2q_n.
 \tag{2}
\]
If \(n^2q_n\) converges, even allowing an extended nonnegative limit, its limit is necessarily
\[
 \frac{\beta(\beta+2)}{2(m-1)^2}.
 \tag{3}
\]

**Theorem 2 (heavy-tail counterexamples).** Let \(2<b<4\). Put
\[
 L_b=\operatorname{Li}_b(1/m)=\sum_{k=1}^{\infty}\frac{m^{-k}}{k^b},
 \quad A_b=(m-1)\zeta(b-1)-\zeta(b),
 \quad c_b=(A_b+L_b)^{-1}.
\]
Define
\[
 \mathbb P(X_0=0)=c_bA_b,\qquad
 \mathbb P(X_0=k)=c_bm^{-k}k^{-b}\quad(k\ge1).
 \tag{4}
\]
This is a nonconstant critical probability distribution, and
\[
 \liminf_{n\to\infty}n^2q_n
 \ \le\ \frac{b(b-2)}{2(m-1)^2}
 \ \le\ \limsup_{n\to\infty}n^2q_n.
 \tag{5}
\]
Consequently it is a counterexample to the assertion that bare criticality implies \(n^2q_n\to4/(m-1)^2\). If its scaled survival probability has a limit, that limit must instead be \(b(b-2)/(2(m-1)^2)\).

In fact, no fixed tilted moment order strictly below three suffices to guarantee the original constant: given \(0<r<3\), choose \(\max(2,r+1)<b<4\) in (4). That law has finite \(r\)-th tilted moment and still contradicts the proposed limit.

For example, take \(b=3\). Then
\[
 c=\left((m-1)\zeta(2)-\zeta(3)+\operatorname{Li}_3(1/m)\right)^{-1},
 \qquad
 p_0=c((m-1)\zeta(2)-\zeta(3)),\quad p_k=c m^{-k}k^{-3}.
 \tag{6}
\]
For this law the liminf in (5) is at most \(3/2\) when \(m=2\), and at most \(3/8\) when \(m=3\). These are strictly below the conjectured constants \(4\) and \(1\), respectively.

**Corollary 3 (finite third tilted moment).** For a nonconstant critical law satisfying \(\mathbb E[X_0^3m^{X_0}]<\infty\),
\[
 \liminf n^2q_n\le\frac4{(m-1)^2}\le\limsup n^2q_n.
 \tag{7}
\]
If \(n^2q_n\) has a limit, it equals \(4/(m-1)^2\). The corollary does not prove existence of that limit or rule out oscillation.

## 2. Literature and the scope of the remaining conjecture

The primary papers were downloaded to `literature/`; searchable extracted texts accompany the PDFs. For Collet et al., the complete October 1983 CERN preprint is available in the [Numdam proceedings scan](https://www.numdam.org/item/RCP25_1983__33__117_0/), saved as `collet_et_al_french.pdf`; the paper itself is in English. Its Appendix III, equations (AIII.9)–(AIII.16), explicitly assumes a smooth asymptotic expansion before deriving the survival prediction. Appendix IV discusses exceptional tilted tails. The published journal metadata were checked separately. The following statements distinguish the deterministic offspring recursion in this problem from related models. The search was checked through 13 November 2026.

| Source | Precise relevant result | Consequence for this question |
|---|---|---|
| [Chen–Hu–Shi, *The sustainability probability for the critical Derrida–Retaux model*](https://arxiv.org/abs/2108.05610), PTRF **182** (2022), 641–684 | Theorem 1.2 assumes \(\mathbb E[t^{X_0}]<\infty\) for some \(t>m\), and proves \(q_n=n^{-2+o(1)}\), as well as the same exponent for \(\mathbb E X_n\). Proposition 4.1 gives an upper bound of order \((\log n)^2/n^2\) under the fifth tilted moment; Proposition 5.1 gives a lower bound \(c/[n^2(\log n)^\nu]\) under the exponential moment. | Neither a third tilted moment alone nor a survival asymptotic constant is its main theorem. |
| [Chen–Shi, *The stable Derrida–Retaux system at criticality*](https://arxiv.org/abs/2006.06140), in *In and Out of Equilibrium 3* (2021), 239–264 | Theorem 1.1: if \(p_k\sim c_0m^{-k}k^{-b}\), \(2<b<4\), then \(c_1n^{b-2}\le\Pi_n\le c_2n^{b-2}\). | This is the published input for Theorem 2. It is a theorem about a product, not a theorem asserting the stable survival limit. |
| [Chen–Derrida–Hu–Lifshits–Shi, *A max-type recursive model: some properties and open questions*](https://arxiv.org/abs/1705.04787), 2019 chapter, 166–186 | Theorem 2 gives \(G_n(m)\to1\) for nonconstant critical laws. Propositions 1 and 2 give \(\Pi_n\asymp n^2\) under a finite third tilted moment. | These imply (1) with \(\beta=2\), and supply the other published input for Theorem 2. |
| [Chen–Dagard–Derrida–Hu–Lifshits–Shi, *The Derrida–Retaux conjecture on recursive models*](https://arxiv.org/abs/1907.01601), Ann. Probab. **49** (2021), 637–670 | Theorem 1.1 proves the free-energy essential-singularity exponent \(1/2\) under the third tilted moment; Theorem 1.2 gives exponent \(1/(b-2)\) for tilted power tails, \(2<b\le4\). | These are near-critical free-energy results, not a critical survival constant. |
| [Derrida–Shi, *Results and conjectures on a toy model of depinning*](https://arxiv.org/abs/2005.10208), Moscow Math. J. **20** (2020), 695–709 | Section 2.1, equations (13)–(14), predicts \(4\) under a finite third tilted moment and \(b(b-2)/2\) for binary tilted power tails. | The altered heavy-tail survival constant was already predicted. Theorem 2 rigorously excludes the original constant without proving this prediction in full. |
| [Hu–Shi, *The free energy in the Derrida–Retaux recursive model*](https://arxiv.org/abs/1705.03792), J. Stat. Phys. **172** (2018), 718–741 | Studies free energy, including a random offspring generalization and dependence on the initial tail. | Does not prove the survival constant in the stated deterministic offspring problem. |
| [Collet–Eckmann–Glaser–Martin, *Study of the iterations of a mapping associated to a spin glass model*](https://doi.org/10.1007/BF01224830), Comm. Math. Phys. **94** (1984), 353–370; [Derrida–Retaux (2014)](https://arxiv.org/abs/1401.6919), J. Stat. Phys. **156**, 268–290 | Foundational criticality and asymptotic predictions. | The universal constant under the question's bare hypothesis cannot hold, by Theorem 2. |
| [Aldous–Contat–Curien–Hénard, *Parking on the infinite binary tree*](https://arxiv.org/abs/2205.15932), PTRF **187** (2023), 481–504 | Theorems 1–2 characterize parking phases and compute critical quantities. Its equation (2) is \(X\stackrel d=(X_1-1)^++(X_2-1)^++A\), with arrivals at internal vertices. | This recursion differs from leaf-only DR iteration. The critical parking formulas do not transfer the survival constant. |
| [Curien–Hénard, *The phase transition for parking on Galton–Watson trees*](https://arxiv.org/abs/1912.06012), Discrete Analysis (2022), paper 1; [Chen–Contat, *Parking on supercritical geometric Bienaymé–Galton–Watson trees*](https://arxiv.org/abs/2402.05612), ALEA **22** (2025), 1287–1299 | Phase criteria for arrivals at every vertex on, respectively, critical conditioned trees and supercritical geometric trees. | Their offspring and arrival settings differ from deterministic leaf-only DR iteration. Neither gives its critical survival constant. |
| [Chen–Hu–Shi, *The dual Derrida–Retaux conjecture*](https://arxiv.org/abs/2306.12717), SPA **171** (2024), 104332; [Chen, *Infinite differentiability of the free energy for a Derrida–Retaux system*](https://arxiv.org/abs/2405.09741) | Respectively near-subcritical decay and smoothness of free energy. | Neither establishes the deterministic critical survival constant. |
| [Li–Zhang, *Asymptotic behavior of the generalized Derrida–Retaux recursive model*](https://arxiv.org/abs/2411.13068), J. Stat. Phys. **192** (2025), 98, corrected v3 dated 18 August 2025 | Theorem 1.3(3), Corollary 1.5(3) prove \(q_n\sim2/((m-1)^2n^2)\), with logarithmic corrections, for **geometric offspring** and geometric-type initial laws. | This is a proved constant for a different model. It does not establish \(4/(m-1)^2\) for deterministic offspring. |
| [Alsmeyer–Hu–Mallein, *The Derrida–Retaux model on a geometric Galton–Watson tree*](https://arxiv.org/abs/2502.02991), v2 dated 9 April 2026 | Exact critical curves and free-energy asymptotics for geometric offspring models. | Again a different offspring law. |
| [Duquesne–Shi, *The continuous Derrida–Retaux branching process in the Brownian CRT*](https://arxiv.org/abs/2609.11435), September 2026 | Studies the candidate continuous branching limit; its introduction explicitly retains discrete-to-continuous convergence as conjectural. | Does not close the discrete critical asymptotic problem. |

No primary paper located in this search proves the survival limit \(4/(m-1)^2\) for the nondegenerate deterministic offspring recursion under a moment hypothesis. This is a statement about the literature located, rather than a claim of exhaustive bibliographic impossibility.

The conjecture requires a nondegeneracy condition even before considering tails: for \(m=2\), the law \(X_0\equiv1\) satisfies the displayed critical equality and remains identically one. Theorem 2 avoids that exception and has positive mass at every positive integer and at zero.

## 3. Proofs

### 3.1 Proof of Theorem A

Since \(k_j\ge2\), all terms defining \(A\) are positive. Also,
\[
 0<A\le(m-1)\sum_{j\ge1}j^{-2}<\infty,
 \qquad 0<T<\infty.
\]
Thus (A1) defines positive masses at zero and at every \(k_j\), summing to one. Direct summation gives
\[
 \mathbb E[m^{X_0}]=c\left(A+\sum_j a_j\right)
   =c(m-1)\sum_j k_ja_j,
 \qquad
 \mathbb E[X_0m^{X_0}]=c\sum_j k_ja_j<\infty.
\]
This proves criticality. For \(r>0\),
\[
 \mathbb E[X_0^rm^{X_0}]
 =c\sum_{j\ge1}\frac{2^{j(r-\rho)}}{j^2},
\]
which converges exactly for \(r\le\rho\). Every ordinary polynomial moment is finite. Also \(\mathbb E[t^{X_0}]<\infty\) for \(0<t\le m\), whereas for any \(t>m\) the positive summands fail to tend to zero, so that expectation is infinite.

Realize the recursion on the complete depth-\(n\) \(m\)-ary tree, with independent copies of \(X_0\) at its leaves. If one leaf has value \(k\), then the value at its ancestor \(h\) edges above is at least \((k-h)^+\). This follows by induction: the other children are nonnegative, and at most one unit is subtracted at each edge. In particular, a leaf with value \(k_j\) guarantees a positive root at depth \(n_j=k_j-1\).

There are \(m^{n_j}\) independent leaves. Therefore
\[
 q_{n_j}\ge1-(1-p_{k_j})^{m^{n_j}}
 \ge1-\exp(-m^{n_j}p_{k_j})
 =1-\exp\left(-\frac{c}{m j^2k_j^\rho}\right),
\]
proving (A2). The exponential argument tends to zero. Hence
\[
 n_j^2q_{n_j}\ge(1+o(1))\frac{c}{m}
       \frac{(k_j-1)^2}{j^2k_j^\rho}
 \longrightarrow\infty
\]
because \(2-\rho>0\) and \(k_j=2^j\). This proves (A3). Setting \(\rho=1\) yields (A4); its logarithm along \(n_j\) is bounded below by \(-\log n_j-O(\log\log n_j)\), which is incompatible with \(q_n=n^{-2+o(1)}\). The stated formula for \(A\) follows by summing \(\sum j^{-2}\) and \(\sum 2^{-j}j^{-2}\). \(\square\)

### 3.2 Exact generating-function identities

For \(s>0\) where the expectations are finite, conditioning on the sum of the independent copies gives
\[
 G_{n+1}(s)=\frac{G_n(s)^m}{s}
       +\left(1-\frac1s\right)G_n(0)^m.
 \tag{8}
\]
Indeed, \(s^{(r-1)^+}=s^{r-1}\) for positive integers \(r\), while the term at \(r=0\) requires adding \(1-s^{-1}\).
Differentiation and evaluation at \(m\) give
\[
 (m-1)mG'_{n+1}(m)-G_{n+1}(m)
 =\big((m-1)mG'_n(m)-G_n(m)\big)G_n(m)^{m-1}.
 \tag{9}
\]
Differentiation at the endpoint follows by monotone convergence from the left. Finiteness propagates by the recursion and its differentiated identity. Thus criticality propagates to every generation.

Set
\[
 H(x)=\frac{(1+x)^m-1}{m},\qquad
 d_n=\frac{m-1}{m}\big(1-(1-q_n)^m\big).
\]
Equation (8) at \(s=m\) is exactly
\[
 u_{n+1}=H(u_n)-d_n.
 \tag{10}
\]
For \(x\ge0\), \(H'(x)=(1+x)^{m-1}\ge1\), and
\[
 H(x)=x+\frac{m-1}{2}x^2+O(x^3).
 \tag{11}
\]
When \(q_n\to0\),
\[
 d_n=(m-1)q_n(1+O(q_n)).
 \tag{12}
\]

### 3.3 A comparison lemma

**Lemma 4.** Let \(u_n\ge0\) tend to zero and satisfy (10). Let \(a=(m-1)/2\). For a fixed \(A>0\), the following assertions hold:

1. If \(\limsup n^2d_n<A+aA^2\), then \(u_n<A/n\) for all sufficiently large \(n\).
2. If \(\liminf n^2d_n>A+aA^2\), then \(u_n>A/n\) for all sufficiently large \(n\).

*Proof.* Put \(w_n=A/n\). From (11),
\[
 H(w_n)-w_{n+1}
   =\frac{A+aA^2}{n^2}+O(n^{-3}).
 \tag{13}
\]
Under the first hypothesis, some \(\eta>0\) and \(N\) satisfy
\[
 R_n:=H(w_n)-d_n-w_{n+1}\ge\eta/n^2\qquad(n\ge N).
\]
If \(u_j\ge w_j\) for one \(j\ge N\), monotonicity and \(H'\ge1\) imply
\[
 u_{j+1}-w_{j+1}
 =H(u_j)-H(w_j)+R_j\ge\eta/j^2.
\]
Inductively \(u_k-w_k\ge\eta/j^2\) for every \(k>j\). This contradicts \(u_k\to0\) and \(w_k\to0\). Hence no such \(j\) exists.

Under the second hypothesis, choose \(\eta,N\) so that \(R_n\le-\eta/n^2\). If \(u_j\le w_j\), then
\[
 w_{j+1}-u_{j+1}=H(w_j)-H(u_j)-R_j\ge\eta/j^2,
\]
and the same induction contradicts convergence of both sequences to zero. This proves the second assertion. \(\square\)

In particular, if \(n^2q_n\to C\in(0,\infty)\), Lemma 4 and (12), with barriers on each side of the positive root, give
\[
 nu_n\longrightarrow A(C),\qquad
 A(C)=\frac{\sqrt{1+2(m-1)^2C}-1}{m-1}.
 \tag{14}
\]
No conclusion about \(u_n-u_{n+1}\) was obtained by differentiating an asymptotic equivalence; (14) follows from the exact recurrence.

### 3.4 Proof of Theorem 1

Define
\[
 C_\beta=\frac{\beta(\beta+2)}{2(m-1)^2},\qquad
 A_\beta=\frac\beta{m-1}.
\]
Then \(A_\beta+aA_\beta^2=(m-1)C_\beta\).
Also, \(q_n\le u_n/(m-1)\), since \(m^k-1\ge m-1\) for \(k\ge1\). Therefore \(q_n\to0\).

Suppose first that \(\liminf n^2q_n>C_\beta\). Choose \(c>C_\beta\) strictly below that liminf, and then choose \(A>A_\beta\) sufficiently close to \(A_\beta\) that
\[
 A+aA^2<(m-1)c.
\]
By (12), \(\liminf n^2d_n\ge(m-1)c\). Lemma 4 yields \(u_n>A/n\) eventually. Hence
\[
 \log\Pi_n=(m-1)\sum_{j<n}\log(1+u_j)
 \ge(m-1)\sum_{N\le j<n}\log(1+A/j).
\]
The sum on the right is \(A\log n+O(1)\), so
\(\liminf\log\Pi_n/\log n\ge(m-1)A>\beta\), contradicting (1).

Suppose next that \(\limsup n^2q_n<C_\beta\). Choose \(c\) strictly between this limsup and \(C_\beta\), and choose \(A\in(0,A_\beta)\) sufficiently close to \(A_\beta\) that
\[
 (m-1)c<A+aA^2.
\]
By (12), \(\limsup n^2d_n\le(m-1)c\). Lemma 4 gives \(u_n<A/n\) eventually. The corresponding upper bound on the logarithmic sum gives
\(\limsup\log\Pi_n/\log n\le(m-1)A<\beta\), another contradiction. This proves (2).

For a convergent nonnegative sequence \(n^2q_n\), the two inequalities in (2) force its limit to equal \(C_\beta\). Since \(0<C_\beta<\infty\), the extended limits zero and infinity are also excluded. \(\square\)

### 3.5 Proof of Theorem 2

Absolute convergence holds because \(b>2\). Furthermore,
\[
 A_b=\sum_{k\ge1}\big((m-1)k-1\big)k^{-b}>0.
\]
Every summand is nonnegative, and a summand with \(k\ge2\) is positive. Thus all masses in (4) are positive and
\[
 p_0+\sum_{k\ge1}p_k=c_b(A_b+L_b)=1.
\]
Moreover,
\[
 \mathbb E[m^{X_0}]=c_b(A_b+\zeta(b))
       =c_b(m-1)\zeta(b-1),
 \qquad
 \mathbb E[X_0m^{X_0}]=c_b\zeta(b-1).
 \tag{15}
\]
These identities prove the required finite critical equality. For any real \(r\ge0\), the positive part of the \(r\)-th tilted moment is
\[
 \sum_{k\ge1}k^rm^kp_k=c_b\sum_{k\ge1}k^{r-b},
\]
which is finite precisely when \(r<b-1\). In particular the third tilted moment is infinite.

Theorem 2 of [Chen–Derrida–Hu–Lifshits–Shi](https://arxiv.org/abs/1705.04787) applies to this nonconstant critical law and gives \(G_n(m)\to1\). Theorem 1.1 of [Chen–Shi](https://arxiv.org/abs/2006.06140) applies because \(p_k=c_bm^{-k}k^{-b}\), and gives constants \(0<c_1\le c_2<\infty\) with
\[
 c_1 n^{b-2}\le\Pi_n\le c_2 n^{b-2}.
\]
Consequently (1) holds with \(\beta=b-2\), and Theorem 1 gives (5).

Finally, \(b(b-2)<8\) for \(2<b<4\). Thus (5) is incompatible with convergence to \(4/(m-1)^2\). The specific values in (6) follow by setting \(b=3\). \(\square\)

The only external estimates used here are the two published results just stated. No survival-limit conjecture is used as an input.

### 3.6 Proof of Corollary 3

The same Theorem 2 supplies \(G_n(m)\to1\). Propositions 1 and 2 of the 2019 chapter imply \(\Pi_n\asymp n^2\) when the third tilted moment is finite. Their product includes one additional bounded factor if indexed through \(n\) instead of \(n-1\); this does not affect its logarithmic exponent. Apply Theorem 1 with \(\beta=2\). \(\square\)

## 4. Numerical method and error analysis

### 4.1 Laws and iteration

All numerical runs use deterministic offspring, \(m=2\) or \(m=3\). The two-point laws have
\[
 p_k=\frac1{1+((m-1)k-1)m^k},\qquad p_0=1-p_k,
 \quad k\in\{2,5\}.
\]
The geometric-type law has \(p_j=c r^j\), \(j\ge1\), with \(r=1/(2m)\). If \(t=mr=1/2\), set
\[
 A=(m-1)\frac{t}{(1-t)^2}-\frac{t}{1-t},\qquad
 c=\left(A+\frac r{1-r}\right)^{-1},\qquad p_0=cA.
\]
The sparse-tail law is (A1) with \(\rho=1\). The power-tail laws are (4), with \(b=2.5,3,3.5,4\). The endpoint \(b=4\) is included numerically; Theorem 2 is asserted only for \(2<b<4\).

`code/iterate.py` evolves \(a_j=m^jp_j\), \(1\le j\le K\), with \(a_0=0\). Write \(A(z)=\sum_{j\ge1}a_jz^j\). The update for positive coefficients is
\[
 a^{\rm new}_k=\frac1m[z^{k+1}](p_0+A(z))^m,\qquad k\ge1.
\]
The linear contribution is \(p_0^{m-1}a_{k+1}\). For \(m=2\), the nonlinear part is \(A^2/2\); for \(m=3\), it is \((3p_0A^2+A^3)/3\). These small nonlinear polynomials are convolved by FFT, avoiding subtraction of a unit-sized constant. FFT length is at least \(mK+1\), so circular aliasing is absent in exact arithmetic. Positive mass above \(K\) is transferred to zero, and
\[
 q=\sum_{j=1}^K a_jm^{-j},\qquad p_0=1-q.
\]
There is no adjustment to enforce criticality during iteration.

Initialization uses 70 decimal digits for the zeta, polylogarithm, and tuning constants, followed by conversion to binary64. The implementation is single-threaded and runs at nice priority at least 10. Output metadata records actual peak resident memory, FFT size, time, and cutoff. The requested 4 GB memory ceiling is respected.

### 4.2 A rigorous truncation bound

**Proposition 5.** For any critical law, put \(B=m^{1/(m-1)}\). Define a finite-support iteration by replacing \(X_0>K\) by zero initially, and replacing every subsequent output exceeding \(K\) by zero. Let its survival probability be \(q_n^{[K]}\). Then
\[
 0\le q_n-q_n^{[K]}
 \le Bm^{-(K+1)}\sum_{j=0}^n m^{n-j}
 =Bm^{-(K+1)}\frac{m^{n+1}-1}{m-1}.
 \tag{16}
\]

*Proof.* Criticality propagates by (9). Under the probability law
\(Q_n(k)=m^k\mathbb P(X_n=k)/G_n(m)\), it gives
\(\mathbb E_{Q_n}X_n=1/(m-1)\). Jensen's inequality therefore gives
\[
 \frac1{G_n(m)}=\mathbb E_{Q_n}[m^{-X_n}]
 \ge m^{-1/(m-1)}.
\]
Thus \(G_n(m)\le B\) and
\(\mathbb P(X_n>K)\le Bm^{-(K+1)}\).

Couple the original and truncated systems on the same depth-\(n\) tree. The recursion before truncation is nondecreasing, and deleting a value never increases it. Induction therefore couples every truncated value below its original, untruncated value. (Deletion at a threshold is itself not a nondecreasing map.) If the root values differ, there must have been a truncation at some vertex, including a leaf. A vertex whose original subtree has height \(j\) has original value distributed as \(X_j\). There are \(m^{n-j}\) such vertices. A union bound over all heights yields (16), without requiring independence among these events. Monotonicity gives its lower bound. \(\square\)

For \(K=N+128\) and \(n\le N\), (16) is below \(5.88\times10^{-39}\) for \(m=2\), and below \(7.35\times10^{-62}\) for \(m=3\). Multiply these bounds by \(N^2\) to bound the error in the tabulated scaled probability.

The code evaluates the survival sum only through index 1070. For \(m\ge2\) this leaves a further error at most \(Bm^{-1071}\) for the exact truncated law. This is negligible beside (16).

The proposition bounds support truncation in exact arithmetic. It does **not** certify floating-point rounding. Small negative FFT outputs are clipped and their total tilted mass is logged. Cutoff and implementation comparisons, reported below, assess rounding empirically; fitted digits are not rigorous intervals. The truncated tilted moments and products in the CSV files are diagnostics for the truncated process, and must not be substituted for the true \(G_n(m)\) or \(\Pi_n\).

### 4.3 Certified fixed-point computation

Representative two-point, geometric-type, and heavy-tail runs are independently recomputed by `code/certified.py`. Set \(S=2^{112}\), and represent each positive probability by
\[
 p_k=\frac{a_k}{S m^k},\qquad a_k\in\mathbb Z_+.
\]
Exact rational arithmetic certifies the two-point and geometric initial coefficients; Arb balls at 240-bit precision certify the power-tail initial coefficients. The exact identity
\[
 \left\lceil S\sum_{k=1}^Kp_k\right\rceil
 =\left\lceil\frac{a_1+\left\lceil(a_2+\cdots)/m\right\rceil}{m}\right\rceil
\]
computes an integer \(v\) by nesting ceilings from the largest index downwards. The zero coefficient used in convolution is \(S-v\), the exact downward rounding of \(Sp_0\). The polynomial with these integer coefficients is raised to the \(m\)-th power by GMP integer multiplication after packing coefficients into blocks of \(128m\) bits. The code checks that the sum of all powered coefficients fits in one block, which excludes carries between blocks. The new coefficient is the exact integer floor of the convolution coefficient divided by \(mS^{m-1}\). Thus the arithmetic of each convolution is exact; only specified downward quantization occurs.

Here is a rigorous error bound for that quantization. For probability laws on \(\mathbb Z_+\), let
\[
 D(\mu,\nu)=\inf\mathbb E|m^X-m^Y|,
\]
where the infimum is over couplings. Write \(F\) for one untruncated DR update and \(T_K\) for deletion of values larger than \(K\).

**Lemma 6.** If \(M=\max(\mathbb E_\mu m^X,\mathbb E_\nu m^Y)\), then
\[
 D(F\mu,F\nu)\le M^{m-1}D(\mu,\nu),\qquad
 D(T_K\mu,T_K\nu)\le D(\mu,\nu).
 \tag{17}
\]
Moreover \(|\mu((0,\infty))-\nu((0,\infty))|\le D(\mu,\nu)/(m-1)\).

*Proof.* For nonnegative integers \(r,s\),
\[
 |m^{(r-1)^+}-m^{(s-1)^+}|\le m^{-1}|m^r-m^s|.
\]
Couple \(m\) independent input pairs using a coupling whose cost is arbitrarily close to \(D\). Telescope the difference of their products \(\prod_i m^{X_i}-\prod_i m^{Y_i}\). Independence of pairs bounds the expected absolute difference by \(mM^{m-1}D\). The displayed inequality cancels the factor \(m\), proving the first claim.

For deletion, it suffices to check \(|m^{T_K(r)}-m^{T_K(s)}|\le|m^r-m^s|\). The only nontrivial case is \(r\le K<s\), when the left side is \(m^r-1\), and the right side is at least \((m-1)m^r\). The latter is larger because \(m\ge2\). Applying the same coupling proves the second claim. Finally, a coupling on which exactly one variable is zero incurs cost at least \(m-1\), proving the survival bound. \(\square\)

Let \(E_n\) bound \(D\) between the exact deleted-tail law and the fixed-point law, and let \(M_n^+\) be any upper bound on the latter's tilted moment. Both numerical laws are stochastically bounded by the original untruncated critical law: each deletion or quantization only decreases its pre-deletion law. Hence their tilted moments are at most \(B\), although they need not be ordered relative to one another. Replacing \(p_0\) by its downward rounding changes the weighted positive mass by at most \(B^{m-1}/S=m/S\); flooring the \(K\) output coefficients adds at most \(K/S\). The triangle inequality and (17) give
\[
 E_{n+1}\le(M_n^++E_n)^{m-1}E_n+\frac{K+m}{S}.
 \tag{18}
\]
An initial bound is \(E_0\le J/S\), where \(J\) counts the nonzero initial coefficients being rounded. The code uses the exact rational upper bound \(M_n^+=1+\sum_k a_k/S\), and rounds the right side of (18) upwards on a \(2^{-192}\) grid using integer arithmetic. Thus this error computation itself has directed rounding. The rational columns in `cert_*.csv` enclose the exact deleted-tail survival probability; adding (16) encloses the original survival probability. For a fully rational support bound one may replace \(B\) by \(m\) in (16).

The independent checks in `code/validate.py` compare all six generations of two small-support examples, for both offspring counts, with direct `fractions.Fraction` convolutions. Every exact rational survival probability is enclosed. Another 200 rational examples check the nested ceiling identity. Independent 80-digit mpmath evaluations also check the Arb initialization, and all 24 sparse-law checkpoints are compared with the one-large-leaf lower bound. Results are saved in `data/validation.json` and `data/sparse_leaf_bounds.csv`.

## 5. Numerical results

Numerical tables and fit diagnostics below are generated from the saved CSV files. The probability enclosures are finite-time certificates; fitted limits are experimental evidence, independent of the proofs in Section 3. The figures are saved as [regular-tail comparisons](data/survival.pdf) and [sparse-tail spikes](data/sparse.pdf), with PNG versions alongside. The horizontal dotted lines in the sparse-tail figure mark the proposed constants 4 and 1.

<!-- BEGIN GENERATED RESULTS -->
### 5.0 Sparse tails: the elementary counterexample

The law in Theorem A with rho=1 has isolated survival spikes. The table includes the depths n_j=2^j−1 where the direct leaf lower bound applies. C denotes certified fixed-point output; F denotes FFT output. A constant-plus-logarithmic fit is inappropriate for this oscillatory sequence.

| m | n | n² q_n | arithmetic |
|---:|---:|---:|:---:|
| 2 | 511 | 2.667980224 | C |
| 2 | 1023 | 4.308248857 | C |
| 2 | 2047 | 7.110769387 | C |
| 2 | 4095 | 11.942054970 | C |
| 2 | 8191 | 20.344564824 | C |
| 2 | 10000 | 0.055798605 | C |
| 3 | 511 | 0.765917608 | C |
| 3 | 1023 | 1.237578362 | C |
| 3 | 2047 | 2.043243178 | C |
| 3 | 4095 | 3.431990998 | C |
| 3 | 8191 | 5.847179077 | C |
| 3 | 10000 | 0.013950630 | C |

At n=10,000 the scaled probabilities are small again. The subsequence spikes, rather than a single large endpoint value, exhibit the failure of the proposed limit. The proof of divergence in Theorem A is independent of these computations.

### 5.1 Values through 10,000 generations

`F` denotes binary64 FFT output with the rigorous support bound (16) but no rounding certificate. `C` denotes the independently certified fixed-point computation. The six-decimal display is a numerical value; certified rational endpoints are provided separately below.

| m | initial law | arithmetic | n=1,000 | n=5,000 | n=10,000 | proposed limit |
|---:|---|:---:|---:|---:|---:|---:|
| 2 | {0,2} | C | 4.052334 | 4.014276 | 4.007964 | 4.000000 |
| 2 | {0,5} | F | 4.021418 | 4.008145 | 4.004908 | 4.000000 |
| 2 | geometric | C | 4.025802 | 4.009018 | 4.005339 | 4.000000 |
| 2 | b=2.5 | F | 0.624781 | 0.625064 | 0.625056 | 0.625000 |
| 2 | b=3 | C | 1.500942 | 1.500487 | 1.500308 | 1.500000 |
| 2 | b=3.5 | F | 2.576227 | 2.599542 | 2.606160 | 2.625000 |
| 2 | b=4 | F | 3.532456 | 3.610671 | 3.639723 | 4.000000 |
| 3 | {0,2} | C | 1.006166 | 1.001875 | 1.001076 | 1.000000 |
| 3 | {0,5} | F | 1.000455 | 1.000735 | 1.000507 | 1.000000 |
| 3 | geometric | C | 1.001350 | 1.000914 | 1.000596 | 1.000000 |
| 3 | b=2.5 | F | 0.156342 | 0.156297 | 0.156280 | 0.156250 |
| 3 | b=3 | C | 0.376433 | 0.375484 | 0.375288 | 0.375000 |
| 3 | b=3.5 | F | 0.653268 | 0.654622 | 0.655013 | 0.656250 |
| 3 | b=4 | F | 0.902998 | 0.917571 | 0.922960 | 1.000000 |

The stable tail changes the observed prefactor. At b=3 the values are close to 1.5 for m=2 and 0.375 for m=3, far from 4 and 1. At b=3.5 the approach to 2.625/(m-1)^2 is slower. At b=4 it is slower still; these finite times do not identify its leading correction.

### 5.2 Certified endpoint intervals

Intervals below include quantization and the rational support bound obtained by using B=m in (16). Endpoints are rounded outwards to twelve decimal places.

| m | law | n | certified enclosure for n² q_n | rounding bound for q_n |
|---:|---|---:|---|---:|
| 2 | {0,2} | 10000 | [4.007963710799, 4.007963710800] | 2.66e-22 |
| 2 | geometric | 10000 | [4.005338853429, 4.005338853430] | 1.13e-22 |
| 2 | b=3 | 10000 | [1.500307923414, 1.500307923415] | 1.82e-25 |
| 2 | sparse (rho=1) | 10000 | [0.055798605399, 0.055798605400] | 2.13e-26 |
| 3 | {0,2} | 10000 | [1.001075562821, 1.001075562822] | 6.86e-23 |
| 3 | geometric | 10000 | [1.000595589825, 1.000595589826] | 4.13e-23 |
| 3 | b=3 | 10000 | [0.375288497543, 0.375288497544] | 8.6e-26 |
| 3 | sparse (rho=1) | 10000 | [0.013950630440, 0.013950630441] | 1.07e-26 |

### 5.3 Fits and sensitivity

Least-squares fits use the requested model C+C1/n+C2 log(n)/n, with all coefficients free. They are extrapolations of finite-time values, not proofs or statistical confidence intervals. All coefficients, conditioning diagnostics, residuals, arithmetic sources, and fit windows are in `data/fits.csv`.

| m | law | C, n≥1,000 | C, n≥3,000 | C, n≥5,000 |
|---:|---|---:|---:|---:|
| 2 | {0,2} | 4.00002127 | 4.00001070 | 4.00000746 |
| 2 | {0,5} | 4.00000210 | 4.00002043 | 4.00004216 |
| 2 | geometric | 3.99999591 | 4.00000019 | 4.00000063 |
| 2 | b=2.5 | 0.62500058 | 0.62500016 | 0.62500009 |
| 2 | b=3 | 1.50000108 | 1.50000032 | 1.50000019 |
| 2 | b=3.5 | 2.61553612 | 2.61765209 | 2.61849761 |
| 2 | b=4 | 3.68078581 | 3.69608338 | 3.70308354 |
| 3 | {0,2} | 1.00000040 | 1.00000042 | 1.00000033 |
| 3 | {0,5} | 1.00000153 | 1.00000422 | 1.00000860 |
| 3 | geometric | 0.99999967 | 0.99999983 | 0.99999990 |
| 3 | b=2.5 | 0.15625005 | 0.15625001 | 0.15625001 |
| 3 | b=3 | 0.37501593 | 0.37500927 | 0.37500720 |
| 3 | b=3.5 | 0.65555378 | 0.65570932 | 0.65577091 |
| 3 | b=4 | 0.93051425 | 0.93345242 | 0.93481570 |

A fractional correction is materially better for b=3.5. Over n=3,000–10,000, fitting C+a/sqrt(n)+b/n gives the following intercepts; for b=4 a logarithmic alternative is also displayed.

| m | law | alternative model | C | RMS residual |
|---:|---|---|---:|---:|
| 2 | b=3.5 | C+a/sqrt(n)+b/n | 2.62418521 | 2.23e-06 |
| 2 | b=4 | C+a/log(n)+b/log(n)^2 | 4.12495467 | 8.54e-06 |
| 3 | b=3.5 | C+a/sqrt(n)+b/n | 0.65611998 | 3.47e-07 |
| 3 | b=4 | C+a/log(n)+b/log(n)^2 | 1.01552090 | 5.64e-07 |

The varying extrapolations at b=3.5 and b=4 demonstrate why a fixed 1/n and log(n)/n basis should not be interpreted as universal. Binary64 finite-moment fits also inherit the rounding drift measured below.

### 5.4 Floating-point checks and long runs

Changing K from 10,128 to 20,128 gives the following changes in n²q at n=10,000. Both cutoffs have negligible support error, so these discrepancies measure numerical sensitivity rather than support bias.

| m | law | FFT at K=10,128 minus FFT at K=20,128 | FFT at K=10,128 minus certified value |
|---:|---|---:|---:|
| 2 | {0,2} | 3.6398e-05 | 0.00011976 |
| 2 | b=3 | -9.1834e-09 | -7.2812e-09 |
| 3 | {0,2} | 3.9266e-06 | 1.6999e-05 |
| 3 | b=3 | 8.1e-10 | 8.3816e-10 |

The raw binary64 runs to 100,000 generations are saved as `data/long_*.csv`. Their support bound remains exponentially small, but the two-point run shows growing rounding sensitivity. Both long runs are excluded from asymptotic fits. The following values are raw diagnostics, not certified estimates.

| m | law | n=10,000 | n=50,000 | n=100,000 |
|---:|---|---:|---:|---:|
| 2 | b=3 | 1.50030792 | 1.50009155 | 1.50005251 |
| 2 | {0,2} | 4.00800591 | 4.02571234 | 4.38532601 |

### 5.5 Reproduction and resource use

Run from this directory:

```sh
python3 code/run_suite.py
python3 code/check_float.py
python3 code/run_long.py
python3 -m pip install --target code/vendor gmpy2==2.3.2 python-flint==0.9.0
python3 code/certified.py --m 2 --law two2 --N 10000 --out data/cert_m2_two2.csv
python3 code/run_cert_suite.py
python3 code/run_cert_geom.py
python3 code/run_sparse.py
python3 code/validate.py
python3 code/analyze.py
```

Every numerical worker uses one thread. No worker pool is used. Resource measurements are stored in the corresponding JSON files.
The largest recorded worker peak RSS is 145.2 MiB. Concurrent worker peaks remain far below 4 GB.

CSV data are saved at every generation through 10 and every 50 generations thereafter; sparse-law runs also include every depth 2^j−1. `data/fits.csv` contains all fit coefficients; the stdout logs retain intermediate diagnostics.

<!-- END GENERATED RESULTS -->

## 6. What remains open

For deterministic offspring and a nondegenerate initial law with finite third tilted moment, this report does not prove that \(n^2q_n\) converges. Corollary 3 identifies its limit if it exists; the logarithmic upper and lower bounds in the cited sustainability paper do not imply existence. A proof must control persistent fluctuations or obtain sharper pointwise estimates. Differencing a conjectural asymptotic for \(G_n(m)-1\) is insufficient without a remainder estimate for its discrete derivative.

Theorem A shows that bare criticality permits arbitrarily large subsequential values of \(n^2q_n\) and does not even imply the exponent two. It does not assert a single asymptotic exponent for the sparse law.

For \(2<b<4\), Theorem 2 disproves the universal constant under bare criticality and identifies the only possible convergent scaled limit. The existence of that limit, the survival exponent for these infinite-tail laws, and exact correction terms remain unproved here. The numerical results distinguish a changing prefactor from an apparent unchanged exponent two, but cannot establish either asymptotic rigorously.

The two inputs in (1) alone cannot establish convergence. To see this at the level of the scalar equation, fix \(\beta>0\) and a sufficiently small \(\varepsilon>0\), and for large \(n\) set
\[
 u_n=\frac{\beta+\varepsilon\sin(\log n)}{(m-1)n},\qquad
 d_n=H(u_n)-u_{n+1},\qquad
 q_n=1-\left(1-\frac{m d_n}{m-1}\right)^{1/m}.
\]
For small enough \(\varepsilon\), \(d_n>0\) eventually and the last expression defines a probability. Taylor expansion gives
\[
 (m-1)^2 n^2q_n=
 \beta+\frac{\beta^2}{2}
 +\varepsilon\big((\beta+1)\sin(\log n)-\cos(\log n)\big)
 +\frac{\varepsilon^2}{2}\sin^2(\log n)+O(n^{-1}).
\]
This sequence oscillates, whereas \(u_n\to0\) and \(\prod_{j<n}(1+u_j)^{m-1}\asymp n^\beta\). Indeed, the oscillatory part of its logarithm has bounded partial sums, by comparison of \(\sum \sin(\log j)/j\) with its bounded integral. These scalar sequences are not asserted to arise from a DR law. They show that additional information about the distributional recursion is needed to turn the product estimate into a survival limit.

At \(b=4\), the third tilted moment diverges logarithmically. The experiments indicate slow convergence compatible with the finite-moment leading constant; neither the endpoint limit nor its correction is proved here. More general slowly varying tilted tails need a separate analysis.

The proof and simulations concern integer \(m\). A noninteger number of independent summands is not defined by the stated model. Replacing the offspring count by a random variable of real mean changes the recursion and its constants, as the geometric offspring results illustrate.
