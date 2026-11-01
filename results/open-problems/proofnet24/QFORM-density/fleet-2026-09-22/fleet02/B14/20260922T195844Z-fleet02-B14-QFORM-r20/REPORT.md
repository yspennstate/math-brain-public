SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B14, 2026-09-22T19:58:44Z.
attacking: aggregate-before-inversion by disjoint-bank compression — collapse diffuse coordinate banks to three independent scalar bank variables before reciprocal determinant payment.

# fleet02/B14 — disjoint-bank compression before inversion

**Run:** `20260922T195844Z-fleet02-B14-QFORM-r20`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Translations and localization / complementary constructions and source-valid counterexamples  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING TARGET-LEVEL THEOREM`; full QFORM remains OPEN.

## 1. First unpaid implication and mechanism change

The preceding B14 run proved that law localization cannot repair matrix localization.  In the target-valid family

\[
A_m=[1]\oplus J_m/m\oplus(-J_m/m)
\]

the total third exterior-volume mass is one, but every nonsingular physical principal triple has determinant magnitude \(m^{-2}\), so a one-triple reciprocal-determinant certificate necessarily loses \(m^{2/3}\).

The new mechanism does **not** select a bounded set of physical coordinates.  It aggregates a whole coordinate bank into one scalar linear form while the original product law is still intact, and only then invokes the completed three-variable determinant theorem.  This is an aggregate-before-inversion operation.

The first unpaid implication after this run is stated precisely in Section 8: extend this exact bank compression to a structural bank/ridge dichotomy for arbitrary target matrices, or prove that a residual transverse matrix prevents such a reduction.

## 2. Source-pinned inputs actually used

### 2.1 Assigned partner result, fleet03/B14 r17

The newest completed assigned-partner result is `QFORM-FRAGMENTWISE-RECENTERING-TAX-v1`, fleet03/B14 run `20260922T193756Z-fleet03-B14-QFORM-r17`, canonical proof

`yspennstate/math-open-problems@4e1811952f5db1e18ed05abc37a8dfc8c51e641f:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260922T193756Z-fleet03-B14-QFORM-r17/REPORT.md`.

It proves that if a local certificate has inverse diagonal-scaling exponents and one first splits an extreme set into components, normalizes/recenters each component, takes an L-infinity bound, and then averages, one pays an unavoidable fragment tax.  For the determinant-triple certificate the artificial tax is exactly \(N^2\) under equal N-fragment partitions.  Its positive replacement is to keep each whole unit-measure extreme set intact, center once, and aggregate before reciprocal scale payment.

This run applies that ordering literally: there is **no** fragment normalization.  Whole coordinate groups are compressed directly under their original product laws.

### 2.2 Principal-triple determinant theorem, fleet03/B14 r16

`QFORM-PRINCIPAL-TRIPLE-DETERMINANT-LOCALIZATION-v1`, canonical proof

`yspennstate/math-open-problems@89e6481f4f7ed7d49a77cfcb989ee93572d5d5cd:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260922T190524Z-fleet03-B14-QFORM-r16/REPORT.md`,

states that for three independent cap-one variables and any nonsingular symmetric 3x3 coefficient matrix B, arbitrary affine perturbations included,

\[
\|p_Q\|_\infty\le 32\sqrt{10}\,|\det B|^{-1/3}.
\tag{2.1}
\]

The theorem is uniform in support geometry and affine shifts.

### 2.3 Product-safe one-dimensional bank projection

`QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical proof

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`,

proves that if u is a unit vector and X has independent cap-one coordinates, then the scalar bank variable

\[
Y=u^T X
\]

has a density satisfying

\[
\|p_Y\|_\infty\le \sqrt e.
\tag{2.2}
\]

This follows from its general k-dimensional projection bound \(e^{k/2}\) at k=1.  No moment, support or continuity assumption is used.

### 2.4 Latest aggregate-bank correction

The current correction `QFORM-R15-AREA-BANK-SINGLE-PACKET-FALSE-v1`, with canonical proof

`yspennstate/math-open-problems@5266d24ea98d9bb5902c51a92eca0e3e38112e39:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260922T193347Z-b07-639234ec/REPORT.md`,

shows that constant aggregate determinant mass cannot in general be collapsed to one uniformly good coordinate packet.  The same report proves a rank-r cross-fiber Plancherel theorem which pays a whole physical cross block at once.  The theorem below is the disjoint-bank analogue on the principal/self-interaction side.

## 3. Main theorem: disjoint-bank compression

### Theorem — `QFORM-DISJOINT-BANK-COMPRESSION-v1`

Let \(G_1,G_2,G_3,R\) be a partition of the original coordinate set.  For each k choose a unit vector \(u_k\) supported on \(G_k\), and let

\[
U=(u_1,u_2,u_3),\qquad U^TU=I_3.
\]

Suppose the symmetric matrix A has, on \(S=G_1\cup G_2\cup G_3\), the exact bank factorization

\[
A_{S,S}=UMU^T,
\qquad
A_{S,R}=UC,
\tag{3.1}
\]

for some nonsingular symmetric \(3\times3\) matrix M and arbitrary matrix C.  There is no restriction on \(A_{R,R}\).

For independent real inputs \(X_i\) whose densities are bounded by one, the full quadratic form \(Q=X^TAX\) has an essentially bounded density and

\[
\boxed{
\|p_Q\|_\infty
\le 32e\sqrt{10}\,|\det M|^{-1/3}.
}
\tag{3.2}
\]

The same estimate holds after arbitrary deterministic translations of the input coordinates or addition of an arbitrary deterministic affine term.  The constant is independent of dimension, support locations, support diameters, fragment counts, fragment separations and moments.

### Proof

Condition on all outside coordinates \(X_R=z\).  Because the groups \(G_1,G_2,G_3\) are disjoint original-coordinate groups and the original coordinates are independent, the scalar bank variables

\[
Y_k=u_k^T X_{G_k},\qquad k=1,2,3,
\]

are mutually independent.

By (2.2), each has a density satisfying

\[
\|p_{Y_k}\|_\infty\le\sqrt e.
\tag{3.3}
\]

The factorization (3.1) gives, for the conditional form,

\[
Q_z
=Y^TMY+2(Cz)^TY+c(z),
\tag{3.4}
\]

where \(c(z)\) includes the arbitrary outside quadratic form and every outside affine term.  Thus all outside geometry has become an arbitrary affine perturbation of the three independent bank variables.

Set

\[
Z_k=\sqrt e\,Y_k.
\]

Then the Z_k remain independent and their densities satisfy

\[
\|p_{Z_k}\|_\infty
=e^{-1/2}\|p_{Y_k}(\cdot/\sqrt e)\|_\infty
\le1.
\tag{3.5}
\]

In the Z variables, (3.4) becomes

\[
Q_z=Z^T(M/e)Z+2e^{-1/2}(Cz)^TZ+c(z).
\tag{3.6}
\]

The principal-triple theorem (2.1) applies directly, including the arbitrary affine vector.  Since

\[
\det(M/e)=e^{-3}\det M,
\]

we get, uniformly in z,

\[
\|p_{Q_z}\|_\infty
\le32\sqrt{10}\,|e^{-3}\det M|^{-1/3}
=32e\sqrt{10}\,|\det M|^{-1/3}.
\tag{3.7}
\]

Averaging the conditional laws over \(X_R\) preserves the same L-infinity bound.  This proves (3.2).

Translations of any original input coordinates only translate the corresponding bank variables and alter the affine/scalar terms in (3.4); neither (3.3) nor (2.1) changes.  No support or moment bound has entered.  QED.

Numerically,

\[
32e\sqrt{10}=275.070780805686\ldots.
\tag{3.8}
\]

The numerical value is not important; the point is dimension-free aggregate payment.

## 4. Exterior-volume interpretation: sum before reciprocal power

If R is empty, so that

\[
A=UMU^T,
\qquad U^TU=I_3,
\tag{4.1}
\]

then the three nonzero eigenvalues of A are exactly the eigenvalues of M.  Hence

\[
\|\wedge^3A\|_{HS}=|\det M|.
\tag{4.2}
\]

Equivalently, Cauchy--Binet gives

\[
\sum_{|I|=|J|=3}\det(A_{I,J})^2
=\det(M)^2.
\tag{4.3}
\]

Therefore (3.2) can be written in the exact-rank-three bank class as

\[
\boxed{
\|p_Q\|_\infty
\le32e\sqrt{10}
\left(
\sum_{|I|=|J|=3}\det(A_{I,J})^2
\right)^{-1/6}.
}
\tag{4.4}
\]

This is precisely the ordering demanded by the previous B14 obstruction: the entire l2 mixed-minor bank is summed **before** a reciprocal curvature power is paid.

If the three nonzero eigenvalues satisfy \(|\lambda_j|\ge1\), then \(|\det M|\ge1\), and (3.2) yields the universal bound

\[
\|p_Q\|_\infty\le32e\sqrt{10}
\tag{4.5}
\]

for this whole disjoint-bank subclass.

## 5. Uniform-bank stress family and the previous B14 obstruction

Take three disjoint groups of sizes \(m_1,m_2,m_3\), and let

\[
u_k=m_k^{-1/2}{\bf1}_{G_k}.
\]

For arbitrary nonsingular symmetric M put

\[
A=UMU^T.
\tag{5.1}
\]

Every physical principal triple which does not choose exactly one coordinate from each bank is singular.  A triple I that chooses one coordinate from each bank satisfies

\[
\det A_{I,I}
=rac{\det M}{m_1m_2m_3}.
\tag{5.2}
\]

There are \(m_1m_2m_3\) such triples, so

\[
\sum_{|I|=3}\det(A_{I,I})^2
=rac{\det(M)^2}{m_1m_2m_3},
\tag{5.3}
\]

which may tend to zero, even though the full mixed-minor bank in (4.3) remains exactly \(\det(M)^2\).

This gives a clean algebraic explanation of the previous B14 family.  For

\[
A_m=[1]\oplus J_m/m\oplus(-J_m/m),
\]

take \((m_1,m_2,m_3)=(1,m,m)\) and \(M=\operatorname{diag}(1,1,-1)\).  Then every nonzero physical principal triple determinant has magnitude \(m^{-2}\), while the bank determinant is exactly one.  The one-triple theorem loses \(m^{2/3}\); Theorem 3.1 gives instead

\[
\|p_Q\|_\infty\le32e\sqrt{10}
\tag{5.4}
\]

uniformly in m.

In fact this particular diagonal bank-level M can be paid more sharply.  Each bank scalar has density at most \(\sqrt e\); after scaling to cap one, the same-sign two-square convolution gives the separable bound \(\pi\), so the original bank variables give \(\pi e\).  Thus the diffuse family that defeated bounded active-set localization is not itself difficult once aggregation is performed first.

This is a supporting family theorem, not a proof that every target A has a disjoint-bank representation.

## 6. Applying the assigned partner's r17 localization-order theorem

The partner r17 theorem says that fragmentwise normalize/recenter/sup/average is inherently nonuniform whenever the downstream certificate has a positive reciprocal scaling exponent.  The new proof avoids exactly that failure:

1. no one-dimensional marginal is decomposed into interval components;
2. no fragment is renormalized;
3. all support locations and distant components remain inside the whole product law;
4. each whole coordinate bank is pushed forward once under a unit linear functional;
5. the product-safe projection theorem bounds that whole bank density by \(\sqrt e\), independently of its support geometry;
6. only after the three whole-bank laws are obtained is the reciprocal determinant \(|\det M|^{-1/3}\) paid.

So arbitrary fragmentation is not merely tolerated: it is never exposed to a reciprocal scale.  This is a concrete realization of the partner's requested aggregate-before-recentering order.

## 7. Relation to cross-fiber Plancherel

The B07 correction proves that aggregate determinant mass can be supported on many individually tiny packets, while the entire rank-three cross block remains uniformly payable.  Its `QFORM-CROSS-FIBER-PLANCHEREL-v1` theorem is therefore complementary to Theorem 3.1:

- a rank-three physical cross block is paid by keeping both coordinate sides whole and using Plancherel on the projected cross interaction;
- a rank-three disjoint self-interaction bank is paid by keeping each coordinate bank whole, projecting it to one scalar, preserving independence across the three disjoint banks, and then applying the three-variable determinant theorem.

Both mechanisms sum the relevant geometry before reciprocal inversion and both are immune to arbitrary support fragmentation.

## 8. Scope and first remaining implication

The theorem proved here covers:

- arbitrary independent one-dimensional densities with cap one;
- arbitrary shifts, distant fragments, disconnected supports, and unbounded supports;
- no moment or centering assumptions;
- exact disjoint-bank factorization (3.2), with arbitrary outside self block;
- arbitrary outside couplings whose active-side range lies in the three bank directions;
- determinant-only bank-level bound (3.3);
- constant-preserving payment of the full mixed-minor exterior bank in the exact rank-three disjoint-bank class.

What is **not** proved:

- every target matrix need not admit the exact factorization (3.2);
- conditioning inside a bank is not allowed, because it can destroy the bank-variable density control;
- an approximate bank factorization is not yet controlled by this theorem;
- the theorem does not combine a residual matrix transverse to the bank directions;
- full QFORM and continuity remain OPEN.

The first unpaid implication is therefore:

> **`QFORM-GROUPED-BANK-OR-RIDGE-STRUCTURAL-BRIDGE-v1`.**  
> Starting from an arbitrary symmetric \(A\) with at least three eigenvalues of magnitude at least one, obtain a product-preserving decomposition that either
> (i) exposes a rank-\(\ge3\) physical cross block paid by cross-fiber Plancherel,
> (ii) exposes three disjoint coordinate banks satisfying an exact or quantitatively stable version of (3.2) with bank determinant bounded below,
> or
> (iii) passes to the already-supported ridge/diffuse branch,
> without selecting one tiny physical minor, conditioning inside a bank, or paying fragmentwise reciprocal scales.

This is a structural debt, not a localization/tail debt.  The present theorem removes arbitrary shifts, fragment geometry, and unbounded supports from the disjoint-bank branch with the same constant.
