# B15 — KL-preserving mesh-band compression of the FEI arithmetic remainder

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated mathematical/cognitive brain retrieval or receiver-context use was available in this derivation.  
**Route:** APPROACHES 4/8 — mass-weighted Fourier-coefficient depth, with an explicit sharp-Hod counterexample criterion.  
**Fresh source frontier before the derivation:** `master` was re-resolved at `6bb4d5709d42e2e10584a36e13d70fc86a0c9745` after reading the 21 September owner continuation and the current B15 packet/free-energy, punctured-subcube, tensor-collision continuations.

This run does **not** rerun the settled read-once certificate and does not audit another FEI report. It attacks the next B15 obligation left explicitly by the punctured-subcube continuation: replace the failed one-bin normalizer by a mass-aware packet partition that retains the negative KL credit.

## 1. Inherited exact packet free energy

For each distinct nonzero Fourier magnitude `a`, keep the inherited notation

\[
A_a=\{S:|\widehat f(S)|=a\},\qquad
p_a=|A_a|a^2,
\]
\[
V_a=\sum_{S\in A_a}\operatorname{sgn}(\widehat f(S))\chi_S,
\qquad
r_a=\min_{V_a(x)\ne0}\nu_2(V_a(x)),
\]
\[
b_a=a2^{r_a}\in(0,1],\qquad
N_a=|A_a|4^{-r_a}=\frac{p_a}{b_a^2}.
\]

The inherited arithmetic remainder is

\[
\mathcal D(f)=\sum_a p_a\log_2\frac1{b_a},
\]

and the exact free-energy identity from the preceding B15 work is

\[
2\mathcal D=\log_2N-D_{\rm KL,2}(p\|q),
\qquad
N=\sum_aN_a,
\qquad
q_a=\frac{N_a}{N}.
\tag{1}
\]

The punctured-subcube family proves that replacing (1) by the raw bound `2D<=log N`, even after multiplying a residual normalizer by the nonconstant spectral mass, loses a `Theta(n)` KL cancellation. The tensor-collision continuation separately proves that `D` is not unconditionally tensor-subadditive. Both obstructions are preserved below.

Put

\[
X_a:=\log_2\frac1{b_a}.
\tag{2}
\]

Then `N_a=p_a2^{2X_a}`, so `q` is exactly the exponential tilt of `p` by the one-dimensional statistic `X`:

\[
q_a=\frac{p_a2^{2X_a}}{\mathbb E_p2^{2X}}.
\tag{3}
\]

This observation is the starting point of the new reduction.

---

## 2. PROVED: exact coarse-grained free-energy identity

Let `pi` be **any** partition of the packet labels into bins `B_j`. Define

\[
P_j=\sum_{a\in B_j}p_a,\qquad
M_j=\sum_{a\in B_j}N_a,
\qquad
Q_j=\frac{M_j}{N}.
\]

For empty bins omit the term, and define the coarse free energy

\[
\boxed{
\mathcal F_\pi(f)
:=\frac12\sum_jP_j\log_2\frac{M_j}{P_j}
=\frac12\bigl[\log_2N-D_{\rm KL,2}(P\|Q)\bigr].
}
\tag{4}
\]

### Theorem 2.1 — `B15-KL-PRESERVING-COARSE-GRAINING`

For every Boolean `f` and every packet partition `pi`, exactly

\[
\boxed{
\mathcal F_\pi(f)-\mathcal D(f)
=\frac12\sum_jP_j
 D_{\rm KL,2}\!\left(p(\cdot\mid B_j)\middle\|q(\cdot\mid B_j)\right)
\ge0.
}
\tag{5}
\]

If `pi'` refines `pi`, then

