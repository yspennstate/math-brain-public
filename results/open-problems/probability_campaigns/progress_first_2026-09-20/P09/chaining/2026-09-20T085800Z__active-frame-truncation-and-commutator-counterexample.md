Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime does not provide authenticated GPT-6/maximum attestation.

# P09 progress-first run — inactive rotations refute the commutator route; active spectral frames are the right entropy object

**Status: PROVED PARTIAL.** This report does **not** solve Randomstrasse101 Conjecture 16 for arbitrary deterministic tensors. The fixed full-source polynomial exponent remains

```text
gamma = 1/2 - 1/(2r)
```

in the unresolved range `2 <= p < 2r`, instead of the conjectured

```text
alpha = 1/2 - 1/p.
```

The run materially changes the route from the preceding report.

1. I give an explicit symmetric order-`r` tensor family showing that the predecessor's proposed small-commutator implication for the **top-k** tangent ranges is false, even inside the actual tensor tangent geometry. One can have exponentially many critical-angle-separated rank-one tangent frames while the normalized covariance commutators are arbitrarily small.

2. The failure is diagnosed exactly: those rotating directions can have singular values far below the critical scale `tau_k = S/sqrt(k)`. Tracking the formal top-`k` singular vectors therefore counts geometry that contributes essentially nothing to the process at that scale.

3. I replace the top-`k` frame criterion by an **active spectral frame criterion**. At scale `k`, discard every singular direction below `c tau_k`. This loses only `c d^alpha S/sqrt(k)` in process distance, while the surviving active range has dimension at most `k/c^2`. Thus only above-threshold frame entropy matters.

4. This yields a strictly broader proved structured class than pairwise commuting tangent covariances: the conjectured polynomial exponent holds whenever, scale by scale, the **active** tangent ranges share a finite/common frame up to critical angular error. The low singular spectrum may rotate arbitrarily, may fail to commute, and the frame may change with scale.

5. Finally, every active output direction `u` forces the combined tensor `sum_i u_i T_i` to have source injective norm at least `c_r S/sqrt(k)`. This converts the remaining inverse problem into a source-normalized large-norm-subspace entropy problem and removes the basis-free commutator quantity that the counterexample invalidates.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Installed title: `Gaussian Tensor Bounds`
- Repository / branch: private `yspennstate/math-open-problems`, `master`
- Pre-write master captured: `7d594b14f30e10214780fbd57fc3521a53c7038e`
- Immediate P09 predecessor: `probability_campaigns/progress_first_2026-09-20/P09/chaining/2026-09-20T082200Z__operator-lipschitz-ridge-and-finite-frame-entropy.md`, creation commit `9747a1daf144a97c7d13543c81bfe2caeb29fff7`, blob `3f6dd57a2e5ef25a55f7405668563e2099bd25b6`.
- Historical C0035 material, all earlier P09 reports, and all peer files are preserved.

## 1. Source and current-status checkpoint

Source: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizic-Nikolac, A. Rodder et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Entry 8, Conjecture 16.

The source uses the symmetric diagonal injective norm

```text
||T||_I_p := sup_{||x||_p <= 1} |T[x,...,x]|.
```

For symmetric tensors, real polarization compares this with the full `r`-linear injective norm up to constants depending only on `r`. I keep that distinction explicit below whenever a mixed evaluation `T[x^(r-1),v]` is used.

The source target is

```text
E ||sum_i g_i T_i||_I_p
 <= C(r,p) polylog(d,n) d^(1/2-1/p)
    (sum_i ||T_i||_I_p^2)^(1/2).
```

A bounded fresh primary-source check on 20 September 2026 found the source still recording Conjecture 16. The strongest general baselines recovered remain:

- Bandeira--Gopi--Jiang--Lucca--Rothvoss, arXiv:2411.10633 / STOC 2025: general geometric tensor concentration, yielding polynomial exponent `1/2 - 1/max{p,2r}` up to logarithms.
- Ishaq Aden-Ali, arXiv:2503.10580: stronger PAC-Bayesian variance-parameter inequality, but still volumetric in the arbitrary correlated low-`p` regime.
- The source itself records the matrix, rank-one, independent-entry and `p>=2r` situations separately from the unresolved arbitrary deterministic regime.

