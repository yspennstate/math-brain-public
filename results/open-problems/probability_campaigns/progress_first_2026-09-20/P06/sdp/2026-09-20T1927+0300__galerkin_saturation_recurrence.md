Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated telemetry does not verify GPT-6 maximum, so I do not claim it.**

# P06 complementary P07 iteration — current-law Galerkin saturation gives a superlinear exact-cost recurrence

Status: **P06 SOURCE KNOWN / preserve `U_ER^cert=1`. P07 OPEN / PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.

Previous substantive checkpoint: `probability_campaigns/progress_first_2026-09-20/P06/sdp/2026-09-20T1830+0300__exact_cost_translated_galerkin_square.md`, creation commit `2e7b56f57fd730eaa9a268502fe997b1c6c42bb9`, readback blob `8f9f865bad12e966c3172f3442fc6b819790a3a4`.

Outside P07 source remains Bandeira--Blasiok--Dmitriev--Faure--Kireeva--Kunisky, arXiv:2502.16227. The inherited full-source bound remains

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

No full-source improvement is claimed in this report.

## 0. New result in one sentence

The preceding run reduced the actual sharp-target decrement to `nu_3<6.9e-4` but left the translated mismatch `epsilon_R` as an apparently new growing-depth quantity. The present run removes the dependence on a **fixed old reference law** and shows that, if the translation is restarted at the *current* law, the mismatch is exactly the finite-Galerkin saturation gap

\[
\Delta_R:=\nu^2-\nu_R^2.
\]

Combining this identity with the exact square cost gives the deterministic recurrence

\[
\boxed{
\nu_+
\le
\sqrt{J_R(\eta)}+\sqrt{\Delta_R/\eta}.
}
\tag{0.1}
\]

If the restricted score has normalized fourth moment `M_R` and satisfies the single saturation condition

\[
\boxed{
\Delta_R\le {1\over2}M_R\nu_R^4,
}
\tag{0.2}
\]

then choosing `eta=(1/2)sqrt(M_R) nu_R` yields

\[
\boxed{
\nu_+
\le (1+\sqrt2)M_R^{1/4}\nu_R^{3/2}.
}
\tag{0.3}
\]

Together with the inherited canonical-word envelope `M_R<=exp(C R log(2R))`, this is already strong enough for an `O(log log n)` tail whenever (0.2) can be maintained with `R_k` growing polynomially in `k`. Thus the growing-depth problem has been reduced to one precise current-law Schur-complement estimate, rather than a moving family of fixed-base translated tails.

A fixed-degree test at the explicit law `p_3` also shows that the **square-cost part is not the obstruction**: the same-mask degree-32 reference/transport gives approximately

\[
\nu_{32}^2=1.26\times10^{-7},
\qquad
J_{32}(0.01)<7\times10^{-11},
\tag{0.4}
\]

so the exact square cost alone is already of quadratic size. What remains is to prove the saturation gap (0.2).

---

# 1. Why the fixed-reference translated mismatch is the wrong tail variable after `p_3`

The previous report used a fixed positive reference `p_0` and wrote the current law as `p=f p_0`. This was ideal for the first translated Galerkin step, because the Gibbs/Hermite source had a factorial tail relative to that fixed reference.

It is not uniform in depth.

The reason is algebraic. At the fixed-c seed, the first comparator square has asymptotic numerator degree two in the degree-16 score, hence chaos/convolution degree `32`. The second comparator square is a rational function whose denominator is bounded away from zero, but its large-score growth remains degree `32`. The exact-cost step from `p_2` multiplies by

\[
w_3(g_{24})
=\eta_3+(1-\eta_3){(1+\alpha g_{24})^2\over 1+\alpha^2\nu_{24}^2},
\]

which contributes degree `48`. Thus, relative to the original fixed Gibbs reference, the current density `p_3/p_0` can carry canonical words through degree

\[
32+48=80.
\]

The density mismatch used by a putative degree-32 translation contains an additional factor `1+g_{32}`, so it can populate canonical words through degree

\[
80+32=112.
\tag{1.1}
\]

