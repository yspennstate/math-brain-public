# MOC4 fleet03/B20 — exact endpoint formula for the parity-payment gate

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Target:** four-dimensional Marcus–de Oliveira conjecture (MOC4)  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Inputs consumed

This run uses two current campaign results rather than restarting the problem.

1. **fleet03/B07, `MOC4-PARITY-SLACK-v1`.** In the standard 3-dimensional Hadamard representation, the exact mixed support inequality has six `S_3` fibers. For `rho in S_3`,

   `F_rho(K) = sum_i |K_{i,rho(i)}| - 2 m_rho(K)`,

   where `m_rho(K)=0` if the selected transversal product is nonnegative and otherwise is the minimum selected absolute entry. For the actual unitary blocks `D,R`, `|D_ij| <= R_ij`. A sufficient gate is the existence of a Birkhoff decomposition `R=sum lambda_rho R_rho` with

   `2 sum_rho lambda_rho m_rho(K) <= W(D,R,K)`,

   where

   `W(D,R,K) := sum_ij (R_ij |K_ij| - D_ij K_ij) >= 0`.

2. **fleet02/B08, `MOC4-REPEATED-MINIMAL-LIFT-v2`.** Repeated-spectrum faces have an exact smaller lift, and a violating simple-spectrum sequence approaching such a face must enter an explicit zero-nonrepeated-row or supported-hull-collinearity stratum. This lets the parity-slack route focus on the genuinely generic simple-spectrum core without pretending repeated spectra are absent from MOC4.

## 2. A direction correction in the convex-roof presentation

The B07 report introduced

`Psi_K(R)=min_lambda sum lambda_rho F_rho(K)`.

That quantity is a valid *strong* sufficient comparison, but it is not equivalent to the later existential parity-payment gate. Because

`sum lambda F = <R,|K|> - 2 sum lambda m`,

minimizing the average `F` **maximizes** the parity payment. The actual existential gate needs the opposite optimization.

Define instead

`Q_K(R) := min_{lambda: R=sum lambda R_rho} sum_rho lambda_rho m_rho(K)`.

Then the following statement is immediate and is the weakest `X`-independent gate supplied by this convex-combination argument.

### Proposition 1 — existential parity-payment gate

If

`2 Q_K(R) <= W(D,R,K)`,

then the exact six-fiber support inequality holds for **every** real `X`, hence the B07 mixed support inequality holds for the given MOC4 datum.

**Proof.** Choose a Birkhoff decomposition attaining `Q_K(R)`. The displayed inequality is exactly

`<D,K> <= sum_rho lambda_rho F_rho(K)`.

Also `<R,X>/2 = sum lambda_rho <R_rho,X>/2`. Therefore

`<D,K> + <R,X>/2 <= sum lambda_rho [F_rho(K)+<R_rho,X>/2]`

and the right side is at most the maximum of its six bracketed terms, which is the exact B07 six-fiber RHS. No common `(P,R)` lift is assumed. QED.

Equivalently, if

`Omega_K(R):=max_lambda sum lambda_rho F_rho(K)`,

then

`Omega_K(R)=<R,|K|>-2 Q_K(R)`,

and `<D,K> <= Omega_K(R)` is sufficient. This is the correct optimization direction for the existential gate.

## 3. Every 3x3 Birkhoff fiber is an interval

Order the six permutations as

- `e = (1,2,3)`,
- `s12 = (2,1,3)`,
- `s13 = (3,2,1)`,
- `s23 = (1,3,2)`,
- `c = (2,3,1)`,
- `cbar = (3,1,2)`.

Write their Birkhoff weights as

`lambda_e, lambda_12, lambda_13, lambda_23, lambda_c, lambda_cbar`.

For a fixed 3x3 doubly stochastic matrix `R=(r_ij)`, set `t=lambda_e`. Solving the nine barycenter equations gives **all** decompositions:

`lambda_e    = t`,

`lambda_12   = r33 - t`,

`lambda_13   = r22 - t`,

`lambda_23   = r11 - t`,

`lambda_c    = r12 - r33 + t`,

`lambda_cbar = r13 - r22 + t`.

Nonnegativity is equivalent to the single interval constraint

`L(R) <= t <= U(R)`,

where

`L(R)=max(0, r33-r12, r22-r13)`,

`U(R)=min(r11,r22,r33)`.

Thus there is no hidden 6-variable linear program in dimension three: the complete Birkhoff fiber is one explicit closed interval.

