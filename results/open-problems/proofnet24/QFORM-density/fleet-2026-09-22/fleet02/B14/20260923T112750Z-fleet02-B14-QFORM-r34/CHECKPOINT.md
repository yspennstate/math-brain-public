# fleet02/B14 r34 early checkpoint — arbitrary-self random-slope mass restoration

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

First unpaid implication attacked: remove the exact zero-self requirement from the whole-bank random-slope branch without treating a small self coefficient as a small random perturbation.

## Provisional theorem (proof complete modulo transcription audit)

Let `X` be an original-coordinate probability variable with density at most one. Let `nu(dv)` be a positive bank submeasure of mass `m>0`, independent of `X`. Let `S(v),R(v)` be arbitrary measurable real functions, and assume the pushforward `S_#nu` has a density bounded by `L`. Put `H=L/m`. For arbitrary `h,t` define

`Y=h X^2 + X S(V)+R(V)`.

Then for every `rho>0`,

`nu_Y{|Y-t|<rho} <= m sqrt(G(4H rho))`,

where

`G(q)=2q(1+log(1/(2q)))` for `0<q<=1/2`, and `G(q)=1` for `q>=1/2`.

Proof: write the left side as `int p(v) nu(dv)` and use Cauchy-Schwarz. With independent copies `X,X'`, two simultaneous hits of the same interval imply

`|(X-X')[h(X+X')+S(v)]|<2rho`.

The arbitrary correlated remainder `R(v)` cancels. For fixed `X,X'`, the slope lies in an interval of length `4rho/|X-X'|`, so the bank submeasure contributes at most `min(m,4Lrho/|X-X'|)`. Since `X-X'` has a probability density bounded by one,

`E min(1,q/|X-X'|) <= G(q)`

by layer cake: for `2q<1`, integrate `min(1,2q/u)` over `u in (0,1)`; for `2q>=1` use one. This proves the claim with no support, moment, fragment, or translation hypothesis and no bathtub-attainment assumption.

Consequently the translated logarithmic potential satisfies

`int log_+(A/|t-y|) dnu_Y(y) <= m J(4HA)`,

`J(q)=int_0^infinity sqrt(G(q e^{-v})) dv`.

At `q=1`,

`J(1)=log 2 + C0`,
`C0=2+sqrt(2 pi e) erfc(1/sqrt(2)) = 3.3113590848...`,

so `J(1)=4.0045062654...`.

After an outer original-coordinate invertible indefinite pair with `D=|det C|`, `kappa=sigma_min(C)`, the existing pair-log envelope therefore gives the subprobability bound

`||p_Q^sub||_inf <= 8 sqrt(mL/kappa) + J(1) m/sqrt(D)`.

Hence any positive bank decomposition with `L_j<=H0 m_j` transfers the same constant exactly after summation: the full power of every unnormalized piece mass survives despite arbitrary hub self-curvature `h`.

## Immediate structural use

For an actual three-coordinate block written `(P,i)` with an invertible indefinite original-coordinate pair `C=A[P,P]`, write

`B=[[C,b],[b^T,d]]`, `h=d-b^T C^{-1}b`,

and for outside couplings `[[C,b,F],[b^T,d,g^T],[F^T,g,E]]` define

`a=g-F^T C^{-1}b`.

Exact pair completion leaves

`h X_i^2 + X_i[beta+2a^T V]+R(V)`.

Thus the theorem applies for every `h`, not only the exact-rank-two endpoint `h=0`. At `h=0`, the newest fleet03/B14 r33 identity identifies `a` with its collective kernel-leakage vector divided by the retained kernel coordinate, so the new result is a genuine arbitrary-self continuation of that completed partner branch rather than a rotated-independence argument.

Next: source the slope cap directly from the required Claude `L^p` lemma, record the full Schur-direction inequality and a target-valid diffuse-leakage family showing fixed-coordinate selection still loses when `h` is small but nonzero.
