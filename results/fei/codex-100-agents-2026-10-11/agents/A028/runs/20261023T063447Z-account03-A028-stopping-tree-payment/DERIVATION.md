# v8: fixed original controller reference, changing nonempty profile

All entropies/KL use bits. Physical blocks Y,X are independent uniform cubes. Boolean a(Y),G(X),H(X) may be arbitrary, and G,H may share all X. Let c=(1-a)/2, p=Ec, V=Var(a), gamma=Pr(G!=H), f=(1-c)G+cH. At a physical history retain all three actual restricted functions and normalized references Ra,Rg,Rh positive on their respective true squared Fourier supports. Each reference inherits through its OWN actual function's phase-sensitive pair channel when its block is queried; it stays fixed on the other block. Reference-only zero pairs use a fair outcome kernel. References retain all off-target mass and actual reference branch normalizers. Controller reference is fixed at the root; there is no fresh supplier at a descendant.

## 1. Exact nonempty-profile target

Write Pa for the actual controller squared spectrum, A(U)=Pa(U)/V on nonempty U if V>0, beta=1-Ra(empty), and B(U)=Ra(U)/beta on nonempty U if beta>0. Positivity gives beta>0 when V>0. When V=0 all following nonempty costs are zero; a zero-mass conditional law is unused.

For data t put g=Ghat(t), h=Hhat(t), q_t=(1-p)g^2+p h^2, r_t=(1-p)Rg(t)+p Rh(t), z_t=(1-p)g+p h, w_t=V(g-h)^2/4. Parseval over Y gives Pf(empty,t)=z_t^2, Pf(U,t)=w_t A(U), q_t=z_t^2+w_t, sum_t w_t=V gamma.

Prescribe the changed output reference Q by

    Q(empty,t)=r_t z_t^2/q_t,
    Q(U,t)=r_t (w_t/q_t) B(U), U nonempty.

At q_t=0 put all row mass r_t at U=empty. Thus Q preserves the actual empty-versus-nonempty row probabilities but replaces the TRUE conditional nonempty shape A by the inherited, externally supplied B. This is a genuine nonempty-profile change whenever A!=B and gamma V>0. No fresh law is chosen after inspecting unused credit.

Let Ddata=D(q||r), Wdata=(1-p)D(Pg||Rg)+pD(Ph||Rh), Z=Wdata-Ddata>=0. Then

    Dstar=D(Pf||Q)=Ddata+gamma V D(A||B).                 (1)

The reference on the controller has exact vacuum/nonempty KL decomposition

    Da=D(Pa||Ra)=Cvac+V D(A||B),
    Cvac=D(Bern(V)||Bern(beta))>=0.                      (2)

All endpoint terms use standard 0 log conventions; support positivity makes the terms finite. In particular V=0 gives Da=Cvac, even when inherited Ra has nonempty off-target mass. Combining (1)-(2),

    T=Wdata+gamma Da,
    S=Z+gamma Cvac>=0,
    Dstar=T-S.                                         (3)

This is the extra vacuum slack missing if one simply treats conditional nonempty KL as a conserved controller account.

## 2. Physical contraction of the ONE original account

For any Boolean source u, pair its coefficients alpha=uhat(T), beta=uhat(T+i). Erase queried spectral membership and send either member to outcome b with probability (alpha+(-1)^b beta)^2/[2(alpha^2+beta^2)]; use1/2 on a zero actual pair. If the reference branch masses are rho0,rho1, normalize each child reference by its own rho_b. True physical branch masses are1/2. Pair erasure and KL chain rule give

    Du_parent = Eu+Ou+(Du_child0+Du_child1)/2,
    Eu>=0, Ou=D(fair||rho)>=0.                          (4)

At DATA queries, Da is unchanged and gamma is exactly harmonic under physical restriction, so gamma Da is harmonic. Wdata contracts by the same weighted source E/O releases as in v7. At CONTROL queries, gamma and both source references/functions stay fixed, Wdata is affine in the harmonic p, and Da contracts by (4). Therefore

    Atot_v=T_v-average T_children>=0                    (5)

for EVERY physical query and every history. In formulas Atot=(1-p)(Eg+Og)+p(Eh+Oh) on DATA and Atot=gamma(Ea+Oa) on CONTROL. This does not assume gamma is independent of the DATA outcome: its actual harmonic identity is what is used.

## 3. Full mixed-tree payment and actual output resets

Put sigma_v=average Dstar_children-Dstar_v. Equation(3) gives sigma=S-average S_children-Atot. For every finite adaptive mixed stopping tree with actual physical reach weights,

    sum_v reach sigma_v + sum_v reach Atot_v
      + E_leaf S_leaf = S_root.                        (6)

