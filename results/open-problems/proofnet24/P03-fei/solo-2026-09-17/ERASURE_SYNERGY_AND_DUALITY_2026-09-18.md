# Erasure synergy and the dual-correlation barrier

Status: proved below and self-checked; novelty UNVERIFIED. These are structural obstructions and equivalences, not a proof of FEI.

For a probability law p on subsets of [n], write

    H(p)=-sum_S p_S log_2 p_S,
    B(p)=sum_i H(X_i | X_{-i}),
    D(p)=H(p)-B(p).

The quantity D is the dual total correlation (also called binding information in parts of the information-theory literature). Only the displayed formula is used here. For a Boolean f, p_S=fhat(S)^2 and we write H(f),B(f),D(f).

## 1. One mixing bit can create m erasure bits

**Theorem.** For every odd m>=3 there are Boolean functions g_0,g_1 on m bits and a Boolean selector F on m+1 bits, whose restrictions at the selector are g_0,g_1, such that

    H(g_0)=H(g_1)=m-1,    B(g_0)=B(g_1)=0,
    I(g_0)=I(g_1)=m/2,

while

    H(F)=B(F)=m+1,        I(F)=(m+1)/2.

The selector influence is exactly 1/2. If q is the equal mixture of the two restriction spectral laws, then

    B(q)-[B(g_0)+B(g_1)]/2=m,

although the mutual information between the input selector and a draw from its restriction spectrum is exactly one bit.

**Construction and proof.** Use {0,1} coordinates for the construction and characters chi_S(y)=(-1)^(sum_{j in S}y_j). Put r=m-1, which is even, and let

    b(t)=(-1)^(t_1 t_2+t_3 t_4+...+t_{r-1}t_r).

The two-bit Walsh transform of (-1)^(uv) is (1,1,1,-1)/2. Tensoring shows that b is bent: every one of its 2^r Fourier coefficients has squared magnitude 2^(-r).

For y in {0,1}^m define

    g_0(y)=b(y_1+y_m,...,y_{m-1}+y_m),
    g_1(y)=(-1)^(y_m) g_0(y),                         (1)

where additions inside b are modulo two. The substitution maps a character indexed by S subset [m-1] to

    S                         if |S| is even,
    S union {m}               if |S| is odd.

This is a bijection from all subsets of [m-1] to the even-cardinality subsets of [m]. Therefore the squared Fourier law of g_0 is uniform on the 2^(m-1) even subsets. Multiplication by (-1)^(y_m) shifts Fourier support by {m}, so the squared law of g_1 is uniform on all odd subsets.

Uniform even or odd parity on m>=3 bits has entropy m-1. Every coordinate is determined by the other m-1 coordinates, so its aggregate erasure entropy is zero. Every coordinate marginal is fair, so its mean Hamming weight, hence Fourier influence, is m/2.

Add a selector z and set F(0,y)=g_0(y), F(1,y)=g_1(y). Its Fourier coefficients are

    Fhat(b,S)=[g0hat(S)+(-1)^b g1hat(S)]/2.            (2)

The two restriction supports are disjoint and partition all subsets S. Equation (2) consequently has squared magnitude 2^(-(m+1)) for every (b,S). Thus F has the uniform spectral law on m+1 bits. Its entropy and erasure entropy are m+1, and its influence is (m+1)/2. Finally g_0 and g_1 differ precisely when y_m=1, proving selector influence 1/2. The parity of S identifies which restriction law generated S, giving one bit of selector/spectrum mutual information. QED.

This refutes every proposed dimension-free inequality of the form

    B(equal mixture of restriction spectra)
       <= average restriction B + C times selector influence.  (3)

The general log-Sobolev control of the one-bit mutual information does not repair (3): aggregate erasure can amplify one latent parity bit into m conditional bits.

## 2. No fixed linear mixture of B and D below H is restriction-stable

For 0<=lambda<1 define

    P_lambda=B+lambda D=lambda H+(1-lambda)B.

If a universal restriction inequality

    P_lambda(F)<= [P_lambda(F_0)+P_lambda(F_1)]/2
                     +C Inf_selector(F)               (4)

held for some finite C, the theorem would give

    m+1 <= lambda(m-1)+C/2,

or C>=2[(1-lambda)m+1+lambda] for every odd m. This is impossible when lambda<1. Thus no fixed linear interpolation strictly below H supplies a dimension-free one-coordinate induction potential. Taking lambda>=1 makes P_lambda dominate H and does not constitute a simplification of the target.

This statement concerns this exact family of potentials and inequality (4). It does not rule out a nonlinear or state-dependent potential.

