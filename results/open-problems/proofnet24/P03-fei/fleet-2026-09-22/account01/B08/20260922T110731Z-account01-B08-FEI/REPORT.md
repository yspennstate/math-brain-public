# account01/B08 — multiscale signed-shift partition certificate

**Run:** `20260922T110731Z-account01-B08-FEI`  
**Classification:** `ESSENTIAL_STEP_APPLIED / LOG_WEIGHTED_MULTISHIFT_CERTIFICATE`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Active assignment and source pins

Fresh owner control revision `2026-09-22.3` supersedes the stale MOC4 prompt: all existing workers are now on FEI. The active account01/B08 task is to construct a logarithmically weighted multi-shift Booleanity statistic bounded above by the exact occurrence I-projection credit `K_occ`, while retaining the sparse-suspension logarithm and respecting the recursive-majority low-level barrier.

The exact source premises used here are:

1. **I-projection identity:** `yspennstate/math-open-problems@4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`. It proves
   \[
   K_{\rm occ}=D_{\rm KL,2}(P\Vert Q_r)=H_{\max}(r)-H(P),
   \qquad R_\Gamma=B_{\inf}^\Gamma+K_{\rm occ}.
   \]
2. **Sparse-suspension obstruction:** `yspennstate/math-open-problems@7ec649dfb3d1ab2f92855f2069590fca2ac956dd`, `proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T093820Z-full-convolution-energy-obstruction/REPORT.md`. On the genuine sparse suspension, the full unweighted convolution-L2 bank is only `Theta(I)` while `K_occ=Theta(mI)`; any viable compression must lose at most `O(I)` there.
3. **Recursive-majority barrier:** `yspennstate/math-open-problems@bff0d7b6c21485f386841c42582eb04f32705046`, `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T100641Z-lowlevel-projection-barrier/REPORT.md`. Fixed/low labelled Fourier levels followed by one merged tail cannot be the universal payment mechanism.
4. **Named OTHER-account result consumed:** account02/B08, `yspennstate/math-open-problems@a83d4009cc98aeb739af4f40b1c2cfa8be7269d0`, `proofnet24/P03-fei/fleet-2026-09-22/account02/B08/B08-20260922T103745Z-0f440e/REPORT.md`. It proves one oriented signed-shift event gives a binary-KL certificate and recovers exactly one half of the leading sparse rare-event logarithm.

The new result below replaces the single binary event by one **multi-cell variational partition fed by many signed shift constraints**. On the same sparse family it recovers `K_occ` up to an additive `O(I)` loss, in fact with exact asymptotic loss `I/ln 2`.

## 1. General multi-cell signed-shift certificate

Let `g:{-1,1}^m->{-1,1}` have uniform Walsh coefficients `a_S`, squared spectral law
\[
P(S)=a_S^2,
\]
and let `Q` be any full-support reference law on `2^[m]`.

For a nonempty shift `U`, write `tau_U(S)=S triangle U`. Booleanity `g^2=1` gives the exact signed convolution identity
\[
\sum_S a_S a_{\tau_U S}=0.
\tag{1.1}
\]
Since `tau_U` has no fixed point, its orbits are unordered pairs.

