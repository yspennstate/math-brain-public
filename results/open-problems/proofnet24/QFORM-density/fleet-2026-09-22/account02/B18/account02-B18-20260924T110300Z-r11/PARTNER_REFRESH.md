# account02/B18 r11 — latest-partner refresh: definite transverse-plane exit is also a literal-coordinate gate

A newer compatible account03/B18 result arrived after the main report was written. The latest completed partner is now

`QFORM-LITERAL-RANK1-DEFINITE-TRANSVERSE-PLANE-v1`,

canonical mathematics `yspennstate/math-open-problems@66fc5c80cc24b1917c2c83114dbd47e197018d2f`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260924T105855Z-account03-B18-QFORM-auto11/REPORT.md`.

Its primary external input is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1. The exact source scope needed here is a genuine product density with one-dimensional caps at most one; every three-dimensional orthogonal marginal then has density cap at most `2^(3/2)`. No moment, support, iid, log-concavity, centering, symmetry or smoothness assumption is present, and the theorem does not create independence among projected coordinates.

The partner theorem says: for an ORIGINAL-coordinate split `{i} disjoint J disjoint K`, if `A_ii=0`, `b=A_(i,J)` has `beta=||b||>0`, `V=span{b}+ran(A_JJ)` is three-dimensional, the compression `Gamma` of `A_JJ` to `V intersect b^perp` is definite with `Delta=|det Gamma|>0`, and `ran(A_JK) subset V`, then

`||p_(X^T A X)||_infinity <= 2^(7/4) sqrt(pi) / sqrt(beta sqrt(Delta))`,

with a continuous `C_0` density in this scope.

## 1. A real inequality on the diffuse endpoint

Retain the two banks `I,J` from the main report, and define one further flat vector on `J`

`z = m^(-1/2) (+1,-1,-1,+1)`

by quarters. Then `v,v2,w,z` are orthonormal. At `eps=0` set

`D_0=u v^T`,

`C_0=w w^T+z z^T`,

`bar A_0=[[0,D_0],[D_0^T,C_0]]`.

Its nonzero spectrum is `{-1,1,1,1}`, so it is a literal owner-target matrix.

Fix any original coordinate `i in I`. Apply the newest partner theorem with

- source coordinate `{i}`;
- `J` equal to the whole opposite bank;
- `K=I\{i}`.

Then

`b=A_(i,J)=v/sqrt(m)`, so `beta=m^(-1/2)`;

`V=span{v,w,z}` has dimension three;

`V intersect b^perp=span{w,z}` and the transverse compression is the identity, so `Delta=1`;

`ran(A_JK)=span{v} subset V`.

Every hypothesis is therefore met, and the latest partner gives the genuine target inequality

`boxed: ||p_(X^T bar A_0 X)||_infinity <= 2^(7/4) sqrt(pi) m^(1/4).`      (1.1)

The numerical prefactor is `5.96180035771636...`. This is a correct source-valid certificate, but it grows like `m^(1/4)`: a literal-coordinate transverse-plane exit does not by itself aggregate a flat rank-one cross bank.

## 2. The overlapping rank-two tail breaks the partner's allowed-affine gate

Now restore the maximally overlapping tail from the main report:

`D_eps=u v^T+eps u2 v2^T`, `0<eps<1`,

and keep `C_0=w w^T+z z^T`. Denote the resulting matrix by `bar A_eps`. Its exact nonzero spectrum is

`{-1,1,1,1,-eps,eps}`,

so it has four eigenvalues of modulus at least one and remains well inside the owner target.

For the same singleton split, write `s_i=sqrt(m)(u2)_i in {+1,-1}`. Then

`b_i=m^(-1/2)(v+s_i eps v2)`,

and

`V_i=span{v+s_i eps v2,w,z}`

is still three-dimensional with the same definite transverse compression `Gamma=I_2`. However the remaining source coordinates contain both signs of `u2`, so

`ran(A_JK)=span{v,v2}`.                                                (2.1)

Because `V_i` contains only one direction from the two-plane `span{v,v2}`, while `w,z` are orthogonal to that plane,

`boxed: ran(A_JK) is not a subset of V_i for every i and every eps>0.`  (2.2)

Thus the same nonzero overlapping tail that breaks the pinned Theorem-F diagonal-twist gate in the main report also breaks the newest partner theorem at its explicit `outside-to-J affine components outside V` hypothesis. This is not a criticism of the theorem; that hypothesis is exactly one of the debts its own handoff leaves open.

The comparison sharpens the live endpoint:

- at `eps=0`, the definite transverse-plane theorem is valid but costs `m^(1/4)` because every literal cross row has norm `m^(-1/2)`;
- at every `eps>0`, the diffuse same-source second cross direction creates an unretained affine direction after conditioning the other original source coordinates, so the theorem is not applicable at all through this singleton split;
- the full matrix nevertheless keeps at least four target-scale eigenvalues.

Hence the needed bridge is aggregate-before-literal-coordinate: one must group the diffuse source bank or use a product-Fourier/projected-crossing mechanism that retains the second cross direction without paying its small singular value or projecting it into an inadmissible conditional affine component.

This latest-partner refresh leaves the main report's unpaid implication unchanged:

`QFORM-OVERLAPPING-RANK2-TAIL-AGGREGATE-STABILITY-v1`.
