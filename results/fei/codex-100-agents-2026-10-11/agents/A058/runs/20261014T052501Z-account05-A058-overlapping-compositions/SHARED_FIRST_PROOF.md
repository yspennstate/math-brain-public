# Independently activated shared phases: a paid physical policy

All physical bits are uniform and independent; entropy is in bits. Let u(S),v(S) be arbitrary quadratic Boolean phases (-1)^P, degree(P)<=2 over F2, on one common finite shared cube S. On disjoint private control blocks X,Y of widths r,t>=1 let A=1_{X=0}, B=1_{Y=0}, p=2^-r, q=2^-t. Define

    G=1+A(u-1), H=1+B(v-1), F=(G+H)/2+z(G-H)/2,

with a fresh fair selector z. No independence, orthogonality, balancedness, equal-width or equal-mean condition is imposed on u and v. The controls remain unqueried during the shared-data phase. Query shared coordinates adaptively until both phases are constant, then query private controls adaptively in any order; z stays unqueried until data completion. Any finite prefix of this policy may stop at arbitrary leaves.

## 1. Exact collision and inherited costs

At a reached shared restriction write alpha_C=uhat(C), beta_C=vhat(C). The shared-only coefficients of G,H are

    g_C=(1-p)1_{C=empty}+p alpha_C,
    h_C=(1-q)1_{C=empty}+q beta_C.

Nonempty private-control frequencies are exclusive to one branch. At every shared query i the common rows sum and subtract coherently. Set mu_C=g_C, a_C=p alpha_(C+i), nu_C=h_C, b_C=q beta_(C+i), for C not containing i. Then the signed correction relative to half the two inherited core erasures is exactly

    D_i=P-N,
    P=sum_C[Phi((mu_C+nu_C)^2,(a_C+b_C)^2)
                       +Phi((mu_C-nu_C)^2,(a_C-b_C)^2)]/4,
    N=sum_C[Phi(mu_C^2,a_C^2)+Phi(nu_C^2,b_C^2)]/2.

Phi(a^2,b^2)<=2|ab|. Let d=Inf_i(u), e=Inf_i(v); these are zero or at least 1/2, and restrictions preserve quadratic degree. Actual Inf_i(F)=(pd+qe)/2. Coefficients of a physical half-difference obey |alpha_i|<=d, |beta_i|<=e. Parseval gives residual vector norms <=1 and derivative-vector norms sqrt(d),sqrt(e). Thus

    P <=(2-p-q)(p|alpha_i|+q|beta_i|)
                       +(p+q)(p sqrt(d)+q sqrt(e))
      <=[2-p-q+sqrt(2)(p+q)](pd+qe)
      <=(1+sqrt(2))(pd+qe),
    N <=p(1-p)d+p^2 sqrt(d)+q(1-q)e+q^2 sqrt(e)
      <=((1+sqrt(2))/2)(pd+qe).

Here sqrt(d)<=sqrt(2)d for d=0 or d>=1/2, and p,q<=1/2 imply p+q<=1. Each Cauchy-Schwarz cross term uses the actual common row vectors; no shared spectral l1 bound is assumed. Since P,N>=0,

    |D_i| <=(2+2sqrt(2)) Inf_i(F) <5 Inf_i(F).       (1)

The same argument works for any hereditary phase derivative gap eta with sqrt(2) replaced by eta^-1/2. The relevant gap belongs to the UNACTIVATED phases, not to the rare physical branches.

## 2. Activation erasure and full shared-query price

For any Boolean phase w and one shared query, let m=Ew, a=what(i), d=Inf_i(w). Enumerating empty/nonempty control frequencies of V=1+A(w-1) gives exactly

    B_i(V)=p B_i(w)+E,
    E=Phi((1-p+pm)^2,p^2a^2)
            +p(1-p)Phi((m-1)^2,a^2)-p Phi(m^2,a^2).

The scalar envelope and |a|<=d imply E<=6pd. This is the same activation formula used by A077 section4, re-derived here. For a quadratic phase, B_i(w)<=1<=2d whenever relevant, and zero if irrelevant. Therefore B_i(G)<=8pd, B_i(H)<=8qe. Keeping both inherited half-core bills and adding (1) yields

    B_i(F) <=(10+2sqrt(2)) Inf_i(F) <13 Inf_i(F).   (2)

Both p and q are fixed through all shared restrictions. This is why the local payment is hereditary along the selected shared-first policy despite arbitrarily rare physical influences.

## 3. Private-control suffix

Once both shared phases are constant, each branch is either constant or a point-defect sign on its own remaining private control block. The two private blocks are disjoint. A point-defect sign has erasure <=3 times every relevant influence: with l>=2 controls and delta=2^(1-l), its exact erasure is Phi((1-delta)^2,delta^2)+2delta(1-delta)<=3delta; l=1 has zero erasure. Restrictions preserve this class.

