SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B20, 2026-09-23T20:32:20Z.
attacking: the r37 common-plane triangle payment problem; expose an exact invariant normal form for the quantitative 2+2+2 main cycle and sharpen the designated fleet04/B20 three-bank product certificate on the same physical partition.

# fleet03/B20 auto11b — transported-edge normal form and sharpened three-fan certificate

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T203220Z-fleet03-B20-QFORM-auto11b`.
Role: proof closure and keeper / synthesis.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Status: **NEW DETERMINISTIC CLOSURE COMPILER + DESIGNATED PARTNER RESULT APPLIED / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.


The canonical fleet03/B20 `20Z` login and the account/hour keeper lease already belonged to the earlier compliant run `20260923T200427Z-fleet03-B20-QFORM-r38`. They were not overwritten or duplicated. This run uses only its own immutable math path and records zero scheduler mutations.

## 1. Immediate source and live quantitative cycle

The immediate source is fleet03/B20 r36 and r37:

- `yspennstate/math-open-problems@1fe3d344529b743f64cb37b42a7a12b6a86a9414`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T180245Z-fleet03-B20-QFORM-r36/REPORT.md`;
- `yspennstate/math-open-problems@598dae792b4a447492bc318bfa830fece803bb6d`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T184417Z-fleet03-B20-QFORM-r37/REPORT.md`.

There are three disjoint ORIGINAL-coordinate banks `D_1,D_2,K`. The r36 common-plane skeleton supplies two-dimensional physical coefficient spaces on all three banks. In orthonormal bases of those spaces write

`B_1, B_2` for the two `D_r-K` main legs and `C_0` for the compressed `D_1-D_2` edge. The proved inequalities are

`s_min(B_r) >= beta := 0.01651671529470044`,                    (1.1)

`|det B_r| >= d_0 := 0.0011039951248231808`,                   (1.2)

and

`||C_0||_F > c_0 := 0.11907425120090158`.                       (1.3)

The off-plane physical tail remains present in the ambient quadratic form and is not discarded; r36 separately records its combined Frobenius square below `5.567385390330438e-6`.

The pure `2+2+2` main-cycle coefficient matrix is

`S = [[0, C_0, B_1],
      [C_0^T, 0, B_2],
      [B_1^T, B_2^T, 0]]`.                                     (1.4)

The point of the next theorem is algebraic. It does **not** declare the rotated two-dimensional coordinates independent. It identifies exactly what the main cycle itself can and cannot degenerate into.

## 2. Exact transported-edge theorem

Define the unnormalized transported edge

`T := adj(B_1) C_0 adj(B_2)^T`,                                 (2.1)

and split it orthogonally into symmetric and skew parts

`H := (T+T^T)/2`, `K := (T-T^T)/2`.                             (2.2)

### Theorem 2.1 — `QFORM-TRIANGLE-TRANSPORTED-EDGE-NORMAL-FORM-v1`

For the main-cycle matrix (1.4):

1. the exact determinant identity is

   `boxed: det S = det(T+T^T) = 4 det H;`                        (2.3)

2. the exact rank identity is

   `boxed: rank S = 4 + rank(T+T^T) = 4 + rank H;`               (2.4)

3. the transported edge has the fixed absolute mass

   `boxed: ||T||_F > tau_0 := beta^2 c_0
          = 3.2483680078521365e-5.`                              (2.5)

Consequently every live common-plane triangle lies in at least one of the following three quantitative chambers:

**(A) two-dimensional symmetric transport:**

`s_2(H) >= tau_0/8 = 4.060460009815171e-6`,                     (2.6)

in which case the complete six-dimensional main-cycle determinant satisfies

`boxed: |det S| >= tau_0^2/16
       = 6.594934196523286e-11;`                                (2.7)

**(B) rank-one symmetric collar:**

`s_2(H) < tau_0/8` and `s_1(H) >= tau_0/4`,                     (2.8)

so

`dist_op(H, rank<=1) < tau_0/8`, `||H||_op >= tau_0/4`;          (2.9)

**(C) symplectic-skew collar:**

`s_1(H) < tau_0/4`.                                             (2.10)

Since every real `2x2` skew matrix is `omega J`, `J=[[0,1],[-1,0]]`, this chamber obeys

`K=omega J`,

`boxed: |omega| > (sqrt(7)/4) tau_0
       = 2.1485934788987656e-5.`                                (2.11)

Thus the formerly generic common-plane cycle has only three invariant algebraic failure modes: fixed six-dimensional determinant, a quantitatively rank-one symmetric transported edge, or a quantitatively nonzero alternating/symplectic transported edge.

### Proof

Let `delta_r=det B_r`, which is nonzero by (1.1). Make only the deterministic congruence

`P = diag(B_1^{-T}, B_2^{-T}, I_2)`.                            (2.12)

Then

`P^T S P = S_D := [[0,D,I_2],[D^T,0,I_2],[I_2,I_2,0]],`         (2.13)

where

`D=B_1^{-1} C_0 B_2^{-T}=T/(delta_1 delta_2)`.                  (2.14)

For `(x,y,z)` in the kernel of `S_D`, the three block equations are

`Dy+z=0`, `D^T x+z=0`, `x+y=0`.                                (2.15)

Hence `y=-x`, `z=Dx`, and the only remaining condition is

`(D+D^T)x=0`.                                                   (2.16)

Therefore

`nullity(S_D)=nullity(D+D^T)`,                                 (2.17)

which immediately yields (2.4), since congruence preserves rank and multiplication by the nonzero scalar `delta_1 delta_2` preserves the rank of the `2x2` symmetric matrix.

A direct `2x2` Schur/block determinant calculation, or elimination using (2.15), gives

`det S_D = det(D+D^T)`.                                        (2.18)

Because `det P=(delta_1 delta_2)^(-1)`,

`det S_D=(delta_1 delta_2)^(-2) det S`.                         (2.19)

On the other hand, from (2.14),

`det(D+D^T)=(delta_1 delta_2)^(-2) det(T+T^T)`.                 (2.20)

Equations (2.18)-(2.20) prove (2.3).

For any invertible `2x2` matrix B with singular values `s_1>=s_2>0`, `adj(B)=det(B)B^{-1}` has singular values exactly `s_1,s_2`. Thus

`s_min(adj(B_r))=s_min(B_r)>=beta`.                             (2.21)

The Frobenius lower bound under left/right multiplication gives

`||T||_F
 >= s_min(adj B_1) s_min(adj B_2) ||C_0||_F
 > beta^2 c_0=tau_0`,                                          (2.22)

proving (2.5).

Now `H` and `K` are Frobenius-orthogonal, so

`||T||_F^2=||H||_F^2+||K||_F^2>tau_0^2`.                       (2.23)

If (A) holds, then for symmetric `H`, `|det H|=s_1(H)s_2(H)>=s_2(H)^2`, and (2.3) gives

`|det S|=4|det H| >=4(tau_0/8)^2=tau_0^2/16`,                  (2.24)

which is (2.7).

If (A) fails but `s_1(H)>=tau_0/4`, we are in (B), and (2.9) is exactly Eckart-Young for a `2x2` symmetric matrix.

Finally suppose `s_1(H)<tau_0/4`. Then

`||H||_F^2 < 2(tau_0/4)^2=tau_0^2/8`,                          (2.25)

so by (2.23), `||K||_F^2>7 tau_0^2/8`. Writing `K=omega J` gives `||K||_F^2=2 omega^2`, hence

`|omega|>sqrt(7) tau_0/4`,                                     (2.26)

which is (2.11). QED.

The determinant/rank calculation is exact. It is a deterministic algebraic compiler only; no density theorem is inferred merely from `det S!=0`, because the latent plane coordinates are not assumed independent and the ambient same-bank curvature remains present.

## 3. Fresh designated fleet04/B20 application: improve the simultaneous three-fan scalar certificate

The completed designated partner is fleet04/B20 r11:

`yspennstate/math-open-problems@9d07c5d5c69c885509db66cb1093acdeff8bcb64`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260923T181642Z-fleet04-B20-QFORM-r11/REPORT.md`.