## 4. Exact endpoint formula for the cheapest parity payment

Abbreviate

`m_e, m_12, m_13, m_23, m_c, m_cbar`

for the six values `m_rho(K)`. Along the interval above the payment is the affine function

`q(t) = t m_e + (r33-t)m_12 + (r22-t)m_13 + (r11-t)m_23`

`       + (r12-r33+t)m_c + (r13-r22+t)m_cbar`.

Hence

`Q_K(R) = min(q(L(R)), q(U(R))).`

Equivalently its slope is

`Gamma(K) = (m_e+m_c+m_cbar) - (m_12+m_13+m_23)`,

so the minimizing endpoint is `L` when `Gamma>=0` and `U` when `Gamma<=0` (both if zero).

### Theorem 2 — endpoint parity-slack certificate

For an actual MOC4 datum `(D,R,K,X)`, define `L,U,q` as above. If either

`2 q(L) <= W(D,R,K)`

or

`2 q(U) <= W(D,R,K)`,

then the exact MOC4 support inequality holds for that datum for every `X`.

This is exactly Proposition 1 with the Birkhoff minimization eliminated.

## 5. Generic sign-pattern reduction

If all nine entries of `K` are nonzero, let

`s_rho = sign(prod_i K_{i,rho(i)})`.

Then

`prod_{rho in S3} s_rho = prod_{i,j} sign(K_ij)^2 = +1`.

Therefore the number of negative-transversal fibers is always even: it can only be `0,2,4,6`, never `1,3,5`.

This is useful on the simple-spectrum strict-support core. The already-proved zero-negative-fiber case is automatic. The next genuinely generic sign regimes begin with exactly two bad fibers. In that case the endpoint choice has a particularly transparent form:

- if both bad fibers are even permutations, `q(t)` is increasing and the optimum is `t=L`;
- if both are odd permutations, `q(t)` is decreasing and the optimum is `t=U`;
- if one is even and one odd, the endpoint is chosen by the comparison of their two minimum-entry penalties.

Zeros cause no discontinuity because `m_rho(K)` tends to zero whenever a formerly negative transversal crosses through a zero entry.

## 6. Interaction with the repeated-spectrum result

The fleet02/B08 repeated-spectrum lift is used here substantively: it removes the need to prove the endpoint certificate by an artificial genericity assumption and then silently discard the boundary. The function `Q_K(R)=min(q(L),q(U))` is continuous in `(R,K)` (each `m_rho` is continuous, and `L,U` are max/min of continuous affine functions). Thus any strict endpoint certificate obtained on a generic neighborhood persists under sufficiently small perturbation until one reaches an actual equality boundary. B08 independently identifies which repeated-spectrum escape strata still need treatment: zero entries in the nonrepeated rows or supported-vertex collinearity.

This does not close those strata by itself; it cleanly separates them from the simple-spectrum parity-payment problem.

## 7. Why this is progress and what remains

The lead's remaining statement was existential over all Birkhoff decompositions of a 3x3 matrix. This run removes that quantifier completely and fixes the optimization direction:

`MOC4-PARITY-SLACK-v1`

is reduced to checking **two explicit scalar endpoint payments** against the genuine unitary orientation slack. No common `(P,R)` lift, arbitrary bistochastic surrogate, or model-generated certificate is used.

The first unpaid universal step is now sharper:

> On the simple-spectrum irreducible strict-compound unique-support-vertex core, prove that the structured spectral block `K` and genuine unitary blocks `(D,R)` satisfy `W(D,R,K) >= 2 min(q(L),q(U))`, or produce a true-unitary structured witness where this sufficient inequality fails and return to the exact six-fiber inequality.

The fleet04/B09 Bezout/Vandermonde formula should now be applied to the **two endpoint expressions**, not to an unspecified Birkhoff decomposition. For a two-bad-fiber sign pattern, this becomes a single endpoint inequality determined by the parity class and the two minimum selected coefficients.

Full MOC4 remains OPEN.

## 8. Verification

`verify_endpoint_gate.py` checks with exact rational arithmetic that the six affine weights reconstruct arbitrary rational Birkhoff mixtures, that the interval endpoints are feasible, and that the endpoint formula agrees with exhaustive one-dimensional minimization on deterministic rational cases. It also enumerates all nonzero 3x3 sign matrices and confirms that negative transversal counts are exactly `0,2,4,6`.
