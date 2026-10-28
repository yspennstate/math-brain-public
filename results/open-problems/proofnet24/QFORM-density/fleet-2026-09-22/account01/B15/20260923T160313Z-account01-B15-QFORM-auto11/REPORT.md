SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T16:03:13Z.
attacking: exact fixed-unit interval/box normal form for the universal density constant, weak-limit stability at that fixed scale, and a direct ruled-majority/minority inequality using account02/B15.

# Status

Classification: `ESSENTIAL_STEP_APPLIED / UNIVERSAL-KERNEL-NORMAL-FORM / FIXED-BOX-EXACT-TARGET / PARTNER-RULED-INEQUALITY`.

The full universal-height QFORM conjecture remains OPEN. The qualitative regularity ledger is sharper: absolute continuity is elementary far below the target hypotheses, and source-pinned B15 work gives a bounded `C_0` density for every fixed rank-`>=3` product target, but the available height bound is matrix dependent. Continuity is not used to prove the universal height statement below.


Preserved corrections: no law-uniform pointwise quadratic Fourier decay; no independence after rotating to the eigenbasis; no projection/X-ray-only shortcut for the two-sheet branch; no arbitrary-joint rank-three coarea bound; no positive conditional-projection-density-moment gate.

## 1. Qualitative absolute continuity is automatic

Let `X` have any absolutely continuous joint law on `R^n` and let `A!=0` be symmetric. Put

\[
q(x)=x^T A x,\qquad \nabla q(x)=2Ax.
\]

Then `q(X)` is absolutely continuous. Indeed, if `N subset R` has Lebesgue measure zero, coarea gives

\[
\int_{q^{-1}(N)} |\nabla q(x)|\,dx
 =\int_N \mathcal H^{n-1}(q^{-1}(t))\,dt=0.
\]

For

\[
E_k=q^{-1}(N)\cap\{|\nabla q|\ge1/k\}
\]

we therefore have `Leb(E_k)=0`. The union of the `E_k` covers `q^{-1}(N)` away from the critical set `ker A`, and `ker A` is a proper linear subspace, hence null. Thus `q^{-1}(N)` is null and the absolutely continuous input law assigns it probability zero.

So under the owner target, absolute continuity costs no quantitative constant and needs neither independence nor the cap `f_i<=1` nor rank three; only `A!=0` and an absolutely continuous joint input are needed.

## 2. Exact universal normal form for every fixed smoothing kernel

Write

\[
s(A):=s_3(A)
\]

for the third largest eigenvalue modulus. For an absolutely continuous probability law `mu=p dx`, let

\[
D_\infty(\mu):=\|p\|_{L^\infty(\mathrm{ess})}\in[0,\infty].
\]

Let `K>=0` be any fixed probability density on `R`, `K in L^1`, `int K=1`, and define

\[
K_r(x)=r^{-1}K(x/r).
\]

### Lemma 2.1 — approximate-identity recovery of essential height

For every probability density `p` and every `r_0>0`,

\[
\boxed{
\sup_{0<r\le r_0}\|K_r*p\|_\infty=\|p\|_\infty,
}
\tag{2.1}
\]

with equality in the extended reals.

The upper bound is Young's inequality. For the reverse bound, standard dilation gives `K_r*p -> p` in `L^1` as `r downarrow0`. If the left side were bounded by some `M<||p||_infinity`, choose `r_m downarrow0`; an `L^1`-convergent subsequence converges almost everywhere, forcing `p<=M` almost everywhere, a contradiction. If `||p||_infinity=infinity`, the same argument shows the left side cannot be finite.

### Theorem 2.2 — fixed-kernel exact QFORM normal form

Let

\[
C_*:=\sup_{\substack{A,X\text{ target}\\s(A)\ge1}}
 s(A)D_\infty(\mu_{X^TAX})
\]

and

\[
C_K:=\sup_{\substack{A,X\text{ target}\\s(A)\ge1}}
 s(A)\|K*\mu_{X^TAX}\|_\infty.
\]

Then, as extended real numbers,

\[
\boxed{C_*=C_K.}
\tag{2.2}
\]

Proof. `C_K<=C_*` is immediate from Young. Conversely fix one target instance, write `Q=X^TAX`, `s=s(A)`, and let `0<r<=s`. The rescaled matrix

\[
A_r=A/r
\]

is still target-valid because `s(A_r)=s/r>=1`, and `Q_r=Q/r`. If `p_r` is the density of `Q_r`, then `p_r(u)=r p(ru)`. Hence

\[
(K*p_r)(y/r)=r(K_r*p)(y).
\]

Multiplying by `s(A_r)=s/r` gives the exact scale cancellation

