SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B11, 2026-09-24T04:17:08Z.
attacking: the punctured heavy-row near-null collar by an exact spectral Schur two-volume identity, then testing which sign/source configurations admit determinant cancellation.

# account04/B11 — spectral Schur budget and the punctured two-sheet collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T041708Z-account04-B11-schur-pseudodet-r1`  
Status: **NEW EXACT IDENTITY / SOURCE-DISJOINT MAJORITY-SIGN COMPILER / FIRST UNSOLVED COLLAR SHARPENED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains OPEN. Continuity is not claimed below. No moments, support bounds, post-rotation independence, arbitrary-joint coarea bound, or density conclusion from a half-line estimate is used.

## 1. Fresh inputs

The current owner control still makes full QFORM the sole target. I used:

- the pinned Claude package at `e5f71d79eff325201dd0274053d20268ce65b837`;
- the later two-sheet update `2b68faa56c5a562d18c51c788bbeb7ecb6f23bd2`;
- account01/B11's binary-indefinite `L^3` and Schur smoothing theorem at `2279571f59ade7a9ec478af1e4818f6c117ac224`;
- account01/B11's zero-pivot Witt-leverage compiler at `22373d23a5a18f91627d8849017beb38a2169f23`;
- account01/B11's arbitrary-pivot low-residual-rank compiler at `5a4909d3e5c696bc6c23c036b60f04a46784157b`.

The Claude statement that the leaking zero-pivot hub is still the smallest open rank-three instance is superseded at essential-boundedness level by the later Witt-leverage compiler: the term `2 epsilon L P` is retained inside the divisible twist. The remaining rank-three obstruction is punctured: a genuinely nonzero but arbitrarily small physical pivot with same-source leakage.

## 2. Exact spectral Schur two-volume identity

Let
[
A=UMU^T,qquad U^TU=I_3,
]
where (M) is invertible symmetric. Thus (A) has exact rank three and its nonzero eigenvalues are those of (M). Fix an ORIGINAL coordinate (h), let
[
v=U^Te_h,qquad q_h=|v|^2,
qquad a=A_{hh}=v^TMv.
]
Assume (a
e0). With the physical split (hmid h^c), write
[
A=egin{pmatrix}a&ell^T\ ell&Cend{pmatrix},
qquad S=C-ellell^T/a.
]

### Theorem 2.1 — `QFORM-SPECTRAL-SCHUR-PSEUDODET-v1`

The Schur complement (S) has rank two and
[
oxed{Delta_2(S)=rac{q_h,Delta_3(A)}{|a|}},
qquad
oxed{|a|Delta_2(S)=q_hDelta_3(A)}. 	ag{2.1}
]
Here (Delta_r) is the product of the nonzero singular values for an exact-rank-(r) symmetric matrix.

#### Proof

Let (U_-) be (U) with row (h) deleted. Then
[
U_-^TU_-=I-vv^T,quad
ell=U_-Mv,quad C=U_-MU_-^T
]
and
[
S=U_-KU_-^T,qquad
K=M-rac{Mvv^TM}{a}. 	ag{2.2}
]
We have (Kv=0). Because (K) is symmetric, it maps (v^perp) into (v^perp). On (v^perp), (U_-) is an isometry:
[
|U_-z|^2=z^T(I-vv^T)z=|z|^2.
]
Hence the two nonzero eigenvalues of (S) are those of (K|_{v^perp}).

Put (e_1=v/sqrt q_h) and write
[
M=egin{pmatrix}alpha&b^T\ b&Dend{pmatrix}
]
in (mathbb Re_1oplus e_1^perp). Since (a=q_halpha), (2.2) becomes
[
K|_{e_1^perp}=D-bb^T/alpha.
]
The Schur determinant identity gives
[
det(K|_{e_1^perp})
=det M/alpha=q_hdet M/a.
]
Taking absolute values proves (2.1). QED.

This is an exact final-matrix identity. It does not rotate the random variables and does not treat a small coefficient as a small random error.

## 3. Signature split

If (A) has inertia ((2,1)), Schur inertia additivity gives:

- if (a>0) is a majority-sign pivot, then (S) has inertia ((1,1));
- if (a<0) is the minority-sign pivot, then (S) is positive definite.

For inertia ((1,2)), reverse all signs. Thus the majority-sign branch exposes the ruled/hyperbolic residual, while the minority-sign branch exposes the convex residual responsible for the two-sheet geometry.

The new ruled one-sheet theorem already controls the one-sheet side of the full rank-three form by (pisqrt2). It cannot by itself control the two-sheet side: the later Claude ring construction shows that a bounded three-dimensional marginal plus uniformly bounded line integrals does not suffice there. Product-convolution structure must still be spent.

## 4. A determinant-cancelling source-disjoint compiler

Account01/B11 proves that every affine nondegenerate binary indefinite quadratic (R(X,Y)) in two ORIGINAL independent cap-one coordinates satisfies
[
|p_R|_3le C_{m bin}D^{-1/3},
qquad D=-det S>0. 	ag{4.1}
]
The completed single-square estimate gives
[
|p_{aZ^2+eta Z+gamma}|_{3/2}
le2|a|^{-1/3}. 	ag{4.2}
]