No later primary result resolving the exact arbitrary deterministic `2<=p<2r` source statement was recovered in this bounded check. This is not a claim about unpublished or unindexed work.

The full-source metric therefore remains

```text
old arbitrary exponent = gamma = 1/2 - 1/(2r)
new arbitrary exponent = gamma = 1/2 - 1/(2r)
target exponent        = alpha = 1/2 - 1/p
status                 = OPEN / not solved here
```

A material post-predecessor handoff was also inspected: RS-2026-CL-A commit `6203d78de928c736c8f8bf22c50750a695996aaf` supplies a finite Hermite-tail/read-k lemma. It is conditional on a useful low-degree local representation and does not by itself control the deterministic active-frame entropy below, so it is not imported as a proof step.

## 2. Inherited exact tangent normalization

Set

```text
S^2 := sum_i ||T_i||_I_p^2,
F(x) := (T_i[x,...,x])_i,
(A_x v)_i := T_i[x,...,x,v],
```

with `r-1` copies of `x` in `A_x v`. The predecessor proved, in the source normalization up to the fixed polarization convention,

```text
F(x)=A_x x,
||F(x)||_2 <= S,
||A_x||_HS <= C_r S,
```

and, using the full multilinear norm convention for the tangent statement, the constant can be taken as one after the fixed `r`-dependent polarization conversion. Since only dimension exponents matter here, write

```text
||A_x||_HS <= C_r S.                                      (2.1)
```

All constants below may absorb this fixed `C_r`.

For the ridge scale

```text
tau_k := S/sqrt(k),
epsilon_k := d^alpha tau_k = d^alpha S/sqrt(k),            (2.2)
```

the predecessor constructed a ridge skeleton with `O(epsilon_k)` pointwise error. It then proposed controlling the formal top-`k` left singular range

```text
L_x(k) = range of the top-k left singular vectors of A_x.  (2.3)
```

The next section shows that this range is too fine an object: it can rotate exponentially through directions whose singular values are negligible compared with `tau_k`.

## 3. Counterexample to the proposed small-commutator/top-k-frame lemma

The preceding report proposed, as a target to prove or refute, a statement of the schematic form

```text
small pairwise ||[C_x,C_y]|| relative to tau_k^4
    => an exp(k polylog)-sized dictionary for L_x(k),       (3.1)
```

where

```text
C_x := A_x A_x^*.
```

I now refute this route inside the actual symmetric-tensor tangent model.

### 3.1. The tensor family

Fix `r>=3`. Write `d=m+1`, let

```text
b := e_1 in R^d,
H := span{e_2,...,e_d} ~= R^m.
```

Index the Gaussian-summand/output coordinates by ordered tuples

```text
I=(i_1,...,i_(r-1)) in [m]^(r-1),
```

so the number of tensors is

```text
n=m^(r-1).
```

For each `I`, let `T_I` be the unique symmetric `r`-linear form whose diagonal polynomial is

```text
P_I(z)
 := z_1 product_(a=1)^(r-1) z_(i_a+1).                    (3.2)
```

Equivalently, `T_I` is the symmetrization of

```text
b tensor e_(i_1+1) tensor ... tensor e_(i_(r-1)+1)
```

with the normalization chosen so that `T_I[z^r]=P_I(z)`.

### 3.2. The source denominator is polynomially large in this representation

For every `I`, clearly

```text
||T_I||_I_2 <= 1.                                         (3.3)
```

There is also a lower bound depending only on `r`. Let the distinct coordinates occurring in `I` have multiplicities

```text
m_1,...,m_t,
```

with `sum_j m_j=r-1`. Choose a unit vector `z` with

```text
z_1^2=1/r,
z_(j-th used coordinate)^2=m_j/r,
```

and all other coordinates zero. Then

```text
|P_I(z)|
 = r^(-r/2) product_j m_j^(m_j/2)
 >= r^(-r/2).                                             (3.4)
```

Therefore

```text
r^(-r) m^(r-1) <= S^2 <= m^(r-1),                         (3.5)
```

