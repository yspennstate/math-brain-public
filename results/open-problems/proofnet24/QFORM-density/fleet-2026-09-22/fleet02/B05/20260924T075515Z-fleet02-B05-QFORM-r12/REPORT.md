SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B05, 2026-09-24T07:55:15Z.
attacking: QFORM-WITT-DISJOINT-PLUCKER-CROSSING-v1 — convert the uniform small transverse-row gate into a source-disjoint aggregate pair/triple Pluecker crossing volume, then spend the fresh physical-cross receiver before any individual-minor reciprocal inversion.

# fleet02/B05 r12 — disjoint 2/3-Pluecker crossing compiler for the heavy-null Witt packet

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** quadratic coarea bound / complementary constructions and source-valid counterexamples  
**Status:** `PROVED SUPPORTING STRUCTURAL/ANALYTIC THEOREM`; full unrestricted QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Regularity:** the nonzero-crossing branch below inherits a bounded continuous density from the exact-cross Fourier receiver; full-target continuity remains separate/open.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The live corrections remain binding. Nothing below uses the false arbitrary-joint three-dimensional coarea estimate, post-rotation probabilistic independence, an unrestricted curved-fiber supremum, law-uniform pointwise quadratic-phase decay, positive moments of worst conditional projection caps, bounded support, moments, log-concavity, or deletion of a small nonzero random tail.

## 1. Exact live packet and inputs actually used

The heavy-null exact-rank-three Witt packet is

\[
Q=2aV(H+\kappa U)+\alpha V^2+2\gamma VW+\delta W^2,                 \tag{1.1}
\]

where `H` is one literal original coordinate, independent of the residual original-coordinate product bank, and

\[
U=u\cdot X,\qquad V=v\cdot X,\qquad W=w\cdot X                     \tag{1.2}
\]

with `u,v,w` orthonormal coefficient vectors on that residual bank. Put

\[
S_i:=a^2|\delta|.                                                       \tag{1.3}
\]

In the target-normalized heavy-null survivor,

\[
\boxed{S_i\ge\frac12.}                                                \tag{1.4}
\]

The previous fleet02/B05 pair-star exit, obtained by applying the completed pair-anchored determinant-star receiver, permits every still-unpaid descendant to assume the uniform transverse-row gate

\[
\boxed{r_i:=v_i^2+w_i^2<\frac1{64}\quad\text{for every residual original coordinate }i.} \tag{1.5}
\]

The fresh compatible partner fleet03/B05 result is r42, `QFORM-WITT-RANKTWO-BANK-NULLHUB-v1`, canonical report `yspennstate/math-open-problems@2a89e0bc63f9559b9cde159e03daafdf79e2cca4`. For an exact original-coordinate cut with both three-frame bank volumes zero, it produces the product-preserving currency

\[
\Gamma=\tau p_{12}^2+(1-\tau)p_{23}^2                               \tag{1.6}
\]

and proves

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le 2C_{NH}(S_i\Gamma)^{-1/3},
\qquad C_{NH}=7.761982175235\ldots .
}                                                                    \tag{1.7}
\]

Thus, in particular, `S_i>=1/2` and `Gamma>=1/16` imply

\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}<49.286.}                       \tag{1.8}
\]

This directly removes the quantitative exact-rank-two-bank branch from the present survivor, uniformly in `kappa`. Its exact unpaid orientation is the pure-`13` shared-middle configuration `Gamma=0` (and the rank-one-bank boundary analogues).

I also use r41's exact physical-cross identity and receiver. For any residual original-coordinate partition `J sqcup K`, define

\[
E_J:=\det\operatorname{Gram}(v_J,w_J),\qquad
D_J:=\det\operatorname{Gram}(u_J,v_J,w_J),                           \tag{1.9}
\]

and similarly `E_K,D_K`. For the physical cut `{H} union J` versus `K`, r41 proves that whenever the crossing has rank three, the product of its three nonzero singular values is exactly

\[
\Delta_{H\cup J,K}
=S_i|\kappa|\sqrt{D_K(E_J+\kappa^2D_J)},                             \tag{1.10}
\]

and the completed exact-cross theorem gives

\[
\boxed{\|p_Q\|_\infty\le6\,\Delta^{-1/3}.}                         \tag{1.11}
\]

The point of the theorem below is to force a quantitative product `E_J D_K` by **aggregate source-disjoint Pluecker mass**, without selecting any individual pair or triple minor.

## 2. Two Pluecker probability measures and their exact marginals

For every residual two-set `A={i,j}`, put

\[
p_A:=(v_iw_j-v_jw_i)^2.                                             \tag{2.1}
\]

Because `v,w` are orthonormal, Cauchy-Binet gives

\[
\boxed{\sum_{|A|=2}p_A=1.}                                          \tag{2.2}
\]

For every residual three-set `B={i,j,k}`, put

\[
q_B:=\det[(u,v,w)_B]^2.                                              \tag{2.3}
\]

Since `[u\ v\ w]` has orthonormal columns,

