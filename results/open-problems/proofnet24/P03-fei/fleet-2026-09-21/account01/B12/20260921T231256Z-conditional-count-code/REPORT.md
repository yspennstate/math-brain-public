# B12 FEI compression route — conditional ordered code and component-count collapse

**Status:** **PARTIAL. Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**

**Joint execution target:** Campaign B, direct Shannon entropy / actual spectral code. This run addresses the assigned task: derive the conditional Shannon increment for the current hierarchical code and bound its missing term on a genuine completed robust sector.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated private GitHub control/research artifacts were consumed, but no native mathematical-brain receiver/context was used.

**Outcome classification:** `ESSENTIAL_STEP_APPLIED` on the fine closed Palm-robust sector; not a universal FEI proof.

## 0. Compatible peer results consumed substantively

Two named other-account results are used in the proof, not merely cited.

1. `account03/B12`, `20260921T224810Z-local-factorial-hierarchy/REPORT.md` (read from scientific master `af0de385d50b5ec2285232310e227d5fbce5cd56`). It proves the exact factorial split
   \[
   Q=Q_{\rm int}+Q_{\rm mac},\qquad Q=\mathbb E\log_2(K!),
   \]
   and, for each fine reciprocal Palm component `C` with `m_C=|C|-1` and
   \[
   \operatorname{TV}(\nu_i,U_{C\setminus\{i\}})\le \frac1{16m_C},
   \]
   the coefficient-one internal payment
   \[
   E_C\le \mathbb E\log_2(K_C!)+c_0P_C,
   \qquad
   c_0=2\log_2 e+\frac1{16}=2.9478900817779268\ldots .
   \tag{0.1}
   \]
   Here `P_C=sum_{i in C}p_i`, `K_C=|Y cap C|`, and
   \(E_C=P_CH((p_i/P_C)_{i\in C})\).

2. `account04/B12`, `20260921T201418Z-palm-trigger-cluster/REPORT.md`, blob `4643e5dd27cc48a508820a30413e24b9c4717fac`. It proves reciprocal trigger locking
   \[
   F_i=C\setminus\{i\}
   \]
   inside a reciprocal component and records the physical near-subcube scale relation
   \[
   |2^{-m_C}-p_i|\le \frac1{16}p_i.
   \tag{0.2}
   \]

The new point below is that, once (0.1) is localized, the remaining macro-label/interleaving cost is not `I H(rho)`: after conditioning on arbitrary side information it collapses to the entropy of the **component count vector**. In the fine physical/Palm sector, that count-vector entropy is itself `O(I)`.

## 1. Exact conditional ordered-code identity

Let `(T,Y)` be any finite joint law where `Y` is a random subset of a finite coordinate set and `T` is arbitrary side information. Put
\[
K=|Y|,\qquad \mu=\mathbb EK,\qquad p_i=\Pr(i\in Y),\qquad q_i=p_i/\mu
\]
when `mu>0`.

Conditional on `Y`, choose a uniformly random ordering
\[
(L_1,\ldots,L_K)
\]
of its elements. Let `P_r=(L_1,\ldots,L_{r-1})` be the ordered predecessor prefix. Under the normalized insertion-edge law, a context is
\[
C=(T,K,P_r),
\]
and the inserted label is `L=L_r`. Every terminal set contributes exactly one edge for each of its coordinates, so the marginal law of `L` under this edge law is exactly `q`.

### Theorem 1.1 — conditional Palm/Shannon equality

\[
\boxed{
H(Y\mid T)
=H(K\mid T)+\mu H(q)-\mathbb E\log_2(K!)
-\mu I_2(L;T,K,P).
}
\tag{1.1}
\]

Equivalently, if
\[
D_T:=\mathbb E\sum_{r=1}^{K}
D_2\!\left(
\operatorname{Law}(L_r\mid T,K,P_r)\,\|\,q
\right),
\]
then
\[
D_T=\mu I_2(L;T,K,P)
\]
and (1.1) reads
\[
H(Y\mid T)=H(K\mid T)+\mu H(q)-Q-D_T.
\tag{1.2}
\]

