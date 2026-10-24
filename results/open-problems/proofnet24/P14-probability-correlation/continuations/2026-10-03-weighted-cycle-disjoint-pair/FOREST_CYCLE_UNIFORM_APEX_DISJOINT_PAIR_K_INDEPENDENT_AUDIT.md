# Independent audit: uniform cycle apex roots and the disjoint-pair extension

3 October 2026 UTC. **PASS.** For a uniform weighted cycle \(C_n\),
\(n\geq3\), with rim activity \(\lambda\geq0\) and uniform profile
\(\beta_j=1\), the one-apex ordinary-forest partition has only negative real
zeros. They are distinct when \(0<\lambda<\infty\), and at \(\lambda=0\)
they coalesce at \(-1\). The same calculation is valid for the optional
two-vertex multigraph \(C_2\) consisting of two parallel rim edges. Combining
this factorization with Sections 2--4 of
forest_disjoint_rank_one_attachment_forest_backbone_proof.md proves the
claimed all-activity negative correlation for the two disjoint marked edges.
It is strict when \(abcd>0\) and \(n\geq2\).

I independently reconstructed the cycle enumeration, the cyclic-composition
factor, the generating-function and Chebyshev formulas, every boundary case,
and the interface with the four-core proof. I also wrote a new exact checker
which imports no implementation from the forest-backbone work. I found no
mathematical gap or counterexample. Historical novelty and external peer
review are not certified.

## 1. Backbone normalization

Let

\[
p=\frac{\lambda}{1+\lambda}.
\]

Finite \(\lambda\geq0\) is equivalent to \(0\leq p<1\). An edge subset of
\(C_n\) is a forest unless it contains all \(n\) rim edges. Therefore

\[
\begin{aligned}
Z_H
 &=\sum_{A\subsetneq E(C_n)}\lambda^{|A|}\\
 &=(1+\lambda)^n-\lambda^n\\
 &=(1+\lambda)^n(1-p^n).
\end{aligned}
\]

This remains correct for \(n=2\) if \(C_2\) means two parallel edges:
choosing both creates the graphic-matroid two-cycle, and every other subset
is acyclic. Thus \(Z_H=1+2\lambda\), which equals the displayed formula.

Equivalently, the weighted backbone forest is independent Bernoulli-\(p\)
bond percolation on the rim, conditioned on the rim not being entirely open.
Indeed

\[
\frac{\lambda^{|A|}}{(1+\lambda)^n}
=p^{|A|}(1-p)^{n-|A|}.
\]

This accounts for the full factor \(1-p^n\) in every normalized coefficient;
there is no missing power of \(1+\lambda\).

## 2. Exact coefficient and the cyclic \(n/k\) factor

Fix a set \(S\) of \(k\geq1\) selected apex spokes. List the positive cyclic
gap lengths between successive vertices of \(S\) as

\[
\ell_1+\cdots+\ell_k=n,\qquad \ell_i\geq1.
\]

No two selected vertices are connected by the rim forest if and only if
every one of these \(k\) arcs contains a closed rim edge. For \(k\geq2\)
this statement is immediate. For \(k=1\), the only arc is the whole cycle;
the condition says merely that the rim is not all open, which is already
the conditioning event, so the same formula remains valid. Independence
before conditioning gives the probability

\[
\frac{\prod_{i=1}^k(1-p^{\ell_i})}{1-p^n}.
\]

The factor \(n/k\) is exact, including for periodic compositions. Count
pairs consisting of a \(k\)-subset \(S\) and a distinguished vertex of
\(S\). On one hand each \(S\) gives \(k\) pairs. On the other hand one may
choose the distinguished labeled cycle vertex in \(n\) ways and then choose
the ordered positive gap composition. Hence summing over all \(S\) is
\(n/k\) times the sum over ordered compositions; no freeness of the cyclic
rotation action is being assumed.

The one-gap generating function is

