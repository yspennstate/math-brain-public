SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-24T03:22:44.403579Z.
attacking: the fresh pair-star/cross-star endpoint — absorb source-disjoint longitudinal leakage into the literal hub, pay every low-transverse-overlap shared-shear configuration, and force any survivor into a genuinely high-cardinality product-overlap chamber before aggregate Pluecker coarea.

# account02/B05 — source-overlap endpoint for the Witt shared shear

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** quadratic coarea / equivalent interval bound preserving arbitrary original-coordinate product densities.  
**Status:** `PROVED_SUPPORTING_THEOREM / FINITE-SPIKE-ENDPOINT-PAID / HIGH-CARDINALITY-SHARED-OVERLAP-FORCED / FULL-QFORM-OPEN`.  
**Regularity:** essential boundedness is proved in the stated branches. Full-target continuity remains separate and OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh state and first unpaid implication


The fresh account01/B05 Witt compiler puts the exact-rank-three heavy-null survivor in the form

\[
Q=2aV(H+\kappa U)+\alpha V^2+2\gamma VW+\delta W^2,                 \tag{1.1}
\]

where

* `H` is a literal original coordinate and is genuinely independent of the residual product bank;
* `U=u\cdot X`, `V=v\cdot X`, `W=w\cdot X`, with `u,v,w` orthonormal coefficient vectors on the residual ORIGINAL coordinates;
* no independence of `U,V,W` is asserted;
* `a\ne0`, `\delta\ne0`; and
* the heavy-coordinate determinant-star currency is exactly

\[
\boxed{S_i=a^2|\delta|=c\Delta_3.}                                  \tag{1.2}
\]

At target normalization in the high-leverage branch, `S_i>=1/2`.

The newest completed designated partner account03/B05 result is r39,
`QFORM-PAIR-ANCHORED-DETSTAR-COAREA-v1`. For every literal pair `{i,j}` in an exact-rank-three form, if

\[
T_{ij}=\sum_{k\notin\{i,j\}}|\det A_{\{i,j,k\}}|>0,
\]

then

\[
\|p_Q\|_{\infty,\mathrm{ess}}
 \le C_{\star}T_{ij}^{-1/3},\qquad
C_{\star}=491.735145127\ldots .                                     \tag{1.3}
\]

In the Witt coordinates, account01's exact identity is

\[
T_{ij}=S_i q_j,\qquad q_j:=v_j^2+w_j^2.                              \tag{1.4}
\]

Therefore a real first exit is already available: if any residual coordinate has

\[
q_j\ge\frac1{64},                                                     \tag{1.5}
\]

then `T_ij>=1/128` and r39 gives

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le C_{\star}128^{1/3}
<2478.190 .
}                                                                    \tag{1.6}
\]

Hence every unpaid descendant may assume

\[
\boxed{q_j<1/64\quad\text{for every residual original coordinate }j.} \tag{1.7}
\]

The new theorem below pays the complementary endpoint where the longitudinal shear is source-disjoint after conditioning a set carrying less than one unit of transverse leverage. The first unpaid implication after it is

`QFORM-WITT-HIGH-CARDINALITY-OVERLAP-AGGREGATE-COAREA-v1`:

> under (1.7), prove the account01 cross-star Borel tube estimate before reciprocal pair selection in the chamber where at least one full unit of transverse leverage is carried by original coordinates that also have nonzero longitudinal coefficient. In this survivor the shared-overlap support has at least 65 coordinates.

This is strictly narrower than the previous “at most three longitudinal spikes” description: the exact finite-spike/source-disjoint endpoint is paid below.

## 2. Source-overlap theorem

For a residual coordinate define its transverse leverage

\[
q_j=v_j^2+w_j^2.                                                       \tag{2.1}
\]

### Theorem 2.1 — `QFORM-WITT-SOURCE-DISJOINT-LONGITUDINAL-TAIL-v1`

Assume the exact Witt form (1.1), with independent cap-one ORIGINAL inputs. Let `S,D,T` be a partition of the residual original coordinates such that

