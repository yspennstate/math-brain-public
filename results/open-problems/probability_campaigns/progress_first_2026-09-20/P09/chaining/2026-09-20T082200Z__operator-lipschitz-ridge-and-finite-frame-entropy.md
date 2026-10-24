Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime does not provide authenticated GPT-6/maximum attestation.

# P09 progress-first run — ridge threshold crossings are operator-Lipschitz, and finite high-leverage frame complexity gives the target exponent

**Status: PROVED PARTIAL.** This report does **not** solve Randomstrasse101 Conjecture 16 for arbitrary deterministic tensors. The full-source worst-case polynomial exponent remains

```text
gamma = 1/2 - 1/(2r)
```

in the unresolved range `2 <= p < 2r`, rather than the conjectured

```text
alpha = 1/2 - 1/p.
```

The mathematical progress this run is threefold.

1. The main technical worry left by the preceding adaptive-ridge report — a possible `1/tau^2` instability when singular values cross the ridge threshold — is removed completely. The *residual* singular-value filter is operator-Lipschitz with constant one for rectangular matrices, by a self-adjoint dilation and a two-resolvent identity. Consequently the retained ridge map is operator-Lipschitz with constant two, uniformly in `tau`. Threshold crossings are therefore cheap without any spectral-gap assumption.

2. Combining the exact source normalization with that stability localizes the unsolved entropy range. At the critical scale `epsilon_k = d^alpha S/sqrt(k)`, the adaptive skeleton is trivially one-ball coverable for `k <= d^(2 alpha)`, while elementary volumetric covering already gives the required `k * polylog(d)` entropy for `k >= c d/log(2d)`. The genuinely new geometric difficulty is therefore the **mesoscopic window**

```text
d^(2 alpha) < k <~ d/log d,
```

with the left endpoint interpreted as `1` when `p=2`.

3. I prove a finite-high-leverage-frame theorem. If, at each critical scale, the top-`k` left singular subspaces of the tangent maps lie within critical-angle distance of at most `exp(k polylog(d,n))` fixed `O(k)`-dimensional subspaces, then the Randomstrasse101 dimension exponent follows. As a clean unconditional corollary, the conjectured exponent holds for the covariance-structure class in which the output tangent covariances `A_x A_x^*` commute for all `x`: simultaneous diagonalization reduces every top-`k` tangent image to one of only `exp(O(k log n))` coordinate subspaces. This includes the diagonal/dense-dust witness that defeated the earlier one-shot PAC-Bayes route.

I do **not** claim literature novelty for the covariance-commuting subclass. It is recorded as a new proved repository theorem and, more importantly, as an exact inverse target for the arbitrary case.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Installed title: `Gaussian Tensor Bounds`
- Repository / branch: private `yspennstate/math-open-problems`, `master`
- Pre-write master captured: `0576f096330f8fa95a43532dbb509472d23acb3c`
- Immediate P09 predecessor: `probability_campaigns/progress_first_2026-09-20/P09/chaining/2026-09-20T065800Z__global-sketch-entropy-counterexample-and-adaptive-ridge-skeleton.md`, creation commit `7022a8606d0b50fded6fc5fdce06354d2fdd1e05`, blob `f8df74b2ac770fa38f290cc8dadcab7fdc3f80c1`.
- Historical C0035 successor-gate material and every earlier P09 report are preserved. No peer or historical file is edited.

## 1. Source/current-status checkpoint

Source: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizic-Nikolac, A. Rodder et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Entry 8, Conjecture 16.

The exact source norm is

```text
||T||_I_p
 := sup_{||x_1||_p,...,||x_r||_p <= 1}
    |T[x_1,...,x_r]|.
```

For symmetric tensors the diagonal polynomial norm is equivalent to the full injective norm by real polarization, with a constant depending only on `r`; all final dimension exponents below therefore transfer to the source norm.

The source target is

```text
E ||sum_i g_i T_i||_I_p
 <= polylog(d,n) C(r,p) d^(1/2-1/p)
    (sum_i ||T_i||_I_p^2)^(1/2).
```

