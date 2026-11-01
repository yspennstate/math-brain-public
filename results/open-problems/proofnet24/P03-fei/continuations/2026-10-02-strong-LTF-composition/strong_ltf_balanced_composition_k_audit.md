# Independent audit: strengthened LTF FEI and balanced composition

2 October 2026. I read every step of [strong_ltf_and_balanced_composition_candidate.md](strong_ltf_and_balanced_composition_candidate.md). The strengthened estimate and balanced composition closure pass this independent analytic audit, conditional on the already completed largest-weight LTF split theorem. A shorter elementary proof of the near-dictator branch is supplied below. Historical novelty and external validation are not certified.

All Fourier transforms use the uniform Boolean cube and entropy uses base-2 logarithms.

## 1. Universal near-dictator lemma for a unate split

Let a Boolean function be increasing in a distinguished coordinate z. Write

\[
 f(x,z)=A(x)+zB(x),\quad
 A=(f^++f^-)/2,\quad B=(f^+-f^-)/2.
\]

Then B\in\{0,1\}, A\in\{-1,0,1\}, and A^2+B^2=1. Set \alpha=\mathbb EB=I_z(f). The other coordinates need not be monotone and f need not be an LTF.

Let a_S=\widehat A(S), b_S=\widehat B(S), and P_S=a_S^2+b_S^2. Parseval gives \sum_SP_S=1. The exact split identity implies

\[
 \Delta_zH(f)\le2\mathcal C,
 \qquad \mathcal C=\sum_SP_Sh_2(a_S^2/P_S),\tag{1}
\]

where zero-mass pairs are omitted. This is the entropy of the spectral component bit conditioned on the remaining Fourier subset. It is unchanged by interchanging the two components.

Suppose \alpha>1/2 and put \delta=1-\alpha. If \delta=0, B=1, A=0, f=z and \Delta_zH=0. Otherwise 0<\delta<1/2. Pointwise |A|=1-B, so

\[
 |a_\varnothing|=|\mathbb EA|\le\delta,
 \qquad b_\varnothing=\alpha.
\]

Since binary entropy is at most one, the nonempty-pair part is at most

\[
 \sum_{S\ne\varnothing}P_S
   =1-P_\varnothing\le1-\alpha^2\le2\delta.\tag{2}
\]

For the empty pair put x=a_\varnothing^2\le\delta^2 and y=\alpha^2. Its entropy contribution is

\[
 x\log_2\frac{x+y}{x}+y\log_2\frac{x+y}{y}.
\]

Use x+y\le1 and \ln(1+x/y)\le x/y. The contribution is at most

\[
 x\log_2(1/x)+x\log_2e
 \le2\delta^2\log_2(1/\delta)+\delta^2\log_2e.\tag{3}
\]

The second inequality follows because x\log(1/x) increases on 0\le x\le\delta^2<1/4<1/e. All zero expressions are defined by continuity. Since \sup_{0<t<1}t\log_2(1/t)=(\log_2e)/e and \delta\le1/2, (1)--(3) give

\[
 \Delta_zH(f)
 \le\left[4+\frac{4\log_2e}{e}+\log_2e\right]\delta
 <8\delta.\tag{4}
\]

This elementary estimate handles every zero-degree atom explicitly and uses no halfspace noise estimate or KL comparison. A coordinate-decreasing split is handled by reversing z, which preserves entropy and influence.

## 2. Independent check of the candidate's complementary KL proof

The longer candidate proof is also valid. With \alpha>1/2, its A=U-D has \mathbb EA^2=\delta, so Q_S=a_S^2/\delta is a probability law and P_S\ge\delta Q_S. The zero-degree mass is

\[
 Q(0)=(u-d)^2/\delta\le\delta.
\]

Uniform hypercontractivity applies to the signed function A, not just indicators: \|A\|_{3/2}^2=\delta^{4/3}. Thus the proposed low-degree bound holds. In nonempty degrees P_S=2(\widehat U(S)^2+\widehat D(S)^2); applying the Boolean halfspace noise bound to 2U-1 and 2D-1 divides their indicator spectral tails by four. Concavity of t\sqrt{\ln(1/t)} gives the stated pair tail. Zero-density tails vanish by continuity; the small-degree regime uses the nonconstant mass at most 2\delta.

In the coarse KL argument, replacing the exact zero atom by \beta\le\delta is in the correct direction: (1-\beta)\log(1/\delta)-\beta is minimized at \beta=\delta. The logarithm is nonnegative. KL data processing lower-bounds the uncoarsened divergence, and P\ge\delta Q prevents a positive Q atom from having zero P mass. Choosing the A component complements the conditional spectral bit and leaves its entropy unchanged. No degree-zero atom or factor of two is omitted.

