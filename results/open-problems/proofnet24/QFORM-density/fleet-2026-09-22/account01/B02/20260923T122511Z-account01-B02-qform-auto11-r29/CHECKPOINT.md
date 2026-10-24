# account01/B02 r29 — early substantive checkpoint

Target: integrated Fourier estimate for the full QFORM programme. Full conjecture remains open.

Fresh input actually used: the collective-tail marginal certificate from `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/PEER_TAIL_EXTENSION.md`, together with account02/B02's current audit of the q-dependent sharp Hausdorff--Young three-volume theorem in `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T110948Z-account02-B02-QFORM-r11/REPORT.md`.

Let `M` be an ORIGINAL-coordinate physical cross block, `s1>=s2>=...` its singular values, `T2=sum_{j>=3}s_j^2>0`, and `P` any row-space orthogonal projection. Put

`h=max_i P_ii`, `beta=sqrt(3)||P_perp M||op/sqrt(T2)`.

The cited tail certificate gives for every third-volume row marginal

`sqrt(alpha_i)<=sqrt(P_ii)+beta sqrt(1-P_ii)`.

Define the exact scalar envelope

`A(h,beta)=max_{0<=u<=h}(sqrt(u)+beta sqrt(1-u))^2`.

If `A(h,beta)<3/4`, then with `q=max(1,2A(h,beta))<3/2`, the audited fractional-volume theorem applies directly to the ACTUAL cross block and yields

`int_R |phi_Q(t)| dt <= 2pi * [3e/((3-2q)sqrt(q))] * E3(M)^(-1/6)`

`<= 2pi * [3e/((3-2q)sqrt(q))] * [s1^2 s2^2 T2]^(-1/6)`.

This is a genuine unweighted `L1_t` bound, retaining all self blocks/outside couplings. No pointwise scalar decay or post-rotation independence is used.

Useful closed form: if `h<1/(1+beta^2)` then

`A(h,beta)=(sqrt(h)+beta sqrt(1-h))^2`;

otherwise `A(h,beta)=1+beta^2`, so the Fourier gate cannot hold. The sharp choice of q is the smallest admissible q because the constant is increasing for q>=1.

Next in this same run: write the full proof, include the transpose/min(row,column) version, derive an explicit high-leverage failure threshold and state exactly what remains for the full theorem.
