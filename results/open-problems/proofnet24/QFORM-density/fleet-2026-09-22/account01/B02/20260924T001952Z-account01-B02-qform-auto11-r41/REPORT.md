SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-24T00:19:52Z.
attacking: the r40 proposed weak-L2 maximal-parabola endpoint glue. I test that first essential implication directly; it is false even for admissible cap-one probability densities. I then return to the physical E3 Fourier receiver rather than weakening the owner target.

# account01/B02 r41 — weak-L2 maximal-chirp counterexample and corrected Fourier frontier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T001952Z-account01-B02-qform-auto11-r41`  
Role: Integrated Fourier estimate  
Status: **ESSENTIAL_STEP_APPLIED_WITH_COUNTEREXAMPLE / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN-NOT-REFUTED**  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.

The owner target is unchanged: independent ORIGINAL real coordinates with one-dimensional densities at most one, arbitrary real symmetric A, and at least three eigenvalues of modulus at least one. No Gaussian, log-concave, moment, compact-support, connected-support, diagonal-basis, or post-rotation-independence assumption is introduced. Continuity is claimed only on branches with a genuine unweighted Fourier-L1 estimate.

## 1. Fresh source state and exact debt attacked

Fresh `math-research-brain/main` was resolved at invocation start at `4236cc1741c65fc0a352b6e37da216296df39b2a`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with the exclusive continuation active. I reread `AGENTS.md`, `scheduled_tasks/README.md` including the OWNER MESSAGE, `fleet.json`, `roles.json`, `PROTOCOL.md`, `MANIFEST.json`, `CURRENT_RESEARCH.md`, `CLAIMS.json`, the live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and `assignments/account01/B02.json`.

The immediately preceding corrected B02 state is

`yspennstate/math-open-problems@6c6385df4bd4f441e4fb6624be200d3552e92a4a`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260923T232013Z-account01-B02-qform-auto11-r40/CORRECTION_AND_REDUCTION.md`.

That correction withdrew a false mixed-norm Minkowski step and proposed the following supporting lemma as one possible uniform glue for the account02/B02 zero-pivot chirp endpoint. For a cap-one probability density `g`, define

`E_g(s,eta)=int g(h) exp(-i(s h^2+eta h)) dh`,

`U_g(s)=sup_eta |E_g(s,eta)|`.

The proposed endpoint was

`sup_(lambda>0) lambda^2 |{s:U_g(s)>lambda}| <= C_w^2`             (1.1)

with a universal constant. If true, (1.1) would exactly cancel the small-tail parameter in the partner chirp kernel. This run tests (1.1) before building on it.

The designated account02/B02 source actually used below is

`yspennstate/math-open-problems@aeaba9e3351623ead11450857c2d014b43664aef`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T200844Z-account02-B02-qform-auto11/REPORT.md`.

In particular, it proves the marginal-free physical-E3 Fourier theorem

`||p_Q||_infinity <= 10.345084 E3(M)^(-1/6)`,

`int_R |phi_Q(t)| dt <= 2 pi (10.345084) E3(M)^(-1/6)`,             (1.2)

for every literal original-coordinate cross block `M` with `E3(M)>0`, with a continuous `C0` density; and it separately proves the exact zero-pivot rank-one shared-hub tensor theorem.

I also consumed the fresh global synthesis from account03/B19 r45, brain handoff commit `f9364e140483e4c7351eb95d366e3e9d23cce1c6`, whose current compact unpaid packets include a disjoint physical cross block with `E2>4/9`, a one-anchor star/cross packet, a physical two-star packet, or a giant near-rank-one physical crossing. The present result changes the analytic mechanism for the small-tail chirp collar rather than claiming any of those packets solved.

## 2. The proposed maximal weak-L2 lemma is false

### Theorem 2.1 — `QFORM-CHIRP-MAXIMAL-WEAKL2-COUNTEREXAMPLE-v1`

For every `N>=2` there exists a probability density `g_N` on `R` satisfying

`0<=g_N<=1`, `int g_N=1`,

such that, for

`U_N(s)=sup_eta |int g_N(h) exp(-i(s h^2+eta h)) dh|`,

one has

`sup_(lambda>0) lambda^2 |{s:U_N(s)>lambda}| >= c N`               (2.1)

for one absolute constant `c>0` independent of `N`.

Consequently there is **no** universal weak-`L2(ds)` estimate of the form (1.1), even in the exact cap-one probability class of the owner target.

This refutes only the proposed maximal-envelope glue. It does **not** refute target-wide unweighted Fourier-L1 for `X^TAX`.

### Proof

The construction is explicit up to harmless translations chosen by a uniform Riemann--Lebesgue argument.

