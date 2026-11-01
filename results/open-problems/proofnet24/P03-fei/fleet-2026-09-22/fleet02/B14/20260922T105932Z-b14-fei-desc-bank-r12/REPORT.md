# fleet02/B14 — persistent descendant bank and nonreusing selector compiler

**Run:** `20260922T105932Z-b14-fei-desc-bank-r12`  
**Assignment:** FEI-20260922-fleet02-B14, Path A, `Persistent descendant bank`  
**Classification:** `ESSENTIAL_STEP_APPLIED / ALL_DEPTH_NONREUSE_IDENTITY / CONDITIONAL_SELECTOR_COMPILER`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository sources were read, but no authenticated native brain receiver/context was used.

## 0. Fresh state, correction scope, and the first missing implication

This report follows owner programme `FEI-ALL-TEAM-20260922T095941Z`, control revision `2026-09-22.3`, and the B14 assignment card at

`yspennstate/math-research-brain`, commit `ef48b20c75f0d87589f8ec1aaffa41e7340591e9`,

The current universal target is still to prove, for one finite dimension-independent constant,
\[
H(f)\le C I(f)
\]
for every finite uniform-cube Boolean function. The all-gate route reduces this to a symmetric finite-cap potential whose exact gate defect is nonnegative on every genuine Boolean gate and every product bias.

The mandatory correction most directly relevant here is
`FEI-DELTA-20260922-14-SAFE-CONE-SELECTOR-GAP`: a globally gate-safe additive direction does **not** imply that its local selector cocycle is nonnegative after one simply discards positive child slack. The affected broad safe-cone floor is therefore `NEEDS_REVALIDATION`. This report does not use that local inference.

The source-valid one-coordinate defect recursion from `SELECTOR_DEBIT` is retained. For a physical split of coordinate `i` of bias `s`, with Boolean children `G_0,G_1`, output probabilities `q_0,q_1`, parent output probability
\[
q=(1-s)q_0+s q_1,
\]
and physical disagreement probability
\[
d=\Pr(G_0\ne G_1),
\]
write
\[
J_\Gamma=(1-s)\Gamma(q_0)+s\Gamma(q_1)-\Gamma(q).
\]
If `B_i` and `JS_i` are the exact conditional spectral entropy and Jensen--Shannon terms from that source, then
\[
\boxed{
D_\Gamma(G)
=(1-s)D_\Gamma(G_0)+sD_\Gamma(G_1)
+J_\Gamma+d\,[\Gamma(s)+h_2(V_s)]-B_i-JS_i,
}
\tag{0.1}
\]
where `V_s=4s(1-s)`. Its proved selector envelope is
\[
B_i+JS_i-dh_2(V_s)
\le g(d),
\qquad
g(d):=h_2(d)+{2\over\ln2}\min\{d,1-d\}.
\tag{0.2}
\]

The first missing implication is therefore genuinely nonlocal: carry child potential slack through successive physical Shannon expansions without spending any inherited slack twice, and obtain a theorem-level criterion by which the accumulated selector debit can be compared with one root-owned reserve.

This run proves exactly that all-depth accounting theorem.

## 1. Exact additive-direction defect and the local cocycle

Let `eta:[0,1]->R` be symmetric, `eta(p)=eta(1-p)`, with `eta(0)=eta(1)=0`. Define its additive gate defect
\[
E_\eta(G;p)
:=\sum_j {\operatorname{It}_j^t(G;p)\over V_{p_j}}\eta(p_j)-\eta(q_G),
\tag{1.1}
\]
where `q_G=Pr(G=1)` and `It_j^t` is the physical biased influence normalization used by the all-gate source.

For the split above, define the exact local additive cocycle
\[
\boxed{
L_\eta(G,i)
:=(1-s)\eta(q_0)+s\eta(q_1)-\eta(q)+d\,\eta(s).
}
\tag{1.2}
\]

### Proposition 1.1 — exact child-slack recursion
For every Boolean gate, every interior product bias and every physical coordinate split,
\[
\boxed{
E_\eta(G)
=(1-s)E_\eta(G_0)+sE_\eta(G_1)+L_\eta(G,i).
}
\tag{1.3}
\]

