# Independent adversarial audit: same-sign, positive-correlation extension

**Disposition.** I find no deterministic counterexample to the proposed same-sign selector or its inherited reflected continuation. The route can support a two-input positive-\(\rho\) theorem when combined with the already reviewed all-mixed theorem, but the new proof must explicitly establish the selected pre-axis law, protect the inherited endpoint at the random axis time, and prove support persistence before invoking a relay formula. I checked these points against `runs/20261023T232238Z/{BOUNDARY_GRID,MACRO_COMPACTNESS}.md`, `runs/20261024T012528Z/REFLECTION_SELECTOR.md`, and `runs/20261024T021857Z/{ALL_MIXED_LIMIT,GLOBAL_REFLECTION}.md`. The existing all-mixed entrance theorem cannot be restarted at the axis: its zero-endpoint initial condition is false here.

## Frozen selector and pre-axis law

For \(R_1,R_2>0\) and \(z>0\), every active projection receives a strictly positive increment, and even an inactive projection receives a strictly positive \(\rho\)-coupled increment while the other is active. Thus any initially active positive-\(z\) row reaches the strict `++` sector in finitely many frozen steps and stays there as long as both residuals are positive. An initially `--` row is exactly stationary. For \(z<0\), each active coordinate decreases by at least \(\gamma |z|R_j\) per step, and both coordinates are nonincreasing, so the row dies in finitely many steps. A finite strict history transfers by `BOUNDARY_GRID`; use a finite marked cutoff and localize its random maximum certificate index before removing cutoffs. The original-mark axis equalities lie on the same countable null hyperplanes as in that theorem.

Consequently the selected mass is
\[
P^+=\int_{z>0}z^2\mathbf1\{(Xu)_1>0\ \text{or}\ (Xu)_2>0\}\,N(dz,du).
\]
It is finite and positive almost surely and independent of \((F,C)\). With \(p_{\rm act}=\Pr\{(XU)_1>0\text{ or }(XU)_2>0\}\), its Laplace transform is \(\exp[-c p_{\rm act}\Gamma(1-\alpha/2)\lambda^{\alpha/2}]\) under the intensity convention of `BOUNDARY_GRID`. The negative same-sign case uses \(P^-\) from \(z<0\) with the same mask and law. Do not substitute the half-mark masses of the initial mixed cone: the mask here is **any active projection**.

On the strictly positive residual phase, every retained row has the macroscopic endpoint \(q_{z}(t)=zGI(t)\), \(I=\int_0^t r\), and dead rows contribute zero. Hence \(r'=-(C+P^+G)r\) up to the first axis time. This should be proved by the fixed-cutoff selection and uniform small-\(|z|\) square-mass estimate, not read off from an unselected inclusion.

## Axis crossing and the inherited offset

The original-coordinate ray formula makes \(C_{12}>0\) almost surely: \(\rho=\sum_\ell x_{1\ell}x_{2\ell}>0\) gives an \(\ell\) with a positive coordinate product; one of its two signed ReLU rays has both coordinates positive and has strictly positive stable square mass. Thus \(Q_{12}=(C+P^+G)_{12}>0\). If \(e^{-Qt}R\) first touches an axis at finite \(\tau\), the other residual is strictly positive and the touched residual has derivative \(-Q_{12}r_{\rm other}<0\). The hit is transversal. A no-finite-hit branch is mathematically harmless: the constant-\(Q\) law remains valid on every fixed horizon. It has probability zero here, if desired: for positive \(R\), no hit requires \(R\) to lie on the positive fast eigenray of \(Q\). Since \(R_1\ne R_2\) almost surely by the marginal density of \(R\), the condition \((C+P^+G)R\parallel R\) is linear in \(P^+\) with nonzero coefficient \(\rho(R_2^2-R_1^2)\). Conditional on \((R,C)\), the independent positive-stable \(P^+\) has a continuous law, so this event is null. The initialization theorem actually makes \(F,C,N\) mutually independent, although the argument here needs only independence of \(P^+\) from \((R,C)\).

The general *actual-subsequence* inclusion has \(Q_{\rm eff,12}(t)\ge C_{12}>0\) and bounded coefficients. From \(r_b(\tau)=0<r_p(\tau)\), variation of constants makes \(-r_b\) strictly positive immediately after \(\tau\); the bounded Metzler system for \((-r_b,r_p)\) then keeps the trajectory strictly mixed. This argument uses the unselected action and therefore does not assume the proposed post-axis law.

For a positive-\(z\) survivor, continuity of its pre-axis path gives
\[
q(\tau)=zGI(\tau)>0,\qquad
\eta(\tau):=q_p(\tau)-\rho q_b(\tau)
 =z(1-\rho^2)I_p(\tau)>0.
\]
Here \(b\) is the axis crossed into the negative residual and \(p\) is the still-positive residual. These are **nonzero inherited data**. On any maximal interval with \(q_p>0\), the inclusion yields \(q_b'=\rho z r_p>0\) whenever \(q_b<0\). The negative-part chain rule therefore gives \(q_b\ge0\). Meanwhile \(\eta'=z(1-\rho^2)r_p>0\). A first \(q_p=0\) would have \(\eta=-\rho q_b\le0\), a contradiction. Thus the supporting gate stays positive for this actual subsequential endpoint. Repeat atomwise and take a countable intersection; no population-wide support margin is needed.

The relay lemma in `REFLECTION_SELECTOR.md` is stated with \(a=zr_b\) bounded away from zero, whereas \(a(\tau)=0\). Since \(q_b(\tau)>0\), continuity gives a short ordinary both-active interval after \(\tau\); start that relay lemma at \(\tau+\delta\), where \(r_b<0\) is bounded away from zero on compact later intervals, and then let \(\delta\downarrow0\). Alternatively prove its reflection identity directly for continuous \(a\le0\). Calling the stated lemma at \(\tau\) without this bridge is a literal hypothesis gap.

The reflected normal is
\[
q_b(t)/z=\mathcal S\big(I_b+\rho I_p\big)(t),\qquad
q_p(t)/z=\rho\mathcal S\big(I_b+\rho I_p\big)(t)
 +(1-\rho^2)I_p(t).
\]
The cumulative driver is measured from time zero. On \([0,\tau]\) it is increasing, so this formula equals \(zGI\); after \(\tau\) its running minimum keeps the positive offset earned before the crossing. If reflection is instead restarted at \(\tau\), its initial level must be \(q_b(\tau)/z\), not zero. Resetting to zero gives a wrong, discontinuous endpoint/output law. For example \(\rho=1/2\), \(Q=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}\), \(R=(3,1)\) has the second residual crossing at \(\tau=(\log2)/2\), but \((GI(\tau))_2=1/2\), not zero.

