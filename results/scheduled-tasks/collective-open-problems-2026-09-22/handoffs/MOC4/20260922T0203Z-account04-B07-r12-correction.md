# MOC4 correction handoff — account04/B07 r12

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Worker/run: account04/B07, `20260922T014149Z-account04-B07-MOC4-r12`  
Outcome: `CANDIDATE_REFUTED`; parent MOC4 OPEN.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

**This handoff supersedes this run's earlier `20260922T014149Z-account04-B07-uf-refuted-parity-endpoint.md` wherever they conflict.** Preserve the earlier file as history.

Final scientific report: `yspennstate/math-open-problems/proofnet24/collective-MOC4/account04/B07/20260922T014149Z-account04-B07-MOC4-r12/FINAL_REPORT.md`, commit `db3088279bf3047340446c546eed9185bda66f67`.

The run's durable new result remains valid: assigned OTHER-account partner account01/B08's earlier `MOC4-UPPER-DRURY-FACET-FAN-v1/(UF)` is exactly refuted by Gaussian-rational spectra. With

`a=(-1+76i,91-158i,1+50i,161+192i)/100`,
`b=(-24+48i,-69-103i,174+159i,197-193i)/100`,
`L(z)=-3 Re(z)-Im(z)`,

all 24 spectral vertices have unique L-maximizer `2341` with `M=942601979/25000000`, while the Drury representative `3u=v_3214+v_4132+v_3421+v_2341-v_3241` has `L(u)=946704719/25000000`. Exact gap:

`L(u)-M=205137/1250000>0`.

This refutes only the spectral-only `(UF)` shortcut, not MOC4.

**Concurrent-peer correction.** After the earlier same-run handoff was committed, two newer exact artifacts became visible:

- account01/B07 `20260922T013731Z-b07-moc4-r11b`, report commit `a0fac94c9342ee4a2c18ed94f7fe770bdf0b12df`, refutes universal existential parity slack on generic structured true-unitary data and proves the exact X-aware support-gap identity;
- newest assigned partner account01/B08 `20260922T013942Z-b08-moc4-r11`, report commit `1204bdd4463fa137bcfb1d53c3b5ce9702930924`, identifies the convex-roof quantifier as the **maximum** endpoint parity penalty and refutes the corrected unconditional scalar roof on generic structured true-unitary data.

Therefore this run's earlier `MOC4-PARITY-ENDPOINT-v2` proposal is **withdrawn**. Its one-parameter S3 Birkhoff algebra is correct but duplicates the concurrent peer derivation and used the wrong endpoint for the roof. No new-credit claim is made for it.

Current first essential routes are the newest partner's stationarity-conditioned roof `MOC4-STATIONARY-ROOF-v1` or account01/B07's more faithful `MOC4-SUPPORT-GAP-RESCUE-v1`; both retain true-unitary structured information. The new UF counterexample additionally rules out replacing those mechanisms by a purely spectral Drury-facet positivity argument.

Exact verifier/output for the UF counterexample remain at commits `9cef5ea97e007820721f6e9ac158e12ecc878447` and `32e4902f06097b125ea84bd097b0803e61b3dd31` in the scientific archive.
