SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-24T07:05:53Z.
attacking: `QFORM-ADJUGATE-6465-TANGENTIAL-COLLAR-RECEIVER-v1`; remove every quantitatively two-dimensional physical three-hub block before treating the genuinely rank-one-hub positive-normal collar.

# fleet02/B06 r15 — finite hub compiler inside the 64/65 tangential collar

Programme: `QFORM-DENSITY-3EIG-20260922`. Full conjecture status: **OPEN / NOT PROVED / NOT DISPROVED**. Execution context: `WITHOUT_VERIFIED_BRAIN`.

Fresh designated partner consumed: fleet03/B06 run `20260924T062005Z-fleet03-B06-qform-r52`, canonical math commit `8e9f088eb1496f376287e67731b7906818ccd703`, result `QFORM-NORMAL-INNOVATION-COMPENSATED-CROSS-VOLUME-v1 + QFORM-NORMAL-TANGENTIAL-ADJUGATE-SPLIT-v1`.

Its selected physical hub triple has actual hub block

\[
F=B+d e_he_h^T,
\]

and after the literal scalar pivot the complete two-row tail cross volume satisfies

\[
a^2\det(NN^T)=W(D+d\theta)^2+d^2H,
\qquad \chi=\frac{H}{W\theta^2}.
\]

The live unpaid branch has `0<chi<1/64`; equivalently more than `64/65` of the selected adjugate curvature is tangential. The result below removes every case in this collar where the actual physical hub block has a quantitative second singular value.

## 1. Structural obstruction: small positive normal innovation need not be bounded below

Take three flat orthonormal Walsh rows `w,v,u` on eight original tail coordinates and put

\[
E=\binom{w}{v},\qquad q=(1/4,1/4),\qquad z_h=qE+\varepsilon u.
\]

Let

\[
B=\begin{pmatrix}-3&1&1\\1&1&-1\\1&-1&1\end{pmatrix},
\qquad d=4.
\]

Then the actual literal hub block is

\[
F=B+\operatorname{diag}(4,0,0)
=\begin{pmatrix}1&1&1\\1&1&-1\\1&-1&1\end{pmatrix},
\qquad \operatorname{spec}(F)=\{2,2,-1\}.
\]

Every physical `2 x 2` hub principal block is singular. In the partner notation one has

\[
W=1,\quad D=-4,\quad \theta=1,\quad H=8\varepsilon^2,
\quad \chi=8\varepsilon^2\to0,
\quad D+d\theta=0,
\]

so

\[
\det(NN^T)=128\varepsilon^2.
\]

Nevertheless the complete mixed layers stay uniformly large:

\[
P_0=4,\qquad P_1=17/2+4\varepsilon^2,
\qquad P_2=9/2+8\varepsilon^2,
\qquad P=17+16\varepsilon^2.
\]

Thus retained layer mass plus diffuse two-/three-frame leverage does **not** force a positive lower bound on `chi`, and large `P_1/P_2` does not force a useful physical pair.

This family is not a QFORM counterexample. Its full matrix has `F` as a principal block, hence by interlacing has two eigenvalues at least `2` and one at most `-1`. Applying the completed pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A from `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` to this literal three-coordinate block, after conditioning on all tail coordinates and retaining all induced affine terms, gives the target-level inequality

\[
\boxed{\|p_{X^TA_\varepsilon X}\|_{\infty,\mathrm{ess}}\le6\sqrt\pi.}
\]

So the example refutes only the intermediate normal-floor / automatic-pair inference.

## 2. Deterministic physical pair-or-triple lemma

### `QFORM-THREEHUB-S2-PAIR-OR-TRIPLE-COMPILER-v1`

Let `F` be any real symmetric `3 x 3` matrix with singular values

\[
s_1\ge s_2\ge s_3\ge0,
\qquad s_2>0.
\]

Then either

\[
\boxed{s_3\ge s_2/4},
\]

or some literal physical `2 x 2` principal block `C` satisfies

\[
\boxed{\sigma_{\min}(C)\ge s_2/6},
\qquad
\boxed{|\det C|\ge s_2^2/36}.
\]

### Proof

Assume `s_3<s_2/4`. Choose an orthonormal eigenbasis `u_1,u_2,u_3` with eigenvalues `lambda_k`, ordered by `|lambda_k|=s_k`. Pick a physical coordinate `i` with `u_{3i}^2>=1/3`, and let `C` be the complementary principal `2 x 2` block. Then

\[
\det C=e_i^T\operatorname{adj}(F)e_i.
\]

Using

\[
\operatorname{adj}(F)
=\lambda_2\lambda_3u_1u_1^T
+\lambda_1\lambda_3u_2u_2^T
+\lambda_1\lambda_2u_3u_3^T,
\]

one obtains

