# Paying for data-coordinate erasure with selector influence

Status: a proved restricted structural lemma, self-checked; novelty UNVERIFIED. This is a response to the addressing obstruction, not a proof of full FEI.

## 1. Statement

Partition the input bits into selector bits x and data bits y=(y_1,...,y_k). Suppose f is Boolean and has degree at most one in the data variables:

    f(x,y)=u(x)+sum_{a=1}^k v_a(x)y_a.                 (1)

Let X,Y be the selector and data parts of a random Fourier subset of f. Write

    B_y(f)=sum_a H(Y_a | X,Y_{-a}),
    I_x(f)=sum_{i in selector bits} Inf_i(f).

Then

    B_y(f) <= H(J) <= 2 I_x(f),                       (2)

where J is the input-side label indicating whether f uses its constant branch or which data bit it uses. The proof defines J precisely. This pays for arbitrarily many individually tiny data influences using actual selector variation.

It does NOT bound B_x, and it assumes no data interactions of degree two or higher. Neither issue can be discarded in a full FEI proof.

## 2. Booleanity gives a genuine partition

Fix x and expand f(x,y)^2=1 in the data characters. The constant coefficient gives u^2+sum_a v_a^2=1. Singleton coefficients give u v_a=0; two-element coefficients give v_a v_b=0 for a!=b. Thus exactly one of u,v_1,...,v_k is nonzero, and it equals +1 or -1.

Define J(x)=0 on the support of u and J(x)=a on the support of v_a. Let A_j={x:J(x)=j} and delta_j=Pr(A_j). These sets form a partition; empty cells cause no difficulty. Let sigma(x) be the sign of the unique nonzero coefficient. Thus f(x,y)=sigma(x) when J=0 and sigma(x)y_J otherwise.

Parseval applied in the x variables shows

    Pr(Y=empty)=sum_S uhat(S)^2=E u^2=delta_0,
    Pr(Y={a})=sum_S vhat_a(S)^2=E v_a^2=delta_a.

There are no other spectral data subsets, so H(Y)=H(J). The conditional chain rule and monotonicity under further conditioning give

    sum_a H(Y_a|X,Y_{-a})
      <= sum_a H(Y_a|X,Y_1,...,Y_{a-1})
      = H(Y|X) <= H(Y)=H(J).                          (3)

This uses the actual signed-Boolean partition structure, not a convex relaxation of arbitrary squared spectra.

## 3. Elementary edge-isoperimetric inequality, with proof

For any set A in an m-dimensional cube with density delta, let

    b(A)=sum_i Pr_x[1_A(x)!=1_A(x flipped at i)].

We claim

    b(A)>=2 delta log_2(1/delta).                     (4)

Use induction on m. Dimension zero is immediate. Split by the last coordinate into densities a,b in dimension m-1. The old-coordinate boundary is at least a log(1/a)+b log(1/b) by induction, and the last-coordinate boundary is at least |a-b|, since the normalized symmetric difference of the two sections is at least their density difference.

Put delta=(a+b)/2. If delta=0 there is nothing to prove. For r=a/(a+b), the sum of these lower bounds is

    2 delta log(1/delta)
      +2 delta [h_2(r)-1+|2r-1|].

Binary entropy is concave and lies above the tent joining (0,0),(1/2,1),(1,0); equivalently h_2(r)>=1-|2r-1|. Concavity follows from h_2''(r)=-1/[ln(2)r(1-r)]<0 in the interior, with continuous endpoints. The bracket is nonnegative, completing the induction. This proves (4) including delta=1.

Apply (4) to every A_j. For a fixed direction i, let eta_i=Pr[J(x)!=J(x flipped at i)]. At an edge where the labels differ, exactly two of the membership indicators change. Thus

    sum_j b(A_j)=2 sum_i eta_i,
    H(J)=sum_j delta_j log(1/delta_j)
        <= (1/2)sum_j b(A_j)=sum_i eta_i.             (5)

## 4. Label variation has a real influence cost

Fix x,x' differing in selector coordinate i. If J(x)!=J(x'), the Boolean outputs f(x,y), f(x',y) differ with probability exactly 1/2 over uniform y. This holds both for constant versus signed data bit, and for two distinct signed data bits. Signs do not change that probability. If the labels agree, the disagreement probability is zero or one; it is never negative. Therefore

    Inf_i(f)>=eta_i/2.

Sum over selector coordinates and combine with (3)-(5) to obtain (2). QED.

For the family in `ADDRESSING_BARRIER_2026-09-18.md`, take (z,x) as selector bits. The label law has probabilities 1/2 and N entries 1/(2N), so

    H(J)=1+m/2,
    B_y=[(N+1)log(N+1)-N log N]/2 <= H(J),
    I_x=(m+1)/2.

The original logarithmic data cost is controlled despite every positive-power majorant diverging relative to total influence.

## 5. Why this does not yet extend to arbitrary f

For arbitrary f the data Fourier expansion includes v_D(x) chi_D(y) for |D|>=2. Booleanity no longer forces the coefficients v_D(x) to occupy disjoint supports: many may be simultaneously nonzero. The label partition J used in (3)-(5) need not exist. Merely dropping the degree-one hypothesis would invalidate the proof, not prove the conjecture.

Taking just one data variable always satisfies the hypothesis, but then (2) only says B_i<=2 sum_{j!=i}Inf_j. Summing that inequality repeats the same influence budget n-1 times, producing a dimension factor. It is not a universal aggregate payment.

The selector contribution B_x is also unresolved by this lemma. Taking no data variables embeds an arbitrary Boolean function on x, so any claimed automatic control of B_x would already require the original universal inequality. The argument must not be advertised as a proof for all functions affine in some chosen subset.

A possible next direction is to preserve a multiscale version of the input-side partition or an equally concrete signed structure, while proving a non-reuse rule for selector influence. Precisely what is missing is such a rule for overlapping higher-degree data spectra. Calling it a partition, charging scheme, or scale allocation without constructing and proving it does not fill the gap.

## 6. A tempting universal input label also fails

One cannot simply replace J by the local sensitivity pattern D_f(x)={i:f(x)!=f(x flipped at i)} and assert H(D_f)<=C I(f). Here is an exact obstruction to that speculative extension.

Let n>=2, N=2^n, and let f be -1 at the zero vertex and +1 elsewhere. Its sensitivity pattern is all n coordinates at zero, the singleton {i} at the i-th neighbor of zero, and the empty set elsewhere. These n+1 nonempty patterns are distinct, each with probability 1/N. Every coordinate has influence 2/N, so

    I(f)=2n/N,
    H(D_f)=h(1-(n+1)/N)+(n+1)n/N,
    H(D_f)/I(f)>=(n+1)/2.

Here h(t)=-t log_2(t)>=0 on [0,1], with h(0)=0. Thus no finite C works for this label entropy. The argument is an all-n proof, not a numerical search. This does not contradict (2): the sensitivity-pattern label is not the degree-one data selector partition used in its proof.

It is again not an FEI counterexample. The Fourier probabilities of this f are (1-2/N)^2 at the empty set and 4/N^2 elsewhere. Since -(1-u)ln(1-u)<=u for 0<=u<1 (integrate 1/(1-t)<=1/(1-u) on [0,u]), its spectral entropy satisfies

    H(f)<=4/[N ln2]+8n/N,
    H(f)/I(f)<=4+2/[n ln2].

The exact constant is unimportant here: input-label entropy can overcount by an unbounded factor even when the relevant Fourier entropy has a uniform bound.