where

```text
S^2=sum_I ||T_I||_I_2^2.
```

Thus

```text
S ~=_r m^((r-1)/2).                                       (3.6)
```

### 3.3. On a hyperplane, every tangent map is rank one and its output line is a tensor-power feature

Take `x in H` with `||x||_2=1`. Since `x_1=0`, differentiating (3.2) in direction `v` gives

```text
D P_I(x)[v]
 = (b^T v) product_(a=1)^(r-1) x_(i_a+1).                 (3.7)
```

For a symmetric degree-`r` polynomial,

```text
D P_I(x)[v] = r T_I[x^(r-1),v].                           (3.8)
```

Hence

```text
(A_x v)_I
 = (1/r) (b^T v)
   product_(a=1)^(r-1) x_(i_a+1).                         (3.9)
```

Let

```text
w_x := x_H^(tensor (r-1)) in R^(m^(r-1)).                 (3.10)
```

Because `||x_H||_2=1`,

```text
||w_x||_2=1.
```

Equation (3.9) becomes the exact rank-one factorization

```text
A_x = (1/r) w_x b^T.                                      (3.11)
```

Therefore the unique nonzero singular value is

```text
s_x=1/r,                                                   (3.12)
```

and

```text
C_x=A_x A_x^*
    =(1/r^2) w_x w_x^T.                                   (3.13)
```

Thus for every `k>=1`, the predecessor's formal top-`k` left range is simply

```text
L_x(k)=span{w_x}.                                          (3.14)
```

### 3.4. Exponentially many separated tangent lines with tiny commutators

For sign vectors

```text
x_sigma := (0,sigma_1,...,sigma_m)/sqrt(m),
sigma in {+-1}^m,                                         (3.15)
```

we have

```text
<w_xsigma,w_xtau>
 = <x_sigma,x_tau>^(r-1).                                 (3.16)
```

Fix any `mu in (0,1/2)`. A standard random-code argument gives a set

```text
Sigma subset {+-1}^m,
|Sigma| >= exp(c mu^2 m),                                 (3.17)
```

such that every distinct pair satisfies

```text
|<x_sigma,x_tau>| <= mu.                                  (3.18)
```

For completeness: for two independent sign vectors, Hoeffding gives

```text
P(|<x_sigma,x_tau>|>mu) <= 2 exp(-mu^2 m/2).
```

Taking `N=floor(exp(mu^2 m/16))` independent codewords and union-bounding over the `N^2` pairs gives positive probability of (3.18) for large `m`.

Set

```text
rho_(sigma,tau)
 := <w_xsigma,w_xtau>.
```

Then

```text
|rho_(sigma,tau)| <= mu^(r-1).                            (3.19)
```

For rank-one orthogonal projectors `P_u=uu^T`, `P_v=vv^T`,

```text
||P_u-P_v||_op = sqrt(1-|<u,v>|^2),                       (3.20)
```

and

```text
||[P_u,P_v]||_op
 = |<u,v>| sqrt(1-|<u,v>|^2).                             (3.21)
```

Using (3.13), every two covariance matrices in the code satisfy

```text
||[C_xsigma,C_xtau]||_op
 <= r^(-4) mu^(r-1),                                      (3.22)
```

while their top singular lines obey

```text
||P_(L_xsigma(k))-P_(L_xtau(k))||_op
 >= sqrt(1-mu^(2r-2)).                                    (3.23)
```

So the top singular lines contain an `exp(c mu^2 m)` constant-angle packing even though the covariance commutators are uniformly as small as we wish by choosing `mu` small.

### 3.5. It directly violates the predecessor's normalized commutator proposal

At scale `k`,

```text
tau_k=S/sqrt(k).
```

By (3.5),

```text
tau_k^4
 >= r^(-2r) m^(2r-2)/k^2.                                (3.24)
```

Thus on the above code

```text
||[C_x,C_y]||_op / tau_k^4
 <= C_r mu^(r-1) k^2 / m^(2r-2).                          (3.25)
```

Take, for example, any fixed `k>=2`, or more generally any

```text
2 <= k <= m/log m,
```