\[
\boxed{\sum_{|B|=3}q_B=1.}                                          \tag{2.4}
\]

Thus `p` and `q` are probability laws on physical pairs and physical triples. Their coordinate-inclusion marginals are exact:

\[
\boxed{\sum_{A\ni i}p_A=v_i^2+w_i^2=r_i,}                           \tag{2.5}
\]

because

\[
\sum_j(v_iw_j-v_jw_i)^2
=v_i^2\|w\|^2+w_i^2\|v\|^2-2v_iw_i\langle v,w\rangle
=v_i^2+w_i^2,                                                        \tag{2.6}
\]

and

\[
\boxed{\sum_{B\ni i}q_B=u_i^2+v_i^2+w_i^2=:t_i.}                   \tag{2.7}
\]

Equation (2.7) is the standard Cauchy-Binet/leverage identity for a three-column orthonormal frame.

## 3. Main combinatorial theorem — the pair and triple can be made source-disjoint

### Theorem `QFORM-WITT-DISJOINT-PLUCKER-CROSSING-v1`

Let `u,v,w` be orthonormal and assume

\[
\rho:=\max_i(v_i^2+w_i^2)<\frac13.                                  \tag{3.1}
\]

Then there is a partition `J sqcup K` of the ORIGINAL residual coordinates such that

\[
\boxed{
E_JD_K\ge\frac{1-3\rho}{32}.
}                                                                    \tag{3.2}
\]

For the live gate `rho<=1/64`,

\[
\boxed{E_JD_K\ge\frac{61}{2048}.}                                  \tag{3.3}
\]

#### Proof

Draw independently a random pair `A` with law `p` and a random triple `B` with law `q`. By the union bound and the exact marginals (2.5),(2.7),

\[
\begin{aligned}
\Pr(A\cap B\ne\varnothing)
&\le\sum_i\Pr(i\in A)\Pr(i\in B)\\
&=\sum_i r_it_i\\
&=\sum_i r_i u_i^2+\sum_i r_i^2.                                    \tag{3.4}
\end{aligned}
\]

Now `sum_i u_i^2=1`, `sum_i r_i=2`, and `r_i<=rho`, so

\[
\sum_i r_i u_i^2\le\rho,
\qquad
\sum_i r_i^2\le2\rho.                                               \tag{3.5}
\]

Hence the total **source-disjoint** pair/triple Pluecker mass

\[
\Omega:=\sum_{A\cap B=\varnothing}p_Aq_B                            \tag{3.6}
\]

satisfies

\[
\boxed{\Omega\ge1-3\rho.}                                          \tag{3.7}
\]

Next choose a random partition `J sqcup K` by assigning each residual original coordinate independently to `J` or `K` with probability `1/2`. Cauchy-Binet gives

\[
E_J=\sum_{A\subset J}p_A,
\qquad
D_K=\sum_{B\subset K}q_B.                                           \tag{3.8}
\]

Therefore

\[
\mathbb E(E_JD_K)
=\sum_{A,B}p_Aq_B\Pr(A\subset J,\,B\subset K).                      \tag{3.9}
\]

If `A cap B` is nonempty, the probability in (3.9) is zero. If `A` and `B` are disjoint, their five distinct coordinates have prescribed bank labels, so the probability is `2^{-5}=1/32`. Thus

\[
\boxed{
\mathbb E(E_JD_K)=\frac{\Omega}{32}\ge\frac{1-3\rho}{32}.
}                                                                    \tag{3.10}
\]

Some deterministic original-coordinate partition attains at least the mean, proving (3.2). With `rho<=1/64`, `1-3rho>=61/64`, giving (3.3). QED.

This is exactly the aggregation required by the correction ledger: no individual minor is inverted, no dimension-dependent maximum is selected, and the pair and triple Pluecker resources are made source-disjoint **before** the analytic receiver is invoked.

## 4. Spend the aggregate crossing on the actual Witt density

For the partition supplied by Theorem 3, `E_JD_K>0`. Hence, for every `kappa != 0`, r41's rank criterion is automatically satisfied and (1.10) gives

\[
\begin{aligned}
\Delta_{H\cup J,K}
&=S_i|\kappa|\sqrt{D_K(E_J+\kappa^2D_J)}\\
&\ge S_i|\kappa|\sqrt{E_JD_K}.                                      \tag{4.1}
\end{aligned}
\]

Under the live target normalization `S_i>=1/2` and `rho<=1/64`,

\[
\boxed{
\Delta_{H\cup J,K}
\ge\frac{|\kappa|}{2}\sqrt{\frac{61}{2048}}.
}                                                                    \tag{4.2}
\]

Insert this into the exact-cross receiver (1.11):

\[
\boxed{
\|p_Q\|_\infty
\le 6\left[2\sqrt{\frac{2048}{61}}\right]^{1/3}|\kappa|^{-1/3}
<13.578\,|\kappa|^{-1/3}.
}                                                                    \tag{4.3}
\]

The density is continuous in this paid branch because the physical crossing theorem obtains an integrable characteristic-function bound.

