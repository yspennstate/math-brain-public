SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T22:14:04Z.
attacking: the global third-compound spectral resource by decomposing every squared 3x3 minor according to physical row/column overlap, then paying the disjoint class by a literal random coordinate cut and identifying the exact one-overlap currency seen by the grouped rank-two kernel-derivative receiver.

# Early substantive checkpoint

Let A=A^T be n x n. Fix an original-coordinate triple T and write

P=A[T,T],   C=A[T,T^c],   G=CC^T.

For each outside coordinate r let c_r=A[T,r] in R^3, and for r<s put w_rs=c_r x c_s. Cauchy--Binet, grouped by the overlap cardinality |S intersect T| of a row triple S with the fixed column triple T, gives the exact identity

    det((A^2)[T,T])
      = det(G)
        + sum_{r<s in T^c} ||P w_rs||^2
        + ||adj(P) C||_F^2
        + det(P)^2.                                      (CP3)

Equivalently, using the second-compound identity sum_{r<s} w_rs w_rs^T=adj(G),

    det(P^2+G)
      = det(G)+tr(P^2 adj(G))+tr(G adj(P)^2)+det(P)^2.

Proof by overlap class: |S∩T|=0 gives the 3x3 minors of C and sums to det G. If |S∩T|=1, write S={k,r,s} with k in T and r,s outside T; symmetry gives

    det A[S,T] = +/- e_k^T P(c_r x c_s),

so summing over k,r,s gives the second term. If |S∩T|=2, S=(T\{k}) union {r}; replacing row k of P by c_r^T gives

    det A[S,T] = +/- e_k^T adj(P)c_r,

so summing gives ||adj(P)C||_F^2. The overlap-three class is S=T and contributes det(P)^2. Finally A[:,T]^T A[:,T]=(A^2)[T,T]=P^2+G.

Summing (CP3) over all triples T yields

    e_3(A^2)=E_0+E_1+E_2+E_3,

where E_j is exactly the sum of det A[S,T]^2 over ordered triples S,T with |S∩T|=j. Under sigma_3(A)>=1, e_3(A^2)>=1, so at least one overlap class has mass >=1/4.

The disjoint class is already paid. For a uniformly random literal bipartition I|J, each ordered disjoint pair (S,T) with |S|=|T|=3 is captured as S subset I, T subset J with probability 2^-6. Hence some cut satisfies

    Z_3=e_3(A[I,J]A[I,J]^T) >= E_0/64.

Using QFORM-PHYSICAL-D3-NO-MARGINAL-GATE-v1 with C_3=3*2^(4/3)*e^(1/3),

    ||p_Q||_infinity <= 2 C_3 E_0^(-1/6).

Therefore E_0>=1/4 implies the target-level continuous-density bound

    ||p_Q||_infinity <= 3*2^(8/3)*e^(1/3) < 26.585,
    P{Q in I0} < 26.585 |I0|.

For a fixed T with rank(C)=2 and unit n spanning ker(C^T), adj(G)=e_2(G) n n^T, so its one-overlap currency is exactly

    V_T = tr(P^2 adj G)=e_2(G)||Pn||^2
        = sum_{r<s} ||P(c_r x c_s)||^2.

This is precisely the aggregate currency in the grouped rank-two kernel-derivative branch. The exact endpoint also sharpens: if rank(C)=2, Pn !=0, and both the overlap-two and overlap-three currencies vanish, then rank(P)=1. Indeed det(P)=0; if rank(P)=2 then adj(P) has rank one with range ker(P), while ||adj(P)C||_F=0 forces range(adj(P)) subset ker(C^T)=span(n), hence Pn=0, contradiction.

This checkpoint is structural/supporting progress, not a proof of the full conjecture. The unresolved step is to pay the globally spread E_1/E_2/E_3 classes without selecting a supposedly uniformly good single physical triple.