#### Proof

Given `(T,Y)`, the auxiliary random ordering has entropy `log2(K!)`. Therefore
\[
H(K,L_1,\ldots,L_K\mid T)
=H(Y\mid T)+\mathbb E\log_2(K!).
\]
The chain rule gives the left side as
\[
H(K\mid T)+\mathbb E\sum_{r=1}^{K}H(L_r\mid T,K,P_r).
\]
For each context, entropy equals cross-entropy against `q` minus the KL divergence to `q`. Summed over all insertion positions, the cross-entropy is exactly
\[
\sum_i p_i\log_2(1/q_i)=\mu H(q),
\]
because coordinate `i` is inserted once exactly on the event `i in Y`. The summed KL term is `mu I(L;T,K,P)` because `q` is the edge-law marginal of `L`. This proves (1.1). QED.

### Corollary 1.2 — exact side-information credit

Under the edge law let `T_*` denote the size-biased side variable. Then
\[
\mu I_2(L;T_*)
=\mathbb E_T\left[
\mu_T D_2(q^T\|q)
\right],
\tag{1.3}
\]
where `mu_T=E[K|T]` and `q^T_i=Pr(i in Y|T)/mu_T`. Hence
\[
H(Y\mid T)
\le H(K\mid T)+\mu H(q)-Q
-\mathbb E_T[\mu_TD_2(q^T\|q)].
\tag{1.4}
\]
This is a genuine one-time branch/profile rebate: no coordinate-name entropy is charged separately for each occurrence of the same side information.

## 2. Universal component-count collapse

Fix any partition `mathcal C` of the coordinate set. Let
\[
K_C=|Y\cap C|,\qquad
N=(K_C)_{C\in\mathcal C},\qquad
P_C=\sum_{i\in C}p_i,
\]
\[
E_C=P_C H((p_i/P_C)_{i\in C}),
\qquad
Q_C=\mathbb E\log_2(K_C!).
\]
Let `M_r` be the component containing `L_r`.

The account03/B12 factorial identity gives samplewise
\[
Q=\sum_CQ_C+Q_{\rm mac},
\qquad
Q_{\rm mac}=\mathbb E\log_2\frac{K!}{\prod_CK_C!}.
\tag{2.1}
\]

### Theorem 2.1 — conditional component-count inequality

For **every** joint law `(T,Y)` and every coordinate partition,
\[
\boxed{
H(Y\mid T)
\le H(N\mid T)+\sum_C(E_C-Q_C).
}
\tag{2.2}
\]

A sharper intermediate identity is
\[
\begin{aligned}
H(Y\mid T)
={}&H(K\mid T)+\mu H(M\mid T,K,P)-Q_{\rm mac}\\
&+\sum_C(E_C-Q_C)
-\mu I_2(L;T,K,P\mid M).
\end{aligned}
\tag{2.3}
\]

#### Proof

Decompose the edge-label entropy in (1.1) through `M=M(L)`. Since
\[
\mu H(L\mid M)=\sum_CE_C,
\]
mutual-information chain rules give (2.3).

Now compare the actual full-prefix predictor with the weaker predictor that sees only the previous component labels. Conditioning on the full coordinate prefix can only reduce the next-component entropy, so
\[
\mu H(M\mid T,K,P)
\le H(M_1,\ldots,M_K\mid T,K).
\tag{2.4}
\]
The macro sequence determines `N`. Conditional on `(N,T,K)`, uniform ordering makes `(M_1,...,M_K)` uniform over the multinomial interleavings, hence
\[
H(M_1,\ldots,M_K\mid T,K)
=H(N\mid T,K)+Q_{\rm mac}.
\tag{2.5}
\]
Insert (2.4)-(2.5) into (2.3), drop the final nonnegative mutual-information credit, and use that `K=sum_C K_C` is determined by `N`:
\[
H(K\mid T)+H(N\mid T,K)=H(N\mid T).
\]
This proves (2.2). QED.

