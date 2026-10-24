Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated binding model/effort selector or runtime telemetry is exposed.

# F0011 — sublinear minimal polynomial, integral spectral-projector lattice, and a three-deletion reconstruction theorem

Date: 2026-09-19 UTC  
Slot: `R7-06`  
Target: Van H. Vu, Conjecture 9.4, integral spectrum of a symmetric Rademacher matrix.  
Methods: **B3 / B11 / B19**.

## 1. Setup

Let `M` be a real symmetric `n x n` matrix with every entry in `{+1,-1}` and suppose its spectrum is integral. Write its distinct eigenvalues as

\[
\theta_1<\cdots<\theta_r,
\qquad
\operatorname{mult}(\theta_j)=m_j,
\qquad
\sum_{j=1}^r m_j=n.
\]

Set

\[
\chi_M(t)=\prod_{j=1}^r(t-\theta_j)^{m_j},
\qquad
g(t)=\prod_{j=1}^r(t-\theta_j),
\qquad
f(t)=\frac{\chi_M(t)}{g(t)}
=\prod_{j=1}^r(t-\theta_j)^{m_j-1}.
\]

The previous R7-06 runs proved the parity theorem

- `n` even: every integral eigenvalue is even;
- `n` odd: exactly one eigenvalue, counted with multiplicity, is odd;

and reduced Vu 9.4 to proving subquadratic entropy of every fixed integral spectral fiber after switching and permutation quotients.

The present run attacks the fixed fiber through the minimal polynomial, rational spectral projectors, and principal spectral decks.

---

## 2. B3 — a deterministic sublinear-degree annihilator for every target matrix

### Theorem 2.1 — explicit bound on the number of distinct eigenvalues

If `n` is even, then

\[
\boxed{r(r^2-1)\le 3n^2.} \tag{2.1}
\]

If `n` is odd, then

\[
\boxed{
1+\frac{(r-1)((r-1)^2-1)}{3}\le n^2.
} \tag{2.2}
\]

Consequently, in all cases

\[
\boxed{r=O(n^{2/3}).} \tag{2.3}
\]

In particular every integral-spectrum symmetric sign matrix is annihilated by the monic integer polynomial

\[
\boxed{g(M)=0,\qquad \deg g=r=O(n^{2/3}).} \tag{2.4}
\]

#### Proof

Every symmetric sign matrix satisfies

\[
\sum_{i=1}^n\lambda_i^2=\operatorname{tr}(M^2)=n^2. \tag{2.5}
\]

For an integer `q>=1`, let `E(q)` be the least possible sum of squares of `q` distinct even integers. If `q=2s+1`, the minimizer is

\[
0,\ \pm2,\ \pm4,\ldots,\pm2s,
\]

so

\[
E(2s+1)=8\sum_{k=1}^s k^2
=\frac{(2s+1)((2s+1)^2-1)}3.
\]

If `q=2s`, a minimizer is

\[
0,\ \pm2,\ldots,\pm2(s-1),\ 2s,
\]

and

\[
E(2s)=8\sum_{k=1}^{s-1}k^2+4s^2
=\frac{(2s)((2s)^2+2)}3.
\]

Therefore, for every `q`,

\[
E(q)\ge \frac{q(q^2-1)}3. \tag{2.6}
\]

If `n` is even, all `r` distinct eigenvalues are even. Taking one copy of each distinct eigenvalue in (2.5) and using (2.6) gives (2.1).

If `n` is odd, exactly one eigenvalue is odd and the remaining `r-1` distinct eigenvalues are even. The odd eigenvalue contributes at least `1` to the square sum, while the even ones contribute at least `E(r-1)`. This gives (2.2).

Finally, because `M` is real symmetric, it is diagonalizable and its minimal polynomial is exactly the square-free polynomial `g`; hence `g(M)=0`. QED.

### Corollary 2.2 — exact two-root boundary

Suppose `r=2`, with roots `theta,phi`. Put `s=theta+phi` and `p=theta phi`. Then

\[
M^2-sM+pI=0. \tag{2.7}
\]

Taking diagonal entries gives

\[
n-sM_{ii}+p=0. \tag{2.8}
\]

Thus either:

1. `s != 0`, in which case **every diagonal entry is the same sign** `(n+p)/s`; or
2. `s=0`, in which case `theta=-phi`, `theta^2=n`, and

\[
\boxed{M^2=nI.} \tag{2.9}
\]

Therefore the second branch is exactly the symmetric-Hadamard locus, and integrality forces `n` to be a perfect square.

