# B13 FEI Booleanity profile — exact upper-zeta posterior divergence and a killed raw-influence payment

**Status:** PARTIAL / PROVED universal auxiliary identity + REFUTED stronger payment. Full uniform-cube Fourier entropy-influence (FEI) remains **OPEN / NOT PROVED**.

**Execution:** **WITHOUT_VERIFIED_BRAIN**. No authenticated mathematical/cognitive brain retrieval or receiver-context use occurred in this run.

**Route:** APPROACHES 2/13/14: block-influence/correlation profiles, Booleanity constraints, and coding/point-process transfer. This run continues fleet03/B13's phase-aware block reduction and directly attacks the residual upper-zeta mixing term. It does not re-run the read-once certificate or audit settled sweeps.

**No novelty claim:** the identities below are new-to-this-run deductions for the fleet. No publication-priority claim is made without a dedicated primary-literature comparison.

## 1. Current exact obstruction

For a probability law `P` on subsets of `[m]`, write

\[
U_P(A)=\sum_{B\supseteq A}P(B)
\]

and define the upper-zeta cancellation functional

\[
B_{\rm can}(P)=\sum_A P(A)\log_2\frac{U_P(A)}{P(A)},
\]

with zero-mass summands omitted.

The preceding fleet03/B13 run proved that for a coordinate split `X \sqcup Y`, the phase loss incurred in replacing coherent Fourier squares by the projected mixture is paid by `J_Y/ln 2`, but leaves `B_can(q)` for the projected mixture `q`. It then refuted the tempting bound

\[
B_{\rm can}((P_0+P_1)/2)-\frac{B_{\rm can}(P_0)+B_{\rm can}(P_1)}2
\le JS(P_0,P_1)
\]

even when both endpoints are Boolean spectral laws.

The exact question attempted here is therefore:

> **Can the Jensen gap of `B_can` be recoded as a genuine information divergence, and can that divergence be paid directly by Boolean disagreement?**

The first part has an exact affirmative answer. The most natural sharp direct payment is then refuted by an exact four-variable Boolean pair.

## 2. Exact upper-zeta posterior identity

### Theorem 2.1 — arbitrary finite mixtures

Let `Y` be a finite label with prior `lambda_y>0`, `sum_y lambda_y=1`. For each label let `P_y` be a probability law on subsets of `[m]`, and put

\[
M(A)=\sum_y\lambda_yP_y(A),\qquad
U_y(A)=\sum_{B\supseteq A}P_y(B),\qquad
U(A)=\sum_y\lambda_yU_y(A).
\]

Whenever `M(A)>0`, define two posterior distributions on the label:

\[
w_A(y)=\frac{\lambda_yP_y(A)}{M(A)}
      =\Pr(Y=y\mid S=A),
\]

\[
v_A(y)=\frac{\lambda_yU_y(A)}{U(A)}
      =\Pr(Y=y\mid S\supseteq A).
\]

Then

\[
\boxed{
B_{\rm can}(M)-\sum_y\lambda_yB_{\rm can}(P_y)
=\sum_A M(A)D_2\!\left(w_A\middle\|v_A\right).
}
\tag{2.1}
\]

Here `D_2` is KL divergence in bits.

In particular:

1. `B_can` is concave under arbitrary finite mixtures;
2. its complete Jensen gap is not ordinary mutual information but the expected divergence between the label posterior from the **exact atom** `S=A` and the label posterior from the **upper-cone event** `S superset A`;
3. this gives the requested **zeta-weighted information divergence** exactly, with no relaxation.

### Proof

For fixed `A` with `M(A)>0`,

\[
\lambda_yP_y(A)=M(A)w_A(y),
\qquad
\lambda_yU_y(A)=U(A)v_A(y).
\]

Therefore

\[
\begin{aligned}
\sum_y\lambda_yP_y(A)\log_2\frac{U_y(A)}{P_y(A)}
&=M(A)\sum_yw_A(y)
 \log_2\frac{U(A)v_A(y)}{M(A)w_A(y)}\\
&=M(A)\log_2\frac{U(A)}{M(A)}
 -M(A)D_2(w_A\|v_A).
\end{aligned}
\]