\[
u_j=0\quad(j\in T),\qquad
v_j=w_j=0\quad(j\in D).                                               \tag{2.2}
\]

Thus every source that is simultaneously longitudinal and transverse has been put into `S`; the bank `D` is purely longitudinal and the bank `T` is purely transverse. Put

\[
q_S:=\sum_{j\in S}(v_j^2+w_j^2).                                     \tag{2.3}
\]

If `q_S<1`, then `Q` has an essentially bounded density and

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le
C_{NH}\left(\frac{2}{1-q_S}\right)^{2/3}S_i^{-1/3},
\qquad C_{NH}=7.761982175235\ldots .
}                                                                    \tag{2.4}
\]

The estimate is uniform in `\kappa`, `\alpha`, `\gamma`, all conditioned values on `S`, all source supports, and all one-dimensional cap-one input laws.

### Proof

Condition only on the literal original coordinates `X_S`. This preserves independence among the untouched original-coordinate banks `H`, `X_D`, and `X_T`.

Because `u_T=0` and `v_D=w_D=0`, after conditioning `S` we can write

\[
U=U_S+U_D,
\qquad
V=c_V+V_T,
\qquad
W=c_W+W_T,                                                           \tag{2.5}
\]

where `U_S,c_V,c_W` are deterministic under the conditioning, `U_D` uses only bank `D`, and `(V_T,W_T)` uses only bank `T`.

Define

\[
H_*:=H+\kappa U_D+\kappa U_S.                                       \tag{2.6}
\]

The law of `H_*` conditional on `X_S` has density cap at most one. Indeed, `H` has density at most one and is independent of `U_D`, so the law of `H+\kappa U_D` is the convolution of the density of `H` with a probability measure; translation by the deterministic `\kappa U_S` changes no cap. Crucially, `H_*` is genuinely independent of the untouched transverse bank `X_T`.

It remains to bound the two-dimensional density of `(V_T,W_T)`. Let

\[
g_j=(v_j,w_j)^T,\qquad j\in S,
\]

and let

\[
G_T=
\begin{pmatrix}
\|v_T\|_2^2&\langle v_T,w_T\rangle\\
\langle v_T,w_T\rangle&\|w_T\|_2^2
\end{pmatrix}.
\]

Since `v,w` are orthonormal and the bank `D` has zero transverse coefficients,

\[
G_T=I_2-\sum_{j\in S}g_jg_j^T.                                      \tag{2.7}
\]

The removed matrix is positive semidefinite with trace `q_S`, hence

\[
\boxed{G_T\succeq(1-q_S)I_2},
\qquad
\sqrt{\det G_T}\ge1-q_S.                                           \tag{2.8}
\]

Whiten the two coefficient columns on bank `T`. The pinned product-projection marginal theorem used in the ruled source gives density cap at most `2` for every orthonormal two-dimensional projection of a cap-one product law. Undoing the whitening therefore gives

\[
\boxed{
\|p_{(V_T,W_T)}\|_\infty
\le\frac{2}{\sqrt{\det G_T}}
\le\frac{2}{1-q_S}.
}                                                                    \tag{2.9}
\]

Translations by `c_V,c_W` do not change this cap.

Now rewrite the conditioned form exactly as

\[
Q=2aVH_*+\alpha V^2+2\gamma VW+\delta W^2.                          \tag{2.10}
\]

Scale the genuine independent hub to `\widetilde H=aH_*`; its density cap is at most `|a|^{-1}`. Apply the completed account02/B05 theorem `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1` to the honest independent hub `\widetilde H` and the actual joint pair `(V,W)`. With

\[
M\le\frac{2}{1-q_S},\qquad m\le|a|^{-1},\qquad c_2=\delta,
\]

that theorem gives, uniformly in the conditioned value `X_S`,

\[
\|p_{Q\mid X_S}\|_{\infty,\mathrm{ess}}
\le C_{NH}(Mm)^{2/3}|\delta|^{-1/3}
\le C_{NH}\left(\frac{2}{1-q_S}\right)^{2/3}
     |a|^{-2/3}|\delta|^{-1/3}.                                     \tag{2.11}
\]

