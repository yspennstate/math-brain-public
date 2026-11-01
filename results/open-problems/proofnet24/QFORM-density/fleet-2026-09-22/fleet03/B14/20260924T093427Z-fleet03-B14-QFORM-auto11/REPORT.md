SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-24T09:34:27Z.
attacking: whether the checked Gaussian-mixture full theorem can be a zero-loss localization mechanism for arbitrary translated, fragmented, or unbounded cap-one input laws.

# B14 report: a sharp BV obstruction to uniform Gaussian-mixture localization

Run: `20260924T093427Z-fleet03-B14-QFORM-auto11`.
Full unrestricted QFORM status: `OPEN / NOT PROVED / NOT DISPROVED`.
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source theorem being tested

The completed interactive theorem
`NEW_GAUSSIAN_MIXTURE_FULL_THEOREM.md` at
`yspennstate/math-open-problems@9dabaf2aaf66687c2b4437fdb359b1aeb4a804bc`
proves the full arbitrary-rank/sign QFORM bound for independent coordinates of the form

\[
X_i=M_i+\sqrt{T_i}G_i,
\qquad \mathbb E T_i^{-1/2}\le \sqrt{2\pi}.
\]

For random centers this inverse-half-variance condition is stronger than the final marginal cap \(\|f_i\|_\infty\le1\). The question attacked here is whether arbitrary cap-one marginals can nevertheless be approximated, with the condition kept uniformly at \(\sqrt{2\pi}\), so that the checked Gaussian-mixture theorem could be transferred by weak localization.

The answer is no, already in one dimension and already for two distant fragments.

## 2. Gaussian peak-moment implies a uniform BV bound

Let

\[
g(x)=\int \phi_t(x-m)\,d\Pi(m,t),
\qquad
\phi_t(u)=\frac{1}{\sqrt{2\pi t}}e^{-u^2/(2t)},
\]

where \(t>0\), and define

\[
M:=\int t^{-1/2}\,d\Pi(m,t)<\infty.
\]

Then

\[
\boxed{\|g\|_\infty\le \frac{M}{\sqrt{2\pi}}}
\tag{2.1}
\]

because each component is bounded by \((2\pi t)^{-1/2}\).

More importantly, \(g\in W^{1,1}(\mathbb R)\) and

\[
\boxed{\operatorname{Var}(g)=\|g'\|_1
\le \sqrt{\frac2\pi}\,M.}
\tag{2.2}
\]

Indeed

\[
\phi_t'(u)=-\frac{u}{t}\phi_t(u)
\]

and therefore

\[
\|\phi_t'\|_1
=\frac{1}{\sqrt t}\,\mathbb E|G|
=\sqrt{\frac2\pi}\,t^{-1/2}.
\]

Fubini/Tonelli in the distributional derivative gives

\[
\|g'\|_1
\le\int\|\phi_t'\|_1\,d\Pi
=\sqrt{\frac2\pi}\,M.
\]

At the exact hypothesis of the checked QFORM mixture theorem,

\[
M\le\sqrt{2\pi},
\]

we obtain simultaneously

\[
\boxed{0\le g\le1,\qquad \int g=1,
\qquad \operatorname{Var}(g)\le2.}
\tag{2.3}
\]

Thus the mixture condition imposes a global geometric regularity constraint absent from the owner target.

## 3. The obstruction survives weak convergence

Let \(g_j\,dx\Rightarrow f\,dx\) weakly as probability measures, and suppose

\[
\sup_j \operatorname{Var}(g_j)\le V.
\]

Then

\[
\boxed{\operatorname{Var}(f)\le V.}
\tag{3.1}
\]

For every \(\psi\in C_c^1(\mathbb R)\), weak convergence gives

\[
\int f\psi'
=\lim_j\int g_j\psi'.
\]

Since

\[
\left|\int g_j\psi'\right|
\le \operatorname{Var}(g_j)\|\psi\|_\infty,
\]

we obtain

\[
\left|\int f\psi'\right|
\le V\|\psi\|_\infty.
\]

Taking the supremum over the standard BV test class proves (3.1).

Consequently, every weak limit of Gaussian location-scale mixtures satisfying

\[
\mathbb E T^{-1/2}\le\sqrt{2\pi}
\]

has one-dimensional total variation at most two.

This is stronger than an \(L^1\)-closure obstruction: even the weak/Portmanteau localization used elsewhere in the fleet cannot bypass it.

## 4. Two fragments already defeat uniform localization

For \(N\ge2\) and \(L>0\), let

\[
I_k=\left[k\left(L+\frac1N\right),
\ k\left(L+\frac1N\right)+\frac1N\right],
\qquad k=0,\dots,N-1,
\]

and put

\[
E_{N,L}=\bigcup_{k=0}^{N-1}I_k,
\qquad f_{N,L}=\mathbf 1_{E_{N,L}}.
\]

Then \(|E_{N,L}|=1\), so \(f_{N,L}\) is an admissible cap-one probability density. It has

\[
\operatorname{Var}(f_{N,L})=2N.
\]

Therefore no sequence of Gaussian location-scale mixtures with the checked theorem's uniform condition

\[
\mathbb E T^{-1/2}\le\sqrt{2\pi}
\]

can converge weakly to \(f_{N,L}\) once \(N\ge2\).

More generally, if \(g_j\,dx\Rightarrow f_{N,L}\,dx\) are Gaussian mixtures with moments

\[
M_j:=\mathbb E T_j^{-1/2},
\]

then (2.2) and lower semicontinuity imply the necessary quantitative cost

\[
2N\le \liminf_j\operatorname{Var}(g_j)
\le \sqrt{\frac2\pi}\,\liminf_j M_j,
\]

hence

