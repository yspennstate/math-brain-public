SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-23T02:56:57Z.
attacking: a product-preserving non-null scalar/dependent-pair curved-fiber kernel, and the exact boundary where joint pair-density information ceases to suffice.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN. Fresh controls were resolved at brain `main` `f44aba147602ade362205984416b49b725ad77fb`, OWNER CONTROL revision `2026-09-22.15`; no later B06 stop was present.

## Candidate positive lemma: physical chain weighted fiber

Let `X,Y,Z` be independent real random variables with probability densities at most one. After conditioning arbitrary outside ORIGINAL coordinates, suppose the surviving quadratic polynomial has quadratic block

```
B = [[a,b,0],
     [b,c,d],
     [0,d,0]]
```

with `a d != 0`; arbitrary linear terms are allowed. Then the proposed bound is

`||p_Q||_infinity <= 4 / sqrt(|a d|)`.

Reason: condition on the middle ORIGINAL coordinate `Y=y`. Complete the `X` square. Its conditional density is dominated by the one-sided kernel `(|a|u)^(-1/2)`. The affine `Z` term has density cap `K(y)=|2dy+ell_Z|^(-1)`. Convolving a probability density of cap `K` against `u^(-1/2)` costs at most `2 sqrt(K)`, not a fiber supremum. Thus

`||p_(Q|Y=y)||_infinity <= 2 |a|^(-1/2)|2dy+ell_Z|^(-1/2)`.

Now average with the actual `Y` density. The cap-one bathtub estimate

`sup_{f<=1, int f=1} int f(y)|y-y0|^(-1/2)dy = 2 sqrt(2)`

gives the claimed constant `4/sqrt(|ad|)`. This keeps the singular middle-fiber weight and pays it only after product averaging.

## Candidate falsifier to an over-strong interface

The preceding statement must NOT be weakened to “`X` independent of a pair `(Y,Z)` whose JOINT density is at most one.” Let

`B0=[[1,1,0],[1,0,1],[0,1,0]]`, `A=3 B0`.

The characteristic polynomial of `B0` is `lambda^3-lambda^2-2lambda+1`. On `|lambda|<=1/3` it is at least `5/27`, hence every eigenvalue of `A` has modulus `>1`.

For integer `N>=16`, let `X~Unif[0,1]`, independent of `(Y,Z)` uniform with density one on

`E_N={e^(-N)/N <= y <= 1/N, 0<=z<=1/(Ny)}`.

The area of `E_N` is one, so this is a joint cap-one probability density. Moreover the conditional density `p_(Z|Y=y)=Ny<=1`. But the middle marginal is `p_Y(y)=1/(Ny)`, which is unbounded with `N`.

For `q0=X^2+2XY+2YZ`, on `X<=1/(4 sqrt(N))` one has `0<=q0<3/N`. Hence for `Q=3q0`,

`P(0<=Q<=9/N) >= 1/(4 sqrt(N))`,

so any density bound for this weakened interface is at least `sqrt(N)/36 -> infinity`. This is not a QFORM counterexample because `Y,Z` are dependent; it is a source-valid obstruction to discarding the ORIGINAL product provenance.

## Partner/source splice

The designated partner account03/B06 r24 result at `math-open-problems@606257652f3c70e90c7b7f80ea7cb76c1abf689b` proves aggregate `e_2`/ridge `L^3` receivers and an outer-square transducer. Applied to the preceding crossed-star/tiny-tail family with singular values `(1,1,eps)`, its third-singular-value endpoint gives `<25/sqrt(|a|eps)`, hence is valid but nonuniform as `eps->0`; its aggregate `e_2` endpoint would be dimension-free, but the physical anchors have ordinary range leverage one and violate the required `q/2` gate. This identifies the exact chamber where the new product-chain averaging is relevant rather than merely citing the partner result.

The required Claude source package `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` was also read. Its physical-pair mechanism covers the independent-input version of the fixed matrix `A=3B0`; the dependent-pair construction above shows why that conclusion cannot be transferred using joint pair-density cap alone.
