# Independent audit: disjoint marked pair over a weighted forest backbone

3 October 2026 UTC. **PASS, subject to the precise proportional-profile and
coordinate-conditioning scope stated below.** I read the complete proof and
checker, reran the checker, independently reconstructed the determinant,
nilpotent-transfer, logarithmic-derivative, Stieltjes, and Rayleigh algebra,
and ran a separate all-vertex exact countersearch. I found no mathematical
gap or counterexample. Historical novelty and external specialist review are
not certified.

The audited proof is
forest_disjoint_rank_one_attachment_forest_backbone_proof.md. Its graph has
a finite weighted forest $H$, a nonnegative profile $\beta_j$, four new
vertices whose spoke weights are respectively
$a\beta_j,b\beta_j,c\beta_j,d\beta_j$, and exactly two marked mutual edges
$e=u_1u_2$, $f=u_3u_4$. The argument does not cover a cyclic backbone,
nonproportional spoke fields, other edges incident to the new vertices, or
negative association of more than this marked pair.

## 1. Tree covariance and the apex polynomial

Put $p_h=w_h/(1+w_h)$ for each backbone edge. Root every component of
$H$, take independent unit Gaussians at the roots, and recursively set

\[
Y_v=\sqrt{p_h}Y_{\operatorname{par}(v)}
    +\sqrt{1-p_h}\,\epsilon_v.
\]

Since every activity is finite, $p_h<1$; the triangular innovation map has
positive diagonal and the covariance matrix $C$ is positive definite. Its
entries are products of $\sqrt{p_h}$ along tree paths, and entries in
different components vanish.

For a selected vertex set $S$, cutting an edge $h$ gives a covariance
block matrix with cross block $\sqrt{p_h}\,uv^T$. Its Schur complement is

\[
\det C_S=\det A\det B
 \{1-p_h(u^TA^{-1}u)(v^TB^{-1}v)\},
\]

so the determinant is separately affine in every $p_h$. At every
$\{0,1\}$ corner, $C_S$ is block diagonal with one all-ones block for
each open percolation component met by $S$. Its determinant is one exactly
when no such component contains two selected vertices, and zero otherwise.
Multiaffine interpolation therefore proves

\[
\det C_S=\Pr(\text{the vertices of }S
                  \text{ lie in distinct open components}).
\]

This is also exactly the condition for adding the corresponding spokes from
one apex without making a cycle. The principal-minor expansion consequently
gives

\[
\frac{D(s)}{Z_H}=\det(I+sB^{1/2}CB^{1/2})
 =\prod_{i=1}^k(1+s x_i),\qquad x_i>0,
\]

where $B=\operatorname{diag}(\beta)$ and
$k=|\{j:\beta_j>0\}|$. The rank statement is valid even with zero profile
entries because a positive principal submatrix of $C$ is positive
definite. The coefficient of $s$ on both sides is
$A_0=\sum_j\beta_j$, hence $\sum_i x_i=A_0$. No cyclic-backbone
real-rootedness result is being smuggled into this step.

## 2. Four-core transfer and its normalization

Fix a backbone forest $A$, contract its components, and let
$x_C=\sum_{j\in C}\beta_j$. Spokes from a component to one new vertex are
parallel graphic-matroid elements, so their weights add to the literal
aggregate $a x_C,b x_C,c x_C,d x_C$. A component cannot contribute two
spokes to an already connected core block. Thus its exact four-core transfer
is

\[
T(x)=d(x)I+x^2P+x^3Q+x^4R,\qquad
d(x)=1+sx,\quad s=a+b+c+d.
\]

Here $P,Q,R$ perform respectively one, two, or three joins. Direct join
counting gives

\[
PQ=QP=3sR,\qquad P^3=6s^2R,\qquad
PR=QR=Q^2=R^2=0.
\]

The $P^3$ coefficient is the weighted four-vertex tree sum
$abcd\,s^2$, multiplied by the $3!$ join orders. This verifies the only
nontrivial combinatorial constant in that relation.

Put

\[
\alpha=x^2/d,\quad b_x=x^3/d,\quad
\chi=x^4(1-sx)/d^3.
\]

The finite logarithm is

\[
\log(T/d)=\alpha P+b_xQ-\tfrac12\alpha^2P^2+\chi R.
\]

To audit the denominators in the proof, sum this expression over components
and write

\[
\mathcal A=\sum\alpha,\quad \mathcal B=\sum b_x,\quad
\mathcal C=\sum\alpha^2,\quad \mathcal K=\sum\chi.
\]

Expansion of the commuting nilpotent exponential gives the $e_3$ term

\[
\mathcal B+s(\mathcal A^2-\mathcal C)=G+s\mathcal A^2,\qquad
G=\sum_C\frac{x_C^3}{d(x_C)^2},
\]

because $b_x-s\alpha^2=x^3/d^2$. Its $e_4$ term is

