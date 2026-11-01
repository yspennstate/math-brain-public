# Independent analytic audit of the disjoint-union entropy lemma

2 October 2026. Immutable audit checkpoint for [stripe_extension_union_lemma.md](stripe_extension_union_lemma.md), the union part of [stripe_extension_verify_union_and_chains.py](stripe_extension_verify_union_and_chains.py), and [stripe_extension_union_and_chains_verification.json](stripe_extension_union_and_chains_verification.json).

**Verdict: analytic PASS.** The Fourier entropy inequality, the exact no-joining-edge influence identity, and their conditional FEI consequence are correct. The proof is elementary; finite tests are corroboration, not the justification of the dimension-independent claim. No external priority claim is certified.

## 1. The pointwise entropy comparison

Let e(t)=t\log_2(1/t), with e(0)=0, and L=\log_2e. For a,b_j\in[0,1], put u=\sum_{j=1}^r b_j and suppose a\le ru. Then

\[
 e(a)\le r\sum_j e(b_j)+(L/e)u. \tag{1}
\]

For u=0, a=0. If 0<u\le1, write a=tu with 0\le t\le r. The exact identity e(a)=t e(u)-ut\log_2t and e(u)\ge0 give e(a)\le r e(u)+(L/e)u, since -t\ln t\le1/e for every t>0. Also e(u)\le\sum_j e(b_j): the difference is u times the entropy of the normalized masses b_j/u. If u>1, e(a)\le L/e\le(L/e)u, while every e(b_j) is nonnegative. Thus all cases, including zero coefficient masses, are covered.

## 2. Apply it to the Boolean union

For pairwise disjoint cube subsets E_j, let g_j=1-2\mathbf1_{E_j} and f=1-2\mathbf1_{\cup E_j}. For every nonempty Fourier set S,

\[
 \widehat f(S)=\sum_j\widehat g_j(S),\qquad
 \widehat f(S)^2\le r\sum_j\widehat g_j(S)^2.
\]

All coefficient squares belong to [0,1] by Parseval. Summing (1) over nonempty S gives

\[
 \sum_{S\ne\varnothing}e(\widehat f(S)^2)
 \le r\sum_jH(g_j)+(L/e)\sum_j\operatorname{Var}(g_j). \tag{2}
\]

Replacing component nonempty entropy by full entropy only increases the right side. Component nonempty coefficient mass is exactly variance.

For the zero coefficient, \widehat f(\varnothing)^2=1-v where v=\operatorname{Var}(f). The elementary inequality -x\ln x\le1-x gives e(\widehat f(\varnothing)^2)\le L\operatorname{Var}(f). Put p_j=\Pr(E_j) and p=\sum_jp_j\le1. Then

\[
 \operatorname{Var}(f)=4p(1-p)
 \le4\sum_jp_j(1-p_j)=\sum_j\operatorname{Var}(g_j),
\]

because p^2\ge\sum_jp_j^2. Hence

\[
 \boxed{H(f)\le r\sum_jH(g_j)
              +L(1+1/e)\sum_j\operatorname{Var}(g_j).} \tag{3}
\]

No minority-density convention, connectivity, or boundary separation is required for (3). Empty components contribute zero. The r=0 union is constant and is handled separately.

## 3. Exact influence identity, including its failure term

Let \ell(x)\in\{0,1,\ldots,r\} label outside the union by zero and E_j by j. For coordinate i define

\[
 q_i=\Pr[\ell(X)\ne0,\ \ell(X^{\oplus i})\ne0,\
                     \ell(X)\ne\ell(X^{\oplus i})].
\]

An edge between outside and E_j contributes one to both the union boundary and the component boundaries. An edge joining E_j to E_k contributes zero to the union boundary and two to the component boundaries. All other edges contribute zero. Therefore, with physical flip influences,

\[
 \boxed{\sum_jI_i(g_j)=I_i(f)+2q_i.} \tag{4}
\]

This matches the checker exactly. In particular I(f)=\sum_jI(g_j) if no cube edge joins distinct components. The condition is also necessary for exact equality: the nonnegative q_i cannot cancel. No orientation factor is missing, since all terms sample a uniform endpoint and its i-flip.

Physical disjointness alone is insufficient. Neighboring singleton components yield a joining edge and a strictly positive failure term. This is boundary counting, not spectral orthogonality.

## 4. FEI consequence and scope

Uniform-cube Poincare is immediate from Fourier degrees:

\[
 \operatorname{Var}(g_j)
 =\sum_{S\ne\varnothing}\widehat g_j(S)^2
 \le\sum_S|S|\widehat g_j(S)^2=I(g_j).
\]

If H(g_j)\le C I(g_j) for each component and no joining edge exists, (3),(4) give

\[
 \boxed{H(f)\le[rC+L(1+1/e)]I(f).} \tag{5}
\]

This applies to arbitrary Boolean-cube subsets, conditional on their component FEI bounds and edge separation. Components need not be intervals, monotone, or connected.

For parallel intervals/rays, each component is covered by the proved slab/LTF theorem. An edge changes the score by at most 2w_max. Successive interval gaps strictly wider than 2w_max therefore imply no joining edge regardless of endpoint conventions. The finite-union consequence is valid with arbitrarily narrow component widths. Complementation preserves H and I, so labels may be exchanged when the complementary components meet the hypothesis. There is no reason to assume that one label's gaps are wide for an arbitrary finite-crossing function.

The physical boundary identity also holds on graphs with nonnegative edge weights. The entropy comparison has an abstract orthonormal-basis analogue when that basis contains the constant. An arbitrary graph, however, does not automatically have the cube Walsh spectrum or Poincare constant one. The statement audited here is the uniform Boolean-cube result; a graph version would need explicit spectral and Poincare conventions.

## 5. Checker inspection

The checker independently transforms truth tables, counts edge influences, and evaluates full entropy and variance. Assignment labels enforce physical disjointness. Its assertion includes the failure term 2\sum_iq_i, rather than testing only the special no-joining case.

The 3,200 union cases cover dimensions 1,2,3,4,5,6,8,10 and r=1,2,3,5, including highly unequal component densities. Boolean Fourier coefficients and influence probabilities are dyadic and exactly representable at these dimensions; entropy logarithms remain floating point. These are finite numerical checks, not a general entropy certificate.

A separate rerun is saved in [stripe_union_k_checker_rerun.json](stripe_union_k_checker_rerun.json), leaving the author verification intact. The shared script also checks 616 random-chain examples; those belong to the almost-symmetric theorem and are not needed for the union proof.

No defect was found. The union note correctly states strict gap separation, avoiding the equality-endpoint problem in the earlier parallel-slab candidate.