### Theorem 4.1 — `QFORM-SOURCE-DISJOINT-SCHUR-CANCELLATION-v1`

Suppose an exact-rank-three form admits, on disjoint ORIGINAL source banks,
[
Q=a,[H+T(P)]^2+R(X,Y), 	ag{4.3}
]
where (H,P,X,Y) are mutually source-disjoint, (H,X,Y) have density caps one, (a
e0), and (R) is binary indefinite with determinant scale (D). Then
[
oxed{|p_Q|_{infty,mathrm{ess}}
le2C_{m bin}(|a|D)^{-1/3}.} 	ag{4.4}
]
If (4.3) is the Schur normal form at physical coordinate (h), then by (2.1)
[
oxed{|p_Q|_{infty,mathrm{ess}}
le2C_{m bin}
(q_hDelta_3(A))^{-1/3}.} 	ag{4.5}
]

#### Proof

The variable (H+T(P)) is a mixture of translates of (H), so its density is capped by one. Its source bank is disjoint from ((X,Y)); therefore its square is independent of (R). Apply (4.1), (4.2), and Young (L^3*L^{3/2}	o L^infty), then insert (2.1). QED.

This is the desired determinant cancellation: the apparent small-pivot loss disappears because the residual two-volume grows exactly as (1/|a|).

### Concrete target family

For independent cap-one (H,P,X,Y), (m,kge1), and (0<qle1), set
[
Q=m(sqrt q,H+sqrt{1-q},P)^2+2kXY. 	ag{4.6}
]
Its nonzero spectrum is ({m,k,-k}), hence it lies in the original target class. Equation (4.5) gives the actual full-line inequality
[
oxed{|p_Q|_{infty,mathrm{ess}}
le2C_{m bin}(qmk^2)^{-1/3}.} 	ag{4.7}
]
In particular, for (qge1/2),
[
|p_Q|_{infty,mathrm{ess}}le2^{4/3}C_{m bin}.
]
No half-line estimate is promoted here; (4.7) is a genuine full-line density bound.

## 5. The exact punctured gap

For a heavy physical row (q_h>1/2) and (Delta_3(A)ge1), the freshest account01/B11 results give:

- at the exact zero pivot,
[
|p_Q|_{infty,mathrm{ess}}
le3,2^{4/3}(q_hDelta_3(A))^{-1/3}
<3,2^{5/3}; 	ag{5.1}
]
- for (|a|gedelta>0), the scalar-pivot theorem gives
[
|p_Q|_{infty,mathrm{ess}}
le128(q_h|a|Delta_3(A))^{-1/4}
le128(delta/2)^{-1/4}. 	ag{5.2}
]

The sole discontinuity is therefore
[
oxed{0<|a|ll1,qquad q_h>1/2,} 	ag{5.3}
]
when the square shift and the rank-two Schur residual use the same original source bank. Existing dependent Abel smoothing gives only an (|a|^{-1/4})-type loss after (2.1); it does not achieve the conjugate-exponent cancellation (4.4).

The missing statement is now precise: prove (4.4), or another universal estimate, when (T) and (R) are entangled functions of the same product source. It is false for an arbitrary joint density; the product-convolution structure is essential.

## 6. The collar is nonempty inside the exact target

Fix (q=3/4), (M=operatorname{diag}(1,1,-1)), and (|arepsilon|<q). Put
[
v_arepsilon=
left(sqrt{rac{q+arepsilon}{2}},0,
      sqrt{rac{q-arepsilon}{2}}ight).
]
Then (|v_arepsilon|^2=q) and
[
v_arepsilon^TMv_arepsilon=arepsilon.
]
Choose (U_arepsilon) with orthonormal columns and first row (v_arepsilon^T). This is always possible because (I-v_arepsilon v_arepsilon^Tge0). By splitting each remaining row into sufficiently many equal copies, every other physical row can be made to have leverage at most (1/3). Define
[
A_arepsilon=U_arepsilon M U_arepsilon^T.
]
Then
[
operatorname{spec}_{
e0}(A_arepsilon)={1,1,-1},
quad q_h=3/4,quad (A_arepsilon)_{hh}=arepsilon,
]
and Theorem 2.1 gives
[
oxed{Delta_2(S_arepsilon)=rac{3}{4|arepsilon|}.} 	ag{6.1}
]
Thus the hard near-null collar is a genuine exact-rank-three target family, not a bookkeeping artifact. At (arepsilon=0), (5.1) is uniform; at nonzero (arepsilon), (5.2) diverges as (|arepsilon|^{-1/4}). Closing that puncture without losing product provenance is the first remaining B11 implication.

## 7. Status

This run proves the exact spectral Schur identity (2.1), closes the source-disjoint majority-sign Schur branch with determinant cancellation, and isolates the actual same-source punctured two-sheet collar. It does not solve unrestricted QFORM. Continuity remains separate.
