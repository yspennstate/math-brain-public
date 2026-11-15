# Verification of the single-replacement collision estimate

The source is OpenAI, *Bose–Einstein condensation at positive temperature in the dilute hard-sphere gas* (October 5, 2026), [Section 6](sources/bridges-current.tex), Lemma 6.3 (`lem:single-hit`). Regularity is defined in [Section 5](sources/slab-current.tex), Definition 5.2. The result below concerns a deterministic obstacle and an unconditioned free bridge law. It does not concern the interacting thermal path law.

## Statement and hypotheses

The lemma in the source reads:

```tex
\begin{lemma}[A single replacement]\label{lem:single-hit}
Let $y\in B_v$, $|z-v|\le3$, and let $c$ be a deterministic regular
path satisfying $d(y,c(0))>s_0$ and $d(z,c(2t))>s_0$.
For either $Q=Q_{y,z}^{B}$, with any target cell $B$, or
$Q=Q_{y,z}^{0}$, one has
\begin{equation}\label{bridge:single-estimate}
 Q(\mathcal C_v\cap\mathcal H(c))
 \le Ctr+C\frac{rD^{3\gamma}}{\sqrt{h_0}}
 \le C\alpha\bigl(tD^{-1}+D^{-1/4}\bigr).
\end{equation}
Thus this probability tends to zero with $D$ for each fixed $t$.
\end{lemma}
```

Here (0<t\le1) is fixed, (r=\alpha/D), (h_0=D^{-1}), (s_0=bD^{-1/3}), and (\gamma=1/12). The parameter (\alpha) ranges over a fixed compact positive interval. Each half of ([0,2t]) has (m=\lceil t/r^2\rceil) intervals of length (\tau=t/m). If (A_k(c)) is the lifted diameter of (c) on interval (k), divided by (r), regularity says

\[
 \max_k A_k(c)\le D^\gamma,
 \qquad \sum_{k=1}^{2m}(1+A_k(c))^3\le2C_{\rm reg}m.
 \tag{1}
\]

It also says that the lifted diameter in either outer window of length (h_0) is at most (s_0/8). The event (\mathcal C_v) requires the trial path to be regular and its chosen lift to stay in the radius-ten ball about (v). The collision event (\mathcal H(c)) means distance at most (r) at some common time.

The law (Q^B_{y,z}) chooses (U) uniformly in the unit target cell (B), then joins independent generator-(\Delta) bridges from (y) to (U) and from (U) to (z), each of duration (t). A target cell is the home cell or a face neighbor; hence (|U-v|\le1+\sqrt3/2<2). The law (Q^0_{y,z}) is a single duration-(2t) Euclidean bridge, projected to the torus.

Take the torus side length (K>50), as in the large-volume application. For sufficiently large (D), uniformly over the specified (\alpha)-interval,

\[
 r^2/2\le\tau\le r^2,\quad
 \tau\le h_0/2,\quad h_0<t/4,\quad
 13\tau/t\le r,\quad rD^\gamma<1,\quad
 r<3s_0/4.
 \tag{2}
\]

Indeed, (m\le t/r^2+1\le2t/r^2) once (r^2\le t); the remaining conditions follow from the displayed powers of (D), with (t) fixed. The lower threshold on (D) may depend on (t). No uniform limit as (t\downarrow0) is being asserted.

## 1. Endpoint exclusion and local lifts

On (\mathcal C_v), both the trial and (c) move by at most (s_0/8) from their initial point during ([0,h_0]). Their torus distance therefore exceeds (s_0-2s_0/8=3s_0/4>r) throughout that window. Time reversal gives the same exclusion in ([2t-h_0,2t]).

Use the forward time coordinate on the first leg and the reversed coordinate on the second leg. Any interval that can contain a collision has starting time (s=j\tau\ge h_0-\tau\ge h_0/2) in that leg's coordinate.

For such an interval, the obstacle's lifted displacement is at most (rA_k(c)\le rD^\gamma<1). If a collision occurs while the trial is confined, then at the interval start (d(c(s),v)<10+r+rD^\gamma<12), after also requiring (r<1). Thus there is a unique lift (c_s) within radius twelve of the chosen lift of (v): two such lifts would differ by a nonzero vector of length at least (K>50), while their mutual distance would be less than twenty-four. Continue this lift over the interval; it stays within radius thirteen. The trial stays within radius ten. At a collision, these lifts must realize the torus distance, since any other lattice translate has distance at least (K-23>r).

Every contributing interval consequently uses one deterministic local lift, with no sum over winding numbers. Obstacles may travel or wind arbitrarily between intervals; their global confinement is unnecessary.