Fix

`delta=pi/12`, `K=49`,

and put

`F(u)=1_{dist(u,2 pi Z)<=delta}`.

The `2pi`-periodic function `F` has mean

`m=delta/pi=1/12`.

#### Step 1: a phase-aligned set of prescribed mass at any sufficiently large chirp scale

For `R>0`,

`int_1^K F(R z^2) dz
 =(1/(2 sqrt(R))) int_R^(R K^2) F(u) u^(-1/2) du`.                 (2.2)

Write `F=m+G`. Since `G` is periodic with mean zero, its primitive

`H(U)=int_0^U G(u) du`

is bounded. Integration by parts gives

`int_R^(R K^2) G(u) u^(-1/2) du = O(R^(-1/2))`,

hence from (2.2)

`int_1^K F(R z^2) dz = m(K-1)+O(R^(-1)) = 4+O(R^(-1)).`            (2.3)

Therefore there exists an absolute `R0` such that every `R>=R0` has

`|{z in [1,K]:dist(R z^2,2 pi Z)<=delta}| >=2`.                    (2.4)

Now fix `N`, set

`lambda=1/N`,

and choose pairwise separated numbers `R_1,...,R_N>=R0`. Put

`T_j=R_j/lambda^2`.

By scaling (2.4), the set

`G_j={y in [lambda,K lambda]:dist(T_j y^2,2 pi Z)<=delta}`

has measure at least `2 lambda`. Choose a measurable subset

`S_j subset G_j`, `|S_j|=lambda`.                                  (2.5)

Set

`a=delta/(2K^2)`

and

`I_j=[T_j-a lambda^(-2), T_j+a lambda^(-2)]`.                      (2.6)

Choose the `R_j` separated enough that the `I_j` are disjoint. If `t in I_j` and `y in S_j`, then

`dist(t y^2,2 pi Z)
 <=delta+|t-T_j| K^2 lambda^2
 <=delta+delta/2
 =pi/8`.                                                           (2.7)

Thus

`Re int_(S_j) exp(-i t y^2)dy >= cos(pi/8) lambda`.                 (2.8)

Write `c0=cos(pi/8)`.

#### Step 2: translate the packets so that the wrong packets are Fourier-invisible to the chosen modulation

Let

`I=union_j I_j`.

For each fixed `k`, the family

`K_k={1_(S_k)(y) exp(-i t y^2): t in I}`

is compact in `L1(dy)`: `I` is compact and the map in `t` is continuous in `L1` by dominated convergence. Therefore the Riemann--Lebesgue lemma is uniform on this compact family:

`sup_(t in I) |int_(S_k) exp(-i t y^2) exp(-i xi y)dy| ->0`

as `|xi|->infinity`.                                               (2.9)

Choose `D` so large that all translated sets below are disjoint and, simultaneously for every `k`,

`sup_(t in I, |xi|>=2 (min I) D)
 |int_(S_k) exp(-i t y^2) exp(-i xi y)dy|
 <= c0 lambda/(2N).`                                               (2.10)

Put `b_j=jD` and

`g_N(x)=sum_(j=1)^N 1_(b_j+S_j)(x)`.                               (2.11)

The translated supports are disjoint, so `0<=g_N<=1`, and by (2.5)

`int g_N=N lambda=1`.

#### Step 3: one modulation selects one resonant packet on each disjoint time interval

Fix `t in I_j` and take the allowed modulation

`eta=-2t b_j`.                                                     (2.12)

On the `j`th packet, after writing `x=b_j+y`, the phase is, up to a constant,

`t y^2`.

On packet `k!=j`, it is, up to a constant,

`t y^2+2t(b_k-b_j)y`.

Hence (2.8), (2.10), and the triangle inequality imply

`U_N(t)
 >= c0 lambda-(N-1)c0 lambda/(2N)
 >= (c0/2)lambda`                                                  (2.13)

for every `t in union_j I_j`.

The disjoint union has measure

`|union_j I_j|=2a N lambda^(-2)`.                                  (2.14)

Take the level

`mu=(c0/4)lambda`.

Then (2.13)-(2.14) give

`mu^2 |{t:U_N(t)>mu}|
 >= (c0^2 lambda^2/16)(2aN lambda^(-2))
 = (c0^2 a/8)N`.                                                   (2.15)

This is (2.1), with

`c=c0^2 a/8
  =cos(pi/8)^2 * pi /(16*24*K^2)>0`.

Since `N` is arbitrary, the universal weak-L2 claim is false. QED.

### Why this respects the owner corrections

