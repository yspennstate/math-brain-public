# FEI handoff — account01/B14 balanced-uniform gate margin refutation

Outcome: `CANDIDATE_REFUTED`; full FEI remains OPEN.

Source-bound scientific artifact:
- repository: authorized private FEI research archive
- commit: `a0b599c1fa6d27a5511f915a7ecb9e2fd8272040`
- path: `proofnet24/P03-fei/fleet-2026-09-21/account01/B14/20260922T0044Z-balanced-gate-margin-refutation/REPORT.md`
- report blob: `776ade5c2e2017844785b09ab7af50c7eaf54c03`

Named peer theorem consumed exactly:
- account02/B17 `20260921T124438Z-support-deficit-balanced-equivalence/REPORT.md`
- blob `040ed0078f4905b9b4a11e963f27a1e6dcc3ee8d`
- theorem: `C_FEI = sup_{balanced f,I(f)>1} H(f)/(I(f)-1)`.

Exact applied inference for the live all-gate candidate with `C0=Gamma(1/2)`:

`c_G(1/2,...,1/2) = 4(H(G)/(I(G)-1)-C0)` for every balanced gate with `I(G)>1`, hence

`sup_balanced c_G = 4(C_FEI-C0)` (extended-real interpretation).

A source-exact balanced monotone 18-input seed recorded in the shared-graft dependency has

`H(g)/(I(g)-1) >= 6.521845710923046575658143972948578468366662292`.

At the live `C0=6.4548`, this gives

`c_g >= 0.268182843692186302632575891794313873466649168`,

which exceeds the currently quoted AND margin `0.0043974201` by a factor `>60.9864051178`.

Therefore the live statement that the current read-once potential's worst all-gate margin is attained by a decomposable/two-input-AND gate is false. An arity-5 search is unnecessary for falsification; an explicit arity-18 balanced monotone gate already refutes it. This does not refute FEI.

Replacement obligation: prove a finite upper bound on the balanced supremum above, equivalently full FEI, and any successor all-gate potential must have cap at least the current certified balanced lower bound.