At a private query the other core has only its constant common coefficient. The exact symmetric-shift comparison gives |D_i|<=Inf_i(queried core)=2Inf_i(F). Thus

    B_i(F)<=5 Inf_i(F)                             (3)

through any adaptive private-control suffix. After all data are fixed the wrapper is a constant or character of z, with zero entropy and zero selector erasure/JS. A final selector query may make leaves constant without adding entropy cost.

## 4. Complete entropy ledger and one reserve

The exact common-frequency potential is

    R=2-sum_C(g_C^2+h_C^2)
      +sum_C[phi((g_C+h_C)^2/4)+phi((g_C-h_C)^2/4)
                          -(phi(g_C^2)+phi(h_C^2))/2],
    H(F)=(H(G)+H(H))/2+R.

At every stopped leaf this is the actual half-sum of both core entropies plus the actual R_leaf, not a free terminal certificate. R>=0 follows by querying the physical selector. For any physical split Delta_i H=B_i+JS_i and 0<=JS_i<=2Inf_i/ln2. Subtracting both inherited core decrements gives a JS difference of magnitude at most 2Inf_i(F)/ln2, since both nonnegative quantities lie in the same interval.

Put K_S=2+2sqrt(2)+2/ln2<8 and K_C=2+2/ln2<5. Along any allowed prefix,

    |R_root-E R_leaf| <=K_S P_S+K_C P_C,             (4)

where P_S,P_C are the actual consumed shared/private-control influences. Completing the data leaves R=0, hence

    0<=R_root<=K_S I_S(F)+K_C I_C(F).

At any stop, the remaining selector potential is paid from the SAME remaining K_S/K_C data budget by the corresponding continuation. There is no reset of a root profile or extra per-core allowance. The prefix satisfies the full terminal-inclusive entropy bound

    H(F_root)<=E H(F_leaf)
          +(10+2sqrt(2)+2/ln2)P_S+(5+2/ln2)P_C.     (5)

After optional cost-zero final selector completion, all leaf entropies vanish. Therefore this entire actual Boolean class has

    H(F)<16 I_data(F)<=16 I(F)

whenever data influence is positive; the zero-data case has H=0. More precisely its erasure tree costs <=(10+2sqrt(2))I_S+5I_C. This is a provable shared-first policy, not an all-query or all-order price.

The physical resources are exactly

    I_S=(p I(u)+q I(v))/2,
    I_C=[rp(1-Eu)+tq(1-Ev)]/2,
    Inf_z=[p(1-Eu)+q(1-Ev)-pq(1-Eu-Ev+Euv)]/2.

Correlated shared phases enter Euv in the selector resource and coherent row amplitudes; no disjoint composition identity is substituted for them.

## 5. Arbitrarily weak branches beyond stable norm/gap admission

Take k even, u the paired quadratic bent sign, v=u chi_{s1}, r=t=k. Both phase means are b=2^-k/2, Euv=0, p=q=2^-k, and I(u)=I(v)=k/2. Thus I_S=kp/2, I_C=kp(1-b), Inf_z=p(1-b)-p^2(1-2b)/2. Every physical influence tends to zero, and total I tends to zero. Fully private-fixed shared slices have Fourier norm 2^(k/2), so no uniform hereditary norm L applies. Nor do the activated branches have a uniform relevant-influence gap: shared influence p/2 tends to zero. Nevertheless (1)-(5) pay the selected shared-first policy with absolute constants, using the phase gap and Cauchy-Schwarz instead of a root-profile reset. These are actual Boolean definitions in all dimensions, not assumed spectral laws.

## 6. Proof lemmas and honest frontier

The envelope Phi(a^2,b^2)<=2|ab| follows by homogeneity from monotonicity of Phi_nat(1,t^2)/(2t) on (0,1]: its derivative numerator (t^2-1)ln(1+t^2)-t^2ln(t^2)>=0 using ln(1+x)<=x and -ln x>=1-x. The private-row upper/lower comparisons follow by integrating the symmetric logarithmic ratio bounded by (1+v^2/t)^2, as proved in our previous norm theorem. The JS scalar bound follows from [(1+t)ln(1+t)+(1-t)ln(1-t)]/2<=1-sqrt(1-t^2). The quadratic derivative gap follows because a nonzero affine F2 derivative is constant one or balanced. These prove all price lemmas without an external theorem premise.

The first unsupported extension is a private-control reveal while both shared phases remain nonconstant, or replacement by arbitrary phases with rare derivatives: the fixed p,q<=1/2 and phase-gap payment are then not the stated mechanism. A077's geometric eligibility mark pays a different common-activation family; it is not silently available for these independent activations. The shortest next test is one control reveal before shared completion, with its original mismatch mark, exact signed child surplus, and both terminal cores retained. Universal C019 and full FEI remain open.
