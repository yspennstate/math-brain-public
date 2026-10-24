# B05 / A023 — sparse odd-surgery selector-payment no-go

**Primary packet:** A023, amortized rarity budget  
**Gap:** `B05_RARE_REFUNDS`  
**Attempt:** `B05-A023-SPARSE-SURGERY-L2-NOGO-02`  
**Status:** author-proved exact/asymptotic no-go, pending A087/A094 review  
**Full FEI:** **OPEN**.

## Result

The independently reviewed odd-surgery theorem has a constant

`1 + 99m/(2 ln 2) + 4 log2(m)`

for `m` edits. Its stated next step was to replace the pointwise Taylor bound
by an averaged payment proportional to `sum_T e_T^2=4m delta`, aiming for a
constant independent of `m`.

That proposed improvement is false. There is an explicit family of genuine
Boolean odd point surgeries of quadratic bent cores, lying in the strict
sparse regime `m*2^(-k/2) -> 0`, for which a fresh one-bit selector satisfies

`[U(F)-(U(g)+U(h))/2] / I_ctl -> infinity`.

Thus no absolute selector-only constant can cover arbitrary odd surgery
counts. The existing `O(m)` upper bound remains valid, but some edit-count,
data-core, or terminal-packet currency is genuinely necessary.

## Construction

Let `k=2r` and

`g(x,y)=(-1)^(x dot y)`, `x,y in F_2^r`.

Set `s=ceil(r/3)`. Fix the first `s` input pairs to state `(1,1)` and allow
each remaining pair to be `(1,0)` or `(1,1)`. Remove the all-`(1,1)` point
and flip `g` on the remaining set. The edit count is

`m=2^(r-s)-1`,

which is odd, while

`m*2^(-k/2) < 2^(-s) -> 0`.

This is a physical truth-table surgery followed by one actual selector bit;
there are no free probability laws or non-Boolean spectra.

## Amplification mechanism

For the relative Fourier perturbation `rho_T=e_T/a_T`, define upper-cap
averaging

`(P rho)(T)=2^(|T|-2r) sum_(Q superset T) rho_Q`.

In the bent-modulated character basis, one fixed `(1,1)` input pair has
amplification `13/16`, while the signed free pair supported on
`{(1,0),(1,1)}` has amplification `5/4`. Before removal of one point, the
exact tensor factor is

`A_r=(13/16)^s (5/4)^(r-s)`.

After removal, reverse triangle gives an explicit lower bound `L_r` with
`L_r/A_r -> 1`. Since

`(13/16)*(5/4)^2 = 325/256 > 1`,

both `A_r` and `L_r` diverge exponentially in `r`. Equivalently, the lower
growth is polynomial in the edit count with exponent

`gamma=(1/2)log2(325/256)=0.172...`.

## Complete charge, not only the scalar surrogate

The relative perturbation obeys `||rho||_infinity <= 2m*2^-r -> 0`, so the
accepted exact scalar identity may be Taylor-expanded uniformly. With
`p=1/2`,

`E Phi = (1/4)[||rho||_2^2 + 2||P rho-rho||_2^2]
         + o(||rho||_2^2+||P rho-rho||_2^2)`.

Moreover `I_ctl=m*2^(-2r)` and `(1/4)||rho||_2^2=I_ctl`. The remaining
difference-spectrum packet satisfies the unconditional lower bound

`K >= -2r sum_T e_T^2`,

so its contribution is at worst `-2r I_ctl`. The cap amplification dominates
this linear loss, proving the displayed divergence of the complete retained
charge.

The full analytic derivation is in `SPARSE_SURGERY_NOGO.tex`.

## Verification

`CHECK.py` uses exact rational arithmetic for the local Gram matrix and
certifies

- fixed-pair amplification `13/16`;
- free signed-pair amplification `5/4`;
- three-block growth `325/256>1`;
- 175 analytic parameter rows through `r=180`;
- odd edit count and the exact sparse inequality on every row.

It also independently reconstructs six full Boolean truth tables and Walsh
spectra through `k=18`, verifying the predicted lower amplification and the
relative-coefficient bound. All checks passed. At `r=180`, the explicit
amplification lower bound already exceeds `1.65e6`; these numbers illustrate
the analytic tensor proof and are not its basis.

## Scope and next step

This theorem refutes only payments charging the retained coherent-surgery
increment to fresh selector influence, or equivalently to an absolute
multiple of `p sum e_T^2`. It does not refute FEI, GU', or a ledger that also
charges physical data coordinates or retained terminal `U`.

The next viable mechanism is therefore different: assign the amplification
to a single-use data-edit/terminal packet, and test whether that packet
telescopes through changing-core restriction histories without being spent at
each ancestor. Mandatory next controls are addressing, shared address bits,
near tensors, and even-surgery zero atoms.

## Sources

- Owner control revision `2026-10-12.1`, commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- B05 contract blob `05447e6d999437bb82a266b427bd76a4b37266b6`.
- Accepted odd-surgery source: canonical commit
  `01c4f518577e183e29d4a6f9fc019d8ed1b8901d`, proof blob
  `5c0206358b13e617f530eff04d9ec179b435a681`.
- Independent A094 review: report blob
  `d1ee8d6fa4d1a0ff2151d38dd62251b5a6f78f1c` at canonical source head
  `83cdeea45b17a296c70da0007e130a89af6402a9`.
- Exact upper-set restriction identity: U-universal source blob
  `5797e9cc38598cbee391cc99d4b1abcd554b662e`.

No external novelty claim is made. No subagent, protected source, scheduler
mutation, paid compute, public release, email, or native Brain ingestion was
used. Independent review of this new no-go is pending A087/A094.
