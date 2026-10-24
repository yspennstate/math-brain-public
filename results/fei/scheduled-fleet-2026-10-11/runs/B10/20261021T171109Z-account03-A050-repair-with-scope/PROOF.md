# A fixed-reference repair for a non-point core

All Boolean inputs are uniform; entropy and KL are in bits. This is a sufficient conditional repair. Full FEI remains open.

## 1. What must be paid

Let P be a Boolean root spectrum and Q a normalized dominating complete reference. At every fresh physical query erase that frequency from both laws, use the SAME actual coherent branch channel, and normalize Q by its own outcome probabilities. On a source-zero erased row choose the fair channel. Never discard reference-only atoms or substitute a new reference.

Writing A=D(P||Q), the full KL chain rule gives

    A = sum_reached(erasure KL + outcome KL) + mean_terminal KL.       (1)

All terms are nonnegative. One-step proof: conditional erasure likelihood times branch-outcome likelihood times inherited-child likelihood equals P(s)/Q(s) for each occupied original atom and each branch with positive actual kernel. Average its logarithm. Reference-only rows have zero source expectation but remain in normalization and branch probabilities. This proves (1), including arbitrary finite adaptive stopping.

Put H0=H(root), Hf=mean H(leaf), If=mean I(leaf), R=I(root)-If>=0, D=H0-Hf, S=4If-Hf. The conservative whole liability is

    L=A+[D-4R]_+.

This is one bill, not the sum of A and the released pieces of A. If CE(P,Q)<=M and H0,Hf>=2, then

    L=max(A,A+D-4R)
      <=max(M-H0,M-Hf-4R)<=M-2.                              (2)

The signed expression D-4R must be retained before taking its positive part. If a genuinely unused certified terminal owner S dominates L, then

    H0+A <=4I(root),

because 4I(root)-H0-A=S-(A+D-4R)>=S-L. This pays every term in (1) and the positive query deficit once, while retaining every terminal entropy. Previously booked conservative overpayments omega>=0 require L+omega, not a new owner. No earlier ancestor debt is supplied by this theorem.

Equation (2) is the scalar step submitted to Lean. It does not formalize Fourier transport, entropy, the canonical reference, or the analytic application.

## 2. Canonical reference: existence without a square-sum assumption

Let h be any Boolean function on data z; t=Pr(h=-1), d_j=Inf_j(h). Define

    F_h(x,a,b,z)=(-1)^a if x=0;
                  h(z) if x=b=1;
                  +1 otherwise.

Its exact marginals are (1/2,1/2,t/2,d_j/4). Its empty mass is p0=(1-t)^2/4, v=1-p0>=3/4. Delete dummy coordinates before forming a reference. Put r_i=Inf_i(F_h)/v. Every remaining r_i lies in (0,1), and sum r_i=I(F_h)/v>1: the xa coefficient has squared mass1/4 at degree2. At least two r_i are positive.

The canonical occupancy parameter c is the unique positive solution in (0,1) of

    1-c=product_i(1-c r_i).                                  (3)

For a proof define phi(c)=[1-product_i(1-c r_i)]/c on c>0, with continuous phi(0)=sum r_i. The telescoping polynomial identity is

    phi(c)=sum_i r_i product_{j<i}(1-c r_j).

Each term is nonincreasing on [0,1], and the second is strictly decreasing. Thus phi is strictly decreasing, phi(0)>1, and phi(1)=1-product_i(1-r_i)<1. The intermediate value theorem gives exactly one c with phi(c)=1. This proof needs no condition sum r_i^2<1. All denominators v,c are positive; product factors stay positive.

Set Q(empty)=p0 and, for nonempty s,

    Q(s)=(v/c) product_i(c r_i)^{s_i}(1-c r_i)^{1-s_i}.

Equation (3) proves normalization and exact marginal matching. The logarithm on nonempty atoms is affine in membership. Since P and Q agree in empty mass, nonempty mass and every marginal,

    CE(P,Q)=H(Q)<=2+G(h),
    G(h)=h2(t/2)+sum_j h2(d_j/4).                            (4)

All source atoms are dominated. Endpoints t=0 cause no difficulty after deleting dummy b/data bits; the two x,a reference parameters remain positive and below1. The all-dimensional application below has t>0 and no dummy bits.

## 3. Hereditary admissibility and its precise scope

Query b first. Thereafter query arbitrary fresh data bits adaptively in the b=1 branch, keeping x,a unqueried and retaining b=0. Stop anywhere, with all terminal spectra included. Suppose each reached terminal data core g has a supplied certificate H(g)<=4I(g). This is a hypothesis about actual leaves, not about Boolean functions in general.

For any such g, the independent character on a separates its spectral support from the other branch, giving exactly

    H(selector((-1)^a,g))=2+H(g)/2,
    I(selector((-1)^a,g))=1+I(g)/2.

Hence each leaf has H>=2 and actual unused S4>=2. The b=0 leaf has H=2,I=1. Every root coefficient has magnitude at most1/2: the a and xa coefficients are1/2; the empty/x terms have magnitude (1-t)/2; the b/xb terms have magnitude t/2; remaining data coefficients have magnitude at most1/4. Therefore H0>=2.

