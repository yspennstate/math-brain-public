# fleet03/B20 r28 early substantive checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`. Full target remains open.

## QFORM-NEARKERNEL-TO-HUB-CROSS-PACKET-v1 (checkpoint form)

Let the exact-rank-three target be

\[
A=U\Lambda U^T,\qquad U^TU=I_3,\qquad s_{\min}(\Lambda)\ge 1.
\]

Take an ORIGINAL-coordinate partition `I sqcup J`, put `B=A[I,I]`, `C=A[I,J]`, and assume the current rank-two-cross packet supplies a unit vector `r in range(U_I)` with

\[
C^Tr=0,\qquad \|Br\|_2<\varepsilon.
\]

Padding `r` by zero on `J` gives `\tilde r`, and

\[
A\tilde r=(Br,C^Tr)=(Br,0).
\]

Hence

\[
\|U_I^Tr\|_2=\|U^T\tilde r\|_2\le \|A\tilde r\|_2<\varepsilon,
\]

because every nonzero singular value of `A` is at least one. Since `r` is a unit vector in `range(U_I)`, the least singular value of `U_I` is `<epsilon`; equivalently, with `G=U_I^TU_I`,

\[
\boxed{\lambda_{\min}(G)<\varepsilon^2.}
\]

Thus there is a spectral unit vector `w` with ORIGINAL-bank frame masses

\[
\boxed{\|U_Iw\|_2^2<\varepsilon^2,\qquad \|U_Jw\|_2^2>1-\varepsilon^2.}
\]

At the live packet threshold `epsilon=1/64`, every near-kernel survivor is therefore a `1/4096` near-coloop, stronger than the earlier `1/64` frame-mass localization.

Now use the completed ridge-window theorem. If every physical spectral leverage

\[
c_k=\|U^Te_k\|_2^2
\]

is at most `1/32`, then the full exact-rank-three law has a continuous density `<64`. Hence an unpaid near-kernel survivor has some physical coordinate `j` with `c_j>1/32`.

The exact-rank-three row norm obeys

\[
\|Ae_j\|_2^2=u_j^T\Lambda^2u_j\ge c_j>1/32.
\]

If `|A_jj|>=1/32`, the completed exact-rank-three physical-pivot theorem gives

\[
\|p_Q\|_\infty\le 128/\sqrt{|A_{jj}|}\le128\sqrt{32}<725.
\]

Thus every still-unpaid survivor has `|A_jj|<1/32`, and its physical off-diagonal star `b=A[j,-j]` satisfies

\[
\boxed{\|b\|_2^2>1/32-1/1024=31/1024.}
\]

The same argument shows that in a still-unpaid state every physical diagonal is `<1/32` in magnitude. Let `K=A[-j,-j]`. Since

\[
A-\operatorname{diag}(0,K)
\]

has rank at most two, Eckart--Young and `s_3(A)>=1` give `\|K\|_{op}>=1`. Therefore, with `Z=K-diag(K)`,

\[
\|Z\|_{op}>31/32.
\]

Apply fleet01/B20's completed zero-diagonal disjointization lemma: there is a physical partition `L sqcup R=-j` such that

\[
\boxed{\|D\|_{op}=\|A[L,R]\|_{op}>31/128.}
\]

Also one of the two star pieces has norm at least

\[
\boxed{\|b_R\|_2> b_0:=\sqrt{31/2048}=0.1230313730\ldots}
\]

after orienting the partition.

Let `s=\|D\|op` and let `v` be a top right singular vector of `D`. For the full physical cross block

\[
M=\begin{pmatrix}b_R^T\\D\end{pmatrix}
\]

between `{j} union L` and `R`, row-compress by the hub row and a top left singular vector of `D`. Singular-value monotonicity gives

\[
\boxed{s_1(M)s_2(M)\ge s\,\operatorname{dist}(b_R,\mathbb Rv).}
\]

Consequently, with `eta=b_0/2`, either

\[
\boxed{s_1(M)s_2(M)> (31/128)(b_0/2)=0.0148983303\ldots}
\]

or the hub star is quantitatively aligned with the top complement-cross direction,

\[
\boxed{s\,|\langle b_R,v\rangle|>
(31/128)(\sqrt3/2)b_0=0.0258046651\ldots.}
\]

This is a product-preserving ORIGINAL-coordinate packet; no rotated coordinates are declared independent.

## Required fleet04/B20 application

Use fleet04/B20 r4, theorem `QFORM-PARTITIONED-NEAR-NULL-HYBRID-v1` (`math-open-problems@f97aa31585b7b547a116d4580f898576af4e0842`). If the heavy row above has leverage `c_j>=1/2` and every other spectral frame row is genuinely partitioned into the longitudinal line `Re` or transverse plane `e^perp`, where `u_j=sqrt(c_j)e`, then its spectral Rayleigh coefficient is

\[
|a|=|e^T\Lambda e|=|A_{jj}|/c_j< (1/32)/(1/2)=1/16<1/2.
\]

The partner theorem therefore applies at its actual hypothesis and gives

\[
\boxed{\|p_Q\|_\infty<105.463}
\]

(essential boundedness; the partner report does not upgrade global continuity). Thus, in the `c_j>=1/2` part of this near-kernel branch, every unpaid survivor must contain a genuinely mixed residual physical spectral row. This is an equation-level use of the designated partner, not a scope extension.

## Remaining step after this checkpoint

Pay the new fixed-strength hub-cross packet when (i) `1/32<c_j<1/2`, or (ii) `c_j>=1/2` but mixed residual rows obstruct the partner's exact longitudinal/transverse product partition. The next mechanism should spend the mixed-row overlap through D'/D5/volume or a rank-two-cross receiver, not by treating the mixed component as a small random perturbation.