## 3. The complementary piece D is itself FEI-complete

It is tempting to treat D=H-B as an easier correction term. The following exact reduction shows that a universal D/I bound is already equivalent to FEI up to a factor two.

Given any Boolean g on n bits, first define its one-coordinate parity lift on n+1 bits by

    f(x_1,...,x_n,z)=g(x_1 z,...,x_n z).                (5)

If S subset [n], its character in g becomes chi_S(x)z^|S|. Thus the nonzero Fourier coefficients of f are

    fhat(S)=ghat(S)                         for |S| even,
    fhat(S union {z})=ghat(S)               for |S| odd.                (6)

All occupied spectral subsets of f have even cardinality, hence no two are adjacent. Therefore

    H(f)=H(g),        B(f)=0,        D(f)=H(g),
    I(f)=I(g)+Pr_{T~ghat^2}(|T| is odd) <=2 I(g).        (7)

The final inequality uses 1{|T| odd}<=|T|. Restricting z=+1 recovers g exactly. This lift adds only one coordinate.

For comparison, an exact-factor pair lift on 2n bits is

    f_pair(x_1,...,x_{2n})=g(x_1 x_2,x_3 x_4,...,x_{2n-1}x_{2n}).        (8)

in sign notation. If S subset [n], the character chi_S in g becomes the character on the union of the corresponding disjoint pairs. Hence

    fhat(union_{j in S}{2j-1,2j})=ghat(S),

and all other Fourier coefficients vanish. The spectral entropies agree and every occupied coordinate in the lift comes with its pair mate:

    H(f_pair)=H(g),   I(f_pair)=2I(g),   B(f_pair)=0,
    D(f_pair)=H(g).                                                    (9)

The equality B(f)=0 holds because membership of any one lifted spectral coordinate is determined by membership of its mate.

Let

    C_FEI=sup_g H(g)/I(g),    K_D=sup_f D(f)/I(f),

with zero-influence constants omitted and extended-real values allowed. Since D<=H,

    K_D <= C_FEI.

Conversely (7), applied to every g, gives H(g)<=K_D I(f)<=2K_D I(g), so

    K_D <= C_FEI <= 2 K_D.                              (7)

Thus finiteness of K_D is equivalent to full FEI. The parity lift converts all spectral entropy into dual total correlation while increasing influence by at most two; the pair lift gives exact factor two. A plan that first proves D<=C I has not separated off an easy remainder; it has solved an equivalent full-scope problem.

Together with the earlier erasure reduction, both summands in H=B+D can independently carry the full difficulty under Boolean-preserving transformations. For B the equivalence was obtained through restriction induction; for D equation (5) is a direct explicit reduction.

There is a sharper class-level consequence. Let Z be the class of Boolean functions whose positive Fourier support contains no adjacent pair. This is exactly the class B=0 (equivalently K=0): a binary conditional entropy is positive precisely when both members of some spectral edge have positive mass. Every parity lift (5) lies in the still smaller class whose Fourier support has even cardinality. Therefore FEI restricted only to that even-support class is already equivalent to full FEI up to factor two. Indeed, a constant C on this class gives

    H(g)=H(f)<=C I(f)<=2C I(g)

for every g. Conversely full FEI of course covers Z.

This does not undermine the universal B or K reduction: that reduction uses induction through restrictions, and Z is not restriction-closed. Fixing z=+1 in (5) gives g. Hence a top-level function can have no spectral edges at all while a single restriction recovers the entire original FEI difficulty. Any direct edge argument must track what restriction creates, not only the edges visible at the current node.

## 4. Exact checks and limits

`check_erasure_synergy.py` performs exact integer Walsh transforms for m=3,5,7, verifies every claimed signed coefficient and the full spectral laws, checks the pair lift on every Boolean truth table through three original variables, and checks the sharper parity lift on every Boolean truth table through four original variables. It also records the exploratory small-dimension maxima of D/I from complete enumeration through four variables; those floating entropy values are not used in a theorem.

The universal statements above are proved algebraically, not by these finite checks. The checks are not an independent audit. Prior-art novelty has not been established.

## 5. Consequence for the live route

The logarithmic edge target K<=C I remains open. A recursive proof cannot replace the restriction entropy by erasure entropy alone: parity-supported restriction spectra have zero B, yet their mixture has maximal B. Nor can the missing D be bounded separately without confronting an FEI-equivalent problem.

A viable potential must retain enough information about global spectral constraints to prevent the parity-to-independent conversion in Section 1, while still admitting a non-reusing influence charge. Merely naming D, adding a fixed fraction of it, or controlling the selector/spectrum mutual information does not do this.
