# Sparse partial matchings: a growing finite erasure witness is not a disproof

This independently reconstructs the live A075 DERIVATION.md spectrum and adds uniform asymptotics. Inputs are binary physical coordinates with uniform measure, characters chi_S=(-1)^(sum_(i in S)x_i), and Boolean outputs are signs. All entropies use bits. Let k>=0, l>=0, r=2k+l, N=2^r and a=1+3k+l. Let A consist of zero, all r unit vectors, and the k two-unit vectors corresponding to a fixed matching. Set f_(k,l)=1-2 1_A. The full matching k=3,l=0 is B15's six-bit witness, up to a coordinate permutation.

## Exact spectra and physical influence

An occupied Fourier intersection with a matched pair contributes -4 relative to its empty intersection, and selecting an isolated Fourier coordinate contributes -2. Thus the indicator Fourier numerator is L_(u,v)=a-4u-2v, with multiplicity C(k,u)3^u C(l,v). For every nonempty S, fhat(S)=-2L_(u,v)/N; the single fully empty coefficient is 1-2a/N. It must replace the formal -2a/N value, not be added to it. Parseval follows either from the actual Boolean definition or indicator character orthogonality.

In A, a paired physical coordinate has two internal edges, and an isolated coordinate has one. Consequently

Inf_paired=2(a-4)/N, Inf_isolated=2(a-2)/N,
I=2[2k(a-4)+l(a-2)]/N.

All coordinates of the same type have equal erasure. Coordinate permutations preserve these identities. Cases a-c=0 are irrelevant coordinates and are omitted from ratios.

## Exact paired spectral rows

For a paired coordinate let z=a-3-4u-2v on the other k-1 pairs and l isolated coordinates, of multiplicity C(k-1,u)3^u C(l,v). If its partner is absent from S, the two indicator numerators are z+3 and z-1. If its partner is present they are both z-1. For an isolated coordinate the two numerators are z+1,z-1, where z=a-1-4u-2v on k pairs and l-1 isolated coordinates. In either case only the all-empty residual row has a parent constant coefficient. Replace its first squared coefficient by (1-2a/N)²; its second squared coefficient is b=4(a-c)²/N², with c=4 for paired and c=2 for isolated coordinates.

Writing Phi(x,y)=(x+y)log2(x+y)-x log2 x-y log2 y, homogeneity Phi(tx,ty)=t Phi(x,y) gives exact O(r²)-row formulas for each B_i. These rows are actual Fourier rows of the Boolean function, with no sign-realizability assumption left unpaid.

## Uniform erasure asymptotics: every relevant ratio tends to 2

Let V=4a/N(1-a/N), the nonempty spectral mass. In all regular rows, B_i=sum q minus an entropy deficit. For arbitrary real row numerators s,t,

(s²+t²)-Phi(s²,t²) <= (|s|-|t|)²/ln2.

To prove this, set z=(s²-t²)/(s²+t²) and apply the derivative inequality d(z)<=1-sqrt(1-z²) from REVIEW_LEAD.md. The right side is exactly the squared difference of magnitudes divided by ln2.

For paired coordinates the difference is at most 4 in the partner-absent sector, and zero in the partner-present sector. There are N/4 partner-absent residual rows. After scaling by 4/N², their total deficit is at most 16/(N ln2). For isolated coordinates the difference is at most 2 on N/2 rows, so the deficit is at most 8/(N ln2). Removing the exceptional empty row can only reduce these upper bounds.

The total regular row mass is V-b. The exceptional contribution lies in [0,b log2(e/b)], using q h2(b/q)<=b log2(e q/b) and q<=1. Because a-c>=1 for a relevant coordinate, log2(e/b)<=2r+log2 e. Therefore, with C=16 (paired) or 8 (isolated),

V-b-C/(N ln2) <= B_i <= V-b+b(2r+log2 e).

