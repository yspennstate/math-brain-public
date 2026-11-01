# A logarithmic FEI bound for parity outputs of unate-gate combinations

Date: 2026-10-02; independently audited 2026-10-03.
**Complete proof; internal analytic audits pass.**
This sharpens the separately preserved
[quadratic gate-count proof](output_parity_unate_gate_combinations_fei_proof.md).
The gates may share inputs and use different coordinate orientations.
The universal \(O(\log n)\) entropy–influence bound used below is
established prior work; a complete elementary derivation is supplied.
Novelty and external peer review are unverified. Full Boolean FEI is
not resolved.

## The theorem

Suppose \(g=F(g_1,\ldots,g_m)\), where \(m\ge1\), each
\(g_j:\{-1,1\}^n\to\{-1,1\}\) is unate, and the outer Boolean
function \(F\) is arbitrary. For any \(T\subseteq[n]\), put
\(h=\chi_Tg\) and \(q=n-|T|\). Then
\[
 \boxed{H(h)=H(g)\le[\log_2(4m^2+2q)+3]I(h).}
\tag{1}
\]
In particular, under full output parity,
\[
 \boxed{H(\chi_{[n]}g)\le(2\log_2m+5)I(\chi_{[n]}g).}
\tag{2}
\]
No disjoint-input or common-orientation premise is imposed on the gates.
This includes arbitrary Boolean combinations of \(m\) halfspaces with
unrelated weights and thresholds. Constant gates may first be removed;
if no gates remain, \(g\) is constant and \(h\) is parity up to a sign,
with zero entropy.

There is a universal influence-vector formulation. For any Boolean
\(g\), if
\[
 M\ge\max\left\{1,\left(\sum_iI_i(g)^2\right)^{1/2}\right\},
\]
then
\[
 \boxed{H(\chi_Tg)\le[\log_2(4M^2+2q)+3]I(\chi_Tg).}
\tag{3}
\]
One can consequently replace \(m\) in (1) by
\(\max\{1,\sum_j\sqrt{\operatorname{Var}(g_j)}\}\), or another
verified bound on the influence-vector norm satisfying \(M\ge1\).
Dimension zero and constant parity outputs have zero entropy and are
handled before any division by influence.

## The elementary universal weak FEI bound

For every Boolean \(f\) in dimension \(n\ge1\),
\[
 \boxed{H(f)\le(\log_2n+3)I(f).}
\tag{4}
\]
Here \(H\) includes the empty Fourier coefficient, and all influences
are physical bit-flip probabilities. We prove (4) completely, without
assuming a constant variance or influence bounded away from zero.

First recall the classical cube edge-isoperimetric inequality, in this
normalization:
\[
 I(f)\ge2r\log_2(1/r),
\tag{5}
\]
where \(r\le1/2\) is the minority probability. An explicit induction
is short. For an event \(E\) of size \(a\) in the \(n\)-cube, its
undirected boundary is at least \(a\log_2(2^n/a)\), with the zero-size
convention. Split its sections into sizes \(a_0\le a_1\), and write
\(u=a_0/a\). By induction, the total internal boundary is at least
\[
 a\log_2(2^{n-1}/a)+ah_2(u).
\]
The crossing boundary is at least \(a_1-a_0=a(1-2u)\).
Since concavity gives \(h_2(u)\ge2u\) on \([0,1/2]\), their sum
is at least \(a\log_2(2^n/a)\). The zero-dimensional base is immediate.
Physical influence is twice the undirected boundary divided by \(2^n\),
giving (5).

For a nonconstant \(f\), let
\(v=\operatorname{Var}(f)=4r(1-r)\) and
\(R=\log_2(1/r)\). The elementary binary entropy bound is
\[
 h_2(v)\le4rR\le2I(f).
\tag{6}
\]
For \(r\le1/4\), indeed
\[
 h_2(v)\le v[\log_2(1/v)+\log_2e]
 =v\left[R+\log_2\frac{e}{4(1-r)}\right]\le vR\le4rR,
\]
because \(4(1-r)\ge3>e\). For \(r\ge1/4\), use
\(h_2(v)\le1\le4r\le4rR\). This includes \(v=1\).
The second inequality in (6) follows from (5). Constants have both
sides zero.

Let \(P\) be the squared-Fourier spectral law. Its empty atom has mass
\(1-v\), and the nonempty atoms have mass \(v\). For \(v>0\), denote
the conditional nonempty law by \(P_+\). On nonempty subsets define
the strictly positive reference probability law
\[
 Q(S)=\frac{n^{-|S|}}{Z_n},\qquad
 Z_n=\sum_{S\ne\varnothing}n^{-|S|}
     =(1+1/n)^n-1.
\]
For \(n\ge1\), \(1\le Z_n<e-1<2\); in dimension one, \(Z_1=1\).
Nonnegativity of the finite relative entropy \(D(P_+\|Q)\) gives
\[
 H(P_+)\le\mathbb E_{P_+}|S|\log_2n+\log_2Z_n.
\]
The full spectral energy satisfies
\(v\mathbb E_{P_+}|S|=I(f)\). Splitting the empty atom and using (6),
\[
 \begin{aligned}
 H(f)&=h_2(v)+vH(P_+)\\
 &\le h_2(v)+I(f)\log_2n+v\log_2Z_n\\
 &\le2I(f)+I(f)\log_2n+I(f).
 \end{aligned}
\]
The final step uses \(\log_2Z_n<1\) and Fourier Poincare
\(v\le I(f)\). This proves (4), with no lost empty spectral atom.

