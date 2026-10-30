SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B03, 2026-09-24T06:25:02Z.
attacking: the genuinely nonzero near-coloop hub-square collar — use Plancherel in the random leaf slope, not in the rough quadratic phase, then splice complementary time weights to a source-disjoint crossing when available.

# fleet03/B03 r50 — fresh-hub slope Plancherel and complementary-weight splice

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW SUPPORTING TIME-INTEGRAL THEOREM + LINEAR-SMALL-BALL SPLICE / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh scope and source-match correction


- no law-uniform pointwise quadratic van-der-Corput decay for arbitrary cap-one laws;
- no independence after rotating the original coordinates;
- no conditional cap for one conjugate sum/difference variable given the other (`QFORM-UV-CONDITIONAL-CAP-FALSE`);
- no replacement of conditional density caps by independence (`QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`);
- no arbitrary-joint coarea-height shortcut and no dependence-blind X-ray/fiber-supremum closure.

The unrestricted theorem and full-target continuity remain OPEN.

The previous B03 r49 report ended by listing the bare **null-pivot** near-coloop density as an unpaid implication. Fresh source matching changes that bookkeeping: the exact zero-hub-square implication is already paid by

`QFORM-FRESH-HUB-DIVISIBLE-TWIST-ABSORPTION-v1`,

at

`yspennstate/math-open-problems@be8062b160868bcc71aff45a77c56ff2d0501a9a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260923T203140Z-fleet02-B16-QFORM-r36/REPORT.md`.

That theorem retains arbitrary light leakage of the form `2LT` by translating one untouched physical hub source and proves the zero-pivot near-coloop density bound. Thus r49's half-Riesz theorem remains valid, but its listed next debt was stale. The live collar is the **nonzero physical hub square** isolated by fleet03/B16:

`yspennstate/math-open-problems@bdbe6e38a3ee3d586e8e6119e518c573310253fb`.

There the exact-rank-three hard chamber has

`Q=a(sqrt(c)X_0+S)^2+2b(sqrt(c)X_0+S)U+uU^2+2vUV+wV^2`,

with `c>63/64`, `D=|det Lambda|>=1`, and the only unpaid Rayleigh collar after the completed outer-pivot bound is

`0<|a|D<2^-12`.

The result below attacks that collar at the assigned **decoupled-time** level without deleting the nonzero `a X_0^2` term.

## 2. Fresh-hub slope Plancherel

### Theorem 2.1 — `QFORM-FRESH-HUB-SLOPE-PLANCHEREL-v1`

Let `H` be a real random variable with probability density `f_H<=1`. Let `W` be an arbitrary random object independent of `H`. Let `L=L(W)` be real-valued with a marginal density satisfying

`||p_L||_infinity <= M`,

and let `R=R(W)` be an arbitrary measurable real function, with no independence assumed between `L` and `R`. For arbitrary real `a` and nonzero real `gamma`, define

`Q = a H^2 + 2 gamma H L + R`.

Then for every `t!=0`,

`boxed:
 |phi_Q(t)|^2 <= min{1, pi M/(|gamma| |t|)}.
`

Consequently

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <= 8 sqrt(pi M/|gamma|).
`

If `Q'` is an independent copy of the **whole scalar output** `Q`, then

`boxed:
 E|Q-Q'|^(-1/2) <= 4 sqrt(2M/|gamma|).
`

The bounds are uniform in the hub-square coefficient `a` and in the complete same-source dependence of `L` and `R`.

### Proof

For fixed `t!=0` and `l`, write

`I_t(l)=int_R f_H(h) exp(i t[a h^2+2 gamma l h]) dh`.

Conditioning only on the light object `W` gives

`phi_Q(t)=E_W[ exp(i t R(W)) I_t(L(W)) ]`.

Cauchy--Schwarz therefore yields

`|phi_Q(t)|^2 <= E |I_t(L)|^2`.

Since the marginal density of `L` is bounded by `M`,

`E|I_t(L)|^2 <= M int_R |I_t(l)|^2 dl`.

Use Fourier convention

`hat g(xi)=int_R g(h)e^{i xi h} dh`

and put

`g_t(h)=f_H(h)e^{i t a h^2}`.

Then

`I_t(l)=hat g_t(2 gamma t l)`.

By the change of variables `xi=2 gamma t l` and Plancherel,

`int_R |I_t(l)|^2 dl
 = [1/(2|gamma t|)] int_R |hat g_t(xi)|^2 dxi
 = [pi/(|gamma t|)] int_R f_H(h)^2 dh`.

Because `0<=f_H<=1` and `int f_H=1`,

`int f_H^2 <=1`.

Thus

`|phi_Q(t)|^2 <= pi M/(|gamma||t|)`.