The density `g_N` is an honest one-dimensional probability density bounded by one. It is deliberately fragmented, with no compact-support or connected-support requirement. The large translated packet locations are allowed because no moment assumption exists. No rotated coordinate is declared independent. The mechanism is precisely the phase-aligned fragmented-support phenomenon that already invalidated law-uniform pointwise van-der-Corput decay, now upgraded to a quantitative obstruction to the r40 maximal weak-L2 proposal.

## 3. Consequence for the zero-pivot chirp programme

The account02/B02 exact nonzero-tail chirp identity and r39's valid strong `L4_s` maximal-parabola estimate remain useful. What is now ruled out is the specific attempt to improve that `L4` information to a law-uniform weak `L2` bound merely from

`0<=g<=1`, `int g=1`.

Thus the small-nonzero-tail endpoint cannot be glued uniformly by first replacing the actual modulation distribution with the worst modulation `sup_eta` and then seeking (1.1). The selector in Theorem 2.1 can chase different spatial fragments on disjoint time windows and makes exactly that supremum too expensive.

The next analytic mechanism must retain the **actual modulation average/distribution** supplied by the other original-coordinate bank, or bypass the chirp endpoint via a physical compound-volume/density receiver. In particular, no claim is made that the actual characteristic function of a QFORM realizes the adversarial selector in Theorem 2.1.

Target-wide universal Fourier-L1 therefore remains `OPEN_NOT_REFUTED`.

## 4. Designated account02/B02 theorem applied to a fresh live inequality

The fresh account03/B19 r45 synthesis leaves, among its explicit unpaid packets, a literal disjoint physical cross block `M` with

`E2(M)>4/9`.

Split this live packet at the concrete third-volume threshold

`E3(M)>=2^(-18)`.                                                  (4.1)

On (4.1), apply the completed account02/B02 marginal-free theorem (1.2) at the actual inequality. Since

`(2^(-18))^(-1/6)=2^3=8`,

one gets

`boxed: ||p_Q||_infinity <=82.760672`,                              (4.2)

and

`boxed: int_R |phi_Q(t)|dt <=520.000639`.                          (4.3)

This branch has a continuous `C0` density.

Therefore the r45 disjoint-`E2` frontier may, for purposes of this slot, be sharpened to the genuinely low-third-volume packet

`E2(M)>4/9`, `E3(M)<2^(-18)`.                                     (4.4)

This is not claimed solved; it is the correct place to couple the rank-two crossing to the third curvature forced elsewhere by `s_3(A)>=1`. The point of (4.2)-(4.4) is that any future argument may assume the physical cross block is `E3`-poor without losing a paid Fourier branch.

## 5. Published maximal-estimate cross-check

As a literature sanity check, I reviewed the one-dimensional Schrödinger maximal-in-space literature. The standard endpoint estimate relevant to a single `L2` datum supplies the familiar `L_t^4 L_x^infinity` scale, not the stronger amplitude weak-`L2_t` estimate proposed in r40. The explicit construction above is self-contained and is the operative proof; no published theorem is invoked to extend it to the QFORM target.

## 6. Correct current B02 frontier

The previous supporting lemma

`QFORM-CHIRP-MAXIMAL-WEAKL2-v1`

must be marked **REFUTED** and must not be used by downstream workers.

The first unpaid analytic implication is now

`QFORM-CHIRP-AVERAGED-MODULATION-OR-PHYSICAL-E3-GLUE-v1`:

> In the exact account02/B02 nonzero-tail chirp kernel, retain the actual original-bank modulation average rather than `sup_eta`, and prove a time-integrated estimate uniform as the tail tends to zero; alternatively route the small-tail state to an actual physical E3/D5, grouped-hub, or direct density receiver. Any argument must survive the fragmented cap-one family of Theorem 2.1.

For the current global r45 disjoint-cross packet, the Fourier side may additionally assume (4.4).

No valid counterexample to the owner QFORM bounded-density conjecture was found. No valid counterexample to target-wide universal unweighted Fourier-L1 was found. Full bounded density remains OPEN. Full-target continuity remains OPEN.

## 7. Integrity checks

- The counterexample is to the proposed maximal weak-L2 **supporting lemma**, not to QFORM and not to target-wide Fourier-L1.
- Every `g_N` is an admissible cap-one probability density.
- The proof uses only original scalar coordinates and Fourier modulation; no independence after rotation/shear is asserted.
- No support or moment bound is assumed; the packet translations are intentional and admissible.
- The account02/B02 theorem is applied to the actual physical inequality `E3(M)>=2^(-18)`, producing the explicit numerical bounds (4.2)-(4.3).
- Same-bank curvature is not dropped in the partner theorem.
- Full-target continuity is not claimed.
