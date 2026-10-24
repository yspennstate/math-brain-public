# B12 FEI creative attempt: one-companion Palm channel and nonreuse factorial payment

**Status:** **PARTIAL. Full uniform-cube Friedgut–Kalai Fourier entropy–influence remains OPEN / NOT PROVED.**  
**Route:** APPROACH 1, spectral-sample compression / sequential prediction.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated mathematical-brain retrieval or receiver context was used.  
**Claim level:** analytic partial theorems and targeted exact checks; no novelty or publication-priority claim.

This run did not audit the read-once certificate or repeat a settled FEI enumeration. It read the required current FEI packet first and then consumed two completed cross-account interfaces:

1. `account03/B12/20260921T194351Z-curvature-palm-nonreuse/REPORT.md` (blob `ddf8baf96385418c56a91c48f62c04168633faaa`), which identifies the exact Palm insertion law and shows that raw derivative depth cannot be paid linearly by sequential information; and
2. the newer `account04/B12/20260921T201418Z-palm-trigger-cluster/REPORT.md` (blob `4643e5dd27cc48a508820a30413e24b9c4717fac`), which proves that sufficiently Palm-robust rows have exact reciprocal trigger blocks and factor-7 scale escapes.

The pair-refund input from `account04/B14/20260921T184113Z-posterior-crossing-budget/REPORT.md` (blob `c974b249c6cc513019bd0e58e7711ad808c80844`) is also used in Section 5.

The point of this run is to replace repeated pair evidence by a **single genuine companion symbol** sampled from the actual Palm prefix. The resulting flow has total mass only `I-V`, never a factorial second moment. It therefore gives an exact nonreuse bridge from the cluster/crossing geometry into the factorial rebate already present in the sequential code.

## 1. Setup: the inherited Palm insertion code

Let

\[
\mu(A)=\widehat f(A)^2,\qquad S\sim\mu,\qquad K=|S|,
\qquad I=\mathbb E K,
\]

and put

\[
p_i=\Pr(i\in S),\qquad V=\Pr(K>0)=1-\widehat f(\varnothing)^2.
\]

The account03/B12 insertion construction gives a normalized edge law on an inserted label `L` and predecessor prefix `P` for which

\[
D_{\rm seq}=I\,I_2(L;P)
\tag{1.1}
\]

and

\[
H(S)\le H(K)+I H(\pi)-\mathbb E\log_2(K!)-D_{\rm seq},
\qquad \pi_i=p_i/I.
\tag{1.2}
\]

A useful exact generative description of that same edge law is:

- draw the terminal set `S` from the size-biased law `K\mu(S)/I`;
- draw `L` uniformly from `S`;
- draw the position of `L` uniformly in `{1,...,K}`;
- conditional on the number `a` of predecessors, draw `P` uniformly among the `a`-subsets of `S\setminus{L}`.

This is just a probabilistic rewriting of the inherited edge weights.

## 2. PROVED: the one-companion channel

Define a randomized statistic `C` of the actual prefix `P`:

- if `P` is empty, set `C=\bot`;
- otherwise choose `C` uniformly from `P`.

Also define

\[
u_i:=\mathbb E\frac{1_{\{i\in S\}}}{K},
\qquad
r_{ij}:=\mathbb E\frac{1_{\{i,j\in S\}}}{K}\quad(i\ne j),
\tag{2.1}
\]

with the integrand taken as zero when `K=0`.

### Lemma 2.1 — exact joint law

Conditional on `(S,L)` with `|S|=K`, `C` is uniform on the `K` symbols

\[
\{\bot\}\cup(S\setminus\{L\}).
\tag{2.2}
\]

Consequently

\[
\boxed{\Pr(L=i,C=\bot)=u_i/I,}
\qquad
\boxed{\Pr(L=i,C=j)=r_{ij}/I\quad(i\ne j).}
\tag{2.3}
\]

The marginals are

