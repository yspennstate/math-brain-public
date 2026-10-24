# B19 / A091 — independent review of B09 biased restriction uncertainty

**Run:** `20261013T074715Z-account01-B19-b09-composition-review-a091`  
**Primary packet:** A091 (composition referee)  
**Reviewed object:** B09 run `20261011T195500Z-account01-B09-biased-restriction-uncertainty`, report blob `71b68e4decf9658a42fef6bb2668e19f25bd214a`, source commit `adb671ffcda143fa68347806bb96e8c305621a7d`  
**Full FEI:** **OPEN.**

## 1. Claim-by-claim verdict

| B09 claim | Verdict | Exact accepted scope |
|---|---|---|
| `L_A=M_A+J_A` and `J_A=I(Z;T)` | **ACCEPTED** | Every finite Boolean function under an interior product measure and every physical coordinate block `A`. |
| `0<=J_A<=M_A+Delta_A(p)` and `L_A<=2M_A+Delta_A(p)` | **ACCEPTED** | Same scope, with `Delta_A=sum_i[h_2(p_i)+log_2 max(p_i,1-p_i)]`. |
| Tax-free `J_A<=M_A` at arbitrary biases | **REFUTED / ACCEPTED COUNTEREXAMPLE** | The repaired source-bound two-bit AND certificate proves `J_A-M_A>0.1195` bits for `p=1/8,q=1/4,A={X}`. |
| `Delta(p)` cannot be replaced uniformly by `O(p)` | **ORIGINAL PROOF GAP; REPAIRED HERE, PENDING FRESH REVIEW** | The original inference from an upper bound was invalid.  Section 5 below supplies a genuine Boolean lower-bound family with `J-M=4q(1-2q)p log_2(1/p)+O(p)` for fixed `0<q<1/2`. Because B19 supplied this repair, it is contributor work, not independent acceptance. |
| Additivity of `M,J,Delta` | **ACCEPTED ONLY FOR EXACT DISJOINT PRODUCTS/TENSORS WITH ALIGNED BLOCKS** | This follows from product spectral laws and product physical channels. |
| Transfer through general Boolean composition | **NOT ESTABLISHED BY B09** | O'Donnell--Tan transfers their normalized biased `FEI+` functional, not the B09 `M,J,Delta` ledger.  The ledger is already nonadditive for AND of two uniform dictators. |
| Endpoint optimality / universal FEI payment | **OPEN** | The order of the one-bit tax is necessary, but no dimension-independent payment of accumulated taxes or conditional label costs is proved. |

The main B09 uncertainty theorem and the finite helper counterexample are accepted independently at their exact scopes.  The broad composition prose in section 5 must not be registered as a B09 closure theorem.

## 2. Sources actually checked

1. Original B09 report at the immutable source commit above.
2. Independent interval repair `verification/B09_interval_repair_20261011/REPORT.md`, `CHECK.py`, and `CHECK.out`, commit `a1ff93577685acd461b154b04e0c1aa0c65645c8`; repaired report blob `2674d84116f7454c45b37fdd4991f78d65eaf31c` and output blob `3bfcf7ddae830e0766863b41e89ebb2ef55f6ba2`.
3. O'Donnell--Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, arXiv:1304.1347.  Theorem 1 composes the paper's product-biased `FEI+` functional over disjoint input blocks; Proposition 3.2 gives its normalized entropy/influence identities.  It does not state a composition theorem for the B09 physical-restriction `M,J,Delta` ledger.

The finite interval certificate was reused rather than presented as a new calculation.  Its corrected implementation takes all four quotient corners for signed numerator intervals, and its scope remains the displayed two-bit Boolean gate only.

## 3. Independent reconstruction of the main lemma

Let `S` have biased spectral law `mu(S)=hat f_p(S)^2`.  Write `A` for the revealed physical block, `B` for the retained coordinates, `T=S_B`, and let `Z` be the physical assignment on `A`.  Biased Parseval on `A` gives

\[
q_T=\Pr[S_B=T]=\sum_{R\subseteq A}\widehat f_p(R\cup T)^2
=\mathbb E_Z\widehat{f_Z}_{p_B}(T)^2.
\]

Thus, under the joint experiment `Z` followed by a spectral label `T` from the restricted child, the marginal law of `T` is exactly `q`.  Therefore

\[
J_A=H(T)-\mathbb E_Z H(T\mid Z)=I(Z;T)\ge0.
\]

The chain rule then yields

\[
L_A=H(S_A,S_B)-\mathbb E_ZH(T\mid Z)
=H(S_A\mid S_B)+I(Z;T)=M_A+J_A.
\]

For each `T` with `q_T>0`, normalize the coefficient fiber

\[
a_R=\widehat f_p(R\cup T)/\sqrt{q_T}
\]

and the physical posterior amplitudes

\[
b_z=\sqrt{\mu_{p_A}(z)}\,\widehat{f_z}_{p_B}(T)/\sqrt{q_T}.
\]

They obey `b=U_Aa`, where `U_A` is the tensor product of the one-bit orthogonal matrices

\[
\begin{pmatrix}\sqrt{1-p_i}&-\sqrt{p_i}\\
\sqrt{p_i}&\sqrt{1-p_i}\end{pmatrix}.
\]

Its largest entry has modulus

\[
c_A=\prod_{i\in A}\sqrt{\max\{p_i,1-p_i\}}.
\]

