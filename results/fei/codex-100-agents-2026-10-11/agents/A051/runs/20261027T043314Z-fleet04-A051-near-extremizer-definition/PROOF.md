# The complete critical budget retains a conditional Gibbs divergence

The complete child account bounds a conditional divergence, including dependence on the unqueried spectrum. Its absolute smallness does not bound the divergence after conditioning on a rare occupied row.

## 1. Finite selection and the error convention

Write H in bits and let a(g) be the minimum influence over invertible affine input changes and multiplication by an output character. These operations permute squared Fourier coefficients. For C>0, if any finite Boolean function violates H<=C I, choose the least essential dimension n of a witness. Compression and finite orbit minimization give a representative with I=a and the same positive deficit. A maximum deficit in this finite dimension exists; no all-dimensional optimizer is asserted. Every proper physical child and every affine/character representative of that child satisfies H<=C a.

For C=K+epsilon with K,epsilon>=0 and C>0, the terminal condition is equivalently H-Ka<=epsilon a. This allocation is made once at a terminal. Local approximation error is charged to influence actually spent, as in A051 TOLERANCE Sections1--4. It is not charged repeatedly to remaining influence. Descendants need not inherit maximality or stationarity.

## 2. An exact identity before criticality

Let A be any nonempty proper coordinate block of size r, sigma=sum_{i in A} Inf_i(f), and g_x the COMPLETE physical children. Put t=E a(g_x), R=E I(g_x)-t>=0, D=H(f)-C I(f), S=E[C a(g_x)-H(g_x)], and L=H(f)-E H(g_x). Then

    D+S+C R=L-C sigma.                                      (1)

Let P be the actual squared Fourier law on (Z_A,Z_B), and J=L-H(Z_A|Z_B). The block Fourier chain rule identifies J with the mutual information between physical assignment x and its complete child spectral label, using uniform physical reaches and the actual child laws. The fibrewise uniform log-Sobolev inequality gives 0<=J<=c sigma, c=2/ln(2). Set G=c sigma-J>=0, gamma=C-c, theta=1/(1+2^gamma), and Q=Ber(theta)^{tensor r}. All coordinates of Q are strictly positive. Define

    W_A=D_2(P_{A,B} || Q tensor P_B)
       =E_{Z_B} D_2(P_{A|Z_B} || Q).

Zero P_B fibres contribute zero. Expanding the cross entropy of Q gives

    W_A=r log2(1+2^(-gamma))+gamma sigma-H(Z_A|Z_B).

Consequently the COMPLETE identity is

    D+S+C R+W_A+G=r log2(1+2^(-gamma)).                    (2)

This is an equality for every Boolean f, without criticality. It also holds with ANY c>=2/ln(2), defining its own nonnegative G. In particular c=3 and integer C give rational theta, allowing exact prime-log checks. The sharp capacity uses exp(2)2^(-C); c=3 uses 2^(3-C) and is deliberately weaker.

Writing p_i=P(Z_i=1), the same divergence is

    W_A=sum_{i in A} h2(p_i)-H(Z_A|Z_B)
        +sum_{i in A} D_2(Ber(p_i)||Ber(theta)).           (3)

The first term includes both internal total correlation and dependence on B. Replacing it by internal correlation alone loses a nonnegative price. No claim of independence of the physical children is used.

## 3. Critical and occupied certificates

At the genuine finite critical representative of Section1, D>0 and S>=0. Thus every proper A has

    W_A+G+C R+S < r log2(1+2^(-gamma)).                    (4)

This independently reconstructs A054 PROOF Sections1--4, and retains exactly the slacks discarded in its bound. In particular it is one shared ceiling, not independent capacity for each term. Upper bounds from different blocks are NOT added as available money.

For any event E determined by Z_A, with v=P(E) in (0,1) and q=Q(E) in (0,1), chain-rule expansion gives

    W_A=d2(v||q)+v W_1+(1-v)W_0,                         (5)
    W_1=D_2(P_{A,B}|E || (Q|E) tensor P_B),
    W_0=D_2(P_{A,B}|E^c || (Q|E^c) tensor P_B).

Notice that the reference exterior law remains P_B, not P_{B|E}. Replacing it silently erases I(1_E;Z_B). All quantities in (5) are nonnegative. Taking E={Z_A!=0} is canonical. Under criticality,

    v W_1 < capacity-D-S-C R-G <= capacity.               (6)

If v>=eta*capacity for a specified eta>0, then W_1<1/eta. This is a sufficient relative occupation hypothesis, not a conclusion that critical sources satisfy it. With v=0 the occupied law is undefined and no division is permitted. With v=1 the complementary term is omitted and the one-event chain rule applies. For the chosen nonempty proper pattern event Q has q in (0,1).

## 4. Actual Boolean counterguard to an absolute-to-relative inference

Let f_n be +1 except at one input, n>=2, and choose A={1}. With p=2^-n, its squared Fourier spectrum is P(0)=(1-2p)^2 and P(s)=4p^2 for all s!=0. The occupied probability is v=2p. Conditional on Z_1=1, Z_B is uniform on 2^(n-1) labels. The exterior law has mass m=1-4p+8p^2 at zero and mass 8p^2 at every other label. Therefore

    W_1=-(n-1)-2p log2(m)-(1-2p)log2(8p^2)
       =(1-4p)n-2+6p-2p log2(m) >= n/2-2  (n>=3).       (7)

For any fixed C and c, however, W_A tends to log2(1+2^(-gamma)), rather than zero: the fixed product reference has fixed positive nonempty mass. Thus fixed-C capacity-smallness alone must not be described as a sequence converging to zero.

For a genuine vanishing absolute-divergence guard take C_n=n, c=3. Then theta_n=1/(1+2^(n-3)) tends to zero and

    0<=W_A<=log2(1+2^(3-n))+(n-3)2^(1-n)->0,

while W_1>=n/2-2 diverges. The inequality uses H(Z_1|Z_B)>=0. This changes C as explicitly stated; it does NOT produce high-C critical witnesses. Point defects are not such witnesses, and neither (4) nor a universal FEI counterexample is claimed for them. The guard only refutes passing from an unnormalized vanishing divergence to a uniform occupied-law bound without a lower occupation hypothesis. There is no mismatch between the fixed-C and varying-C statements.

## 5. Verification and remaining line

Potential failures to check are the sign of S without criticality, the use of complete optimized children, conditional versus marginal exterior laws in (5), zero event mass, the choice of c and theta, and reusing a block ceiling across blocks. Exact finite validation checks all labelled functions through three variables, all proper blocks, complete child minima, conditional Gibbs expansion, all nontrivial pattern events, and negative-reserve controls. A second representation checks point defects and the exterior-reference correction. Scalar Lean checking addresses only budget algebra and division by a positive occupation, not the entropy or log-Sobolev theorem.

FIRST UNSUPPORTED UNIVERSAL LINE: choose and pay an ORIGINAL proper block on every genuine high-C finite critical witness, with phase price, mixed rows, old debits and both full terminals. Equations (2)--(6) quantify a necessary source condition but do not give either a lower occupation bound at a useful block or a lower funding bound. The next mathematical action is to combine signed Boolean convolution and unused quotient rank with this SAME complete child account. Full FEI remains OPEN; no dimension-independent constant improvement is asserted.
