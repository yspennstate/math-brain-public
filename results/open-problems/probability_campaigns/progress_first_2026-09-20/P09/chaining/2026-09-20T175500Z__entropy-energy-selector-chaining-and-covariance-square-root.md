Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but this runtime does not expose an authenticated GPT-6/maximum-effort selector.

# P09 progress-first run — entropy-energy selector chaining, a hard-entropy counterexample, and covariance square-root control

**Status: PROVED PARTIAL.** This report does **not** solve Randomstrasse101 Conjecture 16 for arbitrary deterministic symmetric tensors. In the unresolved regime `2 <= p < 2r`, the fixed full-source metric remains

```text
old arbitrary exponent = 1/2 - 1/(2r),
new arbitrary exponent = 1/2 - 1/(2r),
target exponent        = 1/2 - 1/p.
```

The substantive advance is a correction and strengthening of the immediately preceding selector-entropy route. The predecessor proved a hard-error quantization/chaining theorem for the canonical KKT witness `B(g)` and proposed a polylogarithmic hard quantization entropy profile. This run proves that such a hard-error profile cannot be the universal missing lemma: even a completely standard matrix Gaussian series can have a continuously distributed selected witness with `Omega(d)` hard quantization entropy at a small scale while the tensor norm remains `O(1)` under the exact source normalization.

The replacement keeps the **energy of each selected refinement**, not merely its worst-case radius. Three new pieces are proved:

1. an entropy-energy Gaussian selector inequality in which each refinement costs `sqrt(L2-energy * Shannon-entropy)`;
2. an RMS rate-distortion chaining reduction for the actually selected exposed output `Y(g)`, which automatically discounts high-dimensional geometry occurring only at very small amplitude;
3. a covariance square-root inequality
   `E <g,Y(g)> <= Tr((E YY^T)^(1/2))`, yielding a genuinely broader continuous covariance-structure class and a second route to the target exponent.

The new full-source bottleneck is therefore not a uniform hard covering/entropy bound. It is to prove an **amplitude-weighted selector complexity bound** — either an RMS rate-distortion integral or a trace-square-root bound for the Gaussian-selected exposed output.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Registered role: `chaining / geometric-probabilistic proof`
- Repository / branch: private `yspennstate/math-open-problems`, `master`
- Immediate predecessor: `probability_campaigns/progress_first_2026-09-20/P09/chaining/2026-09-20T165800Z__canonical-kkt-barycenter-and-selection-entropy-chaining.md`.
- Historical C0035 material, all earlier P09 reports, and peer-owned files are preserved. This report is additive and immutable.

---

## 1. Source target and continuity with the strongest recovered general results

Primary source: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizić-Nikolac, A. Rödder et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 16.

For symmetric deterministic order-`r` tensors `T_1,...,T_n` on `R^d`, iid standard Gaussians `g_i`, and

```text
||T||_(I_p)
 := max_(||x||_p<=1) | <T,x^(tensor r)> |,
```

the source asks for

```text
E ||sum_i g_i T_i||_(I_p)
 <= C(r,p) polylog(d,n) d^(1/2-1/p)
    (sum_i ||T_i||_(I_p)^2)^(1/2).                       (1.1)
```

Write

```text
alpha := 1/2 - 1/p,
S^2   := sum_i ||T_i||_(I_p)^2.                           (1.2)
```

The bounded current-primary check for this assignment continues to recover:

- Randomstrasse101, arXiv:2603.29571, Conjecture 16;
- Bandeira--Gopi--Jiang--Lucca--Rothvoss, arXiv:2411.10633, as the geometric/covering baseline for correlated random tensors;
- Ishaq Aden-Ali, arXiv:2503.10580, as the PAC-Bayesian improvement of the general correlated-tensor bound.

Aden-Ali's Theorem 1.2 / Corollary 1.4 controls the expected injective norm by a hierarchy of contraction/Frobenius variance parameters and explicitly notes that the proof is still volumetric in the regimes where the extra Frobenius terms dominate. Nothing in this run relabels the matrix, rank-one, independent-entry, or `p>=2r` cases as new.

No full resolution of the exact arbitrary deterministic `2 <= p < 2r` statement was found in the bounded source check already performed for this P09 assignment. This is not a claim about unpublished or unindexed work.

---

## 2. Inherited exposed-output and KKT witnesses

Let `\widetilde T_i` be the symmetric `r`-linear polarization of the diagonal polynomial of `T_i`. Define

