TASK: B15 ACCOUNT: account02 RUN: 2026-09-21T15:04:19.574061Z — FEI spectral remainder: exact packet/product-measure bridge and an essential-KL obstruction

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**

**Execution context: WITHOUT_VERIFIED_BRAIN.** No genuine retrieved brain context was used.

**Model self-report:** GPT-5.6 Sol. **Reasoning effort requested:** maximum actually supported. **Configured/self-reported reasoning effort:** UNKNOWN / not exposed. **Provider reasoning usage:** not exposed.

## 0. Current assignment and what moved

This run adopts `FEI-PROOF-NUMERICS-SPRINT-20260921T120803Z`, B15/account02: derive an exact entropy-versus-arithmetic-remainder bridge, with all constants and without circular use of FEI. It continues the preceding B15 identities

- `H=2R+2D`, with `R=sum_a p_a r_a` and `D=sum_a p_a log_2(1/b_a)`;
- `2D=log_2 N-D_KL,2(p||q^N)` for `N_a=|A_a|4^{-r_a}`, `N=sum_a N_a`, `q^N_a=N_a/N`;
- packet-local payments and unconditional product subadditivity are false.

The new step is to fuse the arithmetic normalizer law with the independent Bernoulli law having the actual spectral coordinate marginals. The raw `log N` then cancels exactly. The surviving negative credits are (i) one KL divergence to a geometric bridge law on magnitude packets and (ii) a within-packet conditional KL divergence. This gives a genuinely different exact representation of the unpaid remainder and spectral entropy.

A second new result is a decisive obstruction: on the Boolean one-point defect family, the geometric bridge partition function has `log Z ~ (1/2)log_2 n`, while the total influence tends to zero. The new packet-law KL has the same leading `(1/2)log_2 n` and is therefore indispensable. Dropping it destroys any dimension-free influence payment even if the within-packet KL is retained.

Creative moves used, distinct from the preceding run: **#11 dualize** (compare the arithmetic packet law to the maximum-entropy product law with the same marginals), **#12 find what is conserved** (two exact representations of the same `2D`), and **#25 count the same thing twice** (fuse the two KL decompositions rather than upper-bounding either separately).

Tracked quantity: the number of explicitly retained nonnegative information credits in the exact arithmetic bridge changes from **one packet KL** to **two fused credits** (bridge-law KL plus within-packet KL), while the raw normalizer `log N` disappears from the combined formula. This does **not** produce a universal FEI constant.

## 1. Notation

Let `f:{0,1}^n->{-1,+1}` and let the spectral sample `S` have law

`mu(S)=fhat(S)^2`.

For each distinct nonzero Fourier magnitude `a`, let

`A_a={S:|fhat(S)|=a}`, `p_a=mu(A_a)=|A_a|a^2`.

Conditional on the packet label `A=a`, the spectral sample is exactly uniform on `A_a`.

Use the inherited arithmetic quantities

`r_a=min_{V_a(x)!=0} nu_2(V_a(x))`, `b_a=a 2^{r_a}`,

`N_a=|A_a|4^{-r_a}=p_a/b_a^2`, `R=sum_a p_a r_a`,

`D=sum_a p_a log_2(1/b_a)`.

Then

`H(f)=2R+2D`.                                                        (1.1)

Let

`j_i=Pr_mu[i in S]=Inf_i(f)`

and let `nu` be the product Bernoulli law on subsets with these same marginals:

`nu(S)=prod_{i in S} j_i prod_{i notin S}(1-j_i)`.                   (1.2)

Endpoint coordinates `j_i in {0,1}` are interpreted in the usual limiting/support sense. Every `S` in `supp(mu)` has positive `nu(S)`.

For each magnitude packet define its product-shadow mass

`beta_a=nu(A_a)`,                                                     (1.3)

and let `beta_perp=nu(2^[n] \ supp(mu))`. Thus `(beta_a,beta_perp)` is a probability vector, while `(p_a,0)` is the corresponding packet-label law under `mu`.

Finally define the bridge partition function and bridge law

`Z=sum_a sqrt(N_a beta_a)`,

`m_a=sqrt(N_a beta_a)/Z`.                                            (1.4)

## 2. Exact packet/product-measure bridge

### Theorem B15-PRODUCT-BRIDGE-01

For every Boolean `f`, with all logarithms and KL divergences in base two, define the within-packet conditional credit

`C_in = sum_a p_a D_KL,2( Unif(A_a) || nu(.|A_a) ) >=0`.             (2.1)

Then

`4D = sum_i h_2(j_i) - 2R + 2 log_2 Z`

`     - 2 D_KL,2(p||m) - C_in`.                                     (2.2)

Equivalently,

`H(f) = R + (1/2)sum_i h_2(j_i) + log_2 Z`

`       - D_KL,2(p||m) - (1/2)C_in`.                                (2.3)

No FEI inequality is used in this theorem.

### Proof

