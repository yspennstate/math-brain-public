# fleet03/B01 r12 — the order-four endpoint gives all finite L^q bounds at thirteen eigenvalues

Run: `20260924T131114Z-fleet03-B01-fixedmult-r12`  
Current objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Baseline source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Fresh master observed before publication: `8bf72621da7e41feae9a855a6b21e516f6a815d2`.

Status: **PROVED SUPPORTING IMPROVEMENT / THIRTEEN EIGENVALUES GIVE ABSOLUTE CONTINUITY AND EVERY FINITE L^q NORM / NO L^infinity CLAIM / FULL THREE-EIGENVALUE CONJECTURE OPEN.**

The current manuscript proves the bounded-density theorem at seventeen eigenvalues. This note isolates exactly what the same argument already yields at the order-four endpoint. It does not remove the endpoint logarithm, so it does not lower the manuscript's L^infinity threshold from seventeen to thirteen.

## 1. Normalized theorem

Let `X_1,...,X_n` be independent real random variables with probability densities bounded by one. Let `A=A^T` be real symmetric, let `b in R^n`, `c in R`, and

\[
Q=X^TAX+b^TX+c.
\]

Assume

\[
s_{13}(A)\ge1.
\]

Then for every finite `q>=2`, the law of `Q` has a density `p_Q in L^q(R)` and

\[
\boxed{
 \|p_Q\|_q
 \le
 \Bigl(\max\{6010,\,160 e\,q\}\Bigr)^{1-1/q}.
}
\tag{1}
\]

In the **no-pivot branch** of the manuscript, the sharper bound is

\[
\boxed{
 \|p_Q\|_q\le(160e\,q)^{1-1/q}
 \qquad(2\le q<\infty).
}
\tag{2}
\]

In particular,

\[
\boxed{
 \|p_Q\|_2\le\sqrt{320e}=29.493222697882548\ldots .
}
\tag{3}
\]

This is a genuine threshold improvement for absolute continuity and finite-L^q regularity, but not for essential boundedness.

## 2. No-pivot proof: order four is exactly the weak-L^infinity endpoint

Use the manuscript's numerical parameters

\[
\eta=10^{-2},\qquad \kappa=80^{-2}.
\]

Suppose first that `A` has no `eta`-pivot. Apply Proposition `No-pivot spectral-to-volume bound` with `k=4`. Since `4k-3=13`,

\[
V_4(A)\ge\kappa^4.
\tag{4}
\]

The random-coordinate-cut lemma therefore supplies an original-coordinate partition with crossing block `M` satisfying

\[
Z_4(M)\ge4^{-4}\kappa^4=\frac{\kappa^4}{256}.
\tag{5}
\]

The manuscript's volume envelope gives

\[
|\phi_Q(t)|\le\min\{1,u/|t|\},
\qquad
u=\pi e\,Z_4(M)^{-1/8}.
\tag{6}
\]

From (5),

\[
Z_4(M)^{-1/8}
\le 256^{1/8}\kappa^{-1/2}
=2\cdot80=160,
\]
so

\[
\boxed{u\le160\pi e.}
\tag{7}
\]

The point is that (6) is not in `L^1`, but it lies in every `L^p` with `p>1`. For `1<p<=2`,

\[
\begin{aligned}
\int_{\mathbb R}|\phi_Q(t)|^p\,dt
&\le2\int_0^u1\,dt
 +2\int_u^\infty (u/t)^p\,dt\\
&=2u+\frac{2u}{p-1}
=2u\frac p{p-1}.
\end{aligned}
\tag{8}
\]

Let

\[
q=\frac p{p-1}\in[2,\infty),
\qquad p=\frac q{q-1}.
\]

Then (8) reads

\[
\|\phi_Q\|_p^p\le2uq.
\tag{9}
\]

With the manuscript convention `hat f(t)=int e^{itx}f(x)dx`, inverse Hausdorff--Young has the exact interpolation constant

\[
\|\mathcal F^{-1}g\|_q
\le(2\pi)^{-1/p}\|g\|_p.
\tag{10}
\]

