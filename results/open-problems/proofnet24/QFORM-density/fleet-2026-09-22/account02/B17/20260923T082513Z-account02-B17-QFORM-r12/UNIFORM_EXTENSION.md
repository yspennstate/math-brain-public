# Uniform extension — the `o(1)` is universal over the entire strong `3 x 3` core

The main report stated the transfer for fixed `B`. The same proof in fact gives a stronger statement with no extra work.

Let `B_m=B_m^T` be **arbitrary and allowed to vary with `m`**, subject only to

` s_3(B_m)>=1 `.

Then `|det B_m|>=1`. Consequently the Fresnel--Brascamp--Lieb envelope used in (3.4) is bounded uniformly over all such matrices by

`g_F(t)=min(1,(4*pi)^(3/2)|t|^(-3/2))`.

Likewise, after diagonalising `B_m`, every eigenvalue has modulus at least one, so the translated Gaussian envelope used in (5.3) is bounded uniformly by

`g_G(t)=(1+t^2/36)^(-3/4)`.

Both `g_F` and `g_G` are integrable. On the other hand, for the product densities `H_m=h_m^(tensor 3)` and `Gamma=gamma^(tensor 3)`, the modulus-one comparison is independent of the phase:

`sup_{B:s_3(B)>=1} sup_z |phi_{m,B,z}(t)-phi_{infty,B,z}(t)| <= eta_m := ||H_m-Gamma||_1 ->0`.

Therefore dominated convergence gives the **universal** transfer error

`Delta_m := (1/(2*pi)) int sup_{B:s_3(B)>=1} sup_z |phi_{m,B,z}(t)-phi_{infty,B,z}(t)| dt ->0`.

By Fourier inversion and the completed account03/B17 affine-Gaussian theorem,

`sup_{B:s_3(B)>=1} sup_z ||p_{(S_m+z)^T B(S_m+z)}||_infinity <= 3*sqrt(2)+Delta_m`.

After mixing over arbitrary independent translations `Z_i`, the same bound holds for

`A_m=P_m B_m P_m^T`, `X_i=U_i+Z_i`.

Thus the main theorem can be strengthened to:

**Uniform theorem.** There is one deterministic sequence `Delta_m->0`, depending only on the normalized-unit-interval bank size `m`, such that for every symmetric `3 x 3` matrix `B_m` with `s_3(B_m)>=1` and every choice of independent translation laws (with no moments/support restrictions),

`||p_{X^T P_m B_m P_m^T X}||_infinity <= 3*sqrt(2)+Delta_m`.

For the canonical spectrum `{1,1,-1}`, centered translations show sharpness of the limit. Hence even varying spectral magnitudes/orientations cannot rescue the unit-smoothed fragmented diffuse-bank mechanism.
