SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B12, 2026-09-22T18:44:55Z.
attacking: additional-eigenvalue control after scalar-rest conditioning fails; retain scalar-level mass and apply the account04/B12 endpoint-Schur theorem instead of taking a worst conditional fiber.

# B12 handoff — added spectral spike versus scalar conditional fibers

Source control read: `yspennstate/math-research-brain@a57b337af3ad082864f43f387cf28895bcae04c8`, OWNER CONTROL revision `2026-09-22.11`; QFORM remains sole target and no B12/account03 pause was present. Fresh `CURRENT_RESEARCH.md` and `CORRECTION_INBOX.json` were reread before publication. Repository access occurred; native authenticated brain receiver retrieval did not, so this remains `WITHOUT_VERIFIED_BRAIN`.

Canonical proof: `yspennstate/math-open-problems@e2f5bb8e0663997ea4272c13cc21b965b8bf0c5b`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T184455Z-qform-eigenvalue-r15/REPORT.md`.

Main conclusions:

- Concurrent account03/B14 already refuted a universal `sup_b ||p_{Q3|Q'=b}||_infty`; B12 does not claim duplicate priority.
- Independent exact cube/spectral model: with `v=(1,1,1,1)/2`, iid `Unif[0,1]`, core eigenvalues `(1,3/2,2)` on `v^perp`, and extra eigenvalue `mu=-1/2` on `v`, conditioning on the scalar remainder is equivalent near the cube corner to conditioning on `S=sum_i(1-X_i)=s`. Then `Q3|S=s=s^2 T`, so `||p_{Q3|Q'}||_infty >= 1/(2s^2)` and its worst scalar-fiber cap is infinite.
- The endpoint mass compensates the blow-up: `p_S(s)=s^3/6` for `0<s<1`; an explicit coarea estimate gives `||p_T||_infty <=3*pi*sqrt(2)`, hence `E[||p_{Q3|Q'}||_infty; S<1] <= pi*sqrt(2)/4`. This supports mass-weighted scalar conditioning / aggregate-before-supremum as the replacement interface.
- Named partner result actually applied: account04/B12 `20260922T181535Z-account04-B12-endpoint-tail-r1`, canonical path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260922T181535Z-account04-B12-endpoint-tail-r1/REPORT.md`.
- Apply it to `A_{-T}=P_{v^perp}-T vv^T`. For physical coordinate 1 the endpoint Schur matrix is exactly `S_infty=I_3+J_3`, with eigenvalues `(4,1,1)`, while the pivot is `a=(3-T)/4`. Therefore, for every `T>3`,
  `||p||_infty <= 4*sqrt(C_*/(T-3))`, `C_*=24.183038289961516...`, i.e. `19.6705010774.../sqrt(T-3)`. The full density bound improves as the added opposite-sign eigenvalue grows even though the worst scalar conditional core density diverges.
- Exact endpoint geometry: if `A0 v=0` and `v=(u,w)`, then `S_infty=R^T A0 R` with `Ry=(-w^Ty/u,y)`. Hence `A0 >= L P_{v^perp}` implies `S_infty >= L(I+ww^T/u^2) >= LI` without rotating independent coordinates.

Full QFORM remains OPEN. Continuity is not proved by this Schur estimate itself. Next B12 obligation: derive an aggregate-before-supremum inequality stable under arbitrary added spectrum, or combine endpoint-Schur and grouped original-coordinate bank branches into an exhaustive reduction without losing the scalar-level/product mass weight.
