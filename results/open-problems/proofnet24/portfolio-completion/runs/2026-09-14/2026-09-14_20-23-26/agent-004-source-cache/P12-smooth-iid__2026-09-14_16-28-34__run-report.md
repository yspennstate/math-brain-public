# ProofNet24 P12 — Smooth IID Least Singular / Phase-Retrieval Stability

**Run:** 2026-09-14 16:28:34 Asia/Jerusalem  
**Scope:** real iid least-singular-value extremes, smooth/bounded-density laws, phase-retrieval stability; **NO number theory**.  
**Status:** **major closure of the fixed-law real finite-variance frontier.** The exact smooth-iid Conjecture 8.2 is now mathematically proved for every one fixed centered variance-one real iid entry law with bounded Lebesgue density and finite variance, including the moderate-surplus extension. The result is candidate-complete mathematically but not ProofNet24-closed: two OTHER complete audits of the new assembled finite-variance chain are still required.

## 0. Exact source statement

The June 28 source manuscript is **Extreme least singular values with redundancy, radial ensembles, and quantitative stability of phase retrieval**. The 4 August collaborator thread explicitly identifies its Conjecture 8.2 as the project being pursued.

For
\[
A_m\in\mathbb R^{N_m\times m},\qquad N_m/m\to\gamma>1,
\]
with iid real entries, define
\[
M_{m,r}(A_m)=\min_{|T|=m+r}\sigma_m((A_m)_T).
\]
The real source conjecture is
\[
\boxed{
\frac1m\log M_{m,r}(A_m)\xrightarrow{\mathbb P}-\frac{h(\gamma)}{r+1},
\qquad
h(\gamma)=\gamma\log\gamma-(\gamma-1)\log(\gamma-1)
}
\]
for fixed integer \(r\ge0\). The source predicts the complex exponent \(-h(\gamma)/(2(r+1))\), still open.

The moderate-surplus form writes \(k_m=r_m+1\) and asks for
\[
\boxed{
\frac{k_m}{m}\log M_{m,r_m}(A_m)\to-h(\gamma)
}
\]
when \(k_m\log m=o(m)\).

At phase-retrieval redundancy \(N_m=2m-1+r_m\), full spark gives the exact deterministic identity \(\omega(A_m)=M_{m,r_m}(A_m)\), and \(h(2)=\log4\).

The August 6 normalization remark is exact scaling: if \(A=\sigma\widetilde A\), then
\[
M_{m,r}(A)=|\sigma|M_{m,r}(\widetilde A).
\]
For a triangular variance scale \(\sigma_m\), exponent neutrality requires
\[
\boxed{\frac{k_m}{m}|\log\sigma_m|\to0.}
\]
For one fixed positive variance this is automatic.

## 1. Prior state and OTHER reports

The latest P12 state, `P12_smooth_iid_least_singular_2026-09-14_15-20-36.md`, had already proved a real triangular-array theorem under bounded density plus the clean-row rarity condition
\[
m\Pr\{|\xi_m|>a\sqrt{m/\log m}\}\to0,
\]
and, for one fixed finite-variance bounded-density law, a density-level one-normal local CLT on fixed-parameter incompressible directions. Its remaining stated obstacle was the geometry of heavy-tailed random normals and near-parallel overlapping pairs.

P13's latest report proves the same clean-row-rarity theorem with summable deviations and verifies the exact staged normalization
\[
s=t/\sqrt{k},
\]
not \(\sqrt{t/k}\).

P14 proves the fixed-apex pair kernel at sharp \(1+C/D\) under a \(2+\delta\) moment. The newer P24 report removes the higher-moment assumption from the **fixed-angle anti-alignment** mechanism under one fixed finite-variance law: each fresh cut has a law-dependent positive probability of an angular loss \(c/k\), and a sequential adapted Chernoff bound gives
\[
\Pr\{1-(v\cdot w)^2\le y_*\mid A,v\}\le e^{-c_\xi D}
\]
for one fixed \(y_*>0\).

## 2. Tail-free one-normal geometry from random rounding

The decisive external input is Galyna Livshyts, *The smallest singular value of heavy-tailed not necessarily i.i.d. random matrices via random rounding*, J. Analyse Math. 145 (2021), arXiv:1811.07038v4.

Her Section 6 random-subspace argument, in particular Lemma 6.4 together with the compressible-vector theorem, gives exponential incompressibility of a random normal under bounded concentration and the regularized-Hilbert-Schmidt moment condition. For our fixed iid law:

\[
\mathbb E\xi=0,\qquad \mathbb E\xi^2=1,\qquad \|f_\xi\|_\infty\le K,
\]

