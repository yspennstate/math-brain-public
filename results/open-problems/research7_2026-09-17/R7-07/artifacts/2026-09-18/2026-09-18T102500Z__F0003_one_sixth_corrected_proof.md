Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — corrected proof artifact for the 1/6 singularity exponent

Date: 2026-09-18 UTC. Slot: R7-07. Native ID: `6aabe8413f60819197825dd81ca138ae`.

Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797, Section 5 immediately after Theorem 5.2. The full source target is the sharp exponent `d-2` for the singularity probability of the adjacency matrix of a uniformly random simple fixed-d regular graph. The frozen R7-07 metric is

`a_3 = sup{ a >= 0 : P(A_{n,3} singular) <= n^{-a+o(1)} }`.

Before this proof: `a_3 >= 1/7`. After this proof: `a_3 >= 1/6`. This is MOVEMENT but remains PARTIAL relative to the source, whose d=3 endpoint is `a_3=1`.

Methods used: B14 (find the group acting), B6 (deform to a solved point), B29 (add the points at infinity). The previous triple was B11/B25/B18.

This file supersedes the same-run artifact `2026-09-18T102000Z__F0003_isotypic_gaussian_core_improves_exponent_to_one_sixth.md` only for presentation: exact-SHA readback exposed two escaped-control-character formatting defects in displayed formulas there. The mathematical content below is the corrected plain-ASCII version and is the artifact to cite.

---

## 1. Cumulative input

Earlier R7-07 work established the following ingredients.

1. Huang's sparse third non-equidistributed finite-field class can be replaced by a field-independent support sieve. Its contribution is `O_d(n^{2-d})`, with support cutoff `O(p^3 log n)`.
2. For Huang's one-row random walk on `U_{d,p}`, the logarithmic characteristic function has the expansion
   `log phi(s) = -(d/(2p)) ||s||^2 - i (C_{d,p}/(6p)) sum_j s_j^3 + R(s)`,
   where
   `|R(s)| <= C_d [ p^{-2} ||s||^4 + p^{-1} sum_j s_j^4 ]`.
3. The symmetric cubic terms can be glued globally: with the notation below, the leading cubic perturbation has Gaussian average `1 + O_d(p^6 (log n)^3 / n)`.
4. Every exact congruence class has a symmetric integer representative Delta satisfying `||Delta||_F = O_d(p^{3/2})`; translating by it changes the cubic exponent by `O_d(p^{11/2} log n/n)`.
5. These facts already yielded
   `P(A_{n,d} singular) <= O_d(n^{2-d}) + n^{-1/7+o(1)}`.

The remaining 1/7 losses were worst-case estimates on the exact row-normalization denominator, the fourth-order row remainder, and the quadratic cost of translating a congruence class.

---

## 2. B14: exact S_p-isotypic diagonalization

Let A be a real symmetric p by p matrix with total entry sum zero. Define

`r = A 1`,

`B(r) = (r 1^T + 1 r^T)/p`,

`H = A - B(r)`.

Because `1^T r = 0`, one has exactly

`H 1 = 0`,

`<H,B(r)>_F = 0`,

`||B(r)||_F^2 = 2 ||r||^2 / p`.

Huang's quadratic exponent is

`Q(A) = (d n p^2 / 4) ||A||_F^2 - ((d-1) n p / 2) ||r||^2`.

Substituting the orthogonal decomposition gives the exact identity

`Q(A) = (d n p^2 / 4) ||H||_F^2 + (n p / 2) ||r||^2`.        (2.1)

This is the required isotypic splitting: H is the symmetric row-sum-free sector and r is the standard representation sector.

The row-deviation matrix used in the local central limit theorem is

`u_ij = p A_ij - r_i`.

Since `p A = p H + r 1^T + 1 r^T`, cancellation of the row term gives

`u = p H + 1 r^T`.                                             (2.2)

The two terms in (2.2) are Frobenius-orthogonal, so

`||u||_F^2 = p^2 ||H||_F^2 + p ||r||^2`.                       (2.3)

For every fixed d >= 3, (2.1)-(2.3) imply

`Q(A) >= (n/2) ||u||_F^2`.                                    (2.4)

Normalize

`X = sqrt(n) p H`, `Y = sqrt(n p) r`, `Z = sqrt(n) u`.

Under the continuous Gaussian density proportional to exp(-Q), X and Y are independent centered Gaussian vectors and