Using `S_i=a^2|\delta|`, the last two factors equal `S_i^{-1/3}`. Averaging the uniform conditional interval inequality over `X_S` proves (2.4) for arbitrary rough input laws. No conditional density cap is substituted for independence: the only independence used is the literal source-disjointness of `H\cup D` and `T`. QED.

## 3. Canonical overlap-mass corollary

Define the shared longitudinal/transverse support

\[
\mathcal O:=\{j:u_j\ne0\ \text{and}\ q_j>0\},                       \tag{3.1}
\]

and its transverse mass

\[
\Omega:=\sum_{j\in\mathcal O}q_j.                                  \tag{3.2}
\]

Take `S=\mathcal O`, `D=\{j:u_j\ne0,q_j=0\}`, and `T=\{j:u_j=0\}`. These are source-disjoint ORIGINAL-coordinate banks and satisfy (2.2). Therefore:

### Corollary 3.1 — `QFORM-WITT-OVERLAP-MASS-ENDPOINT-v1`

If

\[
\boxed{\Omega<1,}                                                     \tag{3.3}
\]

then

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le
C_{NH}\left(\frac{2}{1-\Omega}\right)^{2/3}S_i^{-1/3}.
}                                                                    \tag{3.4}
\]

Thus any unpaid Witt shared-shear instance must satisfy

\[
\boxed{\Omega\ge1.}                                                  \tag{3.5}
\]

This is a support-sensitive statement, deliberately so. A coefficient that is merely small but nonzero cannot be deleted under arbitrary unbounded inputs. The theorem instead identifies exactly when the genuinely independent longitudinal sources can be convolved into the literal hub without losing the transverse two-dimensional product bank.

## 4. Fresh partner r39 forces high cardinality

Combine Corollary 3.1 with the fresh partner exit (1.6). In an unpaid target-normalized state we may assume `q_j<1/64` for every residual coordinate and `\Omega>=1`. Hence

\[
1\le\sum_{j\in\mathcal O}q_j
 <\frac{|\mathcal O|}{64},
\]

so

\[
\boxed{|\mathcal O|\ge65.}                                          \tag{4.1}
\]

This is a substantive structural gain: the surviving shared-shear obstruction is necessarily high-cardinality. It cannot consist of one, two, three, or any bounded handful of longitudinal/transverse source overlaps at this fixed threshold.

The account01 residual-heavy dichotomy becomes especially clean. Let

\[
\ell'_j=u_j^2+q_j                                                     \tag{4.2}
\]

be the normalized residual row leverage. Under `q_j<1/64`, every residual-heavy row `\ell'_j>1/2` satisfies

\[
u_j^2>\frac{31}{64}.                                               \tag{4.3}
\]

There are therefore at most two such rows. If every overlap coordinate belonged to those heavy rows (with all remaining longitudinal sources pure longitudinal and all remaining transverse sources pure transverse), then

\[
\Omega<\frac2{64}=\frac1{32}.                                       \tag{4.4}
\]

Theorem 2.1 would give, using `S_i>=1/2`,

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
<15.857.
}                                                                    \tag{4.5}
\]

Therefore the fresh account03/B05 r39 “longitudinal-spike” remainder is not a finite-spike obstruction: its exact pure-spike/source-disjoint endpoint is paid. Any genuine survivor must have many **light** original coordinates carrying both nonzero longitudinal and transverse coefficients. That is precisely the regime in which reciprocal single-pair selection is known to lose dimension and in which the account01 cross-star aggregate theorem is the right next interface.

## 5. Relation to the account01 aggregate Pluecker debt

The fresh account01/B05 pairwise theorem proves, for

\[
b_{jk}=v_jw_k-v_kw_j,
\]

a source-valid physical-pair Borel tube bound with cost `|b_jk|^{-1}`, and its exact curvature identity

\[
\sum_{j<k}b_{jk}^2=1.                                                \tag{5.1}
\]