Summing over `A` gives (2.1). If `w_A(y)>0`, then `P_y(A)>0`, hence `U_y(A)>=P_y(A)>0`, so every KL term appearing with positive weight is finite. QED.

### Binary restriction form

For two Boolean restrictions `h_0,h_1` with equal prior, let

\[
P_b(A)=\widehat h_b(A)^2,\qquad M=(P_0+P_1)/2.
\]

Then the residual from the preceding B13 report is exactly

\[
\boxed{
G_\zeta(P_0,P_1)
:=B_{\rm can}(M)-\frac{B_{\rm can}(P_0)+B_{\rm can}(P_1)}2
=\sum_A M(A)D_2(w_A\|v_A).
}
\tag{2.2}
\]

This is a phase-sensitive/correlation-sensitive object: `w_A` sees exact Fourier-square mass, while `v_A` sees the same endpoint label after upper-zeta aggregation over every strict superset of `A`.

## 3. Why this is structurally different from ordinary JS

For equal priors,

\[
JS(P_0,P_1)=I(Y;S)=1-\sum_AM(A)h_2(w_A).
\]

By contrast, (2.2) replaces the fixed prior `(1/2,1/2)` by the atom-dependent upper-cone posterior `v_A`. Thus `G_zeta` measures how much the endpoint label inferred from **exact membership** disagrees with the endpoint label inferred from **containment of the same atom**.

This explains the explicit three-bit counterexample from the preceding run where `G_zeta>JS`: ordinary channel information does not see the extra distortion created by the upper-set geometry.

The identity is also the missing information-theoretic form suggested by APPROACH 14: `B_can` is an entropy-production functional on the subset poset, and its mixing loss is an exact posterior KL divergence along the zeta/containment channel.

## 4. Natural direct Boolean payment attempted

For Boolean `h_0,h_1`, define their disagreement

\[
\delta=\Pr_x[h_0(x)\ne h_1(x)].
\]

Parseval gives

\[
\|\widehat h_0-\widehat h_1\|_2^2=4\delta.
\]

The preceding magnitude-channel theorem has the sharp payment

\[
JS(P_0,P_1)\le\frac{2}{\ln2}\delta.
\]

The most optimistic continuation of the same mechanism would therefore be

\[
\tag{C}
G_\zeta(P_0,P_1)\stackrel{?}{\le}\frac{2}{\ln2}\delta.
\]

If true, (C) would pay the nonlinear projected `B_can` mixing gap by exactly the same local Boolean disagreement budget that already pays ordinary spectral mutual information.

### Result: (C) is REFUTED, rigorously, in four variables

Take the two truth tables (lexicographic binary input order, `+1`/`-1` values)

\[
h_0=(1,-1,-1,1,-1,1,1,1,-1,1,1,1,1,1,1,-1),
\]

\[
h_1=(-1,-1,-1,1,-1,1,1,1,-1,1,1,1,1,1,1,-1).
\]

They differ at exactly one of the sixteen inputs, so

\[
\delta=1/16.
\]

Equivalently, under the bit-mask convention used by the reproducer they are `0x8116` and `0x8117`. The second endpoint is bent: all sixteen normalized Walsh coefficients have magnitude `1/4`. The first is its one-point flip and has Walsh numerators of absolute value `2` on ten atoms and `6` on six atoms.

Direct exact zeta summation gives

\[
\begin{aligned}
B_{\rm can}(P_0)
&=\frac{57}{32}-\frac9{32}\log_2 3
 +\frac1{16}\log_2 5+\frac3{32}\log_2 7,\\
B_{\rm can}(P_1)&=2,\\
B_{\rm can}(M)
&=\frac{263}{128}-\frac{13}{128}\log_2 13
 +\frac5{16}\log_2 3-\frac{25}{64}\log_2 5
 +\frac{15}{64}\log_2 11.
\end{aligned}
\]

Hence

\[
\begin{aligned}
G_\zeta
={}&\frac{21}{128}-\frac{13}{128}\log_2 13
 +\frac{29}{64}\log_2 3-\frac{27}{64}\log_2 5\\
&+\frac{15}{64}\log_2 11-\frac3{64}\log_2 7\\
={}&0.20606883288162958355851656679368797\ldots,
\end{aligned}
\]

