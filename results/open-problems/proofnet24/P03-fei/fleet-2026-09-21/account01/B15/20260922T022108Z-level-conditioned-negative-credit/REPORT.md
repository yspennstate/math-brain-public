# account01/B15 — the missing negative label credit is an exact size-conditioned mutual information

**Classification:** `ESSENTIAL_STEP_APPLIED` to the Shannon/coding mechanism; the unconditioned ordered-label closure is `CANDIDATE_REFUTED`. **Full uniform-cube FEI remains OPEN / NOT PROVED.**

## 0. Source binding and compact conditional argument

This run uses the current all-gate / balanced-excess state, in particular:

1. `account01/B18/20260922T002302Z-gate-refutation-balanced-excess/REPORT.md`, blob `8b4821459619603f126bbc6d947c7028739e0368`, which proves for every finite `C`
   \[
   H(f)\le CI(f)\ \forall f
   \iff
   H(g)\le C\,[I(g)-1]\ \forall\text{ balanced Boolean }g.
   \tag{0.1}
   \]
   Thus, for the spectral sample `S` of balanced `g`, the exact full target is
   \[
   H(S)\le C\,\mathbb E(|S|-1).
   \tag{0.2}
   \]

2. `account03/B12/20260921T104520Z-spectral-compression/REPORT.md`, blob `065a0f4e1a635664169a815a3512dbfa7536597b`, which proves the ordered-set code
   \[
   H(S)\le U(S):=H(K)+I H(q)-\mathbb E\log_2(K!),
   \tag{0.3}
   \]
   where `K=|S|`, `I=E K`, `p_i=P(i in S)` and `q_i=p_i/I`.

Combining (0.1) with (0.3) exposes the natural stronger missing implication
\[
U(S)\le C\,\mathbb E(K-1)
\quad\text{for balanced Boolean spectra.}
\tag{0.4}
\]
I first refute (0.4) for every finite `C`, then identify the exact negative entropy term omitted by the global-label code and prove the corrected coding inequality.

The latest shared-graft lower-bound work (including `account03/B18/20260922T014034Z-shared-graft-tail/REPORT.md`, blob `e8ef3647b38fbe4301b657defe38829e2a3521a5`) is compatible with this statement but is not needed in the proof below; no scalar center is frozen here.

## 1. Level-conditioned ordered coding

Let `S` be any random subset of `[n]`. Put
\[
K=|S|,\qquad P_k=\Pr(K=k).
\]
For every `k>=1` with `P_k>0`, define
\[
q_i^{(k)}:=\frac{\Pr(i\in S\mid K=k)}{k}.
\tag{1.1}
\]
Because \(\sum_i\Pr(i\in S\mid K=k)=k\), `q^(k)` is a probability distribution on coordinates.

### Theorem 1.1 — size-conditioned ordered code

For every random subset law,
\[
\boxed{
H(S)\le U_{\rm lev}(S)
:=H(K)+\sum_{k\ge1}P_k\left[kH(q^{(k)})-\log_2(k!)\right].
}
\tag{1.2}
\]

### Proof

Condition on `K=k`. After sampling `S`, order its `k` elements uniformly at random as `(J_1,...,J_k)`. The ordering contributes exactly `log_2(k!)` conditional bits, and the ordered tuple determines `S`, hence
\[
H(S\mid K=k)+\log_2(k!)
=H(J_1,\ldots,J_k\mid K=k).
\tag{1.3}
\]
Each position `J_r` has marginal `q^(k)`. Encode the ordered tuple by the product model `(q^(k))^{\otimes k}`. Cross entropy dominates entropy, so
\[
H(J_1,\ldots,J_k\mid K=k)\le kH(q^{(k)}).
\tag{1.4}
\]
Combine (1.3)-(1.4), average over `k`, and add `H(K)`. \(\square\)

This is a strict strengthening of the global ordered code whenever the coordinate profile changes with the spectral level.

## 2. Exact negative entropy credit

