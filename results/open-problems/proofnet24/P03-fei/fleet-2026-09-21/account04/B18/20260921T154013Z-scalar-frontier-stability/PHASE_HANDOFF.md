# B18 phase handoff — endpoint stability plus Boolean sign cancellation

**Status:** **PROVED auxiliary bridge / full FEI still OPEN.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Dependency:** the analytic tangent-defect stability theorem in the sibling `REPORT.md`.

The main report proves that small scalar-frontier slack controls upper-mass-weighted posterior error. This note asks the next phase-sensitive question: what does Booleanity force on the **signs** of the nearly geometric Fourier edges?

Let `a_S=hat g(S)` and for a coordinate `i` pair

\[
x_T=a_T^2,\qquad y_T=a_{T+i}^2,\qquad
q_T={y_T\over x_T+y_T}.
\]

Whenever `x_Ty_T>0`, put

\[
\varepsilon_T=\operatorname{sgn}(a_Ta_{T+i})\in\{+1,-1\}.
\]

Booleanity `g^2=1` gives the singleton signed-convolution identity

\[
\boxed{
\sum_Ta_Ta_{T+i}=0,
\qquad\text{equivalently}\qquad
\sum_T\varepsilon_T\sqrt{x_Ty_T}=0.
}
\tag{1}
\]

Fix an endpoint `tau in (0,1/2)`, put `theta=tau/(1-tau)`, and choose

\[
0<\eta<\min\{\tau,1/2-\tau\}.
\]

Call an edge **good** when `|q_T-tau|<eta` and bad otherwise. Let

\[
Y_+=\sum_{T\ good,\ \varepsilon_T=+1}y_T,
\qquad
Y_-=\sum_{T\ good,\ \varepsilon_T=-1}y_T,
\]

\[
V=\sum_Ty_T(q_T-\tau)^2,
\qquad
M=\sum_{T\ bad}y_T.
\]

## Proposition — quantitative signed balance modulo a square-root tail

Define

\[
K_{\tau,\eta}=\sqrt{\frac{1-\tau+\eta}{\tau-\eta}},
\]

\[
L_{\tau,\eta}=
\frac1{2\sqrt{\tau-\eta}(1-\tau-\eta)^{3/2}},
\qquad
C_{\tau,\eta}=K_{\tau,\eta}L_{\tau,\eta}.
\]

Then

\[
\boxed{
|Y_+-Y_-|
\le C_{\tau,\eta}\sqrt{p_iV}
+\sqrt\theta\sum_{T\ bad}\sqrt{x_Ty_T},
}
\tag{2}
\]

where `p_i=sum_T y_T`. In particular, by Cauchy,

\[
\boxed{
|Y_+-Y_-|
\le C_{\tau,\eta}\sqrt{p_iV}
+\sqrt{\theta M}.
}
\tag{3}
\]

### Proof

Put

\[
r(q)=\sqrt{q/(1-q)}.
\]

For a good edge,

\[
y_T=\sqrt{x_Ty_T}\,r(q_T),
\qquad
\sqrt\theta\sqrt{x_Ty_T}
=\sqrt{x_Ty_T}\,r(\tau).
\]

On the good interval,

\[
|r'(q)|={1\over2\sqrt q(1-q)^{3/2}}
\le L_{\tau,\eta},
\]

and

\[
\sqrt{x_Ty_T}
=y_T\sqrt{(1-q_T)/q_T}
\le K_{\tau,\eta}y_T.
\]

Therefore

\[
|y_T-\sqrt\theta\sqrt{x_Ty_T}|
\le C_{\tau,\eta}y_T|q_T-\tau|.
\tag{4}
\]

Using (1),

\[
\begin{aligned}
Y_+-Y_-
&=\sum_{good}\varepsilon_Ty_T\\
&=\sum_{good}\varepsilon_T
   (y_T-\sqrt\theta\sqrt{x_Ty_T})
  -\sqrt\theta\sum_{bad}\varepsilon_T\sqrt{x_Ty_T}.
\end{aligned}
\]

Take absolute values and apply (4). Weighted Cauchy gives

\[
\sum_{good}y_T|q_T-\tau|
\le\sqrt{p_iV},
\]

which proves (2). Finally

\[
\sum_{bad}\sqrt{x_Ty_T}
\le\sqrt{\left(\sum_{bad}x_T\right)
          \left(\sum_{bad}y_T\right)}
\le\sqrt M,
\]

because `sum_Tx_T=1-p_i<=1`. QED.

## Corollary for a restriction-maximal hard core

Let

\[
D_i=B_i-b(r)p_i.
\]

The sibling report proves

\[
V\le D_i/c_r,
\qquad
M\le D_i/(c_r\eta^2).
\]

Hence

\[
\boxed{
|Y_+-Y_-|
\le
{C_{\tau,\eta}\over\sqrt{c_r}}\sqrt{p_iD_i}
+{\sqrt\theta\over\eta\sqrt{c_r}}\sqrt{D_i}.
}
\tag{5}
\]

At the exact scalar endpoint `D_i=0`, every upper edge is good and (5) gives the new exact sign law

\[
\boxed{Y_+=Y_-=p_i/2.}
\tag{6}
\]

Thus exact endpoint Booleanity requires not only a geometric down-set magnitude law but an exact half-half split of each coordinate's influence mass across positive and negative Fourier edge signs.

## The remaining obstruction is now explicit

Equation (2) isolates the phase bottleneck. The first term is paid by the newly proved endpoint-defect energy. The only part not linearly influence-paid is

\[
\boxed{
R_i^{\sqrt{\ }}(\eta)
:=\sum_{|q_T-\tau|\ge\eta}\sqrt{x_Ty_T}.
}
\tag{7}
\]

A tiny-upper-mass edge with `q<<tau` costs little in the scalar size-biased bank (`y_T`), yet can carry much larger signed convolution mass (`sqrt(x_Ty_T)`). This explains why exact endpoint nonattainment does not automatically become a uniform FEI rebate and identifies the precise quantity a signed-transport/block argument has to amplify or charge.

This is compatible with the current B16 warning not to replace signed divergence by unsigned pairwise sums: (7) is not proposed as a globally bounded unsigned bank. The useful handoff is the opposite — after scalar stability, **all sign imbalance is forced into this square-root bad-posterior tail**. A successful next implication can therefore target (7) using shared lower masses, collisions, block restrictions or the existing signed transport field rather than re-proving scalar strictness.