Together with the trivial bound `|phi_Q(t)|<=1`, this proves the pointwise **squared-characteristic** envelope. Notice what made this possible: Plancherel is taken in the random **linear slope parameter** `l`, whereas the rough chirped factor `exp(i t a h^2)` has modulus one. No pointwise quadratic-phase decay is asserted.

Let

`K=pi M/|gamma|`.

Splitting at `|t|=K`,

`int_R |t|^(-1/2) min(1,K/|t|) dt
 =2[ int_0^K t^(-1/2)dt + K int_K^infinity t^(-3/2)dt ]
 =8 sqrt(K)`.

This is the second displayed estimate.

Finally, with the programme's Fourier convention, the positive-regularized Riesz identity is

`int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 =sqrt(2 pi) E|Q-Q'|^(-1/2)`.

Dividing by `sqrt(2pi)` gives

`E|Q-Q'|^(-1/2)
 <=4 sqrt(2M/|gamma|)`.

Only the whole scalar copy difference is used. No `X-X'` coordinate is separated from its conjugate `X+X'`. QED.

## 3. Application to the actual nonzero near-coloop collar

Use the exact fleet03/B16 hard-chamber representation

`Q=a(sqrt(c)X_0+S)^2+2b(sqrt(c)X_0+S)U+uU^2+2vUV+wV^2`.

Here `X_0` is a genuine original-coordinate source independent of the entire leaf bank. The coefficient vectors of `S,U,V` on the leaf bank satisfy

`||S_coeff||_2^2=1-c`,
`||U_coeff||_2=||V_coeff||_2=1`,
`S_coeff . U_coeff = S_coeff . V_coeff = U_coeff . V_coeff=0`.

Expand only in the genuine physical hub `H=X_0`:

`Q=ac H^2+2 sqrt(c) H (aS+bU)+R(leaves)`.

Thus Theorem 2.1 applies with

`gamma=sqrt(c)`,
`L=aS+bU`.

The coefficient vector of `L` has Euclidean norm

`sigma_L=sqrt(a^2(1-c)+b^2)`.

The standard one-dimensional product-projection bound for independent cap-one sources gives

`||p_L||_infinity <= sqrt(2)/sigma_L`.

The deterministic spectral gap gives

`a^2+b^2=||Lambda e_1||_2^2 >=1`

in the normalized owner target. Hence

`sigma_L^2=a^2(1-c)+b^2
 =a^2+b^2-ca^2
 >=1-ca^2`.

In the exact unpaid collar

`c>63/64`, `D>=1`, `0<|a|D<2^-12`,

we have `|a|<2^-12` and therefore

`sigma_L^2>1-2^-24`.

Consequently

`M/|gamma|
 <= sqrt(2)/(sqrt(c) sigma_L)
 < sqrt(2)/(sqrt(63/64)*sqrt(1-2^-24))
 =1.4253933326796289...`.

Theorem 2.1 now gives the genuinely uniform collar estimates

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <16.929038195804875,
`

and

`boxed:
 E|Q-Q'|^(-1/2)
 <6.753709102837353.
`

These bounds retain the nonzero physical square `acX_0^2`, the puncture `2aSU`, the full dependent leaf quadratic `R`, all signs, and arbitrary fragmented or unbounded cap-one input laws. They do **not** prove `||p_Q||_infinity<infinity` for the bare collar, because a weighted collision energy alone is weaker than a one-copy translation-uniform half-Riesz potential. This distinction is essential and agrees with the live caps-only counterexample in fleet03/B16.

Thus the new result pays the assigned **time-integral** debt in the genuinely nonzero collar, but the one-copy height step remains explicit.

## 4. Complementary-weight splice: when the time resource gives linear small-ball scaling

The preceding weighted collision estimate can be turned into an `L^1` characteristic-function bound when a source-disjoint component provides the complementary positive half-weight.

### Lemma 4.1 — `QFORM-COMPLEMENTARY-WEIGHT-SPLICE-v1`

Let `S,T` be independent real random variables. Assume

`A_- = int_R |t|^(-1/2)|phi_S(t)|^2 dt < infinity`,

`A_+ = int_R |t|^(1/2)|phi_T(t)|^2 dt < infinity`.

Then `S+T` has a continuous `C_0` density and

`boxed:
 ||p_(S+T)||_infinity <= (2pi)^(-1) sqrt(A_- A_+).
`

Therefore every interval `I` obeys the genuine linear small-ball estimate

`P(S+T in I) <= (2pi)^(-1) sqrt(A_- A_+) |I|`.

### Proof

Independence gives

`phi_(S+T)=phi_S phi_T`.

Cauchy--Schwarz with weights `|t|^{-1/2}` and `|t|^{1/2}` gives

`int |phi_S(t)phi_T(t)|dt
 <=sqrt(A_- A_+)`.

Hence the characteristic function is in `L^1`; Fourier inversion gives a bounded continuous density vanishing at infinity, with the displayed norm bound. QED.

### Concrete two-bank crossing compiler

Apply the completed B03 theorem `QFORM-TWO-BANK-LOCAL-PHASE-PLANCHEREL-v1`, canonical source

`yspennstate/math-open-problems@545738ea4ac5730dc20e6ed5f50315dfcf3322f1`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T215603Z-fleet03-B03-QFORM-r41/REPORT.md`.

