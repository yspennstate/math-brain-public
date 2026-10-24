# FEI handoff — balanced restriction-minimality of the arity-10 gate falsifier

Source scientific report:
`proofnet24/P03-fei/fleet-2026-09-21/account02/B18/20260922T0117Z-balanced-restriction-minimal-gate/REPORT.md`, scientific commit `e12fe45093331b38a221302f701644218b6087eb`.

Consumed peer results: account03/B12's exact genuine ten-input balanced gate falsifier, account04/B14's exhaustive balanced-monotone six-input extremum, account02/B16's exact signed restriction-margin martingale.

New exact finite theorem: for the account03/B12 ten-input witness, all `3^10-1=59048` proper coordinate restrictions were enumerated. Exactly `9514` are balanced. There is no balanced codimension-one or codimension-two restriction. The first balanced descendants occur at codimension three, exactly forty; after dummy deletion every proper balanced nonliteral descendant has at most six essential variables. Hence account04/B14 applies and gives

`H/(I-1) <= 46/5-(9/5)log2(3) = 6.3470674987... < 6.4548`,

so every proper balanced nonliteral descendant has old-candidate uniform balanced margin at most `-0.4309300051...`, while the ten-input parent has certified margin `>0.01828912655`.

Implication: the completed AND/decomposable-extremality falsifier is restriction-minimal on the balanced slice. A restriction/Bellman proof cannot explain its positive root margin by descending through smaller balanced obstructions; one or two splits necessarily leave balance, and the first return has already collapsed to the safe six-essential-input regime. The exact account02/B16 martingale therefore must retain genuinely unbalanced child continuation slack. This is not a full FEI proof.

Checker and archived deterministic output are adjacent to the scientific report. Full FEI remains OPEN / NOT PROVED.
