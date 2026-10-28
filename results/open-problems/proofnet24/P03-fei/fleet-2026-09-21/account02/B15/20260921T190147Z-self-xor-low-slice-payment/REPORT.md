TASK: B15 ACCOUNT: account02 RUN: 2026-09-21T19:01:47.792390Z — FEI spectral remainder: self-XOR dual-slice payment after the mandatory three-run mechanism pivot

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**

**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated mathematical/cognitive brain retrieval was used in this derivation.

**Model self-report:** GPT-5.6 Sol. **Reasoning effort requested:** maximum actually supported. **Configured/known reasoning effort:** UNKNOWN / not exposed. **Provider reasoning usage:** null / not exposed.

## 0. Fresh state and mandatory pivot


Fresh scientific master on entry was `005117d95f146d0f47c3272149d7aaaed5f6e9ab`; it advanced during the run and was refreshed before writing. I read the current P03 README, the complete latest B15 packet reports, the interactive centered-critical-budget report, B17's self-XOR/Hellinger bridge, B18's current physical mask/Radon integration, and the September-20 spectral-lattice / centroid-and-carries state through the current README. The inherited facts retained here include:

- Full FEI remains open.
- For unequal-magnitude packets, the physical lattice hypothesis is extra; dyadic Fourier coefficients do **not** imply integral physical magnitude projections.
- The universal arithmetic identity `H=2R+2D` and `R<=2J` are valid, but no universal `D<=C I` is known.
- The B15 valuation-depth theorem strengthens `R<=2J` to all-cost / all-tail majorization. It therefore certifies that valuation depth itself is influence-paid, but it does not control normalized physical mesh depth. In particular, the one-point defect has `r_a=0` on its packets while retaining the hard entropy/mesh behavior.
- Raw arithmetic normalizers, packet-local geometry payment, unconditional tensor subadditivity of `D`, and credit-free arithmetic/product interpolation have explicit Boolean obstructions and are not retried below.

### Required comparison with the last THREE B15 reports

1. `20260921T120837Z-punctured-majority-packet-obstruction`: packet-local payment was refuted by a constant-mass affine-simplex packet with logarithmically growing local deficit. The remaining universal implication was a **cross-packet** Boolean compensation theorem retaining global negative credits.
2. `20260921T150419Z-packet-product-bridge`: arithmetic and product-measure KL identities were fused exactly; the raw normalizer disappeared, but the bridge-law KL was proved indispensable. The remaining implication was a dimension-free payment of the **combined** variational residual with that KL retained.
3. `20260921T170301Z-valuation-tail-majorization`: all valuation-depth tails were paid by folded influence and every credit-free escort interpolation was refuted. The remaining implication was still a dimension-free payment of the **physical-mesh / joint-information residual**, with negative information credits retained.

**FULL-PROBLEM CHANGE (same convention, before -> after):** `OPEN / no finite universal FEI upper constant proved -> OPEN / no finite universal FEI upper constant proved`.

**MECHANISM CHANGE (same convention, before -> after):** `packet arithmetic / mesh / escort-KL bookkeeping -> canonical iid spectral self-XOR plus signed Boolean cancellation and physical dual translations`.

**Exact unpaid implication before this run:** a dimension-free global payment for the unequal-magnitude entropy/mesh residual after all known valuation and KL credits are retained.

That implication has remained unpaid across the three reports above. Under the continuation order this run therefore **executes a materially different FEI mechanism now** rather than extending the arithmetic equivalence list. The valuation-tail theorem is used as the stopping certificate for that old mechanism: it has already paid the entire valuation-depth bank, while the residual can remain hard at valuation zero. The new mechanism below pays a genuine universal slice of a different, joint negative-credit representation.

## 1. Entering self-XOR bridge

Let `a_s=fhat(s)`, `p_s=a_s^2`, with normalized Walsh transform and `sum_s p_s=1`. Let `S,S'` be independent with law `p`, and put `D=S xor S'`. Write

