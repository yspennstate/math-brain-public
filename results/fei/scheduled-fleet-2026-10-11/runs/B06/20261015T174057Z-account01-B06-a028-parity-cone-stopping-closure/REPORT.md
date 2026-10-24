# B06 / A028 — parity-cone debt pays a shared-data stopping splice

**Run:** `20261015T174057Z-account01-B06-a028-parity-cone-stopping-closure`  
**Primary packet:** A028 — Stopping-tree payment  
**Retained ownership:** A026–A030 (only A028 is primary in this run)  
**Stable gap:** `G-GU-STOPPING-RESIDUAL`  
**Fixed endpoint:** 2026-10-21T19:15:57Z  
**Actual model/effort:** UNKNOWN

**Status:** PROVED conditional closure theorem for a sign-flip shared-data family; the universal GU inequality and full FEI remain OPEN. Independent review of this new claim is pending.

## 1. Frozen target and prior bound

The sole universal target is
\[
G(f)\le aI(f)+bU(f)
\]
for every genuine Boolean \(f:\{-1,1\}^n\to\{-1,1\}\), all finite \(n\), and one dimension-independent pair \(a\ge0,\ 0\le b<1\). Here
\[
p(S)=\widehat f(S)^2,\quad \pi(S)=\sum_{T\supseteq S}p(T),\quad
U(f)=\sum_{p(S)>0}p(S)\log_2\frac{\pi(S)}{p(S)},
\]
\[
I(f)=\sum_S|S|p(S),\qquad
\Delta_iU(f)=U(f)-\tfrac12(U(f_{i,+})+U(f_{i,-})),\quad
G(f)=\sum_i\Delta_iU(f).
\]
Constants have \(I=U=G=0\) and are handled separately.

The newest own full report, `20261014T083500Z-account01-B06-a028-two-gate-reuse`, proved for \(F=q(x_1,x_2)h(y)\) with disjoint gate/core coordinates that the reused two-level tree has paid residual \(\mathcal R\le I(q)\), exact terminal \(U\) and influence, and GU inheritance \(G(F)\le\max(a,2-b)I(F)+bU(F)\) when \(h\) has GU. Its first unsupported line was a shared-data collision. The preceding paid-\(U\) stopping theorem was independently accepted by B18 only conditionally: terminal \(U(\ell)\le\kappa I(\ell)\) and aggregate paid residual \(\mathcal R\le A\Pi_I+bU\) must be established for each root. It is not a universal tree-existence theorem.

## 2. New exact candidate: sign-flip shared-data splice

Let \(h:\{-1,1\}^n\to\{-1,1\}\) be genuine Boolean and let \(J\subseteq[n]\). Introduce one selector coordinate \(x\) and define
\[
F_J(x,y)=h(z),\qquad z_j=\begin{cases}xy_j,&j\in J,\\y_j,&j\notin J.\end{cases}
\]
Thus the selector and every data coordinate in \(J\) are physically shared; the two selector children are \(h(y)\) and \(h(y^J)\), where \(y^J\) flips all coordinates in \(J\).

Write
\[
q_J=\sum_{|S\cap J|\ {\rm odd}}p_h(S),\qquad
\pi_{J,\mathrm{odd}}(S)=\sum_{\substack{T\supseteq S\\|T\cap J|\ {\rm odd}}}p_h(T),
\]
and
\[
E_J=\sum_{\substack{|S\cap J|\ {\rm odd}\\p_h(S)>0}}
p_h(S)\log_2\frac{\pi_h(S)}{\pi_{J,\mathrm{odd}}(S)}.
\]
For each summand, \(\pi_{J,\mathrm{odd}}(S)\ge p_h(S)>0\) and \(\pi_{J,\mathrm{odd}}(S)\le\pi_h(S)\), so \(E_J\ge0\). The new exact identities are
\[
\boxed{U(F_J)=U(h)-E_J,\qquad I(F_J)=I(h)+q_J,\qquad
\Delta_xU(F_J)=-E_J.}
\tag{1}
\]
In particular \(q_J=\operatorname{Inf}_x(F_J)\) is a real influence contribution, not a formal query count.

### Proof of (1)

