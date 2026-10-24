# E0068 - Rozikov's Problem 21: quadratic stochastic operators with V^r = V

Written 2026-09-09. Status: partial. The structural theorem the integrator asked for is
proved (with the load-bearing algebraic step certified in Lean), the general case is
reduced to a retraction-plus-finite-order decomposition, and an explicit r = 3 example
shows the class is strictly larger than the Bernstein maps. The full description is not
done; it contains the Bernstein problem (r = 2), which is itself unsolved in general.

## 1. The problem as the source states it

Ganikhodzhaev and Rozikov, "Quadratic stochastic operators: results and open problems",
arXiv:0902.4207v2, Section 16, p. 11. Verbatim:

> QSO V is a Bernstein mapping if V^2 = V. This property is just the stationarity
> principle. This property also is known as Hardy-Weinberg law [23]. The problem is to
> describe all Bernstein mappings explicitly. The case m <= 2 is mathematically trivial and
> biologically not interesting. Bernstein [1] solved the above problem for the case n = 3
> and obtained some results for n >= 4. In works by Lyubich (see e.g. [25],[26]) the
> Bernstein problem was solved for all m under the regularity assumption. [...]
>
> Problem 21. Describe all QSOs which satisfy V^r(x) = V(x) for any x in S^{m-1} and some
> r >= 2.

Here a QSO is V: S^{m-1} -> S^{m-1}, (V x)_k = sum_{i,j} P_{ij,k} x_i x_j with P_{ij,k} >= 0,
P_{ij,k} = P_{ji,k}, sum_k P_{ij,k} = 1 (the paper's (4), (5)). The quantifiers: one r >= 2,
and the identity V^r(x) = V(x) for every x in the simplex.

The ledger row quotes the statement faithfully. Its title, "Quadratic stochastic operators
that are eventually idempotent", does not: "eventually idempotent" is V^{n+1} = V^n (the
identity of an n-th order Bernstein algebra, x^{[n+2]} = omega(x)^{2^n} x^{[n+1]}), whereas
Problem 21 is V^r = V, i.e. x^{[r+1]} = omega(x)^{2^r - 2} x^{[2]}. The two classes meet
only in the Bernstein maps: if both V^r = V and V^{n+1} = V^n hold then on the image W =
V(S) we get V^{r-1} = id and V^n = V^{n+1} = ... = V^{r-1} = id, so V = id on W and V^2 = V.
The integrator's hint ("this is the n-th order Bernstein algebra identity") therefore
points at the neighbouring problem, not this one. In Varro's terminology (Comm. Algebra 49
(2021), 10.1080/00927872.2020.1812620, written for characteristic 2) V^r = V says the
evolution operator is "ultimately periodic of pre-period 1 and period r - 1"; the n-th order
Bernstein identity is pre-period n and period 1.

## 2. Findings

Notation. S = S^{m-1}, H = {x in R^m : sum x_i = 1} the affine hull of S, W = V(S).
For a nonempty A subset of [m] let F_A = {x in S : supp x subset of A} be the face, relint F_A
= {x : supp x = A}, and let B(A) = {k : P_{ij,k} > 0 for some i, j in A} be the support map.
For x in S one has supp V(x) = B(supp x), since (V x)_k is a sum of nonnegative terms
P_{ij,k} x_i x_j and x_i x_j > 0 exactly when i, j in supp x. B is monotone for inclusion and
B(A) is nonempty (each row of P sums to 1).

**Theorem A (structure when the image is fat).** Let V be a QSO with V^r = V on S for some
r >= 2. If W = V(S) has nonempty interior in H (equivalently: W is not contained in a proper
algebraic subset of H), then V is a coordinate permutation, V(x)_{sigma(i)} = x_i for a
permutation sigma of [m], and sigma^{r-1} = id. Conversely every coordinate permutation with
sigma^{r-1} = id satisfies V^r = V and V(S) = S.

