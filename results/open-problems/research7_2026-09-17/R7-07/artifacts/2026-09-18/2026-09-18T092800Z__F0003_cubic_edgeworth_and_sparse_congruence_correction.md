Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — cubic Edgeworth transfer and a sparse congruence-correction lemma

Date: 2026-09-18 UTC.  
Target: Van Vu, *Recent progress in combinatorial random matrix theory* (arXiv:2005.02797; Probability Surveys 18 (2021)), Section 5 immediately after Theorem 5.2.  
Primary undirected technical source: Jiaoyang Huang, *Invertibility of adjacency matrices for random d-regular graphs*, arXiv:1807.06465v2, Section 4.  
Analogous directed technique: Hoi H. Nguyen and Amanda Pan, *A note on the singularity probability of random directed d-regular graphs*, arXiv:2308.06461 / European J. Combin. 2024.  
Frozen metric:

\[
a_3:=\sup\{a\ge 0:\Pr(A_{n,3}\text{ singular})\le n^{-a+o(1)}\}.
\]

Metric before this run: **`a_3 >= 1/8`**.  
Metric after this artifact: **`a_3 >= 1/8` — NO MOVEMENT.**

This artifact proves two new technical lemmas that remove two distinct `p^4/sqrt(n)` losses in Huang's undirected equidistributed calculation, but it does **not** yet reassemble the retained cubic phase across the symmetric edge-count matrix. Accordingly it does not promote the metric beyond `1/8`.

Methods: **B21 ASK WHO ELSE HAS THIS SHAPE / B7 TAKE THE LIMIT / B30 LOCALIZE AND IDENTIFY THE GLUING FAILURE**. The immediately preceding R7-07 triple was B15/B24/B5.

---

## 1. Idea before code

The previous run removed Huang's sparse non-equidistributed class as the source of the cubic `1/9` barrier and reached the published undirected local-CLT barrier `p << n^(1/8)`. There are three superficially similar `p^4` losses in Section 4.1, but they have different causes.

1. In the row-wise Fourier inversion Huang expands the characteristic function only to quadratic order and treats the third moment as an error. On his large Fourier ball this costs
   \[
   O\!\left(p^4(\log n)^{3/2}/\sqrt n\right).
   \]
2. In replacing the exact symmetric congruence class `E` by the unconstrained lattice class `\widetilde E`, Huang uses correction matrices whose entries are only bounded entrywise by `O(p)`. The resulting quadratic-weight comparison again costs `p^4 sqrt(log n/n)`.
3. In replacing the Gaussian lattice sum by a Riemann integral, a coarse cell-distortion estimate again produces a `p^4`-scale loss.

Nguyen--Pan's directed proof reveals that item 1 is avoidable: the **same** random walk `X` on `U_{d,p}` has an explicit cubic moment, and the cubic term should be retained as a phase rather than discarded. The directed/undirected distinction does not occur at this local random-walk step; Huang's undirected formula (4.3) also contains independent copies of precisely this `X` for each fixed row. The first genuinely symmetric obstruction occurs only after the row integrals must be recombined over a symmetric matrix `M=[m_ij]`.

For item 2, there is a direct deterministic improvement: the required congruence correction can be supported on a bounded-degree path and has Frobenius norm `O(p^(3/2))`, rather than the `O(p^2)` bound obtained from `p^2` entries of size `O(p)`. This improves the congruence-weight distortion from the `1/8` scale to the `1/7` scale.

For item 3, the natural count lattice has covering radius only `O(p)` in count coordinates; this improves the pure mesh-distortion loss to the `1/6` scale.

What remains is therefore sharply isolated: **sum the cubic-corrected row Fourier integrals over the symmetric edge-count lattice without first taking a uniform absolute bound on the cubic phase.**

---

## 2. B21 — the directed cubic calculation transfers locally, and the first failure is later

Huang's undirected formula (4.3) fixes a symmetric edge-count matrix `M`. Conditional on a row size `n_i`, the row probability is

\[
\Pr(X_1+\cdots+X_{n_i}=m_i),
\]