\[
s(A_r)(K*p_r)(y/r)=s(K_r*p)(y).
\tag{2.3}
\]

Taking the supremum over target instances on the left, then over `0<r<=s` on the right, and using (2.1), gives

\[
C_K\ge s\|p\|_\infty.
\]

Now take the supremum over the original target instance. QED.

This theorem unifies the previously useful Gaussian, Poisson and tent formulations, but importantly it needs no raw-output continuity. Qualitative absolute continuity suffices.

## 3. The exact fixed-unit box target

Choose

\[
K_\Box(u)=\frac12\mathbf1_{[-1,1]}(u).
\]

Then

\[
(K_\Box*\mu_Q)(y)=\frac12\Pr\{|Q-y|\le1\}.
\]

Therefore Theorem 2.2 yields the especially concrete identity

\[
\boxed{
C_*
=
\sup_{\rm target}\sup_{y\in\mathbb R}
\frac{s_3(A)}2\Pr\{|X^TAX-y|\le1\}.
}
\tag{3.1}
\]

Thus the full universal density problem is *exactly* one fixed-width interval inequality. No shrinking-window limit, desmoothing theorem, continuity premise or Fourier inversion is needed in the target statement.

More generally any one fixed interval width gives the same sharp constant after the corresponding spectral rescaling. The width-two form (3.1) is chosen because it interfaces directly with the partner's interval domination theorem.

## 4. Fixed-box profiles are stable under weak output limits

The latest account02/B15 report imports and checks the zero-loss weak interval trace theorem: if probability laws `mu_m=>mu` weakly and `mu` is atomless, then their Kolmogorov distance tends to zero and

\[
\sup_{a\le b}|\mu_m((a,b])-\mu((a,b])|\to0.
\]

Every nonconstant QFORM output here is atomless by Section 1. Consequently, for

\[
B_\mu(y):=\frac12\mu([y-1,y+1]),
\]

we have the quantitative fixed-scale estimate

\[
\boxed{
\sup_y|B_{\mu_m}(y)-B_\mu(y)|
\le d_K(\mu_m,\mu)\longrightarrow0.
}
\tag{4.1}
\]

This is exactly the stability needed for the normal form (3.1). It is intentionally fixed scale. The same latest partner report constructs a target-valid fixed-`I_3` sequence for which normalized *shrinking*-interval profiles do not converge, so (4.1) should not be combined with a window width tending to zero along the approximation.

A cap-preserving smooth-core reduction is therefore zero-loss at the level of (3.1): approximate each fixed finite collection of marginals in `L^1` by smooth compactly supported probability densities still bounded by one. The product laws converge in total variation, hence the output laws do as well, and their fixed-box profiles converge uniformly. Density convergence is neither needed nor generally true.

## 5. Qualitative continuity is a separate theorem, not the height mechanism

The completed account02/B15 product-transversality theorem (`20260922T150242Z-account02-B15-qform-r3`) proves:

> If the independent marginals have densities bounded by one and `rank(A)>=3`, then `Q=X^TAX` has a bounded continuous density; indeed the representative lies in `C_0(R)`.

Its finite height constant is matrix dependent. If `B=A_{J,J}` is a nonsingular physical principal block of order `d in {3,4}`, the theorem gives

\[
\|p_Q\|_\infty\le \frac{C_d}{\sigma_{\min}(B)},
\qquad
C_3=2\pi+3\sqrt3,
\quad C_4=4\pi+8.
\tag{5.1}
\]

A separate account03/B15 mechanism covers the nonzero-physical-diagonal and zero-diagonal cases and also concludes `p_Q in C_0` with matrix-dependent constants. Under the owner's three-large-eigenvalue hypothesis `rank(A)>=3`, so this qualitative continuity theorem applies to every target instance.

Hence the precise regularity ledger is:

1. **absolute continuity:** automatic for any `A!=0` under any absolutely continuous joint input;
2. **bounded density for each fixed target:** proved, but with a matrix-dependent physical-block constant;
3. **continuous density for each fixed target:** proved qualitatively (`C_0`), separately from universal height;
4. **one matrix/dimension/law-independent height constant:** still OPEN and is the substantive conjecture.

The shared `CLAIMS.json` still lists the continuity claim as open; the source-pinned B15 continuity theorems and the earlier immutable continuity correction are newer than that compact ledger. This report does not mutate the shared claim file.

## 6. Apply the completed account02/B15 ruled result to the exact fixed-box target

The latest account02/B15 source independently rechecks the completed ruled one-sheet theorem for an invertible indefinite **original-coordinate** physical triple `S`. Let

\[
B=A_{S,S},\qquad \kappa_S=\sigma_{\min}(B),
\]

