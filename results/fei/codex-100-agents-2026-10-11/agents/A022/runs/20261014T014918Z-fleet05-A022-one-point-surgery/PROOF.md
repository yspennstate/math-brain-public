# Large-contrast one-point switches: expose data before controllers

Uniform signs, entropy in bits. Let k=2m>=4, b(x)=(-1)^{sum_j x_(2j)x_(2j+1)},
v any k-cube vertex, A any Boolean indicator on any number t>=0 of uniform
independent controller bits, a=1-2A, alpha=EA, delta=2^-k. Define the ACTUAL sign

    F(x,z)=b(x)(1-2 1_{x=v} A(z)).

There is no balance, overlap, point-block-width or FEI hypothesis on A.
The statement proved is

    I_ctrl(F)=delta I(a),
    H(F)<=7 I_data(F)+delta H(a).

Consequently H(a)<=C I(a) implies H(F)<=max(7,C)I(F).
The controller entropy is inherited, not established or discarded.
This extends the A022 stopping mechanism to arbitrary overlapping controllers
for one data-vertex flip; it is not a proof of FEI for arbitrary controllers.

## 1. Exact signed root spectrum and its logarithmic costs

For data label S and controller label T,

    Fhat(S,T)=bhat(S) 1_{T=empty}-2delta b(v)chi_S(v) Ahat(T).

For T!=empty, the 2^k data masses are identical, 4delta^2 Ahat(T)^2.
Put phi(u)=u log2(1/u), phi(0)=0, beta=2^(-k/2),
N_plus=(2^k+2^(k/2))/2, N_minus=(2^k-2^(k/2))/2.
The alignment signs bhat(S)b(v)chi_S(v)/beta have sum 1/beta,
so the controller-empty row has N_plus masses (beta-2delta alpha)^2
and N_minus masses (beta+2delta alpha)^2. Hence exactly

    H(F)=N_plus phi((beta-2delta alpha)^2)
        +N_minus phi((beta+2delta alpha)^2)
        +delta[H(a)-phi((1-2alpha)^2)]
        +8delta alpha(1-alpha)k.                         (1)

The last term is the exact data-frequency spreading cost on nonempty
controller rows. No sign-free perturbation is substituted before squaring.
Physical edge counting separately gives

    I_data(F)=k/2+2delta alpha sum_i b(v)b(v xor e_i),
    I_ctrl(F)=delta I(a).                               (2)

These formulas include alpha=0,1 and controllers with dummy coordinates.
The root identities (1)-(2) also hold for every bent sign, beyond the paired
quadratic reference: flatness gives the same alignment count, and
sum_S bhat(S)^2 chi_S(e_i)=0 gives zero autocorrelation in direction i,
hence Inf_i(b)=1/2. The stopping proof below specifically uses the intact
quadratic pairing and is not asserted for an arbitrary bent reference.

## 2. All access nodes are K4-good, without a fair inactive branch

Query ONLY x_0,x_2,...,x_(2m-2), then STOP with every partner and controller
bit retained. At a node after q<m first coordinates, the unedited reference
still has a uniform partner, so its current queried-coordinate influence
is 1/2. If the prefix excludes v, no perturbation remains. Otherwise the
perturbation has physical measure u=alpha 2^{-(k-q)}. Its union with its
coordinate translate has measure 2u, so changing the sign there changes
that coordinate influence by at most 2u. Therefore

    d>=1/2-2alpha 2^{-(k-q)}>=1/2-2^-m>=1/4.

The selector/controller need never have an inactive branch of weight1/2.
Concavity gives B<=h2(d), and the decreasing ratio h2(d)/d gives
B/d<=8-3log2(3)<4. Thus access bad-node odd-face charge at threshold4
is exactly zero, in every controller dimension. A constant node stops early.

## 3. Exact exceptional-leaf entropy

Put tau=2^-m. All but one of the 2^m first-coordinate fibers are characters
in the remaining partner bits (constant in the controllers). The exceptional
fiber is chi_L(t) q(t,z), with

    q(t,z)=1-2 1_{t=w} A(z).

Character multiplication preserves H and every controller influence.
Each raw partner influence is 2tau alpha<=1/2 because m>=2; multiplying
by chi_L complements selected partner influences, so the ACTUAL leaf data
influence is at least J_data=2m tau alpha. Its controller influence is
tau I(a). These are distinct physical coordinate accounts.

The signed q spectrum has controller-empty masses (1-2tau alpha)^2 at
the empty partner label and 4tau^2 alpha^2 at each of the other 2^m-1
partner labels; the T!=empty masses are 4tau^2 Ahat(T)^2 at every partner
label. Thus its exact complete entropy, including the empty row, is

    H(q)=phi((1-2tau alpha)^2)+(2^m-1)phi(4tau^2 alpha^2)
        +tau[H(a)-phi((1-2alpha)^2)]
        +8tau alpha(1-alpha)m.                          (3)

No raw logarithmic term in (3) is asserted bounded by selector influence.
For 0<alpha<=1, use phi(s)<=log2(e)(1-s), discard the nonpositive
-tau phi((1-2alpha)^2), and bound the small masses directly. This gives

    H(q)<=tau H(a)+8m tau alpha
          +8tau alpha^2 log2(1/alpha)+4tau alpha log2(e).

Since alpha log2(1/alpha)<=log2(e)/e,

    H(q)<=tau H(a)+[4+(2+4/e)log2(e)/m] J_data
         < tau H(a)+7 J_data.                           (4)

For m>=2, e>2 and log2(e)<3/2 prove the final comparison. The latter
follows from ln2>2/3, e.g. the first two positive atanh terms give
ln2>56/81>2/3. Alpha=0 is constant and is handled directly.
Formula (4) uses the data-coordinate reserve; it does not consume any
controller influence to pay the alpha log alpha term. This is the required
single-use ownership of the local logarithmic excess.

## 4. Complete physical stopping partition

Let I_access=sum_v pi_v d_v and I_leaf,data be the expected actual data
influence left at stopping leaves. Exactly

    I_data(F)=I_access+I_leaf,data,
    I_ctrl(F)=E_leaf I_ctrl(leaf)=delta I(a).

The exceptional fiber has physical reach tau. Its inherited entropy bill
is tau times tau H(a)=delta H(a), not tau H(a). All other leaf entropies
are zero. Combining (4) and the exact fair-coordinate entropy telescope,

    H(F)<= (4+2/ln2)I_access+7 I_leaf,data+delta H(a)
         <=7 I_data(F)+delta H(a).

Here 4+2/ln2<7 since ln2>2/3. The C005 scalar bound JS<=2d/ln2 has the
self-contained series proof in A022 stage3 PROOF.md §3: its entropy-series
coefficient 1/[2j(2j-1)] is bounded by the square-root-series coefficient;
continuity handles endpoints and signed amplitudes use (|u|-|v|)^2<=(u-v)^2.
Neither a fresh controller reserve nor terminal entropy is recreated below
the root. The actual character-shifted leaf influences are used throughout.

## 5. The exact universal gap

The scoped theorem (1)-(4) and stopping payment are proved. The first
unsupported extension is a dimension-independent certificate for H(a)/I(a)
when the controller itself is arbitrary, or a uniform policy for growing
numbers of edited vertices. TWO_VERTEX_PROOF.md closes the first unequal-
controller two-vertex collision as a scoped follow-up. The one-
vertex transformation inherits arbitrary-controller FEI difficulty, rather
than resolving it. It does remove the logarithmic contrast price from the
data-access budget by spending a named data reserve and retaining the
controller entropy with its exact delta weight. Arbitrary constant-leaf
completion is not asserted K4-good.
