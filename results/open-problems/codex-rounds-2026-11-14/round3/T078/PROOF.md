# Sharp field selection from a magnetization tail

The result below concerns a scalar probability law. Its application to the quantum model is conditional on a zero-field magnetization tail. It does not establish that tail.

## Proposition

Let V>0, 0<L<=1, and let M be a real random variable with

    -V/2 <= M <= V/2,       P(M >= V/4) >= L.

For b>=0 define

    m_b = E[M exp(bM)] / E[exp(bM)],       z = bV/8.

The assertion m_b>=V/8 holds for every probability law satisfying these assumptions if and only if the appropriate condition below holds:

    0 <= z <= 1/5:     exp(6z) >= 5(1-L)/L;
    z >= 1/5:          z exp(z) >= (1-L)/(eL).

Both conditions agree at z=1/5. Failure of the relevant condition is witnessed by a law supported on two points. This optimality is over all scalar laws on the given interval; it does not assert optimality over the discrete spectra of spin systems.

### Proof

Set Y=8M/V. Then -4<=Y<=4, P(Y>=2)>=L, and

    m_b >= V/8  iff  E[(Y-1) exp(zY)] >= 0,                 (1)

since the exponential denominator is strictly positive. All expectations exist because Y is bounded. Write

    f_z(y) = (y-1) exp(zy).

On [2,4], differentiation gives

    f_z'(y) = exp(zy)[1+z(y-1)] > 0,

so f_z(y)>=exp(2z). To minimize f_z on [-4,2), only y<1 matters, because f_z(1)=0 and f_z is nonnegative for y>=1.

If 0<=z<=1/5, then 1+z(y-1)>=1-5z>=0 on [-4,1]. Thus

    min_{-4<=y<2} f_z(y) = f_z(-4) = -5 exp(-4z).          (2)

If z>=1/5, the unique critical point in [-4,1) is

    a_z = 1-1/z.

The derivative is nonpositive to its left and nonnegative to its right. Therefore

    min_{-4<=y<2} f_z(y) = f_z(a_z) = -exp(z-1)/z.         (3)

The expression at z=1/5 is interpreted by either formula and gives a_z=-4. Formula (3) is used only for positive z.

Let p=P(Y>=2), let A=exp(2z), and let B denote the minimum in (2) or (3). Then B<0<A and

    E[f_z(Y)] >= pA+(1-p)B >= LA+(1-L)B,                 (4)

where the last inequality follows from p>=L and A-B>0.

For 0<=z<=1/5, nonnegativity of the last expression in (4) is equivalent to

    L exp(2z) >= 5(1-L) exp(-4z),

which gives the first stated condition. For z>=1/5 it is equivalent to

    L exp(2z) >= (1-L) exp(z-1)/z,

which gives the second condition. No division by 1-L is needed, so L=1 is included.

Conversely, give Y mass L at 2 and mass 1-L at -4 in the first regime, or at a_z in the second. These laws meet all support and tail assumptions. Both inequalities in (4) are then equalities. If the proposed condition fails, (1) fails. This proves necessity, sufficiency, and the two-point sharpness assertion.

## An explicit sufficient condition

For all 0<L<=1, the simpler condition

    bV >= 8 log(1/L)                                     (5)

implies m_b>=V/8.

Here is a separate proof that also checks the factor 8. For z>0 put

    F(z)=E[exp(zY)],       g(z)=log F(z).

Differentiation under the expectation is valid on every bounded z-interval because Y is bounded. Direct calculation gives

    g'(z)=E_z[Y],       g''(z)=E_z[Y^2]-E_z[Y]^2>=0,

where E_z is exponential tilting by exp(zY). Since g(0)=0 and g' is increasing,

    g(z)=integral_0^z g'(t) dt <= z g'(z).

The tail assumption gives F(z)>=L exp(2z), hence

    E_z[Y]=g'(z)>=g(z)/z>=2+log(L)/z.

If z>=log(1/L), the last expression is at least 1. This is precisely (5). If z=0 can satisfy (5), then L=1 and Y>=2 almost surely, so the conclusion holds directly.

## Exact checks of the constants and equality cases

