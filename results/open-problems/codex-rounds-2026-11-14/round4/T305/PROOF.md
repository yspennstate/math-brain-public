# Finite-step energy control for nonquadratic independent blocks

Let an orthogonal decomposition of R^d into blocks of dimensions
1<=k_j<=k_0 be given, and suppose
\[
 V(x)=\sum_{j=1}^N V_j(x_j),\qquad
 mI\preceq\nabla^2 V_j\preceq LI,
 \quad
 \|\nabla^2 V_j(x)-\nabla^2 V_j(y)\|_{\rm op}\le M|x-y|.
 \tag{1}
\]
Each V_j is C^2; no higher continuous derivatives are required. The
constants m,L,M,k_0 are fixed. Set
\[
 H(x,p)=V(x)+|p|^2/2,\quad
 \rho=\pi\otimes N(0,I_d),\quad
 S=\Psi_h^n,\quad \Delta=H\circ S-H,
 \tag{2}
\]
where Psi_h is kick–drift–kick leapfrog, 0<h<=1, and 0<nh<=T_* for a
fixed T_*>0. All proposals are considered before the accept/reject decision.

There are finite constants C_1,C_2,c>0, depending only on m,L,M,T_*,k_0,
such that
\[
 0\le\mu:=E_\rho\Delta
 =D_{\rm KL}(S_\#\rho\|\rho)
 \le C_1 d h^4,
 \tag{3}
\]
and, for every s>0,
\[
 \rho\left\{|\Delta-\mu|>
 2\sqrt{C_2}\,h^2\sqrt{ds}+c^{-1}hs\right\}\le2e^{-s}.
 \tag{4}
\]
Consequently, from any position law nu<=M_0 pi with independent standard
Gaussian momentum, with probability at least 1-delta,
\[
 |\Delta-\mu|\le
 2\sqrt{C_2}\,h^2\sqrt{d\log(2M_0/\delta)}
 +c^{-1}h\log(2M_0/\delta).
 \tag{5}
\]
The center mu is the stationary mean, including under the warm law.
The warm law need not be a product law.

An explicit choice of constants is given below. For the mean in (3), the
dependence on k_0 can be taken polynomial, C_1<=C(m,L,M,T_*) k_0^2.
The constants for (4) are allowed to grow exponentially with k_0.

## 1. Reversibility bounds the mean by a second moment

This section applies to every C^2 potential with mI<=Hessian V<=LI,
without the block assumption. Write J(x,p)=(x,-p). The leapfrog shears are global
volume-preserving diffeomorphisms, and
\[
 J S J=S^{-1},\qquad H\circ J=H.
\]
Thus F=J S is a volume-preserving involution. Since H(Fz)=H(Sz),
\[
 \Delta(Fz)=-\Delta(z).
 \tag{6}
\]
Changing variables z=F y gives, for every nonnegative measurable f,
\[
 E_\rho f(\Delta)=E_\rho[e^{-\Delta} f(-\Delta)].
 \tag{7}
\]
The same formula holds for integrable signed f when the right side is
absolutely integrable. Bounded Hessians, the Gaussian tails of rho, and
the linear growth of every finite composition of shears give finite
moments of Delta. Applying (7) to absolute powers justifies its use for
the corresponding signed powers. In particular,
\[
 E e^{-\Delta}=1,\quad
 E[\Delta e^{-\Delta}]=-E\Delta,\quad
 E[\Delta^2 e^{-\Delta}]=E\Delta^2.
 \tag{8}
\]
For all real t, |tanh(t/2)|<=|t|/2, and hence
\[
 t(1-e^{-t})\le\frac{t^2}{2}(1+e^{-t}).
\]
Using (8),
\[
 E\Delta=\frac12 E[\Delta(1-e^{-\Delta})]
 \le\frac14 E[\Delta^2(1+e^{-\Delta})]
 =\frac12 E\Delta^2.
 \tag{9}
\]
If f_rho is the density of rho, volume preservation gives
f_{S#rho}(Sz)=f_rho(z). Therefore
\[
 D_{\rm KL}(S_\#\rho\|\rho)
 =E_\rho\log\frac{f_\rho(Z)}{f_\rho(SZ)}
 =E_\rho\Delta\ge0.
 \tag{10}
\]
Equations (9)–(10) do not hold for an arbitrary volume-preserving map
without the reversibility used in (7); (10) alone does.

## 2. Two deterministic estimates for a single block

Translate the minimizer of a block to zero, subtract its minimum value,
and write U for its potential, g=grad U, and K=Hessian U. Thus g(0)=0,
U(0)=0, and |g(x)|<=L|x|. The translation and subtraction do not change
leapfrog or energy errors. Put W=|(x,p)| and define
\[
 q=x+hv,\qquad v=p-\frac h2g(x),\qquad
 p'=v-\frac h2g(q),\qquad r=q-x=hv.
\]
Since p=v+h g(x)/2, subtracting the two kinetic energies gives the exact
identity
\[
 \begin{split}
 H(q,p')-H(x,p)
 &=U(q)-U(x)-\frac12 r\cdot(g(q)+g(x))\\
 &\quad+\frac{h^2}{8}(|g(q)|^2-|g(x)|^2).
 \end{split}
 \tag{11}
\]
To bound the first line, let f(t)=U(x+tr), t in [0,1]. Integration by
parts gives
\[
 f(1)-f(0)-\frac{f'(1)+f'(0)}2
 =\int_0^1(1/2-t)f''(t)\,dt.
 \tag{12}
\]
Since |f''|<=L|r|^2 and the integral of |1/2-t| is 1/4, its absolute
value is at most L|r|^2/4. Also f'' is Lipschitz with constant M|r|^3.
It is absolutely continuous, and a second integration by parts gives
\[
 \int_0^1(1/2-t)f''(t)\,dt
 =-\frac12\int_0^1 t(1-t)f'''(t)\,dt.
\]
The derivative here exists almost everywhere and is bounded by M|r|^3.
Thus the same defect is at most M|r|^3/12. These identities require only
the regularity in (1).

Set
\[
 c_v=1+L/2,\quad
 a=Mc_v^3/12,\quad b=L^2c_v(2+c_v)/8,
 \quad e=Lc_v^2/4+b.
 \tag{13}
\]
For h<=1,
\[
 |v|\le c_vW,\quad |q|\le(1+c_v)W,\quad
 |g(q)|+|g(x)|\le L(2+c_v)W.
\]
Also |g(q)-g(x)|<=L|r|. Using the two alternatives following (12) in
(11) yields both estimates
\[
 |H(q,p')-H(x,p)|\le h^3(aW^3+bW^2),
 \tag{14}
\]
\[
 |H(q,p')-H(x,p)|\le e h^2W^2.
 \tag{15}
\]
In (15) the h^3 bW^2 term was enlarged to h^2 bW^2.

A kick has norm growth factor at most 1+hL/2 and a drift at most 1+h,
by the triangle inequality in phase space. Hence every numerical mesh
point at time jh<=T_* has norm at most
\[
 W_j\le E_* W_0,\qquad E_*:=\exp((L+1)T_*).
 \tag{16}
\]
Summing (14) and (15) over n steps, with nh<=T_*, proves
\[
 |\Delta_j|\le B h^2(W_0^2+W_0^3),\qquad
 |\Delta_j|\le D h W_0^2,
 \tag{17}
\]
where Delta_j now denotes the full trajectory's error in this block, and
\[
 B=T_*(aE_*^3+bE_*^2),\qquad D=T_*eE_*^2.
 \tag{18}
\]
B,D depend only on L,M,T_*, not on block dimension. They are conservative
constants. In particular, no distributional assertion about numerical
mesh points was used.

## 3. Stationary radial moments

Let alpha=min(m,1). For a block of position dimension k, its phase-space
potential H_j=U(x)+|p|^2/2 satisfies
\[
 z\cdot\nabla H_j(z)\ge\alpha|z|^2,\qquad z=(x,p)\in R^{2k}.
\]
Integration by parts against z|z|^{2r-2}, justified by Gaussian tails,
gives for integers r>=1
\[
 \begin{split}
 \alpha E W^{2r}
 &\le E[W^{2r-2}Z\cdot\nabla H_j(Z)]\\
 &=(2k+2r-2)E W^{2r-2}.
 \end{split}
\]
Consequently, writing (k)_r=k(k+1)...(k+r-1),
\[
 E W^{2r}\le(2/\alpha)^r(k)_r.
 \tag{19}
\]
Cutoffs justify the integration by parts before removing them; strong
convexity and the upper Hessian bound ensure polynomial integrability.

For 0<=beta<alpha/2, expand the exponential into nonnegative terms and
use (19). For every nonnegative integer r,
\[
 \begin{split}
 E[W^{2r}e^{\beta W^2}]
 &\le\sum_{l=0}^\infty\frac{\beta^l}{l!}
       (2/\alpha)^{r+l}(k)_{r+l}\\
 &=(2/\alpha)^r(k)_r
   (1-2\beta/\alpha)^{-k-r}.
 \end{split}
 \tag{20}
\]
The final equality is the binomial series, with
(k)_{r+l}=(k)_r(k+r)_l.

Since (W^2+W^3)^2<=2(W^4+W^6), define
\[
 P_k=(2/\alpha)^2k(k+1)
      +(2/\alpha)^3k(k+1)(k+2),
 \tag{21}
\]
\[
 J_k=2^{k+1}\left[(4/\alpha)^2k(k+1)
            +(4/\alpha)^3k(k+1)(k+2)\right].
 \tag{22}
\]
Equations (19)–(20), with beta=alpha/4 in the latter, give
\[
 E(W^2+W^3)^2\le2P_k,
 \quad
 E[(W^2+W^3)^2e^{\alpha W^2/4}]\le J_k.
 \tag{23}
\]

## 4. Entropy and centered exponential moments

The block dynamics are reversible in the sense of Section 1. Equations
(9), (17), and (23) imply
\[
 0\le\mu_j=E\Delta_j\le B^2 P_{k_j} h^4.
 \tag{24}
\]
Under rho the initial blocks are independent and the numerical map acts
separately on them. Hence Delta=sum_j Delta_j and mu=sum_j mu_j. Relative
entropy also tensorizes, consistently with (10). Since sum_j k_j=d,
\[
 \mu\le B^2 h^4\sum_jP_{k_j}
 \le C_1d h^4,
 \quad
 C_1=B^2\left[(2/\alpha)^2(k_0+1)
       +(2/\alpha)^3(k_0+1)(k_0+2)\right].
 \tag{25}
\]
This proves (3), including the stated polynomial block-size dependence.

For the tails, set
\[
 c=\frac{\alpha}{4D}>0,\qquad C_2=\frac12 B^2J_{k_0}.
 \tag{26}
\]
For |t|<=c/h, the coarse estimate in (17) gives
|t Delta_j|<=alpha W^2/4, whereas the sharper estimate and (23) give
\[
 E[\Delta_j^2 e^{|t\Delta_j|}]
 \le B^2 h^4 J_{k_j}\le2C_2h^4.
 \tag{27}
\]
For every real u, e^u<=1+u+u^2 e^{|u|}/2. Thus
\[
 E e^{t\Delta_j}\le1+t\mu_j+C_2 h^4t^2.
\]
The right side is positive, since it bounds a positive expectation.
The inequality log(1+x)<=x for x>-1 therefore proves
\[
 \log E e^{t(\Delta_j-\mu_j)}\le C_2h^4t^2,
 \qquad |t|\le c/h.
 \tag{28}
\]
No exponential moment of a positive multiple of W^3 was asserted.
Combining the two bounds in (17) is essential in (27).

Independence and N<=d now give
\[
 \log E_\rho e^{t(\Delta-\mu)}\le C_2d h^4t^2,
 \qquad |t|\le c/h.
 \tag{29}
\]
Put v=C_2dh^4 and b_h=h/c. For 0<t<1/b_h, (29) is at most
v t^2/(1-b_h t). In Chernoff's inequality choose
\[
 t=\frac{\sqrt s}{\sqrt v+b_h\sqrt s},\qquad
 r_s=2\sqrt{vs}+b_hs.
\]
Direct substitution gives
\[
 t r_s-\frac{vt^2}{1-b_ht}=s.
\]
Using the same argument for negative t gives (4).

## 5. Warm starts and rejection

If nu<=M_0 pi and momentum is independently refreshed, the initial
phase-space law is bounded above by M_0 rho, whether or not the warm
position coordinates are independent. Multiply the exceptional
probability in (4) by M_0 and choose s=log(2M_0/delta) to prove (5).

In particular, with probability at least 1-delta under that law,
\[
 \Delta\le C_1dh^4+2\sqrt{C_2}h^2\sqrt{ds}+c^{-1}hs,
 \quad s=\log(2M_0/\delta).
 \tag{30}
\]
For eta>0, the sufficient step-size conditions
\[
 h\le1,\qquad
 h\le\left(\frac{\eta}{3C_1d}\right)^{1/4},\quad
 h\le\left(\frac{\eta}{6\sqrt{C_2}\sqrt{ds}}\right)^{1/2},\quad
 h\le\frac{c\eta}{3s}
 \tag{31}
\]
make the right side of (30) at most eta. Since the conditional rejection
probability is (1-e^{-Delta})_+<=min(1,Delta_+), its average is at most
eta+delta. For fixed eta,delta the reciprocal step size in (31) is
O(d^{1/4}(1+s^{1/4})+s), with constants depending on the displayed
regularity parameters and k_0. A bounded integration time consequently
uses at most that order of leapfrog steps, after rounding n upward and
setting h=T/n. This is a one-proposal acceptance statement.

Stationary average rejection is also at most sqrt(mu/2), by (10) and
Pinsker's inequality. Directly transferring that average by nu<=M_0 pi
would cost M_0; the event argument above gives logarithmic warm dependence.

## 6. Relation to the earlier remainder and to T305

With A=p^T Hessian(V)p/12-|grad V|^2/24, exact Hamiltonian flow preserves
rho, so E(A-A o Phi_T)=0. Consequently the earlier remainder
\[
 R=\Delta-h^2(A-A\circ\Phi_T)
\]
satisfies E R=mu. Equation (25) therefore bounds its mean by C_1dh^4
for these nonquadratic block targets. It does not assert the Gaussian
O(h^4 sqrt(d)) scale for centered remainder fluctuations.

The class (1) still has a dimension-independent Frobenius-Lipschitz
Hessian bound. Indeed
\[
 \begin{split}
 \|\nabla^2V(x)-\nabla^2V(y)\|_F^2
 &=\sum_j\|\nabla^2V_j(x_j)-\nabla^2V_j(y_j)\|_F^2\\
 &\le\sum_j k_jM^2|x_j-y_j|^2
 \le k_0M^2|x-y|^2.
 \end{split}
 \tag{32}
\]
Thus these results extend the earlier finite-step Gaussian analysis to
nonquadratic C^{2,1} blocks, but do not extend the source mixing theorem
to the full class in T305. No mixing theorem or larger-exponent lower
bound is established here.

For comparison, the reversibility and deterministic estimates apply
without blocks in dimension d. Equations (9), (17), and (19) then give
only the coarser bound E Delta<=B^2P_d h^4=O(d^3h^4), not O(dh^4).
Bounding that same second moment by O(dh^4), or controlling its centered
counterpart sufficiently well without independence, remains a concrete
route for the full problem.