`c_d=Pr[D=d]=sum_s p_s p_{s+d}`

and define the Hellinger overlap

`A_d=sum_s sqrt(p_s p_{s+d})=sum_s |a_s a_{s+d}|`.

B17's fresh self-XOR theorem proves `H(f)<=B(p)`, where

`B(p)=H(D)+sum_d c_d log_2 A_d`.

Since `A_d>=c_d` termwise and `A_0=1`, this is

`B(p)=sum_d b_d`,

`b_d:=c_d log_2(A_d/c_d)>=0`, with value zero when `c_d=0`.              (1.1)

This keeps the negative Hellinger credit inside every atom rather than discarding it. The point here is not to rename FEI as `B<=CJ`: it is to pay a genuine universal part of (1.1).

## 2. PROVED: all-shift physical dual collision/Hellinger bound

For a physical translation `x`, define

`delta_x(f)=Pr_y[f(y)!=f(y+x)]`,

`q_x(f)=min(delta_x(f),1-delta_x(f))`.

The folded quantity `q_x` is character-invariant.

### Theorem B15-SELF-XOR-DUAL-01

For every Boolean `f`, every nonzero frequency shift `d`, and every physical translation `x` with `d dot x=1 mod 2`, put `q=q_x(f)`. Then

`c_d <= 2 q^2(1-q)`,                                                    (2.1)

`A_d <= 2 sqrt(q(1-q))`,                                                (2.2)

and consequently

`b_d=c_d log_2(A_d/c_d) <= 2 q_x(f)`.                                  (2.3)

The sharper mass-weighted form retained before the last scalar simplification is

`b_d <= c_d log_2(2 sqrt(q(1-q))/c_d)`.                                (2.4)

No FEI inequality is used.

### Proof

Fix `d,x` with `d dot x=1`. Let `H=ker(d)`. Every physical point has a unique representation `y=z+b x`, `z in H`, `b in {0,1}`. Multiplying `f` by `chi_d` swaps agreement and disagreement across each `x`-pair while translating the spectral law and leaving `c_d,A_d` invariant. Hence assume `q=delta_x(f)<=1/2`.

On `H`, define

`s(z)=(f(z)+f(z+x))/2`, `g(z)=(f(z)-f(z+x))/2`.

Because `f` is Boolean, `s,g in {0,+-1}`, their supports are disjoint,

`E s^2=1-q`, `E g^2=q`, and `E|g|=q`.                                 (2.5)

Characters of `H` index the spectral pairs `{u,u+d}`. With one representative per pair, the two parent coefficients are `shat_u` and `ghat_u` up to an irrelevant sign. Thus

`c_d=2 sum_u shat_u^2 ghat_u^2`,                                      (2.6)

`A_d=2 sum_u |shat_u ghat_u|`.                                        (2.7)

Since `|ghat_u|<=E|g|=q`, Parseval yields

`c_d<=2q^2 sum_u shat_u^2=2q^2(1-q)`, proving (2.1). Cauchy--Schwarz in (2.7) gives (2.2).

For (2.3), set `C=2q^2(1-q)` and `M=2sqrt(q(1-q))`. If `q=0`, then `c_d=0`. For `0<q<=1/2`, `C/M=q^(3/2)sqrt(1-q)<=1/4<1/e`, so `t log_2(M/t)` is increasing throughout `0<t<=C`. Hence

`b_d<=C log_2(M/C)`

`=[2q^2(1-q)/ln2][(3/2)ln(1/q)+(1/2)ln(1/(1-q))]`.                    (2.8)

After dividing by `q`, use `q ln(1/q)<=1/e` and `-(1-q)ln(1-q)<=q`; the numerator is at most `3/e+1/4<2 ln2`. Therefore `b_d<=2q`. QED.

