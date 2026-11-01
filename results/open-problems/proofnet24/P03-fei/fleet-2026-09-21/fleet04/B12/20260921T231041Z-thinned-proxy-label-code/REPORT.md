# B12 FEI — thinned proxy-character label code

**Run:** `B12-20260921T231041Z-r41`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status:** **PARTIAL. Full uniform-cube Fourier entropy--influence remains OPEN / NOT PROVED.**  
**Claim level:** analytic interface-B auxiliary theorem plus exhaustive finite falsification checks. No novelty or publication-priority claim.

## 0. What changed

The preceding fleet04/B12 run paid, at one balanced Bernoulli physical reveal, two quantities without using ambient dimension or the false shortcut `sum_i d_i=O(J)`:

1. the source-exact actual-anchor signed correction from fleet02/B13; and
2. a conservative unresolved robust trigger-incidence address budget.

It still left the branch-dependent **character label** exposed by fleet04/B13's exact proxy-gauge theorem. This run changes the coding object: instead of paying every possible robust label coordinate, encode only those robust proxy bits whose trigger coordinates are actually revealed while the derivative-row coordinate itself survives. The same Bernoulli thinning that controls the support bank then pays the entropy of this resolved character label by `O(J)`.

At the live relative `epsilon=1/16` threshold, for the balanced survival probability

\[
 s_*={J\over4M},\qquad t_*=1-s_*,
\]

the resolved robust proxy-character label obeys

\[
\boxed{
 \mathbb E_A H(\mathsf T_A(Z)\mid A)
 \le {17\over14}\,t_*J
 \le {17\over14}J.
}
\]

Combining it with the preceding actual-anchor correction and unresolved trigger-incidence budget gives

\[
\boxed{
\mathbb E\!\left[
 \Gamma(A)+L_R^{\rm surv}(A)+H(\mathsf T_A(Z)\mid A)
\right]
\le {12\over7}J-{2\over7}{J^2\over M}
\le {12\over7}J.
}
\]

This is an influence-relative three-part code for the robust near-subcube sector. It contains no `n`, `log n`, ambient-alphabet continuity factor, or raw `sum d_i` payment. It still does **not** pay the parent-to-child Fourier-Shannon cost of the physical reveal, nor all high-defect/nonrobust channels, so it is not a proof of FEI.

## 1. Fresh completed peer result consumed

