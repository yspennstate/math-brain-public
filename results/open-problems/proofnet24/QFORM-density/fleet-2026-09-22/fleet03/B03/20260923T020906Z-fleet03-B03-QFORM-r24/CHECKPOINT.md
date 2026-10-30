SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T02:09:06Z.
attacking: decoupled time integral — interpolate the translated Brascamp--Lieb screen estimate in L^q so the exact hub ambiguity function closes beyond the old leverage-1/2 gate.

# Early substantive checkpoint

Status: new derivation in progress; full QFORM remains open.

Source controls: math-research-brain fresh-main control revision 2026-09-22.15; newest required mathematical input is `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md` (q-dependent BL/Hausdorff--Young mechanism). Exact hub ambiguity identity/source: `yspennstate/math-open-problems@f68817886312b904e2cf86ccbfb14f4f130229f3:proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/hub_decoupling/REPORT.md`.

Let `A[I,J_L]=UV^T` have rank r>=1, let `w` be the physical hub row, `P_I=[w_I,U]`, `G_I=P_I^T P_I`, `G_V=V^T V`, `P_J=[V,w_{J_L}]`, `G_J=P_J^T P_J`, and let `h=max_i ell_i` be the maximum row leverage of `P_I`. The exact ambiguity reduction gives, after integrating the `Y=<w_{J_L},W_L>` coordinate in L2,

`|phi_Q(t)|^2 <= 2^((r+1)/4) pi^(1/2) |t|^(-1/2) det(G_J)^(-1/4) * int |Psi_I(2t(P_I xi+beta))| [g_h(sigma)p_Z(z)]^(1/2) dxi`,

uniformly in the dense-twist translation `beta`.

New observation: for any `1<=q<=2` with `q>=2h`, the q-dependent translated frame-BL calculation gives

`int |Psi_I(P_I xi+beta)|^q dxi <= (4pi/sqrt(q))^(r+1) det(G_I)^(-1/2)`.

Indeed the normalized row leverage is `ell_i`; the one-dimensional exponent is `q/ell_i>=2`, so the cap-one Fourier bound applies. Holder against `[g_h p_Z]^(1/2)` costs only `||p_Z||inf^(1/q-1/2)`, with `||p_Z||inf<=2^(r/2)det(G_V)^(-1/2)`.

Writing `k=r+1`, `beta_q=1/2+k/q`, this yields the candidate envelope

`|phi_Q(t)|^2 <= D_(r,q) |t|^(-beta_q)`,

where

`D_(r,q)=2^[1/4+(3r+2)/(2q)] pi^[1/2+k/q] q^[-k/(2q)] det(G_I)^[-1/(2q)] det(G_J)^[-1/4] det(G_V)^[1/4-1/(2q)].`

Thus direct L1 Fourier inversion closes whenever `beta_q>2`, i.e. `q<2(r+1)/3`. In particular: rank 1 closes for h<2/3, rank 2 closes for every h<1, and every rank r>=3 closes with q=2 and no leverage restriction. This strictly extends the prior r23 screen theorem, whose q=1 case required h<=1/2.

The determinant combination after inversion is factorization invariant:

`Omega_(r,q)=det(G_I) det(G_J)^(q/2) det(G_V)^((2-q)/2)`.

Remaining work in this run: verify all constants and endpoint cases; derive the L2/collision form; apply the valid fleet04/B03 collision lemma; refresh live corrections; then commit the final proof and source-pinned handoff.

Execution status: WITHOUT_VERIFIED_BRAIN. No schedule/notification/email/task mutation.
