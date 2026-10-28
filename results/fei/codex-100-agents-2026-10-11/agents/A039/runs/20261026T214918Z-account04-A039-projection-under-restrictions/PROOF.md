# Releasing the character anchor under physical restriction

All spectra are those of genuine Boolean functions on finite uniform cubes. Entropy and KL use bits. The normalized-divergence theorem below is an author-checked proof, with independent review pending. It does not price an arbitrary initial cross-entropy reference and does not prove FEI.

## 1. The reference and the actual coherent channel

For nonempty J and alpha in (0,1), write beta=1-alpha, ell=log2(1/beta), p(S)=fhat(S)^2, u=p(empty), and

    q^J(empty)=u,
    q^J(S)=beta*p(S)+alpha*(1-u)*1[S=J], S nonempty.

When J is empty DEFINE q^empty=p, retaining its full entropy as a terminal/source cost. This definition is essential; adding an empty spike to the nonempty formula would destroy normalization or the empty-mass constraint. Every q is a complete normalized law; for nonempty J it may contain a reference-only atom. Put a=1-p(J), even when J=empty. For nonempty J,

    K=D(p||q^J)<=ell*(1-u-p(J))<=ell*a.                 (1)

The non-J nonempty contributions are exactly ell*p(S). At J, q(J)-p(J)=alpha*(1-u-p(J))>=0, so its KL contribution is nonpositive. Empty mass contributes zero. For empty J, K=0.

For ANY physical coordinate i, delete i to obtain Pbar(T)=p(T)+p(T+i), Qbar likewise. The actual physical children have coefficients fhat(T)+/-fhat(T+i) and laws p_y. Set

    k_y(T)=p_y(T)/(2Pbar(T)) when Pbar(T)>0, else 1/2,
    r_y=sum_T Qbar(T)k_y(T), q_inh,y(T)=Qbar(T)k_y(T)/r_y.

This is a channel only AFTER erasing the queried spectral bit and using the actual signed Boolean amplitudes. It is not a phase-blind physical-restriction channel on p. Its physical outcome law is fair. Since q>=beta*p, r_y>=beta/2>0, including when reference-only rows occur. Thus all normalizations and denominators are valid. The finite KL chain gives

    K=E_i+O_i+mean_y K_inh,y,
    E_i=K-D(Pbar||Qbar)>=0,
    O_i=D(fair||r)>=0.                                (2)

After ACTUALLY resetting both children to their own q with projected anchor J'=J\{i}, the signed cost is

    sigma_i=mean_y K_fresh,y-mean_y K_inh,y
           <=mean_y K_fresh,y.                        (3)

All outcomes, ghosts, refunds and inherited KL remain in (2). No conversion is clipped or declared inherited for free.

## 2. Anchor release and the decreasing bank

At history h let n_h be the number of remaining physical coordinates, J_h the original J with queried coordinates deleted, and a_h=1-p_h(J_h). Define

    B_h=(n_h-1)*a_h if J_h is nonempty, and B_h=0 otherwise.

The first case has n_h>=1, hence B_h>=0. A projected anchor never becomes nonempty again. If J_h is empty, q=p; the same coherent channel gives r=fair and q_inh,y=p_y. Every subsequent exact reset costs sigma=0.

If J_h is nonempty, let b=fhat_h(J_h symmetric_difference {i}). The two coefficients at J' are fhat_h(J_h)+/-b, with a possible interchange of signs when i is in J_h. Therefore

    mean_y a_hy=a_h-b^2.                              (4)

If J' is nonempty, n_h>=2, and

    B_h-mean_y B_hy=a_h+(n_h-2)b^2
                       >=a_h-b^2=mean_y a_hy.

Equations (1),(3) imply sigma_i<=ell*(B_h-mean B_hy). If J' is empty, both fresh references are EXACT child spectra. Then sigma_i=-mean K_inh,y<=0 and B_h-mean B_hy=B_h>=0. This handles the last anchor query without a new anchor or a new source. In particular a SINGLETON anchor can be queried at any time without adding any budget to A036's old r*a bank, since r=n-1.

For every finite adaptive physical restriction tree, including arbitrary stopping and both branches, reset both children after each query according to this rule. Summing the local inequalities at their actual physical reach probabilities yields

    Sigma<=ell*(B_root-E B_terminal),
    K_root+Sigma<=ell*[n_root*a_root-E B_terminal]
                  <=ell*n_root*a_root.                (5)

There is no infinite-time limit: at most n_root queries occur on a branch. Full terminal KL is retained by the exact telescope

    K_root+Sigma=sum reach*E_i+sum reach*O_i+E K_terminal. (6)

This extends A036 PROOF sections1-2 to all physical coordinates. For |J|>1 its old protected bank r*a is replaced by (n-1)*a; the extra initially priced reserve is (|J|-1)*a. No such surcharge arises for the singleton used in the mod3 source. Once J disappears, zero terminal KL does NOT mean zero terminal entropy or zero description cost.

## 3. Complete terminals after the anchor disappears

Equation (4) holds also after J is empty: it is the ordinary conditional-mean square identity. Thus E a_terminal<=a_root for every adaptive stopped tree. At each leaf the distinguished frequency is J_h, possibly empty. Spectral entropy partition at this one atom gives

    H(f_h)<=h2(a_h)+d_h*a_h<=h2(a_h)+D*a_h,
    E H_terminal<=h2(A)+D*A,
    A=E a_terminal<=a_root.                            (7)