A bounded fresh primary-literature check on 20 September 2026 recovered the same baseline as the preceding runs.

- Bandeira--Gopi--Jiang--Lucca--Rothvoss, arXiv:2411.10633 / STOC 2025, gives the general geometric tensor concentration result and the polynomial exponent `1/2 - 1/max{p,2r}` up to logarithms.
- Ishaq Aden-Ali, arXiv:2503.10580, gives the stronger PAC-Bayesian variance-parameter inequality but does not remove the arbitrary correlated low-`p` obstruction.
- Dartois--McKenna, arXiv:2603.01342 (March 2026), gives a moment-based deterministic inequality and sharp bounds for several random-tensor ensembles (including independent-up-to-symmetry and bounded-rank models), but its stated models are not the universal Gaussian sum of arbitrary deterministic correlated summands in Conjecture 16.
- The Randomstrasse101 source remains v1 dated 31 March 2026 and still records the conjecture.

This is a bounded current-status check, not a proof that no unpublished or unindexed resolution exists.

Accordingly the fixed full-source metric is unchanged:

```text
old arbitrary-tensor exponent: gamma = 1/2 - 1/(2r)
new arbitrary-tensor exponent: gamma = 1/2 - 1/(2r)
target exponent:               alpha = 1/2 - 1/p
source status:                 OPEN / not solved here
```

## 2. Exact tangent identities in the source normalization

Write

```text
S^2 := sum_i ||T_i||_I_p^2,
F(x) := (T_i[x,...,x])_i,
(A_x u)_i := T_i[x,...,x,u],
```

where `A_x` contains `r-1` copies of `x` and one copy of `u`. Then

```text
F(x) = A_x x.                                               (2.1)
```

Let `q=p/(p-1)`. Since `p>=2`, `q<=2`.

### Lemma 2.1 (exact Hilbert--Schmidt and variation bounds)

For every `x,y in B_p^d`,

```text
||A_x||_HS <= S,                                           (2.2)
||A_x-A_y||_op <= (r-1) S ||x-y||_p,                      (2.3)
||F(x)-F(y)||_2 <= r S ||x-y||_p,                         (2.4)
||F(x)||_2 <= S.                                           (2.5)
```

#### Proof

For each `i`, the row functional

```text
u -> T_i[x^(r-1),u]
```

has `ell_q` norm at most `||T_i||_I_p`. Because `q<=2`, its Euclidean norm is no larger than its `ell_q` norm. Summing the squared row norms gives (2.2).

For (2.3), telescope the first `r-1` slots:

```text
T_i[x^(r-1),u] - T_i[y^(r-1),u]
 = sum_(a=0)^(r-2)
   T_i[x^a, x-y, y^(r-2-a), u].                            (2.6)
```

Each summand has absolute value at most

```text
||T_i||_I_p ||x-y||_p ||u||_p
 <= ||T_i||_I_p ||x-y||_p ||u||_2,                        (2.7)
```

because `||u||_p<=||u||_2` for `p>=2`. Taking the Euclidean norm in the output index `i` proves (2.3).

The same telescoping over all `r` slots gives (2.4), and (2.5) is immediate from the source norm. QED.

These exact-source bounds remove the polarization constant that was carried in some earlier diagonal-only intermediate formulas; the only polarization loss is when the final diagonal process estimate is transferred back to the full symmetric injective norm.

## 3. The ridge residual is operator-Lipschitz with constant one

The predecessor defined, for a rectangular matrix `A`,

```text
G_tau(A) := A^* A (A^* A + tau^2 I)^(-1),
B_tau(A) := A G_tau(A),                                   (3.1)
```

so the adaptive skeleton is

```text
Z_tau(x) := B_tau(A_x) x.                                 (3.2)
```

The apparent problem is that the usual resolvent identity for `G_tau` alone contains `tau^(-2)`. The next theorem shows that this loss is an artefact of looking at the projector rather than the quantity that actually enters the process.