where `X_1,...,X_{n_i}` are independent copies of the uniform random variable on the multiset `U_{d,p}`. Nguyen--Pan use exactly the same `U_{d,p}` random variable in the directed model. Thus their moment computation applies verbatim to **each fixed undirected row**. Symmetry of `M` has not yet been used at this point.

Let `mu=(d/p)1` and let `s in 1^perp`. Write

\[
Y_s:=\langle s,X-\mu\rangle,\qquad
\phi(s):=\mathbb E e^{iY_s}.
\]

Nguyen--Pan's explicit moment calculation gives, for fixed `d`,

\[
\mathbb EY_s=0,
\qquad
\mathbb EY_s^2=\frac d p\|s\|_2^2,
\]

\[
\mathbb EY_s^3=\frac{C_{d,p}}p\sum_{j=0}^{p-1}s_j^3,
\qquad C_{d,p}=d+O_d(p^{-1}),
\]

and

\[
\mathbb EY_s^4
\le C_d\left(\frac{\|s\|_2^4}{p^2}
+\frac1p\sum_j s_j^4\right).
\]

The hypotheses match exactly: fixed `d`, the same `U_{d,p}`, and `s perpendicular to 1` after Huang's orthogonal change of variables.

The key point is that the third moment is not an amorphous `O(||s||^3/p)` error. It is a one-dimensional cubic invariant, `sum_j s_j^3`, multiplied by a bounded coefficient.

---

## 3. B7 — cubic Edgeworth expansion on Huang's full Fourier ball

### Lemma 3.1 — cubic logarithmic characteristic-function expansion

For fixed `d>=3`, there are constants `delta_d,c_d,C_d>0` such that for every odd prime `p` coprime to `d` and every `s in 1^perp` with `||s||_2<=delta_d`,

\[
\log\phi(s)
= -\frac d{2p}\|s\|_2^2
-i\frac{C_{d,p}}{6p}\sum_j s_j^3
+R_{d,p}(s),
\]

where

\[
|R_{d,p}(s)|
\le C_d\left(
\frac{\|s\|_2^4}{p^2}
+\frac1p\sum_j s_j^4
\right)
\le C_d\frac{\|s\|_2^4}{p}.
\]

#### Proof

Taylor's formula with an absolute fourth-order remainder gives

\[
e^{iy}=1+iy-y^2/2-iy^3/6+O(y^4).
\]

Taking expectations and inserting the four moment identities above yields

\[
\phi(s)
=1-\frac d{2p}\|s\|_2^2
-i\frac{C_{d,p}}{6p}\sum_j s_j^3
+O_d\!\left(
\frac{\|s\|_2^4}{p^2}+
\frac1p\sum_j s_j^4
\right).
\]

For `delta_d` sufficiently small the quantity after the leading `1` has modulus at most `1/2`, uniformly in `p`. Therefore the principal logarithm is defined and

\[
\log(1+z)=z+O(z^2).
\]

The square of the quadratic term is `O(||s||^4/p^2)`; quadratic times cubic and cubic squared are higher order on `||s||<=delta_d` and are absorbed into the same displayed remainder after increasing `C_d`. Finally `sum_j s_j^4<=||s||_2^4`. This proves the claim. QED.

### Corollary 3.2 — the local Taylor remainder itself has a `1/6` barrier, not `1/8`

Assume `N asymp n/p` and restrict to Huang's Fourier ball

\[
\|s\|_2^2\le c\,\frac{p^4\log n}{n}.
\]

Then

\[
\phi(s)^N
=
\exp\!\left(
-\frac{dN}{2p}\|s\|_2^2
-i\frac{C_{d,p}N}{6p}\sum_j s_j^3
\right)
\left(1+O_d\!\left(\frac{p^6(\log n)^2}{n}\right)\right),
\]

uniformly whenever `p^6(log n)^2/n=o(1)`.

#### Proof

By Lemma 3.1,

\[
N|R_{d,p}(s)|
\le C_d\frac Np\|s\|_2^4.
\]

Using `N<=C n/p` and the ball bound,

