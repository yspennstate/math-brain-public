# MOC4 fleet04/B08 r44 — generic strict-support reduction and exact compound-boundary slacks

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal 4-by-4 Marcus–de Oliveira target  
**Worker:** fleet04/B08  
**Candidate:** `MOC4-GENERIC-STRICT-SUPPORT-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED` — every genuine MOC4 counterexample can be perturbed to a simple-spectrum, irreducible, compound-interior counterexample with a strictly positive support gap and a unique maximizing permutation vertex. Thus all spectral/unitary degeneracies can be removed from the remaining proof obligation. The unrestricted MOC4 target remains open.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and consumed peer results

For complex normal 4-by-4 matrices `A,B`, with eigenvalues `a_1,...,a_4` and `b_1,...,b_4`, prove

\[
\det(A+B)\in\operatorname{conv}\left\{
 v_\sigma(a,b):=\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}.
\]

After diagonalizing `A`, write

\[
D(a,b,U)=\det\bigl(\operatorname{diag}(a)+U\operatorname{diag}(b)U^*\bigr),
\qquad U\in U(4).
\]

This run consumed three exact campaign results.

1. **Assigned partner fleet01/B09**, `MOC4-P-MARGINAL-LIFT-v1`, scientific commit `de46011ccf8ca3691052777937631a8c2ac5fd86`: there is an exact rational orthogonal `U` and complex spectra for which `D` is inside the 24-point MOC4 hull, but no convex representation of `D` can preserve the natural one-point marginals `|u_ij|^2`. Therefore a global proof cannot require its final permutation weights to preserve `P=|U|^2`.
2. **fleet02/B08**, `MOC4-DOUBLE-EIGENVALUE-LIFT-v1`, scientific commit `14542c0b3258ea5763ed145dff8dd4d2e47b2136`: MOC4 is proved whenever either spectrum has a repeated eigenvalue, and also on the common-reducing-block boundary.
3. **fleet01/B07**, mixed-minor reduction, scientific commit `d97eb4e3ad5b467c9494293292e5a78256599c53`: for the actual unitary-derived one-point transport `P` and complementary-pair transport `R`, MOC4 is equivalent in each support direction to the structured mixed assignment inequality `(MI)`; the orientation matrix is exactly the Hadamard mean-zero block of `P`.

The partner obstruction is used here as a proof-design exclusion: the reduction below works only with the actual support gap and never assumes a marginal-preserving permutation lift.

## 2. Compact conditional end-to-end argument

The current proof route is now:

1. For each unit complex `eta`, use the B07 identity to rewrite the target support inequality as `(MI)` for the actual pair `(P,R)`.
2. Prove `(MI)` only on a dense generic locus where spectra are simple, the unitary has no compound degeneracies, and the right-hand permutation optimizer is unique.
3. The theorem below shows that if MOC4 failed anywhere, then it would also fail on that generic locus with a still-positive support gap. Hence a proof on the generic locus closes every degenerate case by contradiction/continuity.

The first essential missing implication after this run is therefore no longer “handle all boundary cases”; it is the genuinely interior statement `MOC4-MIXED-ASSIGNMENT-v1` on the generic strict-support locus.

## 3. Support-gap formulation

For `|eta|=1` define

\[
G_\eta(a,b,U)
:=\Re\bigl(\eta D(a,b,U)\bigr)
 -\max_{\sigma\in S_4}\Re\bigl(\eta v_\sigma(a,b)\bigr).
\tag{1}
\]

Because the hull is compact and convex in the complex plane,

\[
D(a,b,U)\notin\operatorname{conv}\{v_\sigma(a,b)\}
\]

if and only if there exists a unit `eta` with

\[
G_\eta(a,b,U)>0.
\tag{2}
\]

For fixed `eta`, `G_eta` is continuous in `(a,b,U)`: the determinant and all 24 permutation products are continuous, and a finite maximum of continuous functions is continuous.

## 4. Generic strict-support counterexample theorem

### Theorem 1

