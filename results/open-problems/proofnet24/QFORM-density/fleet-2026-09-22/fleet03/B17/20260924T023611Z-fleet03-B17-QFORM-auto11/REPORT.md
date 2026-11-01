SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B17, 2026-09-24T02:36:11Z.
attacking: global-tip rigidity for arbitrary weighted three-bank witnesses and the mesoscopic one-heavy interpolation.

# fleet03/B17 — weighted-bank global-tip rigidity and the one-heavy interpolation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T023611Z-fleet03-B17-QFORM-auto11`  
Status: `NEW SUPPORTING SHARP-WITNESS THEOREM / PARTNER RESULT APPLIED / FULL TARGET OPEN`  
Execution memory: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted quadratic-form bounded-density conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The theorem below is a sharp-witness rigidity statement for exact source-valid finite matrices. It does not add any Gaussian, moment, compact-support, connected-support, or post-rotation independence assumption to the owner target. The uniform inputs occur only in this explicit lower-witness family.


## 1. Exact weighted-bank target family

For each bank `j=1,2,3`, choose finitely many nonnegative weights
\[
 w_{j1},\ldots,w_{jn_j},\qquad \sum_{k=1}^{n_j}w_{jk}=1. \tag{1.1}
\]
Zero weights may be omitted. Let all physical variables `U_{jk}` be independent `Unif[-1/2,1/2]` and define the three disjoint original-coordinate bank sums
\[
 Y_j=\sum_{k=1}^{n_j}\sqrt{w_{jk}}\,U_{jk}. \tag{1.2}
\]
Let `R` be the `N x 3` synthesis matrix (`N=n_1+n_2+n_3`) whose physical row `(j,k)` is `sqrt(w_jk)e_j`. Then
\[
 R^TR=I_3. \tag{1.3}
\]
For any orthogonal `O` put
\[
 J=\operatorname{diag}(1,1,-1),\qquad B=O^TJO,\qquad A=RBR^T. \tag{1.4}
\]
Since `R` is an isometry onto its range,
\[
 \boxed{\operatorname{spec}_{\ne0}(A)=\{1,1,-1\}}. \tag{1.5}
\]
Thus every finite member is an exact instance of the owner's three-large-eigenvalue hypothesis, with independent physical cap-one inputs. No independence is asserted after the spectral rotation `O`.

Each bank density `g_j` is even and log-concave: the unit-interval density is even log-concave in the extended-value sense, and convolution plus nonsingular scaling preserve log-concavity. Consequently `g_j` is nonincreasing on `[0,infinity)`.

## 2. Exact global-tip theorem in the aligned signature

First take `O=I`, so
\[
 Q=Y_1^2+Y_2^2-Y_3^2. \tag{2.1}
\]
Let
\[
 W=Y_1^2+Y_2^2,\qquad V=Y_3^2. \tag{2.2}
\]
The variables `W,V` are independent because their banks use disjoint original coordinates. Let `a` and `b` be their densities on `[0,infinity)`.

For `v>0`, evenness gives
\[
 b(v)=\frac{g_3(\sqrt v)}{\sqrt v}, \tag{2.3}
\]
which is nonincreasing because both factors are nonincreasing. For `s>0`, polar coarea gives the exact formula
\[
 a(s)=\frac12\int_0^{2\pi}
 g_1(\sqrt s\cos\theta)g_2(\sqrt s\sin\theta)\,d\theta. \tag{2.4}
\]
For every fixed `theta`, the integrand is nonincreasing in `s`; hence `a` is nonincreasing.

Therefore, for `q>=0`,
\[
 p_Q(q)=\int_0^\infty a(q+v)b(v)\,dv
 \le \int_0^\infty a(v)b(v)\,dv=p_Q(0), \tag{2.5}
\]
and for `r>0`,
\[
 p_Q(-r)=\int_0^\infty a(u)b(u+r)\,du
 \le \int_0^\infty a(u)b(u)\,du=p_Q(0). \tag{2.6}
\]
Thus
\[
 \boxed{\|p_Q\|_\infty=p_Q(0)} \tag{2.7}
\]
for **every finite leverage profile** (1.1), not only equal-weight banks.

The cone-tip integral is finite. Indeed (2.4) gives
\[
 a(s)\le \pi\|g_1\|_\infty\|g_2\|_\infty, \tag{2.8}
\]
while (2.3) is `O(v^{-1/2})` at zero. Both `a` and `b` are probability densities in `L^1`; after extending them by zero outside `[0,infinity)`, `p_Q=a*\widetilde b` is an `L^1*L^1` convolution. Hence this finite weighted-bank family actually has a continuous `C_0` density. This is a scoped continuity theorem, not the still-open full-target continuity statement.

### Rotated one-sheet companion

