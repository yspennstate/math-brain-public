# Exact one-step calibration and its discontinuity at zero learning rate

Parent derivation, 23 October 2026. This supplements A26's categorical random-ReLU-feature model. It retains that model's categorical inputs, frozen axis-aligned features, single-index teacher, summed-loss GD scaling, and proportional-limit interpretation. It is not a Gaussian-input result, a generic neural-network claim, or a novelty certificate.

Write `alpha=n/(2d)` and `gamma=width/(2d)` for their positive limits, let `p in (1/2,1)`, and set `delta=p-1/2`. Conditional on the positive teacher type, let successes and failures be independent Poisson variables of means `alpha p` and `alpha(1-p)`. Put `K=successes-failures`. Independently, `M` is Poisson with mean `gamma`.

One discrete GD step at summed-loss learning rate `c>0` has

\[
R=MK,\qquad z_1=cR/2,\qquad q_1=\sigma(cR/2).
\]

## 1. An explicit calibration curve using finite divisor sums

For every integer `k`, define the absolutely convergent Poisson-convolution series

\[
A_k(\alpha,p)=e^{-\alpha}
\sum_{j\ge\max(0,-k)}
\frac{(\alpha p)^{j+k}(\alpha(1-p))^j}{(j+k)!j!}.
\]

It is the probability that `K=k` under the positive teacher. Directly exchanging success and failure shows

\[
A_{-k}(\alpha,p)=A_k(\alpha,1-p),\qquad
\frac{A_k(\alpha,p)}{A_k(\alpha,1-p)}
=\left(\frac{p}{1-p}\right)^k.
\tag{1}
\]

For a nonzero integer `r`, define a **finite** sum over the positive divisors of `|r|`:

\[
u_+(r)=\sum_{m\mid |r|,\,m\ge1}
 e^{-\gamma}\frac{\gamma^m}{m!} A_{r/m}(\alpha,p),
\qquad
u_-(r)=u_+(-r).
\tag{2}
\]

The score `q_r= sigma(cr/2)` identifies `r` uniquely for every `c>0`. Its mass and true conditional success probability are therefore

\[
\mu_r=\frac{u_+(r)+u_-(r)}2,\qquad
g_r=\frac{p u_+(r)+(1-p)u_-(r)}{u_+(r)+u_-(r)}.
\tag{3}
\]

At `r=0`, the mass is

\[
\mu_0=e^{-\gamma}+(1-e^{-\gamma})A_0(\alpha,p),
\qquad g_0=q_0=1/2.
\]

Equation (1) implies `u_+(r)>u_-(r)` and hence `g_r>1/2` for every positive `r`. Also `g_{-r}=1-g_r` and `mu_{-r}=mu_r`. Thus the population unbinned calibration error has the exact representation

\[
\mathrm{CE}_1(c)=2\sum_{r\ge1}\mu_r
\left|g_r-\sigma(cr/2)\right|.                 \tag{4}
\]

These equations explicitly separate the dependence on sample ratio, width ratio, and learning rate. The calibration curve at the indexed atoms `r` is independent of the positive rate `c`; the reported score values change with `c`.

## 2. Arbitrarily small positive steps do not approach zero unbinned calibration error

Since the summands in (4) are bounded by their masses, dominated convergence gives

\[
\begin{aligned}
L_0&:=\lim_{c\downarrow0}\mathrm{CE}_1(c)\\
&=\delta(1-e^{-\gamma})
 \left[\Pr(K>0\mid H=+)-\Pr(K<0\mid H=+)\right]>0.
\end{aligned}                                             \tag{5}
\]

To verify the equality, write `2 mu_r(g_r-1/2)=delta[u_+(r)-u_-(r)]`, sum over positive `r`, and use that multiplication by a positive `M` preserves the sign of `K`. Strict positivity follows term by term from (1). In particular, the `k=1` pair already gives

\[
L_0\ge 2\alpha\delta^2 e^{-\alpha}(1-e^{-\gamma})>0,       \tag{6}
\]

because the first term of `A_1-A_{-1}` is `alpha(2p-1)e^{-alpha}` and all its remaining terms are positive.

At exactly `c=0`, all scores coincide at `1/2`, the two teacher types have equal mass, and the true conditional success probability is `1/2`. Hence

\[
\mathrm{CE}_1(0)=0\ne\lim_{c\downarrow0}\mathrm{CE}_1(c).
\tag{7}
\]

This is a discontinuity of **unbinned population calibration**, not a contradiction to convergence of the predicted probabilities. For every positive `c`, arbitrarily close score values still reveal the integer statistic `R`; at zero they collapse into a single atom. No claim is made about fixed-width calibration bins or rounded machine outputs.

## 3. Explicit nonzero calibration floor in an informative risk-improvement regime

The sigmoid is `1/4`-Lipschitz, and `E|R|=gamma E|K|<=gamma alpha`. Comparing each absolute value in (4) with its zero-rate limiting value yields

\[
\left|\mathrm{CE}_1(c)-L_0\right|
\le E|\sigma(cR/2)-1/2|
\le c\alpha\gamma/8.                                  \tag{8}
\]

Therefore, whenever

\[
0<c\le\frac{8\delta^2e^{-\alpha}(1-e^{-\gamma})}{\gamma},
\]

we have the explicit floor

\[
\mathrm{CE}_1(c)\ge
\alpha\delta^2e^{-\alpha}(1-e^{-\gamma})>0.               \tag{9}
\]

Independently, A26's direct logistic Taylor bound proves risk improvement for

\[
0<c\le\frac{4\alpha\gamma\delta^2}
{(\gamma^2+\gamma)(\alpha/4+\alpha^2\delta^2)}.
\]

The minimum of these two positive upper bounds is a nonempty regime in which one genuine GD step improves population log-loss and yet has calibration error bounded away from zero by (9). This is stronger than inferring calibration from small changes in the scores, and it requires no identification of training time with a ridge penalty.

For the pure-noise teacher `p=1/2`, the distinction disappears: `g_r=1/2` and `CE_1(c)<=c alpha gamma/8 ->0`. The informative-teacher restriction in (5)–(9) is essential.

## Review boundary

The proof uses elementary conditioning, exact Poisson-convolution identities, and dominated convergence. A26's total-variation occupancy theorem supplies the connection to the finite-dimensional networks for each fixed positive `c`. This note does not interchange a changing-rate `c_d` limit with conditional calibration in finite dimensions. Independent review is requested before promoting these formulas to accepted campaign claims.
