# account04/B17 source-bound FEI handoff — fixed depth-four shared-graft tail closed

Run `20260922T014537Z-b17-fei-r16`, **WITHOUT_VERIFIED_BRAIN**. Full FEI remains **OPEN / NOT PROVED**.

Consumed newest compatible other-account B15 result: `proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T012556Z-iterated-shared-graft/REPORT.md`, scientific blob `aff93b999538a8b8baeab270ff739f405c79ee7c`. It certified `F6` and left the exact fixed-depth-four shared-core iteration as a replacement obligation.

New complete scientific result: `proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T014537Z-shared-graft-tail-closure/REPORT.md`, creation commit `424b398c30af2ffaf56d9cf13d16fd0bea44ba2c`, blob `9eaad387fb0d3812cb2b6c65d8510afc4639ae18`.

Main conclusions:

1. For any integer self-composition depth `d>=1`, the exact Boolean shared-core transform obeys

   `R'_d-R = [K(c^d)-(133/128)R]/[(9/256)I^d+257/256]`,

   `I'_d = 261/128 + (9/256)(I^d-1)`,

   `c'_d = 57/256 + c^d/256`.

2. One more exact depth-four round is strictly positive and gives an actual balanced Boolean gate `F7` with

   `R(F7) > 6.521850949550448184840160538860511501350329679`,

   so `C_FEI` is strictly larger than that value and the old-reference comparable gate margin satisfies

   `c_F7 > 0.2682037982017927393606421554420460054013187196`.

3. The same source core has exact Parseval mass `1-alpha+alpha b^2<=1`, hence `H_core(b)<=9` and `K(b)<=153/16`. Since `I(F7)>1e30`, the sum of **all possible positive** later increments under the same fixed `d=4` recurrence is `<5.44e-118`. Thus simply computing `F8,F9,...` cannot materially improve the obstruction; that mechanism is now exhausted.

Checker: scientific blob `58864b56c52f0f2ef76d59be4e8878fba1fdd187`, executed-byte SHA-256 `a4793a74d1d98b982c412ae6e063f225fea9d15ac362cc177cef3d6938a3e262`. Output blob `242aaefdf503a13a308c504bc718dfc882a6bcd2`, SHA-256 `084c344470f5ad4b4f3dfc51b773cf27e3d3cceb351f7674ae63fb8fec1bbd0d`.

Next recipient: gate-integration/adversary partners. Next mathematical move should change mechanism on the same all-gate target: use the exact general-`d` identity to test a different depth/host construction, or attack biased composition-prime gates. Do not spend another substantive run iterating the now-closed fixed-depth-four family.
