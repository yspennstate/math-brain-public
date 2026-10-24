# Independent adversarial audit: positive-correlation mixed cone

**Disposition.** The frozen dead-or-certified-sliding classification in `agents/h01_entrance.md` passes its stated deterministic scope. The proposed stopped local law
\(Q=C+(1-\rho^2)\operatorname{diag}(P_1,P_2)\) is consistent with the prior finite boundary grid and actual-weight sliding estimate, conditional on the usual finite-cutoff/short-interval transfer. It cannot generally be extended beyond the first exit of the *ratio* cone with a fixed \(Q\). I found no counterexample to the later reflected continuation in `GLOBAL_REFLECTION.md`; its proof needs the precise countable-atom and sign-invariance arguments recorded in `reviews/h03_global_review.md`.

## Frozen certificate and robustness

For \(z>0,r=(-R,S)\), \(S>0,\rho S<R<S/\rho\), the four strict-gate velocities in h01 are correct. If the supporting coordinate \(y_0>0\), it increases by either \(\gamma zS\) or \(\gamma z(S-\rho R)\), both positive. The normal coordinate enters the stated invariant strip, and \(\eta=y-\rho x\) increases by exactly \(\gamma z(1-\rho^2)S\). Thus a finite index can achieve both a strict enlarged-strip interior and \(\eta>\rho\gamma D_*\). If \(y_0\le0\), the row is already dead or follows only the \(x\)-gate to a strict dead pair, except for affine threshold hyperplanes of zero mark probability. The negative-\(z\) statement is the coordinate mirror. For each *finite retained set* the strict certificates and finite histories admit a common open perturbation neighborhood. The probability-one conclusion over countably many PPP atoms follows by countable intersection, not a uniform certificate time or margin.

There is a useful weaker persistence fact after the ratio cone is left. Write the actual physical-grid normal update while the positive-\(z\) support is open as
\[
x_{n+1}=x_n+h(c_n-A_ns_n),\quad c_n=\rho z_nr_{2,n}>0,\quad d_n=-z_n(r_{1,n}+\rho r_{2,n}),\quad x_{n+1}=x_n-hd_n\text{ if }x_n>0.
\]
If \(r_{1,n}<0<r_{2,n}\), \(z_n>0\), \(d_n\le D\), and the certified state has \(x_N\ge-hD\), then \(x_n\ge-hD\) thereafter while support is open: off-side steps increase \(x\), and on-side steps end above \(-hD\). Also \(\eta_{n+1}-\eta_n=h(1-\rho^2)z_nr_{2,n}>0\). Hence \(\eta_N>\rho hD\) gives \(y_n\ge\eta_N-\rho hD>0\). The *upper* strip bound need not survive once \(d_n<0\), because the normal can release to macroscopic size. This is why the fixed Schur law stops at ratio exit even though support can persist.

## Exact ratio-exit diagnostic for the stopped law

For a fixed \(Q=\begin{pmatrix}a&b\\b&d\end{pmatrix}\) with \(b\ge0\), let \(k(t)=-r_1(t)/r_2(t)\) as long as \(r_1<0<r_2\) and \(r'=-Qr\). Direct differentiation gives
\[
k'=f(k):=b+(d-a)k-bk^2.
\]
The stopped fixed-\(Q\) law remains in \((\rho,1/\rho)\) if its vector field points inward at both endpoints, namely \(f(\rho)\ge0\) and \(f(1/\rho)\le0\). If \(f(\rho)<0\), any initial \(k\) sufficiently near \(\rho\) exits through the lower endpoint in finite time; similarly \(f(1/\rho)>0\) yields an upper exit from nearby starts. Equality can give asymptotic approach rather than a finite hit. The exact exit time is the first boundary hit of this scalar ODE, or equivalently of \(-[e^{-Qt}R]_1/[e^{-Qt}R]_2\).

Such exits have positive probability in the actual model. Take \(X\) with rows \((1,0)\) and \((\rho,\sqrt{1-\rho^2})\). Then \(C=A(1,\rho)(1,\rho)^T+B(0,\sqrt{1-\rho^2})(0,\sqrt{1-\rho^2})^T\) for independent positive stable \(A,B\). For \(Q=C+(1-\rho^2)\operatorname{diag}(P_1,P_2)\),
\[
f(\rho)=\rho(1-\rho^2)(B+P_2-P_1).
\]
The event \(P_1>B+P_2\) has positive probability, and independently the full-density initial residual can have \(k(0)>\rho\) sufficiently close to \(\rho\). Hence the ratio exits downward. This is a counterexample to ratio-cone invariance or a global constant-\(Q\) claim, **not** to a reflected continuation.

## Cutoff transfer that must be retained

The h01 certificate time is finite for each frozen mark but is unbounded as \(|z|\downarrow0\), the original mark grows, or the initial supporting projection approaches zero. To invoke `BOUNDARY_GRID.md`, first fix deterministic cutoffs \(\epsilon<|z|<M\), \(\|u\|<B\), localize the initial residual inside a compact double cone and the macro energy/residual bounds, and choose a deterministic boundary-step number \(N\) on an event of arbitrarily high probability. The finite-grid theorem then transports strict histories/certificates, after which the macro bootstrap and changing-weight sliding lemma apply on a positive physical interval. Finally remove mark and \(z\) cutoffs using `MACRO_COMPACTNESS.md`'s uniform small-atom output-increment bound. Finite-grid convergence alone at fixed \(N\) does not justify \(N\asymp L\), and a countable family of certificates does not supply a common positive support margin.

## Audit of the broader mixed-sign entrance proposal

The deterministic dead-or-persistent-support alternative actually extends to every frozen \(r_1=-R<0<S=r_2\) with \(\rho>0\), although the simple selector (8) need not. For \(z>0\), if \(y\) ever reaches \(\le0\), its gate switches off and the remaining \(x\)-only increments \((-\gamma zR,-\gamma\rho zR)\) lead to a strict dead pair in finitely many further steps, except on null affine thresholds. If \(y>0\) forever, \(\eta=y-\rho x\) grows by \(\gamma(1-\rho^2)zS\) every step. The normal recursion has off-side increment \(\gamma\rho zS>0\) and on-side decrement \(\gamma z(R-\rho S)\), which may be negative. For any \(D_*>\max\{z(R-\rho S),0\}\), the normal enters \(x>-\gamma D_*\) in finitely many steps and stays there. Eventually \(\eta>\rho\gamma D_*\), a strict one-sided support certificate. The mirror proof handles \(z<0\). This certificate is robust under bounded evolving mixed residuals and retained weight signs, as in the earlier one-sided induction.

The all-mixed selector can depend on \(\gamma\). For \(\rho=1/2,z=1,r=(-3,1),v_0=(1.1,0.4)\), at \(\gamma=1\) the first both-active step gives \((-1.4,-0.1)\), so the row dies. At \(\gamma=0.2\), three both-active steps give \((-0.4,0.1)\); from there the one-sided certificate is reached and the row survives. Thus any extension beyond the double cone must define \(P_1,P_2\) through the entire finite frozen orbit and allow dependence on \((R,\gamma)\); it cannot retain the independent stable thinning law or gamma-independence asserted only inside the double cone. The same fixed-cutoff/deterministic-\(N\) transfer and atomwise continuation strategy appears applicable, but this broader theorem needs its own written proof and review.