## Stronger same-sign simplification: at most one face capture

There is a useful further consequence that I independently checked. If the axis-crossed coordinate is \(b\), write \(r_b=-k r_p\) after \(\tau\), so \(k(\tau)=0\). While the inherited normal \(V_b>0\), the residual still follows the same constant \(Q=C+P^+G\). In \((b,p)\) order put \(Q=\left(\begin{smallmatrix}a&b_0\\b_0&d\end{smallmatrix}\right)\), \(b_0>0\). Then
\[
k'=b_0+(d-a)k-b_0k^2.
\]
Its unique positive root \(\kappa\) attracts the trajectory monotonically from \(k=0\). The unreflected normal driver \(w=(GI)_b\) has \(w'=r_p(\rho-k)\). If \(\kappa\le\rho\), it increases and never touches zero. If \(\kappa>\rho\), it increases and then decreases, with at most one positive-time zero. A finite face hit occurs exactly when \((GQ^{-1}R)_b<0\); equality gives only an asymptotic approach to zero. This criterion uses the full pre-face trajectory, including its positive offset from before \(\tau\).

At a finite hit \(k>\rho\), and the face action becomes \(Q_s=C+P^+(1-\rho^2)e_pe_p^T\). Its ratio field at \(k=\rho\) satisfies
\[
f_s(\rho)=C_{12}(1-\rho^2)+\rho(C_{pp}-C_{bb})
 +\rho P^+(1-\rho^2)=f_Q(\rho)>0,
\]
because \(\kappa>\rho\). The scalar comparison keeps \(k\ge\rho\) thereafter, so \(w'=r_p(\rho-k)\le0\) on the face and reflection never releases. Thus the same-sign continuation uses either no face or one permanent face, although the general initially mixed theorem still needs full release/recapture reflection. As an exact realizable-style diagnostic, \(\rho=1/2\), \(C=\left(\begin{smallmatrix}4&2\\2&7/4\end{smallmatrix}\right)\), \(P^+=1\), \(R=(4,1)\) gives \((GQ^{-1}R)_2=-1/10\), a first axis hit at about \(0.11648\), and a single later face hit at about \(1.67509\); the post-face ratio remains above \(\rho\). The numerical times check the algebra, not the stochastic proof.

## Scope and possible proof omissions

The \(R_1,R_2<0\) case is the exact sign mirror after putting \(s=-r\), \(J=-I\), and selecting initially active \(z<0\) rows. Its output contribution has the same sign in the residual equation, so the pre-axis matrix is \(C+P^-G\); the inherited reflected formula applies to \(J\). The two mixed orientations require the prior theorem plus an explicit input-label swap.

The all-initial claim remains conditional on writing these steps into the actual-grid subsequence proof. In particular, track selected endpoints jointly with the random axis time; use path continuity to pass \(q(\tau)=zGI(\tau)\), and invoke support positivity from the actual-subsequence inclusion before using relay uniqueness. Exact dead rows stay dead after the crossing. Remove finite cutoffs with the old uniform small-square-mass estimate, not a nonexistent common finite entrance time. Under those conditions I see no remaining obstruction specific to same-sign, positive-\(\rho\) data. This says nothing about negative correlation, more inputs, external novelty, or a pre-step tangent-kernel limit.
