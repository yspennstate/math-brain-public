TASK: B13 ACCOUNT: account02 RUN: 2026-09-21T21:11:22.339120Z — block-Holevo restriction mixing paid by oriented Boolean support boundary

MODEL: GPT-5.6 Sol (self-report)
REQUESTED EFFORT: maximum actually supported
CONFIGURED / KNOWN REASONING LEVEL: UNKNOWN / NOT_EXPOSED
PROVIDER REASONING USAGE: null / NOT_EXPOSED
EXECUTION: WITHOUT_VERIFIED_BRAIN

# Status

**Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**

This run implements the live joint FEI order and changes mechanism away from the preceding harmonic/layer-incidence route. The main result is a universal Boolean block theorem: the mixture-information part of a genuine physical block restriction is bounded, with sharp constant one, by the **oriented sensitivity-support boundary crossing that block**. The same bank also bounds the mutual information between the two Fourier block labels, and its zero set is exactly disjoint multiplicative factorization.

The theorem is tensor-aware: on an exact disjoint product cut the new bank and the paid residual both vanish, even though the signed mixed-curvature bank can be strictly positive. Thus it survives the tensor-amortization obstruction from the previous B13 report instead of merely renaming it.

No finite universal FEI constant is obtained. The remaining source-frontier obligation is the conditional Fourier-label term plus a nonreusing payment of the support-boundary bank along an actual restriction strategy.

# 1. Fresh scientific inputs and the newest other-account result actually used

Scientific master was refreshed during this invocation. The newest compatible completed result was

`proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260921T2122Z-source-frontier-one-shot/REPORT.md`

at scientific commit `7a448238d724e655dd215953778543bc2e69a751`, report blob `8cced1e67ed2181463caaf877946717e81e4e7c8`.

That report consumes the account03 integrability DAG and proves a **one-shot physical reveal block** `A` for the robust near-subcube sector. It removes every non-source robust component, leaves one source representative per source component, and gives

\[
\mathbb E_z J(f_{A=z})\le J_E+\varepsilon J_R,
\]

with `epsilon=1/16` at the current threshold. Its explicit remaining gap is that the full Shannon cost of the reveal block is not yet paid by `O(J)`.

The present theorem is applied exactly to that gap: for **every** physical reveal block `A`, including the account04 source-frontier block, it decomposes the entropy decrement and pays its genuine restriction-mixture term by a physical cross-boundary bank with no ambient-dimension factor.

The other source-exact input is account04/B18

`proofnet24/P03-fei/fleet-2026-09-21/account04/B18/20260921T191147Z-mixed-curvature-global-rigidity/REPORT.md`.

Its notation is retained:

\[
\kappa_{ik}=p_{ik}+4o_{ik},
\]

where `p_ik` is sensitivity-support disagreement and `o_ik` is opposite-sign overlap. The theorem below identifies a residual for which **only `p_ik` is needed**. This does not contradict the B18 warning that unsigned support cannot pay signed additive curvature; the paid residual here is phase-invariant.

I also read the newer account01/B18 prefix-total-correlation result `20260921T2100Z-prefix-tc-refund`. Its nonreuse warning is binding below: the new pair bank is used for one physical block only. I do not sum it over an adaptive tree without a separate telescoping/TC argument.

# 2. Required comparison with the last THREE substantive B13 reports

The last three completed own reports were:

1. `20260921T195704Z-tensor-amortized-incidence`: proved that a global bound on the layer-incidence residual `R_inc` is already full-FEI-strength under Boolean tensor powers, so the correct quantifier had to move to primitive critical cores.
2. `20260921T192906Z-harmonic-layer-incidence`: refuted row-local harmonic-Palm mean closure with odd majority, paid all residual-cardinality entropy, and isolated `R_inc`.
3. `20260921T185920Z-harmonic-marker-payment`: used the actual ternary Boolean derivative plus hypercontractivity to pay the empty/nonempty flag and root-marker entropy, leaving an inverse-size Palm residual.