so

\[
\frac{G_\zeta}{\delta}
=3.2971013261060733369362650686990\ldots.
\tag{4.1}
\]

The refutation does not depend on floating point. Indeed `G_zeta>3/16=3 delta` is equivalent to

\[
3^{58}11^{30}>2^3 13^{13}5^{54}7^6,
\]

and the two integers are respectively

\[
82188930376475602525557232479634993583630695816964049371889
\]

and

\[
15824210126901038540925270581283257342875003814697265625000.
\]

Thus `G_zeta>3 delta`. Also `ln2>2/3` (for example, differentiate `ln x-2(x-1)/(x+1)` on `[1,2]`), hence `2/ln2<3`. Therefore (C) is rigorously refuted.

This is stronger than the preceding three-bit `G_zeta>JS` witness: even replacing ordinary JS by its sharp universal Boolean payment `(2/ln2)delta` is still insufficient.

## 5. Counterexample search and scale of the obstruction

The run also searched the direct-payment ratio

\[
R(h_0,h_1)=G_\zeta(P_0,P_1)/\Pr[h_0\ne h_1].
\]

Classification of the numerical statements below is **COMPUTATIONAL EVIDENCE ONLY**, except for the exact four-bit witness above.

- exhaustive all Boolean pairs on `m=1`: maximum observed `R=1.000000000000000`;
- exhaustive all Boolean pairs on `m=2`: maximum observed `R=2.084962500721156`;
- exhaustive all Boolean pairs on `m=3`: maximum observed `R=2.4253482448368153`;
- exhaustive all **one-point-flip** pairs on `m=4` (`524,288` unique pairs): maximum observed `R=3.2971013261060733`, attained by the exact witness above;
- heuristic one-point-flip search on `m=5`: found `R=3.531561334595537` (mask `0x80010116` versus its one-bit flip);
- heuristic one-point-flip search on `m=6`: found `R=3.92441184348624` (mask `0x91151f3e13fe5ee8` versus its one-bit flip); the flipped endpoint in this witness is bent, with all 64 Walsh numerators of absolute value `8`.

The last two values are lower bounds from a heuristic search, not maxima. They show that the four-bit obstruction is not an isolated numerical accident and that a raw constant near `2/ln2` is decisively the wrong target. They do **not** prove that the ratio is unbounded or that `4` is a valid/sharp constant.

## 6. A second proof step: local geometry at a flat spectrum

The exact identity suggests studying the zeta Jensen gap as a Dirichlet energy. This can be made precise around the uniform law.

Let `p_A=2^{-m}` on the Boolean lattice, let `d` have zero total mass, and define the relative perturbation

\[
r_A=d_A/p_A.
\]

Let

\[
(Kr)(A)=2^{-(m-|A|)}\sum_{B\supseteq A}r_B
\]

be upper-cone averaging under the uniform law. A direct second variation of `B_can` gives

\[
\boxed{
D^2 B_{\rm can,p}[d,d]
=-\frac1{\ln2}\,\mathbb E_{A\sim\mathrm{Unif}(2^{[m]})}
\bigl(r_A-(Kr)(A)\bigr)^2.
}
\tag{6.1}
\]

### Proof

Write `D_A=sum_{B superset A} d_B` and `U_A=sum_{B superset A}p_B`. In natural logarithms,

\[
B_e(p)=\sum_Ap_A\ln U_A-\sum_Ap_A\ln p_A.
\]

Differentiating twice in direction `d` yields

\[
D^2B_e[d,d]
=2\sum_A\frac{d_AD_A}{U_A}
 -\sum_Ap_A\frac{D_A^2}{U_A^2}
 -\sum_A\frac{d_A^2}{p_A}.
\]

At uniform `p`, `D_A/U_A=(Kr)(A)` and `d_A/p_A=r_A`, so the last display is

\[
-\mathbb E_A(r_A-Kr_A)^2.
\]

Divide by `ln2` to obtain (6.1). QED.

Therefore for a small relative perturbation `p(1+epsilon r)`, the midpoint Jensen gap has leading term

