# P0315 — research attempt, 2026-10-11

## Exact target and conventions

For every fixed beta > 0, establish the Forrester–Haldane large-separation
pointwise asymptotic family for the truncated factorial pair density of Sine_beta.
Write T_beta(r) = rho_beta^(2)(0,r) - (2 pi)^(-2) at density (2 pi)^(-1).
For pointwise statements use the continuous representative supplied by
Qu–Valko's Fourier/SDE formula, rather than an arbitrary modification of
a Radon–Nikodym density on a null set.
The predicted leading additive statements are

* beta < 2: T_beta(r) = -1/(pi^2 beta r^2) + o(r^(-2));
* beta = 2: T_2(r) = (cos r - 1)/(2 pi^2 r^2), exactly;
* beta > 2: T_beta(r) = A_beta cos(r) r^(-4/beta) + o(r^(-4/beta)).

The full family has harmonics m with leading powers 4m^2/beta and
successive inverse-distance corrections, plus a nonoscillatory sector starting
with -1/(pi^2 beta r^2). All remainders are additive; a ratio to an oscillating
term is not meaningful at its zeros. Lewin (149) is a summary of the family,
not a definition of arbitrary-order remainder bounds for each descendant.
We do not claim its infinite series converges for fixed r.

Dumaz–Malvy PDF page 3, equation (1.3), gives the three leading regimes;
Lewin PDF page 64, equations (149)–(150), supplies the harmonic family.
Both refer to fixed beta, not a uniform limit as beta tends to zero or infinity.

## 1. Density rescaling (proved)

Let a stationary process of density 1 have factorial pair density p(x,y).
Under dilation x -> Lx its pair density is L^(-2) p(x/L,y/L).
Indeed for disjoint Borel sets A,B the factorial second moment is the old
second moment on A/L,B/L; change both integration variables in its defining
integral. The one-point density changes to L^(-1), so truncation obeys the
same formula. Consequently, for L=2 pi,

    T_DM(r) = (2 pi)^(-2) T_unit(r/(2 pi)).

A unit-density term a_m cos(2 pi m s) s^(-p) becomes
a_m (2 pi)^(p-2) cos(mr) r^(-p). A sine descendant with exponent p+1
instead gains the factor (2 pi)^(p-1). The nonoscillatory inverse-square
coefficient is unchanged. This distinction is essential when comparing amplitudes.

## 2. Beta = 2 (proved special case)

The standard determinantal kernel at unit density is
K(x,y)=sin(pi(x-y))/(pi(x-y)), with diagonal 1. The two by two determinant
is 1-K(x,y)^2, whence T_unit(s)=-sin^2(pi s)/(pi^2 s^2).
The identity 2 sin^2(z)=1-cos(2z) gives both terms of the family exactly.
Rescaling yields T_DM(r)=-sin^2(r/2)/(pi^2 r^2).
At positive multiples of 2 pi this vanishes. This is not a counterexample
to an additive asymptotic expansion.

## 3. General beta: exact hierarchy and formal sector

Set q_k(r)=E exp(ik alpha_r(0)) for the diffusion of Qu–Valko Theorem 1,
and q_0=1. Their representation reads

    T_beta(r) = (2 pi^2)^(-1) sum_{k>=1} w_k Re q_k(r),
    w_k = (-beta/2)_k / (1+beta/2)_k.

The rising factorial convention is used. Their estimate |w_k| <= C_beta
k^(-1-beta) makes this series absolutely and uniformly convergent, because
|q_k|<=1. The diffusion is

    d alpha = (r beta/4) exp(beta u/4) du
              - (beta/2) sin(alpha) du
              + Re[(exp(-i alpha)-1) dZ],  u in (-infinity,0].

Its quadratic variation density is 2(1-cos(alpha)). Ito's formula applied
to exp(ik alpha) therefore gives

    (beta/4) r q_k' = (ik beta r/4 - k^2) q_k
       + (k^2/2 - k beta/4) q_{k+1}
       + (k^2/2 + k beta/4) q_{k-1}.                 (H)

