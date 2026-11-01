# Two-bank Fourier control and a uniform negative strip

**Status.** Proved analytic receiver for the canonical one-hub form in a central negative strip, conditional on a quantitative two-bank decomposition of the light law. It does **not** close the unrestricted negative target interval or the full QFORM conjecture.

## Theorem

Let \(H\) have a probability density \(0\le f_H\le1\) and be independent of \(Z=(L,V,P)\). Suppose \(Z=Z_A+Z_B\), where the two 3D banks are independent and their laws have joint densities \(g_A,g_B\) satisfying
\[
 \|g_j\|_\infty\le M_{3,j},\qquad
 \|p_{(L_j,V_j)}\|_\infty\le M_{2,j}\quad(j=A,B).
\]
Set \(M_2=\sqrt{M_{2,A}M_{2,B}}\) and \(M_3=\sqrt{M_{3,A}M_{3,B}}\). Suppose also that every 2D orthogonal projection of the full light \(Z\) has density cap \(K\). For
\[
 Q_\varepsilon=2HL+\beta L^2+V^2+2\varepsilon LP,\qquad \varepsilon\ne0,
\]
the contribution \(D_\varepsilon(s)\) to its density from \(|L|<1\) has a continuous version satisfying, for all real \(s,t\),
\[
 |D_\varepsilon(s)-D_\varepsilon(t)|
 \le C\sqrt{\frac{|s-t|}{|\varepsilon|}}\sqrt{M_2M_3}. \tag{1}
\]
Here \(C\) is a universal numerical constant independent of \(\beta,\varepsilon,s,t\), the supports, and the hub law. The contribution from \(|L|\ge1\) has density at most \(1/2\). By the nonnegative ruled-line receiver, \(D_\varepsilon(0)\le 1/2+4\sqrt2K\) (and in fact the outer contribution can be subtracted if desired). Thus
\[
 \operatorname*{ess\,sup}_{-|\,\varepsilon\,|\le s\le0}p_{Q_\varepsilon}(s)
 \le 1+4\sqrt2K+C\sqrt{M_2M_3}. \tag{2}
\]
For a genuine orthonormal product projection of independent cap-one originals, \(K\le2\); if the frame admits a two-bank split with fixed bank caps, (2) is uniform in the leakage coefficient and closes the strip \(-|\varepsilon|\le s\le0\).

A companion bound valid at every target is
\[
 \|p_{Q_\varepsilon}\|_\infty
 \le\frac12+C\left[M_2\left(1+\sqrt{\log_+\frac1{|\varepsilon|}}\right)
                         +\sqrt{M_2M_3}\right]. \tag{3}
\]
The logarithmic loss in (3) is a limitation of this absolute-Fourier argument, not evidence for a counterexample.

## Bank Fourier norms

Use the convention \(\widehat u(\xi)=\int e^{-i\xi\cdot x}u(x)\,dx\). For a fixed frequency \(\zeta\) dual to \(P\), let
\[
 S(\zeta)=\int_{\mathbb R^2}
   |\widehat g_A(\xi_L,\xi_V,\zeta)
    \widehat g_B(\xi_L,\xi_V,\zeta)|\,d\xi_Ld\xi_V .
\]
Partial Fourier inversion in \(P\) gives
\[
 \left|\int g_j(l,v,p)e^{-i\zeta p}\,dp\right|
       \le p_{(L_j,V_j)}(l,v).
\]
The left-hand function has \(L^2(\mathbb R^2)\) norm at most \(\sqrt{M_{2,j}}\), because its modulus is at most the corresponding probability density, whose \(L^2\) norm squared is at most its \(L^\infty\) cap. Two-dimensional Plancherel and Cauchy--Schwarz therefore show
\[
 \sup_\zeta S(\zeta)\le(2\pi)^2M_2. \tag{4}
\]
Three-dimensional Plancherel similarly gives
\[
 \int_{\mathbb R}S(\zeta)\,d\zeta
 \le(2\pi)^3M_3,\qquad
 \int S(\zeta)^2d\zeta\le(2\pi)^5M_2M_3. \tag{5}
\]
Finally \(\phi_H=\widehat f_H\) obeys
\(\|\phi_H\|_2^2=2\pi\|f_H\|_2^2\le2\pi\).

## Dyadic kernel and the cancellation at \(s=0\)

