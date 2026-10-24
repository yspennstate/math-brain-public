# FEI for arbitrary parity modulations of linear threshold functions

Date: 2026-10-02 UTC. Complete elementary derivation conditional on the campaign's internally audited strengthened LTF theorem. The [independent full analytic audit](parity_modulated_ltf_heat_audit.md) passes. Historical priority and external peer review are unverified.

For a Boolean function on the uniform cube write H(g)=sum_S ghat(S)^2 log2(1/ghat(S)^2), I_i(g)=Pr[g(X)!=g(X^flip_i)], I(g)=sum_i I_i(g), and V(g)=Var(g). For T contained in the coordinates, let chi_T(x)=product_(i in T) x_i.

## A general character-shift lemma

For every Boolean g,

H(chi_T g)=H(g),

I(chi_T g)=sum_(i not in T) I_i(g)+sum_(i in T)[1-I_i(g)].

The first equality follows from (chi_T g)hat(S)=ghat(S symmetric_difference T). The second follows directly from a coordinate flip: multiplying by a character containing i reverses whether that edge changes value. Hence

I(chi_T g)>=sum_i min(I_i(g),1-I_i(g))
=I(g)-sum_i(2I_i(g)-1)_+.

If at most one coordinate of g has influence greater than1/2, the last loss is at most V(g). Indeed, every I_i(g)<=V(g) by the Fourier identity I_i=sum_(S containing i) ghat(S)^2 and Parseval V=sum_(S nonempty) ghat(S)^2. If a is the sole influence above1/2, then 2a-1<=a<=V(g). If no such coordinate exists the loss is zero. Therefore

I(chi_T g)>=I(g)-V(g)

under this explicit high-influence hypothesis. This step does not require a Chow identity or unateness.

Consequently, any Boolean class with that influence hypothesis and a bound H(g)<=C[I(g)-V(g)] satisfies FEI with the same C after arbitrary character modulation.

## Why every unate Boolean function meets the hypothesis

A function is unate when sign changes of individual inputs make it coordinatewise nondecreasing. Input sign changes preserve each influence. It is therefore enough to consider monotone g.

Fix distinct coordinates i,j and condition on all the others. Each resulting two-bit monotone truth table is one of six types: the two constants, either dictator, AND, or OR (with the usual two-value labels). The sum of its two physical influences is0 for a constant and1 for every nonconstant type. Averaging conditional influences gives

I_i(g)+I_j(g)<=1.

Thus at most one coordinate can have influence greater than1/2. This holds for every unate Boolean function, independently of output bias.

There is also a sharper familiar route for the one-coordinate loss: for monotone g, ghat({i})=I_i(g); input sign changes give absolute value equality for unate g. Parseval therefore gives V(g)>=sum_i I_i(g)^2. Since 2a-1<=a², this independently bounds the loss by V(g). This Chow identity is established prior work, not a new theorem.

## All parity-modulated LTFs

Every linear threshold function g(x)=sign(sum_i w_i x_i-t), with any fixed tie convention, is unate. The campaign's completed [strengthened LTF theorem](../2026-10-02-strong-LTF-composition/strong_ltf_and_balanced_composition_proof.md) supplies one universal C_plus with H(g)<=C_plus[I(g)-V(g)]. Applying the lemma proves

H(chi_T(x) sign(sum_i w_i x_i-t))<=C_plus I(chi_T g)

for every dimension, arbitrary real weights and bias, and every set T. Overall output complementation changes neither quantity. T can grow with dimension, so the displayed polynomial-threshold representation may have unbounded degree. The theorem does not assert FEI for arbitrary polynomial threshold functions or arbitrary input-biased product laws.

The same conclusion applies to arbitrary parity modulations of the earlier balanced read-once LTF formulas. Such a formula is unate on its disjoint leaf variables: every leaf has one path to the root, and the fixed input orientations of its LTF gates multiply along that path to give a fixed monotonicity orientation for that leaf. The [existing formula theorem](../2026-10-02-strong-LTF-composition/strong_ltf_and_balanced_composition_proof.md) gives the same strengthened constant when every nonroot output is balanced and leaf blocks are disjoint. Therefore character modulation preserves ordinary FEI with C_plus. The root may be biased; arbitrary biased nonroot outputs and shared-input circuits remain outside this corollary.

## Limits and provenance

The character-shift and flip identities are elementary standard facts. The unate two-coordinate inequality follows from the explicit six truth tables. The monotone Chow identity is established in O'Donnell's *Analysis of Boolean Functions*, Proposition2.21; this optional route is not needed for the first argument. The new class-wide mathematical input is the campaign's strengthened all-LTF bound. No priority claim is made for this derived modulation principle.

The influence hypothesis cannot be silently dropped: a parity of two or more coordinates has several influences equal to1, and modulation by that same character makes it constant. In that case I(g)-V(g)>0 while the modulated influence is0. This does not violate FEI, since both spectral entropies are0; it shows why the general comparison of budgets needs its stated hypothesis.

The standalone [exact checker](verify_parity_modulation.py) and [output](parity_modulation_checks.json) enumerate all7,778 monotone functions through five variables and all245,470 character modulations. Integer Walsh numerators verify permutation of the entire squared spectrum, and independent physical-flip counts verify the modulation and budget identities exactly. No universal constant is inferred from these finite checks. The analytic proof above supplies the class-wide implication.
