# Boolean phase forces an address-energy cost for cyclic spectral marginals

1 October 2026. Natural logarithms. Candidate derived consequence, pending independent analytic review. Full FEI, unrestricted Boolean signed-middle payment, and critical-source entropy transfer remain open. No remote writes, source-hold changes, model calls, deployment, or novelty claim are made.

## Result and precise scope

Let f(x,y) be a Boolean sign on two disjoint finite uniform coordinate cubes X and Y. Write I_Y(f)=sum_(j in Y)||D_j f||_2^2, where D_j=(Id-flip_j)/2. Let p_X be the X-coordinate marginal of fhat^2. If every nonzero Fourier coefficient of f has X-degree at most an integer d>=1, then

    H(p_X) <= 2 I_Y(f) + 2(d-1) ln2.                    (1)

No independence between the X and Y spectral coordinates is assumed. The exact intermediate transfer, already implicit in the credited physical-restriction ledger, is

    H(p_X) <= E_y H(f_y-hat^2) + 2 I_Y(f).              (2)

The degree/granularity estimate on the genuine Boolean physical children closes the particular marginal-entropy obligation in (1). The new derived scope here is its application to every Boolean phase realization of the cyclic marginal, including internally correlated or source-coupled spectral padding. Equation (2), Gross LSI, the low-degree granularity fact, and character selectors are credited ingredients rather than new identities or constructions.

In particular, let p_X=P_(d,Q) be the uniform cyclic-label law from the pinned obstruction: X consists of d blocks of Q coordinates; every frequency contains exactly one label in each block; its labels sum to zero in Z/QZ. For any Boolean f having this exact spectral marginal,

    I_X(f)=d,
    I_Y(f) >= (d-1) ln(Q/4)/2,                         (3)
    I(f) >= d + max(0,(d-1) ln(Q/4)/2).

This does not assert that the energy lower bound is attained. It does not require the auxiliary cap conjecture K(B)>=4^-J. It is a full-Boolean necessary condition, proved using actual phase-realized physical slices.

For the unchanged exponential-threshold policy and 0<epsilon<=exp(-2), the standalone cyclic signed functional satisfies the further consequence

    R_epsilon(P_(d,Q)) <= I(f)                         (4)

for every such Boolean realization. In a product spectral extension P_(d,Q) tensor B, (4) pays only the original cyclic component of the additive signed functional. An arbitrary correlated padding law B can have its own nonzero signed remainder. For source-coupled padding there is not even a claimed decomposition of the joint process into the standalone cyclic process. No full joint signed-lifetime bound is proved.

## 1. A normalized hybrid law with zero rows handled

For each X frequency S define the real physical Y-row

    c_S(y)=E_x f(x,y) chi_S(x),
    p_S=E_y c_S(y)^2.

Every fixed-y slice f_y is genuinely Boolean, so sum_S c_S(y)^2=1. Thus mu(y,S)=2^(-|Y|)c_S(y)^2 is a probability law, with uniform physical Y marginal. Walsh orthogonality gives

    p_S=sum_T fhat(S,T)^2,
    sum_S I_Y(c_S)=I_Y(f).                             (5)

If p_S=0, the finite nonnegative average forces c_S(y)=0 for every y; omit that row. For the other rows, 0ln0=0 and exact entropy algebra gives

    H(p_X)
      = E_y sum_S c_S(y)^2 ln(1/c_S(y)^2)
        + sum_S Ent_y(c_S^2),                          (6)

where Ent(v)=E(v ln v)-Ev ln Ev. The second sum is exactly I_mu(Y;S). It is nonnegative and is charged once collectively, not once per original spectral atom.

## 2. Self-contained LSI with the exact energy normalization

For a real two-point function taking values a,b, homogeneous entropy obeys

    Ent_(uniform two points)(h^2) <= (a-b)^2/2.

Replacing a,b by their absolute values leaves the left side unchanged and can only decrease the right side. If both are zero the claim is immediate. Otherwise normalize by m=(a^2+b^2)/2 and put z=|a^2-b^2|/(a^2+b^2) in [0,1]. After division by m, the assertion is

    [(1+z)ln(1+z)+(1-z)ln(1-z)]/2
       <= 1-sqrt(1-z^2).

Both sides vanish at z=0. Their derivatives on (0,1) are atanh(z) and z/sqrt(1-z^2). The latter dominates the former: their derivatives are respectively (1-z^2)^(-1) and (1-z^2)^(-3/2), and both functions start at zero. Integrating proves the claim; continuity covers z=1. Since E(Dh)^2=(a-b)^2/4, its right side is exactly 2I(h).

Entropy tensorizes over independent coordinates:

    Ent_Y(v) <= sum_j E_(Y without j) Ent_j(v).

