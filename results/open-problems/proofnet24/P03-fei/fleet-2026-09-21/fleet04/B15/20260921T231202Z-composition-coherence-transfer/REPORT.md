# B15 — exact composition deficit and an exponential coherence obstruction

**Status:** CANDIDATE_REFUTED / ESSENTIAL CLEANUP. Full unrestricted uniform-cube FEI remains OPEN / NOT PROVED.

**Execution:** WITHOUT_VERIFIED_BRAIN. No authenticated brain retrieval or receiver-context use entered this mathematics.

**Live assignment:** FEI-PROOF-EXECUTION-20260921T230620Z, Campaign B, fleet04/B15: test and derive the weakest sufficient entropy-transfer step on actual Boolean compositions, with all branch costs.

## 0. Version/change summary

The newest execution reset supersedes the older interface-D-only slot wording and asks this worker to attack a common direct-Shannon/composition implication. At the start of the run, no post-reset fleet03/B18 Campaign-B lead artifact was yet visible in its scientific directory; its newest visible report was the pre-reset 23:00 UTC interface-C character-parent report. Following the reset's fallback rule, this report reconstructs the smallest explicit composition candidate and attacks it immediately.

The named other-account result consumed substantively is fleet02/B15:

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260921T210305Z-jeffreys-tail-crossing/REPORT.md`

Its source-exact recombination law is

\[
\Delta D-\frac12D_{\rm KL,2}(P\|Q)
=\mathbb E_Q g+\frac12D_{\rm KL,2}(Q\|P)-\kappa,
\tag{0.1}
\]

with signed cancellation credit \(\kappa\ge0\). The remaining sufficient source-consistent target is

\[
\mathbb E_Q g+\frac12D_{\rm KL,2}(Q\|P)
\le KJ(f)-\frac12D_{\rm KL,2}(P\|Q)+\kappa
\tag{0.2}
\]

for a universal finite \(K\), or an equivalent source-exact inequality. The fleet02 remote-gap calculation proves that the reverse KL term can be leading order, so valuation tails alone cannot replace (0.2).

This run tests a tempting Shannon substitute for that source-consistent transport: whether coherent Boolean composition can be paid by the entropy of an incoherent source-origin branching law. It cannot: a genuine read-once Boolean family violates such domination by an exponential factor.

No novelty or publication-priority claim is made. The exact composition factorization below is a deficit-form restatement of the standard biased-product Fourier composition framework of O'Donnell--Tan (arXiv:1304.1347); the point here is the explicit branch-cost identity and the new in-project obstruction to discarding coherent recombination.

---

## 1. Exact block-composition factorization

Let \(G:\{-1,1\}^m\to\{-1,1\}\), and let \(h_i\) be nonconstant Boolean functions on pairwise disjoint uniform-cube blocks. Put

\[
\mu_i=\mathbb Eh_i,\qquad v_i=1-\mu_i^2>0,
\]

and under the product law with means \(\mu_i\) use the orthonormal coordinate

\[
\psi_i(y_i)=\frac{y_i-\mu_i}{\sqrt{v_i}}.
\]

Write the biased Fourier expansion

\[
G(y)=\sum_{U\subseteq[m]}\widetilde G(U)\prod_{i\in U}\psi_i(y_i),
\qquad q_U=\widetilde G(U)^2,
\]

and

\[
\beta_i=\sum_{U\ni i}q_U.
\]

For the inner function define, for nonempty \(T\),

\[
\nu_i(T)=\frac{\widehat h_i(T)^2}{v_i},
\qquad H_i^\circ=H(\nu_i).
\]

Because

\[
\psi_i(h_i)=\sum_{T\ne\varnothing}
\frac{\widehat h_i(T)}{\sqrt{v_i}}\chi_T,
\]

a nonzero global Fourier coefficient of

\[
F=G(h_1,\ldots,h_m)
\]

is indexed uniquely by an active outer set \(U\) and one nonempty inner set \(T_i\) for every \(i\in U\), with

\[
\boxed{
\widehat F((T_i)_{i\in U})
=\widetilde G(U)\prod_{i\in U}
\frac{\widehat h_i(T_i)}{\sqrt{v_i}}.
}
\tag{1.1}
\]

Hence the squared spectrum is a genuine hierarchical probability law: first draw \(U\sim q\), then independently draw \(T_i\sim\nu_i\) inside every active block.

### Theorem 1 — exact entropy and influence chain

Let \(H_\mu(G)=H(q)\) be the biased spectral entropy of \(G\). Then

\[
\boxed{H(F)=H_\mu(G)+\sum_i\beta_iH_i^\circ}
\tag{1.2}
\]

and

\[
\boxed{I(F)=\sum_i\frac{\beta_i}{v_i}I(h_i).}
\tag{1.3}
\]

For Boolean \(G\),

\[
\alpha_i:=\frac{\beta_i}{v_i}
\]

is exactly the probability, under the biased product distribution on the other outer inputs, that coordinate \(i\) is pivotal. Also

\[
H(h_i)=h_2(v_i)+v_iH_i^\circ.
\tag{1.4}
\]

All identities follow directly from (1.1), Shannon's chain rule, and expected Fourier level.

---

## 2. Weakest exact branch transfer for a fixed composition

For a candidate FEI constant \(C\), define the deficit

\[
E_C(f)=CI(f)-H(f).
\]

Substituting (1.2)--(1.4) gives the exact identity

\[
\boxed{
E_C(F)=\sum_i\alpha_iE_C(h_i)-L_G(\mu),
}
\tag{2.1}
\]

where the complete outer branch debit is

\[
\boxed{
L_G(\mu)=H_\mu(G)-\sum_i\alpha_i h_2(v_i).
}
\tag{2.2}
\]

Therefore, for this actual decomposition,

\[
\boxed{
H(F)\le CI(F)
\iff
L_G(\mu)\le\sum_i\alpha_iE_C(h_i).
}
\tag{2.3}
\]

Equation (2.3) is the weakest necessary-and-sufficient local composition transfer once the inner deficits are fixed. It prices every branch cost: the outer biased spectral entropy is not free, and the binary branch entropies \(h_2(v_i)\) are exactly the part already contained in the inner spectral entropies.

This is not a proof of FEI, because no universal payment of \(L_G(\mu)\) by the available inner deficits is proved.

---

## 3. An exact source-origin Shannon balance with its negative KL credit

A natural attempt is to expand the *uniform* Fourier monomials of the outer Boolean function into the biased basis and pay the coherent output spectrum by the entropy of the resulting incoherent source-origin law.

Write

\[
G(y)=\sum_{S\subseteq[m]}a_S\chi_S(y).
\]

For \(U\subseteq S\), define the source-origin probability

\[
\boxed{
P(S,U)=a_S^2
\prod_{i\in U}v_i
\prod_{i\in S\setminus U}\mu_i^2.
}
\tag{3.1}
\]

For each fixed \(S\), the sum over \(U\subseteq S\) is \(a_S^2\), so \(P\) is a probability law. Its pushforward to \(U\) is

\[
m_U=\sum_{S\supseteq U}P(S,U).
\]

The *actual* biased Fourier coefficient is the coherent signed sum

\[
\widetilde G(U)
=\sqrt{\prod_{i\in U}v_i}
\sum_{S\supseteq U}a_S\prod_{j\in S\setminus U}\mu_j,
\tag{3.2}
\]

and \(q_U=\widetilde G(U)^2\). Thus \(m\) is the incoherent source mass while \(q\) is its coherent Boolean recombination.

The source entropy is exactly

\[
\boxed{
H(P)=H_{\rm unif}(G)
+\sum_i\operatorname{Inf}^{\rm unif}_i(G)h_2(v_i).
}
\tag{3.3}
\]

Let

\[
T(q,m)=\sum_U(q_U-m_U)\log_2\frac1{m_U},
\]

with zero-mass terms interpreted by continuity. Since \(q_U=0\) whenever \(m_U=0\), Shannon's chain rule and the KL identity give

\[
\boxed{
H(q)-H(P)
=T(q,m)-D_{\rm KL,2}(q\|m)-H_P(S\mid U).
}
\tag{3.4}
\]

So even this naive source-origin comparison has an exact **negative relative-entropy credit** and an additional negative source-label conditional entropy. The only positive term is the coherent redistribution \(T(q,m)\).

A proof that simply discards coherence would need a universal control of \(T\) by these negative credits. The next section shows that this fails by an exponential factor on an actual Boolean composition.

---

## 4. Genuine Boolean counterfamily: coherent output entropy exceeds source-origin entropy exponentially

Take the two-bit Boolean gate

\[
h(x_1,x_2)=+1\quad\text{except at }(1,1),\text{ where }h=-1.
\]

Then

\[
\mu=\frac12,\qquad v=\frac34,\qquad I(h)=1,\qquad H(h)=2,
\qquad H^\circ=\log_2 3.
\tag{4.1}
\]

Let the outer function \(G_n\) be the one-point gate

\[
G_n(y)=+1\iff y_1=\cdots=y_n=+1,
\]

and set

\[
F_n=G_n(h_1,\ldots,h_n),
\]

on \(2n\) independent input bits. This is an ordinary read-once Boolean formula, not a non-Boolean relaxation.

Put

\[
\delta=(3/4)^n.
\]

Under the biased outer law, the squared spectrum is

\[
q_\varnothing=(1-2\delta)^2,
\qquad
q_U=4\delta^2\,3^{-|U|}\quad(U\ne\varnothing).
\tag{4.2}
\]

Consequently

\[
\beta_i=\delta,\qquad \alpha_i=\frac{4\delta}{3},
\qquad I(F_n)=\frac{4n\delta}{3}.
\tag{4.3}
\]

Let \(\varepsilon=4\delta(1-\delta)\). Conditional on \(U\ne\varnothing\), (4.2) is the law of i.i.d. Bernoulli\((1/4)\) bits conditioned to be nonempty. Hence

\[
\boxed{
H_\mu(G_n)
=h_2(\varepsilon)
+4\delta\,[n h_2(1/4)-h_2(\delta)].
}
\tag{4.4}
\]

The exact branch debit and full entropy are

\[
L_n=H_\mu(G_n)-\frac{4n\delta}{3}h_2(3/4),
\tag{4.5}
\]

\[
H(F_n)=H_\mu(G_n)+n\delta\log_2 3.
\tag{4.6}
\]

Therefore

\[
\boxed{
\lim_{n\to\infty}\frac{L_n}{I(F_n)}
=10-\frac92\log_2 3
=2.8676687467547977\ldots
}
\tag{4.7}
\]

and

\[
\boxed{
\lim_{n\to\infty}\frac{H(F_n)}{I(F_n)}
=12-\frac92\log_2 3
=4.867668746754798\ldots .
}
\tag{4.8}
\]

Now compare with the incoherent source-origin law (3.1). Put \(\delta_0=2^{-n}\), \(\varepsilon_0=4\delta_0(1-\delta_0)\). The uniform outer one-point gate has

\[
H_{\rm unif}(G_n)
=h_2(\varepsilon_0)+\varepsilon_0\log_2(2^n-1),
\qquad
I_{\rm unif}(G_n)=2n\delta_0.
\]

Thus

\[
\boxed{
H(P_n)=h_2(\varepsilon_0)+\varepsilon_0\log_2(2^n-1)
+2n\delta_0h_2(3/4)
=\Theta(n2^{-n}).
}
\tag{4.9}
\]

But (4.4) gives

\[
H_\mu(G_n)=\Theta(n(3/4)^n).
\tag{4.10}
\]

Hence

\[
\boxed{
\frac{H_\mu(G_n)}{H(P_n)}
=\Theta((3/2)^n)\longrightarrow\infty.
}
\tag{4.11}
\]

This rigorously refutes every dimension-free inequality of the form

\[
H_\mu(G)\le C\,H(P)
\]

for the source-origin law (3.1), even on genuine Boolean read-once compositions. In the exact balance (3.4), the positive coherent-redistribution term \(T(q,m)\) must exceed the combined forward-KL and source-label credits by an amount comparable to \(H_\mu(G_n)\); those negative terms cannot be discarded and then replaced by source entropy monotonicity.

This counterfamily does **not** refute FEI: its ratio tends to the finite value (4.8).

---

## 5. Direct verification

The standard-library checker `check_composition_coherence.py` independently constructs \(F_n\) on \(2n\) bits for \(1\le n\le7\), computes its integer Walsh transform, spectral entropy, and total influence, and compares them with (4.3)--(4.6).

It passes through dimension 14 with maximum entropy-formula discrepancy below `1.4e-12`, zero influence discrepancy at double precision, and zero Parseval discrepancy. For `n=7` it obtains

\[
H(F_7)/I(F_7)=4.179025877219024\ldots,
\]

while the analytic formula gives the same value up to numerical rounding. The checker also records the rapidly growing ratio \(H_\mu(G_n)/H(P_n)\), already `7.379576...` at `n=7`.

Finite checks are falsification/self-check evidence; the all-\(n\) statements (1.1)--(4.11) are algebraic/analytic proofs.

---

## 6. What this changes in the common Campaign-B proof chain

**Old tempting missing implication:** coherent biased recombination might be replaced by an incoherent source-origin Shannon law and then paid from the branch entropy already present in the inner functions.

**Outcome:** **CANDIDATE_REFUTED.** Equation (4.11) shows exponential failure on an actual Boolean read-once family.

**Replacement obligation:** keep the coherent transport debit. For block composition the exact scalar obstruction is \(L_G(\mu)\) in (2.2), and the weakest exact local transfer is (2.3). On the arithmetic side, fleet02/B15's more refined source-consistent unpaid object is still (0.1)/(0.2):

\[
\mathbb E_Qg+\tfrac12D_{\rm KL}(Q\|P)-\kappa
\]

after the forward-KL refund. The present counterfamily does not refute that Jeffreys/cancellation target. It shows why replacing it by a credit-free source-entropy monotonicity loses the decisive coherent contribution.

A viable next bridge would have to identify, for an actual Boolean decomposition, how the source-consistent Jeffreys/cancellation ledger controls the branch coherence debit \(L_G(\mu)\) (or an equivalent signed conditional-information term) while surviving this family and tensor/composition stress tests.

**Full FEI change:** OPEN -> OPEN. No universal constant is proved here.

---

## 7. Literature boundary

O'Donnell--Tan, *A composition theorem for the Fourier Entropy-Influence conjecture* (arXiv:1304.1347), already supplies the general biased-product composition framework and proves FEI closure under suitable biased outer and inner hypotheses; therefore Section 1 is not claimed as a new composition theorem.

Potapov (arXiv:2609.21563, 18 September 2026) proves FEI for plateaued functions with sharp class constant 4 and partially bent functions with sharp constant 2, not for arbitrary unequal-magnitude spectra. González--MacManus--Pereyra (arXiv:2606.00246, 29 May 2026) develop a restriction/stopping-tree framework whose key universal restriction inequality would imply full FEI but is not proved in general. Li--Han (arXiv:2512.03117, 2 December 2025) prove a general information-theoretic inequality retaining an additional influence-profile entropy term. These primary-source checks are consistent with unrestricted FEI remaining open.

No novelty or publication-priority claim is made for the branch-deficit reformulation or the coherence counterfamily without a separate literature review.