## FULL-PROBLEM CHANGE

**Before:** the harmonic route had localized a global residual but the immediately proposed global payment was proved FEI-hard by tensor amplification. No tensor-aware physical block theorem paid the mixture information created by a real restriction.

**After:** no full FEI constant is proved. A new universal implication is paid exactly enough to feed interface A/B: for every block `A`, the physical restriction mixture information `JS_A` and the Fourier block mutual information are bounded by a sharp, genuinely Boolean support-boundary bank. For a minimum-dimensional counterexample to `H<=C I`, every proper block is therefore forced to violate an explicit block-payment inequality stated in Section 7.

**Full-bound status:** NO FULL-BOUND MOVEMENT; FEI remains open. The new paid component is a universal block residual, not the whole entropy decrement.

## MECHANISM CHANGE

**Before:** inverse-size spectral markers, layer-incidence entropy, then tensor powers used adversarially against a global residual theorem.

**After:** treat the Boolean truth table as a bipartite phase state across a physical coordinate cut, apply a block Holevo/Han argument, and then convert every binary conditional phase ambiguity to **support boundary** by cube edge isoperimetry. This mechanism is insensitive to pure tensor-phase variation and hence avoids the previous tensor obstruction.

Creative moves from the fleet list: **#1 change the category** (Boolean restriction channel to bipartite phase state), **#11 dualize** (Fourier measurement versus physical support boundary), and **#27 swap the quantifiers** (one arbitrary physical block first, then derive what every minimal counterexample must satisfy).

# 3. Exact physical block restriction identity

Let

\[
f:\mathbb F_2^n\to\{-1,+1\},\qquad
\mu(R)=\widehat f(R)^2,
\]

and split the coordinates into a nonempty proper partition

\[
[n]=A\sqcup B.
\]

Draw the spectral sample `S~mu` and write

\[
S_A=S\cap A,\qquad S_B=S\cap B.
\]

For each physical assignment `a in F_2^A`, let

\[
f_a(y)=f(a,y),\qquad y\in\mathbb F_2^B,
\]

and let

\[
\mu_a(T)=\widehat{f_a}(T)^2,
\qquad T\subseteq B.
\]

Parseval in the `A` variables gives

\[
\bar\mu_B(T):=\mathbb E_a\mu_a(T)
=\sum_{R\subseteq A}\widehat f(R\cup T)^2
=\Pr(S_B=T).
\tag{3.1}
\]

Define the physical-restriction mixture information

\[
\boxed{
\operatorname{JS}_A(f)
:=H(\bar\mu_B)-\mathbb E_a H(\mu_a).
}
\tag{3.2}
\]

This is exactly the mutual information of the channel that chooses a uniform physical block value `a` and then samples a Fourier label from the restriction `f_a`.

Using `H(S)=H(S_B)+H(S_A|S_B)` and (3.1), one gets the exact identity

\[
\boxed{
\Delta_A H(f)
:=H(f)-\mathbb E_aH(f_a)
=H(S_A\mid S_B)+\operatorname{JS}_A(f).
}
\tag{3.3}
\]

The two terms have different meanings. `H(S_A|S_B)` is the unresolved spectral-label cost of the revealed block. `JS_A` is the actual mixing cost of the physical descendants. The next theorem pays the latter.

# 4. The Boolean support-boundary bank

For `i in A` and a fixed assignment `a_{-i}` of the other `A` coordinates, define the sensitivity support in the residual `B` cube

\[
E_{i,a_{-i}}
=
\{y:\ f(0,a_{-i},y)\ne f(1,a_{-i},y)\}.
\tag{4.1}
\]

Let

\[
q_{i,a}=\mu_B(E_{i,a}),
\qquad
q^*_{i,a}=\min(q_{i,a},1-q_{i,a}).
\]

For `k in B`, put

