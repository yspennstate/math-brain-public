SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B17, 2026-09-24T09:08:23.640789Z.
attacking: arbitrary-orientation one-macroscopic-row sharp witnesses, plus an actual target-family application of fleet02/B17's completed random-location Gaussian theorem.

# One-macroscopic-row cone-tip barrier and exact dense target families

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T090823Z-fleet01-B17-QFORM-auto11`  
Status: `NEW SUPPORTING THEOREM / EXACT ROTATED STRESS FAMILY / PARTNER RESULT APPLIED / FULL TARGET OPEN`.

The unrestricted quadratic-form bounded-density conjecture remains **OPEN / not proved / not disproved**. The unrestricted continuity conclusion also remains separate. This report preserves the live corrections: it uses no law-uniform pointwise oscillatory decay, no independence after spectral rotation, no arbitrary-joint coarea lemma, and no fiber-supremum dimension-free claim.

The strongest source-valid general lower obstruction remains
\[
C_{\rm univ}\ge 3\sqrt2.
\]
The new result below does not improve that number. It rules out a substantial candidate overshoot mechanism: **one genuine macroscopic uniform physical row interacting with a minimum-variance diffuse Gaussian residual cannot raise the cone-tip above `3 sqrt(2)`, in any orientation relative to the `(2,1)` spectral splitting, when its covariance is exactly compensated.**

## 1. Hybrid one-macro model

By an orthogonal change only inside the three-dimensional latent spectral space, write
\[
B=\operatorname{diag}(1,1,-1).
\]
This is a latent calculation; no independence of rotated physical coordinates is asserted.

Fix a unit vector `v in R^3` and `0<=q<1`. Let
\[
\Sigma_q=\frac1{12}(I-qvv^T),
\qquad
G_q\sim N(0,\Sigma_q),
\qquad
U\sim {\rm Unif}[-1/2,1/2],
\]
with `G_q` and `U` independent, and define
\[
Y_q=G_q+\sqrt q\,vU,
\qquad
Q_q=Y_q^TBY_q.
\tag{1.1}
\]
The covariance is exactly preserved:
\[
\operatorname{Cov}(Y_q)
=\frac1{12}(I-qvv^T)+\frac q{12}vv^T
=\frac1{12}I.
\tag{1.2}
\]
Thus this model isolates a single macroscopic row while holding the total second-order covariance at the minimum-variance cube value.

## 2. Exact arbitrary-orientation cone-tip formula

Parameterize the upper null cone of `B` by
\[
a_\phi=(\cos\phi,\sin\phi,1),\qquad |a_\phi|^2=2.
\]
The law of `Y_q` is centrally symmetric. Cylindrical coarea therefore gives
\[
p_{Q_q}(0)
=\frac12\int_0^{2\pi}\int_{\mathbb R}\rho_q(ra_\phi)\,dr\,d\phi,
\tag{2.1}
\]
where `rho_q` is the density of `Y_q`.

Condition on `U=u`. Put
\[
\beta_\phi=v\cdot a_\phi,
\qquad
h_\phi=2-\beta_\phi^2,
\qquad
D_\phi=2-qh_\phi.
\tag{2.2}
\]
Because `|beta_phi|<=sqrt(2)`, one has `h_phi>=0`; and because `q<1`, `D_phi>0`.

The inverse covariance is
\[
\Sigma_q^{-1}=12\left(I+\frac q{1-q}vv^T\right),
\qquad
\det\Sigma_q=\frac{1-q}{12^3}.
\tag{2.3}
\]
For the conditional Gaussian mean `m=sqrt(q)u v`, completing the square in the line parameter `r` gives the exact line integral
\[
\int_{\mathbb R}\rho_{q,u}(ra_\phi)\,dr
=\frac6{\pi\sqrt{D_\phi}}
\exp\left(-6qu^2\frac{h_\phi}{D_\phi}\right).
\tag{2.4}
\]
Indeed
\[
a_\phi^T\Sigma_q^{-1}a_\phi
=\frac{12D_\phi}{1-q},
\]
and the precision-distance of `m` from the line `R a_phi` is exactly
\[
12qu^2\frac{h_\phi}{D_\phi}.
\]
Averaging (2.4) over the unit interval and inserting it in (2.1),
\[
\boxed{
 p_{Q_q}(0)
 =\frac3\pi\int_0^{2\pi}
 \frac1{\sqrt{D_\phi}}
 \left[\int_{-1/2}^{1/2}
 e^{-6qu^2h_\phi/D_\phi}\,du\right]d\phi .
}
\tag{2.5}
\]

Define
\[
x_\phi=\frac{qh_\phi}{2-qh_\phi}\ge0,
\qquad
F(x)=\int_{-1/2}^{1/2}e^{-6xu^2}\,du,
\qquad
H(x)=\sqrt{1+x}\,F(x).
\tag{2.6}
\]
Since `D_phi=2/(1+x_phi)`, formula (2.5) becomes
\[
\boxed{
\frac{p_{Q_q}(0)}{3\sqrt2}
=\frac1{2\pi}\int_0^{2\pi}H(x_\phi)\,d\phi .
}
\tag{2.7}
\]
This reduces the entire arbitrary-orientation cone-tip question to one scalar inequality.

## 3. Scalar monotonicity lemma

### Lemma 3.1
For every `x>=0`,
\[
\boxed{H(x)\le1,}
\tag{3.1}
\]
with strict inequality for `x>0`.

### Proof
Let
\[
M_2(x)=\int_{-1/2}^{1/2}u^2e^{-6xu^2}\,du.
\]
Integration by parts gives
\[
12xM_2(x)=F(x)-e^{-3x/2}.
\tag{3.2}
\]
Consequently, for `x>0`,
\[
\frac{d}{dx}\log H(x)
=\frac{(1+x)e^{-3x/2}-F(x)}{2x(1+x)F(x)}.
\tag{3.3}
\]
But
\[
F(x)=e^{-3x/2}
\int_{-1/2}^{1/2}
\exp\{6x(1/4-u^2)\}\,du.
\tag{3.4}
\]
The interval has length one and
\[
\int_{-1/2}^{1/2}u^2du=\frac1{12}.
\]
Jensen therefore yields
\[
\int_{-1/2}^{1/2}e^{6x(1/4-u^2)}du
>e^{6x(1/4-1/12)}=e^x>1+x
\quad (x>0).
\tag{3.5}
\]
Thus the numerator in (3.3) is strictly negative for `x>0`. Since `H(0)=1`, (3.1) follows. QED.

Combining (2.7) and Lemma 3.1 proves the main barrier:
\[
\boxed{p_{Q_q}(0)\le3\sqrt2\qquad(0\le q<1),}
\tag{3.6}
\]
and the inequality is strict for every `q>0`. No assumption on the orientation of `v` was used.

This is a cone-tip theorem, not a global-density theorem for the compensated model. It constrains a proposed sharpness mechanism without claiming the full QFORM result.

## 4. Small-macro orientation rigidity

The scalar factor has the exact expansion
\[
H(x)=1-\frac3{20}x^2+\frac{11}{70}x^3
-\frac{129}{1120}x^4+\frac{237}{3080}x^5+O(x^6).
\tag{4.1}
\]
Let `t=(v\cdot e_3)^2`, the squared component of the macro direction along the minority eigenaxis. Rotating inside the positive eigenspace, write
\[
v=(\sqrt{1-t},0,\sqrt t).
\]
A direct trigonometric average gives
\[
\frac1{2\pi}\int_0^{2\pi}h_\phi^2d\phi
=\frac{19+2t-13t^2}{8}\ge1,
\tag{4.2}
\]
with equality only at `t=1`. Since
\[
x_\phi=\frac q2h_\phi+O(q^2),
\]
we obtain
\[
\boxed{
\frac{p_{Q_q}(0)}{3\sqrt2}
=1-\frac{3q^2}{80}\frac{19+2t-13t^2}{8}+O(q^3).
}
\tag{4.3}
\]
Thus, to second order, the **most dangerous one-macro orientation is exactly the minority eigenvector**. In that aligned case the penalty is only
\[
1-\frac{3}{80}q^2+O(q^3),
\tag{4.4}
\]
explaining why a genuinely macroscopic row can remain surprisingly close to the diffuse `3 sqrt(2)` obstruction.

## 5. Exact entrywise-dense finite target realization with one leverage-1/2 row

Take
\[
n=\frac{(1,2,4)^T}{\sqrt{21}},
\qquad
P=nn^T,
\qquad
B=I-2P,
\tag{5.1}
\]
so `B^2=I` and `spec(B)={1,1,-1}`. Use the tetrahedral Parseval frame
\[
V=\frac12
\begin{pmatrix}
1&1&1\\
1&-1&1\\
1&1&-1\\
1&-1&-1
\end{pmatrix},
\qquad V^TV=I_3.
\tag{5.2}
\]
For `0<q<=1/2`, let
\[
C_q=(I-qP)^{1/2}=I-(1-\sqrt{1-q})P.
\tag{5.3}
\]
Define the `(4m+1) x 3` physical synthesis matrix `R_{m,q}` by taking one row
\[
\sqrt q\,n^T
\]
and then `m` copies of each row of `VC_q/sqrt(m)`. Then
\[
R_{m,q}^TR_{m,q}=qP+C_q^2=I_3.
\tag{5.4}
\]
Set
\[
A_{m,q}=R_{m,q}BR_{m,q}^T.
\tag{5.5}
\]
Hence, for every `m`,
\[
\boxed{\operatorname{spec}_{\ne0}(A_{m,q})=\{1,1,-1\}.}
\tag{5.6}
\]

At the concrete value `q=1/2`, every physical matrix entry is nonzero. The macro--diffuse entries are nonzero because
\[
2\sqrt{21}\,(V_i\cdot n)\in\{7,3,-1,-5\}.
\tag{5.7}
\]
The diffuse `4 x 4` kernel before the `1/m` scaling is exactly
\[
V\left(I-\frac32P\right)V^T
=
\begin{pmatrix}
-1/8&-1/8&3/8&3/8\\
-1/8&33/56&-11/56&29/56\\
3/8&-11/56&41/56&9/56\\
3/8&29/56&9/56&17/56
\end{pmatrix},
\tag{5.8}
\]
whose entries are all nonzero; the macro diagonal entry is `-1/2`.

Take all `4m+1` physical coordinates independent `U[-1/2,1/2]`. Then
\[
R_{m,q}^TX
\Rightarrow
G_q+\sqrt q\,nU,
\tag{5.9}
\]
with the hybrid law of Section 1. The physical eigenframe has row leverages `q` for the macro row and at most `3/(4m)` for the diffuse rows. For `q<=1/2` and `m>=2`, every leverage is at most `1/2`. Therefore the completed source-pinned Fresnel--Brascamp--Lieb Theorem F at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

gives a common integrable `O(|t|^{-3/2})` characteristic-function envelope for the actual finite outputs. Pointwise convergence plus dominated convergence therefore upgrades (5.9) to uniform convergence of the complete output densities.

In the aligned `q=1/2` case, `h_phi=1` identically and (2.5) evaluates to
\[
\boxed{
 p_{Q_{1/2}}(0)
 =2\sqrt{3\pi}\,\operatorname{erf}(1/\sqrt2)
 =4.1916863432298254954\ldots .
}
\tag{5.10}
\]
Thus an exact finite-dimensional target sequence with one genuine leverage-`1/2` physical row, exact active spectrum `{1,1,-1}`, and entrywise-dense physical matrices still approaches a cone-tip only
\[
3\sqrt2-4.191686343229825\ldots
=0.05095434388945965\ldots
\tag{5.11}
\]
below the known sharpness obstruction. A proof cannot assume that one macroscopic row creates a large fixed smoothing gap.

## 6. Completed fleet02/B17 result applied to an actual target family

The designated partner `fleet02/B17` proved and checked `QFORM-RANDOM-LOCATION-GAUSSIAN-INDEFINITE-BARRIER-v1` in

`yspennstate/math-open-problems@f1b5f3b66e19fa17acf395ea31e6615d7ddc7440:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260924T074629Z-fleet02-B17-QFORM-auto11/REPORT.md`,

with checks at commit `97d91254e56ad2f8c79b121a0ce8bf66472a11d9`. For an isotropic `(2,1)` Gaussian reflection with `G~N(0,sI)` and deterministic shift `m`, it supplies
\[
\|p_{(G+m)^TB(G+m)}\|_\infty
\le e^{-|m|^2/(2s)}C_0+
(1-e^{-|m|^2/(2s)})C_1,
\tag{6.1}
\]
where
\[
C_0=\frac1{2\sqrt2s},
\qquad
C_1=\frac{e^{-1/2}}{\sqrt{2\pi}s}.
\tag{6.2}
\]

Apply it to a different exact physical family. Let `\widetilde R_{m,q}` have one row `sqrt(q)n^T` and `m` copies of every row of `V/sqrt(m)`, and define
\[
\widetilde A_{m,q}=\widetilde R_{m,q}B\widetilde R_{m,q}^T.
\tag{6.3}
\]
Now
\[
\widetilde R_{m,q}^T\widetilde R_{m,q}=I+qP.
\]
Since `P` commutes with `B`, the exact nonzero spectrum is
\[
\boxed{
\operatorname{spec}_{\ne0}(\widetilde A_{m,q})
=\{1,1,-(1+q)\}.
}
\tag{6.4}
\]
Thus every finite matrix is itself a strict target instance. It is entrywise dense: the diffuse block is built from
\[
VBV^T=
\begin{pmatrix}
-5/12&-1/4&5/12&7/12\\
-1/4&15/28&-5/28&17/28\\
5/12&-5/28&61/84&11/84\\
7/12&17/28&11/84&13/84
\end{pmatrix},
\tag{6.5}
\]
and (5.7) controls the macro--diffuse entries.

For independent physical unit intervals,
\[
\widetilde R_{m,q}^TX\Rightarrow G+\sqrt q\,nU,
\qquad G\sim N(0,I_3/12).
\tag{6.6}
\]
Condition on `U=u` and use the partner theorem with `s=1/12`. Averaging the conditional density norms gives the actual limit inequality
\[
\boxed{
\left\|p_{(G+\sqrt q nU)^TB(G+\sqrt q nU)}\right\|_\infty
\le C_1+(C_0-C_1)
\int_{-1/2}^{1/2}e^{-6qu^2}\,du,
}
\tag{6.7}
\]
with
\[
C_0=3\sqrt2,
\qquad
C_1=\frac{12e^{-1/2}}{\sqrt{2\pi}}.
\]
For `q=1/2`,
\[
\int_{-1/2}^{1/2}e^{-3u^2}du
=\sqrt{\frac\pi3}\operatorname{erf}(\sqrt3/2),
\]
so
\[
\boxed{
\left\|p_{\rm limit}\right\|_\infty
\le3.9715052655710787928\ldots<3.98<3\sqrt2.
}
\tag{6.8}
\]

This partner result also transfers to the actual finite target sequence, not merely the weak limit. Orthogonalizing `\widetilde R_{m,q}` gives macro leverage `q/(1+q)` and diffuse leverages at most `3/(4m)`. At `q=1/2` these are at most `1/3` and `3/(4m)`. Theorem F therefore supplies a common integrable characteristic-function majorant. Hence the output densities converge uniformly, and
\[
\boxed{
\limsup_{m\to\infty}
\|p_{X^T\widetilde A_{m,1/2}X}\|_\infty
\le3.971505265571079\ldots .
}
\tag{6.9}
\]
In particular, for all sufficiently large `m`,
\[
\boxed{
\|p_{X^T\widetilde A_{m,1/2}X}\|_\infty<3.98.
}
\tag{6.10}
\]
This is the requested application of a completed fleet02/B17 theorem to a genuine finite QFORM family with exact target spectrum `{1,1,-3/2}`.

## 7. Constraint on a prospective sharp proof

The one-macro frontier is now sharply split. If the diffuse covariance is compensated so the active physical spectrum stays exactly at threshold, a single macroscopic unit-interval row cannot push the **cone tip** above `3 sqrt(2)` in any orientation, but it can come within about `0.051` of that value already at leverage `1/2`. If the same macro row is added without compensation, producing strict spectral slack, the completed partner theorem gives a **global** strict gap below `3 sqrt(2)` in the concrete dense target family.

Therefore a sharpness search above `3 sqrt(2)`, if such an overshoot exists at all, must leave this one-macro Gaussian-residual mechanism. The surviving natural stress mechanisms are at least two genuinely interacting macroscopic/non-collinear rows, a non-Gaussian residual shape not representable as an independent location perturbation of a minimum-variance Gaussian core, or additional active spectrum surviving aggregation. This is a constraint on witnesses, not a proof that `3 sqrt(2)` is the unrestricted sharp constant.
