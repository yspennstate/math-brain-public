# A single global choice of output polarity does not repair the prime queue

Use ANY base pattern from PRIME_QUEUE_OBSTRUCTION.md: r=2^w, w>=4, clause widths w_j in {w,w+1}. Write U(X)=product_j OR(X_j) as an indicator, a=Pr(U=1), and take an independent copy Y with V(Y)=1-U(-Y)=OR_j AND(Y_j), b=1-a. Put F=2U(X)V(Y)-1. Here -Y denotes coordinate negation. Let I_0,H_0 be influence and Fourier entropy of the sign function 2U-1. Its clone 2V-1 has the same squared spectrum up to coordinate signs, I and H.

Both base truth probabilities are bounded away from zero: a>1/4 and b>1/3. Independence and physical pivotal counting give

    I(F)=b I_0+a I_0=I_0.                            (1)

## Positive prime queue for F

Every positive prime is a product of a U-positive transversal (one X variable per clause) and one V-positive complete AND clause in Y. Completeness follows from disjoint inputs: an implicant of the product must force both factors. Minimality then forces each factor's minimal certificate. Such primes have width r+w_j>=r, actual rarity at most pi0=2^-r.

For a target A contained in one X clause, every prime contains at most one coordinate of A. Each component's activity is at most pi0 by its ORIGINAL physical packing row, regardless of the nonuniform chosen weights. Thus exactly the base root-cost lower bound applies. On these targets the ACTUAL squared Fourier coefficients of F are b^2 times those of the sign base 2U-1. Its positive-prime queue therefore satisfies

    C_+(F)/I(F)>b^2 r/7>r/63.                        (2)

Only one-block targets from X are used in this lower bound; all other spectral sectors have nonnegative cost.

## Positive prime queue for -F (the negative prime table of F)

The complement event is (U=0) OR (V=0). The COMPLETE positive prime table of -F is the disjoint union of X-zero full clauses (width w_j) and Y-zero transversals (width r). An OR on disjoint inputs has no mixed minimal certificate: if neither factor is forced, independent assignments make both false.

For A contained in one Y clause, only the Y-transversal primes meet A, each in at most one coordinate, with rarity pi0. The cheaper X-clause gates are DISJOINT from A; a successful exact-A run cannot visit them, and the full original denominator D is still retained. They cannot bridge the target components. Packing again gives component activity<=pi0. The squared Fourier coefficients of F (and hence -F) on those targets are a^2 times the base coefficients. Consequently

    C_-(-F)/I(F)>a^2 r/7>r/112.                      (3)

These inequalities hold for EVERY feasible positive reference and EVERY fixed ordered cover in each orientation, even if they are optimized independently. Thus choosing ONE global output polarity before observing a Fourier set still cannot give a dimension-independent prime-queue payment. The corresponding conditioned forest residuals are at least their full queue costs minus K_ref I.

## Scope and true entropy

Product Fourier sectors give

    H(F)=H(sector)+b[H_0-h2(v_0)]+a[H_0-h2(v_0)]
        <=2+H_0<8I(F),

using the independently proved H_0<6I_0 and I_0>1. Also 3/16<Pr(F=1)=a(1-a)<=1/4, so Var(F)>39/64. This is an actual nondegenerate Boolean family with bounded H/I and unbounded reference cost in BOTH global orientations, not an FEI disproof.

This does NOT refute a SINGLE FIXED normalized mixture of the two polarity queues whose output mass is summed before logarithms, or nonprime regular gates. Different spectral sectors may use different components of that mixture, paying its reference label. Such a mixture is not the same as choosing one global output polarity, nor a free post-observation reference reset. The shortest next action is to test that actual mixed output law with its original weights, label cost, denominator and output ambiguity all retained.
