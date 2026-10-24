SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-23T17:14:11Z.
attacking: receiver-driver localization under arbitrary translated fragments — preserve the whole driver through the moving-fold singularity, derive the full L^p mass-homogeneous compiler, and apply account02/B14 r39 at an actual strict-target inequality.

# account01/B14 auto11 — L^p moving-fold localization and zero-tax fragment ledger

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner continuation acknowledged: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Status: `NEW_SUPPORTING_THEOREM + STRICT_TARGET_APPLICATION + SHARPENED_PARTNER_APPLICATION / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`. Continuity is separate and is not claimed.

## 1. Sources and live corrections actually consumed

Fresh control was resolved from `yspennstate/math-research-brain/main`; the current OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no later pause/stop for account01/B14. I read fresh `AGENTS.md`, `scheduled_tasks/README.md` including OWNER MESSAGE, `fleet.json`, `roles.json`, `PROTOCOL.md`, QFORM `MANIFEST.json`, `CURRENT_RESEARCH.md`, `CLAIMS.json`, live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and `assignments/account01/B14.json`. I also read the current continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` and the Claude continuation at `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/README.md`, including the source-pinned `c4c23b784395630c094ba299a50712209921d1ae` update. The proposed `(SP)` adapted-hub estimate there remains OPEN and is not used as a premise.

The designated partner theorem actually used below is account02/B14 r39, canonical report

`yspennstate/math-open-problems@6b6cd1c3be8a9c23a3424593a38b0450acb61cfa`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T155625Z-account02-B14-QFORM-r39/REPORT.md`.

Its moving-fold proof was read in full. The affine slice-Fresnel Fourier bound used by that report was also checked at account03/B14 auto11,

`yspennstate/math-open-problems@8b9adaf929bab4d0d18a15b81055040f3313629a`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260923T153652Z-account03-B14-QFORM-auto11/REPORT.md`.

No refuted pointwise quadratic Fourier decay, arbitrary-joint coarea lemma, post-rotation independence, bounded-diameter localization, or conditional-density supremum shortcut is used.

## 2. A sharp cap-only Riesz lemma for subprobability laws

Let `mu` be a finite measure on `R` with total mass `m` and Lebesgue density bounded by `M`. For `0<alpha<1`, symmetric decreasing rearrangement gives, uniformly in every translation `t`,

\[
\boxed{
\int |x-t|^{-\alpha}\,d\mu(x)
\le
{2^\alpha\over 1-\alpha}M^\alpha m^{1-\alpha}.
}
\tag{2.1}
\]

Indeed the largest integral among densities `0<=g<=M` of mass `m` is obtained by putting density `M` on the interval of length `m/M` centered at `t`; direct integration gives (2.1). Nothing depends on support radius, number of components, their separation, translations, tails, or moments.

This fixed-mass form is the bookkeeping needed below; using a normalized fragment first would erase the powers of `m` that make the final summation exact.

## 3. New theorem: the full L^p moving-fold compiler

Fix `p>2` and put

\[
q={p\over p-1},\qquad \alpha=q-1={1\over p-1}\in(0,1).
\]

Let `nu` be a finite measure on a driver space, of mass `m`. Let `beta(z)` be a scalar measurable statistic such that the pushforward `beta_#nu` has a Lebesgue density bounded by `L`. Let `W` be an independent scalar probability variable with density `f<=1`. For `nu`-almost every `z`, let `T_z` be independent of `W` with density `q_z`, and define

\[
K_p(z)=\|q_z\|_p,
\qquad
S_p=\int K_p(z)^p\,d\nu(z)<\infty.
\]

For arbitrary `a in R`, form the subprobability output measure obtained by mixing

\[
Q_z=T_z+aW^2+\beta(z)W
\tag{3.1}
\]

against `nu`.

### Theorem 3.1 — `QFORM-LP-MOVING-FOLD-SUBPROB-LOCALIZATION-v1`

The output has an essentially bounded density and

\[
\boxed{
\|p_Q^{(\nu)}\|_\infty
\le
C_p\,m^{(p-2)/p}L^{1/p}S_p^{1/p},
\qquad
C_p=2^{2/p}
\left({p-1\over p-2}\right)^{(p-1)/p}.
}
\tag{3.2}
\]

The constant is uniform in `a`, in all translations, and in all support/tail geometry. For `p=3`, (3.2) becomes

\[
\|p_Q^{(\nu)}\|_\infty
\le2^{4/3}(mLS_3)^{1/3},
\tag{3.3}
\]

which is the mass-homogeneous mixed-budget extension of the completed account02/B14 r39 theorem.

### Proof for `a != 0`

For fixed `b`, set

\[
R_b=aW^2+bW,
\qquad x_b=-{b\over2a}.
\]