For a Fourier support \(S\) of \(h\), substitution \(z_j=xy_j\) gives the support map
\[
\phi_J(S)=S\cup\{x\}\quad\text{if }|S\cap J|\text{ is odd},\qquad
\phi_J(S)=S\quad\text{otherwise}.
\]
The map is injective and preserves the \(y\)-part \(S\); the squared mass at \(\phi_J(S)\) is exactly \(p_h(S)\). If \(|S\cap J|\) is even, \(\phi_J(S)=S\) has no \(x\), so its upper cone receives exactly the masses \(p_h(T)\) for \(T\supseteq S\); hence \(\pi_{F_J}(\phi_J(S))=\pi_h(S)\). If \(|S\cap J|\) is odd, the upper cone must also contain \(x\), so only \(T\supseteq S\) with odd \(|T\cap J|\) qualify; hence
\[
\pi_{F_J}(\phi_J(S))=\pi_{J,\mathrm{odd}}(S).
\]
Splitting the defining sum for \(U(F_J)\) into the even and odd parts gives \(U(F_J)=U(h)-E_J\). Since \(|\phi_J(S)|=|S|+\mathbf1_{\{|S\cap J|\text{ odd}\}}\), summing \(p_h(S)|\phi_J(S)|\) gives \(I(F_J)=I(h)+q_J\). Finally, \(F_{J,x=+}=h(y)\) and \(F_{J,x=-}=h(y^J)\); input sign flips preserve every squared Fourier mass and therefore preserve \(U\). Thus \(\Delta_xU=U(F_J)-U(h)=-E_J\).

## 3. Main theorem: closure of a fully paid stopping certificate

For a finite physical restriction tree \(\mathcal T\), let
\[
\rho_i(g)=\Delta_iU(g)-K_i^{(0)}(g),\quad
\mathcal R(\mathcal T)=\sum_{v\in\mathcal T^\circ}p_v\rho_{i_v}(f_v),\quad
\Pi_I(\mathcal T)=\sum_{v\in\mathcal T^\circ}p_v\operatorname{Inf}_{i_v}(f_v).
\]
Here \(K_i^{(0)}\ge0\) is the empty-upper-set KL row in the exact signed restriction identity. The source-reviewed telescopes are
\[
\sum_vp_v\Delta_{i_v}U(f_v)=U(f)-\mathbb E_\ell U(f_\ell),\qquad
\Pi_I(\mathcal T)=I(f)-\mathbb E_\ell I(f_\ell).
\]

**Theorem.** Fix \(A,\kappa\ge0\) and \(0\le b<1\). Suppose \(h\) has a finite physical tree \(\mathcal T_h\) such that every leaf obeys \(U(h_\ell)\le\kappa I(h_\ell)\) and
\[
\mathcal R(\mathcal T_h)\le A\Pi_I(\mathcal T_h)+bU(h).
\]
Then \(F_J\) has a tree with the same constants and the same leaf certificate:
\[
\boxed{\mathcal R(\mathcal T_{F_J})\le
A\Pi_I(\mathcal T_{F_J})+bU(F_J).}
\tag{2}
\]
No disjointness of \(J\) from the core is assumed, and the same physical data coordinates can be queried on both incomparable selector branches.

**Proof.** If \(q_J=0\), the Fourier expansion of \(h\) contains only supports of even \(J\)-parity, whence \(h(y^J)=h(y)\) and \(F_J\) is independent of \(x\); use \(\mathcal T_h\) directly. Otherwise query \(x\) at the root. Its children are \(h\) and an input-sign-flipped copy \(h(y^J)\). Run \(\mathcal T_h\) on the first child and the coordinate-sign-flipped tree on the second. Input sign flips permute branch labels but preserve \(p,\pi,U,I,\Delta_iU,K_i^{(0)},\rho_i\), and influence. Therefore the child trees have the same expected terminal \(U,I\), the same aggregate residual \(\mathcal R_h\), and the same influence budget \(\Pi_h\).

By (1), the root has influence \(q_J\), and
\[
\rho_x(F_J)=\Delta_xU(F_J)-K_x^{(0)}(F_J)
=-E_J-K_x^{(0)}(F_J)\le-E_J.
\]
The exact tree ledgers give
\[
\Pi_I(\mathcal T_{F_J})=q_J+\Pi_h,\qquad
U(F_J)=U(h)-E_J.
\]
Thus
\[
\begin{aligned}
\mathcal R(\mathcal T_{F_J})
&\le -E_J+A\Pi_h+bU(h)\\
&=A(q_J+\Pi_h)+b(U(h)-E_J)
-\underbrace{Aq_J+(1-b)E_J}_{\text{nonnegative amount subtracted}}\\
&\le A\Pi_I(\mathcal T_{F_J})+bU(F_J),
\end{aligned}
\]
because \(Aq_J+(1-b)E_J\ge0\). Each terminal is a sign-flipped copy of a certified \(h_\ell\), so its \(U\) and \(I\) are unchanged. The influence telescope is exact: the root contributes \(q_J\), and the child trees contribute \(\Pi_h=I(h)-\mathbb E I(h_\ell)\). This proves (2), retaining the entire terminal \(U\), terminal influence, normalization, signed KL row, and the real root influence decrement.

## 4. Full implication to FEI and explicit relation to GU

