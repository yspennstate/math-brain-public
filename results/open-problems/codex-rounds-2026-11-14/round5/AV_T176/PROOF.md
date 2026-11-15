# Source audit of the dyadic Lean completion

The sources are OpenAI, *Optimal-order mixing of the Thorp shuffle*, September 26, 2026, and the Lean files saved in [sources/lean](sources/lean). This note checks the meaning and the scalar estimates of the Lean completion. It does not certify the entire manuscript or a Lean build.

## 1. Independent recheck of the previous conditional result

Round 4's tableau construction can be checked directly. For a diagram of size s with longest row or column L=s-u, orient it to have first row L. Reserve labels 1,...,u for the first u top-row cells, choose u lower labels from the remaining L labels, and fill the lower diagram and the remaining top row in row order. All lower columns lie among the first u columns, so every column inequality is satisfied. This gives at least binom(L,u) tableaux.

For 1≤u≤s/4 this is at least 3^u. For u>s/4 and L≥s/8, retain the top row and an initial lower ideal of floor(s/16) cells; the same construction gives at least 2^floor(s/16) tableaux, all extending to the full diagram. If L<s/8, every hook is shorter than s/4, giving degree at least (4/e)^s. The partition envelope exp(3sqrt(s)) makes the latter two classes negligible. In the first class, fix a tail cutoff K, let s tend to infinity in the finite u≤K part, then let K tend to infinity in the summable envelope 2exp(3sqrt(u))3^(-u). The earlier limit holds with this order of limits.

The previous Fourier exponent also checks: an eighth power of an operator bounded by A D^(-5/16) is bounded by A^8 D^(-5/2). Squaring, passing to Hilbert–Schmidt norm, and including Plancherel multiplicity leaves A^16 D^(-3). Replacing eight copies of a probability law by a trim at TV distance r costs at most 8r. If the original sign expectation vanishes, the normalized trim's sign expectation is at most r/(1-r) in absolute value. These reproduce round 4's conditional estimate.

## 2. The physical model and the quantity

[Model.lean](sources/lean/Model.lean) defines Position D as Fin D → Bool and State D as all permutations of that set. There are 2^D positions and (2^D)! states. For D≥1, Coins D has one Boolean for each of the 2^(D-1) suffixes u.

The definitions, together with step_cons in [MaskedResampling.lean](sources/lean/MaskedResampling.lean) and scatterPosition_eq_snoc in [WalshFlow.lean](sources/lean/WalshFlow.lean), give

\[
 \operatorname{step}_D(c)(b,u)=(u,b\mathbin{\mathrm{xor}}c(u)).
\]

Number binary strings in their usual order, with b the most significant bit. The inputs (0,u) and (1,u) are corresponding cards of the two halves. Their adjacent outputs (u,0) and (u,1) appear in the order decided by c(u). This is one physical shuffle in the question.

History D t is the product of t coin functions. The uniform counting law fairMass gives independent fair bits at every time and pair. The definition run multiplies the reversed list of steps: at t=2 it is step(c₁) step(c₀), so the earlier step acts first. One unit is a physical shuffle.

The definition distance is one half of the sum of absolute mass differences over all permutations, against the constant mass 1/(2^D)!. It concerns the full deck. The law from another initial deck is right-translated by its initial permutation. The theorem worst_start_eq in [Support.lean](sources/lean/Support.lean) changes variables by this translation and obtains exactly the same distance for every start.

The mixing time is the infimum of the natural times with distance≤1/4. Its defining set is separately proved nonempty for D≥1 in [MixingBounds.lean](sources/lean/MixingBounds.lean), using reachability and finite positive minorization. Thus an empty-infimum convention is not substituting for a mixing time. D=0 is immaterial to the limit.

## 3. The actual reciprocal-degree dependency

The recursively opened import graph of [Main.lean](sources/lean/Main.lean) contains 51 OAI modules and no cycle. Its only outside import is Mathlib. The [manifest](sources/MANIFEST.md) lists all direct imports. Four additional opened modules—FirstMain, FirstFourier, FirstMoment, ExceptionalShapes—are outside this closure.

FirstMain proves the paper's first-power reciprocal result and its D^(-5/16) Fourier estimate. Main instead uses the inverse-square quantities in [ReciprocalDegrees.lean](sources/lean/ReciprocalDegrees.lean):

\[
 C_2(s)=\sum_{\lambda\vdash s}(f^\lambda)^{-2},\qquad
 E_2(s)=\sum_{\substack{\lambda\vdash s\\
                       \lambda\text{ neither row nor column}}}(f^\lambda)^{-2}.
\]

The source names these reciprocalSum and exceptionalReciprocalSum. Its inverseDegree explicitly means 1/(degree²), not 1/degree.

