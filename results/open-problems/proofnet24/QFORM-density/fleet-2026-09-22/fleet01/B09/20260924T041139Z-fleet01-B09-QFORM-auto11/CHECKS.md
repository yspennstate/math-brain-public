# CHECKS — fleet01/B09 — 20260924T041139Z

Target remains the full QFORM bounded-density conjecture. This file checks only the new singular-pair collision/exclusion calculation and the concrete partner application.

## Algebraic frame checks

Let `u` be a unit vector in the leaf space, `P=I-uu^T`, and let `E=E^T=PEP`, so `Eu=0`. For every unordered leaf edge `I={i,j}`, set

`v_ij = u_j e_i - u_i e_j`.

Then

`sum_I v_I v_I^T = P`.

Consequently

`sum_I ||E v_I||^2 = tr(E^2 P)=||E||_F^2`

and

`sum_{I,J} (v_I^T E v_J)^2 = ||E||_F^2`.

For a fixed coordinate `i`, define

`S_i = sum_{J: i in J} v_J v_J^T`.

For every `x perpendicular to u`, direct expansion gives the exact identity

`x^T S_i x = x_i^2 + u_i^2 ||x||^2`.

Hence, for `I={i,j}` and `x=Ev_I`,

`sum_{J: J intersect I != empty} (v_I^T E v_J)^2 <= x^T(S_i+S_j)x`

`= x_i^2+x_j^2+(u_i^2+u_j^2)||x||^2`.

The component term also has an exact summed form. For fixed `i`, using `Eu=0`,

`sum_{j!=i} (E v_ij)_i^2 = sum_j (u_j E_ii-u_i E_ij)^2`

`= E_ii^2 + u_i^2 sum_j E_ij^2`.

Writing `R_i=sum_j E_ij^2` and `q=max_i u_i^2`, summing over edges yields

`sum_I [(Ev_I)_i^2+(Ev_I)_j^2] = ||diag(E)||_2^2 + sum_i u_i^2 R_i`

`<= ||diag(E)||_2^2 + q ||E||_F^2`.

Also

`sum_I (u_i^2+u_j^2)||Ev_I||^2 <= 2q ||E||_F^2`.

Therefore the ordered intersecting-edge-pair mass obeys

`C_cap := sum_{I,J: I intersect J != empty} (v_I^T E v_J)^2 <= ||diag(E)||_2^2 + 3q ||E||_F^2`.

Subtracting from the total frame mass proves

`D_dis := sum_{I,J: I intersect J = empty} (v_I^T E v_J)^2 >= (1-3q)||E||_F^2 - ||diag(E)||_2^2`.

No dimension-dependent factor occurs.

## Mapping grouped kernel-hub minors back to literal physical coordinates

In the exact singular-pair/rank-one-cross chamber of the preceding B09 run, in the algebraic pair basis `(ell,k)`, the grouped kernel-hub third minor for disjoint leaf edges is

`M_{I,J} = det A[{k} union I, {k} union J] = -s^2 v_I^T E v_J`.

For fixed disjoint `I,J`, form the literal physical-hub `2x2` coefficient matrix

`C_{I,J}(a,b)=det A[{h_a} union I, {h_b} union J]`, `a,b in {1,2}`.

Changing only the deterministic two-dimensional hub basis sends `C_{I,J}` to `O^T C_{I,J} O`, so its Frobenius norm is invariant. The `(k,k)` grouped entry is `M_{I,J}`. Therefore

`sum_{a,b}|C_{I,J}(a,b)|^2 >= |M_{I,J}|^2`.

For disjoint `I,J`, the physical terms with `a=b` are overlap-one third minors and the terms with `a!=b` are disjoint overlap-zero third minors. Thus, with

`T := s^4 D_dis`,

we have the literal physical lower bound

`Omega_0 + Omega_1 >= T`.

More sharply, let `S_off` be the `a!=b` part and `S_diag` the `a=b` part of this selected mass. Since `S_off+S_diag>=T`, either:

1. `S_off>=T/2`. One of the two hub orientations has mass at least `T/4`. Independently half-coloring the leaves captures any ordered disjoint edge pair in that orientation with probability `1/16`, so some literal disjoint coordinate cut has third cross-volume `Z_3>=T/64`; or
2. `S_diag>T/2`, so one of the two literal physical hubs carries overlap-one disjoint-leaf mass greater than `T/4`.

This uses only original-coordinate partitions in the probabilistic receiver step.

## Quantitative collar constants

In the preceding unpaid exact singular-pair collar we already have

`q<1/16`, `s>2`, `||E||_F>7/8`.

If additionally

`||diag(E)||_2^2 <= (1/4)||E||_F^2`,

then

`T > 16*(1-3/16-1/4)*(49/64) = 441/64 = 6.890625`.

Hence the disjoint-cut branch has

`Z_3 > (441/64)/64 = 441/4096 = 0.107666015625`.

Using the completed no-marginal D3 constant

`C3 = 3*2^(4/3)*e^(1/3) = 10.550168831164775`,

the direct continuous-density bound is

`||p_Q||_infinity <= C3 Z_3^(-1/6) < 2*C3*(441/64)^(-1/6) = 15.296062025167252`.

If the global instance is still outside the already-paid `Omega_0>=1/4` branch, then `S_off<1/4`; consequently

`S_diag > T-1/4 > 425/64`,

so one of the two literal hubs carries overlap-one disjoint-leaf mass

`> 425/128 = 3.3203125`.

If the low-diagonal condition fails, then the remaining explicit resource is

`||diag(E)||_2^2 > (1/4)||E||_F^2 > 49/256 = 0.19140625`.

## Designated partner theorem applied to an actual target inequality

Use fleet02/B09's completed square-hyperbola theorem from its r15 handoff:

`||p_{aU^2+2bVW}||_infinity <= 3*2^(2/3) M^(2/3) S^(2/3)|a|^(-1/3)|b|^(-2/3)`,

for `(U,V)` of joint density cap `M` and independent `W` of density cap `S`.

Take independent cap-one `X_1,X_2,X_3` and

`Q=3X_1^2+8X_2X_3`.

Here `(U,V)=(X_1,X_2)`, `W=X_3`, `M=S=1`, `a=3`, `b=4`. The symmetric matrix is

`diag(3, [[0,4],[4,0]])`,

with spectrum `{3,4,-4}`, so the exact owner hypothesis holds. The partner theorem gives

`||p_Q||_infinity <= (3/2)^(2/3) = 1.3103706971044482`,

and the same coefficient multiplying every interval length. Continuity is not inferred from this partner interface.

## Scope audit

The new theorem does not prove the full conjecture. It pays the low-transverse-diagonal branch either by a genuine literal disjoint D3 receiver or localizes a macroscopic overlap-one packet onto one of the two original physical hubs. The remaining branch has explicit aggregate transverse diagonal energy `>49/256`; paying that resource is the next mathematical debt. No random-variable rotation, pointwise law-uniform quadratic van der Corput estimate, arbitrary-joint coarea step, small-random-error deletion, or square-root final small-ball conversion is used.
