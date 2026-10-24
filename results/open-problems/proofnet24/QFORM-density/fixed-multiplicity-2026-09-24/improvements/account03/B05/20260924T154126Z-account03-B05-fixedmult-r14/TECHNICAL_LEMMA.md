# QFORM-S7-GOODSEED-PAIR-ESCALATION-v1

Corrected plain-text statement for run 20260924T154126Z-account03-B05-fixedmult-r14.

Constants: eta=1/100, kappa=1/6400, epsilon*=3*sqrt(2)/80.

Assume A is real symmetric, s_7(A)>=1, and there is no eta scalar or principal-pair pivot. Let B=A[S,T] be a nonsingular disjoint 2-by-2 interpolation seed whose completion A=D+R+E has rank(R)<=6, D diagonal and zero on S union T, and norm(E)<=epsilon*. Write S={s1,s2}.

Rank perturbation gives s_1(D)>=1-epsilon*, so choose h outside S union T with |D_h|>=1-epsilon*. Put

C1 = det A[{s2,h},T],
C2 = det A[{s1,h},T].

The bordered determinant identity and Laplace expansion in the shared h-column give, up to signs,

det(B) D_h = A_(s1,h) C1 - A_(s2,h) C2 + A_(h,h) det(B).

No-pivot gives |A_(h,h)|<eta and |A_(s,h)|^2<eta+eta^2. Therefore

(1-epsilon*-eta)|det B|
 <= sqrt(2(eta+eta^2)) sqrt(C1^2+C2^2).

Hence

C1^2+C2^2 >= R_esc det(B)^2,

where

R_esc = (1-epsilon*-eta)^2/[2(eta+eta^2)]
      = 78633/1616 - 1485*sqrt(2)/404
      = 43.4607496531583016....

Thus one of the two literal successor 2-by-2 minors has determinant square at least

(R_esc/2) det(B)^2 = 21.7303748265791508... det(B)^2.

Aggregate consequence. In the unpaid s7 branch V_3<kappa^3, the standard sampling estimate and Markov imply good seeds carry at least V_2/2. Let m_(H,T) count how many of the two successor incidences from all good seeds produce the same ordered disjoint successor minor A[H,T]. Summation gives

sum_(H,T) m_(H,T) |det A[H,T]|^2 >= (R_esc/2) V_2.

Since sum_(H,T)|det A[H,T]|^2=V_2, the determinant-volume weighted average of m_(H,T) is at least 21.7303748265791508. Therefore some successor has integer multiplicity at least 22.

Precise obstruction. This multiplicity has no dimension-free combinatorial upper bound: a fixed successor pair can be reused by arbitrarily many predecessor row choices. Therefore a successful s7 argument must use the repeated predecessor rows as an original-coordinate product bank, or derive an additional spectral restriction controlling their weighted geometry. Merely asserting O(1) preimages is invalid.

This is a supporting theorem, not an s7 density theorem. Multiplicity seven and the unrestricted three-eigenvalue conjecture remain open.