The quadratic factor in (2.1) is genuinely Boolean: the odd slice `g` is supported on a set of density exactly `q`, so every Fourier coefficient of that slice is at most `q` in magnitude. The statement is also basis-honest: the physical object is the actual translation `x`; no arbitrary linear change is charged as though it preserved original-coordinate influence.

## 3. PROVED: zero + singleton self-XOR slice is influence-paid

Let `q_i=min(Inf_i(f),1-Inf_i(f))` and `J(f)=sum_i q_i`. Multiply `f` by its median character so its coordinate influences equal `q_i`; `c,A,b` are unchanged.

### Corollary B15-SELF-XOR-LOW-SLICE-02

For every Boolean `f`,

`b_0 + sum_i b_{e_i} <= (2+2/ln2) J(f) < 4.886 J(f)`.                  (3.1)

For `d=e_i`, choose `x=e_i` in Theorem 2.1, yielding `b_{e_i}<=2q_i`, hence `sum_i b_{e_i}<=2J`.

For `d=0`, `A_0=1`, so `b_0=c_0 log_2(1/c_0)`. Also

`1-c_0=Pr[D!=0] <= E|D| = sum_i 2q_i(1-q_i) <=2J`.                    (3.2)

Using `-t ln t<=1-t`,

`b_0<=(1-c_0)/ln2<=2J/ln2`. QED.

Define the genuinely multi-coordinate remainder

`B_{>=2}(f)=sum_{d:|d|>=2} b_d`.                                      (3.3)

Because `H(f)<=B(p)`, the exact unpaid implication on this mechanism is now

`B_{>=2}(f) <= K J(f)` for one universal finite `K`.                   (3.4)

If (3.4) is proved, then

`H(f) <= [K+2+2/ln2] J(f) <= [K+2+2/ln2] I(f)`.                        (3.5)

Equation (3.4) is not proved here. Unlike the prior arithmetic targets, however, this run removes a nonzero universal portion of the joint residual with a proved dimension-free payment while retaining the exact Hellinger credit in every remaining atom.

## 4. PROVED: bounded-incidence dual families are paid

Let `E` be any finite family of nonzero frequency shifts. For each `d in E`, choose a physical translation `x_d` with `d dot x_d=1`. Suppose that after median-character folding every original coordinate belongs to at most `L` of the supports `supp(x_d)`. Then

`sum_{d in E} b_d <= 2 L J(f)`.                                       (4.1)

Indeed, Theorem 2.1 gives `b_d<=2q_{x_d}`. In the folded function,

`q_{x_d}<=delta_{x_d}<=sum_{i in supp(x_d)} q_i`                       (4.2)

by traversing the translation along its original-coordinate path. Summing proves (4.1).

For `E={e_i}`, take `x_{e_i}=e_i`, `L=1`, recovering the singleton payment. The full set of all nonzero shifts cannot be handled by assigning one unweighted witness to every shift with bounded incidence; a successful continuation must preserve the actual masses `c_d` and Hellinger refunds `A_d` in (2.4), or exploit further Boolean cancellation among multi-coordinate shifts.

## 5. Role of the valuation-tail theorem

The preceding B15 valuation majorization is not re-proved. It is applied here as a route-elimination gate: it already pays `R=E_p r_a` and every depth tail of `r_a` by folded influence. Splitting the old arithmetic remainder again on `r_a>=m` cannot reach the mandatory one-point-defect stress test because its hard packets have `r_a=0`. After three arithmetic reports with the same unpaid implication, this is why the present run moves to the Boolean self-XOR constraint rather than extending the valuation/mesh equivalence list.

## 6. Exact finite verification

`verify_b15_selfxor_low_slice.py` exhausts **all 65,812 Boolean truth tables through dimension four**. For every nonzero frequency shift `d` and every physical translation `x` with `d dot x=1`, it verifies the rational parts of (2.1)-(2.2), the exact Boolean signed self-convolution, the singleton contribution bound, and the aggregate zero+singleton inequality.