### Proof
For every surviving coordinate `j != i`, physical influence averages under restriction:
\[
\operatorname{It}_j^t(G)
=(1-s)\operatorname{It}_j^t(G_0)+s\operatorname{It}_j^t(G_1).
\]
For the revealed coordinate itself,
\[
\operatorname{It}_i^t(G)=V_s d,
\]
so its normalized coefficient in (1.1) is exactly `d`. Subtracting the weighted child defects from the parent defect leaves precisely (1.2). No Jensen inequality and no sign estimate is used. `QED`.

The correction-14 lesson is now explicit: even when `E_eta(H)>=0` for every Boolean gate `H`, equation (1.3) gives only
\[
L_\eta(G,i)
\ge-\big[(1-s)E_\eta(G_0)+sE_\eta(G_1)\big],
\tag{1.4}
\]
not `L_eta>=0`.

## 2. Persistent frontier bank: exact all-depth telescope

Consider any finite adaptive physical restriction tree `T`. Every internal node `v` carries a restricted Boolean gate `G_v`; its selected physical coordinate has conditional bias `s_v`; the two child branch probabilities are exactly `1-s_v` and `s_v`. Let `w_v` be the genuine reach probability from the root. Thus if `v0,v1` are its children,
\[
w_{v0}=w_v(1-s_v),\qquad w_{v1}=w_v s_v.
\tag{2.1}
\]

For any partial expansion of the tree, let `I` be the already-expanded internal nodes and `F` the current frontier. Multiplying (1.3) by `w_v` and cancelling child terms gives:

### Theorem 2.1 — persistent descendant bank
\[
\boxed{
E_\eta(G_{\rm root})
=
\sum_{v\in I}w_vL_\eta(v)
+
\sum_{u\in F}w_uE_\eta(G_u).
}
\tag{2.2}
\]

In particular, if the tree terminates in constants or literals, then `E_eta=0` at every terminal leaf and
\[
\boxed{
E_\eta(G_{\rm root})
=
\sum_{v\in T_{\rm int}}w_vL_\eta(v).
}
\tag{2.3}
\]

This is the requested persistent reserve. At every stage, **unspent slack is owned only by current frontier nodes**. Expanding a frontier node replaces its single bank entry
\[
w_vE_\eta(G_v)
\]
by the local released amount `w_v L_eta(v)` plus the two child-owned banks. Thus no child bank is simultaneously retained and spent.

The pathwise form is a martingale. Along the random branch generated by the physical restriction probabilities, let `G_k` be the gate after `k` reveals and `L_k` the cocycle released at step `k`. Then
\[
\boxed{
M_k:=E_\eta(G_k)+\sum_{r<k}L_r
}
\tag{2.4}
\]
is a martingale. For every bounded stopping time `tau`,
\[
E_\eta(G_{\rm root})
=\mathbb E\left[\sum_{r<\tau}L_r+E_\eta(G_\tau)\right].
\tag{2.5}
\]
No deterministic-depth assumption appears.

## 3. New nonreuse theorem: negative local credit is paid by disjoint descendants

The telescope alone does not say where a negative local cocycle is paid. Global gate safety supplies exactly enough structure to answer that question.

Assume now that `eta` is **globally gate-safe**:
\[
E_\eta(H)\ge0
\tag{3.1}
\]
for every finite Boolean gate `H` and every product-bias vector in the stated domain. Let a finite physical restriction tree terminate in constants/literals.

For each internal node put
\[
a_v:=w_vL_\eta(v).
\]
For a node `v`, let `T_v` be its full descendant subtree. Applying (2.3) to `G_v` and multiplying by `w_v` gives
\[
\boxed{
\sum_{u\in T_v\cap T_{\rm int}}a_u
=w_vE_\eta(G_v)\ge0.
}
\tag{3.2}
\]
Thus every rooted subtree has nonnegative total signed cocycle mass.

### Theorem 3.1 — descendant matching / unique ownership
There exists a bottom-up allocation of positive cocycle mass to negative cocycle mass such that:

1. every negative amount `(-a_v)_+` is paid entirely by positive amounts `a_u>0` from **strict descendants** `u` of `v`;
2. no positive amount is used more than once;
3. after all negative charges inside `T_v` are paid, the unspent positive mass remaining in that subtree is exactly
\[
w_vE_\eta(G_v).
\tag{3.3}
\]
In particular the root leaves exactly `E_eta(G_root)` unspent.