Here is justification of differentiation without interchanging a derivative
with an infinite sum. For a fixed k all Ito drift terms are bounded on a
finite u interval and the martingale coefficient is bounded by 2k, so its
expectation is zero. The time-shift invariance of the entrance solution
identifies E exp(ik alpha_r(u)) with q_k(r exp(beta u/4)). Ito expectation
is thus an integral equation on any compact r interval in (0,infinity).
The moments are continuous by bounded convergence and continuity of the
SDE flow (Qu–Valko Proposition 21); its integrand is continuous. The
fundamental theorem of calculus implies q_k is continuously differentiable
there and gives (H). This reproduces Qu–Valko Proposition 20, not a new
uniqueness theorem for the infinite hierarchy.

Define

    D_k = 4 k^2/beta, A_k = 2 k^2/beta-k, B_k = 2 k^2/beta+k.

Then (H) is r q_k' = ikr q_k - D_k q_k + A_k q_{k+1}+B_k q_{k-1}.
At beta=2n, A_n=0, so the first n equations close. Away from even beta
there is no such finite closure; a numerical cutoff is an additional
boundary condition and is not justified by these equations.

### Formal nonoscillatory sector: existence and uniqueness (proved algebraically)

In formal inverse powers of r impose P_0=1 and
P_k=sum_{j>=1} c_{k,j} r^(-j) for k>=1. Define c_{0,0}=1,
c_{0,j}=0 for j>=1, and c_{k,0}=0 for k>=1.
The constant coefficient of (H) forces

    c_{k,1} = -B_k 1_{k=1}/(ik).

For each j>=1 the coefficient of r^(-j) forces

    ik c_{k,j+1} = (D_k-j)c_{k,j}
                  - A_k c_{k+1,j} - B_k c_{k-1,j}.    (R)

Since ik!=0 for k>=1, this determines a unique coefficient array.
Conversely coefficients defined this way satisfy every formal coefficient
equation, proving existence. Induction gives c_{k,j}=0 for k>j:
the base column has support k=1, and the next column can extend support
by only one through c_{k-1,j}. Consequently every coefficient of
sum w_k P_k is a finite sum. This is a well-defined FORMAL series even
without any convergence estimate for the coefficient arrays.
For real beta, each column alternates parity: c_{k,j} is purely imaginary
for odd j and real for even j. This follows at j=1 and is preserved by
the real recurrence divided by ik. Thus the real formal series has only
even powers.

Put a=1+2/beta. The first two nonzero columns give

    c_{1,1}=ia,
    c_{1,2}=a(4/beta-1),
    c_{2,2}=-(4/beta+1)a.

The only contributions to the real inverse-square coefficient are k=1,2.
With w_1=-beta/(beta+2),
w_2=beta(beta-2)/((beta+2)(beta+4)), direct simplification gives

    w_1 c_{1,2} = 1-4/beta,
    w_2 c_{2,2} = -(beta-2)/beta,
    sum = -2/beta.

Multiplication by (2 pi^2)^(-1) yields exactly -1/(pi^2 beta).
This finite cancellation is also submitted to Lean in Coefficient.lean;
the actual checker result is recorded in lean_check.txt. Formal coefficients
are not evidence of an actual asymptotic remainder. In particular we
have NOT proved T_beta(r)=-1/(pi^2 beta r^2)+o(r^(-2)) for general beta<2.

### Formal mode exponents (proved as a necessary algebraic condition)

Consider a homogeneous formal ansatz (q_0=0)

    h_k(r)= exp(i m r) r^(-p) (v_k + O_formal(r^(-1))), m>=1,