`Q = (d/4) ||X||_F^2 + (1/2) ||Y||^2`,

`Z = X + 1 (Y/sqrt(p))^T`.                                    (2.5)

Every coordinate of Z has variance bounded by a constant depending only on d.

For `S_i = sum_j Z_ij^2`, standard Gaussian norm concentration yields, for K=K(d) sufficiently large,

`P( ||Y||^2 > K p log p or max_i S_i > K p log p ) <= exp(-c_d p log p)`.    (2.6)

Call the complementary event the isotypic Gaussian core.

---

## 3. Exact row normalization is harmless through the 1/6 scale

The exact row-normalization correction retained from the preceding artifact is

`E2(A) = (d n/2) sum_i U_i [ p r_i / (1+p r_i) ]`,

where `U_i = sum_j u_ij^2 = S_i/n`.

On the Gaussian core,

`rho := max_i |p r_i| <= p ||r|| = sqrt(p/n) ||Y|| <= C_d p sqrt(log p/n)`,

and

`sum_i U_i <= C_d p^2 log p / n`.

For rho <= 1/2 this gives the pointwise core bound

`|E2(A)| <= C_d p^3 (log p)^{3/2} / sqrt(n)`.                  (3.1)

The old p^(7/2) estimate is therefore not the typical scale.

Outside the core but still inside Huang's original equidistributed ball, use (2.4):

`|E2(A)| <= C_d rho Q(A)`,

while the broad-ball estimate gives

`rho <= C p^{3/2} sqrt(log n/n)`.

At the prime scale chosen in Section 7 this is o(1). Thus inserting exp(E2) cannot turn the exponentially small Gaussian complement of (2.6) into a main contribution. The normalized contribution of E2 is 1+o(1) whenever

`p^3 (log p)^{3/2} / sqrt(n) = o(1)`.                          (3.2)

This already allows p = n^(1/6) with logarithmic slack.

---

## 4. B29: average the fourth-order row remainder instead of maximizing it

For one row, the real Gaussian variable after the contour shift has coordinate variance `O_d(p^2/n)` and dimension p. Hence

`E ||s||^4 = O_d(p^6/n^2)`,

`E sum_j s_j^4 = O_d(p^5/n^2)`.

Since the row sample size satisfies `n_i asymp n/p`, multiplying by the two coefficients in the fourth-order bound gives `O_d(p^3/n)` for one row, and therefore

`O_d(p^4/n)`                                                       (4.1)

after all p rows.

The imaginary saddle displacement eta_i satisfies the analytic local bound

`||eta_i|| <= C_d p ||t_i||`,

where

`t_ij = q_ij - 1/p = u_ij / (1+p r_i)`.

Using `S_i = sum_j Z_ij^2`, the target-only fourth-order terms are bounded by

`C_d [ (p/n) sum_i S_i^2 + (p^2/n) sum_{i,j} Z_ij^4 ]`.          (4.2)

The original equidistributed ball gives, without any typicality assumption,

`sum_i S_i = ||Z||_F^2 = n ||u||_F^2 <= C p^2 log n`.

Therefore

`sum_i S_i^2 <= C p^4 (log n)^2`,

`sum_{i,j} Z_ij^4 <= C p^4 (log n)^2`.

The target contribution is consequently

`O_d( p^5 (log n)^2/n + p^6 (log n)^2/n )`.                    (4.3)

Mixed real/imaginary quartic terms are bounded by Cauchy-Schwarz and are no larger than

`O_d( p^4 log n/n + p^6 (log n)^2/n )`.

Equivalently, in each row one may restrict the real Fourier integral to

`||s||^2 <= K p^3 log p/n`,

`max_j |s_j|^2 <= K p^2 log p/n`,

whose Gaussian complement is exp(-c p log p), use the fourth-order bound uniformly on this core, and retain Huang's characteristic-function decay outside.

Thus the old aggregate error `O(p^7 (log n)^2/n)` is replaced by

`epsilon_4 = O_d( p^4 log n/n + p^6 (log n)^2/n )`.             (4.4)

The factor p^7 arose from placing every row simultaneously on the boundary of a Fourier ball sized for the worst row; it is not the Gaussian-integrated scale.

---

## 5. The cubic correction remains harmless

The preceding symmetric gluing artifact writes the leading cubic perturbation as

