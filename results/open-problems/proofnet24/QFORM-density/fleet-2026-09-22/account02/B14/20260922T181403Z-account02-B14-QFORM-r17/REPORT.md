SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B14, 2026-09-22T18:14:03Z.
attacking: mass-linear localization of half-Riesz Schur debts, with arbitrary shifts/fragments and no moment assumptions.

# account02/B14 — mass-cap Riesz localization and scalar-to-zero-diagonal compiler

Programme: QFORM-DENSITY-3EIG-20260922. Control observed at startup: yspennstate/math-research-brain@3b341648e9a7186a0eb3299c4fdda50d3d2245bf, OWNER CONTROL 2026-09-22.10; refreshed before publication to main 0408eca2e2dd4b837a318a4470474d7b90905a65, OWNER CONTROL 2026-09-22.11. Full QFORM remains OPEN. Execution: WITHOUT_VERIFIED_BRAIN.

## 1. First unpaid implication and late correction

The live proof-first programme asks for a scalar-Q_rest conditional local-limit route. A later source-backed correction, QFORM-SCALAR-QREST-SUP-FALSE-v1 (brain commit 3dd2fc2dbfb1fb281b599bb3010623e57da3852a), gives a rotated Hadamard example for which sup_b ||p_(Q3|Q_rest=b)||_infinity is infinite although the same full quadratic form has a uniform density bound. Therefore this run does not pursue the false supremum gate. The correction itself proposes a weighted mixture/Lorentz replacement. The result below supplies an exact positive localization interface of that type for scalar-Schur half-Riesz debts.

A second fresh correction, QFORM-COAREA-AND-CONDITIONAL-MOMENT-CORRECTIONS-v1 (brain commit 938e59f2caed677576b8bb3cd87ee1ffe81ee572), refutes a universal positive moment of a fully vector-conditioned projection density. Nothing below conditions on the full orthogonal vector or assumes such a moment.

## 2. Sharp finite-mass density-to-Riesz inequality

### Theorem A (mass-cap Riesz interpolation)

Let mu be a finite positive measure on R, of mass w, absolutely continuous with density g satisfying 0<=g<=D. Let 0<alpha<1. Then, uniformly in t,

\[
\boxed{
\int |y-t|^{-\alpha}\,d\mu(y)
\le
\frac{2^\alpha}{1-\alpha}\,D^\alpha w^{1-\alpha}.
}
\tag{A}
\]

The constant is sharp for the class with given (w,D): equality is attained by g=D 1_[t-w/(2D),t+w/(2D)] when w,D>0.

Proof. The kernel r -> r^{-alpha} is symmetric decreasing about t. Among all 0<=g<=D of mass w, the bathtub/rearrangement principle puts density D on the centered interval of length w/D. Hence

\[
\int |y-t|^{-\alpha}g(y)dy
\le
2D\int_0^{w/(2D)}r^{-\alpha}dr
=
\frac{2^\alpha}{1-\alpha}D^\alpha w^{1-\alpha}.
\]

The degenerate w=0 case is trivial. If D=0 then necessarily w=0.

For alpha=1/2,

\[
\boxed{
\sup_t\int|y-t|^{-1/2}d\mu(y)
\le 2\sqrt2\,\sqrt{Dw}.
}
\tag{A1/2}
\]

No support, moment, translation or regularity hypothesis appears.

### Theorem B (positive-mixture ledger)

Suppose mu=sum_k mu_k is a finite or countable positive decomposition, where mu_k has mass w_k and density cap D_k. Then

\[
\sup_t\int |y-t|^{-\alpha}d\mu(y)
\le
\frac{2^\alpha}{1-\alpha}
\sum_k D_k^\alpha w_k^{1-\alpha}
\le
\frac{2^\alpha}{1-\alpha}
\Big(\sum_kD_k\Big)^\alpha
\Big(\sum_kw_k\Big)^{1-\alpha}.
\tag{B}
\]

The second inequality is Holder. In particular, if sum_k w_k=1 and the normalized output law of piece k has density cap C_k, then D_k=w_k C_k and

