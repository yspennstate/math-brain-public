# P0162 sharp-boundary attempt — 10 October 2026

## Exact target and scope

For every dimension n and Boolean f:{-1,1}^n -> {-1,1}, does a dimension-independent K exist with H(f) <= K I(f)? Here Fourier weights are squared Walsh coefficients, H is their base-2 Shannon entropy with 0 log(1/0)=0, and I is the sum of bit-flip probabilities. Primary research sources: Han, *Combinatorica* 45:4 (2025), Conjecture 1.1; González–MacManus–Pereyra, arXiv:2606.00246v2 (2026), introduction. No proof of this target is claimed here.

## Independent reproduction of w511's stronger-bridge obstruction

w511 saved the same bent plus one-point-flip family before this referee read the paired proof. The calculation below is my independent reproduction for review; authorship of this lane belongs to w511, and no novelty is claimed.

González–MacManus–Pereyra (2026), introduction equation (3), propose as a sufficient bound for a selected restriction coordinate t:

    sum_S |hat(f^+)(S)^2 - hat(f^-)(S)^2|
        <= K sum_S (hat(f^+)(S) - hat(f^-)(S))^2.

The paper needs a suitable coordinate; the following disproves the stronger demand that this hold with universal K for *every prescribed* coordinate. It leaves the existential-coordinate ansatz and FEI untouched.

Let m=2r>=2, N=2^m, x in F_2^m, and g(x)=(-1)^(sum_{j=1}^r x_{2j-1}x_{2j}). Let h equal g except h(0)=-g(0)=-1. Define the Boolean f(x,t) by f(x,+1)=g(x), f(x,-1)=h(x). For the split t, write a_S=hat g(S), b_S=hat h(S). The Walsh transform of (-1)^(uv) has all four coefficient magnitudes 1/2, so tensoring pairs gives a_S in {+1/sqrt(N),-1/sqrt(N)}. Since g(0)=sum_S a_S=1, the counts P,Q of positive and negative a_S satisfy P-Q=sqrt(N). The one-point flip at 0 gives b_S=a_S-2/N for every S.

Hence sum_S(a_S-b_S)^2=N(2/N)^2=4/N. Also, since 2/N <= 2/sqrt(N), the positive-a terms in sum_S |a_S^2-b_S^2| are 4/(N sqrt(N))-4/N^2 and negative-a terms are 4/(N sqrt(N))+4/N^2. Adding P and Q yields 4(N-1)/N^(3/2). The ratio of the two sides before K is (N-1)/sqrt(N), which diverges as m grows. The coordinate influence I_t(f)=1/N, consistent with the denominator 4 I_t(f).

This is a counterexample to an all-coordinate coefficientwise proxy. The FEI entropy gap for this f and other coordinate choices have not been analyzed. The hardest open piece remains finding a dimension-free bound for at least one suitable split, or another route to universal FEI. The construction uses a bent function as a device; it is not presented as a new theorem about plateaued FEI constants.

Independent next-triad audit of any distinct new referee lemma would go to w515. This reproduction is a review of w511, not a distinct new lemma. No current novelty claim.