It also exhibits a target-valid Walsh family with every individual `|b_jk|=O(1/N)` while the total and a source-disjoint cross Pluecker mass remain one. Thus choosing a single pair before inversion is genuinely insufficient.

The present theorem narrows that aggregate debt further. After the r39 exit and Corollary 3.1, a hard instance has simultaneously

\[
q_j<1/64\ \forall j,\qquad
\sum_{j\in\mathcal O}q_j\ge1,\qquad
|\mathcal O|\ge65.                                                   \tag{5.2}
\]

So the aggregate coarea theorem no longer needs to cover a finite source-overlap exception: every such exception is already paid by an honest independent-hub/two-dimensional-product projection argument. The remaining theorem must exploit a genuinely diffuse overlap of the longitudinal shear with at least one unit of the transverse frame.

This also explains why the target-valid Walsh stress family survives the present reduction: its longitudinal Walsh coefficient is nonzero on every residual coordinate, while `q_j=2/N`, so `\Omega=2` and the overlap is maximally high-cardinality.

## 6. Required pinned source applied to the live obstruction

The exact pinned package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

was reread in this invocation. Two completed results are used with their exact scopes.

First, its product-projection geometry supplies the dimension-free two-dimensional marginal cap used in (2.9), after whitening the actual untouched ORIGINAL-coordinate transverse bank. This is not an arbitrary-joint statement and does not assert independence of `V_T,W_T`.

Second, because an invertible rank-three form possessing a nonzero isotropic vector is necessarily indefinite, the pinned ruled Theorem C applies (after a global sign change if needed) to the one-sheet side and gives the real inequality

\[
\boxed{p_Q(s)\le\pi\sqrt2}                                          \tag{6.1}
\]

on its normalized ruled half-line. Hence the high-cardinality overlap debt isolated in (5.2) is genuinely aimed at the complementary convex/two-sheet side, not at the already-paid ruling. The pinned counterexample search still supplies no target-valid counterexample.

## 7. What remains

The first unpaid implication is now

### `QFORM-WITT-HIGH-CARDINALITY-OVERLAP-AGGREGATE-COAREA-v1`

In the Witt form (1.1), under target normalization and after the exits above, prove the source-disjoint cross-star Borel tube estimate before selecting any physical pair, in the chamber

\[
q_j<1/64\quad\forall j,
\qquad
\Omega=\sum_{j:u_j\ne0}q_j\ge1,
\qquad
|\mathcal O|\ge65.                                                   \tag{7.1}
\]

Equivalently, retain the many-coordinate original-product overlap between `U` and the transverse `(V,W)` plane and convert the aggregate Pluecker currency

\[
M_{J,K}=\sum_{j\in J,k\in K}(v_jw_k-v_kw_j)^2\ge\frac12             \tag{7.2}
\]

into the Borel shell factor `M_{J,K}^{-1/2}` **before** any reciprocal individual minor. Small nonzero shared coefficients cannot be removed, and generic joint-density/X-ray replacements remain invalid by the live corrections.

Full QFORM remains **OPEN / not proved / not disproved**. Full-target continuity remains **OPEN**.

## 8. Source pins

- Own null-hub/transverse-square theorem: `yspennstate/math-open-problems@e7a21ed67b943d7aded714ac17ca48bdab4a1349`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T200516Z-account02-B05-QFORM-auto11c/REPORT.md`.
- Fresh designated partner account03/B05 r39 theorem: `yspennstate/math-open-problems@2c56afab4cdeef591f4d39f4e8d065951a03d572`, with prepublication refresh `479369360517ab50d6f87aaa48b49d5feadd8851`.
- Fresh account01/B05 pairwise Pluecker tube / aggregate debt: `yspennstate/math-open-problems@49e5472fbcb6e988b716d8e014dd9e893510426c`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260924T032721Z-account01-B05-QFORM-auto11/REPORT.md`.
- Required pinned package: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Repository retrieval and Git delivery do not establish native learned-memory ingestion. `full_brain_connected=false`; execution remains `WITHOUT_VERIFIED_BRAIN`.
