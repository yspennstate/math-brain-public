# Independent referee report

**Overall verdict: SOUND.** The mathematical counterexample survives the audit. Its classical proof is elementary and valid. The free proof has the correct branch, derivative, inequalities and support argument. I found no estimate that fails and no counterexample to either lemma. The introductory claim that support is the dividing line overstates what was proved; several boundary conventions should be stated explicitly. Original-source accuracy and novelty remain unverified under the no-browsing rule.

This verdict concerns the theorem as a mathematical assertion and its contradiction of the conjecture **as quoted in PAPER.tex**. It does not certify the quotation, bibliography, priority, funding or research-history declarations. `PAPER.tex` was not changed. Locations below are its original line numbers. `LOG.md` records the nine requested stages in order, with more detailed derivations and individual verdicts.

## Verdict table

GAP (source) below means an unavailable attribution has not been authenticated; it does not identify a missing mathematical estimate. Wording repairs that can be made immediately are identified separately from proof gaps.

| Statement or step | Verdict | Reason |
|---|---|---|
| Definition, line 43 | CORRECT | Standard real-mode definition, including a possible atom at the mode. |
| HU background, lines 4551 | GAP (source) | they prove / in that construction the 5/2-moment is always infinite: original results and exact construction were not supplied and cannot be authenticated from memory. |
| Quoted Conjecture 5.5, lines 4749 | GAP (source) | Exact quotation and scope cannot be checked without the original; the present theorem contradicts the words printed here. |
| [eq:classical], lines 5356 | CORRECT | Drift-free homogeneous Laplace exponent; a strictly stable subordinator. |
| [eq:free], lines 5760 | CORRECT | Negative imaginary part, sublinear growth, exact free stability and time scaling. |
| [eq:mustar], lines 6165 | CORRECT | Positive masses, total one, unbounded negative support and growing gaps. |
| [thm:main], lines 6769 | CORRECT | Both non-unimodality arguments work with this same initial law for all alpha,t. |
| Required (2+alpha)-moment | CORRECT | All absolute exponential moments imply this moment. |
| S_t^(1/2)=L_(t/sqrt(2)), line 71 | CORRECT | Exactly the normalization specified in the question. |
| the dividing line is the support, line 71 | WRONG as an iff assertion | An unbounded exponential initial law gives unimodal convolutions for every t; the correct assertion concerns failure of any uniform positive tail-envelope guarantee. |
| Classical lemma hypotheses, line 80 | CORRECT | Strict tail decrease and infinitely many positive weights are sufficient. |
| Density sum, line 84 | CORRECT | Uniform convergence by bounded g; continuity and Tonelli normalization. |
| I_n nonempty, line 86 | CORRECT | Growing gaps eventually exceed b. |
| Vanishing terms j<n, line 86 | CORRECT | Arguments are strictly negative. |
| Decreasing terms j>=n, line 86 | CORRECT | Arguments exceed b, and a positive weighted term gives strict decrease of the sum. |
| Almost-everywhere representative argument, line 88 | CORRECT | Full-measure sets are dense; continuity transfers monotonicity to q. |
| Mode coverage, line 88 | CORRECT | Every real mode is eventually to the right of an I_n; an infinite mode is excluded by the definition and cannot give an integrable globally monotone density. |
| Kernel scaling and characteristic function, line 96 | CORRECT | Modulus exp(-cos(pi alpha/2)|u|^alpha) is integrable. |
| Bounded continuous density and value zero at 0, line 96 | CORRECT | Fourier inversion, one-sided support and continuity. |
| [eq:series], lines 99101 | CORRECT | Negative-cut Laplace inversion gives exactly (-1)^(k+1) sin(k pi alpha). |
| E entire, line 102 | CORRECT | Stirling gives coefficient root O(k^(alpha-1)), tending to zero. |
| Density derivative display, lines 103105 | CORRECT | Chain rule gives -x^(-2)(E+alpha y E'). |
| Eventual strict decrease, line 106 | CORRECT | The leading coefficient (1+alpha)c_1 is positive. |
| Half-stable density, line 109 | CORRECT | Laplace transform exp(-t sqrt(lambda)). |
| Half-stable derivative, lines 110112 | CORRECT | Zero at t^2/6, negative beyond it. |
| b_t=t^2/6, line 113 | CORRECT | Agrees with scaling t^(1/alpha)=t^2. |
| Moment display, lines 116119 | CORRECT | The summands are eventually bounded by 2^(-n-2). |
| W<=1/4, line 120 | CORRECT | Sum of the geometric upper bounds is 1/4. |
| A_n-A_(n-1)=A_(n-1)(A_(n-1)-1), line 120 | CORRECT for n>=2 | The first actual gap uses a_0=0 separately; specify the index range. |
| Classical theorem application, line 120 | CORRECT | Every kernel has a finite decrease threshold; the gaps exceed any such threshold. |
| Tail-bound remark, line 124 | CORRECT | j>=n are exactly the atoms strictly left of -x; psi(A_n)<=psi(x) is the right direction. |
| Free LvyKhintchine sign/growth, line 130 | CORRECT | arg(-phi) lies in (0,pi), and |phi(iy)|/y tends to zero. |
| Dilation and semigroup, line 130 | CORRECT | Dilation multiplies the transform by c^alpha; transforms add in time. |
| Positive support and absolute continuity, line 130 | CORRECT | Also consistent with direct inversion: support starts at a positive edge ell. |
| [eq:H], lines 133135 | CORRECT | The correct global inverse-subordination map. |
| Nevanlinna form and f, line 136 | CORRECT | Im H=y(1-I); f=0 precisely when I(x,0)<=1. |
| (HW1), line 138 | CORRECT | Boundary homeomorphism follows from the integral difference identity, CauchySchwarz and properness. |
| (HW2), line 139 | CORRECT with boundary convention | A finite real boundary value and nonnegative angular derivative mean H'=1-I(x,0) in [0,1]. |
| Undefined angular derivative, line 139 | GAP (wording) | The real-boundary convention is missing; ordinary complex differentiability alone would make the statement false. The application explicitly verifies realness. |
| (HW3), line 140 | CORRECT in its use | An atom's divergent G excludes B,C; for this stable law f>0 at atoms can also be proved directly. Full classification is taken as cited. |
| (HW4), lines 141144 | CORRECT in its use | Subordination gives the displayed positive-height formula and analytic zero intervals. Global singular-part regularity remains a cited theorem. |
| Free Step 1, line 150 | CORRECT | No nu-atoms and no mass-one mu-atom imply A empty. |
| Free Step 2, line 152 | CORRECT | -Im G>=w_k/y; hence atoms are in V and have positive density images. |
| [eq:nchoice], lines 155157 | CORRECT | A_n^alpha tends to infinity for fixed alpha>0. |
| Midpoint location, line 158 | CORRECT | sqrt(A)<=A/4 for n>=2, including equality at n=2. |
| G and I_2 display, lines 159161 | CORRECT | I_2=-G'>0 on the support gap. |
| Denominator signs/sizes, line 162 | CORRECT | Early terms <=-A/4; late terms >=A/2. |
| G(c)<=-1/A, lines 163165 | CORRECT | Drop negative early terms and use W<=1/4. |
| I_2(c)<9/A^2, lines 166169 | CORRECT | The displayed bound is actually <=8/A^2. |
| Analyticity and negative F, line 170 | CORRECT | The gap is disjoint from the closed atomic support, and F maps C+ into C+. |
| Negative-axis power and real H display, lines 170173 | CORRECT | The upper value is exp(i pi(1-alpha)) |F|^(1-alpha), yielding a positive real increment. |
| [eq:Hprime], lines 175177 | CORRECT | Differentiate a=-G, with a'=I_2. |
| H'(c)>1/2, lines 178181 | CORRECT | Negative exponent reverses the bound on a; [eq:nchoice] supplies the margin. |
| J outside V and p=0 on h(J), line 182 | CORRECT | Real analytic H with H'>0 has I(x,0)<1; inverse continuation is real. |
| Strict ordering display, lines 183185 | CORRECT after shrinking J | Choose closure(J) inside the original gap; this is immediately available. |
| Free Step 4 neighborhoods and null sets, line 187 | CORRECT | Continuity gives positive open neighborhoods; both mode cases permit selections outside the equality null set. |
| Final quantifiers, line 189 | CORRECT | n can depend on alpha,t while mu_* stays fixed. |
| Infinitely many free support gaps, lines 191193 | CORRECT | All sufficiently late, ordered gaps give separate zero intervals bracketed by support. |
| Author's check-script claims, lines 113,189 | GAP (source) | The check script verifies / The check script evaluates: no such program was provided; independent replacements are supplied here. |
| Exact theorem citations, bibliography and novelty | GAP (source) | Original texts were not consulted; confidence and limits are stated below. |

## Classical checks and possible counterexamples

For the classical lemma, take any x<y in I_n. All j<n terms vanish; all j>=n have g(x+a_j)>g(y+a_j). Nonnegative summation and p_n>0 give q(x)>q(y). This argument cannot be defeated by choosing very small weights or by making the kernel flat near the origin. Strict decrease of a nonnegative kernel on its tail also implies positivity throughout that tail. No admissible kernel/weight counterexample was found; the pairwise inequality rules one out.

Passing from a monotone density representative f to continuous q is legitimate: approximate two ordered points by ordered points in the full-measure set f=q. A mode at minus infinity is not a mode under the printed definition. Even if allowed, a globally nonincreasing nonnegative integrable function on the whole real line must vanish almost everywhere, so it cannot be this probability density. The analogous observation applies to a mode at plus infinity.

The density series has an independent derivation. The upper negative-axis value of exp(-s^alpha) is exp(-r^alpha exp(i pi alpha)). The inverse-Laplace jump formula gives

    g_1(x) = -(1/pi) integral_0^infinity exp(-rx)
                           Im exp(-r^alpha exp(i pi alpha)) dr.

Expand the second exponential. The k-th imaginary coefficient is (-1)^k sin(k pi alpha)/k!, so the minus sign produces exactly (-1)^(k+1). Integration gives Gamma(k alpha+1) x^(-k alpha-1). Absolute termwise integration is justified by the integrable majorant exp(-rx+r^alpha), since alpha<1. Stirling proves convergence for every x>0 and the entire-function claim. Thus the numerical agreement below checks an independently derived formula, not just a cited series.

The tail-envelope calculation needs **no reversed inequality correction**. For x in [A_(n-1),A_n), exactly the atoms indexed j>=n lie strictly left of -x, including the endpoint convention. Monotonicity of psi gives

    sum_(j>=n) p_j <= 2^(-n) min(psi(A_n),1)
                   <= psi(A_n) <= psi(x).

At x=A_n one uses n+1. The convention A_0=0 is for this partition, not for the squaring recursion at n=1.

The sentence about support being the dividing line needs qualification. A direct counterexample to its literal interpretation is an initial exponential density e^(-x) 1_(x>0). With the half-stable kernel, put

    q_t(x)=exp(-x) integral_0^x exp(u) g_t(u) du,   x>0.

Then q_t'=D=g_t-q_t, and (exp(x)D)'=exp(x)g_t'. Before the unique mode t^2/6 of g_t, D>0. After that mode, exp(x)D strictly decreases, so D crosses zero at most once. It must cross: otherwise the positive integrable q_t would remain nondecreasing forever. Consequently q_t is unimodal for every t, despite the initial law's unbounded support and finite moments of every polynomial order. The valid replacement is: compact support suffices for this kernel, while arbitrary positive bounds on the left tail do not suffice uniformly over initial laws.

## Free boundary analysis independent of the cited paper

Write beta=1-alpha. The transform is phi(z)=t(-z)^beta with arg(-z) in (-pi,0); its imaginary part is strictly negative in C+. Its positive free Lvy measure has density t sin(pi alpha)/pi times s^(-1-alpha) on s>0. Indeed the compound-Poisson integral of z s/(z-s) at z=-r is t r^beta. Approximation by positive compound-Poisson laws confirms the positive support. For a point-mass initial law, the negative-real inverse map is -r+t r^beta, with maximum

    ell = alpha t^(1/alpha) (1-alpha)^((1-alpha)/alpha) > 0.

The positive free stable law has support [ell,infinity), a density on its interior and no atom. For alpha=1/2,t=1 this gives ell=1/4. Its no-atom property also follows directly from z=F(z)+phi(F(z)): an atom forces F(z) to vanish linearly, while the power term would vanish at the slower order |z-x|^beta, an impossibility.

For general H in the paper's Nevanlinna form, set

    I(x,y)=integral (1+s^2)/((x-s)^2+y^2) d sigma(s).

Then Im H(x+iy)=y(1-I(x,y)). The strictly decreasing function I(x,y) tends to zero as y tends to infinity, and to I(x,0) as y tends to zero. It follows that f(x)=0 iff I(x,0)<=1, and I(x,f(x))=1 when f(x)>0. Testing fixed y values and using the implicit equation proves f is continuous. Define Omega={x+iy:y>f(x)}.

The angular-derivative condition is exactly this threshold **when H has a finite real boundary value**. Finite I(x,0) gives that boundary value and

    H'(x)=1-I(x,0).

Thus nonnegative angular derivative means a value in [0,1]; no additional upper-bound hypothesis is missing. At a real point of analytic continuation where H is real on a real neighborhood, this is the ordinary derivative. If one instead interpreted angular derivative to mean ordinary complex differentiation regardless of boundary value, (HW2) would be false: H(z)=z-i has ordinary derivative 1 but f(x)=1 everywhere. This example explains the needed definition; the actual proof explicitly verifies realness before applying (HW2).

The global boundary ordering can also be recovered. For z_1,z_2 in Omega,

    (H(z_1)-H(z_2))/(z_1-z_2)
      = 1-integral (1+s^2)/((z_1-s)(z_2-s)) d sigma(s).

CauchySchwarz bounds the integral modulus by sqrt(I(z_1)I(z_2))<1, proving univalence. On the closed graph domain the bound is <=1 and also gives |H(z_1)-H(z_2)|<=2|z_1-z_2|, hence boundary continuity. Equality H(z_1)=H(z_2) for distinct boundary points would force equality in CauchySchwarz. For sigma with at least two support points, this forces z_1=conjugate(z_2), which is impossible for distinct points in the closed upper half-plane. For a single support point s, equality forces (z_1-s)(z_2-s)=M>0, with both moduli >=sqrt(M), and again both boundary points must coincide.

For completeness, H is proper on this domain. Divide H(z)-z by z, split the finite measure sigma into a compact part and a tail, and use CauchySchwarz on the latter. Its absolute contribution is bounded by

    sqrt(I(z)) [integral_tail |s+1/z|^2/(1+s^2) d sigma(s)]^(1/2),

which tends uniformly to zero after the tail mass is made small; the compact contribution tends to zero as |z| tends to infinity. Therefore H(z)/z tends to 1 within the closed graph domain. The real boundary map h is continuous, injective and tends to the appropriate infinities, proving (HW1). The same properness and boundary argument makes H(Omega) both open and closed in C+, hence all of C+. On a positive-height boundary arc, Re H'>0 and h'=|H'|^2/Re H'>0 provide a separate derivative check.

The inverse-transform identity near infinity gives

    F_(mu boxplus nu)^(-1)(z)=F_mu^(-1)(z)+phi_nu(z).

Consequently F_(mu boxplus nu)(H(w))=F_mu(w) on Omega by analytic continuation, and the inverse of H is the relevant subordination map. Taking imaginary parts gives the paper's formula

    p(h(x))=-Im G_mu(x+i f(x))/pi
           = f(x)/pi integral d mu(s)/((x-s)^2+f(x)^2),  x in V.

No Jacobian factor belongs in this formula: it is a boundary identity of Cauchy transforms, not a pushforward density calculation. At a real analytic gap with H'>0, the inverse continues analytically with real Cauchy transform, proving that the image interval carries zero measure.

For this construction, the atoms can be put in V directly. At an isolated atom x of mass m,

    F_mu(x+iy) ~ iy/m,
    Im H(x+iy)/y
      = 1-t m^(alpha-1) cos(pi alpha/2) y^(-alpha)(1+o(1)) -> -infinity.

Hence I(x,0)=infinity and f(x)>0. This is independent confirmation of Step 2 without the full (HW3) classification.

I therefore derived (HW1), the properly defined (HW2), and the locally used subordination/density part of (HW4). I take on trust the general A/B/C classification in (HW3) and the global absence of singular continuous mass, atom classification and density-continuity theorem in (HW4). Their quoted forms are what I would expect, subject to the conventions listed below. Exact theorem numbers and source wording remain unchecked.

For the **specific** mu_* and stable phi, even the regularity used in Step 1 can be recovered without trusting those general theorems. The proper boundary bijection H has a continuous inverse up to R. The discrete atom set has no finite accumulation, so G_mu is meromorphic near every real point. If f(x)=0, the finite real boundary value of H excludes a zero of G_mu, because phi(1/G_mu) would diverge there. The direct atom calculation already excludes poles of G_mu at zero-height boundary points. Thus G_mu is finite and regular at every zero-height boundary point; at positive-height points it is analytic in C+. It follows that G_(mu boxplus nu)=G_mu composed with H^(-1) extends continuously with finite values to all R. Local uniform boundary convergence and Stieltjes inversion give a continuous density and no singular part, verifying precisely the specialized conclusion needed in Step 1. The full general HW3/HW4 assertions remain cited results, but the present application has this independent check.

For non-unimodality alone one can use still less: the analytic positive-density neighborhoods at the atom images and the zero-measure image interval already contradict every hypothetical unimodal density representative, regardless of possible singular mass elsewhere.

At c=-A/2 the central estimates are conservative. The denominator bounds give

    G(c)<=(-2+4W)/A<=-1/A,
    I_2(c)<9/A^2,  in fact <=8/A^2.

On G<0, a=-G and the upper power branch yield H=x+t a^(alpha-1), so

    H'=1-(1-alpha)t I_2 a^(alpha-2).

Since alpha-2<0 and a(c)>=1/A, H'(c)>1-9(1-alpha)t A^(-alpha)>=1/2. Shrinking J to have closure inside the gap gives all the strict endpoint orderings. Continuity then upgrades the two positive-density values to neighborhoods, so the final null-set mode argument is complete.

## Numerical tables and reproducibility

All programs used are in `audit.py`, written for this audit. No author program, online source or external dataset was used. Run from this directory:

```sh
python3 audit.py 3 > step3.txt
python3 audit.py 7 > step7.txt
python3 audit.py 8 > step8.txt
```

The script uses standard Python and mpmath, scalar native-complex Newton calculations, one worker and one numerical-library thread. Every invocation has a 240-second alarm. It preserves an inherited nice level >=10. macOS refused RLIMIT_DATA changes; the actual measured peak resident memory was below 39 MB, and the longest successful invocation took 3.582 seconds. There were two initial setup failures, recorded in LOG.md, before the successful mathematical runs. No visible window or background job was created.

### Step 3: independent inverse Laplace transform

The series and de Hoog inversion of exp(-s^alpha) were evaluated independently at 70 decimal digits. The table prints rounded values; relative discrepancies were computed before rounding.

| alpha | x | series | inverse Laplace | relative discrepancy |
|---:|---:|---:|---:|---:|
| 0.3 | 0.5 | 0.240645783025428727 | 0.240645783025428727 | 1.13e-70 |
| 0.3 | 1 | 0.117157002565916154 | 0.117157002565916154 | 4.29e-71 |
| 0.3 | 2 | 0.054783242263121491 | 0.054783242263121491 | 1.96e-71 |
| 0.3 | 5 | 0.019154354837293765 | 0.019154354837293765 | 9.52e-71 |
| 0.5 | 0.5 | 0.483941449038286700 | 0.483941449038286700 | 1.96e-71 |
| 0.5 | 1 | 0.219695644733861199 | 0.219695644733861199 | 1.20e-71 |
| 0.5 | 2 | 0.088016331691074869 | 0.088016331691074869 | 2.19e-71 |
| 0.5 | 5 | 0.024000778968602720 | 0.024000778968602720 | 2.78e-71 |
| 0.7 | 0.5 | 0.965119118469361911 | 0.965119118469361911 | 5.82e-71 |
| 0.7 | 1 | 0.387395010146592490 | 0.387395010146592490 | 1.93e-71 |
| 0.7 | 2 | 0.107688344874337133 | 0.107688344874337133 | 2.02e-71 |
| 0.7 | 5 | 0.019260270724066872 | 0.019260270724066872 | 1.65e-71 |

The half-stable closed form also passed independent Laplace quadrature and numerical differentiation:

| lambda | numerical Laplace transform | exp(-sqrt(lambda)) |
|---:|---:|---:|
| 0.25 | 0.606530659712633424 | 0.606530659712633424 |
| 1 | 0.367879441171442322 | 0.367879441171442322 |
| 4 | 0.135335283236612692 | 0.135335283236612692 |

| u | g_1(u) | numerical derivative | displayed derivative |
|---:|---:|---:|---:|
| 0.1 | 0.732249128096324356 | 7.32249128096324356 | 7.32249128096324356 |
| approximately 1/6 | 0.925081978822615661 | -1.67e-33 | -1.67e-33 |
| 1 | 0.219695644733861199 | -0.274619555917326498 | -0.274619555917326498 |
| 4 | 0.033125441543003570 | -0.011904455554516908 | -0.011904455554516908 |

The tiny derivative at the second row reflects the finite decimal representation of 1/6; the exact derivative there is zero. Full results are `step3.csv` and `step3.txt`.

### Step 7: free convolution grid

Use alpha=1/2,t=1, mu=0.9 delta_0+0.07 delta_-4+0.03 delta_-16. Thus H(w)=w-i sqrt(1/G_mu(w)). Damped Newton solves H(w)=x+i eps with Im w>0. The grid x=-18,-17.98,...,8 was run at eps=1e-4 and 1e-7, totaling 2,602 roots. Maximum residual <3.0e-13; maximum successful iteration count 14.

Real-axis scans and endpoint bisections give:

| input atom gap | component where G<0,H'>0 | image interval with zero limiting density |
|---|---|---|
| (-16,-4) | (-14.603198031408,-4.417483675880) | (-9.978446953609,-2.770859350532) |
| (-4,0) | (-3.131888592060,-0.283558951103) | (-0.920020912522,0.279591324434) |

At c=-8: G=-0.12625, I_2=0.01890625, H'=0.789269052197, H(c)=-5.185609821079. This lies in the first zero interval.

| atom s | f(s) | h(s) | limiting density at h(s) |
|---:|---:|---:|---:|
| -16 | 0.957884509213 | -12.374920619595 | 0.0111845314445 |
| -4 | 0.582724228753 | -2.150020277282 | 0.0484924711226 |
| 0 | 0.561234159812 | 0.554621986590 | 0.511231911173 |

These values come from the boundary equation for f; independent inversion at fixed image locations converges to them:

| x | density at eps=1e-4 | density at eps=1e-7 | density at eps=1e-10 |
|---:|---:|---:|---:|
| -12.374920619595 | 0.0111839969484 | 0.0111845309100 | 0.0111845314439 |
| -2.150020277282 | 0.0484890331333 | 0.0484924676844 | 0.0484924711192 |
| 0.554621986590 | 0.511138688998 | 0.511231817959 | 0.511231911080 |
| -6.374653152070, first gap interior | 5.161755781e-7 | 5.161755783e-10 | 5.161755782e-13 |
| -0.320214794044, second gap interior | 1.774552081e-5 | 1.774552066e-8 | 1.774552106e-11 |

Finite eps computes a Poisson-smoothed density, so it is not exactly zero in a gap. The linear decay in eps is the expected behavior; exact vanishing follows from the analytic real inverse. Positive density at each atom image persists in an open neighborhood because f>0 there. The agreement of the limiting density intervals with H(real),H'>0 is direct corroboration of the proof's mechanism.

For the paper's actual mu_*, choose the **smallest n>=2** satisfying [eq:nchoice]. At 70-digit precision, include every atom through N=max(3,n+1); bound the rest by 2^(-N-2) exp(-A_(N+1)^2). The following derivative values also agree to all shown digits with symmetric differences of the independently evaluated real H, with relative step 1e-20:

| alpha | t | n | A_n | G(c) | I_2(c) | H'(c) |
|---:|---:|---:|---:|---:|---:|---:|
| 0.1 | 1 | 6 | 2^64 | -1.08420217248550443e-19 | 1.17549435082228751e-38 | 0.988577700676240438 |
| 0.1 | 100 | 7 | 2^128 | -5.87747175411143754e-39 | 3.45446742203777785e-77 | 0.986474243505732121 |
| 0.5 | 1 | 3 | 256 | -0.00781250000354508489 | 0.00006103515630628537 | 0.955805826165166861 |
| 0.5 | 100 | 5 | 2^32 | -4.65661287307739270e-10 | 2.16840434497100898e-19 | 0.998921040678121113 |
| 0.9 | 1 | 2 | 16 | -0.125000001758362105 | 0.0156250006593857894 | 0.984610694421876993 |
| 0.9 | 100 | 4 | 65536 | -0.0000305175781250524097 | 9.31322574618677543e-10 | 0.999136832542495556 |

The largest omitted-mass bound is below 10^(-1.8652806e9); it is negligible for every displayed digit. The correction to p_0 is included in that tail error. Full c values, derivative differences and logarithmic tail bounds are in `step7_paper.csv`; `step7_grid.csv` contains every grid root, density, residual and iteration count. Final run: 0.090 seconds, peak RSS 21,938,176 bytes.

### Step 8: classical convolution grid

Use alpha=1/2,t=1 and weights (0.85,0.07,0.05,0.03) at (0,-4,-16,-256). The density and its explicit derivative give:

| x | q(x) | q'(x) |
|---:|---:|---:|
| -255.99 | 1.17531498980118e-10 | 2.76199022603796e-7 |
| -255.9 | 0.0219674738428885 | 0.219674738428928 |
| -250 | 0.000552323909442990 | -0.000134245394656282 |
| -240 | 0.000130181867530859 | -0.0000120774193510074 |
| -225 | 0.0000486375182873252 | -0.00000234077546388012 |
| -210 | 0.0000269785919245818 | -0.000000876549241405956 |
| -200 | 0.0000201046014221932 | -0.000000536913383006595 |
| -20 | 0.00000233178369161171 | -0.0000000148101924897235 |
| -15.9 | 0.0366147287582501 | 0.366124549861726 |
| -3.9 | 0.0515878081202982 | 0.512534244602222 |
| 0.1 | 0.624866669763352 | 6.22331230251476 |

The whole grid [-256,5] has spacing 0.01. On the separate 5,001-point grid [-250,-200], every adjacent density difference is negative, from -1.339740870e-6 to -5.370328975e-9. This is also an exact analytic sign result: throughout that interval q'=0.03 g_1'(x+256)<0 and all other atom contributions vanish. The density is positive further left at -255.9.

The triple -255.9<-20<-15.9 has a strict middle valley, proving this **finite** example is non-unimodal. Continuity transfers the valley to positive-length neighborhoods and excludes changes on null sets. Infinitely many atoms are not needed to defeat unimodality at this particular time. They are needed for the lemma's persistent, arbitrarily-left decreasing-interval argument with a single initial law for all t. A finite leftmost atom leaves room for a mode on its left or near it, and cannot supply arbitrarily-left intervals; the quoted compact-support theorem also gives eventual unimodality for finite mixtures. Full output: `step8_table.csv`, `step8_grid.csv`, `step8.txt`. Runtime 0.082 seconds, peak RSS 21,856,256 bytes.

## Typos, ambiguities and proposed repairs

No arithmetic or sign typo was found in the main displayed formulas. The following are all the unclear or misleading passages I noticed:

1. **Line 45, in that construction the 5/2-moment is always infinite.** The word always asserts a necessity for HU's construction. Give the actual condition on its weights or quote the precise proposition; I could not authenticate this from memory.
2. **Line 51, each new atom has to outweigh the decreasing tails.** Specify that the comparison is between positive and negative *density derivatives* in that particular construction. Do not present it as a necessity theorem for every measure supported toward plus infinity.
3. **Line 71, the dividing line is the support of mu and not its tail.** Replace with the uniform-guarantee statement proved by the remark: compact support suffices, while no prescribed positive upper bound on the left tail suffices in general. Unbounded support alone does not imply failure, as the exponential example shows.
4. **Line 75, since the kernel is positive everywhere.** The classical positive-density statement and the free support mechanism should be distinguished in wording; free convolution has no ordinary convolution kernel whose translated copies are being summed. The intended full-support obstruction is understandable.
5. **Line 120, the A_n-A_(n-1) identity.** Add n>=2 and treat a_1-a_0=4 separately. The remark's A_0=0 is not the value supplied by the formula 2^(2^0).
6. **Line 139, the angular derivative H'(x) exists in [0,+infinity).** Define the real-boundary angular derivative. A bare ordinary derivative at a real point is insufficient if H is not real there. In the relevant analytic real case it equals the ordinary derivative and is automatically <=1.
7. **Line 140, s_nu being the zero of F_nu when it exists.** State explicitly that A is empty if this zero does not exist, or declare the nonexistent-atom term to be zero. The intended convention is clear for the present atomless nu, but the general definition is incomplete without it.
8. **Lines 141144, density values at h(A).** Clarify that assigning p=0 at atomic exceptional points is a choice of representative, not a claim of a continuous limiting value there. No issue arises in the main proof because A is empty.
9. **Line 182, there is an open interval J ... contained in J_0.** Add closure(J) contained in J_0 and in the original atom gap, before asserting the strict infimum/supremum inequalities at line 184. Such a shrink is immediate.
10. **Line 189, The value n ... depends on t.** Say can depend on alpha and t. Alpha was fixed, so the present sentence is valid but less clear about the theorem's quantifiers.
11. **Lines 113 and 189, references to the author's check script.** They cannot serve as verification in a source-only audit; supply a precise version/output if they are meant to be reproducible. The independent calculations here replace them for the tested assertions.
12. **Line 31 versus line 241.** The document date is 17 October 2026, but it cites a paper dated October 2026 at a repository path containing 2026-10-24. A revision date or version statement would resolve the apparent chronology mismatch. This does not affect the mathematics.
13. **Line 215, No data were used.** If retained, No external datasets were used; numerical verification output accompanies the code would describe the computational checks more precisely.

## Attributions, memory and limits

I remember the HasebeUeda eventual-unimodality problem and the stable-process moment conjecture with moderate confidence. I do not remember the exact wording, numbering or weight conditions in Proposition 5.4 well enough to certify them. The strict-stability issue does not provide an escape from the quotation: positive drift-free alpha-stable subordinators for alpha<1 are ordinary strictly stable processes, and the given free transform is strictly stable in the free sense. A separately added deterministic drift would destroy this exact homogeneity, but none is present here. The initial moment hypothesis is amply satisfied.

I recognize HasebeKuznetsov's positive rho=1 free stable family with high confidence, and BercoviciVoiculescu's transform and infinite-divisibility foundations with high confidence. The attribution of stable-law regularity to BercoviciPata and Biane is consistent with my memory, with moderate confidence about the exact location. I do not independently certify any of the printed theorem numbers. The HuangWang framework matches the first-principles calculation, but its exact bibliographical metadata and general boundary classification have not been authenticated.

The plus-infinity explanation is mathematically plausible for the cited bump construction. For alpha=1/2, g_t'(x) is asymptotic to -(3t/(4 sqrt(pi))) x^(-5/2), whereas a new atom's positive derivative at a fixed scaled offset is of order p_n t^(-4). Overcoming the previous negative slopes requires p_n a_n^(5/2) of order t^5 in this method. Covering arbitrarily large t this way forces an infinite 5/2-moment. The explanation is correct for that mechanism; the exact claim about HU's particular construction remains a source check.

I do not recall a specific earlier paper that already refutes this conjecture. That statement has low evidentiary value: this was expressly not a literature search, and novelty is unverified. I have not invented a reference or purported outside quotation. Funding, affiliations, competing interests, repository contents and AI-history claims were not audited. The LaTeX source was read but not compiled. Numerical inversions are finite-precision corroboration, not certified interval arithmetic; the decisive signs and support statements were proved analytically as well.

Task: Be a hard, independent referee of PAPER.tex  12 November 2026, first recorded clock 05:43:33 +04.

**SOUND**
