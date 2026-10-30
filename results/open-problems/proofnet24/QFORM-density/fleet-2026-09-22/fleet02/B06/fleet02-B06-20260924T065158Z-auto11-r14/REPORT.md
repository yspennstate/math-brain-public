SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-24T06:51:58Z.
attacking: `QFORM-ADJUGATE-6465-TANGENTIAL-COLLAR-RECEIVER-v1`; first remove the finite-dimensional hub branch quantitatively, then leave only the genuinely rank-one-hub positive-normal collar.

# fleet02/B06 — finite hub compiler inside the 64/65 tangential collar

Programme: `QFORM-DENSITY-3EIG-20260922`. Full conjecture status: **OPEN / NOT PROVED / NOT DISPROVED**.

Fresh designated partner: fleet03/B06 run `20260924T062005Z-fleet03-B06-qform-r52`, canonical math commit `8e9f088eb1496f376287e67731b7906818ccd703`, theorem `QFORM-NORMAL-INNOVATION-COMPENSATED-CROSS-VOLUME-v1`. Its selected physical hub triple has actual hub block

\[
F=B+d e_he_h^T,
\]

and, after the literal scalar pivot, the complete two-row tail cross volume obeys

\[
a^2\det(NN^T)=W(D+d\theta)^2+d^2H,
\qquad \chi=H/(W\theta^2).
\]

The live unpaid positive-normal branch is `0<chi<1/64`; more than `64/65` of the selected adjugate curvature is tangential. The result below shows that this branch may additionally be assumed to have an **almost rank-one actual physical hub triple**. No fiber supremum is used.

## 1. Early obstruction: the collar does not force a normal floor

The complete calculation is in `EARLY_CALC.md` in this run directory. Briefly, take three flat orthonormal Walsh rows `w,v,u` on eight tail coordinates, put

\[
E=\binom{w}{v},\qquad q=(1/4,1/4),\qquad z_h=qE+\varepsilon u,
\]

and

\[
B=\begin{pmatrix}-3&1&1\\1&1&-1\\1&-1&1\end{pmatrix},
\qquad d=4.
\]

Then the actual literal hub block is

\[
F=B+\operatorname{diag}(4,0,0)
 =\begin{pmatrix}1&1&1\\1&1&-1\\1&-1&1\end{pmatrix},
\qquad \operatorname{spec}(F)=\{2,2,-1\},
\]

all three physical `2 x 2` hub principal blocks are singular, while

\[
\chi=8\varepsilon^2\to0,
\qquad D+d\theta=0,
\qquad \det(NN^T)=128\varepsilon^2.
\]

At the same time the complete mixed layers remain uniformly large:

\[
P_0=4,\qquad P_1=17/2+4\varepsilon^2,
\qquad P_2=9/2+8\varepsilon^2,
\qquad P=17+16\varepsilon^2.
\]

Thus neither retained layer mass nor diffuse two-/three-frame leverage forces a positive lower bound on `chi`, and large `P_1/P_2` does not force a useful physical pair.

The family is nevertheless an exact QFORM target: its full matrix has `F` as a principal block, so interlacing supplies two eigenvalues at least `2` and one at most `-1`. Applying the completed pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A from `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` to this literal three-coordinate block, uniformly over all conditioned tail values and induced affine terms, gives the real target inequality

\[
\boxed{\|p_{X^T A_\varepsilon X}\|_{\infty,\mathrm{ess}}\le 6\sqrt\pi.}
\]

So the construction refutes only the intermediate normal-floor / automatic-pair inference, not QFORM.

## 2. A deterministic pair-or-triple lemma for every physical `3 x 3` block

### Theorem — `QFORM-THREEHUB-S2-PAIR-OR-TRIPLE-COMPILER-v1`

Let `F` be any real symmetric `3 x 3` matrix and write its singular values

\[
s_1\ge s_2\ge s_3\ge0.
\]

If `s_2>0`, then one of the following holds:

1. `s_3>=s_2/4`; hence the full triple has minimum absolute eigenvalue at least `s_2/4`.
2. Some literal physical `2 x 2` principal block `C` of `F` satisfies

\[
\boxed{\sigma_{\min}(C)\ge s_2/6},
\qquad
\boxed{|\det C|\ge s_2^2/36}.
\]

In particular, no assumption about the signs of the eigenvalues or about a nonzero diagonal entry is needed.

### Proof

Assume `s_3<s_2/4`. Choose an orthonormal eigenbasis `u_1,u_2,u_3` with eigenvalues `lambda_k` ordered so that `|lambda_k|=s_k`. Pick a physical coordinate `i` with

\[
u_{3i}^2\ge1/3.
\]

Let `C=F[\{1,2,3\}\setminus\{i\},\{1,2,3\}\setminus\{i\}]`. Its determinant is the `i`th diagonal cofactor,

\[
\det C=e_i^T\operatorname{adj}(F)e_i.
\]

The spectral adjugate identity gives

\[
\operatorname{adj}(F)
 =\lambda_2\lambda_3 u_1u_1^T
 +\lambda_1\lambda_3 u_2u_2^T
 +\lambda_1\lambda_2 u_3u_3^T,
\]

