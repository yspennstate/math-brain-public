SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B01, 2026-09-24T01:21:55Z.
attacking: an averaged-frequency \(L^r\) residual compiler for the critical two-hub packet, extending the completed fleet01/B01 \(L^2\) theorem without pointwise quadratic decay.

# B01 — \(L^r\) residual interpolation for a critical two-hub packet

Run: \`20260924T012155Z-fleet04-B01-lr-residual-r1\`.

Status: **NEW AVERAGED-FREQUENCY THEOREM / STRICT-N3 SCALE RANGE EXTENDED / FULL QFORM OPEN**.

The unrestricted conjecture remains open. No moment, support, Gaussian, log-concavity, smoothness, or post-rotation independence assumption is introduced. The proof uses only original-coordinate product structure, Hausdorff--Young, and an averaged frequency tail. It never asserts a law-uniform pointwise quadratic oscillatory estimate.

## 1. Input from completed fleet01/B01

The completed theorem at \`math-open-problems@8d7d0ff65e86e787e8da9cb04afe3bfdf5401a59\` treats
\[
Q_0=H^TCH+2H^T(BY+d)+R(Y),
\]
where \(H=(H_1,H_2)\) are two original cap-one hubs, \(Y\) is a disjoint product bank, \(B\) has row rank two, and \(R(Y)\) is arbitrary measurable. If
\[
P=\|p_{BY+d}\|_2,
\]
then its complex-pushforward/Plancherel argument proves
\[
|\phi_{Q_0}(t)|\le \min\{1,\pi P|t|^{-1}\}.
\tag{1.1}
\]
The same source proves
\[
P\le\sqrt2\,\det(BB^T)^{-1/4}.
\tag{1.2}
\]
The exponent \(t^{-1}\) is critical and not integrable.

Fleet01/B01 glued (1.1) to an independent residual with an \(L^2\) density. The next theorem extends that gluing to the full interval \(1<r\le2\).

## 2. Main \(L^r\) residual theorem

### Theorem \`QFORM-TWO-HUB-INDEPENDENT-LR-RESIDUAL-v1\`

Let \(Q=Q_0+Z\), where \(Z\) is independent of \((H,Y)\) and has density \(p_Z\in L^r(\mathbb R)\) for some \(1<r\le2\). Put
\[
r'=\frac r{r-1},\qquad
\alpha=\frac{r-1}{r},\qquad
\theta=\frac1{1+\alpha}=\frac r{2r-1}.
\tag{2.1}
\]
Then \(\phi_Q\in L^1(\mathbb R)\), so \(Q\) has a continuous \(C_0\) density, and
\[
\boxed{
\|p_Q\|_\infty
\le
\frac{1+\alpha}{\pi\alpha}
\left[
\frac{\alpha\pi}{2}
\left(\frac2{r-1}\right)^{1/r}
(2\pi)^\alpha
P\|p_Z\|_r
\right]^\theta .
}
\tag{2.2}
\]

### Proof

Independence gives
\[
|\phi_Q(t)|
\le \min\{1,\pi P|t|^{-1}|\phi_Z(t)|\}.
\tag{2.3}
\]
With the convention \(\widehat f(t)=\int e^{itx}f(x)\,dx\), interpolation between \(L^1\to L^\infty\) and Plancherel gives
\[
\|\phi_Z\|_{r'}\le(2\pi)^{1/r'}\|p_Z\|_r
=(2\pi)^\alpha\|p_Z\|_r.
\tag{2.4}
\]
For \(T>0\), Hölder in frequency yields
\[
\begin{aligned}
\int_{\mathbb R}|\phi_Q(t)|\,dt
&\le2T+\pi P\int_{|t|>T}\frac{|\phi_Z(t)|}{|t|}\,dt\\
&\le2T+\pi P
\left(\frac2{r-1}\right)^{1/r}
T^{-\alpha}\|\phi_Z\|_{r'}.
\end{aligned}
\tag{2.5}
\]
Set
\[
K=\pi P
\left(\frac2{r-1}\right)^{1/r}
(2\pi)^\alpha\|p_Z\|_r.
\]
The right side of (2.5) is \(2T+KT^{-\alpha}\). Its minimizer is
\[
T_*=\left(\frac{\alpha K}{2}\right)^\theta.
\tag{2.6}
\]
At the minimizer, \(KT_*^{-\alpha}=2T_*/\alpha\). Fourier inversion therefore gives
\[
\|p_Q\|_\infty
\le\frac1{2\pi}\,2T_*\left(1+\frac1\alpha\right),
\]
which is exactly (2.2). Since the characteristic function is integrable, the density belongs to \(C_0\). \(\square\)

At \(r=2\), \(\alpha=1/2\), and (2.2) becomes
\[
\|p_Q\|_\infty
\le3\,2^{-2/3}(P\|p_Z\|_2)^{2/3},
\tag{2.7}
\]
exactly the completed fleet01/B01 inequality. Thus (2.2) genuinely extends that result rather than replacing it with a different normalization.

## 3. Source-disjoint hyperbolic residual

Let
\[
Z=2cUV+\beta U+\gamma V+\delta,
\qquad c\ne0,
\tag{3.1}
\]
where \(U,V\) are independent cap-one original coordinates, source-disjoint from \((H,Y)\). Fleet01/B01 proved the sharp collision estimate
\[
\|p_Z\|_2\le\sqrt2\,|c|^{-1/2}.
\tag{3.2}
\]
Since \(\|p_Z\|_1=1\), interpolation between \(L^1\) and (3.2) gives, for every \(1<r\le2\),
\[
\boxed{
\|p_Z\|_r\le2^\alpha|c|^{-\alpha}.
}
\tag{3.3}
\]
Combining (1.2), (2.2), and (3.3) yields
\[
\boxed{
\|p_Q\|_\infty
\le C_r\,
\det(BB^T)^{-\,r/[4(2r-1)]}
|c|^{-(r-1)/(2r-1)},
}
\tag{3.4}
\]
where
\[
C_r=
\frac{1+\alpha}{\pi\alpha}
\left[
\frac{\alpha\pi}{2}
\left(\frac2{r-1}\right)^{1/r}
(2\pi)^\alpha\,2^{\alpha+1/2}
\right]^\theta.
\tag{3.5}
\]
The scaling is exact: under \(A\mapsto sA\), the determinant currency scales as \(s^4\) and \(c\) as \(s\), while the exponents in (3.4) sum to one.

At \(r=2\), \(C_2=3\), so (3.4) recovers the fleet01/B01 bound
\[
\|p_Q\|_\infty\le3\det(BB^T)^{-1/6}|c|^{-1/3}.
\tag{3.6}
\]

## 4. Concrete extension beyond the reciprocal-square regime

Use the strict-N3 family from fleet01/B01. Let
\[
BB^T=k^2I_2,\qquad D=\det(BB^T)=k^4,
\tag{4.1}
\]
retain arbitrary measurable same-bank curvature \(R(Y)\), and take a source-disjoint hyperbolic edge with
\[
c=k^{-q},\qquad q\ge2.
\tag{4.2}
\]
The large two-hub packet supplies four spectral values near \(\pm k\), so for \(k\ge2\) this family remains inside the original target even though the physical residual edge tends to zero.

Choose
\[
r=\frac q{q-1},\qquad
\alpha=\frac1q,\qquad
\theta=\frac q{q+1}.
\tag{4.3}
\]
Then the two scale factors in (3.4) cancel exactly:
\[
D^{-r/[4(2r-1)]}|c|^{-(r-1)/(2r-1)}
=k^{-q/(q+1)}k^{q/(q+1)}=1.
\tag{4.4}
\]
Therefore
\[
\boxed{
\|p_Q\|_\infty\le C_{q/(q-1)}
}
\tag{4.5}
\]
uniformly in \(k\), in the leaf dimension, and in the arbitrary same-bank phase \(R(Y)\).

The completed fleet01 theorem corresponds to \(q=2,r=2\) and gives the sharp constant \(3\). The new \(L^r\) compiler covers every fixed \(q>2\): the source-disjoint hyperbolic edge may now shrink like \(k^{-q}\), arbitrarily faster than \(k^{-2}\), while the output density remains bounded by a constant depending only on \(q\), not on dimension or \(k\).

This is an actual full-target inequality, not a pointwise oscillatory heuristic.

## 5. Exact remaining obstruction

The new theorem changes the analytic threshold but not the structural one. It still requires a source-disjoint scalar residual so that
\[
\phi_Q(t)=\phi_{Q_0}(t)\phi_Z(t).
\]
For an entangled residual, neither a generic conditional density cap nor independence of coordinate sums/differences is available. The next unpaid estimate is a conditional \(L^{r'}(dt)\) frequency budget for the entangled residual, averaged over the active original-coordinate packet, with no pointwise quadratic decay and no extra moment/support assumptions.

The full conjecture remains open, and continuity is proved here only for the stated \(L^r\)-residual branch.

## 6. Source pins and corrections

- Owner/control: fresh \`math-research-brain\` main, revision \`2026-09-22.15\`.
- Required Claude base: \`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837\`, \`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/\`.
- Completed fleet01/B01 input: \`math-open-problems@8d7d0ff65e86e787e8da9cb04afe3bfdf5401a59\`.
- Deterministic check commit: \`6b4904f58f254ad48a1a70f87aa33305abdf5ad3\`.
- The phase-aligned fragmented-support counterexample to uniform pointwise quadratic decay is retained.
- No post-rotation independence, arbitrary conditional projection cap, or small-random-error treatment is used.

Repository transport is not native brain ingestion. Model and thinking metadata remain UNKNOWN.
