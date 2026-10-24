SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-23T10:53:14Z.
attacking: weak-limit/trace closure for universal density estimates, and a zero-loss generic-matrix reduction with continuity kept separate.

# QFORM account03/B15 auto16 — weak-limit density-height closure and generic-matrix normal form

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Worker:** account03/B15  
**Run:** `20260923T105314Z-account03-B15-qform-auto16`  
**Status:** `ESSENTIAL_STEP_APPLIED / WEAK-LIMIT-HEIGHT-CLOSURE / GENERIC-MATRIX-REDUCTION / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The unrestricted universal QFORM density bound remains **OPEN**. This run proves a precise no-moment trace/limit principle for density height and uses it to remove exact algebraic degeneracies from the proof target at zero constant loss. It does **not** remove near-degenerate quantitative regimes: any proof on generic matrices must remain uniform as minors, pivots or eigenvalue gaps approach zero.

## 1. Sources and exact dependencies

Fresh owner control was resolved from `yspennstate/math-research-brain` main at commit `3bdcacf42e9612c7fd6d1fc720e70fa2784a763c`; OWNER CONTROL revision remained `2026-09-22.15`, QFORM-only, with no account03/B15 pause. The current B15 delivery obligation is to supply a precise rough-law limit or trace justification used by a new density estimate, with continuity kept separate from the central height problem.

The assigned completed partner result actually applied below is account04/B15:

- `yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T211430Z-account04-B15-heat-regularity-r4/REPORT.md`.

Its exact theorem is: for every probability law `mu` on `R`, if `gamma_eps` is the centered Gaussian density of scale `eps`, then

\[
\mathfrak h(\mu):=\sup_{\varepsilon>0,y}(\mu*\gamma_\varepsilon)(y)
\]

equals the essential `L^infinity` density height when a bounded density exists, and equals `+infinity` otherwise.

The newest owner-required mathematical source actually applied is the volume-stability theorem

- `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`;
- `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

At its exact scope, if an original-coordinate cross block has `M=M0+E`, `s3(M0)>=a`, range leverage at most `1/2`, and `||E||op<=a/16`, then the full ambient quadratic-plus-affine output has a continuous density bounded by

\[
C_{\rm vol}(a)=\frac{24\sqrt3\,e}{5a}<\frac{23}{a}.
\]

All current source corrections are retained: no law-uniform pointwise quadratic phase decay, no post-rotation independence, no arbitrary-joint coarea theorem, no worst-fiber-sup replacement, no assumption of one uniformly conditioned physical minor, and no use of small matrix norm as a law-uniformly small random quadratic perturbation.

## 2. Main regularity lemma: density height is weakly lower semicontinuous

### Theorem 2.1 — weak-limit height closure

Let `mu_m` and `mu` be Borel probability measures on `R` with

\[
\mu_m\Rightarrow\mu
\]

weakly. Then, with `+infinity` allowed,

\[
\boxed{
\mathfrak h(\mu)\le \liminf_{m\to\infty}\mathfrak h(\mu_m).
}
\tag{2.1}
\]

Equivalently: if every `mu_m` has a density bounded by the same constant `C`, then `mu` also has a density bounded by `C`. No absolute continuity of `mu` is assumed in advance.

### Proof

Fix `eps>0` and `y in R`. The function

\[
z\mapsto\gamma_\varepsilon(z-y)
\]

is bounded and continuous. Weak convergence therefore gives

\[
(\mu*\gamma_\varepsilon)(y)
=
\lim_m(\mu_m*\gamma_\varepsilon)(y)
\le
\liminf_m\mathfrak h(\mu_m).
\]

Take the supremum over `eps,y` and apply the completed account04/B15 heat-height theorem:

\[
\mathfrak h(\mu)
=
\sup_{\varepsilon,y}(\mu*\gamma_\varepsilon)(y)
\le
\liminf_m\mathfrak h(\mu_m).
\]

This proves (2.1). QED.

The partner result is therefore used at the actual target inequality

\[
\boxed{
\|p_\mu\|_\infty
\le
\liminf_m\|p_{\mu_m}\|_\infty,
}
\tag{2.2}
\]

