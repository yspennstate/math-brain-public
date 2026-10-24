# Seven-edit collapse and eight-edit physical stopping theorem

All entropy is in bits. Let q be any degree-at-most-two polynomial on F_2^n, M any linear address map, and E at most eight distinct vertices in one M-fiber. The actual Boolean function is F(x,y)=(-1)^q(x)(1-2 1_E(x)) y_(Mx), with independent named data signs. Repeated address values mean the same physical coordinate. We prove an adaptive physical stopping tree has zero localized K=4 bad-boundary bill and H(F)<=7(I(F)-1). If |E|<=7, the stronger H(F)<=(4+2/ln2)(I(F)-1) holds. No universal FEI theorem is asserted.

## 1. Preserved ledgers and critical certificates

INHERITED_PROOF.md sections1,2,4,5,6 and DERIVATION.md preserve the exact signed Fourier update, crossing-edge influence identity, shared-label fiber entropy identity, generic D<=4 erasure certificate, D=5 two-edge certificate, terminal payment, and scalar Jensen-Shannon inequality. They are reproduced locally; critical.py and ternary.py rerun their complete exact critical alphabets. No unsigned mixture, resampling refund, or fresh copy of a reused data bit is introduced.

In detail, with delta=2^-D at a restricted phase node and b=(-1)^q, its coefficients change by -2delta sum_(w in E)b(w)chi_S(w). If Q is the alternating polar matrix and ell the conditional linear coefficient, a nonzero polar row has baseline influence1/2 and

    Inf_i = 1/2 + 2delta sum_(w in E,w+e_i notin E)(-1)^(ell_i+(Qw)_i).

An active address coordinate has actual influence1/2 regardless of the phase. Data influence totals exactly1. A query has entropy decrement B_i+JS_i, with B_i<=h2(Inf_i)<=1 and JS_i<=2Inf_i/ln2. The bad-node boundary is C_i=2 sum_(z,S contains i)|S|p_(S,z), including the retained data degree. The tree below never queries a K4-bad node, so it spends none of this boundary bill.

The complete exact critical certificates are: every coordinate of every Boolean phase on D<=4 obeys B_i<=4Inf_i; on D=5, Inf_i=1/8 also obeys this inequality. The latter normalizes only the unqueried child coordinates; it preserves the selected B and influence, not arbitrary physical influences. Its 2187 ternary cores give13 integer-product histograms. For Inf_i>=3/16, h2(t)/t decreases and h2(3/16)<3/4, certified by 3^3*13^13>2^52. Influence0 has B=0.

## 2. The exact seven-edit all-weak collapse

Only D=5 and exactly seven remaining edits can require a new rule. A quadratic on five bits has an even number of negative values: modulo2 its truth-table sum is zero, since each monomial of degree<=2 is1 on an even number of vertices. Flipping seven points makes that count odd. The number of pivotal undirected edges in ANY coordinate has the same parity as the negative-vertex count (partition vertices into its16 pairs). Thus every influence is an odd multiple of1/16. For a polar row the crossing bound gives Inf_i>=1/2-14/32=1/16. A row is either weak, meaning1/16, or at least3/16 and therefore K4-good.

Suppose every nonzero polar row is weak. Equality in the crossing bound forces, for each such row, all seven edits to cross different boundary edges, and ell_i+(Qw)_i=1 for every w in E. Hence Qw has one fixed value on E. Rows that are zero already impose a constant zero constraint. Therefore E lies in one affine coset A=z+ker Q. A nonzero alternating matrix on five bits has rank2 or4. Rank4 gives coset size2, impossible for seven distinct edits. Consequently rank Q=2, |A|=8, and E=A minus one vertex v.

Choose physical indices i,j with Q_ij=1 and put a=Q_i, b=Q_j. Rank2 and alternating symmetry imply

    Q_km = a_k b_m + b_k a_m  (over F_2).

For example, the two independent columns i,j span the column space, and their i,j entries determine every other column's coefficients. The coset indicator polynomial is

    J_A(x)=(1+a dot (x+z))(1+b dot (x+z)).

Its polar matrix is Q. Thus q+J_A is affine. At w in A, its derivative along coordinate k is the sum of the q derivative and 1+(1+a_k)(1+b_k). The latter equals1 precisely when (a_k,b_k) is nonzero, equivalently when Q_k is nonzero. The all-weak hypothesis makes the q derivative1 on exactly these rows, so the affine polynomial q+J_A has linear coefficient zero on every nonzero polar row. On a zero row its coefficient is ell_k. This establishes the collapse in the original physical coordinates, without a linear change of input basis:

    (-1)^q(1-2 1_E) = sign * chi_l * (1-2 1_{v}),
    l_k=0 whenever Q_k is nonzero.