\[
\frac{\epsilon^2}{8\ln2}
\mathbb E(r-Kr)^2.
\tag{6.2}
\]

This identifies the local obstruction as a **nonreversible upper-cone Dirichlet energy**. It is the coding/point-process object that must be amortized, rather than ordinary JS alone.

For a one-point flip of a bent function on `m=2r` bits, the flat spectral endpoint has Walsh sign pattern `sigma_A in {+-1}` (the dual bent function). The relative perturbation is

\[
\rho_A=-\frac4{2^r}\left(\sigma_A-2^{-r}\right),
\]

and constants disappear under `I-K`. Consequently the leading normalized payment is

\[
\frac{G_\zeta}{\delta}
\sim \frac2{\ln2}\,
\mathbb E_A\bigl(\sigma_A-(K\sigma)(A)\bigr)^2.
\tag{6.3}
\]

This converts the search for hard one-point-flip Boolean pairs into a concrete extremal problem over **dual bent sign codes** under the upper-cone averaging operator. The standard quadratic bent family has this energy tending to `1`, recovering the earlier `2/ln2` asymptotic, while other bent sign arrangements can be substantially worse (as the exact four-bit and numerical six-bit witnesses demonstrate).

Equation (6.3) is an asymptotic/local statement, not a universal bound.

## 7. Interaction with the newest all-pattern Booleanity constraint

The fresh fleet01/B13 handoff proves all-pattern higher-derivative/Laplace constraints for every spectral cell and also proves that its first-moment hierarchy alone does not imply FEI for arbitrary set laws. That result explicitly asks for an additional phase/correlation consistency constraint.

The present identity supplies exactly such a phase-sensitive object: for restriction mixtures, the unpaid upper-zeta term is not an arbitrary entropy gap but the posterior divergence `D(w_A||v_A)` between exact-cell and upper-cone label information.

However the four-bit witness proves that **charging this divergence independently at each restriction step by the same local disagreement constant used for JS is too optimistic**. Any successful combination with the all-pattern Laplace constraints must amortize zeta-posterior divergence across atoms/levels/steps, rather than pay each atom independently.

## 8. What is proved, refuted, and open

**PROVED (universal, all finite mixtures):** the exact zeta-posterior identity (2.1), hence concavity of `B_can`.

**PROVED (universal local differential statement):** the flat-spectrum Hessian/Dirichlet identity (6.1).

**REFUTED (exact Boolean witness):** `G_zeta <= (2/ln2) delta`; in fact the explicit four-bit pair has `G_zeta>3 delta`.

**COMPUTATIONAL EVIDENCE ONLY:** the finite/heuristic ratios in section 5 and the suggestion that bent one-point flips can push the required direct-payment constant substantially upward.

**OPEN:** whether `G_zeta <= C delta` for any universal `C`; whether a weaker amortized zeta-posterior inequality closes a dimension-independent `B_can/I` bound; the full uniform-cube FEI conjecture.

## 9. Next attack

Do **not** try another atomwise constant replacement for (C) first. The next attack should exploit the exact posterior form and one of the following amortizations:

1. **Upper-chain telescoping:** choose a random upper chain from `A` to a sampled superset and decompose `D(w_A||v_A)` into increments whose weights are cone-mass drops; prove that each Boolean disagreement event is charged only O(1) times rather than once per ancestor.
2. **Laplace-credit coupling:** combine the all-pattern derivative-cell Laplace bound with the posterior divergence. Large `D(w_A||v_A)` forces a strong endpoint-label bias change between an exact cell and its upper cone; test whether the higher-derivative small-ball constraint forces enough expected escape mass to pay that change.
3. **Dual-bent extremal problem:** analyze `(I-K)` on bent sign codes. Either prove a uniform energy bound and derive the correct unavoidable local constant, or construct a sequence whose energy grows, decisively killing direct disagreement payment altogether.

The immediate preferred next move is (2): derive a scalar inequality linking a large binary posterior shift `w_A -> v_A` to the conditional escape/Laplace budget of the corresponding exact spectral cell, and stress-test it first on the exact `0x8116/0x8117` witness and the six-bit bent-flip witness.