```text
F(x) := (\widetilde T_i(x,...,x))_i in R^n,              (2.1)
```

and

```text
h(g) := sup_(||x||_p<=1) |<g,F(x)>|.                     (2.2)
```

For `h(g)>0`, choose measurably a sign `sigma(g)` and a maximizing `x(g)` on the `l_p` sphere so that

```text
sigma <g,F(x)> = h(g).                                    (2.3)
```

Two selected vectors from the predecessor will be used.

### 2.1 The actual exposed output

Set

```text
Y(g) := sigma(g) F(x(g)).                                 (2.4)
```

Then exactly

```text
boxed:
h(g)=<g,Y(g)>.                                           (2.5)
```

Moreover, by the source normalization, for every `x in B_p^d`,

```text
||F(x)||_2^2
 = sum_i |T_i[x^r]|^2
 <= sum_i ||T_i||_(I_p)^2
 = S^2.                                                   (2.6)
```

Hence

```text
boxed:
||Y(g)||_2 <= S.                                         (2.7)
```

This radius is smaller than the KKT-barycenter radius and will matter below.

### 2.2 The canonical KKT barycenter

The predecessor also proved that with

```text
J_p(x)_j := |x_j|^(p-2)x_j,
D(x)     := ||J_p(x)||_2^2,
A_x v    := (\widetilde T_i(x^(r-1),v))_i,               (2.8)
```

the vector

```text
b_x := A_x J_p(x)/D(x)                                    (2.9)
```

satisfies

```text
<sigma g,b_x>=h(g),
||b_x||_2 <= kappa_r d^alpha S.                          (2.10)
```

For `p=2`, `b_x=F(x)`, so the two selected vectors coincide.

The hard-error entropy route in the preceding report was formulated for

```text
B(g):=sigma(g)b_(x(g)).                                  (2.11)
```

The present run shows that the hard-error profile proposed there is too rigid for the arbitrary problem, even when `B=Y`.

---

## 3. Counterexample: universal polylogarithmic hard selector entropy is false

This counterexample uses the already-known matrix regime only as a falsification test for the **intermediate selector-entropy lemma**. No matrix theorem is claimed as new.

Take

```text
r=2,
p=2,
input dimension m>=3.                                    (3.1)
```

Let `S_0^m` denote the real traceless symmetric `m x m` matrices, and let

```text
M := dim S_0^m = m(m+1)/2 - 1.                           (3.2)
```

Choose a Frobenius-orthonormal basis

```text
B_1,...,B_M in S_0^m.                                    (3.3)
```

Since `||B_a||_op <= ||B_a||_F=1`, define deterministic symmetric matrices

```text
T_0 := I_m,
T_a := epsilon B_a,
1<=a<=M,                                                  (3.4)
```

where for concreteness

```text
epsilon:=m^(-2).                                         (3.5)
```

### 3.1 Exact source normalization remains constant

For matrices in the `p=2` injective norm,

```text
||T_0||_(I_2)=1,
||T_a||_(I_2)<=epsilon.                                  (3.6)
```

Therefore

```text
S^2
 <= 1 + M epsilon^2
 = 1+O(m^(-2)),                                           (3.7)
```

so `S asymp 1`.

### 3.2 The random matrix norm is `O(1)`

Let

```text
H:=sum_(a=1)^M g_a B_a.                                  (3.8)
```

The Gaussian tensor is the symmetric matrix

```text
G_T = g_0 I_m + epsilon H.                               (3.9)
```

Hence

```text
||G_T||_op
 <= |g_0| + epsilon ||H||_op.                            (3.10)
```

For the orthogonally invariant traceless Gaussian symmetric ensemble,

```text
E||H||_op <= C sqrt(m).                                  (3.11)
```

Thus

```text
boxed:
E||G_T||_op = O(1).                                      (3.12)
```

This is fully consistent with the known matrix case.

### 3.3 The selected witness has a continuously distributed high-dimensional fine component

Because the law of `H` is invariant under orthogonal conjugation, its eigenvectors are Haar distributed modulo sign, independently of the eigenvalue labels. Adding `g_0 I_m` changes eigenvalues but not eigenvectors. The operator norm selects either a top or bottom eigenvector according to the extreme absolute eigenvalue. Since the selection rule depends only on eigenvalues and is conjugation-equivariant, the selected projective eigenvector