with the same polynomial identity valid at a singular endpoint. Therefore

\[
\begin{aligned}
|\det C|
&\ge s_1s_2u_{3i}^2-s_1s_3u_{2i}^2-s_2s_3u_{1i}^2\\
&\ge s_1\bigl[s_2u_{3i}^2-s_3(1-u_{3i}^2)\bigr]\\
&\ge \frac{s_1}{3}(s_2-2s_3)
>\frac{s_1s_2}{6}.
\end{aligned}
\]

Since a principal compression cannot have operator norm exceeding `||F||=s_1`,

\[
\sigma_{\max}(C)\le s_1.
\]

For an invertible symmetric `2 x 2` matrix,

\[
\sigma_{\min}(C)=\frac{|\det C|}{\sigma_{\max}(C)}
>\frac{s_2}{6}.
\]

The determinant lower bound follows because `sigma_max(C)>=sigma_min(C)`. This proves the dichotomy. QED.

## 3. Target-level density compiler

Now let `F=A[H,H]` be any literal physical `3 x 3` principal block of a full QFORM target `A`, so `s_3(A)>=1` in singular-value notation. Put

\[
\tau:=\sigma_2(F)=s_2.
\]

If the triple branch of the theorem holds, conditioning on every coordinate outside `H` leaves the same quadratic block `F` and only changes affine terms. The completed pinned Theorem A gives

\[
\boxed{
\|p_Q\|_\infty\le \frac{24\sqrt\pi}{\tau}.
}
\tag{3.1}
\]

If the pair branch holds and the selected physical pair `C` is definite, the two-dimensional area bound gives

\[
\boxed{
\|p_Q\|_\infty\le \frac{\pi}{\sqrt{|\det C|}}
\le \frac{6\pi}{\tau}.
}
\tag{3.2}
\]

If `C` is indefinite, apply the completed arbitrary-rank physical-pair theorem at
`math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`. Its hypotheses are exactly the present original-coordinate pair plus `s_3(A)>=1`; all outside couplings and affine terms are retained. Since

\[
D_C:=|\det C|\ge \tau^2/36,
\qquad
\kappa_C:=\sigma_{\min}(C)\ge\tau/6,
\]

its bound becomes

\[
\boxed{
\|p_Q\|_\infty
\le 3\,400^{1/3}\,6^{5/6}\,\tau^{-5/6}
<98.387\,\tau^{-5/6}.
}
\tag{3.3}
\]

This is a genuine product-preserving receiver: the pair theorem completes two literal original coordinates and keeps the arbitrary-rank Schur remainder rather than taking a spectral-fiber maximum.

At the concrete scale relevant to the current collar, if

\[
\boxed{\sigma_2(F)\ge1/64,}
\]

then one of (3.1)--(3.3) gives the uniform all-level bound

\[
\boxed{\|p_Q\|_\infty<3149.}
\tag{3.4}
\]

The worst of the three displayed constants at `tau=1/64` is the indefinite-pair value `3148.357...`.

## 4. Consequence for the designated partner's 64/65 collar

The early obstruction has `sigma_2(F)=2`, so it is automatically routed through the localized-triple branch; it no longer belongs to the analytic collar debt.

Consequently, after the designated partner's already-paid branches are removed, the genuinely unresolved positive-normal packet may be sharpened to the simultaneous conditions

\[
\boxed{
0<\chi<1/64,
\qquad
\sigma_2(F)<1/64.
}
\tag{4.1}
\]

Together with the partner's identity

\[
\frac{H}{t^T\operatorname{adj}(G)t}<\frac1{65},
\qquad
\frac{W\theta^2}{t^T\operatorname{adj}(G)t}>\frac{64}{65},
\]

(4.1) says that the remaining obstruction is not merely a small positive normal innovation: the **actual physical three-hub quadratic block is itself within operator distance `1/64` of rank one**. Any branch with a quantitatively two-dimensional hub action is already paid by (3.4).

This reduction is independent of the tail dimension, keeps every conditioning weight, and does not rotate the input law.

## 5. First unpaid implication

The first unpaid implication is now

`QFORM-R52-RANKONE-HUB-TANGENTIAL-COLLAR-v1`:

> In the partner r52 low-disjointness packet, assume `0<chi<1/64`, `sigma_2(F)<1/64`, the diffuse two-frame leverage gate, and the retained layer-0/1/2 curvature mass. Use the near-rank-one **physical** hub block together with the `>64/65` tangential adjugate curvature to obtain an all-level product-preserving receiver, or route to the finite heavy-tail-hub endpoint. The small rank-two part of `F` cannot simply be discarded on arbitrary unbounded product inputs.

This is strictly narrower than the previous `QFORM-ADJUGATE-6465-TANGENTIAL-COLLAR-RECEIVER-v1`: all quantitatively two-dimensional hub blocks, including the explicit normal-floor obstruction above, have been removed by a source-valid target-level payment.

No moments, support bounds, log-concavity, Gaussianity, identical laws, diagonal-basis assumption, or post-rotation independence are used. Continuity remains separate from the essential density bounds above.
