# Independent audit: regular three-state ML10 cycle surplus

2 October 2026. Auditor: `/root/antivoter_audit`.

**Verdict: PASS within the stated finite-host scope.** I independently
checked the full written proof
`continuation_20261002_regular3_cycle_surplus_proof.md`, the full-assignment
enumerator, the cycle-surplus generator, and the root-free transfer
regenerator and their saved exact reports. I found no mathematical gap.
This is an internal proof audit, not an assertion of historical novelty or
external acceptance. It does not settle unrestricted Sidorenko.

## 1. Domain coverage and normalization

Write (P=W/3), so (P) is symmetric, nonnegative and has row sum (s).
For off-diagonal entries (a,b,c), putting

\[
\alpha=s-a-b-c
\]

gives (P=\alpha I+aS_{01}+bS_{02}+cS_{12}) exactly. If
\(\alpha\ge0\), the four coefficients are nonnegative. If
\(\alpha=-u<0\), the diagonal constraints give
\(a,b,c\ge u\), and

\[
P=uK_3+(a-u)S_{01}+(b-u)S_{02}+(c-u)S_{12}.
\]

Here (I+K_3=S_{01}+S_{02}+S_{12}\). This proves both-cone coverage
without an unproved classification of the regular polytope. Relabeling
the three states induces every permutation of the three transpositions,
so sorting the coefficients loses no host. The factor two in cone T
is a coordinate scaling only. The author's two row-sum formulas and all
nine matrix-entry formulas agree with these generator matrices.

ML10 has ten vertices and fifteen edges. Equal atom weights (1/3) and
(W=3P) give (F=t(ML10,W)=3^5\operatorname{hom}(ML10,P)). This factor
is essential and is correct. Cycle densities are \(\operatorname{tr}P^k\),
so the eigenvalues in the statement are those of (P), not (W).

## 2. Centered moments

Each transposition restricts to a reflection on the two-dimensional
mean-zero subspace, their sum is zero, and (K_3\) restricts to (-I\).
For reflection coefficients (\beta,\gamma,\delta\), the squared
eigenvalue of their sum is

\[
\beta^2+\gamma^2+\delta^2-\beta\gamma-\beta\delta-\gamma\delta.
\]

In the ordered cones this is (R=B^2+BC+C^2\) or (4R\). Therefore
the centered eigenvalues are (D\pm\sqrt R\) in I and
(-D\pm2\sqrt R\) in T. Expanding their fourth and sixth powers gives
exactly the author's formulas (7). I also independently computed the
three-by-three polynomial matrix powers and obtained the same complete
cycle polynomials. All signs, normalizations and degenerate eigenvalue
cases are consistent.

## 3. Third complete polynomial route

The new checker
`regular3_cycle_surplus_ant_independent_check.py` imports no author
module. It uses a third derivation, distinct from both the author's
59,049-assignment enumeration and its nine-state transfer:

\[
\operatorname{hom}(ML10,P)
=\sum_{x\in\{0,1,2\}^5}\prod_{j=0}^4
\left[\sum_{y=0}^2P_{x_{j-1},y}P_{x_j,y}P_{x_{j+1},y}\right].
\]

Indices are cyclic. The five right vertices are integrated independently
after summing every one of the 243 left assignments. Their ten possible
unordered neighbor triples have exact cubic polynomials. The 243
assignments group into 39 identical products; every label is still
included, so no root-fixing or label-transitivity assumption is made.

The checker independently builds the cones from the actual generator
matrices. It encodes polynomial exponents as base-16 integers rather
than using the author's tuple representation. Every product has total
degree at most 15, so digit addition has no carry. Signed polynomial
addition retains all negative coefficients until the final sign check.

Its saved report `regular3_cycle_surplus_ant_independent_checks.json`
certifies the following exact comparisons:

