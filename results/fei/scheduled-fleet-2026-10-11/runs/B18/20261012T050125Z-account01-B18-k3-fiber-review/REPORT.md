# B18 / A088 independent reconstruction — B07 three-address Boolean fibers

Run ID: `20261012T050125Z-account01-B18-k3-fiber-review`  
Primary packet: `A088` (Booleanity referee)  
Reviewed claim: `B07-A034-K3-FIBER-v1`  
Review verdict: **HOLDS AT THE DECLARED RESTRICTED SCOPE, WITH TWO RECORD REPAIRS**  
Full FEI: **OPEN**

## 1. Frozen source and exact scope

I reviewed the B07 author package at canonical final commit
`f73eca4c1bc554d485ae8d2439060bdf781d7dea`, path

`reports/fei-2026-10-11/runs/B07/20261012T041024Z-account01-B07-a034-k3-fibers/`.

The mathematical claim has two layers:

1. every genuine Boolean fiber on a three-bit address cube is a character,
   a one-point defect, or a semibent affine-two-flat fiber, with the exact
   address-energy values stated by B07;
2. under the additional A2 product-row hypothesis, odd normalized
   granularity forces a common odd-trace point-defect cylinder and hence a
   simultaneous lower reserve in all eight rows.

No K3 FEI theorem, no arbitrary-row theorem, and no uniform-in-`k` recurrence
is part of the reviewed statement.

## 2. Independent proof of the fiber trichotomy

Fix the data input and write the address-fiber Walsh coefficients as
`g_T`. Put

\[
 a_T=4g_T=\frac12\sum_{y\in\mathbb F_2^3}f(y)(-1)^{T\cdot y}.
\]

Then every `a_T` is an integer, all eight have the same parity, and Parseval
gives

\[
 \sum_T a_T^2=16.
\]

If the common parity is odd, eight positive odd squares totaling 16 must be
`(9,1^7)`. If it is even, dividing the squares by four leaves a representation
of four as eight squares, hence either `(4,0^7)` or `(1,1,1,1,0^4)`.
Rescaling gives exactly the three magnitude patterns

\[
 (1,0^7),\qquad(3/4,1/4^7),\qquad(1/2^4,0^4).
\]

The middle pattern has correlation `3/4` with a signed character, hence
Hamming distance `(1-3/4)/2=1/8`: exactly one flipped value.

For the four-point support `K` in the last pattern, Booleanity gives, for
every nonzero `U`,

\[
 \sum_T g_Tg_{T\triangle U}=0.\tag{1}
\]

If `|K intersect (K+U)|=2`, (1) consists of two equal nonzero ordered
products and cannot vanish. Therefore every difference of two points of `K`
stabilizes `K`; translating one point to zero shows that `K` is a
two-dimensional subspace, so the original support is an affine two-flat.
Equation (1) on that flat is precisely the two-bit bent sign condition.

This reconstructs the classification without using the author's checker.
Counting gives 16 characters, `16*8=128` point defects, and
`14*8=112` semibent fibers.

## 3. Exact address-energy transfer

For `J_A=sum_T |T|g_T^2`:

- a character supported at `D` has `J_A=|D|`;
- a point defect with major coefficient `D` has
  `J_A=3/4+|D|/2`;
- a semibent flat `F` has `J_A=(1/4)sum_{T in F}|T|`, whose possible values
  are exactly `1,3/2,2`.

Thus every non-character fiber costs at least `3/4`, and pointwise integration
proves

\[
 \Pr[\text{non-character fiber}]\le\frac43 I_A(f).\tag{2}
\]

The constant `4/3` is sharp for this pointwise statement: a point defect with
major address `D=emptyset` has `J_A=3/4`.

## 4. Independent numerator-parity reconstruction of the odd reserve

For every row `U`, `4g_U(x)` is odd exactly on the same point-defect set `P`.
On `P`, its square is `9/16` when the major address equals `U` and `1/16`
otherwise. Consequently

\[
 \mathbb E[1_Pg_U^2]
 =\frac{\mu(P)}{16}+\frac12\mu\{x\in P:D(x)=U\},\tag{3}
\]

and summing `|U|` times (3) gives

\[
 I_A(P)=\frac34\mu(P)+\frac12\mathbb E[1_P|D(x)|]
 \ge\frac34\mu(P).\tag{4}
\]

It remains to justify the parity transfer rather than inherit it. Strip the
Fourier-frozen data coordinates of a nonzero product row and let `r` active
coordinates remain. Write `c(x)=4g_T(x)` and

\[
 N_V=\sum_xc(x)(-1)^{V\cdot x}
 =2^{r+2}\widehat g_T(V).
\]

Modulo two, every sign is one, so all `N_V` have common parity

\[
 N_V\equiv |P_{\rm trace}|\pmod2.\tag{5}
\]