\[
\Pr(L=i)=p_i/I,
\qquad
\Pr(C=\bot)=V/I,
\qquad
\Pr(C=j)=(p_j-u_j)/I.
\tag{2.4}
\]

### Proof

For fixed `(S,L)`, the empty prefix occurs with probability `1/K`. For a fixed `j in S\setminus{L}`, condition on prefix size `a>=1`. The probability that `j` is in the random `a`-prefix is `a/(K-1)`, and then the probability that the uniform companion choice selects `j` is `1/a`. Each `a=1,...,K-1` therefore contributes `1/[K(K-1)]`; summing over `a` gives `1/K`. This proves (2.2), and averaging under the size-biased terminal-set law gives (2.3)-(2.4). QED.

Since `C` is obtained from `P` by a label-independent randomized channel, data processing gives a new explicit sequential-code rebate

\[
\boxed{D_{\rm seq}\ge D_{\rm comp}:=I\,I_2(L;C).}
\tag{2.5}
\]

Written only in spectral quantities,

\[
\boxed{
D_{\rm comp}
=\sum_i u_i\log_2\frac{Iu_i}{p_iV}
 +\sum_{i\ne j}r_{ij}\log_2
 \frac{I r_{ij}}{p_i(p_j-u_j)}.
}
\tag{2.6}
\]

The usual `0 log 0=0` convention applies. Equivalently,

\[
I H(\pi)-D_{\rm comp}
=V H(u/V)
+\sum_j(p_j-u_j)
 H\!\left(\frac{(r_{ij})_{i\ne j}}{p_j-u_j}\right).
\tag{2.7}
\]

Thus the diffuse global influence-profile code has been replaced by one **reversible killed companion channel**: `r_ij=r_ji`, a null/killing mass `u_i`, and row sum

\[
\boxed{u_i+\sum_{j\ne i}r_{ij}=p_i.}
\tag{2.8}
\]

This is the intended cluster-safe observable. A latent cluster can contribute only through one companion symbol at a time, so the selector-of-parities overcount that killed the all-pairs KL sum cannot occur here.

## 3. PROVED: the total companion flow is automatically influence-scale

Summing (2.1) gives the exact identities

\[
\boxed{\sum_i u_i=V,}
\qquad
\boxed{\sum_{i\ne j}r_{ij}=I-V.}
\tag{3.1}
\]

Indeed every nonempty terminal set of size `K` contributes `K/K=1` to the first sum and `K(K-1)/K=K-1` to the second.

Also, for integer `K>=1`,

\[
\log_2(K!)\ge K-1,
\]

so

\[
\boxed{
\mathbb E\log_2(K!)\ge I-V=\sum_{i\ne j}r_{ij}.
}
\tag{3.2}
\]

This is the first clean resolution of the raw-depth congestion problem in this route: the physical pair bank `sum q_ij` can be of factorial-moment size, but the companion bank `sum r_ij` is **always at most first-moment size** and is already paid by the exact factorial rebate in (1.2).

## 4. PROVED: Palm-robust trigger rows spend a constant fraction of their influence in the companion flow

Use the account04/B12 notion of an `epsilon`-Palm-robust row. Conditional on `i in S`, let

\[
B=S\setminus\{i\},
\qquad
\nu_i=\operatorname{Law}(B\mid i\in S),
\]

and suppose

\[
\operatorname{TV}(\nu_i,U_{F_i})\le\epsilon,
\tag{4.1}
\]

where `U_F` is uniform on all subsets of the trigger set `F_i`, and `m_i=|F_i|>=1`.

From (2.1),

\[
\frac{u_i}{p_i}=\mathbb E_{\nu_i}\frac1{1+|B|},
\qquad
\frac1{p_i}\sum_{k\in F_i}r_{ik}
=\mathbb E_{\nu_i}\frac{|B\cap F_i|}{1+|B|}.
\tag{4.2}
\]

