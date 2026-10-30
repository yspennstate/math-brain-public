# Heat-flow identity and a pointwise-envelope obstruction

All logarithms in this derivation are natural. Let f:{-1,1}^n->{-1,1}, a_S=hat f(S), p_S=a_S^2, d_S=|S|. Parseval gives sum p_S=1, I=sum d_S p_S, H_nat=sum p_S log(1/p_S). Zero-mass terms are zero.

## Exact semigroup and functional

Let L chi_S=d_S chi_S and T_t=exp(-t L); equivalently T_t is ordinary cube noise with correlation exp(-t). Thus hat(T_t f)(S)=exp(-t d_S)a_S. The evolving squared spectrum q_t(S)=exp(-2t d_S)p_S is **unnormalized**, with mass Z(t)=||T_t f||_2^2. No Booleanity of T_t f is asserted.

Write F(t)=sum q_t(S) log(1/q_t(S)), E(t)=sum d_S q_t(S), and define the initial-information functional

G_f(t)=F(t)-2t E(t)=sum p_S exp(-2t d_S) log(1/p_S).

This is a corrected entropy functional, not the Shannon entropy of the normalized evolving law. Direct finite-sum differentiation gives

J_f(t)=sum d_S p_S exp(-2t d_S) log(1/p_S)>=0,
G_f'(t)=-2J_f(t).

For comparison, F'(t)=-2J_f(t)-4t sum d_S^2 q_t(S)+2E(t), so the uncorrected derivative need not have a fixed sign. A dictator has F(t)=2t exp(-2t), which initially increases although its Fourier entropy is zero.

G_f(0)=H_nat(f) and G_f(infinity)=p_empty log(1/p_empty)=:b_f. Consequently

H_nat(f)=b_f+2 integral_0^infinity J_f(t) dt.                                      (1)

At every finite cutoff T, H_nat=b_f+2 integral_0^T J_f+R_f(T), where
R_f(T)=sum_{S nonempty}p_S exp(-2T d_S)log(1/p_S).
Thus 0<=R_f(T)<=exp(-2T)(H_nat-b_f), and also R_f(T)<=exp(-2T)J_f(0).

## Both endpoints, with quantifiers

For each fixed finite-dimensional f, J_f is a finite sum of smooth exponentials. At small times 0<=J_f(t)<=J_f(0)<infinity; in particular integral_0^epsilon J_f<=epsilon J_f(0). At large times J_f(t)<=exp(-2t)J_f(0), so integral_T^infinity J_f<=J_f(0)exp(-2T)/2. There is no small-time singularity for an individual f.

For a nonconstant Boolean sign with n>=1, every Walsh coefficient is an integer multiple of 2^(1-n): its numerator is a sum of 2^n signs and hence even. Any nonzero p_S is therefore at least 2^(2-2n). Consequently J_f(0)<=2(n-1)ln(2) I(f). This finite-dimension bound is not dimension independent. For n=0 or constant f, J=H=I=0. The n=1 bound is also correct: every Boolean sign on one bit has one spectral atom.

Since -u ln u<=1-u on [0,1] and 1-p_empty=sum_{S nonempty}p_S<=I, the boundary term satisfies 0<=b_f<=I. Hence a universal estimate

integral_0^infinity J_f(t) dt <= K I(f) for all Boolean f                         (OPEN)

would imply H_bits(f)<=((1+2K)/ln 2) I(f). Conversely FEI with constant C in bits implies integral J_f<=C ln(2) I(f)/2. Thus this is an equivalent unpaid universal target, up to the explicitly paid boundary term; (1) is not a proof of FEI.

## A stronger sufficient mechanism is impossible

Consider actual Boolean point defects f_n(x)=1-2 1_{x=(1,...,1)}, n>=2. Their coefficients are a_empty=1-2^(1-n), and a_S=-2^(1-n) for S nonempty. Thus p_S=2^(2-2n) off the empty set, I=n 2^(1-n), and the binomial degree identity gives

J_{f_n}(t)/I(f_n)=(2n-2)ln(2) exp(-2t) [(1+exp(-2t))/2]^(n-1).                   (2)

Suppose a nonnegative measurable k(t), independent of f and n, satisfies J_f(t)<=I(f)k(t) for all Boolean f and almost every t. It suffices to intersect the full-measure sets for the countable family f_n. For 0<t<=1/4 choose n=ceil(1/t). Since (1+exp(-2t))/2=exp(-t)cosh(t)>=exp(-t), 2n-2>=n, n>=1/t, and (n+1)t<=1+2t<=3/2, (2) implies

k(t)>=ln(2) exp(-3/2)/t for almost every 0<t<=1/4.

Therefore integral_0^(1/4) k(t) dt=infinity. In particular **no universal integrable pointwise influence envelope exists for J_f**. A finite prefactor C can be absorbed into k and does not evade the obstruction. This does not rule out the integrated target or other dissipation functionals.

The spike is integrable for each family member. Substitute r=exp(-2t) into (2) to obtain the exact area

(integral J_{f_n})/I(f_n)=2(1-1/n)(1-2^(-n))ln(2)<=2ln(2).                      (3)

Its height is of order n and its width of order 1/n. In particular H_bits(f_n)/I(f_n)->4; this is not a counterexample to FEI. The point-defect spectrum itself is a recovered seed control; the application here rules out a specific universal heat-flow envelope.

## Scope and next gap

The identity and endpoint proof only need a finite normalized spectrum and its degree statistic; they do not exploit full signed Boolean convolution constraints. On arbitrary normalized spectral vectors even the integrated target fails: put p_{ {i} }=1/n for i=1,...,n and all other masses zero. Then I=1 and integral J=(ln n)/2. These vectors are not assumed Boolean. Any future proof of the integrated target must use a genuine Boolean restriction, or equivalent structure, beyond normalization.

The next mathematical action is to seek an influence charging argument across dyadic time intervals with charges summable **for each function**, rather than summing a universal supremum separately at every time. Proving each interval has O(I) charge is insufficient because there may be arbitrarily many intervals. Independent reviewers: A070 and A088/A094.
