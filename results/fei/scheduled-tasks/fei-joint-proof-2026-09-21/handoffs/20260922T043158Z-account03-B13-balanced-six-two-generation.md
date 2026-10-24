# account03/B13 handoff — balanced six-bit two-generation child-slack theorem

Status: `ESSENTIAL_STEP_APPLIED / STRUCTURED_SLICE_CLOSED`. Full uniform-cube FEI remains `OPEN / NOT PROVED`. Execution: `WITHOUT_VERIFIED_BRAIN`.

Scientific source: `yspennstate/math-open-problems`, package at master commit `fc7bb0ee858fa4d58771761635689b7ae282e413`, report path `proofnet24/P03-fei/fleet-2026-09-21/account03/B13/20260922T043158Z-balanced-six-two-generation/REPORT.md`, report blob `6c49a913a2d4cf1e268b77bdcb6e17965d3d274c`; checker blob `4674d422c44ea23ecf7cb22bd367d7703d39dd1f`.

Exact candidate version: `LIMIT-PRIME-GATE-LIFT-v1`, stable centre `C_*=6.5218512`, `Gamma_*=Gamma_RO+0.2682048 p(1-p)`.

Consumed peer artifacts: account04/B17 exact restriction cocycle, blob `d32321447c5f30282f243d9a2907ec719d483c92`; account01/B17 exact balanced arity-five completion, blob `076b4f50407e7af639566671c0367728decc0d28`.

Prior missing implication: the preceding account03/B13 bent-swap run refuted every-node scalar payment and required a child/descendant-slack aggregate.

New proved inference: for every balanced Boolean `G` on six uniform inputs, if one pivot has two balanced five-bit restrictions (equivalently `hat G({j})=0`), then

`H(G) <= 6.5218512 [I(G)-1]`.

The proof uses the exact two-generation ledger

`E_C(G)=0.5 E_C(G0)+0.5 E_C(G1)+C delta-JS(P0,P1)-H(J|S)`,

plus the analytic bound `JS<=2 delta/ln2`, `H(J|S)<=h2(delta)`, and the account01/B17 child-slack gap. Every nonliteral balanced five-bit child has stable slack at least `0.2609256`; the exact-rational checker over `delta=k/32` proves the largest possible local information debit is `<0.110011246728135`, so one nonliteral child leaves parent defect `>0.020451553271865`. Literal-literal cases are solved exactly.

Correlation consequence: any balanced-uniform six-input violation of the stable candidate must have `hat G({j}) != 0` for every coordinate. Quantization gives `|hat G({j})|>=1/16` for every `j`, hence first-level weight `W^{=1}>=3/128`; after input negations all six singleton coefficients may be taken positive.

Applied_to_claim: this is the first explicit two-generation payment replacing the refuted pointwise-local margin route.

Remaining_implication: `LIMIT-PRIME-GATE-LIFT-v1` remains open. The balanced arity-six threat is now confined to the all-nonzero-singleton correlation chamber; biased inputs and higher arity are untouched.

Next attack: combine the six singleton lower bounds with edge-boundary/influence accounting and the exact restriction ledger to close or falsify the remaining balanced arity-six chamber.

Next recipients: primary `account03/B18`; secondary `account01/B17` and `account02/B17`.
