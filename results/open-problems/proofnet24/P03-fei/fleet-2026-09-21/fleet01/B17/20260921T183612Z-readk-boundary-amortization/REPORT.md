# B17 FEI creative continuation: common-boundary MUX lemma and an improved read-k decision-tree bound

**Status:** **PARTIAL. Full Friedgut--Kalai Fourier entropy--influence (FEI) remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Primary route:** APPROACH 3/7/14 — sensitivity-boundary coupling, larger composition class, and entropy coding.  
**Scientific source:** entered from `yspennstate/math-open-problems` master `03edf97be0d9e68ef87bdaa33aaad49a0d6a7332`, refreshed before delivery through `a6e765a1cfc60c41405060577ce86097952d55ba`.  
**Continuation point:** fleet01/B17 bounded-overlap MUX theorem (`20260921T173715Z-bounded-overlap-mux`).  
**No audit:** no read-once certificate or settled finite sweep was rerun.

## 1. Why this is a new move on the B17 route

The preceding B17 run proved a local MUX toll `Omega <= O(r) q` when the two branches share `r` variables. That is dimension-free for fixed overlap but does not help when the overlap grows. The earlier shared-MUX run also proved a sharper boundary form involving the whole disagreement indicator `ab`, but that bound charges boundary in variables that occur in only one branch and therefore does not directly amortize in a decision tree.

This run isolates only the boundary **inside the common-variable block**, then shows that those common-boundary terms globally amortize in a read-`k` decision tree. The result is a new proof mechanism and a substantially smaller explicit linear-in-`k` constant than the classical `9k` decision-tree bound. A quick literature comparison found the standard Wan--Wright--Wu read-`k` estimate `H <= 9k I` (arXiv:1312.3003 / ITCS 2014), also cited as the known read-`k` result by González--MacManus--Pereyra (arXiv:2606.00246, 2026). **No publication-priority claim is made** for the constant improvement without a fuller literature search and independent proof checking.

## 2. Local setup

Let `Y` be the variables shared by two Boolean branches, and let `U,V` be their disjoint residual variable sets:

\[
a=a(Y,U),\qquad b=b(Y,V),\qquad U\cap V=\varnothing.
\]

Let `z` be fresh and

\[
f=\operatorname{MUX}_z(a,b)=\frac{a+b}{2}+z\frac{a-b}{2}.
\]

Put

\[
q=\Pr[a\ne b]=\operatorname{Inf}_z(f),\qquad s=\min(q,1-q).
\]

As in the earlier B17 MUX reports,

\[
H(f)=\frac{H(a)+H(b)}2+\Omega,
\]

and if `p_S=ahat(S)^2`, `r_S=bhat(S)^2`, while `Z` records whether the selector belongs to the spectral sample of `f`, then exactly

\[
\boxed{\Omega=\operatorname{JS}(p,r)+H(Z\mid S).}\tag{2.1}
\]

Changing `b` to `-b` swaps the two selector channels but changes neither `Omega`, `H(b)`, the squared branch spectrum, nor any influence of `ab`. Hence for the proof we may sign-align the branches so that `q=s<=1/2`.

## 3. New local theorem: only the common-coordinate sensitivity boundary is charged

Let

\[
D(Y,U,V)=a(Y,U)b(Y,V)\in\{-1,1\},
\]

and write

\[
I_Y(D)=\sum_{j\in Y}\operatorname{Inf}_j(D).
\]

### Theorem 3.1 — common-boundary MUX inequality

For all Boolean branches of the form above,

\[
\boxed{
\Omega
\le
\frac{1}{2\ln2}\,I_Y(D)
+
C_0\,s,
}\tag{3.1}
\]

where

\[
\boxed{
C_0=2+\frac{2+2/\sqrt e}{\ln2}
=6.635467631606982\ldots .
}\tag{3.2}
\]

The important point is not the numerical constant but the support of the boundary term: **exclusive residual variables `U,V` do not appear in it.**

### Proof

#### Step 1: JS term

The Fourier-Hellinger estimate from the preceding shared-MUX calculation gives

