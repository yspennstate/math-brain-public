# Exact product spectra of Boolean projections defeat a componentwise payment

Date: 2026-09-30. Full FEI remains OPEN. This is a counterexample to a proposed component inequality, not to FEI and not to the collective target in REPORT.md Section 5.

## Rejected claim

There is no universal finite C such that every nonzero partial Fourier projection g of a genuine Boolean function satisfies

    H(ghat^2/||g||_2^2)
      <= C[I(g)/||g||_2^2 + log2(1/||g||_2^2)]                (1)

even when |g|<=1 and its normalized squared Fourier law is exactly a product law. Adding any multiple of its total correlation does not rescue (1), since that correlation is zero. Replacing the logarithm by the smaller quantity `log2(||g||_infinity^2/||g||_2^2)` also fails.

The examples below are exact dyadic functions and are exact conditional means of Boolean functions. There is no approximation or irrational-coefficient escape at the unnormalized projection level.

## 1. Product weights with a bounded real sign realization

Let M>=2 be an integer, n=M^4, and Z=(M^2+1)^n. For each S subset [n], choose a sign sigma_S independently and uniformly, and define a normalized Fourier polynomial b by

    bhat(S)=sigma_S M^(n-|S|)/sqrt(Z).

Its squared Fourier law is precisely the product law with every inclusion probability

    q=1/(M^2+1).

Thus, for every sign choice,

    ||b||_2^2=1,
    I(b)=nq,
    H(bhat^2)=n h2(q),
    TC(bhat^2)=0.                                             (2)

There is a sign choice for which

    ||b||_infinity<=t:=sqrt(2(n+2)ln2).                       (3)

Indeed, for each fixed physical input x, b(x) is a sum of independent random signs with squared coefficient sum one. The elementary exponential-moment estimate `cosh u<=exp(u^2/2)` and Markov's inequality give

    Pr_sigma[|b(x)|>t]<=2 exp(-t^2/2).

A union bound over all 2^n physical inputs yields a failure probability at most

    2^(n+1) exp(-(n+2)ln2)=1/2.

Therefore a sign choice satisfying (3) exists. This is a finite probabilistic existence proof; the signs do not need to be efficiently found for the theorem.

## 2. Make the polynomial exactly dyadic and bounded by one

Let K be the smallest integer such that

    4^K>=Z t^2,

and set

    ghat(S)=2^(-K) sigma_S M^(n-|S|).

Write

    w=||g||_2^2=Z/4^K.

By minimality of K,

    1/(4t^2)<w<=1/t^2,
    |g(x)|=sqrt(w)|b(x)|<=1,
    log2(1/w)<log2(4t^2).                                    (4)

Every coefficient and every physical value of g belongs to `2^(-K) Z`. Scaling does not change the normalized spectral law, so

    H(ghat^2/w)=n h2(q),
    I(g)/w=nq,
    TC(ghat^2/w)=0.                                           (5)

## 3. g is an actual Boolean conditional mean

For every physical x, write `g(x)=m_x/2^K`, with integer `-2^K<=m_x<=2^K`. Introduce a fresh block y of K+1 bits, identified with integers in `{0,...,2^(K+1)-1}`, and define

    f(y,x)=+1 if y<2^K+m_x,
           -1 otherwise.

This is a genuine Boolean function on a finite uniform cube. For every x,

    E_y f(y,x)
      =[2(2^K+m_x)-2^(K+1)]/2^(K+1)
      =m_x/2^K=g(x).                                         (6)

Thus g is exactly the empty-label partial Walsh projection of f on the y block, and w is precisely the probability of that spectral address. Its normalized squared Fourier law is an exact product with rare, non-dyadic marginals. This does not contradict Boolean product rigidity, because the projected function itself is not Boolean.

## 4. Divergence of the proposed ratio

Since n=M^4 and q=1/(M^2+1),

    nq~M^2,
    n h2(q)~M^2[2log2 M+log2 e],
    log2(4t^2)=O(log M).

Equations (4)–(5) give the explicit lower bound

    H(ghat^2/w)/[I(g)/w+log2(1/w)]
       >= n h2(q)/[nq+log2(4t^2)] -> infinity.                (7)

This proves every rejected quantifier in (1).

## 5. What survives for the full FEI task

The full projection family of f still satisfies the pointwise all-shift Boolean identities

    sum_T g_T(x)g_(T triangle U)(x)=1_{U=empty}.

The other projections, their influence, and the entropy of the entire spectral address law have not been bounded here. The construction therefore does not refute a collective estimate that keeps those resources. It proves that boundedness, dyadic arithmetic, exact conditional-product structure and the single component's logarithmic normalization cost are insufficient on their own.

No publication-priority claim is made. Finite checks of the M=2 realization and numerical asymptotic lower bounds are regression evidence; the all-dimensional proof is (2)–(7).
