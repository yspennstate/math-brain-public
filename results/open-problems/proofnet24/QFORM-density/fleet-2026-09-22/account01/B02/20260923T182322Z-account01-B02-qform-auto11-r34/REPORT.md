SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T18:23:22Z.
attacking: the low-cross-rank/small-leak collar by combining exact rank-two crossing decay with an independent square in L^3 Fourier, and treating the critical rank-one-crossing + one-square endpoint directly in density.

# account01/B02 r34 — integrated rank-two crossing + square, and the Fourier-critical rank-one boundary

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN / GLOBAL_FOURIER_CRITERION_OPEN_NOT_REFUTED`.
Continuity: proved on the new rank-two-crossing branch by Fourier L1 and on the new rank-one hyperbolic branch by direct convolution; not proved for the unrestricted target.
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh source state and exact inputs

The current owner continuation is `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`; QFORM remains the sole research target and the unrestricted conjecture remains OPEN. I reread the current control, assignment, MANIFEST, CURRENT_RESEARCH, CLAIMS, CORRECTION_INBOX, and MEMORY_PROTOCOL before the mathematical write.

The exact grouped crossing input is the checked source

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`,

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its rank-two exact-crossing specialization says the following. If X and Y are independent source banks, B has exact rank two with nonzero singular values s1,s2, the two-dimensional crossing projections have density caps M_X,M_Y, and F(X),G(Y) are arbitrary measurable real internal phases, then for

R=F(X)+2 X^T B Y+G(Y)

we have

|phi_R(t)| <= min{1,K/|t|},

K=pi (M_X M_Y)^(1/2) (s1 s2)^(-1/2).                    (1.1)

No random coordinate is rotated and declared independent; U^T X and V^T Y are only used through their projection-density caps.

The designated partner actually consumed is account02/B02 at

