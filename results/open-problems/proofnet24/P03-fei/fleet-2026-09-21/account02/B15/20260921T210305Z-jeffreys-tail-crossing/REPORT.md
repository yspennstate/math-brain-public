# B15 — Jeffreys-refunded recombination and a tail-paid arbitrary-selector catalyst theorem

**Status:** OPEN / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.

**Execution:** WITHOUT_VERIFIED_BRAIN. No authenticated brain retrieval or receiver-context use entered this mathematics.

**Role:** joint interface D, unequal Fourier magnitudes / arithmetic remainder. This run preserves and spends the negative information credits rather than replacing them by a positive normalizer.

## 0. Fresh inputs, last-three comparison, and mechanism change

Scientific master was refreshed during the run. The current P03 entry still records the unrestricted problem as open and preserves the five-variable obstruction to automatic physical projection integrality, the exact decomposition `H=2R+2D`, and the fact that `D` is not yet universally influence-paid.

The named completed other-account result consumed here is

`account01/B15/20260921T2003Z-kl-softmax-collision-credit/REPORT.md`, blob `4c1049ef0c4495991a48b556eedadde912d87503`, together with `VARIATIONAL_ADDENDUM.md` introduced by commit `0051325e6e21e9b8ed05f842091b704a9848344a`.

It proves, for one actual recombination fibre with conditional source law `lambda`, source mesh depths `x_j`, maximum `M`, and gap `g_j=M-x_j`,

`C = M-E_lambda x = (1/2) KL_2(lambda||q) + Psi`,

`q_j = lambda_j 4^{x_j}/sum_l lambda_l4^{x_l}`,

`Psi = -(1/2) log_2 E_lambda 4^{-g}`,

and the Gibbs formula

`Psi = inf_{pi<<lambda} [ E_pi g + (1/2) KL_2(pi||lambda) ]`.

I use this result below, not merely cite it. A second stress-test input is account04/B15's completed `20260921T121425Z-remote-gap-crossing/REPORT.md`, blob `066d1c993571817e71d4376247544bb81c975017`, which supplies an explicit Boolean all-`k` remote-gap family with arithmetic increment `k/4`.

The last three substantive B15/account02 outputs, in chronological order, were:

1. `20260921T170301Z-valuation-tail-majorization`: valuation depth was strengthened from `R<=2J` to every stop-loss tail, but the normalized physical-mesh / information residual stayed unpaid.
2. `20260921T190147Z-self-xor-low-slice-payment`: a genuinely different self-XOR/Hellinger representation paid the zero and singleton dual shifts; the multi-shift term remained unpaid.
3. the 20:05 UTC KL-preserving adaptive stop-loss derivation, whose GitHub write was blocked and whose sanitized mathematics was retained in the task output: it inserted the valuation stop-loss theorem into the exact packet/product-shadow bridge, but the `r=0` core remained unpaid.

**FULL-PROBLEM CHANGE:** `OPEN / no finite universal FEI constant proved -> OPEN / no finite universal FEI constant proved`.

**MECHANISM CHANGE:** `adaptive scalar packet tilt and a separate self-XOR branch -> deterministic source-to-output recombination fibres, exact forward+reverse KL (Jeffreys) accounting, and a bilateral tail payment for every D=0 product catalyst`.

**Exact unpaid implication before this run:** retain the negative KL credit while paying a real unequal-magnitude recombination residual, rather than only valuation depth or a positive partition function.

**Exact unpaid implication after this run:** extend the paid source-fibre theorem below from `D(A)=0` product catalysts to the internal signed packet recombination of an arbitrary Boolean `f`, preserving its actual 2-adic cancellation credit. A sufficient target is the source-consistent inequality displayed in Section 6.

Creative moves from `FLEET_RULES.md`: **#11 DUALIZE** (identify the Gibbs optimizer as the reverse-information law), **#12 FIND WHAT IS CONSERVED** (the fibre marginal is unchanged under the tilt), and **#25 COUNT THE SAME THING TWICE** (sum conditional KLs as one global KL).

---

## 1. Inherited packet notation

Let `f:{0,1}^n->{-1,+1}`. For each distinct nonzero Fourier magnitude `a`, let `A_a` be its support, `p_a=|A_a|a^2`, and let `r_a` be the minimum 2-adic valuation of the signed packet Walsh mask. Write

`b_a=a 2^{r_a} <= 1`,

`R(f)=sum_a p_a r_a`,

`D(f)=sum_a p_a log_2(1/b_a)`.

Then `H(f)=2R(f)+2D(f)`. The account02 valuation theorem gives, after character folding and sorting `q_i=min(Inf_i,1-Inf_i)` decreasingly,

