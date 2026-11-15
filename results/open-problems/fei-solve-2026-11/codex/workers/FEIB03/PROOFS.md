# Containment entropy: proofs and failed routes

All functions called Boolean take values in {-1,+1}. Coordinates use x_i=(-1)^bit_i. A truth-table integer has bit x set when f(x)=-1. Write p(S)=fhat(S)^2, u(S)=sum_{T containing S}p(T), and A(f)=sum p(S) log2(1/u(S)). Zero-weight summands are zero. I(f)=sum |S|p(S). Unless explicitly extended to real functions, Parseval gives total mass one.

The general A-conjecture is unresolved by this work. The statements proved below are partial results and exact obstructions to particular proof steps.

## (a) Generalized influences

The primary source consulted was [Kelman, Kindler, Lifshitz, Minzer and Safra, arXiv:1911.10579v2](https://arxiv.org/html/1911.10579), Definition 2.3, Section 4.1 and Theorem 1.3. Their generalized influence is u(S). Their low-degree entropy bound retains a factor log(|S|+1). Direct summation of higher derivatives counts a spectral set T once for every subset of the chosen order; the paper also identifies this obstruction. Translating their entropy theorem to the present +/-1 convention and using A<=H gives A<=O(I+sum |S|log(|S|+1)p(S)). This implication retains the extra logarithm; it does not prove A<=CI.

Here is an elementary influence-tail estimate reconstructed independently. Fix k>=1. Set W_k=sum_{|S|=k}p(S) and M_k=sum_{|S|=k}u(S)=E[binom(|U|,k)]. For a restriction to a k-dimensional face, the top coefficient c_S is a multiple of 2^(1-k). Consequently |c_S|<=2^(k-1)c_S^2, and

    |fhat(S)| <= E|c_S| <= 2^(k-1)u(S),
    p(S) <= 4^(k-1)u(S)^2.

For any t in (0,1],

    sum_{|S|=k, u(S)<=t}p(S) <= min(W_k, 4^(k-1)t M_k).

Integrate the spectral tail at t=2^(-r), r>=0. With Q_k=4^(k-1)M_k and W_k>0, this proves

    A_k <= W_k log2(Q_k/W_k) + W_k/ln(2).

Indeed integrate W_k up to r=log2(Q_k/W_k), and Q_k 2^(-r) thereafter. Q_k>=W_k, since M_k>=W_k. When W_k=0 both sides are zero.

For k=1, p({i})<=I_i^2 gives the simpler bound A_1<=I/(e ln 2), because t log2(1/t)<=1/(e ln 2). For higher levels, the missing step is a dimension-free payment for the factorial moments M_k. The tempting estimate sum_{|S|=k}u(S)<=C_k I is false for every fixed k>=2: parity on n coordinates has left side binom(n,k) and I=n. At k=2 their ratio is (n-1)/2. This refutes that summation step, not every use of the KKLMS method. The tail estimate above has not removed the factorial-moment loss.

Verdict (a): proved a levelwise tail estimate; no constant bound for A; parity refutes the naive higher-influence payment.

## (b) Coordinate recursion and its obstruction

Extend A to an arbitrary real function using the same unnormalised formula. For g=a+x_i d, put u=u_a and v=u_d, with S omitting i. Its Fourier coefficients are ahat(S) and dhat(S); its upward sums are u(S)+v(S) and v(S). Subtracting the definitions proves exactly

    A(g)=A(a)+A(d)-J,
    J=sum_S ahat(S)^2 log2(1+v(S)/u(S)) >= 0.

If ||g||_2=1 and t=||a||_2^2, homogeneity gives

    A(g)=t A(a/sqrt(t))+(1-t)A(d/sqrt(1-t))+h_2(t)-J.

Endpoint terms use their continuous values. Thus the normalization entropy is explicit, with a subtractive J. The normalized children are generally not Boolean. The extension A(g)<=C I(g) to all norm-one real functions is false: g=(x_1+...+x_m)/sqrt(m) has A=log2(m) and I=1.

The direct Boolean restriction inequality

    A(f) - (A(f_{i=+1})+A(f_{i=-1}))/2 <= C I_i(f)

also fails for every fixed C. Here is an explicit family and proof, not a real-valued surrogate.

Let m=2r, N=2^m, t=1/N, and

    h(x)=(-1)^(sum_{j=0}^{r-1} bit_{2j} bit_{2j+1}).

Let delta be the indicator of the all-zero bit input on these m variables. Define f(x,+1)=h(x) and f(x,-1)=h(x)-2delta(x). These are both Boolean because h(0)=1. Then a=h-delta, d=delta, and I_i(f)=t.

For a subset S of the m core variables, let b be its number of full pairs, c its number of singleton pairs, and k=2b+c. A pairwise transform gives

    w_S=hhat(S)=2^(-r)(-1)^b,
    u_h(S)=2^(-k),
    C_S=sum_{T containing S}hhat(T)
       =(-1/2)^b if c=0, and 0 otherwise.

The last identity follows by factoring the sum pair by pair: an empty pair contributes 1, a singleton pair 0, and a full pair -1/2. Also delta_hat(S)=t and u_delta(S)=t 2^(-k). Write q_S=1-2^k C_S. The upward probabilities for the parent sets omitting i and the flipped child are respectively

    2^(-k)(1+2t q_S),   2^(-k)(1+4t q_S).

Sets containing i in the parent have upward probability t 2^(-k). Substitute these and the coefficients w-t, t, w, w-2t into A. All terms multiplying k cancel, leaving the exact identity

    Delta_i A = m t
      - sum_S (w_S-t)^2 log2(1+2t q_S)
      + (1/2)sum_S (w_S-2t)^2 log2(1+4t q_S).       (1)

The remaining two sums are o(t). Here are explicit estimates sufficient for that conclusion. For r>=4, |4t q_S|<=4*4^(-r)(1+2^r)<1/2. On this interval

    |log2(1+x)-x/ln(2)| <= x^2/ln(2).

The linear contribution in the two sums of (1) combined is

    [-4t^2(1-(3/2)^r)+6t^3(4^r-(-1)^r)]/ln(2).

To obtain it, use sum w=1, sum w*2^k C=(3/2)^r and sum 2^k C=(-1)^r. The square remainder has absolute value at most

    48 t^3 (4^r+2+5^r)/ln(2),

since (w-t)^2 and (w-2t)^2 are at most 4t and sum q_S^2=4^r-2(-1)^r+5^r. Dividing both the linear expression and this remainder by t gives quantities tending to zero. Therefore

    Delta_i A / I_i(f) = m + o(1) -> infinity.

Multiplying this whole family by a fresh dictator y makes the parent and both distinguished-coordinate slices balanced. Every spectral set gains the mandatory coordinate y, so A is unchanged in all three functions, and I_i is unchanged. The obstruction therefore persists even with balanced parent and balanced children. A potential depending only on their means cannot repair this restriction inequality, since all three means are zero.

This family also prevents J from paying the normalization entropy up to O(I_i). For r>=2, u_a(S)>=2^(-k)/2, whereas u_d(S)=t 2^(-k). Hence

    J <= sum ahat(S)^2 log2(1+2t) <= 2t/ln(2),
    h_2(t)/t = m+1/ln(2)+o(1).

Consequently h_2(t)-J is not O(t). This is the precise failure of the tempting entropy-credit step in the normalized recursion. It leaves open a richer potential using additional information about the children.

`routes.py` evaluates (1) by multiplicities r!/(b!c!(r-b-c)!)*2^c, using Decimal arithmetic, and compares it with truth tables through m=18. The plain local restriction payment cannot work.

Verdict (b): exact recursion proved; direct constant coordinate payment refuted by a Boolean bent-slice family.

## (c) Association: pointwise and averaged versions both fail

Already for n=3, truth table 0x13 has I_0=1/4, I_1=3/4, u({0,1})=1/8, and p({0,1})=1/16. Thus u({0,1})<I_0 I_1 on an actual spectral-support set.

There is no universal multiplicative correction depending only exponentially on |S|. For k>=0 start with a mux on x_0,x_1 selected by x_2, with k unused variables. Flip exactly the input whose bits are (0,1,0,0,...,0). Call this Boolean function F_k. For S={0,1}, the derivative in these two coordinates vanishes in the mux and has magnitude 1/2 after the flip exactly when x_2 and all marker bits are zero. Hence

    u(S)=2^(-k-3),  p(S)=2^(-2k-4),
    I_0=1/2-2^(-k-2),  I_1=1/2+2^(-k-2).

Their product tends to 1/4, so log2(I_0 I_1/u(S))=k+1+o(1), while |S|=2 throughout. This disproves u(S)>=2^(-C|S|) product_{i in S}I_i for every fixed C, even if only spectral-support sets are considered. Its individual spectral weight is tiny, so it does not refute an averaged correction or the A-conjecture.

The uncorrected averaged replacement fails as well. At n=3, truth table 0x19 has A=1.1832951340357143, whereas sum_i I_i log2(1/I_i)=1.1225562489182657, with influences (3/4,3/4,1/4). Substituting its coefficients gives the exact gap

    A - sum I_i log2(1/I_i) = (1/16) log2(3^22/(2^13*5^9)) > 0,

because 3^22=31,381,059,609 exceeds 2^13*5^9=16,000,000,000. These displays are also checked by exact-integer/high-precision computation in `routes.json`.

An averaged correction that always holds, even for arbitrary probability laws on subsets, is

    A <= sum_i I_i log2(1/I_i) + I/ln(2).

Indeed A<=H(p)<=sum_i h_2(I_i) by entropy subadditivity, and -(1-t)log2(1-t)<=t/ln(2). This is a valid replacement for the false uncorrected averaged bound, but the marginal logarithms remain uncontrolled by I.

There is also an exact chain rule. Order S as i_1,...,i_k and set S_j={i_1,...,i_j}. Wherever p(S)>0,

    u(S)=product_{j=1}^k [u(S_j)/u(S_{j-1})],
    A=E_S sum_j log2(1/Pr[i_j in U | S_{j-1} subset U]).

This is exact, but the conditional influences can be arbitrarily smaller than the marginal ones, as F_k shows. Their spectral average remains the missing bound. Even the hypothetical uncorrected marginal bound would leave the uncontrolled quantity sum I_i log(1/I_i).

Verdict (c): pointwise association, a fixed exponential correction, and the uncorrected averaged replacement are false; an additive I/ln(2) averaged correction and the conditional chain rule are valid but do not prove the conjecture.

## (d) The two-sample moment does not control A from above

For independent spectral samples S,U,

    Q=Pr[S subset U]=sum_S p(S)u(S)
      =E_U sum_{S subset U}p(S)
      =E_U ||E[f | x_U]||_2^2.

This follows by conditional expectation killing every Fourier character not contained in U. Jensen gives -log2(Q)<=A; its direction is a lower bound for A.

A reverse estimate A<=C log2(1/Q) is false even for balanced functions. Let h_k be the k-address function on k+2^k inputs, and mux between a fresh dictator y and h_k with a fresh selector z. There are four disjoint spectral branches from (y+h_k+zy-zh_k)/2. In particular p({y})=1/4 and u({y})=1/2, so Q>=1/8 for all k.

For the address function, each spectral set consists of one data coordinate and an arbitrary subset of the address coordinates. Each of its 2^(2k) nonzero coefficients has squared value 2^(-2k), and the spectral sample is uniform on those sets. Thus u(S)=2^(-k-|S_address|), A(h_k)=3k/2 and I(h_k)=1+k/2. The balanced heterogeneous composition law proved below gives for the mux family

    A=3/2+3k/4 -> infinity,     I=3/2+k/4.

In fact Q=(3/16)(1+(3/8)^k): the dictator branches contribute 3/16 and the h_k branches contribute (3/16)Q(h_k), with Q(h_k)=(3/8)^k. Thus Q remains bounded below while A grows. This kills the single-moment reverse-Jensen step, not all possible moment methods. The exact tail integral

    A=integral_{r>=0} Pr_{S~p}[u(S)<2^(-r)] dr

shows what is missing: a tail bound whose integral is O(I), rather than one averaged containment probability.

Verdict (d): the identity is valid; Jensen points the wrong way; a balanced mux-address family refutes a universal reverse estimate using Q alone.

## Balanced block composition

Let F=f(g_1,...,g_m), with disjoint blocks and all g_j balanced Boolean. Spectrally, sample T from p_f, and for every j in T sample a nonempty S_j from p_{g_j}. This description follows by expanding the outer Fourier series; balance ensures no inner empty coefficient and therefore makes the block pattern T unique. Squaring gives the product probabilities without cross terms.

For a fixed target set S, let T be the blocks it intersects. An independent sample contains S exactly when its outer sample contains T and, for every j in T, its inner sample contains S_j. The unmentioned blocks impose no condition. Therefore

    u_F(S)=u_f(T) product_{j in T}u_{g_j}(S_j).

Average its negative logarithm under the product spectral sampling rule:

    A(F)=A(f)+sum_j I_j(f) A(g_j),
    I(F)=sum_j I_j(f) I(g_j).

The outer function need not be balanced. For identical g_j=g this is the proposed law A(f composed with g)=A(f)+I(f)A(g). It does require balanced inner functions. For example composing two 2-input AND gates gives AND_4; A(AND_4)=31/32, whereas A(AND_2)+I(AND_2)A(AND_2)=2. Thus balance cannot be dropped.

If both f and g are balanced and have I>1, writing R(h)=A(h)/(I(h)-1) gives

    R(f composed with g)
      = [(I(f)-1)R(f)+I(f)(I(g)-1)R(g)]/[I(f)I(g)-1].

This is a convex combination. Different gates need not give a constant sequence. Self-composition of a fixed balanced gate does:

    I(f^[d])=I(f)^d,
    A(f^[d])=A(f)(I(f)^d-1)/(I(f)-1),
    R(f^[d])=R(f).

Hence iterating a fixed gate cannot produce a diverging balanced ratio. At I=1 a balanced Boolean function is a signed dictator: the degree average is one and the empty mass vanishes, so all Fourier mass is at degree one; squaring a real linear Boolean function forces only one nonzero coefficient. Its A is zero. Such inner gates leave the law unchanged, while an outer dictator passes through its selected inner gate; the quotient R of the dictator itself is undefined.

## Equality of the two universal optimal constants

Let C_A be sup A(f)/I(f) over all nonconstant Boolean functions and C_bal be sup A(f)/(I(f)-1) over balanced functions with I>1. They are equal, allowing +infinity.

First, for arbitrary nonconstant f, the balanced function y*f on a fresh coordinate has spectral sets {y} union S. Its upward probabilities on the support equal those of f. Thus A(y*f)=A(f), I(y*f)=I(f)+1, and C_bal>=C_A.

Conversely, self-compose a balanced f with I(f)>1. The composition formulas show

    A(f^[d])/I(f^[d])=R(f)(1-I(f)^(-d)) -> R(f).

Thus C_A>=C_bal. In particular the audited K3,3 coin value gives a lower bound for the constant in the A-conjecture, even though its own finite-gate A/I is smaller.

## Closed forms used as computational controls

For the AND gate which differs from the constant +1 only at one input, every nonempty coefficient has squared value 2^(2-2n). Thus u(S)=2^(2-n-|S|) for S nonempty, I=n*2^(1-n), and

    A/I = 3-4/n + 2^(1-n)(2-n)/n.

For address the formulas above give A/(I-1)=3 for all k>=1. For the paired bent quadratic on n=2r inputs, all squared coefficients equal 2^(-n), u(S)=2^(-|S|), A=I=n/2 and Q=(3/4)^n. All controls are tested from their truth tables.