Maassen--Uffink gives

\[
H(a^2)+H(b^2)\ge-2\log_2c_A
=-\sum_{i\in A}\log_2\max\{p_i,1-p_i\}.
\]

Averaging over `T` makes the two entropies `M_A` and `H(Z|T)`.  Since `J_A=H(Z)-H(Z|T)` and `H(Z)=sum_i h_2(p_i)`, this is exactly

\[
J_A\le M_A+\sum_{i\in A}
\left(h_2(p_i)+\log_2\max\{p_i,1-p_i\}\right).
\]

No Boolean phase, normalization, endpoint, or zero-mass step is missing.  This proves the accepted theorem, but it does not pay `M_A` or the tax by influence.

## 4. Composition scope: the precise boundary

For an exact disjoint product `f=f_1f_2` and an aligned block `A=A_1 union A_2`, the spectral law and physical posterior channel are products.  Hence conditional entropy and mutual information add:

\[
M_A=M_{A_1}+M_{A_2},\qquad
J_A=J_{A_1}+J_{A_2},\qquad
\Delta_A=\Delta_{A_1}+\Delta_{A_2}.
\]

This is tensorization, not arbitrary Boolean composition.

A smallest control separates the two.  Let `g_1(x)=x`, `g_2(y)=y` under uniform inputs and let the outer gate be sign-AND, `F(u,v)=(-1)^{((1-u)/2)((1-v)/2)}` (equivalently use the `{0,1}` convention `(-1)^{xy}`).  Each dictator has a point-mass spectrum, so its own `M` and `J` are zero.  But the composite two-bit AND has four equal spectral masses.  Revealing `x` while retaining `y` gives

\[
M_{\{x\}}=1,\qquad J_{\{x\}}=1.
\]

Thus the B09 ledger is not the sum of base-function ledgers under a nonlinear outer gate.  O'Donnell--Tan's theorem remains applicable to its own `FEI+` functional and explicitly includes an outer-gate term at the induced biases; it cannot be cited as a transfer theorem for `M,J,Delta` without a new identity.  Consequently B09 section 5 establishes exact tensor compatibility but no broader prime-gate closure.

## 5. New repair: a genuine Boolean endpoint lower-bound family

The original section 5(4) inferred necessity of a `p log(1/p)` correction from the asymptotic size of the proved upper bound `Delta(p)`.  That inference is invalid: an upper bound alone supplies no lower bound on `J-M`.

The claim's order can nevertheless be repaired on the same genuine Boolean gate.  Fix `0<q<1/2`, let

\[
g(x,y)=(-1)^{xy},\qquad \Pr[X=1]=p,\quad\Pr[Y=1]=q,
\]

and reveal `A={X}`.  Put `s=4q(1-q)`.  The exact squared biased Fourier masses are

\[
(1-2pq)^2,quad 4p(1-p)q^2,quad
4p^2q(1-q),quad4p(1-p)q(1-q).
\]

The retained spectral bit has nonempty mass `ps`.  Conditional on it being nonempty, the revealed spectral bit has entropy `h_2(p)`.  Conditional on it being empty, its nonempty probability is

\[
r_p=\frac{4p(1-p)q^2}{1-ps}.
\]

Therefore, exactly,

\[
M=(1-ps)h_2(r_p)+psh_2(p),\qquad
J=h_2(ps)-p h_2(s).
\]

For fixed positive `a`,

\[
h_2(ap)=ap\log_2(1/p)+O(p)
\quad(p\downarrow0).
\]

Since `r_p=4q^2p+O(p^2)`, it follows that

\[
M=4q^2p\log_2(1/p)+O(p),
\]

while

\[
J=4q(1-q)p\log_2(1/p)+O(p).
\]

Hence

\[
\boxed{J-M=4q(1-2q)p\log_2(1/p)+O(p).}
\]

The coefficient is positive for every fixed `0<q<1/2`; at `q=1/4` it is `1/2`.  Thus no bound `J<=M+Cp` with a constant `C` uniform in `p` can hold even for this fixed two-bit Boolean gate.  This proves order-level necessity of a rare logarithm.  It does **not** prove the exact B09 tax sharp, nor control repeated taxes through a composition hierarchy.

Because this argument was added by the reviewer, claim version `B09-ENDPOINT-ORDER-02` is **CONTRIBUTOR_PROVED_PENDING_FRESH_REVIEW**, not independently accepted in this run.

## 6. What remains unpaid

The reviewed theorem is local.  Full FEI still needs a dimension-independent mechanism that pays the aggregate conditional spectral-label cost and every nonreused biased endpoint tax under general Boolean restriction/composition.  Exact tensor additivity and a two-bit lower-bound family do not provide that mechanism.

Concrete next step: freeze a hierarchy claim in which each physical pivotal event receives the endpoint charge at most once, then test it on nested rare AND activations with changing terminal cores.  Any claimed composition transfer must state the outer-gate term and induced biases explicitly.

## 7. Reproduction

`CHECK_AND_ASYMPTOTIC.py` evaluates the exact formulas at 90 decimal digits, confirms the repaired finite gap, numerically approaches the proved endpoint coefficient, and records the AND-of-dictators nonadditivity control.  Randomness: none.  The analytic proof above, not the decimal output, is the evidence for the asymptotic claim.

No protected source, held proof-chain payload, new worker, paid computation, scheduler change, public release, or live-state mutation was used.