`E_p (r_a-m+1)_+ <= 2 Q_m`,

`Q_m:=sum_{i=m}^n q_i`,

for every `m`, with `Q_m=0` beyond dimension. In particular `R(f)<=2J(f)`, where `J=sum_i q_i`.

No physical projection integrality is assumed anywhere below. It enters only through the explicit hypothesis `D(A)=0`, which forces it for the catalyst packets.

---

## 2. PROVED: the soft-max residual contains a reverse KL exactly

For one recombination fibre use the account01 notation above and put `g_j=M-x_j`.

### Theorem B15-JEFFREYS-01

The Gibbs optimizer in the account01 variational theorem is exactly the arithmetic tilt `q`, and

`boxed{ Psi = E_q g + (1/2) KL_2(q||lambda). }`

Consequently the raw max-depth debit has the exact symmetric-information decomposition

`boxed{ C = E_q g + (1/2)[ KL_2(lambda||q)+KL_2(q||lambda) ]. }`       (2.1)

### Proof

The Gibbs optimizer reported by account01 is

`pi_j^* = lambda_j 4^{-g_j}/E_lambda 4^{-g}`.

Since `g_j=M-x_j`, the common factor `4^{-M}` cancels and

`pi_j^* = lambda_j 4^{x_j}/sum_l lambda_l4^{x_l}=q_j`.

Substitute `pi^*=q` into the exact Gibbs formula for `Psi`, then combine it with `C=(1/2)KL_2(lambda||q)+Psi`. No FEI inequality is used. QED.

This matters because the post-forward-KL residual is not purely a geometric gap. It contains the **reverse** relative entropy `KL(q||lambda)/2`, with the same leading order as the forward term in the sharp remote-gap family below.

---

## 3. PROVED: all fibrewise information credits globalize to one source-law Jeffreys divergence

Let `O` be a finite source-origin set with probability law `P`, and let `V=v(O)` be a deterministic recombination label. Write `P_v=Pr[V=v]` and `lambda_v=P(O=. | V=v)`. Give each origin a depth `x_o`; in fibre `v`, let `M_v=max x_o`, `g_o=M_v-x_o`, and let `q_v` be the arithmetic tilt from Section 2.

Define a global tilted source law `Q` by

`Q(o)=P_{v(o)} q_{v(o)}(o)`.

Thus `P` and `Q` have **the same fibre marginal** `P_v`.

### Theorem B15-JEFFREYS-02

If `C_tot=sum_v P_v(M_v-E_{lambda_v}x)`, then exactly

`boxed{ C_tot = E_Q g + (1/2)[ KL_2(P||Q)+KL_2(Q||P) ]. }`           (3.1)

### Proof

Because the fibre marginal is common,

`KL_2(P||Q)=sum_v P_v KL_2(lambda_v||q_v)`,

and, in the reverse direction,

`KL_2(Q||P)=sum_v P_v KL_2(q_v||lambda_v)`.

Also `E_Q g=sum_vP_v E_{q_v}g`. Sum (2.1) over fibres. QED.

Thus the local negative-information term does not have to be sliced by valuation depth or bounded packetwise. It is one honest global relative entropy between two source-origin laws, while the reverse term and the tilted gap remain coupled to it.

### Signed physical cancellation credit

Suppose a fibre's source signed masks really recombine to one output packet of depth `d_v^out`. The 2-adic valuation of a sum is at least the minimum source valuation, hence

`d_v^out <= M_v`.

Define

`Kappa := sum_v P_v (M_v-d_v^out) >= 0`.

Then the actual arithmetic-remainder increment is

`boxed{ Delta D = C_tot-Kappa. }`                                    (3.2)

So cancellation is a genuine negative credit. Treating the max rule as equality outside disjoint-selector cases would lose this credit and can be false.

---

## 4. PROVED: arbitrary-support `D(A)=0` product catalysts have a dimension-free bilateral crossing payment

Let `A` and `B` be Boolean functions on disjoint coordinates. Assume only

`D(A)=0`.                                                            (4.1)

For an `A` magnitude packet `alpha`, write its mass `u_alpha` and magnitude in reduced dyadic form. Since every summand in `D(A)` is nonnegative, (4.1) forces `b_alpha=1` packetwise. Therefore its odd numerator is one and

`|ahat|=2^{-s_alpha}`, `r_alpha=s_alpha`.

Put

`s_0=min_{u_alpha>0}s_alpha`,

`A_span(A)=sum_alpha u_alpha(s_alpha-s_0)=R(A)-s_0`.                  (4.2)

