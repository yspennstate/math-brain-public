# FOREST / account02 B02 — homogenized size-slack matrix and a summed Simpson obstruction

**Outcome:** `ESSENTIAL_STEP_APPLIED`. The Grimmett–Winkler uniform-all-forests pairwise negative-correlation conjecture remains **OPEN**. `FULL_PROOF_CANDIDATE=false`.

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`.

Assignment: derive a source-valid polynomial/probabilistic comparison for the uniform law on **all unrooted forests** at unit weights, and justify exactly what log-concavity/Rayleigh input applies.

Named partner consumed: `account03/B03`, latest complete run `20260922T002444Z-b03-forest-r11`, report blob `192564587f0f8ec3e12e805ce0593b9c367bbeef` (`FOREST-NO-UNIFORM-SIGNCLUSTER-SLACK-20260922`). Campaign lead consumed: `account01/B01`, run `20260922T000824Z-account01-B01-forest-11`, report blob `367d85a8c6ac4ef3f00e1686a28eac60642274e0`.

Brain status: **WITHOUT_VERIFIED_BRAIN**. No authenticated brain retrieval/context runtime was used.

## 1. Exact source scope and source audit

Let `G=(V,E)` be a finite simple graph, `m=|E|`, and

\[
P_G(\mathbf z)=\sum_{F\subseteq E:\,F\text{ acyclic}}\mathbf z^F.
\]

This is the independent-set polynomial of the graphic matroid. It counts every acyclic edge subset: disconnected forests, every possible size, and the empty forest. At unit weights write `Z=P_G(1)`, and for distinct edges `e,f`,

\[
\Delta_G(e,f)=Z_e Z_f-ZZ_{ef}.
\]

If `\Phi` is uniform over all forests and `X_e=1_{e\in\Phi}`, then

\[
\operatorname{Cov}(X_e,X_f)=-\frac{\Delta_G(e,f)}{Z^2}.
\]

Thus the source target is exactly `Delta_G(e,f)>=0`.

Two primary-source gates used below were rechecked.

1. **Complete log-concavity really applies to this unrooted law.** Anari–Liu–Oveis Gharan–Vinzant, *Log-Concave Polynomials III: Mason's Ultra-Log-Concavity Conjecture for Independent Sets of Matroids*, arXiv:1811.01600, Theorem 4.1, proves that for a matroid on `m` elements
   \[
   H(y,\mathbf z)=\sum_{I\in\mathcal I}y^{m-|I|}\mathbf z^I
   \tag{1.1}
   \]
   is completely log-concave. For the graphic matroid, `I` is exactly a forest. Setting `y=1` recovers `P_G` itself. No rooted-forest, spanning-tree, fixed-size, or component-weighted surrogate is being used.

2. **The weighted minor gate used by the lead is genuinely fixed-graph, not merely class-level.** Semple–Welsh, *Negative Correlation in Graphs and Matroids*, CPC 17 (2008), pp. 423–435, define “independence correlated” using **all positive real edge weights**. Their final note to Question (3) records Cocks's result: if the unit Grimmett–Winkler inequality holds for a graph `G`, then `M(G)` is independence correlated. Hence minimality on a smaller simple graph legitimately upgrades that smaller graph to the positive weights created by parallel-class simplification after contraction. This pays the source gate required by the lead's conditioning argument.

For orientation, Erickson, *Sums of squares and negative correlation for spanning forests of series parallel graphs*, Australasian J. Combin. 52 (2012), p. 76, uses the same independent-set Rayleigh difference and records the all-graphs I-Rayleigh conjecture. Complete log-concavity is only spectral negative dependence; it is not by itself the entrywise Rayleigh sign theorem.

## 2. Current lead and partner inputs

The lead proves for a lexicographically minimal source counterexample that the positive-covariance graph on physical edges is a **matching**. If `{e,f}` is a violating pair and `g` is any third edge, then

\[
C_{ef}:=\operatorname{Cov}(X_e,X_f)>0,
\qquad
C_{eg}<0,\quad C_{fg}<0,
\tag{2.1}
\]

and the exact binary total-covariance decomposition plus the source-valid deletion/contraction gate gives

\[
\boxed{\frac{C_{eg}C_{fg}}{\operatorname{Var}(X_g)}\ge C_{ef}.}
\tag{2.2}
\]

The named partner `account03/B03` then shows on the explicit 3-connected split family `S_{r,m}=K_r\vee\overline{K_m}` that the corresponding deletion/contraction ratio can approach one arbitrarily closely. Therefore **no graph-independent per-third-edge multiplicative slack** can finish the proof. Their explicit limit is

\[
L_r=\frac{r^2+r+2}{(r+1)(r+2)},
\qquad 1-L_r\to0.
\tag{2.3}
\]

So the next mechanism should aggregate the simultaneous inequalities (2.2), rather than trying to strengthen each of them by a fixed epsilon. This run does exactly that.

## 3. New source-valid augmented Hessian

Let

\[
K=|\Phi|,\qquad S=m-K,
\qquad p_i=\mathbb E X_i,
\qquad v_i=\operatorname{Var}(X_i)=p_i(1-p_i),
\]

and write

\[
\mu=\mathbb E K,\qquad V=\operatorname{Var}(K),
\qquad u_i=\operatorname{Cov}(K,X_i),
\qquad t=\mathbb E S-V=m-\mu-V.
\tag{3.1}
\]

Evaluate (1.1) at `y=1` and every edge variable equal to one. Complete log-concavity implies

\[
Q:=-\nabla^2\log H(1,\mathbf1)\succeq0.
\tag{3.2}
\]

Direct differentiation gives every entry needed here:

\[
\boxed{
Q_{yy}=t,
\qquad Q_{yi}=u_i,
\qquad Q_{ii}=p_i^2,
\qquad Q_{ij}=-C_{ij}\ (i\ne j).
}
\tag{3.3}
\]

The `y` coordinate is the missing piece in the previous edge-only spectral argument. It couples pair correlations to fluctuations of the **total forest size** without changing the source measure.

### Size variance consequence

Restrict all edge variables to a common variable `z`. Then the `2x2` `y,z` block of `-Hess log H` is

\[
\begin{pmatrix}
 m-\mu-V & V\\
 V & \mu-V
\end{pmatrix}\succeq0.
\]

Its determinant yields the exact all-graph bound

\[
\boxed{V\le \frac{\mu(m-\mu)}{m}.}
\tag{3.4}
\]

This is a genuine unit-law statement for the unrooted forest size distribution, derived directly from the same complete-log-concavity theorem.

Also, summing `u_i=Cov(K,X_i)` gives the identity

\[
\boxed{\sum_i u_i=V.}
\tag{3.5}
\]

## 4. New theorem: aggregate all third-edge Simpson constraints

Assume now that `G` is a minimal counterexample and `{e,f}` is its violating pair. Put

\[
C=C_{ef}>0.
\]

For every external edge `g`, define

\[
x_g=-C_{eg}>0,
\qquad y_g=-C_{fg}>0,
\qquad \sigma_g=\sqrt{v_g}.
\]

By (2.2),

\[
x_g y_g\ge C v_g=C\sigma_g^2.
\tag{4.1}
\]

Let

\[
A_e=\sum_{g\ne e,f}x_g,
\qquad
A_f=\sum_{g\ne e,f}y_g,
\qquad
W=\sum_{g\ne e,f}\sigma_g.
\]

Cauchy–Schwarz and (4.1) give the **aggregate lower bound**

\[
\boxed{A_eA_f\ge C W^2.}
\tag{4.2}
\]

But covariance with the total size gives exact expressions

\[
u_e=v_e+C-A_e,
\qquad
u_f=v_f+C-A_f,
\tag{4.3}
\]

so

\[
A_e+A_f=v_e+v_f+2C-(u_e+u_f).
\tag{4.4}
\]

Now use the positive-semidefinite matrix (3.3). The PSD Cauchy inequality between the `y` Gram vector and the sum of the `e,f` Gram vectors is

\[
(u_e+u_f)^2
\le
 t\bigl(p_e^2+p_f^2-2C\bigr),
\tag{4.5}
\]

because the `e,f` Gram inner product is `Q_{ef}=-C`. Consequently

\[
A_e+A_f
\le
v_e+v_f+2C
+\sqrt{t\bigl(p_e^2+p_f^2-2C\bigr)}.
\tag{4.6}
\]

Since `A_e,A_f>=0`, AM–GM and (4.2) give the new necessary condition:

### Theorem 4.1 — homogenized summed-Simpson obstruction

Every violating pair in a lexicographically minimal source counterexample must satisfy

\[
\boxed{
4C\left(\sum_{g\ne e,f}\sqrt{v_g}\right)^2
\le
\left[
 v_e+v_f+2C
 +\sqrt{t\bigl(p_e^2+p_f^2-2C\bigr)}
\right]^2.
}
\tag{4.7}
\]

This is the first direct join between the named partner's “sum over all third edges” direction and the source-valid homogenized complete-log-concavity coordinate. It does not seek any fixed per-edge epsilon, so the partner's split-graph obstruction (2.3) does not defeat it.

## 5. Eliminate the external list: a scalar necessary condition

Two elementary matroid facts make (4.7) source-usable without recording every third-edge marginal.

First, for any edge `g`, deleting `g` maps every forest containing `g` injectively to a forest omitting `g`. Thus

\[
\boxed{p_g\le\frac12.}
\tag{5.1}
\]

Therefore

\[
v_g=p_g(1-p_g)\ge \frac{p_g}{2}.
\]

Hence

\[
W^2\ge\sum_{g\ne e,f}v_g
\ge \frac12\sum_{g\ne e,f}p_g
=\frac12(\mu-p_e-p_f).
\tag{5.2}
\]

Substitution into (4.7) gives the compact scalar obstruction

\[
\boxed{
2C(\mu-p_e-p_f)
\le
\left[
 v_e+v_f+2C
 +\sqrt{t\bigl(p_e^2+p_f^2-2C\bigr)}
\right]^2.
}
\tag{5.3}
\]

Second, for the uniform independent-set law of any **loopless matroid of rank `r`**,

\[
\boxed{\mathbb E|I|\ge r/2.}
\tag{5.4}
\]

A short deletion/contraction induction proves this. If `e` is a coloop, uniform independent sets are obtained from a uniform independent set of `M\setminus e` and an independent fair choice whether to add `e`, so the mean rises by `1/2`. If `e` is not a coloop, `M\setminus e` has rank `r` while `M/e` has rank `r-1` (loops created by contraction can be discarded without changing its independent sets). By induction the absent stratum has mean at least `r/2`, while the present stratum has mean at least `1+(r-1)/2=(r+1)/2`; their weighted average is at least `r/2`.

For a connected graph the graphic rank is `|V|-1`. Combining (5.1), (5.3), and (5.4), any violating pair in a 3-connected minimal counterexample on `n` vertices must obey

\[
\boxed{
C(n-3)
\le
\left[
 v_e+v_f+2C
 +\sqrt{t\bigl(p_e^2+p_f^2-2C\bigr)}
\right]^2.
}
\tag{5.5}
\]

The current complete source coverage through nine vertices makes `n>=10` in the preserved minimal-counterexample programme, so in particular the right side must be at least `7C`.

## 6. What this pays and what remains unpaid

The lead's compact conditional end-to-end route is now sharper:

1. take a minimal source counterexample;
2. source-valid fixed-graph Cocks/Semple–Welsh weighting makes deletion and contraction strata Rayleigh;
3. the lead's total-covariance argument makes every violation an isolated matching edge and forces (2.2) for **every** third edge;
4. the partner proves no fixed multiplicative slack can be extracted from any one triple;
5. this run aggregates all triples and, using the homogenizing coordinate of the exact unrooted forest polynomial, forces (4.7), hence (5.3)/(5.5).

The **first essential missing implication** is now concrete and graph-local: use 3-connectivity / reconnection structure to force the external variance mass and marked-edge size sensitivities to violate (4.7), or exhibit a source-valid 3-connected response satisfying (4.7) together with the lead's simultaneous Simpson inequalities. Merely proving another per-third-edge `R<=1-epsilon` is ruled out by the named partner and is no longer the requested route.

No unsupported claim that complete log-concavity itself gives the Rayleigh sign is made. Equation (4.7) is a necessary obstruction, not a proof of `C<=0`.

## 7. Exact computation

The exact standard-library checker stored beside this report exhausts all `1,098` labelled simple graphs on `2..5` vertices and all `11,766` present edge pairs. It uses exact `Fraction` arithmetic and independently verifies the moment identities and inequalities used above:

- size-variance bound (3.4);
- edge-pair spectral bound `C_ef^2<=p_e^2p_f^2`;
- homogenized support bound (4.5);
- `mu>=rank/2`;
- `p_e<=1/2`;
- `sum_i u_i=Var(K)`.

Archived output:

```text
graphs=1098
present_edge_pairs=11766
positive_covariance_pairs=0
size_variance_bound_failures=0
edge_pair_psd_failures=0
homogenized_support_bound_failures=0
rank_half_mean_failures=0
edge_marginal_half_failures=0
sum_u_identity_failures=0
minimum_size_slack=0
minimum_support_slack=0
ALL_EXACT_CHECKS_PASSED
```

Checker blob: `6552eadcdae4c70e2a6eb8ca45e58da4d59637cd`. Output blob: `ccfd6b5dcc175b6a68d620eedf713dfc2930f887`.

The absence of positive covariance through five vertices is finite regression evidence only and is not used to prove the parent conjecture.

## 8. Status

- Parent target: **OPEN**.
- New result: exact homogenized moment matrix (3.3), size variance bound (3.4), and summed-Simpson obstruction (4.7), scalarized to (5.3)/(5.5).
- Named OTHER-account result applied: `account03/B03` no-uniform-slack theorem, report blob `192564587f0f8ec3e12e805ce0593b9c367bbeef`.
- Lead version applied: `account01/B01` matching/universal-Simpson report blob `367d85a8c6ac4ef3f00e1686a28eac60642274e0`.
- Outcome label: **`ESSENTIAL_STEP_APPLIED`**.
- Novelty/priority: **UNVERIFIED**; no priority inference is made from repository or web search absence.