For unit common-plane direction `h=Va`, with weights `w_k=h_k^2` and `eta=max_k w_k<1/16` in the r37 diffuse branch, its exact three-color theorem gives

`E[W_1W_2W_3] > (1-3/16)/27 = 13/432`.                         (3.1)

Always `W_1W_2W_3<=1/27`. Let

`E_s={W_1W_2W_3>=1/72}`.                                      (3.2)

Then

`13/432
 < E[W_1W_2W_3]
 <= (1/72) P(E_s^c) + (1/27)P(E_s)`,                            (3.3)

so, exactly,

`boxed: P(E_s)>7/10.`                                          (3.4)

The same random coloring is used in r37's matrix Chernoff step. Its matrix-balanced event `E_m`, on which all three common-plane sub-Grams satisfy `G_b >= I_2/12`, has

`P(E_m)>0.302217653453289`.                                    (3.5)

Therefore

`P(E_m intersect E_s)
 >0.302217653453289+0.7-1
 =0.002217653453289>0`.                                        (3.6)

Hence one and the same deterministic ORIGINAL-coordinate partition

`K=K_1 disjoint_union K_2 disjoint_union K_3`                   (3.7)

can be chosen so that all six r37 physical arm bounds remain valid,

`s_2(A[D_r,K_b])>0.002408434254376076`,                         (3.8)

