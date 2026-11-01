# B15 — radius-one tensor saturation and a Boolean counterexample to the softmax/radius-one dichotomy

**Run:** `20260921T2302Z-fleet02-B15-r11`  
**Directive:** `FEI-PROOF-EXECUTION-20260921T230620Z`  
**Campaign / assignment:** B — apply exact relative-entropy credits to the common residual and prove the influence payment, not a renamed remainder.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Outcome classification:** **CANDIDATE_REFUTED**.  
**Full unrestricted FEI:** **OPEN / NOT PROVED**.

## 0. Before / after

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`. No finite universal FEI constant is proved here.

**MECHANISM CHANGE:** the preceding durable B15 reports moved through valuation-tail majorization, self-XOR low-slice payment, and Jeffreys-refunded recombination. The later owner execution reset reassigns B15 to the common Shannon/code campaign. The newest B lead artifact available at the scientific snapshot is still pre-reset interface-C work, so the reset explicitly permits reconstruction of the smallest candidate from accessible dependencies. I therefore attack the strongest completed, exact-KL-compatible B candidate currently available:

\[
\mathcal W(f)\le \frac34J(f)\quad\text{or}\quad T_2(f)\le4J(f).
\tag{0.1}
\]

The first branch is fleet03/B15's real-restriction softmax current; the second is fleet04/B15's collision-KL-refunded radius-one Shannon exposure. Fleet04/B17 proved that (0.1), if true for every Boolean function, would imply full FEI with constant `6+2/ln2`, and supplied a 16-variable Boolean example that kills the first branch but satisfies the second.

This run proves two structural product laws and then gives a genuine 48-variable Boolean function that kills **both** branches of (0.1).

## 1. Completed peer inputs actually used

1. **fleet01/B15**, `20260921T222602Z-zero-valuation-height-tilt-obstruction/REPORT.md`, REPORT blob `f85d23ec06d69416084fe742c8fc710f74910a15`. Its one-point family proves that forward, reverse, and Jeffreys divergences of the global physical-height tilt are not separately `O(J)`; the cancellation `log Z - KL_forward` must be retained. This rules out repairing the candidate below by charging a separately positive global KL term.

2. **fleet04/B15**, `20260921T211141Z-refunded-radius1-transfer/REPORT.md`, REPORT blob `ec1224f39f7ac67703d1a5b22235561f167f0a78`. After spending the self-XOR fibre KL credit exactly, it defines
\[
T_2(f)=\sum_s p_s\log_2(1/p_s)
\left(1-p_s-\sum_i p_{s\triangle e_i}\right),
\qquad p_s=\widehat f(s)^2,
\tag{1.1}
\]
and proposes the sufficient open bound `T_2<=4J`.

3. **fleet04/B17**, `20260921T214628Z-softmax-counterexample-dichotomy/REPORT.md`, REPORT blob `d0f27070c7942f4d6d79db3eeeba40a95b8d7c2c`. It refutes the standalone conjecture `mathcal W<=3J/4` and replaces it by the dichotomy (0.1), proving that the dichotomy would imply FEI.

4. **fleet03/B15**, `20260921T211127Z-real-restriction-softmax-credit/REPORT.md`. It defines
\[
W_i(f)=\frac12\sum_{\{s,s\triangle e_i\}}
\min(p_s,p_{s\triangle e_i})
\log_2\frac{p_s+p_{s\triangle e_i}}
{2\min(p_s,p_{s\triangle e_i})},
\qquad \mathcal W=\sum_iW_i.
\tag{1.2}
\]
The packet-orientation information credit has already been spent before (1.2), so this is a genuine post-credit residual rather than raw entropy.

The calculations below retain those negative-credit reductions. They do not assume integral physical projections or dyadic-lattice closure.

## 2. PROVED — tensor saturation of the radius-one refunded residual

For a probability law `p` on the Fourier cube define the closed radius-one spectral mass
\[
L_f(s)=p_s+\sum_i p_{s\triangle e_i}.
\tag{2.1}
\]
Then (1.1) is exactly
\[
T_2(f)=\sum_s p_s\log_2(1/p_s)\,[1-L_f(s)].
\tag{2.2}
\]

Let `f` be a non-character Boolean function and set
\[
p_*=\max_s p_s<1.
\]
For `t>=1`, let `F_t=f^{\otimes t}` on `t` disjoint coordinate blocks. Its spectral law is the product law.

### Theorem 2.1 — radius-one loss is exponentially suppressed by tensoring

For `x=(s_1,...,s_t)`,
\[
\boxed{
L_{F_t}(x)
=
\sum_{r=1}^t
L_f(s_r)\prod_{k\ne r}p_{s_k}
-(t-1)\prod_{k=1}^t p_{s_k}.
}
\tag{2.3}
\]
Consequently
\[
0\le L_{F_t}(x)\le t\,p_*^{\,t-1}
\tag{2.4}
\]
and
\[
\boxed{
0\le H(F_t)-T_2(F_t)
\le t^2p_*^{\,t-1}H(f).
}
\tag{2.5}
\]

#### Proof

In (2.3), the `r`-th summand contributes the central product atom once plus all Fourier neighbours obtained by flipping a coordinate in block `r`. The central atom is therefore counted `t` times, so subtracting `t-1` copies leaves exactly the closed radius-one mass of `x`. This proves (2.3).

Each `L_f(s_r)<=1` and every product over the other `t-1` blocks is at most `p_*^(t-1)`. Dropping the nonnegative subtraction gives (2.4). Finally,
\[
H(F_t)-T_2(F_t)
=
\sum_x p_x\log_2(1/p_x)L_{F_t}(x)
\le
t p_*^{t-1}H(F_t).
\]
Entropy tensorizes, `H(F_t)=tH(f)`, giving (2.5). QED.

Folded influence also tensorizes for disjoint Boolean products:
\[
J(F_t)=tJ(f).
\tag{2.6}
\]
Therefore
\[
\boxed{
\frac{T_2(F_t)}{J(F_t)}
\longrightarrow
\frac{H(f)}{J(f)}.
}
\tag{2.7}
\]
Since `T_2(f)<=H(f)` pointwise, (2.7) implies the exact optimal-constant identity
\[
\boxed{
\sup_{\text{Boolean }f,\ J(f)>0}\frac{T_2(f)}{J(f)}
=
\sup_{\text{Boolean }f,\ J(f)>0}\frac{H(f)}{J(f)},
}
\tag{2.8}
\]
with equality understood in the extended nonnegative reals.

### Consequence

The inequality `T_2<=CJ` is **not a strictly easier universal constant problem than FEI**: its best possible universal constant is exactly the FEI `H/J` constant. The fibre KL refund is exact and useful locally, but the radius-one exposure alone loses asymptotically all of its radius-one discount under tensor powers.

More generally, if a proposed additional refund `Gamma>=0` satisfies
\[
\Gamma(f^{\otimes t})=o(t)
\quad\text{for every fixed Boolean }f,
\tag{2.9}
\]
then
\[
\frac{T_2(f^{\otimes t})-\Gamma(f^{\otimes t})}{J(f^{\otimes t})}
\to\frac{H(f)}{J(f)}.
\tag{2.10}
\]
Thus any information credit intended to lower the universal constant of the `T_2` bridge must retain **linear tensor-scale mass** on hard base functions. A local credit that disappears under repeated products cannot close the gap.

This is the tensor analogue of fleet01/B15's warning that large positive and negative information terms may cancel and must not be estimated separately.

## 3. PROVED — the real-restriction softmax current is additive

Let `f` and `g` use disjoint coordinates. For a coordinate belonging to `f`, every Fourier edge of `f\otimes g` has endpoint probabilities
\[
q_t p_s,\qquad q_t p_{s\triangle e_i},
\]
where `q` is the spectral law of `g`. The edge functional in (1.2) is positively 1-homogeneous: multiplying both endpoint masses by `q_t` multiplies its value by `q_t` and leaves the logarithmic ratio unchanged. Summing over `t` gives `sum_t q_t=1`. The same argument holds for coordinates of `g`.

Hence
\[
\boxed{
\mathcal W(f\otimes g)=\mathcal W(f)+\mathcal W(g).
}
\tag{3.1}
\]
Together with `J(f\otimes g)=J(f)+J(g)`, the ratio `mathcal W/J` is unchanged by tensor powers.

This makes the fleet04/B17 dichotomy particularly vulnerable: if one Boolean base has both `mathcal W/J>3/4` and `H/J>4`, tensor powers preserve the first failure while Theorem 2.1 forces `T_2/J` toward the second ratio.

The next section supplies such a base in a form whose tensorized version can be evaluated exactly without enumerating `2^48` Fourier atoms.

## 4. Explicit genuine Boolean counterexample

On four bits define
\[
g(x)=
\begin{cases}
+1,& |x|\le1,\\
-1,& |x|\ge2,
\end{cases}
\qquad
r(x)=\frac{1-g(x)}2=\mathbf 1_{\{|x|\ge2\}}.
\tag{4.1}
\]
For a local Fourier frequency of Hamming weight `k=0,1,2,3,4`,
\[
\widehat r(k)
=
\frac1{16}\left(11,-3,-1,1,3\right)_k.
\tag{4.2}
\]
Indeed, for `k>0` the complement `{|x|<=1}` has Walsh sum `1+(4-2k)=5-2k`, so `rhat(k)=-(5-2k)/16`, while `rhat(0)=11/16`.

Put
\[
\mu=\mathbb E r=\frac{11}{16}.
\tag{4.3}
\]
For `m` disjoint four-bit blocks define the Boolean block-OR
\[
\boxed{
F_m(x^{(1)},\ldots,x^{(m)})
=
1-2\prod_{b=1}^m r(x^{(b)}).
}
\tag{4.4}
\]
Thus `F_m=+1` unless **every** local block has Hamming weight at least two.

For every nonzero global Fourier frequency,
\[
\widehat F_m(s_1,\ldots,s_m)
=
-2\prod_{b=1}^m\widehat r(s_b),
\tag{4.5}
\]
while
\[
\widehat F_m(0)=1-2\mu^m.
\tag{4.6}
\]

### Exact folded influence

Let `rho_s=rhat(s)^2`. In one local coordinate,
\[
\sum_{s:\,s_i=1}\rho_s=\frac3{32}.
\tag{4.7}
\]
Therefore every physical coordinate of `F_m` has influence
\[
\operatorname{Inf}_i(F_m)
=
4\mu^{m-1}\frac3{32}
=
\frac38\mu^{m-1}.
\tag{4.8}
\]
For `m=12` this is below `1/2`, so no extra folding occurs and
\[
\boxed{
J(F_{12})
=
\frac{3m}{2}\mu^{m-1}\Big|_{m=12}
=
\frac{2567805035499}{8796093022208}.
}
\tag{4.9}
\]

## 5. Exact 48-variable evaluation and strict failure of both dichotomy branches

The committed checker does **not** enumerate `2^48` states. It uses the 16-state local Fourier law (4.2), exact rational product identities, and rigorous rational intervals for every logarithm.

The required local moments are
\[
A_0=\sum_s\rho_s^2=\frac{941}{4096},
\qquad
B=\sum_{\{s,s\triangle e_i\}}\rho_s\rho_{s\triangle e_i}
=\frac{141}{8192},
\tag{5.1}
\]
together with the corresponding entropy-weighted moments
\[
A_1=\sum_s\rho_s^2\log_2(1/\rho_s),
\qquad
B_1=\sum_{\{s,s\triangle e_i\}}
\rho_s\rho_{s\triangle e_i}
\log_2\frac1{\rho_s\rho_{s\triangle e_i}}.
\tag{5.2}
\]

The only correction to the raw product spectrum is at the global zero frequency. The raw product square there is
\[
p^{\rm raw}_0=4\mu^{2m},
\tag{5.3}
\]
whereas the actual Boolean zero atom is
\[
p_0=(1-2\mu^m)^2.
\tag{5.4}
\]
For one singleton frequency,
\[
p_e=\frac9{64}\mu^{2m-2}.
\tag{5.5}
\]

The checker applies this single exact correction to entropy, the softmax zero-singleton edge, and the radius-one diagonal/edge moment. All logarithms are enclosed using
\[
\ln y
=
2\sum_{j\ge0}\frac{z^{2j+1}}{2j+1},
\qquad
z=\frac{y-1}{y+1},
\tag{5.6}
\]
with an explicit positive geometric tail bound after exact power-of-two normalization.

For `m=12`, hence `n=48`, it certifies:
\[
\frac{H(F_{12})}{J(F_{12})}
=
4.3489407923190538523\ldots,
\tag{5.7}
\]
\[
\boxed{
\frac{\mathcal W(F_{12})}{J(F_{12})}
>
0.76118423918207877137
>
\frac34,
}
\tag{5.8}
\]
and
\[
\boxed{
\frac{T_2(F_{12})}{J(F_{12})}
>
4.05924537070733980774
>
4.
}
\tag{5.9}
\]

The certified strict margins are
\[
\frac{\mathcal W}{J}-\frac34
>
0.01118423918207877137,
\tag{5.10}
\]
\[
\frac{T_2}{J}-4
>
0.05924537070733980774.
\tag{5.11}
\]

Therefore the fleet04/B17 universal dichotomy (0.1) is **false**.

This is an actual Boolean counterexample, not a relaxed probability law. It does **not** refute FEI: the same function has `H/J≈4.34894`.

## 6. Why the counterexample was structurally expected

The local gate already has a softmax ratio above `3/4` after enough block-OR amplification, so (3.1) protects the softmax failure under disjoint products. Meanwhile (2.7) says the radius-one exposure loses its local discount under tensoring and converges to the full entropy ratio.

The combined lesson is stronger than either numerical violation:

- an either/or theorem built from one **additive** post-credit current and one **radius-one** post-credit entropy exposure is not automatically composition-stable;
- any repaired Campaign-B bridge must keep a negative information term whose product law itself survives at order `t`, or it will asymptotically collapse back to the full FEI ratio.

This is exactly where fleet01/B15's exponential KL-cancellation warning matters: the repair cannot be "bound one more KL term positively." The compensating term must remain signed in the common residual.

## 7. Checker and scope

`check_radius1_counterexample.py` is standard-library only. It:

- uses the exact local Fourier law (4.2);
- verifies `mu=11/16`, the exact local influence `3/32`, `A_0=941/4096`, and `B=141/8192`;
- computes the `m=12` entropy, softmax current, and `T_2` from exact rational product moments;
- encloses every logarithm by a rational atanh-series interval with an explicit tail;
- asserts the two strict inequalities (5.8) and (5.9).

Checker SHA-256: `3fa55b57faf78a26c373136b7fdbbaeace41df5c55fce083ecc7f6799fa97964`.

Recorded output SHA-256: `1b74a78246b730b2d45c9cf164b0795fee835d34a795c49d92ffdc8920ec8061`.

The 48-variable certificate establishes only the stated counterexample. The tensor-saturation theorem and softmax additivity theorem are analytic and all-dimensional.

## 8. Exact candidate status after this run

**CANDIDATE_REFUTED:**
\[
\boxed{
\mathcal W(f)\le\frac34J(f)\quad\text{or}\quad T_2(f)\le4J(f)
}
\]
fails for the explicit Boolean `F_12`.

**Also refuted as a universal inequality:**
\[
\boxed{T_2(f)\le4J(f)}.
\]
This does not refute fleet04/B15's exact KL-refunded identities; it refutes only the proposed constant-four payment for their sufficient radius-one exposure.

**Proved structural obstruction:** the optimal universal `T_2/J` constant equals the optimal universal `H/J` constant by tensor saturation.

**Full FEI:** OPEN.

## 9. New quantified missing implication

A viable B-campaign residual must now include a signed information credit that remains macroscopically present under tensor products. One source-exact sufficient target has the form
\[
\boxed{
T_2(f)-\Gamma_B(f)\le KJ(f)
}
\tag{9.1}
\]
for every Boolean `f`, where `Gamma_B>=0` is not introduced as a separately payable positive divergence but is retained as an exact negative term in the Shannon/code identity.

Theorem 2.1 imposes the necessary tensor test:
\[
\boxed{
\text{if }\Gamma_B(f^{\otimes t})=o(t)
\text{ for a hard base }f,\text{ then (9.1) cannot improve the }H/J\text{ constant on that base.}
}
\tag{9.2}
\]

So the next B15 attack should derive the campaign lead's post-reset common Shannon residual and identify its exact **linear-under-products negative relative-entropy term**, rather than proposing another scalar radius-one exposure, additive softmax threshold, or separately positive KL budget.

No novelty or publication-priority claim is made for these calculations. Full unrestricted FEI remains OPEN.
