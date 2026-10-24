# R11 / I0054 research idea before code — shuffled sticky Markov paintboxes

Model requested by owner: GPT-6 maximum. Actual runtime identifies as GPT-5.6 Sol; reasoning level is UNVERIFIED, so GPT-6 / maximum is not claimed.

Source target: Aldous--Janson, arXiv:2303.02529v3, Open Problem 18. Frozen metric entering this run: 77 author-side discrete model classes with a complete fixed-restriction/full-projective CTCS(infinity) limit proof.

Methods selected, nonrepeating from the prior #1/#13/#27 triple:

- #6 DEFORM TO A POINT YOU CAN SOLVE: interpolate the sticky Markov field from iid persistence eps=0 toward eps=1 and identify the actual boundary rather than the previous crude eps H_N condition.
- #12 FIND WHAT IS CONSERVED: compute the exact two-label separation rate; it exposes the averaged persistence invariant that any CTCS limit must kill.
- #29 ADD THE POINTS AT INFINITY: compactify the persistence scale by c_N=N(1-eps_N), with CTCS at c=infinity and a non-CTCS boundary visible for finite c.

## Idea A: sharpen the fixed-order C077 theorem

At grid bias x=j/N, the stationary binary Markov kernel is

K(a,b)=(1-eps) pi_x(b)+eps 1_{a=b}.

For visible positions r_1<...<r_m, write d_q=r_{q+1}-r_q and rho_q=eps^{d_q}. For any nonconstant oriented color pattern y, use its first color change. The stationary initial factor and that first change contribute exactly x(1-x)(1-rho_q). After dividing by x(1-x), every remaining transition factor lies in [0,1]. A telescoping product comparison with rho=0 therefore gives

|P_eps(y)-P_0(y)| <= x(1-x) sum_q rho_q <= (m-1) eps x(1-x).

Adding the complementary orientation doubles this. Since the harmonic-grid clock at x is 1/(2N x(1-x)), the singular x(1-x) denominator cancels. Hence a specified unordered split rate differs from the iid harmonic-grid rate by at most

(m-1) eps (N-1)/N.

Thus eps_N -> 0 already suffices for full fixed-restriction generator convergence. It is also necessary: for adjacent labels the exact pair split rate is

q_N(1|1)=((N-1)/N)(1-eps_N).

So the true fixed-order CTCS basin is eps_N -> 0; the preceding eps_N H_{N-1}->0 condition was only a crude sufficient bound.

## Idea B: randomize the ambient order and allow eps_N -> 1

At each harmonic-grid clock ring, independently draw a uniform permutation sigma of [N], then draw the stationary Markov chain Y_1,...,Y_N along the permuted positions, and color label l by Y_{sigma^{-1}(l)}. Use a fresh permutation/field at every ring and block.

For a fixed visible m-set, its positions form a uniform m-subset of [N]. Conditional on sorted positions s_1<...<s_m, the same pattern argument gives a quotient error bounded by sum eps^{s_{q+1}-s_q}. This adjacent-gap sum is at most the all-pairs sum. Define the exact mean pair persistence

A_N(eps) = 2/[N(N-1)] sum_{d=1}^{N-1} (N-d) eps^d.

Then

E sum_{q=1}^{m-1} eps^{s_{q+1}-s_q} <= binom(m,2) A_N(eps).

Therefore every specified m-label split rate differs from the iid harmonic-grid rate by at most

binom(m,2) A_N(eps) (N-1)/N.

For two labels there is equality in the diagnostic direction:

q_N(1|1)=((N-1)/N)(1-A_N(eps)).

Hence the shuffled model has the CTCS limit iff A_N(eps_N)->0. Moreover

A_N(eps) <= 2/[(N-1)(1-eps)],

while if N(1-eps_N) stays bounded along a subsequence then A_N is bounded away from zero by summing d<=N/2. Thus

A_N(eps_N)->0  iff  N(1-eps_N)->infinity.

This is much stronger than the fixed-order result: random shuffling permits eps_N -> 1 as long as the Markov correlation length o(N).

Concrete proposed class C078:

L_N=ceil(sqrt(N)), eps_N=1-1/L_N.

Then eps_N->1 but N(1-eps_N)=N/L_N->infinity, so every fixed restriction should converge in generator, path TV on compact intervals, J_1, and then in the frozen summable projective metric to CTCS(infinity).

At N=4, eps=1/2. Exact enumeration should be used only after this idea is committed. Preliminary hand derivation predicts exchangeable specified rates different from CTCS; the checker will certify the exact witness and pair formula.

## Boundary / compactification diagnostic

If N(1-eps_N)->c in [0,infinity), then the exact pair-persistence invariant has candidate limit

A(c)=2 integral_0^1 (1-s)e^{-cs} ds = 2(c-1+e^{-c})/c^2,

with A(0)=1. Thus the limiting pair split rate is 1-A(c), not 1 for finite c. CTCS is the c=infinity boundary point. This proves sharpness at the two-label level even before identifying the whole finite-c limiting fragmentation.

No code/checker has been written for this run before this idea file.