There are two exact representations of `2D`.

First, put

`N=sum_a N_a`, `q^N_a=N_a/N`.

The preceding packet free-energy identity is

`2D = log_2 N - K_N`,

`K_N:=D_KL,2(p||q^N)`.                                               (2.4)

Second, the independent product law `nu` has the same coordinate marginals as `mu`. Therefore its entropy is `sum_i h_2(j_i)`, and the standard maximum-entropy identity is exact:

`T:=D_KL,2(mu||nu)=sum_i h_2(j_i)-H(f)`.                             (2.5)

Using (1.1),

`2D=sum_i h_2(j_i)-2R-T`.                                            (2.6)

Now apply the KL chain rule to the map that records the magnitude packet and sends points outside `supp(mu)` to a symbol `perp`. Since `mu(.|A_a)=Unif(A_a)`,

`T = K_beta + C_in`,                                                  (2.7)

where

`K_beta=D_KL,2( (p_a,0) || (beta_a,beta_perp) )`

`      =sum_a p_a log_2(p_a/beta_a)`.                                (2.8)

The two packet-label KL divergences combine exactly. Set

`B=sum_a sqrt(q^N_a beta_a)=Z/sqrt(N)`

and

`m_a=sqrt(q^N_a beta_a)/B=sqrt(N_a beta_a)/Z`.

Then, by direct expansion,

`K_N+K_beta`

` =sum_a p_a log_2[p_a^2/(q^N_a beta_a)]`

` =2 D_KL,2(p||m)-2 log_2 B`.                                        (2.9)

Add (2.4) and (2.6), substitute (2.7)-(2.9), and use

`log_2 N + 2 log_2 B = 2 log_2 Z`.                                  (2.10)

This proves (2.2). Equation (2.3) follows from `H=2R+2D`. QED.

### What the identity preserves

The old raw-normalizer formula loses all information if `K_N` is simply discarded. The marginal-entropy formula loses all dependence information if `T` is discarded. Equation (2.2) fuses them before discarding anything. The apparently dangerous `log N` cancels exactly against the normalization hidden in the Hellinger/Bhattacharyya overlap `B`.

The two remaining explicit nonnegative credits are structurally different:

1. `D_KL(p||m)` measures mismatch between the actual packet masses and the geometric mean of the arithmetic normalizer weights `N_a` and product-shadow masses `beta_a`.
2. `C_in` measures non-product structure *inside* each equal-magnitude packet after conditioning the product law to that packet.

Dropping only `C_in` gives the valid universal upper bound

`H(f) <= R + (1/2)sum_i h_2(j_i)+log_2 Z-D_KL,2(p||m)`.              (2.11)

This is not yet FEI: the surviving right-hand side has not been bounded by a universal multiple of influence.

## 3. The bridge-law KL is essential: one-point defect

Let

`f_n(x)=1-2 1_{x=0}`, `n>=3`.

Its unnormalized Walsh spectrum is

`W(empty)=2^n-2`, `W(S)=-2` for every nonempty `S`.

Thus there are two magnitude packets:

`A_0={empty}`, `N_0=1`, `r_0=0`,

`A_1={S:S!=empty}`, `N_1=2^n-1`, `r_1=0`.                            (3.1)

Every spectral coordinate has

`j=2^{1-n}`.                                                         (3.2)

Hence under the product law

`beta_0=(1-j)^n`, `beta_1=1-(1-j)^n`,                               (3.3)

and

`Z=sqrt(beta_0)+sqrt((2^n-1)beta_1)`.                               (3.4)

Since `beta_1=nj+O(n^2j^2)=n2^{1-n}(1+o(1))`,

`Z=sqrt(2n)(1+o(1))`,

`log_2 Z=(1/2)log_2(2n)+o(1)`.                                      (3.5)

Meanwhile the actual packet mass on `A_0` is

`p_0=(1-2^{1-n})^2=1-o(1)`,                                         (3.6)

whereas the bridge law has

`m_0=sqrt(beta_0)/Z=(2n)^{-1/2}(1+o(1))`.                            (3.7)

Therefore

`D_KL,2(p||m)=(1/2)log_2(2n)+o(log n)`.                             (3.8)

The leading growth in (3.5) is cancelled by (3.8).

This cancellation cannot be replaced by `C_in`. Indeed `0<=C_in<=T`, where `T` is the total correlation in (2.5), and

`T<=sum_i h_2(j_i)=n h_2(2^{1-n}) -> 0`.                             (3.9)

Also `R=0` and the total influence is

`I(f_n)=n2^{1-n}->0`.                                                (3.10)

Consequently, if one drops the bridge-law KL term from (2.3), even while retaining the within-packet credit, the remaining upper expression contains `(1/2)log_2 n+o(log n)` but influence tends to zero. No dimension-independent influence payment can result.

So the new KL is not decorative bookkeeping. It is asymptotically the entire cancellation mechanism on a canonical genuine Boolean obstruction.