For `B` uniform on subsets of an `m`-set,

\[
 a_m:=\mathbb E\frac1{1+|B|}
 =\frac{2-2^{-m}}{m+1}.
\tag{4.3}
\]

Both functions in (4.2) take values in `[0,1]`, so total variation changes their expectations by at most `epsilon`. Under the uniform law the second expectation equals `1-a_m`. Hence

\[
\boxed{
\left|\frac{u_i}{p_i}-a_{m_i}\right|\le\epsilon,
}
\tag{4.4}
\]

and

\[
\boxed{
\sum_{k\in F_i}r_{ik}
\ge p_i(1-a_{m_i}-\epsilon).
}
\tag{4.5}
\]

Since `a_m<=3/4` for every `m>=1`,

\[
\boxed{
\sum_{k\in F_i}r_{ik}\ge(1/4-\epsilon)p_i.
}
\tag{4.6}
\]

At the account04 threshold `epsilon<=1/16`, this is

\[
\boxed{\sum_{k\in F_i}r_{ik}\ge\frac3{16}p_i.}
\tag{4.7}
\]

Summing over any collection `R` of such nontrivial robust rows and using (3.1)-(3.2),

\[
\boxed{
\frac3{16}\sum_{i\in R}p_i
\le I-V
\le\mathbb E\log_2(K!).
}
\tag{4.8}
\]

There is no pairwise double counting hidden here: the left side is injected into the actual oriented companion-flow mass, whose entire global mass is exactly `I-V`.

This is directly compatible with the newest account04/B12 trigger-cluster theorem. Reciprocal robust rows may be contracted to their common trigger signature; nonreciprocal robust triggers are factor-7 scale escapes. Equation (4.8) says that **before any finer component accounting**, every nontrivial robust row already has a constant influence fraction routed through a real, globally nonreusable companion flow.

## 5. PROVED: physical crossing refunds force a quadratic factorial rebate

Let

\[
q_{ij}=\Pr(i,j\in S).
\]

For every pair, Cauchy–Schwarz gives

\[
q_{ij}^2
=\left(\mathbb E\left[1_{\{i,j\in S\}}K^{-1/2}K^{1/2}\right]\right)^2
\le r_{ij}\,\mathbb E[K1_{\{i,j\in S\}}]
\le I r_{ij}.
\tag{5.1}
\]

Therefore

\[
\boxed{r_{ij}\ge q_{ij}^2/I.}
\tag{5.2}
\]

Summing over unordered pairs and using (3.1),

\[
\boxed{
I-V\ge\frac2I\sum_{i<j}q_{ij}^2.
}
\tag{5.3}
\]

Now specialize to the centered restriction-critical core from account04/B14 and the preceding account01/B12 crossing-to-Palm bridge. Put

\[
R=H/I,\qquad
D=\sum_i\Psi(p_i)-RI,
\qquad
A_{ij}:=[\Psi(p_i)+\Psi(p_j)-D]_+.
\]

The physical pair-refund theorem plus the exact two-face identity give

\[
q_{ij}\ge A_{ij}/(4R).
\tag{5.4}
\]

Substitution into (5.3) and then (3.2) yields the new nonreuse factorial payment

\[
\boxed{
\mathbb E\log_2(K!)
\ge I-V
\ge
\frac{1}{8R^2 I}
\sum_{i<j} A_{ij}^2.
}
\tag{5.5}
\]

This is complementary to the previous **linear** crossing-to-Palm KL rebate. If many pair refunds repeat the same latent cluster information and therefore cannot be added as KL terms, their squared mass still has only one place to go: multi-element spectral sets, and those sets create an actual factorial rebate.

## 6. Combined critical-core compression inequality

Let

\[
D_{\rm cross}
=\sum_i p_i\log_2\frac1{1-b_i},
\qquad
b_i=\frac1{8RI}\sum_{j\ne i}A_{ij},
\]