with nonzero leading vector v. The terms one power larger force
i(m-k)v_k=0 for each k>=1. Therefore v is supported at k=m.
The terms of order exp(imr)r^(-p) in equation k=m then force
-p v_m=-D_m v_m, since the neighbors have zero leading coefficient and
the diagonal frequency cancels even for the next-order coefficient.
Thus p=4m^2/beta. This establishes the necessary exponent for this
specified formal ansatz; it does not establish that these modes exhaust
the actual solution, exist as functions with remainders, or have the
predicted phase/amplitude. In particular arbitrary formal mode amplitudes
remain undetermined by analysis at infinity.

### A quantitative obstruction to using uniform convergence alone (proved)

The weight bound and |q_k|<=1 imply for every integer K>=1

    |sum_{k>K} w_k Re q_k(r)| <= C_beta sum_{k>K} k^(-1-beta)
                             <= (C_beta/beta) K^(-beta),

uniformly in r, by comparison with the integral from K to infinity.
To guarantee this upper bound is o(r^(-N)), one can take
K(r)/r^(N/beta) -> infinity. A fixed-mode asymptotic estimate with
constants depending on k does not provide estimates for that moving
cutoff. For even beta the weights terminate and this difficulty disappears;
it remains a real missing estimate for non-even beta. This observation
is an obstruction to this proof method, not an impossibility theorem.

## 4. Beta = 4: full classical asymptotic mechanism (proved special case)

Qu–Valko (14) gives at density (2 pi)^(-1), with r>0,

    4 pi^2 T_4(r) = -sin^2(r)/r^2
              + (cos(r)/r - sin(r)/r^2) Si(r),
    Si(r) = integral_0^r sin(t)/t dt.

We now justify the tail expansion including a quantitative remainder.
First integral_0^infinity sin(t)/t dt=pi/2: inserting exp(-epsilon t),
differentiate the integral with respect to the sine frequency b. The
derivative is epsilon/(epsilon^2+b^2), justified by exponential domination.
Integration from b=0 to b=1 gives arctan(1/epsilon). To pass epsilon down
to zero, integrate by parts on [R,infinity): both damped and undamped
tails are bounded by 2/R, uniformly in epsilon>=0, because exp(-epsilon t)/t
is decreasing. The compact integral converges by dominated convergence.
Hence its undamped value is pi/2.

Write F_n(r)=integral_r^infinity exp(it)t^(-n) dt for n>=1, with n=1
interpreted as an improper integral. Integration by parts gives

    F_n = i exp(ir) r^(-n) - i n F_{n+1},
    |F_n| <= 2 r^(-n).

For the bound, the boundary term is at most r^(-n) and the integral of
the derivative magnitude is also r^(-n). After L steps the remainder
in F_1 has magnitude at most 2 L! r^(-L-1).
Taking imaginary parts gives, for L=3,

    J(r):=pi/2-Si(r)
       = cos(r)/r + sin(r)/r^2 - 2 cos(r)/r^3 + E(r),
    |E(r)| <= 12/r^4.                               (J3)

Substitute Si=pi/2-J into the exact beta=4 formula and multiply out.
With c=cos(r), s=sin(r),

    4 pi^2 T_4(r) = pi c/(2r) - (1+pi s/2)/r^2
                    + (2c^2+s^2)/r^4 + R(r),
    |R(r)| <= 26/r^5, r>=1.                        (B4)

Indeed the finite product equals
-1/r^2+(2c^2+s^2)/r^4-2sc/r^5 after removing the pi/2 part;
the omitted E contribution has magnitude <=(1/r+1/r^2)12/r^4
<=24/r^5, while 2|sc|/r^5<=2/r^5. Thus (B4) is an explicit
uniform additive remainder bound. The sine-squared identity rewrites
2c^2+s^2=(3+cos(2r))/2. Repeating the F_n recursion proves arbitrary
orders of this beta=4 asymptotic expansion with finite factorial error
constants. No convergence of its infinite asymptotic series is required.

The leading terms are

    T_4(r)=cos(r)/(8 pi r) -1/(4 pi^2 r^2)
            -sin(r)/(8 pi r^2) + O(r^(-4)).