which lies in the predecessor's `p=2` mesoscopic window for large `m`. Then the right-hand side of (3.25) tends to zero polynomially in `m`, while (3.23) still gives an exponential constant-angle packing of the formal top-`k` ranges.

Consequently a statement of the form proposed in predecessor equation (10.1), using only small normalized commutators, `Tr(C_x)<=S^2`, and the **formal top-`k` ranges**, is false.

This refutes an intermediate method lemma only. It does not refute Conjecture 16.

## 4. Diagnosis: the rotating directions are spectrally inactive

The same example explains why the source conjecture itself is not threatened.

Every tangent map in Section 3 has unique singular value `1/r`, whereas (3.6) gives

```text
tau_k=S/sqrt(k)
 ~=_r m^((r-1)/2)/sqrt(k).                                (4.1)
```

For every `k<=m` and `r>=3`,

```text
s_x/tau_k
 <= C_r sqrt(k)/m^((r-1)/2)
 <= C_r m^((2-r)/2)
 -> 0.                                                     (4.2)
```

So the exponentially rotating singular lines are far **below** the process-critical singular scale. The top-`k` frame criterion from the predecessor was therefore sufficient but unnecessarily strong: it demanded a dictionary for directions that contribute negligibly at the radius being covered.

This suggests the correct repair: define high-leverage geometry by a **singular-value threshold**, not by the ordinal label `top k`.

## 5. New theorem: active spectral truncation loses only the critical radius

Fix `c in (0,1)`. Let

```text
A_x = U_x diag(s_1(x),s_2(x),...) V_x^T
```

be an SVD. Define the right and left active spectral projectors

```text
P_x^(act)(k,c)
 := 1_{[c tau_k,infinity)}((A_x^* A_x)^(1/2)),

Q_x^(act)(k,c)
 := 1_{[c tau_k,infinity)}((A_x A_x^*)^(1/2)),            (5.1)
```

and the active hard skeleton

```text
Y_(k,c)(x)
 := A_x P_x^(act)(k,c) x
  = Q_x^(act)(k,c) F(x).                                  (5.2)
```

Let

```text
L_x^(act)(k,c)
 := range Q_x^(act)(k,c).                                 (5.3)
```

### Theorem 5.1 (active truncation)

For every `x in B_p^d`,

```text
||F(x)-Y_(k,c)(x)||_2
 <= c d^alpha S/sqrt(k)
 = c epsilon_k,                                            (5.4)
```

and

```text
dim L_x^(act)(k,c)
 <= C_r k/c^2.                                             (5.5)
```

Moreover,

```text
||Y_(k,c)(x)||_2 <= ||F(x)||_2 <= S.                      (5.6)
```

#### Proof

On the orthogonal complement of the active right singular space, every singular value of `A_x` is strictly smaller than `c tau_k`. Therefore

```text
||(I-Q_x^(act))F(x)||_2
 = ||A_x(I-P_x^(act))x||_2
 <= c tau_k ||x||_2.                                      (5.7)
```

For `p>=2`,

```text
||x||_2 <= d^(1/2-1/p)||x||_p <= d^alpha.                 (5.8)
```

Equations (5.7)--(5.8) give (5.4).

For (5.5), every active singular value contributes at least `c^2 tau_k^2` to the Hilbert--Schmidt norm. Hence, using (2.1),

```text
(dim L_x^(act)) c^2 tau_k^2
 <= ||A_x||_HS^2
 <= C_r S^2.                                               (5.9)
```

Since `tau_k^2=S^2/k`, this yields (5.5).

Finally `Y_(k,c)(x)` is an orthogonal projection of `F(x)` onto a left singular subspace, so (5.6) is immediate. QED.

### Why this theorem is the right repair

The theorem keeps exactly the singular directions capable of moving the process by the critical scale. Any frame rotation below `c tau_k` is absorbed into the allowed covering radius before a frame dictionary is even considered.

On the counterexample of Section 3, (4.2) implies

```text
L_x^(act)(k,c)={0}
```

throughout the relevant mesoscopic range for large `d`. The exponential fake frame complexity disappears completely.

## 6. Active-frame entropy criterion