Divide by Inf_i=2(a-c)/N. The center V/Inf_i=2a(1-a/N)/(a-c) tends uniformly to 2 as r grows, because r+1<=a<=1+3r/2 and c is 2 or 4. The lower error is O(1/r)+O(r/2^r); the upper error is O(r²/2^r). In particular, simultaneously for all k,l with 2k+l=r, every relevant B_i/Inf_i tends to 2. This proves E(f)=min_i B_i/Inf_i ->2 and B(f)/I(f)->2 uniformly, rather than extrapolating a finite six-bit record.

Completely explicit coarse brackets for r>=4 are

2 - 12/(r-3) - [2(1+3r/2)²/(r-3)+2(1+3r/2)]/2^r
 <= B_i/Inf_i
 <= 2 + 8/(r-3) + 2(1+3r/2)(2r+3/2)/2^r.

Here ln2>=2/3 (the first positive atanh term at z=1/3), so log2 e<=3/2. These proved errors are deliberately coarse but dimension-uniform. For r>=64 the upper bracket is below 11/5: the checker verifies the strict rational comparison at r=64. Both error terms decrease thereafter. Indeed, for P(r)=2(1+3r/2)(2r+3/2), each affine factor has positive intercept, so P(r+1)/P(r)<=((r+1)/r)^2<2; hence P(r)/2^r decreases, as does 8/(r-3). Thus every partial matching in dimension at least 64 has every coordinate ratio <11/5. This destroys the proposed increasing-erasure mechanism while leaving the finite B15 obstruction intact.

## Actual FEI ratio: uniform limit 4, bounded in all dimensions

For every nonempty coefficient |fhat(S)|<=2a/N. Hence

H(f)>=V(2r-2log2 a-2).

Conditioning on the nonempty spectrum gives H(f)<=h2(V)+V log2(N-1)<=V[r+log2(e/V)]. From the exact influence formula,

2r(a-4)/N <= I <=2ra/N.

For r>=4, a/N<=7/16, a>=5, and 4a(1-a/N)>e (e<3 suffices). Consequently the entropy upper bracket r+log2(e/V) is at most 2r. Therefore

4(1-a/N)[1-(log2 a+1)/r] <= H/I <=4a/(a-4)<=4+16/(r-3).

When the lower bracket is negative, its assertion follows from H/I>=0; when it is nonnegative, divide the entropy lower bound by the influence upper bound. Both bounds tend uniformly to 4 as r grows through arbitrary partial matchings. For r>=4 the upper bound is at most 20. For r<=3, H<=r and every nonconstant Boolean has I>=2^(1-r) by at least one boundary edge, so H/I<=12. Thus the whole family has H/I<=20, and supplies no FEI disproof.

This limit is not a new universal FEI constant. It is a rigorous no-growth verdict on the natural scalable extension of a certified finite counterexample to a small selection constant. Tensor powers do not repair it: they preserve H/I and take the minimum of factor-wise selectable erasure ratios. For the standard independent activation construction, the earlier A080 FEI_DISPROOF_STANDARD.md records the required control influence and rules out amplification of bounded H/I by that construction; no general recentering operation is excluded here.

## Physical descendants and the remaining frontier

A075's restriction observation also reconstructs directly: fixing zero coordinates breaks matching pairs into isolated coordinates and retains the same partial-matching family. A history with exactly one fixed one leaves a point defect, with its partner possibly a dummy; exactly two fixed ones leaves a point defect only if they form a matching pair, otherwise a constant; three or more fixed ones leaves a constant. Thus no newly admitted complex Boolean descendant has been hidden by the root analysis. Point-defect terminal costs are already established and are not re-proved as a new class result here.

The next unsupported mechanism is a restriction/recentered or composition operation that changes the actual paired profile and keeps a ratio gain at every new relevant coordinate, with a complete entropy/influence ledger. Neither the fixed seed ratio nor the partial-matching asymptotics supply that operation. This is the source-bound handoff to A075/A074/A089, adjacent to C018 and C019.
