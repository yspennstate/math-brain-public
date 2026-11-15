# A sharp Gaussian-mixture risk reduction for a four-ReLU family

This result is a reduction for a restricted nonlinear family. It makes no assertion that unconstrained gradient descent reaches that family. No matching sample-size rate for gradient descent is proved here.

## 1. Model and exact risk

Let d >= 2. Let Y be uniform on {-1,+1}, let Z have law N(0,Sigma), independently of Y, and set X = Y mu + Z. Assume Sigma is positive definite. Write

    Q(t) = (2 pi)^(-1/2) integral_t^infinity exp(-s^2/2) ds.

Classify by the sign of a real score and write R(f) = P(Y f(X) < 0). In all the scores below the probability of a zero score is zero, so the rule at zero is immaterial.

For u,v in R^d with u+v and u-v both nonzero, define

    f_{u,v}(x) = u^T x + |v^T x|,
    rho_+ = (u+v)^T mu / sqrt((u+v)^T Sigma (u+v)),
    rho_- = (u-v)^T mu / sqrt((u-v)^T Sigma (u-v)).

**Theorem 1.** This is a bias-free two-layer ReLU score of width four, and

    R(f_{u,v}) = [Q(rho_+) + Q(rho_-)] / 2.                 (1)

The identity holds with any signs of rho_+ and rho_-. If u and v depend measurably on a training sample independent of the test point, (1) holds conditionally on that sample whenever the two nondegeneracy conditions hold.

**Proof.** For sigma(t)=max(t,0), the identities sigma(t)-sigma(-t)=t and sigma(t)+sigma(-t)=|t| give

    f_{u,v}(x) = sigma(u^T x)-sigma(-u^T x)
                +sigma(v^T x)+sigma(-v^T x).

Put T=mu+Z, L=u^T T and H=v^T T. Conditional on Y=+1, an error is L+|H|<0. Conditional on Y=-1, symmetry of Z allows X to be replaced in distribution by -T. An error is then

    f_{u,v}(-T)>0,

or -L+|H|>0, equivalently L-|H|<0. Thus

    R(f_{u,v}) = [P(L+|H|<0)+P(L-|H|<0)]/2.              (2)

For every pair of real numbers L,H, the unordered pair {L+|H|,L-|H|} equals {L+H,L-H}. Consequently the sum of the two event indicators in (2) equals the sum of the indicators of L+H<0 and L-H<0. Each of (u+v)^T T and (u-v)^T T is a nondegenerate Gaussian. Standardizing their means and variances proves (1). The zero set of f is contained in the union of their two zero hyperplanes, hence has probability zero. Conditioning on the training sample gives the last assertion. QED.

The same symmetry calculation applies to an arbitrary score f(x)=l(x)+e(x), where l is odd and e is even, provided ties have probability zero:

    R(f) = [P(l(T)+e(T)<0)+P(l(T)-e(T)<0)]/2.            (3)

For any bias-free two-layer ReLU score sum_j a_j sigma(w_j^T x), the odd and even components are exactly

    l(x) = (1/2)(sum_j a_j w_j)^T x,
    e(x) = (1/2)sum_j a_j |w_j^T x|.                    (4)

Equation (1) uses the special single-absolute-value form. It does not turn the general even sum in (4) into a Gaussian random variable.

## 2. The precision required for constant-factor Gaussian tails

Let phi(t)=(2 pi)^(-1/2) exp(-t^2/2).

**Lemma 2.** For a >= b >= 1,

    exp((a^2-b^2)/2)
       <= Q(b)/Q(a)
       <= (a/b) exp((a^2-b^2)/2).                      (5)

In particular, for sequences a,b >= 1, the ratio Q(a)/Q(b) stays bounded above and below by positive constants if and only if |a^2-b^2| stays bounded.

**Proof.** For t>0, since s/t >= 1 when s>=t,

    Q(t) <= (1/t) integral_t^infinity s phi(s) ds
         = phi(t)/t.

Integration by parts, using phi'(s)=-s phi(s), gives

    Q(t) = phi(t)/t - integral_t^infinity phi(s)/s^2 ds
         >= phi(t)/t - Q(t)/t^2.

Rearrangement yields Q(t)>=t phi(t)/(1+t^2). Hence the Gaussian hazard h(t)=phi(t)/Q(t) satisfies

    t <= h(t) <= t+1/t.

Because -(log Q)'=h, integrating from b to a gives

    (a^2-b^2)/2 <= log[Q(b)/Q(a)]
               <= (a^2-b^2)/2 + log(a/b),

which proves (5). If D=a^2-b^2 is bounded and b>=1, then a/b=sqrt(1+D/b^2)<=sqrt(1+D); (5) bounds the ratio. Conversely, a bounded ratio in (5) bounds D. For unordered a,b apply the argument to their minimum and maximum. QED.

For example, Q(c t)/Q(t) diverges for every fixed 0<c<1 as t tends to infinity. A constant factor in a tail argument is therefore not a constant factor in the resulting error.