Let
\[
p_i=\Pr(i\in S),\qquad I=\mathbb E K,\qquad q_i=p_i/I.
\]
Define a size-biased level variable `K*` and a coordinate mark `J` by
\[
\Pr(K^*=k,J=i)=\frac{\Pr(K=k,\ i\in S)}{I}.
\tag{2.1}
\]
Then
\[
\Pr(K^*=k)=\frac{kP_k}{I},\qquad
\Pr(J=i\mid K^*=k)=q_i^{(k)},\qquad
\Pr(J=i)=q_i.
\tag{2.2}
\]
Consequently
\[
I H(q)-\sum_k kP_k H(q^{(k)})
=I\,I(K^*;J).
\tag{2.3}
\]
Subtracting (1.2) from the old functional (0.3) gives the exact identity
\[
\boxed{
U_{\rm lev}(S)
=U(S)-I\,I(K^*;J).
}
\tag{2.4}
\]

Thus the missing term is not a heuristic refund: it is a genuine **negative mutual-information credit**. The global-label code loses exactly the information that spectral level `K*` carries about which coordinate occurrence is being transmitted.

This is the requested sign: the correction is always nonnegative and enters with a minus sign.

## 3. A balanced Boolean family where the old loss diverges

For `m>=2`, let `h_m:{-1,1}^m->{-1,1}` be the one-point defect
\[
h_m(x)=1\quad\text{except at one point, where }h_m=-1.
\]
Put
\[
a:=2^{1-m}.
\tag{3.1}
\]
Its Fourier magnitudes are
\[
|\widehat h_m(\varnothing)|=1-a,
\qquad
|\widehat h_m(T)|=a\quad(T\ne\varnothing).
\tag{3.2}
\]
Now adjoin a fresh unbiased coordinate `y` and define
\[
g_m(y,x)=y\,h_m(x).
\tag{3.3}
\]
Then `g_m` is balanced Boolean. Its spectral sample always contains `y`; explicitly
\[
\Pr(S=\{y\})=(1-a)^2,
\qquad
\Pr(S=\{y\}\cup T)=a^2\quad(\varnothing\ne T\subseteq[m]).
\tag{3.4}
\]
The excess influence is
\[
\boxed{\delta_m:=I(g_m)-1=ma.}
\tag{3.5}
\]
The true entropy obeys
\[
\frac{H(g_m)}{\delta_m}\longrightarrow4.
\tag{3.6}
\]
Indeed the nontrivial spectral mass is `2a-a^2` and every nontrivial atom has surprisal `2(m-1)` bits, while the singleton atom contributes `o(ma)`.

### Proposition 3.1 — the unconditioned ordered code is infinitely too expensive

For the family (3.3),
\[
\boxed{
\frac{U(g_m)}{I(g_m)-1}\to\infty.
}
\tag{3.7}
\]
More precisely,
\[
\frac{U(g_m)}{\delta_m}
=m-\log_2m+O(1).
\tag{3.8}
\]

### Proof

The coordinate influences are
\[
p_y=1,\qquad p_i=a\ (1\le i\le m),\qquad I=1+ma.
\tag{3.9}
\]
Hence
\[
I H(q)=I\log_2 I+ma\log_2(1/a)
=I\log_2 I+ma(m-1).
\tag{3.10}
\]
Also `H(K)=O(am)` and, conditional on `K>1`, `K-1` is asymptotically `Bin(m,1/2)`, so Stirling gives
\[
\frac{\mathbb E\log_2(K!)}{ma}=\log_2m+O(1).
\tag{3.11}
\]
Divide (0.3) by `ma`; (3.10) contributes `m+O(1)` and (3.11) removes only `log_2m+O(1)`. This proves (3.8), hence (3.7). \(\square\)

Therefore no finite FEI proof can be obtained by combining balanced-excess equivalence directly with the global-label ordered functional `U`. This is a genuine Boolean obstruction, not a non-Boolean relaxation.

## 4. The negative credit cancels the whole divergent loss