```text
X in RP^(m-1)                                             (3.13)
```

has Haar/projective-uniform law.

For `p=2`, the canonical KKT witness equals the exposed output. Up to the selected overall sign,

```text
Y
 = (1,
    epsilon (X^T B_a X)_(a=1)^M ).                       (3.14)
```

The fine component is the traceless quadratic Veronese embedding of `RP^(m-1)` scaled by `epsilon`.

For any unit `x,y`, since `xx^T-yy^T` is traceless,

```text
sum_a (x^T B_a x - y^T B_a y)^2
 = ||xx^T-yy^T||_F^2
 = 2(1-<x,y>^2).                                         (3.15)
```

Thus the fine selected-witness metric is exactly

```text
||Y_fine(x)-Y_fine(y)||_2
 = epsilon sqrt(2(1-<x,y>^2)).                           (3.16)
```

### 3.4 Lower bound on hard-error quantization entropy

Let `Q(Y)` be any finite-valued quantizer satisfying

```text
||Y-Q(Y)||_2 <= delta
almost surely,                                           (3.17)
```

with

```text
0<delta<=c epsilon.                                      (3.18)
```

Any one quantizer cell can contain only projective points lying in a projective ball of radius `O(delta/epsilon)`, because two points in the same cell are at output distance at most `2delta` and (3.16) converts that into projective angular distance.

A Haar projective ball of small radius `rho` has probability at most

```text
(C rho)^(m-1).                                           (3.19)
```

Consequently every quantizer atom has probability

```text
p_atom
 <= (C delta/epsilon)^(m-1).                             (3.20)
```

For every discrete law, Shannon entropy obeys

```text
H(Q(Y))
 = sum_a p_a log(1/p_a)
 >= log(1/p_max).                                        (3.21)
```

Therefore

```text
boxed:
H(Q(Y))
 >= (m-1) log(c epsilon/delta).                          (3.22)
```

In particular, at `delta=epsilon/100`,

```text
boxed:
H_Y^hard(epsilon/100) >= c m.                            (3.23)
```

Yet the process has expectation `O(1)` and `S asymp1`.

### 3.5 Consequence for the previous proposed universal lemma

The preceding report proposed, as a sufficient route, a hard-error profile of schematic form

```text
H_B^hard(delta)
 <= polylog(d,n)^2 [1+log(R_*/delta)]^2.                 (3.24)
```

The example above shows that such a profile cannot be the **universal** missing theorem. Here `R_*=O(1)`, while at `delta=Theta(m^-2)` the left side is `Omega(m)` and the right side is only a fixed polylogarithm of `m` for any fixed polylogarithmic exponent.

The issue is not a large process. The high-dimensional geometry lives at amplitude only `epsilon=m^-2`.

This is the exact obstruction that the new entropy-energy chaining theorem removes.

---

## 4. New lemma: entropy-energy cost of one adaptive Gaussian vector

The predecessor bounded a finite-valued selected vector using its worst-case radius. Retaining its **mean squared size** gives a strictly stronger inequality.

### Lemma 4.1 — Gaussian conditional mean shift

Let

```text
G~N(0,I_n),                                               (4.1)
```

and let `E` be a measurable event of probability `pi>0`. Then

```text
boxed:
||E[G|E]||_2 <= sqrt(2 log(1/pi)).                       (4.2)
```

#### Proof

Let

```text
u:=E[G|E]/||E[G|E]||_2                                   (4.3)
```

when the conditional mean is nonzero. For any `lambda>0`, conditional Jensen and the Gaussian moment generating function give

```text
pi exp(lambda <nu,E[G|E]>)
 <= E[1_E exp(lambda<nu,G>)]
 <= E exp(lambda<nu,G>)
 = exp(lambda^2/2).                                      (4.4)
```

Thus

```text
||E[G|E]||_2
 <= log(1/pi)/lambda + lambda/2.                         (4.5)
```

Optimize at `lambda=sqrt(2log(1/pi))`. QED.

### Theorem 4.2 — entropy-energy selector inequality

Let `V=V(G)` be any finite-valued `R^n`-valued measurable function of `G`. Then

```text
boxed:
E <G,V>
 <= sqrt( 2 E||V||_2^2 H(V) ).                          (4.6)
```

Here `H(V)` is the Shannon entropy of the discrete selected law.

#### Proof

Let `V=v_a` on the events `E_a`, with probabilities `pi_a`. Then by Lemma 4.1,

