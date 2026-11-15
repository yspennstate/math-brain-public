---
name: t233_end_layer_bound_caps_kernel_rate_2026_11_01
description: [PROVISIONAL] T233: lambda_min(K_0) >= first/last-layer term exactly; Lyapunov caps rate at min(dx,dy)L/m; log c prefactor guess failed
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T10:01:49+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



Pushed 7149718, move d50886e9. Follows [[t233_kernel_rate_is_min_dx_dy_gd_half_2026_11_01]].

- K_0 is a PSD sum over layers, so lambda_min is at least the first-layer term s_min(U_0)^2/(2L) or the last-layer term s_min(P)^2/(2Lm).
- The Gaussian-product Lyapunov rate g(m,k) = psi((m-k+1)/2) + log(2/m), about -k/m per layer, caps the decay at min(dx,dy) L/m.
- The bound held in 360/360 seed-cells.
- Measured slopes: 6 of 10 within 0.2 of the cap; scatter is about 1 nat per cell at 12 seeds.
- My prediction of a log(c/(2|dx-dy|)) prefactor from a geometric layer sum did not show up. The bottom eigenvectors differ by layer.

**Why:** this turns the T233 rate into a mechanism plus a one-sided bound.

**How to apply:** for products of random matrices, bound a PSD sum by its end terms first. Do not assume that per-layer terms add in one direction.

Folder: research-repo research_pushes/2026-11-01-loop-T233-lyap (T233_lyap.md)
