# B16 / A080 — exact classification of point-defect tensor candidates

**Run:** `20261012T034627Z-account01-B16-a080-point-defect-potential`  
**Primary packet:** A080 (Universal-counterexample standard)  
**Attempt:** `A080-POINT-DEFECT-TENSOR-AUDIT-1`  
**Claim:** `B16-A080-POINT-DEFECT-TENSOR-CLASSIFICATION-v1`  
**Stable gap:** `G-A080-UNIVERSAL-COUNTEREXAMPLE`  
**Status:** author-proved candidate classification pending independent review.  
**Full FEI:** OPEN.

## Outcome

The A077 sparse tower refuted a tax-free biased helper but its uniform Boolean
realization had `H/I -> 4`. A079 then proved that shared encoders preserving
the same rare gate cannot avoid the physical boundary cost. This run applies
the A080 disproof standard to the complete uniform candidate sequence and
adds the previously missing exact upper-set-potential calculation.

For a Boolean point defect `q_d`, negative at one point of the uniform
`d`-cube, let `delta=2^-d`. Then

```
I(q_d) = 2 d delta,
U(q_d) = (1-2delta)^2 log2(1/(1-2delta)^2)
         + 2 d delta (1-2delta).
```

The proof establishes, for every `d>=1`,

```
H(q_d) < 4 I(q_d),
U(q_d) < 3 I(q_d),
H(q_d)/I(q_d) -> 4,
U(q_d)/I(q_d) -> 1.
```

The new structural point is that `U` is exactly additive under disjoint
tensor products, just like `H` and `I`: the upper-set masses factor. Therefore
**every finite tensor tower of point defects, with arbitrary dimensions and
multiplicities, satisfies `H<4I` and `U<3I`.** This closes the whole
point-defect tensor mechanism as either an FEI counterfamily or an unbounded
`U/I` family.

For the exact A077 sequence, with `2^(2k)` copies in dimension `2k` at each
scale,

```
I(F_K) = 4 sum_{k=3}^K k,
H(F_K) = 16 sum_{k=3}^K k + O(K),
U(F_K) = 4 sum_{k=3}^K k + 4(K-2)log2(e) + O(1).
```

Hence `H/I -> 4` and `U/I -> 1`. The biased B09 helper divergence disappears
when encoder labels and the actual uniform-cube boundary are retained.

## Exact derivation

The squared spectrum of `q_d` is

```
p_empty = (1-2delta)^2,
p_S = 4delta^2 for every nonempty S.
```

For nonempty `S`,

```
pi(S)=4delta^2 2^(d-|S|),
log2(pi(S)/p_S)=d-|S|.
```

Summing `d-|S|` over nonempty subsets gives `d2^(d-1)-d`, yielding the
displayed exact formula for `U`. The inequality `-ln(1-x)<=x/(1-x)` gives

```
U/I <= (1-2delta)(1+2/(d ln 2)) < 3
```

for `d>=2`; `q_1` is a signed dictator with `H=U=0`. The same logarithmic
bound and the exact point-defect entropy formula give `H<4I`, with the
`d=1` endpoint handled separately.

For disjoint spectra `p_{f g}(S,T)=p_f(S)p_g(T)`, and
`pi_{fg}(S,T)=pi_f(S)pi_g(T)`. The logarithm splits, proving exact `U`
additivity without a numerical approximation or an assumed surrogate law.

## Movement

**Prior status.** A077 and A079 showed that one rare biased-gate mechanism is
physically compensated, but they did not calculate `U`, classify arbitrary
scale multiplicities, or apply the formal A080 standard to the complete
candidate closure.

**New status.** The entire disjoint point-defect tensor closure is now
analytically excluded as an FEI or `U/I` counterfamily. This includes the
shared-variable A079 example because its negative set is still a singleton.
The result is all-dimensional and independent of the number of scales,
their dimensions, and their multiplicities.

**Remaining gap.** A credible next counterfamily must leave point-defect
tensor closure: for example an overlapping nonlinear surgery or a different
gate with a non-singleton output cell. Its signed coefficients, `H`, all
physical influence, and `U` must be derived anew. No such family is supplied
here.

## Mandatory controls

- **Genuine Booleanity:** every component is an explicit uniform-cube truth
  function; no abstract probability law is substituted.
- **Rare events:** the empty Fourier atom and its logarithm are retained in
  the exact `U` formula.
- **Cross-scale interference:** the classified theorem assumes disjoint
  tensor copies and proves additivity. It does not claim an overlap formula.
- **Shared encoders:** A079's correlated realization has a singleton negative
  cell, hence lies inside the point-defect classification.
- **Addressing/selectors:** not represented by the theorem unless their final
  function is actually a point-defect tensor.
- **Near tensors:** exact tensors are closed; overlapping perturbations remain
  open.
- **Counterexample standard:** divergence of the biased helper is not called
  FEI divergence. The actual ratios are bounded and explicitly computed.

## Verification

Command:

`python3 verify_point_defect_potential.py`

The checker used exact `Fraction` arithmetic for all Walsh coefficients,
upper-set masses, and influences. It verified dimensions `1..10`, every
upper-set identity, and all ordered tensor pairs with component dimensions
`1..4`. Ninety-digit Decimal logarithms checked only the closed analytic
formulas.

```
exact rational assertions: 4128
90-digit decimal assertions: 62
seed: None
status: PASS
```

The finite audit is not the all-dimensional proof; that proof is in
`CANDIDATE_SEQUENCE_AUDIT.tex`.

## Source pins

- Full-FEI priority overlay: Brain commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`, CASE_TARGETS blob
  `97e41262ebb4f09eec53630a918acae09efc9a48`.
- B16 compact contract blob:
  `319bbb049c631c103a842cf9a530c7be91a319d0`.
- A077 report blob: `d016b494606fd3a7132068fdea3925d55d0a1262`;
  proof blob: `69f15d64c066e6ada7898795e3d2be62c07fb91b`;
  source package commit `3428cf1d55810b1792ce2e38898f99229f6e428f`.
- A079 report blob: `4830187ce209f36c917fab9f0536c6a71bda6d09`;
  canonical commit `8e46b8d689ce8aa54c16242b4da13dd7be87d1f1`.

No literature novelty, independent review, native ingestion, or full-FEI
conclusion is claimed. Runtime identifies the assistant as Codex based on
GPT-5; separate reasoning-effort telemetry was not exposed.

## Handoff

Route the candidate-sequence audit to A092/A088. A075 and B20 can use the
exact `U` tensor law and the `H<4I`, `U<3I` classification to retire
point-defect tensor towers from counterexample search. The next B16 attempt
should freeze a nonlinear overlapping gate before search and calculate all
three ledgers from its truth table.
