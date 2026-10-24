SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B17, 2026-09-23T06:04:24Z.
attacking: unequal-signature one-singleton/two-independent-rank-one-bank stress families; extend the Ball/Livshyts--Paouris--Pivovarov two-norm bound to distinct bank leverage vectors and arbitrary spectral magnitudes >=1, then apply account02/B17 mode-at-zero theorem globally.

# QFORM B17 — arbitrary cap-one singleton plus two distinct symmetric-unimodal rank-one banks

Run: `QFORM-B17-20260923T060424Z-r15`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING SHARP-WITNESS THEOREM; FULL QFORM OPEN / NOT PROVED**  
Full-target continuity: separately open.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Main theorem

Let `m,n>=1`, let `a in R^m`, `b in R^n` satisfy

\[
\|a\|_2=\|b\|_2=1,
\]

and let

\[
X,\ U_1,\ldots,U_m,\ V_1,\ldots,V_n
\]

be mutually independent. Assume only that `X` has an arbitrary probability density `f_X<=1`. For the bank coordinates assume the densities of each `U_j` and `V_k` are even, nonincreasing on `[0,infinity)`, and bounded by one. They need not be compactly supported, identical, or uniform. Put

\[
S=\sum_{j=1}^m a_jU_j,\qquad T=\sum_{k=1}^n b_kV_k.
\]

For arbitrary spectral magnitudes

\[
\alpha,\beta,\gamma\ge1,
\]

define

\[
Q=\alpha X^2+\beta S^2-\gamma T^2.
\tag{1.1}
\]

Then `Q` has a density and

\[
\boxed{
\|p_Q\|_\infty
\le \mathcal B(\alpha,\beta,\gamma)
:=\frac4{\sqrt\alpha}\int_0^{\pi/2}
\min\left\{
\frac1{\sqrt{2\beta}},
\frac1{2(\beta\gamma)^{1/4}\sqrt{\sin\theta}}
\right\}\,d\theta .
}
\tag{1.2}
\]

In particular the right side is pointwise nonincreasing in each of `alpha,beta,gamma`, so

\[
\boxed{
\|p_Q\|_\infty\le C_{\rm sep}
:=4\left[
\frac{\pi}{6\sqrt2}
+\frac12\int_{\pi/6}^{\pi/2}(\sin\theta)^{-1/2}\,d\theta
\right]
=3.8172923460947289\ldots<3\sqrt2.
}
\tag{1.3}
\]

A fully elementary certificate, avoiding the decimal evaluation of the integral, is

\[
C_{\rm sep}
\le 2\pi\left(1-\frac1{\sqrt3}+\frac1{3\sqrt2}\right)
<\frac{5148}{1225}<3\sqrt2.
\tag{1.4}
\]

Thus this whole exact finite stress architecture is separated from the known `3sqrt(2)` lower-obstruction scale. The arbitrary singleton law may be translated, disconnected, unbounded, or fragmented; no symmetry assumption is made on it.

The sign-reversed statement follows by replacing `Q` by `-Q`.

## 2. Exact target provenance

On the original independent physical coordinates `(X,U,V)`, take

\[
A_{a,b}^{\alpha,\beta,\gamma}
=\operatorname{diag}\!\left(\alpha,\,\beta aa^T,\,-\gamma bb^T\right).
\tag{2.1}
\]

Because `aa^T` and `bb^T` are rank-one orthogonal projections in their respective physical banks,

\[
\boxed{
\operatorname{spec}_{\ne0}(A_{a,b}^{\alpha,\beta,\gamma})
=\{\alpha,\beta,-\gamma\}.
}
\tag{2.2}
\]

Hence every finite matrix in this family satisfies the original hypothesis of at least three eigenvalues of absolute value at least one. For nontrivial `a,b`, both bank blocks contain genuine physical off-diagonal couplings. The two bank dimensions and leverage vectors are completely independent of one another.

Every physical cross cut of (2.1) has rank at most two, while the singleton contributes a leverage-one direction. Thus this family is deliberately outside proof routes that require a rank-three physical cross cut or fully diffuse leverage.

## 3. Two product-marginal norm bounds for each bank

Let `h` be the density of `S`. The sharp one-dimensional product-marginal theorem of Livshyts--Paouris--Pivovarov gives

\[
\boxed{\|h\|_\infty\le\sqrt2.}
\tag{3.1}
\]

Indeed the coefficient vector `a` is unit and every physical input density is bounded by one.

A second application gives the stronger `L^2` fact needed below. Let `S'` be an independent copy of `S`. Then