### Theorem 3.1 (rectangular ridge-residual contraction)

For every pair of real rectangular matrices `A,B` of the same size and every `tau>0`, define

```text
R_tau(A)
 := tau^2 A(A^*A + tau^2 I)^(-1).                         (3.3)
```

Then

```text
||R_tau(A)-R_tau(B)||_op <= ||A-B||_op.                   (3.4)
```

Consequently,

```text
||B_tau(A)-B_tau(B)||_op <= 2 ||A-B||_op,                 (3.5)
```

uniformly in `tau`.

Moreover,

```text
||R_tau(A)||_op <= tau/2.                                 (3.6)
```

#### Proof

Introduce the self-adjoint dilation

```text
D(A) := [ 0   A  ]
        [ A^* 0  ].                                       (3.7)
```

Then

```text
||D(A)-D(B)||_op = ||A-B||_op.                            (3.8)
```

Consider the odd scalar function

```text
h_tau(t) := tau^2 t/(t^2+tau^2).                          (3.9)
```

Functional calculus for the dilation gives

```text
h_tau(D(A))
 = [ 0          R_tau(A) ]
   [ R_tau(A)^* 0        ].                               (3.10)
```

The key point is the exact two-resolvent representation

```text
h_tau(t)
 = (tau^2/2) [ (t-i tau)^(-1) + (t+i tau)^(-1) ].         (3.11)
```

For self-adjoint `X,Y`, the resolvent identity gives

```text
||(X-zI)^(-1) - (Y-zI)^(-1)||_op
 <= ||X-Y||_op / |Im z|^2.                               (3.12)
```

Apply (3.12) at `z=+- i tau` and insert it into (3.11):

```text
||h_tau(X)-h_tau(Y)||_op <= ||X-Y||_op.                   (3.13)
```

Taking the upper-right block and using (3.8) proves (3.4).

Since

```text
B_tau(A) = A - R_tau(A),                                  (3.14)
```

(3.5) follows from the triangle inequality.

Finally, if `s` is a singular value of `A`, the corresponding singular value of `R_tau(A)` is

```text
tau^2 s/(s^2+tau^2) <= tau/2,                             (3.15)
```

with equality at `s=tau`. This proves (3.6). QED.

### Why this matters

There is **no spectral-gap hypothesis** and no `tau^(-1)` or `tau^(-2)` loss in (3.4)--(3.5). A singular value can move directly through `tau`; the process-level retained map changes at the same operator scale as the original tangent matrix.

This proves the predecessor's proposed "threshold crossing is cheap" step in a stronger form than anticipated.

## 4. Uniform stability of the adaptive skeleton

Take

```text
tau_k := S/sqrt(k),
Acrit  := d^alpha S,
Z_k(x) := B_(tau_k)(A_x) x.                               (4.1)
```

### Corollary 4.1 (critical-scale error and no-gap Lipschitz bound)

For every `x,y in B_p^d`,

```text
||F(x)-Z_k(x)||_2
 <= (1/2) d^alpha S/sqrt(k),                              (4.2)
```

and

```text
||Z_k(x)-Z_k(y)||_2
 <= (2r-1) d^alpha S ||x-y||_p.                           (4.3)
```

#### Proof

Equation (3.14) gives

```text
F(x)-Z_k(x)=R_(tau_k)(A_x)x.                              (4.4)
```

By (3.6) and `||x||_2<=d^alpha ||x||_p<=d^alpha`,

```text
||F(x)-Z_k(x)||_2
 <= (tau_k/2)d^alpha,                                     (4.5)
```

which is (4.2).

For the increment,

```text
Z_k(x)-Z_k(y)
 = [B_(tau_k)(A_x)-B_(tau_k)(A_y)]x
   + B_(tau_k)(A_y)(x-y).                                 (4.6)
```

The first term is at most

```text
2 ||A_x-A_y||_op ||x||_2
 <= 2(r-1)d^alpha S ||x-y||_p.                            (4.7)
```