The predecessor's finite-frame theorem now has a sharper version.

### Theorem 6.1 (finite active-frame criterion)

Fix `c in (0,1)` and a scale `k`. Suppose there is a collection of fixed output subspaces

```text
W_(k,1),...,W_(k,M_k) subset R^n                         (6.1)
```

with

```text
dim W_(k,a) <= C_0 k/c^2,                                 (6.2)
```

such that for every `x in B_p^d` there is an index `a=a(x)` with

```text
||P_(L_x^(act)(k,c))-P_(W_(k,a))||_op
 <= eta_k,                                                 (6.3)
```

where

```text
eta_k <= c_0 d^alpha/sqrt(k).                              (6.4)
```

Then, for a constant `C=C(r,c,c_0,C_0)`,

```text
log N(F(B_p^d), C epsilon_k B_2^n)
 <= log M_k
    + C (k/c^2)
      log(1+C sqrt(k)/d^alpha).                            (6.5)
```

In particular, if throughout the mesoscopic dyadic scales

```text
log M_k <= C (k/c^2) polylog(d,n),                        (6.6)
```

then the Randomstrasse101 target polynomial exponent `d^alpha` follows, up to polylogarithmic factors, after the same coarse/fine-scale chaining already proved in the predecessor.

#### Proof

By Theorem 5.1, replacing `F(x)` by `Y_(k,c)(x)` costs at most `c epsilon_k`.

For the dictionary subspace `W=W_(k,a(x))`, since `Y_(k,c)(x)` belongs to `L_x^(act)(k,c)` and has norm at most `S`,

```text
||Y_(k,c)(x)-P_W Y_(k,c)(x)||_2
 <= eta_k S
 <= c_0 epsilon_k.                                        (6.7)
```

For fixed `W`, the projected point lies in the Euclidean ball `S B_2` inside a space of dimension at most `C_0 k/c^2`. At radius comparable to `epsilon_k=d^alpha S/sqrt(k)`, this ball has covering number at most

```text
(1+C sqrt(k)/d^alpha)^(C_0 k/c^2).                        (6.8)
```

Take the union over the `M_k` dictionary spaces and add the truncation and angular errors. This proves (6.5). The dyadic chaining consequence is the predecessor's argument with `L_x(k)` replaced by `L_x^(act)(k,c)`. QED.

## 7. A broader proved covariance class: scale-wise active common frames

Pairwise commuting full covariances from the predecessor are sufficient because they give a single common eigenbasis at every singular scale. The active criterion shows that much less is needed.

### Theorem 7.1 (scale-selective active-frame class)

Assume that for each dyadic mesoscopic scale `k` there is an orthonormal basis

```text
U^(k)={u_1^(k),...,u_n^(k)}                               (7.1)
```

such that for every `x`, the active range `L_x^(act)(k,c)` is spanned by a subset of this basis. No condition is imposed on singular directions below `c tau_k`, and the basis `U^(k)` may depend on `k`.

Then

```text
E ||sum_i g_i T_i||_I_p
 <= C_(r,p,c) d^alpha S polylog(d,n).                     (7.2)
```

The same conclusion holds if each active range is only within projector distance

```text
O(d^alpha/sqrt(k))                                        (7.3)
```

of such a coordinate subspace.

#### Proof

By Theorem 5.1, every active range has dimension at most `C_r k/c^2`. For a fixed scale, the number of coordinate subspaces of this dimension in the basis `U^(k)` is at most

```text
sum_(j<=C_r k/c^2) binom(n,j)
 <= exp(C_(r,c) k log(2n)).                               (7.4)
```

If `n=O(k)`, one may simply use the full output space, which also fits the `O(k)` dimensional budget. Thus Theorem 6.1 applies with

```text
log M_k <= C_(r,c) k log(2n).                             (7.5)
```

The predecessor already handles the coarse and near-fine scales and converts these dyadic entropy bounds to the Gaussian-process estimate. QED.

### Strictly broader than full covariance commutation

This hypothesis allows the low singular spectrum to rotate arbitrarily and to fail pairwise commutation. For example, at a fixed scale one may have

