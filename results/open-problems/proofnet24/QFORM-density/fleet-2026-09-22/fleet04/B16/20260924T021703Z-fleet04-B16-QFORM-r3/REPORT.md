SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B16, 2026-09-24T02:17:03Z.
attacking: innovation-free shared-square endpoint by taking the minimum of the genuine-fresh and shared-bank transverse pair caps before applying the curved zero-pivot receiver.

# QFORM-FRESH-OR-TRANSVERSE-PAIRCAP-DICHOTOMY-v1

Programme: \`QFORM-DENSITY-3EIG-20260922\`  
Run: \`20260924T021703Z-fleet04-B16-QFORM-r3\`  
Status: \`ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN\`.

The unrestricted conjecture remains open. This note closes the zero-pivot shared-square branch whenever either a genuine fresh coefficient or a source-valid two-dimensional transverse Gram determinant is quantitative. It preserves the original product provenance and does not use a worst conditional-density supremum.

## Pinned inputs

1. Fleet01/B16, \`math-open-problems@693cb2f86df07dc102701767d7eddd09306ab201\`, theorem \`QFORM-TRANSLATED-FRESH-SQUARE-SIGNFREE-v1\`.
2. Fleet02/B16, \`math-open-problems@be8062b160868bcc71aff45a77c56ff2d0501a9a\`, theorem \`QFORM-FRESH-HUB-DIVISIBLE-TWIST-ABSORPTION-v1\`:
   \[
   \|p_Q\|_\infty\le
   3\,2^{2/3}M^{2/3}|\gamma^2\kappa|^{-1/3}.
   \]
3. The product-Fourier two-frame estimate used in fleet01/B06 and pinned at \`math-open-problems@3ae4b0c272e0d3c60f956c9f039bea38fc0f9077\`: a normalized two-frame with physical leverage at most \(1/2\) has joint density cap \(4\).

## Theorem

Let \(X=(X_j)\) be a product bank of independent cap-one real variables, let \(Z\) and \(H\) be two further independent cap-one original sources, and assume \(X,Z,H\) are mutually independent. Let
\[
L=\langle \ell,X\rangle,\qquad S=\langle v,X\rangle,\qquad
V=\sigma Z+S,
\]
where \(\|\ell\|_2=1\). Put
\[
G=\det\operatorname{Gram}(\ell,v)
=\|v-\langle v,\ell\rangle\ell\|_2^2.
\]
When \(G>0\), assume the Gram-normalized two-frame
\[
[\ell\ v]\operatorname{Gram}(\ell,v)^{-1/2}
\]
has every physical row leverage at most \(1/2\).

Let \(T\) be an arbitrary measurable function of the light bank \((X,Z)\), and set
\[
Q=2\gamma HL+2LT+\alpha L^2+2\delta LV+\kappa V^2,
\qquad \gamma\kappa\ne0.
\]
Then \(Q\) is absolutely continuous and
\[
\boxed{
\|p_Q\|_\infty
\le 3\,2^{2/3}
\min\!\left\{\frac{\sqrt2}{|\sigma|},\frac4{\sqrt G}\right\}^{2/3}
|\gamma^2\kappa|^{-1/3},
}
\tag{1}
\]
where an unavailable term (\(\sigma=0\) or \(G=0\)) is omitted.

Equivalently, the two separate source-valid bounds are
\[
\boxed{
\|p_Q\|_\infty
\le 6\,|\sigma|^{-2/3}|\gamma^2\kappa|^{-1/3},
}
\tag{2}
\]
and
\[
\boxed{
\|p_Q\|_\infty
\le 12\,[G|\gamma^2\kappa|]^{-1/3}.
}
\tag{3}
\]

### Proof

First use the untouched source \(Z\). Convolution only in the second coordinate gives
\[
p_{L,V}(l,y)
=\int p_{L,S}(l,s)\,
\frac1{|\sigma|}f_Z\!\left(\frac{y-s}{\sigma}\right)\,ds
\le \frac{p_L(l)}{|\sigma|}
\le \frac{\sqrt2}{|\sigma|}.
\tag{4}
\]
This uses genuine independence of the original source \(Z\), not projected independence.

Second use shared-bank transversality. Write
\[
(L,S)=Y\,\operatorname{Gram}(\ell,v)^{1/2},
\]
where \(Y\) is the Gram-normalized two-frame projection. The pinned product-Fourier estimate gives \(\|p_Y\|_\infty\le4\). The deterministic Jacobian therefore yields
\[
\|p_{L,S}\|_\infty\le\frac4{\sqrt G}.
\tag{5}
\]
Convolution with the independent law of \(\sigma Z\) cannot increase this cap, so the same bound holds for \((L,V)\).

Thus the actual pair cap is
\[
M\le \min\!\left\{\frac{\sqrt2}{|\sigma|},\frac4{\sqrt G}\right\}.
\tag{6}
\]
The hypotheses of the completed fleet02/B16 curved zero-pivot theorem now hold exactly: \(H\) is untouched, the entire twist \(T\) may depend on the same light sources as \((L,V)\), and only the pair cap \(M\) is used. Substitution of (6) proves (1); the two choices separately give (2) and (3). No fiberwise conditional cap or arbitrary-joint coarea estimate appears.

## Concrete live gate

At
\[
|\gamma|\ge1,\qquad |\kappa|\ge1,
\]
either
\[
|\sigma|\ge\frac1{64}
\quad\Longrightarrow\quad
\boxed{\|p_Q\|_\infty\le96},
\tag{7}
\]
or
\[
G\ge2^{-12}
\quad\Longrightarrow\quad
\boxed{\|p_Q\|_\infty\le192}.
\tag{8}
\]
Therefore every survivor of both receivers satisfies the explicit coefficient collar
\[
\boxed{
|\sigma|<\frac1{64},
\qquad
\operatorname{dist}\bigl(v,\operatorname{span}\{\ell\}\bigr)
=\sqrt G<\frac1{64}.
}
\tag{9}
\]
This is the exact innovation-free/near-collinear obstruction, rather than a qualitative statement that all innovations vanish.

## Completed fleet01/B16 theorem applied at an equation

In the twist-free subfamily \(T=0\), view \(Q\) as a quadratic form in \((H,L,V)\) with
\[
B=
\begin{pmatrix}
0&\gamma&0\\
\gamma&\alpha&\delta\\
0&\delta&\kappa
\end{pmatrix},
\qquad
\det B=-\gamma^2\kappa,\qquad b=\kappa.
\]
Fleet01/B16 applies because \(V=\sigma Z+S(X)\) has the required fresh innovation and \(H\) is fresh. Since \(\|p_L\|_\infty\le\sqrt2\), its sign-free theorem gives the actual comparison
\[
\boxed{
\|p_Q\|_\infty
\le \frac{8\sqrt2}{|\sigma|\sqrt{|\gamma\kappa|}}.
}
\tag{10}
\]
At \(|\sigma|,|\gamma|,|\kappa|\ge1\), this is \(8\sqrt2\). Equation (2) is generally better near a small \(\sigma\), while (10) persists for the nonzero-pivot sign-free Schur family covered by fleet01/B16. Both estimates are on the same original-coordinate model.

## Remaining implication

The first unpaid B16 case is now sharply localized: the zero-pivot survivor has both a fresh coefficient below \(1/64\) and a shared transverse coefficient vector within \(1/64\) of the hub direction, after Gram normalization. Closing it requires a source-first grouped descent or a rank-one/near-coloop receiver. A bounded arbitrary joint density alone is insufficient, and no claim is made for the unrestricted theorem or global continuity.

## Source boundary

Claude baseline: \`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837\`.  
Fleet01/B16 completed theorem: \`693cb2f86df07dc102701767d7eddd09306ab201\`.  
Fleet02/B16 zero-pivot receiver: \`be8062b160868bcc71aff45a77c56ff2d0501a9a\`.  
Product-Fourier two-frame input: \`3ae4b0c272e0d3c60f956c9f039bea38fc0f9077\`.