Therefore it is **false as a proof strategy** to assume that a fixed-base translated mismatch after degree `R=32` starts in a factorially tiny degree-33 tail. The old density factors themselves manufacture a long deterministic high-chaos block. This does not invalidate the previous fixed-depth theorems, where every analytic insertion was transported directly; it invalidates the naive attempt to turn their fixed-reference `epsilon_R` into a uniform `R_k=O(k)` tail estimate.

This is the first useful negative conclusion of the run: the recurrence should not be organized around a permanently frozen Gibbs reference.

---

# 2. Restart the translation at the current law

The translated-comparator lemma is reference-invariant. Use that freedom.

Let `p` be the **current** positive law, let `L=p(1+y)` be any signed law of total mass one having the exact target feature moments, and let `F` be the full centered target-feature span in `L^2(p)`. Denote the full Newton score by

\[
g_N=P_Fy,
\qquad
\nu^2=\|g_N\|_p^2.
\tag{2.1}
\]

Let `K_R\subset F` be any finite same-mask Galerkin subspace and

\[
g_R=P_{K_R}y,
\qquad
\nu_R^2=\|g_R\|_p^2.
\tag{2.2}
\]

Now apply the translated-comparator construction with **reference law equal to `p` itself**. Thus `f=1` in the notation of the preceding report. The density mismatch is simply

\[
D_R=(1+g_R)-(1+y)=g_R-y.
\tag{2.3}
\]

Project it onto the full feature span:

\[
q_R=P_FD_R.
\tag{2.4}
\]

Because `g_R\in F` and `P_Fy=g_N`,

\[
\boxed{
q_R=g_R-g_N.
}
\tag{2.5}
\]

Therefore the translated mismatch energy is no longer an opaque analytic tail:

\[
\boxed{
\epsilon_R
=\|q_R\|_p^2
=\|g_N-g_R\|_p^2
=\nu^2-\nu_R^2.
}
\tag{2.6}
\]

The last equality is Pythagoras because `g_R=P_{K_R}g_N`.

The translated exact target law is

\[
\widehat L_R
=p(1+g_R-q_R)
=p(1+g_N).
\tag{2.7}
\]

This is a signed law in general, but it has the exact target moments by the Newton normal equations. No positivity of `1+g_N` is needed; positivity is supplied only after the regularized square update.

### Lemma 2.1 — current-law restart identity

For every finite Galerkin subspace,

\[
\boxed{
\epsilon_R=\Delta_R:=\nu^2-\nu_R^2.
}
\tag{2.8}
\]

So the sole approximation quantity required by the exact-cost square lemma is exactly the **Galerkin saturation gap** of the current Newton system.

This identity avoids the degree pollution in Section 1 completely.

---

# 3. Exact-cost square with a Galerkin saturation error

Retain the square weight from the previous report. For

\[
s_R=\sqrt{1-\nu_R^2},
\qquad
\alpha_R={1\over1+s_R},
\]

and `eta in (0,1)`, let

\[
w_{R,\eta}(x)
=\eta+(1-\eta){(1+\alpha_Rx)^2\over1+\alpha_R^2\nu_R^2}.
\tag{3.1}
\]

Set

\[
p_+=p\,w_{R,\eta}(g_R).
\tag{3.2}
\]

The exact-cost translated Galerkin lemma from the previous run, now with (2.8), gives immediately

\[
\boxed{
\nu_+
\le
\sqrt{J_R(\eta)}
+
\sqrt{{\Delta_R\over\eta}},
}
\tag{3.3}
\]

where

\[
J_R(\eta)
=\mathbf E_p
{\{1+g_R-w_{R,\eta}(g_R)\}^2\over w_{R,\eta}(g_R)}.
\tag{3.4}
\]

Equation (3.3) is deterministic. It no longer mentions the old Gibbs reference, a fixed-base projection, or an accumulated analytic density ratio.

---

# 4. A universal `3/2`-power bound for the exact square cost

The exact cost itself admits a simple quantitative upper bound using only the **restricted** score fourth moment. This is not a return to the old full-score kurtosis obstruction: `g_R` is a finite canonical same-mask score, so its moments are exactly the objects controlled by the inherited finite/growing-degree collision theorem.

