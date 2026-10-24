# Source-owned occupancy transport at the exposed priority fixture

All units are bits. The actual Boolean ancestor selects u=(-1,-1,-1,+1) when x=0,a=1, selects v=(-1,+1,+1,+1) when x=1,b=1, and otherwise +1. Expose u0=0: its original physical influence is 1/8 and the reached u is -1. Drop only its remaining irrelevant data coordinate. The reached root has coordinates x,a,b,v0,v1 and

    F=-1 if x=0,a=1;
      -1 if x=1,b=1,v0=v1=0;
      +1 otherwise.

The first tested query is private a. This is exactly the source's exposed priority fixture, not an independent surrogate with the same marginal means.

## 1. The reference that is owned

Let P be the root squared Fourier law, v=P(nonempty)=55/64 and d=(1/2,1/2,1/8,1/8,1/8). Let Q_occ maximize entropy on nonempty sets at marginals r=d/v. Its unique positive normalization root c satisfies

    1-c=(1-32c/55)^2(1-8c/55)^3,  3/4<c<1.

With theta=c r, complete this *same original* reference by M(empty)=9/64, M(S)=v Q_occ(S) for S nonempty. The source-owned bank is A=D(P||M)=v K_occ. Entropy maximization follows because log Q_occ is affine in the set indicators; Gibbs then proves maximality among matched-marginal nonempty laws. Strict concavity of g(c)=1-c-product, g(0)=0, g'(0)>0 and g(1)<0 prove the unique interior root. The exact source bracket g(3/4)>0 is independently certified by 4*31^2*49^3<55^5.

The interval certificate starts from [3/4,1] and bisects 48 times with exact rational polynomial signs. Its final bracket is

    907464997206015/1125899906842624 < c
                                      < 443098143167/549755813888.

Both endpoint signs are checked. No approximate normalization or fitted reference is used.

## 2. Physical coherence and the actual one-use bank

At a node with inherited reference Q and actual spectrum p, let T be the residual spectral set after erasing queried i. Set q(T)=p(T,0)+p(T,1), Q_T=sum_i Q(T,i). Define the released conditional KL

    E_i=E_q D_2(p(S_i|T)||Q(S_i|T)).

Use the actual signed child spectra p_y(T) and the common kernel k(y|T)=p_y(T)/(2q(T)); extend it fairly on zero q fibers. Apply exactly this kernel to Q_T, with outcome probabilities Q_Y and normalized Bayes child references Q_y. Then the reference ledger is

    D(p||Q)=E_i+D_2(fair||Q_Y)+average_y D(p_y||Q_y).       (1)

This is the usual KL chain rule at an actual coherent restriction, applied to the specified root credit. It is not a new general chain-rule claim. It identifies where the excluded spectral support can be released, which is precisely the missing application in A038's handoff. Every child reference debt in (1) remains. Reference outcome KL need not be zero, although the original *product* reference in A038 has fair outcomes.

With inherited Q_y and further actual physical queries, (1) telescopes on the original reference tree:

    A=sum_internal w_h(E_h+O_h)+E_leaf D(p_leaf||Q_leaf),  O_h=D_2(fair||Q_Y,h).

No fresh root bank is inserted. The checker reconstructs all eight possible second-query nodes, then all sixteen policies selecting any remaining coordinate separately in the two a branches. Each is a genuine depth-two stopping tree. Both the reference KL at its leaves and their actual spectral entropy/H-U-R profiles remain. Numerical interval overlap checks are consistency checks for (1); the equality follows from its analytic log expansion. Strict signs and margins, in contrast, are certified by rational interval bounds.

## 3. Released credit exceeds the stated debt at this fixture

The actual root masses are 9/64 at empty and {x}, 1/4 at {a} and {x,a}, and fourteen masses 1/64, all with a absent. Hence q_empty=q_{x}=25/64; conditional queried-bit probability is 16/25 at both exceptional residual fibers and zero elsewhere. Put

    t=32c/55, s=(1-8c/55)^3,
    h=(1-t)s/2, b0=h/(9/64+h).

The original reference's conditional a probability is b0 at the empty residual fiber and t at every nonempty residual fiber. Therefore

    E_a=(25/64)D_2(Ber(16/25)||Ber(b0))
        +(25/64)D_2(Ber(16/25)||Ber(t))
        +(7/32)log2(1/(1-t)).                              (2)

