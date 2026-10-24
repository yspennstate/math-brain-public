# POS3 handoff — account03/B10 endpoint atom and insertion-cut moments

Status: `ESSENTIAL_STEP_APPLIED`; parent POS3 remains **OPEN / NOT PROVED**.  Execution context: `WITHOUT_VERIFIED_BRAIN`.

Source-bound scientific artifact:
- repository: `yspennstate/math-open-problems`
- report: `proofnet24/collective-POS3/account03/B10/20260922T011516Z-b10-pos3-r11/REPORT.md`
- report commit: `c4aeebd9046d68350b33939b5d67749b36bb377d`
- report blob: `baed44f6a8185fd3632d9da99701a25011494c7e`
- checker blob: `ef638bdc242828060f53e9218858bf4bc4a6fd4e`
- archived checker-output blob: `2207b160a3a7a0df74f3f4533d2cf182ecec80af`

## Safe peer artifacts consumed and exact change

Newest named partner consumed: account04/B11 `B11-20260922T011236Z-pos3-r12/REPORT.md`, blob `e37a40f77dbe414014200d2db8a4cd5601f57d24`. It proves that the true bounded-range residue is `7<=pi(P)<=K_3` and refutes the finite-kernel shortcut even at `pi=7`. Its preceding report blob `f4b7ca2b9a3902e527f9d30de8cb8ea043f670d4` supplies the generic canonical-rank atom and mean insertion bound.

Newest compatible integrator consumed: account04/B20 `20260922T011156Z-b20-auto11/REPORT.md`, blob `b6b06537e4543c606c96d3f159567192fc0daeac`. It gives the exact nested-profile lower-fringe-minus-upper-fringe defect and whole-majority-block canonical-gap mass `>1/3`.

Exact validation/research change from B10:
1. At either strong-majority endpoint, width three implies at most two minimal opposite-side boundary elements can be incomparable with the endpoint. Shepp XYZ therefore strengthens the endpoint canonical-rank atom from `>8/27` to **`>4/9`**.
2. Hence for deletion of a strong-majority endpoint, under the **uniform** law on `L(P-x)`, the exact insertion multiplicity satisfies **`E W_x < 9/4`** and `E(W_x-1)<5/4`.
3. For every element `x`, define the exact insertion-cut cost `C_x(tau)` as the total number of majority-orientation errors across all legal lifts of a deletion fiber. Then
   `sum minority probabilities involving x = E C_x / E W_x`.
   In a counterexample this is `< m_x/3`, where `m_x=|I(x)|`.
4. Pointwise `C_x(tau) >= floor(W_x(tau)^2/4)`, so every hypothetical counterexample obeys
   **`E W_x^2 < (4m_x/3) E W_x + 1`**.
5. At a strong-majority endpoint, exactly `C_x=W_x(W_x-1)/2`, giving
   `E[W_x(W_x-1)] < (2m_x/3)E W_x < 3m_x/2`,
   `E W_x^2 < 3m_x/2 + 9/4`, and the factorial tail bound
   `Pr(W_x>=t) < 3m_x/(2t(t-1))` for integers `t>=2`.

Regression: exact enumeration through six vertices checked 3,702 width-at-most-three posets, 2,419 qualifying local `(P,x)` cases, and 1,662 endpoint cases. Minimum observed endpoint atom was `10/19`, maximum observed endpoint mean insertion multiplicity `19/10`; marker `POS3_INSERTION_MOMENT_CHECK_PASS`.

## Next exact obligation

Combine the B20 two-fringe boundary-charge decomposition and whole-block `>E/3` corridor pinning with the new no-balanced insertion-cut budget. Prove the signed nested-profile charges across consecutive strong-majority blocks cannot all retain the required orientation while every element satisfies the cut-cost inequalities, or construct a genuine width-three family satisfying the complete system and identify the missing invariant. Do **not** replace this by a finite census or bounded-density argument; the newest B11 family refutes that shortcut.

No benchmark gold, held-out labels, FEI proof material, credentials, scheduler metadata, unrelated private data, email/Drive content, paid API/Codex use, workflow dispatch, or public release is present.
