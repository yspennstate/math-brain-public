# B15 — exact child-slack Shannon split and a 2e-5 axial prime collar

**Classification:** `ESSENTIAL_STEP_APPLIED / CHILD_SLACK_PACKET_TRANSPORT / AXIAL_PRIME_COLLAR`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 0. Candidate, old gap, and what changes

This run binds to the current B-lead candidate `LIMIT-PRIME-GATE-LIFT-v1`:

\[
C^\dagger=6.521851214,\qquad
\Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p).
\]

For a Boolean gate `G` at product bias `p`, write

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]

The exact universal missing implication is still

\[
D_{\Gamma^\dagger}(P;p)\ge0
\quad\text{for every finite composition-prime Boolean gate }P
\text{ and every interior product bias }p.
\tag{0.1}
\]

The newest B-lead theorem proves every essential five-input composition-prime gate has central reserve at least

\[
D_{\Gamma^\dagger}(P;1/2^5)\ge0.004906502214.
\]

I use the weaker exact decimal floor

\[
\delta_0:=0.0049065.
\tag{0.2}
\]

The named other-account result consumed and applied is account02/B15

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0704Z-gibbs-kl-prime-tube/REPORT.md`.

It proves the exact common-residual factorization

\[
D_\Gamma(G;p)=v\left[
D_{\rm KL,2}(w^+\|\nu_p^+)
-\log_2{Z-1\over x_q}
\right]
\tag{0.3}
\]

and proves that the packet statistic

\[
T(S)=\left(|\widehat G_p(S)|,\prod_{i\in S}x_i\right)
\]

is KL-sufficient. Thus the object below is the same versioned all-gate Shannon residual, not a renamed norm or a non-Boolean relaxation. That peer also proved a full sup-norm prime tube of radius `4.4e-6`, retaining an exact negative KL transport credit.

**New inference this run.** If only one of the five input biases moves away from `1/2`, the actual biased Fourier transform has a much sharper two-coordinate structure than the generic five-coordinate transform estimate. Retaining both the child slacks and the negative relative-entropy credit gives a source-valid radius

\[
\boxed{|p_k-1/2|\le2\times10^{-5}}
\]

along **every coordinate axis** for every essential five-input composition-prime gate. This is more than 4.54 times the peer's full-box radius in the axial direction. It does not enlarge the full five-dimensional box and does not prove FEI.

## 1. Exact child-slack Shannon decomposition

Fix a coordinate `k`. Put all other input biases at `1/2`, and let the last bias be `t`. Let `G_0,G_1` be the two restrictions of `G` obtained by fixing input `k`, and let

\[
q_b=\Pr[G_b=-1],\qquad H_b=\widetilde H(G_b),
\qquad d=\Pr[G_0\ne G_1],
\]

where probabilities for the first four inputs are uniform. Write

\[
A(t)=\Gamma^\dagger(t)+h_2(V_t).
\]

For `j\ne k`, biased influence is the branch mixture

\[
\operatorname{It}_j(G;t)
=(1-t)\operatorname{It}_j(G_0)+t\operatorname{It}_j(G_1),
\]

while

\[
\operatorname{It}_k(G;t)=V_t d.
\]

The genuine biased spectral entropy obeys the exact Shannon split

\[
\widetilde H_G(t)
=(1-t)H_0+tH_1
+JS_t(\mu_0,\mu_1)+B_k(t),
\tag{1.1}
\]

where `mu_b` is the actual four-bit spectral law of `G_b`, `JS_t` is its weighted Jensen--Shannon divergence, and `B_k(t)=H(S_k\mid S_{-k})` is the conditional entropy of the last spectral bit. Consequently

\[
\boxed{
D_G(t)
=(1-t)D_0+tD_1+R_k(t),
}
\tag{1.2}
\]

with

\[
\begin{aligned}
R_k(t)=&\;dA(t)+(1-t)\Gamma^\dagger(q_0)+t\Gamma^\dagger(q_1)
-\Gamma^\dagger((1-t)q_0+tq_1)\\
&-JS_t(\mu_0,\mu_1)-B_k(t).
\end{aligned}
\tag{1.3}
\]

This identity explains precisely why the owner's already-refuted naive arity induction loses information: it tries to demand `R_k(t)>=0` after discarding `(1-t)D_0+tD_1`. Here the child slack is retained exactly.

The account01/B17 all-five-input central theorem, applied to a four-input gate padded by one dummy input and then lifted from `0.01` to `0.268204856`, gives

\[
0\le D_b\le C^\dagger I(G_b)\le4C^\dagger.
\tag{1.4}
\]

The same inequality gives

\[
0\le\Gamma^\dagger(q_b)\le4C^\dagger.
\tag{1.5}
\]

No child cost is omitted.

## 2. Exact one-coordinate Fourier transport

Set

\[
s=t-1/2,\qquad r=2s.
\]

For each `A subset [5]\{k}`, denote the **central** uniform Fourier coefficients by

\[
c_A=\widehat G_{1/2^5}(A),\qquad
d_A=\widehat G_{1/2^5}(A\cup\{k\}).
\]

Equivalently, if `u_A,v_A` are the uniform Fourier coefficients of the two branch functions, then

\[
c_A={u_A+v_A\over2},\qquad d_A={v_A-u_A\over2}.
\]

A direct calculation in the normalized biased basis gives the exact pair transport

\[
\boxed{
\widehat G_t(A)=c_A+r d_A,
\qquad
\widehat G_t(A\cup\{k\})=\sqrt{1-r^2}\,d_A.
}
\tag{2.1}
\]

Thus no off-center integrality is assumed. The only lattice input is the true central Boolean one: every nonzero five-bit uniform Fourier coefficient is an integer multiple of `1/16`, hence its squared mass is at least `1/256`.

Let `w^0` and `w` be the central and perturbed spectral laws, and let

\[
J=\{S:w^0(S)>0\},\qquad
\zeta=\sum_{S\notin J}w(S).
\]

Parseval gives

\[
\sum_A(c_A^2+d_A^2)=1.
\]

From (2.1), new atoms can occur only in the first member of a pair with `c_A=0`; therefore

\[
\boxed{\zeta\le r^2.}
\tag{2.2}
\]

Moreover

\[
\begin{aligned}
\|w-w^0\|_1
&\le2|r|\sum_A|c_Ad_A|+2r^2\sum_Ad_A^2\\
&\le |r|+2r^2,
\end{aligned}
\tag{2.3}
\]

because `sum |c_A d_A| <= sqrt(sum c_A^2 sum d_A^2) <=1/2`.

Condition `w` on `J` and call the resulting probability law `rho`. Then

\[
(1-\zeta)\|\rho-w^0\|_1
\le\|w-w^0\|_1+\zeta
\le |r|+3r^2.
\tag{2.4}
\]

## 3. Keep the negative information credit

For `S in J`, put

\[
\ell_S=\log_2{1\over w^0(S)}.
\]

The central Boolean lattice gives `0<=ell_S<=8`. The entropy shift on the old support has the **exact** identity

\[
H(\rho)-H(w^0)
=\sum_{S\in J}(\rho_S-w^0_S)\ell_S
-D_{\rm KL,2}(\rho\|w^0).
\tag{3.1}
\]

Since the signed mass difference has total mass zero, its pairing with a function of range eight is at most eight times total variation. Multiplying by `1-zeta` and using (2.4),

\[
(1-\zeta)\sum(\rho-w^0)\ell
\le4|r|+12r^2.
\tag{3.2}
\]

The leakage law lives on at most sixteen genuinely new atoms, because only the no-`k` member of each Fourier pair can be born from zero. Hence

\[
\boxed{
H(w)-H(w^0)
\le
4|r|+16r^2+h_2(r^2)
-(1-\zeta)D_{\rm KL,2}(\rho\|w^0).
}
\tag{3.3}
\]

This is the conditional packet decomposition used below. It preserves the negative KL credit exactly. It uses the true central physical lattice only where valid and does not assert any physical projection integrality off center.

## 4. Apply the decomposition to the live defect

The source-valid candidate regularity already proved in the earlier B15 central-tube report is

\[
|(\Gamma^\dagger)'|<85
\tag{4.1}
\]

on every input/output interval needed here. Indeed a nonconstant five-bit gate has central output mass `m/32`, and moving a single input bias by `epsilon` moves that output mass by at most `epsilon`; at `epsilon<=2e-5` the smaller output representative remains strictly above `1/64`.

Let `epsilon=|s|`. Compare (1.2) at `t=1/2+s` and `t=1/2`.

* The child-slack mixture can lose at most `4 C^dagger epsilon` by (1.4).
* The last-coordinate term `dA(t)` can lose at most `85 epsilon`: `h_2(V_t)>=0` and `d<=1`.
* The branch-potential mixture can lose at most `4 C^dagger epsilon` by (1.5).
* The output potential can lose at most `85 epsilon`.
* The branch entropy interpolation contributes at worst `4 epsilon`, since `0<=H_b<=4`.
* By (3.3), the actual spectral entropy can increase by at most

\[
8\epsilon+64\epsilon^2+h_2(4\epsilon^2)
-(1-\zeta)D_{\rm KL,2}(\rho\|w^0).
\]

Therefore every essential five-input composition-prime gate obeys

\[
\boxed{
\begin{aligned}
D_{\Gamma^\dagger}(P;p)
\ge&\;\delta_0
-(8C^\dagger+182)\epsilon
-64\epsilon^2-h_2(4\epsilon^2)\\
&+(1-\zeta)D_{\rm KL,2}(\rho\|w^0),
\end{aligned}
}
\tag{4.2}
\]

whenever exactly one input bias differs from `1/2` by `epsilon`.

This is a direct estimate on the same gate defect that account02/B15 factorizes as the packet/price Gibbs-KL excess. It retains, rather than discards, the transport relative-entropy credit.

## 5. Certified radius `2e-5`

Set

\[
\epsilon_0=2\times10^{-5},
\qquad z=4\epsilon_0^2=1.6\times10^{-9}.
\]

The elementary inequality

\[
h_2(z)\le z\log_2(e/z)
\]

is enough. Since `e<3` and

\[
2^{31}z=3.4359738368>3,
\]

we have

\[
h_2(z)<31z=4.96\times10^{-8}.
\]

Using exact decimal/rational arithmetic,

\[
(8C^\dagger+182)\epsilon_0
=0.004683496194240,
\]

\[
64\epsilon_0^2=0.000000025600000,
\qquad
31z=0.000000049600000.
\]

Hence the total worst-case loss in (4.2), before using any positive KL credit, is strictly less than

\[
0.004683571394240.
\]

Subtracting from the deliberately weakened central prime reserve gives

\[
\boxed{
\delta_0-0.004683571394240
=0.000222928605760>0.
}
\tag{5.1}
\]

Therefore:

### Theorem B15-AXIS-CHILD-SLACK-KL

For every essential composition-prime five-input Boolean gate `P`, every coordinate `k`, and every interior bias vector satisfying

\[
p_j=1/2\quad(j\ne k),
\qquad
\boxed{|p_k-1/2|\le2\times10^{-5}},
\tag{5.2}
\]

the fixed candidate `LIMIT-PRIME-GATE-LIFT-v1` satisfies

\[
\boxed{
D_{\Gamma^\dagger}(P;p)
\ge
0.000222928605760
+(1-\zeta)D_{\rm KL,2}(\rho\|w^0)
>0.
}
\tag{5.3}
\]

Equivalently, any five-input composition-prime falsifier lying on a coordinate axis through the uniform point must have

\[
\boxed{|p_k-1/2|>2\times10^{-5}.}
\]

The adjacent checker performs only the deterministic rational arithmetic in this section. No finite truth-table sweep is needed for the new implication; the finite central reserve is imported from the already-completed rigorous certificate and prime-orbit theorem.

## 6. Dead envelope and counterexample status

The same deliberately coarse envelope does **not** certify `epsilon=2.1e-5`:

\[
\delta_0-	ext{loss}_{\rm envelope}(2.1\times10^{-5})
=-1.1253911952\times10^{-5}<0.
\]

This is **not** a Boolean counterexample to the gate inequality. It is exact negative information about this proof envelope: improving the radius further requires spending more structure instead of rounding every potential/child term independently.

No source-valid counterexample to `LIMIT-PRIME-GATE-LIFT-v1` was produced in this run.

## 7. Exact handoff fields and implication to FEI

**candidate_version:** `LIMIT-PRIME-GATE-LIFT-v1`, `C^dagger=6.521851214`, `Gamma^dagger=Gamma_0+0.268204856 p(1-p)`.

**prior_missing_implication:** prove `D_{Gamma^dagger}(P;p)>=0` for every finite composition-prime gate and every interior bias.

**consumed_peer_artifact:** account02/B15 `20260922T0704Z-gibbs-kl-prime-tube/REPORT.md`; applied its exact Gibbs-KL/packet-price factorization and its requirement to retain negative KL information on the same normalized gate residual.

**new_proved_inference:** exact child-slack Shannon decomposition plus exact one-coordinate Fourier-pair transport proves the live gate inequality for every essential five-input prime on all five central coordinate axes out to radius `2e-5`, with explicit reserve (5.3).

**replacement_obligation:** the five-input frontier now consists of (i) off-axis bias vectors outside the peer's `4.4e-6` full cube and (ii) axial points beyond `2e-5`; higher arity remains fully open. To push the axis farther, keep the Gibbs packet/price KL and couple the two `85 epsilon` potential drifts instead of paying them separately, or derive exact source secants on the finite branch/output dyadic values.

**next_recipient:** `account03/B18` (Campaign-B lead); secondary compatible recipient `account02/B15` for the packet/price KL continuation.

**implication_to_full_FEI:** direct but partial. The all-gate equivalence plus composition cocycle would give full FEI with finite constant `C^dagger` only after the same gate inequality is proved for **every** composition-prime gate at **every** interior product bias. That universal step is still open.

## 8. Verification / scope

Checker: `check_axis_child_slack.py`. Captured output: `check_axis_child_slack.out`; result `PASS`.

The report uses only FEI mathematics and sanitized repository-relative provenance. It contains no credentials, scheduler identifiers, machine paths, unrelated private material, email/Drive actions, public posting, paid model/API/Codex use, workflow dispatch or permission change.