\[
\frac Np\|s\|_2^4
\le C\frac n{p^2}
\left(\frac{p^4\log n}{n}\right)^2
=C\frac{p^6(\log n)^2}{n}.
\]

Exponentiating the logarithmic expansion gives the result. QED.

### Consequence

Huang's quadratic-only step (his (4.7)--(4.9)) loses `p^4(log n)^(3/2)/sqrt(n)` because it discards the cubic term. Once the cubic phase is retained, the **Taylor remainder** is harmless all the way to

\[
p\ll n^{1/6}/(\log n)^{1/3+o(1)}.
\]

This does **not** yet extend Huang Proposition 4.1: the cubic phase still has to be integrated and then summed compatibly with symmetry of `M`. The statement here is only about the local analytic expansion, and that distinction is essential.

---

## 4. B30 — an exact sparse correction for Huang's symmetric congruences

We now improve the deterministic correction used to pass from Huang's exact lattice `E` to the unconstrained lattice `\widetilde E`.

For a symmetric integer matrix `Delta=[Delta_ij]`, define

\[
R_i(\Delta):=\sum_j\Delta_{ij},
\qquad
S_i(\Delta):=\sum_j j\Delta_{ij}.
\]

Huang needs to realize prescribed residues

\[
R_i(\Delta)\equiv r_i\pmod d,
\qquad
S_i(\Delta)\equiv s_i\pmod p,
\]

with `sum_i r_i=0 mod d`, while preserving symmetry, even diagonal, and total sum zero.

### Lemma 4.1 — sparse congruence correction

Fix `d>=3`. For every odd prime `p` with `gcd(p,d)=1`, every

\[
r\in(\mathbb Z/d\mathbb Z)^p,
\qquad \sum_i r_i=0,
\]

and every

\[
s\in(\mathbb Z/p\mathbb Z)^p,
\]

there exists a symmetric integer matrix `Delta` such that

1. every diagonal entry `Delta_ii` is even;
2. `sum_{i,j} Delta_ij=0`;
3. `R_i(Delta)=r_i (mod d)` for every `i`;
4. `S_i(Delta)=s_i (mod p)` for every `i`;
5. `max_{ij}|Delta_ij|<=C_d p`;
6. `||Delta||_F<=C_d p^(3/2)`.

#### Proof

**Step 1: choose small exact row sums.** Pick integer representatives `rho_i` of `r_i` with `|rho_i|<=d`. Since `sum rho_i` is a multiple of `d`, first change `rho_0` by a multiple of `d` so that the resulting vector `R` has exact sum zero. This makes `|R_0|=O_d(p)` and leaves the other coordinates `O_d(1)`.

Let

\[
T:=\sum_i s_i\pmod p.
\]

The weighted row sum `sum_i iR_i` may not equal `T` modulo `p`. Change `R_1` by `dt` and `R_0` by `-dt`, where

\[
t\equiv d^{-1}\left(T-\sum_i iR_i\right)\pmod p
\]

is chosen with `|t|<=p/2`. Exact total sum remains zero, every row sum remains in the prescribed residue class modulo `d`, and now

\[
\sum_i iR_i\equiv T\pmod p.
\]

Moreover

\[
\|R\|_2=O_d(p).
\]

**Step 2: realize the exact row sums with an even diagonal.** The number of odd coordinates of `R` is even because `sum_i R_i=0`. Pair the odd coordinates arbitrarily. Put a `1` in each paired off-diagonal position and its symmetric mate, put zero in all other off-diagonal positions, and define

\[
B_{ii}:=R_i-o_i,
\]

where `o_i` is `1` if `i` was paired and `0` otherwise. Then `B` is symmetric, `B_ii` is even, its row sums equal `R_i`, and its total sum is zero. Also

\[
\|B\|_F^2\le C_d(\|R\|_2^2+p)=O_d(p^2).
\]

Let

\[
u_i:=S_i(B)=\sum_j jB_{ij}.
\]

By symmetry,

