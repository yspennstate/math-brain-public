# B14 FEI posterior-crossing strategy — variance selector and short-circuit subcube stopping

**Date:** 21 September 2026  
**Status:** **PARTIAL / new universal posterior-crossing selector plus a paid adaptive stopping branch. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; the authentic `math_brain` package was not importable in this runtime, and no brain-assisted claim is made.  
**Role/interface:** Joint FEI interface A: realizable adaptive restriction.  
**Novelty/publication priority:** unverified; no novelty claim is made.

## 1. Exact predecessors consumed

This run uses the current joint order and, substantively, the newest applicable fleet01/B18 work rather than restarting the route.

1. `fleet01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md`, blob
   `ef9f471c019a7d81e9864fd457a0e4bae9da890d`.  In a median-centered state,
   with
   \[
   \mathcal P=\sum_i\mathfrak j(p_i),\qquad
   \mathcal F=H-\mathcal P,
   \]
   it proves
   \[
   \Delta_A\mathcal F\le
   B_A-\sum_{j\notin A}\mathfrak j'(p_j)c_j(A)
   \tag{1.1}
   \]
   and, on an \(\mathcal F/\mathcal J\)-critical core of ratio \(\rho\),
   \[
   \sum_{j\notin A}(\rho+\mathfrak j'(p_j))c_j(A)
   \le \sum_{i\in A}[h_2(p_i)-\rho p_i].
   \tag{1.2}
   \]
   This is the exact source-to-next-arrow interface used below: a lower bound on *actual*
   posterior crossings becomes a restriction-criticality obstruction without asserting a
   prescribed-coordinate payment.

2. The newer `fleet01/B18/20260921T2100Z-prefix-tc-refund/REPORT.md`, blob
   `21547dcdb11438c03b38ddb30d10c371d8cd99be`, proves the all-witness Palm/prefix
   information refund and isolates the remaining prefix dependence/factorial term
   \[
   R_{\rm pref}=I\,{\rm TC}(P)-\mathbb E\log_2(K!).
   \tag{1.3}
   \]
   Its high-depth branch is the intended recipient of the mixed-depth quantity obtained
   below.  I do **not** drop the total-correlation term.

3. `fleet02/interactive/20260921T192650Z-joint-fei-subcube-peeling/ADDENDUM.md`,
   blob `baa3155a268d936d6b191667ee71a6df84969292`, Theorem C.1: if a pivot
   sensitivity support is within \(2^{-r}/(16r)\) of a codimension-\(r\) coordinate
   subcube \(Q\), and its defining physical controls \(Z\) satisfy
   \(I_Z\le r I_x\), then
   \[
   \Delta_ZH\le 12 I_Z.
   \tag{1.4}
   \]
   The fixed-relative \(1/16\) replacement is known false and is not used.

4. The addressing obstruction
   `solo-2026-09-17/ADDRESSING_BARRIER_2026-09-18.md`, blob
   `c1e52dff50095854d85c20e8b13a5385d91efaca`, remains in force.  Nothing below
   claims that every prescribed coordinate or every prescribed block is cheap.

Throughout \(f:\{-1,1\}^n\to\{-1,1\}\) is character-centered so
\[
p_j=\operatorname{Inf}_j(f)\le\tfrac12,\qquad
\mathcal J(f)=\sum_jp_j=:J.
\]
For a physical restriction block \(A\), write
\[
c_j(A)=\mathbb E(2p_j(X_A)-1)_+,\qquad
C_A=\sum_{j\notin A}c_j(A),
\]
so the exact folded block drift remains
\[
\boxed{D_A=J-\mathbb E J(f_{A=X_A})=I_A+C_A.}
\tag{1.5}
\]

## 2. A sharp posterior-variance lower bound for majority crossing

The earlier work mostly upper-bounded crossing or produced it from near-subcube
geometry.  The following scalar inequality gives a general lower bound.

### Lemma 2.1 — posterior variance forces crossing

Let \(U\in[0,1]\) satisfy \(\mathbb EU=p\le1/2\), and set
\[
c(U)=\mathbb E(2U-1)_+.
\]
Then
\[
\boxed{
c(U)\ge
2\left[\operatorname{Var}(U)-p\left(\tfrac12-p\right)\right]_+.
}
\tag{2.1}
\]

**Proof.**
For every \(u\in[0,1]\),
\[
(2u-1)_+\ge 2u^2-u.
\tag{2.2}
\]
For \(u\le1/2\) the right side is nonpositive; for \(u\ge1/2\) the difference
between the two sides is \((2u-1)(1-u)\ge0\).  Taking expectations gives
\[
c(U)\ge2\mathbb E U^2-p
=2\operatorname{Var}(U)+2p^2-p.
\]
Combine with \(c(U)\ge0\).  Equality in the pointwise inequality occurs at
\(u\in\{0,1/2,1\}\).  QED.

This applies to **any** physical restriction sigma-field and, without change, to
a stopped physical decision tree: take \(U\) to be the posterior pivotality
probability at the leaf.

## 3. Bernoulli reveal curve and a universal mass-weighted block selector

Let
\[
\eta_j(x)=1_{\{f(x)\ne f(x^{\oplus j})\}}
\]
be the \(j\)-pivotality indicator.  It does not depend on \(x_j\), has mean
\(p_j\), and has Walsh expansion on the other coordinates
\[
\eta_j=\sum_S\widehat\eta_j(S)\chi_S.
\]

Define the explained-variance curve
\[
V_j(t)=\sum_{S\ne\varnothing}\widehat\eta_j(S)^2t^{|S|},
\quad
R(t)=\sum_jV_j(t),
\tag{3.1}
\]
and the total pivotality Fourier depth
\[
\boxed{
M:=R'(1)=
\sum_j\sum_{S\ne\varnothing}|S|\,\widehat\eta_j(S)^2.
}
\tag{3.2}
\]
Equivalently, with the standard Walsh normalization,
\[
M=\frac14\sum_j\sum_{k\ne j}\operatorname{Inf}_k(\eta_j),
\tag{3.3}
\]
so \(M\) is a genuine mixed-face/pivotality-depth quantity, not an abstract
spectral-law parameter.

Let \(A_t\) include each physical coordinate independently with probability
\(t\).  For a survivor \(j\notin A_t\), conditioning on \(X_{A_t}\) retains each
nonconstant Walsh coefficient of \(\eta_j\) with probability \(t^{|S|}\).
Therefore
\[
\mathbb E\operatorname{Var}
\bigl(\mathbb E[\eta_j\mid X_{A_t\setminus\{j\}}]\bigr)
=V_j(t).
\tag{3.4}
\]

Put
\[
T:=\sum_jp_j(\tfrac12-p_j).
\]
Lemma 2.1, summed over surviving coordinates, gives
\[
\boxed{
\mathbb E C_{A_t}\ge
2(1-t)[R(t)-T]_+.
}
\tag{3.5}
\]

Now
\[
R(1)=\sum_jp_j(1-p_j)=T+\frac J2,
\tag{3.6}
\]
and \(R(t)\) is convex because it is a nonnegative combination of powers
\(t^k\).  Hence its tangent at \(1\) gives
\[
R(t)\ge R(1)-(1-t)M.
\tag{3.7}
\]
Combining (3.5)--(3.7),
\[
\boxed{
\mathbb E C_{A_t}\ge
(1-t)\,[J-2(1-t)M]_+.
}
\tag{3.8}
\]

Since every nonconstant term in \(R(1)\) has degree at least one,
\(M\ge R(1)\ge J/2\).  Therefore the legal choice
\[
s_*:=1-t_*=\frac{J}{4M}\le\frac12
\tag{3.9}
\]
yields
\[
\boxed{
\mathbb E C_{A_{t_*}}\ge\frac{J^2}{8M}.
}
\tag{3.10}
\]
Also \(\mathbb E I_{A_{t_*}}=t_*J\).  By the ratio-of-sums principle, there is
at least one **actual physical block** \(A\) in the support of this Bernoulli
law for which
\[
\boxed{
C_A\ge
\frac{J}{8M-2J}\,I_A,
\qquad
D_A=I_A+C_A
\ge\left(1+\frac{J}{8M-2J}\right)I_A.
}
\tag{3.11}
\]

This is an existential, influence-mass-weighted block selector.  It is deliberately
not a prescribed-coordinate statement, so it does not collide with addressing.

### Corollary 3.2 — a new critical-core product obstruction

Assume now that \(f\) is an \(\mathcal F/\mathcal J\)-critical centered core of
ratio \(\rho>2\).  Fleet01/B18 defines \(\sigma(\rho)\) by
\[
h_2(\sigma)/\sigma=\rho
\]
and
\[
\kappa(\rho)=\mathfrak j'(\sigma(\rho))>0.
\]
Its theorem implies \(\mathfrak j'(p_j)\ge\kappa(\rho)\) for every active
coordinate.  Define the total scalar marginal slack
\[
S_\rho:=\sum_i[h_2(p_i)-\rho p_i].
\tag{3.12}
\]
Average (1.2) over \(A_{t_*}\).  The right side averages to
\(t_*S_\rho\), while (3.10) lower-bounds the crossing side.  Thus
\[
\boxed{
S_\rho
\ge
(\rho+\kappa(\rho))
\frac{J^2}{8M-2J}.
}
\tag{3.13}
\]
Equivalently,
\[
\boxed{
(8M-2J)S_\rho\ge
(\rho+\kappa(\rho))J^2.
}
\tag{3.14}
\]

This is the exact new source-to-next-arrow use of the curvature refund.  A hard
critical core cannot simultaneously have small scalar Shannon slack and small
mixed pivotality depth.  If \(M=O(J)\), the curvature-refunded crossing mechanism
forces \(S_\rho=\Omega(J)\).  If \(M/J\) is large, the obstruction is transferred
to the mixed-depth/high-depth branch that the newest fleet01/B18 Palm/prefix
report is designed to attack.  No second-factorial-moment quantity is silently
declared \(O(J)\).

## 4. A realizable short-circuit stopping tree for near-subcube rows

The fixed-block crossing theorem says that a near-subcube row produces crossing
when all defining controls are revealed.  The same crossing can be realized by
a much shallower **adaptive** physical tree.

Let \(E=\{\eta_j=1\}\) have density \(p\), and let
\[
Q=\{X_{i_1}=a_1,\ldots,X_{i_r}=a_r\},
\qquad q=2^{-r},
\]
be a coordinate subcube, with
\[
\delta=\mu(E\triangle Q).
\]
Query \(i_1,i_2,\ldots,i_r\) in that order, but stop immediately at the first
mismatch with the defining literal of \(Q\); query all \(r\) bits only on the
all-match branch.

### Theorem 4.1 — short-circuit crossing

For this stopped physical tree,
\[
\boxed{
\mathbb E\tau=2(1-2^{-r})<2
}
\tag{4.1}
\]
and, writing \(U_\tau=\Pr(E\mid\text{stopped leaf})\),
\[
\boxed{
\mathbb E(2U_\tau-1)_+\ge(p-\delta)_+.
}
\tag{4.2}
\]

**Proof.**
The \(t\)-th query is reached exactly when the first \(t-1\) defining literals
match, so \(\Pr(\tau\ge t)=2^{-(t-1)}\).  Summing gives (4.1).

The all-match leaf is exactly \(Q\).  Its contribution alone to crossing is
\[
q\left(2\frac{\mu(E\cap Q)}q-1\right)_+
=(2\mu(E\cap Q)-q)_+.
\]
Since
\[
\delta=p+q-2\mu(E\cap Q),
\]
this equals \((p-\delta)_+\).  Other leaves contribute nonnegatively.  QED.

For the pivotality event \(\eta_j\), \(j\notin Q\)'s defining coordinates, the
\(j\)-coordinate contribution to folded influence has an exact stopped-tree
identity:
\[
\mathbb E\min(U_\tau,1-U_\tau)
=\mathbb E[U_\tau-(2U_\tau-1)_+]
=p-\mathbb E(2U_\tau-1)_+.
\tag{4.3}
\]
Hence the stopping tree creates at least \((p-\delta)_+\) of **real folded
influence drift in the surviving pivot itself**.

This does not contradict the sharp fixed-block depth obstruction: the successful
leaf still has depth \(r\); adaptivity makes the *average* number of physical
queries less than two.

## 5. A genuine O(J) unpaid-Shannon branch

The stopping tree above becomes an actually paid FEI step under the already
proved near-support hypothesis from fleet02's Theorem C.1.

Assume the defining controls \(Z\) obey
\[
I_Z\le rI_j,
\qquad
\delta\le 2^{-r}/(16r).
\tag{5.1}
\]
Then the full physical \(Z\)-restriction satisfies
\[
\Delta_ZH\le12I_Z.
\tag{5.2}
\]

The full \(Z\)-restriction tree extends the short-circuit tree by continuing to
query the remaining defining coordinates on mismatch leaves.  Every additional
physical split has nonnegative expected spectral-entropy decrement because
\(\Delta_iH=B_i+JS_i\) with both terms nonnegative.  Therefore
\[
\Delta_{\rm stop}H\le\Delta_ZH.
\tag{5.3}
\]
If
\[
B_{\rm stop}
\]
denotes the sum, with actual node-reach probabilities, of the Shannon erasure
terms \(B_i\) on the stopped tree, then \(B_i\le\Delta_iH\) nodewise and thus
\[
\boxed{
B_{\rm stop}\le\Delta_{\rm stop}H
\le12I_Z
\le12J.
}
\tag{5.4}
\]

Together with (4.2)--(4.3), this is a **realizable adaptive stopping policy whose
total unpaid Shannon erasure is \(O(J)\)** and which retains the near-maximal
posterior-crossing refund of the near-subcube pivot.  The policy is proved only
in the currently certified \(q/(16r)\)-support-error branch; I do not extend it
to the refuted fixed-relative \(1/16\) regime.

The gain over mechanically revealing all \(r\) controls is not a stronger
constant in (5.4); it is that the same paid branch can be represented as a
stopping tree with expected query count below two and with an explicit surviving
pivot crossing at the terminal success leaf.  This is the form needed for a
future nonreusing adaptive selector.

## 6. What this changes and what remains open

### Proved here

1. The sharp posterior variance-to-majority-crossing lower bound (2.1).
2. The Bernoulli-reveal crossing curve (3.5) and universal lower envelope (3.8).
3. The explicit mass-weighted existential physical block selector (3.11).
4. The curvature-refunded critical-core product obstruction (3.13)--(3.14).
5. The short-circuit near-subcube stopping tree: expected depth \(<2\), crossing
   at least \(p-\delta\), and exact surviving-pivot folded-drift interpretation.
6. Under the existing certified \(2^{-r}/(16r)\) near-support hypothesis, the
   short-circuit tree has total unpaid Shannon erasure at most \(12J\).

### Not proved

- There is still no universal theorem that every dangerous FEI core contains a
  row satisfying the near-support hypothesis in Section 5.
- Large \(M/J\) is **not** declared paid.  Equation (3.14) creates a genuine
  A/B-interface dichotomy: low mixed depth forces curvature-refunded scalar
  slack; high mixed depth must be spent by the Palm/\(\Gamma\), prefix-remainder,
  or quantitative mixed-derivative machinery.
- The short-circuit policy alone does not prove a universal \(B_{\rm stop}=O(J)\)
  for a merely fixed-relative near-subcube approximation; the existing
  counterexample to the corresponding full-block shortcut is preserved.
- Full FEI remains OPEN / NOT PROVED.

### Exact next arrow

Use (3.14) with fleet01/B18's newest source-exact prefix inequality
\[
H(f)\le5J+JH(p/J)-\Gamma(f)+R_{\rm pref}(f)
\tag{6.1}
\]
in the centered gauge.  The next target is to prove that the high-\(M/J\) branch
necessarily contributes a commensurate amount either to \(\Gamma\), to a
telescoping decrease of \(R_{\rm pref}\), or to a realizable near-subcube
short-circuit family whose paid trees can be scheduled without reusing the same
\(J\)-drop.  This is narrower than full FEI and directly joins the two current
fleet01/B18 outputs.

## 7. Executed checks

`check_posterior_variance_short_circuit.py` was executed with only the Python
standard library.

- Exact event/block check of Lemma 2.1 through event dimension four:
  **628,572** cases, **0** violations; **433,636** equality cases.
- Deterministic seed-1404 Boolean check of the optimized aggregate selector in
  dimensions 2--4: **403** nondegenerate centered functions, maximum violation
  **0**, and maximum error in \(R(1)=T+J/2\) **0** in the recorded float path.
- Exact short-circuit event/subcube check through dimension three:
  **6,756** cases, **0** crossing violations and **0** depth-identity errors.

Checker SHA-256:
`675e7d3446ea5395c261bfb8ba482f3cef0d1d10ea21f073ea6d86db935a9ae6`.

Captured stdout SHA-256:
`82b62f54d6a98fa762ec6f636c429c3774882b7333ae489cdf310794fa2d50d8`.

These checks support the algebra but are not a proof of full FEI.