\[
\operatorname{JS}(p,r)
\le \frac{1-\sum_S|\widehat a(S)\widehat b(S)|}{\ln2}.
\]

After sign alignment, `E[ab]=1-2s>=0`, hence

\[
\sum_S|\widehat a(S)\widehat b(S)|
\ge \sum_S\widehat a(S)\widehat b(S)
=1-2s.
\]

Therefore

\[
\boxed{\operatorname{JS}(p,r)\le \frac{2}{\ln2}s.}\tag{3.3}
\]

#### Step 2: split selector entropy into the shared Fourier core and residual atoms

Define conditional means on the common physical block,

\[
g(y)=\mathbb E_U a(y,U),\qquad h(y)=\mathbb E_V b(y,V).
\]

The branch spectra can overlap only on subsets of `Y`; their common Fourier cores are `ghat` and `hhat`. Let

\[
R_a=1-\mathbb E g^2,\qquad R_b=1-\mathbb E h^2.
\]

Every off-core base spectral atom belongs to only one branch, so conditioned on such an atom the selector channel is fair. Thus the off-core contribution to `H(Z|S)` is exactly

\[
T_{\rm res}=\frac{R_a+R_b}{2}.
\]

Because

\[
2-g^2-h^2\le 2(1-gh)
\]

pointwise and, by conditional independence of `U,V` given `Y`,

\[
\mathbb E_Y[gh]=\mathbb E[ab]=1-2s,
\]

we have `R_a+R_b<=4s` and therefore

\[
\boxed{T_{\rm res}\le2s.}\tag{3.4}
\]

#### Step 3: turn the common-core selector mass into a physical conditional-disagreement density

Let

\[
\delta(y)=\Pr_{U,V}[a(y,U)\ne b(y,V)\mid Y=y]
=\frac{1-g(y)h(y)}2.
\]

Then `E delta=s`. Put

\[
e(y)=\frac{g(y)-h(y)}2.
\]

The identity

\[
(1-gh)^2-(g-h)^2=(1-g^2)(1-h^2)\ge0
\]

implies the pointwise domination

\[
|e(y)|\le\delta(y).\tag{3.5}
\]

If `Q` denotes the total selector-1 mass lying in the common Fourier core, Parseval gives

\[
Q=\frac14\sum_{T\subseteq Y}(\widehat g(T)-\widehat h(T))^2
=\mathbb E e^2
\le \mathbb E\delta^2=:\mu.
\tag{3.6}
\]

Since `0<=delta<=1`, `mu<=s<=1/2`.

Let `M_T=(ghat(T)^2+hhat(T)^2)/2` and `A_T=(ghat(T)-hhat(T))^2/4`. The common-core conditional entropy is

\[
T_{\rm core}=\sum_T M_T h_2(A_T/M_T).
\]

By concavity of binary entropy,

\[
T_{\rm core}\le M_{\rm core}h_2(Q/M_{\rm core})\le h_2(Q)\le h_2(\mu),\tag{3.7}
\]

where the middle inequality uses that `M -> M h_2(Q/M)` is increasing for `M>=Q`, and the last uses `Q<=mu<=1/2`.

#### Step 4: physical cube log-Sobolev pays the rare coherent core only with common-variable boundary

For the nonnegative function `delta` on the `Y`-cube, the standard two-point log-Sobolev inequality, tensorized over `Y`, gives in bits

\[
\operatorname{Ent}(\delta^2)
\le \frac{1}{2\ln2}
\sum_{j\in Y}\mathbb E(\delta(y)-\delta(y^{\oplus j}))^2.
\tag{3.8}
\]

As `delta in [0,1]`, square differences are at most absolute differences. Moreover, coupling the same residual `(U,V)` on the two neighboring `Y`-fibres gives

\[
\mathbb E|\delta(y)-\delta(y^{\oplus j})|
\le \operatorname{Inf}_j(D).
\]

Hence

\[
\boxed{
\operatorname{Ent}(\delta^2)
\le \frac{1}{2\ln2}I_Y(D).
}\tag{3.9}
\]