\[
\sum_i u_i
=\sum_{i,j}jB_{ij}
=\sum_j jR_j
\equiv T
=\sum_i s_i\pmod p.
\]

Hence the residual vector

\[
\tau_i:=s_i-u_i\pmod p
\]

has `sum_i tau_i=0 mod p`.

**Step 3: repair the weighted moments without changing row sums.** For `a!=b` let

\[
K_{ab}:=(e_a-e_b)(e_a-e_b)^T.
\]

This matrix is symmetric and has every row sum zero. Its weighted-moment vector is

\[
S(K_{ab})=(a-b)(e_a-e_b).
\]

Use only the path edges `(0,1),(1,2),...,(p-2,p-1)`. For `1<=k<=p-1`, choose an integer `c_k`, `|c_k|<=p/2`, satisfying

\[
2c_k\equiv-\sum_{i=0}^{k-1}\tau_i\pmod p.
\]

This is possible because `p` is odd. Set

\[
C:=2\sum_{k=1}^{p-1}c_kK_{k-1,k}.
\]

Then `C` is symmetric, has even diagonal, zero row sums and zero total sum. Its weighted moment at vertex `0` is `-2c_1=\tau_0`; for `1<=i<=p-2` it is

\[
2c_i-2c_{i+1}=\tau_i\pmod p,
\]

and at the final vertex it is `2c_{p-1}=\tau_{p-1}` because `sum_i tau_i=0`. Thus

\[
S_i(C)\equiv\tau_i\pmod p.
\]

The matrix `C` is tridiagonal. Every nonzero off-diagonal entry has magnitude at most `p`, and every diagonal entry has magnitude at most `2p`; there are only `O(p)` nonzero entries. Therefore

\[
\|C\|_F=O(p^{3/2}).
\]

Finally put `Delta=B+C`. All six requirements follow. QED.

---

## 5. What Lemma 4.1 buys in Huang's Gaussian weight

Huang's final quadratic weight on normalized deviations

\[
A:=\left[m_{ij}/(dn)-1/p^2\right]
\]

has the form

\[
Q(A)=\frac{dnp^2}{4}\operatorname{Tr}A^2
-\frac{(d-1)np}{2}\|A\mathbf 1\|_2^2.
\]

His diagonalization shows that on `Sym_p^0` the eigenvalues of this positive quadratic form are exactly `dnp^2/4` on the zero-row-sum subspace and `np^2/4` on the additive subspace. In particular its operator norm is `O_d(np^2)`.

For an equidistributed matrix,

\[
\|A\|_F^2\le b\log n/n.
\]

Lemma 4.1 gives a count correction `Delta` with

\[
H:=\Delta/(dn),\qquad
\|H\|_F\le C_d p^{3/2}/n.
\]

Because `Q` is quadratic,

\[
|Q(A+H)-Q(A)|
\le C_dnp^2\left(2\|A\|_F\|H\|_F+\|H\|_F^2\right),
\]

so

\[
\boxed{
|Q(A+H)-Q(A)|
\le C_d\left(
\frac{p^{7/2}\sqrt{\log n}}{\sqrt n}
+\frac{p^5}{n}
\right).
}
\]

Therefore the **congruence-shift distortion itself** is `1+o(1)` throughout

\[
p^7\log n=o(n).
\]

This is a `1/7` scale, strictly beyond Huang's `1/8` scale. The construction is exact; no random or numerical step is involved.

A technical boundary note is required. Addition of `Delta` can move a point across the chosen truncation boundary defining `E` or `\widetilde E`. At `p^7 log n=o(n)`, all central entries are much larger than `O(p)`, so positivity is unaffected. Boundary-shell bookkeeping still has to be performed when this lemma is inserted into the full Proposition 4.1 proof. I am **not** claiming that bookkeeping completed here; the proved statement is the correction lemma and its pointwise quadratic-weight distortion.

---

## 6. A second localization: the count lattice has covering radius O(p), not O(p^2)

Let

\[
\Lambda:=\{H=H^T\in\mathbb Z^{p\times p}: H_{ii}\text{ even},\ \sum_{i,j}H_{ij}=0\}.
\]

