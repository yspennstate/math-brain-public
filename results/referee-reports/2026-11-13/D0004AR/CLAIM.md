COUNTEREXAMPLE

# Law-determined norms and complete mixability

## Main results

**Theorem A.** Let \(X\) have finite mean \(\mu\), let \(n\geq2\), and put \(Y=n\mu-(n-1)X\). Write \(\mathcal N_n\) for the two inequalities in the question, for every threshold and every Definition 5 norm.

1. If \(X\) is bounded, then \(\mathcal N_n\) is equivalent to
   \[
   X\leq_{\rm cx}Y,\qquad\text{or equivalently}\qquad
   X-\mu\leq_{\rm cx}-(n-1)(X-\mu).                 \tag{1}
   \]
2. For arbitrary integrable \(X\), this equivalence holds if the norm quantifier is restricted to norms with the Fatou property. The original \(\mathcal N_n\) implies (1). Ordinary submajorization does not compare arbitrary unbounded arguments in every Definition 5 norm.
3. For arbitrary integrable \(X\), the original \(\mathcal N_2\) is equivalent to symmetry about \(\mu\), hence to 2-CM.

**Theorem B.** The condition \(\mathcal N_n\) does not imply \(n\)-CM for \(n=3,4\), even for densities on \([0,1]\) bounded above and bounded away from zero. At \(n=3\), one may take the analytic density
\[
f(x)=\frac1{10}+\frac{27}{10}(2x-1)^2,\qquad 0\leq x\leq1.       \tag{2}
\]
For both \(n=3,4\), there are also globally \(C^\infty\) densities supported on \([0,1]\), positive on \((0,1)\), satisfying \(\mathcal N_n\) without being \(n\)-CM. An explicit nonsymmetric \(n=4\) example is given below.

**Theorem C.** For \(0<p<1\), Bernoulli\((p)\) satisfies \(\mathcal N_n\) if and only if
\[
1/n\leq p\leq1-1/n.                                \tag{3}
\]
It is \(n\)-CM if and only if \(np\) is an integer. In particular, Bernoulli\((1/2)\) passes every inequality for \(n=3\) and is not 3-CM. For general discrete laws, reachability of \(n\mu\) is necessary but insufficient. The exact finite-support correction is the balanced count-vector condition in Proposition 5.

Thus absolute continuity, full interval support, smoothness, and an unspecified positive density floor are insufficient extra assumptions. Some positive shape classes and the unresolved scope are specified below.

## 1. Source and literature

