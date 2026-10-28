SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-24T02:43:13Z.
attacking: the first fully quadratic three-variable perturbation beyond the null-leaf barrier: add a nonzero middle pivot while retaining nonzero XY, YZ, and XZ couplings, and prove a global sharp-constant obstruction in original physical coordinates.

# account02/B17 — nonzero-middle-pivot fully quadratic global barrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T024313Z-account02-B17-QFORM-auto11`  
Claim label: `QFORM-NONZERO-MIDDLE-PIVOT-GLOBAL-BARRIER-v1`  
Status: `NEW SUPPORTING THEOREM / SHARP-WITNESS OBSTRUCTION / FULL TARGET OPEN`

The unrestricted quadratic-form bounded-density conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains separate. The result below is a source-valid global barrier for a genuinely fully quadratic 3-variable target family. It assumes only independence and marginal density caps `<=1`; there is no moment, bounded-support, log-concavity, connected-support, regularity, or post-rotation-independence hypothesis.


## 1. First unpaid implication paid

The preceding account02/B17 report left the following perturbation genuinely unpaid: introduce a nonzero quadratic pivot in the middle physical coordinate, so that no physical leaf remains affine after conditioning the other two variables. The following theorem pays a two-parameter target-valid subfamily of exactly that regime.

Let `X,Y,Z` be arbitrary independent real random variables with probability densities `f_X,f_Y,f_Z` satisfying

\[
0\le f_X,f_Y,f_Z\le1,\qquad \int f_X=\int f_Y=\int f_Z=1.
\]

For `kappa>0`, `a!=0`, and `beta in R`, define

\[
Q_{\kappa,\beta,a}
=\beta Y^2+2aXY+2aYZ+\kappa(X-Z)^2.
\tag{1.1}
\]

Equivalently, in the original independent physical coordinates,

\[
A_{\kappa,\beta,a}=
\begin{pmatrix}
\kappa&a&-\kappa\\
a&\beta&a\\
-\kappa&a&\kappa
\end{pmatrix}.
\tag{1.2}
\]

### Theorem (`QFORM-NONZERO-MIDDLE-PIVOT-GLOBAL-BARRIER-v1`)

For every choice above,

\[
\boxed{
\|p_{Q_{\kappa,\beta,a}}\|_\infty
\le {2\sqrt2\over\sqrt{\kappa|a|}}.
}
\tag{1.3}
\]

The estimate is global in the output level and independent of `beta`. In particular, if

\[
a=1,\qquad \kappa\ge{1\over2},\qquad |\beta|\le1,
\tag{1.4}
\]

then the physical matrix has three eigenvalues of magnitude at least one and

\[
\boxed{
\|p_Q\|_\infty\le4<3\sqrt2.
}
\tag{1.5}
\]

Thus a nonzero middle pivot together with all three nonzero pair couplings does not produce a sharp-constant overshoot in this family.

## 2. Exact physical spectrum

Introduce the orthonormal basis

\[
e_+=(1,0,1)/\sqrt2,\qquad e_Y=(0,1,0),\qquad e_-=(1,0,-1)/\sqrt2.
\]

This is used only to compute the spectrum; independence is never transferred to these coordinates. In this basis,

\[
A_{\kappa,\beta,a}\sim
\begin{pmatrix}
0&\sqrt2a&0\\
\sqrt2a&\beta&0\\
0&0&2\kappa
\end{pmatrix}.
\tag{2.1}
\]

Hence

\[
\det(\lambda I-A)
=(\lambda-2\kappa)(\lambda^2-\beta\lambda-2a^2)
\]

and

\[
\boxed{
\operatorname{spec}(A_{\kappa,\beta,a})
=\left\{2\kappa,
{\beta+\sqrt{\beta^2+8a^2}\over2},
{\beta-\sqrt{\beta^2+8a^2}\over2}
\right\}.
}
\tag{2.2}
\]

For `a=1` and `beta in [-1,1]`, the positive root is at least one (its minimum is attained at `beta=-1`) and the negative root has magnitude at least one (its minimum magnitude is attained at `beta=1`). Thus (1.4) is genuinely inside the owner's target spectral class.

The clean endpoint witness is

\[
\boxed{
A_*=
\begin{pmatrix}
1/2&1&-1/2\\
1&1&1\\
-1/2&1&1/2
\end{pmatrix},
\qquad
\operatorname{spec}(A_*)=\{2,1,-1\}.
}
\tag{2.3}
\]