Executed totals:

- Boolean functions: `65,812`;
- dual `(d,x)` rational checks: `7,871,588`;
- singleton checks: `262,948`;
- largest observed `(b_0+sum_i b_{e_i})/J`: `1.8310938414579052`;
- proved analytic bound: `2+2/ln2 = 4.885390081777927`.

Finite checks validate implementation only; the universal statements above are analytic.

Checker SHA-256 before repository write: `d60fbca7be52d37970fc245eb9a203e649fc0f848baa606d58c6db7284346aae`.

Recorded output SHA-256: `8e20231c5e921ffaa160aea54401331271d5e937334eed775d556148719218b9`.

The one-point defect, odd majority, five-variable physical-lattice counterexample, and valuation-misaligned product collision remain valid stress tests. No step assumes projection integrality, packet tensor subadditivity, coordinatewise scalarization of the self-XOR law, or a global l1 budget.

## 7. Coordination / non-overlap

B17 owns the **global self-XOR/Hellinger bridge** and proved that coordinate-marginal scalarization loses the decisive joint total correlation. This B15 report does not re-derive that bridge; it pays a specific universal part of its exact atomwise negative-credit expansion using Boolean physical slices.

B18 owns physical product-noise / mask-Radon and curvature-refund integration. The B15 theorem supplies an all-shift dual-translation atom estimate and original-coordinate bounded-incidence corollary but does not claim B18's compiler or Radon push-forward. B14 remains on restriction/critical-core selection and B16 on signed q-flip/current compilation. The remaining B15 scope is the mass-weighted multi-shift remainder (3.4), preserving `c_d`, `A_d`, signs and original-coordinate geometry.

## 8. Current primary literature check

A fresh primary-source check on 21 September 2026 still finds unrestricted FEI open in the inspected sources:

- V. N. Potapov, arXiv:2609.21563, posted 18 September 2026: FEI for plateaued functions (sharp class constant 4) and partially bent functions (sharp class constant 2), not all Boolean functions.
- M. J. González, P. MacManus, M. C. Pereyra, arXiv:2606.00246, 29 May 2026: restriction/stopping-tree progress and new classes, but no full universal restriction theorem.
- P. Li, G. Han, arXiv:2512.03117, 2 December 2025: a strengthened information-theoretic Fourier entropy/influence inequality retaining the coordinate influence-profile entropy term.

No publication-priority claim is made for B15-SELF-XOR-DUAL-01 or its low-slice corollary.

## 9. Before / after and next exact obligation

**Before:** after three B15 arithmetic reports, valuation depth was fully influence-paid but the physical-mesh / joint-information residual still required a global negative-credit payment; refining the same packet axis again would violate the mandated pivot rule.

**After:** on the materially different canonical self-XOR mechanism, every shift `d` has a source-exact Boolean dual-translation bound (2.1)-(2.4), the entire zero plus weight-one Hellinger-refunded contribution is universally paid by `<4.886 J`, and every bounded-incidence dual family is paid in original coordinates.

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`.

**MECHANISM CHANGE:** `packet arithmetic/mesh -> self-XOR atomwise Hellinger-refunded dual-translation payment`.

**Precise remaining obligation:** prove or refute a dimension-free **mass-weighted** physical-dual payment for

`B_{>=2}(f)=sum_{|d|>=2} c_d log_2(A_d/c_d)`

without replacing it by coordinate marginals, raw l1 norms, unweighted all-shift covers, or arbitrary linear-coordinate budgets. A promising exact form is to preserve (2.4) while assigning only the actual mass-bearing multi-shifts to physical translations `x` with `d dot x=1`, with congestion weighted by the same `c_d` / Hellinger information. If such a statement has universal constant `K`, (3.5) gives full FEI. A Boolean family violating every such mass-weighted assignment would decisively terminate this pivot and should be preserved rather than hidden.