bounded density implies a concentration function separated from one, and for the relevant \((m-1)\times m\) iid hyperplane matrix the \(p=1\) moment condition is exactly a second-moment Hilbert-Schmidt bound. Hence there are fixed law-dependent constants \(\delta,\rho,c>0\) with
\[
\boxed{
\Pr\{u_m\in\mathrm{Comp}(\delta,\rho)\}\le e^{-cm},
}
\]
where \(u_m\) is the unit null direction of one fixed iid \((m-1)\times m\) hyperplane matrix.

No fourth moment and no \(O(\sqrt m)\) operator-norm event is required.

## 3. Exponentially many normals: fraction, not union bound

Choose a base pool of \(n_0=\lfloor\beta m\rfloor\) rows, \(1<\beta<\gamma\), and let
\[
\mathcal H_m=\{S\subset[n_0]:|S|=m-1\},\qquad L_m=|\mathcal H_m|.
\]
Then
\[
\log L_m=h(\beta)m+o(m).
\]
Each normal \(u_S\) has the same marginal distribution as the Livshyts random normal. Therefore
\[
\mathbb E\frac1{L_m}\#\{S:u_S\text{ compressible}\}\le e^{-cm}.
\]
By Markov,
\[
\boxed{
\Pr\left\{\#\{S:u_S\text{ bad}\}>e^{-cm/2}L_m\right\}\le e^{-cm/2}.
}
\]
Thus an overwhelming fraction of the exponential family is useful. No union bound over hyperplanes is needed.

For these fixed-parameter incompressible normals, P12-LD-04 supplies a density floor and ceiling at zero:
\[
\boxed{
c_\xi s\le \Pr\{|\langle X,u\rangle|\le s\}\le C_\xi s,
\qquad 0<s\le1,
}
\]
uniformly in every useful normal, including exponentially small \(s\).

## 4. New deterministic two-slab bound

Let \(X\) have independent coordinates with density at most \(K\). For arbitrary deterministic unit vectors \(u,v\), write \(\rho=u\cdot v\). The Livshyts–Paouris–Pivovarov two-dimensional marginal theorem gives density at most \(2K^2\) in any orthonormal two-dimensional projection. Passing from an orthonormal basis of \(\mathrm{span}\{u,v\}\) to \((u,v)\) costs the Jacobian
\[
\sqrt{1-\rho^2}.
\]
Therefore
\[
\boxed{
\Pr\{|\langle X,u\rangle|\le s,\ |\langle X,v\rangle|\le s\}
\le
\frac{8K^2s^2}{\sqrt{1-\rho^2}}.
}
\tag{P12-2SLAB-BD}
\]
This has no moment and no diffuseness assumption. If \(1-\rho^2\ge y_*\), it is simply \(C_{K,y_*}s^2\).

## 5. Heavy-tail pair geometry without a global norm event

For two base hyperplanes \(S,T\), set
\[
D=m-|S\cap T|.
\]
The shared block has \(m-D\) rows and each private block has \(D-1\) rows.

### High overlap
For fixed \(S\), the number of \(T\)'s with a given \(D\) is exactly
\[
\binom{m-1}{D-1}\binom{n_0-m+1}{D-1}.
\]
For \(D=\delta m+O(1)\), the exponent per fixed \(S\) is
\[
g_\beta(\delta)=H(\delta)+(\beta-1)H\!\left(\frac\delta{\beta-1}\right).
\]
Since \(g_\beta(\delta)\downarrow0\) as \(\delta\downarrow0\), choose fixed \(\delta_0>0\) so all pairs with \(D<\delta_0m\) form at most \(e^{-\kappa m}L_m^2\) ordered pairs.

### Low overlap
If \(D\ge\delta_0m\), condition on the shared rows and first private normal. P24-MIDEDGE-FV gives one fixed \(y_*(\xi)>0\) with
\[
\Pr\{1-\rho^2\le y_*\mid A,u_S\}\le e^{-c_\xi D}\le e^{-c_\xi\delta_0m}.
\]
Averaging over pairs and applying Markov shows that, with probability \(1-e^{-cm}\), the number of low-overlap near-parallel pairs is at most \(e^{-cm}L_m^2\).

Thus, with exponentially high probability, the complete exceptional-pair graph satisfies
\[
\boxed{e_0\le e^{-\kappa m}L_m^2.}
\tag{P12-PAIR-GEOM-FV}
\]
For every nonexceptional pair P12-2SLAB-BD gives \(Cs^2\); for exceptional pairs the one-dimensional density ceiling gives \(Cs\). These are exactly the two pair probabilities required by the source graph recursion.

## 6. Peer audit — P24 finite-variance sequential anti-alignment

**AUDIT_FOR=P24**  
**Source:** `2026-09-14_15-53-57__run-report.md`  
**Claim IDs:** `P24-UI-FV`, `P24-ENERGY-FV`, `P24-STEP-LOSS-FV`, `P24-MIDEDGE-FV`.  
**Verdict:** **PROVED / PASS.**

The uniform-integrability lemma is valid by truncating the coordinate law and controlling the bounded part in fourth moment. The projected-energy lemma is valid by splitting \(X^TPX-k\) into a diagonal integrable part and an off-diagonal quadratic part with variance at most \(2k\). Uniform integrability then yields a fixed interval \([1/4,M]\) for \((q^TX)^2\) with positive probability, while projected energy is at most \(2k\) with probability tending to one. Hence every sufficiently large fresh cut has a fixed law-dependent probability of loss at least \(1/(8k)\).

Sequentially, the exact projector identity gives
\[
(v\cdot w)^2=\prod_{k=2}^{D}(1-Z_k).
\]
Conditional on the past, every next row is a fresh original product-law row, so the one-step success probability remains bounded below. The conditional Laplace-transform argument gives an adapted Chernoff lower-tail bound. Fixed near-parallelity would require too few successful losses, hence
\[
\Pr\{1-(v\cdot w)^2\le y_*\mid A,v\}\le e^{-cD}.
\]
No projected-coordinate independence or higher moment is used.

## 7. Original staged recursion now closes at finite variance

Let \(k=k_m=r_m+1\) and fix \(\varepsilon>0\). Put
\[
\lambda=h(\gamma)-\varepsilon,
\qquad
t=e^{-\lambda m/k},
\qquad
\boxed{s=t/\sqrt{k}}.
\]
Choose \(1<\beta<\gamma\) so \(h(\beta)>\lambda\), and split reserved fresh rows into \(k\) batches of size \(b\asymp m/k\).

The source one-stage graph lemma applies with fixed law-dependent constants:
\[
\boxed{M_j\ge\theta sM_{j-1},\qquad e_j\le As e_{j-1}.}
\]
The entropy checks are unchanged:
\[
\log(s^kL_m)
\ge
(h(\beta)-\lambda)m-\frac{k}{2}\log k-O(k)+o(m)\to+\infty,
\]
and
\[
\log\frac{e_j}{sM_j^2}
\le
-\kappa m+\frac{k}{2}\log k+O(k)\to-\infty.
\]
Both use \(k\log m=o(m)\). All stages succeed except with probability at most
\[
Ck e^{-cm/k}+Ce^{-cm}.
\]
At the end the selected rows obey
\[
\sum_{j=1}^{k}|\langle X_j,u\rangle|^2\le ks^2=t^2,
\]
so an actual \((m+k-1)\times m\) row submatrix has
\[
\sigma_m\le t.
\]

The lower exponential bound is unchanged and uses only bounded density: for a fixed \((m+k-1)\times m\) submatrix,
\[
\Pr\{\sigma_m\le t\}\le e^{O(k\log m)}t^k.
\]
There are \(e^{h(\gamma)m+o(m)}\) choices, so at
\[
t_-=e^{-(h(\gamma)+\varepsilon)m/k}
\]
the union bound is \(e^{-\varepsilon m+o(m)}\).

## 8. Main theorem P12-MAIN-FV

Let \(\xi\) be one fixed real law satisfying
\[
\boxed{
E\xi=0,\qquad E\xi^2=1,\qquad \|f_\xi\|_\infty<\infty.
}
\]
Let \(A_m\) have iid entries \(\xi\), \(N_m/m\to\gamma>1\), and \(k_m=r_m+1\) with \(k_m\log m=o(m)\). Then
\[
\boxed{
\frac{k_m}{m}\log M_{m,r_m}(A_m)\xrightarrow{\mathbb P}-h(\gamma).
}
\tag{P12-MAIN-FV}
\]
For fixed \(r\),
\[
\boxed{
\frac1m\log M_{m,r}(A_m)\xrightarrow{\mathbb P}-\frac{h(\gamma)}{r+1}.
}
\]
Thus the real fixed-law smooth-iid Conjecture 8.2 holds under assumptions strictly weaker than its original wording: **bounded density plus finite variance are enough.**

The proof yields a summable qualitative failure bound of the form
\[
C_{\xi,\varepsilon}e^{-c_{\xi,\varepsilon}m}
+
C_{\xi,\varepsilon}k_m e^{-c_{\xi,\varepsilon}m/k_m}
+
e^{-\varepsilon m+o(m)}.
\]
Hence the same normalized-log convergence is almost sure under any chosen cross-dimension coupling. The source only asks for convergence in probability.

## 9. Phase retrieval

At \(N_m=2m-1+r_m\), bounded density gives full spark almost surely and \(\omega=M\). Since \(h(2)=\log4\),
\[
\boxed{
\frac1m\log\omega(A_m)\xrightarrow{\mathbb P}-\frac{\log4}{r+1}
}
\]
for fixed \(r\), and
\[
\boxed{
\frac{r_m+1}{m}\log\omega(A_m)\xrightarrow{\mathbb P}-\log4
}
\]
when \((r_m+1)\log m=o(m)\).

This is the exact source obstruction scale for stable real phase retrieval. It should not be silently identified with every possible lower Lipschitz constant outside the source deterministic setup.

## 10. Scope and counterexamples

- **Fixed law:** proved as above.
- **Arbitrary triangular array with only density bound + variance one:** not proved and should not be claimed; P12 already has a smooth rare-spike triangular-array counterexample to uniform local Gaussianity.
- **Complex iid:** open; predicted factor \(1/2\) remains to be proved.
- **Noncentered laws:** open without a shift-control theorem because \(E\langle X,u\rangle=\mu\sum u_i\) can move the small slab away from zero.
- **Expectation of normalized log:** open; probability/a.s. convergence does not imply uniform integrability of the deep negative tail.
- **Naive truncation + Weyl:** invalid at exponential singular-value scale.
- **Global \(O(\sqrt m)\) norm route:** unnecessary and generally false under finite variance.
- **One-matrix least-singular theorem alone:** insufficient; the extreme minimum still needs the exponential-family staging and pair graph.

## 11. Ledger

### PROVED

- `P12-SOURCE-01`: exact real Conjecture 8.2 and complex prediction recovered.
- `P12-NORM-EMAIL`: exact variance normalization and triangular neutrality condition.
- `P12-LD-04`: fixed-law finite-variance one-normal density local CLT.
- `P12-MAIN-03`: triangular-array real theorem under clean-row rarity.
- `P12-NORMAL-FV` **NEW/imported and verified**: Livshyts random rounding gives exponential incompressibility of one fixed iid hyperplane normal under bounded concentration + second moment.
- `P12-FRACTION-FV` **NEW**: exponential one-normal incompressibility implies an exponentially tiny bad fraction of the exponential hyperplane family, with no union bound.
- `P12-2SLAB-BD` **NEW**: arbitrary-direction two-slab product-density bound with determinant factor.
- `P12-PAIR-GEOM-FV` **NEW**: fixed-angle near-parallel low-overlap pairs are exponentially sparse under fixed finite variance, without a global norm event.
- `P12-MAIN-FV` **NEW**: fixed real centered bounded-density finite-variance law gives the full moderate-surplus exponent.
- `P12-PR-FV` **NEW**: phase-retrieval exponent \(-\log4\) in moderate-surplus normalization.
- `P12-AUDIT-P24-MIDEDGE` **NEW**: P24 finite-variance sequential anti-alignment passes independent audit.

### CANDIDATE COMPLETE / protocol-open

- `P12-MAIN-FV` and `P12-PR-FV`: mathematically complete, but require two OTHER complete audits before ProofNet24 closure.

### OPEN

1. Two independent complete audits of the new finite-variance chain.
2. Complex iid theorem and factor \(1/2\).
3. Expectation / negative-tail uniform integrability.
4. Uniform triangular-array finite-variance theorem without a Lindeberg/rarity condition.
5. Noncentered version with exact shift hypotheses.

### REJECTED

- ordinary CDF Berry--Esseen at exponentially small windows;
- naive truncation/Weyl;
- Bai--Yin/operator norm as a necessary heavy-tail route;
- a union bound over all hyperplane normals;
- pair diffuseness as a necessary condition for the two-slab upper bound;
- the full singular-edge integral as a necessary input to the original staged graph proof;
- automatic variance normalization for arbitrary exponentially varying triangular scales.

## 12. Next attack

The highest-value mathematical target is now the complex source prediction
\[
\frac1m\log M_{m,r}^{\mathbb C}\stackrel{?}{\to}-\frac{h(\gamma)}{2(r+1)}.
\]
Before declaring the real theorem closed, two OTHER workers should independently rederive:

1. the Livshyts Lemma 6.4 mapping to an iid \((m-1)\times m\) hyperplane;
2. the expected-bad-fraction argument;
3. P24 fixed-angle anti-alignment;
4. P12-2SLAB-BD;
5. the staged recursion and its two entropy balances.

## 13. Bottom line

The fixed-law real smooth-iid conjecture no longer needs subgaussianity, a fourth moment, a \(2+\delta\) moment, or clean-row rarity. For one fixed centered real iid law with positive finite variance and bounded density, after exact variance normalization,
\[
\boxed{
\frac{r_m+1}{m}\log M_{m,r_m}(A_m)\to-h(\gamma)
}
\]
whenever \((r_m+1)\log m=o(m)\), and at phase-retrieval redundancy
\[
\boxed{
\frac{r_m+1}{m}\log\omega(A_m)\to-\log4.
}
\]

The missing ingredient was not a stronger global norm theorem. It was the combination of random-rounding incompressibility for one heavy-tailed random hyperplane, fraction-level averaging over the exponential family, and finite-variance fixed-angle anti-alignment from fresh-row sequential geometry.

