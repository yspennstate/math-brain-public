# Retaining ancestor packing pays the second physical query

All cubes are uniform; all functions are Boolean signs; entropy uses bits. Let n>=3, p=2^(-n), let F have Fourier support of minimum Hamming distance at least 3 (a singleton has infinite distance), and let G differ from F at exactly one physical vertex v. Put s=|supp Fhat|. Choose a coordinate i of maximum influence in G. In each actual child G_b=G|_(x_i=b), choose a remaining coordinate j_b of maximum influence in that child. T is this depth-two physical tree and its four leaves have their actual probability 1/4. Neither j_b nor a leaf reference is identified across different branches.

Write Q=Inf_i(G)+(Inf_(j_0)(G_0)+Inf_(j_1)(G_1))/2. This is influence consumed, not a renewed child budget. Then

    H(G)-E_T H(G_leaf) < (71/2)p,
    Q >= 4p,
    H(G)-E_T H(G_leaf)-9Q < -p/2.                 (1)

Consequently, for every real K>=9 and D_K(h)=H(h)-K I(h),

    D_K(G)-E_T D_K(G_leaf) < -p/2,
    E_T D_K(G_leaf) > D_K(G)+p/2.                (2)

These are paid-tree and actual-terminal statements. They do not prove FEI(9) for this neighborhood: an unclosed terminal can retain arbitrary-core hardness.

## 1. Inherited support, coefficients and exact rows

Radius-one packing in the ORIGINAL spectrum gives s(n+1)<=2^n. Projection of that support through a single physical query is injective, because two indices with the same projection differ in at most one bit. No coefficients merge. Each seed child F_b has exactly s nonzero coefficients with the same magnitudes, and its support has distance at least 2. A further singleton projection is again injective; hence H(F_b)=H(F_b restricted at j) for both signs and every remaining j. The unedited child therefore has exactly zero second-query entropy decrement.

Exactly one first-level child contains the physical edit. This child is a one-point edit of F_b on m=n-1 bits, with point mass p'=2p. It retains the ORIGINAL count bound s<=1/((n+1)p), which is stronger than replacing s by a generic distance-two packing estimate.

Every distance-at-least-two Boolean spectrum on m>=2 bits has a zero coefficient. All its integer Walsh sums are congruent modulo 4 to minus twice its negative truth count: for nonempty characters the Walsh sum of the constant vector is zero, and reducing the negative-vertex character sum modulo 2 removes the character signs. A zero Walsh coefficient therefore makes every Walsh sum a multiple of 4. Every nonzero coefficient has magnitude at least 4p'. Editing one point changes every coefficient by magnitude 2p'. In each singleton Fourier row the old anchor thus remains at least as large as its newly created partner. Ties cause no problem.

## 2. A row bound with the original s retained

Let U on m>=2 bits have support distance>=2 and exactly s coefficients. Let V be a one-point edit, q=2^(-m). For a singleton query there are s occupied old rows and 2^(m-1)-s empty old rows. The edit amplitude is 2q. Every empty row has mass 8q^2 and contributes twice its mass to the actual entropy decrement. Their total contribution is 8q-16s q^2 <=8q.

The occupied rows have total off-anchor squared mass b=4s q^2. If their total mass is A<=1, their conditional spectral entropy is at most A h2(b/A)<=b log2(1/b)+b/ln2, with zero terms defined by continuity. The occupied physical-channel entropy is at most (2/ln2)b. This is the two-point log-Sobolev bound, applied separately to each row and recentered on its larger coefficient. Thus, whenever b<=b0<=1,

    L_j(V) <= 8q + b0[log2(1/b0)+3/ln2].       (3)

The replacement uses that t[log2(1/t)+3/ln2] is increasing on (0,1], since its derivative is log2(1/t)+2/ln2>0. No lower bound on a row's total mass or a selected influence is used. This is a subnormalized occupied-row calculation; the newly created rows are retained separately.