**Corollary A'.** A QSO that is a bijection of S of finite order (V^n = id on S for some n)
is a coordinate permutation. (Take r = n + 1.) In particular no Volterra QSO other than the
identity has finite order, although Volterra QSOs with |a_ij| < 1 are homeomorphisms of S.

**Theorem B (general decomposition, no hypothesis on the image).** Let V^r = V and put
E = V^{r-1}, g = V|_W.
(i) E is idempotent, E(S) = W, and E|_W = id: E is a polynomial retraction of S onto W.
(ii) g is a homeomorphism of W onto itself with g^{r-1} = id_W; V = g o E on S.
(iii) Conversely, if E is any idempotent map of S with image W and g any map W -> W with
g^{r-1} = id, then V = g o E satisfies V^r = V.
(iv) The support map satisfies B^r = B; on the family of image supports {B(A)} it is a
bijection with B^{r-1} = id.
(v) Let Z be the Zariski closure of W in H. Then Z is irreducible, E(H) is contained in Z,
E|_Z = id, V(Z) is contained in Z, and V|_Z is a polynomial automorphism of Z with
(V|_Z)^{r-1} = id. So the coordinate ring R[Z] is a retract of the polynomial ring
R[H] = R[x_1, ..., x_{m-1}], and the "finite-order part" of V is a finite-order automorphism
of a polynomial retract of affine space.

**Example (r = 3, not Bernstein, not linear).** Let m = 3, p = x_1 + x_2/2, q = x_3 + x_2/2,
and V(x) = (q^2, 2pq, p^2) (the Hardy-Weinberg map followed by the swap of coordinates 1 and
3). V is a QSO (all P_{ij,k} >= 0, rows sum to 1; checked in checks.py), V^3 = V exactly on
S, and V^2 - V = (2x_1 + x_2 - 1, 0, 1 - 2x_1 - x_2) is not zero. Its image is the
Hardy-Weinberg parabola, on which V acts as the involution p <-> q. This is the pattern of
Theorem B with W a curve, E = V^2 the Hardy-Weinberg map, g the flip.

**Example (linear, g not a coordinate permutation).** V(x) = Mx with the column-stochastic
matrix M = [e_3, e_3, (e_1+e_2)/2] (columns are M e_1, M e_2, M e_3). Then M^3 = M, M^2 != M,
W is the segment from (1/2, 1/2, 0) to e_3 and g flips it. No coordinate permutation maps
(1/2,1/2,0) to e_3, so V is not of the form "coordinate permutation composed with a
Bernstein map". So the finite-order part g need not come from a symmetry of the simplex;
Theorem A says it does exactly when W is fat.

## 3. Proofs

### Theorem A

Step 1 (V is a finite-order bijection of S). For y = V(x) in W, V^{r-1}(y) = V^r(x) = V(x)
= y. So the polynomial map V^{r-1} - id on H vanishes on W, which contains a nonempty open
subset of H; a polynomial vanishing on a nonempty open subset of an affine space vanishes
identically. Hence V^{r-1} = id on H, in particular on S. Then V is a bijection of S (its
inverse on S is V^{r-2}) and W = S.

Step 2 (the support map is induced by a permutation). For x with supp x = A,
B^{r-1}(A) = supp V^{r-1}(x) = supp x = A. So B is a bijection of the nonempty subsets of
[m] with inverse B^{r-2}, and both B and B^{-1} = B^{r-2} are monotone (compositions of the
monotone map B). Hence B is an automorphism of the poset of nonempty subsets ordered by
inclusion. Such an automorphism sends minimal elements to minimal elements: if B({i}) = C
strictly contained a singleton {k}, then B^{-1}({k}) is a nonempty subset of B^{-1}(C) = {i},
so B^{-1}({k}) = {i} and B({i}) = {k}, a contradiction. So B({i}) = {sigma(i)} for a
permutation sigma, and likewise B^{-1}({k}) = {sigma^{-1}(k)}. By monotonicity B(A) contains
sigma(A) for every A, and B^{-1}(C) contains sigma^{-1}(C); applying the second to C = B(A)
gives A contains sigma^{-1}(B(A)), i.e. B(A) is contained in sigma(A). So B(A) = sigma(A).

