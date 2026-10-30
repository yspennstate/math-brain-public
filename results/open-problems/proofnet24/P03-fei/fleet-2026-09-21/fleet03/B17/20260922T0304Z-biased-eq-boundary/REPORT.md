# B17 — exact biased antipodal-defect reduction for the all-gate FEI candidate

**Classification:** `ESSENTIAL_STEP_APPLIED` to the adversarial gate programme; full uniform-cube FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository sources were consumed directly; no authenticated installed-brain retrieval/context was used.

## 1. Candidate and peer results actually consumed

The live target is the all-gate inequality
\[
D_\Gamma(G;p):=\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
  \bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
 -\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u),
\tag{1.1}
\]
for one symmetric nonnegative finite-centre potential and every Boolean gate and product bias. The stable fixed candidate from fleet01/B18 is `LIMIT-PRIME-GATE-LIFT-v1`,
\[
 C_*=6.5218512,\qquad a_*=0.2682048,\qquad
 \Gamma_*(p)=\Gamma_{\rm RO}(p)+a_*p(1-p).
\tag{1.2}
\]
A proof of (1.1) for every composition-prime gate with \(\Gamma_*\), followed by the proved gate-composition cocycle, would imply full FEI with constant \(6.5218512\). This universal implication is still open.

Two completed peer results are applied here.

1. **fleet01/B17, `20260922T003221Z-gate-addressing-collapse`.** It proves that every one/two-point sparse-defect gate reduces by NPN symmetry and the decomposable-margin cocycle to binary AND plus the antipodal equality core
\[
 \operatorname{EQ}_d=1_{\{0^d,1^d\}},
\]
and that uniform-bias \(\operatorname{EQ}_d\) is strictly safer than its AND reduction. Thus the first unresolved sparse-defect adversary is genuinely biased \(\operatorname{EQ}_d\), beginning at \(d=3\).
2. **fleet01/B12, `20260922T0227Z-shared-core-margin-envelope`.** It proves that changing only the integer-depth schedule inside the existing nine-host shared-core construction cannot push its required margin above \(0.2682048520515108946\ldots\). Hence this run changes mechanism rather than repeating that exhausted depth family: it attacks the genuinely biased sparse core left by item 1.

## 2. Exact biased spectrum of the antipodal core

Use the convention that the Boolean sign is \(-1\) on \(0^d,1^d\) and \(+1\) elsewhere. Feed all coordinates with the same bias \(\Pr[x_i=1]=p\), put \(q=1-p\), and use the normalized biased basis
\[
 \varphi_i(1)=\sqrt{q/p},\qquad \varphi_i(0)=-\sqrt{p/q}.
\]
Let
\[
 r=p^d+q^d=\Pr[\operatorname{EQ}_d=1].
\]
For every nonempty Fourier set \(S\), \(|S|=s\), direct evaluation on the two exceptional points gives
\[
 \widehat f(S)
 =-2\left[p^{d-s/2}q^{s/2}+(-1)^s q^{d-s/2}p^{s/2}\right].
\tag{2.1}
\]
The empty coefficient is \(\widehat f(\emptyset)=1-2r\). Therefore the exact spectral mass of each level-\(s\) atom is
\[
 w_s=4\left[p^{d-s/2}q^{s/2}+(-1)^s q^{d-s/2}p^{s/2}\right]^2,
\quad s\ge1,
\tag{2.2}
\]
with multiplicity \(\binom ds\), while \(w_0=(1-2r)^2\). Thus
\[
 \widetilde H_{\rm EQ_d}(p)
 =\phi(w_0)+\sum_{s=1}^d {d\choose s}\phi(w_s),
 \qquad \phi(x)=x\log_2(1/x).
\tag{2.3}
\]
No finite search or non-Boolean relaxation is used in (2.1)--(2.3).

