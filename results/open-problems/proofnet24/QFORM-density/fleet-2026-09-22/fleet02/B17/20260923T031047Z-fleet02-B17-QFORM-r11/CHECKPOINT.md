# B17 checkpoint — exact finite heavy-law reduction

Run `20260923T031047Z-fleet02-B17-QFORM-r11`. Full QFORM remains OPEN.

For the exact source-valid family
\[
A_m=\operatorname{diag}(1,J_m/m,-J_m/m),\qquad
Q_{m,f}=X_f^2+S_m^2-T_m^2,
\]
where `f<=1`, `int f=1` is arbitrary and the two banks are normalized sums of independent centered unit intervals, every finite matrix has nonzero spectrum exactly `{1,1,-1}`.

Let `h_m` be the density of `S_m`. It is even and nonincreasing on `[0,infinity)` (induction under convolution with an interval). Hence the square density
\[
a_m(u)=h_m(\sqrt u)/\sqrt u\quad(u>0)
\]
is decreasing. Therefore the iid difference-square kernel
\[
k_m(w)=p_{S_m^2-T_m^2}(w)
\]
is even and nonincreasing in `|w|`, because for `w>=0`,
\[
k_m(w)=\int_0^\infty a_m(u)a_m(u+w)\,du.
\]

For fixed output `s`, maximizing
\[
\int f(x)k_m(s-x^2)\,dx
\]
over the entire cap-one class is an exact bathtub problem. Since `k_m` decreases with `|s-x^2|`, the optimizer is the measure-one set closest to the level `x^2=s`: centered `[-1/2,1/2]` for `s<=1/8`, and for `s>=1/8` the two-shell set `[-a,-b] union [b,a]` with `a-b=1/2`, `a^2+b^2=2s`.

For `s>=1/8`, the distance `R_s=|x^2-s|` on that measure-one shell is stochastically increasing in `s`: for `0<=r<1/8`,
\[
|\{|x^2-s|\le r\}|=2(\sqrt{s+r}-\sqrt{s-r})
\]
has negative `s` derivative, while at `s=1/8` all shell distances are at most `1/8`. Thus the optimized value for every `s>=1/8` is at most its value at `s=1/8`.

Combining this with the already completed separated symmetric-unimodal mode-zero theorem for the centered heavy interval gives the exact finite reduction
\[
\boxed{
\sup_{0\le f\le1,\int f=1}\|p_{Q_{m,f}}\|_\infty
= p_{U^2+S_m^2-T_m^2}(0),\qquad U\sim\mathrm{Unif}[-1/2,1/2].
}
\]
Equality is attained by the centered unit interval at output zero. Hence fragmentation/translation of the one heavy majority-sign law can never improve this finite family at any bank size. The only remaining sharp-constant question inside this family is the scalar sequence on the right.