`yspennstate/math-open-problems@727768b1384cc165e2ee915145bfdfc873837229`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T170839Z-account02-B02-qform-auto11/REPORT.md`.

For every literal physical cross block M with Z=E3(M)>0 it proves

||p_Q||_infinity <=10.345083232147514 Z^(-1/6),

integral_R |phi_Q(t)|dt <=2pi*10.345083232147514 Z^(-1/6).       (1.2)

The current source corrections used below include: no law-uniform pointwise one-dimensional quadratic decay, no independence after rotation, no arbitrary-joint coarea cap, no conditional-density supremum shortcut, and no inference from one good cross minor alone.

## 2. A sharp L^(3/2) bound for one square density

This elementary estimate is the first new ingredient.

### Lemma 2.1 — `QFORM-SQUARE-L32-v1`

Let V have probability density f with 0<=f<=M. For lambda!=0 and c real, let

T=lambda(V+c)^2.

Then the density g_T satisfies

||g_T||_(3/2) <= 2 M^(2/3) |lambda|^(-1/3),                      (2.1)

and, with Fourier convention hat g(t)=integral exp(itx)g(x)dx,

||phi_T||_3 <= 2(2pi)^(1/3) M^(2/3)|lambda|^(-1/3).              (2.2)

Proof. Translation reduces to c=0 and scaling to lambda=1. For u>0 put

F(x)=f(x)+f(-x), x>0.

Then F<=2M, integral_0^infinity F=1, and

g(u)=F(sqrt u)/(2 sqrt u).

With u=x^2,

integral_0^infinity g(u)^(3/2)du
 =2^(-1/2) integral_0^infinity F(x)^(3/2)x^(-1/2)dx.             (2.3)

Since F^(3/2)<=sqrt(2M)F and, by the one-dimensional bathtub principle,

integral_0^infinity F(x)x^(-1/2)dx
 <=2M integral_0^(1/(2M)) x^(-1/2)dx
 =2sqrt(2M),                                                       (2.4)

(2.3) is at most 2sqrt(2)M. Raising to power 2/3 gives ||g||_(3/2)<=2M^(2/3). Scaling gives (2.1). Hausdorff--Young between L^(3/2) and L^3, with the present Fourier convention, gives (2.2). QED.

This proof uses no pointwise oscillatory estimate for the square phase, so it is compatible with the fragmented-support correction.

## 3. Main new Fourier theorem: rank-two crossing + one independent square

### Theorem 3.1 — `QFORM-RANK2-CROSS-PLUS-INDEPENDENT-SQUARE-L1-v1`

Let X,Y,V be mutually independent, with X,Y arbitrary source banks and V scalar. Assume:

1. `R=F(X)+2 X^T B Y+G(Y)` with arbitrary measurable real F,G;
2. B has exact rank two, nonzero singular values s1,s2;
3. the two crossing projections have density caps M_X,M_Y;
4. V has density cap M_V;
5. lambda!=0 and T=lambda(V+c)^2 for any c.

More generally, all displayed translations and F,G may depend measurably on an auxiliary random element P independent of (X,Y,V); condition on P in the proof.

Then Q=R+T has a genuine unweighted integrated characteristic-function estimate

boxed:
integral_R |phi_Q(t)|dt
 <=4 pi 3^(2/3)
    M_V^(2/3)(M_X M_Y)^(1/3)
    (s1 s2 |lambda|)^(-1/3).                                     (3.1)

Hence

boxed:
||p_Q||_infinity
 <=2 3^(2/3)
    M_V^(2/3)(M_X M_Y)^(1/3)
    (s1 s2 |lambda|)^(-1/3).                                     (3.2)

The density has a continuous representative vanishing at infinity.

Proof. Conditional on P=p, the rank-two source theorem gives (1.1), while Lemma 2.1 gives the uniform L3 estimate (2.2) for the independent square characteristic function psi_p. Put

w(t)=min{1,K/|t|}.

Exactly

||w||_(3/2)^(3/2)
 =2[int_0^K 1 dt + int_K^infinity (K/t)^(3/2)dt]
 =6K,                                                               (3.3)

so

||w||_(3/2)=(6K)^(2/3).                                             (3.4)

Holder with exponents 3/2 and 3 gives

integral |phi_(Q|P=p)|
 <=(6K)^(2/3) * 2(2pi)^(1/3)M_V^(2/3)|lambda|^(-1/3).              (3.5)

Substituting K from (1.1) simplifies the constant exactly to 4pi*3^(2/3), proving (3.1). The bound is uniform in p, so |E_P phi_p|<=E_P|phi_p| and Tonelli preserve it after averaging P. Fourier inversion gives (3.2) and C_0 continuity. QED.

For cap-one crossing projections and cap-one V,

integral |phi_Q| <=26.13910423 (s1 s2 |lambda|)^(-1/3),             (3.6)

||p_Q||_infinity <=4.160167647 (s1 s2 |lambda|)^(-1/3).             (3.7)

This is a true integrated-Fourier mechanism. It is stable at the exact rank-two boundary and does not ask for a third cross singular value.

## 4. Actual low-rank strong-cut consequence

On the current strong-cut matrix M, the source gives

E=||M||_F^2 > E0:=11907/16384.                                    (4.1)

Consider the exact-rank-two boundary of the surviving near-rank-two tube, but exclude the near-rank-one tube:

rank M=2,

x2>=E/64,                                                           (4.2)

where x1>=x2 are the squared singular values. Since x1+x2=E and x1>=E/2,

s1 s2=sqrt(x1 x2)>=E/sqrt(128)>E0/sqrt(128).                       (4.3)

If, in addition, an independent physical square bank supplies |lambda|>=1 with scalar cap one, Theorem 3.1 gives the completely uniform endpoint estimate

boxed:
integral |phi_Q| <65.268,                                          (4.4)

boxed:
||p_Q||_infinity <10.388.                                          (4.5)

Arbitrary internal functions on each of the two crossing banks are retained by Theorem 3.1. Thus this is not a diagonal or separable-crossing calculation. What remains structural is to produce the independent square bank, or a replacement that survives overlap, from the arbitrary low-cross-rank target geometry.

## 5. Designated partner applied to the complementary actual inequality

The latest account02/B02 theorem (1.2) is applied here to the actual strong-cut inequality, not quoted abstractly. Outside the two low-rank tubes, its source gives

x1>63E/256,

x2>=E/64,

T2:=sum_(r>=3)x_r>=E/64.                                           (5.1)

Therefore

Z=E3(M)>=x1 x2 T2
 >[63/1048576]E^3
 >Z0:=[63/1048576](11907/16384)^3
 =2.3061517378361292e-5.                                           (5.2)

Substituting (5.2) into (1.2) gives

boxed:
||p_Q||_infinity <61.317722,                                       (5.3)

boxed:
integral_R |phi_Q(t)|dt <385.270608.                              (5.4)

Thus the latest designated partner pays every strong-cut state outside the near-rank-one/near-rank-two tubes, while Theorem 3.1 now pays a genuine exact-rank-two boundary chamber whenever the third curvature is furnished by an independent square bank. This is the equation-level partner application required by the assignment.

## 6. The critical rank-one-crossing + one-square endpoint can be paid directly in density

The preceding Fourier theorem starts exactly at crossing rank two. At crossing rank one, the reviewed exact-crossing estimate only gives a weight of order |t|^(-1/2); pairing that by Holder with the universal square L3 estimate is endpoint-insufficient. Rather than claim a false Fourier decay improvement, the corresponding independent-bank density problem can be solved directly.

### Lemma 6.1 — half-potential for a hyperbolic product

If Y,W are independent with density caps M_Y,M_W and kappa!=0, then

boxed:
sup_s E|2 kappa YW-s|^(-1/2)
 <=4 sqrt(2 M_Y M_W)|kappa|^(-1/2).                               (6.1)

Proof. For any density f<=M of mass one,

sup_c integral f(y)|y-c|^(-1/2)dy <=2sqrt(2M),                     (6.2)

again by the bathtub principle. Conditional on W=w!=0, (6.2) gives

E_Y|2kappa wY-s|^(-1/2)
 <=2 sqrt(M_Y)|kappa w|^(-1/2).                                    (6.3)

Average in W and use (6.2) a second time. QED.

### Theorem 6.2 — `QFORM-RANK1-HYPERBOLIC-PLUS-SQUARE-DENSITY-v1`

Let Y,W,V be mutually independent with caps M_Y,M_W,M_V. Let P be any independent random element. Let a(P),b(P),c(P),d(P) be arbitrary measurable real functions. For kappa lambda !=0 put

Q=2kappa(Y+a(P))(W+b(P)) + lambda(V+c(P))^2+d(P).                  (6.4)

Then Q has a bounded continuous density and

boxed:
||p_Q||_infinity
 <=4sqrt(2) M_V sqrt(M_Y M_W) / sqrt(|kappa lambda|).               (6.5)

In particular, for scalar cap-one variables and |kappa|,|lambda|>=1,

||p_Q||_infinity <=4sqrt(2)<5.657.                                 (6.6)

Proof. Condition on P=p. The square term has density bounded by

M_V / sqrt(|lambda| |u|)                                           (6.7)

on its sign half-line. Let Z=2kappa(Y+a)(W+b). Convolution and (6.1) give

p_(Q|p)(s)
 <=M_V |lambda|^(-1/2) E|s-d-Z|^(-1/2)
 <=4sqrt(2)M_V sqrt(M_YM_W)/sqrt(|kappa lambda|).                  (6.8)

For fixed p, both Z and the square term are absolutely continuous L1 laws, so their convolution is continuous and C_0. The uniform cap in (6.8) permits dominated convergence when averaging over P, proving continuity of the unconditional density. QED.

This theorem shows that a leakage parameter entering only through an independent random translation of the shared hyperbolic factor is free: for example

2H(L+beta)+2epsilon P L+lambda V^2
 =2(H+epsilon P)(L+beta)+lambda V^2-2epsilon beta P,                (6.9)

and (6.5) is independent of epsilon whenever H,P,L,V arise from mutually independent source banks. The live source model is harder precisely because L,V,P may be projections of the SAME rough product bank, so (6.9) does not restore the independence needed for (6.5). I do not use it outside its stated provenance.

## 7. What this says about the stronger Fourier criterion

The resource accounting is now sharper:

- two exact crossing directions + one independent square give genuine Fourier L1 by Theorem 3.1;
- one exact hyperbolic crossing direction + one independent square already gives a uniformly bounded continuous density by Theorem 6.2;
- the elementary Holder route does not prove Fourier L1 in that critical rank-one + one-square configuration.

This is not a counterexample to the universal integrated-Fourier conjecture. No source-valid counterexample was found. As a control, for independent Uniform[-1/2,1/2] Y,W one has the explicit bilinear transform 2 Si(t/2)/t=O(1/t), so multiplying by the usual square Fresnel t^(-1/2) tail is integrable; this standard smooth control is therefore not a counterexample.

The remaining B02 question is narrower: either prove a uniform integrated estimate through the overlapping-bank rank-one/square small-leak geometry, or construct a fixed rough cap-one product law whose characteristic function is not L1 while its quadratic output remains bounded. The present run does neither, so the target-wide Fourier criterion remains `OPEN_NOT_REFUTED`.

## 8. First unpaid implication

`QFORM-OVERLAPPING-BANK-RANK1-SQUARE-INTEGRATED-OR-COUNTEREXAMPLE-v1`:

starting from the current low-cross-rank strong-cut/hub survivor, retain original-coordinate product provenance and decide whether the critical one-hyperbolic-direction + one-square configuration has a law-uniform Fourier-L1 estimate when the partner/square/leak projections share the same rough product bank. If not, produce a fixed cap-one product counterexample to L1 and continue with direct density. The independent-bank case is now paid uniformly, so any genuine obstruction must use overlap/dependence created by projection, not merely a vanishing leakage coefficient.

No assumption of Gaussianity, moments, log-concavity, compact support, connected support, or independence after a general rotation was introduced.
