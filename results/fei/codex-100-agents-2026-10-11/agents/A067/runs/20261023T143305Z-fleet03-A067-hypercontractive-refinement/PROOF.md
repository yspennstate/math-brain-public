# Original source payment for overlapping quadratic edits and every descendant tree

All entropies and CE/KL quantities are in bits. Fix m>=2, n=2m, and ANY
pure quadratic polynomial q(x)=sum_(i<j) M_ij x_i x_j over F2 whose
alternating polar matrix has full rank n. Put b=(-1)^q, A=2^-m, d=A^2,
delta=d/2. Adjoin a dummy w, set c=b-2*1{Y=0,w=0}, and take the original
G with actual z terminals b,c. Choose rate4 ONCE at this original source.
The z split is fixed first; below it EVERY finite adaptive physical stopping
tree is allowed. References are only marginals of the original b and c
spectra. No reference reset or bank renewal occurs.

## 1. Actual noncanonical source allowance

The quadratic rank calculation in A067 stage20 gives |bhat(S)|=A at every
Y label. Write bhat=A sigma. Since b(0)=1, sum sigma=1/A; thus sign counts
are (4^m +/-2^m)/2, regardless of overlapping interactions. Every b coordinate
has influence1/2; b(0) and every marked neighbor equal+1. The dummy is also
+1 along its marked edge. Therefore I(b)=m and I(c)=m+(4m+2)delta.
The actual source I_X=(I(b)+I(c))/2=m+(2m+1)delta.

The four (w,z) Fourier cells of G have coefficients A sigma-delta on00,
and magnitude delta on each of the other three cells. These are exactly
the histogram and physical energies of the independently checked canonical
source. Thus its actual old z entropy debit D and S2 satisfy
r=S2-D=2I_X-H(G)>delta/4=d/8 by the stage17 scalar certificate. This
extends the allowance by proof of equal histograms and physical energies,
not by reusing capital belonging to a different function. At the ORIGINAL
rate4, S4=S2+2I_X and r4=r+2I_X>2m. Old D is unchanged.

## 2. A conditional floor from the original spectrum, before AND after w

At the actual c terminal the original full law Q satisfies

 Q(W0,S)=d(sigma-A)^2 in [d(1-A)^2,d(1+A)^2],
 Q(W1,S)=d^2.

After summing any t queried data Fourier bits, every W0 entry lies between
2^t d(1-A)^2 and2^t d(1+A)^2; W1 entries are exactly2^t d^2. Summing w
adds the same positive quantity to both bounds, which only improves their
ratio. Thus, for ANY next data bit, before or after w, at every full label,

 Q_marg/Q <= rho(A)=1+((1+A)/(1-A))^2 <=34/9<4.

This is a bound for the ACTUAL inherited original law, without a phase
matching or a conditional equality hypothesis. Averaging against the actual
parent spectrum gives complete two-child CE drop L<2. Physical influences
are nonnegative, so its rate4 debit e_Q=L-4Inf<2. No false claim that every
data debit is nonpositive is made; isolated edited coordinates can cost.

There is only ONE surviving edited path: it fixes each queried coordinate
to0. Each1 outcome removes the defect and yields a genuine quadratic phase
with possibly affine terms. Its active original G reaches at query depth t
are2^(-t-1). Therefore the sum of ALL data-query signed debits, at ANY
stopped prefix and in ANY adaptive order, is strictly less than2, since
sum_(t>=0)2^(-t-1)=1. The choices use preceding outcomes only.

## 3. Pay w in any position once

Suppose t data bits have been fixed to0 and w is now queried. Let s=2^t d.
The actual W1 spectral mass of the edited restriction is s; the W0 mass is
1-s. Each inherited W0 coefficient is at least2^t d(1-A)^2 and W1 is2^t d^2.
For W0 labels, log2(Q_marg/Q)<=d/((1-A)^2 ln2)<(8/3)d.
For W1 labels the ratio is at most1+(1+A)^2/d<2/d, so its logarithm is
less than2m+1. The actual physical w influence is s: the unedited seed is
dummy in w and only the data-origin edge is toggled. With ORIGINAL reach
2^(-t-1), its rate4 signed source charge is therefore

 E_w < (4/3)d+(2m+1)d/2-4d/2=d(m-1/6)<=11/96.

The last scalar bound decreases from m=2. This retains both physical w
children, including the clean exit. If w is never queried, its charge is0.
Together with section2, the COMPLETE cumulative source debit obeys
E_Q<2+11/96=203/96 at every edited-path frontier.

## 4. Entire terminal KL bill and the complete tree

After h physical queries on the edited zero path, the reference at each
leaf is the average spectrum of ALL restrictions on its queried coordinates.
The actual leaf is one of those restrictions. The physical square-sum identity
therefore gives P_leaf<=2^j Q_leaf at depth j, hence KL_leaf<=j.
The one exits have original reaches2^(-j-1), j=1..h; the surviving edited
leaf has reach2^(-h-1). The unchanged b terminal has KL0. Therefore

 K_frontier <=sum_(j=1..h) j*2^(-j-1)+h*2^(-h-1)
            =1-2^-h<1.

Since the original terminal references were their actual spectra, the full
actual rate4 debit E_H=E_Q+K_frontier<299/96. Its named ORIGINAL remaining
account after old D is r4-E_H>2m-299/96>=85/96>0.

Now attach ANY finite adaptive continuation to EVERY clean exit and to
the original b sibling. Every such leaf is a quadratic Boolean phase.
Its entropy equals its polar rank. A nonisolated physical query has influence
1/2 and rank drop0 or2; an isolated query is a character or dummy. Thus at
rate4 its COMPLETE actual entropy debit is nonpositive at every node.
All these arbitrary clean forests can only reduce the total actual invoice.
Every finite stopping tree below the fixed z split decomposes in this way:
one edited zero path, all clean off-path subtrees. Thus the same85/96
remaining lower bound applies to EVERY such tree.

The KL<1 bound above is ONLY for the initial zero-path frontier. It is NOT
carried through clean refinements. For each continued clean leaf L the exact
increment is E_H(L)=E_Q(L)+K_after(L)-K_before(L), with both full children.
The new full KL may grow with m. All signed banks and old invoices remain.
At every final frontier, S_final,H-(D+E_H,total)=r4 exactly. Legacy rate2
invoices are explicitly E_2=E_4+2J_total, where J_total is the actual
root-weighted removed influence; no old bound on J is extended silently.

## 5. Exact scope and first unsupported universal line

This is a new original-source supplier and continuation theorem for EVERY
full-rank pure quadratic phase, including overlapping graphs, not just a
matching. It uses one rate4 chosen before the history. It does not preserve
the previous canonical rate3 price, and does not claim an optimal constant.
The marked first jet is essential: adding linear terms can preserve bentness
but reverse an incident edge, changing the source influence increment.

The first unproved line for general FEI is an original-spectrum conditional
floor and an affordable clean-branch supplier once the seed is non-bent,
has higher F2 degree, or has multiple marked edits. The present floor can
fail under cancellations in those regimes. Full FEI remains OPEN; no
universal supplier is inferred from this one-point quadratic closure.
