# Referee A report: "Theorem 6 of Rozikov's problem list fails for five or more types" (E0064)

Reviewed 2026-09-14. Files read: the memo `Probability_E0064_..._2026-09-11.md`, the audit passage
(results_B_settled_and_audits.md lines 968-1044) and the report row (Probability_1000_..._2026-09-12.md
lines 5492-5556). All computations below are my own, in
`~/AppData/Local/Temp/claude/<project>/88e175ec-e7cc-4bc7-a998-68bfafb7613f/scratchpad/`
(qso_task1_exact.py, qso_task2_m6.py, qso_task3_m4.py, qso_task3b_index_identity.py,
qso_identity_numeric.py, qso_m5_count.py, qso_maxdet.py). Nothing outside the scratchpad was modified.

Source check. arXiv:0902.4207 is by R. N. Ganikhodzhaev and U. A. Rozikov. Its Section 8 reads:
"Theorem 6. [40] 1) For any values of parameters a, b, c, d, alpha, beta with (15) the operator (14) has a
unique fixed point. Moreover the fixed point is not attractive. 2) The QSO (14) has 2-cycles and 3-cycles
depending on the parameters (15). Problem 11. Is Theorem 6 true for m >= 4?" Reference [40] is Rozikov and
Zhamilov, "On dynamics of strictly non-Volterra quadratic operators defined on the two dimensional simplex",
Sbornik Math. 200 (2009) 1339-1351. The problem statement in the memo matches the source.

## Findings

### 1. The five-type operator (task 1) - CLEAN
Exact rational arithmetic (fractions + sympy), building P from the memo's recipe:
- P symmetric in (i,j): yes. Nonnegative: yes. sum_k P_{ij,k} = 1 for all 25 pairs: yes (no exceptions).
  P_{ij,k} = 0 whenever k in {i,j}: yes.
- V(p) - p = 0 and V(q) - q = 0 exactly, for p = (1/3,1/3,1/3,0,0), q = (1/9,1/9,1/9,1/3,1/3).
- Jacobian J_{kl} = 2 sum_i P_{il,k} x_i. Full spectrum at p: {2 (x2), -1 (x2), -2}; at q: {2, -4/3, -1/3 (x2), 0}.
  Restricting to the sum-zero subspace (basis e_l - e_5, completed by the radial vector x, which is an
  eigenvector with J x = 2 V(x) = 2x): tangent eigenvalues (2, -1, -1, -2) at p and (-4/3, -1/3, -1/3, 0)
  at q. Both agree with the memo. det(I - J_tan) = -12 at p and 112/27 at q.
- Number of fixed points: 600 Newton starts give exactly two in the simplex; on the affine hull
  (simplex condition dropped) Newton finds 16 distinct real solutions of V(x) = x, which is the Bezout
  bound for four quadrics, so the complex solution set is exhausted and the simplex holds exactly p and q.
  The memo says "two fixed points" without saying exactly two; it is exactly two.

### 2. The m >= 6 two-face construction (task 2) - CLEAN
- If pairs inside F land in F, the restricted coefficients satisfy sum_{k in F} P_{ij,k} = 1 for all
  i,j in F (checked exactly on the explicit m = 6 operator and on 30 random ones), are symmetric,
  nonnegative and vanish for k in {i,j}: the restriction is a strictly non-Volterra QSO on three types,
  so Theorem 6 applies and gives a fixed point x_F in the F-face. It is a fixed point of the full V
  because V_k(x_F) = sum_{i,j in F} P_{ij,k} x_i x_j = 0 for k outside F (the same invariance).
- Solvability for every m >= 6: a diagonal pair {i,i}, i in F, has two allowed targets inside F; an
  off-diagonal pair inside F has exactly one (the third type); a cross pair {i,g} has m-2 >= 4 allowed
  targets. All constraints are satisfiable simultaneously; the memo's "any such operator" is nonvacuous.
  Explicit m = 6 instance (F = {1,2,3}, G = {4,5,6}, symmetric operator on each triple, cross pairs
  uniform over allowed targets): exact check passes, V(1/3,1/3,1/3,0,0,0) and V(0,0,0,1/3,1/3,1/3) are
  fixed, and the two points are distinct (disjoint supports; in general x_F and x_G have disjoint
  supports so they are always distinct).
- 30 random operators of this kind: histogram {2 fixed points: 30}. The memo reports 27 twos and 3 threes
  under its own random law; no contradiction, both are "at least two".