```text
E<G,V>
 = sum_a pi_a <E[G|E_a],v_a>
 <= sqrt(2) sum_a pi_a ||v_a||_2 sqrt(log(1/pi_a)).       (4.7)
```

Cauchy--Schwarz yields

```text
(sum_a pi_a ||v_a|| sqrt(log(1/pi_a)))^2
 <= (sum_a pi_a ||v_a||^2)
    (sum_a pi_a log(1/pi_a))
 = E||V||^2 H(V).                                        (4.8)
```

This proves (4.6). QED.

### Why this is stronger than the predecessor's radius form

If `||V||<=R` then (4.6) recovers

```text
E<G,V> <= R sqrt(2H(V)).                                 (4.9)
```

But if the complicated selected values have small amplitude, (4.6) pays their RMS energy rather than the largest possible norm. This is exactly what the counterexample in Section 3 requires.

---

## 5. Main new theorem: entropy-energy selector chaining

### Theorem 5.1 — L2 adaptive selector chaining

Let

```text
G~N(0,I_n)                                               (5.1)
```

and let `B=B(G)` be square-integrable. Let

```text
Q_0:=0,Q_1,Q_2,...                                       (5.2)
```

be finite-valued measurable functions of `G` such that

```text
Q_k -> B in L2.                                          (5.3)
```

Set

```text
Delta_k:=Q_k-Q_(k-1),                                    (5.4)
```

and

```text
e_k:=E||Delta_k||_2^2,
h_k:=H(Q_(k-1),Q_k).                                     (5.5)
```

Then

```text
boxed:
E<G,B>
 <= sqrt(2) sum_(k>=1) sqrt(e_k h_k),                    (5.6)
```

whenever the right side is finite.

#### Proof

Each `Delta_k` is finite-valued and is a deterministic function of the pair `(Q_(k-1),Q_k)`, hence

```text
H(Delta_k)<=h_k.                                         (5.7)
```

Applying Theorem 4.2 gives

```text
E<G,Delta_k>
 <= sqrt(2 e_k h_k).                                     (5.8)
```

For finite `K`,

```text
Q_K=sum_(k=1)^K Delta_k,                                 (5.9)
```

so

```text
E<G,Q_K>
 <= sqrt(2) sum_(k=1)^K sqrt(e_k h_k).                   (5.10)
```

Finally, because `Q_K->B` in `L2`,

```text
E|<G,Q_K-B>|
 <= (E||G||_2^2)^(1/2)
    (E||Q_K-B||_2^2)^(1/2)
 ->0                                                     (5.11)
```

for the fixed finite output dimension `n`. Let `K->infinity`. QED.

### Interpretation

This is the selector analogue of chaining with a crucial change:

```text
old cost per level:
worst radius * sqrt(entropy),

new cost per level:
RMS increment size * sqrt(entropy).                      (5.12)
```

Large entropy is harmless if it appears only in sufficiently small-energy refinements.

---

## 6. RMS rate-distortion formulation

Hard-error entropy is the wrong universal object. Define instead the mean-square rate-distortion entropy

```text
R_B(delta)
 := inf {
          H(Q) :
          Q finite-valued,
          E||B-Q||_2^2 <= delta^2
        }.                                               (6.1)
```

Let

```text
R_2(B):=(E||B||_2^2)^(1/2).                              (6.2)
```

Choose dyadic distortions

```text
delta_k:=2^(-k) R_2(B),
k>=0.                                                     (6.3)
```

For each `k>=1`, choose a finite quantizer `Q_k` with

```text
E||B-Q_k||^2 <= delta_k^2                                (6.4)
```

and entropy arbitrarily close to `R_B(delta_k)`.

Then

```text
E||Q_k-Q_(k-1)||^2
 <= 2delta_k^2+2delta_(k-1)^2
 <= C delta_(k-1)^2.                                    (6.5)
```

Also

```text
H(Q_(k-1),Q_k)
 <= H(Q_(k-1))+H(Q_k).                                   (6.6)
```

Theorem 5.1 therefore yields the rate-distortion chain

```text
boxed:
E<G,B>
 <= C sum_(k>=1)
      delta_(k-1)
      sqrt(
        R_B(delta_(k-1))
        +R_B(delta_k)
      ).                                                 (6.7)
```

The arbitrarily small optimization errors in the entropies may be chosen summably and then removed.

