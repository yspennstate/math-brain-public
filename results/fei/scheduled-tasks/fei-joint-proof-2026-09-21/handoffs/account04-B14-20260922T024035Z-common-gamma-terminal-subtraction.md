# account04 / B14 FEI handoff — common-Gamma terminal subtraction

**Status:** `ESSENTIAL_STEP_APPLIED / FINITE_OBSTRUCTION_CLOSED`; full FEI remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## Exact consumed sources

- Stable fixed candidate: `proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T0222Z-shared-graft-tail/REPORT.md`. It fixes
  `C*=6.5218512`, `a*=0.2682048`, `Gamma*=Gamma_RO+a* p(1-p)` and leaves `LIMIT-PRIME-GATE-LIFT-v1`.
- G10 stopping tree: `proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T0254Z-and-atom-stopping/REPORT.md`, blob `8a35d08850c8bf38a36c58af4ee3dcd670fa0de9`.
- Exact signed stopping ledger: account02/B16 `20260922T010120Z-gate-margin-restriction-martingale`, blob `335d6ffa58cae84c7b47e742a250a20d2e2bddd4`.
- Read-once dyadic AND/OR tightness: account03/B17 `20260922T014022Z-prime-dyadic-barrier`, blob `495aa3932db915878b3c3f379d946dbd89ccba4e`.

## New lemma and application

For any quadratic lift `Gamma_a=Gamma_0+a phi`, `phi(p)=p(1-p)`, and any bounded physical stopping rule `sigma`,

`D_a(G)-E D_a(G_sigma) = [D_0(G)-E D_0(G_sigma)] + a [P(G)-E P(G_sigma)]`.

Hence if every nonaffine terminal is tight for `Gamma_0`, the common-potential block residual is exactly

`D_block(a)=D_0(G)+a Q_block`.

For exact prime `G10`, the B12 stopping tree has `Q_block=229/1024`; all nonaffine terminals are uniform two-input AND/OR atoms and are tight for `Gamma_RO`. With `C0=6.4548` and the certified G10 entropy interval, the exact lift threshold for the stopped block is

`0.020605216813393513082969432314 < a_G10,block < 0.020605216813393517554585152838`,

or center

`6.459951304203348378270742358079 < C_G10,block < 6.459951304203348379388646288210`.

The stable lift `a*=0.2682048` clears this by a factor greater than 13 and leaves strict block residual

`0.055371391161848520 < D_block(Gamma*) < 0.055371391161848521`.

Independent check: stable root slack is `>0.062967034911848520`; expected terminal AND/OR slack is exactly `0.00759564375`; subtraction matches the displayed block interval.

Thus the terminal-atom subtraction problem is closed for the source-valid G10 uniform restriction corridor **with one and the same Gamma***. No prescribed-coordinate erasure claim is made.

## Scientific artifacts

`proofnet24/P03-fei/fleet-2026-09-21/account04/B14/20260922T024035Z-common-gamma-terminal-subtraction/`

- `REPORT.md` blob `71523d7c82657e78141eea99278f3efb82680713`
- `CHECKER.py` blob `939373274291bfe9cc14864b18d6eda54f9858ca`
- `CHECK_OUTPUT.txt` blob `066346ed496c3a23e3aa2ee8c16db72c146a2f14`
- scientific readback commit `092b88b5672460f30d5336115bbe6d4bb1aac448`
- checker SHA-256 `93c776230e016c9eaf06adf9e4a9947318a5fbae0f76125aab61d17c6c792610`
- output SHA-256 `026e09b48f8149a8dc65d697987eccd67ad832beeafb23cae1de90c962f02f96`

## Next arrow

Keep the fixed `LIMIT-PRIME-GATE-LIFT-v1` target. Prove, for every prime near-obstruction, existence of a realizable stopping rule with `Gamma_RO`-safe terminals and

`-[D_RO(G)-E D_RO(G_sigma)] <= a* [P(G)-E P(G_sigma)]`, `a*=0.2682048`,

or produce a source-valid gate/bias counterexample to this stopped-block compiler.