For general `O`, the density of `Y=(Y_1,Y_2,Y_3)` is centrally symmetric and log-concave; the same remains true after the deterministic rotation `z=OY`. The exact ruling/Prekopa argument already completed for the three-bank family therefore applies verbatim to these arbitrary weighted banks and yields
\[
 \boxed{p_Q(s)\le p_Q(0)\quad(s\ge0).} \tag{2.9}
\]
For genuinely non-aligned rotations, only the minority-sign/two-sheet side `s<0` remains a possible off-tip escape. No generic two-sheet X-ray bound is used here.

## 3. One-heavy plus one diffuse bank: a two-parameter exact finite family

Now use the same leverage profile in all three banks:
\[
 w_0=\ell,\qquad
 w_k=\frac{1-\ell}{m}\quad(1\le k\le m),\qquad 0\le\ell<1. \tag{3.1}
\]
Thus
\[
 Y_{m,\ell}=\sqrt\ell\,U_0+
 \sqrt{\frac{1-\ell}{m}}\sum_{k=1}^m U_k. \tag{3.2}
\]
Every finite physical target matrix obtained from (1.4) still has exact nonzero spectrum `{1,1,-1}`. Define the leverage cumulant parameters
\[
 S_{m,\ell}=\ell^2+\frac{(1-\ell)^2}{m},\qquad
 T_{m,\ell}=\ell^3+\frac{(1-\ell)^3}{m^2}. \tag{3.3}
\]
We consider the joint diffuse limit `ell ->0`, `m->infinity`.

The characteristic function of one bank is exactly
\[
 \phi_{m,\ell}(t)=
 \operatorname{sinc}\!\left(\frac{\sqrt\ell\,t}{2}\right)
 \left[
 \operatorname{sinc}\!\left(
 \frac{\sqrt{1-\ell}\,t}{2\sqrt m}
 \right)
 \right]^m. \tag{3.4}
\]
Using
\[
 \log\operatorname{sinc}z
 =-\frac{z^2}{6}-\frac{z^4}{180}-\frac{z^6}{2835}+O(z^8), \tag{3.5}
\]
one obtains, on the local Fourier window,
\[
 \log\phi_{m,\ell}(t)
 =-\frac{t^2}{24}
 -\frac{S_{m,\ell}t^4}{2880}
 -\frac{T_{m,\ell}t^6}{181440}
 +O\!\left(
 [\ell^4+(1-\ell)^4/m^3]t^8
 \right). \tag{3.6}
\]
The completed designated-partner `fleet04/B17` weighted local Edgeworth theorem supplies the needed global Fourier-tail mechanism: its equal-bank factor has an integrable polynomially weighted `O(m^{-2})` remainder, obtained by the local logarithmic expansion and the global `|sinc u|<=min(1,|u|^{-1})` split. In (3.4) the additional heavy sinc factor has modulus at most one, while the diffuse factor is only rescaled by `sqrt(1-ell)`. Choosing the local cutoff below both `ell^{-1/2}` and `m^{1/2}` and using the same diffuse Gaussian/tail split therefore gives the uniform weighted inversion
\[
 g_{m,\ell}(y)
 =\gamma_\sigma(y)
 \left[1-\frac{S_{m,\ell}}{20}H_4(y/\sigma)\right]
 +O\!\left(T_{m,\ell}+S_{m,\ell}^2\right)(1+|y|)^{-8}, \tag{3.7}
\]
where `sigma^2=1/12` and `H_4(x)=x^4-6x^2+3`. This is exactly the partner theorem when `ell=0`; the only new algebra is that the fourth-cumulant factor `1/m` is replaced by the exact sum of squared leverages `S_{m,ell}`.

Partner source actually used:

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`,  
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260922T211900Z-fleet04-B17-QFORM-r3/REPORT.md`.

## 4. Cone contraction and an actual global-norm inequality

Let `u in S^2` and
\[
 B_u=I_3-2uu^T. \tag{4.1}
\]
The partner's exact cone contraction gives, for the Gaussian cone measure,
\[
 \mathbb E\sum_{j=1}^3H_4(q a_j)
 =\frac{177-39\sum_j u_j^4}{32}. \tag{4.2}
\]
Inserting (3.7) into the same rank-three cone parametrization therefore yields
\[
 \boxed{
 p_{m,\ell,u}(0)
 =3\sqrt2\left[
 1-c(u)S_{m,\ell}
 +O\!\left(T_{m,\ell}+S_{m,\ell}^2\right)
 \right],} \tag{4.3}
\]
with
\[
 \boxed{c(u)=\frac{177-39\sum_j u_j^4}{640},\qquad
 \frac{69}{320}\le c(u)\le\frac{41}{160}.} \tag{4.4}
\]
The weighted remainder in (3.7) is integrable on the cone, uniformly in `u`, so equivalently there is an absolute `C` and a sufficiently diffuse regime in which the actual inequality
\[
 \left|
 \frac{p_{m,\ell,u}(0)}{3\sqrt2}
 -\left(1-c(u)S_{m,\ell}\right)
 \right|
 \le C\left(T_{m,\ell}+S_{m,\ell}^2\right) \tag{4.5}
\]
holds. This is the completed partner Edgeworth estimate applied to the present source-valid finite target family.

