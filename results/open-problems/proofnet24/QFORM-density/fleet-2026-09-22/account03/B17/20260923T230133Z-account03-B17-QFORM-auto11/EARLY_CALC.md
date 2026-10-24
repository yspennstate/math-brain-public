# Early calculation — two-heavy / one-diffuse null-pivot family

Take
\[
B=\begin{pmatrix}
1/2&-1/2&-1/\sqrt2\\
-1/2&1/2&-1/\sqrt2\\
-1/\sqrt2&-1/\sqrt2&0
\end{pmatrix}
=I-2nn^T,\qquad n=(1/2,1/2,1/\sqrt2).
\]
Then `B^2=I` and `spec(B)={1,1,-1}`. For independent heavy coordinates X,Y and Z~N(0,v), v=1/12,
\[
Q=(X,Y,Z)^TB(X,Y,Z)=\frac12(X-Y)^2-\sqrt2(X+Y)Z.
\]
Writing `u=x-y`, `s=x+y`, the conditional density at level q is
\[
K_q(x,y)=\frac{1}{2\sqrt{\pi v}|s|}
\exp\!\left[-\frac{(q-u^2/2)^2}{4vs^2}\right].
\]
For q=0, the exact distribution function under Lebesgue measure in (x,y) is
\[
|\{K_0>t\}|=D_v t^{-3/2},\qquad
D_v=\sqrt2\,\pi^{-3/4}v^{-1/2}
\frac{\Gamma(5/4)}{(3/2)^{5/4}}.
\]
For every q, the one-dimensional u-section of each superlevel set is at most \(\sqrt2\) times the q=0 section, hence
\[
|\{K_q>t\}|\le\sqrt2 D_v t^{-3/2}.
\]
Thus any joint heavy density rho with `0<=rho<=1`, `int rho=1` satisfies by bathtub/rearrangement
\[
\sup_q\int \rho K_q
\le 3(\sqrt2D_v)^{2/3}.
\]
At v=1/12 this constant is
\[
C_{2H1G}=\frac{2^{13/6}\sqrt3}{\sqrt\pi}\Gamma(5/4)^{2/3}
=4.109270566451296\ldots<3\sqrt2.
\]
This is already stronger than needed for independent X,Y because their joint density fg also has cap one.

Next step in this run: transfer this limiting theorem to exact finite cap-one one-bank approximants using the completed account04/B17 weighted local Edgeworth estimate at commit `2156b76156ad5956c214a881fcfd6d977d6f3b9f`.
