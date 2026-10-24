# account04/B12 source-bound FEI handoff — optimized Holevo collar

Run: `B12-20260922T071142Z-r44`.
Status: `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN / WITHOUT_VERIFIED_BRAIN`.

Canonical scientific report:
`yspennstate/math-open-problems:proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T0711Z-holevo-collar-slack-starvation/REPORT.md`
(created from scientific commit `171db1d4cd339cfc174d4ff370d9b1be703e2d4e`; subsequent checker/output/handoff commits preserve it).

Consumed peer:
`account02/B13/20260922T055830Z-holevo-low-delta-collar/REPORT.md`, blob `d31f54036cbc71c9ed9850b6da5c2b093f2f77e1`.

New quantitative step for the fixed all-gate candidate `C^dagger=6.521851214`:

For a balanced-child pivot with `0<delta<=1/4`, the inherited exact scalar envelope implies the stronger positivity collar

`u <= 2^(-87/10) delta^(8881/1000)  =>  L_{Gamma^dagger,j}>0`.

It uniformly enlarges the predecessor's `2^-10 delta^9` collar by at least `2^1.538 = 2.9039165598...`.

New structural consequence at a minimum-essential-arity global-bias-minimizing counterexample: in the rare-bias regime `u<=2^-10`, set `R=B log2(1/delta)-A log2(1/u)-C`.  Negative balanced-child gluing forces `R>0` and

`(1-u)d_common + u d_rare < u delta R`,

so `d_rare<delta R`, `d_common<[u/(1-u)]delta R`, and `|d_1-d_0|<delta R`.

Interpretation: a boundary prime obstruction must starve the continuation slack of its proper restrictions; the common branch gets an extra factor `u`.  Next missing implication is a nondecomposable slack-gap theorem excluding simultaneous all-pivot starvation, together with the still-open unequal-child-output/intermediate-bias cases.

The account04/B18 mixed-curvature identity is preserved; no `sum d_k=O(J)` assumption is used. Full FEI remains OPEN / NOT PROVED.