The half-angle identity gives

\[
1+\alpha_R^2\nu_R^2=2\alpha_R.
\tag{4.1}
\]

Hence

\[
{(1+\alpha_Rx)^2\over1+\alpha_R^2\nu_R^2}
={1+s_R\over2}+x+{\alpha_R\over2}x^2.
\]

Therefore

\[
\boxed{
1+x-w_{R,\eta}(x)
=\eta x-{(1-\eta)\alpha_R\over2}(x^2-\nu_R^2).
}
\tag{4.2}
\]

Because `w_{R,eta}>=eta`, `alpha_R<=1`, and `E g_R^2=nu_R^2`,

\[
\begin{aligned}
J_R(\eta)
&\le {1\over\eta}
\mathbf E_p\left[
\eta g_R-{(1-\eta)\alpha_R\over2}(g_R^2-\nu_R^2)
\right]^2\\
&\le
2\eta\nu_R^2
+{(1-\eta)^2\alpha_R^2\over2\eta}
\mathbf E_p(g_R^2-\nu_R^2)^2\\
&\le
\boxed{
2\eta\nu_R^2+{\mathbf E_pg_R^4\over2\eta}.
}
\end{aligned}
\tag{4.3}
\]

Write

\[
M_R={\mathbf E_pg_R^4\over\nu_R^4}.
\tag{4.4}
\]

If

\[
\sqrt{M_R}\,\nu_R\le1,
\tag{4.5}
\]

choose

\[
\boxed{
\eta_R={1\over2}\sqrt{M_R}\,\nu_R.
}
\tag{4.6}
\]

Substitution into (4.3) gives

\[
\boxed{
J_R(\eta_R)
\le2\sqrt{M_R}\,\nu_R^3,
}
\tag{4.7}
\]

and hence

\[
\boxed{
\sqrt{J_R(\eta_R)}
\le\sqrt2\,M_R^{1/4}\nu_R^{3/2}.
}
\tag{4.8}
\]

This is the exact-cost analogue of the old skew-based `3/2` power, but it needs only a finite restricted fourth moment and no full-score `Gamma`.

---

# 5. One scalar saturation condition closes the recurrence

Combine (3.3) and (4.8). Suppose in addition that the current finite Galerkin system satisfies

\[
\boxed{
\Delta_R
=\nu^2-\nu_R^2
\le {1\over2}M_R\nu_R^4.
}
\tag{5.1}
\]

Then, using (4.6),

\[
{\Delta_R\over\eta_R}
\le
{M_R\nu_R^4/2\over \sqrt{M_R}\nu_R/2}
=\sqrt{M_R}\nu_R^3.
\]

Therefore

\[
\boxed{
\nu_+
\le
(1+\sqrt2)M_R^{1/4}\nu_R^{3/2}.
}
\tag{5.2}
\]

This is the main deterministic theorem of the run.

It says that all growing-depth work can be concentrated on one source-coupled statement: the finite same-mask Galerkin space must capture the current Newton energy up to an error of order `M_R nu_R^4`. No full inverse-covariance estimate and no fixed-reference analytic tail is required.

---

# 6. Combine with the inherited growing-degree collision envelope

The checkpoint `2026-09-20T1130+0300__growing_degree_coarse_tail.md` established for canonical iteration-generated words an envelope of the form

\[
M_R\le \exp\{C R\log(2R)\}
\tag{6.1}
\]

through the source-sufficient growing-degree regime `R=o(log n/log log n)`.

Insert (6.1) into (5.2), and write

\[
y_k=-\log\nu_k.
\]

On every step satisfying (4.5) and (5.1),

\[
\boxed{
y_{k+1}
\ge {3\over2}y_k
-C_0R_k\log(2R_k)-O(1).
}
\tag{6.2}
\]

Consequently, if the saturation theorem can be proved with, for example,

\[
R_k\le C(1+k)^A
\tag{6.3}
\]

for any fixed `A`, then

