# B04 early substantive checkpoint: optimized volume-marginal Fourier gate

Programme: QFORM-DENSITY-3EIG-20260922. Run: B04-20260923T032130Z-r23. Status: supporting calculation, full QFORM open.

I independently checked the matrix/tail certificate in `interactive/20260923T002323Z-volume-stability/REPORT.md` and `PEER_TAIL_EXTENSION.md` through the volume-marginal identity, projection estimate, q-dependent Hausdorff--Young/Brascamp--Lieb step, and inversion. No contradiction found in the checked chain.

A new optimization is immediate and materially sharpens/extends the stated tail exit. Let `P` be an orthogonal projection on the row side of a physical cross block `M`, put

- `L=max_i P_ii`,
- `T2=sum_{j>=3} s_j(M)^2`,
- `rho=||(I-P)M||op/sqrt(T2)`,
- `delta=sqrt(3) rho`.

From `T2 E2 <= 3 E3` and `W <= (E2/E3) M M^T`, the exact third-volume row marginals satisfy

`sqrt(alpha_i) <= sqrt(P_ii)+delta sqrt(1-P_ii)`.

For `L<=1/2`, this gives `alpha_i <= A=(1+delta)^2/2` whenever `delta<=1`. The q-dependent Fourier theorem allows every `q>=max(1,2A)` with `q<3/2`, and its constant is increasing in q. Hence if

`rho < rho_*=(sqrt(3/2)-1)/sqrt(3)=0.1297565119969...`,

we may take the optimal admissible `q=(1+sqrt(3)rho)^2` and obtain

`||p_Q||inf <= C(rho) E3(M)^(-1/6)`,

`C(rho)=3e / ([3-2(1+sqrt(3)rho)^2](1+sqrt(3)rho))`.

At the previously used `rho=1/15`, this improves the coefficient from `9 sqrt(3)e/2 = 21.186910...` to `14.2939411744...`. For `P` equal to the top-two left singular subspace, `rho=s3/sqrt(T2)`, so a tail stable rank `T2/s3^2 > 59.3938769...` already suffices, improving the prior sufficient threshold 225. For example stable rank at least 64 gives a finite explicit coefficient `166.6516673...`.

Remaining work this run: write the full proof carefully, quantify the near-diffuse perturbation improvement, apply the optimized certificate to an explicit genuinely rotated indefinite no-pivot matrix, refresh corrections, and publish final report/handoff.