The actual complete nonnegative entropy path cost DeltaH=H(f)-average H(f_child) and the complete changed-reference terminal CE satisfy

    sum_v reach DeltaH_v + E_leaf CE(Pf,Q)
      = H(f_root)+E_leaf Dstar
      = H(f_root)+T_root-sum_v reach Atot_v-E_leaf S
      <=H(f_root)+Wdata_root+gamma_root Da_root.        (7)

DeltaH=B_i+JS_i>=B_i>=0, so (7) also pays the erasure path cost. Both children and all terminal KL bills remain in (6)-(7). Negative decomposed transactions are retained.

If Q at a node is transported through the actual OUTPUT physical pair channel, yielding inherited Q_b^inh and output refunds Ef,Of, its raw reconstruction cost kappa=average[D(P_child||Q_child)-D(P_child||Q_b^inh)] is exactly sigma+Ef+Of by(4). Only net kappa-Ef-Of=sigma is charged in(6). No assertion bounds positive raw resets by Sroot.

## 4. Root calibration, same JS slack, and influence units

At the root only, suppose Ra(empty)=Pa(empty)=1-V. Then Cvac_root=0 and Da_root=V D(A||B). If also Rg=Rh at the root, S_root=Z_root=J_root=JS_p(Pg,Ph) EXACTLY. Descendants may have different Rg,Rh and uncalibrated Ra; replacing S by a fresh JS there is invalid. The additional controller-shape debt gamma Da was already included once in the ORIGINAL Troot allowance. It is not free JS credit, and is never renewed.

Given the v5 scoped surcharge inequality

    Pi=H(f)-weighted source H
      <=gamma Hplus(a)+3 log2(e) gamma I(a)+(V/2)I(GH),

the ORIGINAL full allowance in(7) is bounded by

    weighted source CE + gamma CEplus(a,Ra)
      +3 log2(e)gamma I(a)+(V/2)I(GH),                  (8)

where CEplus(a,Ra)=sum_{U!=empty} Pa(U)log2(1/Ra(U))=Hplus(a)+Da under root calibration. Thus supplied source CE rates Lg,Lh and calibrated controller CEplus<=K I(a) give the SAME dimension-independent rate max{K+3log2(e),Lg+2p,Lh+2(1-p)} times I(f). This is conditional on genuine source/controller certificates and the stated v5 surcharge premise. The new reference transport (1)-(7) is independent of that optional premise.

An old debit b requires original U-b>=Hroot+Troot or a valid upper bound(8). At any reached frontier its remaining original credit is exactly U-b-Hroot-Troot+sum prior reach Atot+E_frontier S. Changing the root supplier or issuing a new gamma Da is not allowed.

## 5. First unsupported universal line

Supplying calibrated controller and data CE certificates at dimension-independent influence rates for every Boolean input remains open. Also, Q retains the true DATA-row empty/nonempty ratio w_t/q_t; an externally required change of that ratio or data marginal needs an additional priced KL term. The present theorem pays all nonempty-controller-shape changes induced by one inherited original controller reference, including interleaved DATA histories, but does not pay arbitrary fresh descendant references or assert full FEI.

The extra root liability gamma Da is a real hypothesis, not something supplied by v7. To reuse a pre-existing v7 earmark U with old debit b one must prove gamma Da_root<=U-b-Hroot-Wdata_root (or use an actual reached-frontier reserve). The seven-variable exact receipt below checks this condition against the SAME old rate4 earmark. A dimension-independent controller CEplus supplier is stronger than a plain controller entropy bound; no substitution between them is licensed.

## 6. Exact obstruction to paying a genuine shape change from JS alone

Let a on two controls equal -1 only at00. Its spectrum is Pa=(1/4,1/4,1/4,1/4), V=3/4. Let G(z,d)=z and H(z,d)=-z, with d a physically present dummy data coordinate, so f=a*z, gamma=1, Pg=Ph, and choose Rg=Rh=Pg. Then J=Z=Wdata=0, H(f)=2 and I(f)=2. The original v7 tight allowance is U=Hroot+Wdata=2. Query the dummy d (both full source children are nonconstant), with actual entropy decrement0 and unchanged source references. Now prescribe nonempty controller law B=(1/6,1/3,1/2), keeping the actual controller empty mass1/4 and the exact data marginal. This is the calibrated external Ra=(1/4,1/8,1/4,3/8). Both terminal CE bills increase by

    delta=(3/4) D((1/3,1/3,1/3)||B)
         =(2-log2(3))/4=(1/4)log2(4/3)>0.

Thus original-J-only payment for arbitrary genuine nonempty-profile changes is FALSE even after an actual DATA query, with both nonconstant sources and zero old debit. The new v8 allowance explicitly adds the necessary original liability gamma Da=delta; it cannot be called free or inserted again below the query. Adding any number of dummy data coordinates preserves this obstruction and H/I=1. This is an obstruction to a reference-payment assertion, not a counterexample to FEI or an unbounded entropy-influence family.