and let `G_S` be the conditional majority/one-sheet event after conditioning on the outside original coordinates. Its output submeasure

\[
\mu_S^+(E):=\Pr\{Q\in E,\,G_S\}
\]

satisfies

\[
\boxed{
\mu_S^+(E)\le C_S|E|,
\qquad
C_S\le\frac{\pi\sqrt2}{\kappa_S}.
}
\tag{6.1}
\]

This allows arbitrary outside quadratic terms and cross-couplings and uses no post-rotation independence.

Apply (6.1) to the exact unit box

\[
J_y=[y-1,y+1].
\]

Then

\[
\frac{s(A)}2\Pr\{Q\in J_y,G_S\}
\le s(A)C_S,
\]

so

\[
\boxed{
\frac{s(A)}2\Pr\{|Q-y|\le1\}
\le
s(A)C_S
+\frac{s(A)}2\Pr\{|Q-y|\le1,\,G_S^c\}.
}
\tag{6.2}
\]

Using the partner constant,

\[
\boxed{
\frac{s(A)}2\Pr\{|Q-y|\le1\}
\le
\pi\sqrt2\frac{s(A)}{\kappa_S}
+\frac{s(A)}2\Pr\{|Q-y|\le1,\,G_S^c\}.
}
\tag{6.3}
\]

Thus if `kappa_S>=c s(A)`, the entire majority contribution to the **exact sharp target functional** costs at most `pi sqrt(2)/c`. The only local unpaid term is the minority/two-sheet unit-window mass.

## 7. Weighted soft-majority residual at the exact target scale

Take a finite bank `T` of such original-coordinate indefinite triples and weights `a_S>=0`. Put

\[
R(X)=\sum_{S\in\mathcal T}a_S\mathbf1_{G_S}(X),
\qquad
\beta_\delta(E)=\Pr\{Q\in E,\,R(X)<\delta\}.
\]

The pointwise inequality

\[
1\le \mathbf1_{\{R<\delta\}}+R/\delta
\]

and (6.1) give, for every interval `J`,

\[
\mu_Q(J)
\le
\beta_\delta(J)
+\frac{|J|}{\delta}\sum_S a_SC_S.
\]

For the exact width-two box and after multiplying by `s(A)/2`, this becomes

\[
\boxed{
\frac{s(A)}2\Pr\{|Q-y|\le1\}
\le
\frac{s(A)}2\beta_\delta(J_y)
+\frac{s(A)}{\delta}\sum_Sa_SC_S.
}
\tag{7.1}
\]

This is sharper conceptually than a smoothing-only reduction: by (3.1), its left side is **exactly** the global sharp-constant functional.

If we use the coarse partner bound and choose

\[
a_S=\frac{\kappa_S}{\sum_T\kappa_T},
\]

then

\[
\sum_Sa_SC_S
\le
\frac{\pi\sqrt2\,N}{\sum_S\kappa_S}.
\]

Hence an average-conditioning certificate

\[
\frac1N\sum_S\kappa_S\ge c\,s(A)
\]

implies

\[
\boxed{
\frac{s(A)}2\Pr\{|Q-y|\le1\}
\le
\frac{s(A)}2\beta_\delta(J_y)
+\frac{\pi\sqrt2}{c\delta}.
}
\tag{7.2}
\]

If the exact ruled constants `C_S` are retained, harmonic weights `a_S=C_S^{-1}/\sum_T C_T^{-1}` replace the reciprocal-minor payment by the exact mean ruled capacity.

## 8. What is now exactly unpaid

Combining the fixed-box identity (3.1) with (7.1), the central remaining implication on this B15 interface is no longer a regularity or desmoothing question. It is the structural estimate

\[
\boxed{
\sup_{\rm target}\sup_y
\frac{s_3(A)}2
\Pr\{|Q-y|\le1,\,R(X)<\delta\}<\infty
}
\tag{8.1}
\]

for a cost-efficient original-coordinate physical bank whose paid term in (7.1) is universal.

In words: after all majority/one-sheet pieces are paid, a counterexample must place a large **fixed-width** small-ball mass on points that are simultaneously minority/two-sheet for almost all cost-efficient physical triples. This is the branch that must be connected to one of the existing product-preserving ridge/volume/grouped-coordinate mechanisms. The live two-sheet X-ray correction prevents replacing (8.1) by generic projection information.

There is no remaining need, on this interface, to prove a universal continuity modulus, density convergence of source approximants, or a shrinking-window limit. Those are strictly stronger than the exact fixed-box target and the latest partner obstruction shows that source-uniform shrinking-window convergence is false even inside the fixed `A=I_3` target.

Execution context: `WITHOUT_VERIFIED_BRAIN`. Full QFORM status: `OPEN_NOT_PROVED`.