This is the sharp obstruction to the proposed stronger `exp(O(n log n))` fiber target: even the two-root case already contains symmetric Hadamard enumeration. Ferber–Jain–Zhao prove the first quadratic-exponent improvement for general Hadamard counting and explicitly state that even `2^{o(n^2)}` would require new ideas; their stronger `2^{O(n log n)}` growth conjecture remains open. Hence B3 does not justify claiming the stronger uniform fiber estimate.

### B3 outcome

The gain is structural rather than source closure: **every** target matrix, without any probabilistic semicircle input, lies on an integer matrix variety `g(M)=0` whose annihilating degree is `O(n^{2/3})`. The strongest proposed `exp(O(n log n))` fixed-fiber bound immediately meets the symmetric-Hadamard boundary when `r=2`, so that route cannot be treated as routine compression.

---

## 3. B11 — dualize a fixed spectrum into an integral projector lattice

Let `P_j` be the orthogonal spectral projector onto the `theta_j`-eigenspace. For a vertex `i`, let `M^{(i)}` denote the principal matrix obtained by deleting row and column `i`, and put

\[
\chi_i(t)=\det(tI-M^{(i)}).
\]

### Theorem 3.1 — rooted deletion polynomial and exact rational weights

For every vertex `i`,

\[
\boxed{\chi_i(t)=f(t)q_i(t)} \tag{3.1}
\]

for a monic polynomial `q_i in Z[t]` of degree `r-1`. Moreover

\[
\boxed{
((tI-M)^{-1})_{ii}=\frac{q_i(t)}{g(t)}
=\sum_{j=1}^r\frac{w_{ij}}{t-\theta_j},
} \tag{3.2}
\]

where

