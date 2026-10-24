SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-24T07:00:11Z.
attacking: dimension-free majority-sheet regularity versus diffuse leverage; sharpen submass stability and independently audit the ruled rough-input bridge.

# Early calculation — leverage-sensitive ruled submass stability

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: full QFORM OPEN. This note pays a regularity implication on the completed ruled majority sheet; it does not address the complementary two-sheet/convex side.
Execution: `WITHOUT_VERIFIED_BRAIN`.

Let `R in R^{n x 3}` have orthonormal columns and

\[
q_R(X)=\langle r_1,X\rangle^2+\langle r_2,X\rangle^2-\langle r_3,X\rangle^2.
\]

Write `rho_j in R^3` for the j-th row of R and `a_j=|rho_j|^2`. Then

\[
0\le a_j\le1,\qquad \sum_j a_j=3.
\]

The preceding account02/B15 submass theorem (`math-open-problems@45779cb1dca5f453ac620431b380ad015a052e70`) gives, when the j-th original-coordinate factor is a cap-one subdensity of mass `m<=1`, the ruling-wise two-dimensional trace estimate

\[
h_\theta\le 2\min\left(1,{m\over\sqrt{d_j(\theta)}}\right),
\]

where, for the unit ruling direction `\hat v_\theta=(e_\theta^\perp+e_3)/\sqrt2` and its orthogonal projection `U_\theta` onto `\hat v_\theta^\perp`,

\[
d_j(\theta)=1-|U_\theta\rho_j|^2.
\]

The elementary observation not used in the preceding square-root proof is

\[
\boxed{d_j(\theta)\ge1-a_j\quad\text{for every }\theta.}
\]

Indeed orthogonal projection cannot increase Euclidean norm. The exact ruled coarea factor is `1/2` and the ruling parameter has speed `sqrt(2)`, so the positive-sheet output submeasure `nu_{j,m}^+` satisfies

\[
H(\nu_{j,m}^+)
\le {1\over2\sqrt2}\int_0^{2\pi}h_\theta\,d\theta
\le \sqrt2\,\pi\min\left(1,{m\over\sqrt{1-a_j}}\right),
\tag{E1}
\]

with the second term interpreted as unavailable when `a_j=1`. Combining (E1) with the preceding orientation-uniform square-root bound gives

\[
\boxed{
H(\nu_{j,m}^+)
\le
\min\left\{20\sqrt2\sqrt m,
\sqrt2\pi\min\left(1,{m\over\sqrt{1-a_j}}\right)
\right\}.
}
\tag{E2}
\]

Thus a low-leverage coordinate has a linear-in-mass stability cost. In particular, if `a_j<=1/2`,

\[
\boxed{H(\nu_{j,m}^+)\le2\pi m.}
\tag{E3}
\]

Now compare two cap-one product laws `f=(f_i)` and `g=(g_i)`. Put `delta_j=||f_j-g_j||_1` and telescope the products in original coordinates. The positive and negative parts of `f_j-g_j` are cap-one subdensities of mass `delta_j/2`. Hence the signed j-th telescoping contribution has majority-sheet density norm

\[
\le \min\left\{40\sqrt{\delta_j},
{\sqrt2\pi\,\delta_j\over\sqrt{1-a_j}}
\right\}.
\tag{E4}
\]

For the heavy set `H={j:a_j>3/4}`, the trace identity `sum a_j=3` implies `|H|<=3`. On its complement, (E4) is at most `2 sqrt(2) pi delta_j`. Therefore, with `Delta=sum_j delta_j`,

\[
\boxed{
||r_f^+-r_g^+||_\infty
\le 2\sqrt2\pi\,\Delta+40\sqrt{3\Delta}.
}
\tag{E5}
\]

This is dimension-free in the aggregate product `L1` perturbation `Delta`; all square-root instability is confined to at most three high-leverage original coordinates. If `max_j a_j<=1/2`, no heavy coordinates are needed and (E4) gives the sharper Lipschitz estimate

\[
\boxed{||r_f^+-r_g^+||_\infty\le2\pi\Delta.}
\tag{E6}
\]

These are essential-height statements. Continuity is not used: (E1)-(E6) are first proved for smooth factors via the exact ruling formula and then pass to arbitrary rough factors by product `L1` convergence, restriction, and deterministic pushforward, all of which contract total variation.

A concrete exact-target family is obtained from three disjoint banks of size m:

\[
Y_k=m^{-1/2}\sum_{j=1}^m X_{k,j},\qquad Q_m=Y_1^2+Y_2^2-Y_3^2.
\]

Its matrix has spectrum `{1,1,-1,0,...,0}` and every row leverage is `1/m`. For `m>=2`, (E6) applies uniformly in m. Every invertible physical `3x3` principal block, however, has curvature scale exactly `1/m`; thus the latest account03/B15 localized-triple theorem would pay a bound of order m, whereas the ruled majority-sheet estimate stays universal. This is a source-valid obstruction to a proof interface that selects and reciprocates one physical triple before aggregating the diffuse banks.
