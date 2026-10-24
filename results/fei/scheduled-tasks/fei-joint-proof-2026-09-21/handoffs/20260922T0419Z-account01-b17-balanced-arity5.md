# account01/B17 FEI handoff — balanced uniform arity five closed exactly

Outcome: `AUXILIARY_ONLY`; full FEI remains OPEN / NOT PROVED.

Source-bound scientific artifact: `proofnet24/P03-fei/fleet-2026-09-21/account01/B17/20260922T040831Z-balanced-arity5-complete/REPORT.md`, report commit `8c031a6ad73baf21eab4dc58e19c1a18b642cf44`, report blob `076b4f50407e7af639566671c0367728decc0d28`.

Exact peer inputs consumed: account04/B12 `20260922T004033Z-prime-safe-split/REPORT.md` (safe-split envelope and prime all-coordinate obstruction for the fixed read-once potential), and account04/B14 `20260922T005458Z-gate-balanced-small-arity/REPORT.md` plus its rigorous rational entropy-atom table generator/output.

New theorem: for every balanced Boolean gate on five uniform inputs with `I>1`,

`H/(I-1) <= 6`, sharply.

At the current fixed candidate center `C0=6.4548`, the exact balanced-uniform gate-margin identity therefore yields

`c_G <= 4(6-C0) = -1.8192`.

The proof reduces high edge boundary to `H<=5`, and exhaustively certifies only the low-boundary cases using two Q4 layer masks, exact integer Walsh transforms, and the inherited rational upward entropy atom bounds. It checks 22,620,546 candidate layer pairs; 867,930 have boundary at most 28. Equality is attained by layer masks `000f` and `33ff`, with `I=3/2`, `H=3`.

Implication: the owner's arity-five falsifier cannot be a balanced gate at uniform input bias, including non-unate gates. Any arity-five falsifier must have unbalanced uniform output or genuinely nonuniform input biases. This does not produce a replacement universal potential and does not prove FEI.

Checker source commit `73e01be8c7873b8f7ae47235d22854d83f0abc5d`; output commit `9e8bfdf7dabdce9fd24f9bc3dea2aaa0755db640`; checker exited `PASS=1`.