For a source-disjoint component

`T=F(X)+G(Y)+X^T C Y`, `X,Y in R^2`, `det C !=0`,

with the four physical scalar inputs mutually independent and cap-one, r41 proves

`|phi_T(t)| <= min{1, 2pi |det C|^(-1/2)|t|^(-1)}`

while allowing arbitrary same-bank measurable phases `F,G`. Put

`A=2pi |det C|^(-1/2)`.

Then

`int_R |t|^(1/2)|phi_T(t)|^2dt
 <=2[ int_0^A t^(1/2)dt + A^2 int_A^infinity t^(-3/2)dt ]
 =(16/3) A^(3/2)`

and hence

`boxed:
 A_+ <= (16/3)(2pi)^(3/2)|det C|^(-3/4).
`

Combining this with Theorem 2.1 for the source-disjoint fresh-hub packet gives

`boxed:
 ||p_(S+T)||_infinity
 <= [2^(13/4)/sqrt(3)]
    (M/|gamma|)^(1/4)|det C|^(-3/8).
`

This is an actual linear-small-ball compiler from the assigned negative-half weighted time resource. On the normalized near-coloop collar above, if a genuinely source-disjoint crossing with `|det C|>=1` is present, the numerical bound is

`boxed:
 ||p_(S+T)||_infinity <6.001648263752153,
`

and the density is continuous. This is a sufficient branch, not a claim that every unresolved collar automatically contains such a disjoint crossing.

## 5. Required designated-partner application: fleet04/B03 r4

The newest completed designated-partner handoff consumed in this run is fleet04/B03 r4,

brain handoff commit `d0836f4eda662ba6298b9c61658e474da836c232`,

canonical mathematics

`yspennstate/math-open-problems@5f93186cf8952b2b8b0255e08a78fd8506c613e4`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B03/20260924T051411Z-fleet04-B03-plucker-overlap2-r4/REPORT.md`.

In its exact-rank-three overlap-two branch it applies the literal inequality

`||p_Q||_(infinity,ess)
 <=129.924435862525374 J_2(H)^(-1/6)`.

Apply this completed partner result to the B03 assigned whole-copy time quantity. Since the density of `Q-Q'` is `p_Q * tilde p_Q`,

`||p_(Q-Q')||_infinity <= ||p_Q||_infinity`.

The elementary cap-to-half-Riesz estimate gives

`E|Q-Q'|^(-1/2)
 <=2 sqrt(2 ||p_Q||_infinity)`.

Therefore the whole-copy Riesz identity yields the actual inequality

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2dt
 <=80.81283593365677 J_2(H)^(-1/12).
`

Under the partner's normalized diffuse-Pluecker hypotheses `Delta>=1`, `eta>=1/4`, `w_*<=eta/6`, its density estimate is `<333.880`, so the same calculation gives

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2dt
 <129.54782623760602.
`

This is an equation-level application of the completed designated-partner result, not a transfer of independence to spectral or sum/difference coordinates.

## 6. What is and is not closed

Newly proved here:

1. A **uniform squared-characteristic Plancherel estimate** for a rough fresh physical hub with arbitrary nonzero quadratic square coefficient, after averaging over a random slope with bounded marginal density.
2. A uniform negative-half weighted whole-copy time bound `<16.93` in the exact current nonzero near-coloop collar `0<|a|D<2^-12`.
3. The corresponding collision half-Riesz bound `<6.754`.
4. A complementary-weight Fourier compiler that converts this resource into a bounded continuous density and linear small-ball estimate whenever a genuinely source-disjoint invertible `2x2` physical crossing supplies the positive-half time budget.
5. A concrete application of the newest fleet04/B03 overlap-two result to the assigned time integral.

Not proved:

- The bare nonzero near-coloop collar does not yet have a universal `L^infinity` density bound from Theorem 2.1 alone.
- The structural hypothesis `s_3(A)>=1` has not been shown to force the source-disjoint crossing used in Section 4.
- The unrestricted QFORM theorem remains OPEN.
- Full-target continuity remains OPEN.

The next B03 implication is now precise: **upgrade the collar's uniform collision/time resource to a one-copy height bound using the actual three-dimensional product-projection provenance of `(S,U,V)`, or prove that every remaining structural survivor supplies a complementary positive-half time resource on a source-disjoint bank.** A dependence-blind marginal/conditional-cap upgrade is ruled out by the existing counterexample and will not be attempted.