with the convention that either side may be infinite. This is not merely a qualitative citation.

## 3. Varying quadratic coefficients need no moments

The source state correctly warns that a small matrix error is **not** a law-uniformly small random quadratic error when supports are arbitrary and unbounded. Nevertheless, coefficient limits are perfectly safe for each fixed law, because only weak convergence is needed.

### Lemma 3.1 — varying-map pushforward

Let `nu_m=>nu` weakly on `R^n`, and let `q_m,q:R^n->R` be continuous functions such that `q_m->q` uniformly on every compact set. Then

\[
(q_m)_\#\nu_m\Rightarrow q_\#\nu.
\tag{3.1}
\]

### Proof

Let `phi` be bounded continuous on `R`. Weak convergence makes `{nu_m}` tight. Given `eta>0`, choose a compact `K` such that `nu(K)>=1-eta` and, after enlarging `K` slightly if necessary, `nu_m(K)>=1-2eta` for all large `m`. On `K`, `q_m->q` uniformly. The sets `q_m(K)` eventually lie in a fixed compact interval, on which `phi` is uniformly continuous. Hence

\[
\sup_{x\in K}|\phi(q_m(x))-\phi(q(x))|\to0.
\]

Outside `K` the integral difference is at most `4||phi||infinity eta`. Thus

\[
\int\phi(q_m)d\nu_m-\int\phi(q)d\nu_m\to0.
\]

Also `phi o q` is bounded continuous, so `int phi(q)dnu_m -> int phi(q)dnu`. This proves (3.1). QED.

### Corollary 3.2 — quadratic-affine coefficient closure

Let `X` be any random vector in `R^n`, finite almost surely; no moment is assumed. If

\[
A_m\to A,\qquad b_m\to b,\qquad c_m\to c,
\]

then

\[
Q_m=X^TA_mX+b_m^TX+c_m\to X^TAX+b^TX+c=:Q
\]

almost surely, and therefore

\[
\boxed{
\mathfrak h(\mathcal L(Q))
\le
\liminf_m\mathfrak h(\mathcal L(Q_m)).
}
\tag{3.2}
\]

In particular, any density estimate whose constant remains bounded along a nondegenerate coefficient approximation passes to the degenerate endpoint with **zero constant loss**.

This is one-way. An estimate at an exact null endpoint does not imply a uniform estimate for nearby nonzero coefficients.

## 4. The cap-one product class is weakly closed

### Lemma 4.1

Suppose probability measures `mu_m=f_m dx` on `R` satisfy `0<=f_m<=1` and `mu_m=>mu`. Then `mu=f dx` for some `0<=f<=1`.

### Proof

For every open set `G`, Portmanteau gives

\[
\mu(G)\le\liminf_m\mu_m(G)\le |G|.
\]

By outer regularity, `mu(E)<=|E|` for every Borel `E`, hence `mu<=dx` and the Radon--Nikodym density is at most one. QED.

For fixed finite `n`, if every marginal `mu_{i,m}=>mu_i`, then the product measures converge:

\[
\bigotimes_i\mu_{i,m}\Rightarrow\bigotimes_i\mu_i.
\]

Thus Theorem 2.1 and Lemma 3.1 apply simultaneously to weak limits of cap-one product laws and coefficient limits. This gives a genuine rough-law/trace closure theorem without truncation, moments or continuity assumptions.

## 5. Exact zero-loss generic-matrix normal form

The preceding closure has a useful structural consequence.

Fix `n`. Let `P_1,...,P_N` be any finite family of nonzero real polynomials in the entries of a symmetric `n x n` matrix. Let

\[
\mathcal G_n=\{A=A^T: P_j(A)\ne0\ \text{for all }j\}.
\]

Because each zero set is a proper algebraic hypersurface (or lower-dimensional algebraic set), `G_n` is dense in the vector space of real symmetric matrices.

For a rank-at-least-three matrix write `s=s_3(A)>0` and define the scaled height

\[
\mathcal C(A;X)=s_3(A)\,\mathfrak h(\mathcal L(X^TAX)).
\]