The singular-value multiplier of `B_tau` is

```text
s^3/(s^2+tau^2) <= s,                                     (4.8)
```

so `||B_tau(A_y)||_op<=||A_y||_op<=S`. Hence the second term is at most

```text
S ||x-y||_2 <= d^alpha S ||x-y||_p.                       (4.9)
```

Adding (4.7)--(4.9) gives (4.3). QED.

### Interpretation

The ridge skeleton may have rapidly changing singular vectors, but those changes do not produce a large process increment merely because a threshold is crossed. Any remaining entropy obstruction must come from **genuinely many geometrically distinct high-gain tangent directions**, not from the discontinuity of a hard spectral cutoff.

## 5. The unresolved scale window is smaller than it looked

Define the critical radius

```text
epsilon_k := d^alpha S/sqrt(k).                            (5.1)
```

The preceding report treated every dyadic `1<=k<=d` as potentially difficult. Two ends of that scale range are actually automatic.

### Proposition 5.1 (coarse scales are one-ball coverable)

For every `x`,

```text
||Z_k(x)||_2 <= ||F(x)||_2 <= S.                          (5.2)
```

Therefore, whenever

```text
k <= d^(2 alpha),                                         (5.3)
```

we have `epsilon_k>=S` and hence

```text
N(Z_k(B_p^d), epsilon_k)=1.                               (5.4)
```

#### Proof

In a singular basis of `A_x`, the multiplier defining `B_tau(A_x)` is no larger than the corresponding singular value of `A_x`. Thus

```text
||B_tau(A_x)x||_2 <= ||A_xx||_2=||F(x)||_2.               (5.5)
```

Now use (2.5). QED.

For `p=2`, `alpha=0`, so this only removes the trivial `k=1` endpoint. For every `p>2`, however, it removes a polynomial initial segment.

### Proposition 5.2 (near-fine scales are already volumetric)

There is a constant `C_r` such that

```text
log N(Z_k(B_p^d), epsilon_k)
 <= d log(1 + C_r sqrt(k)/d^alpha).                        (5.6)
```

In particular, for

```text
k >= c_r d/log(2d),                                       (5.7)
```

we have

```text
log N(Z_k(B_p^d), epsilon_k)
 <= C_r k log^2(2d).                                      (5.8)
```

#### Proof

By (4.2), every `Z_k(x)` lies within `epsilon_k/2` of `F(x)`. By (2.4), an `ell_p` net of `B_p^d` with mesh

```text
delta_k := d^alpha/(4r sqrt(k))                            (5.9)
```

induces an `epsilon_k` cover of `Z_k(B_p^d)` after changing an absolute constant in the covering radius.

The standard volumetric bound in its own norm is

```text
N(B_p^d, delta B_p^d)
 <= (1+2/delta)^d.                                        (5.10)
```

Substitute (5.9) to obtain (5.6).

If `k>=c_r d/log(2d)`, the right side of (5.6) is at most `C_r d log(2d)`, while

```text
k log^2(2d) >= c_r d log(2d).                             (5.11)
```

Adjust constants to get (5.8). QED.

### Consequence: the mesoscopic bottleneck

Up to harmless endpoint constants, the only scale range not handled by these two elementary arguments is

```text
d^(2 alpha) < k < d/log(2d).                              (5.12)
```

At `p=2` this is essentially `1<k<d/log d`. At larger `p` the unresolved window shrinks from the left as `d^(1-2/p)`.

This localization is useful because any inverse theorem only has to control the high-leverage subspace family in (5.12), not at every scale.

## 6. Hard top-k skeleton and a finite-frame theorem

For each `x`, let

```text
s_1(x)>=s_2(x)>=...
```

be the singular values of `A_x`, let `P_x(k)` be the orthogonal projector onto `k` top right singular vectors (take all nonzero vectors if the rank is smaller), and define

```text
H_k(x) := A_x P_x(k) x.                                   (6.1)
```

Let