### The correct selector complexity functional

Define

```text
J_sel(B)
 := sum_(k>=1)
      delta_(k-1)
      sqrt(
        1+R_B(delta_(k-1))+R_B(delta_k)
      ),                                                 (6.8)
```

with `delta_k=2^-k R_2(B)`. Then

```text
boxed:
E<G,B> <= C J_sel(B).                                    (6.9)
```

Up to absolute constants and dyadic discretization, `J_sel` is the RMS rate-distortion analogue of a Dudley entropy integral.

The decisive difference from the predecessor's hard profile is that entropy appearing only below a tiny amplitude scale is multiplied by that tiny scale.

---

## 7. Application to P09 using the actual exposed output

Use the selected exposed output `Y(g)` from (2.4), not the larger KKT barycenter. Recall

```text
h(g)=<g,Y(g)>,
||Y(g)||_2<=S.                                           (7.1)
```

Therefore

```text
R_2(Y)<=S.                                               (7.2)
```

### Corollary 7.1 — RMS selector-rate reduction for Conjecture 16

If

```text
boxed:
J_sel(Y)
 <= C(r,p) d^(1/2-1/p) S polylog(d,n),                  (7.3)
```

then

```text
boxed:
E||sum_i g_iT_i||_(I_p)
 <= C'(r,p) d^(1/2-1/p) S polylog(d,n).                  (7.4)
```

This is an exact full-source reduction, not a solution.

### Why (7.3) is materially weaker than the previous hard-entropy target

The previous condition asked for a polylogarithmic bound on the entropy at **every hard scale**, regardless of how much selected energy lived there. Condition (7.3) allows, for example,

```text
R_Y(delta) = Theta(m log(epsilon/delta))
for delta << epsilon,                                    (7.5)
```

provided the entire high-entropy part has amplitude `epsilon` small enough that

```text
epsilon sqrt(m)
```

is acceptable.

This is exactly the geometry of the matrix counterexample in Section 3.

---

## 8. Calibration: the continuous matrix selector is cheap in entropy-energy

Return to Section 3. Split the selected output schematically as

```text
Y=Y_anchor+Y_fine,                                       (8.1)
```

where `Y_anchor` takes only the two sign values in the identity coordinate and

```text
||Y_fine||_2 <= epsilon.                                 (8.2)
```

At scales below `epsilon`, the projective manifold has metric dimension `m-1`, so its rate-distortion entropy is of order

```text
R_(Y_fine)(delta)
 <= C m log(C epsilon/delta).                            (8.3)
```

A dyadic chain below `epsilon` therefore costs at most

```text
C sum_(k>=0)
  epsilon 2^(-k)
  sqrt(m(1+k))
 <= C' epsilon sqrt(m).                                  (8.4)
```

For `epsilon=m^-2`, this is

```text
O(m^(-3/2)).                                              (8.5)
```

The anchor costs only an absolute constant. Thus the entropy-energy chain sees the continuous `Omega(m)` fine-scale hard entropy but charges it at its true tiny amplitude.

This is the behavior the arbitrary P09 proof needs: high-dimensional fine structure must be allowed when its selected output energy is correspondingly small.

---

## 9. A second new inequality: covariance square-root control

The selector distribution also admits a simple but useful covariance bound that requires **no discretization at all**.

### Theorem 9.1 — Gaussian adaptive covariance inequality

Let `G~N(0,I_n)` and let `Y=Y(G)` be any square-integrable random vector. Define its uncentered second-moment matrix

```text
Sigma_Y:=E[YY^T].                                        (9.1)
```

Then

```text
boxed:
E<G,Y>
 <= Tr(Sigma_Y^(1/2)).                                   (9.2)
```

#### Proof

Diagonalize `Sigma_Y` in an orthonormal basis `u_1,...,u_n`, with eigenvalues `lambda_j>=0`. Rotational invariance makes

```text
G_j:=<G,u_j>
```

standard normal. Write

```text
Y_j:=<Y,u_j>.                                             (9.3)
```

Then

```text
E Y_j^2=lambda_j.                                        (9.4)
```

Termwise Cauchy--Schwarz gives

```text
E[G_jY_j]
 <= |E[G_jY_j]|
 <= sqrt(EG_j^2 EY_j^2)
 = sqrt(lambda_j).                                       (9.5)
```

Summing over `j` proves (9.2). QED.

### Equivalent block-covariance interpretation

