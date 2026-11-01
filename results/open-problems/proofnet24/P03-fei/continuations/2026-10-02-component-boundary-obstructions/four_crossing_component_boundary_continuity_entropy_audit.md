# Full continuity and entropy audit of the four-crossing proof

Date: 2026-10-02. **PASS.**

I read the entire
[final obstruction proof](four_crossing_component_boundary_obstruction_proof.md)
after its entropy section was added. This is a new audit; the
[earlier analytic audit](four_crossing_component_boundary_analytic_audit.md)
and independent five-crossing files remain preserved.

The construction, nonempty attained components, all three physical
influence formulas, and the divergent four-crossing ratio pass. No
numerical enumeration was used in this audit. Two optional clarifications
were sent to the author: the central thresholds satisfy
\(0\le t-q<t+q<1\), and the increasing sign function associated with
the event (E_3) is (2\mathbf1_{E_3}-1=-h_{E_3}). Negating the
output preserves influence, so this is a wording clarification, not a
change to the calculation.

## Exact entropy formula

The function is (f=1-2\mathbf1_{\{c^*\}}(1-\mathbf1_{\{v\}})).
An indicator of a specified coarse point has every Fourier coefficient
of magnitude (p). An indicator of a specified fine point has every
Fourier coefficient of magnitude (q). Their products have the stated
signs determined by the specified points. Thus:

* the empty coefficient is (1-2p(1-q));
* every nonempty coarse support with empty fine support has magnitude
  (2p(1-q)), with (2^k-1) such coefficients;
* every support with a nonempty fine part has magnitude (2pq), with
  (2^k(2^N-1)) such coefficients.

Their squared magnitudes sum to one. Consequently equation (8),
\[
 H(f)=e([1-2p(1-q)]^2)
 +(2^k-1)e(4p^2(1-q)^2)
 +2^k(2^N-1)e(4p^2q^2),
\]
is exact, with (e(u)=u\log_2(1/u)).

## Uniform (H<7I) estimate

Write (L_e=\log_2e). If (V=1-[1-2p(1-q)]^2\), then
\(V\le4p(1-q)\) and (e(1-V)\le L_eV\). Hence the empty term
is at most (4L_ep(1-q)).

Expanding the nonempty terms gives exactly
\[
 \begin{aligned}
 C&=4p(1-p)(1-q)^2[2k-2-2\log_2(1-q)],\\
 D&=4pq(1-q)[2k+2N-2].
 \end{aligned}
\]
After discarding the negative terms from each (-2), their terms
involving (k,N) are at most
\[
 8kp(1-q)[(1-p)(1-q)+q]+8pNq(1-q)
 \le8kp(1-q)+8pNq=4I(f).
\]
The logarithmic remainder is
\[
 8p(1-p)(1-q)^2[-\log_2(1-q)]
 \le8L_epq(1-q),
\]
using (-\ln(1-q)\le q/(1-q)). Since (N\ge2), one has
(q\le1/4). Adding the empty term gives a total remainder of at
most (6L_ep(1-q)). Finally, (k\ge2) and the exact influence
formula imply
\[
 I(f)=2kp(1-q)+2pNq\ge4p(1-q)>0.
\]
Therefore
\[
 \boxed{H(f)\le\left(4+\tfrac32\log_2e\right)I(f)<7I(f).}
\]
The entropy calculation confirms that the construction obstructs the
component-boundary comparison and does not contradict FEI. This audit
certifies neither novelty nor external peer review.
