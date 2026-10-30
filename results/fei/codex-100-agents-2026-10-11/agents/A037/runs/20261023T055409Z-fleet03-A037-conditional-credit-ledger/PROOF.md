# An original-variance budget for adaptive profile strengthening

All entropies and divergences are bits. Full FEI is OPEN. The analytic argument below extends the current point-factor hereditary-reference mechanism; independent review is pending. It does not supply the missing arbitrary-Boolean reference.

## 1. Actual inherited references and the consumed local theorem

For a point factor v on w bits, p is its squared Walsh spectrum and V=1-p(empty). Define q_beta(empty)=p(empty), and q_beta(T)=beta p(T)+(1-beta)V 1[T=full] on nonempty T, 0<beta<=1. Constant/character endpoints use their actual laws. All factors have disjoint inputs.

In the coherent selector G_epsilon(x,z)=epsilon at x=0 and g(z) at x=1, lift a matched-empty tensor reference by copying the two ACTUAL zero-data controller masses (epsilon +/- E g)^2/4 and putting q_g(T)/4 on both controller copies for T nonempty. This is normalized, same-support, and its KL equals D(p_g||q_g)/2. Factor profiles may differ.

After a physical bit query of a point factor, the actual inherited law uses the coherent kernel and its OWN outcome normalizer. The complete same-profile reset of ONLY that factor has signed mean sigma_same<=0. This consumes A036-NONPOSITIVE-COHERENT-SAME-PROFILE@1, whose proof is reconstructed as follows. With l=q_v/p_v, s=q_u/p_u and ratio1 at zero/zero, R=P l s. B=P l is normalized; writing bars for frequency erasure and r for actual reference outcomes, the exact reset identity is

    sigma_same = (1/2) E_y D(p_vy||q_vy) - D(Pbar||Bbar) + D(fair||r).

The spectator likelihood cancels pointwise, including the outcome normalization because q_u(empty)=p_u(empty). For w>=3, d=2^-w, alpha=1-beta, coarsen to the remaining target frequency. Cancellation of nonfull atoms leaves the upper bound

    Vgap = A log2(1-2 alpha d^2/A)
          +4d^2 log2(1+alpha d/[alpha+(2-4alpha)d]),
    A=1-2d+4d^2.

Using ln(1-z)<=-z and ln(1+z)<=z gives (ln2)Vgap<=-(4/3)alpha^2 d^2. The normalized outcomes are (1-eta)/2,(1+eta)/2 with 0<=eta<=4alpha d^2. Consequently (ln2)D(fair||r)<= (32/255)alpha^2 d^2. Thus sigma_same<=-(308/255)alpha^2 d^2/ln2. Width2 has zero fresh factor KL and follows directly by data processing. Constants and characters match. This reconstruction, the complete A036 proof, and our independent local tests retain all outcome costs. No unnormalized product-channel shortcut is used.

## 2. The price of changing a profile

For any finite probability p and V=1-p(empty), let t=p(full)>0. With alpha=1-beta,

    D_alpha=(V-t)log2(1/(1-alpha))
            +t log2(t/[t+alpha(V-t)]).

