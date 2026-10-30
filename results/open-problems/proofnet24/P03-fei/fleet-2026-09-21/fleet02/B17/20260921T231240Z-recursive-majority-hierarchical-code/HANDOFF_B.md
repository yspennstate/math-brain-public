# B17 -> Campaign B handoff: global CFC refuted, nested branch-surplus code survives

Source run: fleet02/B17 `20260921T231240Z-b17-fei`.

Consumed other-account source:
`fleet03/B12/20260921T224810Z-local-factorial-hierarchy/REPORT.md`
(blob `96737b71a9bb921b9dbae1051844314a5e96bfbc`).

## Decisive adversary

For depth-d recursive ternary majority `M_d`, an actual balanced Boolean function,

- `I_d=(3/2)^d`;
- `H(M_d)=4(I_d-1)`, so `H/I<4`;
- the B12 one-level ordered envelope
  `U=H(K)+I H(q)-E log2(K!)` obeys
  `U/I >= d log2 3 - log2(2(3/2)^d-1) > d-1`.

Therefore no finite universal beta can satisfy `U<=beta I`.
This kills only the stronger one-level code bridge, not FEI.

## Replacement proved

For any rooted coordinate-partition tree, with node-activity probabilities `tau_v`,
conditional active-child subset size `D_v`, mean `mu_v`, and normalized child profile `q_v`,
define

`U_v=H(D_v|A_v=1)+mu_v H(q_v)-E[log2(D_v!)|A_v=1]`.

Then for every random subset law

`H(S) <= h2(tau_root)+sum_v tau_v U_v`

and exactly

`sum_v tau_v(mu_v-1)=I-tau_root`.

For recursive majority on its natural ternary tree the nested code has constant
`2[h2(1/4)+(3/2)log2 3-(1/4)log2 6]`
=`5.084962500721156...` against `I-1`, uniformly in depth.

The code is also stable under balanced disjoint composition and incurs only
`r log2 r-log2(r!) <= 2 log2(e)(r-1)` root overhead for an r-fold balanced tensor product.

## New missing implication

Find, for every balanced Boolean spectral law, an adaptive source-admissible coordinate tree with

`sum_v tau_v U_v <= C (I-1)`.

The exact local obstruction is singleton routing: arbitrary subset laws can have `D_v=1`
with high child-identity entropy and zero local branch surplus, but a global exactly-degree-one
Boolean spectrum is only dictator/constant. The missing theorem must use Boolean realizability
to amortize near-singleton routing across ancestors (near-dictator/character certificate,
excess-degree payment, or negative conditional-information credit).

Do not retry the refuted one-level CFC bridge.