Its actual Fourier amplitudes, up to signs and character shift, have squared numerators900 once and4 thirty-one times, denominator1024. Every unmodulated coordinate has influence1/16; each coordinate in l has influence15/16. Character modulation preserves entropy and only increases influence. The sparse terminal lemma with s=1 proves H<=4I_phase. Stop here, retaining the complete actual phase and its named data sign. The proof does not merely infer a useful representation and discard its entropy.

collapse.py enumerates all155 rank-two alternating matrices, all4 cosets, all8 missing vertices and every allowed conditional linear part on the zero rows:13120 cases. It independently checks the factorization, indicator truth table, affine character, zero-row support, actual edited truth table, direct physical edge influences and integer Walsh histogram. The rank4 impossibility is the proved dimension argument, not a claimed rank4 census.

## 3. Adaptive physical tree for at most eight edits

First query address-active physical coordinates; they have influence1/2. After the address is fixed, stop unedited branches at their actual quadratic phase. Stop edited branches whose restricted polar matrix is zero at their character times edit mask. Otherwise:

* At D>=6, at most eight edits give Inf_i>=1/2-16/2^D>=1/4 for every polar row. Query any such physical coordinate.
* At D<=4, every physical coordinate is K4-good by the generic certificate. Query a polar row.
* At D=5 with at most six edits, use the inherited two-edge certificate or the >=3/16 entropy bound.
* At D=5 with seven edits, query a polar row of influence>=3/16 if one exists. If none exists, apply section2 and stop at its paid one-point terminal.
* At D=5 with eight edits, the negative-vertex count is even, so every coordinate has an even number of pivotal edges. A positive influence is at least1/8. Influence1/8 is covered by the two-edge certificate; larger even lattice values are at least1/4, and influence0 has B=0. Query any polar row.

Every query satisfies B_i<=4Inf_i. The tree terminates since each query removes one physical control. Restrictions preserve the edit-count bound and the actual affine address. Zero-influence representation pivots are allowed, with entropy decrement zero. No same gate label is charged again when reused across levels.

## 4. Complete terminal payment and constants

For any character times an s-point mask with s<=8, the inherited sparse/dense proof gives H<=7I_phase. For density u=s2^-D<=1/4, character modulation cannot decrease influence, the spectral tail mass is v=4u(1-u), and edge isoperimetry gives I>=2u log2(1/u). These imply H/I<=4+log2 s<=7. For u>1/4, 2^D<4s<=32 forces D<=4, and actual influence granularity gives H<=(D-1+log2 e)I<7I. Constants have zero entropy. Clean quadratic terminals obey H<=2I_phase; collapsed terminals obey H<=4I_phase.

For at most seven edits, terminal rate C7=4+log2 7 is below K=4+2/ln2: e>1+1+1/2+1/6=8/3 gives e^2>7. Access rate K is below7: ln2>2/3 follows from ln2=2(1/3+1/(3^3*3)+...)>2/3. Thus, writing A for weighted queried influence and T for weighted terminal phase influence,

    I(F)-1=A+T,
    H(F)<=K A+C7 T<=K(I(F)-1)  (|E|<=7),
    H(F)<=K A+7T<=7(I(F)-1)   (|E|<=8).

The weighted terminal data influence is exactly1, including when distinct leaves retain the same physical data sign. It is the influence partition under conditioning, not a new independent bit per leaf. This proves the stated scoped theorem with the full terminal bill.

## 5. Preserved obstruction and first unsupported universal line

The five-control seven-edit fixture q=x0*x1+x1*x2+x3*x4, E=[7,11,15,19,23,27,31] still has a bad minimum-index pivot, exact B>4Inf iff 2^192*13^156>3^180*5^200, and full fixed-order boundary bill3/8. The adaptive rule selects a good pivot and gives bill0; seven.py reruns both original policies. No assertion that every pivot is good replaces this obstruction.

The first unsupported continuation is an adaptive good-pivot or single-reserve payment lemma for arbitrary nine-edit five-control nodes. At influence1/16 the crossing sum is -7, but nine edits can now realize seven crossing negative endpoints plus one internal edited edge, or nine crossing endpoints with eight negative and one positive derivative. The seven-edit equality no longer pins the entire edit set to one radical coset. Larger edit counts also make the sparse terminal bound grow like log s. A count-independent refinement with the SAME retained terminal reserve is not proved. Full FEI remains open.
