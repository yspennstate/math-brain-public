# Full FEI continuation — coded scalar-budget obstruction

19 September 2026. **Full Friedgut–Kalai FEI: OPEN / partial research progress only.** No finite universal FEI constant has been proved. This is an owner-requested continuation, not an independent audit or a scheduled-runtime receipt.

## Read and reproduce

- [Full proofs and remaining gap](../continuations/2026-09-19-coded-budget/REPORT.md).
- [Executed standard-library verifier](../continuations/2026-09-19-coded-budget/verify_continuation.py).
- [Actual rational-check output](../continuations/2026-09-19-coded-budget/verification.json).

Run `python verify_continuation.py --part all --output verification.json` from that folder. All accepted inequalities use integers or outward rational logarithm intervals; elapsed time is merely execution metadata. The check is not Lean and not an independent audit.

## What changed

The preceding `continuation-2026-09-19/RESEARCH_NOTE.md` proposed `D_cross <= K(R+Q_log)`. **That estimate is false for every constant K**, not merely for K=8. A deterministic coded perturbation of a tensor of rare clauses has D_cross ->16, R~4m*2^(-m), and Q_log~4m^2*2^(-m). Its ordinary FEI ratio H/I tends to four, so this is NOT an FEI counterexample.

For the explicit 2,040-variable member, a rational certificate proves

    13.716218533308 <= D_cross/(R+Q_log) <= 13.716220897459.

The program enumerates all 2,047 nonzero words of its 11-dimensional code and checks all 255 block-complement ranks. It does NOT enumerate 2^2040 input assignments. A uniform entropy-packet theorem supplies the analytic reduction and the error for every shift.

The dimension-dependent scalar-budget constant satisfies

    n/[40(log_2 n)^3] <= K_n^scalar <= 4(n+1),  n>=2040.

Positive-power variants of the same scalar resolvent also fail for every constant. Do not spend another run merely increasing K or changing that power.

## Positive results retained

1. Code-separated spectral multiplication is approximately entropy-additive, with error `n(eta+sqrt eta)+h_2(eta)+h_2(sqrt eta)`. The corresponding influence formula has error at most `n(eta+sqrt eta)`. Actual signed amplitudes and coherent interference are retained.
2. Along independent uniform multiplicative derivatives, `sum 2^(-k) E R(f_k) <=5J(f)` and `sum 2^(-k) E Q_log(f_k) <=(5/2)J(f)`.
3. The full pivotal resolvent `C=sum_i sum_{A nonempty} u_i_hat(A)^2/(1+|A|)`, `u_i=f*f^{e_i}`, satisfies `sum 2^(-k) E C(f_k) <=(8/ln2+3sqrt2)J(f)<16J(f)`. An exact one-point calculation shows that any universal constant in this accumulated bound is at least eight.
4. In the new obstruction, C tends to sixteen rather than zero. Hence `D_cross/(C+Q_log)->1`: the full-resolvent candidate survives this example.

Historical attribution matters: the September 13 archive already contains a resolvent-payment argument and a minority-conjunction closure theorem. The report credits them. Do not call the existence of every earlier resolvent payment newly discovered, and do not claim a complete reread of all 1,506 archive pages.

## Exact next full-scope task

A sufficient remaining estimate is

    D_cross(f) <= K [C(f)+Q_log(f)]  for every Boolean f.

It is UNPROVED. It is a sufficient strengthening, not a proved equivalent reformulation. If it holds, the explicit accumulated bounds give

    H(f) <= [4/ln2+(3/2)sqrt2+5/4] K J(f) <(37/4)K J(f).

No additional unknown summability lemma is needed after that pointwise estimate. Alternatively continue the correctly quantified universal erasure target `sup B(f)/I(f)<infinity`. Do not revive the false pointwise shortcut `H(f)<=B(f)+(2/ln2)I(f)`.

The separate latest recovery/partition work remains intact. Its boundary-decomposition obstruction and code-erasure results have not been replaced or relabeled by this continuation.

## Delivery and ledger scope

Report creation: `d12d70d86c7a6231f91c1d5627de96a450bc724d`.
Verifier creation: `712972bf65518295067503e3c8dea3e6c1ffdf96`.
Output creation: `8198c1418420da49270af66b1459872d6c93fb4e`.

The report and executed script were read back and their Git blob hashes matched the local files. The output records script SHA256 `618ada5279ab8be5f7b6cfa74d0467587a66ac6096c4175fbd848502904569ae`.

Methods: attack the negation; make a rare coded perturbation; exploit exact conserved Fourier mass and a positive resolvent; sum the actual derivative chain. Source-level before/after: full FEI OPEN -> OPEN. Auxiliary before/after: scalar-budget candidate unproved -> disproved for every constant; packet and quantitative accumulated-budget theorems proved on the page, subject to independent review. Preserve the native P03 finite-dimension metric unchanged; it was not re-audited here.

No schedule was created, restarted, paused, or modified. No peer file, shared root ledger, access control, or repository visibility was changed. Repository delivery is not proof that a scheduled worker has already read the handoff.