\[
p_{ik}(a_{-i})
=
\Pr_y[1_{E_{i,a}}(y)\ne1_{E_{i,a}}(y+e_k)].
\tag{4.2}
\]

Average over `a_{-i}` and sum across the cut:

\[
\boxed{
P_{A\to B}(f)
:=
\sum_{i\in A}\sum_{k\in B}
\mathbb E_{a_{-i}}p_{ik}(a_{-i}).
}
\tag{4.3}
\]

This is exactly the oriented `p_ik` support-disagreement bank from the account04/B18 mixed-curvature notation, summed only across the chosen block cut.

# 5. PROVED: block-Holevo / support-boundary theorem

### Theorem B13-BLOCK-HOLEVO-SUPPORT-01

For every Boolean `f` and every nontrivial partition `A sqcup B`, let `E_{A:B}(f)` be the bipartite entropy of the normalized Boolean phase state

\[
|\Psi_f\rangle
=2^{-n/2}\sum_{a,y}f(a,y)|a\rangle|y\rangle.
\]

Then

\[
\boxed{
\max\{\operatorname{JS}_A(f),\ I_2(S_A;S_B)\}
\le E_{A:B}(f)
\le
\min\{P_{A\to B}(f),P_{B\to A}(f)\}.
}
\tag{5.1}
\]

In particular,

\[
\boxed{
\operatorname{JS}_A(f)
\le
\min\{P_{A\to B}(f),P_{B\to A}(f)\}.
}
\tag{5.2}
\]

The constant one is sharp.

### Proof, first inequality

For a physical block value `a`, define the normalized residual sign state

\[
|\psi_a\rangle
=2^{-|B|/2}\sum_y f(a,y)|y\rangle.
\]

The reduced state on `B` is

\[
\rho_B=\mathbb E_a|\psi_a\rangle\langle\psi_a|,
\qquad
E_{A:B}=S(\rho_B).
\]

Walsh measurement of `|psi_a>` has outcome law `mu_a`. Hence the Holevo/data-processing inequality gives

\[
\operatorname{JS}_A=I(a;S_B)\le S(\rho_B).
\tag{5.3}
\]

Alternatively measure the `A` side of the pure phase state in the Walsh basis. Conditional on `S_A`, the residual `B` state is pure. A subsequent Walsh measurement on `B` produces the actual joint spectral law of `(S_A,S_B)`. Holevo again gives

\[
I_2(S_A;S_B)\le S(\rho_B).
\tag{5.4}
\]

### Proof, support-boundary upper bound

The physical `A` bits are independent and uniform in the pure-state ensemble `a -> |psi_a>`. Quantum conditional-entropy subadditivity gives the Han-type bound

\[
S(\rho_B)=I(A:B_q)
\le
\sum_{i\in A}I(A_i:B_q\mid A_{-i}).
\tag{5.5}
\]

For fixed `a_{-i}`, the two conditional residual states are pure and equiprobable. Their overlap is

\[
\langle\psi_{0,a}|\psi_{1,a}\rangle
=
\mathbb E_y f(0,a,y)f(1,a,y)
=1-2q_{i,a}.
\tag{5.6}
\]

The equal binary mixture of two pure states with overlap `c` has nonzero eigenvalues `(1+|c|)/2` and `(1-|c|)/2`. Thus

\[
I(A_i:B_q\mid A_{-i}=a_{-i})
=h_2(q^*_{i,a}).
\tag{5.7}
\]

For any subset `E` of a Boolean cube of measure `t<=1/2`, edge isoperimetry in the present influence normalization gives

\[
\sum_k\Pr[1_E(y)\ne1_E(y+e_k)]
\ge2t\log_2(1/t).
\tag{5.8}
\]

The elementary scalar inequality

\[
h_2(t)\le2t\log_2(1/t),\qquad 0\le t\le1/2,
\tag{5.9}
\]

then yields

\[
h_2(q^*_{i,a})
\le
\sum_{k\in B}p_{ik}(a_{-i}).
\tag{5.10}
\]