Assume MOC4 fails for some `(a,b,U)`. Then for every neighborhood of that data there are perturbed data `(a',b',U')` and a support direction `eta'` such that:

1. `G_{eta'}(a',b',U')>0`;
2. all `a'_i` are nonzero and pairwise distinct, and all `b'_j` are nonzero and pairwise distinct;
3. the 24 complex numbers `v_sigma(a',b')` are pairwise distinct;
4. `U'` has no zero 1-by-1 or 2-by-2 minor;
5. for every two-row/two-column block `M=U'[S,T]`, the two eigenvalues of `MM*` are distinct;
6. the normal pair `diag(a')`, `U'diag(b')U'^*` has no nontrivial common reducing subspace;
7. the maximum on the right side of (1) is attained by a unique permutation.

In particular, any counterexample can be chosen with simple spectra, irreducible unitary coupling, strict local compound inequalities, and a unique exposed hull vertex.

### Proof

Suppose `G_eta(a,b,U)=delta>0` for some unit `eta`, obtained from strict separation. By continuity, there is an open neighborhood `N` of `(a,b,U)` on which

\[
G_\eta>\delta/2>0.
\tag{3}
\]

It remains to show that the conditions (2)–(6) define a dense subset of the parameter space.

**Spectral degeneracies.** The equalities `a_i=a_j`, `b_i=b_j`, `a_i=0`, `b_j=0` are proper complex-algebraic conditions. Their finite union has empty interior. Thus simple nonzero spectra are dense.

**Permutation-product collisions.** For distinct `sigma,tau`,

\[
v_\sigma(a,b)-v_\tau(a,b)
\]

is a nonzero polynomial in the spectral variables. Hence each collision locus `v_sigma=v_tau` is a proper algebraic set. Avoiding the finitely many such loci makes all 24 vertices distinct.

**Zero entries and zero 2-minors.** For a fixed entry or fixed 2-by-2 minor of `U`, its squared modulus is a real-analytic function on `U(4)` and is not identically zero. Therefore its zero set has empty interior. Avoiding the finitely many such sets gives condition (4). For a 4-by-4 unitary, nonzero entries also imply all complementary 3-by-3 minors are nonzero by Jacobi complementarity.

**Equal singular values in a 2-by-2 compression.** For fixed `S,T`, put `M=U[S,T]`. The discriminant

\[
\Delta_{S,T}(U)
:=\operatorname{tr}(MM^*)^2-4\det(MM^*)
\tag{4}
\]

is real analytic and equals `(lambda_1-lambda_2)^2`, where `lambda_1,lambda_2` are the eigenvalues of `MM*`. It is not identically zero: one can choose a unitary sending one selected row direction into `T` and the other into `T^c`, giving singular values `1,0`. Thus each equality locus `Delta_{S,T}=0` has empty interior, and finitely many can be avoided simultaneously.

**Common reducing subspaces.** Once `a'` is simple, every reducing subspace of `diag(a')` is spanned by a subset of coordinate vectors. For each nonempty proper subset `S`, the condition that the same coordinate subspace reduce `U'diag(b')U'^*` is the vanishing of all cross-block entries

\[
\bigl(U'\operatorname{diag}(b')U'^*\bigr)_{ij},
\qquad i\in S,\ j\notin S.
\]

For simple `b'` this is a proper real-algebraic condition and is not satisfied by a generic unitary. There are only finitely many `S`, so irreducible pairs are dense.

The complement of a finite union of the proper sets above is dense. Hence choose `(a',b',U')` in `N` satisfying (2)–(6). By (3), the same `eta` still gives a positive support gap.

Finally, because the 24 vertices are pairwise distinct, the set of support directions for which two of them have equal real projection is finite on the unit circle: each pair contributes at most two normal directions. Perturb `eta` slightly away from those directions. The positive gap persists by continuity, while the maximizing permutation becomes unique. This gives `eta'` and proves the theorem. ∎

### Corollary 1 — generic-locus sufficiency