\[
\boxed{\liminf_j M_j\ge N\sqrt{2\pi}.}
\tag{4.1}
\]

Thus fragment count is paid linearly by the inverse-scale moment. The allowed value \(\sqrt{2\pi}\) can approximate at most the one-fragment BV budget; it cannot be a universal localization parameter for the arbitrary-fragment owner target.

The statement is translation invariant, because translating a Gaussian mixture only translates its component centers and leaves \(M\) unchanged.

## 5. Quantitative L1 separation for distant fragments

The preceding weak obstruction can be made quantitative. Let \(g\) be any probability density satisfying

\[
0\le g\le1,
\qquad \operatorname{Var}(g)\le V.
\]

Set

\[
e=\|f_{N,L}-g\|_1.
\]

Because both are probability densities and \(g\le1\),

\[
\int_{E_{N,L}}g=1-\frac e2.
\tag{5.1}
\]

For each occupied interval define its average

\[
A_k=N\int_{I_k}g,
\]

and for each gap \(G_k\) of length \(L\) define

\[
B_k=L^{-1}\int_{G_k}g.
\]

Choose \(x_k\in I_k\) with \(g(x_k)\ge A_k\), choose \(y_k\in G_k\) with \(g(y_k)\le B_k\), and choose tail points on the far left and right where \(g\) is arbitrarily small. Evaluating total variation on the ordered sequence of these points gives

\[
\operatorname{Var}(g)
\ge 2\sum_{k=0}^{N-1}A_k
-2\sum_{k=0}^{N-2}B_k.
\]

Now

\[
\sum_k A_k=N\left(1-\frac e2\right)
\]

by (5.1), while all gap mass is at most \(e/2\), so

\[
\sum_k B_k\le \frac{e}{2L}.
\]

Therefore

\[
V\ge2N-Ne-\frac eL,
\]

or

\[
\boxed{
\|f_{N,L}-g\|_1
\ge\frac{2N-V}{N+L^{-1}}.
}
\tag{5.2}
\]

For the checked Gaussian-mixture hypothesis, \(V=2\), so

\[
\boxed{
\|f_{N,L}-g\|_1
\ge\frac{2(N-1)}{N+L^{-1}}.
}
\tag{5.3}
\]

As the fragments are moved farther apart, \(L\to\infty\), the lower bound tends to

\[
2-\frac2N.
\]

For many fragments the target density is therefore almost maximally far in total variation from every mixture law covered by the checked theorem.

## 6. Unbounded-support version

Let

\[
E_\infty=\bigcup_{k\ge1}[k^2,k^2+2^{-k}],
\qquad f_\infty=\mathbf1_{E_\infty}.
\]

Since \(\sum_{k\ge1}2^{-k}=1\), this is another admissible cap-one probability density, now with unbounded support. Its variation is infinite because every interval contributes two jumps.

Hence \(f_\infty\,dx\) cannot be a weak limit of any sequence of Gaussian mixtures whose inverse-half-variance moments remain uniformly bounded, in particular not of the owner-normalized class \(M\le\sqrt{2\pi}\).

This shows that neither remote fragments nor unbounded support can be removed by a uniform Gaussian-component-peak localization.

## 7. Required partner application to an actual QFORM inequality

Use the completed fleet04/B14 theorem
`QFORM scale-covariant three-coordinate Schur localization` at

`yspennstate/math-open-problems@deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260924T001624Z-fleet04-B14-scaled-schur-localization-r10/REPORT.md`.

Take

\[
B_*=I_3-\frac23\mathbf1\mathbf1^T,
\qquad \operatorname{spec}(B_*)=\{1,1,-1\}.
\]

Let \(X_1\) have the fragmented density \(f_{N,L}\) above, and let \(X_2,X_3\) be arbitrary independent cap-one variables. For

\[
Q=X^TB_*X,
\]

we are in the exact owner target and the partner theorem applies with \(\sigma=1\):

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le6\sqrt\pi.
}
\tag{7.1}
\]

This is an actual inequality on a family whose first marginal is quantitatively excluded from every uniformly normalized Gaussian-mixture localization by (5.3).

Thus the Gaussian-mixture full theorem is a valid powerful chamber, but its missing arbitrary-rough-law step cannot be supplied by a constant-preserving weak or total-variation localization with the same inverse-half-variance bound.

This does not refute the QFORM conjecture; (7.1) explicitly confirms the opposite on this chamber.

## 8. Consequence for proof architecture

The owner target permits arbitrarily many fragments and unbounded supports. Any attempt to transfer the checked Gaussian determinant theorem to all cap-one laws by first writing or approximating each marginal as a location-scale Gaussian mixture must therefore do one of the following:

1. allow the inverse-half-variance moment to grow with fragmentation, which destroys a universal transfer if inserted directly into the existing determinant averaging;
2. exploit cancellation or grouping before the mixture peak moment is paid;
3. use a different localization class whose compactness does not impose a uniform BV bound.

The useful surviving direction is therefore not a per-coordinate Gaussian-mixture approximation. Product-preserving grouping, direct small-ball estimates, or a receiver that averages the rough fragments jointly with the matrix geometry are still required.

## 9. Status and novelty discipline

This run proves the BV and quantitative separation statements above from first principles. The consumed Gaussian-mixture theorem itself already warns qualitatively that random separated centers are a gap; this report turns that warning into an explicit weak-closure obstruction and a sharp linear fragment-cost inequality. No literature-wide novelty claim is made. Repository code search for an exact prior fleet statement was rate-limited during this run, so this result is published as a scoped supporting/correction theorem, not as a novelty claim.

Full QFORM remains open. Continuity of the full arbitrary-law target remains open; the partner inequality used here is an essential-height statement.