For completeness the channel bound follows from Ent(w^2)<=(w0-w1)^2/2 in natural units. After normalizing w0^2+w1^2=2, its comparison function has derivative u/sqrt(1-u^2)-atanh(u)>=0 for 0<=u<1; differentiating this last expression gives (1-u^2)^(-3/2)-(1-u^2)^(-1)>=0. Absolute values only reduce the right side. Applying to w=(a+b,a-b), and exchanging a,b by multiplying the queried character, gives channel <=2 min(a^2,b^2)/ln2. Endpoints follow by continuity. The exact physical row decrement is spectral conditional entropy plus this channel, so it includes both actual child signs.

## 3. Uniform constants through the first query

For the original root take q=p and b0=4p/(n+1). Equation (3) gives

    L_i(G) <=8p+(4p/(n+1))[n+log2(n+1)-2+3/ln2]
           <(31/2)p.                              (4)

Indeed ln2>2/3 (the first positive term 2/3 in its atanh series), while log2(n+1)<=(n+1)/2 for integer n>=3. Equality holds in the latter at n=3; its induction uses (n+2)/(n+1)<=5/4<sqrt(2). The resulting upper coefficient is 14+6/(n+1)<=31/2. The strict logarithm inequality makes (4) strict.

For the edited child take q=2p and b0=16p/(n+1). This b0 is at most 1/2 for n>=3. The ORIGINAL support count gives b=4s(2p)^2<=b0. Now (3) yields, for EVERY remaining coordinate j,

    L_j(G_edited) <=16p+(16p/(n+1))[n+log2(n+1)-4+3/ln2]
                  <40p.                           (5)

The bracket is less than n+log2(n+1)+1/2, hence less than (3/2)(n+1). The other child has second-query decrement zero by Section 1. Averaging both complete children gives

    L_tree = L_i(G)+(L_(j_0)(G_0)+L_(j_1)(G_1))/2
           <(31/2)p+20p=(71/2)p.                  (6)

Only half the cost in (5) is charged. It is not a statement that each second query is separately paid from its child influence.

## 4. One influence owner and all actual terminals

Use the previously independently reconstructed A053 packing lemma I(G)>=2np (PACKING_CRITICAL_EXCLUSION, Section 3, accepted analytically by A054). Its boundary cases n=3 and constant seeds are included there. For clarity its nonconstant n>=4 proof bounds both physical sign classes by indicator Fourier uncertainty using support size<=s+1. After editing, each sign class has probability at least a=(3n-1)p/4<=11/64. Boolean Poincare gives I(G)>=4a(1-a)>2np. The constant case is I(G)=2np; at n=3 the seed must be a signed character and the direct influence formula gives the same bound.

Set I=I(G), a=Inf_i(G), and b=(Inf_(j_0)(G_0)+Inf_(j_1)(G_1))/2. Greedy choice and the physical influence identity give

    a>=I/n,
    b>=(I-a)/(n-1),
    Q=a+b>=2I/n>=4p.                              (7)

For the middle implication, (n-1)b>=I-a and na>=I; multiplying and adding yields n(n-1)Q>=2(n-1)I. All canceled denominators are positive since n>=3. Zero child influences are allowed; any maximizing index is admissible.

The exact physical telescope is I(G)-E_T I(G_leaf)=Q, with the four actual leaves and their original weights. Combining this with (6)--(7) proves (1)--(2). In particular if the root violates K>=9, at least one ACTUAL terminal has deficit strictly greater than D_K(G)+p/2. A least-dimensional violation cannot have this structure. No component, normalized row, recentered phase or arbitrary reference has been assigned an actual-child reserve.

## 5. Boundary of the argument

Two queries can project the original distance-three support to distance one. At that point a third query can merge two old coefficients. Equations (3)--(5) do not apply: the old-anchor uniqueness hypothesis fails. Paying that coherent signed interface, including all actual terminal deficits and earlier booked debits, is the first unsupported continuation. Generic affine minimality cannot replace actual child eligibility, as A052's path-code construction shows. This theorem buys exactly one more physical level from the ancestor packing and one influence owner; it makes no universal FEI claim.
