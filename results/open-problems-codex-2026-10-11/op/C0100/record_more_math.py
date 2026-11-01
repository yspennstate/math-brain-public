from pathlib import Path
p=Path('ATTEMPT.md')
p.write_text(p.read_text(encoding='utf8')+r'''
## 5. Quadratic limiting patches yield local frequencies (proved conditional application)

Conventions. Write Gamma_3 for attainable quadratic Hessians with discrete Laplacian at most 3, Gamma_2 for the bound 2 convention in Pegden–Smart 2020. Let E=diag(1,0). The integer polynomial q(x)=x_1(x_1+1)/2 has Delta q=1; hence Gamma_2=Gamma_3-E, and the isolated extremal classes Gamma_2^+ and Gamma_3^+ correspond by that translation. In this section, a maximal pattern means the pattern supplied for a matrix in Gamma^+, not an arbitrary matrix on the boundary of Gamma.

Claim. Let U be the locally uniform limit of u_n/n on R^2\{0}, with N=sqrt(n). Suppose P is an open subset of {U>0}\{0}, and U on P is a quadratic polynomial with Hessian A in Gamma_3^+. Then on every bounded Jordan set D with closure in P, the height frequencies of s_n converge to those of the canonical periodic pattern associated to A.

The external ingredients are Pegden–Smart 2013, Theorem 4.2 and the fundamental-solution normalization (locally uniform odometer convergence away from 0), and Pegden–Smart 2020, Proposition 8, Lemma 13 and Theorem 10 (pattern witnesses, approximation of arbitrary slopes, and pattern stability). Theorem 10's proof is local: its uses of recurrence are inside B_R, via Lemma 14. Thus it applies to a function recurrent in B_R, with values on its neighboring boundary. We justify that local recurrence for u_n below rather than assume that u_n is globally recurrent (it is not globally recurrent).

Local recurrence lemma. On any finite Y in a region where u_n>=1, excluding 0, if w is integer-valued and Delta w<=3 in Y, then

max_Y(u_n-w) <= max_{partial Y}(u_n-w),

where partial Y is the outer nearest-neighbor boundary. Proof: let c=max_{partial Y}(u_n-w). If M=max_Y(u_n-w)>c, integrality gives M-1>=c. Define z=u_n outside Y and z=min(u_n,w+M-1) in Y. Everywhere z>=u_n-1>=0 in Y, and outside z>=0. At a site where z=u_n, all neighbor values weakly decreased, so Delta z<=Delta u_n. At a lowered site, z=w+M-1; for neighbors inside Y one has z<=w+M-1 by construction, and for neighbors outside Y one has z=u_n<=w+c<=w+M-1. Thus Delta z<=Delta w<=3 there. No lowered site is the origin, so n delta_0+Delta z<=3 throughout the lattice. At the origin or any other unchanged site the inequality follows from Delta z<=Delta u_n. This z is a nonnegative integer stabilizing comparison function, smaller than u_n at a maximizer of u_n-w. This contradicts the least-action principle. The local maximum principle follows. Subtracting q transforms this recurrence inequality to the bound-2 convention.

Proof of the claim. Fix a ball C whose closure and a slightly larger concentric ball are compactly contained in P. At scale N choose a nearby lattice center x_N and a lattice ball of radius R_N=cN whose rescaled closure lies in that larger ball, with c>0 fixed. For large n all sites in this ball and its outer boundary have u_n>=1, since U has a positive minimum there. Define, in centered coordinates z,

v_n(z)=u_n(x_N+z)-q(z).

This is integer-valued, recurrent locally with Delta v_n<=2. Let

Q_n(z)=N^2 U((x_N+z)/N)-q(z).

Its Hessian is H=A-E in Gamma_2^+, and it is a quadratic polynomial whose affine part depends on n. Locally uniform convergence gives

sup_{|z|<=R_N+1}|v_n(z)-Q_n(z)|=o(N^2).

By Proposition 8 choose the canonical integer recurrent witness o with Hessian H, and a quadratic q_H with o-q_H bounded. Lemma 13 says that for any real slope b there is a translation tilde_o (allowing integer affine additions) with

|tilde_o(z)-o(z)-b dot z|<=C_H(1+|z|).

Apply this to the difference of the affine parts of Q_n and q_H, and add a nearest integer constant to tilde_o to fit the constant term. The resulting translation o_n satisfies

sup_{|z|<=R_N+1}|Q_n(z)-o_n(z)|<=C_H(1+R_N).

In particular a_n:=sup|v_n-o_n|=o(N^2). Set h_n=max(C_H,N^(1/4),sqrt(a_n)). Then h_n/N->0. For any fixed sufficiently large r (depending on H), the hypotheses h_n>=C, r>=C|V|, h_n r>=C|V|^3, and R_N>=C h_n r of Theorem 10 hold eventually. That theorem gives, at all but an O(r h_n/R_N)=o(1) fraction of centers in B_{R_N-r}, equality v_n=some translation of o_n throughout B_r at that center. Taking Laplacians loses at most one unit of radius, so s_n=Delta v_n+1 equals a translation of p_A:=Delta o+1 in B_{r-1}. This last '+1' is essential to match the original bound-3 heights. The fixed-width annulus between R_N-r and R_N has o(N^2) sites. Cover any smaller compact set by finitely many such balls; the bad centers remain o(N^2). Section 3 now gives the claimed frequencies on D.

Consequences and limits. No rate of convergence of the odometer is required here: h_n=o(N) suffices with r fixed. No global phase of the pattern is required. If the point-source limiting odometer admitted an almost-everywhere cover by such maximal quadratic patches (with a separately controlled exterior), section 4 would give the desired height-frequency conclusion. We have NOT proved that cover. In particular, almost-everywhere twice differentiability or a.e. membership in the boundary of Gamma does not by itself imply membership in the isolated subset Gamma^+, let alone an open quadratic patch. The source's Apollonian theorem is not a proof of that missing assertion.

## 6. Full one-dimensional special case (proved)

On Z with threshold 2, for k>=0 the stabilization of 2k+1 grains is height 1 on [-k,k] and 0 elsewhere; for k>=1 the stabilization of 2k grains is height 1 on [-k,k]\{0} and 0 elsewhere. Thus on any interval B of positive length under spatial scale n,

F_n(B,1) -> |B intersect [-1/2,1/2]|/|B|,
F_n(B,0) -> 1-|B intersect [-1/2,1/2]|/|B|,

and all other height fractions are zero.

Proof of the exact configurations by induction using legal topplings. Begin with n=1. From the even configuration 2k, adding one grain fills its empty origin and gives the stated odd configuration 2k+1 without toppling. From the odd configuration, add one grain at 0. Its height is now 2. Perform stages t=k,k-1,...,0, in each stage toppling 0, then 1,2,...,t, then -1,-2,...,-t (the side lists are empty when t=0). Before the first stage all sites 1<=|x|<=k have height 1 and the center has height 2. After the first center toppling each side sweep is legal: the next site has received one grain, going from 1 to 2; its toppling sends one grain forward and one backward. At the end of a stage t>=1 the center has received one grain from each side and has height 2; sites 1<=|x|<t have height 1, the two sites |x|=t have height 0, and the previous holes at |x|=t+1 (or the unoccupied exterior at the first stage) are filled with height 1. Thus the next stage t-1 satisfies the same conditions. In the final stage t=0 the center becomes 0 and fills the two holes at +/-1. The result is height 1 on [-k-1,k+1]\{0}. All moves were legal and the result stable, so Abelian uniqueness proves the formula for 2k+2. The induction is complete.

For completeness, with k=floor(n/2), the odometer in both cases is

u_n(x)=((k-|x|)(k-|x|+1))/2 for |x|<=k, and 0 otherwise.

The sweep counts prove this: passage from 2k+1 to 2k+2 adds k+1-|x| topplings for |x|<=k and none beyond; this is exactly the difference of the displayed formulas at k+1 and k. Passage from even to odd adds no topplings. The base k=0 is zero. Counting integer points in the interval intersection gives the frequency limits, with at most O(1) error from the origin and interval endpoints; floor(n/2)/n->1/2.

This settles d=1, not the intended planar question. It supplies an exact small/boundary case rather than a claim of planar resolution.

## 7. Frequencies on extreme-mean balls (proved special case in all dimensions)

Let H=2d-1. On a fixed ball B let the mean heights tend to mu_B, as supplied by weak-* convergence. Since heights are nonnegative integers, 1_{s_n!=0}<=s_n, so if mu_B=0 then F_n(B,0)->1 and every other frequency tends to 0. Likewise 1_{s_n!=H}<=H-s_n, so if mu_B=H then F_n(B,H)->1 and all other frequencies tend to 0. This uses neither geometry nor periodicity and applies to the actual point-source model. It says nothing about balls with intermediate mean.
''',encoding='utf8')
