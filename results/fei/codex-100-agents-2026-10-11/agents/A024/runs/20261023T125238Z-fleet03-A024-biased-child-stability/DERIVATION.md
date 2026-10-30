# A024 v6: actual overlap before payment

All entropies are in bits. All restrictions fix physical input coordinates of a uniform cube; untouched coordinates remain independent and uniform. Write e(s)=-s log2(s), e(0)=0, L(a,b)=e(a²)+e(b²)-e(a²+b²), and B_i=sum_{S not containing i} L(fhat(S),fhat(S+i)). The v5 proof of 0<=L(a,b)<=2|ab| is retained. Let d=Inf_i(f), and A(f)=sum_S |fhat(S)|, the Fourier algebra norm.

## 1. Universal actual-function overlap price

For every Boolean f and every coordinate i,

    B_i <= 2 sum_S |fhat(S) fhat(S+i)|
        <= 2 d sum_{S not containing i}|fhat(S)| <= 2 A(f) d.       (8)

Indeed fhat(S+i) is a Fourier coefficient of (f|i=0-f|i=1)/2. This derivative has absolute value one exactly on the pivotal set and zero elsewhere, so every such coefficient has absolute value at most d. This proves (8), including d=0, without a division by a mean or variance. Its first bound uses the actual spectrum after all interference. A(fg)<=A(f)A(g) follows from Fourier convolution and the triangle inequality. A physical restriction cannot increase A: child coefficients are sums or differences of the two parent fiber coefficients. A character has norm one. A nonempty affine-flat indicator has norm one: on its annihilator all coefficients have magnitude Pr(A), and there are 1/Pr(A) of them. The empty indicator has norm zero. These facts hold for arbitrary affine orientations and cosets.

Consequently for any two affine flats A,B, including empty flats, and any affine phase q,

    f=(-1)^q (1-2*1_(A union B))
      =(-1)^q (1-2*1_A-2*1_B+2*1_(A intersection B))

has A(f)<=7. This is a single actual-function bound; it does not add two separately renewed accounts. In particular every coordinate satisfies B_i<=10d. If f is a constant sign times a flip on B\A its norm is at most five; a single-flat flip has norm at most three.

### Sharper affine half-spectrum price

The norm-seven estimate alone gives14d, but the actual half-spectrum in (8) gives10d. For a physical direction e_i and nonempty flat A with direction space V_A, its Fourier support is W_A=V_A^perp. If e_i is not in V_A (a transverse query), exactly half of W_A has i in its label; therefore each half of the flat-indicator spectrum has l1 mass1/2. If e_i is in V_A (a tangent query), all support excludes i. Multiplication by the affine character of q translates these supports: a tangent flat contributes half-mass1 when q excludes i, and0 when q contains i; a transverse flat still contributes1/2. Empty flats contribute0.

If both A and B are tangent, their union is invariant under i. The actual f is then either independent of i or changes sign identically along i, so each Fourier fiber has at most one nonzero coefficient and B_i=0. Otherwise at least one flat is transverse, and their nonempty intersection is also transverse. When q excludes i, the half-spectrum triangle bound is at most1+2(1/2)+2(1)+2(1/2)=5, including its character term. When q contains i, the character term and tangent-flat terms contribute0, so the bound is at most3. Equation (8) thus proves B_i<=10d for EVERY coordinate of an affine phase with a two-flat union edit. These are bounds on the same actual half-spectrum, not separately spent banks. In the degree-three pivot cases below the bounds were already<=10d, so the hereditary class improves toK10.

## 2. Quadratic phase with two possibly overlapping flat edits

Claim: for every dimension, quadratic F2 polynomial q, and affine flats A,B, every nonconstant f=(-1)^(q+1_(A union B)) has a physical coordinate with B_i<=10 Inf_i(f). The class is closed under every physical restriction, so it has a complete selected 10-good continuation after every physical prefix. Empty flats and dimension-zero constant leaves are allowed. This is an author proof, pending independent reconstruction.

We use two elementary polynomial facts. An affine flat of codimension k is the product over F2 of k affine linear equations; its indicator has degree at most k. A nonzero F2 polynomial of degree at most r has support probability at least 2^(-r). For the latter, induct on the number of variables: if independent of the last variable, use induction; otherwise write P=P0+x_n P1 with nonzero P1 of degree at most r-1. On every input where P1=1 exactly one of the two extensions has P=1, giving probability at least (1/2)2^(-(r-1)). Constants start the induction. Thus a nonconstant phase of degree at most three has some active coordinate of influence at least 1/4. A genuinely quadratic phase has an incident coordinate of influence exactly 1/2. If two functions differ on a set of density epsilon, any coordinate's influences differ by at most 2epsilon, since a changed edge must have at least one endpoint in the edit set.

If q is affine, apply the sharper affine half-spectrum price above. Otherwise sort the two nonempty codimensions k<=l, with an empty flat assigned infinity.

