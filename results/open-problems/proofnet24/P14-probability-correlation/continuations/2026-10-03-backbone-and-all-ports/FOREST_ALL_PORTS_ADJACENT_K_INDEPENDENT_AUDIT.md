# Independent audit: adjacent edges in a rank-one attachment with any number of common neighbors

3 October 2026. **PASS within the precise proportional-profile configuration.**
I read the complete proof, its full exact checker and report, and the imported
literal three-spoke helper. I independently derived all four marked-edge
coefficients, the outer-edge terms, the component-mixture normalization, and
the log-concavity closure. I reran the author's complete checker to a separate
output and regenerated additional original-graph coefficients by a different
connectivity DP. No mathematical gap was found. Historical novelty and human
peer review are not certified.

The audited proof is
[`forest_adjacent_rank_one_attachment_all_ports_proof.md`](forest_adjacent_rank_one_attachment_all_ports_proof.md).
Its theorem permits an arbitrary weighted backbone \(H\), arbitrarily many
nonzero profiles \(\beta_j\geq0\), three new vertices with spokes
\(a\beta_j,b\beta_j,c\beta_j\), two marked edges along their path, and an
optional outer edge of activity \(\rho\geq0\). All ordinary unrooted-forest
weights are products of edge activities. The three new vertices have no other
incident edges. These restrictions are necessary to the proof; arbitrary
marked positions and nonproportional individual spoke fields are not covered.

## 1. Why reversing the roles removes the port-count restriction

Fix one actual backbone forest \(A\), and contract each of its components.
If a component \(C\) has profile sum \(x_C=\sum_{j\in C}\beta_j\), its remaining
spokes to the three new vertices have aggregated weights
\(a x_C,b x_C,c x_C\). Two spokes from the same component to the same new
vertex would form a cycle; one spoke can be chosen in any of the original
ways, and its weights sum to the indicated aggregate. Different core
vertices can be joined through this terminal exactly as in a literal
three-spoke star. This is a weighted forest bijection. It does not replace
the random backbone components by independent objects.

The original three attachment vertices are now a three-vertex core. The
number of contracted backbone components is unrestricted. Thus the three
core connectivity states needed for the nilpotent transfer are independent
of the original number of common-neighbor profile entries.

Put \(s=a+b+c\), \(d(x)=1+sx\),
\(\alpha(x)=x^2/d(x)\), and \(\gamma(x)=x^3/d(x)^2\). The terminal transfer
is \(T(x)=d(x)I+x^2P+x^3Q\), with
\(P^2=2sQ\), \(PQ=QP=Q^2=0\). In particular

\[
d(x)e^{\alpha(x)P+\gamma(x)Q}
=d(x)I+x^2P+d(x)(\gamma(x)+s\alpha(x)^2)Q
=T(x).
\]

The last equality uses
\(d(\gamma+s\alpha^2)=x^3(1+sx)/d=x^3\); it checks the sometimes delicate
second-order normalization in this exponential representation.

## 2. The mixture variance and the exact apex inequality

For a fixed backbone forest let
\(D_A=\prod_Cd(x_C)\), \(U_A=\sum_C\alpha(x_C)\), and
\(G_A=\sum_C\gamma(x_C)\). Normalize the weights
\(w_A D_A\) by \(D=\sum_Aw_A D_A>0\), and set

\[
U=\mathbb E U_A,\qquad
\Gamma=\mathbb E G_A+s\operatorname{Var}(U_A).
\]

The mixture's \(P\)-coefficient is \(U\), and its \(Q\)-coefficient is
\(\mathbb E G_A+s\mathbb E U_A^2\). This equals
\(\Gamma+sU^2\), so the complete averaged transfer is
\(D e^{UP+\Gamma Q}\). In particular the variance has been retained with
the correct sign and factor. Nonnegativity gives \(U,\Gamma\geq0\).
Moreover \(U>0\) exactly when \(\sum_j\beta_j>0\), since every forest
component list then has at least one positive profile sum.

The scalar \(D(s)\) is the actual ordinary forest partition of \(H\) with
one new apex and apex activities \(s\beta_j\). For each fixed \(H\)-forest,
at most one apex spoke is accepted from a component; its optional choices
have weight \(1+sx_C\). This proves the identity without rooted determinant
weights.

