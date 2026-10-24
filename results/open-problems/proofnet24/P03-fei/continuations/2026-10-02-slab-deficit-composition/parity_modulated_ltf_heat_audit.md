# Independent audit: parity modulation of a unate strong-FEI class

2 October 2026. This independently checks the root's stated parity-output
extension, including its generic unate lemma. Once it was available I read
the entire [parity-modulated proof](parity_modulated_ltf_proof.md), including
its more general high-influence hypothesis and read-once formula corollary.
I also read the complete
[strengthened LTF proof](../2026-10-02-strong-LTF-composition/strong_ltf_and_balanced_composition_proof.md),
which supplies the strong bound used in the LTF corollary. Earlier
completed proofs were not edited.

**Verdict: analytic PASS.** On the uniform cube, if a unate Boolean g
satisfies H(g)≤C[I(g)−Var(g)], then every h=χ_T g satisfies ordinary FEI
H(h)≤C I(h), with the same constant and with no disjointness assumption
between the parity coordinates and the coordinates used by g. Applying
the internally proved strong all-LTF theorem gives the asserted
parity-modulated LTF subclass. This does not assert strong FEI for every
unate function or unrestricted Boolean FEI.

## 1. Pairwise unate influence bound

Coordinate sign changes make a unate g increasing in every coordinate
while preserving all physical influences. Fix distinct i,j and condition
on all other coordinates. The resulting two-variable monotone Boolean
function is one of six possibilities: two constants, the two dictators,
AND, or OR, in sign encoding. Its influence pair is respectively
(0,0), (1,0), (0,1), or (1/2,1/2). In every case the sum is at most one.
Averaging the conditional influences therefore proves

I_i(g)+I_j(g)≤1.

This is not an assumption about the conditional distributions: under
the uniform cube the remaining pair still consists of independent
uniform signs. It follows that at most one influence is strictly greater
than 1/2. Equality at 1/2 causes no loss term.

## 2. Degree-one weight pays for all possible parity losses

For a coordinatewise increasing Boolean function,

ghat({i})=E[(g(x_i=+1)−g(x_i=−1))/2]=I_i(g).

For an arbitrary unate coordinate the coefficient is ±I_i(g). Thus
Parseval gives Var(g)≥Σ_i I_i(g)². By Section 1 there is at most one
positive term in Σ_i(2I_i(g)−1)_+. If its influence is a>1/2, then
2a−1≤a² because (a−1)²≥0. If no such influence exists the sum is zero.
Therefore

Σ_i(2I_i(g)−1)_+≤Var(g).

The exact identity min(a,1−a)=a−(2a−1)_+ then yields

Σ_i min(I_i(g),1−I_i(g))≥I(g)−Var(g).

The one-coordinate case satisfies the same argument, with the pairwise
step vacuous. Constants have both sides zero. The right side is
nonnegative by Poincaré or its Fourier expression
Σ_{S≠∅}(|S|−1)ghat(S)².

## 3. Exact character modulation

For T⊆[n], χ_T(x)=Π_{i∈T}x_i. The character identity
χ_Tχ_S=χ_(S symmetric-difference T) gives

hhat(S)=ghat(S symmetric-difference T).

This is a permutation of the entire squared Fourier spectrum, including
the empty coefficient, so H(h)=H(g) exactly. No positivity or statistical
independence is needed.

If i is outside T, flipping input i leaves χ_T unchanged, and h changes
exactly when g changes. If i is in T, it reverses χ_T, and h changes
exactly when g does not change. Consequently

I_i(h)=I_i(g) for i outside T,
I_i(h)=1−I_i(g) for i in T.

Adding these exact coordinate identities proves

I(h)≥Σ_i min(I_i(g),1−I_i(g))≥I(g)−Var(g).

Combining with the assumed strong bound gives H(h)=H(g)≤C I(h).
T may contain coordinates irrelevant to g; then those coordinates simply
contribute influence one to h. An additional output sign preserves all
quantities. Input-coordinate sign changes also preserve the conclusion.

## 4. Strong LTF input independently read

The strong-LTF companion uses the already proved largest-weight split
bound ΔH≤C_*α. I checked its elementary near-dictator supplement:
for an increasing split f=A+zB, B is a 0–1 indicator with EB=α,
|EA|≤1−α, and nonempty pair mass at most 1−α². If α>1/2, the empty
pair entropy is bounded by 2(1−α), and the nonempty contribution by
2(1−α), giving ΔH≤8(1−α). This produces

ΔH≤C_+ α(1−α), C_+=2max{C_*,8}.