Product Fourier magnitudes factor the integer numerators as

\[
 |N_V|=\nu'\prod_i s_i(V_i),
\]

where each pair `s_i(0),s_i(1)` is the coprime numerator/denominator pair of
the active magnitude ratio. Integrality gives the A2 normalization
`nu'=nu/prod q_i`. If `nu'` is odd, common parity (5), applied also at the
corner using every coprime numerator, forces all ratio numerators and
denominators odd, hence every `N_V` odd. Conversely, if every `N_V` is odd,
their common integer factor `nu'` is odd. Therefore

\[
 \nu'_T\text{ odd}\iff |P_{\rm trace}|\text{ odd}.\tag{6}
\]

Fourier-frozen coordinates make `|g_T|`, hence the parity of `4g_T`, constant
along their fibers, so `P` is a cylinder over the active set. From (6),
`mu(P)>=2^{-r}`. Equations (3)--(4) then give

\[
 w_U\ge2^{-r-4}\quad\text{for every }U,
 \qquad I_A(f)\ge\frac34,2^{-r}.\tag{7}
\]

This proves the odd-granularity part at exactly its product-row scope. It does
not apply to arbitrary signed rows.

## 5. General-`k` warning

For a one-point defect from a signed `k`-bit character with major address
`D`, direct Walsh calculation gives

\[
 J_A=k2^{1-k}+(1-2^{2-k})|D|.\tag{8}
\]

At `D=emptyset`, the available local charge is `k/2^{k-1}`. Therefore any
scheme charging a fixed positive cost for each defect solely to this local
quantity loses at least order `2^k/k`. This is a valid obstruction to that
payment mechanism, not a counterexample to FEI and not proof that no
multi-row credit can work.

## 6. Independent exact computation

`INDEPENDENT_AUDIT.py` was written without importing B07's checker. It checks:

- all 256 three-bit Boolean truth tables;
- integer Parseval, common parity, all seven nontrivial Boolean convolution
  identities, affine support, type and exact address energy;
- every major character in the general-`k` point-defect formula for
  `k=2,...,9`;
- a separate exhaustive numerator-parity/product-magnitude audit for all
  integer rows `c(x) in {-4,...,4}` on one and two active data bits.

Command: `python3 INDEPENDENT_AUDIT.py`.

Result: **PASS**. No random seed or floating-point arithmetic is used.

## 7. Review verdict and repairs

### HOLDS

`B07-A034-K3-FIBER-v1` is independently accepted at its exact restricted
scope. The trichotomy, the `4/3` transfer, and the odd product-row reserve are
correct. `B07-A034-POINTDEFECT-k-v1` is also correct.

### Record repairs required

1. `K3_FIBER_STRUCTURE.tex` equation (4) prints
   `I_A >= (3/4),2^{-r_T}`. The comma must be multiplication:
   `I_A >= (3/4)2^{-r_T}`. The report and JSON statement already use the
   correct formula, so this is a TeX typo rather than a proof defect.
2. The two distinct entries in B07 `CLAIMS.json` carry the same
   `statement_sha256`. At least one registry hash is stale. The mathematical
   statements remain readable, but the hashes must be regenerated before
   hash-based adoption.

Because this review reconstructs rather than repairs the mathematics, it is
independent acceptance of the theorem after those record-only corrections.

## 8. First unsupported line and next material hypothesis removal

The first unsupported line is exactly the **even** normalized layer
`nu'_T=2`. Equation (5) then supplies only zero modulo two. Semibent fibers
and paired point defects both contribute modulo four, with signs that can
cancel across data points; no common cylinder event analogous to `P` has
been proved.

The next useful theorem must classify

\[
 2^{r+2}\widehat g_T(V)\pmod4
\]

jointly across all eight address rows and pay the resulting event by (4) or a
new conditional/multi-row reserve. Proving only another fixed three-bit
census would not remove the live hypothesis. Even a complete K3 theorem
would still leave the dependence on `k`; equation (8) explains why a
pointwise defect charge alone cannot yield a uniform recurrence.

Full FEI therefore remains **OPEN**.

## 9. Sources and routing

- Reviewed author commit:
  `f73eca4c1bc554d485ae8d2439060bdf781d7dea`.
- Reviewed proof blob: `K3_FIBER_STRUCTURE.tex` from that commit.
- Author report path:
  `reports/fei-2026-10-11/runs/B07/20261012T041024Z-account01-B07-a034-k3-fibers/REPORT.md`.
- Author dependencies named in the source: `A2-L3k`, `A2-H-ladder`, and
  `A2-E-k3`; the parity/divisibility step needed here was reconstructed above
  rather than accepted from the dependency label.

Route the accepted theorem to A003, A032, A033, A079, A096/B20. Route the
record repairs to B07. A fresh reviewer is still needed for any future mod-4
extension; this review does not accept such an extension in advance.