This is the difference lattice underlying `\widetilde E`.

### Lemma 6.1 — covering radius

In the Frobenius norm on the total-sum-zero symmetric subspace,

\[
\rho(\Lambda)\le Cp.
\]

#### Proof

Take a real symmetric total-sum-zero matrix `X`. Round every off-diagonal pair to the nearest integer and every diagonal entry to the nearest even integer. Before enforcing the total-sum constraint, the Frobenius rounding error is `O(p)` because there are `Theta(p^2)` coordinates and every coordinate error is `O(1)`.

The rounded matrix has even diagonal, and its total sum `T` is even. Since the original total sum is zero and each rounded coordinate differs by `O(1)`, `|T|=O(p^2)`. Changing one symmetric off-diagonal pair by `+1` or `-1` changes the total sum by `2` and adds squared Frobenius distance `2`. Use `|T|/2=O(p^2)` distinct off-diagonal pairs with the appropriate sign to restore total sum zero. The additional Frobenius distance is therefore `O(sqrt(p^2))=O(p)`. QED.

### Corollary 6.2 — pure Riemann-cell distortion has a 1/6-scale bound

After normalization by `dn`, a fundamental cell may be chosen with covering radius `O_d(p/n)`. On Huang's central ball, the quadratic-weight oscillation across such a cell is at most

\[
O_d\!\left(
\frac{p^3\sqrt{\log n}}{\sqrt n}
+\frac{p^4}{n}
\right).
\]

#### Proof

Use the same quadratic estimate as in Section 5 with `||H||_F=O_d(p/n)` instead of `O_d(p^(3/2)/n)`. QED.

Thus the intrinsic mesh of the Gaussian lattice sum is not a `1/8` obstruction. Completing a full Riemann-sum replacement still requires standard control of cells crossing the truncation boundary, but the local cell distortion is already compatible with `p<<n^(1/6)`.

---

## 7. Exact location of the remaining gluing failure

After Sections 3--6, the remaining obstruction is no longer an unidentified `p^4` term.

For each row `i`, after Huang's orthogonal reduction the central Fourier integral can be written schematically as

\[
I_i(M)=\int_{\mathbf1^\perp}
\exp\left(
-\frac{dn_i}{2p}\|s\|_2^2
-i\langle s,b_i(M)\rangle
-i\frac{C_{d,p}n_i}{6p}\sum_j s_j^3
\right)ds,
\]

up to a uniform multiplicative remainder `1+O(p^6(log n)^2/n)` and exponentially small outer-frequency tails. Huang drops the cubic term, at which point `I_i(M)` is an explicit Gaussian and the product over rows becomes a quadratic function of the symmetric matrix `M`. Nguyen--Pan keep the cubic term in the directed model and can continue because the directed count variable has only one global type vector rather than a symmetric `p x p` edge-count matrix.

In the undirected model the row targets satisfy

\[
m_{ij}=m_{ji},
\]

and this is precisely where the product `prod_i I_i(M)` must be summed over a coupled symmetric lattice. Taking absolute values of the cubic term too early recreates a `p^4/sqrt(n)`-type loss; keeping it as a phase preserves the improved Taylor remainder.

### The missing lemma, stated without disguise

Let `W_St(M)` denote Huang's exact Stirling/combinatorial prefactor for an equidistributed symmetric matrix. Prove, for odd primes with

\[
p\ll (n/\log n)^{1/7},
\]

that