```text
C_x = D_x + E_x,                                          (7.6)
```

where the part of `D_x` above `(c tau_k)^2` is diagonal in `U^(k)`, while `E_x` is supported entirely below that threshold and may be an arbitrary noncommuting family. The active-frame theorem ignores `E_x` at the critical radius.

Hence Theorem 7.1 is a genuinely broader covariance-structured partial class than the predecessor's pairwise commuting theorem. No literature-novelty claim is made for this subclass.

## 8. Active directions force large source-norm combined tensors

The active criterion can be expressed without commutators or a chosen eigenbasis.

For `u in R^n`, define the symmetric combined tensor

```text
T(u) := sum_i u_i T_i.                                    (8.1)
```

### Lemma 8.1 (large-norm certificate for every active direction)

There is a constant `c_r>0` depending only on the tensor order such that, for every `x in B_p^d`, every scale `k`, every `c in (0,1)`, and every unit vector

```text
u in L_x^(act)(k,c),                                      (8.2)
```

we have

```text
||T(u)||_I_p
 >= c_r c S/sqrt(k).                                      (8.3)
```

More strongly, the same `x` witnesses a large mixed contraction:

```text
sup_(||v||_p<=1)
 |T(u)[x^(r-1),v]|
 >= c S/sqrt(k).                                          (8.4)
```

#### Proof

Since `u` lies in the left singular subspace corresponding to singular values at least `c tau_k`,

```text
||A_x^* u||_2 >= c tau_k.                                 (8.5)
```

Take

```text
v := A_x^*u / ||A_x^*u||_2.
```

Then `||v||_2=1`, hence `||v||_p<=1` for `p>=2`. By definition of `A_x`,

```text
T(u)[x^(r-1),v]
 = <u,A_x v>
 = <A_x^*u,v>
 = ||A_x^*u||_2
 >= c tau_k.                                               (8.6)
```

This proves (8.4). The source norm is the symmetric diagonal norm, whereas (8.4) is a mixed evaluation. Real polarization gives

```text
sup_(||x_1||_p,...,||x_r||_p<=1)
 |T(u)[x_1,...,x_r]|
 <= C_r ||T(u)||_I_p.                                     (8.7)
```

Combining (8.6)--(8.7) yields (8.3) with `c_r=C_r^(-1)`. QED.

### The new inverse target

Define the source-normalized high-level set in coefficient space

```text
U_k(c)
 := {u in S^(n-1):
       ||T(u)||_I_p >= c_r c S/sqrt(k)}.                  (8.8)
```

Then every active tangent range satisfies

```text
S(L_x^(act)(k,c)) subset U_k(c),                          (8.9)
```

where `S(L)` is the Euclidean unit sphere of `L`.

There is an even stronger common-witness statement. Define

```text
N_x(u)
 := sup_(||v||_p<=1) |T(u)[x^(r-1),v]|.                   (8.10)
```

For every active range,

```text
inf_(u in S(L_x^(act)(k,c))) N_x(u)
 >= c S/sqrt(k).                                          (8.11)
```

Thus the remaining entropy problem is not an arbitrary Grassmannian problem. It is:

```text
How many O(k)-dimensional output subspaces can have an
entire Euclidean unit sphere on which one common contraction
point x makes the tensor map at least S/sqrt(k)?           (8.12)
```

This formulation retains both the source normalization and the shared polynomial witness `x^(r-1)`. The rotating-rank-one counterexample from Section 3 cannot fake activity here because its singular value is far below `S/sqrt(k)`.

## 9. Why commutators alone are no longer the right next invariant

The counterexample establishes two separate facts.

1. **Approximate commutation does not control formal eigenspaces.** Rank-one projections onto almost orthogonal vectors have tiny commutators, not a common frame. In the tensor construction there are exponentially many such lines.

2. **Source-scale activity matters.** The same construction has `S` so large relative to the rank-one singular value that none of those lines is active in the unresolved scale range.

Therefore any useful inverse theorem must combine frame rotation with a lower singular-value threshold tied to `S/sqrt(k)`. A statement about `[C_x,C_y]` by itself, even normalized by `tau_k^4`, can be overwhelmed by a large source denominator generated by many individually bounded summands.

