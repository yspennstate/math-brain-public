# Quantitative checks for `QFORM-SMOOTH-CONNECTED-SLICE-ROUGH-HUB-FALSE-v1`

Run: `20260923T233929Z-fleet03-B14-QFORM-auto11`.

## Constants

The interval-concentration constant in (2.6) is

\[
\frac{7\sqrt2}{8}=1.2374368670764582\ldots.
\]

The frozen-slice constant is

\[
\frac{3\sqrt7}{16}=0.49607837082461076\ldots<\frac12.
\]

The designated partner target constant is

\[
4+2\log8=8.158883083359672\ldots.
\]

## Algebraic checks

For `A_2=[[0,1,-1],[1,0,0],[-1,0,0]]`,

\[
\det(\lambda I-A_2)=\lambda(\lambda^2-2),
\]

so the spectrum is `{sqrt(2),-sqrt(2),0}` and the counterexample interface is rank two in the target sense.

For

\[
Q_N=2X_1X_2+\frac12(X_3+X_4)^2,
\]

the first two coordinates have matrix `[[0,1],[1,0]]`, spectrum `{1,-1}`, and the last two have matrix `(1/2)[[1,1],[1,1]]`, spectrum `{1,0}`. Hence the nonzero spectrum is `{1,-1,1}`, satisfying the exact three-large-eigenvalue target.

## Inequality checks

For `r<=4`,

\[
|E_N\cap J|\le\min(r,2/N)\le\sqrt{2r/N}.
\]

For `r>4`, an interval meets at most `r/4+2 <=3r/4` components, hence

\[
|E_N\cap J|\le\min(1,3r/(4N))\le\sqrt{3r/(4N)}\le\sqrt{r/N}.
\]

Since `L_N>=2N`,

\[
|H_N\cap J|/L_N\le\min(r/(2N),1)\le\sqrt{r/(2N)}.
\]

Combining these gives exactly

\[
(3/4)\sqrt{2r/N}+(1/4)\sqrt{r/(2N)}=(7\sqrt2/8)\sqrt{r/N}.
\]

With `N>=2/epsilon` and `l>=7epsilon/8`,

\[
1/N\le\epsilon/2\le4l/7,
\qquad
\frac{|I|}{2lN}\le\frac{2|I|}{7}.
\]

Therefore

\[
(3/4)(7\sqrt2/8)\sqrt{2/7}=3\sqrt7/16<1/2.
\]

Finally, `||f_N||_2^2>=1/2` and `g_epsilon=3/4` on `[2epsilon,1]` yield

\[
p_T(0)\ge(1/2)(3/4)(1/2)\int_{2\epsilon}^1l^{-1}dl
=(3/16)\log(1/(2\epsilon)).
\]

All bounds are independent of support diameter, bridge height, smoothing radius, and fragment separation.