For \(r=2^{-j-1}\), \(j\ge0\), restrict to either \(r\le L\le2r\) or \(-2r\le L\le-r\). After integrating the independent hub, the level-\(s\) kernel on that strip is
\[
 W_{s,r}(l,v,p)
 ={\bf1}_{r\le|l|\le2r}\,
   \frac{f_H((s-\beta l^2-v^2-2\varepsilon lp)/(2l))}
        {2|l|}.
\]
Fourier transform first in \(p\). Its factor is
\[
 \frac{\phi_H(\zeta/\varepsilon)}{2|\varepsilon l|}
 \exp\!\left[-\,i\frac{\zeta(s-\beta l^2-v^2)}
                           {2\varepsilon l}\right]
\]
up to complex conjugation/sign, irrelevant to the bound. The Fourier transform in \(v\) is a Fresnel integral of modulus
\(\sqrt{2\pi|\varepsilon l/\zeta|}\). Integrating \(l\) on the dyadic strip and taking absolute values yields, uniformly in the frequencies dual to \(L,V\), in \(s,\beta\), and for \(\zeta\ne0\),
\[
 |\widehat W_{s,r}(\xi_L,\xi_V,\zeta)|
 \le C\sqrt{\frac r{|\varepsilon\zeta|}}\,
       |\phi_H(\zeta/\varepsilon)|. \tag{6}
\]
The only \(s\)-dependence is the phase \(e^{-is\zeta/(2\varepsilon l)}\). Thus
\[
 |\widehat W_{s,r}-\widehat W_{t,r}|
 \le C\sqrt{\frac r{|\varepsilon\zeta|}}\,
       |\phi_H(\zeta/\varepsilon)|
       \min\!\left(2,\frac{|s-t|\,|\zeta|}
                            {|\varepsilon|r}\right). \tag{7}
\]
Pair this with \(\widehat g=\widehat g_A\widehat g_B\), integrate the two \(L,V\) frequencies into \(S(\zeta)\), and substitute \(\zeta=\varepsilon\eta\). Summing the positive and negative \(L\)-strips gives
\[
 |D_\varepsilon(s)-D_\varepsilon(t)|
 \le C\int_\mathbb R
 \frac{S(\varepsilon\eta)|\phi_H(\eta)|}{\sqrt{|\eta|}}
 \sum_{r=2^{-j-1}}\sqrt r\,
 \min\!\left(2,\frac{|s-t|\,|\eta|}{r}\right)d\eta. \tag{8}
\]
The elementary geometric-series bound
\[
 \sum_{r=2^{-j-1}}\sqrt r\min(2,u/r)
 \le C\min(1,\sqrt u)\le C\sqrt u
\]
removes the singular factor \(|\eta|^{-1/2}\) in (8). Cauchy--Schwarz, (5), and Plancherel for \(H\) finish the estimate:
\[
 |D_\varepsilon(s)-D_\varepsilon(t)|
 \le C\sqrt{|s-t|}
       \int S(\varepsilon\eta)|\phi_H(\eta)|\,d\eta
 \le C\sqrt{\frac{|s-t|}{|\varepsilon|}}\sqrt{M_2M_3}.
\]
This proves (1).

For (3), omit the phase difference in (6). After the same dyadic sum the remaining integral is
\(\int S(\varepsilon\eta)|\phi_H(\eta)|/\sqrt{|\eta|}\,d\eta\).
On \(|\eta|\le1\), use (4) and \(|\phi_H|\le1\). For \(1<|\eta|<1/|\varepsilon|\), when this interval exists, use (4) and Cauchy--Schwarz against \(d\eta/|\eta|\), costing \(\sqrt{\log(1/|\varepsilon|)}\). On \(|\eta|\ge\max(1,1/|\varepsilon|)\), use Cauchy--Schwarz, (5), and \(1/|\eta|\le\min(1,|\varepsilon|)\). This gives (3).

## Justification and scope

For smooth rapidly decreasing bank and hub densities, the displayed Fourier manipulations can be justified by inserting \(e^{-\delta v^2}\) in \(W_{s,r}\). Its \(v\)-transform is a complex Gaussian with modulus at most the Fresnel amplitude in (6), uniformly in \(\delta>0\). The phase difference in (7) is unchanged. Fourier inversion is then absolutely valid on each dyadic strip; dominated convergence as \(\delta\downarrow0\) gives the claims. In particular, there is no additional atom at \(\zeta=0\): the singularity \(1/\sqrt{|\zeta|}\) in (6) is locally integrable once paired with the bounded \(S\).

For general densities, truncate each bank and the hub to large balls/intervals, and then Gaussian-mollify. These are subprobability approximations whose \(M_2,M_3\), hub cap, and full-light projection cap \(K\) do not increase. The estimates above hold for them uniformly; their quadratic pushforwards converge weakly to the desired law. The uniform interval bounds pass to the limit, establishing the essential density caps. The common Hölder modulus gives a continuous version of the inner density \(D_\varepsilon\).


## Genuine product diffuse-frame corollary

Let \(X_i\) be independent with probability densities at most one and let the \(3\times n\) light frame \(U\) have orthonormal rows. Write its columns as \(u_i\), and assume
\[
 \rho:=\max_i\|u_i\|^2\le1/24. \tag{9}
\]
There exists a partition of the original coordinates into two independent banks whose \(3\times3\) frame Grams both dominate \(I_3/4\). Indeed, choose independent Rademacher signs \(\sigma_i\). For \(R=\sum_i\sigma_i u_iu_i^T\),
\[
 {\mathbb E}\|R\|_F^2
 =\sum_i\|u_i\|^4
 \le\rho\sum_i\|u_i\|^2
 =3\rho\le1/8.
\]
Some sign choice has \(\|R\|_{\mathrm{op}}\le\|R\|_F\le1/\sqrt8<1/2\). The two bank Grams are \((I_3\pm R)/2\succeq I_3/4\).

Whitening each bank and applying the product-projection inequality gives
\[
 M_{3,j}\le\frac{2^{3/2}}{\sqrt{\det G_j}}\le16\sqrt2,\qquad
 M_{2,j}\le\frac{2}{\sqrt{\det (G_j)_{LV}}}\le8.
\]
The full light has every 2D projection cap \(K\le2\). Hence (2) supplies a numerical universal density bound for the original product problem on \(-|\varepsilon|\le s\le0\), uniformly in \(\beta\), \(\varepsilon\ne0\), the number of originals, and their support fragmentation. When \(|\varepsilon|\ge1\), this covers the entire central negative interval \((-1,0)\). More directly, the all-target estimate (3) has no logarithmic loss when \(|\varepsilon|\ge1\). It alone gives a universal density cap at **every** output level for the original-product \(a=0\), diffuse-frame, \(|\varepsilon|\ge1\) subclass, without invoking an outer-level theorem.

**Boundary.** The dependent-light negative shell fake passes every full-light plane cap but need not admit a two-full-rank-bank convolution with uniform \(M_2,M_3\). The genuine product problem still requires controlling the region \(|\varepsilon|<|s|<1\) in the diffuse two-bank case, along with physical frames that have no uniformly conditioned bank split and the hub-square term.