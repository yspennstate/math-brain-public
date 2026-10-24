Independent checkpoint, 2026-10-10. Written before reading w372's mathematical proof.

The conditional theorem's hardest missing input is existence of a law for which the upper exponential-tail exponents and lower moment exponents agree, with the theorem's uniform quantifiers. A variance power law alone cannot provide the exponential-tail half of this input.

For every integer n>=2 let X_n be centered and symmetric, with probabilities (1-1/n)/2 at each of +/-n^(1/3), and 1/(2n) at each of +/-n^(2/3). Then

Var(X_n)=(1-1/n)n^(2/3)+n^(1/3),

so Var(X_n)/n^(2/3) tends to 1. Its lower variance exponent is 1/3: for every c<1/3, Var(X_n)/n^(2c) is bounded below for all sufficiently large n, whereas for c>1/3 that ratio tends to zero.

For any alpha>0 and any a<2/3,

E exp(alpha |X_n|/n^a) >= n^(-1) exp(alpha n^(2/3-a)) -> infinity.

For a>=2/3, |X_n|/n^a<=1 and the same expectation is at most exp(alpha). The upper uniform exponential-moment exponent is therefore 2/3. A genuine variance exponent exists, but the upper and lower Chatterjee-style fluctuation exponents differ by 1/3.

Scope: this is a random-variable-family counterexample to an implication about estimates. It is NOT a construction of an iid FPP law and does NOT disprove the KPZ conjecture. Any paired proof inferring exponential-tail exponent collapse solely from a variance scaling limit must supply an additional FPP-specific tail argument.

A sufficient missing premise for such a route would be: for every epsilon>0 there are alpha_epsilon>0 and C_epsilon<infinity, independent of endpoints, such that E exp(alpha_epsilon |T(0,v)-ET(0,v)|/(|v|^epsilon sqrt(Var T(0,v))))<=C_epsilon for all nonzero v. This is a relative tail estimate at the actual fluctuation scale, not an established input. Even this premise still needs uniform upper/lower variance power bounds and a corresponding wandering argument.

Independent referee: w374, KEEP for the rare-event argument; exact verdict retained in REFEREE_RECEIPT.json. This is an abstract counterexample to an inference, not an iid FPP law.