\[
\|h\|_2^2=p_{S-S'}(0).
\tag{3.2}
\]

But

\[
\frac{S-S'}{\sqrt2}
=\left\langle\frac{(a,-a)}{\sqrt2},(U,U')\right\rangle,
\]

and `(a,-a)/sqrt(2)` is again a unit vector in `R^{2m}`. Applying the same marginal theorem to the doubled product source gives

\[
p_{(S-S')/\sqrt2}(0)\le\sqrt2.
\]

Since `p_{(S-S')/sqrt(2)}(0)=sqrt(2) p_{S-S'}(0)`, we obtain

\[
\boxed{\|h\|_2^2\le1.}
\tag{3.3}
\]

Exactly the same statements hold for the density `k` of `T`.

The assumed even-unimodal physical bank laws imply that `h` and `k` are themselves even and nonincreasing on `[0,infinity)`: one may prove this by the standard layer-cake representation of an even decreasing density as a positive mixture of centered interval indicators, together with closure of one-dimensional symmetric unimodality under convolution.

After scaling

\[
Y=\sqrt\beta\,S,\qquad Z=\sqrt\gamma\,T,
\]

write their densities as `h_beta,k_gamma`. Then

\[
\|h_\beta\|_\infty\le\frac{\sqrt2}{\sqrt\beta},
\qquad
\|h_\beta\|_2^2\le\frac1{\sqrt\beta},
\tag{3.4}
\]

and

\[
\|k_\gamma\|_\infty\le\frac{\sqrt2}{\sqrt\gamma},
\qquad
\|k_\gamma\|_2^2\le\frac1{\sqrt\gamma}.
\tag{3.5}
\]

Literature source: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1; its `k=1` bound is `sqrt(2)` and is an adaptation of Ball's cube-slicing argument.

## 4. Partner theorem applied to a sigma-finite cap majorant

This is the step that removes every symmetry requirement from the singleton `X` while still obtaining a **global-output** estimate.

Scale

\[
W=\sqrt\alpha\,X,
\]

so its density satisfies

\[
f_W(w)\le c:=\alpha^{-1/2}.
\tag{4.1}
\]

For `R>0`, replace `f_W(w)` by the finite majorant `c 1_{[-R,R]}(w)`. Its mass is `2Rc`; after normalization it is the law of a uniform variable `W_R~Unif[-R,R]`.

The completed designated partner theorem account02/B17,

`QFORM-SEPARATED-SYMMETRIC-UNIMODAL-OFFZERO-v1`,
canonical source `yspennstate/math-open-problems@84ffc0f291ae192f4d82742ae6909943f6710bc7`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/B17-20260922T235536Z-r12-symmetric-unimodal/REPORT.md`,

proves that for independent symmetric-unimodal `Y_1,Y_2,Y_3` and positive coefficients, the density of `Y_1^2+Y_2^2-Y_3^2` has its global maximum at zero.

Apply that completed result to the actual triple

\[
W_R,\quad Y,\quad Z.
\]

If `\bar p_R` denotes the output density generated by the unnormalized first-coordinate measure `c1_{[-R,R]}dw`, then

\[
\boxed{\bar p_R(t)\le \bar p_R(0)\qquad\forall t.}
\tag{4.2}
\]

This is an actual inequality-level application of the partner theorem: `\bar p_R=2Rc\,p_{W_R^2+Y^2-Z^2}`.

Since the true first-coordinate density is pointwise at most `c`, positivity of the convolution representation gives, for the canonical density representative,

\[
p_Q(t)\le \bar p(t):=\lim_{R\to\infty}\bar p_R(t).
\tag{4.3}
\]

Monotone convergence in `R`, together with (4.2), yields

\[
\boxed{p_Q(t)\le\bar p(t)\le\bar p(0)\qquad\forall t.}
\tag{4.4}
\]

Thus the whole global problem in this branch reduces to the zero value of a sigma-finite cap majorant. No post-rotation independence, arbitrary-joint coarea estimate, conditional density-cap moment, or pointwise oscillatory decay is used.

## 5. Polar formula and the anisotropic envelope

Because `k_gamma` is even, the density of `Z^2` at `u>0` is

\[
q_Z(u)=\frac{k_\gamma(\sqrt u)}{\sqrt u}.
\]

Tonelli and polar coordinates in the `(w,y)` plane therefore give

\[
\bar p(0)
=c\int_{\mathbb R^2}
 h_\beta(y)\frac{k_\gamma(\sqrt{w^2+y^2})}{\sqrt{w^2+y^2}}\,dw\,dy
\]

and hence

\[
\boxed{
\bar p(0)=\frac4{\sqrt\alpha}
\int_0^{\pi/2}J(\theta)\,d\theta,
\qquad
J(\theta)=\int_0^\infty h_\beta(r\sin\theta)k_\gamma(r)\,dr.
}
\tag{5.1}
\]

The first norm estimate uses (3.4) and the fact that an even probability density has half its mass on the positive half-line:

\[
J(\theta)\le
\frac{\sqrt2}{\sqrt\beta}\cdot\frac12
=\frac1{\sqrt{2\beta}}.
\tag{5.2}
\]

For `theta>0`, Cauchy--Schwarz and (3.4)-(3.5) give

\[
\begin{aligned}
J(\theta)
&\le
\left(\int_0^\infty h_\beta(r\sin\theta)^2dr\right)^{1/2}
\left(\int_0^\infty k_\gamma(r)^2dr\right)^{1/2}\\
&\le
\frac1{2(\beta\gamma)^{1/4}\sqrt{\sin\theta}}.
\end{aligned}
\tag{5.3}
\]

Substitution into (5.1) proves (1.2).

For completeness, let

\[
\tau=\frac12\sqrt{\frac\beta\gamma}.
\]

If `tau<1`, the two bounds cross at `theta_0=arcsin(tau)` and

\[
\mathcal B(\alpha,\beta,\gamma)
=\frac4{\sqrt\alpha}
\left[
\frac{\theta_0}{\sqrt{2\beta}}
+\frac1{2(\beta\gamma)^{1/4}}
\int_{\theta_0}^{\pi/2}(\sin\theta)^{-1/2}d\theta
\right].
\tag{5.4}
\]

If `beta>=4 gamma`, then the first bound is always smaller and

\[
\mathcal B(\alpha,\beta,\gamma)
=\frac{\sqrt2\,\pi}{\sqrt{\alpha\beta}}.
\tag{5.5}
\]

Both component bounds in (1.2) are nonincreasing in each spectral magnitude. Hence their pointwise minimum is also nonincreasing and the worst case is `alpha=beta=gamma=1`. At that point the crossing angle is `pi/6`, proving (1.3).

## 6. Elementary comparison with `3sqrt(2)`

On `[0,pi/2]`, concavity of sine gives

\[
\sin\theta\ge\frac{2\theta}{\pi}.
\]

Therefore

\[
\int_{\pi/6}^{\pi/2}(\sin\theta)^{-1/2}d\theta
\le
\pi\left(1-\frac1{\sqrt3}\right),
\]

which gives the first inequality in (1.4). Next use

\[
\pi<\frac{22}{7},\qquad
\frac1{\sqrt3}>\frac47,\qquad
\frac1{3\sqrt2}<\frac6{25}.
\]

Then

\[
2\pi\left(1-\frac1{\sqrt3}+\frac1{3\sqrt2}\right)
<\frac{5148}{1225}.
\]

Finally

\[
5148^2=26,501,904
<27,011,250=18\cdot1225^2,
\]

so `5148/1225<3sqrt(2)`.

## 7. Sharp-witness consequence

The known exact target-level obstruction remains

\[
C_{\rm univ}\ge3\sqrt2,
\]

from the completed account02/B17 diffuse three-bank construction `QFORM-UNIVERSAL-CONSTANT-LOWER-3SQRT2-v1`.

The present theorem therefore excludes a substantially broader low-cross-rank/high-leverage escape than the preceding equal-bank calculation:

- the singleton physical law is completely arbitrary under the cap one;
- the two aggregate banks may have different dimensions and unrelated unit leverage vectors;
- every physical law inside either bank may be any symmetric-unimodal cap-one density;
- the three nonzero eigenvalue magnitudes may be arbitrary `alpha,beta,gamma>=1`.

None of those changes can produce a peak even as large as `3sqrt(2)`; the explicit branch ceiling is the smaller constant `C_sep=3.817292346...` from (1.3).

Accordingly, a witness above `3sqrt(2)`, if one exists, must leave this architecture. The credible surviving mechanisms are genuinely shared-coordinate/non-collinear heavy rows spanning several spectral directions, asymmetric/fragmented laws inside more than the singleton coordinate, coupled spectral tails that are not disjoint rank-one banks, or a finite/mesoscopic structure that destroys the symmetric-unimodal bank reduction.

This is a supporting witness theorem only. It does **not** prove that `3sqrt(2)` is the universal sharp constant and does not prove the unrestricted QFORM conjecture.

## 8. Corrections and provenance

Fresh brain control at the start of this run was `yspennstate/math-research-brain@8d98eb1d7fea52498479553c484486558c2ebc60`; the operative owner control is revision `2026-09-22.15`, QFORM-only. The live correction inbox was read before this proof. In particular this argument does not use the refuted arbitrary-joint rank-three coarea inequality, conditional projection-cap moments, post-rotation independence, a universal physical rank-three cross extraction, scalar-remainder worst conditioning, or law-uniform pointwise stationary-phase decay.

External source checked this run: Livshyts--Paouris--Pivovarov, arXiv:1507.07949, whose abstract states the sharp `2^{k/2}` marginal-density bound for product densities bounded by one; the `k=1` case is exactly the `sqrt(2)` input used in Section 3.
