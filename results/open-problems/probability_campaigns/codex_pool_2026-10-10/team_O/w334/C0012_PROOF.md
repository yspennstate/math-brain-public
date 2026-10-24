C0012: two invalid steps in the resistance route
Label: proofs and explicit counterexamples to generic implications. These do not disprove the DGFF conjecture. Blind audit pending.

For a finite undirected conductance network killed on boundary A, let mu(x) be the total incident conductance, let tau_A be the first boundary hit by the discrete-time walk, and put v(x)=P_x(T_o<tau_A), with v(o)=1. The exact identity is
E_o tau_A = R_eff(o,A) sum_(x outside A) mu(x) v(x).
To see this, solve the unit-current potential with boundary zero. Its value at o is R_eff(o,A) and, by harmonicity and uniqueness, its value at x is R_eff(o,A)v(x). The expected number of visits to x divided by mu(x) is this same Green potential. Summing the visit counts gives the identity. In particular E_o tau_A <= R_eff(o,A) mu(B); a uniform lower bound by a fixed positive multiple of R_eff(o,A)mu(B) requires additional control of the volume-weighted potential v.

Explicit counterexample. Use B={o,x}, boundary {a}, and undirected conductances c_(o,a)=1, c_(o,x)=1, c_(x,a)=M>0. Then mu(o)=2, mu(x)=M+1, R_eff=(M+1)/(2M+1), and v(x)=1/(M+1). Therefore
E_o tau_A = 3 R_eff,
E_o tau_A/[R_eff mu(B)] = 3/(M+3) -> 0.
The claimed generic positive lower comparison fails on a reversible finite network. A DGFF-specific comparison could still hold, but it does not follow from the commute-time identity quoted by the old attempt.

Second obstruction. For integer L>=2, let T_L be 1 with probability 1-1/L and L^3 with probability 1/L. Then E T_L=L^2+1-1/L, whereas P(T_L >= E T_L/2)=1/L ->0. Thus a large lower bound for an expectation cannot imply a high-probability lower bound for the random variable by Markov's inequality. Markov bounds the opposite tail from an upper bound on the mean.

The existing C0012 attempt makes both problematic generic moves: it quotes E tau >= c R_eff mu(B) without a weighted-potential hypothesis and invokes Markov after a lower expectation bound. The corrected route must prove an actual lower-tail estimate for tau, with DGFF-specific spatial control; neither counterexample is itself a DGFF environment.

Checks: discrete versus continuous time; conductance measure versus normalized stationary law; the direction of the resistance inequality; and the direction of the probability tail. The exact experiment solves the two-state killed-chain equations independently and records the ratio for increasing M.