## 4. Relation to the preceding packet obstructions

The preceding B15 run built a punctured-majority family where one constant-mass affine-simplex packet has

`p_a log N_a / e_a^* ~ log n`

while its own exact best affine energy stays `Theta(1)`. That killed every packet-local geometry payment. The present identity explains what a successful cross-packet replacement must retain: the product-shadow masses `beta_a` couple every packet to the *global* spectral coordinate profile, and `D_KL(p||m)` couples the actual packet weights to both arithmetic mesh and that global profile.

This is compatible with the other current B15 mechanisms rather than duplicating them: account01 is working on carry/restriction payment, account03 on mesh/Boolean geometric restrictions, and account04 on extremal/obstruction families. Account02/B14 is on existential restriction, B16 on signed/shared-variable transport, B17 on a distinct support/face route, and B18 on fixed-cardinality Han/restriction descent. The theorem here stays on the unequal-magnitude arithmetic remainder.

## 5. Exact remaining obligation

By the inherited centroid/lattice theorem,

`R <= 2 Ifrak(f) <= 2 I(f)`.                                        (5.1)

Thus full FEI would follow from a dimension-independent bound

`(1/2)sum_i h_2(j_i)+log_2 Z-D_KL,2(p||m)-(1/2)C_in <= K I(f)`       (5.2)

for all Boolean `f`, with resulting FEI coefficient `K+2`.

Equation (5.2) is **not proved here**. Nor is it presented as progress merely because it is another equivalent target. The concrete progress is the exact cancellation of the old raw normalizer and the proof that the new bridge-law KL is forced by an actual Boolean family. Any next inequality on this route must keep that KL, or replace it by a quantitatively equivalent negative credit.

A sharper next attack is to use Boolean restrictions on the product-shadow masses `beta_a`, rather than bounding `Z` and the KL separately. In particular, seek a direct influence-summable estimate on the *combined variational term*

`log_2 Z-D_KL,2(p||m)`                                               (5.3)

plus half the marginal entropy, with the punctured-majority and one-point-defect families as mandatory stress tests.

## 6. Finite sanity check

A direct Walsh enumerator was run on every Boolean truth table in dimensions one through four: `4+16+256+65536=65812` functions. For each function it reconstructed the magnitude packets, exact integer `r_a`, product marginals, `beta_a`, `Z`, `m`, and both KL credits. The largest floating residual in (2.2) was `1.7763568394002505e-15` bits. Per dimension: n=1: 0; n=2: 0; n=3: `8.881784197001252e-16`; n=4: `1.7763568394002505e-15`.

This finite computation is only a sanity check on the algebra and implementation. The theorem is proved above symbolically; the finite sweep is not used to infer any all-dimensional inequality.

## 7. Literature and scope check, 21 September 2026

Fresh primary-source search found no unrestricted FEI upper bound. Relevant current items are:

- V. N. Potapov, *On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions*, arXiv:2609.21563, posted 18 September 2026: FEI for plateaued functions with sharp class constant 4, and partially bent functions with class constant 2. This is a structured-class result, not unrestricted FEI.
- M. J. Gonzalez, P. MacManus, M. C. Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246, 29 May 2026: restriction/stopping-tree progress and new classes, not full FEI.
- P. Li, G. Han, *Strengthening Han's Fourier Entropy-Influence Inequality via an Information-Theoretic Proof*, arXiv:2512.03117, 2 December 2025: an information-theoretic bound retaining an influence-profile entropy term. It is structurally relevant to the `sum_i h_2(j_i)` side of (2.3), but it does not supply the missing dimension-free payment here.

The public optimization-constants ledger currently records an external certified monotone lower bound `C_FEI>6.521845710923046575` from an 18-variable seed. That lower bound corrects the older `6.4547837` unrestricted target but does not affect this upper-bound derivation.

I make no publication-priority claim for Theorem B15-PRODUCT-BRIDGE-01. The KL chain rule and geometric-mean fusion are elementary information identities; their usefulness here is project-specific.

## 8. Before / after ledger

**Before:** the arithmetic route had `2D=log N-K_N`, the marginal-entropy obstruction was known separately, and packet-local geometry as well as unconditional tensor subadditivity were already refuted. It was not clear how to combine the arithmetic KL with the spectral dependence credit without dropping one of them.

**After:** the two credits are fused exactly. The raw `log N` cancels, producing the bridge partition function `Z`, a geometric bridge packet law `m`, and the exact formula (2.2)/(2.3). The one-point defect proves that `D_KL(p||m)` is asymptotically indispensable. Full FEI remains OPEN.

**Next precise obligation:** control the combined variational quantity in (5.2), not `log N`, `Z`, or marginal entropy separately. A useful next theorem would bind `log Z-D_KL(p||m)` to influence using Boolean constraints on the product-shadow packet masses `beta_a`; a counterexample where this combined quantity still outruns influence would decisively kill this bridge route.