\[
\sum_{j\ge0}
\left({2\over3}\right)^j
R_j\log(2R_j)<\infty.
\tag{6.4}
\]

Once the initial `y_k` exceeds the resulting absolute discounted-error threshold, (6.2) gives

\[
y_k\ge c(3/2)^k.
\tag{6.5}
\]

Thus

\[
\nu_k\le n^{-3}
\]

after

\[
\boxed{k=O(\log\log n)}
\tag{6.6}
\]

steps.

For polynomial `R_k`, the maximum required degree is only `poly(log log n)`, far inside the already proved collision range `o(log n/log log n)`.

The density floors are also compatible with this scaling. From (4.6),

\[
-\log\eta_k
=y_k+O(R_k\log R_k).
\]

Because the `y_k` grow geometrically, their partial sums are dominated by the final term. By the time `y_k=O(log n)`, the product floor is therefore only `n^{-O(1)}` times subpolynomial factors from the degree term. This is precisely the scale the previous checkpoint identified as acceptable for source-sufficient analytic insertions, provided the constants are tracked explicitly.

So the degree/floor bookkeeping is no longer the main conceptual obstruction. The missing theorem is (5.1).

---

# 7. One more explicit square-cost calculation from the actual `p_3` state

The previous report constructs the actual positive law

\[
p_3=p_2w_{24,0.005}(g_{24})
\]

with

\[
\nu_3<6.9\times10^{-4}+o_{\mathbf P}(1)
\]

and density floor

\[
{p_3\over p_0}\ge3.339\times10^{-4}.
\]

To test whether the exact-cost term itself has entered the expected power-law regime, build the same-mask degree-32 Galerkin system under this **fixed** law. The deterministic Gaussian/Hermite reference system, evaluated with the same fixed projector used in all preceding reports, gives

\[
\nu_{32}^2\approx1.26\times10^{-7}.
\tag{7.1}
\]

This is a fixed-degree covariance/residual calculation. The existing same-mask analytic insertion plus collision transport therefore promotes the deliberately loose finite-model statement

\[
\boxed{
\nu_{32,D}^2\le1.4\times10^{-7}+o_{\mathbf P}(1)
}
\tag{7.2}
\]

outside source-sufficient failure.

Now evaluate the exact square cost at the simple fixed floor

\[
\eta_4=0.01.
\]

The reference value is approximately `5.9e-11`; again this is a quadratic-growth analytic insertion. Hence a conservative transported statement is

\[
\boxed{
J_{32,D}(0.01)
\le7.0\times10^{-11}+o_{\mathbf P}(1).
}
\tag{7.3}
\]

In particular

\[
\sqrt{J_{32,D}(0.01)}
\le8.4\times10^{-6}+o_{\mathbf P}(1).
\tag{7.4}
\]

Compare this with

\[
\nu_{32,D}\lesssim3.75\times10^{-4}.
\]

The main exact-cost term has therefore dropped by a factor exceeding forty already at one further fixed step. Numerically it is consistent with a **quadratic** rather than merely `3/2`-power contraction.

This does **not** prove a fourth positive law `p_4`, because (3.3) still requires a source-sufficient bound on the saturation gap `Delta_32`. The point of (7.2)--(7.4) is to isolate the obstruction: the scalar exact square cost is already safely small; only Galerkin saturation remains.

---

# 8. Exact Schur-complement form of the remaining gap

The saturation gap has a standard but useful exact form that avoids a global minimum-eigenvalue estimate.

Split the full current covariance and target residual into the degree-`R` Galerkin block and its orthogonal coefficient complement:

\[
\Sigma=
\begin{pmatrix}
A&B\\
B^T&C
\end{pmatrix},
\qquad
r=\binom{r_R}{r_\perp}.
\]

The restricted decrement is

\[
\nu_R^2=r_R^TA^{-1}r_R.
\]

Let

\[
S=C-B^TA^{-1}B
\]

be the Schur complement and

\[
\zeta_R=r_\perp-B^TA^{-1}r_R.
\tag{8.1}
\]

Then block inversion gives the **exact identity**