Therefore the longer complementary-KL argument and the elementary argument (4) independently establish the same near-dictator conclusion, with different convenient constants.

## 3. Exact local potential decrement

Let C_* be the existing largest-weight split constant, and put K=\max\{C_*,8\}. For an LTF split on a largest absolute defining weight, the prior theorem gives \Delta H\le C_*\alpha. If \alpha\le1/2, this is at most 2K\alpha(1-\alpha). If \alpha>1/2, (4) is at most 8(1-\alpha)\le2K\alpha(1-\alpha). Cases \alpha=0,1 have zero split increment. Hence

\[
 \Delta_zH(f)\le2K\alpha(1-\alpha).\tag{5}
\]

For a monotone split, the two restricted means are \mathbb EA\pm\alpha. Therefore

\[
 \operatorname{Var}(f)
 -\frac{\operatorname{Var}(f^+)+\operatorname{Var}(f^-)}2
 =\alpha^2.\tag{6}
\]

The physical influence split is

\[
 I(f)-\frac{I(f^+)+I(f^-)}2=\alpha.
\]

Subtracting (6) proves that the decrement of I-\operatorname{Var} is exactly \alpha(1-\alpha), not \alpha or \alpha^2. Coordinate sign changes and output sign changes preserve I, variance, entropy and the split increment. Thus the same identity applies after the usual unate sign normalization of every LTF restriction.

Dimension induction with (5) consequently gives

\[
 \boxed{H(f)\le2K\,[I(f)-\operatorname{Var}(f)]}
\]

for every uniform-cube LTF, including constants, arbitrary weights, arbitrary threshold and arbitrary output bias. Constants have all three quantities zero; both restrictions remain LTFs and use the same constant. The Fourier identity

\[
 I(f)-\operatorname{Var}(f)
   =\sum_{S\ne\varnothing}(|S|-1)\widehat f(S)^2\ge0
\]

checks the potential and the dictator boundary case. If one keeps the candidate's longer KL proof, its stated 2C_* constant is valid directly. The shorter proof naturally gives 2\max\{C_*,8\}; the explicit C_* in the prior note is itself greater than 8.

## 4. Balanced composition telescopes exactly

Let the child functions f_i depend on mutually disjoint input blocks and satisfy \mathbb Ef_i=0. Their outputs are independent uniform signs. For F=g(f_1,...,f_m), the Fourier expansion has a unique outer-index decomposition: selected child Fourier subsets are nonempty, so the occupied blocks recover the outer set T. There is no summation or cancellation between different outer sets.

The squared coefficient law therefore gives exactly

\[
 H(F)=H(g)+\sum_iI_i(g)H(f_i),\qquad
 I(F)=\sum_iI_i(g)I(f_i),\qquad
 \operatorname{Var}(F)=\operatorname{Var}(g).\tag{7}
\]

Suppose every component satisfies H(h)\le C[I(h)-\operatorname{Var}(h)] with a common C. Each balanced child has variance one, and \sum_iI_i(g)=I(g). Substituting into (7) cancels the outer influence exactly:

\[
 H(F)\le C\left[I(g)-\operatorname{Var}(g)
             +\sum_iI_i(g)(I(f_i)-1)\right]
       =C[I(F)-\operatorname{Var}(F)].
\]

Thus the strengthened theorem extends with the same constant to every read-once formula with LTF gates, disjoint leaf blocks, and balanced outputs at every nonroot gate. The root may be biased. Leaves are independent input signs or their negatives, with H=0 and I=\operatorname{Var}=1. The induction is independent of depth, formula size and gate fan-in. It does not cover arbitrary shared-input circuits or unbalanced child outputs.

## Verdict and boundaries

Full analytic audit PASS. The local \alpha(1-\alpha) decrement, all zero-degree atoms, the complement-bit entropy interpretation, and the exact balanced composition cancellation are correct. The elementary universal near-dictator lemma is an independent simplification of the longer candidate branch.

This is a stronger LTF bound and a balanced read-once LTF-formula corollary. It does not prove unrestricted Boolean FEI or FEI under nonuniform input-product laws. The prior theorem's external analytic inputs and historical-priority limits remain those documented in [largest_weight_ltf_fei_proof.md](../2026-10-02-largest-weight/largest_weight_ltf_fei_proof.md) and its source checkpoint.