Theorem 4.1 and Lemma 2.2 of Anari–Liu–Oveis Gharan–Vinzant,
[*Log-Concave Polynomials III*](https://arxiv.org/pdf/1811.01600), apply to
the coefficient-one homogeneous independent-set polynomial. Setting its
dummy variable to one, fixing the backbone coordinates, and specializing
apex activities linearly gives this ordinary partition. Thus
\((\log D)''(s)\leq0\). No factorial-normalized polynomial, edgewise Hessian
sign, or unproved forest negative-correlation theorem is substituted.

Let \(A_0=\sum_j\beta_j\), constant over all backbone forests, and
\(W_A=\sum_Cx_C/d(x_C)\). For \(s>0\), termwise algebra gives

\[
U_A=(A_0-W_A)/s,\quad
U_A/s-G_A=\sum_Cx_C^2/[s d(x_C)^2],
\]

\[
(\log D)''=-\mathbb E\sum_Cx_C^2/d(x_C)^2
              +\operatorname{Var}(W_A).
\]

Since \(\operatorname{Var}(U_A)=\operatorname{Var}(W_A)/s^2\), these imply
the exact closure

\[
\boxed{U/s-\Gamma=-(\log D)''/s\geq0.}
\]

This argument remains valid for arbitrary topology, cycles, activity fields,
and dependence among backbone components. The \(s=0\) case is separated
before any division.

## 3. Independent derivation of all four coefficients, including the outer edge

Write \(\ell=ab+ac+bc\), \(j=abc\), and use formal activities \(p,q\) for
the two marked path edges; the outer edge has activity \(\rho\). The ordinary
core forest partition is

\[
S=1+p+q+\rho+pq+p\rho+q\rho.
\]

Its \(P\)-coefficient is
\(L=\ell+p c(a+b)+q a(b+c)+\rho b(a+c)\), and its \(Q\)-coefficient is
\(j\): only the initially all-separated core contributes the latter.
Consequently the full partition is

\[
Z(p,q)=D[S+LU+j\Gamma+s jU^2].
\]

Reading its coefficients gives, independently of the marked activity values,

\[
\begin{aligned}
A/D&=1+\rho+[ab+ac+bc+\rho b(a+c)]U+abc\Gamma+sabcU^2,\\
E/D&=1+\rho+c(a+b)U,\\
F/D&=1+\rho+a(b+c)U,\\
C/D&=1.
\end{aligned}
\]

The last line is independent of \(\rho\) because both marked edges already
connect the three core vertices; selecting the outer edge would complete
a forbidden triangle. The \(p\rho,q\rho\) terms contribute precisely the
constant \(\rho\) inside \(E/D,F/D\), and no additional terminal-joining
term, because those two-edge core forests are connected.

Expanding \(EF-AC\) gives

\[
\boxed{R=D^2\{\rho(1+\rho)
       +ac[(1+2\rho)U+acU^2-b\Gamma]\}. 
\]

Specifically the constant difference is \((1+\rho)^2-(1+\rho)
=\rho(1+\rho)\). The linear \(U\)-difference is
\((1+\rho)[c(a+b)+a(b+c)]-[\ell+\rho b(a+c)]
=ac(1+2\rho)\). The quadratic difference is
\(ac[(a+b)(b+c)-sb]U^2=a^2c^2U^2\). Thus both the \(\rho^2\) and \(2\rho\)
factors are verified directly rather than inferred by continuity from the
zero-outer-edge case.

The apex bound then gives

\[
R\geq D^2\{\rho(1+\rho)
   +ac[((a+c)/s+2\rho)U+acU^2]\}\geq0.
\]

For positive marked activities \(w_e,w_f\), the literal four-mass law yields
\(\operatorname{Cov}(1_e,1_f)=-w_ew_fR/Z^2\). This confirms the covariance
sign and normalization. Strictness is exactly the condition in the theorem:
\(\rho>0\), or \(ac>0\) and \(\sum\beta_j>0\). If neither holds, the exact
formula itself vanishes. When \(s=0\), all three columns vanish and the
separate triangle calculation gives \(R=D^2\rho(1+\rho)\), so it agrees
with the same criterion without invoking \(U/s\).

## 4. Conditioning and fields

Required-present backbone edges form an acyclic set under any conditioning
of positive probability. Contract them and add their profile weights;
delete required-absent edges. The fixed required-edge activity product is
a common positive scalar, and the remaining model has precisely the same
proportional-profile form. Backbone loops and parallel edges are handled by
ordinary graphic-matroid cycle rejection. All derivations therefore apply
to the conditioned law, and arbitrary positive backbone fields are allowed.

Fields on the three mutual edges merely change \(w_e,w_f,\rho\). Common
column or profile changes preserve the hypothesis. Independent arbitrary
spoke fields can destroy proportionality and are not covered. Conditioning
the outer edge absent sets \(\rho=0\); conditioning it present identifies
the two outer vertices, making the two marked edges parallel, so their
simultaneous occurrence is forbidden and their negative correlation is
immediate. No arbitrary spoke conditioning is claimed.

## 5. Static checker review and independent exact reconstruction

I read the entire
[`forest_adjacent_rank_one_attachment_all_ports_exact.py`](forest_adjacent_rank_one_attachment_all_ports_exact.py)
and its imported `canonical`/`terminal` routines. The latter enumerates all
eight possible spoke subsets and rejects a subset precisely when two chosen
ports are already connected. Its forgetting of a processed terminal is
valid because the backbone component was fully contracted and no later
edge can touch that terminal independently. The original-graph recursive
checker retains all vertices and rejects cycles before adding the marked
subset, so it supplies a separate literal check of this reduction.

The author's apex derivative routine correctly counts selected apex spokes
to obtain \(D,D',D''\) when \(s>0\). It deliberately does not use the
division-by-\(s\) routine at \(s=0\); the report marks that apex comparison
false in the zero-column case. The component formulas still compute the
derivatives there. The recorded seven cases all have positive backbone edge
activities, so a nonempty admissible conditioned-record list indeed has
positive weight. If that generic checker is later extended to zero backbone
activities, positive weight should be checked explicitly rather than only
list nonemptiness; this is not a defect in its existing recorded checks.

I reran the complete author checker to a **separate** output. It exited zero
and the full JSON equals the original report, including all 2440 positive
partial backbone conditionings and every recorded exact rational value.
The rerun files are
[`forest_adjacent_rank_one_attachment_all_ports_k_rerun.py`](forest_adjacent_rank_one_attachment_all_ports_k_rerun.py)
and
[`forest_adjacent_rank_one_attachment_all_ports_k_rerun_results.json`](forest_adjacent_rank_one_attachment_all_ports_k_rerun_results.json).

A genuinely different original-graph reconstruction is
[`forest_all_ports_adjacent_k_independent.py`](forest_all_ports_adjacent_k_independent.py).
It keeps the connectivity partition of **all** backbone and added vertices
through every edge operation; it never calls the author's three-spoke
terminal transfer and never contracts backbone components when calculating
marked-edge coefficients. It calculates all eight mutual-triangle
coefficients, then incorporates \(\rho\) only after this calculation. A
separate all-vertex apex DP constructs the entire polynomial by apex-spoke
degree and evaluates its derivatives faithfully even at \(s=0\).

All eleven additional exact cases passed. They include four, five and six
positive profiles; a nonuniform complete backbone; cyclic backbones;
extra vertices with zero profile; \(0<\rho<1\); backbone contractions;
rational fields and profiles; zero backbone activity; zero middle/outer
columns; all-zero columns and profiles. The checker compares all four
coefficients, the exact Rayleigh identity and lower bound, strictness, and
the literal covariance at three different positive pairs of marked
activities. Record:
[`forest_all_ports_adjacent_k_independent_results.json`](forest_all_ports_adjacent_k_independent_results.json).
These checks support the proof; they do not extrapolate an inequality from
finitely many graphs.

## 6. Primary-source scope and a corrected model distinction

The proof uses established ordinary matroid log-concavity, rather than a
new general negative-dependence theorem. Earlier primary results include
Erickson's
[*Sums of squares and negative correlation for spanning forests of series parallel graphs*](https://arxiv.org/pdf/1008.3660)
and Huang's
[*On Negative Correlation of Arboreal Gas on Some Graphs*](https://arxiv.org/pdf/2311.00965).
The former covers every marked pair in series-parallel graphs; the latter
includes adjacent pairs at sufficiently large fugacity. Neither source
statement, by its scope alone, supplies the present arbitrary-backbone,
all-activity proportional-profile result. Some of its subcases can of
course overlap these known classes.

I reopened the current primary preprint
[*Negative Correlations for Forests and the q<1 Random Cluster Model*](https://arxiv.org/pdf/2610.00549).
Its Proposition 5.7 contains an adjacent-edge result with outer activity
at least one, **in the random-cluster model at fixed \(0<q<1\)**. This must
not be mistaken for an ordinary-forest result at the same activity. The
arboreal limit uses random-cluster activities \(z_e=q\beta_e\); a fixed
finite forest activity has \(z_e\to0\) as \(q\to0\). Thus that lower bound
cannot directly be transported to the present \(\rho\geq1\) forest subcase.
An earlier research-thread suggestion of this overlap was corrected once
the full proposition's model and normalization were read.

A bounded search for a primary vertex-cloning or proportional-neighborhood
theorem did not identify this exact all-profile statement. That absence is
not a historical novelty certificate. The transpose observation and the
resulting application of an established log-concavity theorem should be
described as a derived restricted result pending broader literature and
human review.

**Verdict:** the complete all-common-neighbor adjacent marked-pair theorem,
including its optional outer edge and stated conditioning/field closure,
passes this independent analytic and literal exact audit. It removes the
neighbor-count limit for this configuration. It does not solve the general
forest edge negative-correlation or negative-association problem.
