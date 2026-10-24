# B01 / A003 — exact KL-by-JS falsifier and tensor family

**Run:** `20261012T090930Z-account01-B01-kl-js-falsifier-a003`  
**Primary packet:** A003, minimal target formulation  
**Stable gap:** `G-UPPER-SET-ASYMMETRY`  
**Attempt:** `A003-GUP-KL-BY-JS-FALSIFIER-4`  
**Status:** exact auxiliary-inequality refutation and all-depth tensor counterfamily author-proved; pending A086/A094 independent review.  
**Full FEI:** **OPEN**.

## 1. Frozen target and change of mechanism

The source-pinned identity

`Delta_i U = B_i - Gamma_i + KL_i`

isolates a nonnegative upper-set posterior mismatch `KL_i`. The ordinary
entropy restriction identity has a Jensen–Shannon term `JS_i` with a known
dimension-free influence payment. Before enumeration, this run froze the
concrete proposed bridge

`sum_i KL_i <= sum_i JS_i`.                                           (P)

If true, (P) would pay the full upper-set KL term using an already controlled
physical restriction currency. This attempt pivots away from the preceding
fixed-core activation/overlap extensions: it attacks the remaining
asymmetry term directly on all genuine Boolean spectra through dimension four.

## 2. Exact result

**REFUTED:** (P) is false.

There is a genuine four-bit Boolean function whose two selector slices are a
three-bit parity and that parity with exactly its `000` and `111` values
flipped. Its nonzero Fourier coefficients are

`(-1/4,-1/4,-1/4,3/4; 1/4,1/4,1/4,1/4)`

on sets `1,2,3,123; 1z,2z,3z,123z`. All physical-input accounting is native:
there are four Boolean cube coordinates, the selector is the fourth actual
coordinate, Parseval holds, and `I(f)=5/2`.

For the first three coordinates both candidate currencies vanish. For the
selector coordinate, exact evaluation gives

`KL_z = (3/8) log2(3)`,

`JS_z = 2 - (5/8) log2(5)`.

Hence

`sum_i(KL_i-JS_i) = (1/8) log2(3^3 5^5 / 2^16) > 0`,

because `84375 > 65536`. The defect is
`0.045565997075035...` bits, or `0.018226398830014... I(f)`.
The sign is an exact integer comparison; decimals are scale information only.

The complete derivation is in `KL_JS_FALSIFIER.tex`.

## 3. Parametric extension

Both aggregate quantities are additive under disjoint Boolean tensor product.
Indeed the squared spectrum and upper caps factor; for a coordinate in one
factor, its fibre mass acquires the other factor's spectral probability while
the two posterior parameters `eta` and `x` are unchanged. Summation over the
other factor has total mass one.

Therefore the tensor powers `f^(tensor r)`, `r>=1`, give genuine Boolean
functions on `4r` inputs with

- defect `r delta`, where `delta=(1/8)log2(3^3 5^5/2^16)>0`;
- influence `5r/2`;
- normalized defect exactly `0.018226398830014...`, independent of dimension
  and tensor depth.

The newly covered object is thus an unbounded-dimension counterfamily to the
specific payment (P), not a finite numerical accident. It is not a
counterfamily to FEI.

## 4. Exact surviving term

At one fibre the excess of upper-set KL over restriction JS is exactly

`-1/2 log2(1-x^2) - (eta/2) log2((1+x)/(1-x))`.

The witness has three anti-aligned fibres with `eta=-1` but cap posterior
`x=1/3`; their positive excess is not canceled by the aligned fibre
`eta=x=3/5`. This identifies the first unsupported line in the direct
`KL -> JS -> influence` route: cap-posterior alignment is essential and is
not encoded by the local restriction JS alone.

A valid repair may still use a coefficient larger than one, an added `bU`
term with `b<1`, or a nonlocal signed hierarchy credit. This run neither
refutes nor proves any of those possibilities.

## 5. Verification

`SEARCH.py` exhaustively scans one representative of each output-complement
pair through four variables. Floating discovery found maximum normalized
defect zero through dimension three and `0.018226398830014...` at dimension
four, mask `6038`. This is discovery evidence, not the proof of minimality.

`CHECK.py` independently reconstructs the truth table, performs exact
`Fraction` Walsh and upper-cap arithmetic, verifies the four fibre records,
checks `I=5/2`, proves the sign from `84375>65536`, and directly checks the
tensor square at 100 decimal digits. `python CHECK.py` and
`python SEARCH.py` both passed; outputs are archived. The all-`r` tensor
extension and sign are analytic.

## 6. Scope and next unpaid step

Previous status: fixed-core rare-activation, nested-ledger, and complete
phase-overlap classes had dimension-free payments, but no universal control
of the aggregate upper-set asymmetry mismatch.

New status: the most direct attempt to pay the `KL_i` term by the already
influence-paid `JS_i` term is rigorously eliminated, including all tensor
depths. This is a substantive obstruction, not a reformulation.

Next action: retain the signed alignment expression above and test the precise
GU' candidate

`sum_{i,T} m_{i,T}[KL(eta||x)-JS(eta||0)] <= a I + b U`, `b<1`,

first on the tensor counterfamily, rare surgery, addressing, and prime gates.
The analytic task is to find a single-use upper-set credit that controls the
anti-alignment without paying the same cap at every ancestor. No
dimension-independent such estimate is proved. Full FEI remains **OPEN**.

## 7. Sources and execution record

- Owner control revision `2026-10-12.1`, commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`; order blob
  `81b6d6f988aee4489512c6e62543253900620453`; case-target blob
  `97e41262ebb4f09eec53630a918acae09efc9a48`.
- A003 assignment blob `ac038a028831d59ad053dd56b2b527e2a71ffdee`.
- U-universal source blob `5797e9cc38598cbee391cc99d4b1abcd554b662e`
  for Theorem G, GU', and the exact `B_i-Gamma_i+KL_i` identity.
- Current-status blob
  `c416d4b4a83fc67965cb95d06a0cc80c5c29a520`.
- Canonical source head at research start:
  `3dd5f38ff0768c47b18a5be8b409723a8bb1a9ac`.
- Brain source head observed at research start:
  `8bbad4bf3d4c747b0a0904746682d25391a65b36`.
- Repository search found the restriction-JS literature inside the campaign
  but no previous occurrence of the proposed `upper-set KL <= restriction JS`
  comparison; no external novelty claim is made.
- No subagent, scheduler mutation, protected source, paid compute, public
  release, email, or native Brain ingestion was used.
- Exposed model: Codex; reasoning-effort metadata was not exposed.
- Independent review of the new exact claims is pending A086/A094.
