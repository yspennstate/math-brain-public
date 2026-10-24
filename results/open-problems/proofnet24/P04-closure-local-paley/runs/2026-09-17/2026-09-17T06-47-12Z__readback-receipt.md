Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. GPT-6 / maximum was requested in prompt text only; no scheduler model/reasoning selectors or authenticated routing receipt are exposed.

# P04 / I0101 immutable readback receipt

Report:

`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T06-47-12Z__run-report.md`

Creation commit:

`674e887e89a1715a699192d78a78ec3eba623524`

Verified report blob at that exact commit:

`9e91d81dea89249141b7de6dc1d0c9e0c801b682`

Readback was performed from the creation commit, not from moving `master`, in contiguous requested ranges:

- lines 1--220;
- lines 221--440;
- lines 441--660;
- lines 661--900 / EOF.

The final range contains the terminal marker:

`**End of complete run report.**`

Status:

`COMPLETE_READBACK_VERIFIED_WITH_ONE_TEXTUAL_TYPO`

One harmless transport/authoring typo was detected in the inverse-zero proof: the sentence rendered as

`Let i ne j be a nonedge.`

It should read

`Let i != j be a nonedge.`

(or equivalently LaTeX `i\ne j`). The immediately following sentence identifies `S_ij=S_ji` as a free nonedge coordinate, the perturbation is explicitly `E_ij+E_ji`, and the conclusion `(K_t)_ij=0 on every distinct nonedge` is stated correctly before and after this sentence. No formula, claim, proof step, audit verdict, metric, or conclusion changes. The immutable report was not overwritten.

Verified run state:

- frozen metric: `4021 -> 4021` (`NO MOVEMENT`);
- complete exact-certified domain: `{149,257,1009,4001,4013,4021}`;
- unchanged streak: `1 -> 2`;
- methods: `B5, B21, B24`;
- new claim: `P04-I0101-MAXDET-PRECISION-CENTRAL-PATH-16 = PROVED / STRUCTURAL-PARTIAL`;
- checker: none, by design; continuous theorem proved symbolically;
- directed audit: `P04-AUDIT-P11-I0062-FINITE-COLUMN-MIN-SHARP-08 = PASS (CLAIM-SCOPED)`;
- source status: `OPEN`; P04 status: `PARTIAL`;
- next methods: `B18, B7, B12`.

**End of readback receipt.**