Now

\[
h_2(\mu)
=\operatorname{Ent}(\delta^2)
+\mathbb E\!\left[\delta^2\log_2\frac1{\delta^2}\right]
+(1-\mu)\log_2\frac1{1-\mu}.
\]

Using

\[
(1-\mu)\log_2\frac1{1-\mu}\le \frac{\mu}{\ln2}
=\mathbb E\frac{\delta^2}{\ln2},
\]

the last two terms are at most

\[
\mathbb E\left[
\frac{\delta^2}{\ln2}\left(2\ln\frac1\delta+1\right)
\right].
\]

For `0<=t<=1`,

\[
t\left(2\ln\frac1t+1\right)\le\frac{2}{\sqrt e},
\]

with equality at `t=e^{-1/2}`. Therefore

\[
\mathbb E\left[
\frac{\delta^2}{\ln2}\left(2\ln\frac1\delta+1\right)
\right]
\le \frac{2}{\sqrt e\,\ln2}\,\mathbb E\delta
=\frac{2}{\sqrt e\,\ln2}s.
\]

Combining with (3.9),

\[
\boxed{
T_{\rm core}
\le \frac{1}{2\ln2}I_Y(D)
+\frac{2}{\sqrt e\,\ln2}s.
}\tag{3.10}
\]

Finally (3.3), (3.4), and (3.10) yield (3.1)--(3.2). QED.

## 4. Global amortization in read-k decision trees

Consider a reduced deterministic decision tree for `F`: no variable is queried twice on one root-to-leaf path. At each internal node `v`, write `x_v` for its queried variable, `A_v,B_v` for its two residual Boolean subfunctions, `w_v` for the uniform-input probability of reaching `v`, and

\[
q_v=\Pr[A_v\ne B_v],\qquad s_v=\min(q_v,1-q_v).
\]

Let `Y_v` be the variables that occur in both child subtrees, and `D_v=A_vB_v`.

The exact MUX entropy recurrence telescopes:

\[
\boxed{H(F)=\sum_v w_v\Omega_v.}\tag{4.1}
\]

Likewise the influence spent at query nodes telescopes:

\[
\boxed{I(F)=\sum_v w_v q_v.}\tag{4.2}
\]

The second identity follows occurrence-by-occurrence: for a fixed variable `y`, its query nodes are incomparable in a reduced tree, their reach events are disjoint and unaffected by flipping `y`, and the contribution of a query occurrence `u` is exactly `w_u q_u`.

### Boundary amortization

For `y in Y_v`, pointwise

\[
\operatorname{Inf}_y(D_v)
\le \operatorname{Inf}_y(A_v)+\operatorname{Inf}_y(B_v)
=2\operatorname{Inf}_y(F_v).
\tag{4.3}
\]

Fix a variable `y` and suppose it labels `t_y` query nodes in the whole tree. Those occurrence nodes are an antichain. A node `v` has `y in Y_v` precisely only if the subtree of `v` contains occurrences of `y` in both children. For an occurrence `u` of `y`, the number of such branching ancestors is at most `t_y-1`: each branching ancestor has a sibling subtree containing a different `y`-occurrence, and these sibling witnesses can be chosen distinctly along the path.

Also

\[
w_v\operatorname{Inf}_y(F_v)
=\sum_{u:\,u\text{ is a }y\text{-query below }v}w_u q_u.
\]

Consequently

\[
\sum_v w_v I_{Y_v}(D_v)
\le 2\sum_y(t_y-1)_+\operatorname{Inf}_y(F).
\tag{4.4}
\]

If the decision tree is read-`k`, then `t_y<=k`, so

\[
\boxed{
\sum_v w_v I_{Y_v}(D_v)
\le2(k-1)I(F).
}\tag{4.5}
\]

This is the global payment that was missing from the previous bounded-overlap theorem: overlap *size* may be arbitrarily large at an individual node; only repeated-query multiplicity is charged.

## 5. The resulting read-k FEI theorem

Apply Theorem 3.1 at each node, multiply by `w_v`, sum, use `s_v<=q_v`, (4.2), and (4.5):

