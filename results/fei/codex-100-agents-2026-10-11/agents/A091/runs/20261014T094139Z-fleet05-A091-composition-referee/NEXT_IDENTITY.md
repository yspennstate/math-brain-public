# Exact next unpaid private-query interface

Take F=(1-Y)G+Y[A u+(1-A)H], H=B v+(1-B)G. A is a private point event of current probability q=2^-r, r>=1; B is any event on a separate private block, probability p. Y is still unexposed. Cores u,v and the actual fallback G occupy disjoint blocks; G may be a private fine selector. There is ONE physical G. Let m=Eu, n=EH, U_S,H_S,G_S denote actual Fourier coefficients embedded on the same union of all other physical blocks. Write L_S=(1-q)H_S+q U_S, w_S=q(U_S-H_S). Pairing the queried A bit and the still-unexposed Y gives the exact erasure

    B_A=(q-2q^2)(1-mn)
      +sum_S [Phi((G_S+L_S)^2/4,w_S^2/4)
             +Phi((L_S-G_S)^2/4,w_S^2/4)].       (1)

Proof: at the empty remaining-A frequency, the two Y frequencies have even amplitudes (G+L)/2 and (L-G)/2 and queried amplitudes w/2. Every nonempty remaining-A frequency gives equal-paired squared amplitudes. Their summed multiplier is q-2q^2, while E[Y(u-H)^2]=1-mn. The actual influence is d=q(1-mn)/2.

The original physically merged fine rarity release is

    kappa=q Var(u)/2+p k(q) Var(v)/2+k_G(q,p) Z_G,
    k(q)=eta(1-q)-eta(1-2q)/2,
    s=(1+(1-q)(1-p))/2,
    s0=(2-p)/2, s1=(1+(1-2q)(1-p))/2,
    k_G=eta(s)-[eta(s0)+eta(s1)]/2.              (2)

Here Z_G=sum a_l Var(g_l) uses the actual fallback's fine cores. Its label mass is a_l*s, combining inactive-Y and active failed-prefix histories BEFORE calculating eta. All logarithms of a_l cancel in the drift. Concavity gives k_G>=0. Independently summing the two occurrence labels would produce a different reserve.

Equations(1),(2) are checked independently on physical tables in code/next_query.py. They are an interface, NOT a paid inequality. The first unsupported line is uniformly bounding (1)-(2) by a fixed multiple of d, possibly with one named unused signed surplus. The coherent packets retain actual G_S/H_S correlation. This is the next mechanism to audit, rather than enumerating another gate-width class.
