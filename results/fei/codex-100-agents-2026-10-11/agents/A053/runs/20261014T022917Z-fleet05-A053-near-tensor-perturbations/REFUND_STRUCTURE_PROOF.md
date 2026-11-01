# Exact refund zeros and one-point surgery on distance-three spectra

Uniform finite cubes, Boolean signs, entropy in bits. For a coordinate pair i,j use A052's Fourier quartet (alpha,beta,gamma,delta), squared mass q, pair collision Q, singleton contributions c_i,c_j, parity cost P, and merging refunds M_i,M_j. Their totals are obtained by summing retained indices. Zero fractions mean their continuous zero extension. For a Boolean function define its spectral support distance as the minimum Hamming distance between distinct nonzero Fourier indices; a singleton support has distance infinity.

## 1. Complete zero-refund row classification

Let Delta=alpha delta-beta gamma. Elementary factorization gives

    alpha beta(gamma^2+delta^2)-gamma delta(alpha^2+beta^2)
      =-Delta(alpha gamma-beta delta),
    alpha gamma(beta^2+delta^2)-beta delta(alpha^2+gamma^2)
      =-Delta(alpha beta-gamma delta).

The weighted-variance formulas for M_i and M_j therefore show that both refunds vanish exactly when either

    (T) Delta=0,

or, if Delta!=0,

    (E) alpha gamma=beta delta and alpha beta=gamma delta.

Zero denominator cases cause no exception: Delta!=0 forces both weights in each variance denominator to be positive. Case(T) is precisely a rank-one real2x2 Fourier row, including rows with zeros. Its physical partial Fourier row is a product of two real affine one-bit factors; those factors need not be Boolean.

Case(E) is exhausted by (a) beta=gamma=0 with alpha delta!=0; (b) alpha=delta=0 with beta gamma!=0; or (c) all four coefficients nonzero with delta=s alpha, gamma=s beta for s in{-1,1}, and alpha^2!=beta^2. To check the exhaustion, any zero coefficient forces the opposite-diagonal case. If all are nonzero, multiplying/dividing the two equations gives delta^2=alpha^2 and gamma^2=beta^2, and their signs must use the same s. In(c), the physical row is

    w(x_i,x_j)=(1+s x_i x_j)(alpha+beta x_i).

It is supported on two of the four physical assignments, so its normalized collision is at least1. In(a),(b) the signed parity term can remain although both refunds vanish. Thus refund zeros encode several distinct structures, not just a tensor cut of the parent Boolean function. Rank-one rows themselves may occur throughout sparse code spectra without yielding a single global coordinate tensor factorization.

## 2. A sharp exponential scale for sparse-spectrum point surgery

Let F be any Boolean function on n>=3 named coordinates whose Fourier support distance is at least3. Let G=F-2F(v)1_v, p=2^-n, e=2p. Each Fourier coefficient changes by an amount of absolute value e. Every queried singleton row of F has at most one nonzero coefficient; every queried pair row likewise has at most one. Hence initially all singleton and pair B,J,Gamma,C and all pair merging refunds are zero.

In an edited singleton row one of the two amplitudes has magnitude e, because its old amplitude was zero. Thus

    4a^2 b^2/(a^2+b^2)<=4e^2.

There are2^(n-1) rows, giving C_i(G)<=8p. By nonnegativity of refunds and their definitions, for every pair

    0<=M_i^total(G)+M_j^total(G)<=C_i(G)+C_j(G)<=16p.     (1)

For a pair row, multiplication by a Fourier character permits putting the possible old nonzero coefficient at alpha without changing the physical-square collision. Its edited quartet has the form (u,plus/minus e,plus/minus e,plus/minus e). Each of the three signed square coefficients is bounded in absolute value by e(|u|+e), so

    Q<=12e^2 (|u|+e)^2/(u^2+3e^2)<=16e^2.

The last inequality is weighted Cauchy--Schwarz: (|u|+e)^2<=(4/3)(u^2+3e^2). All-zero old rows obey the same estimate. Summing2^(n-2) rows gives

    C_{ij}(G)<=16p.                                       (2)

This O(p) estimate is specific to distance-three spectral support, and improves the general O(sqrt(p)) Gamma surgery modulus. It is not asserted for arbitrary sparse support with close Fourier indices.

## 3. Joint entropy/collision prices and exact critical-source exclusion

In every pair row choose its old active Fourier index as anchor, choosing any index on an old zero row. The other three edited amplitudes all have magnitude e. The total mass off these row-dependent anchors is exactly3e^2*2^(n-2)=3p. Conditional entropy concavity gives

    B_{ij}(G)<=h2(3p)+3p log2 3.