and simultaneously the selected common-plane scalar masses obey the stronger

`boxed: W_1W_2W_3 >=1/72.`                                     (3.9)

For the three disjoint-bank scalar projections `H_b`, the partner projection theorem therefore improves r37's simultaneous joint cap from `<44.817` to

`boxed:
 ||p_(H_1,H_2,H_3)||_infinity
 <= e^(3/2)/sqrt(W_1W_2W_3)
 <= sqrt(72)e^(3/2)
 <38.029.}`                                                     (3.10)

This is an equation-level application of the designated fleet04/B20 result to the live common-plane inequalities. Independence in (3.10) comes only from the disjoint original-coordinate banks; it is not post-rotation independence. And (3.10) is not, by itself, promoted to a curved quadratic pushforward estimate.

## 4. New first missing implication

The common-plane triangle is now constrained simultaneously by:

- two invertible main legs with fixed `s_min` and determinant;
- a nonzero in-plane `D_1-D_2` edge;
- the exact transported-edge trichotomy (A)/(B)/(C);
- in the diffuse common-K-plane branch, one source-valid three-way partition with six fixed rank-two arms and the improved independent scalar certificate (3.10).

The first remaining implication is therefore

`QFORM-TRIANGLE-TRANSPORTED-SYM-R1-OR-SYMPLECTIC-PAYMENT-v1`:

1. turn chamber (A)'s fixed six-dimensional main-cycle determinant into a product-safe receiver **without** assuming the latent plane coordinates are independent and while retaining all same-bank phases and the nonzero off-plane tail;
2. in chamber (B), spend the fixed rank-one symmetric transported edge together with the two invertible legs;
3. in chamber (C), exploit the fixed alternating scalar `omega`, equivalently the near-symplectic relation between `C_0` and the two leg maps, rather than treating it as generic edge mass;
4. on the diffuse physical three-fan, combine (3.8)-(3.10) with a grouped receiver that keeps same-bank shear and extra spectrum.

The invariant `T=adj(B_1)C_0 adj(B_2)^T` is preferable to a reciprocal-minor choice: it aggregates the entire two-dimensional leg geometry before inversion and has the fixed lower Frobenius mass (2.5).

## 5. What is and is not proved

Proved here:

- exact determinant and rank normal forms (2.3)-(2.4) for the quantitative r36 main cycle;
- the fixed transported mass (2.5) and exhaustive quantitative chambers (A)-(C);
- the sharpened same-partition partner certificate `W_1W_2W_3>=1/72` and joint scalar density cap `<38.029` in the r37 diffuse branch.

Not proved:

- that a nonzero determinant of the latent 6D skeleton alone gives the ambient output-density bound;
- payment of the rank-one-symmetric or symplectic-skew collars;
- the arbitrary-extra-spectrum global splice;
- the unrestricted QFORM conjecture;
- full-target continuity.

The unrestricted quadratic-form bounded-density conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. No new continuity conclusion is claimed in this run.

Deterministic constants were independently recomputed in `CHECKS.py`/`CHECKS.txt` in this immutable run directory (`STATUS=PASS`). Those checks verify arithmetic only; the proof above is analytic.
