# Actual-charge payment in the failed-truncation corner

This is a continuation and repair of the existing prime56067 sharp-payment route, not a new universal FEI claim. All logarithms are natural. The proof is by the author; independent review remains pending.

## Statement and actual packet owners

Let a,x,y,z be independent Bernoulli coordinates of interior probabilities alpha,e,d,q. Consider the actual Boolean sign

    f=-1+2z+2xy-2z[ax+(1-a)y].

Put u=4alpha(1-alpha), vx=4e(1-e), vy=4d(1-d), w=4q(1-q), Tx=u vx w/16, Ty=u vy w/16, and T=Tx+Ty>0. In the biased orthonormal spectrum, these are precisely the two triple masses; there is no fourth-degree mass. Thus R=T, and Delta=B+2T, where B is the sum of pair masses. Write E for the corrected nonempty Fourier entropy, E_1 for its singleton part, and S=4Delta-2T-E_1. The original joint-spectrum owners are retained throughout.

For 0<d<=e<1 define

    K(alpha,e,d,q)=2sqrt(q)+2sqrt(alpha)
                   +2d/[e(1-e)]+2sqrt(e)/(1-e).

Then the actual higher-degree excess G satisfies

    G <= K(alpha,e,d,q) T.                                  (1)

In particular, on the full four-dimensional collar

    0<alpha,q,e<=1/16,       0<d<=e/16,                      (2)

one has G<=5T/3 and

    (4+ln4)Delta-E = S+2T-G >= S+T/3 >= T/3.                (3)

The swapped collar, obtained by alpha -> 1-alpha and e <-> d, has the same conclusion. Formula (3) also holds with S replaced on its right by any S_m, m>=0, from the existing reserve hierarchy. No approximation tail is spent in this payment: G<=2T by itself suffices here.

## Scalar estimates

For 0<t<=1 put A(t)=t ln(1/t)/(1-t), with A(1)=1, and h(t)=2t^2 ln(1/t), with h(0)=0. The elementary inequality

    ln r <= sqrt(r)-1/sqrt(r),   r>=1,

follows because the derivative of the right side minus ln r is (sqrt(r)-1)^2/(2r^(3/2))>=0, and the difference vanishes at r=1. Taking r=1/t gives

    A(t)<=sqrt(t),       h(t)<=2t^(3/2)(1-t).               (4)

Also ln r<=r-1 gives A(t)<=1 and h(t)<=2t(1-t). These bounds extend continuously to endpoints when needed. They imply the familiar Boolean singleton reserve S>=0: for D_i=(f|i=1-f|i=0)/2 in {-1,0,1}, let c_i=E D_i, d_i=E D_i^2 and t_i=|c_i|. Booleanity gives d_i>=t_i, and the exact variance identity yields

    S=sum_i v_i[2(d_i-t_i)+2t_i(1-t_i)-h(t_i)]>=0.

Here sum_i v_i Var(D_i)=2Delta-R, by counting each actual Fourier packet |A| times. Thus this use of reserve creates no constituent bank and no duplicate ownership.

## Ledger reconstruction and payment

Writing each Fourier coefficient as sqrt(product v_i) times c_A, direct centered derivatives give singleton coefficients

    q(d-e), d-q alpha, e-q(1-alpha),
    1-alpha e-(1-alpha)d,

pair coefficients in order ax,ay,az,xy,xz,yz

    -q/2, q/2, (d-e)/2, 1/2, -alpha/2, -(1-alpha)/2,

and triple coefficients c_axz=-1/4, c_ayz=1/4; the remaining coefficients of degree at least three vanish. Thus each pair has baseline ln4 times its mass, while each triple contributes ln16 times its mass. After collecting these ORIGINAL pair masses, the exact identity is

    E_ge2 = ln4 Delta+G,
    G=2T A(q)+2Tx A(alpha)+2Ty A(1-alpha)+(uw/4)h(d-e).     (5)

For example, ax and ay together contribute 2T A(q) beyond their pair baseline, because w=4q(1-q); xz and yz similarly give the two alpha terms. The az pair gives (uw/4)h(d-e). These computations use h(|d-e|) when d>e. Nothing is conditioned on a truncated spectrum.

For d<=e let r=e-d. Divide (5) by T. By (4), A(1-alpha)<=1, and Tx/T<=1,

    G/T <= 2sqrt(q)+2sqrt(alpha)
           +2vy/(vx+vy)+4h(r)/(vx+vy).

Since vy<=4d and vx+vy>=4e(1-e), the third term is at most 2d/[e(1-e)]. Since 0<=r<=e, (4) gives h(r)<=2r^(3/2)<=2e^(3/2), so the fourth term is at most 2sqrt(e)/(1-e). This proves (1).

On (2), the first two terms total at most 1. The third is at most 2/15, and the fourth is at most 8/15. Hence K<=1+2/15+8/15=5/3. Substituting into the exact residual identity proves (3). Interchanging x,y and replacing alpha by 1-alpha leaves the Boolean polynomial unchanged, proving the swapped assertion.

## Repair of the all-fixed-order obstruction

The previous stage established for this same prime and every fixed m that along

    (alpha,e,d,q)=(t,t^2,t^4,t),     t->0,

one has (S_m-4T)/T -> -4/(m+1). Every t in (0,1/16] on that path satisfies (2), since d/e=t^2<=1/256. Therefore the actual sharp residual is at least T/3 throughout this explicit interval, even where all sufficiently thin fixed-m fixtures violate S_m>=4T. The false sufficient surrogate is not needed. The stronger certificate S_m+2T-G>=T/3 holds for every m, because S_m>=0.

The general adaptive criterion K<=2 can be used beyond the rectangular collar, and K<=2-eta gives residual at least S+eta T. It is sufficient only. For example, at all four fair biases (5) gives G/T=4ln2>2, so the reserve-free assertion G<=2T is false globally. This control does not refute G<=S+2T.

## First unsupported line and universal scope

The first unsupported line remains G<=S+2T for ALL interior four-bias laws outside regions paid by (1) or by other already proved bounds. No finite grid proves that extension. The all-arity bridge remains a uniform corrected FEI+ theorem on genuine disjoint-composition primes at their actual induced product biases. Such a common bound transfers by the exact nonnegative-weight entropy/deficit composition identities, as established in earlier A043 stages and rederived by the lead. This collar proof supplies neither a uniform theorem on all primes nor full FEI.

The logarithm inequalities and the continuum derivation above are analytic author proofs. The checker uses independent vertex sums, rational arithmetic and outward logarithm intervals to test coefficients, identities and signs on a frozen finite domain. That check is not a formalization or independent human review of the continuum theorem.