```text
L_x(k) := range(A_x P_x(k)) subset R^n                    (6.2)
```

be the corresponding top left singular subspace.

From (2.2),

```text
s_(k+1)(x) <= S/sqrt(k+1),                                (6.3)
```

so

```text
||F(x)-H_k(x)||_2
 <= d^alpha S/sqrt(k+1).                                  (6.4)
```

Also `H_k(x)` is obtained by deleting singular components of `F(x)=A_xx`, hence

```text
||H_k(x)||_2 <= ||F(x)||_2 <= S.                          (6.5)
```

### Theorem 6.1 (finite high-leverage frame criterion)

Fix `k`. Suppose there is a collection of subspaces

```text
W_(k,1),...,W_(k,M_k) subset R^n                          (6.6)
```

with

```text
dim W_(k,a) <= C_0 k                                      (6.7)
```

such that for every `x in B_p^d` there is an index `a=a(x)` satisfying

```text
||P_(L_x(k)) - P_(W_(k,a))||_op
 <= eta_k,                                                 (6.8)
```

where

```text
eta_k <= c_0 d^alpha/sqrt(k+1).                            (6.9)
```

Then, at radius

```text
rho_k := C d^alpha S/sqrt(k+1),                            (6.10)
```

with `C` depending only on `c_0,C_0`,

```text
log N(F(B_p^d), rho_k)
 <= log M_k
    + C_0 k log(1 + C sqrt(k+1)/d^alpha).                  (6.11)
```

In particular, if for every dyadic `k` in the mesoscopic range (5.12)

```text
log M_k <= C k polylog(d,n),                              (6.12)
```

then, together with Propositions 5.1--5.2 and the standard terminal fine-scale cover, the Randomstrasse101 target dimension exponent `d^alpha` follows up to polylogarithms.

#### Proof

Fix `x` and choose `W=W_(k,a(x))`. Since `H_k(x) in L_x(k)`, (6.8) and (6.5) give

```text
||H_k(x)-P_W H_k(x)||_2
 <= eta_k ||H_k(x)||_2
 <= eta_k S.                                               (6.13)
```

By (6.9), this is at most a constant multiple of the critical radius `d^alpha S/sqrt(k+1)`.

For fixed `W`, the possible projected points lie in the Euclidean ball

```text
W intersect S B_2^n.                                      (6.14)
```

A Euclidean ball of dimension at most `C_0 k` and radius `S` has, at scale comparable to `d^alpha S/sqrt(k+1)`, covering number at most

```text
(1 + C sqrt(k+1)/d^alpha)^(C_0 k).                        (6.15)
```

Take the union over the `M_k` dictionary subspaces, then add the hard-skeleton approximation error (6.4). This proves (6.11).

If (6.12) holds throughout the only unresolved scale window, the dyadic Dudley sum has the same `d^alpha * polylog(d,n)` order as in the predecessor's entropy criterion. The already-solved coarse and near-fine scales supply the remaining pieces. QED.

### What this criterion removes

A generic Grassmannian cover costs `exp(Theta(kd))`; Theorem 6.1 shows that one does **not** need to control the entire ridge operator or every singular vector continuously. It is enough to prove that the actual high-gain tangent ranges visit only `exp(k polylog)` effective frames at the critical angular resolution.

This is the exact structural quantity the next inverse argument should attack.

## 7. A proved covariance-structure class: commuting tangent covariances

The finite-frame criterion has a clean unconditional application.

### Theorem 7.1 (pairwise commuting output tangent covariances)

Assume that the symmetric positive-semidefinite matrices

```text
C_x := A_x A_x^* in R^(n x n)                             (7.1)
```

commute pairwise:

```text
C_x C_y = C_y C_x
for all x,y in B_p^d.                                     (7.2)
```

Then the Gaussian tensor bound of Randomstrasse101 Conjecture 16 holds for this tensor family with the conjectured polynomial dimension exponent:

```text
E ||sum_i g_i T_i||_I_p
 <= C_(r,p) d^alpha S * polylog(d,n).                     (7.3)
```