The survey is by **Ruodu Wang** alone: *Current Open Questions in Complete Mixability*, first submitted in November 2014, published in *Probability Surveys* **12** (2015), 13–32, DOI [10.1214/14-PS250](https://doi.org/10.1214/14-PS250), [arXiv:1411.6190](https://arxiv.org/abs/1411.6190). The cited numbering is Definition 5, Theorem 5, and Open Problem 4, Section 2.4. Open Problem 4 is on PDF page 16 of the 24-page arXiv version and PDF page 14 of the 20-page author copy. Both are saved in `sources/`.

The following sources and follow-ups available by 13 November 2026 were checked.

| Source | Relevant conclusion |
|---|---|
| B. Wang and R. Wang (2011), [*The complete mixability and convex minimization problems with monotone marginal densities*](https://doi.org/10.1016/j.jmva.2011.05.002), *J. Multivariate Anal.* 102, 1344–1360 | The support/mean condition is sufficient for monotone densities. Together with the necessary norm inequalities, this already gives a converse within that class. |
| G. Puccetti, B. Wang and R. Wang (2012), [*Advances in complete mixability*](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/798B85CDAE8726564BACD67389FC9A6F/S0021900200009189a.pdf/advances_in_complete_mixability.pdf), *J. Appl. Probab.* 49, 430–440 | Structural results and complete mixability of concave densities. |
| G. Puccetti, B. Wang and R. Wang (2013), [*Complete mixability and asymptotic equivalence of worst-possible VaR and ES estimates*](https://doi.org/10.1016/j.insmatheco.2013.09.017), *Insurance Math. Econom.* 53, 821–828 | Theorem 3.4 gives the quantitative sufficient condition \(f\geq3/[n(b-a)]\). This is a three-author 2013 paper, distinct from the 2016 MOR paper. |
| G. Puccetti and R. Wang (2015), [*Detecting complete and joint mixability*](https://doi.org/10.1016/j.cam.2014.11.050), *J. Comput. Appl. Math.* 280, 174–187 | Numerical detection using minimum variance and rearrangements; no general norm converse. |
| B. Wang and R. Wang (2016), [*Joint mixability*](https://doi.org/10.1287/moor.2015.0755), *Math. Oper. Res.* 41, 808–826 | Norm necessary conditions and sufficient conditions for specified families, including monotone and symmetric unimodal densities. |
| C. Yin and D. Zhu, [*Joint mixability of elliptical distributions and related families*](https://arxiv.org/abs/1706.05499), 2017 preprint, v4 revised 11 May 2023 | Examples 2.1 and 2.3 give an odd-dimensional mass obstruction and symmetric polynomial densities that are not 3-CM. Combined with Theorem A, these already refute a density-only norm converse. Proposition 3.1 states a general finite-variance sufficiency criterion that is false: identical Bernoulli\((1/2)\) marginals at \(n=3\) refute it. It cannot be used as a valid converse. |
| T. Mao, B. Wang and R. Wang (2019), [*Sums of standard uniform random variables*](https://www.math.uwaterloo.ca/~wang/papers/2019Mao-Wang-Wang-JAP.pdf), *J. Appl. Probab.* 56, 918–936 | Characterizes the aggregation set of uniform marginals in dimension at least three, rather than the present arbitrary-marginal converse. |
| A. Komisarski and J. Labuschagne (2024; online 2023), [*The Distributions of the Mean of Random Vectors with Fixed Marginal Distribution*](https://doi.org/10.1007/s10959-023-01277-2), *J. Theor. Probab.* 37, 2121–2129 | Reviews the known shape classes and strengthens necessary conditions on centers; no general norm converse. |
| T. Koike, L. Lin and R. Wang (2024), [*Joint mixability and notions of negative dependence*](https://www.math.uwaterloo.ca/~wang/papers/2024Koike-Lin-Wang-MOR.pdf), *Math. Oper. Res.* 49, 2786–2802 | Relates constant sums to negative dependence and proves finite-support decompositions. |
| N. Mohammed (2026), [*Joint Exclusivity*](https://arxiv.org/abs/2604.17490), v4, 29 October 2026, Section 4.4 | Recalls the integer-sum criterion for Bernoulli joint mixability; not a norm converse. |
| O. P. Faugeras (2026), [*The Stick-Breaking and Ordering Representations of Compositional Data: Copulas and Regression Models*](https://doi.org/10.17713/ajs.v55i1.1986), *Austrian J. Statist.* 55, 1–31 | Connects simplex marginal compatibility to mixability and cites established necessary and family-specific sufficient conditions. |

No valid general converse to Theorem 5 was located. Valid class-specific converses are already in print, as indicated above. The symmetric bimodal obstruction has a clear predecessor in Yin–Zhu; no novelty claim is made for that obstruction. The reductions and examples below have independent proofs.

Searches used the exact phrases “law-determined norms,” “norm condition,” “Open Problem 4,” and combinations of complete mixability with convex order, bimodal densities, positive densities, counterexamples, and 2015–2026. The author's [working-paper list](https://www.math.uwaterloo.ca/~wang/pages/WPS3.html) and [publication list](https://www.math.uwaterloo.ca/~wang/publications.html) were also checked. This documents the search without claiming exhaustive coverage.

## 2. Majorization and the norm quantifier

Work on a standard atomless probability space; equivalently, realize laws on \((0,1)\) with Lebesgue measure. This assumption is used when constructing rearrangements. A norm means an extended-valued functional satisfying all five axioms of Definition 5, including monotonicity on nonnegative arguments. Set \(N(0)=0\) and use \(0\cdot\infty=0\).

For \(Z\geq0\), let \(Z^*\) be its decreasing rearrangement and put
\[
K_Z(a)=\int_0^a Z^*(u)\,du,\qquad0\leq a\leq1.
\]
For nonnegative integrable variables, \(U\prec\!\prec V\), meaning \(K_U\leq K_V\), is equivalent to increasing convex order \(U\leq_{\rm icx}V\). The Fatou property is
\[
0\leq Z_j\uparrow Z\quad\Longrightarrow\quad N(Z_j)\uparrow N(Z),       \tag{4}
\]
including infinite limits. Definition 5 does not impose (4).

**Lemma 1 (norm comparison).** Let \(U,V\geq0\) be integrable.

(a) The following are equivalent:
\[
\begin{aligned}
K_U(a)&\leq K_V(a) &&(0\leq a\leq1);                       \tag{5}\\
E(U-z)_+&\leq E(V-z)_+ &&(z\geq0);                        \tag{6}\\
N(U)&\leq N(V) &&\text{for every Fatou Definition 5 norm}. \tag{7}
\end{aligned}
\]
(b) If \(U,V\) are bounded, (5) is equivalent to comparison in every Definition 5 norm, without a Fatou or completeness assumption.

*Proof.* The quantile/stop-loss identities are
\[
K_Z(a)=\inf_{z\geq0}\{az+E(Z-z)_+\},\qquad
E(Z-z)_+=\sup_{0\leq a\leq1}\{K_Z(a)-az\}.                 \tag{8}
\]
They follow by splitting the decreasing-quantile integral at a crossing of \(Z^*\) and \(z\); a portion of a level set handles atoms. They prove (5) iff (6). The case \(a=1\) includes the mean inequality.

For \(0<a\leq1\),
\[
T_a(Z)=a^{-1}\int_0^a |Z|^*(u)\,du                        \tag{9}
\]
is a law-determined Fatou norm. Indeed,
\[
aT_a(Z)=\sup\{E[|Z|H]:0\leq H\leq1,\ EH\leq a\}.
\]
The formula proves the triangle inequality, homogeneity, monotonicity and Fatou property. Definiteness follows because \(a>0\). Thus (7), or comparison in all norms, implies (5).

For the converse, replace \(N\) by its absolute extension \(\nu(Z)=N(|Z|)\). It agrees with \(N\) on positive arguments and satisfies all the axioms: use \(|Z+W|\leq|Z|+|W|\), monotonicity, and subadditivity.

If \(\nu(V)=\infty\), comparison is immediate. If \(V=0\), (5) implies \(U=0\). Otherwise suppose \(\nu(V)<\infty\). Choose \(\varepsilon>0\) with \(p=P(V\geq\varepsilon)>0\). Monotonicity makes the norm of an indicator of probability \(p\) finite. Finitely many translates of a length-\(p\) interval on the unit circle cover the circle. Their indicators are equidistributed and their sum dominates 1. Hence \(C=\nu(1)<\infty\), and for bounded arguments
\[
\nu(Z)\leq C\|Z\|_\infty,\qquad
|\nu(Z)-\nu(W)|\leq C\|Z-W\|_\infty.                     \tag{10}
\]

We first establish, for bounded \(V\geq0\) and a finite partition \(\mathcal P\),
\[
\nu(E[V\mid\mathcal P])\leq\nu(V).                       \tag{11}
\]
On each positive-probability cell choose a uniform variable \(T_i\) and let \(q_i\) be the conditional quantile of \(V\). On that cell define \(V_j=q_i((T_i+j/m)\bmod1)\), \(0\leq j<m\). Each \(V_j\) has the law of \(V\). The cyclic average is an equally spaced Riemann sum of the monotone function \(q_i\). If \(0\leq V\leq M\), its error from the integral is at most \(M/m\), uniformly. Therefore
\[
\left\|m^{-1}\sum_{j=0}^{m-1}V_j-E[V\mid\mathcal P]\right\|_\infty\leq M/m.
\]
The triangle inequality and (10) give (11).

The probabilistic Hardy–Littlewood–Pólya theorem, namely the increasing-convex version of Strassen's coupling theorem, says that (5) is equivalent to a coupling with
\[
U\leq E[V\mid U]\quad\text{a.s.}                        \tag{12}
\]
Take this coupling. If \(U,V\) are bounded, partition the range of \(U\) into intervals of length at most \(\delta\), and let \(U_\delta\) equal the lower endpoint in each cell. Conditioning (12) on this partition gives \(U_\delta\leq E[V\mid\mathcal P_\delta]\). Equations (10) and (11) imply
\[
\nu(U_\delta)\leq\nu(V),\qquad
\nu(U)\leq\nu(V)+C\delta.
\]
Let \(\delta\downarrow0\). This proves (b), using uniform continuity on bounded variables rather than an unqualified a.s. limiting argument.

For unbounded \(U,V\) and a Fatou norm, take (12) and set \(W_j=E[V\wedge j\mid U]\). Jensen gives \(W_j\leq_{\rm cx}V\wedge j\). The bounded result yields
\[
\nu(W_j)\leq\nu(V\wedge j)\leq\nu(V).
\]
Conditional monotone convergence gives \(W_j\uparrow E[V\mid U]\geq U\). The Fatou property and monotonicity prove (7). The absolute extension has the positive Fatou property when \(N\) does. \(\square\)

The classical coupling theorem used in this proof is V. Strassen, [*The existence of probability measures with given marginals*](https://doi.org/10.1214/aoms/1177700153), *Ann. Math. Statist.* 36 (1965), 423–439. It is precisely the probabilistic HLP theorem, not a continuity assumption about norms. The equivalent exact-interpolation viewpoint is the Calderón majorization principle for \((L^1,L^\infty)\); see A. P. Calderón, [*Spaces between \(L^1\) and \(L^\infty\) and the theorem of Marcinkiewicz*](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/26/3/96141/spaces-between-l-1-and-l-and-the-theorem-of-marcinkiewicz).

**Proposition 2 (unbounded non-Fatou obstruction).** There exist nonnegative integrable \(U,V\) with \(U\leq_{\rm cx}V\) and a Definition 5 norm with \(N(V)<\infty=N(U)\).

*Proof.* On \((0,1)\), define
\[
v(t)=
\begin{cases}[t\log^2(1/t)]^{-1},&0<t<e^{-3},\\0,&e^{-3}\leq t<1.\end{cases}
\]
It is decreasing with integral \(1/3\). Let \(V=v(T)\), \(T\sim U(0,1)\). Put \(L_k=3^k\), \(a_k=e^{-2L_k}\), \(b_k=e^{-L_k}\). On each of the disjoint intervals \(I_k=(a_k,b_k)\), replace \(v\) by its average
\[
h_k=\{2L_k(b_k-a_k)\}^{-1}.
\]
Leave \(v\) unchanged elsewhere and call the resulting variable \(U=u(T)\). It is a conditional expectation of \(V\): the sigma field has the \(I_k\) as atoms and retains all information on their complement. Thus \(U\leq_{\rm cx}V\).

Let \(D\) consist of the random variables \(Z\) for which some \(C<\infty\) and integer \(m\geq1\) satisfy
\[
|Z|^*(t)\leq C v(t/m)\quad\text{for a.e. }0<t<1.        \tag{13}
\]
This is a law-invariant solid linear subspace of \(L^1\). Solidity is immediate; linearity follows from
\[
|Z+W|^*(t)\leq |Z|^*(t/2)+|W|^*(t/2)
\]
by increasing \(m\). Integrating (13) proves \(D\subset L^1\). It contains \(V\) and all bounded variables: choose \(m>e^3\), so that \(v(t/m)\geq v(1/m)>0\).

On all of \(L^0\), define
\[
N(Z)=
\begin{cases}E|Z|,&Z\in D,\\+\infty,&Z\notin D.\end{cases}              \tag{14}
\]
The properties of \(D\) prove all five axioms. For the triangle inequality, if both right-hand norms are finite, both arguments and their sum lie in \(D\); otherwise it is automatic.

Put \(t_k=(b_k-a_k)/2\). Since \(u=h_k\) on a set of measure \(2t_k\), \(U^*(t_k)\geq h_k\). For every fixed \(m\),
\[
\frac{h_k}{v(t_k/m)}
=\frac{\log^2(m/t_k)}{4mL_k}\longrightarrow\infty.
\]
For every \(t\in[t_k/2,t_k]\), monotonicity gives
\[
\frac{U^*(t)}{v(t/m)}
\geq\frac{h_k}{v(t_k/(2m))}
=\frac{\log^2(2m/t_k)}{8mL_k}\longrightarrow\infty.
\]
Thus no a.e. bound (13) is possible: \(U\notin D\), whereas \(V\in D\). Finally \(U\wedge j\in D\), and \(N(U\wedge j)\uparrow EU<\infty\), while \(N(U)=\infty\). The norm explicitly fails Fatou. \(\square\)

This counterexample concerns the general norm comparison lemma. It does not assert that a particular hinge pair generated by one \(F\) has this pathology. For unbounded integrable \(F\), the implications established here are exactly
\[
\mathcal N_n\text{ for all Definition 5 norms}
\ \Longrightarrow\ (1)\
\Longleftrightarrow\
\mathcal N_n\text{ for all Fatou norms}.               \tag{15}
\]

## 3. Reduction of the threshold family; \(n=2\)

**Proposition 3.** The first two assertions of Theorem A hold. For bounded laws the first inequality, tested in \(L^1\) at every threshold, already implies the entire norm family.

*Proof.* Put \(c=n-1\), \(s=(n\mu-t)/c\). Then
\[
c(X-s)_-=(Y-t)_+,\qquad c(X-s)_+=(Y-t)_-.             \tag{16}
\]
The first \(L^1\) inequality is therefore \(E(X-t)_+\leq E(Y-t)_+\) for all real \(t\). Since \(EX=EY=\mu\), this is exactly \(X\leq_{\rm cx}Y\).

Conversely assume this convex order. For fixed \(t\), both \(x\mapsto(x-t)_+\) and \(x\mapsto(t-x)_+\) are convex. Composing either with an increasing convex function gives
\[
(X-t)_+\leq_{\rm icx}(Y-t)_+,\qquad
(X-t)_-\leq_{\rm icx}(Y-t)_-.                       \tag{17}
\]
Apply Lemma 1 and (16). Bounded arguments allow every Definition 5 norm; integrable arguments allow all Fatou norms. \(\square\)

In increasing-quantile notation, the explicit majorization conditions are, for \(0<a\leq1\),
\[
\begin{aligned}
\int_{1-a}^1(Q_X(u)-t)_+\,du
&\leq c\int_0^a(s-Q_X(u))_+\,du,\\
\int_0^a(t-Q_X(u))_+\,du
&\leq c\int_{1-a}^1(Q_X(u)-s)_+\,du.                \tag{18}
\end{aligned}
\]
Endpoint conventions at atoms do not change the integrals. Lemma 1 states exactly when (18) replaces the literal norm quantifier.

For comparison, \(n\)-CM implies (1) directly. If \(Z_i=X_i-\mu\) form a complete mix, \(Z_1=-\sum_{i=2}^n Z_i\); thus for convex \(\phi\),
\[
E\phi(Z_1)\leq\frac1{n-1}\sum_{i=2}^nE\phi(-(n-1)Z_i)
=E\phi(-(n-1)Z_1).
\]
This necessary convex order does not construct the joint coupling in the reverse direction.

**Proposition 4.** For every integrable \(F\), \(\mathcal N_2\), symmetry about its mean, and 2-CM are equivalent.

*Proof.* The \(L^1\) implication gives \(X\leq_{\rm cx}2\mu-X\). Affine reflection preserves convex order and gives the reverse comparison. The call functions therefore agree at every threshold. Their right derivatives are \(-P(X>t)\), so \(X\stackrel d=2\mu-X\).

For a symmetric law, \((X,2\mu-X)\) is a complete mix. With \(s=2\mu-t\), the positive-part law of \(X-t\) is the negative-part law of \(X-s\), and conversely. Every original norm inequality is an equality, including infinite values. Finally any 2-complete mix has \(X_2=2\mu-X_1\), proving symmetry. \(\square\)

## 4. Atoms and the discrete correction

*Proof of Theorem C.* Let \(B\sim\operatorname{Bernoulli}(p)\), \(0<p<1\). Convex order \(B\leq_{\rm cx}np-(n-1)B\) requires the interval spanned by the latter support to contain \([0,1]\); otherwise a hinge beyond one endpoint violates the order. Hence \(np\geq1\) and \(np-(n-1)\leq0\), giving (3).

Conversely, under (3), the two-point variable \(Y=np-(n-1)B\) has mean \(p\) and endpoints \(l\leq0\), \(h\geq1\). A convex function on \([l,h]\) lies below its endpoint chord. Taking expectations at \(B\) shows \(E\phi(B)\leq E\phi(Y)\), because the expectations of the chord agree and \(Y\) is supported on its endpoints. Proposition 3 proves the norm condition.

A sum of Bernoulli variables is integer-valued, so a complete mix requires \(np\in\mathbb Z\). If \(np=k\), choose a uniformly random \(k\)-element subset of the coordinate indices and use its membership indicators. Each marginal is Bernoulli\((k/n)\), and the sum is \(k\) surely. The degenerate laws \(p=0,1\) satisfy all inequalities and are completely mixable as well. \(\square\)

In particular the inequalities for Bernoulli\((1/2)\), \(n=3\), hold for every norm and every threshold, but the required sum \(3/2\) is impossible.

More generally, every bounded symmetric law satisfies \(\mathcal N_n\). For centered symmetric \(Z\) and \(c\geq1\),
\[
Z\leq_{\rm cx}cZ\stackrel d=-cZ.                    \tag{19}
\]
Indeed \(Z=c^{-1}(cZ)+(1-c^{-1})0\); convexity followed by \(E\phi(cZ)\geq\phi(0)\) proves the comparison. Symmetric lattice laws therefore give further counterexamples whenever their prescribed sum is inaccessible. Not every inaccessible lattice law passes the inequalities: Bernoulli\((1/10)\) fails them at \(n=3\).

If the support lies in \(a+h\mathbb Z\), \(h>0\), a necessary condition is
\[
n\mu\in na+h\mathbb Z.                              \tag{20}
\]
For a proper subset \(A\) of that lattice, the stronger necessary condition is \(n\mu\in A+\cdots+A\), with \(n\) summands. Reachability still omits the marginal masses.

**Proposition 5 (finite-support characterization).** Suppose \(F\{a_j\}=p_j>0\), \(1\leq j\leq m\), and define
\[
\mathcal K=\{k\in\mathbb Z_+^m:\ \sum_jk_j=n,\ \sum_jk_ja_j=n\mu\}.
\]
Then \(F\) is \(n\)-CM if and only if
\[
(p_1,\ldots,p_m)\in\operatorname{conv}\{k/n:k\in\mathcal K\}.          \tag{21}
\]

*Proof.* Symmetrize a complete mix by an independent uniform permutation. Its count vector lies in \(\mathcal K\) and has expected counts \(np_j\), proving necessity. Conversely choose a count vector according to the convex-combination weights in (21), then uniformly permute the multiset. Every marginal has probabilities \(p_j\), and every sum is \(n\mu\). \(\square\)

For countably supported discrete laws the exact condition is a probability measure on admissible finite-count vectors with the prescribed expected counts; an unspecified closed convex hull should not replace that condition.

The natural discrete correction is arithmetic reachability **and compatibility of masses with admissible count vectors**. For two-point laws reachability alone is sufficient. In general (21), or its dual capacity inequalities, is stronger than the norm condition.

For example, give \(0,1,2\) masses \(49/100,1/50,49/100\), and let \(n=3\). Symmetry about 1 proves every norm inequality. The target 3 is reachable, and each atom occurs in an admissible tuple. But the only unordered sum-3 triples are \((0,1,2)\) and \((1,1,1)\). Every such triple contains a 1, requiring \(P(X=1)\geq1/3\), whereas its actual probability is \(1/50\).

## 5. Absolutely continuous counterexamples

**Lemma 6 (mass obstruction).** Let \(X\) have mean \(\mu\), and let \(A\) be measurable with
\[
\operatorname{dist}(n\mu,A+\cdots+A)\geq d>0.
\]
Write \(q=P(X\notin A)\). Every coupling with the same marginals satisfies
\[
E\left(\sum_iX_i-n\mu\right)^2\geq d^2(1-nq)_+.      \tag{22}
\]
In particular \(q<1/n\) excludes \(n\)-CM. Without a positive distance, \(n\mu\notin A+\cdots+A\) still requires \(q\geq1/n\) for a complete mix.

*Proof.* The union bound gives probability at least \(1-nq\) that every coordinate belongs to \(A\). On that event the deviation is at least \(d\). If equality of the sum is impossible on the event, its probability must be zero for a complete mix. \(\square\)

This is the continuous counterpart of the discrete capacity obstruction. Its odd-dimensional symmetric form appears in Yin–Zhu, Example 2.1. All applications here have strict margins and do not depend on boundary conventions in that example.

### 5.1 Two endpoint components

Define
\[
G_{p,\varepsilon}=(1-p)U[0,\varepsilon]+pU[1-\varepsilon,1],
\qquad0<\varepsilon<1/2.
\]
It is the law of \(X=(1-\varepsilon)B+\varepsilon U\) with independent Bernoulli\((p)\) \(B\) and uniform \(U\). Its mean is \(\mu=(1-\varepsilon)p+\varepsilon/2\).

**Lemma 7.** If \(1/n\leq p\leq1-1/n\), then \(G_{p,\varepsilon}\) satisfies \(\mathcal N_n\).

*Proof.* Theorem C gives \(B-p\leq_{\rm cx}-(n-1)(B-p)\); the centered uniform satisfies the same comparison by (19). Convex order is preserved under independent addition, by conditioning first on one summand and then the other. Apply this to \((1-\varepsilon)(B-p)\) and \(\varepsilon(U-1/2)\), then apply Proposition 3. \(\square\)

Take
\[
G_3=G_{1/2,1/10},\qquad G_4=G_{2/5,1/20}.
\]
Their densities are
\[
g_3(x)=5\mathbf1_{[0,1/10]\cup[9/10,1]}(x),\qquad
g_4(x)=12\mathbf1_{[0,1/20]}(x)+8\mathbf1_{[19/20,1]}(x).
\]
Both pass all norms. For \(A_\varepsilon=[0,\varepsilon]\cup[1-\varepsilon,1]\), its \(n\)-fold sum is the union
\[
\bigcup_{k=0}^n[k(1-\varepsilon),\ k(1-\varepsilon)+n\varepsilon].      \tag{23}
\]
For \(G_3\) the target is \(3/2\); the adjacent intervals end at \(6/5\) and start at \(9/5\), giving gap \(3/10\). For \(G_4\), the mean is \(81/200\), the target is \(81/50\); the adjacent intervals end at \(23/20\) and start at \(19/10\), giving gap \(7/25\). Since every marginal is in its core surely, neither law is completely mixable at the specified dimension.

### 5.2 Full support and a positive density floor

Let
\[
F_3=\tfrac9{10}G_3+\tfrac1{10}U[0,1].              \tag{24}
\]
Let \(H_4\) have density
\[
h_4(x)=\tfrac{157}{100}-\tfrac{57}{50}x,\quad0\leq x\leq1,
\]
which integrates to 1, is at least \(43/100\), and has mean \(81/200\). Put
\[
F_4=\tfrac9{10}G_4+\tfrac1{10}H_4.                 \tag{25}
\]

**Proposition 8.** \(F_3,F_4\) pass every norm inequality at \(n=3,4\), respectively, but are not 3-CM and 4-CM. Their densities are bounded below by \(1/10\) and \(43/1000\), respectively.

*Proof.* \(F_3\) is symmetric, so (19) proves its norm condition. For \(F_4\), the reflected-dilation order for the filler \(H_4\) can be checked directly. On \([0,1]\) its call function is
\[
C(t)=(1-t)^2(81-38t)/200.
\]
With \(\mu=81/200\) and \(s=(4\mu-t)/3\), one has \(s\in[0,1]\) for \(t\in[0,1]\), and
\[
\begin{split}
D(t)&=3\{C(s)+s-\mu\}-C(t)\\
&=\frac{11875000t^3-35208750t^2+17910675t+10797948}{56250000}.          \tag{26}
\end{split}
\]
The degree-three Bernstein coefficients on \([0,1]\) are
\[
\frac{299943}{1562500},\quad
\frac{5589391}{18750000},\quad
\frac{2750537}{14062500},\quad
\frac{5374873}{56250000}.                            \tag{27}
\]
They are positive, so \(D\geq0\). For \(t\leq0\), Jensen makes the call of \(4\mu-3H_4\) at least \(\mu-t\), the call of \(H_4\). For \(t\geq1\), the latter call is zero. Thus \(H_4\leq_{\rm cx}4\mu-3H_4\).

Convex-order inequalities are preserved under mixtures of laws with the same mean: average the convex-function inequalities. Both \(G_4,H_4\) have mean \(81/200\); Lemma 7 and Proposition 3 therefore prove the norm condition for \(F_4\).

For \(F_3\), the core \(A=[0,1/10]\cup[9/10,1]\) has outside probability \(q=2/25\) and sum gap \(3/10\). Lemma 6 gives, for every coupling,
\[
E(S-3/2)^2\geq\frac9{100}(1-6/25)=\frac{171}{2500}>0.                \tag{28}
\]
For \(F_4\), use \(A=[0,1/20]\cup[19/20,1]\). Integrating the affine filler over the symmetric middle interval gives \(q=9/100\). Hence
\[
E(S-81/50)^2\geq\frac{49}{625}(1-36/100)=\frac{784}{15625}>0.         \tag{29}
\]
The positive fillers also give the stated density bounds. \(\square\)

### 5.3 An analytic example and global smoothing

**Proposition 9.** The analytic density (2) passes all norm inequalities at \(n=3\), but is not 3-CM.

*Proof.* It integrates to 1 and is symmetric about \(1/2\), proving the norm condition. Three points of \([0,1]\) summing to \(3/2\) must include one in \([1/4,3/4]\). Otherwise the centered points \(2x_i-1\) all have absolute value greater than \(1/2\). Two have the same sign; their sum in absolute value exceeds 1 and cannot be cancelled by the third.

A complete mix would therefore require \(3P(X\in[1/4,3/4])\geq1\). Direct integration of (2) gives
\[
P(X\in[1/4,3/4])
=\tfrac1{10}\tfrac12+\tfrac9{10}(\tfrac12)^3
=\tfrac{13}{80}<\tfrac13,
\]
a contradiction. \(\square\)

The zero-floor component \(3(2x-1)^2\) is the affine image of the \(r=1\) example in Yin–Zhu, Example 2.3. The uniform component makes the density positive without removing the strict obstruction. A quantitative certificate uses core \([0,1/5]\cup[4/5,1]\), with sum gap \(1/10\) and outside probability \(159/625\). It gives
\[
E(S-3/2)^2\geq 37/15625>0.                          \tag{30}
\]

**Corollary 10.** For \(n=3,4\), a globally \(C^\infty\) compactly supported density can satisfy \(\mathcal N_n\) without being \(n\)-CM.

*Proof.* Start from \(F_n\) in (24) or (25). Add an independent centered symmetric variable \(Z\) with a smooth bump density supported on \([-\eta,\eta]\), positive inside, with all derivatives zero at the endpoints. Use \(\eta=1/100\), and for instance normalize \(\exp[-1/(1-(z/\eta)^2)]\) inside the interval.

The reflected-dilation order is preserved by independent addition, using (19) for \(Z\). The resulting density is globally smooth, supported on \([-\eta,1+\eta]\), and positive in its interior.

It puts probability at least \(9/10\) in the enlarged core \(A_n+[-\eta,\eta]\), since the \(G_n\) mixture component always does. The sum gap is at least \(d_n-n\eta>0\), with \(d_3=3/10,d_4=7/25\). The outside probability is at most \(1/10<1/n\), so Lemma 6 still excludes a complete mix. Finally the affine map \(x\mapsto(x+\eta)/(1+2\eta)\) gives support \([0,1]\) and preserves both properties. \(\square\)

There is no conflict with the quantitative density-floor theorem of 2013: that theorem requires a specified bound depending on \(n\), rather than an arbitrary positive floor. A globally smooth compactly supported density must approach zero at its support endpoints. The polynomial (2) instead is analytic and uniformly positive on the closed interval itself.

## 6. Positive classes

The monotone-density theorem gives sufficiency of
\[
a+\frac{b-a}{n}\leq\mu\leq b-\frac{b-a}{n}            \tag{31}
\]
for a density monotone on its bounded support \([a,b]\). The norm condition implies (31) by using \(L^\infty\) at \(t=\mu\). Thus the known 2011 theorem supplies the norm converse in that class.

A larger class is the union of bounded monotone densities and symmetric unimodal densities. For example, a symmetric triangular density belongs to the latter class and is not monotone on its whole support. The following classical result is included with a construction.

**Proposition 11.** A law with a symmetric unimodal density about \(\mu\) is \(n\)-CM for every \(n\geq2\); when its mean exists, the center is \(\mu\).

*Proof.* Translate to \(\mu=0\), and take a nonincreasing right-continuous version \(f(r)\) on \(r>0\). Its symmetric density is a mixture of uniforms on \([-r,r]\), with mixing measure
\[
G(dr)=-2r\,df(r).
\]
Integration by parts gives total mass \(2\int_0^\infty f(r)\,dr=1\), and
\[
f(x)=\int_{[|x|,\infty)}(2r)^{-1}\,G(dr)
\]
almost everywhere. Boundary terms vanish because \(rf(r)\to0\) both at zero and infinity for nonincreasing integrable \(f\).

Pairs of uniforms on \([0,1]\) are \((U,1-U)\). For a triple, uniformly permute
\[
(T,\ T+1/2,\ 1-2T),\qquad T\sim U[0,1/2].
\]
Its sum is \(3/2\); each marginal is uniform because on either half-interval the three component densities sum to \(2+1=3\), divided by 3 after permutation. Use pairs for even \(n\), and this triple with pairs for odd \(n\). Translate and rescale to \([-r,r]\), obtaining sum zero. Draw a single common radius \(R\sim G\) and use the conditional uniform complete mix. Every marginal has density \(f\), and its sum is zero. Translate back. \(\square\)

This is the symmetric-unimodal theorem of Rüschendorf–Uckelmann, also used in Wang–Wang (2016). It does not settle the converse for arbitrary nonsymmetric unimodal densities. For even \(n\), symmetry alone suffices by antithetic pairs; the \(n=4\) counterexample is accordingly nonsymmetric.

## 7. Characterizing Definition 5 norms

**Proposition 12.** The restrictions of Definition 5 norms to nonnegative variables are exactly the definite homogeneous subadditive monotone law-invariant gauges on that cone. Every such gauge extends to a Definition 5 norm by \(Z\mapsto\nu(|Z|)\). Thus Theorem 5 has the same quantifier when restricted to absolute law-determined norms.

*Proof.* Restriction preserves the axioms. For the extension, use \(|Z+W|\leq|Z|+|W|\), monotonicity and subadditivity to prove the triangle inequality. All other axioms follow immediately. Every argument appearing in Theorem 5 is nonnegative. \(\square\)

The literal signed norm need not be absolute. For \(\alpha>0\),
\[
N_\alpha(Z)=E|Z|+\alpha|EZ|\quad(Z\in L^1),\qquad
N_\alpha(Z)=\infty\quad(Z\notin L^1)                 \tag{32}
\]
satisfies Definition 5. A centered Rademacher variable has value 1, whereas its absolute value has norm \(1+\alpha\). Thus the literal definition is broader than absolute rearrangement-invariant Banach function norms.

For an absolute norm, the finite domain is a solid law-invariant normed linear space, extended by infinity elsewhere; the converse construction also satisfies Definition 5. Completeness and Fatou are separate requirements. An allowed degenerate positive-cone case assigns infinity to every nonzero positive variable. If any nonzero positive variable has finite norm, the indicator-covering argument in Lemma 1 gives \(0<\nu(1)<\infty\), hence finiteness and uniform continuity on bounded variables.

Under Fatou, the nondegenerate absolute norms are the usual rearrangement-invariant Banach function norms on the probability interval. Their Köthe/Lorentz–Luxemburg representation is
\[
\nu(Z)=\sup_{w\in\mathcal W}\int_0^1|Z|^*(u)w(u)\,du,               \tag{33}
\]
where \(\mathcal W\) can be taken to consist of nonnegative decreasing associate-dual weights. Infinite integrals are allowed. Hardy's lemma gives full symmetry from this representation. Conversely, the supremum over a separating family of such weighted integrals, if finite on 1, gives an absolute law-invariant Fatou norm. The rearrangement inequality \(K_{|Z+W|}\leq K_{|Z|}+K_{|W|}\) and Hardy's lemma give subadditivity. Monotone convergence gives Fatou. The classical representation is discussed in the [Dodds–Dodds notes on symmetric function norms](https://maths.anu.edu.au/files/CMAProcVol29-DoddsDodds2.pdf).

For completeness, conditional averaging and Fatou give \(\nu(Z)\geq\nu(1)E|Z|\). A series with summable \(\nu\)-norms therefore converges absolutely a.s.; Fatou bounds the norm of each tail by the sum of its constituent norms. The summable-subsequence argument then proves completeness.

Definition 5 without Fatou permits the domain restriction (14), so it cannot simply be identified with the class in (33). For a modern discussion of automatic Fatou properties under additional assumptions, see S. Chen, N. Gao, D. Leung and L. Li, [*Automatic Fatou Property of Law-invariant Risk Measures*](https://arxiv.org/abs/2107.08109). No automatic-Fatou result from that setting is assumed here. The signed extensions beyond Proposition 12 are not fully classified by this report.

## 8. Numerical validation

The main run used one process and one numerical thread and reported peak resident memory **822,984,704 bytes** (0.823 GB; 0.766 GiB), below 4 GB. Versions were Python 3.13.2, NumPy 2.2.3, SciPy 1.15.2. Inherited nice priority was 10. No helper agents or worker pools were used.

### 8.1 LP formulation

Partition \([0,1]\) into \(M\) equal cells, integrate the piecewise densities to obtain probabilities \(p_j\), and use cell midpoints \(x_j\). Symmetrization permits one nonnegative variable \(w_k\) per unordered \(n\)-tuple, with marginal constraints
\[
\sum_k(k_j/n)w_k=p_j.
\]
For feasibility, retain only tuples satisfying
\[
\left|\sum_jk_jx_j-n\mu\right|\leq n/(2M).           \tag{34}
\]
A continuous complete mix necessarily rounds into this band, so this is a relaxation rather than a spurious exact-lattice test. Floating-point infeasibility is a diagnostic, not the proof; Lemma 6 supplies exact certificates.

The cost LP keeps all unordered tuples and minimizes squared deviation from the original target \(n\mu\). Its optima concern the finite midpoint laws, not the original continuous laws. A coarse midpoint-law mean can differ from the continuous mean if a cell straddles a density discontinuity. Density integration uses exact-form antiderivatives evaluated in floating-point arithmetic.

The exact continuous lower bounds are:

| Law | n | Mean | Core sum gap | Outside-core probability | Universal lower bound on squared error |
|---|---:|---:|---:|---:|---:|
| G3 | 3 | 1/2 | 3/10 | 0 | 9/100 = 0.090000 |
| F3 | 3 | 1/2 | 3/10 | 2/25 | 171/2500 = 0.068400 |
| G4 | 4 | 81/200 | 7/25 | 0 | 49/625 = 0.078400 |
| F4 | 4 | 81/200 | 7/25 | 9/100 | 784/15625 = 0.050176 |

Band LP results (HiGHS status 2 means infeasible):

| Law | M=20 | M=40 | M=80 | M=160 | Columns at M=160 |
|---|---|---|---|---|---:|
| G3 | infeasible | infeasible | infeasible | infeasible | 0 |
| F3 | infeasible | infeasible | infeasible | infeasible | 12,960 |
| G4 | infeasible | infeasible | infeasible | infeasible | 0 |
| F4 | infeasible | infeasible | infeasible | infeasible | 387,936 |

For G3 and G4 there are no admissible band columns; enumeration establishes infeasibility before a solver is invoked.

Finite-law cost LP optima and rearrangement mean squared errors:

| Law | Cost LP M=10 | Cost LP M=20 | RA M=1000 | RA M=4000 | RA M=16000 |
|---|---:|---:|---:|---:|---:|
| G3 | 0.202500000 | 0.160625000 | 0.147298153 | 0.147396755 | 0.147367984 |
| F3 | 0.166500000 | 0.125225000 | 0.115132419 | 0.115129426 | 0.115143667 |
| G4 | 0.194800000 | 0.216600000 | 0.176148159 | 0.176135307 | 0.176150770 |
| F4 | 0.147026800 | 0.159581950 | 0.123989607 | 0.124003486 | 0.123995637 |

### 8.2 Rearrangement algorithm and controls

For each marginal, the algorithm uses quantiles \((i+1/2)/M\), four deterministic-seed random starts, and cyclic rearrangement of each column opposite to the sum of the remaining columns. It stops below improvement \(10^{-14}\) or at 100 sweeps and keeps the best squared error. These are heuristic upper bounds for empirical quantile-law problems; no optimality or nonmixability conclusion follows from the algorithm alone. Some runs reach the sweep limit.

Uniform controls at \(n=3,4\) were feasible in the band LP for \(M=20,40\), with residuals below \(10^{-15}\). Their \(M=1000\) rearrangement mean squared errors were \(2.5\times10^{-7}\) and \(1.46\times10^{-7}\), respectively.

The exact symbolic checks use rational coefficients for every call-gap polynomial piece, evaluating all interval endpoints and real stationary points. They independently verify the norm condition for all four endpoint-based density laws. Rational support-gap and mass calculations verify the nonmixability bounds. The analytic proofs do not depend on the LP solver.

### 8.3 Reproduction and files

From this folder, run:

~~~sh
python3 code/exact_checks.py > data/exact_checks.log 2>&1
python3 code/experiments.py > data/experiments.log 2>&1
python3 code/controls.py > data/controls.log 2>&1
~~~

The numerical script sets thread environment variables to 1 before importing numerical libraries and passes `threads=1` to HiGHS. The solver time limit is 20 seconds; setup/postprocessing can make total wall time longer. The largest band LP had 387,936 columns. The initial exploratory log is retained as `data/preliminary_experiments.log`; reported data come from `data/experiments.log`.

| Path | Contents |
|---|---|
| `code/experiments.py` | Sparse exchangeable LPs, piecewise density integration, inverse CDFs, rearrangement diagnostics. |
| `code/exact_checks.py` | Exact rational/algebraic checks for call gaps, support gaps, masses, the polynomial example and the reachable-lattice example. |
| `code/controls.py` | Uniform controls. |
| `data/lp_results.csv` and `data/lp_results.json` | All LP rows, statuses, residuals and sizes. |
| `data/ra_results.csv` and `data/ra_results.json` | Rearrangement results and empirical sum ranges. |
| `data/exact_certificates.json` | Exact certificates and call-gap polynomial pieces. |
| `data/controls.json` and `data/environment.json` | Controls, software versions, main-run RSS and thread setting. |
| `sources/*.pdf` and `sources/*.txt` | Downloaded primary papers and extracted text. |
| `LOG.md` | Running log and sandbox limitations. |

Pinned dependencies are in requirements.txt; source URLs and SHA-256 hashes are in sources/manifest.json.

## 9. Remaining scope

The unrestricted converse is false for atoms and densities, including smooth densities and positive full-support densities. For bounded laws, adding further Definition 5 norms cannot improve on (1).

The positive results here are the \(n=2\) equivalence; the Bernoulli criterion with its arithmetic correction; the finite-support count-vector criterion; the established monotone-density converse; and the symmetric-unimodal construction. The union of the last two classes strictly contains the monotone-density class.

The following questions remain unsettled here:

- A useful shape characterization beyond these classes, particularly for **nonsymmetric unimodal** densities satisfying the norm condition.
- The sharp quantitative density-floor threshold at fixed \(n\) and mean. An unspecified positive floor is insufficient; the established bound \(3/[n(b-a)]\) is sufficient.
- A stronger reduction for the special hinge pairs generated by one unbounded integrable law under the literal all-Definition-5 quantifier. Proposition 2 rules out the general unbounded submajorization shortcut; (15) is the exact implication proved here.
- A classification of all signed extensions in Definition 5 without Fatou or completeness, beyond the positive-cone reduction.

No assertion about every sufficiently large dimension for a fixed law follows from these fixed-\(n\) counterexamples.

Task: “when do the law-determined-norm inequalities imply complete mixability?” — 13 November 2026, 02:28 Asia/Tbilisi (session launch).