Universal weak bounds of order \(\log n\) precede this work. For
example, the primary Wan–Wright–Wu manuscript
[*Decision Trees, Protocols, and the Fourier Entropy-Influence Conjecture*](https://arxiv.org/pdf/1312.3003)
discusses such bounds in Section 1.1; its Lemma 1.5 and Appendix B
retain the empty atom at cost \(2I(f)\). The proof above is supplied
for transparent constants and normalization, not as a novelty claim
for (4) or classical edge isoperimetry.

## Apply parity and the influence-vector bound

For any Boolean \(g\), parity multiplication gives exactly
\[
 H(\chi_Tg)=H(g),\qquad
 I(\chi_Tg)=\ell+\sum_{i\notin T}I_i(g)-\sum_{i\in T}I_i(g),
 \qquad \ell=|T|.
\tag{7}
\]
The Fourier coefficient indexed by \(S\) is translated to the one
indexed by \(S\mathbin\triangle T\). On an \(i\)-edge parity changes
sign precisely for \(i\in T\), complementing the pivotal condition
there and preserving it elsewhere. These observations prove (7).

If the influence-vector norm is at most \(M\), Cauchy–Schwarz gives
\[
 I(h)\ge\ell-M\sqrt\ell.
\tag{8}
\]
Suppose first that
\(\ell\ge\max\{4M^2,q\}\). Then
\(I(h)\ge\ell/2\), while \(n=\ell+q\le2\ell\). The spectral law
has at most \(2^n\) atoms, so \(H(h)\le n\), and consequently
\[
 H(h)\le4I(h).
\tag{9}
\]
If instead \(\ell<\max\{4M^2,q\}\), then
\[
 n=\ell+q<q+\max\{4M^2,q\}\le4M^2+2q.
\]
For \(n\ge1\), (4) implies
\[
 H(h)\le[\log_2(4M^2+2q)+3]I(h).
\tag{10}
\]
Since \(M\ge1\), the displayed constant is at least 5 and therefore
also covers (9). This proves (3) in both regimes. All thresholds are
real numbers; the comparisons with the integer \(\ell\) require no
rounding assumption.

## Verify the gate hypothesis

For each unate gate, condition on all coordinates but \(i\). Its
singleton Fourier coefficient is either \(I_i(g_j)\) or
\(-I_i(g_j)\), depending on that gate's coordinate orientation.
Hence Parseval gives
\[
 \|(I_i(g_j))_i\|_2^2
 =\sum_i\widehat g_j(\{i\})^2\le\operatorname{Var}(g_j)\le1.
\]
Different gates may use different orientations. If the outer output
changes on an edge, some gate changes there, so
\(I_i(g)\le\sum_jI_i(g_j)\). By the Euclidean triangle inequality,
\[
 \|(I_i(g))_i\|_2
 \le\sum_j\|(I_i(g_j))_i\|_2
 \le\sum_j\sqrt{\operatorname{Var}(g_j)}\le m.
\]
Thus (3) applies with \(M=m\), proving (1) and (2).

## Scope and verification

The theorem is for the **parity output**. It gives no dimension-independent
bound for the unmodulated \(g\) when \(T\) is empty, because then
\(q=n\). It does not establish general FEI closure under overlapping
compositions, ordinary FEI for arbitrary nearby three-crossing scores,
or FEI for nonuniform product input measures. For fixed gate count and
a bounded missing-parity count, the bound is dimension independent.

The earlier quadratic proof and path-based parity theorem are retained
as separate results; no stable file was modified to obtain this
refinement. The fresh [author checker](verify_output_parity_unate_gate_combinations_logarithmic.py)
and [report](output_parity_unate_gate_combinations_logarithmic_checks.json)
pass 1,053,853 exact isoperimetric/parity checks, including every Boolean
function through dimension four and 440 shared-input gate combinations
through dimension twelve. Entropy and KL comparisons are explicitly
numerical supplements to the analytic proof.

The separate [independent analytic audit](output_parity_unate_gate_combinations_logarithmic_heat_audit.md)
passes every step. Its [independent checker](verify_output_parity_logarithmic_heat.py)
and [report](output_parity_logarithmic_heat_checks.json) pass 4,366
character-output pairs, 4,296 direct conditional-KL checks, 12 exact
Gibbs normalizations, 96 shared-input gate combinations, and 49,446
real-parameter regime comparisons. Root independently rederived the
Gibbs normalization, empty-atom bound, and dimension split. These are
internal checks, not external peer review or a historical priority
certificate. Full Boolean FEI remains open.
