# account04/B15 — physical two-coordinate elliptic slices and the Hadamard no-pair barrier

**Run:** `20260922T112652Z-b15-qform-r1`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PAID_REGION_AND_ROUTE_BARRIER`  
**Full quadratic-form bounded-density conjecture:** **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 0. Current target and fresh peer state

The later owner control, revision `2026-09-22.4`, supersedes FEI and directs all workers to the following target: independent real (X_i) have densities at most one, (Q(x)=x^TAx) has at least three eigenvalues of magnitude at least one, and one seeks a universal bound on the density of (Q(X)).

Two fresh reports completed while this run was in progress, so their results are consumed rather than duplicated.

1. account03/B17, repository `yspennstate/math-open-problems`, commit `c64fcff680b0a252a3c92002c60eedba02bbb9ec`, path `qform/fleet-2026-09-22/account03/B17/account03-B17-20260922T112131Z/REPORT.md`, proves the exact \pi bound for coordinate-diagonal forms by selecting a same-sign pair, and refutes law-uniform pointwise Fresnel decay.
2. account01/B08, commit `aa81e06a1ea739fc6ec7895469ce9f8551b7d840`, path `proofnet24/quadratic-form-bounded-density/account01/B08/20260922T110731Z-account01-B08/REPORT.md`, proves a uniform one-square (L^3) characteristic-function bound, obtains a diagonal constant (8), and identifies the rotated product-measure coupling as the live crux.

This report moves beyond the diagonal case.  It proves a coordinate-free-in-the-pair conditional theorem for **any definite physical (2\times2) principal block**, including a cross term.  It then gives an exact infinite Hadamard family satisfying the owner's three-large-eigenvalue hypothesis but having no definite physical (2\times2) principal block at all.  Thus the theorem pays a real rotated region and simultaneously proves that selecting one fixed physical pair cannot close the target.

## 1. Conditional elliptic-slice theorem

Let (A) be a real symmetric (n\times n) matrix.  For a physical coordinate pair (I=\{i,j\}), write

\[
B=A_{I,I}=
\begin{pmatrix}
A_{ii}&A_{ij}\\
A_{ij}&A_{jj}
\end{pmatrix}.
\tag{1.1}
\]

### Theorem 1.1 — `QFORM-PHYSICAL-ELLIPTIC-PAIR-v1`

Suppose (B) is positive definite or negative definite.  Let (X_1,\ldots,X_n) be independent and let each (X_k) have a density bounded by one.  Then (Q(X)=X^TAX) has a density satisfying

\[
\boxed{
\|p_Q\|_\infty
\le {\pi\over\sqrt{|\det B|}}.
}
\tag{1.2}
\]

In particular, any physical definite principal pair with |det B|\ge1 proves the owner's desired conclusion with (C=\pi), irrespective of the other entries of (A), all remaining eigenvalues, and the dimension.

### Proof

Condition on all coordinates outside (I), writing their realized value as (w).  With (z=(X_i,X_j)^T),

\[
Q(z,w)=z^TBz+2\ell(w)^Tz+c(w).
\tag{1.3}
\]

Because (B) is definite it is invertible.  Completing the square gives

\[
Q(z,w)
=(z+B^{-1}\ell)^TB(z+B^{-1}\ell)+c'(w).
\tag{1.4}
\]

The conditional density of (z) is exactly (f_i(z_i)f_j(z_j)), hence is bounded by one.  Translation by (B^{-1}\ell) preserves that bound.

Assume first that (B) is positive definite.  For (0\le a<b), the planar shell

\[
E_{a,b}=\{z:a<z^TBz\le b\}
\]

has area

\[
|E_{a,b}|
={\pi(b-a)\over\sqrt{\det B}},
\tag{1.5}
\]

because (u=B^{1/2}z) maps the shell to (a<|u|^2\le b) with Jacobian (1/\sqrt{\det B}).  Therefore, for every interval (J), the conditional law obeys

\[
\Pr\{Q(X)\in J\mid X_{I^c}=w\}
\le {\pi\over\sqrt{\det B}}|J|.
\tag{1.6}
\]

The same statement follows for negative definite (B) after replacing (B) by (-B).  Averaging (1.6) over the probability law of (X_{I^c}) preserves the bound.  The resulting interval domination implies absolute continuity and (1.2) by the Lebesgue differentiation theorem.  QED.

### Consequences

* Cross terms inside the selected physical pair are fully allowed.
* All couplings from the pair to the remaining coordinates become arbitrary linear terms and disappear by completing the square.
* No density or regularity of the outside conditional law is needed; one averages against a probability measure rather than Lebesgue measure.  This is precisely what fails if one first rotates to an eigenplane and then integrates unnormalized affine slices.

The account03/B17 same-sign diagonal pair lemma is the special case (A_{ij}=0).  The present theorem is a strict extension because the physical (2\times2) block may be any definite matrix.

## 2. Why a physical pair is not forced by three large eigenvalues

The next natural hope would be a matrix lemma asserting that the owner's spectral hypothesis forces some physical definite (2\times2) principal block with determinant bounded below.  That statement is false, even without a small-constant issue.

### Theorem 2.1 — `QFORM-HADAMARD-NO-ELLIPTIC-PAIR-v1`

For every (n=2^m\ge4), there is a real symmetric (n\times n) matrix (A_n) with spectrum

\[
\boxed{(1,1,-1,0,\ldots,0)}
\tag{2.1}
\]

such that **every** physical (2\times2) principal minor has nonpositive determinant.  Hence no physical principal pair is definite.

### Proof

Choose three distinct normalized Walsh--Hadamard rows (r_1,r_2,r_3\in\{\pm n^{-1/2}\}^n).  They are orthonormal.  Set

\[
A_n=r_1r_1^T+r_2r_2^T-r_3r_3^T.
\tag{2.2}
\]

The orthonormality immediately gives (2.1).  For every coordinate (a),

\[
(A_n)_{aa}={1+1-1\over n}={1\over n}.
\tag{2.3}
\]

For (a\ne b), each number (n(r_k)_a(r_k)_b) is \pm1, so

\[
n(A_n)_{ab}=\varepsilon_1+\varepsilon_2-\varepsilon_3
\in\{-3,-1,1,3\}.
\tag{2.4}
\]

In particular, |((A_n)_{ab})|\ge1/n.  Thus

\[
\det A_n[\{a,b\}]
={1\over n^2}-(A_n)_{ab}^2\le0.
\tag{2.5}
\]

Every physical (2\times2) principal block therefore fails to be definite.  QED.

This family meets the exact sharp sign pattern (+,+,-) with all three large eigenvalues at magnitude one.  It proves that a fixed-pair conditioning proof cannot follow from eigenvalue counting alone.

## 3. A broader coordinate-minor barrier

The same delocalization explains why selecting a single physical triple also incurs a dimension loss.  Let (R) be the (3\times n) matrix with rows (r_1,r_2,r_3).  Every column has Euclidean norm \sqrt{3/n}.  Hence, for every coordinate triple (J), Hadamard's determinant inequality gives

\[
\boxed{
|\det R_J|\le\left({3\over n}\right)^{3/2}.
}
\tag{3.1}
\]

On the other hand Cauchy--Binet gives the exact global identity

\[
\boxed{
\sum_{|J|=3}(\det R_J)^2=\det(RR^T)=1.
}
\tag{3.2}
\]

Thus no single coordinate chart has a dimension-free Jacobian, while the **entire family of charts has total squared Jacobian one**.  This identifies a concrete replacement mechanism: an averaged/minor-weighted coarea or Brascamp--Lieb argument could retain (3.2), whereas choosing the best triple first loses order (n^{3/2}).

Equation (3.2) is not itself the missing probability inequality.  The product density must be distributed among the charts without reusing mass.  It does, however, show exactly what a dimension-free proof must aggregate and why a one-chart proof cannot work on maximally delocalized eigenvectors.

## 4. End-to-end implication and first unpaid step

The current conditional architecture is now:

1. If a physical definite (2\times2) principal block has determinant (d>0), Theorem 1.1 gives the complete target conclusion with (C=\pi/\sqrt d).
2. The diagonal target is the (d\ge1) special case already sharpened by account03/B17.
3. The Hadamard matrices (2.2) show that the general three-large-eigenvalue hypothesis may have (d=0) for every physical pair, so the pair route has an exact boundary.
4. In the delocalized regime, Cauchy--Binet retains a dimension-free aggregate reserve (3.2).

The first essential missing implication is therefore:

> derive a nonreusing, minor-weighted coarea inequality for product densities which sums the physical coordinate charts with weights comparable to ((\det R_J)^2), or give a source-valid counterexample to that aggregation.  The inequality must handle the indefinite (+,+,-) phase and must not select a single triple before summing.

This is narrower than the full conjecture and directly survives the Hadamard stress test.  It also respects the fresh peer correction: no law-uniform one-frequency decay is assumed.

## 5. Exact verification

The accompanying standard-library checker constructs the first three Walsh characters for (n=4,8,16,32,64), verifies their orthogonality, verifies (A_nr_1=r_1), (A_nr_2=r_2), (A_nr_3=-r_3), checks every physical pair determinant is nonpositive, and checks the integer Cauchy--Binet identity

\[
\sum_{|J|=3}\det(S_J)^2=n^3,
\]

where (S=\sqrt n,R\) is the sign matrix.  This finite checker is regression evidence; Theorems 1.1 and 2.1 are proved analytically above.

## 6. Status

* `QFORM-PHYSICAL-ELLIPTIC-PAIR-v1`: **PROVED_IN_SOURCE**.
* `QFORM-HADAMARD-NO-ELLIPTIC-PAIR-v1`: **PROVED_IN_SOURCE**.
* Single physical-pair extraction from the three-large-eigenvalue hypothesis: **REFUTED**.
* Full rotated quadratic-form bounded-density conjecture: **OPEN / NOT PROVED**.