All three diagonal entries of `A_*` are nonzero. Therefore no original physical coordinate remains affine after the other two are conditioned. This is exactly the structural feature that was missing from the previous null-leaf theorem.

## 3. Product-valid density proof

The proof uses the deterministic integration variables

\[
U={X+Z\over\sqrt2},\qquad V={X-Z\over\sqrt2}.
\tag{3.1}
\]

**No independence of `U,V` is asserted.** Their exact joint density is

\[
g(u,v)
=f_X\!\left({u+v\over\sqrt2}\right)
 f_Z\!\left({u-v\over\sqrt2}\right),
\tag{3.2}
\]

because the orthogonal change of variables has Jacobian one. Therefore

\[
0\le g\le1,\qquad \iint_{\mathbb R^2}g(u,v)\,du\,dv=1.
\tag{3.3}
\]

In these integration coordinates,

\[
Q=\beta Y^2+2\sqrt2\,aUY+2\kappa V^2.
\tag{3.4}
\]

For fixed `y!=0` and `v`, the level equation `Q=s` is affine in `u`, with unique root

\[
u_s(y,v)
={s-\beta y^2-2\kappa v^2\over2\sqrt2\,a y}.
\tag{3.5}
\]

Since `Y` is absolutely continuous, the exceptional set `y=0` has probability zero. Resolving the `u` variable gives for almost every output level `s`

\[
p_Q(s)
=\int_{\mathbb R}
 {f_Y(y)\over2\sqrt2|ay|}
 J_s(y)\,dy,
\qquad
J_s(y)=\int_{\mathbb R}g(u_s(y,v),v)\,dv.
\tag{3.6}
\]

The right side will be bounded uniformly in `s`, proving in particular that this pushforward measure has an essentially bounded density.

## 4. Parabola-preimage bathtub lemma

We use the following one-dimensional fact.

**Lemma.** If `0<=f<=1`, `int f=1`, `A>0`, and `c,v_0 in R`, then

\[
\int_{\mathbb R} f(c\pm A(v-v_0)^2)\,dv\le {2\over\sqrt A}.
\tag{4.1}
\]

Proof. Translate `v_0` to zero and put `t=Av^2`. Then

\[
\int_{\mathbb R} f(c\pm Av^2)\,dv
=A^{-1/2}\int_0^\infty f(c\pm t)t^{-1/2}\,dt.
\]

On `[0,infinity)`, `h(t)=f(c\pm t)` satisfies `0<=h<=1` and `int_0^infinity h<=1`. Since `t^{-1/2}` is decreasing, the cap-one bathtub principle gives

\[
\int_0^\infty h(t)t^{-1/2}\,dt
\le\int_0^1t^{-1/2}\,dt=2.
\]

This proves (4.1). No support or regularity assumption is used.

## 5. Apply the lemma in an original-coordinate factor

From (3.2) and `f_Z<=1`,

\[
J_s(y)
\le\int_{\mathbb R}
 f_X\!\left({u_s(y,v)+v\over\sqrt2}\right)\,dv.
\tag{5.1}
\]

The argument is a quadratic polynomial in `v`:

\[
{u_s(y,v)+v\over\sqrt2}
={s-\beta y^2\over4ay}
-{\kappa\over2ay}v^2+{v\over\sqrt2}.
\tag{5.2}
\]

After completing the square, its quadratic curvature magnitude is exactly

\[
A_y={\kappa\over2|ay|}.
\tag{5.3}
\]

Applying (4.1) to the **original marginal density `f_X`** therefore gives

\[
\boxed{
J_s(y)\le2\sqrt{{2|ay|\over\kappa}}.
}
\tag{5.4}
\]

Substitution into (3.6) yields

\[
p_Q(s)
\le {1\over\sqrt{\kappa|a|}}
\int_{\mathbb R}f_Y(y)|y|^{-1/2}\,dy.
\tag{5.5}
\]

A second cap-one bathtub estimate, now for the even decreasing kernel `|y|^{-1/2}`, gives

\[
\int f_Y(y)|y|^{-1/2}\,dy
\le\int_{-1/2}^{1/2}|y|^{-1/2}\,dy
=2\sqrt2.
\tag{5.6}
\]

Equations (5.5)-(5.6) prove the global theorem (1.3). The output sign never entered the argument.

At the endpoint matrix (2.3), `kappa=1/2`, `a=1`, and therefore

\[
\boxed{
\|p_{X^TA_*X}\|_\infty\le4<3\sqrt2
}
\tag{5.7}
\]