For completeness, (10) is obtained by interpolating the inverse-transform bounds `L^1 -> L^infinity` with norm `(2pi)^(-1)` and `L^2 -> L^2` with norm `(2pi)^(-1/2)`.

There is no hidden density assumption in applying (10). If `mu` is the law of `Q`, convolve it with the Gaussian approximate identity `g_epsilon` used in the manuscript. Its density has transform `phi_Q(t)e^{-epsilon t^2}`. Equation (10) gives a uniform `L^q` bound, and weak compactness of `L^q`, together with weak convergence `mu*g_epsilon -> mu`, identifies `mu` with an `L^q` density. Thus

\[
\begin{aligned}
\|p_Q\|_q
&\le(2\pi)^{-1/p}(2uq)^{1/p}\\
&=(uq/\pi)^{1/p}\\
&\le(160e\,q)^{(q-1)/q},
\end{aligned}
\]
which proves (2).

The `q=2` instance gives (3). Notice that the norm grows essentially linearly with `q`; the endpoint `q=infinity` is exactly where this proof fails.

## 3. A quantitative near-Lipschitz small-ball consequence

Still in the normalized no-pivot branch, let `I` be an interval of length `0<h<=e^{-2}`. Set

\[
L=\log(1/h)\ge2,
\qquad q=L.
\]

By Holder and (2),

\[
\begin{aligned}
\Pr(Q\in I)
&\le\|p_Q\|_q h^{1-1/q}\\
&\le(160eL)^{1-1/L}\,e h\\
&\le160e^2\,h\log(1/h).
\end{aligned}
\tag{11}
\]

Hence

\[
\boxed{
 \Pr(Q\in I)
 \le160e^2\,|I|\log(1/|I|)
 \quad(0<|I|\le e^{-2})
}
\tag{12}
\]

in the no-pivot normalized thirteen-eigenvalue chamber. The coefficient is

\[
160e^2=1182.248975828904\ldots .
\]

This makes the remaining endpoint obstruction concrete: the present machinery is one logarithm away from the uniform linear small-ball bound needed for an `L^infinity` density theorem.

## 4. Why all pivot branches already close at thirteen eigenvalues

Now suppose `A` has an `eta`-pivot. The existing main-proof pivot arguments need fewer than seventeen large eigenvalues.

### Scalar pivot

A nonzero scalar pivot removes at most one large spectral direction under the manuscript's Schur count. From `s_13(A)>=1`, its Schur complement therefore has at least twelve eigenvalues of modulus at least one, hence in particular `s_9>=1`. The manuscript's nine-eigenvalue full half-potential theorem and scalar square profile give

\[
\|p_Q\|_\infty\le\eta^{-1/2}\cdot601=6010.
\tag{13}
\]

### Definite pair

The manuscript's definite-pair lemma directly gives

\[
\|p_Q\|_\infty\le\pi\eta^{-1/2}=10\pi<40.
\tag{14}
\]

### Indefinite pair

An invertible two-coordinate pivot removes at most two large spectral directions, so its Schur complement retains at least eleven. In particular its operator norm is at least one, which is all the manuscript's logarithmic-potential estimate needs. The existing hyperbolic-pair calculation therefore gives the same

\[
\|p_Q\|_\infty<251.
\tag{15}
\]

Thus every pivot branch under `s_13>=1` has `L^infinity` density at most 6010. Since a probability density satisfying `||p||_infinity<=M` obeys `||p||_q<=M^{1-1/q}`, combining the pivot and no-pivot branches proves (1).

## 5. General density cap K and spectral scale s

Let the independent coordinate densities be bounded by `K>0` and assume

\[
s_{13}(A)\ge s>0.
\]

Set `Y=KX` and

\[
\widetilde Q
=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c,
\qquad
Q=(s/K^2)\widetilde Q.
\]

The coordinates of `Y` have density cap one and `s_13(A/s)>=1`. Density scaling gives

\[
\|p_Q\|_q
=(K^2/s)^{1-1/q}\|p_{\widetilde Q}\|_q.
\]

Therefore, for every finite `q>=2`,