As log2(1+c)<=c/ln2, (2) yields

    V_{ij}(G)<=h2(3p)+3p log2 3+16p/ln2
             <(3n+29)p.                                  (3)

Here h2(x)<=x log2(1/x)+x/ln2 and ln2>2/3. The conditional entropy bound holds since3p<=3/8<3/4 for n>=3, in the increasing range of the capped three-atom remainder entropy. Analogously each singleton has off-anchor mass2p and

    V_i(G)<=h2(2p)+8p/ln2 <(2n+13)p.                      (4)

Write D_K=H-KI and actual S_A=-E D_K(physical child). Restriction gives D_K(G)+S_A=L_A(G)-K I_A(G) exactly. Thus if G were a least-essential-dimension K-violation, K>0, all S_A>=0, and (3),(4) force

    0<D_K(G)+S_{ij}+K I_{ij}(G)<(3n+29)p,
    0<D_K(G)+S_i+K Inf_i(G)<(2n+13)p.                     (5)

Since each edited influence differs from the seed by at most2p, the necessary seed-relative inequalities are

    D_K(G)+S_{ij}+K(I_{ij}(F)-4p)<(3n+29)p,
    D_K(G)+S_i+K(Inf_i(F)-2p)<(2n+13)p.                  (6)

In particular, K(I_{ij}(F)-4p)>=(3n+29)p rules out minimality of a violating G. A singleton condition from(6) is stronger when its seed influence is healthy. These are quantitative exclusions with a complete root/child/influence account, not an absolute positive lower bound on D. They do not claim every minimal witness is near a distance-three spectral seed.

## 4. All-dimensional Boolean admission with tiny total refunds

Fix a nonconstant Boolean h on k>=1 essential bits. On kt logical bits take h^(tensor t), and replace every logical bit by the product of three fresh fair physical signs. Call the resulting Boolean sign F_t; n=3kt. Its Fourier indices are unions of entire disjoint triples, so distinct indices differ on at least3 coordinates. Exact Fourier substitution gives

    H(F_t)=t H(h), I(F_t)=3t I(h).

Flip any one physical vertex to obtain G_t. For t>=2, F_t is a nontrivial coordinate product and has even negative count. G_t has odd negative count, hence is prime across every coordinate partition. All integer Walsh sums are2 modulo4, so its Fourier support is full and every coordinate essential. Its cross-copy multiplicative plaquette defects equal4p, connecting the entire coordinate graph.

(1)--(4) apply simultaneously to ALL singleton and pair cuts. In particular the sum of both merging refunds over all pairs is at most16*binom(n,2)*2^-n, tending to zero. The entropy and influence continuity estimates for one-point surgery give

    lim_(t->infinity) H(G_t)/I(G_t)=H(h)/(3I(h)).         (7)

For completeness, squared-spectrum TV is at most2sqrt(p(1-p)) by the unit-vector product inequality. Maximal coupling bounds the entropy change by h2(delta)+delta log2(2^n-1) at the true TV delta; this is O(n sqrt(p)), and |delta I|<=2np. These errors tend to zero, while seed influence grows linearly in t. No unbounded-ratio seed is assumed. A universal FEI constant C for this prime, full-support, vanishing-refund class would imply FEI(3C) for every h; FEI for all Boolean functions obviously bounds the class. This is constant-factor hardness admission, not a disproof.

Every logical bit of F_t has fixed positive seed influence (after removing seed dummies). Thus(6) excludes these G_t as minimal witnesses at any fixed K>0 for sufficiently large t if they violate that K. A physical version also retains the terminal: fix two bits in every triple and all but one logical copy, choosing one fixed bit away from the edited vertex. The remaining child is an input translate of +/-h. If H(h)>3K I(h), that child violates K, while the root eventually violates K by(7); the root is not dimension-minimal. This preserves the distinction between arbitrary hard seeds and child-certified sources.

## 5. Remaining universal line

The exact refund-zero classification and sparse-seed surgery estimates close this mechanism on a meaningful structural boundary. Small or absent merging refunds do not by themselves certify parent factorization or universally low entropy/influence, even after qualitative primitivity and full support are imposed. The first unsupported line is a dimension-independent selection/payment rule on genuine minimal witnesses controlling the residual signed pair cost relative to D+S_pair and its phase bank. No theorem here makes every such witness close to a distance-three code spectrum or supplies a positive refund floor on the complementary dense regime.
