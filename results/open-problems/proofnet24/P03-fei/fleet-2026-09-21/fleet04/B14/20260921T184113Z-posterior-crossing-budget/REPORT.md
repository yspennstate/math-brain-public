# B14 — posterior-threshold crossing budget for FEI critical cores

**Run:** `B14-20260921T184113Z-r11`, fleet04/B14  
**Live role:** FEI erasure and selector proof  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** **PARTIAL / new analytic necessary condition on every centered restriction-critical core. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Publication priority:** **UNVERIFIED.** No novelty claim is made.

## 1. Exact starting point

Fresh FEI master was recovered before this derivation. The required 21 September packet was read in the mandated order: `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md`. I also consumed the newest compatible centered-budget and B14 selector handoffs rather than restarting an older singleton route.

For a Boolean function `f`, let `X` be its spectral sample, `p_i=Pr(i in X)`, and after median-character centering put

\[
q_i=\min(p_i,1-p_i),\qquad J=\sum_iq_i.
\]

Character multiplication preserves spectral entropy and `J`; hence FEI is equivalently a universal bound `H<=C J`. Choose a physical restriction descendant `g` maximizing

\[
R={H(g)\over J(g)}
\]

and then center it by its median character. The inherited primitive-core reduction gives `p_i<=1/2` for every remaining coordinate, so now `J=I=sum_i p_i`, and for every nonempty physical restriction block `A`,

\[
\Delta_A H(g)\ge R D_A(g),\qquad
D_A(g):=J(g)-\mathbb E_zJ(g_{A=z}).
\tag{1}
\]

The inherited block restriction identity and block-JS tensorization give

\[
\Delta_AH=B_A+JS_A,\quad
B_A=H(X_A\mid X_{A^c}),\quad
JS_A\le\sum_{i\in A}\mathfrak j(p_i),
\tag{2}
\]

where

\[
\mathfrak j(p)=1-h_2\!\left({1\over2}+\sqrt{p(1-p)}\right).
\]

Consequently

\[
\Delta_AH
\le H(X_A)+\sum_{i\in A}\mathfrak j(p_i)
\le\sum_{i\in A}\Psi(p_i),
\qquad
\Psi(p):=h_2(p)+\mathfrak j(p).
\tag{3}
\]

No prescribed-coordinate upper restriction-payment statement is assumed; the known counterexamples to such statements remain untouched.

### Source/provenance note

Fresh scientific master entering the run was `03edf97be0d9e68ef87bdaa33aaad49a0d6a7332`; it advanced during the derivation and was refreshed to `e4f58c7ac32a2699fb3c50da09922a7fa77f9958` before delivery. The exact inherited B14 inputs used here include:

- fleet02/B14 centered refunded selector, report blob `8d12c2253a34b46f0cbd55cd9afb9fd092323069`;
- fleet02/B14 block-JS / critical-Han continuation, report blob `f490ce01f24431ee2a8b54d8e64cc9336c46ac6f`;
- fleet04/B14 strong-concavity selector continuation, consumed through the newer block-JS handoff;
- the fresh interactive centered-budget/primitive-core handoff on the current master.

These are mathematical dependencies, not independently re-audited claims. The proof below rederives the new implication from their stated exact identities and inequalities.

## 2. New exact identity: centered drift equals removed influence plus posterior threshold crossings

For `j notin A`, let

\[
p_j(z):=\operatorname{Inf}_j(g_{A=z})
       =\mathbb E[\eta_j\mid x_A=z],
\]

where `eta_j(x)=1{g(x) != g(x^j)}` is the `j`-pivotality indicator. Since the parent is centered, `p_j<=1/2`, and influence is a martingale under unrelated restrictions:

\[
\mathbb E_zp_j(z)=p_j.
\tag{4}
\]

Use the elementary identity

\[
\min(r,1-r)=r-(2r-1)_+.
\tag{5}
\]

Then the centered restriction drift is exactly

\[
\boxed{
D_A
= I_A + C_A,
\qquad
C_A:=\sum_{j\notin A}\mathbb E_z(2p_j(z)-1)_+,
\qquad
I_A:=\sum_{i\in A}p_i.
}
\tag{6}
\]