\[
\mathcal K-\mathcal A^2+\mathcal C
\quad+3s\mathcal A\mathcal B+s^2\mathcal A^3
\quad-3s^2\mathcal A\mathcal C
 =2H-\mathcal A^2+3s\mathcal A G+s^2\mathcal A^3,
\]

where

\[
\mathcal K+\mathcal C=\sum_C(\chi+\alpha^2)
 =2\sum_C\frac{x_C^4}{d(x_C)^3}=2H.
\]

This independently recovers formula (6), including the terms most vulnerable
to a missing denominator or factor two.

Normalize $w_A\prod_Cd(x_C)$ by $D(s)$. Averaging the preceding formula
produces

\[
U=\mathbb E\mathcal A,\qquad
\Gamma=\mathbb E G+s\operatorname{Var}(\mathcal A),
\]

and

\[
\Omega=\mathbb E H-\tfrac12\operatorname{Var}(\mathcal A)
 +\tfrac{3s}{2}\operatorname{Cov}(\mathcal A,G)
 +\tfrac{s^2}{2}\operatorname{Cum}_3(\mathcal A).
\]

Substitution shows that the averaged $e_4$ coefficient is exactly
$2\Omega-U^2+3sU\Gamma+s^2U^3$; in particular, none of the variance,
covariance, or third-cumulant terms has been discarded or assigned an
unproved sign.

## 3. Logarithmic derivatives and the Stieltjes certificate

For a fixed $A$, let
$W_A=\sum_Cx_C/d(x_C)$. Then
$U_A=(A_0-W_A)/s$. Differentiation under the tilted finite sum gives

