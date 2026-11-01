# Root normalization is paid for every signed implicant table

Let f:{-1,1}^n -> {-1,1} be nonconstant, q=Pr(f=-1)>0, v=4q(1-q), and I_i its physical influence. Fix any finite table of conjunctions implying f=+1. Gate e fixes w_e>=1 physical coordinates R_e to specified signs. It need not be prime, and its signs may disagree with other gates. Set pi_e=2^-w_e. Fix positive weights satisfying sum_(e:i in R_e) lambda_e<=1, and D=product_e(1+lambda_e*pi_e)-1. All logarithms in costs are base two.

For k=min_e w_e, put a_k=(1-2^-k)/k. Then

    S=sum_e lambda_e*pi_e <= a_k I/(2q),                    (1)
    v log2 D <= [2 a_k (1-q)/ln 2] I.                     (2)

In particular (2) is at most (1-q)I/ln 2 for every signed implicant table; when all widths are at least two it is at most 3(1-q)I/(4 ln 2). No private leaves, monotonicity, independence between gates, posterior choice, or Fourier-profile assumption is used. The bound concerns the same original D, not a substitute reference. A universal upper bound for a signed term does not erase a negative value of that term.

## A local physical inequality

Every nonempty proper subset B of the w-cube has at least w undirected boundary edges. Here is a proof, including the boundary cases. The claim is immediate for w=1. Split into two (w-1)-cubes. If both layers are nonempty and proper, induction gives at least 2(w-1)>=w boundary edges for w>=2. If exactly one is nonempty and proper, it contributes w-1 internal boundary edges and differs from the constant other layer on at least one vertical edge. If both layers are constant and the full set is nonempty and proper, they are opposite, giving 2^(w-1)>=w vertical edges. These cases exhaust the possibilities.

Fix a gate e and an assignment outside R_e. The false set B in the remaining w_e-cube excludes the gate's satisfying point. Thus B is either empty or nonempty proper. In the latter case

    |boundary B| >= w_e >= w_e |B|/(2^w_e-1).

The same displayed lower bound is zero when B is empty. Average over outside assignments. A physical influence is twice the number of undirected crossing edges divided by the cube size, so

    sum_(i in R_e) I_i >= [2q w_e/(2^w_e-1)].             (3)

This step uses actual physical boundary edges; it does not replace physical restriction by spectral conditioning. All false fibers have at least one true point because the SAME fixed gate is an implicant on every outside assignment. Mixed gate signs cause no problem. If a gate is merely correlated with f rather than implying it, this premise fails.

Rearranging (3), with q>0, gives

    pi_e <= [(1-2^-w_e)/(2q w_e)] sum_(i in R_e) I_i.

The sequence (1-2^-w)/w is nonincreasing for integers w>=1: the adjacent comparison is equivalent to 2^(w+1)>=w+2. Multiply by lambda_e, sum, and use the packing rows to obtain (1). For a single AND_k gate at weight one, (1) is equality. This checks the factor two, the width dependence and the nonzero denominator.

Since D>0 and ln D <= ln(1+D)=sum_e ln(1+lambda_e*pi_e)<=S, multiplying by v>=0 proves (2). The bound remains valid when D<1; no absolute value, truncation or second root credit is introduced. If a table contains a width-zero gate, f is constant +1 and is handled separately. Constant -1 has no such nonempty table.

## What this removes, and what it leaves

In the original conditioned forest ledger, Lambda+log2 Z=log2 D. Therefore this SAME root-normalization contribution is universally O(I) for conjunction implicants. Individual root rarity charges remain in the occupation bill. Any successful proof must still pay those rarities and the whole expected label, subset, attachment and rank costs after the legitimate posterior ambiguity refund. This argument supplies none of those payments and does not prove FEI. It applies to arbitrary Boolean implicant tables, whereas A009's complete <11I result still needs genuine private neighbors.

The next unpaid line is a fixed packing whose complete non-root occupation bill is O(I) on shared/leafless incidence, keeping the original output law. With (2), root normalization no longer needs a separate private-leaf or positive-controller hypothesis for this table type.

## Immediate substitution into the independently reviewed A009 reference

A009 v1's unchanged private-block queue gives C_PL <= (log2 96)I+(9/4)I+v log2 D. Its gates all have width two. Substituting (2), without changing its weights, events, spectrum or normalizer, gives

    C_PL <= [log2 96+9/4+3(1-q)/(4 ln 2)]I
         < (399/40)I < 10I.

For the strict rational comparison use log2 96<33/5 (equivalently 3^5<2^8) and ln 2>2/3 (the first positive atanh-series term is 2/3, with further positive terms). Then 33/5+9/4+9/8=399/40. This is downstream use of the universal root payment on an existing reference, not a new claim about arbitrary graph labels or full FEI.