Choose pairwise disjoint events `H_1,...,H_J`. For each `j`, choose a nonempty shift `U_j` and a collection `E_j` of `tau_{U_j}`-orbits such that `H_j` contains exactly one endpoint of every orbit in `E_j`; put
\[
H_j'=\tau_{U_j}(H_j),
\]
so `H_j` and `H_j'` are disjoint. Let `D_j` be the complementary collection of `tau_{U_j}`-orbits and define
\[
\Delta_j:=\left|\sum_{\{S,\tau_{U_j}S\}\in D_j} a_Sa_{\tau_{U_j}S}\right|.
\tag{1.2}
\]
By (1.1), the same absolute value is obtained by summing over `E_j`. Hence Cauchy--Schwarz gives
\[
\Delta_j^2
\le P(H_j)P(H_j').
\tag{1.3}
\]
Define the source-valid lower mass
\[
\ell_j:=
\begin{cases}
\Delta_j^2/P(H_j'),&P(H_j')>0,\\
0,&P(H_j')=0.
\end{cases}
\tag{1.4}
\]
Then always
\[
0\le \ell_j\le P(H_j).
\tag{1.5}
\]

Write `q_j=Q(H_j)` and `q_0=1-sum_j q_j`. For arbitrary nonnegative weights `t_j>=0`, the bounded Donsker--Varadhan test
\[
T(S)=\sum_j t_j 1_{H_j}(S)
\]
uses disjointness to give
\[
D_2(P\Vert Q)
\ge \sum_j t_j P(H_j)
 -\log_2\left(q_0+\sum_jq_j2^{t_j}\right).
\tag{1.6}
\]
Because every `t_j` is nonnegative, (1.5) yields the fully source-valid statistic
\[
\boxed{
\mathfrak B(P,Q;a,\mathcal H,\mathcal U)
:=\sup_{t_j\ge0}
\left\{
\sum_jt_j\ell_j
-\log_2\left(q_0+\sum_jq_j2^{t_j}\right)
\right\}
\le D_2(P\Vert Q).
}
\tag{1.7}
\]

This is a genuine nonlinear/logarithmically weighted Booleanity certificate. It combines all cells through **one** data-processing/variational inequality, so no KL credit is double spent. The signed Boolean equations enter only through the simultaneous lower bounds `ell_j`; the logarithmic weights are dictated by the actual reference masses `q_j`.

If `Q=Q_r` is the exact occurrence I-projection, (1.7) becomes
\[
\boxed{\mathfrak B\le K_{\rm occ}.}
\tag{1.8}
\]

## 2. Exact sparse-suspension specialization

Consume the genuine Boolean family from account04/B15. For `m>=4`, put
\[
p=2^{1-m},
\qquad
g_m(x)=1-2\mathbf 1_{\{x=0\}}.
\tag{2.1}
\]
Its Walsh coefficients are
\[
a_\varnothing=1-p,
\qquad a_S=-p\quad(S\ne\varnothing),
\tag{2.2}
\]
and the old-coordinate I-projection is
\[
Q_m(S)=p^{|S|}(1-p)^{m-|S|}.
\tag{2.3}
\]
The suspension has `I=m p` beyond its fresh dictator coordinate, and the exact source asymptotic is
\[
{K_{\rm occ}\over mp}=m-5+{1\over\ln2}+o(1).
\tag{2.4}
\]

For each `k=3,...,m`, let
\[
L_k:=\{S:|S|=k\}.
\]
Choose a distinct singleton shift
\[
U_k=\{k-2\},
\qquad \tau_k(S)=S\triangle U_k.
\tag{2.5}
\]
A singleton flip changes cardinality by exactly one, hence no `tau_k`-orbit contains two points of `L_k`. Let `E_k` be precisely the orbits having one endpoint in `L_k`, oriented so that
\[
H_k=L_k.
\]
There are
\[
N_k={m\choose k}
\]
such orbits. Because `k>=3`, neither endpoint of any selected orbit is empty; by (2.2) every selected orbit product equals `p^2`. Therefore the complementary-orbit sum forced by (1.1) has magnitude
\[
\Delta_k=N_kp^2.
\tag{2.6}
\]
Moreover `tau_k(L_k)` also consists of `N_k` nonempty atoms, each of squared mass `p^2`, so
\[
P(\tau_kL_k)=N_kp^2.
\tag{2.7}
\]
Hence the signed-shift Cauchy certificate is exact on every retained level:
\[
\boxed{
\ell_k={\Delta_k^2\over P(\tau_kL_k)}
=N_kp^2=P(L_k),
\qquad 3\le k\le m.
}
\tag{2.8}
\]

Thus the many Boolean shift equations recover the exact physical masses of all levels `k>=3` without separately spending KL.

## 3. Reference-log weights and closed-form certificate

For `k>=3`, set
\[
t_k=(k-2)\log_2{1-p\over p}\ge0.
\tag{3.1}
\]
These are exactly reference log-likelihood increments relative to cardinality two. Since
\[
q_k:=Q_m(L_k)={m\choose k}p^k(1-p)^{m-k},
\tag{3.2}
\]
we have
\[
q_k2^{t_k}
={m\choose k}p^2(1-p)^{m-2}.
\tag{3.3}
\]
Let the residual cell be all levels `0,1,2`. Substituting the exact masses (2.8) and weights (3.1) into (1.7) gives the explicit lower certificate
\[
\mathcal C_m
:=p^2\log_2{1-p\over p}
\sum_{k=3}^m {m\choose k}(k-2)
-\log_2 Z_m,
\tag{3.4}
\]
where
\[
Z_m=Q_m(|S|\le2)+\sum_{k=3}^m q_k2^{t_k}.
\tag{3.5}
\]
Two elementary binomial identities give
\[
\sum_{k=3}^m {m\choose k}(k-2)
=2^{m-1}(m-4)+m+2,
\tag{3.6}
\]
and, using `2^m p=2`,
\[
\boxed{
Z_m=(1-p)^{m-2}\bigl(1+mp(1-2p)\bigr).
}
\tag{3.7}
\]
Therefore
\[
\boxed{
\begin{aligned}
\mathcal C_m={}&
 p^2\bigl(2^{m-1}(m-4)+m+2\bigr)
 \log_2{1-p\over p}\\
&-(m-2)\log_2(1-p)
-\log_2\bigl(1+mp(1-2p)\bigr),
\end{aligned}
}
\tag{3.8}
\]
and by the general theorem
\[
\boxed{0\le \mathcal C_m\le K_{\rm occ}(F_m).}
\tag{3.9}
\]
(The left inequality also follows from the variational supremum by allowing all `t_k=0`; formula (3.8) is the displayed feasible choice.)

## 4. The logarithmic loss is only O(I)

Because `p=2^{1-m}`,
\[
\log_2{1-p\over p}=m-1+\log_2(1-p).
\]
Using `p->0` and `mp->0`, equations (3.6)--(3.8) yield
\[
\begin{aligned}
\mathcal C_m
&=p(m-4)(m-1)+o(mp)\\
&=mp\,(m-5)+o(mp).
\end{aligned}
\tag{4.1}
\]
Combining with the exact source asymptotic (2.4),
\[
\boxed{
K_{\rm occ}(F_m)-\mathcal C_m
=\left({1\over\ln2}+o(1)\right)mp
=\left({1\over\ln2}+o(1)\right)I(g_m).
}
\tag{4.2}
\]
Equivalently,
\[
\boxed{
{\mathcal C_m\over K_{\rm occ}(F_m)}\longrightarrow1.
}
\tag{4.3}
\]

This closes the precise sparse-family acceptance target left by account04/B15: unlike the full unweighted convolution energy, the new signed-shift statistic retains the rare-event logarithm and loses only `O(I)`. It also strictly upgrades the account02/B08 one-event certificate, whose leading ratio was `1/2` on the same family.

## 5. Recursive-majority preflight

This result does **not** claim universal FEI closure. The account03/B18 recursive-majority obstruction is respected:

- the statistic (1.7) is not a fixed low-level labelled projection;
- it allows an arbitrarily growing collection of source-chosen cells and shifts;
- the sparse proof retains every cardinality level `k>=3` separately rather than merging the high spectrum into one tail.

However, the sparse specialization uses cardinality cells because that source is uniform within each nonempty level. Recursive ternary majority has hierarchical high-scale dependence, and no claim is made that the same radial partition pays its full `K_occ`. A universal continuation must choose a genuinely hierarchy-aware partition/shift family and prove enough simultaneous lower masses to pay the Bellman deficit. Merely reusing the radial cells is not justified by this report.

## 6. Conditional end-to-end chain and first missing implication

The now-valid Path-B chain is:

1. **PROVED IN SOURCE:** `R_Gamma=B_inf^Gamma+K_occ`, with `K_occ=D_2(P||Q_r)`.
2. **PROVED HERE:** every disjoint family of signed-shift source constraints yields the single no-double-spending variational certificate (1.7), hence `mathfrak B<=K_occ`.
3. **PROVED HERE ON THE GENUINE SPARSE SUSPENSION:** there is an explicit multishift/multilevel choice with
   \[
   K_{\rm occ}-\mathfrak B=O(I),
   \]
   and in fact exact asymptotic loss `I/ln2`.
4. **UNPAID:** construct a source-valid hierarchy-aware family of cells/shifts for arbitrary balanced Boolean sources such that
   \[
   \mathfrak B\ge H_{\max}(r)-C(I-1)-O(I_{\rm already\ paid})
   \]
   for one finite universal `C`, with no repeated credit and with recursive-majority high scales retained.

Call this remaining implication

`B08-HIERARCHICAL-MULTISHIFT-PARTITION-v1`.

A promising next target is to use a recursive partition aligned with composition blocks and to feed each cell with a signed shift whose reference weight is its exact conditional `Q_r` rarity. The crucial point is that all cells must enter one partition DV test, as in (1.7), rather than as a sum of separate binary KL certificates.

## 7. Scope

This report proves a new intermediate FEI certificate and its sharp sparse-family asymptotics. It does not prove FEI, does not refute recursive majority, and does not revive any refuted fixed potential, unweighted-L2, or low-level-projection mechanism.
