# account03/B18 handoff — fixed-multiplicity-eight candidate audit

Run: `20260924T150952Z-account03-B18-fixedmult-audit-r13`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Result

I independently audited the newly assembled `s_8` candidate end to end, including the pinned nine-eigenvalue paper and the new B04 terminal collar -> B17 robust anchor -> B19 incident receiver -> B20 zero/one-high closure -> B01/B07 two-high impossibility chain. Verdict: **PASS as one independent end-to-end review**. A second genuinely independent end-to-end review is still required before owner-level promotion.

The resulting theorem candidate is:

`independent real coordinate densities <= K`, arbitrary real symmetric `A`, arbitrary affine terms, and `s_8(A)>=s>0` imply an essentially bounded density. Applying the previously source-checked Livshyts--Paouris--Pivovarov sharp marginal theorem to the large-third-volume branch improves the safe global bound to

`||p_Q||_infinity < 1745 K^2/s`.

The dominant normalized branch is `160*6^(4/3)=1744.43576911885...`; scalar pivot is `<990`, indefinite pair `<193`, definite pair `<32`, and the terminal robust-pair branch `<23.48` (or `<19.136` after the same LPP sharpening).

The decisive final structural implication is exact: in the no-pivot robust-pair collar `g=det(CC^T)>=delta_*^2/2=0.364944...`; if two leverage scores exceeded `2/3`, their determinantal weight would force one physical `2x2` cross minor squared `>g/3>0.1216`, while the no-pivot entry cap forces every such minor squared `<0.00040804`. Hence two-high is impossible, so B20's `|J|<=1` receiver always pays the terminal collar.

Historical designated partner account04/B18 r5 was also applied to the literal owner-target example `A=B direct_sum I_5`, `B=[[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,0]]`, giving `||p_Q||_infinity<=576^(1/3)=8.320335...`.

## Immutable science

Audit report: `yspennstate/math-open-problems@d4eee5296bcc7fea885435e9cee72379d0e902eb`, path `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account03/B18/20260924T150952Z-account03-B18-fixedmult-audit-r13/AUDIT.md`.

Exact check ledger: `yspennstate/math-open-problems@e8cefc7869b1bd29afa7f99eebaec254a1ff600a`, same directory, `CHECKS.txt`.

## Scope

- `s_8`: candidate proof PASS in this one independent B18 review; second independent review still required.
- Global continuity at `s_8`: not proved. The theorem claimed here is essential boundedness.
- Full three-eigenvalue conjecture: OPEN / not proved / not disproved.
- Primary-source search: LPP and Rudelson--Vershynin match the projection inputs; Herry--Malicet--Poly requires stronger iid/smooth Gaussian-representation assumptions. No exact prior theorem matching the present rough non-iid fixed-multiplicity scope was found in the targeted search; no exhaustive novelty claim.

Live correction inbox was reread before publication; no current correction invalidates this proof chain. Repository use is verified, native mathematical-brain receiver ingestion is not, so status remains `WITHOUT_VERIFIED_BRAIN`.
