# r22 late-correction addendum — compatibility with B16 square-peel log barrier

A later fresh-main read after the immutable r22 report exposed account02/B16 r25, canonical math `yspennstate/math-open-problems@0936cdfbdb963107eeef788ede720897943cf902`, theorem/obstruction `QFORM-NEAR-NULL-SQUARE-PEEL-LOG-BARRIER-v1`.

That result is binding. It shows that for the exact-target leverage-one family

`Q_delta = delta X_0^2 + 2 sqrt(1+delta) X_0 Y + Z^2`,

the translation-uniform scalar-square envelope and the full half-Riesz certificate diverge as `delta -> 0`, although the true density is uniformly bounded by the source-applied Fourier theorem. Thus one may not claim that arbitrary near-null coloop states are uniformly closed by scalar completion alone.

The r22 theorem remains compatible because its scalar-completion step is used **only** in the disjoint branch

`0<|a|<=1/16`, `|gamma|<1/2`,

where the inverse certificate proves first that

`|a det B| >=255/512`.

Consequently the square/half-Riesz estimate there has a uniformly nondegenerate determinant currency before it is invoked:

`||p_Q||_infinity <=16 sqrt(30)|a det B|^(-1/4) <104.319`.

The B16 log-barrier family lies in the opposite branch: after aligning the scalar cross vector it has

`a=delta`, `beta=sqrt(1+delta)`, `delta_cross=0`, `gamma=1`,

so `|gamma|>=1/2` and `|a det B|=delta(1+delta)->0`. R22 does **not** use scalar completion there. It uses the r21 selector-preserving theorem `QFORM-NEARNULL-SCALAR-DEPENDENT-PAIR-v1`, whose proof explicitly retains the translated scalar source factor instead of replacing it by height one.

Therefore the later B16 correction narrows the interpretation, but does not invalidate `QFORM-COLOOP-MIXED-INVERSE-CERTIFICATE-v1` or `QFORM-EXACT-COLOOP-CLOSURE-v1`. The logical split is now explicit:

- large direct transverse curvature (`|gamma|>=1/2`): selector-preserving r21 mechanism;
- small direct transverse curvature (`|gamma|<1/2`): inverse certificate first, then scalar-square/rank-two half-Riesz with `|a det B|` already bounded below;
- generic near-null scalar completion without one of those certificates: prohibited by the B16 r25 log barrier.

Full QFORM remains OPEN.