The output changes under coordinate \(i\) exactly when the other \(d-1\) bits are all equal. Hence the biased spectral influence is
\[
 \operatorname{It}_i=V_p\bigl(p^{d-1}+q^{d-1}\bigr),
\tag{2.4}
\]
and therefore
\[
 I_d(p)=dV_p\bigl(p^{d-1}+q^{d-1}\bigr).
\tag{2.5}
\]
Substitution into the live gate functional yields the exact one-variable reduction
\[
 \boxed{
 D^{\rm EQ_d}_\Gamma(p)
 =d\bigl(p^{d-1}+q^{d-1}\bigr)
   \bigl(\Gamma(p)+h_2(V_p)\bigr)
 -\widetilde H_{\rm EQ_d}(p)-\Gamma(r).
 }
\tag{2.6}
\]
Its Poincare currency is exactly
\[
 \boxed{
 W_d(p)=dpq\bigl(p^{d-1}+q^{d-1}\bigr)-r(1-r).
 }
\tag{2.7}
\]
Consequently the required additional quadratic margin, whenever \(W_d(p)>0\), is the scalar function
\[
 c^{\rm EQ_d}_\Gamma(p)=-D^{\rm EQ_d}_\Gamma(p)/W_d(p).
\tag{2.8}
\]
Thus the whole equal-bias antipodal sparse-defect family has been reduced to a one-dimensional exact calculation for each \(d\); no ambient truth-table sweep remains.

## 3. The first genuine core, EQ3, collapses further

For \(d=3\), set \(u=pq\). Then
\[
 r=p^3+q^3=1-3u,
\qquad
 W_3(p)=3u^2
\tag{3.1}
\]
**exactly**. The nonzero spectral masses are
\[
 w_0=(1-6u)^2,
\qquad w_1=4u(1-4u)\quad(\text{multiplicity }3),
\qquad w_2=4u^2\quad(\text{multiplicity }3),
\qquad w_3=0.
\tag{3.2}
\]
Hence, using symmetry \(\Gamma(1-3u)=\Gamma(3u)\),
\[
\boxed{
\begin{aligned}
D^{\rm EQ_3}_\Gamma(p)
={}&3(1-2u)\bigl(\Gamma(p)+h_2(4u)\bigr)-\Gamma(3u)\\
&-\phi((1-6u)^2)-3\phi(4u(1-4u))-3\phi(4u^2),
\end{aligned}}
\tag{3.3}
\]
and
\[
\boxed{c^{\rm EQ_3}_\Gamma(p)=-{D^{\rm EQ_3}_\Gamma(p)\over3u^2}.}
\tag{3.4}
\]
This is the exact normalized object that a future interval proof or counterexample search must test for the first genuinely new two-defect core. It uses the correct margin rather than the incomparable raw defect \(D\).

## 4. Boundary theorem: positive linear-log tails repel the biased defect

The extreme-bias limit can be resolved analytically for a broad class of candidate potentials. Suppose a symmetric potential has
\[
 \Gamma(p)=A\,p\log_2(1/p)+Bp+o(p)
 \qquad(p\downarrow0)
\tag{4.1}
\]
with \(A>0\). For every fixed \(d\ge3\), equations (2.2)--(2.7) give
\[
 W_d(p)={d\choose2}p^2+O(p^3),
\tag{4.2}
\]
\[
 \widetilde H_{\rm EQ_d}(p)
 =4dp\left[\log_2(1/p)-2+{1\over\ln2}\right]
 +O\bigl(p^2\log(1/p)\bigr),
\tag{4.3}
\]
and the same first-order entropy term occurs in
\(d(p^{d-1}+q^{d-1})h_2(V_p)\). Meanwhile
\[
 1-r=dp+O(p^2)
\]
and symmetry plus (4.1) gives
\[
 d(p^{d-1}+q^{d-1})\Gamma(p)-\Gamma(r)
 =Adp\log_2 d+o(p).
\tag{4.4}
\]
Therefore
\[
 \boxed{
 D^{\rm EQ_d}_\Gamma(p)=Adp\log_2 d+o(p)>0
 }
\tag{4.5}
\]
for sufficiently small \(p\), and
\[
 \boxed{
 p\,c^{\rm EQ_d}_\Gamma(p)
 \longrightarrow
 -{2A\log_2 d\over d-1}<0.
 }
\tag{4.6}
\]
So any symmetric candidate with a positive linear-log small-bias tail has **arbitrarily large favorable slack** in normalized-margin units near the extreme bias. A two-point antipodal sparse defect cannot defeat such a candidate by sending all common input biases to \(0\) or \(1\); any violation must occur in an interior bias region.