Let `C_full` be the supremum of this quantity over all finite dimensions, all rank-at-least-three symmetric matrices, and all cap-one independent product laws. Let `C_G` be the same supremum restricted, in each dimension, to `A in G_n`.

### Theorem 5.1 — algebraically generic matrices suffice exactly

\[
\boxed{C_{\rm full}=C_{\mathcal G}.}
\tag{5.1}
\]

### Proof

The inequality `C_G<=C_full` is immediate. For the reverse inequality, fix a rank-at-least-three symmetric `A`, put `s=s_3(A)>0`, and fix a cap-one product source `X`.

Choose `eta_m downarrow0`. Since `G_n` is dense, choose symmetric perturbations `E_m` with

\[
\|E_m\|_{op}<\eta_m s
\]

such that

\[
A_m=(1+2\eta_m)A+E_m\in\mathcal G_n.
\]

Then `A_m->A`. Weyl's singular-value inequality gives

\[
s_3(A_m)
\ge(1+2\eta_m)s-\|E_m\|_{op}
>(1+\eta_m)s,
\]

while continuity of singular values gives `s_3(A_m)->s`.

By (3.2),

\[
\mathfrak h(Q_A)\le\liminf_m\mathfrak h(Q_{A_m}).
\]

If `C_G<infinity`, then

\[
\mathfrak h(Q_{A_m})\le \frac{C_G}{s_3(A_m)}.
\]

Hence

\[
\mathfrak h(Q_A)
\le \frac{C_G}{s},
\qquad
s\,\mathfrak h(Q_A)\le C_G.
\]

The same statement is tautological if `C_G=+infinity`. Taking the supremum over `A,X` proves `C_full<=C_G`. QED.

### Concrete genericities that may be imposed without loss

For the purpose of proving the universal constant, one may therefore impose any **finite collection** of algebraic nondegeneracy conditions, for example:

- `det A !=0` (invertible full matrix);
- simple spectrum (nonzero discriminant);
- every physical diagonal `A_ii !=0`;
- every specified physical `2x2`, `3x3`, or other finite list of minors nonzero;
- all matrix entries nonzero;
- simultaneous avoidance of any finite collection of polynomial pivot coincidences.

The sharp universal constant is unchanged.

This does **not** permit quantitative lower bounds such as `|det B|>=c` or `|A_ii|>=c`. The approximants may have arbitrarily tiny nonzero pivots/minors. Thus the theorem removes exact algebraic endpoint bookkeeping, not the near-null/high-leverage difficulty.

A particularly useful corollary is:

> It is enough to prove QFORM uniformly for invertible, simple-spectrum target matrices with no exact zero physical pivots/minors, provided the proof constant stays universal as those quantities approach zero.

Repeated eigenvalues and exact zero pivots therefore need not be treated as separate endpoint theorems in a future uniform proof.

## 6. Actual application to the newest volume-stability theorem

Let `V_a` be the set of original-coordinate cross blocks covered by the newest volume-stability theorem at scale `a`, i.e. blocks admitting a decomposition

\[
M=M_0+E,
\quad s_3(M_0)\ge a,
\quad \max_i(P_{\mathrm{range}(M_0)})_{ii}\le1/2,
\quad \|E\|_{op}\le a/16.
\]

The theorem at commit `c2414ef6...` gives, for every such cross block and arbitrary fixed remaining quadratic/affine coefficients,

\[
\mathfrak h(Q_M)
\le
\frac{24\sqrt3 e}{5a}.
\tag{6.1}
\]

Now suppose `M_m in V_a` and `M_m->M` in operator norm. Keep the same cap-one product source and the same remaining coefficients, changing only the corresponding symmetric cross block. Then `Q_{M_m}->Q_M` almost surely for that fixed law, so Theorem 2.1/Corollary 3.2 gives

\[
\boxed{
\mathfrak h(Q_M)
\le
\liminf_m\mathfrak h(Q_{M_m})
\le
\frac{24\sqrt3 e}{5a}<\frac{23}{a}.
}
\tag{6.2}
\]