For completeness, the two-factor chain identity is Ent_(U,V)(v)=E_V Ent_U(v)+Ent_V(E_U v). Convexity of the homogeneous entropy functional (the log-sum inequality) bounds its second term by E_U Ent_V(v). Iterate. Applying the two-point estimate to v=h^2 therefore proves

    Ent_Y(h^2) <= 2 I_Y(h).

Apply this to every c_S, sum, and use (5). The second sum in (6) is at most 2I_Y(f), proving (2). This is the same normalization as the already credited Gross step in EXTENDED_NOISE_LEDGER.md Section10; its reproof is included to remove any imported-constant ambiguity.

## 3. The genuine-Boolean slice lattice

For any Boolean sign g on a finite X cube with Fourier degree at most d>=1, every Fourier coefficient lies in 2^(1-d) Z. Here is a proof covering lower as well as top degrees.

Set u_i=(1-x_i)/2 in {0,1}. The unique multilinear expansion g=sum_U b_U product_(i in U)u_i has degree at most d, since the affine change of variables preserves the degree bound. Its coefficients are finite alternating sums of g's sign values on U-faces. For U nonempty the sum has 2^|U| terms, each an odd integer, and hence b_U is even. The constant coefficient b_empty is +1 or -1. Expanding product u_i into sign characters gives

    ghat(S)=(-1)^|S| sum_(U superset S) 2^(-|U|) b_U.

Every nonempty-U summand is in 2^(1-d)Z; the integer constant term is too. This proves the lattice for all S. A zero coefficient contributes no entropy. Every nonzero square is at least 4^(1-d), and Parseval gives

    H(ghat^2) <= 2(d-1)ln2.                            (7)

The source X-degree assumption implies each physical slice f_y has degree at most d: c_S(y)=sum_T fhat(S,T)chi_T(y), and every |S|>d row is identically zero. Apply (7) slice by slice in (2) to prove (1). The case d=0 is separate and simpler: f is independent of X, p_X is the empty atom, and H(p_X)=0. It is not covered by a negative right side with d-1.

## 4. Cyclic marginal and padding energy

Suppose the exact X marginal is P_(d,Q). It has N=Q^(d-1) supported atoms, each of mass 1/N, and all have degree d. For every S outside that support, p_S=0 forces every coefficient fhat(S,T)=0. Therefore no hidden X-degree hypothesis has been added: the given nonnegative marginal itself forces X-degree d and I_X(f)=d.

Its entropy is (d-1)ln Q. Substituting this into (1) gives (3). This argument permits arbitrary dependence among Y spectral coordinates and arbitrary dependence between their joint law and the original cyclic X law. Passing a scalar cap family alone cannot invoke the argument: it needs actual Boolean physical restrictions and their coefficient lattice.

The lower bound in (3) is weaker numerically than the previous cap-derived product-padding lower bound. Its different scope is important: it applies to any actual Boolean phase realization, even where no product K factorization or universal correlated K inequality is available. It does not prove those auxiliary probability-law statements.

## 5. Payment of the standalone original cyclic component

Use exactly the original-time, complete-cascade functional in the pinned cyclic report, including every forced-information refund. If epsilon Q<=1, a complete initial cascade resolves the cyclic source at time zero: any unresolved block has marginal sum one over at most Q candidates, so some bit remains eligible. Its continuous cost is zero and its refund is nonnegative. Hence R<=0 and (4) follows.

If epsilon Q>1, put T=ln(epsilon Q)/2. The pinned exact formula and its proof give two separate upper bounds:

    R <= d H_(d-1),
    R <= d T.

For the second, E Gamma_t=d c_Q exp(-t)[1-(1-exp(-t))^(d-1)] before T, with 0<c_Q<=1; integrating exp(t)Gamma and dropping the nonnegative refund gives at most dT. The first follows from the exact harmonic formula by dropping both nonnegative subtractions. No changed stopping rule, restarted time, or missing refund is used.

Write a=ln Q/2, b=ln2, h=H_(d-1). Then a>1 because epsilon<=exp(-2), and

    R <= d min(h,a-1),
    I(f) >= d+(d-1)(a-b).                              (8)

The last quantity is positive. Since h<=d-1 and b<1, the following elementary comparison proves (4).

If a<=h+1, the difference between d(a-1) and the energy lower bound is a-2d+(d-1)b. It is at most h+1-2d+(d-1)b<=-d+(d-1)b<0.

If a>=h+1, the difference between dh and that lower bound is largest at a=h+1. There it equals h-d-(d-1)(1-b)<=-1-(d-1)(1-b)<0.

Thus (4) follows. It cannot be summed with a fresh full-source energy payment for the padding component. If the initial squared law factors as P_(d,Q) tensor B on disjoint coordinates, no-click likelihood, clicks and forced answers preserve the two-factor posterior. Threshold choices in one factor do not change the other. With the same original-coordinate ordering, each factor follows its standalone policy at original time. Gamma and each forced MI loss then add, giving R_joint=R_cyclic+R_B. Only R_cyclic is paid by (4). For a coupled joint law this factorization is not asserted.