Here D is the original core dimension. The first inequality uses at most 2^d_h other frequencies; when a_h=0 or d_h=0 it remains valid with 0log0=0. Jensen applies to the finite leaf law, so there is no interchange-of-limit issue. Replacing A by a_root is justified when a_root<1/2 since h2(t)+Dt is increasing on [0,a_root]. There is NO surviving nonempty-character influence lower bound once the anchor has disappeared.

## 4. SAME supplied mod3 source: arbitrary core queries are now paid

This application is conditional on A036's ORIGINAL source/extraction inequalities, PROOF sections3-5, claim CHARACTER-ANCHORED-NORMALIZED-DIVERGENCE-BANK@1 (statement hash 7394ec7514ebcfa945e20a463d9a41d170f1ee708c6b2a30af133db2fdf7bf1e). Its universal normalized bank is independently reconstructed above; the full original-source construction is an explicit external dependency, not newly independently accepted here.

Use its same even N>=10, D=2N, delta=2^-N, h, singleton J={z1}, alpha=1/6 and complete original selector source. Its extracted active core has physical reach 1/4; the complementary terminals contribute rate4 surplus 2. Its source bounds are

    delta<=a=1-p_h(J)<=12delta,
    A0+c/4=K_J(h)/4,
    4I(F)-H(F)>=741/256,

where c is the ACTUAL signed old-full-spike-to-J conversion. Retain c and A0 exactly once. Now allow EVERY finite adaptive tree of ALL 2N core coordinates, including z1; after J becomes empty use exact spectra and keep their complete terminal entropy. Equations (5)-(6) give the SAME inclusive reference/conversion/reset bill

    L=A0+c/4+Sigma_core/4<=D*a*ell/4
                                <=6Ndelta*ell<1/64.   (8)

The integer certificate 6^15<16*5^15 proves ell<4/15. Also N2^-N<=10/1024 for N>=10; the ratio between consecutive N values is (N+1)/(2N)<=1. Therefore the last inequality in (8) is exact.

Using (7), a>=delta, a<=12delta<1/2 and log2(e)<2,

    E H(core_terminal)<12delta*(3N+2)<=3/8.

The final bound is decreasing for N>=10 since (3N+5)/(2(3N+2))<1. We use ONLY I_terminal>=0. The FULL selector terminal surplus is consequently

    S=2+[4E I_core_terminal-E H_core_terminal]/4>61/32. (9)

This is deliberately smaller than A036's protected-anchor 741/256 bound: that bound used a nonempty unqueried frequency. It must not be retained after z1 is queried.

Let e=H(F)-E H_terminal-4(I(F)-E I_terminal), and let Sigma_total=c/4+Sigma_core/4, retaining its sign. Algebra gives

    S-[A0+e+Sigma_total]_+
       =min(S,4I(F)-H(F)-A0-Sigma_total).

By (8)-(9) and the unchanged root surplus, the second entry exceeds 737/256 while S>61/32. Subtracting the SAME old 0<=omega<=1/4 leaves STRICTLY MORE THAN 53/32. Every original debit, complementary terminal, signed refund, ghost and own-outcome normalizer remains. This closes the singleton-anchor-query gap on that supplied nonfactor family. It does not price an arbitrary initial supplier or a new nonempty anchor after absorption.

## 5. Why the initial bound still cannot be priced by influence universally

Even optimizing J, D*(1-p(J)) is not O(I) on all Boolean functions. For odd majority on n=2m+1 bits, m>=1, all coordinates have influence c_m=binom(2m,m)/4^m and I=n*c_m. For any nonempty J choose i in J. Monotonicity gives D_i f in {0,1}, and fhat(J)=E[D_i f chi_(J\{i})], so |fhat(J)|<=E D_i f=c_m. This uses no unproved bound on higher-degree majority coefficients. Empty frequency is zero by oddness.

Since c_m=product_(k=1)^m (2k-1)/(2k), the inequality

    ((2k-1)/(2k))^2<=k/(k+1), k>=1,

follows by clearing positive denominators to 1<=3k. Thus c_m^2<=1/(m+1), and for every nonempty J,

    n*(1-p(J))/I >= (1-c_m^2)/c_m
                       >=sqrt(m+1)-1/sqrt(m+1) -> infinity.

All these majority coordinates are essential, so deleting dummy variables does not repair the bound. This refutes universal influence-pricing of this PARTICULAR initial upper budget, not the actual selected-policy cost, the majority FEI theorem, or FEI. Choosing a singleton anchor and immediately absorbing it makes reset cost nonpositive but leaves arbitrary child entropy unpaid; it cannot supply a universal entropy proof.

## 6. Checks and the exact remaining line

Checks that could invalidate the result: coefficient deletion for inside-anchor queries; last-anchor absorption; nonzero outcome normalizers; fair ghost rows; sigma signs; complete terminal entropy; constants/characters; majority higher coefficients. code/check.py checks ALL Boolean functions through n3, all anchors and all queries with exact laws and exact prime-log chain equalities; outward rational atanh bounds certify signs. code/audit.py independently verifies moving-anchor and bank telescopes using a different Walsh algorithm and complete/stopped trees, including terminal entropy bounds through an exact support-count surrogate. Finite checks alone do not prove (5): its finite-tree algebra is supplied in sections1-2.

First unsupported universal line: a useful arbitrary-core ORIGINAL reference/decomposition whose complete source cross-entropy and adaptive terminal bills are paid from O(I) unused original capacity. The n*a upper budget fails that price on majority. A036's protected universal bank is independently reconstructed at its exact local scope; its full mod3 source is a stated conditional dependency. External independent review and a full Lean entropy/KL proof are pending. Full FEI remains OPEN.
