# HARD10-03 — 2026-09-16T12-51-30Z checkpoint addendum

**SOLUTION STATUS: PARTIAL.** The full `d=3` Tóth infinite-cycle conjecture remains open. This append-only file records delivery receipts, a coarse Frostman reformulation of `NEW-L90`, and the finite combinatorial sanity certificate. No prior task file is overwritten.

## 1. Main report delivery receipt

Main report:

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T12-51-30Z__report.md`

Create commit:

`4a4a97bd9fdc1f9f25e2788d679eb38ced385c17`

Exact-create-commit readback blob:

`6d0250275d6a102679302af7adc1da1606711fde`

The file was fetched back using exactly that commit ref. The opening target/backfill section, the deterministic occupancy lemma and `NEW-L90`, and the complete `NEW-L91` Green-energy/capacity proof were all read back from the immutable create commit. Main-report delivery is therefore **VERIFIED**.

No transient retry was needed. No approval/security denial occurred. Approval requirement: **NOT EXPOSED**.

---

# 2. NEW-L92 — coarse `3/2`-Frostman law on subdiffusive scales

The scale frontier in `NEW-L90` has a useful geometric reformulation.

For a finite cycle `C`, write its uniform probability measure as

\[
\mu_C=\frac1{|C|}\sum_{x\in C}\delta_x.
\]

For scales

\[
R=\beta^\rho,
\qquad
\frac13\le\rho<\frac12,
\]

`NEW-L90` gives

\[
\sup_z\mu_C(B_2(z,R))
\le
C_{\rho,\epsilon}
\beta^{-\left(\frac34-\frac{3\rho}{2}\right)+\epsilon}
\]

outside an exceptional finite-cycle event of probability `O(beta^{-epsilon})`.

Set

\[
s:=\frac12-\rho\in(0,1/6].
\]

Then

\[
\frac34-\frac{3\rho}{2}
=
\frac{3s}{2},
\]

and

\[
\beta^{-3s/2}
=
\left(\frac{\beta^{1/2-s}}{\sqrt\beta}\right)^{3/2}
=
\left(\frac{R}{\sqrt\beta}\right)^{3/2}.
\]

Therefore:

### Corollary NEW-L92 — PROVED

For every fixed `rho in [1/3,1/2)` and `epsilon>0`, for all sufficiently large `beta`,

\[
\boxed{
\mathbb P\left(
L_\beta(0)<\infty,\ 
\sup_{z\in\mathbb Z^3}
\mu_{C_0}(B_2(z,\beta^\rho))
>
C_{\rho,\epsilon}
\beta^{\epsilon}
\left(\frac{\beta^\rho}{\sqrt\beta}\right)^{3/2}
\right)
\le
C_{\rho,\epsilon}\beta^{-\epsilon}.
}
\tag{2.1}
\]

Thus, between spatial scales `beta^{1/3}` and `beta^{1/2-o(1)}`, a hypothetical finite root cycle obeys a quenched coarse Frostman upper bound with effective exponent `3/2`, up to `beta^{o(1)}` losses.

This does **not** assert that the support has Hausdorff dimension `3/2` in any limiting geometric sense. It is a scale-dependent mass-distribution statement for the random finite cycle at large `beta`. Its value is operational: a no-peeking exploration that preserves this mass-spread structure would have many candidate neighborhoods at each subdiffusive scale rather than a single dense trap.

At smaller scales `rho<=1/3`, the current method saturates at the `beta^{-1/4+o(1)}` mass bound; improving that saturation would require information beyond the present `o(sqrt(beta))` driver-coupling horizon.

---

## 3. Finite combinatorial certificate for Lemma 3.1

After the mathematical report had already been committed, an exhaustive finite sanity check was run for the deterministic cyclic occupancy inequality underlying `NEW-L90`.

The checker encodes a fixed spatial ball by a binary cyclic word: marked positions are cycle vertices lying in the ball. A cyclic start is bad when its `H+1` window contains at least two marked positions. For `H>=L`, the actual orbit window repeats a cycle vertex, so every start is correctly forced bad.

The checked inequality is

\[
\frac{|S|}{L}
\le
\frac{\#\{\text{bad starts}\}}{L}
+
\frac1{H+1}.
\tag{3.1}
\]

All binary words for every `1<=L<=10` and `1<=H<=10` were enumerated: `20,460` cases, zero failures.

This finite enumeration is only a sanity certificate. The proof in the main report is the actual argument.

Checker path:

`proofnet24/HARD10-03/artifacts/2026-09-16T12-58-00Z__local_mass_combinatorial_check.py`

Create commit:

`ac07a659785bb03bfdb5363f4892ff75e81efe9d`

Exact-create-commit readback blob:

`05ea88de11412f48afef330fe55f144e604bc659`

Status: **VERIFIED**.

Executed-output path:

`proofnet24/HARD10-03/artifacts/2026-09-16T12-58-00Z__local_mass_combinatorial_check_output.json`

Create commit:

`8e83b5cd1e5f6f990b5a16ef7d6b5a63bb3c360f`

Exact-create-commit readback blob:

`885c362127aa537339348367d27b44e83556a7e2`

The output records

```json
{
  "cases_checked": 20460,
  "failures": [],
  "max_L": 10,
  "status": "PASS"
}
```

Status: **VERIFIED**.

---

## 4. Post-write scope check

1. `NEW-L90` is a statement about the complete finite permutation cycle but is proved only from short driver-coupled cyclic windows plus exact orbit averaging; it does not treat chronological SRW paths as permutation cycles.
2. The uniform local-mass conclusion is simultaneous over all deterministic or random ball centers because it follows pathwise from the fraction of bad cyclic starts; no union bound over spatial centers is used.
3. `NEW-L91` uses the uniform ball bound only after restricting to the event that the root cycle is finite. It does not assume `P(L=infinity)=0` globally.
4. The capacity implication has the correct direction: `Cap_g(A)^{-1}` is the infimum of Green energies over probability measures on `A`, hence it is at most the energy of the uniform measure.
5. Neither `NEW-L91` nor `NEW-L92` is fed back into a same-slab deterministic closure inequality; the anticipativity barrier remains explicit.
6. The conjecture is not closed by these results. The missing step is still a nonanticipative extraction/restart lemma that converts the now-quenched mass-spread/capacity geometry into fresh conditional escape or closure cost.

The next run should prioritize that admissible exploration step rather than further unconditional repackaging of the same geometry.