Average (5.10), sum `i in A`, and combine with (5.5):

\[
E_{A:B}\le P_{A\to B}.
\]

Swap `A,B` to get `E_{A:B}<=P_{B->A}`. This proves (5.1). QED.

### Sharpness

On the two-bit one-point defect `f=[1,-1,1,1]` with `A={0}`, direct calculation gives

\[
\operatorname{JS}_A=1,
\qquad
P_{A\to B}=1.
\]

So the coefficient one in (5.2) cannot be uniformly improved.

# 6. PROVED: zero support-boundary is exact tensor factorization

### Proposition B13-BLOCK-PRIMITIVITY-02

For a nontrivial partition `A sqcup B`,

\[
\boxed{
P_{A\to B}(f)=0
\quad\Longleftrightarrow\quad
f(a,y)=g(a)h(y)
}
\tag{6.1}
\]

for Boolean `g,h` (up to an overall sign).

### Proof

The reverse implication is immediate: for a product, an `A`-edge either flips for every `y` or for no `y`, so every sensitivity-support indicator is constant on the `B` cube.

Conversely assume `P_{A->B}=0`. Then every support indicator in (4.1) has zero boundary in every `B` direction and hence is constant on the connected `B` cube. Therefore for every `A` edge `(a,a+e_i)`, the ratio

\[
f(a,y)f(a+e_i,y)\in\{\pm1\}
\]

is independent of `y`.

Fix `y_0`. For any `y`, the ratio

\[
R_y(a)=f(a,y)f(a,y_0)
\]

is unchanged along every `A` edge, hence is constant in `a`. Choosing a basepoint `a_0`,

\[
f(a,y)=\bigl[f(a,y_0)f(a_0,y_0)\bigr]f(a_0,y),
\]

which is the required product factorization. QED.

Thus `P_{A->B}` is an exact **physical primitivity defect**. A tensor-primitive critical core has positive bank on every nontrivial partition, but no dimension-independent positive floor is claimed.

# 7. Transfer back to ordinary entropy/influence and the minimal-counterexample constraint

For physical restriction of block `A`, ordinary influence on the unrevealed coordinates is a martingale:

\[
\mathbb E_a I(f_a)
=
\sum_{k\in B}\operatorname{Inf}_k(f)
=I(f)-I_A(f),
\qquad
I_A:=\sum_{i\in A}\operatorname{Inf}_i(f).
\tag{7.1}
\]

Suppose `f` is a minimum-dimensional counterexample to a proposed bound

\[
H(g)\le C I(g).
\]

Every proper restriction `f_a` obeys the bound by minimality. Hence (3.3), (5.2), and (7.1) show that **any** proper block satisfying

\[
\boxed{
H(S_A\mid S_B)
+\min(P_{A\to B},P_{B\to A})
\le C I_A
}
\tag{7.2}
\]

would contradict minimality. Therefore every minimum-dimensional counterexample must satisfy the strict block-expansion condition

\[
\boxed{
H(S_A\mid S_B)
+\min(P_{A\to B},P_{B\to A})
> C I_A
}
\tag{7.3}
\]

for every nonempty proper `A`.

This is a true Boolean/tensor-aware critical-core constraint, not a sign-free probability relaxation. It also transfers to the centered formulation: multiply by the coordinate character that folds every influence, preserving `H` and making `I=J` at the parent. A universal `H<=C J` theorem would imply the original FEI with the same `C`.

# 8. Application to the newest account04 source-frontier block

Take the actual one-shot reveal block `A` constructed in account04/B13 `20260921T2122Z-source-frontier-one-shot`. That theorem gives the **influence side**

\[
\mathbb E_zJ(f_{A=z})\le J_E+\varepsilon J_R.
\tag{8.1}
\]

The present theorem gives, for the very same physical restriction,

