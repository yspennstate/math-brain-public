# HARD8-06 — verification addendum for 2026-09-16T08-48-30Z

This append-only note records the exact checks and publication receipts for the mathematical report

`hard8_2026-09-16/HARD8-06/runs/2026-09-16/2026-09-16T08-48-30Z__report.md`.

## 1. Exact local checks actually executed

The verifier logic was executed with exact SymPy `ZZ` / `F_3` polynomial arithmetic. No floating point, randomized solver, SAT timeout, or numerical root approximation was used.

Results:

- **30** Chebyshev square identities checked exactly, for every `1 <= k <= 30`:
  - odd `k`: `C_k-2=(y-2)A_k^2`;
  - even `k`: `C_k-2=(y^2-4)A_k^2`.
- **720** exact trace-torsion resultant factorizations checked on deterministic randomly generated monic trace polynomials of degrees `1,...,5` (12 polynomials per degree, `k=1,...,12` each):
  - odd `k`: `Res(Q,x^k-1)=Q(1) Res(R,A_k)^2`;
  - even `k`: `Res(Q,x^k-1)=Q(1)Q(-1) Res(R,A_k)^2`.
- **600** exact characteristic-3 criterion checks on deterministic randomly generated monic polynomials of degrees `1,...,6`: direct enumeration of all signed Chebyshev coefficient vectors at tested depths agreed in every case with the criterion that `R mod 3` has an irreducible factor of degree at most `m`.
- Lehmer benchmark verified exactly through `k=12`. The pairs `(Res(R_L,A_k), Res(Q_L,x^k-1))` were

  ```text
  (1,   1,  -1)
  (2,   1,  -1)
  (3,   1,  -1)
  (4,  -3,  -9)
  (5,   1,  -1)
  (6,   1,  -1)
  (7,   1,  -1)
  (8,  -3,  -9)
  (9,   1,  -1)
  (10,  1,  -1)
  (11,  1,  -1)
  (12,  9, -81)
  ```

- The exact reduction
  `R_L mod 3 = y*(y^4+y^3+y^2+y+1)` was checked, as were `3 notin E_0` and `3 in E_1`.

These computations verify the algebraic identities and finite benchmarks only. They are not independent verification of the full conjecture and are not used as a substitute for the proofs in the report.

## 2. Publication receipts

### Mathematical report

Path:

`hard8_2026-09-16/HARD8-06/runs/2026-09-16/2026-09-16T08-48-30Z__report.md`

Creation commit:

`a6388da8a1a4c747adc82adb11c4a592e2d3ed59`

Read back at that exact commit successfully. Returned blob SHA:

`3cd78c1b78e3bb5920c4e0474e8a7c2cbd2ff51d`

Status: **VERIFIED**.

### Exact verifier artifact

Path:

`hard8_2026-09-16/HARD8-06/artifacts/2026-09-16T08-48-30Z__trace_torsion_square_sieve_verifier.py`

Creation commit:

`81ba44aff17f989a2a7a630d5fec23353d20efe7`

Read back at that exact commit successfully. Returned blob SHA:

`75c020a61bb8d0ee9e6d16d97df07b2fab57b846`

Status: **VERIFIED**.

## 3. Last completed mathematical step

The last substantive step of this bounded run was the polynomial-interval clean-prime theorem: after combining the previous short-collision resultant set with the new trace-square torsion sieve, for every fixed `delta < log_3(2)` and all sufficiently large reciprocal hard-core trace degrees, asymptotically almost all primes in a suitable polynomial interval simultaneously give maximal binary trace growth at logarithmic depth and multiplicative order greater than `(log p)^2` for every reduction root.

The exact unresolved gap is residue degree / extension-field counting: these roots need not lie in `F_p`, so this does not yet feed directly into the Breuillard–Varju `bad prime` criterion.