\[
U=(A_0-(\log D)')/s,\qquad
U'=-\Gamma,\qquad U''/2=\Omega.
\]

Consequently

\[
T_0:=U-s\Gamma=-(\log D)''.
\]

These are exact identities, not sign assumptions. Differentiating
$T_0=U+sU'$ also gives
$2\Omega=2\Gamma/s-(\log D)'''/s$, matching the checker's independent
third-derivative calculation.

The forest factorization now yields, term by term,

\[
\alpha_i=\frac{x_i^2}{1+sx_i},\quad
\gamma_i=\frac{x_i^3}{(1+sx_i)^2},\quad
\tau_i=\frac{x_i^2}{(1+sx_i)^2},\quad
\eta_i=\alpha_i\tau_i.
\]

Thus $U=\sum_i\alpha_i$, $\Gamma=\sum_i\gamma_i$,
$T_0=\sum_i\tau_i$, $\Omega=\sum_i\eta_i$, and
$\gamma_i^2=\alpha_i^2\tau_i$. Direct expansion gives

\[
UT_0-\Omega=\sum_{i\ne j}\alpha_i\tau_j\geq0
\]

and

\[
\Gamma^2+U^2T_0-2U\Omega
=\sum_{i\ne j}\alpha_i^2\tau_j
 +2\sum_{i<j}\gamma_i\gamma_j
 +2\sum_{\substack{i<j\\k\notin\{i,j\}}}
       \alpha_i\alpha_j\tau_k\geq0.
\]

I checked the repeated-index cancellation explicitly: the diagonal part is
$\gamma_i^2+\alpha_i^2\tau_i-2\alpha_i\eta_i=0$, and the two-index
$2\alpha_i\alpha_j(\tau_i+\tau_j)$ terms cancel against the off-diagonal
part of $2U\Omega$. The displayed sums contain every surviving monomial.

## 4. Marked coefficients, Rayleigh sign, and strictness

Let $p=a+b$, $q=c+d$, $u=ab$, $v=cd$, and set

\[
H_3=\Gamma+sU^2,\qquad
H_4=2\Omega-U^2+3sU\Gamma+s^2U^3.
\]

Deletion/contraction of each marked pair in the exact four-core expression
gives

\[
\begin{aligned}
A/D&=1+(pq+u+v)U+(uq+vp)H_3+uvH_4,\\
E/D&=1+(pq+v)U+vpH_3,\\
F/D&=1+(pq+u)U+uqH_3,\\
C/D&=1+pqU.
\end{aligned}
\]

I expanded these four polynomials independently. All constant and linear
terms cancel from $EF-AC$ except through $uv=abcd$, and the exact result
is

\[
\frac{EF-AC}{D^2abcd}
=2(UT_0-\Omega)
 +pq(\Gamma^2+U^2T_0-2U\Omega).
\]

The two Stieltjes sums prove nonnegativity. If $a,b,c,d>0$ and $k\ge2$,
the first sum is already strictly positive. If $k\le1$, both sums vanish.
If a row factor is zero, the corresponding marked edge has a leaf endpoint
and is a bridge, so equality is also correct. The all-zero-spoke case is
separate and immediate, avoiding division by $s$.

For positive marked activities $z_e,z_f$, the four-mass law
$Z=A+Ez_e+Fz_f+Cz_ez_f$ gives

\[
\operatorname{Cov}(1_e,1_f)
=-\frac{z_ez_f(EF-AC)}{Z^2}.
\]

The sign and normalization therefore match the claimed negative
correlation.

## 5. Conditioning and boundary cases

Coordinate conditioning of backbone edges is legitimate. Contract every
required-present edge, add the profile weights within each contracted
component, and delete every required-absent edge. Because $H$ is a forest,
no remaining backbone edge becomes a loop through an alternative path. The
fixed present-edge activity product is a common positive factor. Parallel
spokes created by contraction aggregate by summing their weights, so the
proportional profile is preserved. The strictness rank becomes the number of
contracted components with positive profile sum, exactly as stated.

For precision, “arbitrary positive-probability conditioning of $H$ edges”
should be read as arbitrary **coordinate/cylinder conditioning** (fixing any
chosen edge indicators present or absent). The contraction-deletion argument
does not prove preservation after conditioning on an arbitrary non-cylinder
event such as a parity event. This is a wording clarification, not a defect
in the standard conditional-negative-association usage or in the proof's
explicit contraction/deletion claim.

Zero backbone activities cause no analytic problem: then $p_h=0$, while
$C$ remains positive definite. A zero-activity edge cannot be conditioned
present with positive probability. Required-present contraction can reduce
multiple positive original profile vertices to one positive component, and
the asserted conditioned equality criterion correctly detects this case.

## 6. Exact checker inspection and adversarial countersearch

The independent source and its generated compact report are
forest_disjoint_rank_one_attachment_forest_backbone_k_independent.py and
forest_disjoint_rank_one_attachment_forest_backbone_k_independent_results.json.

I inspected all of
forest_disjoint_rank_one_attachment_forest_backbone_exact.py and the
imported forest_records/conditioned routines. The determinant routine is
exact Gaussian elimination over Fraction. The rational kernel used in the
checker is nonsymmetric. When all path probabilities are positive, it is
diagonally similar on every tree component to the symmetric Gaussian
covariance. A zero-probability edge makes that diagonal scaling singular,
but ordering vertices across the zero edge makes the kernel block triangular,
so the principal-determinant identity still follows (also by continuity).
The checker separately compares those determinants with literal
percolation probabilities. The percolation routine exhausts every backbone
subset and checks every principal minor. The four-terminal routine enumerates
all spoke subsets and rejects precisely those that join an already connected
core block. The literal routine instead keeps every original graph vertex
and tests cycles by union-find, so its two recorded cases do not rely on the
contracted transfer formula.

The checker also retains the full variance, covariance, and third cumulant,
compares $D,D',D'',D'''$, verifies both nonnegative brackets and the exact
Rayleigh identity, and checks every partial coordinate conditioning in its
five cases. I reran it unchanged; it exited zero. All 324 positive-probability
partial conditionings passed, including 26 and 242 strict conditionings in
the two larger connected examples, all equality conditionings for the
one-profile and zero-row examples, rational weights, disconnected
backbones, and the two literal original-graph comparisons.

As a separate countersearch, I used an all-vertex connectivity-partition DP
that never contracts the backbone into the proof's $P,Q,R$ transfer and
does not import the author checker. Each ordinary edge was processed by an
exact skip/join update; after all unmarked edges, the two marked edges were
inserted in all four subsets and rejected only on a literal cycle.

The exhaustive run covered every labeled forest backbone on one, two, and
three vertices, profiles in $\{0,1,2\}$, row factors in $\{0,1\}$, and every
partial backbone coordinate conditioning. It checked 16,608 exact cases:
632 strict and 15,976 equality cases. Every Rayleigh difference was
nonnegative and strict exactly under the contracted-component criterion.
A further 1,200 seeded exact-rational cases used random forest backbones on
one through five vertices, rational edge weights, rational profiles and row
factors (including zeros), and random coordinate conditionings. Again no
counterexample or strictness mismatch occurred; the smallest positive
Rayleigh value encountered was $29/129600$.

These finite checks are corroboration, not the source of the universal
claim. The universal sign follows from the determinant factorization and the
two explicit Stieltjes expansions above.

## 7. Verdict and scope boundary

The proof is internally complete for the stated forest-backbone,
rank-one/proportional-spoke, disjoint-marked-pair configuration. The
determinantal factorization, all transfer constants, mixture cumulants,
logarithmic derivatives, Rayleigh cancellation, positivity, equality cases,
and coordinate-conditioning closure check out. I found no mathematical gap.

The result must not be restated for cyclic backbones, independently weighted
spokes, arbitrary events used for conditioning, other marked-edge
placements, a whole matching, strong Rayleigh, or the general forest
negative-correlation conjecture. Those statements do not follow from this
audit.
