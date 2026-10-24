# B18 exact phase-defect theorem — no truncation and no dimension loss

**Status:** **PROVED phase-sensitive consequence / full FEI remains OPEN.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Dependencies:** only the tangent-defect decomposition in `REPORT.md` and the Boolean identity `g^2=1`.

The earlier phase handoff used a good/bad posterior cutoff. A sharper argument removes that cutoff completely by pairing the scalar tangent defect with Cauchy in the correct homogeneous measure.

## 1. Signed supported upper mass

For coordinate `i`, write

\[
x_T=\widehat g(T)^2,
\qquad
y_T=\widehat g(T\cup\{i\})^2,
\qquad
q_T={y_T\over x_T+y_T}.
\]

On edges with `x_Ty_T>0`, define

\[
\varepsilon_T=\operatorname{sgn}(\widehat g(T)\widehat g(T\cup\{i\})).
\]

Let

\[
Z_i=\sum_{T:x_Ty_T>0}\varepsilon_Ty_T.
\tag{1.1}
\]

Thus `Z_i` is the signed difference between positive- and negative-sign **upper spectral mass**, excluding only unsupported upper edges `x_T=0<y_T`.

Booleanity gives the singleton convolution cancellation

\[
\boxed{
\sum_{T:x_Ty_T>0}\varepsilon_T\sqrt{x_Ty_T}=0.
}
\tag{1.2}
\]

Fix the hard-core endpoint `tau=tau(r)`, put

\[
\theta={\tau\over1-\tau},
\]

and retain the tangent defect

\[
G_r(q)=\beta(q)-b(r)-\lambda(r)(\kappa(q)-r)\ge0.
\]

## 2. A scalar phase-transfer constant

Define

\[
N_\tau(q)=q-\sqrt{\theta q(1-q)}
\tag{2.1}
\]

and

\[
\boxed{
K_r=
\sup_{0<q\le1,\ q\ne\tau}
{N_\tau(q)^2\over qG_r(q)}.
}
\tag{2.2}
\]

Then

\[
\boxed{K_r<\infty.}
\tag{2.3}
\]

### Proof of finiteness

At `q=tau`, `N_tau(tau)=0`. Both numerator and `G_r` vanish quadratically there: `N_tau` is smooth with a simple zero, while the sibling report proves

\[
G_r''(\tau)=\kappa'(\tau)\lambda'(\tau)>0.
\]

Hence the quotient has a finite removable limit at `tau`.

As `q downarrow0`,

\[
N_\tau(q)^2\sim\theta q,
\]

while `G_r(q)\to+infinity` logarithmically, so the quotient tends to zero. At `q=1`,

\[
N_\tau(1)=1,
\qquad
G_r(1)=d_r:=\lambda r-b>0,
\]

so the quotient tends to `1/d_r`. Continuity away from `tau` now gives a finite supremum. QED.

## 3. Main theorem: scalar slack pays signed phase imbalance quadratically

Let

\[
D_i=B_i-b(r)p_i
\]

for a restriction-maximal core, and let

\[
S_i=\sum_{T:y_T>0}y_TG_r(q_T).
\]

The exact tangent-defect decomposition gives

\[
0\le S_i\le D_i.
\tag{3.1}
\]

### Theorem 3.1

For every relevant coordinate,

\[
\boxed{Z_i^2\le K_rS_i\le K_rD_i.}
\tag{3.2}
\]

Consequently,

\[
\boxed{
\sum_iZ_i^2\le K_r\,[B(g)-b(r)I(g)].
}
\tag{3.3}
\]

### Proof

By (1.2),

\[
\begin{aligned}
Z_i
&=\sum_{x_Ty_T>0}\varepsilon_T
\left[y_T-\sqrt\theta\sqrt{x_Ty_T}\right]\\
&=\sum_{x_Ty_T>0}\varepsilon_T(x_T+y_T)
\left[q_T-\sqrt{\theta q_T(1-q_T)}\right].
\end{aligned}
\]

Put `w_T=x_T+y_T`. Weighted Cauchy with weight `y_TG_r(q_T)=w_Tq_TG_r(q_T)` gives

\[
Z_i^2
\le
\left(\sum_{supported}y_TG_r(q_T)\right)
\left(
\sum_{supported}
 w_T{N_\tau(q_T)^2\over q_TG_r(q_T)}
\right).
\]

The second factor is at most

\[
K_r\sum_{supported}w_T\le K_r,
\]

because the fibre weights sum to one. This proves (3.2), and summing coordinates proves (3.3). QED.

No posterior cutoff, ambient-dimension factor, or square-root tail remains.

## 4. Unsupported upper mass is also linearly paid

Let

\[
U_i=\sum_{T:x_T=0<y_T}y_T.
\]

Every such edge has `q_T=1`, so it contributes exactly `d_r y_T` to `S_i`, where

\[
d_r=G_r(1)=\lambda r-b>0.
\]

Hence

\[
\boxed{U_i\le D_i/d_r,}
\qquad
\boxed{\sum_iU_i\le {B-bI\over d_r}.}
\tag{4.1}
\]

If `Y_{i,+}` and `Y_{i,-}` are the supported upper masses of the two edge-sign classes, then

\[
p_i=Y_{i,+}+Y_{i,-}+U_i,
\qquad
Z_i=Y_{i,+}-Y_{i,-}.
\]

Therefore

\[
\left(Y_{i,+}-{p_i\over2}\right)^2
+\left(Y_{i,-}-{p_i\over2}\right)^2
={Z_i^2+U_i^2\over2}.
\]

Since `U_i<=1` implies `U_i^2<=U_i`, (3.3) and (4.1) give the robust half-half law

\[
\boxed{
\sum_i\left[
\left(Y_{i,+}-{p_i\over2}\right)^2
+\left(Y_{i,-}-{p_i\over2}\right)^2
\right]
\le
{B-bI\over2}
\left(K_r+{1\over d_r}\right).
}
\tag{4.2}
\]

At exact scalar-frontier saturation this collapses to

\[
Y_{i,+}=Y_{i,-}=p_i/2,
\qquad U_i=0
\]

for every relevant coordinate.

## 5. Calibration and interpretation

At the inherited calibration

\[
r=6.521845710923046575,
\quad
\tau=0.1740316570325050...,
\quad
\theta=0.2107001539638352...,
\]

\[
d_r=\lambda r-b=1.867278534313846... .
\]

A dense numerical scan (calibration only, not used by the proof) found the quotient in (2.2) below approximately `0.53554`, with the largest sampled value at the endpoint `q=1`, where it equals `1/d_r`. No closed-form claim `K_r=1/d_r` is made; that identity fails for some larger `r` calibrations.

The important point is structural: the sharp scalar frontier does not merely force unsigned posterior concentration. Combined with the exact Boolean signed convolution, its slack linearly pays an **L2 phase-imbalance bank** with no dimension loss.

This is directly compatible with the current B16 signed-transport direction: B16's viable interfaces also retain a square of a signed divergence. The next missing implication is now to connect a nontrivial part of that signed transport/plaquette divergence to the concrete spectral phase vector `Z=(Z_i)`, or else classify the regime where `Z` is small while the high-r hard-core constraints persist. No unsigned pairwise replacement is required or asserted.
