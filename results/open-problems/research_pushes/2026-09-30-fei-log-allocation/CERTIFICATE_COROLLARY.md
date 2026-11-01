# Hereditary short certificates: arbitrary bounded-width DNF and CNF

Date: 2026-09-30. A constructive corollary of the audited universal logarithmic allocation theorem. Independently mathematically reviewed. This is a restricted-class theorem, not full FEI. Literature novelty is unverified.

## Theorem

Let w>=1. Suppose a class of Boolean functions is closed under physical coordinate restrictions, and every nonconstant member has at least one ordinary coordinate certificate of length at most w, for either output value. Then

    H(f)<=[w+2+7/(2 ln2)] I(f)<(w+7.049433) I(f).                (1)

In particular this holds for every width-w DNF or CNF, with arbitrary positive and negative literals, arbitrary overlaps, and no bound on the number of terms or variable occurrences. Contradictory DNF terms may be discarded; every nonconstant restriction has a satisfiable term of size at most w. CNF follows by negation.

The coefficient depends on w. Every Boolean function can have w as large as its dimension; this dependence is exactly why (1) does not solve unrestricted FEI.

## 1. Certificate-coordinate influence lemma without monotonicity

Let f have a certificate fixing coordinates i_1,...,i_l to specified values and forcing output+1. Put q=Pr[f=-1], and let q_j be that probability after fixing the first j certificate coordinates. Then q_0=q and q_l=0.

At step j, the difference between the average of the two child probabilities and the selected child probability is bounded by half the physical influence of i_j on the currently restricted function. Also unconditional influence is the average over all 2^(j-1) prefix assignments of these conditional influences. Therefore

    |q_(j-1)-q_j|
       <=(1/2) Inf_(i_j)(f|prefix)
       <=2^(j-2) Inf_(i_j)(f).

Telescoping absolute differences gives

    q<=sum_(j=1)^l 2^(j-2) Inf_(i_j)(f)
      <=[(2^l-1)/2] max_(i in certificate) Inf_i(f).             (2)

No monotonicity of q_j or f was assumed. If the certificate forces -1, negate f first. With m=min(Pr[f=1],Pr[f=-1]), (2) supplies a coordinate of actual physical influence d satisfying

    d>=2m/(2^w-1).                                             (3)

The September24 monotone down-set report proved the same selector for minterms by a different, monotonicity-specific argument. The forced-coordinate telescope removes that hypothesis.

## 2. The smaller child is close to a constant

For any physical coordinate, let the root-minority output probabilities in its two children be m_0,m_1. Their average is m, so one is at most m. For that child u,

    kappa(u)=1-max_T uhat(T)^2
       <=1-(Eu)^2=4m_u(1-m_u)<=4m.

Consequently the smaller child character defect obeys kappa_min<=4m, whether or not either child is monotone.

## 3. Local entropy payment

The audited theorem in REPORT.md says, for j=min(d,1-d),

    B_i(f)<=j[C_log+log2(1+kappa_min/(2j))],
    C_log=2+3/(2ln2).

For a>=0 the function x[C_log+log2(1+a/x)] is increasing for x>0. Indeed its derivative is

    C_log+[ln(1+a/x)-a/(x+a)]/ln2>0,

using ln(1+z)>=z/(1+z). Thus the same bound remains valid with j replaced by d; the endpoint j=0 has B_i=0 separately. Using (3) and kappa_min<=4m,

    B_i(f)<=d[C_log+log2(1+2m/d)]
           <=d(C_log+w).                                      (4)

The exact physical entropy identity and the already proved universal recombination bound give

    H(f)-[H(f_i^+)+H(f_i^-)]/2
      =B_i(f)+JS(f_i^+,f_i^-)
      <=B_i(f)+(2/ln2)j
      <=[w+2+7/(2ln2)]d.                                      (5)

## 4. Induction

Both children remain in the class. Constants have zero entropy and influence. Applying induction to the children and using

    I(f)=d+[I(f_i^+)+I(f_i^-)]/2

turns (5) into (1), with the same coefficient at every depth. There is no repeated minor-child surcharge. QED.

## Additional monotone refinement

For a monotone function, after choosing the root-minority output and orienting the queried bit appropriately, one child has minority probability m-d/2. Hence

    kappa_min<=4(m-d/2)(1-m+d/2)<=4m-2d.

Replacing the estimate in (4) accordingly gives

    B_i<=d[C_log+log2(2m/d)].

For the same certificate selector, monotone width-w DNF/CNF therefore obey

    H(f)<=[2+7/(2ln2)+log2(2^w-1)]I(f).                        (6)

For w=2 this coefficient is 8.634395143..., improving the repository's earlier 9.41 bound by this direct consequence. No claim of the sharp class constant is made.

An additional two-packet scalar relaxation for unate splits was explored numerically and suggests a smaller coefficient, but it is not used or certified here.

## Source comparison and independent audit

The complete report and the nonmonotone extension were independently checked. The reviewer confirmed (2), the child-variance estimate, monotone extension from j to d, and induction.

The September24 repository continuation proofnet24/P03-fei/continuations/2026-09-24-downset/REPORT.md gives monotone width-w coefficient w+8.1 and monotone width2 coefficient9.41. Equations (1) and (6) are a comparison against those exact repository statements, not a literature-first claim.

A targeted primary-source check of Arunachalam, Chakraborty, Koucky, Saurabh and de Wolf, Improved bounds on Fourier entropy and Min-entropy, arXiv:1809.09819 (https://arxiv.org/abs/1809.09819), found bounds involving average unambiguous certificates and min-entropy/minimum-certificate bounds. Its stronger proposed entropy bound in terms of min(C0,C1) alone is different from (1), which retains I(f); this corollary does not establish that proposal or Mansour's conjecture. Bounded search did not establish publication priority for (1).

The remaining full-scope need is to avoid a worst-case width charge on general Boolean functions, while preserving the real packet cancellations and one-time influence budget. This report supplies an actual constructive restricted application of the logarithmic lemma, not that missing universal step.