**Interpretation.** After the exact internal factorial rebate is kept local, the entire remaining macro-address/interleaving problem is only the entropy of the occupancy-count vector. The multinomial interleaving entropy cancels against `Q_mac` automatically.

## 3. New bound on one fine closed component count

Now assume a reciprocal component `C` has size
\[
r=m+1\ge2,
\]
and satisfies the two already-proved compatible hypotheses from Section 0:
\[
\operatorname{TV}(\nu_i,U_{C\setminus\{i\}})\le\epsilon_i\le\frac1{16m},
\tag{3.1}
\]
\[
|2^{-m}-p_i|\le\frac1{16}p_i
\qquad(i\in C).
\tag{3.2}
\]
Put `N_C=|Y cap C|` and `P_C=E N_C`.

### Lemma 3.1 — size-biased component count

Let `N_C^*` have the size-biased law
\[
\Pr(N_C^*=k)=\frac{k\Pr(N_C=k)}{P_C},\qquad k\ge1.
\tag{3.3}
\]
Then
\[
\operatorname{TV}\!\left(
N_C^*,1+\operatorname{Bin}(m,1/2)
\right)
\le \bar\epsilon_C
:=\frac{1}{P_C}\sum_{i\in C}p_i\epsilon_i
\le\frac1{16m}.
\tag{3.4}
\]

#### Proof
Choose the distinguished included coordinate `i` with probability `p_i/P_C`, then sample `Y` under the Palm law conditional on `i in Y`. The resulting law of `N_C` is exactly size-biased, since a terminal set with `k` coordinates in `C` is counted once for each of those `k` coordinates. Under the ideal Palm law the count is `1+Bin(m,1/2)`. Convexity of total variation under the mixture gives (3.4). QED.

Let
\[
a_C:=\Pr(N_C>0).
\]
Since
\[
\frac{a_C}{P_C}=\mathbb E\frac1{N_C^*},
\]
and
\[
\mathbb E\frac1{1+\operatorname{Bin}(m,1/2)}
=\frac{2-2^{-m}}{m+1},
\]
(3.4), `m+1<=2m`, and `m>=1` imply
\[
\boxed{
\frac{11}{8r}P_C\le a_C\le\frac{17}{8r}P_C.
}
\tag{3.5}
\]
The physical scale relation (3.2) gives
\[
P_C\ge r\frac{16}{17}2^{-m},
\]
so from the lower half of (3.5),
\[
a_C\ge\frac{22}{17}2^{-m}>2^{-m}.
\tag{3.6}
\]
Hence
\[
\log_2(1/a_C)\le m.
\tag{3.7}
\]

### Theorem 3.2 — component-count entropy is influence-scale

\[
\boxed{
H(N_C)\le c_{\rm count}P_C,
\qquad
c_{\rm count}:=\frac{17}{16}(2+\log_2 e)
=3.6578634809445236\ldots .
}
\tag{3.8}
\]

#### Proof
Split on the event `N_C>0`:
\[
H(N_C)=h_2(a_C)+a_CH(N_C\mid N_C>0)
\le h_2(a_C)+a_C\log_2r.
\]
Use `h_2(a)<=a log2(e/a)`, (3.5), and (3.7):
\[
H(N_C)
\le\frac{17P_C}{8r}
\left(m+\log_2e+\log_2r\right).
\tag{3.9}
\]
For integer `m>=1`, the bracketed coefficient divided by `r=m+1` is maximized at `m=1`. Indeed the required comparison with the `m=1` value is equivalent to
\[
2\log_2(m+1)+\log_2e-2\le m\log_2e,
\]
whose right-minus-left derivative for real `m>=1` is
\[
\frac{1-2/(m+1)}{\ln2}\ge0
\]
and equality holds at `m=1`. This proves (3.8). QED.

For the exact ideal Palm law with `p_i=2^{-m}`, the ratio `H(N_C)/P_C` is much smaller: the diagnostic maximum through `m=200` is `2.517551362821715` at `m=5`. The proof uses the larger constant only to cover the allowed total-variation and density slack.