\[
\boxed{
 \|p_Q\|_q
 \le
 \left(\frac{K^2}{s}\right)^{1-1/q}
 \Bigl(\max\{6010,160e\,q\}\Bigr)^{1-1/q}.
}
\tag{16}
\]

Every original theorem quantifier is retained: arbitrary dimension, arbitrary signs, arbitrary remaining spectrum, arbitrary affine terms, and arbitrary rough product densities subject only to the density cap.

## 6. Applying the completed fleet04/B01 averaged-frequency theorem to an actual inequality

The older B01 assignment designated `fleet04/B01` as partner. Its completed source report

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260924T012155Z-fleet04-B01-lr-residual-r1/REPORT.md`

proves the following `r=2` compiler. For the critical two-hub packet

\[
Q_0=H^TCH+2H^T(BY+d)+R(Y),
\]
with `H=(H_1,H_2)` two original cap-one hubs, `Y` a disjoint product bank, `B` of row rank two, `R` arbitrary measurable, and

\[
P=\|p_{BY+d}\|_2,
\]
if `Z` is source-disjoint from `(H,Y)` and has `p_Z in L^2`, then

\[
\|p_{Q_0+Z}\|_\infty
\le3\,2^{-2/3}(P\|p_Z\|_2)^{2/3}.
\tag{17}
\]

It also records

\[
P\le\sqrt2\,\det(BB^T)^{-1/4}.
\tag{18}
\]

Apply (17) to a source-disjoint normalized no-pivot quadratic residual

\[
Z=W^TSW+\beta^TW+\gamma,
\qquad s_{13}(S)\ge1,
\]
whose original coordinates `W` have independent cap-one densities. Equation (3) gives

\[
\|p_Z\|_2\le\sqrt{320e}.
\]

Substituting this and (18) into (17) yields the concrete bounded-density inequality

\[
\boxed{
 \|p_{Q_0+Z}\|_\infty
 \le3(160e)^{1/3}\det(BB^T)^{-1/6}
 <22.730\,\det(BB^T)^{-1/6}.
}
\tag{19}
\]

Thus the order-four endpoint's `L^2` currency is genuinely usable: although it does not by itself yield an `L^infinity` density at thirteen eigenvalues, it closes after combination with a source-disjoint critical two-hub packet through the completed partner theorem.

This application is scoped exactly as stated. It does not assert that every thirteen- or three-eigenvalue form decomposes into such source-disjoint pieces.

## 7. Relation to the phase-aligned obstruction

Nothing above uses, or revives, a uniform pointwise quadratic-phase bound. The known phase-aligned fragmented-support construction still makes `Re E exp(i tau X^2)` arbitrarily close to one at any prescribed nonzero frequency `tau`. The present estimate instead starts from the manuscript's joint crossing-determinant bound, whose order-four consequence is the averaged `L^p`, `p>1`, control in (8).

## 8. Exact remaining obligation

This run does **not** prove the thirteen-eigenvalue bounded-density theorem. It identifies its endpoint sharply:

- `s_13>=1`, no pivot -> `Z_4` currency -> `|phi(t)| <= min(1,u/|t|)` with `u<=160 pi e`;
- this yields every finite `L^q` density norm with growth `O(q)` and small-ball `O(h log(1/h))`;
- to lower the manuscript's `L^infinity` threshold from 17 to 13 one must remove that logarithm, equivalently obtain a dimension-free uniform-in-q improvement from additional quadratic/product structure rather than from the absolute envelope alone.

A black-box `1/|t|` estimate cannot do this. The next proof mechanism should exploit cancellation or a second compatible crossing currency before taking the decisive absolute value.

## 9. Scope/status

- Baseline seventeen-eigenvalue candidate: unchanged.
- New thirteen-eigenvalue finite-`L^q` theorem: **proved in this report; independent review not yet claimed**.
- New thirteen-eigenvalue `L^infinity` theorem: **not proved**.
- Continuity at thirteen eigenvalues: **not proved by this endpoint argument**. The law is absolutely continuous and belongs to every finite `L^q`.
- Full unrestricted three-eigenvalue conjecture: **OPEN**.
- No Gaussian, moment, log-concavity, bounded-support, connected-support, diagonal-basis, or post-rotation independence assumption is used.