The last term is the released part of the excluded a-plus-data event, but it is not the entire bank: both exceptional fibers matter. The direct whole-spectrum checker and independently written three-fiber checker give

    0.239583496125 <= E_a <= 0.239583496126,
    0.025269476786 <= E_a-rho <= 0.025269476787,
    E_a-rho>1/40,

where rho=2+(21/32)log2(7)-(25/16)log2(5) is the source's original residual-product reset. Thus one withdrawal of rho from this particular erasure release is feasible, with the inherited child debts in (1) untouched. The sixteen depth-two trees explicitly keep this debit once and the positive remaining margin.

The original occupancy bank is in [0.514825178263,0.514825178264]. The constant-variance selector release remains kappa=0. No influence payment is claimed by this bank withdrawal; it is a reference-credit application at this one actual root.

## 4. Conversion between the actual references, rather than identifying them

The transported occupancy Q_y differs from the Bayes prediction from a residual product reference. Let R_y be each *actual* child's product projection and sigma_occ=average_y E_{p_y} log2(Q_y/R_y). In supported finite form,

    sigma_occ=average_y TC(f_y)-average_y D(p_y||Q_y).

Equation (1) then becomes

    A=O_occ+average_y TC(f_y)+(E_a-sigma_occ).               (3)

This specific fixture satisfies

    0.198062421435 <= sigma_occ <= 0.198062421436,
    E_a-sigma_occ>1/25.

Consequently the original root occupancy KL pays its own reference outcome mismatch and the complete mean child product KL, with more than 1/25 bit left. This is an actual reference-conversion statement; it does not identify sigma_occ with rho. Debiting rho and applying (3) are ALTERNATIVE uses of E_a, not simultaneous deductions. The second-query computations transport unreset Q_y; they do not assert that exercising (3) supplies another bank for those computations.

An independent moment-only calculation computes A=h2(v)+v Hmax(r)-H(F). The occupancy-reference outcome probability is

    Q(Y=0)=1/2+(12/25)[9/64-ts/2].

The true children both have entropy H_child=6-(49/32)log2(7), mean product KL 4h2(1/8)-H_child. This independently verifies A-O_occ-average TC_child>1/25, without enumerating reference atoms or using the main checker transitions.

## 5. Actual terminal obligations

For the exclusive independent-core decomposition, U=sum_j q_j[H(core_j)-eta(mean_j^2)] and R=sum_j eta(q_j)Var(core_j). At the root and both a children U=R=3/8: the v core is still the actual two-bit point defect, with selector probability 1/4. The constant reached u contributes zero to U and R. Therefore

    (H-U-R)_root=13/4-(9/16)log2(3),
    (H-U-R)_child=21/4-(49/32)log2(7),
    average H_child>17/10.

Root influence is 11/8, queried influence 1/2, mean remaining influence 7/8. Every depth-two leaf profile is computed from its actual remaining v truth table and its original exclusive controller partition. Zero terminal profiles use exact formal-log cancellation, not a numerical positivity tolerance. Their reference debt is a different object from H-U-R and from spectral entropy. Nothing in (1)-(3) supplies a universal payment for those terminal obligations.

## 6. Sharp scope failure of the attempted continuation

RARE_OBSTRUCTION.md proves an actual Boolean family with the same essential-exposure provenance and v_n a point defect on n bits. For every n>=16 its original product reset rho_n satisfies rho_n>=((n-2)/2)2^-n, while the erasure release of its own canonical root occupancy reference satisfies 0<E_n<=3*2^-n. Hence rho_n/E_n>=(n-2)/6 grows without bound. Frozen n=16,24,32,64 checks corroborate this all-dimensional proof.

The same rare family has the stronger actual conversion deficit A_n-O_occ,n-average TC(child)<=-((n-6)/2)2^-n: the original occupancy bank cannot cover its outcome mismatch plus the freshly projected child product KL without an additional debit. This is proved in the final section of RARE_OBSTRUCTION, using the compensated TC identity, Delta>=0 and the binary entropy chord. It distinguishes a source-compatible reset cost from the original product rho rather than assuming they are equal.

Thus this stage closes both the source fixture payment and the proposed universal fixed-factor release mechanism's failure. A large root occupancy bank may survive in inherited child references; its existence does not mean a particular query releases it. The first unsupported universal line is allocating that still-retained child/core credit to the reset, controller decrement and actual terminal entropy using one compatible reference and one unused physical influence/slack account. No FEI constant improves and no actual H/I counterfamily is supplied.