be the already-proved crossing-to-Palm self-witness rebate from the preceding account01/B12 report. Since `D_seq` is at least both `D_comp` and `D_cross`, while the factorial term is at least both lower bounds in (4.8) and (5.5), the inherited code (1.2) gives the safe strengthened bound

\[
\boxed{
\begin{aligned}
H(S)\le{}&H(K)+I H(\pi)
-\max\{D_{\rm comp},D_{\rm cross}\}\\
&-\max\left\{
 \frac3{16}\sum_{i\in R}p_i,
 \frac{1}{8R^2 I}\sum_{i<j}A_{ij}^2
 \right\}.
\end{aligned}
}
\tag{6.1}
\]

Here `R` in the set sum denotes any collection of `epsilon<=1/16` Palm-robust rows with nonempty trigger sets; it is unrelated to the ratio `R=H/I` except by notation, so in subsequent work the robust-row set should be renamed to avoid this collision.

Equation (6.1) is not FEI closure. It is a three-way nonreuse ledger:

1. **predictable/heterogeneous branch:** paid by actual companion mutual information;
2. **crossing branch:** paid by the previous self-witness KL or by the new quadratic factorial term;
3. **Palm-robust cluster branch:** a constant influence fraction is already routed into the first-moment companion/factorial bank, while account04/B12 supplies the exact reciprocal blocks and scale-separated quotient DAG needed for the remaining codimension/address charge.

## 7. Targeted exact checks

`check_companion_factorial.py` uses integer Walsh transforms and exact `Fraction` arithmetic for every algebraic identity. It tests four deliberately different hard families rather than repeating a settled exhaustive FEI sweep:

| family | `I` | `I-V` | `E log2(K!)` | `D_comp` | `D_seq` | `2 sum q_ij^2/I` |
|---|---:|---:|---:|---:|---:|---:|
| parity, `n=8` | 8 | 7 | 15.2992080184 | 1.3485155456 | 8.7007919816 | 7 |
| majority, `n=7` | 2.1875 | 1.1875 | 2.1210882441 | 0.2640910003 | 1.0393339181 | 0.46875 |
| one-point defect, `n=7` | 0.109375 | 0.078369140625 | 0.1210288714 | 0.01742870294 | 0.04373306542 | 0.0234375 |
| selector of two 3-parities | 3.5 | 2.5 | 3.5849625007 | 2.8723481718 | 4.6919847858 | 1.0714285714 |

All exact companion-flow identities passed, the generated companion joint law matched `(u,r)` exactly, `D_comp<=D_seq` held in every case, and both inequalities in

\[
\mathbb E\log_2(K!)\ge I-V\ge 2\sum_{i<j}q_{ij}^2/I
\]

held. The selector-of-parities family is especially useful: the earlier all-pairs KL sum overcounted its repeated latent cluster bit, whereas the one-companion channel remains a single honest data-processing statistic.

These finite checks validate implementation and boundary cases only; the analytic statements above carry the proof.

## 8. Exact remaining implication

The surviving obstruction is now narrower. In the account04/B12 robust sector, reciprocal trigger components have one exact common signature and cross-component robust edges jump by factor at least seven. The companion theorem shows that every nontrivial robust row sends at least `3/16` of its influence into one globally first-moment flow, but that by itself pays only an activation-scale cost, not the full rare-coordinate `p_i log(1/p_i)` address cost.

The next attack should therefore use a **hierarchical block-valued statistic of the actual prefix**, not another pair sum: contract each reciprocal trigger component, expose only the first companion/trigger block hit, recurse inside the selected block, and retain the exact factorial rebate at every contraction. The factor-7 quotient DAG prevents a label from escaping through comparable scales indefinitely. What remains to prove is that the accumulated block-address entropy is `O(I)` after the exact zero-defect components from the new B13 peeling result are removed.

That is a genuine remaining theorem. It is not proved here, and full FEI remains **OPEN**.