**Corollary 3 (a conditional target for a training analysis).** Let u=u_{n,d}(S), v=v_{n,d}(S) be training-sample-dependent vectors in Theorem 1. Let q=q_{n,d}>=1 be a proposed effective-margin scale. On any event in S on which rho_+,rho_- >= 1, put

    m = min(rho_+,rho_-).

Along any sequence of such samples, dimensions and sample sizes,

    R(f_{u,v}) is comparable to Q(q) by uniform constants

if and only if

    |m^2-q^2| is uniformly bounded.                    (6)

**Proof.** The function Q is decreasing, so (1) gives

    Q(m)/2 <= R(f_{u,v}) <= Q(m).

Apply Lemma 2 to m and q. More explicitly, if |m^2-q^2|<=C, set K=exp(C/2)sqrt(1+C). Then

    1/(2K) <= R(f_{u,v})/Q(q) <= K.

Conversely, uniform upper and lower bounds on R(f_{u,v})/Q(q) give uniform bounds on Q(m)/Q(q); Lemma 2 then gives (6). QED.

This is a pathwise equivalence. It becomes a high-probability statement if a training theorem establishes its hypotheses on an event of specified probability. It does not automatically give an expectation bound over the training sample: the complement of that event must also be controlled at the scale Q(q).

## 3. An exact obstruction to controlling only the odd component

Take Sigma=I_d, mu=r e_1 with r>0, u=e_1 and v=b e_2 with b>=0. Then

    f_b(x)=x_1+b|x_2|,
    R(f_b)=Q(r/sqrt(1+b^2)).                            (7)

The Bayes classifier is sign(x_1) and its risk is Q(r). Indeed the log ratio of the two conditional Gaussian densities at x equals 2r x_1. Also Y X_1=r+Y Z_1 has law N(r,1), giving its error Q(r).

The odd component of f_b is exactly x_1 for every b. Its even component is b|x_2|, with

    E[e(X)^2]=b^2,                                     (8)

since X_2 is a standard normal independent of Y.

**Theorem 4 (sharp contamination threshold).** As r tends to infinity, allowing b=b(r),

    R(f_b)/Q(r) stays bounded

if and only if r b stays bounded. If r b tends to a finite c>=0, then

    R(f_b)/Q(r) -> exp(c^2/2).                          (9)

In contrast, b=r^(-1/2) gives E[e(X)^2]=1/r -> 0 but R(f_b)/Q(r) -> infinity, even though the odd component equals the Bayes score.

**Proof.** Formula (7) follows from (1), since both effective margins equal

    t=r/sqrt(1+b^2).

Alternatively, conditional on Y, write Y f_b(X)=r+Y Z_1+Y b|Z_2|. The pair (Y Z_1,Y|Z_2|) consists of independent standard normals: conditional on Y, the first coordinate has the same standard normal law, while the balanced independent sign Y converts |Z_2| to a standard normal. Thus the signed score has law N(r,1+b^2), proving (7) independently.

Put

    D=r^2-t^2=r^2 b^2/(1+b^2).                          (10)

If r b is bounded, then b tends to zero, t tends to infinity and D is bounded. Lemma 2 bounds the risk ratio. Conversely, if the risk ratio is bounded, Q(t)<=C Q(r) tends to zero, so t tends to infinity. Lemma 2 implies D is bounded. For sufficiently large r with r^2>2D, equation (10) implies

    b^2=D/(r^2-D) <= 2D/r^2.

Thus r b is bounded, proving the equivalence.

If r b -> c, then b->0, D->c^2 and log(r/t)=log(1+b^2)/2->0. Applying (5) with a=r and b there replaced by t gives

    D/2 <= log[R(f_b)/Q(r)] <= D/2+log(r/t).

The two endpoints tend to c^2/2, proving (9). Finally, if b=r^(-1/2), equation (10) gives D=r^2/(r+1), which tends to infinity, while t tends to infinity. The lower bound in (5) gives a risk ratio at least exp(r^2/[2(r+1)]). Equation (8) gives the stated vanishing second moment. QED.

The counterexample is a family of functions, not an exhibited gradient-descent trajectory or an interpolating training construction. It rules out the implication from those two function-level controls alone. Extra restrictions imposed by gradient descent could rule out this family.

## 4. Transferring the reduction to an approximate representation

If a trained classifier F and a score f_{u,v} disagree in their predicted signs on test mass at most delta, their error indicators differ only on that set. Therefore

    |R(F)-R(f_{u,v})| <= delta.                         (11)

Consequently, if c Q(q)<=R(f_{u,v})<=C Q(q) and delta<=eta Q(q) for 0<=eta<c, then

    (c-eta)Q(q) <= R(F) <= (C+eta)Q(q).

This proves a sufficient route from a training analysis to a constant-factor test-error bound: identify the relevant margins to bounded additive error in their squares, and control approximation disagreements at the target error scale. Equation (11) is sufficient, not a claim that every successful analysis must take this route. Neither training assertion is supplied here.