### Proof
Proceed by induction from the leaves upward. A terminal leaf has no cocycle charge and zero residual bank. Assume the statement has been constructed for both child subtrees of an internal node `v`.

By induction, after all negative charges internal to those children have been paid, the two child subtrees contain disjoint unspent supplies whose total is
\[
w_{v0}E_\eta(G_{v0})+w_{v1}E_\eta(G_{v1})\ge0.
\tag{3.4}
\]
If `a_v>=0`, add `a_v` as fresh supply. The total residual is, by (1.3),
\[
a_v+w_{v0}E_\eta(G_{v0})+w_{v1}E_\eta(G_{v1})
=w_vE_\eta(G_v),
\]
which proves the induction step.

If `a_v<0`, then global safety and (1.3) imply
\[
w_{v0}E_\eta(G_{v0})+w_{v1}E_\eta(G_{v1})
=w_vE_\eta(G_v)-a_v
\ge -a_v.
\tag{3.5}
\]
So the already-disjoint unused child supplies are sufficient to pay the entire parent deficit `-a_v`. Consume exactly that amount from those child supplies, in any fixed deterministic order. The remainder is
\[
w_{v0}E_\eta(G_{v0})+w_{v1}E_\eta(G_{v1})+a_v
=w_vE_\eta(G_v)\ge0.
\]
No supply previously used lower in the tree is reused because only the inductively unspent remainder is available at the parent. This proves all three claims. `QED`.

This theorem is strictly stronger than saying the total cocycle sum is nonnegative. It is a constructive nonlocal payment rule with a unique owner for every unit of inherited slack. It repairs the **mechanism** invalidated by correction 14, while not resurrecting that report's unsupported numerical safe-cone floor.

## 4. Exact seed-debit decomposition for a shaped potential

Now write a candidate potential as
\[
\Gamma=\Gamma_b+\lambda\eta,
\qquad \lambda\ge0,
\tag{4.1}
\]
where `Gamma_b` is any symmetric baseline and `eta` is an additive direction. No sign assumption on the baseline gate defect is needed.

Define the exact baseline selector debit
\[
\boxed{
R_b(v)
:=B_v+JS_v-d_vh_2(V_{s_v})
-J_{\Gamma_b}(v)-d_v\Gamma_b(s_v).
}
\tag{4.2}
\]
Then (0.1) is exactly
\[
D_{\Gamma_b}(G_v)
=(1-s_v)D_{\Gamma_b}(G_{v0})+s_vD_{\Gamma_b}(G_{v1})-R_b(v).
\tag{4.3}
\]
Linearity of the potential part and (1.2) give
\[
R_{\Gamma_b+\lambda\eta}(v)
=R_b(v)-\lambda L_\eta(v).
\tag{4.4}
\]

Summing (4.3)--(4.4) over a finite physical tree yields the central theorem of this run.

### Theorem 4.1 — exact root-owned descendant-bank identity
For every finite adaptive physical restriction tree with frontier `F`,
\[
\boxed{
\begin{aligned}
D_{\Gamma_b+\lambda\eta}(G_{\rm root})
={}&\sum_{u\in F}w_uD_{\Gamma_b+\lambda\eta}(G_u)\\
&+\lambda\left(E_\eta(G_{\rm root})-\sum_{u\in F}w_uE_\eta(G_u)\right)
-\sum_{v\in I}w_vR_b(v).
\end{aligned}
}
\tag{4.5}
\]
If the tree terminates in constants/literals, both terminal terms vanish and
\[
\boxed{
D_{\Gamma_b+\lambda\eta}(G_{\rm root})
=\lambda E_\eta(G_{\rm root})
-\sum_{v\in T_{\rm int}}w_vR_b(v).
}
\tag{4.6}
\]

Equation (4.6) is a nonreuse theorem, not a local-sign claim. The entire safe-direction contribution available to the completed tree is **one root-owned bank** `lambda E_eta(root)`. A proof may decide at which descendant nodes to release it, but it may not spend `lambda E_eta(root)` at a parent and then again spend the unchanged child defect as if it were new credit.

For several safe directions `eta_r` with coefficients `lambda_r>=0`, (4.6) simply becomes
\[
D_{\Gamma_b+\sum_r\lambda_r\eta_r}(G_{\rm root})
=
\sum_r\lambda_rE_{\eta_r}(G_{\rm root})
-\sum_vw_vR_b(v).
\tag{4.7}
\]
Each direction has its own root-owned bank and its own unique descendant matching.