Completing the square and writing `r=|W-x_b|`, the two inverse branches give

\[
p_{R_b}(y)={f(x_b+r)+f(x_b-r)\over2|a|r},
\qquad dy=2|a|r\,dr.
\]

Because `0<=f<=1`, `f(x_b+r)+f(x_b-r)<=2`, hence

\[
(u+v)^q\le2^{q-1}(u+v),\qquad 0\le u,v\le1.
\]

The powers of two cancel exactly with the Jacobian:

\[
\begin{aligned}
\|p_{R_b}\|_q^q
&\le |a|^{1-q}
\int_0^\infty r^{1-q}
\{f(x_b+r)+f(x_b-r)\}\,dr\\
&=|a|^{1-q}H_\alpha(x_b),
\end{aligned}
\tag{3.4}
\]

where

\[
H_\alpha(x)=\int |w-x|^{-\alpha}f(w)\,dw.
\]

Since `(q-1)/q=1/p`,

\[
\boxed{
\|p_{R_b}\|_q
\le |a|^{-1/p}H_\alpha(x_b)^{1/q}.
}
\tag{3.5}
\]

Conditional Young gives

\[
\|p_{Q_z}\|_\infty
\le K_p(z)|a|^{-1/p}
H_\alpha\!\left(-{\beta(z)\over2a}\right)^{1/q}.
\tag{3.6}
\]

Let `mu_X` be the pushforward of `nu` by `z -> -beta(z)/(2a)`. It has mass `m` and density cap

\[
M=2|a|L.
\tag{3.7}
\]

Holder with exponents `p,q` gives

\[
\int K_p(z)H_\alpha(X(z))^{1/q}d\nu(z)
\le S_p^{1/p}
\left(\int H_\alpha(x)d\mu_X(x)\right)^{1/q}.
\tag{3.8}
\]

By Fubini and (2.1),

\[
\int H_\alpha(x)d\mu_X(x)
\le {2^\alpha\over1-\alpha}M^\alpha m^{1-\alpha}.
\tag{3.9}
\]

Using `alpha=1/(p-1)`, `1/q=(p-1)/p`, and (3.7), the `|a|` powers cancel:

\[
|a|^{-1/p}
\left[{2^\alpha\over1-\alpha}(2|a|L)^\alpha m^{1-\alpha}\right]^{1/q}
=
C_p\,m^{(p-2)/p}L^{1/p}.
\]

This proves (3.2) for nonzero receiver self-curvature.

### Proof for `a=0`

Now `R_b=bW`, and because `f<=1` has mass one,

\[
\|p_{bW}\|_q\le |b|^{-1/p}.
\tag{3.10}
\]

Thus

\[
\|p_Q^{(\nu)}\|_\infty
\le \int K_p(z)|\beta(z)|^{-1/p}d\nu(z).
\]

Holder reduces this to