for **every independent cap-one product law** on the three physical coordinates.

## 6. Required pinned-source result applied to a real inequality

The required pinned source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,  
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Its completed Theorem C gives the one-sheet rank-three estimate for signature `(+,+,-)`. Applying that theorem to the **actual physical matrix** `A_*`, whose spectral magnitudes are `(2,1,1)`, gives for `s>=0`

\[
p_{A_*}(s)
\le {1\over\sqrt2}
\int_0^{2\pi}
{d\theta\over
\sqrt{\sin^2\theta/2+\cos^2\theta+1}}
\le\pi\sqrt2.
\tag{6.1}
\]

The generic ceiling `pi sqrt(2)` is larger than `3 sqrt(2)`, so (6.1) alone does not certify the proposed sharp constant. The new original-coordinate estimate (5.7) is global and gives `4<3 sqrt(2)`. Thus this is a concrete case where failure of the generic pinned constant to reach the candidate sharp constant is a **proof-constant limitation, not a QFORM counterexample**.

## 7. Latest partner result consumed

The latest compatible account03/B17 result read in this run is

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260924T023611Z-account03-B17-QFORM-auto11/REPORT.md`

on the current master lineage. It proves global cone-tip rigidity for every finite aligned weighted uniform-bank witness

\[
Q=Y_1^2+Y_2^2-Y_3^2,
\qquad \|p_Q\|_\infty=p_Q(0).
\tag{7.1}
\]

Apply this completed theorem to the source-valid smallest bank choice: one unit interval in each bank,

\[
U_1,U_2,U_3\stackrel{ind}{\sim}\operatorname{Unif}[-1/2,1/2],
\qquad Q_0=U_1^2+U_2^2-U_3^2.
\]

At the cone tip, direct coarea/root integration gives

\[
\begin{aligned}
p_{Q_0}(0)
&=\iint_{x^2+y^2\le1/4}
{dx\,dy\over\sqrt{x^2+y^2}}\\
&=\int_0^{2\pi}\int_0^{1/2}dr\,d\theta
=\pi.
\end{aligned}
\tag{7.2}
\]

Therefore the partner theorem upgrades this exact cone-tip calculation to the real global obstruction

\[
\boxed{\|p_{Q_0}\|_\infty=\pi<3\sqrt2.}
\tag{7.3}
\]

The same partner report also proves that diffuse aligned weighted banks approach `3 sqrt(2)` from below; thus the Gaussian sharp candidate remains supported by the diffuse witness direction rather than by the present finite fully quadratic perturbation.

## 8. Scope and next unpaid mechanism

This theorem pays a genuinely new branch of the prior B17 witness search:

- every physical diagonal entry may be nonzero;
- all three physical pair couplings `XY`, `YZ`, and `XZ` are nonzero at the endpoint witness;
- all three eigenvalue magnitudes meet the target threshold exactly or better;
- every input law may be an arbitrary rough cap-one density;
- the estimate is global over both output signs;
- no independence is used after the `(X,Z)` orthogonal integration change.

What remains unpaid is a **generic fully quadratic three-variable matrix** in which, after any convenient two-coordinate integration change, the same physical marginal cannot be isolated as a single one-dimensional parabola preimage. In particular, unequal `XY/YZ` couplings, an additional independent `X+Z` quadratic curvature, or a dense generic matrix can leave simultaneous quadratic dependence in both transformed coordinates. Failure of the present one-parabola mechanism there would be only a proof-mechanism failure.

A finite example with density peak above `3 sqrt(2)` would refute only the proposed sharp constant. A genuine counterexample to QFORM must force the essential density beyond every finite universal constant. The unrestricted conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

## 9. Algebraic checks

For symbolic parameters,

\[
\det(\lambda I-A_{\kappa,\beta,a})
=(\lambda-2\kappa)(\lambda^2-\beta\lambda-2a^2).
\]

For `(kappa,beta,a)=(1/2,1,1)`,

\[
\det(\lambda I-A_*)=(\lambda-2)(\lambda-1)(\lambda+1),
\]

so the exact spectrum is `{2,1,-1}` and `det A_*=-2`. Numerically `4<3 sqrt(2)=4.2426406871...`.

MODEL: `GPT-5.6 Sol`. THINKING LEVEL: `UNKNOWN`. THINKING USAGE: `null / not exposed`. PROVIDER THINKING TIME: `null / not exposed`. ELAPSED WORK: `UNKNOWN/null`.