\[
\sum_{\ell\geq1}(1-p^\ell)z^\ell
=\frac{z}{1-z}-\frac{pz}{1-pz}
=\frac{(1-p)z}{(1-z)(1-pz)}.
\]

Consequently, if \(c_{n,k}\) is the coefficient of \(s^k\) in
\(D_n(s)/Z_H\), then for every \(k\geq1\),

\[
\boxed{
c_{n,k}
=\frac nk\frac{(1-p)^k}{1-p^n}
 [z^{\,n-k}]\bigl((1-z)(1-pz)\bigr)^{-k}.
}
\]

For \(k=1\), the bracket is
\(\sum_{j=0}^{n-1}p^j=(1-p^n)/(1-p)\), so \(c_{n,1}=n\), as it must:
one apex spoke can be added to every backbone forest in \(n\) ways. For
\(k=n\), the formula gives \((1-p)^n/(1-p^n)\), the conditional probability
that every rim edge is closed. Both endpoint coefficients therefore match
literal forest counting.

## 3. Closed form from logarithmic coefficient extraction

Write

\[
G(z)=\frac{(1-p)z}{(1-z)(1-pz)},\qquad
A(s)=1+p+(1-p)s.
\]

Using the preceding \(n/k\) formula,

\[
\begin{aligned}
\sum_{k\geq1}c_{n,k}s^k
 &=-\frac{n}{1-p^n}[z^n]\log(1-sG(z)).
\end{aligned}
\]

The logarithm's argument factors as

\[
1-sG(z)
=\frac{1-A(s)z+pz^2}{(1-z)(1-pz)}
=\frac{(1-r_+z)(1-r_-z)}{(1-z)(1-pz)},
\]

where

\[
r_\pm^2-A(s)r_\pm+p=0
\]

means that \(r_++r_-=A(s)\) and \(r_+r_-=p\). Since
\([z^n]\log(1-qz)=-q^n/n\), the positive-degree part is

\[
\frac{r_+^n+r_-^n-1-p^n}{1-p^n}.
\]

Adding the constant coefficient \(1\) yields exactly

\[
\boxed{
\frac{D_n(s)}{Z_H}
=\frac{r_+^n+r_-^n-2p^n}{1-p^n}.
}
\]

The subtraction is \(2p^n\), not \(p^n\): one \(p^n\) comes from the
denominator's logarithm, and the second appears when the constant term is
combined over \(1-p^n\). At \(s=0\), \(r_+=1,r_-=p\), so the numerator is
\(1-p^n\), confirming the normalization.

The expression is polynomial despite the quadratic radicals. If
\(R_m=r_+^m+r_-^m\), then

\[
R_0=2,\quad R_1=A(s),\quad
R_m=A(s)R_{m-1}-pR_{m-2}.
\]

This recurrence also supplies a radical-free exact interpretation of the
closed form and was one of the independent checker's three coefficient
routes.

## 4. Chebyshev roots and their signs

Assume \(0<p<1\). Set

\[
x=\frac{A(s)}{2\sqrt p}
 =\frac{1+p+(1-p)s}{2\sqrt p}.
\]

The quadratic roots are
\(\sqrt p\,(x\pm\sqrt{x^2-1})\), and the standard defining identity for
the Chebyshev polynomial gives

\[
r_+^n+r_-^n=2p^{n/2}T_n(x).
\]

Thus, up to the positive constant \(2p^{n/2}/(1-p^n)\),

\[
\frac{D_n(s)}{Z_H}
\quad\text{is}\quad T_n(x)-p^{n/2}.
\]

Let

\[
\theta=\arccos(p^{n/2})\in(0,\pi/2).
\]

The \(n\) values

\[
x_j=\cos\frac{\theta+2\pi j}{n},
\qquad j=0,\ldots,n-1,
\]

