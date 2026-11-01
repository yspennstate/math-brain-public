# Local-limit addendum for the positive-heavy K0 theorem

This addendum supplies the uniform density convergence used in Section 6 of `REPORT.md` without appealing to a generic arbitrary-density stationary-phase estimate.

Let `f` be an even density nonincreasing on `[0,infinity)` and put `M=f(0)=||f||_infinity`.  By layer cake there are radii `r(s)` such that

`f(x)=integral_0^M 1_{|x|<=r(s)} ds`.

Hence, for `t!=0`,

`psi_f(t):=integral_R exp(i t x^2) f(x) dx
 = integral_0^M [integral_{-r(s)}^{r(s)} exp(i t x^2) dx] ds`.

The Fresnel partial integrals are uniformly bounded after the scaling `u=sqrt(|t|)x`, so for one absolute constant `C_F`,

`|psi_f(t)| <= C_F M |t|^(-1/2)`,

while trivially `|psi_f(t)|<=1`.  This is a BV/symmetric-unimodal estimate for the explicit bank laws; it is **not** the refuted law-uniform pointwise estimate over arbitrary cap-one densities.

For the finite family in `REPORT.md`, all three spectral aggregates have even decreasing densities.  The heavy-bank density is fixed, so its supremum `M_a` is finite.  For

`Y_m=m^(-1/2) sum_{k=1}^m U_k`, `U_k~Unif[-1/2,1/2]`,

Ball's cube-slicing bound gives `||p_{Y_m}||_infinity<=sqrt(2)` uniformly in `m` (and the same uniform boundedness also follows directly from the explicit Irwin--Hall formula).  Consequently the characteristic function of

`Q_m=Y_1^2+Y_{2,m}^2-Y_{3,m}^2`

obeys the integrable envelope

`|phi_Qm(t)| <= C_a min(1,|t|^(-3/2))`,

uniformly in `m`.

The classical CLT gives `Y_{2,m},Y_{3,m} => N(0,1/12)`, so for each fixed `t`,

`phi_Qm(t) -> phi_Qinfty(t)`.

Dominated convergence in `L^1(dt)` and Fourier inversion therefore yield the stronger uniform local limit

`||p_Qm-p_Qinfty||_infinity -> 0`.

In particular,

`||p_Qm||_infinity=p_Qm(0) -> p_Qinfty(0)=||p_Qinfty||_infinity`

because the completed fleet02/B17 symmetric-unimodal theorem puts the global mode at zero for every finite `m` and in the limit.

This proves the finite-source transfer claimed in Section 6 with a correction-safe, explicit `|t|^{-3/2}` envelope tied to the symmetric-unimodal bank structure.