Thus `C_A` is not an auxiliary estimate: it is the exact extra refund beyond the influence physically removed by the block.

There is a clean statistical meaning. Before revealing `x_A`, the optimal prediction of the rare event `eta_j=1` has Bayes error `p_j`. After revealing `x_A`, its Bayes error is

\[
\mathbb E_z\min(p_j(z),1-p_j(z))
=p_j-\mathbb E_z(2p_j(z)-1)_+.
\]

So the `j` summand of `C_A` is exactly the Bayes-error reduction for predicting whether coordinate `j` is pivotal. The quantity `C_A` is the aggregate *posterior majority-crossing gain* created by revealing the block.

## 3. New theorem: every block's crossing gain is paid by the restricted coordinates' scalar slack

Define the coordinate slack at slope `R`

\[
\delta_i(R):=\Psi(p_i)-R p_i.
\tag{7}
\]

Singleton criticality and the inherited concave restriction cap imply `delta_i(R)>=0` on this core.

### Theorem 3.1 — posterior-threshold crossing budget

For every physical block `A` of the centered restriction-critical core,

\[
\boxed{
R\,C_A\le\sum_{i\in A}\delta_i(R).
}
\tag{8}
\]

### Proof

Combine the exact critical lower payment (1), the drift identity (6), and the universal block upper payment (3):

\[
R(I_A+C_A)
=R D_A
\le \Delta_AH
\le \sum_{i\in A}\Psi(p_i)
=R I_A+\sum_{i\in A}\delta_i(R).
\]

Cancel `R I_A`. QED.

This is an all-block theorem and an exact nonreuse statement: posterior flips of surviving pivotality probabilities across `1/2` cannot appear for free. Their total mass is charged to the scalar slack of the coordinates actually revealed.

It is also compatible with the known failure of every-coordinate payment. The theorem is a **necessary structural condition on one specially selected restriction-critical descendant**; it does not upper-bound `Delta_iH/Inf_i` for an arbitrary prescribed coordinate of an arbitrary Boolean function.

## 4. Endpoint and two-face consequences

Let

\[
D:=\sum_i\delta_i(R)
 =\sum_i\Psi(p_i)-RI.
\tag{9}
\]

Because `H=RI` on the centered core,

\[
\boxed{D=\operatorname{TC}(X)+\sum_i\mathfrak j(p_i),}
\tag{10}
\]

where `TC(X)=sum_i h_2(p_i)-H(X)` is total correlation.

### 4.1 Leave one coordinate unresolved

Take `A=[n]\setminus\{j\}`. After all other variables are fixed, the residual one-bit function is constant or a character, so `p_j(z)` is `0` or `1`. Therefore `C_A=p_j`, and (8) gives

\[
\boxed{
R p_j\le D-\delta_j,
\qquad\text{equivalently}\qquad
D\ge\Psi(p_j)
\quad\text{for every relevant }j.
}
\tag{11}
\]

Thus the shared dependence-plus-recombination bank must dominate every single-coordinate scalar cap.

### 4.2 Leave a pair unresolved: forced non-affine two-faces

For distinct `j,k`, put `A=[n]\setminus\{j,k\}`. On each residual two-dimensional face let `d_0,d_1` be the two `j`-edge disagreement indicators, indexed by the value of `x_k`. Then

\[
p_j(z)={d_0+d_1\over2},\qquad
(2p_j(z)-1)_+=d_0d_1.
\]

Let

\[
c_{jk}:=\Pr_z(d_0\ne d_1)
       =\operatorname{Inf}_k(\eta_j)
       =\operatorname{Inf}_j(\eta_k).
\tag{12}
\]

The equality of the last two quantities is the parity identity around a Boolean square. Equivalently, `c_jk` is the probability that the random `(j,k)` face is non-affine (has a nonzero quadratic `x_jx_k` term in its `F_2` truth-table representation).

Since

\[
\mathbb E_z d_0d_1=p_j-\frac{c_{jk}}2,
\]

and similarly for `k`,

\[
\boxed{C_A=p_j+p_k-c_{jk}.}
\tag{13}
\]