| Check | Cone I | Cone T |
|---|---:|---:|
| Complete density coefficients matched | 816/816 | 816/816 |
| Nonzero unrefined gap coefficients matched | 790/790 | 790/790 |
| Direct matrix cycle polynomials matched | Yes | Yes |
| All nonzero scaled-surplus coefficients matched | 744/744 | 741/741 |
| Smallest nonzero scaled-surplus coefficient | 12,394 | 108,620 |
| Exact minimum sixth-cycle coefficient ratio | (265/18\) | (265/18\) |

The scaled polynomial is

\[
L=18(F-s^{15})-90s^{11}E_4-265s^9E_6.
\]

Every one of its nonzero coefficients is a positive integer. The
checker compares the entire coefficient dictionaries, not only their
counts or numerical evaluations. It also checks every denominator-present
ratio and every denominator-absent coefficient in
\(F-s^{15}-5s^{11}E_4\). The indicated limiting monomials are valid;
the checker records the additional tied limiting monomials too. Thus
(265/18\) is indeed the largest coefficient certified by this exact
coefficientwise subtraction procedure. This does not prove it is the
best mathematical constant on the host domain.

No numerical tolerances, eigenvalue solvers or optimizer output enter
these checks. The author's older invalid root-fixed calculation is not
an input to this checker or to the audited theorem.

## 4. Equality, sharpness and the sixth-constant witness

The inequality follows on both nonnegative cones, including boundaries.
For (s>0\), the positive fourth-cycle contribution is strict unless
both centered eigenvalues vanish. Since (P\) is selfadjoint, vanishing
centered operator means (P=sJ_3/3\), hence (W\) is constant. If (s=0\),
nonnegativity forces (W=0\). The equality statement is correct.

I independently counted the simple cycles of the literal ladder by DFS:
there are five four-cycles and fifteen six-cycles. A centered regular
perturbation has zero contributions whenever the selected edge subgraph
has a degree-one vertex. There is no selected subgraph of fewer than
four edges without such a vertex. At order four only the five four-cycles
survive. At order five, bipartiteness and simplicity again preclude a
nonzero contribution. This proves the fourth coefficient's leading
sharpness independently of the coefficient certificate.

For an explicit perturbation, set (W=J_3+\varepsilon(3I-J_3)\), valid
for sufficiently small positive or negative \(\varepsilon\). Then
\(s=1\), both centered eigenvalues equal \(\varepsilon\), and the
checker recovers the exact polynomial

\[
F=1+10\varepsilon^4+30\varepsilon^6+10\varepsilon^7
+90\varepsilon^8+100\varepsilon^9+166\varepsilon^{10}
+180\varepsilon^{11}+110\varepsilon^{12}+30\varepsilon^{13}
+2\varepsilon^{15}.
\]

Thus a fourth-cycle coefficient exceeding five fails near the constant
host, regardless of any fixed sixth coefficient. The odd seventh term
also explains why the sixth coefficient fifteen can fail on a negative
perturbation.

For the stated exact witness (W_{ii}=49/50\), (W_{ij}=101/100\), the
checker evaluates the whole polynomial at
((A,B,C,D)=(49/300,0,0,1/100)\) in cone T and obtains exactly the
author's density and negative gap:

\[
F-\left(1+10/100^4+30/100^6\right)
=-\frac{45549178945150001}{500000000000000000000000000000}.
\]

The gap above the proved (265/18\) threshold is instead

\[
\frac{2090057389493649991}{4500000000000000000000000000000}>0.
\]

This is a valid counterexample to the stronger quantitative bound and
is not a Sidorenko counterexample.

## 5. Scope and remaining external questions

The proof establishes the exact theorem for nonnegative symmetric
regular three-by-three kernels on three equal-measure atoms, and for
graphon blow-ups of those kernels. It permits unequal diagonal entries.
It does not cover unequal atom measures, nonregular three-state kernels,
arbitrary larger hosts or unrestricted graphons. I found no hidden
extension of the scope in the written argument.

The ladder transfer is prior art and is correctly treated as such.
Historical novelty of the resulting quantitative inequality remains
unverified. A bounded source search cannot certify novelty. This audit
does not upgrade that caveat or claim a solution to the famous open
unrestricted problem. Within its written scope the analytic reduction
and complete exact algebra pass.
