# B07 / A034 — exact K3 fiber structure and joint odd-granularity reserve

Run ID: `20261012T041024Z-fleet01-B07-a034-k3-fibers`

Mathematical status: **PROVED pending independent review** at the stated structural scope.  The sharp K3 FEI bound and full FEI remain **OPEN**.

## 1. Frozen target and prior status

Primary packet: A034 (phase-energy transfer).  Stable campaign gap: `G-PHASE-COND`; exact new sub-obstruction: `G-K3-MOD4`.

The owner-directed target is to extend the conditional-product hierarchy from K2 to K3 and expose the dependence on the number `k` of spectral address bits.  The source A2 route had already proved the product-row granularity identity for every `k`, proved the sharp K2 constant, and supplied finite evidence for K3 at `n=5`.  It explicitly left open the all-arity three-bit fiber classification and its joint weight reserve.

Prior quantitative status:

- `C_2 = 16/3-(3/2)log_2 3 = 2.955889582...` (A2-T-S, pending the campaign's independent-review rules).
- K3 finite census at `n=5`: maximum `H/I = H(AND_4)/I(AND_4) = 12-(49/16)log_2 7 = 3.402475551...`; evidence only.
- General product-row identity: `L_T+H(q_T)=2(k-1)-2log_2 nu'_T+sum_i Ft(p_i,q_i)`; the missing ingredient for `k=3` was the analogue of the K2 pointwise fiber/weight lemma.

Bounded objective for this run: classify every genuine three-address Boolean fiber, compute its exact address-influence charge, and determine what odd row granularity forces simultaneously across all eight rows.

## 2. New theorem

Let `f:{-1,1}^A x {-1,1}^C -> {-1,1}` with `|A|=3`, and let

`g_T(x)=E_y[f(y,x) chi_T(y)]`, `w_T=E_x g_T(x)^2`.

The complete proof is in `K3_FIBER_STRUCTURE.tex`.  Its conclusions are:

1. **Exact fiber trichotomy.** Every fixed-data fiber has one of exactly three Walsh magnitude patterns:
   - character: `(1,0^7)`;
   - point defect: `(3/4,1/4^7)`;
   - semibent: `(1/2^4,0^4)`, supported on an affine two-flat with a two-bit bent phase.

   Across all 256 truth tables the counts are 16, 128 and 112.

2. **Exact phase-to-address-energy transfer.** With `J_A(x)=sum_T |T|g_T(x)^2`:
   - character with support `D`: `J_A=|D|`;
   - point defect with major address `D`: `J_A=3/4+|D|/2`;
   - semibent support flat `F`: `J_A=(1/4)sum_{T in F}|T|`, which is exactly `1`, `3/2`, or `2`.

   Therefore, for the set `N` of non-character fibers,

   `mu(N) <= (4/3) I_A(f)`.

3. **Joint odd-granularity reserve.** Suppose a nonzero row has product conditional spectrum and use the A2-L3k normalization `nu'_T`.  Let `P` be the point-defect set and `D(x)` its major address.  Then, for every row `U`,

   `E[1_P g_U^2] = mu(P)/16 + (1/2)mu{x in P:D(x)=U}`.

   Hence the point-defect portion of address influence is

   `(3/4)mu(P)+(1/2)E[1_P |D(x)|] >= (3/4)mu(P)`.

   Moreover, `nu'_T` is odd iff `P` is a cylinder over the active set `R_T` with odd trace.  If this holds, then

   `mu(P)>=2^{-|R_T|}`, `w_U>=2^{-|R_T|-4}` for all eight rows, and `I_A>=3*2^{-|R_T|}/4`.

This is the requested first joint 2-adic compatibility constraint.  It is an all-data-arity theorem, not a finite census.

## 3. Derivation boundary

Put `a_T=4g_T=(1/2)sum_y f(y,x)chi_T(y)`.  The eight `a_T` are integers of a common parity and satisfy `sum_T a_T^2=16`.  These two facts force the three square patterns above.  Signed Boolean convolution then forces every four-point support to be an affine two-flat and its signs to be bent.

For a product row, every active Walsh numerator has parity equal to the number of data points where `4g_T` is odd.  The fiber trichotomy makes this odd-value set exactly the same point-defect set `P` for every row.  The A2 divisibility normalization converts common odd numerator parity into `nu'_T` odd.  This proves the cylinder and weight claims without discarding phases.

The first unsupported line is now sharply located: **even rows with `nu'=2`**.  Semibent fibers and pairs of point-defect fibers can both contribute even numerators, and their signed contributions need not define a common event modulo four.  A K3 FEI theorem still needs that joint mod-4 classification and a row envelope.  No bound `H<=C I` for all K3 functions is claimed here.

## 4. General-k obstruction exposed

For a one-point defect from a signed character on `k>=2` address bits, with major address `D`, exact calculation gives

`J_A = k 2^{1-k} + (1-2^{2-k})|D|`.

At `D=empty`, the local reserve is only `k/2^{k-1}`.  Therefore a recurrence paying a fixed per-defect entropy charge only from this local address reserve necessarily loses order `2^k/k`.  This explains explicitly why the present K3 mechanism cannot be iterated to a uniform-in-`k` FEI constant.  It is a failure of that payment mechanism, not a Boolean counterfamily with unbounded `H/I`.

## 5. Exact validation

Frozen pilot:

- Domain: all `2^8=256` Boolean truth tables on three bits; additionally every major character for one-point defects for `k=1,...,8`.
- Arithmetic: integers and Python `Fraction`; no floating point, randomness, or symmetry reduction.
- Command: `python3 VERIFY.py`.
- Observed runtime: 22.46 seconds on the natural run.
- Assertions: integer Parseval, common parity, exhaustive type classification, affine support closure, bent sign product, exact address energy, and the general-k defect formula.

Output: `K3_FIBER_CENSUS_PASS`; 256 truth tables and 510 general-k point-defect cases passed.  Full output is in `CHECK.out`.

The computation certifies the finite three-bit classification only.  The cylinder and product-row implications are analytic and valid for arbitrary data dimension.

## 6. Required stress controls

- **Addressing/multiplexers:** character fibers have `N=empty`; the theorem assigns no spurious non-character charge.  This is compatible with the established addressing endpoint.
- **Rare defects:** the point-defect reserve is exact, including the rare-event probability.  The general-k calculation records its exponentially decreasing local charge rather than hiding it.
- **Near tensors:** no arbitrary data-tensor entropy is claimed paid.  The earlier A034 Rényi-half tensor-additivity guard remains intact.
- **Actual prime Boolean gate:** AND4 lies in K3 (take three address bits and one data bit) and has exact ratio `12-(49/16)log_2 7`.  The theorem covers its fibers but does not prove it extremal in K3.
- **Signs/realizability:** every step starts from a genuine Boolean truth table; semibent affine support is derived from signed convolution, not from a normalized probability vector.

## 7. Sources actually read

- Owner control revision `2026-10-12.1`, source commit `40210272c19f43fed84f6a67653f9a04b0e11e28` (`ORDER.md`, `CASE_TARGETS.json`; B07 row).
- `math-open-problems` B07 contract, blob `2402180c94777484a0f41d5f13a9e01059107569`; protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- A034 soft Rényi baseline: canonical artifact commit `89735cd5f31664f0a6d965bc7330b4be1d204e40` and delivery receipt `c7f4db2eb2566b5c3ba9228a9b1ac6357603c566`.
- Archived original A2 route: `A2-two-addresses/NOTES.md` blob `7df82ce208f2bd61bc9b5310022d8705f0079beb`, `CLAIMS.json` blob `e6c926538094cd1da3d48b8b0a56ae47e69861e9`, and independent `REFEREE.md` blob `576d755fb6ba875c4545d5efaf894e622ca518ef`.  Used claims: A2-L3k, A2-H-ladder, and A2-E-k3 at their exact scopes.

No novelty claim beyond the campaign sources is made.

## 8. Status, routing, and next action

Claim `B07-A034-K3-FIBER-v1` is author-proved and awaits independent A088/A094 review.  It advances the K3 all-arity bridge but does not complete A034 or solve K3/full FEI.

Next action: classify the joint residues `2^{r+2}\widehat g_T(V) mod 4` for the even `nu'=2` rows, separating semibent affine-flat incidences from paired point defects.  The desired output is either a common mod-4 reserve paid by the exact pointwise `J_A`, or a genuine Boolean falsifier showing that such a reserve cannot be row-local.

Named consumers: A003, A032, A033, A079, A088, A096/B20.  Independent reviewers: A088 and A094.