Consequently, for any sigma<2, the additional computable hypothesis

    G(h)<=sigma AND the supplied final surplus is unused               (5)

implies L<=G(h)<=sigma<S, with at least 2-sigma remaining. This holds through every stated data-only continuation using the same initial Q and same owner. No independent renewal of canonical marginals occurs at descendants.

Comparison of repairs: (a) exact conditional likelihood matching is sufficient for zero conditional cost but excludes nonmatching examples; (b) the prior rowwise second-moment hypothesis prices conditional KL only and does not alone price the quotient/source account; (c) (5) together with certified terminal slack pays that full account, without requiring matching or a conditional influence price. These are differently scoped sufficient conditions; there is no claimed global ordering or globally weakest repair. Within (2) plus marginal subadditivity (4), G is the exact excess supplied by this particular certificate. The sharper exact CE-H floors can admit further cases.

Excluded operations are querying x/a, choosing fresh descendant references without paying their reset, omitting the b=0 terminal, using an already spent terminal owner, and admitting arbitrary cores without terminal certificates. Arbitrary high-degree parity cores fail (5): G=h2(1/4)+k h2(1/4) grows with k. This excludes a universal claim rather than contradicting the known FEI bound for parity itself.

## 4. A non-point family with two nonconstant data children

Let h be the product of m point-defect signs on disjoint blocks of width r:

    h(z)=product_{ell=1}^m [1-2 1_{block ell is all ones}].

Write delta=2^-r. Then

    t=[1-(1-2delta)^m]/2<=m delta,
    Inf_j(h)=2delta for every data bit,
    G=h2(t/2)+mr h2(delta/2).

Every restriction is a product, up to an overall sign, of point defects on the surviving disjoint blocks; some blocks may become constant. Tensor Fourier laws have additive entropy/influence. For a k-bit point defect, epsilon=2^-k, the nonempty entropy is 8(k-1)epsilon(1-epsilon), and the empty contribution is <=4epsilon(1-epsilon)/ln2. The inequality ln2>1/2 gives H<=8k epsilon=4I for k>=2. k=0,1 are constant/character and have zero entropy. Thus every actual terminal certificate required in Section3 is proved.

For r>=8 and 2<=m<=r, m delta/2<1/2. Binary entropy is increasing there, and h2(u)<=u log2(e/u), with log2(e)<3/2. Thus

    G < m(r+1)(r+5/2)/2^(r+1)
      <= r(r+1)(r+5/2)/2^(r+1)
      <= 189/128 <3/2.                                   (6)

The last bound is attained by its rational upper envelope at r=8. Its successive ratio is (r+2)(r+7/2)/[2r(r+5/2)]<1, since the denominator minus numerator is r^2-r/2-7>0 for r>=8. This is an all-r proof, not extrapolation of the boundary checks. It pays L<189/128 from the same certified S>=2, leaving more than67/128 bit.

After b=1, querying any first data bit has two nonconstant core children when m>=2,r>=2: the zero child retains the other m-1 nonconstant blocks; the one child has a nonconstant (r-1)-bit block and the other blocks. In particular this is a weak data exposure rather than an immediate point-core collapse. At the two-query tree the exact removed influence is t/2+delta/2; the second term includes the physical b=1 reach1/2 and the x-selected data-query influence delta.

## 5. Independent source review and remaining obstruction

A047's complete fixed-reference payment, run20261014T124731, Sections1-5, is accepted at stated scope by a fresh reconstruction of (1)-(2), the occupancy matching argument, point-defect terminal certificate, and its balanced overpayment ledger. In that balanced fixture the old conservative withdrawal plus remaining source/quotient costs equals A+log2(V)/4, not A or a second copy of the booked withdrawal. The integer signs 3^12>2^19 and2209^8<2*2040^8 imply <21/32 from the same final2 owner. A085's larger remaining amount concerns child quotient payment only and excludes the earlier source/outcome bill; it is not inconsistent with A047's full source-inclusive remainder43/32. The new proof here extends the admitted core and reference existence argument; it does not modify the accepted A047 source.

The earlier arbitrary-reference obstruction is retained: for a parity-one-flip selector with mu=2^(1-r), a=mu^2 and erased reference tilt alpha=1-a^2, mean inherited conditional KL=(1-2a)log2((1-a)/a)/2 grows like r-1 while removed selector influence tends to1/2. A full-support reference and actual Booleanity alone do not give an influence price. Our prescribed canonical reference plus marginal-gap/unused-surplus condition changes the hypothesis.

FIRST UNSUPPORTED UNIVERSAL LINE: for arbitrary supplied cores and mixed histories, prove enough genuinely unused terminal surplus to pay the actual canonical CE gap and any fresh-reference reset after earlier booked debts. No such certificate is proved here. The marginal gap itself grows on elementary cores, so (5) cannot be asserted universally. C018 and full FEI receive no universal constant improvement.