Its summability calculation checks as follows. For defect u=s-max(λ₁,λ′₁), there are at most 2p(u)≤2^(u+1) shapes, encoding the oriented lower partition and the orientation. For 0<u≤s/4 their degrees are at least 3^u. Hence the inverse-square slice is at most 2(2/9)^u, a summable bound. At each fixed positive u the binomial lower bound tends to infinity, so the slice tends to zero.

The other shapes have degree at least 2^floor(s/16). The partition-count bound used by the source is

\[
 p(s)\le(s+1)^{2\lfloor\sqrt{s}\rfloor}.
\]

To see this, record the first r=floor(sqrt(s)) row lengths and first r column lengths, padding with zeros. Every box lies in those rows or columns: otherwise the diagram would contain an (r+1)-square. Those 2r numbers in {0,...,s} determine the shape. Therefore the inverse-square bulk sum is at most

\[
 (s+1)^{2\lfloor\sqrt{s}\rfloor}4^{-\lfloor s/16\rfloor}\longrightarrow0,
\]

since its logarithm is O(sqrt(s)log(s+1))-(log 4)s/16+O(1). Dominated convergence in the small slices and this bulk bound give E₂(s)→0. The row and column contribute at most two, so C₂(s)≤2+E₂(s) and eventually C₂(s)≤3. This explains the constant three in EightBlocks without a numerical uniform bound for the paper's C₁.

## 4. The inverse-square Fourier completion

The orbit/projector input in [CosetBounds.lean](sources/lean/CosetBounds.lean) gives, for an irreducible representation of dimension D and a probability ν with all eight block caps at most B times uniform mass,

\[
 \|\widehat\nu v\|^2\le {8BS\over D}\|v\|^2,\qquad
 S=\sum_{f^8\le D}f^2.
\]

Here f runs over irreducible block-group degrees. Each tensor constituent for the eight commuting block groups has product degree at most D; at least one factor satisfies f^8≤D. The coefficient bound and orthogonal splitting supply the eight. The calculation below is conditional on that orbit/projector input.

For every selected f, f⁴≤sqrt(D), so f²≤sqrt(D)f^(-2). Summing gives S≤sqrt(D)C₂. The independent Cauchy–Schwarz calculation in low_degree_sq is

\[
 S^2\le\left(\sum f^{-2}\right)\left(\sum f^6\right)
       \le C_2(DC_2)=DC_2^2.
\]

Put R=8BS/D. Iteration gives ||ν̂⁸v||²≤R⁸||v||². Sum over an orthonormal basis, then include the Plancherel multiplicity:

\[
 D\|\widehat\nu^{\,8}\|_{\rm HS}^2
 \le D^2R^8\le(8BC_2)^8D^{-2}.
\]

A second exponent check starts with ||ν̂||≤sqrt(8BC₂)D^(-1/4). Eight powers, a square and two factors D give exponent -4+2=-2. No normality is assumed. Thus this alternative contraction has exactly the inverse-square summability it needs; it need not use the paper's stronger -5/16 contraction.

[FourierBounds.lean](sources/lean/FourierBounds.lean) uses the unnormalized squared Hilbert–Schmidt norm. Cauchy–Schwarz gives (Σ|f|)²≤|G|Σ|f|², and Parseval changes the latter into ΣD||f̂||². There is no missing group-size factor.

## 5. Trimming, sign, marginals and clock

[Trimming.lean](sources/lean/Trimming.lean) retains one common set whose eight coset masses are each at most twice uniform mass. If the discarded probability is r≤1/2, the normalized retained law ν has all eight caps B=4 and TV(μ,ν)=r.

The original positive-time shuffle law has zero sign expectation: toggling one coin reverses parity and preserves its probability. A character bounded by one changes expectation by at most 2r, so |ν̂(sign)|≤2r. Centering kills the trivial representation. The source bounds both exceptional shapes by the sign bound and counts at most two; this harmless overcount gives

\[
 {\rm TV}(\mu^{*8},U)
 \le8r+\frac12\sqrt{2(2r)^{16}+(32C_2)^8E_2(2^D)}. \tag{1}
\]

This is the estimate in trimmed_eight_tv, [BlockLaws.lean](sources/lean/BlockLaws.lean). For block size 2^j and deck dimension D=j+3, eventual C₂(2^j)≤3 replaces 32C₂ by 96. The identity law_realPower identifies μ equal to the law at 200D and eight convolutions with exactly 1600D physical steps. Main removes the cofinal dimension shift j+3. No sweep-to-step factor is lost.