\[
\boxed{
\mathcal D(f)\le \mathcal F_{\pi'}(f)\le\mathcal F_\pi(f).
}
\tag{6}
\]

### Proof

Apply the chain rule for relative entropy to the deterministic map `a -> j`:

\[
D_{\rm KL}(p\|q)
=D_{\rm KL}(P\|Q)
+\sum_jP_jD_{\rm KL}(p(\cdot\mid B_j)\|q(\cdot\mid B_j)).
\]

Subtract this from (1) and divide by two. This gives (5). Data processing says refinement can only increase the retained coarse KL, hence (6). `□`

**Interpretation.** The one-bin relaxation killed by the punctured-subcube example is precisely `pi={all packets}`. It discards *all* of the negative KL credit. Refining the packet partition monotonically restores that credit; no sign, collision, valuation, or unequal-magnitude hypothesis is changed.

---

## 3. PROVED: narrow mesh-depth bins lose only a dimension-free quadratic amount

Fix `delta>0` and bin packets by actual normalized mesh depth `X_a`, for example

\[
B_j=\{a:j\delta\le X_a<(j+1)\delta\},\qquad j=0,1,2,\ldots.
\tag{7}
\]

This is a partition by **`X=log_2(1/b)`**, not by a raw denominator exponent. Thus a large odd numerator, such as in the punctured-subcube high packet, is not accidentally charged as deep merely because its unreduced Walsh denominator is large.

### Theorem 3.1 — `B15-MESH-BAND-LOSS`

For the partition (7),

\[
\boxed{
0\le\mathcal F_\delta(f)-\mathcal D(f)
\le\frac{\ln2}{4}\,\delta^2.
}
\tag{8}
\]

The bound is independent of the dimension, the number of packets, their magnitudes, and all valuation/carry behavior.

### Proof

Inside a nonempty bin, let expectation be under the conditional law `p(\cdot|B_j)`. By (3),

\[
D_{\rm KL,2}(p_j\|q_j)
=\log_2\mathbb E 2^{2X}-2\mathbb E X
=\frac1{\ln2}\log\mathbb E e^{2\ln2(X-\mathbb EX)}.
\tag{9}
\]

The conditional variable `X` lies in an interval of length at most `delta`. Hoeffding's lemma gives

\[
\log\mathbb E e^{\lambda(X-\mathbb EX)}
\le\frac{\lambda^2\delta^2}{8}.
\]

With `lambda=2 ln 2`, (9) gives

\[
D_{\rm KL,2}(p_j\|q_j)\le\frac{\ln2}{2}\delta^2.
\]

Insert this in (5) and use `sum_j P_j=1`. `□`

This is stronger than the informal statement that sufficiently fine bins “retain most of the KL credit”: the loss is explicit and uniform.

---

## 4. PROVED: an influence-relative one-dimensional reduction

For a nonconstant Boolean function set, for any `epsilon>0`,

\[
\delta_\epsilon(f)
:=2\sqrt{\frac{\epsilon I(f)}{\ln2}}.
\tag{10}
\]

Let `F_epsilon(f)` denote the coarse free energy (4) for the mesh-depth bins (7) with this width. Theorem 3.1 immediately gives

\[
\boxed{
\mathcal D(f)\le\mathcal F_\epsilon(f)
\le\mathcal D(f)+\epsilon I(f).
}
\tag{11}
\]

For constants put all quantities equal to zero.

Let

\[
C_D=\sup_f\frac{\mathcal D(f)}{I(f)},
\qquad
C_\epsilon=\sup_f\frac{\mathcal F_\epsilon(f)}{I(f)}.
\]

Then

\[
\boxed{
C_D\le C_\epsilon\le C_D+\epsilon.
}
\tag{12}
\]

The inherited isolation theorem proves the exact universal relation

\[
C_H:=\sup_f\frac{H(f)}{I(f)}=2C_D.
\tag{13}
\]

Consequently

\[
\boxed{
C_H=2\lim_{\epsilon\downarrow0}C_\epsilon.
}
\tag{14}
\]

This is a genuine reduction of the **optimal full FEI constant** to a one-dimensional, mass-aware histogram of the actual packet mesh depth `X=log_2(1/b)`. It is not itself a bound on `C_epsilon`, so full FEI remains open.

### Sharp-Hod criterion

Let

\[
\beta:=\beta(1/2)=6.4547837\ldots,
\qquad \beta/2=3.22739185\ldots.
\]

Using (11)--(14):

- proving, for every `epsilon>0` and every Boolean `f`,
  \[
  \mathcal F_\epsilon(f)\le(\beta/2+\epsilon)I(f)
  \tag{15}
  \]
  would prove the sharp full-FEI conjecture `C_H=beta` (the opposite inequality is Hod's lower bound);
- conversely, a single Boolean `f` satisfying
  \[
  \boxed{
  \mathcal F_\epsilon(f)>(\beta/2+\epsilon)I(f)
  }
  \tag{16}
  \]
  would imply `D(f)>(beta/2)I(f)` by (11), hence `C_D>beta/2`, and by the inherited isolation theorem `C_H>beta`. Thus (16) is a rigorous finite **counterexample criterion for Hod's proposed universal sharp constant**, though it is not a counterexample to FEI itself.

This supplies APPROACHES 8 with a lower-dimensional search statistic that does not throw away the arithmetic/KL information exposed by B15.

---

## 5. Mandatory obstruction tests

The new reduction was tested on the exact packet formulas of the two families that killed previous normalizer shortcuts. These are checks of the new formulas, not exhaustive FEI searches.

### 5.1 Punctured codimension-c subcube

For the inherited family `f_{n,c}=1-2 1_{B\{0}}`, the three relevant packet meshes are the constant packet, the high packet, and the exponentially fine low packet. At `epsilon=0.01`, the adaptive widths in (10) separate all three packets in the examples below, so the conditional KL term in every bin is zero and

\[
\mathcal F_\epsilon=\mathcal D
\]

exactly up to floating-point display error. In particular the `Theta(n)` cancellation between the raw normalizer and global KL is **not lost**.

| family | `I` | `D/I` | `F_epsilon/I` |
|---|---:|---:|---:|
| `c=3,n=8` | 0.765625 | 1.4762868 | 1.4762868 |
| `c=3,n=12` | 0.7529297 | 1.4793488 | 1.4793488 |
| `c=3,n=20` | 0.7500267 | 1.4779610 | 1.4779610 |
| `c=4,n=20` | 0.5000229 | 1.7012382 | 1.7012382 |

Thus the exact family that makes `v log N_perp/I` diverge remains harmless for the banded statistic.

### 5.2 One-point defect

For `f_n=1-2 1_{0}`, the two packet meshes are also separated at the same adaptive resolution. Hence again `F_epsilon=D` in the tested cases:

| `n` | `I` | `D/I` | `F_epsilon/I` |
|---:|---:|---:|---:|
| 8 | 0.0625 | 1.9213913 | 1.9213913 |
| 16 | 0.00048828125 | 1.9651357 | 1.9651357 |
| 24 | 2.8610e-6 | 1.9767788 | 1.9767788 |

This is important because `I` tends to zero: using a fixed additive coarse-graining error would be useless here, while the adaptive width (10) makes the information loss `O(epsilon I)`.

### 5.3 Tensor-collision obstruction is preserved

The fleet04 B15 example proves that valuation-misaligned equal-product-magnitude collisions can make `D(f\otimes g)>D(f)+D(g)`. Nothing in Theorems 2.1--3.1 assumes tensor subadditivity or replaces the true output packet valuation. The statistic is computed from the final packet meshes `b_a`, after every collision and carry. Thus that counterexample remains valid and is not silently bypassed.

---

## 6. Numerical verifier

`verify_mesh_band_reduction.py` checks (8) directly on 5,000 deterministic pseudo-random finite packet laws and on the exact one-point/punctured-subcube packet formulas above. The largest observed ratio

`(F_delta-D) / ((ln 2) delta^2/4)`

was `0.4625151812203136`; no violation occurred. At `epsilon=0.01`, every structured example above satisfied the stronger adaptive target `F-D<=epsilon I` and, because its packets fell in separate bins, had zero loss to numerical precision.

These computations only test the algebra implemented by the script; Theorems 2.1 and 3.1 are analytic.

---

## 7. What moved, what did not, and next attack

### PROVED in this run

1. Any packet partition has the exact KL chain-rule identity (5).
2. Refinement monotonically decreases the coarse free energy to the exact arithmetic remainder.
3. Binning by actual mesh depth `X=log_2(1/b)` with width `delta` loses at most `(ln 2)delta^2/4`, independent of dimension and packet count.
4. Choosing `delta` proportional to `sqrt(I)` turns this into an arbitrarily small **influence-relative** loss.
5. Together with the inherited equality `C_H=2C_D`, the optimal FEI constant is exactly the limit of the one-dimensional banded constants (14), and (16) is a rigorous search certificate against the conjectural sharp Hod constant.

### NOT proved

- No universal bound on `F_epsilon/I` is proved.
- No counterexample to Hod's constant was found here.
- No tensor-subadditivity claim is revived.
- No automatic integrality, bounded carry depth, fixed physical lattice, or structured-class representation is assumed.
- Full FEI remains OPEN.

### Next B15 attack

The high-dimensional packet problem has now been reduced, up to `epsilon I`, to the one-dimensional mesh-depth bins **without sacrificing the essential KL cancellation**. The next nonoverlapping question is therefore precise:

> For the adaptive bins (10), can one charge each coarse term
> \[
> \frac12P_j\log_2(M_j/P_j)
> \]
> to Fourier influence using only Booleanity and neighboring-bin carry constraints, with total coefficient at most `beta/2+o(1)`?

A decisive failure mode would be an explicit Boolean family for which `F_epsilon/I` exceeds `beta/2+epsilon`; by (16) that would rigorously refute Hod's constant as the universal sharp FEI constant. Any proposed payment must be tested first on the punctured-subcube family and the valuation-misaligned tensor-collision example, because one-bin counting and unconditional tensor subadditivity are already false.

## Literature boundary

A current primary-literature check during this run found the May 2026 restriction/stopping-tree paper of González--MacManus--Pereyra and the September 2026 plateaued-function paper of Potapov. The latter proves sharp constant 4 for plateaued functions; neither source is used here to claim publication priority for the mesh-band reduction. **No novelty/priority claim is made.**