`C0(A) = lambda T(Z)`,

`lambda = C_{d,p} p/sqrt(n)`,

`T(Z) = sum_{i,j} Z_ij^3`.

T is odd under A -> -A. On the symmetric Gaussian lattice/continuum the cosh argument from the preceding artifact gives

`E_Q exp(C0) = 1 + O_d( p^6 (log n)^3/n )`.                    (5.1)

Restoring the exact denominators changes the cubic exponent by

`O_d( p^(11/2) (log n)^2/n )`.                                 (5.2)

Both terms are o(1) at p = n^(1/6) with logarithmic slack.

For tail domination, (2.4) and `max |u_ij| <= ||u||_F <= p ||A||_F` show on the full equidistributed ball that

`|C(A)| <= o(1) Q(A)`

at that same scale. Thus the cubic perturbation does not resurrect the complement of the Gaussian core.

---

## 6. B6: deform congruence cosets at the level of Gaussian mass

The preceding congruence lemma constructs a symmetric integer correction Delta with

`||Delta||_F = O_d(p^(3/2))`                                   (6.1)

for every required exact congruence class. The old 1/7 proof bounded the cross term in Q pointwise. The correct object is the Gaussian theta mass of a coset.

Use count coordinates `W = d n A`. From (2.1), the eigenvalues of the quadratic form in W are all between constant multiples (depending only on d) of `p^2/n` on the symmetric total-sum-zero space.

The exact character identity from the preceding artifact is

`1_{L(W)=0} = |G|^{-1} sum_{chi in G-hat} chi(L(W))`,

with `|G| = d^(p-1) p^p`.

For a nontrivial character, at least one independent count-coordinate frequency is a nonzero multiple of 1/p (or 1/d). Modulo the dual of the unconstrained symmetric count lattice, the distance is at least `c_d/p`. Poisson summation for the Gaussian theta series therefore gives

`|S_chi/S_1| <= exp( C_d p^2 log p - c_d n/p^4 )`.              (6.2)

The entropy term `C_d p^2 log p` follows from the elementary packing bound for a dual lattice in dimension O(p^2). Since `log |G| = O(p log p)`, summing (6.2) over the nontrivial characters yields

`S_congruent = (1+o(1)) |G|^{-1} S_unconstrained`               (6.3)

provided

`n/p^4 >> p^2 log p`.                                          (6.4)

This condition has a large margin at the 1/6 scale used below.

There is a complementary translate estimate. Put `h = Delta/(d n)`. From (6.1) and the exact diagonalization,

`Q(h) = O_d(p^5/n) = o(1)`.                                    (6.5)

Completing the square shows that the normalized Gaussian on a congruence translate differs from the zero-congruence Gaussian by an exponential linear tilt whose L2 cost is `exp(O(Q(h))) = 1+o(1)`. The Poisson estimate is uniform in the center, so this discrete statement has the same bound as its continuous Gaussian analogue.

The zero congruence lattice is symmetric under A -> -A, hence the odd-cubic cancellation in Section 5 holds there exactly. Translation by h changes the cubic exponent by the already-proved `O_d(p^(11/2) log n/n)` and changes the normalized row-deviation vector by

`||sqrt(n) u(h)||_F = O_d(p^(5/2)/sqrt(n)) = o(1)`.             (6.6)

Completing the square also gives subgaussian linear moment bounds on every congruence translate. A 1/2-net argument then gives the row-norm concentration used in (2.6) uniformly over the translates. Therefore the denominator correction, cubic correction, and integrated fourth-order correction each have normalized expectation 1+o(1) on the exact congruence class. No pointwise p^(7/2)/sqrt(n) Gaussian cross-term is needed.

---

## 7. Error table and prime choice

The sufficient errors are now:

- Stirling: `O(p^3 (log n)^(3/2)/sqrt(n))`;
- exact row denominator on the isotypic core: `O(p^3 (log p)^(3/2)/sqrt(n))`;
- integrated fourth-order row term: `O(p^4 log n/n + p^6 (log n)^2/n)`;
- contour factor: `O(p^3 sqrt(log n/n))`;
- cubic Gaussian average: `O(p^6 (log n)^3/n)`;
- nontrivial congruence characters: `exp(C p^2 log p - c n/p^4)`;
- congruence translate energy: `O(p^5/n)`;
- congruence cubic distortion: `O(p^(11/2) log n/n)`;
- Riemann quadratic cell distortion: `O(p^3 sqrt(log n/n) + p^4/n)`;
- Riemann cubic cell distortion: `O(p^5 log n/n)`.

