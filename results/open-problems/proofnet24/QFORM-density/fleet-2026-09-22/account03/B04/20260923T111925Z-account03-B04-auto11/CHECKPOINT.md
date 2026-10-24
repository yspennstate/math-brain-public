SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-23T11:19:25Z.
attacking: fourth-compound two-sample disjointness as a product-Fourier exit, with a four-row/four-column compound-hub complement.

# Early substantive checkpoint

Let `M=A_{I,J}` be an ORIGINAL-coordinate cross block between disjoint independent coordinate banks after conditioning all other original coordinates. Write

`Z4=E4(M)=sum_{|S|=|T|=4} det(M_{S,T})^2`.

Assume `Z4>0` and let `nu(S,T)=det(M_ST)^2/Z4` be the canonical 4-volume law. Let `S1,S2` be iid row-set marginals of `nu` and define

`delta4^r=P(S1 cap S2 = emptyset)`.

Condition the iid pair on the disjointness event. By symmetry the first marginal `w` has every row inclusion probability <=1/2, because on the event the two row sets are disjoint and the two marginals are equal. Moreover

`D(mu || nu_r x nu_r)=log(1/delta4^r)=2D(w||nu_r)+I_mu(S1;S2)>=2D(w||nu_r)`,

so `D(w||nu_r)<=0.5 log(1/delta4^r)`. Lift this marginal construction to the full canonical minor law by conditioning two iid full minors only on row-set disjointness; the same symmetry and KL identity give a full-minor marginal `w` with row inclusion <=1/2 and

`D(w||nu)<=0.5 log(1/delta4^r)`.

For arbitrary minor weights, the determinant/weighted-AM-GM step in the completed product Brascamp-Lieb theorem replaces `Z4` by

`G4(w)=exp(E_w log det(M_ST)^2 + H(w)) = Z4 exp(-D(w||nu))`.

Hence

`G4(w)>=Z4 (delta4^r)^(1/2)`.

Apply the completed `k=4,q=1` fractional-volume Fourier estimate (same determinant/BL proof, with arbitrary weights exactly as in the completed entropy-weighted `k=2` extension): since the row marginals are <=1/2,

`||p_Q||_infinity <= 4 sqrt(e) G4(w)^(-1/8)`.

Therefore

`||p_Q||_infinity <= 4 sqrt(e) Z4^(-1/8) (delta4^r)^(-1/16)`.

The same holds after swapping the two banks, so `delta4=max(delta4^r,delta4^c)` may be used.

Complement: if `delta4^r<tau`, averaging `nu_r({S':S' cap S=emptyset})` over `S` gives one physical 4-row set `S0` for which at least `1-tau` of canonical 4-volume row mass intersects `S0`. If also `delta4^c<tau`, one physical 4-column set `T0` similarly exists; union bound shows at least `1-2tau` of the full canonical 4-volume lies on minors meeting both `S0` and `T0`.

This is a new order-4 product-Fourier/hub dichotomy. It does not solve the rank-3 survivor or the full QFORM target.