\[
S_p^{1/p}
\left(\int |b|^{-1/(p-1)}d(\beta_\#\nu)(b)\right)^{1/q}.
\]

Applying (2.1) directly to `beta_#nu` gives the same powers of `m,L`, with constant smaller than `C_p` by the factor `2^{1/p}`. Hence (3.2) holds for every real `a`. QED.

## 4. Exact fragment ledger and zero localization tax

Suppose

\[
\nu=\sum_j\nu_j
\]

is any finite or countable positive decomposition. Write `m_j=nu_j(1)`, let `L_j` be a density cap for `beta_#nu_j`, and put

\[
S_{p,j}=\int K_p(z)^p d\nu_j(z).
\]

Applying Theorem 3.1 before summing yields the exact positive ledger

\[
\boxed{
\|p_Q^{(\nu)}\|_\infty
\le C_p\sum_j
m_j^{(p-2)/p}L_j^{1/p}S_{p,j}^{1/p}.
}
\tag{4.1}
\]

The safe zero-tax criterion is linear unnormalised projection mass:

\[
L_j\le m_j L_0\quad\hbox{for every }j.
\tag{4.2}
\]

Then Holder gives

\[
\begin{aligned}
\sum_jm_j^{(p-2)/p}L_j^{1/p}S_{p,j}^{1/p}
&\le L_0^{1/p}
\sum_jm_j^{(p-1)/p}S_{p,j}^{1/p}\\
&\le L_0^{1/p}
\left(\sum_jm_j\right)^{(p-1)/p}
\left(\sum_jS_{p,j}\right)^{1/p}.
\end{aligned}
\tag{4.3}
\]

For a probability driver, this is exactly the same constant as the unsplit whole-law theorem. Thus arbitrary translations, arbitrarily distant fragments, countably many components, unbounded support and absence of moments cost **zero** whenever the unnormalised driver projection cap retains the fragment mass.

In particular, fragmenting an *outside* independent environment is always safe: its mass simply multiplies the untouched driver law, so (4.2) holds with equality. What remains unsafe is normalizing fragments of the certificate-active driver itself before the moving fold is averaged. The correct proof order is

`outside conditioning / outside fragments -> keep active driver whole -> moving-fold Riesz payment -> sum outside masses`.

This is the localization mechanism required by the assignment. It preserves the analytic constant, not merely finiteness.

## 5. Strict full-target application of account02/B14 r39

The completed partner theorem becomes especially useful when the core itself has a logarithmic singularity and no bounded density. Let all coordinates below be mutually independent with densities bounded by one. Let `U_1,U_2,W` be scalars, `Z in R^m` and `Y in R^r` product vectors. Fix `c!=0`, `v!=0`, arbitrary symmetric `H,G`, arbitrary matrix `R`, arbitrary vectors `r_1,r_2,s`, and arbitrary `a in R`. Consider

\[
\begin{aligned}
Q={}&2cU_1U_2+Z^THZ+aW^2+2(v^TZ)W\\
&+2(r_1^TY)U_1+2(r_2^TY)U_2
+2Z^TRY+2(s^TY)W+Y^TGY.
\end{aligned}
\tag{5.1}
\]

There are **no** support, moment, centering, connectedness or tail assumptions.

Condition on `Y=y` and use `Z=z` as the whole moving-fold driver. The `U` core is

\[
2cU_1U_2+2(r_1^Ty)U_1+2(r_2^Ty)U_2+\hbox{constant}.
\]

Completing the hyperbolic product shows that it is a translate of `2c(U_1-u_0)(U_2-v_0)` plus a constant. For every `p>1`, Minkowski and the cap-only Riesz bound give the translation-uniform estimate

\[
\boxed{
\|p_{2c(U_1-u_0)(U_2-v_0)}\|_p
\le p|c|^{-1+1/p}.
}
\tag{5.2}
\]

Indeed, conditional on `U_1=u`, the scaled `U_2` density has `L^p` norm at most `(2|c||u-u_0|)^{-1+1/p}`; integrating in `u` and using

\[
\mathbb E|U_1-u_0|^{-(1-1/p)}
\le {2^{1-1/p}\over1/p}=p2^{1-1/p}
\]

cancels the factor `2^{-(1-1/p)}` and proves (5.2).

The receiver coefficient is

\[
\beta_y(z)=2v^Tz+2s^Ty.
\]

The product-projection theorem on the untouched original-coordinate bank `Z` gives

\[
\|p_{\beta_y(Z)}\|_\infty
\le {1\over\sqrt2\,\|v\|_2}
\tag{5.3}
\]

uniformly in `y`. The arbitrary dense term `Z^THZ+2Z^TRy+Y^TGy` is only a measurable translation of `T_z` and therefore does not affect (5.2). Apply Theorem 3.1 with a probability driver and the uniform core budget from (5.2):

\[
\boxed{
\|p_Q\|_\infty
\le
C_p\,p\,2^{-1/(2p)}
|c|^{-1+1/p}\|v\|_2^{-1/p}.
}
\tag{5.4}
\]

Choosing `p=3` gives the clean explicit inequality

\[
\boxed{
\|p_Q\|_\infty
\le
3\,2^{7/6}
|c|^{-2/3}\|v\|_2^{-1/3}
=6.7347722898\ldots\ |c|^{-2/3}\|v\|_2^{-1/3}.
}
\tag{5.5}
\]

This is a direct equation-level application of account02/B14 r39's moving-fold mechanism to a core whose density can genuinely be unbounded logarithmically.

### Why (5.1) is genuinely in the owner's target

The active principal coefficient block on `(U_1,U_2,Z,W)` is

\[
\begin{pmatrix}0&c\\c&0\end{pmatrix}
\oplus
\begin{pmatrix}H&v\\v^T&a\end{pmatrix}.
\tag{5.6}
\]

The first block has eigenvalues `+|c|,-|c|`. For the second symmetric block `S`,

\[
\|S\|_{op}\ge\|Se_W\|_2
=\sqrt{\|v\|_2^2+a^2}\ge\|v\|_2,
\tag{5.7}
\]

so it has an eigenvalue of modulus at least `||v||_2`. Therefore if

\[
|c|\ge1,\qquad \|v\|_2\ge1,
\tag{5.8}
\]

the active principal block already has at least three eigenvalues of modulus at least one. Adding the arbitrary outside block `Y` and all couplings displayed in (5.1) preserves the positive/negative threshold counts by Cauchy interlacing. Hence (5.5) is a strict target-valid theorem, not merely a toy inequality.

It allows arbitrary dense same-bank curvature `H`, arbitrary receiver self-curvature `a`, arbitrary outside curvature `G`, arbitrary active-outside couplings, arbitrary translations, remote fragments, unbounded supports, and no moments.

## 6. Sharpening the completed partner's slice-Fresnel branch

Account02/B14 r39 combined its moving-fold theorem with the account03/B14 affine slice-Fresnel core. The source-bound Fourier estimate is

\[
|\phi_{T_z}(t)|\le
\min\{1,B|t|^{-3/4}\},
\qquad
B=2\pi^{3/4}|h|^{-1/2}|\gamma|^{-1/4},
\tag{6.1}
\]

uniformly in the conditioning-generated affine data and arbitrary hub phase.

The partner chose the `p=3` endpoint. Theorem 3.1 allows the whole family `2<p<4`. Put `q=p/(p-1)`. Since `q>4/3`,

\[
\int_{\mathbb R}|\phi_{T_z}(t)|^qdt
\le {6q\over3q-4}B^{4/3}.
\tag{6.2}
\]

The inverse Hausdorff-Young inequality for the convention used in the source gives

\[
\boxed{
\|p_{T_z}\|_p
\le
(2\pi)^{-1/q}
\left({6q\over3q-4}\right)^{1/q}
B^{4/(3q)}.
}
\tag{6.3}
\]

Take the convenient rational value

\[
p={12\over5},\qquad q={12\over7}.
\]

Then `6q/(3q-4)=9`, and (6.3) simplifies exactly to

\[
\boxed{
\|p_{T_z}\|_{12/5}
\le
3^{7/6}2^{7/36}
|h|^{-7/18}|\gamma|^{-7/36}.
}
\tag{6.4}
\]

For the same scalar receiver as account02/B14 r39, `beta(Z)=2v^TZ+d`, (5.3) supplies `L<=1/(sqrt2||v||_2)`. Theorem 3.1 therefore gives

\[
\boxed{
\|p_Q\|_\infty
\le
2^{17/72}3^{7/6}7^{7/12}
|h|^{-7/18}|\gamma|^{-7/36}\|v\|_2^{-5/12}.
}
\tag{6.5}
\]

At the partner's normalized active scale

\[
|h|\ge1/\sqrt2,\qquad |\gamma|\ge1,\qquad \|v\|_2\ge1,
\]

this becomes

\[
\boxed{
\|p_Q\|_\infty
\le
2^{31/72}3^{7/6}7^{7/12}
=15.1086429339\ldots .
}
\tag{6.6}
\]

The completed account02/B14 r39 `p=3` bound on this same structured branch was `20.9817209872...`. Thus the L^p localization compiler improves the explicit constant by about 28 percent while retaining arbitrary scalar receiver self-curvature, translations, disconnected/unbounded supports and absence of moments. A continuous numerical optimization over `p` is slightly smaller, but (6.6) is preferred because it is exact and source-auditable.

## 7. What this resolves, and what it does not

This run resolves a precise localization debt:

* the moving-fold singularity has a complete `L^p` mass-homogeneous treatment for every `p>2`;
* arbitrary outside fragments with mass-proportional unnormalised projection caps can be summed with **exactly zero constant loss**;
* distant fragments, translations, unbounded supports and all moments disappear from the estimate;
* account02/B14 r39's scalar receiver theorem extends from a uniform `L^3` core to an `L^p`-averaged core budget and admits a strictly better explicit slice-Fresnel constant;
* the strict target family (5.1) is covered even though its hyperbolic core can have an unbounded logarithmic density.

The full QFORM conjecture is still OPEN. The unpaid implication is structural: from the bare condition `s_3(A)>=1`, before normalizing any certificate-active fragment, force either a whole-law ridge/volume/mixed-hub/grouped-bank exit, or a decomposition exposing a driver statistic with a dimension-free projection cap and a core whose `L^p` budget is controlled in the precise sense of Theorem 3.1. The newest Claude `(SP)` adapted-hub estimate remains open for arbitrary rough separated laws, and this report does not prove it.

The localization lesson is now quantitative: a fragment-first proof must retain the mass powers in (4.1). If it destroys the linear unnormalised projection scaling `L_j<=m_jL_0`, it may create an artificial divergence even when the whole-law moving-fold estimate is uniform.

## 8. Source integrity and status

Full QFORM: **OPEN**.  
No pointwise quadratic Fourier decay claim is made.  
No arbitrary-joint coarea claim is used.  
No independence after rotation is assumed.  
No bounded fragment count or bounded support diameter is assumed.  
No moment bounds are assumed.  
Partner result actually applied: account02/B14 r39 at the moving-fold equation, with its account03/B14 Fourier core used only in the exact scope stated above.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.