This theorem is independent of the unavailable numerical NPZ for the current read-once candidate. Applying it numerically to `LIMIT-PRIME-GATE-LIFT-v1` requires only the source-exact small-bias coefficient of \(\Gamma_{\rm RO}\); the quadratic lift \(a_*p(1-p)\) changes only the \(O(p)\) term and not \(A\). I do **not** invent that coefficient here from a missing binary candidate file.

## 5. Stress tests and refutation attempts

A separate direct biased-Walsh checker constructs \(\operatorname{EQ}_d\) from its truth table and compares every spectral mass, entropy, influence and Poincare currency against (2.1)--(2.7) for \(d=3,\ldots,7\) and several interior/extreme biases. The maximum discrepancies are at floating roundoff. It also checks the exact \(d=3\) identity \(W_3=3(pq)^2\) and numerically verifies the coefficient in (4.6) on synthetic potentials with prescribed \(A>0\). These are checks of the analytic derivation, not evidence for full FEI.

Boundary cases are explicit: \(d=2\) is XNOR/XOR and is already decomposable-safe by the inherited cocycle; \(p=1/2\) is the uniform antipodal case already proved safer than AND by fleet01/B17; \(p\to0,1\) is handled by (4.5)--(4.6) under the stated tail hypothesis. The unresolved region is therefore genuinely interior and begins with the exact one-variable function (3.4).

## 6. Exact movement of the proof gap

**Exact candidate version:** `LIMIT-PRIME-GATE-LIFT-v1`, \(C_*=6.5218512\), \(\Gamma_*=\Gamma_{\rm RO}+0.2682048\,p(1-p)\).

**Old missing implication:** after tribes/addressing/uniform sparse defects were reduced, a genuinely biased antipodal sparse defect \(\operatorname{EQ}_d\) could still be a composition-prime counterexample to the fixed all-gate candidate.

**New proved inference:** equal-bias \(\operatorname{EQ}_d\) has the exact scalar formulas (2.6)--(2.8); the first genuine core \(\operatorname{EQ}_3\) has the closed formula (3.3)--(3.4); and every positive-linear-log candidate is safe in the extreme-bias limit by (4.5)--(4.6).

**What was not proved:** no claim is made that \(\Gamma_*\) satisfies (3.4) throughout the interior, because the exact numerical `cert_vi_h96k40_f4` data needed to evaluate \(\Gamma_{\rm RO}\) was not present at the canonical repository path read in this run. No finite test is substituted for that missing input.

**Replacement obligation / next recipient:** `fleet01/B14` or `fleet01/B18` should plug the exact current \(\Gamma_*\) representation into (3.3) and certify \(D^{\rm EQ_3}_{\Gamma_*}\ge0\) on the compact interior interval left after the tail cutoff, or return an exact interior counterexample. If EQ3 is safe, repeat the scalar formula (2.6) for \(d\ge4\); if an EQ core fails, it is a genuine source-valid falsifier of `LIMIT-PRIME-GATE-LIFT-v1` but still not a disproof of FEI.

**Implication to full FEI:** this removes the extreme-bias escape route for the reduced two-point-defect adversary under the stated tail condition and converts the first unresolved sparse core to one exact scalar inequality. The universal prime-gate implication remains open, so full FEI remains **OPEN / NOT PROVED**.

No novelty or publication-priority claim is made.