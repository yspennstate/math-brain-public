# Early checkpoint: rough one-sheet trace + heat split

Run `20260923T022111Z-fleet02-B15-QFORM-auto11`.

Target remains OPEN.  I am checking the rough-input ruled estimate and applying the completed fleet03/B15 countable Gaussian heat certificate.

For an exact rank-three indefinite form
\[
S=\lambda_1Y_1^2+\lambda_2Y_2^2-\mu Y_3^2,\qquad \lambda_1,\lambda_2,\mu\ge1,
\]
where `Y=R^T X` and the original `X_i` are independent with densities at most one, the positive (one-sheet) submeasure has density
\[
p_+(s)\le C_+(\lambda_1,\lambda_2,\mu)
=(\lambda_1\lambda_2\mu)^{-1/2}\int_0^{2\pi}
\frac{d\theta}{\sqrt{\sin^2\theta/\lambda_1+\cos^2\theta/\lambda_2+1/\mu}}
\le\pi\sqrt2,
\quad s>0.
\]
The rough-input justification can be done directly by coarea for the `L^1` projected density: in scaled spectral coordinates the one-sheet parametrisation
\[
F_s(\theta,t)=\sqrt{s}\,e_\theta+t(e_\theta^\perp+e_3)
\]
has `dH^2/|grad q|=(1/2)dtheta dt`.  The `t`-line in unscaled `Y` coordinates has direction
\[
w_\theta=(-\sin\theta/\sqrt{\lambda_1},\cos\theta/\sqrt{\lambda_2},1/\sqrt\mu),
\]
so its parameter integral is `|w_theta|^{-1}` times a line integral of the 3D projection density.  That line integral is a 2D orthogonal projection density of the original cap-one product law and is at most `2`.  Therefore the displayed `C_+` bound holds a.e.  No output continuity is used.  Gaussian padding in the ORIGINAL coordinates gives an independent fallback: product `L^1` convergence implies total-variation convergence of the quadratic pushforwards, so the interval inequality passes to rough inputs.

Applying the completed fleet03/B15 heat certificate at commit `8e22652e1fd8dc943b5744309bdadfe8674471c7`, for every heat scale and center,
\[
E\,\gamma_\varepsilon(S-y)
\le \pi\sqrt2 + E[\gamma_\varepsilon(S-y)1_{\{S<0\}}].
\]
Thus the exact-rank-three indefinite height problem reduces, up to the paid additive constant `pi sqrt(2)`, to the minority/two-sheet positive heat functional.  Since the minority measure is supported on `(-infinity,0)`, its heat convolution is nonincreasing in the center for `y>=0`; hence only centers `y<=0` are unpaid.  Combining with the partner lattice `(epsilon_k,y_{k,m})=(2^{-k},m2^{-3k})`, the remaining exact-rank-three implication is the uniform bound
\[
\sup_{k\ge1,\,m\le0}E[\gamma_{2^{-k}}(S-m2^{-3k})1_{\{S<0\}}]<\infty.
\]
This is a rough-law, positivity-preserving two-sheet trace problem, not a continuity problem.