Therefore the completed newest-Claude volume theorem automatically extends, with no loss, to the **operator-norm closure** of its certified cross-block class. This can include coefficient-degenerate boundary points for which a preferred decomposition or range projection ceases to be stable as a literal certificate.

What this does **not** show is that every N3/high-leverage survivor belongs to such a closure with one fixed `a>0`; that remains a genuine structural problem.

## 7. Why small matrix norm is still not a uniform random perturbation

The limit theorem above must not be misread as a law-uniform perturbative inequality. Let the base target be `A=I_3`, let

\[
E_\delta=\delta\,\mathrm{diag}(1,0,0),
\qquad \|E_\delta\|_{op}=\delta,
\]

and choose the admissible cap-one first marginal uniform on `[delta^{-1},delta^{-1}+1]`. Then almost surely

\[
X^TE_\delta X=\delta X_1^2\ge \delta^{-1}.
\]

Thus `||E_delta||op->0` while the induced random quadratic perturbation is not even tight uniformly over the permitted product laws. This is exactly why (3.2) is a **fixed-law sequential closure theorem**, not permission to treat small operator-norm tails as uniformly small random errors.

## 8. Continuity is not inherited from the same closure argument

The central `L^infinity` height and the stronger continuous-representative assertion are genuinely different at the level of limit theory.

Let

\[
p_m=\mathbf 1_{[0,1]}*\gamma_{1/m}.
\]

Then each `p_m` is a `C^infinity cap C_0` probability density and

\[
0\le p_m\le1.
\]

Moreover `p_m->1_[0,1]` in `L^1`, hence the corresponding laws converge in total variation. The limit has density bounded by one, exactly as Theorem 2.1 predicts, but it has **no continuous representative**: any continuous function equal to one almost everywhere on `(0,1)` and zero almost everywhere outside `[0,1]` would have incompatible one-sided limits at `0` and `1`.

Therefore:

- uniform bounded density passes to weak/TV limits;
- continuity does not pass without an additional target-specific regularity input.

For QFORM, any fixed-instance `C_0` theorem must therefore be justified by the quadratic/product geometry itself; it cannot be obtained merely by smoothing rough inputs, proving continuous approximant densities, and passing to the limit.

## 9. Consequence for proof assembly

The new proof-map simplification is precise:

1. **Exact algebraic degeneracies can be removed from the universal proof target at zero loss.** Work on a dense generic set if that helps the derivation.
2. **Near-degenerate scales remain essential.** Constants must stay bounded as generic pivots/minors/eigenvalue gaps tend to zero; reciprocal-minor blowup is not repaired by the closure theorem.
3. **Uniformly bounded supporting estimates pass to coefficient and rough-law limits.** This is the rigorous endpoint/trace justification required by the B15 assignment.
4. **Continuity remains separate.** Weak-limit closure proves only the central `L^infinity` statement.

A useful next consumer is a proof-assembly or hub/near-null worker: it may freely formulate the remaining quantitative theorem on invertible, simple-spectrum, algebraically generic matrices, provided every bound is uniform up to the excluded algebraic boundary. If such a generic theorem is obtained, Theorem 5.1 closes the exact endpoints automatically.

## 10. Integrity ledger

- Full unrestricted QFORM universal constant: **OPEN / NOT PROVED**.
- New result: weak lower semicontinuity of the optimal density height under arbitrary weak output limits.
- New target-level reduction: exact zero-loss restriction to any finite algebraically generic dense matrix class.
- New application: volume-stability bound extends to the operator-norm closure of its certified class with the same `<23/a` constant.
- Assigned partner account04/B15 heat-height theorem was applied at the actual inequality (2.2), not merely cited.
- No pointwise van-der-Corput estimate, post-rotation independence, arbitrary-joint coarea bound, moment assumption, compact-support assumption, or law-uniform small-matrix perturbation was used.
- Continuity was kept logically separate and an explicit smooth-to-discontinuous limit shows why the height closure alone cannot prove it.
- Repository use is not native mathematical-memory ingestion; execution status remains `WITHOUT_VERIFIED_BRAIN`.