Its derivative is nonnegative and at most V/((1-alpha)ln2). Therefore for 0<beta'<=beta<=1,

    0 <= D(p||q_beta')-D(p||q_beta)
       <= V log2(beta/beta').                         (1)

This also holds with zero difference at constant/character endpoints. It is a bound on a difference, not two newly available KL allowances.

At a node whose target profile is beta, first perform the physical query and the conceptual SAME-beta factor reset. A036's local theorem pays that signed step. Then strengthen the queried factor, separately in either physical child, to beta_y in [beta_*,beta]. Keep all other paid factor references unchanged. Rebuild the actual child controller masses. Since the coherent lift KL is half its core KL, the ACTUAL reset obeys

    sigma_node <= (1/2) E_y[V_y log2(beta/beta_y)].    (2)

The conceptual intermediate is used only to subtract two KLs at the same child; it issues no resource. The destination and the actually transported old reference are exactly those in sigma_node. Either sign may have a different beta_y. Unqueried factors keep their current, possibly heterogeneous, profiles.

## 3. Optional-crossing lemma: do not spend the variance again

Let (V_h) be a nonnegative supermartingale on a finite fair physical query tree, and L_h an adapted nondecreasing process starting at0 and bounded by L_*. Then

    E sum_edges V_child (L_child-L_parent) <= V_root L_*. (3)

Proof directly as a conditional credit ledger: attach R_h=V_h(L_*-L_h) to the current node. At a query, the mean released charge is C_h=E_h[V_child(L_child-L_h)]. The exact local identity is

    R_h-C_h-E_h R_child
       =(L_*-L_h)(V_h-E_h V_child) >=0.               (3a)

All R_h are nonnegative. Telescope over the finite tree: total released charge plus the full final residual is at most the ORIGINAL R_root=V_root L_*. A child receives its actual diminished residual; conditioning never creates a fresh V_child L_* allowance.

An independent proof: for each lambda in (0,L_*], let tau_lambda be the first node at which L reaches lambda, killed if it never does. Layer cake writes the left side as integral E[V_tau_lambda 1[crossing]] d lambda. Optional stopping on the finite tree, followed by nonnegativity on the no-crossing outcomes, bounds every integrand by V_root. Both proofs handle increments chosen AFTER seeing the child. Replacing them by predictable increments would not justify the theorem. No variance is restarted at a descendant.

For an original Boolean factor v_i, V_h=1-(E[v_i|h])^2 is a nonnegative supermartingale under arbitrary adaptive fresh-data queries: conditional means form a martingale and Jensen gives variance contraction. This remains true when the next queried coordinate belongs to another factor or policies depend on the fixed controller sign.

At an already-reset coherent child start every factor at beta_start=5/6. Along every subsequent physical path, its beta can decrease arbitrarily often, but never below beta_*=4/5, and can change only when that factor is queried and actually refreshed. Set L_i=log2((5/6)/beta_i). Sum (2) and apply (3) separately to each ORIGINAL factor. The entire later signed bill is bounded by

    sigma_later <= (1/2) log2(25/24) sum_i V_i(start). (4)

All repeated same-profile terms are nonpositive. Branch-dependent strengthening, stopping, and queried-factor choices are allowed. Histories are finite, all physical children and both activation signs are retained. Monotonicity of profiles is essential to this particular proof; no unrestricted oscillation claim is made.

## 4. The SAME initial owner pays the first reset and every strengthening

Use h a tensor of m>=1 width-r>=2 point defects; d=2^-r, t=Pr(h=-1). The original Boolean F is chi_a at x=0, h at x=b=1, and +1 otherwise. The initial source Q0 is the correlated sector lift of the original factor beta0=7/8 laws: copy all six actual zero-data/control masses and put q_h(T)/16 on each of four controller masks for nonempty data. This is the same source used in A036's first actually paid reset; it is not a free conversion from an older canonical occupancy source.

Query b and retain b0. In b1 allow any finite adaptive fresh-data prefix keeping x,a unqueried. At any selected complete prefix leaves query a, retain both signs, and ACTUALLY reset their references to the coherent lifts with factor beta_start=5/6. Let sigma1 be this signed new-minus-inherited KL. Every complementary terminal remains. Within those already-reset a children allow the arbitrary finite monotone-profile histories of Section3. No x query is included in this theorem.

The first reset fresh KL bound is (1/2)log2(6/5) sum_i V_i at each a child; dropping only its nonnegative inherited KL gives an upper bound for sigma1. Equation(4) charges all later strengthening against the SAME variances at that first frontier. Optional stopping on the ORIGINAL data prefix, and b1 reach1/2, give the combined bill

    sigma1+sigma_later
      <= (1/4) log2(5/4) sum_i Var(original v_i)
       = m d(1-d) log2(5/4).                         (5)

Neither the first reset nor any intervening query budget is removed. This is a physically weighted bound; the two factors1/2 are the coherent lift and b1 reach.

The original root satisfies I0=1+t/2+I(h)/4, H0<=3+H(h)/4, and A0=D(P0||Q0)=D(p_h||q_h^0)/4. For a width-r point factor, nonempty entropy is 8(r-1)d(1-d), empty entropy is <=4d(1-d)/ln2, and KL0<=4d(1-d)log2(8/7). Consequently its SAME inclusive root headroom M0=4I0-H0-A0 obeys

    M0 >= 1+2t + m[2r d^2
                +d(1-d)(2-1/ln2-log2(8/7))].          (6)

Subtracting (5) leaves

    M0-sigma1-sigma_later
      >1+2t + m[2r d^2+d(1-d)/45] >1.               (7)

Here ln2>9/13 follows already from 2(1/3+1/81+1/1215)>9/13, and log2(10/7)<8/15 follows from 10^15<2^8 7^15. Thus 2-1/ln2-log2(10/7)>1/45. Unlike the earlier coarse source bound, (6) is strong enough to pay all profiles down to4/5 at arbitrary load m. More generally, within the declared starting-profile domain beta_*<=5/6, the same sufficient source calculation works when 2-1/ln2-log2(8/(7 beta_*))>0, equivalently beta_*>2e/7; the verified finite suite uses4/5 only.

## 5. Complete terminal ledger and retained old booking

All restrictions of the point-tensor core have H<=4I by their explicit spectra and tensor additivity. For G_epsilon(g),

    4I(G_epsilon)-H(G_epsilon)
      >= -2 epsilon E g + (4I(g)-H(g))/2.

Under each complete finite sign-conditioned data partition the mean E g is preserved. The two signs therefore cancel even when their policies and profile schedules differ. The untouched b0 terminal contributes1 globally; complementary unexposed leaves have nonnegative surplus. Thus the COMPLETE final S=4If-Hf is at least1. No positivity assumption is made for each individual sign child.

With e=H0-Hf-4(I0-If), sigma_total=sigma1+sigma_later, all actual reference changes telescope as

    A0+sigma_total = cumulative erasure KL
                    + cumulative normalized outcome KL + final full KL.

The original signed recovery identity, retaining both final outcomes and all old costs, is

    S-[A0+e+sigma_total]_+ = min(S,M0-sigma_total) >=1.

Subtract the SAME old booking 0<=omega<=1/4 ONCE. At least3/4 remains. No source, variance, old first-reset charge, influence allowance or earned credit is renewed. The theorem covers every m,r and the declared arbitrary finite adaptive profile histories, not just the finite validation domain.

## 6. Scope and first unsupported universal line

The new delta is the optional-crossing payment for actual, branch-dependent profile strengthening, combined with a sufficiently sharp original source budget. A036 already proves same-profile iteration; A039 already proves the one-query coherent identity. Their results are consumed and reconstructed, not renamed as new discoveries. The finite tests check the hard child-adapted variance payment separately from the coherent transport and full source ledger. Independent external acceptance remains pending.

The first unsupported universal line remains an influence-priced correlated initial supplier and hereditary normalized factor-refresh inequality for an arbitrary Boolean target. This argument uses the point-factor same-profile inequality in Section1. Replacing it by an arbitrary-factor theorem is not justified by optional stopping or KL telescoping. Unrefreshed multi-query gaps, arbitrary simultaneous spectator changes, or unlimited nonmonotone profile schedules are also outside the proved statement. Full FEI's universal constant improves by zero.