The joint second-moment block matrix of `(G,Y)` is positive semidefinite. If

```text
K:=E[GY^T],                                               (9.6)
```

then its Schur complement gives

```text
K^T K <= Sigma_Y.                                        (9.7)
```

When `K` is positive semidefinite, as it is for smooth exposed-output selectors after Gaussian integration by parts, (9.2) can also be viewed as

```text
Tr K <= Tr sqrt(Sigma_Y).                                (9.8)
```

The elementary proof above does not require smoothness.

---

## 10. New continuous covariance-structure theorem for P09

Apply Theorem 9.1 to the exposed output `Y(g)=sigma F(x(g))`. By (2.5),

```text
E||sum_i g_iT_i||_(I_p)
 = E<g,Y>.                                                (10.1)
```

Therefore

```text
boxed:
E||sum_i g_iT_i||_(I_p)
 <= Tr((E YY^T)^(1/2)).                                  (10.2)
```

Since `||Y||<=S`,

```text
Tr(EYY^T)=E||Y||^2<=S^2.                                (10.3)
```

Define the selector covariance effective dimension

```text
d_eff(Y)
 := [Tr((EYY^T)^(1/2))]^2
    / Tr(EYY^T)                                           (10.4)
```

when the denominator is nonzero.

Then

```text
boxed:
E||sum_i g_iT_i||_(I_p)
 <= S sqrt(d_eff(Y)).                                    (10.5)
```

Consequently:

### Corollary 10.1 — covariance-effective-dimension class

If

```text
d_eff(Y)
 <= C(r,p)
    d^(1-2/p)
    polylog(d,n)^2,                                      (10.6)
```

then

```text
boxed:
E||sum_i g_iT_i||_(I_p)
 <= C'(r,p)
    d^(1/2-1/p)
    S polylog(d,n).                                      (10.7)
```

This is a **restricted theorem**, not the full conjecture.

### Why this is genuinely broader than the earlier deterministic classes

Condition (10.6) does not require:

- a common tangent frame;
- commuting covariance matrices;
- low deterministic contraction rank;
- a finite selected witness set;
- low hard covering entropy;
- a finite branch dictionary;
- or independent tensor entries.

The selector may have continuous full-rank support. Only the amplitude-weighted spectrum of its **actual Gaussian-selected output covariance** matters.

An even weaker direct condition is simply

```text
Tr((EYY^T)^(1/2))
 <= C(r,p)d^alpha S polylog(d,n),                         (10.8)
```

which permits very large effective rank whenever the total selected energy is small.

---

## 11. Spectral-layer form: high rank is allowed at small amplitude

Let the eigenvalues of `Sigma_Y` be

```text
lambda_1>=lambda_2>=...>=0.                              (11.1)
```

Then

```text
Tr sqrt(Sigma_Y)=sum_j sqrt(lambda_j).                   (11.2)
```

Group eigenvalues into dyadic amplitude layers

```text
I_q
 := {j:
      2^(-(q+1))S < sqrt(lambda_j)
      <=2^(-q)S}.                                        (11.3)
```

Writing `m_q:=|I_q|`,

```text
boxed:
Tr sqrt(Sigma_Y)
 <= S sum_(q>=0) 2^(-q)m_q.                              (11.4)
```

Thus a sufficient spectral-counting target for the arbitrary problem is

```text
sum_q 2^(-q)m_q
 <= C(r,p)d^alpha polylog(d,n).                           (11.5)
```

This formulation makes the new lesson explicit: a huge number of selected output modes is harmless if they occur only at sufficiently small RMS amplitude.

The earlier hard-entropy target ignored exactly this amplitude factor.

---

## 12. Falsification tests for the new criteria

### 12.1 Hadamard hypercube

In the predecessor's normalized Hadamard-hypercube example, the `p=2` selected output takes `2^m` sign-code values in an `m`-dimensional output subspace with approximately isotropic covariance

```text
Sigma_Y approx I_m/m.                                    (12.1)
```

Therefore

```text
Tr sqrt(Sigma_Y)
 approx sqrt(m)
 = Theta(sqrt(log d)),                                   (12.2)
```

matching the necessary logarithmic growth.

The covariance criterion does **not** incorrectly erase the genuine sign-code complexity.

### 12.2 Continuous tiny-amplitude matrix selector