* If k>=4, the edit density is at most 1/8. An incident quadratic coordinate retains influence at least 1/2-2/8=1/4; B_i<=1 (conditional entropy of the two-point fiber label) therefore gives B_i<=4d. This includes the case of two empty flats.
* If k<=3 and l>=4, set g=(-1)^(q+1_A), which has degree at most three. The actual f differs from g only on B\A, of density at most 1/16. If g is nonconstant, choose its active coordinate: d_f>=1/4-2/16=1/8, hence B_i<=8d_f. If g is constant, f is a constant sign times a flip on B\A, so (8) and norm five give B_i<=10d_f at every coordinate.
* If k,l<=3, put C=A intersection B and g=(-1)^(q+1_A+1_B), of degree at most three. Since 1_(A union B)=1_A+1_B+1_C over F2, f=g*(-1)^1_C. If C is nonempty of codimension at most three, the full exponent also has degree at most three; an active coordinate gives d>=1/4. Otherwise C is empty or has density at most 1/16. If g is nonconstant an active coordinate retains d_f>=1/8. If g is constant use the single-flat norm-three bound in (8). Constant f needs no query.

These cases exhaust arbitrary nonparallel flats, unequal codimensions, containment, coincident flats, disjoint cosets and deterministic limits. No affine coordinate change is used to select the physical query. B_i<=1 follows by grouping the squared Fourier spectrum into fibers: it is the average binary entropy within a fiber, bounded by the total spectral mass one.

## 3. Actual disjoint composition and prefixes

Disjoint products preserve the coordinate ratio B_i/d_i: their spectra tensorize, L(ca,cb)=c²L(a,b), and influences are unchanged by multiplying a disjoint Boolean factor. The v5 exact binary-activation identity for arbitrary disjoint Boolean w,h is retained:

    F=1-(1-w)(1-h)/2, r=Pr(h=-1), d_F=r d_w,
    B_i(F)=r B_i(w)+R_r(Ew,beta), R_r<=6r d_w.

Thus OR/AND of any finite number of disjoint products of the new two-flat components has a selected 16-good physical continuation, after every physical prefix. Group all other factors into h, which may have any output mean; this induces biased outer inputs and does not bias any remaining physical input. At r=0 the output is deterministic and both B,d vanish. At r=1 the transport remainder is exactly zero. No rare logarithm is left in this scalar transport. Corrected FEI+ is sum over nonempty S of p_mu(S) log2(product_{j in S}(1-mu_j²)/p_mu(S)); no output-variance factor belongs in its numerator, and deterministic children must first be contracted.

Let an already executed physical stopping prefix have prior debit U_K and full actual terminal functions f_l, with their real reach probabilities p_l. Splicing these continuations adds zero further bad-node odd-face debit at K=10 for products or K=16 for activation. U_K is retained exactly. Neither terminal entropy, any reference/KL liability, nor any earlier expenditure is discarded. The exact identities are

    I(f_root)=I_spent_prefix+sum_l p_l I(f_l),
    H(f_root)=sum_prefix p_v[H(f_v)-(H(f_v0)+H(f_v1))/2]
              +sum_l p_l H(f_l).

This does NOT pay U_10 or replace it by U_16, and does not transfer an old prescribed-tree potential to the repaired order. If the original account already used threshold 16, its old debit is unchanged and its continuation liability here is zero. Without such a premise the old threshold-10 account remains open. Using inherited B05 localization with c_JS=2/ln2 gives relaxed entropy constants 13 for the product class and 19 for its OR/AND class. These corollaries depend on the inherited localization proof's review status.

### Credit needed for changed inner means

The inherited remainder bound explicitly asks for at most6*d_F units of credit per ACTUAL lifted query. Over any physical prefix its accumulated positive remainders are at most6*I_spent_prefix. The influence identity leaves the exact unspent source potential6*sum_l p_l I(f_l) from an ORIGINAL reserve6*I(f_root), provided this reserve was earmarked and each earlier debit was booked against it. This specifies a sufficient influence-priced credit with both full terminals retained; it does not establish that a previously diminished threshold10 bank possesses that reserve. Any old debit U must still be subtracted; a new reserve cannot be installed retrospectively. Thus the inner two-flat K10 repair closes, while changing its inner-output means in actual OR composition still needs this same-account6*d_F payment to retain threshold10. Threshold16 avoids additional bad-node debit without claiming payment of old threshold10 liabilities.

## 4. Exact first unsupported line

There is no proof that an arbitrary Boolean residual admits the two-flat representation with a bounded number of edits, bounded algebra norm, or a robust bounded-degree pivot. Nor is the old threshold-10 debit for the enlarged class paid from its diminished original bank. Equation (8) does not help uniformly when A(f) is unbounded; it cannot be substituted for a universal O(I) selected-tree price of the v5 localized overlap liability. Full FEI remains OPEN. The proposed next action is an actual two-flat mixed-query replay at threshold 10 with both terminals and old debit retained, testing whether the algebra-norm price can be replaced by a debit from the original reserve.