For the aligned negative bank `u=e_3`, Section 2 upgrades (4.3) from a cone-tip statement to the **actual global output-density norm**:
\[
 \boxed{
 \|p_{m,\ell}\|_\infty
 =3\sqrt2\left[
 1-\frac{69}{320}S_{m,\ell}
 +O\!\left(T_{m,\ell}+S_{m,\ell}^2\right)
 \right].} \tag{4.6}
\]
At `ell=0`, this reduces to the designated partner's exact unrotated control
\[
 \|p_{m,0}\|_\infty
 =3\sqrt2\left[1-\frac{69}{320m}+O(m^{-2})\right]. \tag{4.7}
\]
The new point is that (4.6) is global for every finite `m,ell`, and quantifies the entire interpolation from a diffuse bank to a genuine macroscopic physical row.

## 5. Exact leverage-rigidity identity

The fourth-cumulant cost (3.3) has the exact decomposition
\[
 \boxed{
 S_{m,\ell}
 =\frac1{m+1}
 +\frac{((m+1)\ell-1)^2}{m(m+1)}.} \tag{5.1}
\]
Therefore the first non-Gaussian density deficit is uniquely minimized at
\[
 \boxed{\ell=\frac1{m+1},} \tag{5.2}
\]
which is precisely the point where the nominally `heavy` coordinate has the **same** leverage as each of the `m` diffuse coordinates. In other words, within this entire one-heavy-plus-bank interpolation, concentrating leverage into a distinguished physical coordinate never improves the sharp witness at first order; equal leverage is the unique optimizer.

A particularly informative mesoscopic scale is
\[
 \ell=\frac{c}{\sqrt m},\qquad c\ge0\text{ fixed}. \tag{5.3}
\]
Then
\[
 S_{m,\ell}=\frac{1+c^2}{m}-\frac{2c}{m^{3/2}}+O_c(m^{-2}),
 \qquad
 T_{m,\ell}=O_c(m^{-3/2}), \tag{5.4}
\]
so the aligned **global** density norm satisfies
\[
 \boxed{
 \|p_{m,c/\sqrt m}\|_\infty
 =3\sqrt2\left[
 1-\frac{69(1+c^2)}{320m}
 +O_c(m^{-3/2})
 \right].} \tag{5.5}
\]
Thus a mesoscopic physical row of leverage `c/sqrt(m)` opens an additional strict first-order deficit `69c^2/(320m)` rather than creating an overshoot.

## 6. Exact genuinely rotated stress family

Take the rational unit vector
\[
 u_*=(10,10,49)/51. \tag{6.1}
\]
Then
\[
 B_*=I-2u_*u_*^T
 =\frac1{2601}
 \begin{pmatrix}
 2401&-200&-980\\
 -200&2401&-980\\
 -980&-980&-2201
 \end{pmatrix}. \tag{6.2}
\]
Every entry is nonzero and `B_*^2=I`, so every finite lifted physical matrix has exact nonzero spectrum `{1,1,-1}` and all three banks are coupled. The exact cone coefficient is
\[
 \boxed{
 c(u_*)=\frac{53990741}{240540480}
 =0.22445594604284486\ldots .} \tag{6.3}
\]
Hence
\[
 p_{m,\ell,u_*}(0)
 =3\sqrt2\left[
 1-\frac{53990741}{240540480}S_{m,\ell}
 +O(T_{m,\ell}+S_{m,\ell}^2)
 \right]. \tag{6.4}
\]
By (2.9), every nonnegative output level obeys
\[
 \boxed{
 \sup_{s\ge0}p_{m,\ell,u_*}(s)=p_{m,\ell,u_*}(0).} \tag{6.5}
\]
Therefore a finite/mesoscopic overshoot above the `3sqrt(2)` scale in this fully coupled family, if one exists at all, is forced onto the **negative two-sheet side** and must overcome the explicit deficit (6.4). This is a concrete analytic stress constraint on any proposed sharp proof.

## 7. Sharp-constant consequence and remaining gap

Taking `ell=0` and `m->infinity` in the exact finite cap-one family recovers the source-valid obstruction
\[
 \boxed{C_*\ge3\sqrt2.} \tag{7.1}
\]
The present theorem does **not** prove that `3sqrt(2)` is the universal sharp constant. What it adds is an exact global exclusion of off-tip escape for the entire aligned weighted-bank class, plus a two-parameter quantitative statement showing that a distinguished heavy coordinate worsens the first non-Gaussian correction rather than improving it.

What remains genuinely open for B17 is the negative two-sheet side of non-aligned weighted banks, rough/non-log-concave bank laws, several non-collinear macroscopic shared rows, surviving non-Gaussian components, and interacting additional spectrum. The full universal QFORM bound and the full-target continuous-density conclusion remain **OPEN**.