Consequently P_{ii,k} = 0 for k != sigma(i), so P_{ii,sigma(i)} = 1 and V(e_i) = e_{sigma(i)};
and P_{ij,k} = 0 unless k in {sigma(i), sigma(j)}. Let pi be the coordinate permutation
(pi x)_{sigma(i)} = x_i and put U = pi^{-1} o V. Then U is a QSO with coefficients
Q_{ij,k} = P_{ij,sigma(k)}, which vanish unless k in {i, j}: U is a Volterra QSO, in the
source's form (7)-(8): (U x)_k = x_k (1 + sum_i a_{ki} x_i), a_{ki} = 2 Q_{ik,k} - 1,
a_{ii} = 0, a_{ki} = -a_{ik}.

Step 3 (edges). Fix i != j and t in [0,1], x = t e_i + (1 - t) e_j. Then
(U x)_i = Q_{ii,i} t^2 + 2 Q_{ij,i} t(1-t) + Q_{jj,i} (1-t)^2 = t^2 + (1 + a_{ij}) t(1-t)
= t + a_{ij} t (1 - t) =: g_{a_{ij}}(t), and (U x)_j = 1 - (U x)_i, (U x)_k = 0 otherwise.
So V maps the edge [e_i, e_j] into the edge [e_{sigma(i)}, e_{sigma(j)}], sending the point
with parameter t (the weight on e_i) to the point with parameter g_{a_{ij}}(t) (the weight on
e_{sigma(i)}). Iterating, V^{r-1} maps [e_i, e_j] into [e_{sigma^{r-1}(i)}, e_{sigma^{r-1}(j)}]
= [e_i, e_j] (sigma^{r-1} = id by Step 2) with parameter map
g_{a_{r-2}} o ... o g_{a_1} o g_{a_0}, where a_l = a_{sigma^l(i) sigma^l(j)}.
Since V^{r-1} = id, this composition equals t on [0,1], hence as a polynomial.

Step 4 (degree). For real polynomials, natDegree(f o g) = natDegree f * natDegree g, and
natDegree g_a = 2 when a != 0, = 1 when a = 0. A composition of the g_{a_l} equal to X thus
has all factors of degree 1, i.e. every a_l = 0; in particular a_{ij} = 0. This is exactly
the content of `chain_eq_X_all_zero` in U_E0068.lean (compiled clean; axioms propext,
Classical.choice, Quot.sound). It is also checked symbolically for a chain of three edge maps
in checks.py: the composition has degree 8, leading coefficient -a_1 a_2^2 a_3^4, and the only
solution of "composition = t" is a_1 = a_2 = a_3 = 0.

Step 5. Since i != j were arbitrary, the skew matrix (a_{ij}) is zero, U = id, and V = pi.
Finally pi^{r-1} = V^{r-1} = id gives sigma^{r-1} = id. The converse is immediate. QED.

The "equivalently" in the statement: if W is not contained in a proper algebraic subset of
H then V^{r-1} - id, which vanishes on W, vanishes on H, and Step 1 goes through; conversely
a set with nonempty interior is not contained in a proper algebraic subset.

### Theorem B

