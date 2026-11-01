# fleet03/B18 — recursive-majority barrier to fixed-depth I-projection payment

**Run:** `20260922T100641Z-fleet03-B18-auto11b`  
**Classification:** `CANDIDATE_REFUTED / COMMON_TARGET_PRESERVED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Version/change summary

The immutable Campaign-B target remains

`B-BALANCED-IPROJECTION-v1`.

For a balanced Boolean function `f`, put

\[
P_f(S)=\widehat f(S)^2,\qquad r_i=P_f(i\in S)=\operatorname{Inf}_i(f),\qquad \mu=\sum_i r_i=I(f).
\]

Let `Q_r` be the maximum-entropy law on nonempty subsets with the same coordinate marginals, let

\[
H_{\max}(r)=H(Q_r),\qquad K_{\rm occ}(f)=D_{\rm KL,2}(P_f\Vert Q_r)=H_{\max}(r)-H(f).
\]

Then the exact common residual is

\[
\boxed{\mathcal R_C(f)=K_{\rm occ}(f)+C(\mu-1)-H_{\max}(r)=C[I(f)-1]-H(f).}
\tag{0.1}
\]

The preceding B18 result proved that full FEI at `C` is equivalent to `\mathcal R_C(f)\ge0` for every balanced Boolean `f`, and that the coordinate-labelled projection

\[
\Delta_d(f;r):=D_{\rm KL,2}(\Pi_dP_f\Vert\Pi_dQ_r)
\tag{0.2}
\]

is a genuine signed-source lower bound on `K_occ`; `\Pi_d` retains every individually labelled atom with `1\le|S|\le d` and merges all larger sets into one tail symbol. Finite computation showed `d=2` pays all balanced functions through `n=4`, but no all-dimensional theorem was claimed.

This run attacks the exact missing inference

> **`B-LOWLEVEL-PROJECTION-v1`:** a fixed-depth, or uniformly low-depth, coordinate-labelled projection `\Delta_d` supplies the dimension-free dependence payment needed in (0.1).

It is **REFUTED** below on the genuine Boolean recursive ternary-majority family. The common target (0.1) itself is not refuted.

### Completed cross-account results consumed substantively

1. fleet02/B17, `20260922T091146Z-strong-prime-shaped-repair/REPORT.md`, supplies the current source-valid shaped all-gate candidate
   \[
   \Gamma^{\rm shape}(p)=\Gamma^\dagger(p)+{374403\over10^7}
   \left[1-(1-2p)^4-{113009\over5\cdot10^6}(4p(1-p))^3\right]
   \]
   with center
   \[
   C_{\rm shape}=6.55844529582746,
   \]
   and proves that the added direction is universally gate-safe. I apply its **actual center** in the numerical specialization below rather than retaining the already superseded quartic-only center.
2. fleet02/B18, `20260922T093253Z-balanced-slice-admission/REPORT.md`, proves that for every finite symmetric gate potential of center `C`, its balanced-uniform gate defect is exactly `C[I(f)-1]-H(f)`. Therefore the shaped candidate's balanced obligation is precisely (0.1), so an off-center repair cannot bypass the dependence-payment problem tested here.

These are applications, not a claim that either peer result proves FEI.

## 1. Smallest conditional universal argument

The current Campaign-B chain is:

1. **PROVED:** full FEI at constant `C` is equivalent to `H(f)\le C[I(f)-1]` for every balanced Boolean `f`.
2. **PROVED:** the exact I-projection split is `H(f)=H_{\max}(r)-K_{\rm occ}(f)`, preserving every coordinate marginal and the entire negative KL credit.
3. **PROVED:** `K_{\rm occ}\ge\Delta_d` for every `d` by data processing; coordinate labels at levels `\le d` are paid explicitly.
4. **UNPAID:** obtain a dimension-independent lower bound on the **actual** `K_{\rm occ}` strong enough to pay
   \[
   A_C(r):=H_{\max}(r)-C(\mu-1)
   \tag{1.1}
   \]
   whenever this quantity is positive.
5. **FAILED MECHANISM:** replace step 4 by `\Delta_d\ge A_C(r)` for fixed `d`, or even for every cutoff below one half of the recursive depth. Theorem 2.1 refutes this.

No unsigned spectral law is introduced: the counterfamily is an explicit balanced Boolean family and `P_f` is its exact squared Fourier spectrum.

## 2. Main theorem — low-level labelled KL becomes negligible on recursive majority

Let `M_1=Maj_3`, with

\[
Maj_3(x_1,x_2,x_3)={x_1+x_2+x_3-x_1x_2x_3\over2},
\]

and let `M_m` be the depth-`m` disjoint recursive ternary-majority formula. It has `N_m=3^m` physical input coordinates.

### Theorem 2.1 — `RM3-LOWLEVEL-BARRIER-v1`

Fix any finite real `C` and any `\varepsilon\in(0,1/2)`. For each `m`, let `d_m` be an integer satisfying

\[
1\le d_m\le(1/2-\varepsilon)m.
\tag{2.1}
\]

Let `P_m` be the exact spectral law of `M_m`, let `Q_m` be its influence-matched nonempty conditional-product I-projection, and put

\[
\Delta_{d_m}^{(m)}=D_{\rm KL,2}(\Pi_{d_m}P_m\Vert\Pi_{d_m}Q_m).
\]

Then, for all sufficiently large `m`, the demand

\[
A_m(C):=H_{\max}(r^{(m)})-C[I(M_m)-1]
\]

is positive and

\[
\boxed{
{\Delta_{d_m}^{(m)}\over A_m(C)}\longrightarrow0.
}
\tag{2.2}
\]

In particular, for every fixed integer `d`,

\[
\Delta_d^{(m)}<A_m(C)
\]

for all sufficiently large `m`. Thus no fixed finite level projection can prove the common target by itself.

### Proof

#### 2.1 Exact recursive-majority spectral process

The base spectral law of `Maj_3` chooses each singleton with probability `1/4` and the triple with probability `1/4`. Under disjoint composition, every active spectral coordinate independently expands according to

\[
X=\begin{cases}
1,&\text{probability }3/4,\\
3,&\text{probability }1/4.
\end{cases}
\tag{2.3}
\]

Therefore the spectral cardinality `Z_m=|S_m|` is a Galton-Watson population after `m` generations. In particular

\[
r_i^{(m)}=2^{-m},\qquad
\mu_m:=I(M_m)=\mathbb E Z_m=(3/2)^m,
\tag{2.4}
\]

and the standard composition recurrence gives

\[
H(M_m)=4(\mu_m-1).
\tag{2.5}
\]

Equation (2.5) will be used only to interpret the obstruction; the projection estimate itself uses the exact branching law.

#### 2.2 The true spectral mass below `d_m` is exponentially small in depth

Choose one deterministic spectral spine: when a node has one child follow it; when it has three children follow the first. Along this spine the events `X=3` are independent Bernoulli(`1/4`) trials, so

\[
B_m\sim\operatorname{Bin}(m,1/4).
\]

Every triple event anywhere in the branching tree increases the final population by two. Hence

\[
Z_m=1+2T_m,
\]

where `T_m` is the total number of triple events in the whole tree, and `T_m\ge B_m`. Consequently

\[
\Pr_{P_m}(Z_m\le d_m)
\le
\Pr\!\left(B_m\le{d_m-1\over2}\right).
\]

By (2.1), the right side is at most

\[
\alpha_m:=\Pr_{P_m}(Z_m\le d_m)
\le e^{-\kappa_\varepsilon m},
\tag{2.6}
\]

where one may take the strictly positive natural-log Bernoulli divergence

\[
\kappa_\varepsilon
=D_{\rm KL}\!\left({1\over4}-{\varepsilon\over2}\,\middle\|\,{1\over4}\right)>0.
\]

#### 2.3 The I-projection has exponentially growing cardinality mean

Because every marginal equals `r_m=2^{-m}`, the peer I-projection theorem gives

\[
Q_m(S)=c_m^{|S|-1}r_m^{|S|}(1-c_mr_m)^{N_m-|S|},\qquad S\ne\varnothing,
\tag{2.7}
\]

where `c_m\in(0,1]` is the positive solution of

\[
1-c_m=(1-c_mr_m)^{N_m}.
\tag{2.8}
\]

At `c=1/2`,

\[
(1-r_m/2)^{N_m}\le e^{-\mu_m/2}<1/2
\]

for every `m\ge1`; uniqueness of the positive root therefore gives

\[
c_m\ge1/2.
\tag{2.9}
\]

Equivalently, under `Q_m`, cardinality is `Bin(N_m,t_m)` conditioned to be nonzero, where

\[
t_m=c_mr_m,
\qquad
\lambda_m=N_mt_m=c_m\mu_m\ge\mu_m/2.
\tag{2.10}
\]

Since `d_m=O(m)` but `\mu_m=(3/2)^m`, eventually `d_m\le\lambda_m/2`. A standard binomial Chernoff bound and `c_m\ge1/2` imply

\[
\beta_m:=Q_m(|S|\le d_m)
\le 2e^{-\mu_m/16}.
\tag{2.11}
\]

#### 2.4 Every retained atom has an explicit coordinate-label price

For an individually labelled set `S` of size `k\le d_m`, (2.7), `c_m\ge1/2`, and

\[
-\ln(1-x)\le {x\over1-x}
\]

give

\[
\log_2{1\over Q_m(S)}
\le k(m+1)+{2\mu_m\over\ln2}.
\tag{2.12}
\]

Thus the coordinate identities are not hidden: the `km` term explicitly pays the names of `k` leaves among the `3^m` physical coordinates.

#### 2.5 Coarse KL bound

Expanding the labelled-low-level plus one-tail KL,

\[
\Delta_{d_m}^{(m)}
=
\sum_{1\le|S|\le d_m}P_m(S)\log_2{P_m(S)\over Q_m(S)}
+(1-\alpha_m)\log_2{1-\alpha_m\over1-\beta_m}.
\]

Since `P\log(P/Q)\le P\log(1/Q)`, (2.12) bounds the first term by

\[
\alpha_m\left[d_m(m+1)+{2\mu_m\over\ln2}\right].
\]

For sufficiently large `m`, `\beta_m\le1/2`, and the tail term is at most

\[
\log_2{1\over1-\beta_m}
\le {2\beta_m\over\ln2}
\le {4e^{-\mu_m/16}\over\ln2}.
\]

Hence

\[
\boxed{
\Delta_{d_m}^{(m)}
\le
e^{-\kappa_\varepsilon m}
\left[d_m(m+1)+{2\mu_m\over\ln2}\right]
+{4e^{-\mu_m/16}\over\ln2}.
}
\tag{2.13}
\]

#### 2.6 The common Shannon demand is order `\mu_m m`

The exact maximum entropy is

\[
H_{\max}(r^{(m)})
={N_m h_2(c_mr_m)-h_2(c_m)\over c_m}.
\tag{2.14}
\]

Using `h_2(x)\ge x\log_2(1/x)`, `c_m\ge1/2`, and `h_2(c_m)/c_m\le2`,

\[
H_{\max}(r^{(m)})
\ge \mu_m\log_2{1\over c_mr_m}-2
\ge \mu_m m-2.
\tag{2.15}
\]

Therefore

\[
A_m(C)\ge \mu_m(m-C)+C-2,
\tag{2.16}
\]

which is positive and of order `\mu_m m` for every fixed finite `C`. Combining (2.13) and (2.16), using `d_m=O(m)` and exponential growth of `\mu_m`, proves (2.2). `QED`

## 3. Why this is a proof-mechanism counterexample, not an FEI counterexample

For recursive ternary majority, (2.5) gives

\[
\mathcal R_C(M_m)=C(\mu_m-1)-H(M_m)=(C-4)(\mu_m-1).
\tag{3.1}
\]

Thus for every `C>4`, including the currently consumed shaped center `C_shape`, this family is safely inside the desired FEI inequality. Its true irreducible dependence credit is

\[
K_{\rm occ}=H_{\max}-4(\mu_m-1),
\]

which is large. The theorem says that this credit is **not visible in any fixed collection of individually labelled low Fourier levels**. It lives in genuinely multiscale/high-cardinality dependence.

This is exactly the distinction Campaign B needed: source-valid low-level KL is real credit, but a fixed-depth code cannot be the universal decoder/payment.

## 4. Deterministic `d=2` diagnostic at the current shaped center

For `d=2`, recursive majority has no level-two spectral atoms. The exact projected KL can therefore be evaluated from the singleton mass and one tail. The adjacent standard-library checker prints:

| depth `m` | `I=(3/2)^m` | demand `Hmax-C_shape(I-1)` | `Delta_2` | ratio |
|---:|---:|---:|---:|---:|
| 4 | 5.0625 | 0.668932244 | 0.816378784 | 1.220421 |
| 5 | 7.59375 | 5.505831257 | 1.163695239 | 0.211357 |
| 6 | 11.390625 | 16.501529343 | 1.644434282 | 0.099653 |
| 8 | 25.62890625 | 80.406301195 | 2.770476128 | 0.034456 |
| 10 | 57.66503906 | 288.168262792 | 4.045056960 | 0.014037 |
| 12 | 129.74633789 | 899.741787324 | 5.504947665 | 0.006118 |
| 16 | 656.84083557 | 7155.770912600 | 9.322946240 | 0.001303 |
| 20 | 3325.25673008 | 49500.507794700 | 15.145369774 | 0.000306 |

The crossover is informative: the same `Delta_2` mechanism that succeeds on the small four-variable exhaustive baseline already pays only about 21% of the required I-projection deficit at recursive-majority depth five, and its fraction then collapses to zero. The table is diagnostic; Theorem 2.1 is analytic.

## 5. Exact failed claim, replacement obligation and next recipients

**Common candidate version:** `B-BALANCED-IPROJECTION-v1` remains unchanged and OPEN.

**Attempted mechanism version:** `B-LOWLEVEL-PROJECTION-v1`.

**Old missing implication:** derive a dimension-free Boolean lower bound on `K_occ` strong enough to pay `Hmax-C(\mu-1)`, with the previous finite `Delta_2` success as the simplest candidate mechanism.

**New result:** `RM3-LOWLEVEL-BARRIER-v1` proves that every fixed cutoff, and more generally every `d_m\le(1/2-\varepsilon)m`, contributes an asymptotically vanishing fraction of the required Shannon payment on recursive ternary majority. Thus the fixed-depth projection mechanism is **REFUTED** at universal scope.

**Replacement obligation:** a successful Shannon code/payment must be multiscale. On this family it must retain labelled information at levels growing at least to the middle scale of recursion, or exploit a different signed Boolean statistic that captures the same high-level dependence without enumerating those labels. The full `K_occ` credit remains available; only this low-level extraction is inadequate.

**Consumed peer artifact:** primarily fleet02/B17 `20260922T091146Z-strong-prime-shaped-repair`; fleet02/B18 `20260922T093253Z-balanced-slice-admission` fixes the exact balanced interpretation.

**Next recipients:**
- fleet03/B12: replace fixed-depth decoding by a hierarchical/multiscale spectral code and explicitly price block/leaf identities;
- fleet02/B15: derive a chain-rule or multiscale lower bound on the full `K_occ` rather than another fixed `Pi_d` projection;
- fleet02/B17: adversarially test candidate growing cutoffs around the `m/2` threshold and other branching families;
- fleet04/B12: seek a Boolean coupling whose conditioning reveals high-cardinality dependence without paying ambient labels one by one.

**Implication to full FEI:** none yet at target level. The common residual remains exactly equivalent to full FEI, but one natural proposed way of paying its only missing information term is now rigorously eliminated. Full FEI remains **OPEN / NOT PROVED**.

## 6. Scope and verification

The adjacent checker is deterministic and standard-library only. It verifies the closed formulas used in the `d=2` table and the expected monotone collapse after the small-depth crossover. It is supporting evidence, not the proof of Theorem 2.1.

No novelty or publication-priority claim is made. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private material, email/Drive content, public posting, paid model/API/Codex call, remote workflow, or permission change is used here.