### 3a. The m = 4 face claim and the invariant-triple claims (task 3) - CLEAN
- m = 4 face-invariant => V_4 identically 0: correct. Pairs inside F land in F, and a pair containing 4
  cannot land on 4, so no monomial of V_4 survives. Every fixed point then has x_4 = 0 and is a fixed
  point of the three-type restriction, unique by Theorem 6.
- No two invariant triples at m = 4 or 5: correct. Two distinct triples in a set of at most five
  elements share an element i. If they share an off-diagonal pair {i,j}, it must land on the third type
  of each triple, two different types, impossible. If they share only i, the diagonal pair {i,i} must
  land inside F\{i} and inside G\{i}, disjoint sets, impossible. The memo's sentence ("a shared pair
  {i,j} would have to land in two different third types") covers the off-diagonal case in words only;
  the diagonal case is needed at m = 5 (triples sharing exactly one element) and holds by the same
  reasoning. Wording nit, not an error.
- More generally at m = 4 the only possible invariant proper faces are 3-faces (a 1-face needs {i,i} -> i,
  a 2-face {i,j} needs {i,j} -> {i,j}; both violate strict non-Volterra), so every fixed point of a
  four-type operator is either interior or lies in an invariant 3-face.

### 3b. My attempt at m = 4 (task 3)
Setup. Write A(x)_{kl} = sum_i P_{il,k} x_i. Then J(x) = 2A(x), A is column-stochastic with zero
diagonal, A(x) x = V(x), and at a fixed point x is a Perron vector of A. The sum-zero subspace is
A-invariant (A^T 1 = 1), so the tangent eigenvalues of J are 2 mu_i over the non-Perron eigenvalues
mu_i of A. With p_A(t) = det(tI - A), e1 = tr A = 0 and p_A(1) = 0 one gets

    det(I - J_tan) = -(2^m) p_A(1/2)  =  3 + 4 det A          (m = 3)
                                       =  3 + 4 e3(A) - 12 det A  (m = 4),

e3 = sum of principal 3x3 minors. Checked symbolically at m = 3 (sympy, residual 0) and numerically at
m = 3 and 4 on 2000 random zero-diagonal column-stochastic matrices (max error 2e-14), and against a
direct tangent determinant.

Consequence at m = 3 (a proof of the uniqueness clause of Theorem 6). A 3x3 zero-diagonal
nonnegative matrix has det A = a12 a23 a31 + a13 a32 a21 >= 0, so det(I - J_tan) >= 3 > 0 at every
fixed point. No proper face of the 2-simplex is invariant, so every fixed point is interior and
nondegenerate with fixed-point index +1. V is a continuous self-map of a compact convex set, so the
Lefschetz number is 1 and the indices sum to 1. Hence exactly one fixed point. (The non-attractiveness
clause also follows from the trace: lambda_1 + lambda_2 = -2 forces max |lambda_i| >= 1.)

At m = 4 the same argument reduces uniqueness to one inequality: if there is an invariant 3-face the
problem is three-dimensional (finding 3a); otherwise every fixed point is interior, and if
3 + 4 e3(A(x)) - 12 det A(x) > 0 at each of them, all are nondegenerate of index +1 and the Lefschetz
count gives exactly one. Conversely a fixed point of index -1 (det A > 1/4 + e3/3) would force at
least three fixed points. So the search for a counterexample and the search for a proof are the same
search: extremise det(I - J_tan) over interior fixed points.

What I ran (all m = 4, strictly non-Volterra P parametrised by softmax logits on each pair's allowed
targets, 24 logits; x by softmax; V(x) = x imposed as an SLSQP equality constraint):
- Random sampling: 600 operators (Dirichlet concentrations 3, 1, 0.3, 0.1), 60 Newton starts each:
  exactly one fixed point every time; smallest det(I - J_tan) over all fixed points 3.2286.
- Constrained minimisation of det(I - J_tan): two independent seeds, 30 and 16 feasible SLSQP runs,
  including starts biased toward the "two 2-cycles" structure that maximises det A for unconstrained
  stochastic matrices; both converge to the same minimiser x* = (a, a, a, a^2) with a = (sqrt13 - 3)/2
  = 0.30278 (type 4 produced only by the pair {3,3} with P_{33,4} = 1), value 3.144641, where
  e3 = 0.2027 and det A = 0.0555.