In Section 3, the fine selected geometry has dimension `m-1` but amplitude `epsilon=m^-2`. The hard-error entropy at relative fine scale is `Omega(m)`, while the entropy-energy cost is only `O(epsilon sqrt(m))` at that scale.

The covariance square-root criterion also remains bounded because the fine covariance trace is `O(epsilon^2)` and its eigenvalues are spread over the quadratic harmonic sector.

Thus both new criteria correctly tolerate continuous high-dimensional geometry at tiny amplitude.

### 12.3 Zero-process rotating-column example

The previous zero-process example had dramatic tangent rotation with no actual output movement on the relevant slice. For the exposed-output selector, zero output contributes zero `L2` increment energy and zero covariance. Hence the new criteria charge it nothing.

### 12.4 Dense dust

A large number of tiny selected directions contribute according to their RMS energy in Theorem 5.1 and according to the square roots of their covariance eigenvalues in Theorem 9.1. They are no longer charged at the radius of the largest branch.

### 12.5 Auxiliary randomized sketches

The new objects are functions of the **actual selected output law**. No auxiliary Haar sketch or external random partition is inserted into the selector, so artificial entropy generated by proof randomness is avoided.

---

## 13. A multiscale mixed structural theorem

The entropy-energy and covariance inequalities can be combined componentwise.

Suppose the exposed output admits a measurable decomposition

```text
Y=sum_(q>=0) Y_q                                          (13.1)
```

with convergence in `L2`. For each component choose either:

- a finite-valued description with entropy `H_q`, or
- its covariance matrix `Sigma_q:=E[Y_qY_q^T]`.

Then linearity and Theorems 4.2 / 9.1 give

```text
E<G,Y>
 <= sum_q min {
      sqrt(2 E||Y_q||^2 H_q),
      Tr(Sigma_q^(1/2))
    },                                                   (13.2)
```

where the first option is used only when `Y_q` is finite-valued (or after a finite quantization).

Therefore the source exponent follows for any tensor family admitting an exposed-output decomposition satisfying

```text
sum_q min {
  sqrt(2 E||Y_q||^2 H_q),
  Tr(Sigma_q^(1/2))
}
 <= C(r,p)d^alpha S polylog(d,n).                         (13.3)
```

This class permits exponentially many fine branches, continuous components, noncommuting tangent geometry, and scale-dependent descriptions. It strictly contains the earlier finite-dictionary situation because a component with enormous support may be paid for through covariance instead of branch count.

Again, this is a restricted structural theorem, not a claim that (13.3) has been proved for arbitrary tensors.

---

## 14. What this says about the volumetric obstruction

The low-`p` volumetric barrier can now be separated into two distinct failures of naive covering.

### Failure A: nonexistent geometry

Raw tangent or critical-atom covers pay for directions that Gaussian optimization never selects. The anchored cubic counterexample from the predecessor demonstrated this.

### Failure B: wrong amplitude

Even the **actual selected witness** may have large hard covering entropy at a fine scale while carrying tiny RMS energy there. Section 3 demonstrates this with a continuous matrix selector.

A successful arbitrary proof must therefore be both

```text
selection-aware
and
amplitude-aware.                                         (14.1)
```

The new entropy-energy chain is exactly both.

The covariance trace-square-root inequality is a complementary amplitude-aware formulation with no discretization.

---

## 15. Remaining full-source gap

The full conjecture is not solved. The arbitrary exponent is unchanged.

The sharpened obligations are now:

### Obligation A — RMS selector rate-distortion

Prove directly for

```text
Y(g)=sigma(g)F(x(g))                                     (15.1)
```

that

```text
J_sel(Y)
 <= C(r,p)d^alpha S polylog(d,n).                         (15.2)
```

Unlike the previous hard profile, (15.2) allows high information at tiny amplitude.

### Obligation B — selector covariance trace-root

Alternatively prove

```text
Tr((EYY^T)^(1/2))
 <= C(r,p)d^alpha S polylog(d,n).                         (15.3)
```

This is a deterministic-looking second-moment target for the **selected** output distribution and may be approachable through KKT/coarea.

Neither (15.2) nor (15.3) has been proved for arbitrary deterministic tensors here.

---

## 16. Next concrete attack

The next run should not return to uniform hard covering numbers. It should attack the amplitude-weighted selector law directly.

### 16.1 First branch: KKT-conditioned second moments

For an orthonormal output direction `u`, define the combined tensor

```text
T_u:=sum_i u_i T_i.                                      (16.1)
```