\[
\boxed{
\sup_t\int |y-t|^{-\alpha}d\mu(y)
\le
\frac{2^\alpha}{1-\alpha}
\Big(\sum_k w_k C_k\Big)^\alpha.
}
\tag{B'}
\]

Thus the correct localization currency is the mass-weighted density-cap budget sum w_k C_k. One need not control sup_k C_k.

This is exactly compatible with arbitrary shifts: translating each mu_k changes neither w_k nor D_k.

## 3. Why normalization before aggregation is genuinely dangerous

The exponent of the piece mass in (A) is sharp. Let N pieces have

\[
d\mu_k(y)=1_{[0,1/N]}(y)dy,
\]

so w_k=1/N and D_k=1. Their sum has density N on [0,1/N], and

\[
\int |y|^{-\alpha}d\Big(\sum_k\mu_k\Big)(y)
=
\frac{N^\alpha}{1-\alpha}.
\]

Hence an argument that slices into N tiny pieces but retains an O(1) unnormalized output cap for every piece can lose N^alpha. In contrast, if each piece carries D_k<=C w_k, then sum D_k<=C and (B) is dimension/fragment free. This is a proof-mechanism counterexample, not a QFORM counterexample.

## 4. Scalar-Schur compiler

Let X be independent of Y and have density <=1. Suppose, after conditioning on any additional outside coordinates, a quadratic form can be written

\[
Q=aX^2+2X\,u^TY+dX+R_0(Y),\qquad a\ne0.
\]

Completing the square conditionally on Y gives

\[
Q=a\Big(X+\frac{u^TY+d/2}{a}\Big)^2+R(Y),
\]

where

\[
R(Y)=R_0(Y)-\frac{(u^TY+d/2)^2}{a}.
\]

For fixed Y=y, the shifted X still has density cap one. The density of a(X-h)^2 obeys the exact envelope

\[
p_{a(X-h)^2}(s)\le |a|^{-1/2}|s|^{-1/2}.
\]

Consequently

\[
\boxed{
\|p_Q\|_\infty
\le |a|^{-1/2}\sup_t E|t-R(Y)|^{-1/2}.
}
\tag{S}
\]

Now decompose the Y-law into positive subprobability pieces of masses w_k. If the pushforward of piece k under R has density cap D_k=w_k C_k, then Theorem B gives

\[
\boxed{
\|p_Q\|_\infty
\le 2\sqrt{\frac{2}{|a|}}
\Big(\sum_k w_k C_k\Big)^{1/2}.
}
\tag{SC}
\]

This is the requested localization compiler: arbitrary fragment number, shifts, distant supports and unbounded supports cost nothing provided the ordinary remainder-density certificates are aggregated with their original masses before normalization. No moment assumption is introduced.

## 5. Application of the completed partner result account03/B14 r15

Partner source applied: yspennstate/math-open-problems@49f1c21b47979575eaa8c34b90d066c8034140b4, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260922T173618Z-account03-B14-QFORM-r15/REPORT.md`.

That report proves: for independent cap-one X,Y,Z and every affine vector, if

\[
B=\begin{pmatrix}0&b_{12}&b_{13}\\ b_{12}&0&b_{23}\\ b_{13}&b_{23}&0\end{pmatrix},\qquad \det B\ne0,
\]

then

\[
\|p_{Y^TBY+\ell^TY+c}\|_\infty
\le C_{off}|\det B|^{-1/3},
\quad C_{off}=21\,2^{1/3}e^{-2/3}<13.585,
\]

uniformly in the affine term, shifts and supports.

Apply this to a four-coordinate physical block with scalar pivot a!=0. Write the block as

\[
\begin{pmatrix}a&u^T\\u&C\end{pmatrix}
\]

and let its three-coordinate Schur remainder be

\[
B=C-uu^T/a.
\]

If B has zero physical diagonal and det B!=0, then after conditioning on every outside coordinate the induced linear term in the triple is arbitrary but partner r15 applies uniformly. Thus R has density cap

\[
C_R=C_{off}|\det B|^{-1/3}.
\]

Putting this into (SC) with one piece gives the new hybrid branch

\[
\boxed{
\|p_Q\|_\infty
\le
2\sqrt{2C_{off}}\,|a|^{-1/2}|\det B|^{-1/6}
<10.425\,|a|^{-1/2}|\det B|^{-1/6}.
}
\tag{H}
\]

The bound survives arbitrary extra dimensions because the outside coordinates only induce affine terms and constants after conditioning; the partner theorem is uniform over them. If |a|>=1 and |det B|>=1, this branch closes with constant <10.425.

This is not a proof that the three-large-eigenvalue hypothesis forces such a pivot/Schur triple. The structural existence step remains unpaid.

## 6. Relation to the late scalar-Q_rest correction

QFORM-SCALAR-QREST-SUP-FALSE-v1 refutes replacing the full mixture by sup_b of conditional density caps. Theorems A-B identify a strictly weaker and source-compatible obligation: retain the scalar mixture weights and prove a finite weighted cap budget (or directly a finite sum D_k) before taking the half-Riesz transform. Rare conditional fibers may have arbitrarily large normalized caps provided their unnormalized density-cap mass is summable.

For a scalar parameter B with law nu, a discretized/partitioned version reads: if on cells E_k of nu-mass w_k one can prove an unnormalized remainder-output density cap w_k C_k and sum w_k C_k<=Cbar, then the scalar-Schur contribution is bounded by 2 sqrt(2 Cbar/|a|), with no sup_k C_k. This is precisely the type of weighted mixture norm suggested by the correction.

## 7. Status and next implication

FULL QFORM: OPEN. New supporting results: Theorems A-B, scalar-Schur compiler (SC), and the partner-composed zero-diagonal Schur branch (H). No false unrestricted rank-three coarea lemma, no vector-conditioned positive moment, no scalar-Q_rest conditional supremum, no rotated independence, no pointwise Fourier decay, and no support/moment assumption is used.

First unpaid B14 implication: on the surviving general scalar-Schur branches, prove a dimension-free mass-weighted density-cap budget for the Schur remainder after scalar Q_rest localization, rather than a uniform conditional cap; or construct a source-valid product-law example where even that weighted budget diverges while the full output remains bounded. The distinction is target-relevant because (SC) converts any such weighted budget immediately into an unconditional density bound.
