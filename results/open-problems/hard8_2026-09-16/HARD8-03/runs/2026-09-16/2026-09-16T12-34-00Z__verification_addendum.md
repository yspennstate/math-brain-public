# HARD8-03 — verification addendum for 2026-09-16T12:12:08Z

This append-only companion records exact GitHub receipts and the completed bounded verifier for the nullity-three signed-rank checkpoint.

## 1. Exact publication/readback receipts

### Mathematical report

- Path: `hard8_2026-09-16/HARD8-03/runs/2026-09-16/2026-09-16T12-12-08Z__report.md`
- Creation commit: `af3147e8862ef89839c6f297ae52a125f88d4906`
- Exact-commit readback: **VERIFIED**.
- Blob SHA: `330de94494416a6888610e0f8129f7999e56195a`.

### Exact verifier

- Path: `hard8_2026-09-16/HARD8-03/artifacts/2026-09-16T12-12-08Z__nullity3_signed_rank_verifier.py`
- Creation commit: `46151d6938a30ddc1d1a64ab8210eae425374c2d`
- Exact-commit readback: **VERIFIED**.
- Blob SHA: `b6a8cfcfd562f139ad447cdd1a8684f9007fa0d9`.

### Exact output

- Path: `hard8_2026-09-16/HARD8-03/artifacts/2026-09-16T12-12-08Z__nullity3_signed_rank_output.txt`
- Creation commit: `40defc8f238785d68b15c7a9d90c635ae0aaf4e6`
- Exact-commit readback: **VERIFIED**.
- Blob SHA: `787ebb38c9ca4939bd27cddde1d33c02248f9b3b`.

No older report/artifact, peer file, shared index, workflow, branch setting, or access rule was modified.

## 2. Exact execution

The archived verifier was executed before the output file was published. It uses only the Python standard library, exact integer arithmetic, and `fractions.Fraction`; there is no floating-point acceptance condition, randomness, external solver, or timeout inference.

It exhaustively enumerated every set of distinct nonzero Boolean columns in ambient dimensions `1,2,3,4` with exact real nullity three. As in the preceding nullity-two census, configurations embedded in more than one ambient dimension are counted once per ambient universe rather than quotienting by coordinate isomorphism.

Completed counts:

- ambient dimension 3: `7` configurations;
- ambient dimension 4: `6495` configurations;
- total census instances: **6502**;
- signed-relation-rank `sigma=2`: **280**;
- signed-relation-rank `sigma=3`: **6222**;
- exact profile checks: **24,560**;
- exact checks on `sigma<=2` census instances: **840**;
- exact high-threshold checks `rho(r)=0`: **6502**;
- profile values encountered: `rho=0` on **20,267** threshold instances, `rho=1` on **3,492**, and `rho=2` on **801**;
- no `rho=3` threshold occurred in this small Boolean census, so the universal Theorem 6.1 remains supported by proof rather than by a nonvacuous finite instance here;
- no actual small Boolean basis state met the unresolved `rho=2`, `2(k+1)>r` common-negative normal form, so that repository-state check was also vacuous in this census;
- the common-negative pivot algebra itself was independently exercised on **6,136** synthetic exact ternary-coordinate cases through rank parameter `r<=5`;
- maximum observed census ratio `((k+1)rho)/r` was `2/4=1/2`;
- terminal status: `ALL_CHECKS_PASSED`.

The absence of `rho=3` or of the unresolved local normal form in dimensions at most four is finite evidence only. It is not used to assert their universal nonexistence.

## 3. Mathematical status after verification

The deterministic log-rank conjecture remains open. The exploratory universal profile inequality `(P_k)` also remains open.

The new proved reductions retained from the primary report are:

1. nullity three with signed-relation rank at most two satisfies `(P_k)`;
2. all nullity-three configurations satisfy `rho(k)=0` for `k>=r`;
3. a nullity-three rank-three heavy tail obeys the stronger inequality `3(k+1)<=r-1` and therefore cannot violate `(P_k)`;
4. any remaining nullity-three counterexample must have exactly `sigma=3`, `rho=2`, and `2(k+1)>r`, and admits a real-basis normal form with one light and two independent heavy omissions;
5. pivoting one heavy omission through a common negative basis coordinate either makes the second heavy omission light or permits it to be adjoined, increasing the dissociated-set size.

These are self-reviewed project results, not independent peer review.

## 4. Next exact target

The remaining nullity-three task is the `rho=2` transfer-of-heaviness problem. A useful next invariant should follow a sequence of common-negative pivots and prove that the third omitted target cannot repeatedly absorb the heavy role without either decreasing a discrete support potential or closing an impossible sign cycle. Closing that case would prove the candidate profile inequality through real nullity three, but it would still not by itself resolve unrestricted deterministic log-rank.