At unit density this becomes exactly the beta=4 expression in Lewin (148).
The r^(-4) terms split into a nonoscillatory term and harmonic m=2,
matching its predicted exponent 4m^2/beta=4.

## 5. Beta = 1: a missing sine descendant in the survey (proved special case)

Qiu–Qu–Yuan–Valko–Venancio (2026), equation (2), PDF p. 2,
records the exact classical beta=1 formula. At z=r/2>0 it gives

    4 pi^2 T_1(r) = -sin^2(z)/z^2
                     -(cos(z)/z-sin(z)/z^2) J(z).

The integration-by-parts argument above with L=4 yields
J(z)=c/z+s/z^2-2c/z^3-6s/z^4+E_4, |E_4|<=48/z^5.
Multiplication gives

    4 pi^2 T_1(r) = -1/z^2 + (3+cos(2z))/(2z^4)
                    +2 sin(2z)/z^5 + R_1(z),
    |R_1(z)|<=102/z^6, z>=1.

Indeed the displayed polynomial product leaves -6s^2/z^6, and the
E_4 product is bounded by 96/z^6. At unit density z=pi x, this is

    T_1,unit(x) = -1/(pi^2 x^2)
        +(3+cos(2 pi x))/(2 pi^4 x^4)
        +2 sin(2 pi x)/(pi^5 x^5)+O(x^(-6)).

Thus Lewin (148), as printed in the downloaded survey, omits the fifth-order
sine term while claiming O(x^(-6)). Along x=n+1/4, the difference
between its displayed terms and the exact formula, multiplied by x^5,
tends to 2/pi^5, so that printed remainder cannot be correct literally.
The correct error after just its first two displayed terms is O(x^(-5)).
This is an error in a special-case summary, NOT a counterexample to the
Forrester–Haldane family: the missing term is precisely its m=1 sine
descendant, with exponent 4/beta+1=5 at beta=1. The same recursion proves
arbitrary orders with explicit error constants in this classical case.

## 6. A literal truncation caveat in Lewin (149)

The post-source beta=6 paper, Proposition 2, PDF p. 3, includes the nonzero
term -Gamma(1/3)^2 (64/729) cos(r) r^(-8/3) in 4 pi^2 rho_6^(2).
This is a second descendant of harmonic m=1. Lewin (149) displays only
the first cosine/sine pair for each harmonic and a global O(r^(-4)).
If that is read literally as an exact truncation, this omitted descendant
has larger order than r^(-4), and hence cannot be placed in that remainder.
Therefore the intended target here is the complete asymptotic family,
including descendants to the specified order. The user explicitly asks
for that family; disproving a shorthand truncation would not answer it.

## 7. Computation and hostile-referee checklist

check_math.py uses 80-digit mpmath arithmetic to check (B4) at eight
distances including 1, 3, 10, 100, 1000, a multiple of pi, a nearby
distance, and a zero of cosine. Every residual satisfies its explicit
26/r^5 bound. Sympy independently computes the formal recurrence
through fourth order and verifies finite support and the weighted
inverse-square coefficient. It obtains the fourth-order formal coefficient
12(beta-2)^2/beta^3 before multiplication by 1/(2 pi^2).
This last value is a computer-algebra consistency check, not a claimed
general-beta analytic asymptotic. Results are saved in checks.json.
check_beta1.py independently verifies the explicit beta=1 remainder at
seven distances with 80-digit arithmetic. Along z=n pi+pi/4 it checks
that z^5 times the survey's omitted residual approaches 2, as proved
above. No stochastic sampling is used. These calculations take seconds,
use small coefficient arrays, and have no large-memory jobs.