## 2. Conditional bridge fluctuation

For a generator-(\Delta) bridge of duration (H) ending at (a), its segment after time (s) has the conditional representation

\[
 X_{s+q}=X_s+\frac q{H-s}(a-X_s)+R_q,
 \qquad0\le q\le\tau.
 \tag{3}
\]

Here (R) is independent of (X_s) and is a centered bridge of duration (L=H-s), restricted to ([0,\tau]). Its covariance is (2(\min(q,q')-qq'/L)I). To check independence directly, the bridge covariance gives

\[
 \operatorname{Cov}(X_s,X_{s+q})
 =2s\left(1-\frac{s+q}{H}\right)I
 =\left(1-\frac q{H-s}\right)\operatorname{Var}(X_s).
\]

The covariance of (X_s) with the residual in (3) is therefore zero. Joint Gaussianity gives independence. The residual covariance and mean identify its law, which does not depend on the prescribed endpoints.

Represent (R_q=W_q-(q/L)W_L), where (W) is Brownian motion with generator (\Delta). Since (\tau\le r^2) and (\tau\le L),

\[
 \mathbb E\left[\left(r^{-1}\sup_{q\le\tau}|R_q|\right)^3\right]\le C.
 \tag{4}
\]

For completeness, (mathbb E|W_u|^4=60u^2). Doob's fourth-moment inequality and the monotonicity of moment norms give

\[
 \mathbb E\sup_{q\le\tau}|W_q|^3
 \le(4/3)^3 60^{3/4}\tau^{3/2},\qquad
 \mathbb E|W_L|^3\le60^{3/4}L^{3/2}.
\]

Apply ((x+y)^3\le4(x^3+y^3)). The two contributions after division by (r^3) are bounded by constants times

\[
 \tau^{3/2}/r^3\le1,\qquad
 \tau^3/(r^3L^{3/2})
 = (\tau^{3/2}/r^3)(\tau/L)^{3/2}\le1.
\]

This proves (4) without conditioning on the trial cutoff. The number sixty is checked independently by expanding ((W_1^2+W_2^2+W_3^2)^2): three diagonal terms contribute (3\cdot12u^2), and six cross terms contribute (6\cdot4u^2).

## 3. A leg with a uniformly chosen midpoint

First consider a duration-(t) leg from (y) to (U), conditionally on (U=u). The reversed second leg has exactly the same form with (z) as its starting endpoint.

For (s\le t/2), (X_s) has covariance (2s(1-s/t)I\ge sI), so its density is at most ((2\pi s)^{-3/2}), independently of (u,y). On the cutoff, (|X_s-v|\le10), and (|u-v|<2). In (3), the drift over the interval is at most (24\tau/t), since (t-s\ge t/2). Require (24\tau/t\le r), an additional fixed-geometric-constant instance of (2); this again only enlarges the threshold on (D).

Let (B_s=r^{-1}\sup_{q\le\tau}|R_q|). A collision on the interval, together with (\mathcal C_v), implies

\[
 |X_s-c_s|\le r(2+A_k(c)+B_s).
 \tag{5}
\]

Discard the cutoff after obtaining this necessary event. The center (c_s) is deterministic, and (B_s) is independent of (X_s) conditionally on (u), with the endpoint-independent moment bound (4). Integrating the density over the ball in (5) yields

\[
 \mathbb P(\mathcal C_v\cap\{\text{collision in interval }k\}\mid U=u)
 \le Cr^3(1+A_k(c))^3s^{-3/2}.
 \tag{6}
\]

Indeed, the ball volume is (4\pi r^3(2+A_k+B_s)^3/3), and ((2+A_k+B_s)^3\le C((1+A_k)^3+B_s^3)). Average (6) over (u); the bound is unchanged. Neither regularity nor confinement has been imposed on the unrestricted law in this integration.

For (s>t/2), the preceding density bound would become singular near the midpoint. Instead write

\[
 X_q=(1-q/t)y+(q/t)U+\beta_q,
\]

where the entire centered bridge (\beta) is independent of (U). Conditional on (\beta), the density of (X_s) is at most ((t/s)^3\le8): this is the Jacobian of a scaled uniform unit cell. Put

\[
 \widetilde B_s=r^{-1}\sup_{q\le\tau}|\beta_{s+q}-\beta_s|.
\]

Writing (\beta_q=W_q-(q/t)W_t) and applying the same fourth-moment calculation to the Brownian increments gives (mathbb E\widetilde B_s^3\le C). Independence of those increments from (X_s) is not needed. The linear mean moves by at most (5\tau/t\le r), uniformly in (U), since both possible outer endpoints are within radius three and (U) is within radius two.

A collision again implies (5), now with (\widetilde B_s). Conditional on (\beta), the ball radius is fixed while (U) remains uniform. Integrate over (U) first, using the density bound eight, then over (\beta). The result is

\[
 \mathbb P(\mathcal C_v\cap\{\text{collision in interval }k\})
 \le Cr^3(1+A_k(c))^3.
 \tag{7}
\]

This argument includes the final interval ending at the midpoint. It avoids any independence assertion between (X_s) and the centered bridge increment.

## 4. Mesh sum

Let (n=\lceil h_0/(2\tau)\rceil\ge1). Monotonicity and an integral give

\[
 \sum_{j\ge n}(j\tau)^{-3/2}
 \le\tau^{-3/2}(n^{-3/2}+2n^{-1/2})
 \le\frac{3\sqrt2}{\tau\sqrt{h_0}}
 \le\frac{6\sqrt2}{r^2\sqrt{h_0}}.
 \tag{8}
\]

The possible lack of an integer endpoint for (t/2\tau) does not matter: extending the finite sum to infinity increases it. As a second bound, (s\ge\tau) implies

\[
 s^{-3/2}\le\frac{2^{3/2}}\tau\int_s^{s+\tau}x^{-3/2}\,dx.
\]

Sum these disjoint integrals from (s=n\tau\ge h_0/2). Their total is at most (8/(\tau\sqrt{h_0})), confirming the same scale independently, including (n=1).

For the early intervals use ((1+A_k)^3\le8D^{3\gamma}), then (6) and (8), on both legs. Their total is at most

\[
 C r^3D^{3\gamma}\frac1{r^2\sqrt{h_0}}
 = C\frac{rD^{3\gamma}}{\sqrt{h_0}}.
 \tag{9}
\]

For the late intervals use (1) and (7). Their total is at most

\[
 Cr^3\sum_{k=1}^{2m}(1+A_k)^3
 \le2CC_{\rm reg}r^3m
 \le4CC_{\rm reg}tr,
 \tag{10}
\]

where (m\le2t/r^2). Equations (9) and (10) prove the claimed estimate for (Q^B_{y,z}).

## 5. The ordinary duration-(2t) bridge

Use the forward orientation on ([0,t]) and the reversed orientation on ([t,2t]). For each oriented interval start (0<s\le t), (3) has (H=2t) and remaining duration (2t-s\ge t). Its time-(s) covariance is (2s(1-s/(2t))I\ge sI), hence its density is at most ((2\pi s)^{-3/2}). On the cutoff the drift is at most (13\tau/t\le r), since the terminal endpoint has distance at most three from (v).

Endpoint exclusion, (4), (5), and (6) consequently apply on every interval of either orientation. Sum using (8) and the maximum part of (1). This proves the slightly stronger bound

\[
 Q^0_{y,z}(\mathcal C_v\cap\mathcal H(c))
 \le C rD^{3\gamma}/\sqrt{h_0}.
\]

Adding the nonnegative (Ctr) term gives the common statement in the source.

Finally,

\[
 tr=\alpha tD^{-1},\qquad
 rD^{3\gamma}h_0^{-1/2}
 =\alpha D^{-1+1/4+1/2}=\alpha D^{-1/4}.
\]

Both terms tend to zero for every fixed (t>0). This establishes the quoted estimate in the large-torus regime needed by the application.

## Uniformity and boundary checks

The constants use only fixed endpoint bounds, the cell volume, dimension, and (C_{\rm reg}). They do not depend on the obstacle's detailed shape, location, global winding, or any other obstacle. Thus the bound applies to each permitted deterministic opponent even if different opponents collide with one another. Mutual avoidance never entered the argument.

Endpoint separation is essential. If (d(y,c(0))\le r), collision holds at time zero. Midpoint averaging is also essential for the two-leg law. For a prescribed midpoint (u=c(t)), collision is certain at time (t); the proof makes no estimate uniform in a prescribed midpoint. Restricting the uniform midpoint to a measurable subset of volume at least (a>0) costs at most (a^{-1}) for a nonnegative event, and conditioning on a success event of probability at least (b>0) costs at most (b^{-1}). Such costs must be paid after the unconditioned estimate, as in the prior insertion argument.

The event (\mathcal C_v) is used for endpoint exclusion, lift localization, and drift control, then discarded in a necessary-event upper bound. No independence of the cutoff and the collision event, and no conditional Gaussianity given the cutoff, has been assumed.

The estimate removes the single-path collision assumption from the earlier conditional insertion check. It does not establish the conditional reference law, the thermal certificate supply, the encounter estimate for routes, or the condensation theorem.