The active large-norm certificate (8.11) is more faithful: every direction being counted must pay a definite amount of source-normalized tensor norm at one common tangent point.

## 10. Next concrete attack

The next run should attack the common-witness active-subspace problem (8.12), not try to repair the false top-`k` commutator lemma.

### Route A: order reduction / decoupling of the shared witness

For fixed `u`, the map

```text
x -> A_x^*u
```

is an `(r-1)`-homogeneous vector-valued polynomial. If an entire `j`-dimensional output sphere satisfies

```text
||A_x^*u||_2 >= c S/sqrt(k),
```

at one common `x`, then the restricted operator

```text
A_x^*|_L : L -> R^d
```

has smallest singular value at least `c S/sqrt(k)` and rank `j<=Ck`. The next goal is to decouple the repeated `x^(r-1)` slots and show that too many critical-angle-separated such subspaces force a lower-order contraction family with either sparse support, a norming-set structure, or an improved source-normalized square-function bound.

This is genuinely lower order: removing one repeated `x` slot replaces degree `r-1` dependence by degree `r-2` dependence.

### Route B: active spectral energy packing

Given a packing `x_1,...,x_M` with separated active ranges, try to select unit vectors `u_a` in successive range differences so that

```text
||A_(x_a)^* u_a||_2 >= c S/sqrt(k).                       (10.1)
```

Unlike the false commutator criterion, every selected direction now carries a quantitative source-energy certificate. The desired contradiction would be a Bessel/square-function inequality that sums these certificates after decoupling the `x_a` dependence.

### Route C: structured subclass expansion

Theorem 7.1 already permits arbitrary noncommuting low-spectrum covariance. The next safe partial expansion is to allow a bounded number of active frames per scale, or active frames generated by a sparse coordinate dictionary after a fixed output rotation. Any such result must be phrased only for the above-threshold projectors.

### Handoff assessment

- The newest RS finite-Hermite/read-k handoff is potentially useful only if Route A creates a genuinely local low-degree Gaussian bad-event representation. It is not currently the missing step.
- C05's basis-free low-rank covariance ideas can still help when an **active** covariance cluster is close to isotropic-plus-low-rank. Its sign/mod-4-specific conclusions are irrelevant here and are not imported.

## 11. Obligation ledger

```text
FULL SOURCE METRIC
  arbitrary deterministic symmetric tensors, 2 <= p < 2r:
  exponent before = gamma = 1/2 - 1/(2r)
  exponent after  = gamma = 1/2 - 1/(2r)
  target          = alpha = 1/2 - 1/p
  status          = OPEN / not solved here

NEW THIS RUN
  [PROVED]
    explicit symmetric-tensor rotating-rank-one tangent family
  [PROVED]
    exponentially many separated formal top-k frames with arbitrarily
    small normalized covariance commutators
  [REFUTED AS METHOD]
    predecessor equation (10.1)-type implication from small commutators
    to a small dictionary for the formal top-k tangent ranges
  [PROVED]
    active spectral truncation at c S/sqrt(k) loses only c epsilon_k
  [PROVED]
    active range dimension <= C_r k/c^2
  [PROVED]
    finite active-frame entropy criterion
  [PROVED PARTIAL CLASS]
    scale-wise active common frames imply the conjectured d^alpha exponent;
    arbitrary low-spectrum noncommutation is allowed
  [PROVED]
    every active output direction gives a combined tensor with
    source norm >= c_r c S/sqrt(k), with one common tangent witness x

INHERITED / STILL OPEN
  [PROVED]
    ridge threshold crossings are operator-Lipschitz at process level
  [PROVED]
    only the mesoscopic scale range needs new geometry
  [PROVED PARTIAL CLASS]
    fully commuting tangent covariances imply the target exponent
  [OPEN]
    entropy of common-witness active subspaces in (8.12)
  [OPEN]
    order-reduction / square-function inequality summing separated
    active-direction certificates without reintroducing the volumetric loss
```

No finite exhaustive claim requiring a checker is introduced. The new claims are analytic and their proofs are written on the page. The source conjecture remains open.