To prove MOC4 for all complex normal 4-by-4 pairs, it is enough to prove the B07 mixed assignment inequality `(MI)` for the locus in Theorem 1 and for support directions with a unique maximizing permutation.

Indeed, a failure anywhere would produce a failure on that locus, contradicting the generic-locus theorem.

This corollary removes singular matrices, repeated spectra, accidental equal hull vertices, common reducing blocks, zero compound minors, and local equal-singular-value strata from the indispensable proof obligation. The fleet02/B08 repeated-spectrum/common-block theorem independently closes two of those boundaries and is consistent with this continuity reduction.

## 5. Exact characterization of the local compound boundaries

The B07 reduction associates to every 2-by-2 block `M=U[S,T]`

\[
q=|\det M|^2,
\qquad
q'=|\det U[S,T^c]|^2,
\]

and

\[
d=q-q',\qquad r=q+q'.
\tag{5}
\]

Let `lambda_1,lambda_2 in [0,1]` be the eigenvalues of `MM*`. Since the complementary two-column block `N=U[S,T^c]` satisfies `MM*+NN*=I_2`,

\[
q=\lambda_1\lambda_2,
\qquad
q'=(1-\lambda_1)(1-\lambda_2),
\qquad
d=\lambda_1+\lambda_2-1.
\tag{6}
\]

The two inequalities used by B07 admit exact slack identities:

\[
\boxed{r+d=2\lambda_1\lambda_2=2q,}
\tag{7}
\]

\[
\boxed{r-d=2(1-\lambda_1)(1-\lambda_2)=2q',}
\tag{8}
\]

and

\[
\boxed{\frac{1+d^2}{2}-r
=\frac{(\lambda_1-\lambda_2)^2}{2}.}
\tag{9}
\]

Therefore:

- `r=|d|` if and only if one of the two complementary 2-by-2 minors vanishes, equivalently at least one singular value of `M` is `0` or `1`;
- `r=(1+d^2)/2` if and only if `MM*` is scalar, equivalently `lambda_1=lambda_2`;
- on the generic locus of Theorem 1,

\[
\boxed{|d|<r<\frac{1+d^2}{2}}
\tag{10}
\]

for every two-row/two-column block.

Thus the local feasible region used by `(MI)` has an explicit geometric boundary: rank/complement-rank loss on the lower side, and equal principal angles on the upper side. Neither type needs to be treated as a possible isolated counterexample mechanism in the remaining proof, because any true support failure would persist after perturbing into the strict region.

## 6. Why the partner no-go result matters here

The fleet01/B09 certificate gives an exact point for which the determinant lies in the MOC4 hull while every convex representation preserving `P=|U|^2` is ruled out by a support-functional dual certificate. Therefore the generic reduction cannot be strengthened by saying “choose generic data and then lift the actual `P` marginals to the exposed permutation.” That route is already false.

The valid conclusion is weaker and exactly aligned with `(MI)`: at a hypothetical generic counterexample, one has a positive support gap against a unique permutation vertex, but no prescribed final permutation marginals. The remaining proof must exploit the common-unitary relation between `P` and `R` directly, or another support-level argument.

## 7. Remaining obligation

After this run the indispensable case can be stated without degeneracies:

> **`MOC4-MIXED-ASSIGNMENT-GENERIC-v1`.** For every `U in U(4)` on the generic locus of Theorem 1, every simple nonzero complex spectra `a,b`, and every unit support direction `eta` for which the 24 permutation products have a unique maximizing permutation, the actual unitary-derived `P,R` satisfy the B07 mixed assignment inequality `(MI)`.

Proving this statement is enough for full MOC4 by Corollary 1. A counterexample to an unrestricted `(P,R)` polytope relaxation or the existence of a nonmonomial stationary/maximizing unitary would still not refute MOC4; one needs a positive support gap against all 24 actual permutation products.

No claim of worldwide novelty is made. No benchmark gold, held-out answers, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, public posting, paid model/API calls, or remote workflows were used.