\[
\boxed{
w_{ij}=(P_j)_{ii}
=\frac{q_i(\theta_j)}{g'(\theta_j)}.
} \tag{3.3}
\]

The weights satisfy

\[
w_{ij}\ge0,\qquad \sum_jw_{ij}=1,\qquad
\sum_j\theta_jw_{ij}=M_{ii}\in\{\pm1\}, \tag{3.4}
\]

and, for every `j`,

\[
\boxed{\sum_{i=1}^n w_{ij}=m_j.} \tag{3.5}
\]

Equivalently,

\[
\boxed{
\sum_{i=1}^n q_i(t)=\frac{\chi_M'(t)}{f(t)}
=\sum_{j=1}^r m_j\prod_{k\ne j}(t-\theta_k).
} \tag{3.6}
\]

#### Proof

Cauchy interlacing implies that deleting one row and column lowers the multiplicity of each eigenvalue by at most one, so `chi_i` is divisible by `f`. Since both polynomials are monic integral polynomials and `f` is monic, exact division gives `q_i in Z[t]`; its degree is

\[
(n-1)-(n-r)=r-1.
\]

Cramer's rule gives

\[
((tI-M)^{-1})_{ii}=\frac{\chi_i(t)}{\chi_M(t)}=\frac{q_i(t)}{g(t)}.
\]

The spectral theorem gives the second equality in (3.2), with `w_ij=(P_j)_{ii}`. Taking residues at `theta_j` gives (3.3). Positivity and the first sum in (3.4) follow because the `P_j` are orthogonal projectors summing to `I`; the first moment gives `M=sum_j theta_j P_j`, hence the diagonal identity in (3.4). Taking traces of `P_j` gives (3.5).

Finally, the derivative of a determinant is the sum of its diagonal cofactors, so

\[
\chi_M'(t)=\sum_i\chi_i(t)=f(t)\sum_iq_i(t),
\]

which is (3.6). QED.

### Corollary 3.2 — finite lattice of possible rooted signatures

Because `q_i(theta_j)` is an integer and `0<=w_ij<=1`, each value `q_i(theta_j)` has at most

\[
|g'(\theta_j)|+1
\]

possibilities. Since the `r` interpolation values determine `q_i`, the number of possible rooted deletion polynomials in a fixed spectral fiber is at most

\[
\boxed{
\prod_{j=1}^r\bigl(|g'(\theta_j)|+1\bigr).
} \tag{3.7}
\]

Every eigenvalue lies in `[-n,n]`, so

\[
|g'(\theta_j)|
=\prod_{k\ne j}|\theta_j-\theta_k|
\le (2n)^{r-1}.
\]

Thus the number of rooted signatures is

\[
\boxed{\exp(O(r^2\log n)).} \tag{3.8}
\]

This is not yet a fixed-fiber count: many non-switching-equivalent matrices can share all one-vertex rooted signatures.

### Theorem 3.3 — simultaneous exact finite-field rank profile at every good prime

Let

\[
\Delta(g)=\prod_{j<k}(\theta_j-\theta_k).
\]

If a prime `p` does not divide `Delta(g)` — in particular, any prime `p>2n` is good — then the reduction `M mod p` is diagonalizable over `F_p` and

\[
\boxed{
\dim_{\mathbb F_p}\ker(M-\theta_jI)=m_j
\quad\text{for every }j.
} \tag{3.9}
\]

#### Proof

The exact integer identity `g(M)=0` survives modulo `p`. At a good prime `g mod p` has distinct linear roots, hence is square-free. Therefore the minimal polynomial of `M mod p` is square-free and `M mod p` is diagonalizable. The characteristic polynomial reduces to

\[
\prod_j(t-\theta_j)^{m_j}
\]

with pairwise distinct roots modulo `p`; for a diagonalizable matrix, algebraic and geometric multiplicities agree. QED.

This is strictly stronger than merely requiring the characteristic polynomial to split modulo `p`: a fixed integral spectrum imposes the full simultaneous corank vector `(m_1,...,m_r)` at every good prime.

### Corollary 3.4 — integral scaled projectors

Define

\[
A_j:=\prod_{k\ne j}(M-\theta_kI).
\]

Then `A_j` is an integer symmetric matrix and

\[
\boxed{
A_j=g'(\theta_j)P_j,
\qquad
A_j^2=g'(\theta_j)A_j,
\qquad
A_jA_k=0\ (j\ne k).
} \tag{3.10}
\]

Thus if `p | g'(theta_j)`, then `A_j^2=0 mod p`; at good primes the normalized projectors are defined over `F_p`.

### Proposition 3.5 — why one-vector walk-matrix/SNF methods cannot directly cover F0011

For any vector `v`, the Krylov space

\[
\mathcal K(M,v)=\operatorname{span}\{v,Mv,M^2v,\ldots\}
\]

has dimension at most `r`. Indeed

\[
M^kv=\sum_j\theta_j^kP_jv,
\]

so it is contained in the span of the at most `r` vectors `P_jv`.

More generally, for a block of `k` seed vectors `B`, the block Krylov space can fill `R^n` only if

\[
\boxed{k\ge\max_jm_j\ge n/r=\Omega(n^{1/3}).} \tag{3.11}
\]

The first inequality holds because within the `theta_j`-eigenspace, applying powers of `M` does not create new directions; the block contributes at most `k` directions there.

The 2026 Raza–Ahmad–Shabbir–Abbas generalized-cospectral-mate bounds are built on nonsingularity of a one-vector walk matrix (controllability) and Smith-normal-form arithmetic. Proposition 3.5 shows that any such single-seed walk matrix is singular for every repeated-spectrum target, hence for every F0011 instance with `n>=6` by the previous R7-06 repeated-spectrum theorem. This is a genuine hypothesis mismatch, not a criticism of that work.

There is nevertheless a useful bridge. In the first-row switching normalization, let `e` be the all-ones vector, let `e_1` be the first coordinate vector, and put `d=M_11`, `c=1-d`. Then

\[
e=(M+cI)e_1. \tag{3.12}
\]

Writing `R(t)=(tI-M)^{-1}`, one obtains

\[
\boxed{
e^TR(t)e
=(t+c)^2R_{11}(t)-(t+2c)-d.
} \tag{3.13}
\]

Hence the full spectrum together with the single rooted polynomial `q_1` determines the characteristic polynomial of every rank-one perturbation `M+sJ` through

\[
\boxed{
\det(tI-M-sJ)
=\chi_M(t)\bigl(1-s\,e^TR(t)e\bigr).
} \tag{3.14}
\]

So the failure of the current walk-matrix method is specifically controllability/rank, not lack of access to a generalized rank-one spectrum.

### B11 outcome

A fixed spectral fiber is now dualized into a finite lattice of rational projector diagonals and simultaneous exact rank profiles at every good prime. The price is clear: F0011 lives in the maximally non-controllable repeated-spectrum regime, so the strongest current SNF walk-matrix mate bounds do not apply without a genuinely block-Krylov replacement.

A second obstruction is mod `2`: the parity theorem makes the annihilator identity automatic there. If `n` is even then `g(t)=t^r mod 2` and `M=J mod 2` with `J^2=0`; if `n` is odd then `g(t)=t^{r-1}(t+1) mod 2`, `M=J mod 2`, and `J^2=J`. Thus `g(M)=0 mod 2` carries no new information. Any adaptation of Caden Young's 2026 finite-field/rational-canonical strategy must therefore use a nontrivial `2`-adic lift (such as mod `4`) or odd primes rather than the bare `F_2` identity.

---

## 4. B19 — an exact reconstruction algorithm from the codimension-three spectral deck

For a subset `S` of vertices, write `M^{(S)}` for the principal submatrix obtained by deleting all indices in `S`, and

\[
\chi_S(t):=\det(tI-M^{(S)}).
\]

The **codimension-three spectral deck** is the labeled collection

\[
\{\chi_S(t): |S|\le3\}.
\]

### Theorem 4.1 — three-deletion spectral reconstruction

The codimension-three spectral deck of a symmetric sign matrix determines the matrix **up to diagonal sign switching**.

#### Proof

Let

\[
R(t)=(tI-M)^{-1}.
\]

Jacobi's complementary principal-minor identity gives, for every `S`,

\[
\boxed{
\frac{\chi_S(t)}{\chi_\varnothing(t)}
=\det R(t)_{S,S}.
} \tag{4.1}
\]

For `S={i}` this gives `R_ii(t)` exactly. Since

\[
R_{ii}(t)=t^{-1}+M_{ii}t^{-2}+O(t^{-3}),
\]

the diagonal sign `d_i=M_ii` is recovered.

For `S={i,j}`,

\[
\frac{\chi_{ij}}{\chi_\varnothing}
=R_{ii}R_{jj}-R_{ij}^2,
\]

so every rational function `R_ij(t)^2` is recovered.

For three distinct vertices,

\[
\frac{\chi_{ijk}}{\chi_\varnothing}
=R_{ii}R_{jj}R_{kk}
+2R_{ij}R_{ik}R_{jk}
-R_{ii}R_{jk}^2
-R_{jj}R_{ik}^2
-R_{kk}R_{ij}^2.
\]

All terms except the triple product are already known from the one- and two-deletion data, hence the deck determines

\[
R_{ij}(t)R_{ik}(t)R_{jk}(t). \tag{4.2}
\]

For `i != j`, the resolvent expansion is

\[
R_{ij}(t)=M_{ij}t^{-2}+O(t^{-3}),
\]

therefore

\[
R_{ij}R_{ik}R_{jk}
=\tau_{ijk}t^{-6}+O(t^{-7}),
\qquad
\tau_{ijk}:=M_{ij}M_{ik}M_{jk}. \tag{4.3}
\]

Thus every triangle product `tau_ijk` is recovered. The previous exact switching lemma says the diagonal signs together with all triangle products determine a labeled symmetric sign matrix up to diagonal sign conjugation. QED.

The theorem is an application of classical Jacobi identities and the principal-minor reconstruction mechanism; no novelty priority is claimed from the bounded search. Brunel–Urschel (Linear Algebra Appl. 703 (2024), 232–267; arXiv:2404.06302) give modern polynomial-time recovery theory for magnitude-symmetric matrices from principal minors. The point here is the specific **spectral-deletion** formulation adapted to the F0011 fiber.

### Proposition 4.2 — deletion levels one and two lose exactly the hard Hadamard information

On the symmetric-Hadamard branch `H^2=nI`,

\[
R(t)=(tI-H)^{-1}=\frac{tI+H}{t^2-n}. \tag{4.4}
\]

Therefore

\[
R_{ii}(t)=\frac{t+d_i}{t^2-n},
\qquad
R_{ij}(t)^2=\frac1{(t^2-n)^2}\quad(i\ne j). \tag{4.5}
\]

Hence, once the spectrum and diagonal vector are fixed, **the entire one- and two-deletion spectral deck is independent of every off-diagonal Hadamard sign**.

By contrast, for a triple `S={i,j,k}`,

\[
\frac{\chi_{ijk}(t)}{\chi_\varnothing(t)}
=
\frac{
(t+d_i)(t+d_j)(t+d_k)
-(t+d_i)-(t+d_j)-(t+d_k)
+2\tau_{ijk}
}{(t^2-n)^3}. \tag{4.6}
\]

So the first spectral-deletion level that sees the switching invariant `tau_ijk` is exactly level three.

This is an information-theoretic obstruction to solving F0011 using only vertex-deleted or pair-deleted spectra: on the deepest two-eigenvalue boundary those data deliberately erase the off-diagonal switching class, while the triple level restores it one triangle bit at a time.

### Proposition 4.3 — exact row-extension energy constraints

There is also a recursive form useful for the next attack. Write a principal extension as

\[
M=\begin{pmatrix}d&x^T\\x&B\end{pmatrix},
\qquad d\in\{\pm1\},\quad x\in\{\pm1\}^{n-1}.
\]

Let the distinct eigenvalues of `B` be `mu_a`, with orthogonal projectors `Q_a`. Schur complementation gives

\[
\frac{\chi_M(t)}{\chi_B(t)}
=t-d-x^T(tI-B)^{-1}x
=t-d-\sum_a\frac{\|Q_ax\|^2}{t-\mu_a}. \tag{4.7}
\]

Thus, once `B` and the target full characteristic polynomial are fixed, every allowed border sign vector `x` must satisfy the exact simultaneous quadratic constraints

\[
\boxed{
\|Q_ax\|^2
=-\operatorname*{Res}_{t=\mu_a}
\frac{\chi_M(t)}{\chi_B(t)}
\quad\text{for every }a,
} \tag{4.8}
\]

with the obvious cancellation interpretation when numerator and denominator share roots. Conversely these residue constraints, together with the `t-d` behavior at infinity, recover the characteristic polynomial.

Equation (4.8) isolates the next genuine counting problem: bound the number of sign vectors having a prescribed energy in every eigenspace of the previously exposed principal block. This is exactly the type of vector anti-concentration problem for which the Hadamard counting work of Ferber–Jain–Zhao is the nearest strong analogue.

### B19 outcome

The fixed spectral fiber now has an exact deterministic reconstruction hierarchy:

- one-deletion spectra = rational diagonal projector weights;
- two-deletion spectra = squared off-diagonal resolvent data;
- three-deletion spectra = triangle signs, hence the whole switching class.

The symmetric-Hadamard branch proves that level two is genuinely insufficient as a general strategy, while (4.8) converts level-three reconstruction into a row-by-row sign-vector anti-concentration problem rather than an opaque cospectrality question.

---

## 5. Literature check, 2026-09-19

A bounded current search was repeated for Vu Conjecture 9.4 / integral symmetric Rademacher spectrum. I did not locate a later source proving the `2^{-(1/2+o(1))n^2}` asymptotic. This is **negative search evidence only**, not an openness or novelty certificate.

Relevant current/nearby references recovered:

1. Van H. Vu, *Recent progress in combinatorial random matrix theory*, Probability Surveys 18 (2021), Conjecture 9.4; arXiv:2005.02797.
2. Yi Han, *On the rank of a random symmetric matrix in the large-deviation regime*, JLMS, first published 30 May 2026: `exp(-c k n)` large-corank control up to `k=O(sqrt n)`. It remains a one-shift result and does not sum the costs of the full multiplicity vector.
3. Caden Young, *Sharp Exponential Asymptotics for Normal Sign Matrices*, arXiv:2607.15294, 1 July 2026: obtains a sharp quadratic exponent by mod-4 reduction, rank duality, and finite-field rational canonical types. Its mechanism is a serious model for a multi-eigenspace attack, but the bare mod-2 annihilator of F0011 is automatic as explained above.
4. Muhammad Raza, Obaid Ullah Ahmad, Mudassir Shabbir, Waseem Abbas, *On the Enumeration of Generalized Cospectral Mates of Graphs*, arXiv:2601.07373 (2026): quantitative mate bounds from Smith-normal-form arithmetic of a nonsingular walk matrix. F0011's repeated spectra force every one-seed Krylov matrix to have rank at most `r<n`.
5. Victor-Emmanuel Brunel and John Urschel, *Recovering a Magnitude-Symmetric Matrix from its Principal Minors*, Linear Algebra Appl. 703 (2024), 232–267; arXiv:2404.06302: principal-minor recovery and quadratic-query algorithms.
6. Asaf Ferber, Vishesh Jain, Yufei Zhao, *On the number of Hadamard matrices via anti-concentration*, Combin. Probab. Comput. 31 (2022), 455–477; arXiv:1808.07222: the strongest direct counting analogue for the two-root Hadamard boundary.

No search miss above is used as a novelty proof.

---

## 6. Exact remaining gap and next attack

The source remains **PARTIAL / OPEN**. The frozen finite metric `N_exact` is unchanged at `8`; no new exhaustive `n=9` classification was attempted because this run was deliberately structural rather than checker-driven.

The new sharp bottleneck is equation (4.8): for a nested principal extension, how many sign vectors can simultaneously realize a prescribed collection of eigenspace energies? A proof that the cumulative logarithm of these branching numbers is `o(n^2)` would prove the fixed-spectrum entropy bound and hence Vu 9.4.

The next nonrepeating methods are fixed as

- **B12** condition on the principal-block spectral/multiplicity structure before counting the next sign row;
- **B21** formulate the row-extension problem as a conditional entropy bound;
- **B29** amortize anti-concentration savings from the simultaneous energy constraints across the entire exposure process.

A third consecutive `N_exact` no-movement run would make the **following** invocation the required thinking-only stuck diagnosis; this run is only the second unchanged F0011 run.