More explicitly, the argument gives a factor no worse than

```text
C_(r,p) d^alpha S
 [ sqrt(log(2n)+log(2d)) log(2d) + sqrt(log(2d)) ],        (7.4)
```

up to harmless changes of logarithmic powers from dyadic rounding and polarization.

#### Proof

A pairwise commuting family of real symmetric matrices is simultaneously orthogonally diagonalizable. Thus there is one fixed orthonormal basis

```text
u_1,...,nu_n                                               (7.5)
```

of the output space in which every `C_x` is diagonal.

The left singular vectors of `A_x` are eigenvectors of `C_x`. Therefore, for every `x` and every `k`, the top left singular subspace `L_x(k)` is spanned by at most `k` vectors from the fixed basis (7.5), after an arbitrary coordinate choice inside ties.

Hence the dictionary in Theorem 6.1 can be chosen as the coordinate subspaces of dimension at most `k`. Its cardinality satisfies

```text
log M_k <= C k log(2n)                                    (7.6)
```

for all `k` (if `k` is comparable to or larger than `n`, simply use the full output space, whose dimension is `O(k)`). Here `eta_k=0`.

Substituting (7.6) into (6.11) gives

```text
log N(F(B_p^d), C d^alpha S/sqrt(k))
 <= C k [log(2n)+log(2d)]                                 (7.7)
```

at every dyadic scale not already trivial. Dudley's entropy integral/dyadic chaining then yields the diagonal symmetric-process estimate (7.4). Real polarization transfers it to the full symmetric `I_p` norm with an `r`-dependent constant. QED.

### Why this class is useful rather than cosmetic

The theorem is not merely a spectral-gap special case. Eigenvalues may cross arbitrarily often and have arbitrary multiplicities; only the *common eigenframe* matters. The threshold-crossing theorem from Sections 3--4 shows why no extra gap assumption is needed.

The class also contains the diagonal/dense-dust tensor witness

```text
T = sum_j e_j^(tensor r),                                 (7.8)
```

and its corresponding diagonal tangent families. That witness was exactly where a previous one-scale product-posterior method paid a false polynomial covariance price. The present route handles it because all high-leverage ranges live in a fixed coordinate frame.

The theorem also permits arbitrary eigenvalue profiles and arbitrary correlations compatible with the common output frame; it is not an independent-entry assumption.

Again, no literature-novelty claim is made here. The value is that a concrete covariance property, strictly stronger than what the full conjecture assumes but qualitatively aligned with its difficult examples, is now proved sufficient.

## 8. Counterexample checks

### 8.1 Dense diagonal dust

For diagonal tensors, `C_x` is diagonal in the standard output basis. Theorem 7.1 therefore applies directly. The proof never inserts the global Frobenius covariance into every slot, so the `d^(1/(2r))` loss that killed the earlier anisotropic product-Gaussian route does not reappear.

### 8.2 The global Haar-sketch obstruction from the predecessor

That family had a tiny true process image but a global random rank-one sketch could create an artificial `exp(c d)` cloud. No random sketch is used here. The ridge residual is a deterministic 1-Lipschitz singular-value function of the tangent operator, so external sketch noise cannot create new geometry.

### 8.3 Matrix case

For `r=2` the source problem is already known by matrix concentration. The present theorems are consistent with that case but are not presented as a replacement for the sharper matrix theory.

## 9. What remains open

The full arbitrary-tensor exponent did **not** move. The remaining obstruction is now more specific than in the predecessor.

At a mesoscopic scale `k` satisfying

```text
d^(2 alpha) < k < d/log d,                                (9.1)
```

one must control the number of essentially different top-left tangent ranges

```text
L_x(k)=range(A_x P_x(k))                                  (9.2)
```

at angular resolution

```text
~ d^alpha/sqrt(k).                                         (9.3)
```

Theorem 3.1 rules out spectral-threshold discontinuity as the source of a large count. Therefore, if an `exp(omega(k polylog))` family of such ranges really exists, it must come from substantial rotation of genuinely high-gain directions.

