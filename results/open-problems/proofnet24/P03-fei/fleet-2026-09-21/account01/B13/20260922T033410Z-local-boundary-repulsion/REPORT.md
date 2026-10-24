# B13 — local restriction-margin boundary repulsion for the live FEI gate candidate

**Classification:** `ESSENTIAL_STEP_APPLIED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact live candidate and source-bound peer input

The active all-gate target is
\[
D_\Gamma(G;p):=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u),
\tag{0.1}
\]
for every Boolean gate and every interior product bias. The gate-reformulation report proves that one finite symmetric nonnegative potential satisfying (0.1) universally implies full FEI.

The fixed candidate currently under attack is
\[
\Gamma_*(p)=\Gamma_{\rm RO}(p)+a_*p(1-p),
\qquad a_*=0.2682048,
\qquad \Gamma_*(1/2)=C_*=6.5218512.
\tag{0.2}
\]
The newest compatible other-account result used substantively here is account04/B17,

`proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`,

whose canonical creation commit is `b6897a3675bb78bb3c262bc73f64ffb1e9c20301`. It proves, for a pivot of bias `t`, restrictions `G_0,G_1`, output biases `r_0,r_1`, disagreement probability `delta`, and exact information credit `C_j>=0`,
\[
D_{\Gamma}(G)=(1-t)D_\Gamma(G_0)+tD_\Gamma(G_1)+\mathcal R_{\Gamma,j}+\mathcal C_j,
\tag{0.3}
\]
and for the quadratic lift the exact local currency
\[
\mathcal W_j=t(1-t)\bigl(\delta-(r_1-r_0)^2\bigr)\ge0.
\tag{0.4}
\]
Moreover the global requested scalar correction is a nonnegative weighted average of the positive-currency local margins
\[
c_j^{\rm loc}=-{\mathcal R_{\Gamma_{\rm RO},j}+\mathcal C_j\over \mathcal W_j}.
\tag{0.5}
\]
Thus any violation of the live scalar lift `a_*` must contain a physical restriction node with `c_j^{loc}>a_*`. The purpose of this report is to characterize where such a node can occur.

I also use the source read-once certificate. Its base fixed-point potential has
\[
C_0:=\Gamma_{\rm RO}(1/2)=6.4548,
\tag{0.6}
\]
obeys the dyadic AND-chain equality, and has the small-bias expansion
\[
\Gamma_{\rm RO}(t)=A\,t\log_2(1/t)+O(t),
\qquad
A=2(C_0-4)=4.9096>0.
\tag{0.7}
\]
The same certificate proves the binary AND/OR gate inequality after adding `0.01 p(1-p)` to this base potential.

## 1. Decisive exact small case from the fresh account04/B17 handoff

Account04/B17 hands off the composition-prime four-bit gate
\[
B_0:\quad A=\{0,1,2,3,4,5,8,10\}\subset Q_4.
\]
For pivots `2` and `3` at uniform bias it proves exactly
\[
\mathcal W_j={1\over16},
\qquad
\mathcal R_{\Gamma_{\rm RO},j}+\mathcal C_j
=\Gamma_{\rm RO}(1/4)-{1\over2}C_0-1.
\tag{1.1}
\]
The read-once fixed point equals the AND-chain slack at every dyadic measure. Since the uniform two-bit AND has `I=1`, `H=2`, and output measure `1/4`,
\[
\Gamma_{\rm RO}(1/4)=C_0-2.
\tag{1.2}
\]
Therefore the local base contribution is exactly
\[
(C_0-2)-{C_0\over2}-1={C_0\over2}-3={1137\over5000}=0.2274,
\tag{1.3}
\]
so the requested base correction is
\[
\boxed{c_j^{\rm loc}=-16(0.2274)=-3.6384.}
\tag{1.4}
\]
After the live lift, the local defect is still strictly positive:
\[
0.2274+{0.2682048\over16}=0.2441628.
\tag{1.5}
\]
Thus this exact prime-gate orbit is not merely below the candidate margin; it lies deep on the favorable side. The calculation also illustrates why the signed/information credit in the B17 cocycle must be retained.

## 2. General theorem: every genuinely two-sided local gluing is repelled from a bias boundary

Fix the other product biases and a physical pivot `j`. Write `t=p_j`, and expand the two restrictions in the biased Walsh basis on the remaining coordinates:
\[
a_S=\widehat{f_0}(S),\qquad b_S=\widehat{f_1}(S),\qquad d_S=b_S-a_S.
\]
The exact parent coefficients from account04/B17 are
\[
\widehat f(S)=(1-t)a_S+t b_S,
\qquad
\widehat f(S\cup\{j\})=\sqrt{t(1-t)}\,d_S.
\tag{2.1}
\]
Let
\[
\delta=\Pr(f_0\ne f_1),
\qquad
\Delta=r_1-r_0,
\qquad
\kappa=\delta-\Delta^2.
\tag{2.2}
\]
Parseval gives
\[
\sum_S d_S^2=4\delta,
\tag{2.3}
\]
and the exact local currency is
\[
\mathcal W_j=t(1-t)\kappa.
\tag{2.4}
\]
Assume first that `r_0` is interior, so `0<r_0<1`, and that `\kappa>0`.

### Theorem 2.1 — local boundary-repulsion asymptotic

For every fixed Boolean restriction pair with `0<r_0<1` and `\kappa>0`,
\[
\boxed{
\mathcal R_{\Gamma_{\rm RO},j}+\mathcal C_j
=A\delta\,t\log_2(1/t)+O(t)
\qquad(t\downarrow0),
}
\tag{2.5}
\]
and hence
\[
\boxed{
{c_j^{\rm loc}(t)\over\log_2(1/t)}
\longrightarrow
-A{\delta\over\delta-\Delta^2}
\le -A=-4.9096.
}
\tag{2.6}
\]
In particular
\[
\boxed{c_j^{\rm loc}(t)\to-\infty}
\tag{2.7}
\]
as `t->0`. The symmetric statement holds as `t->1` with `r_1` in place of `r_0`.

### Proof

Put `phi(x)=x log_2(1/x)`. From (2.1), the parent spectral entropy minus the product-weighted child entropies is
\[
E(t):=\widetilde H_G-(1-t)\widetilde H_{G_0}-t\widetilde H_{G_1}.
\]
For each fixed Fourier index `S`,
\[
\phi\bigl(t(1-t)d_S^2\bigr)
=t d_S^2\log_2(1/t)+O(t).
\tag{2.8}
\]
The no-pivot coefficient contributes only `O(t)`: if `a_S\ne0`, `phi(((1-t)a_S+t b_S)^2)` is locally Lipschitz in `t`; if `a_S=0`, that mass is `t^2b_S^2` and contributes `O(t^2 log(1/t))`, while the weighted child term is only `O(t)`. Summing the finite Walsh expansion and using (2.3) gives
\[
\boxed{E(t)=4\delta\,t\log_2(1/t)+O(t).}
\tag{2.9}
\]
On the other hand
\[
h_2(V_t)=4t\log_2(1/t)+O(t),
\tag{2.10}
\]
so
\[
\delta h_2(V_t)-E(t)=O(t).
\tag{2.11}
\]
The exact entropy cocycle in account04/B17 says
\[
h_2(t)+h_2(\operatorname{It}_j)-\mathcal C_j=E(t).
\tag{2.12}
\]
Substituting (2.11) into its exact local defect formula therefore leaves
\[
\mathcal R_{\Gamma_{\rm RO},j}+\mathcal C_j
=(1-t)\Gamma_{\rm RO}(r_0)+t\Gamma_{\rm RO}(r_1)-\Gamma_{\rm RO}((1-t)r_0+t r_1)
+\delta\Gamma_{\rm RO}(t)+O(t).
\tag{2.13}
\]
Because `r_0` is interior and the fixed-point representation is locally Lipschitz on compact interior intervals, the first three terms in (2.13) are `O(t)`. Using (0.7) proves (2.5). Finally (2.4) gives
\[
\mathcal W_j=t\kappa+O(t^2),
\]
which yields (2.6). Since `\kappa<=\delta`, the ratio `\delta/\kappa>=1`, proving the dimension-free leading bound in (2.6). `QED`.

This is not the earlier `EQ_d` boundary theorem: it applies to an **arbitrary Boolean pair of physical restrictions** and to the exact local gluing margin in the restriction-tree max principle.

## 3. The only exceptional boundary geometry is one-sided, and it is already paid by binary AND/OR

Theorem 2.1 assumed `r_0` interior. Under interior biases on the remaining variables, `r_0=0` or `1` holds only if `G_0` is constant.

If `G_0` is constant and `G_1` is nonconstant, then the physical node is a one-sided composition of `G_1` with a binary AND/OR gate (up to input/output negations). Comparing the exact restriction cocycle with the standard gate-composition cocycle gives
\[
\boxed{c_j^{\rm loc}=c_{\rm AND/OR}(t,r_1)}
\tag{3.1}
\]
relative to the same base potential `Gamma_RO`. If both restrictions are constant, the node is a dummy/literal case and has zero positive-currency obstruction, exactly as classified by account04/B17.

The read-once interval certificate proves the binary gate inequality for
\[
\Gamma_{\rm RO}(p)+0.01p(1-p).
\]
Therefore every one-sided physical node satisfies the rigorous global bound
\[
\boxed{c_j^{\rm loc}\le0.01<0.2682048=a_*.}
\tag{3.2}
\]
Thus a local violation of the live stable lift cannot hide in the exceptional constant-child boundary geometry either.

## 4. Consequence for the universal gate problem

Combine account04/B17's weighted-average theorem with Theorem 2.1 and (3.2).

### Corollary 4.1 — any live-candidate violation contains a genuinely interior gluing node

If a Boolean gate satisfies
\[
-D_{\Gamma_{\rm RO}}(G)/W_G>a_*=0.2682048,
\]
then on every complete physical restriction tree there exists a positive-currency node with
\[
c_j^{\rm loc}>a_*.
\]
Such a node cannot be a dummy/literal node, cannot be one-sided constant-child AND/OR geometry, and cannot arise by taking its pivot bias to `0` or `1` while the source-side restriction output remains interior. Therefore any counterexample mechanism to `LIMIT-PRIME-GATE-LIFT-v1` must contain a **genuinely two-sided interior restriction gluing**.

For a fixed arity `k` and a compact box for the other biases, the argument is uniform: there are finitely many Boolean restriction pairs, `delta` and all nonconstant output measures stay bounded away from zero on that box, and the `O(t)` bounds above are uniform. Hence, once the lower-dimensional boundary faces are controlled, there exists a common positive boundary-strip width in which no local margin can exceed `a_*`. This turns each fixed-arity verification problem into a compact-interior problem rather than an open boundary search.

This compactness statement is per fixed arity; it is not a dimension-independent cutoff as `k->infinity`, and I do not claim one.

## 5. Compact conditional end-to-end argument and exact new missing implication

The current universal candidate now has the following exact conditional proof chain.

1. A universal proof of `(G)` for `Gamma_*` implies full FEI with constant `C_*=6.5218512` by the gate reformulation.
2. The proved gate-composition cocycle reduces any global violation to a composition-prime violating factor.
3. Account04/B17's restriction-tree theorem reduces the required scalar correction of any gate to a weighted average of exact local physical gluing margins with **all KL/information credits retained**.
4. This report proves that every genuinely two-sided local gluing is strongly repelled from a pivot-bias boundary, with dimension-free leading coefficient at most `-4.9096`, while every one-sided boundary gluing is already certified below `0.01` by the binary AND/OR theorem.
5. Therefore a counterexample to the live lift must produce an **interior**, positive-currency Boolean restriction pair with local margin above `0.2682048`.

The old missing implication was the unrestricted all-prime/all-bias gate inequality. The new, strictly localized missing implication is:

\[
\boxed{
\mathcal R_{\Gamma_{\rm RO},j}+\mathcal C_j
+a_*\mathcal W_j\ge0
}
\tag{5.1}
\]
for every genuinely two-sided **interior** Boolean restriction pair. By the weighted-average theorem, proving (5.1) universally would prove the live all-gate candidate; an exact violation would refute that candidate but not FEI.

I do not have a proof of (5.1) on the full interior class in this run. No finite search, auxiliary subclass, or boundary theorem is promoted to full FEI.

## 6. Status

**Result:** `ESSENTIAL_STEP_APPLIED`. The boundary part of the exact local restriction-gluing problem is closed for the live scalar-lift mechanism, including the constant-child exception. The remaining threat is genuinely interior.

**Full FEI:** **OPEN / NOT PROVED**.  
**Live candidate `LIMIT-PRIME-GATE-LIFT-v1`:** **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

Scoped privacy/provenance review: mathematical formulas, public theorem names, and repository-relative private artifact identifiers only; no credentials, scheduler IDs, machine paths, unrelated private material, benchmark gold, email/Drive content, paid/remote compute, workflows, permission changes, or public-posting actions.
