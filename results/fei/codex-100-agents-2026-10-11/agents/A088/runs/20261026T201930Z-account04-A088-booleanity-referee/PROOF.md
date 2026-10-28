# Two edited points: an original source and every physical tree

All logarithms are base2. This is an author proof awaiting independent review.

Let m>=4, n=2m, d=4^-m. Let b=(-1)^q for ANY quadratic F2 polynomial, including arbitrary affine terms, with full alternating rank n. Pick ANY two distinct data inputs a,beta. Adjoin dummy w. The Boolean c equals b except at (a,0),(beta,0), where its signs are reversed. Let G have z children b,c. Fix rate4 at this original source. Every reference is a marginal of the ORIGINAL squared spectrum of its z child. All outcomes, full terminal KL, old z debit D and actual influence removal remain.

Define I_X=(I(b)+I(c))/2, D=H(G)-(H(b)+H(c))/2, S4=4I_X-(H(b)+H(c))/2, r4=S4-D=4I_X-H(G). For any physical forest below z let E_H be the sum of original-reach entropy-drop-minus4-influence invoices. The same original remaining reserve is r4-E_H. No renewal occurs.

## Quadratic Fourier facts used below

For a quadratic F2 phase, its autocorrelation at shift h is zero unless h belongs to the kernel of its alternating polar matrix M; on that kernel it is a character. Fourier inversion therefore makes the squared spectrum uniform on a coset of (ker M)^perp, with entropy rank(M). In full rank the autocorrelation is supported only at0, so every squared Fourier coefficient is2^-n=d. A nonzero polar row gives a nonconstant affine Boolean derivative and physical influence1/2. A zero row gives a character or dummy and influence1 or0. Removing one physical coordinate changes alternating rank by0 or2 (principal deletion changes rank by at most2, and alternating ranks are even); both physical children have that same remaining polar matrix. These facts prove the root and clean-node calculations without using an unreviewed supplier.

## 1. Original source bound

Full rank gives |bhat|=A=2^-m, H(b)=2m, I(b)=m. Arbitrary linear and constant terms do not change these facts. No marked first-jet condition is used in this new source estimate. On the (n+1)-cube each point-edge weight is 2^-n=d. Flipping two points changes each data influence by at most2d, hence certainly at most4d. We use the weaker4d bound to keep the source estimate simple. Thus I(c)>=m-8md+2d, since its physical w influence is exactly2d. Hence I_X>=m-4md+d. The actual G is Boolean on n+2 bits, so H(G)<=2m+2. Therefore r4>=2m-16md+4d-2. This bound is from the ACTUAL original source and requires no prior scalar reserve.

## 2. Original spectral floor with real cancellations retained

Put s_a=b(a), s_beta=b(beta). With chi_S(x)=(-1)^(S dot x), T(S)=d(s_a chi_S(a)+s_beta chi_S(beta)). The two w sectors of the original c law are Q(0,S)=(bhat(S)-T(S))^2 and Q(1,S)=T(S)^2. Since |T|<=2d,

 d(1-2A)^2<=Q(0,S)<=d(1+2A)^2.

Q(1,S) is exactly4d^2 on a parity hyperplane, and zero on its complement. After marginalizing t data labels it is either uniform2^(t+1)d^2 or a parity-half-support law with positive entries2^(t+2)d^2. Thus at EVERY occupied W1 entry, a next-data erasure has Q_marg/Q<=2, including the first erased bit of the parity equation. This is where cancellations are handled; zero entries are not replaced by a positive floor.

At W0, the conditional ratio is at most1+((1+2A)/(1-2A))^2. After erasing w, it is at most1+((1+2A)^2+4d)/(1-2A)^2. For A<=1/16 both are <=131/49<4. Therefore every edited data query has complete original-reference CE drop <2; subtracting4Inf only lowers it. Support inheritance follows from the physical square-sum identity, so zero Q entries never carry positive actual spectral mass.

There are at most TWO edited nodes at each physical depth. Including the original c reach1/2, their total reaches over ALL depths are bounded by

 (1/2)+(1/2)+sum_{j>=2}2^-j=3/2.

Consequently the total data CE debit is <3. This allows both edited paths and arbitrary adaptive orders, rather than following just the origin.

## 3. Every possible w query

At a node reached after t data restrictions, the occupied W1 reference entries are at least2^(t+1)d^2. W0 reference entries are between2^t d(1-2A)^2 and2^t d(1+2A)^2. At W0,

 log2(Q_marg/Q)<=4d/((1-2A)^2 ln2)<8d,

