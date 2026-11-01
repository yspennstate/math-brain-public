# Independent obstruction: an arbitrary splitting coordinate fails

2026-10-10. Derived and saved before reading w513's proof. Author proof only; independent referee w515 must check it. Entropies in this file use log base 2.

For every even n=2m>=4, define

g(x)=product_{j=1}^m (1+x_{2j-1}+x_{2j}-x_{2j-1}x_{2j})/2,
y=(1,...,1), delta_y(x)=1{x=y}, h=g-2delta_y,
F(x,t)=g(x)-(1-t)delta_y(x), t in {-1,1}.

Each pair factor has values +/-1, g(y)=1, and h just reverses g at y. Therefore g,h,F are Boolean. F's restrictions at t=+1 and -1 are g and h. Let r=2^{-m}, p=r^2=2^{-n}.

Claim C002: I_t(F)=p and

Delta_t(F):=H(F)-(H(g)+H(h))/2 >= n p.

Consequently, there is no finite universal K for which Delta_i(f)<=K I_i(f) holds for every Boolean f AND EVERY coordinate i. This says nothing against a bound with an existential choice of i depending on f.

Proof. Every Fourier coefficient of g is +/-r: this follows by multiplying the disjoint pair expansions, whose four coefficients are 1/2,1/2,1/2,-1/2. Write a_S=sigma_S r. Since g(y)=sum_S a_S=1, the fractions of plus and minus signs are (1+r)/2 and (1-r)/2. The coefficients of h are a_S-2p. The coefficients of F without t are a_S-p, and with t are p. Thus I_t(F)=2^n p^2=p, including the empty x-subset in that sum.

Define phi(z)=z^2 log_2(z^2) for z>0 and
L(u)=((1+r)/2)phi(1-u r)+((1-r)/2)phi(1+u r), 0<=u<=2.

The squared Fourier norm of g-u delta_y is 1+(u^2-2u)p, so its unnormalized spectral entropy is
E(u)=n[1+(u^2-2u)p]-L(u).
In particular H(g)=n, H(h)=n-L(2). The t-containing coefficients of F contribute 2np entropy, and its other coefficients contribute E(1). Hence

H(F)=n(1+p)-L(1),
Delta_t(F)=np+L(2)/2-L(1).

For n>=4, r<=1/4, and 1+/-ur lies in [1/2,3/2] on u in [0,2]. We have phi''(z)=(4 ln z+6)/ln 2 >= (6-4 ln 2)/ln 2 >0 on this interval. Thus L is convex, L(0)=0, and L(1)<=L(2)/2. This proves the bound. For any proposed finite K choose an even n>K.

Boundary checks: n>=4 is part of the claim; no derivative is taken at zero. The target has n+1 variables; n counts only the bent core. No independence is assumed except the expressly disjoint pair factors used to calculate g's Fourier coefficients. The construction is nonmonotone. The one-point indicator is unnormalized. The proof concerns the actual entropy increment, rather than only the stronger spectral L1 surrogate.

Remaining hard bridge: find a dimension-free entropy increment bound for AT LEAST ONE relevant coordinate of EVERY nonconstant Boolean f, with a family closed under the ensuing restrictions, or find a different global entropy argument. Neither this construction nor a flat-spectrum special case supplies that bridge.

Claim C003: the same F satisfies the global FEI bound H(F)<=2 I(F). In particular C002 is not a counterexample to FEI. Each core coordinate has influence 1/2 in g. The point y and each of its core-coordinate neighbors all have value +1 in g, so reversing y adds 2p to each influence in h. Averaging the two branches gives I_i(F)=1/2+p for every core coordinate, and I(F)=n/2+(n+1)p. In the spectral law of F, membership of t has probability p. Conditional on that membership, the residual subset has at most 2^n possible values. The entropy chain rule gives H(F)<=n+h_2(p). Since p=2^{-n}, h_2(p)<=np+p/ln(2)<(n+2)p<=2(n+1)p. Thus H(F)<=n+2(n+1)p=2 I(F). The scalar bound follows from -(1-p)ln(1-p)<=p, including the standard endpoint convention.

Related primary source: https://arxiv.org/html/2606.00246v2, Sections 1 and 4.2. Its induction ansatz uses an existential splitting coordinate. Section 5.1 gives a different obstruction for the stronger L1 surrogate. No novelty claim is made for C002.