1. At z=0 the first criterion reduces to L>=5/6. At equality the extremal law has M=V/4 with probability 5/6 and M=-V/2 with probability 1/6. Its mean is

       (5/6)(V/4)+(1/6)(-V/2)=5V/24-V/12=V/8.

   Independently, the minimum unweighted mean under the tail assumption is L(V/4)+(1-L)(-V/2)=V(3L/4-1/2), which reaches V/8 exactly at L=5/6.

2. At the regime boundary z=1/5, both formulas give

       L >= L_* := 5/(5+exp(6/5)).

   For the second formula, substituting (1-L_*)/L_*=exp(6/5)/5 gives the same equality z exp(z)=exp(1/5)/5. The two minimizing locations also agree: 1-1/z=-4.

3. At z=1 take L=1/(1+e^2). The second condition is an equality. The extremal law has M=0 or V/4. Tilting with bV=8 multiplies the upper atom's weight by e^2, making the two tilted weights equal. Their mean is V/8. This checks the interior minimizer and the factor e in the second criterion without differentiating f_z.

4. For L=1 the support lies entirely above V/4, so every b>=0 works. Both criteria confirm this. At fixed z each criterion can be made false by taking L sufficiently small; a tail mass cannot be omitted from the hypothesis.

An independent derivation of the maximizer uses the two-point laws directly. For a lower atom a<1 and upper atom 2, the tilted mean is at least 1 exactly when

    (1-a) exp(z(a-2)) <= L/(1-L),                         (6)

assuming L<1. The logarithmic derivative of the left side with respect to a is z-1/(1-a), and its second logarithmic derivative is -1/(1-a)^2. Thus its maximum on [-4,1) occurs at -4 for z<=1/5 and at 1-1/z for z>=1/5. Substitution in (6) reproduces both criteria. Points a>=1 cannot lower the tilted mean below 1.

## Conditional application to the Heisenberg model

For a finite volume Lambda and spin S, put ell=2S and V=ell|Lambda|. The total z-spin M has spectrum in [-V/2,V/2]. For the isotropic Hamiltonian H, [H,M]=0. Consequently, if P_0 is the spectral distribution of M in the zero-field Gibbs state at inverse temperature beta, then the distribution in field h>=0 is

    dP_h(M) = exp(beta hM) dP_0(M) / E_0[exp(beta hM)].

Indeed, simultaneous diagonalization of the commuting finite-dimensional self-adjoint operators H and M gives exp[-beta(H-hM)]=exp(-beta H)exp(beta hM). Taking traces on each M-eigenspace gives the displayed law.

Therefore, assuming P_0(M>=V/4)>=L, condition

    beta hV >= 8 log(1/L)

implies <M>_{beta,h}>=V/8=|Lambda|S/4. The proposition gives the exact universal scalar condition if the sharper implicit criterion is desired.

The released source's field-selection step instead requires

    L^(-1) exp(-beta hV/16) <= 1/11,

equivalently beta hV>=16 log(11/L). The implication above supplies a smaller sufficient field for every 0<L<=1.

In particular, if an independent argument supplies L=(1/2)exp(-A), A>=0, it suffices that

    beta hV >= 8(A+log 2).

For cubes in dimension D, a conditional tail cost A<=C|boundary Lambda|, with fixed C, gives sufficient field

    h >= 8[C|boundary Lambda|+log 2]/[beta ell|Lambda|].

This tends to zero because the boundary-to-volume ratio tends to zero. It proves finite-volume field selection from the assumed surface tail; the construction and equilibrium properties of an infinite-volume limit require additional arguments.

## Source of the comparison

OpenAI, *Spontaneous magnetization in the quantum Heisenberg ferromagnet*, September 24, 2026. The manuscript's theorem has been opened at its [PDF copy](https://mathcommunity.github.io/oai-math-revised/papers/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/paper.pdf). The scalar selection hypotheses and constants compared above are in [PhysicalTilt.lean](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/Heisenberg/PhysicalTilt.lean), `matrix_tilt_mean`; their use in the ordering theorem is in [CubeSelection.lean](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/Heisenberg/CubeSelection.lean), `field_ordered_cubes`. The scalar proposition is derived in full above. No claim of priority is made for this elementary extremal calculation.