are distinct and satisfy \(T_n(x_j)=p^{n/2}\). They exhaust the roots because
the polynomial has degree \(n\). To see distinctness directly, equality of
two cosines would make their angles congruent modulo \(2\pi\), giving equal
indices, or opposite modulo \(2\pi\), which would require
\(\theta/\pi+j+k\) to be an integer multiple of \(n\); this is impossible
because \(0<\theta/\pi<1/2\). They are simple: writing
\(\phi_j=(\theta+2\pi j)/n\), neither \(\sin\phi_j\) nor
\(\sin(n\phi_j)=\sin\theta\) vanishes, so
\(T_n'(x_j)=n\sin(n\phi_j)/\sin\phi_j\ne0\).

Each \(x_j\in[-1,1]\). Mapping back to \(s\),

\[
s_j=\frac{2\sqrt p\,x_j-(1+p)}{1-p}
\leq-\frac{(1-\sqrt p)^2}{1-p}
=-\frac{1-\sqrt p}{1+\sqrt p}<0.
\]

Hence all \(n\) roots are distinct, real, and strictly negative. The sign
argument is stronger than merely locating \(x_j\) in \([-1,1]\): the value
of \(x\) corresponding to \(s=0\) is
\((1+p)/(2\sqrt p)>1\), so no Chebyshev root can map to a nonnegative
\(s\).

## 5. The cases \(p=0\), \(n=2\), and the strictness boundary

When \(\lambda=p=0\), the rim is absent and the apex graph is a star.
Directly,

\[
\frac{D_n(s)}{Z_H}=(1+s)^n.
\]

The composition formula gives the same answer because

\[
\frac nk[z^{n-k}](1-z)^{-k}
=\frac nk\binom{n-1}{k-1}
=\binom nk.
\]

Thus all \(n\) roots equal \(-1\). Distinctness is lost at \(p=0\), but
real-rootedness and the later Stieltjes argument do not require distinct
roots.

For the optional parallel-edge \(C_2\), literal enumeration gives

\[
D_2(s)=(1+s)^2+2\lambda(1+2s),\qquad Z_H=1+2\lambda.
\]

This agrees with both the composition and closed formulas. For
\(\lambda>0\) it has two distinct negative roots; for \(\lambda=0\) it is
\((1+s)^2\). The \(n/k\) argument is still valid: the two cyclic arcs are
the two labeled parallel rim edges.

The exclusion of \(n=1\) from the strictness statement is necessary. An
edgeless one-vertex backbone has \(D_1(s)=1+s\), only one Stieltjes factor,
and the disjoint marked edges are independent. Thus \(n\geq2\) is the sharp
rank condition for strictness in this family.

The formula does not cover \(p=1\), which would correspond to infinite
\(\lambda\) and makes the displayed normalization singular. The theorem
claims only finite rim activities, so this is not a missing boundary case.

## 6. Why the four-core proof transfers to a cyclic backbone

Section 1 of the forest-backbone proof is forest-specific, but it is used
only to establish the factorization of \(D(s)\). Sections 2 and 3 explicitly
sum over backbone **forest configurations** \(A\) and are algebraic for an
arbitrary finite weighted backbone \(H\). Nothing in those sections assumes
that every edge subset of \(H\) is acyclic.

For each fixed acyclic \(A\subseteq E(H)\), contract its components and let
\(x_C\) be their profile sums. Edges of \(H\setminus A\) are simply absent
in that configuration. The exact four-terminal transfer

\[
T(x)=(1+sx)I+x^2P+x^3Q+x^4R
\]

therefore remains valid. Summing it with the actual weights
\(\lambda^{|A|}\) gives the same \(U,\Gamma,\Omega,T_0\) and the same
identities

\[
U=\frac{n-(\log D)'(s)}s,\qquad
\Gamma=-U'(s),\qquad
\Omega=\frac{U''(s)}2,\qquad
T_0=-(\log D)''(s).
\]

The use of \(n\) here is justified by
\(D'(0)/D(0)=n\): a single apex spoke is compatible with every backbone
forest and has \(n\) possible endpoints.

The cycle result supplies precisely the only missing input to Section 4.
Because \(D_n(0)=Z_H>0\), its degree is \(n\), and all roots are negative,
there exist \(x_i>0\) such that

\[
D_n(s)=Z_H\prod_{i=1}^n(1+s x_i),
\qquad \sum_i x_i=n.
\]

For \(p=0\), all \(x_i=1\); repeated factors cause no problem. Substitution
into the already audited Stieltjes identities gives

\[
UT_0-\Omega=\sum_{i\ne j}\alpha_i\tau_j>0
\]

when \(n\geq2\), since every \(\alpha_i,\tau_i\) is positive. The second
bracket is nonnegative. Therefore the exact marked Rayleigh formula

\[
\frac{EF-AC}{D^2abcd}
=2(UT_0-\Omega)
 +(a+b)(c+d)(\Gamma^2+U^2T_0-2U\Omega)
\]

is strictly positive when \(abcd>0\) and \(n\geq2\). If a row factor
vanishes, the corresponding marked edge has a leaf endpoint and the
Rayleigh difference is zero. For positive marked-edge activities,

\[
\operatorname{Cov}(1_e,1_f)
=-\frac{w_ew_f(EF-AC)}{Z(w_e,w_f)^2},
\]

so the two marked indicators are negatively correlated, strictly under the
stated condition.

There is no hidden reuse of forest-backbone independence, Gaussian
covariance, or determinant structure in this transfer. The cycle-specific
Chebyshev calculation replaces Section 1 completely; Sections 2--4 then
apply verbatim.

## 7. Independent exact checker

The standalone checker and report are
forest_cycle_uniform_apex_disjoint_pair_k_independent.py and
forest_cycle_uniform_apex_disjoint_pair_k_independent_results.json. The
checker imports no author or forest-backbone helper.

Its apex route retains all \(n\) rim vertices and the apex in a literal
connectivity-partition DP. Each rim or spoke edge is skipped or joined, and
a join is rejected exactly when it closes a cycle. For 32 cases
\(2\leq n\leq9\) and

\[
p\in\{0,1/5,1/2,4/5\},
\]

the complete normalized coefficient vector agrees exactly among three
independent descriptions:

1. the literal all-vertex forest DP;
2. the cyclic-composition coefficient formula; and
3. the radical-free power-sum recurrence.

For every \(p>0\) case, an exact rational Sturm sequence finds exactly \(n\)
distinct negative roots and verifies square-freeness. Every \(p=0\) case
equals the binomial coefficient vector of \((1+s)^n\).

A second literal DP retains all \(n+4\) vertices of the marked graph and
computes \(A,E,F,C\) by inserting the two marked edges in all four subsets.
Nine cases cover \(2\leq n\leq6\), \(p=0\), rational positive \(p\), rational
unequal row factors, and two zero-row boundaries. All four coefficients
agree with an independently reconstructed logarithmic-derivative/four-core
formula. All seven positive-row cases have a strictly positive exact
Rayleigh difference; both zero-row cases have exact equality. The two
Stieltjes brackets are also checked directly and are nonnegative in every
case.

These finite checks corroborate the derivation; the cyclic composition and
Chebyshev arguments prove the unbounded statement.

## 8. Verdict and scope

Every proposed normalization and algebraic transition checks out:

- \(Z_H=(1+\lambda)^n(1-p^n)\) is exact;
- the cyclic \(n/k\) factor is a valid pointed-subset double count;
- the coefficient, quadratic-root, recurrence, and Chebyshev forms agree;
- all roots are negative, with the correct coalescence at \(\lambda=0\);
- the parallel-edge \(n=2\) extension is valid;
- \(n\geq2\) is exactly the strictness threshold; and
- the four-core identity uses no hidden forest assumption after the apex
  factorization is supplied.

The theorem remains restricted to an equal-activity cycle, the uniform
profile, four proportional spoke rows, and exactly the two specified
disjoint marked edges. It does not establish real-rootedness for a
nonuniform cycle, an arbitrary cyclic backbone, nonproportional spokes, a
whole matching, strong Rayleigh, or general forest negative correlation.