Its exact variance split is
Var(f)−[Var(f⁺)+Var(f⁻)]/2=(EB)²=α²,
while the influence split increment is α. Therefore I−Var has exactly
the budget α(1−α) required by the restriction induction. Restrictions
are still LTFs; the zero-variable, constant and irrelevant-coordinate
cases are valid. No additional input-biased theorem is assumed.

Thus the companion's all-LTF strong bound legitimately supplies the
hypothesis of the generic result, since every LTF is unate after input
sign normalization. The parity-modulated conclusion has no regularity,
bias, threshold-spacing, degree, or fan-in condition. Its degree may grow
with dimension, but it is not a theorem for arbitrary polynomial threshold
functions or arbitrary output Boolean modulations.

## 5. Source and research-priority distinctions

The monotone influence/degree-one identity is established standard
Fourier analysis, not a new ingredient. I independently verified
Proposition 2.21 and Exercise 2.5(a) of Ryan O'Donnell's May 2021 edition
of [Analysis of Boolean Functions](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf).
They state the monotone identity and the absolute-value unate extension.
The same source's Fact 1.6 states the character symmetric-difference
identity used in Section 3. Parseval and the physical influence convention
are standard and were derived again here to check the normalization.

The pairwise influence bound and its variance-loss consequence have
short complete proofs above. I found no need to assign them a historical
priority claim. A limited targeted primary search for parity-modulated
LTF FEI and the corresponding unate extension did not identify a matching
theorem, but that is not exhaustive novelty verification. The substantial
dependency is the strong all-LTF estimate; all its external analytic
inputs and priority caveats remain those documented in the companion.

## 6. Necessary scope boundaries

The unate hypothesis is essential to this particular generic implication.
For the two-bit parity g=x_1x_2, both influences equal one, so the sum of
coordinatewise minima is zero whereas I(g)−Var(g)=1. Multiplying by
χ_{1,2} makes h constant. Hence one cannot replace the generic unate
lemma by an assertion about all Boolean functions using this influence
comparison.

Neither the result nor the standard spectral permutation says that
ordinary FEI is closed under parity multiplication for every class.
The strong I−Var hypothesis is what pays for any loss of influence.
Nor is there an implicit extension to arbitrary invertible linear
transformations of the input bits or to nonuniform product measures.
The proof uses uniform-cube physical flips and multiplication by a
single output character.

## 7. Full written proof's stronger generic hypothesis and formula corollary

The full proof uses an even more general sufficient hypothesis: at most
one coordinate of g has influence strictly greater than 1/2, without
requiring g to be unate. This strengthening is valid. For every Boolean
g and every i,

I_i(g)=Σ_{S containing i}ghat(S)²≤Σ_{S≠∅}ghat(S)²=Var(g).

If a is the only influence greater than 1/2, then 2a−1≤a≤Var(g).
Thus exactly the same total-loss argument goes through without a Chow
identity. Unateness is used only to verify the high-influence hypothesis
for the intended base classes. This statement should retain that
hypothesis; the parity counterexample in Section 6 still shows why it
cannot be discarded.

The full written proof also includes parity modulations of the existing
balanced read-once LTF formulas. Such a formula is indeed unate in its
leaf variables: every gate has fixed monotonicity orientations for its
input bits, and each leaf has a unique path to the root. Multiplying
the gate orientations along that path gives a fixed global orientation
for the leaf. Zero gate weights or irrelevant leaves introduce no
exception. The already established strong bound applies under the same
disjoint-leaf and balanced-nonroot assumptions, so Section 3's modulation
argument supplies the same ordinary FEI constant for this larger class.
The parity and formula may use the same leaves; no further independence
assumption is required. Shared-input circuits and arbitrary biased
nonroot outputs remain outside that corollary.

The stated potentially unbounded-degree polynomial-threshold
interpretation is also legitimate. Threshold ties can first be moved
into a finite attained-score gap, preserving the underlying LTF and
making its affine form nonzero at every cube point. Its parity modulation
is then the sign of that affine form times χ_T, a polynomial of degree
at most |T|+1 after reducing x_i²=1. This interpretation does not imply
a theorem for all polynomial threshold functions of that degree.

## Assessment

The generic conditional statement, the LTF application, and all endpoint
cases pass. Constants and dictators have entropy zero, so the vanishing
I−Var case requires no division. No assumption of disjoint or independent
parity and threshold coordinates appears. The unrestricted Boolean FEI
conjecture remains open, and internal audits do not certify external
acceptance or research novelty.