The named newest compatible fleet02 row-stability/coding input used here is

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260921T215826Z-cross-plaquette-tensor-correction/REPORT.md`,

report blob `17387ba6940056fd7df07a4205d816e9ce4dc7cf`, introduced at scientific commit `fac5798cba0a75b45b237d0dfd1b431191d40da8`.

For every physical cut `A|B`, it constructs an **actual anchor child** and branch signs. If

\[
 \epsilon_a=\Pr_b[f(a,b)\ne\sigma_a f(a_0,b)],
 \qquad
 \Gamma(A):=\mathbb E_a h_2(\epsilon_a),
\]

then

\[
\boxed{\Gamma(A)\le {1\over2}P_{B\to A}(f).}
\tag{1.1}
\]

For a Bernoulli reveal in which each coordinate is revealed with probability `t` and survives with probability `s=1-t`, the genuine support-disagreement bank therefore gives

\[
\boxed{
 \mathbb E_A\Gamma(A)
 \le 2stM,
 \qquad
 M={1\over4}\sum_{i\ne k}p_{ik}.
}
\tag{1.2}
\]

**Exact implication supplied to this run:** the signed child-correction term can be paid directly from the support part `M` of the mixed-curvature bank *before* replacing it by total derivative depth. This leaves the same reveal available to encode the robust proxy-character label below.

The compatible fleet02/B12 factorial-component work is also retained as a fine-scale coding input; it pays internal reciprocal-component row identity from the pre-existing factorial/prefix refunds. The theorem below addresses a different object: the physical branch-dependent proxy character created by a robust reveal.

## 2. Mixed-curvature integrability and robust trigger load retained exactly

Use fleet04/B18's current integration. In the minimizing-character gauge,

\[
0<j_i=\operatorname{Inf}_i(f)\le {1\over2},
\qquad J=\sum_i j_i.
\]

For the derivative support indicator `eta_i`, let

\[
p_{ik}=\Pr[\eta_i(x)\ne\eta_i(x+e_k)]
\]

and retain opposite-sign overlap `o_ik`. The genuine integrability law is

\[
\kappa_{ik}=p_{ik}+4o_{ik},
\qquad
D:=\sum_i d_i=M+O,
\qquad
O:=\sum_{i\ne k}o_{ik}.
\tag{2.1}
\]

Nothing below assumes `D=O(J)`, and the orientation bank `O` is not silently relabelled as support.

For a family `R` of relative-`epsilon` physical near-subcube rows, choose proxies

\[
Q_i=\{x_{F_i}=a_i\},
\qquad r_i:=|F_i|,
\qquad u_i:=\mu(Q_i)=2^{-r_i},
\]

with

\[
\mu(E_i\triangle Q_i)\le\epsilon j_i.
\tag{2.2}
\]

Then `|u_i-j_i|<=epsilon j_i`, hence

\[
u_i\le(1+\epsilon)j_i.
\tag{2.3}
\]

The B18 support-depth theorem gives

\[
\boxed{
L_R:=\sum_{i\in R}j_i r_i
\le {2\over1-2\epsilon}M.
}
\tag{2.4}
\]

At `epsilon=1/16`,

\[
\boxed{L_R\le {16\over7}M.}
\tag{2.5}
\]

The same integration gives `M>=J/2`, so the balanced survival `s_*=J/(4M)` is always in `(0,1/2]` for a nonconstant state.

## 3. Proxy-gauge input: the remaining structure really is a character label

Fleet04/B13's one-shot proxy-gauge theorem shows why the label below is the correct object rather than residual Boolean noise. When a robust row survives while its trigger set has been revealed, the proxy bit

\[
q_i(z)=1_{\{z_{F_i}=a_i\}}
\tag{3.1}
\]

is an explicit branch-dependent character toggle. Quotienting the child by the character made from these bits leaves influence equal to the physical proxy error. Thus exact-subcube structure should be paid as a **label**, not again as residual influence.

The preceding theorem did not pay the information cost of which branch character occurs. The next theorem pays the robust resolved portion of precisely that cost.

## 4. New theorem: Bernoulli thinning pays the resolved robust character label

Let `A=A_t` be a Bernoulli physical reveal: every coordinate lies in `A` independently with probability `t`; write `s=1-t`.

A robust row is **resolved and surviving** when

\[
i\notin A,
\qquad F_i\subseteq A.
\]

For a realized reveal block `A`, define

\[
R_{\rm res}(A)
:=\{i\in R:i\notin A,\ F_i\subseteq A\}.
\tag{4.1}
\]

For the uniformly random revealed branch value `Z`, define the resolved proxy-character label vector

\[
\mathsf T_A(Z)
:=\bigl(q_i(Z)\bigr)_{i\in R_{\rm res}(A)},
\qquad
q_i(Z)=1_{\{Z_{F_i}=a_i\}}.
\tag{4.2}
\]

### Theorem B12-THINNED-PROXY-LABEL

For every relative-`epsilon` robust family with `epsilon<1/2`,

\[
\boxed{
\mathbb E_A H(\mathsf T_A(Z)\mid A)
\le
{4(1+\epsilon)\over1-2\epsilon}\,stM.
}
\tag{4.3}
\]

At `epsilon=1/16`,

\[
\boxed{
\mathbb E_A H(\mathsf T_A(Z)\mid A)
\le {34\over7}stM.
}
\tag{4.4}
\]

At the balanced scale `s_*=J/(4M)`,

\[
\boxed{
\mathbb E_A H(\mathsf T_A(Z)\mid A)
\le {17\over14}t_*J
\le {17\over14}J.
}
\tag{4.5}
\]

### Proof

Fix `A`. Joint entropy is at most the sum of marginal entropies, so

\[
H(\mathsf T_A(Z)\mid A)
\le
\sum_{i\in R_{\rm res}(A)} h_2(2^{-r_i}).
\tag{4.6}
\]

Indeed, when `F_i subset A`, the revealed coordinates in `F_i` are uniform, so `q_i(Z)` is Bernoulli with parameter `u_i=2^{-r_i}`. No independence among different proxy bits is required.

For `r>=1`, putting `u=2^{-r}` gives

\[
h_2(u)\le2ru.
\tag{4.7}
\]

For `r=1` there is equality. For `r>=2`,

\[
-(1-u)\log_2(1-u)\le {u\over\ln2}\le ru,
\]

while the first binary-entropy term is `ru`. For `r=0`, the proxy bit is deterministic and has entropy zero.

The event `i notin A` and `F_i subset A` has probability `s t^{r_i}` because `i` is not one of its transverse trigger coordinates. Averaging (4.6) and using (4.7),

\[
\begin{aligned}
\mathbb E_A H(\mathsf T_A(Z)\mid A)
&\le
\sum_{i\in R}s t^{r_i}h_2(u_i)\\
&\le
2s\sum_{i\in R}t^{r_i}r_i u_i\\
&\le
2(1+\epsilon)s\sum_{i\in R}t^{r_i}r_i j_i.
\end{aligned}
\tag{4.8}
\]

For every nontrivial trigger row `r_i>=1`, `t^{r_i}<=t`; the `r_i=0` terms vanish. Hence

\[
\mathbb E_A H(\mathsf T_A(Z)\mid A)
\le2(1+\epsilon)stL_R.
\tag{4.9}
\]

Apply (2.4) to obtain (4.3). Setting `epsilon=1/16` gives (4.4), and substituting `s_*=J/(4M)` gives (4.5). QED.

### Interpretation

This is not an ambient-alphabet continuity estimate. A large trigger codimension actually makes a proxy bit rarer; its entropy is paid by `r_i 2^{-r_i}`, and the physical near-subcube relation converts `2^{-r_i}` back to `j_i`. The resulting total is controlled by the support-disagreement bank `M`, not by the number of cube coordinates.

## 5. New three-part robust-row code at one common physical reveal

Retain the two payments already proved for the same Bernoulli reveal:

1. from fleet02/B13,
\[
\mathbb E\Gamma(A)\le2stM;
\tag{5.1}
\]

2. for unresolved surviving robust trigger incidences,
\[
L_R^{\rm surv}(A)
:=\sum_{\substack{i\in R\\i\notin A}}j_i|F_i\setminus A|,
\qquad
\mathbb E L_R^{\rm surv}(A)=s^2L_R
\le{16\over7}s^2M.
\tag{5.2}
\]

The new label theorem gives

\[
\mathbb E H(\mathsf T_A(Z)\mid A)
\le{34\over7}stM.
\tag{5.3}
\]

Therefore, at `epsilon=1/16`,

\[
\boxed{
\mathbb E\left[
 \Gamma(A)+L_R^{\rm surv}(A)+H(\mathsf T_A(Z)\mid A)
\right]
\le
{48\over7}stM+{16\over7}s^2M.
}
\tag{5.4}
\]

Choose `s=s_*=J/(4M)`. Since `t=1-s`,

\[
{48\over7}stM+{16\over7}s^2M
={48\over7}sM-{32\over7}s^2M,
\]

so

\[
\boxed{
\mathbb E\left[
 \Gamma+L_R^{\rm surv}+H(\mathsf T_A\mid A)
\right]
\le
{12\over7}J-{2\over7}{J^2\over M}
\le {12\over7}J.
}
\tag{5.5}
\]

At the smallest allowed support depth `M=J/2`, the displayed coarse right side is `8J/7`; as `M/J` becomes large it approaches `12J/7`. The policy adapts by revealing more physical coordinates instead of charging that support depth at unit price.

### Why there is no double charge

The three terms have distinct roles.

- `Gamma` is signed physical child-to-anchor correction entropy.
- `H(T_A|A)` describes proxy-character bits that have become fully determined by the revealed trigger coordinates while their row coordinate survives.
- `L_R^surv` is a conservative capacity for trigger incidences still unresolved after the reveal.

The label theorem does not spend the opposite-sign overlap bank `O`; the support-depth theorem spends only `M`. The exact relation `D=M+O` is preserved, and nowhere is `sum_i d_i` asserted to be `O(J)`.

## 6. Exact finite falsification check

`check_thinned_proxy_label_code.py` exhaustively enumerates Boolean functions modulo global sign through dimension four. For each function it performs the minimizing-character coordinate gauge, constructs the derivative-support rows, exhaustively chooses best coordinate-subcube proxies, selects the relative-`1/16` robust rows, computes `M`, and checks the analytic inequalities at the balanced scale.

Executed with the system Python and no external packages, it returned:

```text
PASS
functions_mod_global_sign=32906
active_after_folded_gauge=32876
robust_rows_tested=23848
M_ge_J_over_2=32876
support_depth_load=32876
resolved_label_entropy=32876
combined_three_part_code=32876
min_M_over_J=0.5
max_M_over_J=1.5
worst_exact_label_over_bound=0.823529411765
worst_exact_three_part_over_J=1
```

The source SHA-256 at execution was

`d596d0a39b36f1740e47b2a5781465f6fb46f0408b876d7ec270ee53441bc47e`.

This enumeration is falsification evidence only. The universal claim is the analytic proof above.

## 7. What remains open

Full FEI remains OPEN / NOT PROVED. This run removes one specific interface-B obstacle: the varying **resolved robust proxy-character label** no longer requires an ambient-dimensional code. It does not establish a parent Fourier-Shannon recursion for the physical reveal itself. It also does not by itself dispose of high-defect/nonrobust rows or prove that repeated adaptive use of the same resources is nonreusing.

The next useful implication is to combine this robust three-part code with fleet04/B13's one-shot exceptional-coordinate reveal/proxy-gauge identity and the folded activation/crossing telescope, and then isolate the exact Fourier-Shannon reveal term. A successful closure still needs that term and every exceptional/off-trigger remainder paid once from `J` or an existing negative refund.

## 8. Collaboration handoff

- `joint_directive`: `FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z`.
- `consumed_peer_artifact`: fleet02/B13 `20260921T215826Z-cross-plaquette-tensor-correction/REPORT.md`.
- `applied_to_claim`: Bernoulli support-bank payment for the actual signed anchor correction, coupled to the same reveal used for robust proxy-label thinning.
- `next_recipient`: interface-B/B18 integration and interface-A physical-reveal coding workers.
- `remaining_implication`: parent-to-child Fourier-Shannon cost of the physical reveal plus nonrobust/high-defect channels, without raw-depth reuse.
- `full_problem_change`: resolved robust branch-character label is now influence-relative; full FEI unchanged/open.
- `mechanism_change`: branch-character entropy under Bernoulli thinning, rather than another raw-depth or ambient-alphabet continuity estimate.
