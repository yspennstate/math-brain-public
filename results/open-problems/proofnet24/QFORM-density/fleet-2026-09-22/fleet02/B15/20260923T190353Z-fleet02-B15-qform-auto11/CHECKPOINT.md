# fleet02/B15 early checkpoint — bounded Fisher budgets are not a rough-input closure class

Run `20260923T190353Z-fleet02-B15-qform-auto11`. Full unrestricted QFORM remains OPEN.

## First unpaid implication

The new projected-Fisher theorem gives a uniform QFORM height only when the projected information
`J_E=sum_i ell_i I(f_i)` is finite and quantitatively controlled. The first unpaid regularity implication is therefore **not** continuity of the rough output. It is whether arbitrary cap-one product laws can be reached from the Fisher-regular class while keeping the theorem's `J_E` budget uniformly bounded. The calculation below shows that this is false already for the extremal interval marginal, and quantitatively so.

## Lemma — L1 distance to a jump forces Fisher information to diverge

Let `u=1_[0,1]`. Let `f` be any probability density with `sqrt(f) in H^1(R)`, and write

`eta=||f-u||_1` and `I(f)=4 ||(sqrt f)'||_2^2`.

If `0<eta<=1/8`, then

`I(f) >= 1/(4 eta)`.                                           (1)

Proof. Put `g=sqrt(f)` and `v=1_[0,1]`. Since `(sqrt a-sqrt b)^2<=|a-b|`,

`||g-v||_2 <= sqrt(eta)`.                                     (2)

For `0<h<=1`, `||v(.+h)-v||_2=sqrt(2h)`. Hence by two applications of the triangle inequality,

`||g(.+h)-g||_2 >= sqrt(2h)-2 sqrt(eta)`.                      (3)

The H1 translation inequality gives

`||g(.+h)-g||_2 <= h ||g'||_2 = h sqrt(I(f))/2`.               (4)

Take `h=8 eta<=1`. Equations (3)-(4) give

`4 eta sqrt(I(f)) >= 2 sqrt(eta)`,

which is exactly (1). The choice `h=8 eta` optimizes the constant produced by this argument.

No density cap was used in (1).

## Cap-one weak-separation corollary

If additionally `f<=1`, write `m=1-int_0^1 f`, the mass outside `[0,1]`. Then

`||f-u||_1=2m`.

Consequently every cap-one Fisher-regular density satisfies

`m >= min(1/16, 1/(8 I(f)))`,                                 (5)

with the convention that the second term is irrelevant when `I(f)=0`. Thus a class with `I(f)<=J<infinity` obeys

`P_f([0,1]) <= 1-min(1/16,1/(8J))`.                           (6)

In particular, no cap-one class with a common finite Fisher-information budget can converge weakly to `Uniform[0,1]`. This is stronger than checking one particular mollifier: **every** Fisher-regular cap-preserving approximation must pay diverging information.

## Exact QFORM consequence

For the normalized three-large-eigenvalue matrix

`A=[[0,1,0],[1,0,0],[0,0,1]]`,

one has `Q=2 X_1 X_2+X_3^2` and spectrum `{1,-1,1}`. Its selected three-dimensional eigenspace is all of `R^3`, so the new Fisher theorem has

`J_E=I(f_1)+I(f_2)+I(f_3)`.                                  (7)

If regular product laws `prod f_i` converge in L1 to the cube law `u^⊗3` with joint distance `eta<=1/8`, marginalization contracts L1, so `||f_i-u||_1<=eta` for each i. Applying (1) coordinatewise gives

`boxed( J_E >= 3/(4 eta) )`.                                  (8)

Therefore the projected-Fisher certificate cannot remain uniform along **any** L1 rough-input approximation to this exact target source. This is a route obstruction only; it says nothing adverse about the true QFORM height.

## Completed source result applied to the same rough target

The completed ruled one-sheet theorem in `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` applies to this same matrix. In spectral coordinates it has signature `(1,1,-1)` and one-sheet coefficient

`C_+=int_0^(2pi) dtheta/sqrt(2)=pi sqrt(2)`.

For the actual rough source `X_i~Uniform[0,1]`,

`Q=2X_1X_2+X_3^2 >=0` almost surely,

so the majority one-sheet submeasure is the entire output law. Hence, without any smoothing or continuity premise,

`boxed( P(Q in I) <= pi sqrt(2) |I| )`                         (9)

for every interval `I`, and therefore `||p_Q||_infinity<=pi sqrt(2)` essentially. Integrating the triangular kernel also gives

`boxed( E (eps-|Q-y|)_+ <= pi sqrt(2) eps^2 )`.                (10)

Thus the exact rough law that forces every Fisher-regular approximation budget to blow up is nevertheless paid directly by product-sensitive ruled geometry.

The rough bridge behind (9) is the safe one: mollify the **original coordinates**, use the smooth ruled formula, then pass the already-proved interval inequality by total-variation contraction of deterministic pushforward. Continuity of the rough output is not used to obtain the height.

## Partner connection

The latest compatible fleet03/B15 result (`20260923T182510Z-fleet03-B15-qform-auto25`) proves an analogous, but different, separation for the full Gaussian-component-mixture branch: with `E T^(-1/2)<=sqrt(2pi)`, every component-mixture marginal places at most `alpha_*=2 Phi(sqrt(pi/2))-1<0.79` mass in a unit interval, so it cannot even converge weakly to `Uniform[0,1]`. The present Fisher lemma shows that the other new regularity branch also has a genuine non-density obstruction: bounded projected information is not a closure mechanism for arbitrary cap-one inputs.

This does not refute either regular-input theorem and does not provide a QFORM counterexample. It isolates the rough endpoint: a full proof needs a mechanism that uses the final density cap/product provenance directly rather than a uniform hidden regularity budget.