\[
\begin{aligned}
|\det C|
&\ge s_1s_2u_{3i}^2-s_1s_3u_{2i}^2-s_2s_3u_{1i}^2\\
&\ge s_1\bigl[s_2u_{3i}^2-s_3(1-u_{3i}^2)\bigr]\\
&\ge \frac{s_1}{3}(s_2-2s_3)
>\frac{s_1s_2}{6}.
\end{aligned}
\]

Since a principal compression has operator norm at most `s_1`,

\[
\sigma_{\min}(C)=\frac{|\det C|}{\sigma_{\max}(C)}>s_2/6.
\]

Then `|det C|=sigma_max(C)sigma_min(C)>=sigma_min(C)^2>s_2^2/36`. QED.

## 3. Product-preserving density compiler

Let now `F=A[H,H]` be a literal physical `3 x 3` principal block of a full target matrix `A`, and put

\[
\tau:=\sigma_2(F).
\]

The full target assumption implies `s_3(A)>=1` in singular-value notation.

If the triple branch holds, the minimum absolute eigenvalue of `F` is at least `tau/4`. Conditioning only on the other original coordinates leaves the same `F` and only changes affine terms. The required pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A therefore yields

\[
\boxed{\|p_Q\|_\infty\le\frac{24\sqrt\pi}{\tau}.}
\tag{3.1}
\]

If the pair branch yields a definite `C`, the two-dimensional physical-pair area bound gives

\[
\boxed{\|p_Q\|_\infty\le\frac{\pi}{\sqrt{|\det C|}}\le\frac{6\pi}{\tau}.}
\tag{3.2}
\]

If `C` is indefinite, apply the completed arbitrary-rank original-coordinate pair theorem at `math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`. It retains arbitrary outside couplings, arbitrary remaining spectrum and all affine terms. Since

\[
D_C:=|\det C|\ge\tau^2/36,
\qquad
\kappa_C:=\sigma_{\min}(C)\ge\tau/6,
\]

and the full target has `s_3(A)>=1`, that theorem gives

\[
\boxed{
\|p_Q\|_\infty
\le3\,400^{1/3}6^{5/6}\tau^{-5/6}
<98.387\,\tau^{-5/6}.
}
\tag{3.3}
\]

This is a genuine product-preserving receiver: two literal original coordinates are completed and the arbitrary-rank Schur remainder is averaged through its small-ball law, rather than taking a worst conditional fiber density.

In particular,

\[
\boxed{\sigma_2(F)\ge1/64\quad\Longrightarrow\quad\|p_Q\|_\infty<3149.}
\tag{3.4}
\]

At `tau=1/64`, the three branch constants are respectively `2722.490`, `1206.372`, and `3148.357`; the last is worst.

## 4. Consequence for partner r52

The explicit obstruction in Section 1 has `sigma_2(F)=2`, so it is automatically paid by the localized triple branch. More generally, after partner r52's already-paid branches and the compiler above are removed, its genuinely unresolved positive-normal packet can be sharpened to

\[
\boxed{0<\chi<1/64,\qquad \sigma_2(F)<1/64.}
\tag{4.1}
\]

Together with r52's exact split

\[
\frac{H}{t^T\operatorname{adj}(G)t}<\frac1{65},
\qquad
\frac{W\theta^2}{t^T\operatorname{adj}(G)t}>\frac{64}{65},
\]

this means the remaining obstruction has two simultaneous properties: the selected adjugate curvature is more than `64/65` tangential, and the **actual physical three-hub quadratic block is within operator distance `1/64` of rank one**. Every quantitatively two-dimensional hub action is already paid by (3.4).

No spectral rotation of the input law is used, no tail term is deleted, and no conditional fiber supremum appears.

## 5. First unpaid implication

`QFORM-R52-RANKONE-HUB-TANGENTIAL-COLLAR-v1`:

> In partner r52's low-disjointness packet, assume `0<chi<1/64`, `sigma_2(F)<1/64`, the diffuse two-frame leverage gate, and the retained layer-0/1/2 curvature mass. Use the near-rank-one **physical** hub block together with the `>64/65` tangential adjugate curvature to obtain an all-level product-preserving receiver, or route to the finite heavy-tail-hub endpoint. The small rank-two part of `F` cannot simply be discarded on arbitrary unbounded product inputs.

This is strictly narrower than `QFORM-ADJUGATE-6465-TANGENTIAL-COLLAR-RECEIVER-v1`.

No moments, support bounds, log-concavity, identical laws, diagonal-basis assumption, or post-rotation independence were introduced. Continuity remains separate from the essential density bounds. A narrow manual pre-commit review found no credentials, account secrets, signed URLs, machine paths, scheduler identifiers, or unrelated private data in this report; no repository-local automated privacy checker was exposed through the connector, so that limitation is recorded explicitly.