The finite-frame theorem says exactly what an inverse result must produce:

```text
Either
  {L_x(k)} has an exp(k polylog)-sized critical-angle dictionary,

or
  the tensor family has additional structure forced by the excessive
  rotation of high-gain tangent directions.                              (9.4)
```

The second branch is where the C05 handoffs can now be used correctly. The useful transferred facts are the basis-free low-rank covariance decomposition and the profile-to-low-rank-defect principle; the mod-4/sign-specific statement itself is not imported into this Gaussian problem.

## 10. Next concrete attack

The next run should attack (9.4), not redo ridge stability.

1. **Commutator branch.** Quantify how many critical-angle-separated `L_x(k)` can exist while the covariance family `C_x=A_xA_x^*` has small pairwise commutators. Try to prove that small commutators on a large packing imply an approximate common frame, which would feed Theorem 6.1.

2. **Noncommuting inverse branch.** If many pairs have large commutators, use

```text
[C_x,C_y]
```

as a certificate of two genuinely different high-gain directions. Expand `C_x-C_y` and the commutator using the degree-`r-1` polynomial structure of `A_x`; search for a lower-order contraction or sparse/norming witness forced by repeated large commutators.

3. **Low-rank-defect branch.** Test the C05 basis-free statement on covariance clusters that are close to `lambda I + R` with low-rank `R`. The isotropic bulk should be below threshold at mesoscopic scales, leaving only the low-rank exceptional sector, which is exactly a finite-frame situation if the exceptional ranges can be discretized.

4. **Counterexample first.** Before promoting any approximate-commuting lemma, test it against diagonal dust, the predecessor's global-sketch obstruction, and a family of rotating rank-one tangents. If a rotating rank-one example violates the proposed dictionary bound without violating source normalization, record that obstruction rather than adding assumptions silently.

A particularly useful next lemma would be:

```text
If ||[C_x,C_y]||_op <= delta tau_k^4
throughout a critical packing and Tr(C_x)<=S^2,
then the top-k ranges admit an angle-O(delta^c) dictionary
of size exp(C k polylog(d,n)).                             (10.1)
```

The exponent and norm in (10.1) are deliberately not asserted here; they are the next object to prove or refute.

## 11. Obligation ledger

```text
FULL SOURCE METRIC
  arbitrary deterministic tensors, 2 <= p < 2r:
  exponent before = gamma = 1/2 - 1/(2r)
  exponent after  = gamma = 1/2 - 1/(2r)
  target          = alpha = 1/2 - 1/p
  status          = OPEN / not solved here

NEW THIS RUN
  [PROVED] exact source-normalized tangent HS bound ||A_x||_HS <= S
  [PROVED] exact tangent variation ||A_x-A_y||_op <= (r-1)S||x-y||_p
  [PROVED] rectangular ridge residual R_tau is operator-Lipschitz with constant 1
  [PROVED] retained ridge map B_tau is operator-Lipschitz with constant 2
  [PROVED] threshold crossings cost no inverse power of tau
  [PROVED] coarse critical scales k<=d^(2alpha) are one-ball coverable
  [PROVED] scales k>=c d/log d already have k log^2 d entropy
  [PROVED] only the mesoscopic range d^(2alpha)<k<d/log d needs new geometry
  [PROVED] finite high-leverage-frame criterion at critical angular resolution
  [PROVED PARTIAL CLASS]
           commuting output tangent covariances imply the conjectured d^alpha exponent

INHERITED / STILL OPEN
  [PROVED] global Haar-sketch entropy hypothesis is false as a method
  [PROVED] adaptive hard/ridge skeleton reaches the critical pointwise scale
  [OPEN]   arbitrary mesoscopic high-leverage frame complexity
  [OPEN]   inverse theorem: too many frames => sparse/block/low-rank covariance structure
```

No finite exhaustive claim requiring a checker is introduced in this report. The new claims are analytic and their proofs are written on the page.