## 5. Nonlocal Shannon-payment compiler

The exact debit `R_b` still contains the hard conditional spectrum. The selector-debit theorem (0.2) gives a candidate-independent upper bound while preserving the exact potential Jensen term. Define
\[
\boxed{
U_b(v)
:=g(d_v)-J_{\Gamma_b}(v)-d_v\Gamma_b(s_v),
}
\tag{5.1}
\]
with `g` from (0.2). Then
\[
R_b(v)\le U_b(v).
\tag{5.2}
\]
Combining this with (4.6) gives:

### Theorem 5.1 — banked selector compiler
For every finite adaptive physical tree terminating in constants/literals,
\[
\boxed{
D_{\Gamma_b+\lambda\eta}(G_{\rm root})
\ge
\lambda E_\eta(G_{\rm root})
-
\sum_{v\in T_{\rm int}}w_vU_b(v).
}
\tag{5.3}
\]
Therefore it is sufficient to construct, for each target gate, a realizable terminating physical policy `pi` satisfying
\[
\boxed{
\mathbb E_\pi\sum_v U_b(v)
\le \lambda E_\eta(G_{\rm root}).
}
\tag{5.4}
\]
This is all-depth, all-arity and uses actual restriction probabilities. It keeps the full baseline potential Jensen term `J_{Gamma_b}` and spends the safe-direction reserve exactly once.

The key distinction from the refuted local argument is that (5.4) permits one node's positive child slack to pay an ancestor's adverse selector debit. The bookkeeping theorem guarantees no descendant credit is reused.

## 6. Specialization to the current shaped candidate and the balanced endpoint

The current source-pinned shaped candidate is
\[
\Gamma_*(p)=\Gamma^\dagger(p)+\lambda_*\eta_{\epsilon_*}(p),
\]
with
\[
\epsilon_*=0.0226886585855132,
\qquad
\lambda_*=0.037443614456434,
\]
\[
\eta_{\epsilon}(p)=1-(1-2p)^4-\epsilon\,[4p(1-p)]^3,
\]
and source-reported center
\[
C_*=6.5584452830718245\ldots .
\]
The source proves universal gate safety of `eta_{epsilon_*}` by a continuum Bernstein certificate. This candidate remains `CANDIDATE_UNPROVED`; no all-gate sign is claimed here.

Take in Theorem 5.1
\[
\Gamma_b=\Gamma^\dagger,
\qquad \eta=\eta_{\epsilon_*},
\qquad \lambda=\lambda_*.
\tag{6.1}
\]
Using the refuted `Gamma^dagger` as an algebraic **baseline** is legitimate: no universal nonnegativity of the baseline is assumed anywhere in (4.5)--(5.4).

On a balanced uniform Boolean root, every input bias and the output bias equal `1/2`. Since
\[
\eta_{\epsilon_*}(1/2)=1-\epsilon_*,
\]
we have the exact root bank
\[
\boxed{
E_{\eta_{\epsilon_*}}(f)
=(1-\epsilon_*)[I(f)-1].
}
\tag{6.2}
\]
Numerically,
\[
\lambda_*(1-\epsilon_*)
=0.03659406907182439\ldots .
\tag{6.3}
\]
Thus a sufficient balanced-uniform restriction criterion for the current shaped candidate is
\[
\boxed{
\exists\pi_f:\quad
\mathbb E_{\pi_f}\sum_v U_{\Gamma^\dagger}(v)
\le
0.03659406907182439\ldots\,[I(f)-1].
}
\tag{6.4}
\]
For exact work, (6.4) is kept in the symbolic form
\[
\lambda_*(1-\epsilon_*)[I(f)-1].
\]
By the source `BALANCED` equivalence, proving (6.4) for every balanced Boolean function would already imply the same-constant uniform-cube FEI statement for `Gamma_*`. This is conditional only; (6.4) is the first unpaid implication after this run.

The value of (6.4) is conceptual and technical: it turns the vague instruction “use descendant slack” into one explicit expected tree inequality with a fixed root budget, actual branch weights, the exact Jensen term and no repeated safe-direction credit.

## 7. Named other-account result consumed and applied

This run consumes the latest compatible completed `fleet03/B14` result available at startup:

`yspennstate/math-open-problems`, commit `dd372aa67dfdb1b5cce6b807c15e02b377d42f9b`,
`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B14/20260922T094337Z-mux-maxvar-credit/REPORT.md`, Section 2.

Its candidate-independent MUX currency identity is
\[
W_M=\omega_0+\omega_1,
\qquad
\omega_j={t(1-t)V_j\over4},
\tag{7.1}
\]
and the max-variance first data reveal satisfies
\[
\omega_{\rm first}\ge {W_M\over2},
\qquad
W_M=\omega_{\rm first}+\mathbb E W_{\rm child}.
\tag{7.2}
\]

Apply Theorem 2.1 to the quadratic safe direction
\[
\eta_{\rm quad}(p)=p(1-p).
\]
Its additive gate defect is exactly
\[
E_{\eta_{\rm quad}}(G)
={1\over4}\sum_i\operatorname{It}_i^t(G)-q(1-q)
=W_G.
\tag{7.3}
\]
Therefore the partner identity (7.2) is precisely the two-stage specialization of our persistent bank:
\[
L_{\eta_{\rm quad}}(M,D_j)=\omega_j,
\qquad
\mathbb E E_{\eta_{\rm quad}}(G_{\rm child})=W_M-\omega_j.
\tag{7.4}
\]
Choosing the max-variance data bit releases at least half the root quadratic bank immediately and leaves **at most half** with the binary children. The second physical data reveal spends the remaining child-owned bank and terminalizes to constants/literals. No unit of `W_M` is spent twice.

This is an exact application of a named other-account result to the B14 target. I use only its candidate-independent physical currency theorem; its old `Gamma^dagger` candidate discussion is superseded by the current shaped-candidate state.

## 8. Why this is more than the previous martingale observation

The previous B14 attempt identified the basic cocycle martingale but did not supply a complete unique-ownership payment theorem or an exact compiler against the source selector debit. The new content here is:

1. the frontier-bank identity (2.2) for every partial adaptive tree;
2. the constructive descendant matching theorem (Theorem 3.1), proving that every adverse local safe-direction cocycle is paid by disjoint positive strict-descendant mass under global gate safety;
3. the exact seed-debit decomposition (4.6), showing that a shaped direction contributes only one root-owned amount no matter how many restriction levels are used;
4. the all-depth banked selector compiler (5.3)--(5.4), which keeps the exact potential Jensen term and the true restriction probabilities;
5. the explicit balanced-uniform current-candidate target (6.4).

This is not a fixed-depth check, fixed-arity scan, raw-U4 argument, unweighted-L2 payment, or resurrection of any refuted scalar lift.

## 9. What remains unpaid

**FULL-PROBLEM CHANGE:** none. Full uniform-cube FEI remains open.

**MECHANISM CHANGE:** yes. The correction-14 local-sign gap is replaced by an exact all-depth descendant-bank mechanism with constructive nonreuse.

The first missing implication is now the concrete policy bound (5.4), and for the current shaped candidate the balanced specialization (6.4):
\[
\exists\pi_f\quad
\mathbb E_{\pi_f}\sum_v
\left[
 h_2(d_v)+{2\over\ln2}\min\{d_v,1-d_v\}
 -J_{\Gamma^\dagger}(v)-d_v\Gamma^\dagger(s_v)
\right]
\le
\lambda_*(1-\epsilon_*)[I(f)-1].
\tag{9.1}
\]

A successful next step must prove this for all balanced Boolean `f`, or replace the selector envelope by a sharper exact information term while keeping the same nonreuse ledger. A finite gate scan or a new local selector name would not close the implication.

## 10. Verification scope and privacy

The identities (1.3), (2.2), (4.5) and (4.6) are algebraic consequences of the source-exact physical influence and defect recursions. As a regression check during this run, Proposition 1.1 was evaluated numerically on 1,000 random Boolean gates through three variables at random interior product biases for the current `eta_{epsilon_*}`; the maximum absolute discrepancy was `4.44e-16`, consistent with floating roundoff. This is only a sanity check, not the proof.

This report contains only FEI mathematics, logical account/slot labels and source-pinned repository references. It contains no scheduler identifiers, credentials, machine paths, unrelated private data, benchmark gold, email/Drive content, public-posting action, paid calls, remote workflow dispatch or permission changes.