## 6. Explicit full-phase lift, as a credited control

For Q=2^m, let Y consist of k=(d-1)m physical bits encoding d-1 independent labels. Map them bijectively to cyclic frequency sets U(y), setting the final label to minus the sum. The sign function

    F(x,y)=chi_(U(y))(x)

is Boolean. Every physical Y-row c_U(y) is a point indicator. Consequently

    Fhat(U,T)=2^-k chi_T(y_U),
    Fhat(U,T)^2=2^(-2k),
    P_(X,Y)=P_(d,Q) tensor Ber(1/2)^k,
    I_X=d, I_Y=k/2, H_joint=2kln2.                     (9)

The selector-class theorem at the exact pin below already supplies this construction and flat-spectrum identity; (9) specializes it to the cyclic code. This is a useful full-phase control, not a new general selector theorem. It proves realizability with r=k fair padding bits, not with the smaller cap-only threshold k-2(d-2), whose phase realization is not established here.

Because epsilon<=exp(-2)<1/2, all fair padding bits are forced at time zero; their independence gives zero Gamma and zero forced MI refunds. The existing product-padding coupling therefore gives R(Fhat^2)=R(P_(d,Q)). For fixed epsilon in (0,exp(-2)], d=2^ell and Q=d^6, (9) and the pinned cyclic estimate give ratio R/I(F) tending ln2/3. This is a bounded-ratio Boolean control. It cannot revive the original divergent arbitrary-law ratio.

## 7. Source overlap and exact pins

The live route directory was read at 13:57 UTC and still listed addenda11.24 through11.53. CURRENT_SOURCE_INDEX.json has observed_at 2026-10-01T13:29:34Z, snapshot c9b3298ca16faff26591f535d278875132336f8a, blob694be758081c18eeacd50459aeb62f9535bd9803. Historical REPORT blob216cb662e7b21cfe6d7c2034a6690f3c10b886fa. These are navigation, not proof or admission decisions.

- The exact hybrid law and summed-Gross information payment are prior EXTENDED_NOISE_LEDGER.md Section10, math-open-problems commit c63180b23321ce9130dbcbab825546f6c14923d0, blob dcc66530c8349916aa7700a43fa6768eb23f749d. That section also credits earlier block-JS and uncertainty sources. Equations (5)-(6) and (2) are not claimed as new identities.
- The derivative-value hierarchy is prior mixed-derivative-hierarchy/REPORT.md, commit70fa674aa26e14eaf8fa7682ca2ede7936ee6d61, as linked by route11.40. The stronger top-degree Boolean lattice is explicitly retained in route11.51's polynomial-alphabet clarification. We prove the full low-degree lattice above for this application; no newness claim for granularity is made.
- Exact cyclic signed formula and all-cascade scope: commit809f828d52ea0b5acdd0963f6315c526b9290c34, cyclic-label-signed-lifetime-obstruction/REPORT.md, blob2515ec570dd6042cb8febc5d5b9903c2000987b4. The frozen report's original pending-review wording is historical; route11.51 records its completed review. The current consequence does not change the earlier arbitrary-law falsifier.
- Independent product padding: commitdf7bbb4c664ee7f0388b7fe946f9be4d5a833606, product-padding-guard/AUDIT.md, blob13b7493c0280cb98651618ab9e7d0c7b226752c8. Its sharper cap-energy constant has product scope. General correlated K and extra-padding signed lifetime remain open, as route11.53 records.
- Distinct-character selectors: commit971fe8a485349a69914decb992000879acbc892e, address-ensemble-profile/CLOCK_FLUX_AND_CHARACTER_SELECTORS.md Section2. Its data characters may overlap, including the cyclic support; its logical address labels are distinct. This is the source of the control (9), not an independent novel construction.
- The dominant-source theorem at commit71f60ac4ad2ae9dd54437fe0e4e3a0ceeee19ccd, blobe0988e2e2d1618c8e1372bec484924d9c110da8c, concerns a different rare-row/source-sensitive endpoint. It is not invoked here and its unpaid rare-row scope remains unchanged.

All exact paths, blobs and URLs are recorded in SOURCE_PINS.json. Local source copies support readback and comparison only; they are not publication additions or new evidence of live ingestion. No full literature-priority search was performed.

## Verification boundary

The universal inequalities above have analytic proofs. A bounded standard-library checker will test the hybrid normalization, full/partial Walsh energy identities, coefficient lattice, exact entropy decomposition as rational prime-log forms, rational outward logarithm enclosures of finite inequalities, actual selector phases, and a nonproduct padding fixture. It does not simulate the full continuous policy, prove universal statements by enumeration, or establish the unrelated correlated joint signed bound. Independent mathematical review is required before changing this candidate status.

