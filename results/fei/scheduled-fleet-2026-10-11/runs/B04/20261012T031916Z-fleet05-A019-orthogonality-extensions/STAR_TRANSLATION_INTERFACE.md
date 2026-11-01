# Conditional-row payment with one shared selector

Let `F(x,z,y)=g(y+sum_j v_j 1{x=s_j} A_j(z_j))`, with all private blocks disjoint and fresh. The core may be arbitrary; vectors and orientations may repeat. Define `h_j=(-1)^A_j`, `rho_j=Pr[g(y)!=g(y+v_j)]`, and `p_T=ghat(T)^2`. For selected modules `T dot v_j=1`, the two selector-phase children are products of module signs on disjoint private groups. Their means are `alpha_T,beta_T`.

Exact debts and budgets:

- `M_W=0`, `I_data=I(g)`, `I_priv=sum_j rho_j I(h_j)/2`.
- `I_x=sum_T p_T(1-alpha_T beta_T)/2`.
- `B_W=sum_j rho_j H(h_j)/2+sum_T p_T kappa(alpha_T,beta_T)`; the complete signed empty-sector correction is defined in REPORT section 2.
- `Delta_x H<=I_priv+(3/ln2)I_x` by applying the accepted boundary lemma to actual Boolean selector phases.
- The actual derivative has `2I(D_xF)=I_priv+2sum_T p_T|T|d_T`. The extra core term is removed only under this Boolean-phase hypothesis.
- Certified module entropy `H(h_j)<=C_act I(h_j)` yields `B_W<=max(C_act+1,3/ln2)I_W`. Full closure also retains a separately certified terminal `H(g)`.

For private point activations this is `B_W<=5I_W`. The selector-first tree has `B_i<=3Inf_i` at all its queried nodes, hence exactly zero localized boundary bill at threshold3 and terminal resources `H(g),I(g)`. The proof holds for unbounded module count, private width, majority-core dimension and fresh nesting depth.

Correction guard: shared-bit erasure includes `1-(alpha^2+beta^2)/2` from all nonempty private frequencies, in addition to the empty-sector Phi term. Omitting that mass is false; the initial failure is preserved. The repaired uniform bound is3, not2.

Universal admission remains open: arbitrary normalized shared-data coefficient rows need not be Boolean phases. Selector/core coordinate coupling destroys the current justification for removing the data-core term. This is the next target, not permission to pay arbitrary terminal entropy twice.