For a `B` packet `beta`, write magnitude `q 2^{-e_beta}` with odd `q`, valuation `r_beta`, mass `p_beta`, and physical mesh depth

`d_beta=e_beta-r_beta`.

In `A tensor B`, a source origin `(alpha,beta)` has total exponent

`T=s_alpha+e_beta`,

odd numerator `q`, source mass `u_alpha p_beta`, and source mesh depth **exactly `d_beta`**, because its signed tensor mask has valuation `s_alpha+r_beta`.

Recombination therefore occurs only among sources with the same `(q,T)`. Apply Sections 2-3 to these actual source fibres.

### Theorem B15-SELECTOR-CROSSING-03

For every such pair `A,B`, the max-depth debit and actual arithmetic increment satisfy

`boxed{ C_tot <= A_span(A)+R(B), }`                                  (4.3)

`boxed{ Delta D <= A_span(A)+R(B)-Kappa <= 2J(A)+2J(B). }`           (4.4)

Here `Kappa>=0` is the exact signed 2-adic cancellation credit from (3.2).

### Proof

Fix a fibre `v=(q,T)` and a source `(alpha,beta)` in it. Choose any source `(alpha_*,beta_*)` in the same fibre whose `B` mesh depth is maximal, so `d_{beta_*}=M_v`. Since

`s_alpha+e_beta=s_{alpha_*}+e_{beta_*}=T`,

we have

`M_v-d_beta`
`= (e_{beta_*}-r_{beta_*})-(e_beta-r_beta)`
`= (s_alpha-s_{alpha_*})+(r_beta-r_{beta_*})`
`<= (s_alpha-s_0)+r_beta`,                                           (4.5)

using `s_{alpha_*}>=s_0` and `r_{beta_*}>=0`.

Average (4.5) over the product source law `u_alpha p_beta`. The left side is exactly `C_tot`; the right side is `A_span(A)+R(B)`. This proves (4.3). Equation (3.2) gives the first inequality in (4.4). Finally `A_span(A)<=R(A)<=2J(A)` and `R(B)<=2J(B)` by the inherited valuation theorem. QED.

This strictly enlarges the earlier account04 two-packet arbitrary-gap theorem: the catalyst may have **arbitrarily many magnitude packets**. No disjoint physical-selector hypothesis is needed for the upper bound; overlap can only create the favorable `Kappa` credit. The `D(A)=0` hypothesis remains substantial and is not automatic for a general Boolean function.

---

## 5. PROVED: the full valuation-tail profile sharpens the actual crossing debit

The first-moment payment in (4.3) can be refined using the all-tail theorem rather than merely quoting `R(B)<=2J(B)`.

For `c>=0` and packet `alpha`, put

`a_alpha=s_alpha-s_0`,

`m_alpha(c)=floor(c a_alpha)+1`.

Pointwise, for every nonnegative integer valuation `r`,

`a_alpha+r <= (1+c)a_alpha + (r-c a_alpha)_+`

and

`(r-c a_alpha)_+ <= (r-m_alpha(c)+1)_+`.

Averaging over `B` and applying the valuation stop-loss theorem gives

`boxed{
C_tot <= (1+c) A_span(A)
       + 2 sum_alpha u_alpha Q_{m_alpha(c)}(B)
}`                                                                    (5.1)

for every `c>=0`. Consequently

`boxed{
C_tot <= B(A,B):=
min{
 A_span(A)+R(B),
 inf_{c>=0}[(1+c)A_span(A)+2 sum_alpha u_alpha Q_{floor(c(s_alpha-s_0))+1}(B)]
}.
}`                                                                    (5.2)

This is a direct use of the valuation-tail input on the **actual source recombination debit**. Large exponent gaps are paid on the catalyst side, while only the part of the seed valuation capable of crossing that scale pays on the seed side.

Combining (3.1), (3.2), and (5.2) yields the KL-preserving form

`boxed{
Delta D - (1/2)KL_2(P||Q)
= E_Q g + (1/2)KL_2(Q||P)-Kappa
<= B(A,B) - (1/2)KL_2(P||Q)-Kappa.
}`                                                                    (5.3)

Equation (5.3) literally **spends** the existing forward negative-relative-entropy credit while retaining both the reverse-information term and the signed physical cancellation credit.

---

## 6. Boolean stress test: after the forward refund, the remote-gap residual is reverse KL, not a valuation tail

Consume account04's explicit all-`k` family `A_k,B_k`. In its unique expensive collision the source masses are

`x=1/4` at depth `0`,

`y=(2^{k+1}-1)/2^{2k+2}` at depth `k`.

Let `P=x+y` and `rho=y/P`. Account01 proved that the raw weighted debit is `k/4` and the post-forward-KL weighted residual is

