# fleet04/B12 — explicit endpoint stability under a large added eigendirection and dependent tail

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Worker:** fleet04/B12  
**Run:** `20260922T181535Z-fleet04-B12-endpoint-tail-r1`  
**Status:** PROVED_SUPPORTING_THEOREM / FULL QFORM OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. Target and scope

The full target asks for one universal constant for the density of (X^TAX), for arbitrary independent cap-one coordinate densities and every real symmetric (A) with at least three eigenvalues of modulus at least one.

This report proves a stability corollary for adding:

1. one rank-one eigendirection of completely unrestricted magnitude and either sign; and
2. an arbitrary-rank, mixed-sign symmetric tail which remains genuinely dependent on the core after rotation.

No convolution independence is asserted. The proof stays in the original coordinates and uses Schur complements.

## 2. Completed partner theorem used

I apply fleet01/B12's completed endpoint-Schur theorem:

- repository/commit: `yspennstate/math-open-problems@9c39f272f2bbaa526533f38ba0ff82ee801732a1`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B12/20260922T171905Z-fleet01-B12-QFORM-r14/REPORT.md`.

Write
[
 A_	au=A_0+	au vv^T,qquad
 A_0=egin{pmatrix}alpha&b^T\\b&Cend{pmatrix},qquad
 v=(u,w),quad u
e0,
]
relative to one original coordinate. Define
[
 a_	au=alpha+	au u^2,quad
 z=b-rac{alpha}{u}w,quad
 S_infty=C-rac{bw^T+wb^T}{u}+rac{alpha}{u^2}ww^T.
]
Then
[
 operatorname{Sc}_i(A_	au)=S_infty-a_	au^{-1}zz^T.
]

Let (sigmain{pm1}). Suppose a physical residual triple (T) satisfies
[
 lambda_2!left(sigma S_infty[T,T]ight)ge L>0
]
and (sigma a_	au<0). If an arbitrary symmetric tail (E) has
(|E|_{m op}ledelta<|a_	au|), put
[
 arepsilon_{m tail}
 =
 rac{deltaleft(1+|b+	au uw|/|a_	au|ight)^2}
 {1-delta/|a_	au|}.
]
When (arepsilon_{m tail}<L), the partner theorem gives
[
 |p_{X^T(A_	au+E)X}|_infty
 le
 2sqrt{rac{C_*}{(L-arepsilon_{m tail})(|a_	au|-delta)}},
 	ag{2.1}
]
where (C_*=24.183038289961516ldots). This is the actual inequality used below.

## 3. Explicit asymptotic stability theorem

### Theorem 3.1

With the notation above, set
[
 r=rac{|w|}{|u|}.
]
Assume
[
 operatorname{sign}(	au)=-sigma,
 qquad
 |	au|u^2ge
 max{2|alpha|,;2|b|,;4delta},
 	ag{3.1}
]
and
[
 deltale rac{L}{16(1+r)^2}.
 	ag{3.2}
]
Then, for every collection of independent real coordinates with probability densities at most one,
[
 oxed{
 |p_{X^T(A_	au+E)X}|_infty
 le
 rac{4sqrt{2C_*/L}}{|u|sqrt{|	au|}}.
 }
 	ag{3.3}
]

Thus the output-density height decays like the inverse square root of the magnitude of the added eigenvalue, uniformly over the full arbitrary-rank dependent tail (E) satisfying (3.2).

### Proof

From (|	au|u^2ge2|alpha|),
[
 |a_	au|=|alpha+	au u^2|
 ge rac12|	au|u^2.
 	ag{3.4}
]
The sign condition also gives (sigma a_	au<0).

Next,
[
 rac{|b+	au uw|}{|a_	au|}
 le
 rac{|b|+|	au||u||w|}{|	au|u^2/2}
 le 1+2r,
 	ag{3.5}
]
where the last step uses (|	au|u^2ge2|b|). Therefore
[
 1+rac{|b+	au uw|}{|a_	au|}
 le2(1+r).
 	ag{3.6}
]
Also, (3.1) and (3.4) imply (delta/|a_	au|le1/2). Consequently
[
 arepsilon_{m tail}
 le
 2delta,[2(1+r)]^2
 =
 8delta(1+r)^2
 le rac L2
 	ag{3.7}
]
by (3.2). Hence
[
 L-arepsilon_{m tail}gerac L2,
 qquad
 |a_	au|-deltagerac{|a_	au|}{2}
 gerac{|	au|u^2}{4}.
 	ag{3.8}
]
Substituting (3.8) into (2.1) yields
[
 |p|_infty
 le
 2sqrt{rac{C_*}{(L/2)(|	au|u^2/4)}}
 =
 rac{4sqrt{2C_*/L}}{|u|sqrt{|	au|}}.
]
This proves (3.3). QED.

## 4. Interpretation

The hypothesis (3.2) is independent of (|	au|): once the tail is below the endpoint spectral reserve (L) after paying the geometric factor ((1+|w|/|u|)^2), the added eigendirection may become arbitrarily large without destabilizing the density estimate. In fact the estimate improves as (|	au|^{-1/2}).

This is not an independent-convolution argument. The tail can mix every coordinate and can have arbitrary rank and either signs. Its effect is controlled inside the same physical Schur complement by the partner perturbation inequality.

For a coordinate-local added direction ((w=0)), (3.2) becomes simply
[
 deltale L/16,
]
and the same conclusion holds. For a delocalized direction the exact price is the coordinate-overlap ratio (r=|w|/|u|); choosing a coordinate of maximal (|u|) minimizes this price.

## 5. Relation to the full conjecture

This theorem pays a genuine additional-eigenvalue branch: one unrestricted large rank-one component plus a nonseparable arbitrary-rank small tail. It does not prove that every target matrix admits a coordinate and sign with an endpoint triple satisfying the hypotheses with universal (L,u,r).

The remaining universal implication is structural: starting from three protected eigenvalues, select or aggregate original-coordinate endpoint certificates so that either the ridge/grouped-coordinate theorems apply or one obtains (3.1)–(3.2) at universal scale. The known singleton-plus-two-banks family prevents replacing that aggregation by a single uniformly conditioned small principal minor.

The theorem establishes an essentially bounded density. Continuity follows separately for every fixed rank-at-least-three target from the completed B15 regularity theorem, but no continuity claim is needed in the Schur estimate itself.

## 6. Integrity notes

The arbitrary-joint coarea lemma and conditional projected-density moment gate are not used; both are refuted in the current correction ledger. No rotation is claimed to preserve independence, no moment or support assumption is added, and no numerical experiment is used as proof.