using ln2>2/3. At occupied W1, Q_marg/Q<=1+(1+2A)^2/(2d)<1/d, so its logarithm is <2m. If k in {1,2} marked points survive at that node, its ACTUAL W1 spectral mass and w influence are both k*2^t*d. Summing their original weights over all w-query nodes is <=d: each of the two original marked points is counted at most once, with original z reach1/2. The w-query nodes form an antichain, so their total reach<=1 (indeed<=1/2). Thus the combined w debit is <8d+(2m-4)d=(2m+4)d. This argument includes trees in which w is never queried.

## 4. Both full terminal bills and arbitrary clean refinements

First prune the tree when a branch has no surviving edited point. Every pruned clean leaf is a restriction of a quadratic phase, with possible affine terms. Each inherited Q_leaf is the average of spectra over ALL restrictions of its particular queried coordinate set. Hence P_leaf<=2^j Q_leaf at depth j and KL_leaf<=j. The complete terminal KL, with original reaches, is bounded by the expected pruned depth, which equals the sum of original reaches of its queried edited nodes, <=3/2. The original b sibling has KL0 at this cut. Therefore E_H=E_Q+K_terminal<9/2+(2m+4)d.

For every clean quadratic query, entropy equals polar rank; a nonzero row has influence1/2 and rank drop0 or2, so the rate4 actual entropy debit is <=0. A zero row is a character or dummy and also costs<=0. Attach ANY finite adaptive clean forests. They cannot increase E_H. Their full KL may grow; the3/2 KL cap is NOT reused after continuation.

The SAME original remaining reserve consequently satisfies

 r4-E_H>2m-13/2-18m*4^-m>=39/32>0.

The last expression increases for integers m>=4 (m/4^m decreases). Every terminal, the old D, and the actual removed influence J are included. Legacy E2=E4+2J holds, but the rate was explicitly chosen as4 initially. This is an all-dimensional TWO-edit closure, not full FEI.

## 5. Booleanity referee and scope

The floor/CE inequalities alone are finite probability algebra. The two-point Boolean edit supplies exact edge bounds, equal child norms, the one-parity W1 cancellation pattern, and clean QUADRATIC exits. The nonpositive clean debit uses discrete F2 polar rank and derivative influences, not only normalization. It fails for complex unimodular phases: values [1,(399+40i)/401] have unit modulus, normalized children at every restriction, spectral law [400/401,1/401], and influence1/401. Their complete rate4 entropy debit is h2(1/401)-4/401>0 because401>16. This counterexample is a child of the two-variable complex phase [1,1,u,-u], u=(399+40i)/401 (x is the low bit). That parent has EXACTLY uniform squared Fourier spectrum1/4, both root coordinate energies1/2, and unit norms at every physical restriction. Fixing x=0 yields [1,u]. Thus even a flat bent root and all conditional norm identities cannot replace discrete binary phase in the clean-node argument. This refutes the relaxed claim that every clean-node debit remains nonpositive, not the full Boolean source theorem or its total original reserve. Arbitrary real normalized flat-spectrum fields also fail branch normalization. These are scope diagnostics, not Boolean FEI counterexamples.

## 6. Independent audit of A067 one-edit source

A067-OVERLAPPING-QUADRATIC-ORIGINAL-RATE4-ALL-TREES@1 is reconstructed unchanged. Its single-origin pure-quadratic marked jet supplies I_X=m+(2m+1)d/2 and its inherited scalar root allowance. Its W1 law is uniform, its W0 floor gives ratio<=34/9, and its unique edited path has total original reach<1. Its E_Q<203/96 and pre-clean KL<1 therefore give E_H<299/96. Clean rate4 debits are nonpositive as above. Its SAME reserve>85/96 HOLDS at its stated scope; the new result does not repair that proof. A088 authored an ancestor scalar source, so this is independent reconstruction of the NEW overlapping-source/continuation reasoning, not a conflict-free second audit of that ancestor.

## 7. First unsupported universal line

For a growing number k of marked points, W1 is the squared Fourier transform of a general signed sparse set, rather than a single parity hyperplane. Fixed-k cancellations may still be controlled by signed orthogonality and integer coefficient gaps; three edits are not asserted to obstruct the method. What remains unpaid is a uniform influence-priced full-reference supplier when k grows, including the occupation of all edited branches. Nonflat or higher-degree seeds additionally lose the present clean quadratic admission. The shortest next test is a k-dependent conditional-ratio and edited-tree occupation bound, followed by payment from the SAME original reserve, with all branches and full terminals. The supplier must ultimately reach arbitrary cores, rather than repeatedly closing one fixed edit count.