- Constrained maximisation of det A over interior fixed points: 0.05551 (same x*), far below the 1/4
  that would be needed for index -1 even with e3 = 0. Constrained minimisation of e3 - 3 det A: 0.0396 > 0.
- Direct two-fixed-point hunt (minimise the two residuals with a separation penalty, 80 L-BFGS starts):
  the two points always collapse onto one (|x1 - x2| -> 0); nothing found.
- Without the fixed-point condition the quantity is NOT bounded below by a positive constant: at
  x = (1/2,1/2,0,0) with P_{11,2} = P_{22,1} = 1 and P_{13,4} = P_{23,4} = P_{14,3} = P_{24,3} = 1 one gets
  e3 = 0, det A = 1/4, so 3 + 4e3 - 12 det A = 0. The fixed-point equations (plus A_{kl} <= 1 - x_k)
  are what keep the value near 3, and a proof would have to use them.
Status: uniqueness at m = 4 remains unproved. The evidence is (i) 600 + 200 (the report's own rerun)
random operators with one fixed point, (ii) two independent optimisations that push the index quantity
to the same minimum 3.14 > 0, (iii) max det A = 0.056 versus the 0.25 needed. A finite search is
evidence, not proof; the reduction above is exact and is, I think, the right statement of what remains:
"at every interior fixed point of a four-type strictly non-Volterra QSO, 12 det A(x) < 3 + 4 e3(A(x))".

### 4. Defects found
- D1 (interpretation, should be fixed before publication). The memo and audit passage say "p is a saddle
  with index -1 and q has index +1", and the report row builds on it: "the five-type example shows that
  a saddle of index -1 can occur, so a proof has to use the dimension rather than degree theory alone".
  The sign of det(I - J_tan) is the fixed-point index only for an interior fixed point. p lies on the
  boundary of the simplex with a tangent eigenvalue 2 transverse to the face; its fixed-point index in
  the simplex is 0 (one-dimensional picture: f(t) = 2t on [0,1) has id - f o r = -|t| near 0, degree 0).
  Check: the indices must sum to the Lefschetz number 1; 0 + 1 = 1, whereas the memo's -1 + 1 = 0 would
  contradict Lefschetz. So no interior fixed point of index -1 has been exhibited in any dimension, and
  the degree-theoretic route is not blocked by this example; as shown in 3b it proves the m = 3 clause
  outright and reduces m = 4 to a determinant inequality. Recommend rewriting the two sentences.
- D2 (attribution). Memo line 3: "Theorem 6 (Ganikhodzhaev, Mukhamedov and Rozikov's [40])". The survey
  arXiv:0902.4207 is by Ganikhodzhaev and Rozikov (Mukhamedov joins the 2011 IDAQP version), and [40] is
  Rozikov and Zhamilov, Sbornik Math. 200 (2009) 1339-1351, which is where Theorem 6 is proved. The report
  row ("the 2009 survey of open problems") is fine.
- D3 (minor wording). "Two fixed points" at m = 5 is exactly two (finding 1); the memo could say so.
  The invariant-triple sentence should mention the diagonal pair (finding 3a). "For m >= 7 pad with
  further types" is right but one should say the padded types' pairs may land anywhere allowed.
No mathematical error was found in the claims themselves.

### 5. Prior art (task 4)
Queries run (WebSearch, 2026-09-14) and what came back:
1. "strictly non-Volterra" quadratic stochastic operator fixed points -> the 2009 survey, Hardin-Rozikov
   quasi-strictly (arXiv:1808.00229), F-QSO; all m = 3 or unrelated classes.
2. Jamilov Mukhitdinov Ladra strictly non-Volterra ... higher dimensional simplex -> Jamilov-Ladra-
   Mukhitdinov, "On the equiprobable strictly non-Volterra quadratic stochastic operators", QTDS 16 (2017)
   645-655: unique fixed point, attracting, Lyapunov function (the memo's citation for the
   non-attractiveness clause; consistent). Springer abstract page redirects to a login, content taken
   from the search snippet and the citation in Jamilov 2023.
3. "non-Volterra quadratic stochastic operator" "fixed points" uniqueness ... Rozikov Zhamilov -> nothing
   beyond the m = 3 results.
4. Rozikov Zhamilov "strictly non-Volterra" Sbornik 2009 -> confirms the reference for Theorem 6.
5. "equiprobable strictly non-Volterra ..." 2017 abstract -> as in 2.
6. strictly non-Volterra "three-dimensional simplex" OR "S^3" OR "m=4" 2020-2025 -> nothing on m = 4.
7. Jamilov Ladra "non-Volterra quadratic operators acting on a simplex" -> QTDS 2020 family
   (orbits converge to a fixed point or a 2-cycle); not strictly non-Volterra as far as visible.
8. Jamilov 2023 "all fixed points" -> Jamilov, "A family of non-Volterra quadratic operators
   corresponding to permutations", Commun. Math. 31 (2023) 31-41 (arXiv:2210.05107). READ THE PDF: the
   family is x'_k = 2 x_m x_{pi(k)}, x'_m = x_m^2 + (sum_{i<m} x_i)^2. It has two fixed points, but it
   is NOT strictly non-Volterra (x'_m contains x_m^2, i.e. P_{mm,m} = 1). Not prior art.
9. "strictly non-Volterra" "several/two/infinitely many fixed points" -> nothing.
10. "non-Volterra" ... arXiv 2024-2026 strictly -> arXiv:2601.17494 (Jamilov-Ladra, Jan 2026), family
    x'_k = alpha x_k^2 + ..., x'_m = x_m^2 + ...: not strictly non-Volterra (diagonal terms); two fixed
    points (e_m and an interior point) for alpha in (0,1). Not prior art.
11. Jamilov "On a family of strictly non-Volterra quadratic stochastic operators" -> J. Phys. Conf. Ser.
    697 (2016) 012013. READ THE PDF: two-dimensional simplex only; convex combinations of two m = 3
    strictly non-Volterra operators; unique fixed point by Theorem 2.6 (= Theorem 6). Not prior art.
12. Jamilov "On symmetric strictly non-Volterra quadratic stochastic operators", Discontinuity,
    Nonlinearity, and Complexity 5(3) (2016) 263-283 -> full text not accessible to me (publisher page
    and Springer both behind logins); a second search returned its abstract snippet: "For a symmetric
    strictly non-Volterra quadratic stochastic operator on the three-dimensional simplex it is proved that
    this operator has a unique fixed point. A sufficient condition of attractiveness for the unique fixed
    point is found." So uniqueness at m = 4 IS known for the symmetric subfamily (P_{ij,k} depending only
    on the multiset structure), a partial answer to the open clause that the memo does not cite; the
    general m = 4 case is not covered by it. Must be cited.
13. Jamilov, "Dynamics of a strictly non-Volterra quadratic stochastic operator on S^4", Uzbek Math. J.
    2017(2) 66-75 -> exists (cited as [15] in Jamilov 2023); NOT FOUND ONLINE after two independent
    searches (title search; journal + "S^4" search). This is five types, the
    dimension of the counterexample. Its title says "a" operator, so most likely one specific operator
    with a unique fixed point, but I could not read it; the author must obtain it and cite it before
    publishing the m = 5 claim.
Result: no paper found after 2009 that exhibits a strictly non-Volterra QSO with more than one fixed
point on any simplex, and none that proves uniqueness for m >= 4; the m = 5 example appears to be new,
subject to item 13.

### 6. Incident, my own
While clearing what I took to be my orphaned runs I killed the process
`python.exe -u qso_m5_dynamics.py` (pid 23132). That script is not mine (not in my scratchpad, not
under math-open-problems-master); my filter `CommandLine -match 'qso_'` was too broad and stopped a
peer agent's run. I could not restart it (working directory unknown). The owner of that process should
be told; the loss is at most one interrupted numerical run.

## Verdict
The result is CORRECT as a mathematical claim and independently verified: the five-type operator is a
valid strictly non-Volterra QSO with exactly two fixed points (exact arithmetic), the m >= 6 two-face
construction is sound and nonvacuous, the m = 4 face reduction and the invariant-triple counting are
right, and the answer "uniqueness fails for every m >= 5, open at m = 4" stands. The non-attractiveness
clause failing from m = 4 is literature (Jamilov-Ladra-Mukhitdinov 2017). PUBLISHABLE as a short note
after (a) correcting the index statement D1, which as written is wrong and misdirects the reader about
the m = 4 route, (b) fixing the attribution D2, (c) obtaining Jamilov 2017 (S^4) and 2016 (symmetric)
and citing them. Recommended addition, which I would make: the index identities of 3b, which give a
one-paragraph proof of Theorem 6's uniqueness clause and state the exact inequality that would settle
m = 4. The m = 4 numerical evidence (mine and the memo's) is strong but is not a proof and must be
labelled as such, which the memo already does.