Lean 4 checked Coefficient.lean with exit code 0 using `lake env lean
~/brain_workers/TRIO_1011/op/P0315/Coefficient.lean` from
~/lean_verify. The proof uses field_simp and ring, no sorry,
no native_decide. Only the rational coefficient identity is formalized;
none of the analytic asymptotic claims is presented as Lean-checked.
The first run failed because the minimal imports lacked Real.Basic;
adding that import and explicit nonzero denominator hypotheses fixed it.

### Why signed local averages do not by themselves give pointwise decay

For r>=1 and lambda>=0, integration by parts gives

    integral_r^(r+lambda) exp(it^2) dt
      = [exp(it^2)/(2it)]_r^(r+lambda)
        + integral_r^(r+lambda) exp(it^2)/(2it^2) dt.

The sum of the bounds on these terms is exactly 1/r. Thus the smooth,
bounded, even function f(r)=sin(r^2) has signed local averages bounded
by 1/r uniformly in lambda, but f(sqrt(pi/2+2 pi n))=1 for all n>=0.
This disproves a general inference from signed local-average estimates
plus continuity to pointwise decay. It is NOT proposed as a point-process
pair density; realizability would require additional constraints. The
example diagnoses a missing implication, not a counterexample to P0315.

* Pair densities are factorial densities off the diagonal. No delta mass
  from self-counting is included; a self-count covariance would be different.
* Both coordinates must be rescaled; amplitudes change by exponent-dependent
  factors. Section 1 proves this rather than guessing from frequency.
* A leading oscillatory expression requires additive remainders at zeros.
* The source's characterization of Qu–Valko is checked against its actual
  theorem; an upper bound is not an equivalent or a coefficient formula.
* Formal recurrence is uniquely solvable coefficient by coefficient but
  this does not imply uniqueness of an infinite ODE solution or its
  asymptotic representation. Qu–Valko explicitly list that uniqueness as
  an open question. We do not assume it.
* The infinite Fourier sum is uniformly convergent at fixed scale; one
  cannot exchange it with an inverse-distance expansion without weighted
  remainder control. The moving-cutoff calculation quantifies the gap.
* Mode exponents leave amplitudes and phases unknown; symmetry alone was
  not used to claim that the leading term is a cosine with known phase.
* The beta=4 tail remainder was proved by integration by parts, and is
  checked at generic phases and near zeros with high-precision arithmetic.
* No Monte Carlo evidence is interpreted as a proof. No general-beta
  moment truncation was used as a claimed numerical solution.

## Remaining gap

**Update after the second attempt:** SECOND_ATTEMPT.md contains a new
actual small-beta decay bound and uniqueness within probability-valued
solutions of the moment hierarchy. At density (2pi)^(-1), it proves
|T_beta(r)|<=C_beta r^(-kappa), with kappa=2-4beta for 0<beta<=1/3
and kappa=(1-beta)^2/(2beta) for 1/3<=beta<1. It improves the previously
recorded Qu–Valko upper bound when 0<beta<1/2. It does not prove the
general-beta oscillatory asymptotic family, and its remainder is not
o(r^(-2)). The precise updated obstacle is described there.
The same second attempt proves uniqueness of normalized positive-definite
hierarchy solutions on r>0 for beta<1, and actual inverse-square
coefficients for each fixed Fourier moment when beta<3-2sqrt(2).
Those fixed-mode constants do not sum against the correlation observable,
so neither result closes the pair-correlation asymptotic gap.

No general-beta oscillatory expansion has been proved in this attempt.
The precise missing theorem is a weighted large-r decomposition of the
SDE-selected moments into the formal particular sector and homogeneous
oscillatory sectors, with the Forrester–Haldane amplitudes/phases and
remainder estimates summable in k at every specified order. Even at
leading order for non-even beta this has not been obtained here. Neither
the bound in Qu–Valko Theorem 3 nor a formal recurrence supplies it.
The general question is still unresolved by this work. Verified results
are the density lemma, exact beta=2 case, beta=4 remainder mechanism,
formal hierarchy algebra, necessary formal mode powers, and a tail bound.
