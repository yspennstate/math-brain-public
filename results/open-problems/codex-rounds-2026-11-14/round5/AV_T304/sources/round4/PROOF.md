# Coefficient and scale bounds for the numerical circuits

Source: OpenAI, *Subpolynomial query complexity for well-conditioned log-concave sampling*, September 26, 2026, Theorem 6.7 (`thm:numerical-interface`) and Section 7. The original formulas are saved in [numerics.tex](../preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/build/sections/numerics.tex) and [implementation.tex](../preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/build/sections/implementation.tex).

The result here concerns deterministic affine formulas and their parameter bounds. It does not establish the ideal-law approximation estimates in part (iv) of Theorem 6.7, the high-order derivative estimates used there, or the full sampling theorem.

## 1. The inherited conditional recurrence

Let a seeded map satisfy
\[
 M(c+u;z+v\otimes u/r)=M(c;z),\qquad \|v\|\le D_s.
\]
Put \(a=v/(2D_s)\), \(P=(I-aa^T)^{1/2}\), and \(n=r/(2D_s)\). For independent standard Gaussian arrays G and Z,
\[
 M(x+nZ;PG)=M(x;PG-a\otimes Z).
\]
The seed array on the right is centered Gaussian with covariance \(P^2+aa^T=I\), so it has the standalone seed law. If an approximate center C is at W₂ distance c from \(N(x,n^2I)\), couple these centers first and then adjoin independent G. A fixed-seed center Lipschitz constant K gives a cost Kc, and a standalone child error e gives the additional cost e. This proves the bound Kc+e without conditioning on C.