\[
\boxed{
\Delta_R
=\nu^2-\nu_R^2
=\zeta_R^TS^{-1}\zeta_R.
}
\tag{8.2}
\]

Thus the next proof obligation is not `lambda_min(Sigma)>c`. It is a source-coupled bound on the one residual vector `zeta_R` in the complement Schur metric:

\[
\boxed{
\zeta_R^TS^{-1}\zeta_R
\le {1\over2}M_R\nu_R^4.
}
\tag{8.3}
\]

The existing fixed-projector convolution machinery is tailored to exactly these objects: `zeta_R` is a finite list of higher convolution coefficients after subtracting the low-degree covariance columns, and the same Bessel/Parseval plus connected-collision estimates can control its energy without proving a worst-case spectral bound on the whole Fourier subspace.

---

# 9. Intermediate-obligation ledger

| Obligation | Status after this run |
|---|---|
| P06 Randomstrasse Conj. 17 | **KNOWN in later literature; preserve `U_ER^cert=1`; no rescreen** |
| Full P07 source bound | **OPEN / PROVED PARTIAL**; still `sqrt(n) <= E theta <= C sqrt(n log log n)` |
| Actual fixed-slack positive seed | **PROVED PARTIAL** through `p_3`, with `nu_3<6.9e-4+o_P(1)` |
| Exact-cost square lemma | **PROVED** |
| Fixed-reference growing-depth tail | **REJECTED as uniform architecture** because accumulated density creates a deterministic high-chaos block |
| Current-law restart identity `epsilon_R=nu^2-nu_R^2` | **PROVED** |
| Restricted-score `3/2` recurrence | **PROVED conditional only on saturation (5.1)** |
| Growing-degree moment factor | **INHERITED PROVED PARTIAL**, `M_R<=exp(CR log(2R))` |
| `p_3` degree-32 square-cost main term | **PROVED PARTIAL fixed-degree transport**, `J_32(0.01)<=7e-11+o_P(1)` |
| Current-law saturation bound (8.3) | **OPEN; now the sole tail bottleneck** |
| Even cyclic order | **OPEN**; self-inverse frequency untreated |

---

# 10. Next attack

Spend at least 90% useful effort on the **current-law Galerkin saturation theorem (8.3)**. Do not go back to full-score kurtosis, generic `lambda_min`, `max|g|`, worst-case `2->4` norms, or the now-rejected fixed-Gibbs translated tail.

Start at the explicit `p_3` state and degree `R=32`. Expand the Schur residual

\[
\zeta_{32}=r_\perp-B^TA^{-1}r_{32}
\]

in the same fixed-projector Hermite/convolution dictionary. The low-degree coefficients vanish by the Galerkin normal equations. Pair the remaining coefficient words before applying Bessel/Parseval. The desired concrete inequality is

\[
\Delta_{32}
\le {1\over2}M_{32}\nu_{32}^4.
\]

It is acceptable to increase the degree to `R=40,48,...` if the source-specific Schur residual drops materially; the point is to bound the **single residual vector in its Schur metric**, not the entire complement spectrum.

For a uniform theorem, prove that some polynomially growing `R_k` makes

\[
\Delta_{R_k,k}\le {1\over2}M_{R_k,k}\nu_{R_k,k}^4
\]

while preserving the inherited canonical-word moment envelope. Then (5.2) and Section 6 immediately give `nu<=n^-3` in `O(log log n)` steps.

Once `nu<=n^-3`, use the sharp target as the stronger target for each fixed source slack

\[
d=(1+\epsilon)^{-1}<1.
\]

The inherited estimate `lambda_max Sigma<=n/2` then makes the coordinate residual smaller than `(1-d)/sqrt(n)` for all sufficiently large `n`, giving the one-sided selected-moment certificate. Finish with the source-required expectation transfer: the published `theta<=1+4 sqrt(n log n)` fallback has failure at most `2/n`, and the final trivial fallback is `theta<=n`.

Odd cyclic order remains the scope. Even-order removal requires a separate explicit treatment of the self-inverse frequency and must not be asserted before that proof exists.
