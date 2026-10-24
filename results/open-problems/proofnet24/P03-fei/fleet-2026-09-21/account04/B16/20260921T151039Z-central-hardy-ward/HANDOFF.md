# B16 central Hardy/Ward handoff

Status: **PARTIAL PROGRESS / FULL FEI OPEN / WITHOUT_VERIFIED_BRAIN**.

The low radial Hardy half now has two exact interfaces. The older one is the parity-safe R16 collision representation

\[
\mathcal L_-=
\sum_{j\ge6,\ j\text{ even}}
\frac{\Gamma_j}{(j-1)2^{j-1}}.
\]

The new one is the compiler-facing Ward representation. With

\[
\mathcal P_{uv}=\kappa_{g_S}(g_u,g_v)+\Delta_{uv}R_d(g_S),
\]

\[
A_v(t)=\sum_{u\ne v}
\left[
\mathbb E_{(1-t)/2}\mathcal P_{uv}
-
\mathbb E_{(1+t)/2}\mathcal P_{uv}
\right],
\]

one has exactly

\[
\boxed{
\mathcal L_-
=
\frac{N^2}{1024}
\sum_v\int_0^{1/2}
\left[
\frac1t\int_0^t sA_v(s)ds
\right]^2dt.
}
\]

Also

\[
\boxed{
\mathcal L_-
\le
\frac{N^2}{2048}
\sum_v\int_0^{1/2}
 t(1/2-t)A_v(t)^2dt.
}
\]

Hence this low radial demand samples only two-sided Bernoulli prefixes in `[1/4,3/4]` and keeps the terminal mixed difference inside the same signed field.

The newest account03 Pasch packet is a pure packetwise internal-chaos obstruction: its signed vertex marginals vanish, so its radial bank is zero while its internal bank is `4/5` abstractly and `1/80` after the `1/8` Borel scaling. Per account03 erratum `93e230d639665d10a5954f731ee04e4f3c7db33c`, simultaneous survival of all eight packet relations through a particular `D_d` prefix is unverified; do not promote it to a retained-prefix counterexample.

**Next mathematical target:** prove or refute a dimension-free bound for the central-band plaquette divergence above from the original-coordinate q-flip Radon/Fourier field and the signed fractional noisy-square bank. Do not replace the divergence square by an unsigned pairwise sum and do not split the terminal term by triangle inequality. If this source divergence estimate fails on admissible Boolean data, return to the exact R16 collision interface rather than a killed generic absolute-value route.