In particular,

\[
|\kappa|\ge\frac1{64}
\quad\Longrightarrow\quad
\boxed{\|p_Q\|_\infty<54.312.}                                     \tag{4.4}
\]

This closes the entire moderate/large shared-shear chamber under the already-forced small transverse-row gate, irrespective of how the longitudinal coefficients are spread across the same original sources.

## 5. Exact localization of the new survivor

In the heavy-null normalization used in the predecessor B05 chain,

\[
\kappa^2=\frac{1-c}{c},                                              \tag{5.1}
\]

where `c>1/2` is the spectral leverage of the literal null hub. Therefore any packet surviving (4.4) must satisfy

\[
|\kappa|<\frac1{64}
\quad\Longrightarrow\quad
\boxed{c>\frac{4096}{4097}.}                                        \tag{5.2}
\]

Thus the remaining punctured obstruction is an extremely near-coloop heavy-null geometry. The exact coloop `c=1` was already paid by the rough independent-hub/transverse-square theorem; (4.3) pays every fixed nonzero `kappa`; what is genuinely missing is a bound **uniform as `kappa -> 0`** without treating `kappa U` as a small random error.

The fresh partner r42 result removes an important exact endpoint inside that puncture: whenever an exact two-bank cut has `D_J=D_K=0` but `Gamma>=1/16`, equation (1.8) gives `<49.286` uniformly in `kappa`. Its pure-`13` orientation `Gamma=0` is therefore the correct exact rank-two-bank stress configuration, rather than generic bank-rank collapse.

Combining all exits, an unpaid heavy-null Witt descendant can now be required to satisfy simultaneously:

- `v_i^2+w_i^2<1/64` for every residual original coordinate;
- `|kappa|<1/64`, hence `c>4096/4097`;
- no available exact rank-two-bank cut with `Gamma>=1/16` (otherwise r42 pays it);
- if the signature is indefinite, only the convex/two-sheet level side remains after the ruled theorem below.

This is a structural localization, not a full proof.

## 6. Required pinned `e5f71d79...` result applied to the actual geometric obstruction

The pinned `COUNTEREXAMPLE_SEARCH.md` proves Theorem C: for a normalized exact rank-three `(2,1)` form, the one-sheet side has

\[
\boxed{p_Q(s)\le\pi\sqrt2}                                          \tag{6.1}
\]

by a genuine ruling parametrization and line integrals of the projected product density. It explicitly identifies the convex two-sheet side as the open geometric side.

The Witt latent matrix is indefinite: in the orthonormal full-frame representation its `2x2` principal block involving the hub direction and `V` has determinant

\[
-a^2(1+\kappa^2)<0.                                                   \tag{6.2}
\]

Thus its signature is `(2,1)` or `(1,2)`; after an overall sign reversal if necessary, Theorem C applies to the one-sheet half of the exact rank-three level geometry. Consequently the punctured survivor isolated in Section 5 does **not** require re-proving the ruled side. The first unpaid geometric implication is on the complementary convex/two-sheet side, exactly as required by the B05 assignment.

This is a real use of the pinned theorem: it removes one full sign/level branch from the new near-coloop survivor rather than serving only as background citation.

## 7. What was not proved and the next implication

The estimate (4.3) deliberately deteriorates as `|kappa|^{-1/3}`. That deterioration cannot be repaired by declaring `kappa U` a small perturbation: the inputs may have arbitrary unbounded and fragmented support. Nor can one pass to a bounded joint density of `(U,V,W)` and invoke three-dimensional coarea; that interface is explicitly false in the live correction ledger.

The first unpaid implication is therefore

`QFORM-WITT-NEARCOLOOP-PURE13-TWOSHEET-v1`:

> In the exact heavy-null Witt packet (1.1), under the forced row gate `v_i^2+w_i^2<1/64`, prove a rough-input interval bound uniform for `|kappa|<1/64` on the convex/two-sheet side, with particular attention to r42's pure-`13` shared-middle orientation. The proof must retain the two original product-bank geometries jointly until after the split longitudinal variable is integrated; it may not condition on the projected middle coordinate, take a curved-fiber supremum, or replace the product projection by an arbitrary bounded joint law.

A useful target currency is a **combined** receiver that stays positive both at the exact r42 rank-two-bank endpoint (through `Gamma`) and away from it (through aggregate `E_JD_K`) before any reciprocal operation. The present theorem supplies the second term quantitatively; r42 supplies the exact first term. The unresolved step is a dependence-safe interpolation between them.

## 8. Source and scope record

Sources consumed in this run include fresh owner-controlled QFORM state, the live correction ledger, the pinned `e5f71d79eff325201dd0274053d20268ce65b837` `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`, fleet03/B05 r41 exact crossing, and the newest compatible fleet03/B05 r42 exact rank-two-bank null-hub theorem. No historical refuted premise is used positively.

Full unrestricted QFORM remains **OPEN**. No target-valid counterexample is produced. Essential boundedness and continuity are kept separate.