Substitution in (8) yields the new two-face rigidity inequality

\[
\boxed{
R\,(p_j+p_k-c_{jk})
\le D-\delta_j-\delta_k,
}
\tag{14}
\]

or, after cancellation,

\[
\boxed{
R\,c_{jk}\ge \Psi(p_j)+\Psi(p_k)-D.
}
\tag{15}
\]

Hence whenever the global scalar slack `D` is smaller than the two local scalar caps, Booleanity forces a quantitative density of genuinely non-affine `(j,k)` faces. This is a bridge from the erasure/selector ledger to an actual mixed-derivative Boolean constraint, rather than another scalar spectral relaxation.

The elementary upper bound `c_jk<=2 min(p_j,p_k)` further gives the necessary profile constraint

\[
\boxed{
D\ge \Psi(p_j)+\Psi(p_k)-2R\min(p_j,p_k)
\quad\text{for every pair }j\ne k.
}
\tag{16}
\]

This may be useful precisely in the rare-marginal regime where `Psi(p)/p` carries a logarithmic cost.

## 5. A second information-theoretic reading

Let

\[
c_j(A):=\mathbb E_z(2p_j(z)-1)_+.
\]

The Bayes error for predicting `eta_j` from `x_A` is `p_j-c_j(A)`. Binary Fano therefore gives

\[
\boxed{
I(\eta_j;x_A)
\ge h_2(p_j)-h_2(p_j-c_j(A)).
}
\tag{17}
\]

Thus any block that spends much of its permitted crossing budget also carries a quantitatively forced amount of information about surviving pivotality. Equation (8) controls the sum of the *Bayes-error improvements* by a nonreused FEI slack; (17) converts each improvement into a genuine input-side information cost. I do not have a universal summation theorem for these information costs yet, so this is a next bridge, not FEI closure.

## 6. Decisive finite regression check

`verify_crossing_budget.py` exhaustively enumerates Boolean functions through dimension four modulo global output sign, median-centers them, keeps exactly those whose `H/J` ratio is maximal over every noncharacter physical restriction descendant, and tests:

1. (8) for every nonempty block;
2. the exact pair identity (13);
3. the pair rigidity inequality (15).

The exact checker SHA-256 is `e5401b3c3cfe4e7dee38bbc31a57ebe1170898831de637264d0d42fb3d5e5c72` and the exact captured stdout SHA-256 is `a8ca2830dd565e7dcc16b1002d1b47aab8c92b1ca66eef86349d8010e349474d`. The process exited `0`; the runtime also emitted an unrelated spreadsheet-warmup warning on stderr, which is not mathematical output and whose machine path is intentionally not persisted. It finds `4`, `88`, and `1312` sign-normalized noncharacter critical cores in dimensions `2`, `3`, and `4`, respectively. The maximum recorded violation of the all-block budget is `0.0`; maximum pair-identity error is `0.0`; maximum pair-budget violation is `0.0` in double arithmetic. This computation is only a regression check for the written analytic proof and is not used to infer a higher-dimensional theorem.

## 7. What failed / what remains

The theorem does **not** close FEI. In the high-ratio critical regime the inherited marginal cap already puts every `p_i` below about `0.174`, so a *single* restriction cannot create the centered refund; block restrictions are where majority crossings can first accumulate. Equation (8) identifies exactly how much such multistep accumulation is allowed.

A route that only studies scalar marginals remains insufficient: the fresh dyadic relaxation counterfamily passes a large collection of scalar/cylinder/parity/profile tests with unbounded entropy per mean size but cannot be signed into a Boolean spectrum. The new pair corollary (15) deliberately moves to genuine Boolean mixed-face geometry.

**Next target.** Combine the hierarchy (8) over adaptively chosen blocks with (17) or with the two-face quantities `c_jk`. A promising dichotomy is:

- if crossing gains accumulate, (8) forces substantial scalar slack to be spent and the restriction tree should telescope it;
- if crossing gains stay small, surviving pivotality posteriors remain below `1/2`, so seek a direct erasure selector from the resulting near-affine two-face geometry.

The missing statement is a summable theorem linking the mixed-face/information costs to `J`; no such theorem is claimed here.
