# R15 idea note — n=30 projective-polygon / positive-mass attack

UTC 2026-09-20. Status: **SELF_CHECK_ONLY / NOT CLAIMED / PENDING**. This is retained-screen work only. It does not reopen Burdzy--Scheutzow I0076, RS-2026-CL-B, or I0124, and it does not promote F0111 to READY.

Immediate previous R15 method triple was #1/#18/#27. This run uses **#6 DEFORM TO A POINT YOU CAN SOLVE, #14 FIND THE GROUP ACTING, #24 FIND THE EXTREMAL OBJECT**.

## Route before computation

The preceding R15 report gave an exact Gram-polygon characterization of the PSD/null/projective-fourth-order subsystem for a two-level mixed Hessian-null direction. For an outer-branch full-support candidate the block masses satisfy

- `r_i > rho := -k/(n-1)` because `q_i>0` and `k=-(n-1)/S(q)`,
- `r_i <= 1/A_J` on `J` and `r_i <= 1/A_K` on `K` from the projective residual diagonal,
- `sum_J r_i=x`, `sum_K r_i=y`,
- the residual polygon lengths are `(1+delta)sqrt(r_i(1-A_J r_i))` on `J` and `(1-delta)sqrt(r_i(1-A_K r_i))` on `K`.

The earlier aggregate projective bound leaves its first possible full-support dimension at `n=30`, necessarily on the `z>1` branch, with the sharp old boundary approached at `z downarrow 1`, `delta -> 1/2`.

This run will attack exactly that first surviving dimension rather than derive another generic derivative condition. The intended chain is:

1. **#6** deform the `z>1` branch to the sharp boundary `(delta,z)=(1/2,1)` and identify which integer block split `(M,N)`, `M+N=30`, can survive the mass lower bounds and projective caps;
2. **#14** use the full within-block permutation symmetry of the constraints to reduce extremal mass allocations to endpoint/equalized patterns, not an arbitrary 30-variable search;
3. **#24** solve the extremal problem for the Euclidean polygon lengths under `rho < r_i <= 1/A` and fixed block sum. In particular, determine the least possible opposing polygon length and the greatest possible compensating length. If the largest required edge still exceeds the sum of all possible opposing edges, `n=30` is impossible.

The key new ingredient relative to the previous report is the strict positive lower mass `rho=-k/(n-1)`, which prevents the polygon construction from hiding arbitrary coordinates at zero mass. If the attack fails, record the exact extremal family that survives; that family becomes the next candidate rather than another generic lemma.
