# Linear surgery radius for a genuine critical witness

All cubes uniform; signs Boolean; Fourier transform normalized; entropy in bits. Let n>=3, p=2^-n, and let F have Fourier support of minimum Hamming distance at least three. Suppose G differs from F on exactly R distinct physical vertices, with R>=1. For every relevant original coordinate i,

    L_i(G) < (37/4) R Inf_i(G),                    (1)

where L_i=H(G)-[H(G|i=0)+H(G|i=1)]/2. At K=10R the actual expected complete-child deficit gain is therefore greater than (3/2)Rp. There is no parity, factorization, connectedness or sign-pattern assumption on the edit set.

Consequently any least-essential-dimension positive fixed-K Boolean witness, K>=0, on n>=3 must have

    R > 4K/37                                    (2)

from EVERY distance-three Fourier-support seed on its n coordinates. Distance zero is also excluded. This improves the preceding quadratic threshold to a linear threshold; the earlier sharper single-edit two-query rate9 is unchanged.

## 1. Exact common row bounds

Write e=G-F. Parseval gives sum ehat^2=4Rp and |ehat(S)|<=2Rp. If the seed support size is s, disjoint radius-one Hamming balls give s(n+1)<=1/p.

Fix i. Every signed Fourier pair (a,b) of G contains at most one seed coefficient. On an occupied row orient a at that seed label and call b the off-anchor coefficient. Define beta=sum_occupied b^2. Empty rows have total mass M<=4Rp and beta<=4sR^2p^2.

The exact loss is B+J, where B is spectral conditional binary entropy and J is the Jensen-Shannon divergence of the two actual squared child spectra. Rowwise,

    0<=J_row<=2min(a^2,b^2)/ln2.

For clarity, if z=2ab/(a^2+b^2), the natural-log row expression is q psi(z), psi=[(1+z)ln(1+z)+(1-z)ln(1-z)]/2. Compare derivatives atanh z<=z/sqrt(1-z^2), then integrate to get psi(z)<=1-sqrt(1-z^2); multiply by q. This proves the displayed curvature bound for all real signed rows, with endpoints by continuity.

Empty rows cost at most M(1+1/ln2)<10Rp. Occupied rows cost at most beta log2(1/beta)+3beta/ln2: the anchor term is <=beta/ln2, and log-sum bounds the other entropy terms by beta log2(1/beta). Every nonzero Boolean coefficient has magnitude at least2p, so beta=0 or beta>=4p^2. Since ln2>2/3,

    L_i <10Rp+(2n+5/2)beta,                       (3)
    L_i <[10R+(8+2/(n+1))R^2]p.                  (4)

If beta=0 use the empty-row bound directly. These are the preceding stage's row estimates, rederived here; no independent-row assumption occurs. The same spectral decomposition also gives for ANY n-bit Boolean G with I=Inf_i(G)>0,

    L_i <= h2(I)+(2/ln2)I
        <= I[log2(1/I)+3/ln2]
        < I(n+7/2).                              (5)

The first inequality uses B<=h2(I), J<=2I/ln2; the last uses I>=2p. In particular (5) does not require G to be near F.

## 2. The seed does not depend on the queried coordinate

Suppose Inf_i(F)=0 and put I=Inf_i(G)>0. Pair physical vertices x,x+i. Then F is equal on each pair. In ehat(S+i), for S not containing i, two edited endpoints of a pair cancel. Each pair with exactly one edited endpoint contributes magnitude at most2p. Let U be the number of such pairs. They are exactly the sign-crossing edges of G in direction i. Thus

    |ehat(S+i)|<=2pU=I,   I<=2Rp.

Every occupied seed label excludes i. Therefore beta<=s I^2. Dividing (3) by I, using I>=2p, and then s I<=2R/(n+1), gives

    L_i/I <5R+(2n+5/2)s I
           <=5R+(4+1/(n+1))R
           <=(37/4)R.

This edge cancellation is the new ingredient missing from the quadratic estimate. It retains the actual influence even when only one crossing edge survives. If I=0 no ratio or payment claim is made.

## 3. The seed depends on the queried coordinate

Let s_i count seed Fourier labels containing i. The physical half-derivative D_iF=(F(x)-F(x+i))/2 takes values0,+1,-1 and has squared norm Inf_i(F). At any point where its magnitude is1, Fourier Cauchy-Schwarz gives

    1 <= sqrt(s_i Inf_i(F)).

Hence Inf_i(F)>=1/s_i>=1/s>=(n+1)p. Changing R vertices changes any directional influence by at most2Rp.

If n+1>=4R, then

    I=Inf_i(G)>=(n+1-2R)p>=(n+1)p/2.

Divide (4) by this lower bound:

    L_i/I <20R/(n+1)+[16+4/(n+1)]R^2/(n+1)
           <=5+4R+R/(n+1)
           <=4R+21/4
           <=(37/4)R.

The last step uses R>=1. If n+1<4R instead, use the universal bound (5):

    L_i/I < n+7/2 <4R+5/2 <=(13/2)R <(37/4)R.

These cases exhaust the seed-dependent branch. The Cauchy-Schwarz lower bound is NOT asserted when the seed is independent of i; that branch was separately proved above.

## 4. SAME bank and critical consequence

For D_K=H-KI the exact original-coordinate identity is

    E D_K(actual child)-D_K(G)=K Inf_i(G)-L_i.

Both complete children stay at original reach1/2. Thus (1) gives a positive gain at K>=37R/4 and a gain>(3/4)R Inf_i>=(3/2)Rp at K=10R.

A least-essential-dimension positive K-witness has all coordinates relevant and every proper Boolean child nonpositive in deficit. Its complete bank would require L_i-K Inf_i=D_K(G)+E[-D_K(child)]>0. This contradicts (1) if K>=37R/4, proving (2). At R0, singleton Fourier pairs have at most one occupied coefficient, so B=J=L_i=0 and the same contradiction applies.

This is root-local. After a restriction the inherited seed may lose distance-three packing; the theorem does not grant a new reference, erase old debit, or license another paid query without its hypotheses. The previous third-query collision obstruction is unaffected.

## First unsupported universal line

Criticality is not known to force either a uniformly bounded edit distance to a distance-three seed or sufficient unused quotient-rank release on the complementary far-from-code class. The new lower bound R>4K/37 strengthens that precise structural separation, but does not select and pay a universal original proper block. Full FEI remains OPEN.