## 4. Closed fine-sector conditional Shannon theorem

Suppose the active coordinates of `Y` are partitioned entirely into reciprocal components satisfying (3.1)-(3.2). Then the account03/B12 local factorial theorem (0.1) gives
\[
\sum_C(E_C-Q_C)\le c_0\mu.
\tag{4.1}
\]
By subadditivity and Theorem 3.2,
\[
H(N\mid T)\le H(N)\le\sum_CH(N_C)
\le c_{\rm count}\mu.
\tag{4.2}
\]
Combining (2.2), (4.1), and (4.2):

### Theorem 4.1 — arbitrary-side-information robust code

\[
\boxed{
H(Y\mid T)
\le C_{\rm robust}\,\mathbb E|Y|,
}
\tag{4.3}
\]
where
\[
\boxed{
C_{\rm robust}
=c_0+c_{\rm count}
=6.605753562722450\ldots .
}
\tag{4.4}
\]

The side variable `T` is completely arbitrary. In particular, the result is stable under the branch-character side information in the current controlled-character spectral projection; no extra `H(T)` is hidden in (4.3).

### Partial-coverage form

If `R` is the union of the fine closed components and every coordinate outside `R` is left as a singleton block, then
\[
\boxed{
H(Y\mid T)
\le C_{\rm robust}\mu_R
+\sum_{i\notin R}h_2(p_i),
}
\tag{4.5}
\]
where `mu_R=sum_{i in R}p_i`. Thus the only ambient-address entropy left by this theorem is explicitly localized to the non-fine/nonclosed sector. No robust component macro-label term remains.

## 5. Application to the current controlled-character candidate

The preceding account01/B12 controlled-character transfer proves, after a physical reveal block `A` and branch character label `T`,
\[
H(f)\le B_A+H(T)+H(Y\mid T),
\tag{5.1}
\]
where `Y` is the survivor spectral projection of the global branch-gauged Boolean function. The compatible account04/B13 proxy-gauge theorem gives
\[
\mathbb E|Y|\le \mathcal D(f)
\tag{5.2}
\]
for its source-frontier residual.

Therefore, on the branch where the residual active coordinates are covered by the fine closed components above,
\[
\boxed{
H(f)\le B_A+H(T)+6.605753562722450\,\mathcal D(f).
}
\tag{5.3}
\]
Using the already-completed physical label payment at the current source-frontier scale,
\[
H(T)\le\frac{17}{8}J+\frac{15}{14}\mathcal P_{\rm ext},
\]
this becomes
\[
\boxed{
H(f)
\le B_A+rac{17}{8}J+rac{15}{14}\mathcal P_{\rm ext}
+6.605753562722450\,\mathcal D(f)
}
\tag{5.4}
\]
in that exact fine-closed residual sector.

This is the promised conditional-Shannon increment bound: the previous unresolved `H(Y|T)` is now fully influence-scale on the fine closed Palm/physical sector, and the macro interleaving/address entropy is gone rather than merely estimated.

## 6. What remains open

This does **not** prove full FEI. The unresolved universal work is now concentrated in:

1. **non-fine / nonclosed residual rows:** in (4.5) they appear explicitly as `sum h_2(p_i)`; a small total mass is not enough by itself to pay this entropy;
2. **scale-escape components:** the fixed-`1/16` robust DAG can leave the fine `1/(16m)` regime, so the new count theorem cannot simply be iterated across every robust row;
3. **parent block-erasure cost `B_A` and the remaining external/defect ledgers:** (5.4) is a branch theorem, not the final global FEI closure.

A useful next target is therefore not another macro predictor. It is a **fine-or-escape decomposition for the count vector**: show that components failing (3.1) can be charged once to the existing scale-escape / hypercontractive exception flow, while the fine components are removed by (4.3). That would eliminate the last `sum h_2(p_i)` address term without reintroducing pairwise overcount.

**Full unrestricted FEI remains OPEN / NOT PROVED.**