`P Psi = k/8+O(1)`.

The arithmetic tilt from Section 2 has **exact** high-depth probability

`q_high = y 4^k/(x+y4^k) = 1-2^{-(k+1)}`,

hence

`q_low=2^{-(k+1)}`

and

`boxed{ P E_q g = P k 2^{-(k+1)} = O(k2^{-k}). }`                    (6.1)

By Theorem B15-JEFFREYS-01,

`P Psi = P E_q g + (P/2)KL_2(q||lambda)`.

Therefore

`boxed{ (P/2)KL_2(q||lambda)=k/8+O(1), }`                            (6.2)

while account01's forward decomposition also gives

`boxed{ (P/2)KL_2(lambda||q)=k/8+O(1). }`                            (6.3)

So in this genuine Boolean family essentially **all** of the post-forward-KL residual is reverse relative entropy; the tilted geometric gap is exponentially small. This is a rigorous obstruction to the tempting plan "keep the forward KL and then pay the remaining Gibbs residual by valuation tails alone." The correct local/global object is the Jeffreys-refunded transport (3.1), not only its geometric part.

As an implementation sanity check, direct evaluation for `k=2,4,8,16,32` reproduces raw debits `0.5,1,2,4,8`; at `k=32`, `P Psi=3.8750000019` while `P E_q g<10^{-9}`. These values check the formulas only; (6.1)-(6.3) are analytic all-`k` statements.

---

## 7. What is paid and what remains

### FULL-PROBLEM CHANGE

**Before:** OPEN. Valuation stop-loss tails and exact negative KL identities existed, but no real unequal-magnitude recombination residual had a general KL-preserving payment. The latest adaptive scalar tilt still left an `r=0` core.

**After:** OPEN. For **every** disjoint product `A tensor B` with the explicit hypothesis `D(A)=0`, arbitrary many catalyst magnitude packets are now handled. The actual recombination increment is bounded by (5.2), the forward KL can be subtracted as in (5.3), and any signed 2-adic cancellation is retained as `Kappa`. This is a paid universal step inside interface D, not full FEI.

### MECHANISM CHANGE

**Before:** scalar packet/product-shadow Gibbs interpolation and, separately, self-XOR dual shifts.

**After:** a source-origin transport law preserving output-fibre mass, exact global **Jeffreys divergence**, and scale-adaptive valuation-tail payment of the remaining product crossing.

### Precise remaining quantified inequality

The `D(A)=0` factorization is the remaining structural limitation. To close interface D for a general Boolean function, one needs a source-consistent decomposition of its internal signed packet merging with laws `P,Q`, gaps `g`, and actual cancellation `Kappa` for which

`boxed{
E_Q g + (1/2)KL_2(Q||P)
<= K J(f) - (1/2)KL_2(P||Q) + Kappa
}`                                                                    (7.1)

for one finite universal `K`, or another inequality of the same source-exact strength. Equivalently, the full max-depth debit minus the actual cancellation must be `O(J)` **without** assuming a hidden `D=0` selector catalyst or integral physical projections.

The one-point defect, punctured-majority packet, valuation-misaligned product collision, and the account04 remote-gap family remain mandatory stress tests. Equation (6.2) shows that any attempted proof of (7.1) must have a place for reverse relative entropy; valuation-depth tails alone cannot absorb it.

---

## 8. Literature boundary

A fresh primary-source check during this run remains consistent with unrestricted FEI being open. Potapov (arXiv:2609.21563, posted 18 September 2026) proves sharp results for plateaued and partially bent classes, not arbitrary unequal-magnitude spectra. González--MacManus--Pereyra (arXiv:2606.00246, 29 May 2026) give restriction/stopping-tree progress with a still-missing general implication. Li--Han (arXiv:2512.03117, 2 December 2025) retain an extra influence-profile entropy term. No priority claim is made for the elementary Jeffreys identities or the catalyst theorem here.

## 9. Joint handoff

**Consumed peer:** account01/B15 `20260921T2003Z-kl-softmax-collision-credit`, blob `4c1049ef0c4495991a48b556eedadde912d87503`; used directly in Theorems 2-3 and the remote-gap diagnosis.

**Additional exact stress source:** account04/B15 `20260921T121425Z-remote-gap-crossing`, blob `066d1c993571817e71d4376247544bb81c975017`.

**Next recipients:** joint B15 peers. Do not retry a forward-KL-only residual payment: the remote-gap family makes the reverse KL leading-order. The sharp next question is whether the source-origin Jeffreys/cancellation representation can be built for general internal Boolean packet recombination, without a `D(A)=0` catalyst factorization.