(i) E(S) = V^{r-2}(W); V|_W is a bijection of W (V^{r-1} = id on W, computed in Step 1 above
without any hypothesis), so V^{r-2}(W) = W. E|_W = V^{r-1}|_W = id, and E^2 = E follows.
(ii) g = V|_W maps W into W (V(W) = V^2(S) is contained in V(S)), g^{r-1} = id_W, so g is a
bijection of the compact set W, continuous, hence a homeomorphism; and g o E = V^r = V.
(iii) (g o E)^r = g^r o E (since E o g o E = g o E as E|_W = id) = g o E.
(iv) For x with supp x = A, B^r(A) = supp V^r(x) = supp V(x) = B(A).
(v) V^{r-1} - id vanishes on W, hence on its Zariski closure Z. E^{-1}(Z) is Zariski closed
and contains S, which is Zariski dense in H; so E(H) is in Z. Same for V^{-1}(Z), which
contains W and so Z. Irreducibility: the ideal of Z is {f : f o E = 0 on H}, and R[H] is a
domain, so it is prime. E* : f -> f o E is a ring retraction of R[H] onto the subring
{f o E} = R[H]/I(Z) = R[Z].

## 4. What is not done

The full description asked for in Problem 21. It contains the Bernstein problem (r = 2),
which is solved only under Lyubich's regularity assumption and in small dimensions, so a
complete description of the r >= 3 case would have to solve that first. What is new here is
that the r >= 3 case is not Bernstein in disguise: Theorem B splits V into a retraction
(a Bernstein-type object, of degree 2^{r-1} in general) and a finite cyclic symmetry g of the
image, the examples show g can be nontrivial, and Theorem A shows that the symmetry is a
coordinate permutation and the retraction is trivial as soon as the image is fat.

Two directions that look tractable and are not done:
1. Image of dimension one. Then Z is a rational curve and, since V = phi o u on H with phi a
   parametrisation of Z and u scalar, deg phi * deg u <= 2, so Z is a line or a parabola and g
   is t -> t or t -> c - t in the parameter: r = 2 or V^3 = V, and E = g^{r-2} o V is quadratic.
   Whether E is then a QSO (nonnegative coefficients after rehomogenising with sum x = 1) is
   the point I did not settle; if it is, the one-dimensional case reduces exactly to
   "Bernstein map with one-dimensional image, optionally flipped". This sketch uses that a
   polynomial retract of affine space of dimension one is a polynomially parametrised line
   (Costa, J. Algebra 44 (1977)); I did not re-check the hypotheses of that theorem.
2. Whether E = V^{r-1} always agrees on S with a quadratic map (it does in both examples).
   If yes, Problem 21 reduces to: Bernstein QSOs V_0 plus finite-order homeomorphisms g of
   V_0(S) such that g o V_0 is quadratic with nonnegative coefficients.

## 5. Checks

- checks.py (sympy + numpy): the swapped Hardy-Weinberg map has V^3 - V = 0 identically on
  the simplex (after substituting x_3 = 1 - x_1 - x_2) and V^2 - V = (2x_1 + x_2 - 1, 0, ...);
  its cubic matrix has nonnegative entries with unit row sums; 20,000 random Dirichlet points
  give max |V^3 - V| = 1.6e-15 and max |V^2 - V| = 0.99 (independent floating-point check of
  the symbolic identity). The m = 2 case: the edge map a t^2 + 2b t(1-t) + c(1-t)^2 has t^2
  coefficient a - 2b + c, which must vanish, leaving the affine map c + (2b - 2c) t; the only
  affine bijections of [0,1] of finite order are t and 1 - t. Composition of three edge maps
  has degree 8 with leading coefficient -a_1 a_2^2 a_3^4; the solve of "composition = t"
  returns only a_1 = a_2 = a_3 = 0. The linear example M satisfies M^3 = M, M^2 != M.
- U_E0068.lean: `edgeMap_natDegree` (degree 2 when a != 0), `natDegree_eq_one_of_comp_eq_X`
  (multiplicativity of degree under composition), `chain_eq_X_all_zero` (a chain of edge maps
  equal to X has all coefficients zero). Compiled with `lake env lean` in ~/erdos_fc; one
  fix was needed (a wrong lemma name, `Nat.mul_eq_one`, replaced by
  `Nat.eq_one_of_mul_eq_one_right/left` inside a `first` combinator). The file was run a
  third time unchanged only to capture the `#print axioms` lines into lean_axioms.txt.