\[
\boxed{
\Delta_AH
\le
H(S_A\mid S_B)
+\min(P_{A\to B},P_{B\to A}).
}
\tag{8.2}
\]

Thus the phrase “pay the whole Shannon cost of the reveal block” can now be replaced by the exact narrower target

\[
\boxed{
H(S_A\mid S_B)
+\min(P_{A\to B},P_{B\to A})
\stackrel{?}{\le} C\,[J(f)-\mathbb E_zJ(f_{A=z})]
}
\tag{8.3}
\]

for the source-frontier block. The `JS` mixture term is no longer an unnamed gap; it is universally paid by the physical support-boundary bank. What remains unproved is an influence-scale/nonreusing payment of that bank together with the conditional Fourier label term.

This interfaces cleanly with account01/B18's all-witness prefix theorem: its total-correlation correction is exactly why one must not simply sum pairwise payments over successive blocks. The present report makes only the one-block statement (8.2).

# 9. Decisive tensor stress: signed curvature is the wrong surrogate for this residual

A tempting stronger replacement would charge the new mixture residual by full signed mixed curvature

\[
\sum_{i\in A,k\in B}\kappa_{ik}
=
\sum(p_{ik}+4o_{ik}).
\]

That loses the tensor-aware property badly. Take

\[
f(x_A,x_B)=\operatorname{AND}_2^{\pm}(x_A)\,
            \operatorname{AND}_2^{\pm}(x_B),
\]

a genuine disjoint Boolean product. Across the aligned factor cut, the executed checker gives

\[
\operatorname{JS}_A=0,
\qquad
P_{A\to B}=0,
\]

but

\[
\sum o_{ik}=1,
\qquad
\sum\kappa_{ik}=4.
\]

So the opposite-sign curvature is real but is pure tensor-phase variation and should not be charged to physical restriction mixing. This is why the support component `p`, not the full `kappa`, is the correct bank for Theorem 5.1.

This does **not** refute account04/B18's use of `kappa` for additive curvature and derivative-row rigidity. It separates the two residuals that need different signed information.

# 10. Verification

Executed standard-library checker:

`check_block_holevo_support.py`

Archived output:

`CHECKER_OUTPUT.txt`

Exact scope of the executable self-check:

* all `32,906` Boolean functions modulo global output sign through dimension four;
* all `459,536` directed nontrivial block cuts for those functions;
* exact entropy-decomposition discrepancy `0.000e+00` in the executed floating evaluation;
* maximum `JS_A-P_{A->B}`: `0.000e+00`;
* maximum spectral-block mutual-information excess over `min(P_AB,P_BA)`: `0.000e+00`;
* zero-boundary/factorization mismatches: `0`;
* sharp two-bit witness: `JS=P=1`;
* aligned product stress: `JS=P=0` while opposite-sign overlap is `1` and signed curvature is `4`.

Checker status: **PASS**. The theorem itself is analytic; the exhaustive computation is a self-check, not an independent audit.

Local pre-upload SHA-256 values:

* checker: `3b4bb503ecf3654a147a4ac5836af8f9aa49aee522965f253303e593eb3227c2`;
* output: `5593e66f22f4df366ebf633ea31ff1aad92b802e54e9a0cf7dcbac979bcaba2a`.

# 11. Honest remaining implication and next recipient

**Full FEI remains OPEN.** The new theorem pays the physical restriction-mixture residual but not the conditional spectral-label term, and it does not prove that the cross support-boundary bank is globally `O(J)` under repeated restriction.

The exact next shared-interface target is now:

> For the account04 source-frontier one-shot block, pay
> `H(S_A|S_B)+min(P_AB,P_BA)` by the folded drift `D_A`, using the account01 all-witness/TC nonreuse bank on low-congestion trigger components and a genuinely different elimination for the high-depth/exceptional cluster.

The tensor-product stress in Section 9 must be preserved: any replacement that charges the full signed cross curvature for this mixture term is structurally too expensive even on an exact product cut.