\[
\begin{aligned}
H(F)
&\le \frac{1}{2\ln2}\sum_vw_v I_{Y_v}(D_v)
   +C_0\sum_vw_vs_v\\
&\le \left(\frac{k-1}{\ln2}+C_0\right)I(F).
\end{aligned}
\]

Thus:

### Theorem 5.1 — read-k decision-tree bound from common-boundary amortization

Every Boolean function computed by a reduced read-`k` decision tree satisfies

\[
\boxed{
H(F)\le C_k I(F),\qquad
C_k=2+\frac{k+1+2/\sqrt e}{\ln2}.
}\tag{5.1}
\]

Numerically,

\[
C_1=6.635467631606982\ldots,
\qquad
\boxed{C_2=8.078162672495946\ldots},
\qquad
C_k=1.442695040888963\,k+5.192772590718\ldots .
\]

The classical Wan--Wright--Wu theorem states `H<=9k I` for read-`k` decision trees. Therefore, subject to independent checking and literature-priority clearance, (5.1) is a substantial constant improvement within an already-known FEI-positive class. It is **not** a proof of full FEI because general Boolean functions need decision trees with unbounded read count.

## 6. Stress tests

The accompanying deterministic checker directly recomputes Fourier transforms and tests Theorem 3.1 on exact Boolean branch truth tables in three overlap/residual geometries:

- shared block `r=2`, no residual variables: all `16 x 16 = 256` branch pairs;
- shared block `r=1`, one exclusive bit in each branch: all `16 x 16 = 256` pairs;
- shared block `r=2`, one exclusive bit in each branch: all `256 x 256 = 65,536` pairs.

There were **zero violations**. After subtracting the proved boundary term `(2 ln 2)^{-1} I_Y(D)`, the largest observed residual coefficient `(Omega - (2 ln2)^{-1}I_Y(D))/s` was `4.000000000000000`, well below the analytic `C0=6.635467631606982`. These finite computations are stress tests only; the theorem above is analytic.

Checker SHA-256: `a8c24f69cf7e462ca481c0e6dc3e0ce07e8994eebceaf73292600e5f49e7138d`.  
Recorded stdout SHA-256: `4d39a3ec932a9f875b966668bf4a49eaf556ed0ae81c3d36a1260f829a03d720`.

## 7. Relation to current literature

A fresh source check during this run found:

- Wan, Wright, Wu, *Decision Trees, Protocols, and the Fourier Entropy-Influence Conjecture* (arXiv:1312.3003; ITCS 2014): read-`k` decision trees satisfy `H<=9k I`.
- González, MacManus, Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture* (arXiv:2606.00246v2, June 2026): explicitly lists read-`k` decision trees as a known FEI class with a constant linear in `k`, and develops the restriction-step/stopping-tree framework relevant to the present route.

This report does **not** claim that the numerical constant (5.1) is unpublished. A complete priority search and independent proof verification would be required before such a claim.

## 8. What this changes for the full problem

The previous B17 obstruction showed that a local shared-MUX charge `Omega<=C q` cannot hold with dimension-independent `C`; a rare bent-plus-one-point flip forces a term linear in the shared dimension. The present theorem shows that the right object is instead the **common-coordinate boundary of the branch-disagreement process**, because that boundary can be amortized by query multiplicity rather than overlap cardinality.

For full FEI the remaining gap is now precise. A general restriction tree may query a coordinate many times across incomparable nodes. To remove the read-`k` parameter, one needs either:

1. a replacement for (4.5) that charges the common-boundary sum to `I(F)` without occurrence multiplicity, using cancellation/negative information credits between sibling regions; or
2. an adaptive stopping/restriction scheme in which the effective weighted branching multiplicity is universally bounded even though the literal decision-tree read count is not.

The most promising next B17 calculation is therefore to keep the signed disagreement fields `D_v` and test a **cross-node cancellation identity** for the weighted sum `sum_v w_v I_{Y_v}(D_v)`, rather than returning to local overlap-size bounds. Full FEI remains OPEN.
