# B16 handoff — clone-pair physical resolvent transfer

**Full FEI remains OPEN / NOT PROVED.** Execution: `WITHOUT_VERIFIED_BRAIN`. No novelty claim.

The central parity-current bank now has a direct no-reuse physical transfer for its authentic dummy slice pairs.

Let an ordered-min parent be the codimension-`c>=2` one-subcube defect `g=1-2 1_A`. After one dummy split write
`g=h_0h_1`, where `h_b` is negative exactly on `A x {b}`. For any Boolean background phase `H` and physical plaquette frustration `P_H(u,v)`, define
\[
\mathfrak D P_H=P_H+P_{Hg}-P_{Hh_0}-P_{Hh_1}.
\]
Then exactly
\[
\mathfrak D P_H
=-\frac12 E\,Q_H(1-Q_{h_0})(1-Q_{h_1}),
\]
so
\[
|\mathfrak D P_H|
\le2\Pr(Q_{h_0}=Q_{h_1}=-1).
\]
The bound is uniform in `H`, hence all other syndrome masks may be conditioned on for free.

For independent physical product-noise translations `U_s,V_t`, `s,t<=1/2`, the slice geometry gives
\[
E\Pr(Q_{h_0}=Q_{h_1}=-1)
\le2st(1-st)J(g),
\]
and therefore
\[
\boxed{
E|\mathfrak D P_H(U_s,V_t)|
\le4st(1-st)J(g).
}
\]
The double inverse-noise singularity is consequently integrable with the explicit constant
\[
\boxed{
\int_0^{1/2}\!\int_0^{1/2}
\frac{E|\mathfrak D P_H(U_s,V_t)|}{st}\,ds\,dt
\le\frac{15}{16}J(g).
}
\]

Combining this atom-by-atom with the existing positive central current parent masses `mu_j`,
\[
\sum_j\mu_jJ(g_j)\le E_{cen}\le\frac{11}{192}W,
\]
gives for the **pure plaquette mask-translation surcharge**
\[
\boxed{
T_{cen}^{pair/plaq}
\le\frac{15}{16}\sum_j\mu_jJ(g_j)
\le\frac{55}{1024}W.
}
\]
This does not spend the terminal mixed difference, R16/moment refunds, negative entropy credits or dual-code multiplicity, and it does not prove FEI.

There is a sharp structural warning at codimension one. If the parent is a character (`c=1`), then projectively `J(g)=0`, but its two dummy slices can have `|mathfrak D P|=2` on the old-coordinate/dummy-coordinate square. Thus the parent-only transfer is impossible at `c=1`; the authentic ordered-min relation family avoids this because its displacement is `e_i+w` with `w!=0`, hence `c>=2`.

**Next attack:** keep the terminal mixed difference inside the same clone-pair correlation derivative. Either derive an analogue of the simultaneous-slice support identity for the full plaquette-plus-terminal atom, or isolate the exact remainder that the retained terminal-band ledger must pay.