The independently reviewed paid-\(U\) theorem states that a **universal** tree certificate with fixed \(A,\kappa,b\), \(b<1\), implies
\[
U(f)\le\frac{\max\{A,\kappa\}I(f)+(2/\ln2)\operatorname{Var}(f)}{1-b}
\le\frac{\max\{A,\kappa\}+2/\ln2}{1-b}I(f).
\]
The original Theorem G reduction, read in `gu/U-universal/NOTES.md`, is
\[
H(f)\le2(I(f)-\operatorname{Var}(f))+2U(f)\le2I(f)+2U(f).
\]
Consequently a universal paid-tree theorem gives
\[
H(f)\le\left(2+\frac{2(\max\{A,\kappa\}+2/\ln2)}{1-b}\right)I(f).
\]
This is dimension-independent but is only conditional until the tree and aggregate residual exist for every Boolean root.

The direction from GU to a paid tree is also explicit. If the target GU pair \(G\le aI+bU\) holds universally, the reviewed restriction induction gives \(U\le aI/(1-b)\). At every nonconstant node, \(\sum_i\Delta_iU=G\le aI+bU\le [a/(1-b)]I\); since \(\sum_i\operatorname{Inf}_i=I\), some relevant coordinate satisfies \(\Delta_iU\le[a/(1-b)]\operatorname{Inf}_i\). Querying such a coordinate until constants gives a finite tree with terminal \(U=0\) and \(\mathcal R\le[a/(1-b)]\Pi_I\), since \(\rho_i=\Delta_iU-K_i^{(0)}\le\Delta_iU\). Thus universal GU implies the stopping certificate with \(A=a/(1-b),\kappa=b_{\rm stop}=0\). The converse is not claimed: a universal paid tree yields FEI but does not by itself prove GU.

For the single-coordinate case \(J=\{j\}\), \(E_J=0\), because every \(T\supseteq S\) preserves the parity of \(S\cap J\) when \(S\) contains \(j\). Direct restriction accounting then gives
\[
G(F_{\{j\}})=G(h)-\Delta_jU(h),\quad
I(F_{\{j\}})=I(h)+\operatorname{Inf}_j(h),\quad U(F_{\{j\}})=U(h).
\]
So same-pair GU inheritance requires an additional lower bound \(\Delta_jU(h)\ge-a\operatorname{Inf}_j(h)\); it cannot be asserted from tensor additivity. For example, the three-bit truth-table mask 24 has \(U=1/2\), \(I=3/2\), \(\Delta_0U=-1/2\), and \(\operatorname{Inf}_0=1/2\). Its one-coordinate shear has \(U=1/2\), \(I=2\), \(G=-1\) versus \(G(h)=-3/2\). This is a local-transfer obstruction, not a GU or FEI counterexample.

## 5. A tempting stronger payment is refuted, so the mechanism changes

The auxiliary claim \(E_J\le4q_J\) would pay the parity-cone debt by selector influence alone. It is false: for the four-bit Boolean truth-table mask 5737 and \(J=[4]\), direct Walsh computation gives
\[
E_J=0.5907006944895206,\qquad q_J=0.125,\qquad E_J/q_J=4.7256055559161645.
\]
This refutes only the coefficient-four auxiliary payment, not every finite \(E_J\le Cq_J\) bound and not GU/FEI. The proof above avoids that loss entirely: the root's negative \(U\)-drift pays \(E_J\) with the strict factor \(1-b\), while the actual influence \(q_J\) is retained in the telescope. That is the substantive mechanism change.

## 6. Executed validation

`python verify_sign_shear.py` uses exact integer Walsh numerators and exact `Fraction` squared masses; only logarithms are float64 diagnostics. There is no random seed. It exhausts all Boolean truth tables through dimension three and all \(J\subseteq[n]\) (2,120 pairs), checking the parent \(U\) identity, influence identity, selector decrement, and the single-coordinate \(G\) identity. It separately checks the coefficient-four auxiliary failure at the stated four-bit witness.

The output is saved verbatim in `CHECK.out`. Finite verification audits the identities and implementation; the proofs above are the all-dimensional argument. The universal GU residual remains OPEN.

## 7. Sources actually read

See `SOURCES.md` for repository, branch, path, blob pins, and the prior response-only missing-delivery check. The current focus and ORDER supersede older broad targets; A028 remains the sole primary packet and A026–A030 remain retained.

## 8. Next mathematical action

Extend the sign-flip selector pair \((h,h^J)\) to an arbitrary shared-data pair \((h_+,h_-)\) by deriving the exact parent-to-child upper-cone transport for the first non-flat collision. Keep \(-\Gamma_i\), every terminal \(U\), and the exact influence decrement. The acceptance test is a dimension-independent bound for the paid residual in (2), not a GU assumption at each node. Do not claim universal tree existence, universal GU, or full FEI from this closure result.

**Persistence:** canonical and Math Brain mirror are written and read back only when the final `DELIVERY_READBACK.json` receipt and post-receipt checks confirm them. Model/effort remains UNKNOWN; no schedules, protected sources, public release, email, paid compute, or live graph/store were changed.
