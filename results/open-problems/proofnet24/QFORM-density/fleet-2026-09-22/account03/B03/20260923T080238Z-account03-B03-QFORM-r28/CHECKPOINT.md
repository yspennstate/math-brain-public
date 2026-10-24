SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T08:02:38Z.
attacking: replace the raw 1/2 leverage gate in the rank-two decoupled/product time integral by determinant-weighted disjoint-basis averaging, then apply it to the live one-sided right-plane packet before taking the independent-copy energy.

# Early substantive checkpoint

Current claim under derivation: for an original-coordinate rank-two coefficient frame, the determinant-weighted probability `delta` that two iid physical 2-bases are disjoint supplies a balanced Brascamp--Lieb exponent law with every coordinate marginal at most 1/2. Combining this with the completed determinant-entropy BL theorem yields an integrated estimate without pretending `X-X'` and `X+X'` are independent.

For the grouped-hub packet

`T=A(h.Y+xi(Omega))^2+2d U(Omega)(v.Y)+F(Omega)+sum_j V_j(Y_j)`,

where `Y` is an original product bank independent of `Omega`, `||p_U||inf<=L`, and `h,v` are linearly independent, set `G=[h,v]^T[h,v]`, whiten the physical rows, and let `delta` be the disjoint 2-basis mass of the whitened frame. The determinant-entropy estimate gives

`int_R2 prod_j |Psi_j(h_j s+v_j eta)| ds deta <= (2pi)^2 e delta^(-1/2) det(G)^(-1/2)`.

The Fresnel/grouped-hub calculation therefore predicts

`|phi_T(t)| <= min(1,K |t|^(-3/2))`,

`K=pi^(3/2)e L delta^(-1/2)/(|d|sqrt(|A|)sqrt(det G))`.

Consequences to finish/check this run:

`||p_T||inf <=3 e^(2/3)L^(2/3) delta^(-1/3)[|A|d^2 det G]^(-1/3)`,

`int |t|^(-1/2)|phi_T(t)|^2 dt <=(24/5)K^(1/3)`,

and the exact independent-copy identity converts the latter to a half-Riesz collision energy without separating any coordinate sum/difference pair. I will also record the rank-two localization identity for small `delta` and apply the valid account04/B03 collision lemma to the resulting L2 estimate.

Full QFORM and full-target continuity are not claimed here.