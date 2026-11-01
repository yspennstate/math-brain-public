# A027 block controls

## Frozen rule

For a Boolean modulation node

`F(x,z)=g(x_1 h_1(z),...,x_n h_n(z))`,

query the fresh block `Z` as one proper physical block, keep every reach
probability, and retain the child entropy as terminal debt.  The exact ledger
is

`decrement = B_Z + M_Z = sum_S ghat(S)^2 H(h_S)`,

`M_Z=0`, and

`queried influence = I_Z(F) = sum_S ghat(S)^2 I(h_S)`.

The rule is valid only when at least one older variable remains, so it never
uses the vacuous choice `W=[n]`.

## Controls

| Control | Exact behavior | Consequence |
|---|---|---|
| Character-coded plateau | Every `h_S` is a character; `B_Z=M_Z=0` and every partial restriction preserves entropy | The block skips arbitrarily many zero-gain coordinate steps, but terminal entropy is not erased |
| Point-defect modulation | All `h_i=q_m`; `Delta H/Delta I=H(q_m)/I(q_m)<=9/2` whenever the odd spectral mass is positive | Gives a nonlinear, arbitrary-depth Boolean hierarchy with every added influence included |
| Addressing or near-tensor base | Core squared spectrum is preserved at every block outcome | Closure uses only the already proved base constant; no new universal claim |
| Rare restriction | A point defect has a rare exceptional input, yet its full Fourier entropy and influence are charged by the exact auxiliary ratio | Rare logarithmic cost is not dropped |
| Bent splice | Branch squared spectra differ; the uniform branch-square hypothesis fails | The known `Delta H/I >= m-1` obstruction remains live |
| Shared signed dictator | Allowing arbitrary auxiliary products would ask for FEI on those products | Universalizing the hypothesis would be circular |
| Fixed-root tree telescope | Terminal `H(f_0)` is explicit and each fresh block influence is used once | No coefficient involving the unknown extremal ratio is assumed |

## Scope

Status is PROVED pending independent review for the stated modulation
hierarchy.  It is not a proof of full FEI, not an existential block theorem
for every Boolean function, and not a repair of bent-splice low-energy
selection.
