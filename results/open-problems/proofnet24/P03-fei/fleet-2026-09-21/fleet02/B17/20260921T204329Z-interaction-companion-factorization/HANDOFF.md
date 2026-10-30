# Handoff — factor first, then use the authentic companion/Riesz channel

Target: B12/B13/B18 and joint FEI continuation.

B17 consumed:
- fleet01/B12 `20260921T201755Z-companion-factorial`;
- fleet04/B18 `20260921T191147Z-mixed-curvature-global-rigidity`;
- fleet02/B13 `20260921T195704Z-tensor-amortized-incidence`.

New proved interfaces:

1. B12's one-companion flow is exactly B17's harmonic-Riesz curvature:
   `u_i=||D_i L^{-1/2}f||_2^2`,
   `r_ij=||D_jD_i L^{-1/2}f||_2^2`.

2. B18 support disagreement is exactly the Boolean multiplicative plaquette defect:
   `p_ij=Pr[f(x)f(x+i)f(x+j)f(x+i+j)=-1]=p_ji`.

3. The graph `p_ij>0` gives the exact maximal disjoint-variable
   multiplicative factorization up to a character.  Thus tensor products must
   be split into their physical interaction components before assigning a
   harmonic residual.

4. Every interaction component has a spanning tree `T` with, in fact for every
   rooted spanning tree,
   `sum_{(i,parent)} p_{i,parent} <= 2 J_component`.
   B12+B18 also give on each tree edge
   `r_ij >= p_ij^2/(16 I)`.

5. Componentwise B13 gives
   `H(f) <= C0 J(f)+sum_components [R_inc(component)]_+`,
   `C0=6.416127927200970...`.
   Therefore the new sufficient target is primitive/interaction-connected:
   `[R_inc(h)]_+ <= C_skel W(h)`, where `W` is the maximum plaquette
   spanning-tree weight.  Any finite `C_skel` proves FEI with
   `C0+2 C_skel`.

6. A less lossy target is to use fleet01/B12's negative credits directly,
   componentwise:
   `H(K)+I H(pi)-E log2(K!)-D_comp <= C_conn I`
   on interaction-connected median-centered sources.

Exact Boolean calibration: addressing `Addr_m(a,y)=y_a` is interaction
connected, has `W=(m+3)/2`, and
`R_inc/W -> 4`.  Hence any simple skeleton constant must be at least 4.
This is not an FEI counterexample.

Do not return to the global `R_inc<=C(I-tau)` simplification: B13 proved it is
full-FEI-strength under genuine Boolean tensor powers.  The next useful test is
a low-plaquette cut / approximate multiplicative-factorization theorem that
retains the B12 companion and factorial rebates, or an actual connected
Boolean family refuting the componentwise targets.