- The strongest case that Theorem A is wrong is that the poset argument in Step 2 might let
  B send a singleton to a larger set. I checked this against the Hardy-Weinberg example,
  where B({2}) = {1,2,3}: there W is a curve, V^{r-1} = id fails off W, B is not injective
  (B({1}) = {3}, B({1,2}) = {1,2,3} = B({2})), and the theorem does not apply, as it should
  not. The other place to break it is Step 1; it needs only that W contains an open subset of
  H, which is the hypothesis.

## 6. Prior art

The session's web-search budget was exhausted before this task started, so the search was
done by direct fetches of the arXiv API, the zbMATH Open API and Crossref (scripts
fetch_prior_art.py, fetch_prior_art2.py; raw JSON kept). arXiv returned HTTP 429 on every
call; zbMATH and Crossref answered.

- Ganikhodzhaev, Rozikov, arXiv:0902.4207 (2009), the source. Problem 21 as quoted above.
- Ganikhodzhaev, Eshmamatova, "Quadratic automorphisms of a simplex and the asymptotic
  behavior of their trajectories", Vladikavkaz. Mat. Zh. 8 (2006) no. 2, 12-28 (zbMATH
  summary): "an arbitrary quadratic automorphism can be represented as the composition of a
  Volterra operator and a permutator". This is Step 2 of Theorem A for bijective QSOs
  (proved there by a different route, presumably); Steps 3-4, the finite-order part, I did not
  find anywhere. Saburov, Shakhidi, "Localization of fixed and periodic points of quadratic
  automorphisms in a finite-dimensional simplex", Uzb. Mat. Zh. 2007 no. 3, 81-87, studies
  periodic points, not periodic operators. Neither paper was accessible in full text.
- Ganikhodzhaev, Mukhamedov, Rozikov, "Quadratic stochastic operators and processes: results
  and open problems", IDAQP 14 (2011) 279-335 (zbMATH record): the later survey by the same
  authors; the record does not show whether Problem 21 was updated, and arXiv was
  rate-limited, so its text was not read.
- Varro, Comm. Algebra 49 (2021) no. 2, 10.1080/00927872.2020.1812620: classifies
  "ultimately periodic" evolution operators V^{n+p} = V^n, but over fields of characteristic
  2, where V(x) = x^2 is additive; not applicable to real stochastic operators.
- n-th order Bernstein algebras (Ouattara 1991; Gonzalez, Gutierrez, Martinez 1994; Towers,
  Bowman 1996; Gonzalez, Guzzo, Vicente 2001): identity x^{[n+2]} = omega(x)^{2^n} x^{[n+1]},
  i.e. V^{n+1} = V^n. A different identity from Problem 21 (see Section 1).
- Plenary train algebras (Gutierrez Fernandez 2000; Behn, Hentzel, J. Algebra 324 (2010);
  Bayara, Coulibaly, J. Algebra 646 (2024)): the identity of Problem 21 is the plenary train
  identity x^{[r+1]} = omega^{2^r-2} x^{[2]}, whose train roots are 0 and the (r-1)-th roots of
  unity; the plenary-train literature works with distinct real roots or asks for idempotents,
  and I found no treatment of this root configuration.
- Lyubich, "The Bernstein problem in mathematical genetics and Bernstein algebras" (1994) and
  the 1992 monograph: the Bernstein case r = 2, regular case solved; general case open.

Phrases that found things: "quadratic automorphisms of a simplex" (zbMATH), "ultimately
periodic evolution operator" (zbMATH), "Bernstein algebras of order" (zbMATH), "plenary train"
(zbMATH, Crossref). Phrases that found nothing relevant: "V^r = V" with "quadratic stochastic",
"Problem 21" Rozikov.

(This was the ask: attack E0068, Rozikov Problem 21, QSOs with V^r = V; survey and prove the
structural theorem that a fat image forces a coordinate permutation.)
