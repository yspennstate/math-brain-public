# Projection histories and the actual forward interface fee

All logarithms are base2. A distribution is a finite normalized probability law. Every KL expression below is finite unless explicitly noted. Full FEI remains OPEN.

## 1. What the supplied projection-history theorem says

A012 stage22 uses two precise operations. A physical query passes BOTH children the spectral projection Q'=pi_i Q. A reference update replaces a cell profile q by (1-t)q+t p for 0<=t<=1, retaining old within-cell reference conditionals. The fee is D(R||Q), in that direction. Neither operation is A011's normalized true-kernel inheritance in general.

For the projection, the average true child law is P'=pi_i P. Write L=D(P||Q)-D(P'||Q') and J=average D(P_child||P'). The relative-entropy chain rule gives L>=0. Expanding the two child likelihoods gives

 average D_child-D_parent=J-L.

For a profile update put G=D(R||Q)+D(P||R)-D(P||Q). At 0<t<1, exact cancellation of old conditionals gives

 G=-((1-t)/t)[D(r||q)+D(q||r)]<=0,
 r=(1-t)q+t p.

At t=0 the reference is unchanged; at t=1 the new profile is true and G=0. The true support is covered; zero true/reference cells can be omitted only together. Full ghost mass remains in q and r. These are the stated finite-support hypotheses.

For an arbitrary finite adaptive tree with physical reaches w, retained terminal CE, fixed old bill b, and the A012 bill convention (entropy decrements plus projection contractions plus full conversion fees), the exact identity is

 Bill=b+CE_root+sum_queries w J+sum_updates w G.       (1)

This is a finite telescoping identity, so no stopping-limit interchange is needed. A012's two-point inequality J<=(2/ln2)Inf_i then gives its scoped bound. More precisely the influence paid is the retired influence I(root)-E I(terminal). No new constant improvement is claimed; this is a reconstruction of the source's potential argument. Its two-point proof handles arbitrary real coefficient signs by first taking absolute values, and the scalar j''<=4 argument supplies the boundary limits. Initial CE<=C0 I remains an additional premise.

## 2. The general price of an unlisted update

For ANY covering replacement R with finite D(R||Q), the same definition of G and exact identity (1) apply, but G need not be nonpositive. Direct expansion gives

 G=sum_s (R(s)-P(s))log2(R(s)/Q(s)).                  (2)

Terms with R=P=0 are zero. If Q=P, then

 G=D(R||P)+D(P||R),

which is strictly positive whenever R differs from P (on the common finite support). Thus an update away from a matched current reference cannot be included as a free paid-profile update. Both divergence orientations matter. For any affine moment class satisfied by P, a matched Q=P is itself the unique minimum of D(v||Q); an affine information projection cannot produce a different R at zero cost either.

This observation is classical relative-entropy algebra, not a new information inequality. The following actual Boolean witness instantiates it in the two campaign interfaces with an explicitly influence-priced original reference.

## 3. Actual AND3 and both complete physical children

Let f be -1 at one input of the three-cube and +1 elsewhere. Translating inputs and complementing f do not change the following squared laws. Its parent spectrum is

 P=(9/16,1/16,1/16,1/16,1/16,1/16,1/16,1/16).

Each physical influence is1/4, so I=3/4. Supply the complete original reference Q=Uniform(8), with CE(P,Q)=3=4I. Query any coordinate. On the exterior four labels,

 m=pi_i P=(5/8,1/8,1/8,1/8),
 q=pi_i Q=(1/4,1/4,1/4,1/4).

One actual child is constant, P_c=delta_empty. The other is an AND2-sign function, P_a=Uniform(4)=q. Both physical outcomes have reach1/2.

A011's normalized true-kernel reference at child b is

 R_b(T)=[q(T) P_b(T)/m(T)]/Z_b,
 Z_b=sum_T q(T)P_b(T)/m(T).

All m(T)>0 here; no ghost convention is hidden. Exact values are

 Z_c=2/5, R_c=delta_empty;
 Z_a=8/5, R_a=(1/16,5/16,5/16,5/16).

The normalizers have mean1. Every target atom is covered. The forward conversion D(R_b||q) is finite on BOTH children, including the constant child. This differs from the reverse-infinite AND2 support guard already recorded by A012/A013.

At the constant child, D(R_c||q)=D(P_c||q)=2 and D(P_c||R_c)=0, hence G_c=0. At the nonconstant child q=P_a, so

 G_a=D(R_a||P_a)+D(P_a||R_a)
    =(3/16)log2(5)>0.

For an explicit check, D(P_a||R_a)=2-(3/4)log2(5), and D(R_a||P_a)=(15/16)log2(5)-2. Each is nonnegative, but their sum is the simpler exact expression. Therefore the full all-outcome handoff deficit is

 Gbar=(G_c+G_a)/2=(3/32)log2(5)>0.                   (3)

A conservative exact upper bound is Gbar<15/64 because 5^2<2^5. No numerical logarithm sign is used. Reaches sum to1; there is no multiplication by the number of leaves.

The complete one-query bill followed by this handoff satisfies

 Bill=b+CE_root+J_root+(3/32)log2(5),

by (1). The positive last term is an additional owner obligation. It is not a contradiction to A012: that theorem does not permit this update. It is not a contradiction to A011: that theorem uses true-kernel inheritance directly and a different exact ledger. Nor does (3) show that a sufficiently large original bank cannot pay; actual unused capacity or other separately retained slack could do so. The example has H/I bounded and is not an FEI counterfamily.

## 4. Independent checks and scope

code/check.py computes truth tables and Walsh spectra directly for every input translation and output sign of this AND3 function (16 actual labelled tables), each of3 physical queries, and BOTH children:48 queries/96 children. No symmetry representatives are silently substituted. Fraction arithmetic and formal prime-log sums verify exact fee orientation, normalizers, KL/CE identities and (3). Additional partial-profile fixtures include t=0,1/4,1/2,3/4,1 and a true-zero ghost atom. PASS5723 exact assertions. Generic identities are proved above; finite checks are not extrapolated to arbitrary functions.

The key algebra is not Lean-checked: fresh memok exited1 (physical free2.2GB<4GB;commit free2.1GB<8GB), so no compiler was started. This is a formal-verification hold, not mathematical evidence. Source identities are independently reconstructed, while the new Boolean interface guard awaits A012/A011/A094 review.

## 5. First unsupported universal line

A useful hereditary policy for arbitrary Boolean cores still needs an ORIGINAL complete source CE<=C0 I or a required interface handoff paid from actual unused original margin, retaining prior charges and both full terminals. A supplied source plus stable projection histories does not establish the initial price. If true-kernel conversion is required, its actual G in (2), rather than an oppositely directed KL or an unproved profile label, must enter that SAME owner ledger. The witness makes one previously qualitative interface restriction an exact finite invoice; it gives no universal constant improvement.