The selector covariance quadratic form is

```text
u^T Sigma_Y u
 = E[ T_u[x(g)^r]^2 ].                                   (16.2)
```

Use the KKT relation

```text
A_x^* g = sigma h(g) J_p(x)                              (16.3)
```

and the Gaussian normal-cone law to bound how many orthogonal directions `u` can simultaneously have large values in (16.2). The target is a dyadic eigenvalue-count inequality strong enough to imply (11.5).

This is more concrete than counting critical points: it asks for the number of **selected output covariance modes above a specified RMS threshold**.

### 16.2 Second branch: coarea by amplitude layer

Reuse the earlier Kac--Rice/coarea cancellation only after restricting to a covariance/energy layer

```text
|T_u[x^r]| approx 2^-q S.                                (16.4)
```

The previous work showed that inverse curvature cancels against the critical-field Jacobian on regular image sheets and that switching strata are weighted by actual output chords. The new goal is to integrate **squared output amplitude** or a covariance trace on a layer, not raw branch multiplicity.

### 16.3 Third branch: one-slot contraction energy

Because

```text
T_u[x^r]=<A_x^*u,x>,                                     (16.5)
```

large selector covariance in many orthogonal output directions should force many large one-slot contractions at selected points. Attempt a Bessel/square-function inequality after conditioning on the KKT normal direction. If this fails, search for a tensor family realizing many large orthogonal selected covariance modes while keeping the source sum `S^2` fixed; such a construction would directly falsify (15.3) as the universal route.

### 16.4 Mandatory countertests

Any proposed covariance/rate-distortion lemma must survive:

1. the Hadamard hypercube, where `sqrt(log d)` is genuine;
2. the continuous tiny-amplitude matrix selector in Section 3, where hard entropy is `Omega(d)` at fine scale but amplitude is tiny;
3. the anchored cubic raw-atom counterexample;
4. the zero-process rotating-column construction;
5. the dense-dust example;
6. the previous global-Haar-sketch example.

### 16.5 Pivot rule

The previous run changed method to selector entropy; this run found a counterexample to the **hard** entropy profile and replaced it by energy-weighted selector complexity. If the next two runs fail to obtain a nontrivial bound on either (15.2) or (15.3), preserve this reduction and hand off to another registered probability bottleneck as directed by the owner policy.

---

## 17. Obligation ledger

| Item | Before this run | After this run |
|---|---|---|
| Full arbitrary exponent in `2<=p<2r` | `1/2-1/(2r)` | unchanged |
| Target exponent | `1/2-1/p` | unchanged |
| Selected object | canonical KKT witness `B(g)` | **actual exposed output `Y(g)` used whenever possible, radius `S`** |
| Proposed selector complexity | hard-error entropy at every scale | **refuted as a universal target** |
| New counterexample | raw critical-atom width can be huge | **continuous Haar/projective selected witness with `Omega(d)` fine-scale hard entropy but `O(1)` process** |
| Chaining inequality | worst-error radius times `sqrt(entropy)` | **RMS increment energy times `sqrt(entropy)`** |
| New rate-distortion object | hard quantization entropy | **mean-square selector rate-distortion integral `J_sel`** |
| New covariance inequality | none | **`E<g,Y> <= Tr((EYY^T)^(1/2))`** |
| New restricted class | low selector hard rate | **amplitude-weighted selector covariance / entropy-energy classes** |
| Remaining gap | polylog hard selector entropy | **KKT control of amplitude-weighted selected modes** |

---

## 18. Status

**PROVED PARTIAL.** The full Randomstrasse101 Conjecture 16 remains open here, and the arbitrary polynomial exponent has not improved.

The mathematical progress is a sharper correction of the volumetric obstruction:

- universal hard selector entropy is falsified by an explicit matrix Gaussian series with a continuous high-dimensional selected witness at tiny amplitude;
- a stronger entropy-energy Gaussian selector inequality is proved;
- a full RMS rate-distortion chaining theorem is proved;
- the P09 target is reduced to an amplitude-weighted selector complexity integral for the actual exposed output;
- an independent covariance square-root inequality is proved and yields a broad continuous covariance-structure theorem;
- the next arbitrary bottleneck is localized to controlling the RMS spectrum or rate-distortion of the KKT-selected output law, not to covering all algebraically possible branches.

No known special case is called a full solution, and all conditional/restricted statements are labeled accordingly.