[BlockFibers.lean](sources/lean/BlockFibers.lean) bounds the discarded mass using a fixed-input marginal estimate from [MarginalBounds.lean](sources/lean/MarginalBounds.lean), stronger than the paper's averaged-input Proposition 4.2. For N=8·2^j, k=7·2^j, m=2^j, that estimate is

\[
 {k\over2}\sqrt{N\{2^{-8(j+3)}+32(9/10)^m\}}.
\]

The squared prefactor is k²N/4=98·2^(3j). The first term obeys 2^(3j)2^(-8(j+3))≤(1/32)^j, and 98·32=3136. A loose common upper bound is therefore

\[
 {\tt marginalRate}(j)
 =\sqrt{3136\{(1/32)^j+2^{3j}(9/10)^{2^j}\}}\longrightarrow0.
\]

Each of the eight fixed block complements has this bound. The discarded mass is at most twice the sum of those eight errors, hence at most 16·marginalRate(j). Substitution in (1) gives the displayed fullRate tending to zero, conditional on the conditional-flow and representation inputs.

## 6. Spot check: preparing a deterministic free set

The fixed-list dependency raises a concrete concern: a deterministic free set might occupy only one half. The lemma pair_both_half_balance in [FreshCoins.lean](sources/lean/FreshCoins.lean) supplies the preparation used by expectedNoise_dimension in [MarginalEnergy.lean](sources/lean/MarginalEnergy.lean).

Fix any set B of m free positions before one shuffle, and let X_h be the number in output half h. Each original matching pair contributes 0, a fair Bernoulli variable, or 1, according as it has 0, 1 or 2 free points. Distinct pairs use independent coins. After rotation these halves are distinguished by the last coordinate.

Consider W_h=(5/4)^m(4/5)^(4X_h). The expected local factors are exactly

| Free points in pair | Expected factor | Upper bound |
| --- | --- | --- |
| 0 | 1 | 1 |
| 1 | (5/8)(1+256/625)=881/1000 | 9/10 |
| 2 | (25/16)(256/625)=16/25 | (9/10)² |

Multiplication gives E W_h≤(9/10)^m. On 4X_h<m, W_h=(5/4)^(m-4X_h)>1. Markov's inequality and a union bound give the exact source estimate

\[
 \Pr(4X_0<m\ \text{or}\ 4X_1<m)\le2(9/10)^m. \tag{2}
\]

No random input set is needed.

An independent tail derivation checks the constants. If a pairs are doubly free and b singly free, then m=2a+b and X_h=a+Bin(b,1/2). For b=0 the bad event is empty. For b>0 the centered Bernoulli log moment-generating function has second derivative at most 1/4, so it is at most θ²/8. Exponential Markov and optimization give

\[
\begin{split}
 \Pr(X_h<m/4)
 &\le\inf_{\theta>0}\exp(-\theta m/4+b\theta^2/8)\\
 &=\exp(-m^2/(8b))
 \le\exp(-m/8)<(9/10)^m
\end{split}
\]

when m>0. For the last inequality, exp(1/8)>1+1/8=9/8>10/9. This proves the same half bound independently of the rational generating-function factors.

On the good event X_h≥m/4 and m≥N/8, each half density is at least (m/4)/(N/2)≥1/16. During the following D-1 layers the prepared halves exchange no positions; their markers rotate with the frame and their coin arrays are disjoint. The half-factorization in EnergyDecay uses opposite halves, rather than asserting independence of flow and availability within a half.

On the bad event the centered flow has squared norm at most one. Arbitrary correlation of the energy with that event therefore costs at most (2). This explains the source noise estimate b_s≤(15/16)E_s+2(9/10)^m for s≥D. Its geometric recurrence has additive term [2(9/10)^m]/(1/16)=32(9/10)^m, as required in the fixed-list marginal bound.

Boundary checks: m=0 makes the bad event empty; all-doubly-free pairs give deterministic equal halves; all-singly-free pairs give the binomial case. For m=N both halves are full. Equality 4X_h=m is correctly retained by the strict bad-event inequality. The initial preparation plus D-1 lookback layers accounts for s≥D. Small dimensions excluded by N≥16 are harmless in the asymptotic shift.

## 7. Limits

The checked model and scalar completion concern dyadic full-permutation mixing in physical steps. No defect was found in these links. The conditional-resampling identities, full half-history reindexing, and Specht classification/projector proofs have source bodies but have not all been independently proved here.

A lexical scan of 55 solution modules found no literal sorry, admit, axiom or unsafe. Comparator challenge placeholders are separate. No local compiler, kernel axiom report, Comparator check or dependency-version build ran. There is no non-dyadic state family or all-even reduction in this theorem; this audit does not certify the complete preprint or settle the general row.