For an affine sum of independent complete occurrences, product couplings and the L² triangle inequality give
\[
 \epsilon_E\le\sum_i|a_i|(K\epsilon_{E_i}+e_i).
 \tag{1}
\]
The residual variance is nonnegative when \(\sigma_i=n/(2A')\) and \(\sum_i|a_i|\le A'\), since \(\sum_i a_i^2\sigma_i^2\le n^2/4\). Expanding (1) along paths of a tree of height h gives, with the notation of the earlier proof,
\[
 \|\epsilon_f\|_2\le B\overline D\delta^p
 \left[\frac n2+A_fS\delta^{-1/4}
             \sum_{j=1}^{h-1}(KA)^j\right].
 \tag{2}
\]
At tier j+1 the coefficient products sum to at most \(A_fA^j\) and there are j factors K. This independently recovers the earlier finite-tree formula and its exponent difference \(1/3-1/4=1/12\). The script checks different rational data and unequal trees, independently of the inherited script.

## 2. Scalar quadrature weights

All interpolation orders below are fixed before dimension tends to infinity. Constants may depend on those orders. Let \(h=\delta^w\), \(R=\delta^t\), \(\psi=\delta^{4t}\), and \(b_*=(1-R^2)^{1/2}\).

For ordinary interpolation on a cell of length ell, scaling a fixed Lagrange basis on [0,1] bounds its absolute basis sum by a constant C. A partial-integral row has absolute sum at most C times the integrated length. Summing across disjoint cells whose total length is at most one gives a uniform constant W for every probability-flow integration row. Orientation changes signs only. For a harmonic row, integrating the same basis against sine over an interval of length at most one also gives a constant bound H. For sufficiently large dimension the requested angles, bounded by \(C_m\psi\), lie in such an interval. The outer centering integration has a fixed row bound O. Increasing W,H,O to at least one is harmless.

The angle derivative stencil is the derivative at zero of the polynomial interpolant at nodes \(0,\psi,\ldots,(m-1)\psi\). Scaling the fixed stencil gives absolute weight sum
\[
 D_\theta\le C_m/\psi.
 \tag{3}
\]

For the kernel quadrature define \(A_0=-\log(1-b_*)\), \(n_0=\lceil A_0/h\rceil\), and \(a_0=A_0/n_0\). For sufficiently large dimension, \(A_0/h\ge1\), hence \(h/2\le a_0\le h\). The cell endpoints are \(\rho_c=1-e^{-ca_0}\). For rho in cell c its length satisfies
\[
 (1-e^{-a_0})(1-\rho)\le\ell_c
                  \le(e^{a_0}-1)(1-\rho).
\]
Thus \(ch(1-\rho)\le\ell_c\le Ch(1-\rho)\), and the first cell has length comparable to h.

On ordinary cells a derivative interpolation row has absolute sum at most \(C_m/\ell_c\). Integrating against \(1/\rho\), and summing, bounds the absolute value weights by
\[
 \frac{C_m}{h}\int_{\rho_1}^{b_*}
          \frac{d\rho}{\rho(1-\rho)}
 \le\frac{C_m}{h}(1+|\log h|+|\log R|).
\]
For the first cell impose the exact Hermite condition that the interpolant's derivative at zero is zero, together with m−1 value conditions including zero. These conditions determine a polynomial of degree at most m−1 uniquely: a polynomial in their null space has a double zero at zero and m−2 other distinct zeros, so is zero. In unit-cell coordinates each value basis polynomial \(L_j\) then satisfies \(L'_j(u)=uQ_j(u)\). Consequently \(\int_0^1|L'_j(u)|du/u\) is finite and bounded in terms of the fixed order. Scaling back contributes at most \(C_m/\ell_0\le C_m/h\). Therefore the complete kernel value-weight sum obeys
\[
 Q\le B_d\delta^{-w},\qquad B_d=C(1+\log d)^C.
 \tag{4}
\]
This argument applies to arbitrary supplied values. It does not assume that approximate values satisfy an endpoint identity; that identity is imposed on the interpolating polynomial itself.

## 3. Affine expansion and the cancellation of r

An affine state's coefficient norm means the sum of the absolute scalar coefficients of its exact mean symbols. An earlier mean is treated as one symbol; its own center is not substituted into that state. Combining repeated symbols can only decrease this norm.

The probability update is
\[
 y_i^{[k+1]}=y_{\rm in}-r\sum_jw_{ij}M_{\rho_j}(y_j^{[k]}).
\]
Each layer has direct term equal to the original input and coefficient norm at most rW, independent of the number of layers. If the input itself is affine in mean symbols, its coefficient norm is added once. The harmonic update has direct term \(\cos z_i\,y_{\rm in}+\sin z_i\,G_{\rm in}\) and adds at most rH. The factor rho in its integral is at most one.

The forward correction, with its starting position subtracted, is exactly
\[
 \mathrm{corr}_{ij}=-r\sum_kw_{ijk}M_{ijk}.
\]
With \(s=\sigma/2\), the approximate kernel velocity is consequently
\[
 -\frac1{rs}\sum_iq_i\sum_jd_j\mathrm{corr}_{ij}
       =\frac1s\sum_{i,j,k}q_id_jw_{ijk}M_{ijk}.
 \tag{5}
\]
This is an exact algebraic identity, valid before any law or approximation estimate. Its coefficient norm is at most
\[
 V_Y=\frac{2Q D_\theta W}{\sigma}
           \le B_d\sigma^{-1}\delta^{-4t-w}.
\]
The other velocity component is \((M_*-M_0)/s\), of coefficient norm at most \(V_G=4/\sigma\). The centering Picard update resets to the original anchors y,G at each layer. Its position and momentum correction norms are bounded respectively by \(U=OV_Y\) and \(V=OV_G\); no factor U or V is raised to the number of layers in these local expressions.

Now follow the free terms through one kernel evaluation. A backward position has direct term y and correction norm at most U+rW. A harmonic position has direct term \(\cos z\,y+\sin z\,G\) and correction norm at most \(U+V+rW+rH\). A subsequent forward position has the same direct term and norm at most \(U+V+2rW+rH\). These bounds use \(|\sin z|,|\cos z|\le1\). A physical primitive center is x+r rho times its normalized position. Its mean coefficient norm is thus at most
\[
 rO(V_Y+V_G)+r^2(2W+H)
 \le B_d(r/\sigma)\delta^{-4t-w}+C_mr^2.
 \tag{6}
\]
The direct physical terms are exactly \(x+r\rho y\) or \(x+r\rho(\cos z\,y+\sin z\,G)\). The separate M₀ node has direct center x and no earlier means. Formula (6) proves the declared bound
\[
 A_M=C_1(1+\log d)^{C_1}
       [(r/\sigma)\delta^{-4t-10w}+r^2]
\]
after increasing the fixed constant. The enlargement from w to 10w is allowed because \(0<\delta<1\).

For sampling there is just the probability circuit. Its physical center coefficient norm is at most r²W. Thus \(A_S=C_1r^2\). The mean output is \(\sigma G/2+\sum_j\omega_jM_*(y_j)\), so \(A_{f,M}=C_1\). The sample output is the probability state divided by \(\rho_e\); since \(\rho_e\ge2/\sqrt5\), \(A_{f,S}=C_1r\). All these constants can be covered by one fixed C₁. None introduces an inverse power of r beyond the displayed ratio r/sigma.

The number P of probability nodes is at most \(B_d\delta^{-w}\). A position-velocity list contains at most \(C_mP^2\) mean occurrences: a kernel quadrature node and a forward integral node are the two varying indices. All other quadratures have a fixed number of nodes. Substituting free positions adds only a bounded number of such lists and transport lists, stopping at mean symbols. Hence direct expression size is at most \(B_d\delta^{-2w}\), which implies the source's weaker \(B_d\delta^{-10w}\). Each inner kernel path crosses at most N backward, N harmonic and N forward layers. At most N outer layers and the final mean therefore give dependency depth at most \(3N^2+1\), independent of mesh size and interpolation order.

## 4. Scales and shifts

Every mean at probability time rho has scale \(r_i=r\tau_i\), \(\tau_i=\sqrt{1-\rho_i^2}\). Mean-circuit times obey \(\rho_i\le b_*\), so \(\tau_i\ge R\); the final mean symbols all have scale rR. For sampling,
\[
 \rho_i\le\rho_e=(1+\eta^2/4)^{-1/2},\qquad
 \sqrt{1-\rho_e^2}=\eta/\sqrt{4+\eta^2}\ge R/\sqrt5.
 \tag{7}
\]
This is uniform over \(R\le\eta\le1\).

The compiler's direct center shifts also stay bounded after scale normalization. In a sampling parent,
\[
 0\le1-\rho_i\rho_e\le1-\rho_i^2=\tau_i^2,
 \qquad |k_i|/\tau_i\le1.
\]
For a mean parent, use \(0\le\rho_i/b_*\le1\), \(1-\cos z\le z^2/2\), and \(1-\rho_i/b_*\le1-\rho_i\le\tau_i^2\). Then
\[
 0\le1-\rho_i\cos z/b_*\le\tau_i^2+z^2/2,
 \qquad |k_i|/\tau_i\le1+z^2/(2R)
                          \le1+C_m^2\delta^{7t}/2.
 \tag{8}
\]
This proves a bounded ratio, with slightly sharper constants than the source's unspecified C. The assertion is asymptotic for fixed interpolation order; it makes no uniform claim in a growing order.

## 5. Consequences for the compiler's size labels

Write \(\lambda=\delta\), \(L=\lambda r\), \(l=\lambda r^2\), and \(D_s=\delta^{-t}\). Assume a mean parent's size condition \(\max(l,L/\sigma)\le B_d\delta^b\). Formula (6), enlarged as above, gives
\[
 \lambda A_M\le B_d\delta^{b-4t-10w}.
 \tag{9}
\]
For a sample parent, \(l/\eta\le B_d\delta^b\) and \(\eta\le1\) give \(\lambda A_S=C_1l\le B_d\delta^b\).

At a nonfinal expression term, if the supplied center belongs to a node of scale \(r\tau_{\rm prev}\), its evaluation budget is \(r\tau_{\rm prev}/(2D_s)\). Therefore a mean invoked in that expression has
\[
 \sigma_i=\frac{r\tau_{\rm prev}}{4D_sA},\qquad
 \frac{L_i}{\sigma_i}=4D_s\lambda A\frac{\tau_i}{\tau_{\rm prev}}
                 \le4\sqrt5(D_s/R)\lambda A.
 \tag{10}
\]
Using \(D_s/R=\delta^{-2t}\), the exponent in the mean case is \(b-6t-10w\), and in the sample case it is \(b-2t\). If \(10w<t\), these are stronger than the assigned exponent b−10t, with slack greater than 3t and equal to 8t respectively. Also \(l_i\le l\). The same-center sampling anchor of a mean parent has \(\eta=R/b_*\), so \(l/\eta\le l/R\), leaving slack 9t relative to b−10t.

For final terms of a mean parent, \(\sigma_i\) is a fixed positive multiple of sigma and \(r_i=rR\). Thus \(L_i/\sigma_i\) gains t in its exponent and \(l_i\) gains 2t, as required by the label b+t. For final sample terms, \(\sigma_i\) is a fixed positive multiple of eta/r, so \(L_i/\sigma_i\le C l/\eta\) and the unchanged label b is valid.

The nonfinal noise units are also as asserted. The declared \(A_M\) is bounded below by a positive fixed multiple of r/sigma, hence (10) gives \(\sigma_i\le C\sigma\). For sampling, \(A_S=C_1r^2\) gives \(r\sigma_i\le1/(4C_1D_s)\le C\). Consequently \(A_{f,M}\sigma_i\le C\sigma\) and \(A_{f,S}\sigma_i\le C\), precisely the two units needed in (2).

Finally the source requires \(K_0\ge2\), \(40(K_0+2)t<1/4\), and \(10w<t\). These imply \(t<1/640\). For reachable b>1/2,
\[
 b-4t-10w>b-5t>\frac12-\frac1{128}
                         =\frac{63}{128}>\frac13.
 \tag{11}
\]
Thus the source's \(\lambda A\le B_d\delta^{1/3}\) follows with room to spare. A fixed power of log d can be absorbed into the strict exponent margin when \(\delta=d^{-e}\), with fixed e>0. Combining the coarser 1/3 gain with the 1/4 accuracy loss recovers the earlier 1/12 margin.

## 6. Checks against failure cases

The derivation allows arbitrarily small positive r, positive sigma, signed interpolation weights, zero coefficients, and a repeated mean symbol. Bounds use absolute sums and declared positive upper bounds. A zero-length probability interval has no integral rows. All scale lower bounds here require R>0, as in the source; no assertion is made at R=0.

Subtracting the forward starting state in (5) is essential. If the full forward state T(W_z) were differentiated instead, its free term would contribute G at z=0, giving an unwanted term −G/(rs). Even when the forward correction vanishes, that term need not vanish. The actual formula differentiates T−id and avoids it.

Likewise a shared-center version of (1) fails. For the family \(M(c;z)=\alpha(c+z)\), a common center Z/2 and transformed fresh seed \(\sqrt3G_i/2\) give exact marginal child variance alpha² but covariance alpha²/4 between the two calls. Averaging them with weights 1/2 and adding the prescribed residual to target variance one gives variance \(1+\alpha^2/8\), rather than one. This recovers the earlier 33/32 at alpha=1/2 and gives 73/72 at alpha=1/3. The source's duplicated supplying subtrees exclude this example.

These checks establish the deterministic coefficient and scale inputs to the previously audited local recurrence. They do not replace the remaining analytic, query-cap, or final-target arguments.
