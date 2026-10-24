# account04/B17 — biased Booleanity quadratic-form KL gap

**Classification:** `ESSENTIAL_STEP_APPLIED / QUANTITATIVE_BOOLEANITY_KL_CREDIT`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Exact source state consumed

This run does **not** revive the refuted fixed potential `LIMIT-PRIME-GATE-LIFT-v1`. The newest compatible other-account B15 result consumed substantively is account03/B15

`proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T085625Z-product-equality-rigidity/REPORT.md`

(report creation commit `84c69136ca6b008badb76f15bf1071d029c927aa`, report blob `7904b3ca9ec1b04150b0d23520c65eec9e1010c2`). It proves, on the balanced uniform slice, that the canonical dependence credit `K_occ` vanishes exactly for character-times-bent spectra, hence only on decomposable/dictator endpoints.

I also retain the exact account02/B15 I-projection theorem at scientific commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`: for every nonconstant gate, after conditioning the spectral law on nonempty sets and matching the exact original-coordinate occurrence marginals,

\[
K_{\rm occ}=D_{2}(P\|Q_r)=H_{\max}(r)-H(P),
\]

and for every symmetric potential

\[
R_\Gamma=B_{\rm inf}^{\Gamma}+K_{\rm occ}.
\]

Thus the current missing implication is quantitative: signed Boolean realizability must force enough of this exact negative KL credit to pay any negative first-moment Bellman residual. The theorem below gives a potential-independent, source-exact lower bound for `K_occ`, including **arbitrary product biases**, from the Boolean equations themselves.

## 1. Exact biased Booleanity matrices

Fix a product bias `p=(p_1,...,p_k)` with `0<p_i<1`. Use the normalized one-bit basis

\[
\phi_i(x_i)={x_i-p_i\over\sqrt{p_i(1-p_i)}},\qquad x_i\in\{0,1\},
\]

and `phi_S=product_{i in S} phi_i`. Then

\[
\phi_i^2=1+\kappa_i\phi_i,
\qquad
\kappa_i={1-2p_i\over\sqrt{p_i(1-p_i)}}.
\]

For `U subseteq [k]`, let

\[
M_U=\bigotimes_{i=1}^k A_i(U),
\qquad
A_i(U)=
\begin{cases}
I_2,&i\notin U,\\
\begin{pmatrix}0&1\\1&\kappa_i\end{pmatrix},&i\in U.
\end{cases}
\]

If `a=(a_S)` is the biased Fourier coefficient vector of a Boolean gate `G`, multiplication of the basis gives exactly

\[
[\phi_U](G^2)=a^T M_U a.
\]

Since `G^2=1`,

\[
\boxed{a^T M_Ua=0\quad(U\ne\varnothing).}
\tag{1.1}
\]

The local matrix eigenvalues give the exact operator norm

\[
\boxed{
\|M_U\|_{\rm op}
=L_U:=\prod_{i\in U}
\sqrt{{\max(p_i,1-p_i)\over\min(p_i,1-p_i)}}.
}
\tag{1.2}
\]

This is the biased replacement for the uniform xor-convolution equations; no non-Boolean spectral relaxation is introduced.

## 2. A quantitative KL credit from every Boolean equation

Let `q=Pr[G=-1]`, `v=V_q=4q(1-q)>0`, and let

\[
P(S)={a_S^2\over v},\qquad S\ne\varnothing,
\]

be the actual nonempty spectral law. Let `Q=Q_r` be account02/B15's maximum-entropy nonempty law with the same exact coordinate marginals. Keep the actual signed empty coefficient `a_empty=E G`, so `a_empty^2=1-v`.

For any choice of signs `sigma_S in {+-1}` on the nonempty atoms, define a unit vector

\[
b^\sigma_\varnothing=a_\varnothing,
\qquad
b^\sigma_S=\sigma_S\sqrt{vQ(S)}.
\]

For each nonempty `U`, define the **Booleanity quadratic gap**

\[
\boxed{
\mathfrak g_U(Q;p,q)
:=\min_\sigma |(b^\sigma)^TM_Ub^\sigma|.
}
\tag{2.1}
\]

### Theorem — `B-BIASED-BOOLEANITY-GAP-v1`

For every nonconstant Boolean gate at every interior product bias,

\[
\boxed{
K_{\rm occ}
\ge
{\mathfrak g_U(Q_r;p,q)^2
 \over 4vL_U^2\ln2}
\quad\text{for every }U\ne\varnothing.
}
\tag{2.2}
\]

Hence, without dropping any KL credit,

\[
\boxed{
K_{\rm occ}
\ge {1\over4v\ln2}
\max_{U\ne\varnothing}{\mathfrak g_U^2\over L_U^2}.
}
\tag{2.3}
\]

### Proof

Take the sign choice `sigma*` equal to the actual signs of the nonempty Fourier coefficients and write `b=b^{sigma*}`. By (1.1), `a^TM_Ua=0`. Therefore

\[
\mathfrak g_U
\le |b^TM_Ub-a^TM_Ua|
\le \|b-a\|_2\,\|M_U(b+a)\|_2
\le 2L_U\|b-a\|_2.
\]

Because the empty coordinates agree exactly,

\[
\|b-a\|_2^2
=v\sum_{S\ne\varnothing}
(\sqrt{P(S)}-\sqrt{Q(S)})^2.
\]

For probability laws `P,Q`, KL in bits dominates squared Hellinger distance:

\[
D_2(P\|Q)
\ge {1\over\ln2}
\sum_S(\sqrt{P(S)}-\sqrt{Q(S)})^2.
\]

Combining these identities gives (2.2), and taking the maximum gives (2.3). `QED`.

The theorem is completely potential-independent. It plugs directly into account02/B15's exact decomposition `R_Gamma=B_inf^Gamma+K_occ`: any proposed Bellman repair may now spend the lower bound (2.3) as an authenticated negative-information credit.

## 3. It quantitatively strengthens the newest B15 equality theorem

At a balanced uniform gate, `v=1`, every `p_i=1/2`, `kappa_i=0`, and `L_U=1`. Account03/B15 proved that if the I-projection conditioning parameter `c<1`, exact equality `P=Q_r` is impossible by applying the Boolean convolution equation at the full active set `E`.

The same calculation now has a quantitative form. Write `t_i=cr_i` on the `m` active coordinates and

\[
d={1\over c}\prod_{i\in E}\sqrt{t_i(1-t_i)}.
\]

For `U=E`, the pair `{empty,E}` has zero `Q` weight, while each of the other

\[
2^{m-1}-1
\]

unordered complementary pairs has geometric weight exactly `d`. This number is odd, so the minimum signed quadratic residual is

\[
\mathfrak g_E=2d.
\]

Therefore

\[
\boxed{K_{\rm occ}\ge {d^2\over\ln2}.}
\tag{3.1}
\]

Thus the newest B15 `c<1` parity contradiction is no longer merely an equality endpoint: it supplies an explicit positive KL reserve everywhere in that branch.

## 4. Exact Boolean adversary to the one-equation replacement

The full-active-set reserve (3.1) is **not**, by itself, influence-relative. This failure occurs on an exact balanced Boolean family, not on a relaxed spectral law.

For `k>=3`, start from the dictator `chi_1` and flip its value at two vertices of opposite dictator sign and Hamming distance two. Put

\[
q_k=2^{2-k}.
\]

Its squared Walsh law is exactly

\[
(1-q_k)^2\quad\text{on }\{1\},
\qquad
q_k^2\quad\text{on every other set containing exactly one of }\{1,2\},
\]

and zero elsewhere. Hence

\[
r=(1-q_k,q_k,\ldots,q_k),
\qquad
I-1=(k-2)q_k.
\tag{4.1}
\]

The positive I-projection root satisfies

\[
1-c=(1-c(1-q_k))(1-cq_k)^{k-1}.
\]

Moreover `c>=1/2`: at `c=1/2`, the needed inequality is

\[
(1+q_k)(1-q_k/2)^{k-1}\le1,
\]

which follows from `ln(1+q)<=q` and `ln(1-q/2)<=-q/2` for `k>=3`.

Consequently the full-active product `d` obeys

\[
d\le q_k^{(k-1)/2},
\]

and the **entire guarantee supplied by the single full-active Boolean equation** is at most

\[
{d^2\over\ln2}
\le {q_k^{k-1}\over\ln2}.
\]

Relative to the actual influence excess in (4.1), this is at most

\[
{q_k^{k-2}\over (k-2)\ln2}\to0.
\tag{4.2}
\]

So an argument that robustifies only the exact B15 full-active parity equation cannot close the required dimension-free remainder payment. This is the requested adversarial failure. It does **not** refute FEI and it does **not** say the actual `K_occ` is small enough to violate a candidate; it says that this one-equation certificate throws away almost all of the available Booleanity information.

## 5. Genuinely different replacement: the all-equations Booleanity bank

The replacement is (2.3), not another use of `U=E`. It keeps every biased Boolean quadratic equation available and chooses the strongest normalized gap after paying its exact operator norm. The deterministic checker executes this replacement on actual Boolean sources.

* On the exact four-bit prime witness with Walsh numerator vector
  `(0,-4,-4,0,-4,0,0,-4,-12,0,0,4,0,4,4,0)`, it reconstructs a Boolean truth table exactly, verifies
  `r=(1/4,1/4,1/4,3/4)`, and obtains
  `K_occ=0.8012879378504626955...`. The strongest quadratic-gap certificate gives the rigorous-formula lower quantity `0.0022229157596198670...`.
* On the exact `k=5` two-flip source, the full-active equation alone gives only `0.00003112386407223417...`, whereas the best `U` among all 31 nonempty equations gives `0.01157360325406454267...`, an improvement by a factor about `371.86` in the certified KL amount. This is finite deterministic evidence for the replacement bank, not a universal sufficiency theorem.
* To exercise the genuinely biased theorem rather than only its uniform specialization, the checker takes the exact Boolean `MAJ_3` truth table at rational biases `(3/8,2/5,1/3)`. It verifies all seven biased quadratic Booleanity equations to 50+ decimal digits, finds `K_occ=0.4748676582334332495...`, and obtains a positive all-equation lower certificate `0.0015668153390476566...`.

The checker is standard-library only. Its executed source SHA-256 is
`6a399794d729ca25f7cac5b05c544c59b34b0f99eb2930495bbb620734260097`; the captured output SHA-256 is
`e05ffef466819ce8c44222560861dda5459c41f4e06f010039532652b269c327`. It returned `PASS`.

## 6. Exact implication and remaining obligation

**Old missing implication:** lower-bound the canonical B15 dependence credit `K_occ` by the negative Bellman first-moment deficit, while preserving signed Boolean realizability and all KL credits.

**New proved inference:** every nontrivial biased Booleanity equation supplies the exact lower bound (2.2), and their maximum gives (2.3). This survives arbitrary product biases and therefore applies directly to the all-gate formulation, not only to uniform Walsh spectra.

**Exact failed strengthening:** using only the full-active-set parity equation from the balanced B15 equality proof is not influence-relative; the exact two-flip Boolean family proves the certificate-to-`I-1` ratio tends to zero.

**Replacement obligation:** compare the all-equations bank

\[
{1\over4v\ln2}\max_{U\ne\varnothing}{\mathfrak g_U^2\over L_U^2}
\]

directly with `[-B_inf^Gamma]_+` for the next repaired symmetric potential, or construct a source-valid gate/bias where even the all-equations bank is too small. A stronger next step would combine several quadratic equations simultaneously instead of taking only their maximum; no such dimension-free joint coercivity is claimed here.

This is an essential quantitative Boolean-source bridge, not a full FEI proof. Full FEI remains **OPEN / NOT PROVED**.

## 7. Verification and scope notes

No benchmark gold, mock source, paid/remote compute, workflow dispatch, email, Drive, unrelated private data, scheduler mutation, or weakened source/proof gate was used. The committed material was manually reviewed as a narrow mathematics-only allowlist; no credentials, machine paths, account identifiers, or unrelated excerpts are present. Repository access here is coordination/storage, not verified native brain ingestion, so the run remains `WITHOUT_VERIFIED_BRAIN`.