For the same family, conditional on `K=r+1` with `r>=1`, the set of the `r` non-root coordinates is uniform among the `r`-subsets of `[m]`. Therefore
\[
q_y^{(r+1)}=\frac1{r+1},
\qquad
q_i^{(r+1)}=\frac{r}{m(r+1)}.
\tag{4.1}
\]
A direct calculation gives
\[
(r+1)H(q^{(r+1)})-\log_2((r+1)!)
=r\log_2\frac{m(r+1)}r-\log_2(r!).
\tag{4.2}
\]
Subtracting the actual conditional entropy `log_2 binom(m,r)`, the level-code excess is
\[
d_{m,r}
=r\log_2\frac{m(r+1)}r
-\log_2\frac{m!}{(m-r)!}\ge0.
\tag{4.3}
\]
For `R~Bin(m,1/2)`, Stirling plus concentration gives
\[
\frac{2}{m}\,\mathbb E[d_{m,R}]
\longrightarrow \log_2 e-1.
\tag{4.4}
\]
The `R=0` conditioning error is exponentially negligible. Since the nontrivial spectral mass is `2a-a^2`, equations (3.6) and (4.4) yield
\[
\boxed{
\frac{U_{\rm lev}(g_m)}{I(g_m)-1}
\longrightarrow
4+(\log_2 e-1)
=3+\log_2 e
=4.442695040888963\ldots .
}
\tag{4.5}
\]

Combining (2.4), (3.8), and (4.5),
\[
\boxed{
\frac{I(g_m)\,I(K^*;J)}{I(g_m)-1}
=m-\log_2m+O(1).
}
\tag{4.6}
\]
So the newly exposed negative mutual-information term has exactly the same divergent scale as the old candidate's largest loss. It is not a lower-order cosmetic correction.

## 5. A useful anchor identity

The same correction behaves cleanly under the standard balancing lift. Let `f` be any Boolean function with spectral size `K`, and let `g(y,x)=y f(x)`. Then the spectral size of `g` is `K+1`. Applying (1.2) level by level gives the exact identity
\[
\boxed{
U_{\rm lev}(y f)
=U_{\rm lev}(f)
+\mathbb E\left[K\log_2\left(1+\frac1K\right)\mathbf 1_{K>0}\right].
}
\tag{5.1}
\]
In particular,
\[
U_{\rm lev}(y f)
\le U_{\rm lev}(f)+(\log_2 e)\Pr(K>0)
\le U_{\rm lev}(f)+(\log_2 e)I(f).
\tag{5.2}
\]
This shows that the corrected code respects the exact balancing operation behind (0.1) with only an `O(I)` charge; the unconditioned code does not.

## 6. What is and is not proved

**Old missing implication:** use the ordered spectral code directly to pay the balanced-excess target, i.e. establish `U<=C(I-1)` with finite dimension-independent `C`.

**Exact failed claim:** that implication is false for every finite `C`, by (3.7).

**New proved inference:** the correct size-conditioned code is (1.2), and the improvement over the old code is exactly the negative term `I I(K*;J)`. On the balanced sparse-defect obstruction, this term cancels the entire divergent `m-log m` label loss and leaves the finite limit `3+log_2 e`.

**New missing implication:** determine whether the genuinely corrected residual
\[
U_{\rm lev}(S)
\tag{6.1}
\]
can be bounded by `C E(K-1)` for Boolean balanced spectra, or identify the next Boolean counterfamily. Nothing here proves that such a finite `C` exists. In particular, (1.2) is a stronger coding upper bound on `H`, not FEI itself.

The new correction should be retained in any Shannon/code continuation: discarding `I(K*;J)` recreates an artificial divergence already disproved by the explicit family (3.3).

## 7. Outcome

**`ESSENTIAL_STEP_APPLIED`** to the requested negative-entropy accounting, together with **`CANDIDATE_REFUTED`** for the unconditioned ordered-label closure. Full FEI remains **OPEN**.