Set

`x_n = n^(1/6)/(log n)^2`.

By Bertrand's postulate, for all sufficiently large n choose a prime `p_n in [x_n,2x_n]`. For fixed d, eventually p_n is odd, greater than d, and therefore does not divide d. Every error above is o(1). In particular,

`p^3 (log n)^(3/2)/sqrt(n) = O((log n)^(-9/2))`,

`p^6 (log n)^3/n = O((log n)^(-9))`,

and

`n/p^4 = Theta(n^(1/3) (log n)^8) >> p^2 log p`.

Hence Huang's equidistributed finite-field contribution has bounded expected number of nonzero kernel vectors at `p=n^(1/6-o(1))`.

---

## 8. Non-equidistributed vectors

Huang's first, second, and fourth non-equidistributed regimes remain exponentially small at this p. The cumulative R7-07 sparse-support sieve gives

`P(E_sparse) = O_d(n^(2-d))`.

Its support cutoff is still valid because

`p^3 log n = O(n^(1/2) (log n)^(-5)) = o(n)`.

If `N_ns` denotes the number of nonzero F_p-kernel vectors outside the sparse event, then

`E N_ns = O_d(1)`.                                              (8.1)

---

## 9. Theorem

For every fixed integer d >= 3, let A_{n,d} be the adjacency matrix of a uniformly random simple d-regular graph. Then

`P(A_{n,d} singular over R) <= O_d(n^(2-d)) + n^(-1/6+o(1))`.  (9.1)

In particular,

`P(A_{n,3} singular) <= n^(-1/6+o(1))`,

so

`a_3 >= 1/6`.                                                   (9.2)

### Proof

Choose `p=p_n` from Section 7. Sections 2-7 extend the finite-field equidistributed calculation used in the preceding R7-07 1/7 theorem to `p=n^(1/6-o(1))`; Section 8 preserves the non-equidistributed contribution. Hence, outside E_sparse, the expected number of nonzero F_p-kernel vectors is O_d(1).

If A is singular over F_p outside E_sparse, its kernel contains at least p-1 nonzero vectors. Thus

`(p-1) 1_{A singular over F_p and E_sparse^c} <= N_ns`.

Taking expectations and using (8.1),

`P(A singular over F_p) <= O_d(n^(2-d)) + O_d(1/p)`.

An integer matrix singular over R has determinant zero and is therefore singular modulo every prime. Consequently the same upper bound holds over R. Finally `1/p = n^(-1/6+o(1))`, proving (9.1) and (9.2). QED.

---

## 10. Scope, source check, and next obstruction

This does not solve Vu's sharp-exponent question. The source-predicted d=3 endpoint is exponent 1, not 1/6, and full source closure requires exponent d-2 for every fixed d >= 3.

The dependency chain is noncircular: Huang supplies the undirected finite-field decomposition and outer/non-equidistributed estimates; earlier R7-07 work supplies the sparse-support sieve; Nguyen-Pan is used only for the identical one-row U_{d,p} cumulant calculation; the preceding R7-07 artifact supplies symmetric cubic gluing and the sparse congruence representative; this artifact supplies the isotypic diagonalization, integrated fourth-order estimate, and Gaussian coset deformation.

Fresh bounded literature checks dated 2026-09-18 recovered Vu arXiv:2005.02797, Huang arXiv:1807.06465, Nguyen-Pan arXiv:2308.06461, Huang-McKenzie-Yau arXiv:2412.20263, Huang-Yau arXiv:2602.00975, and the September 2026 directed hard-edge paper arXiv:2609.05297. The latter works do not state the undirected sharp fixed-degree exponent `d-2`. No source-matching later theorem was recovered in the bounded check. This is negative evidence only; worldwide openness and publication novelty remain UNVERIFIED.

At 1/6 the surviving terms `p^3/sqrt(n)`, `p^6/n`, and the first even Edgeworth correction meet. The next nonrepeating methods are B5 (parameterize and differentiate the cumulant strength), B12 (seek a conserved global second-Edgeworth tensor after symmetric gluing), and B24 (identify the extremal S_p-isotypic direction). The next metric milestone is `a_3 >= 1/5`; it is not claimed here.