\[
\sum_{M\in E}W_{St}(M)\prod_i I_i(M)
=(1+o(1))\times\text{(Huang's quadratic Gaussian main term)}.
\]

Call this the **symmetric cubic-gluing lemma**.

If this lemma is established with the existing sparse-class sieve from the preceding run, the already-proved correction and mesh lemmas above remove the other `1/8` losses and the same finite-field argument immediately yields

\[
\Pr(A_{n,3}\text{ singular})\le n^{-1/7+o(1)}.
\]

This is a **conditional implication only**. The frozen metric remains `a_3>=1/8` until the cubic-gluing lemma itself is proved.

---

## 8. Why the new lemmas are noncircular

The argument uses three inputs that do not depend on the desired sharp exponent.

1. Huang's exact configuration-model decomposition and quadratic form are published independently of R7-07.
2. Nguyen--Pan's moment identities are for the same finite-field walk `U_{d,p}` but in a directed application; importing the moment calculation does not import their directed singularity theorem as an undirected conclusion.
3. Lemmas 4.1 and 6.1 are deterministic integer-lattice statements proved above from scratch.

The previous R7-07 sparse-support theorem is not needed for Lemmas 3.1, 4.1, or 6.1. It enters only in the conditional final implication from an improved equidistributed estimate to a stronger singularity exponent.

---

## 9. Dated literature check — 2026-09-18

* Vu's primary survey/arXiv record remains arXiv:2005.02797 (2020; Probability Surveys 2021). The ordinary nonsingularity conjecture is now known, while the source's sharp polynomial decay question is the target retained by F0003.
* Huang's current arXiv record for the undirected fixed-degree quantitative theorem is arXiv:1807.06465v2 (last 2018 revision; journal version later). Its published undirected quantitative exponent is the interface being sharpened here.
* Nguyen--Pan, arXiv:2308.06461, published in *European Journal of Combinatorics* in 2024, proves an `n^{-1/3+o(1)}` bound for the **directed** fixed-degree model and explicitly develops the broader characteristic-function method. It does not state the symmetric sharp exponent.
* Huang--McKenzie--Yau's 2024/2025 random-regular work concerns Ramanujan property, rigidity, and edge universality, not the rare exact-zero singularity exponent.
* A bounded 2026-09-18 web search did not surface a later source resolving `Pr(A_{n,d} singular)=n^{-d+2+o(1)}` for the undirected fixed-degree model. This is negative evidence only; worldwide openness and publication novelty remain **UNVERIFIED**.

---

## 10. Outcome and next attack

### Proven this run

1. The directed cubic moment calculation transfers exactly to each row of Huang's undirected configuration decomposition.
2. Retaining that cubic phase improves the **local characteristic-function Taylor remainder** from the quadratic-only `1/8` scale to a `1/6` scale.
3. Every congruence residue class needed in Huang's `E -> tilde E` smoothing has an exact symmetric correction with even diagonal, zero total sum, `max|Delta_ij|=O_d(p)` and
   \[
   \boxed{\|\Delta\|_F=O_d(p^{3/2})}.
   \]
4. The resulting pointwise Gaussian-weight distortion is
   \[
   O_d\left(p^{7/2}\sqrt{\log n/n}+p^5/n\right),
   \]
   compatible with a `1/7` scale.
5. The unconstrained symmetric count lattice has covering radius `O(p)`, so pure Riemann-cell distortion is compatible with a `1/6` scale.

### Not proved

The symmetric cubic-gluing lemma is still missing. Therefore no `1/7` singularity exponent is claimed and the source is not solved.

### Frozen metric

`a_3 >= 1/8 -> a_3 >= 1/8` (**NO MOVEMENT**).  
Ordinary unchanged count after the preceding movement run: `0 -> 1`.

### Next nonrepeating methods

Use **B11 DUALIZE / B25 DOUBLE-COUNT / B18 TRANSLATE THE STATEMENT**:

1. B11: impose the row congruences by exact character/Fourier filters rather than deterministic translates and identify the nontrivial dual frequencies of the symmetric lattice;
2. B25: interchange the symmetric `M`-sum with the row Fourier integrals before taking absolute values, looking for cancellation of the cubic phases under `m_ij=m_ji`;
3. B18: translate the resulting central object into expectation of an explicit cubic polynomial under Huang's Gaussian on `Sym_p^0`, with the target estimate `E exp(i C_3)=1+o(1)` or an exact obstruction.

The simplest unresolved subproblem is the cubic-gluing lemma restricted to `d=3` and exact uniform row sizes `n_i=n/p`; solving even that special central case would determine whether the `1/7` route is genuinely viable.
