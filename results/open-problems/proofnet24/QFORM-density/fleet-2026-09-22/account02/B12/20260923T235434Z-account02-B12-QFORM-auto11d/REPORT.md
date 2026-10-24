# account02/B12 — local column-packet seven-mode hybrid

Run: `20260923T235434Z-account02-B12-QFORM-auto11d`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. First unpaid implication

The target remains: independent ORIGINAL coordinates with scalar densities at most one, symmetric A with at least three eigenvalues of modulus at least one, and a universal essential density bound for X^T A X (or a valid counterexample).

This run does **not** infer a bounded carrier from the bare spectral hypothesis. The live correction `QFORM-GSTAR-SCALE-FORCING-FALSE-v1` rules out that shortcut. The remaining structural debt is to force either a universal-scale bounded ORIGINAL-coordinate carrier of the kind compiled below, or a source-valid projected-crossing / volume / grouped-bank / hub / ridge / physical-pair / Schur exit.

The new result is a genuinely local packet theorem: arbitrary added matrices are charged only through their action on the chosen physical carrier columns. Their global rank and global operator norm may be arbitrarily large.

## 2. Local packet reserve on carrier columns

Let H be a set of m ORIGINAL coordinates and let P_H:R^m -> R^n be the coordinate embedding. Write

A = A_0 + E_1 + ... + E_M + T,

where A,A_0,E_l,T are symmetric and

||T||_op <= delta.

For each packet choose q_l >= 0 and define the **local** tail

eta_l := s_{q_l+1}(E_l P_H),

with eta_l=0 if rank(E_l P_H)<=q_l. Put

Q := sum_l q_l,
eta := sum_l eta_l.

Assume 7+Q <= m and define

g := [ s_{7+Q}(A_0 P_H) - eta - delta ]_+.

### Theorem 2.1 — `QFORM-LOCAL-COLUMN-PACKET-SEVEN-MODE-HYBRID-v1`, reserve part

One has

sqrt(lambda_7((A^2)[H,H])) = s_7(A P_H) >= g.                 (2.1)

#### Proof

For every l take a best rank-q_l singular-value truncation

E_l P_H = R_l + F_l,
rank(R_l)<=q_l,
||F_l||_op=eta_l.

These truncations need not come from symmetric global matrices; that is irrelevant because this step concerns only the actual carrier-column matrix A P_H. Put R=sum R_l and F=sum F_l. Then

rank(R)<=Q,
||F||_op<=eta,

and

A P_H = A_0 P_H + R + F + T P_H.

Rank interlacing gives

s_7(A_0P_H+R) >= s_{7+Q}(A_0P_H),

while Weyl and ||TP_H||<=delta give

s_7(AP_H)
 >= s_{7+Q}(A_0P_H)-eta-delta.

Finally

(AP_H)^T(AP_H)=P_H^T A^2 P_H=(A^2)[H,H].

This proves (2.1). QED.

### Strict localization versus global packet budgets

For every l,

s_{q_l+1}(E_l P_H) <= s_{q_l+1}(E_l),

so (2.1) is never weaker on a fixed carrier than charging the global packet tail. It can be drastically stronger: if E_l P_H=0, that packet costs exactly zero even if E_l has arbitrarily high rank and arbitrarily large norm.

No statement about the size of X^T T X is used. The only dense-tail step is ||TP_H||<=||T||.

## 3. Seven square-energy modes split into a physical core or five cross directions

Write the actual final matrix in the ORIGINAL-coordinate split H union H^c as

A = [[C, B], [B^T, D]],

so

(A^2)[H,H]=C^2+B B^T.

For positive semidefinite matrices, Weyl's upper inequality gives

lambda_{p+q-1}(X+Y) <= lambda_p(X)+lambda_q(Y).

Taking X=C^2, Y=BB^T, p=3 and q=5 yields

lambda_7((A^2)[H,H]) <= s_3(C)^2+s_5(B)^2.                    (3.1)

Combining with (2.1),

s_3(C)^2+s_5(B)^2 >= g^2.                                     (3.2)

This is exactly the receiver split needed by two completed source-valid theorems:

* physical-core receiver: if s_3(C)>=sigma, conditioning only outside the ORIGINAL set H preserves the product law and gives

  ||p_{X^TAX}||_(infinity,ess) <= 2 sqrt(6 pi m)/sigma;

* pinned fifth-volume receiver: if s_5(B)>=tau, then e_5(B^T B)>=tau^10, hence

  ||p_{X^TAX}||_infinity <= 5 sqrt(2e)/tau.

The second receiver has no row-marginal condition and is applied to the **actual final** cross block B.

## 4. Optimized hybrid constant

Put

A_m := 2 sqrt(6 pi m),
B_5 := 5 sqrt(2e).

For any theta in (0,1), (3.2) implies either

s_3(C)>=theta g

or

s_5(B)>=sqrt(1-theta^2) g.

Therefore

||p_{X^TAX}||_(infinity,ess)
 <= (1/g) max{A_m/theta, B_5/sqrt(1-theta^2)}.

The optimal threshold is

theta_* = A_m/sqrt(A_m^2+B_5^2),

for which both branches agree. Hence:

### Theorem 4.1 — optimized local seven-mode hybrid

If g>0, then

boxed:
||p_{X^TAX}||_(infinity,ess)
 <= sqrt(24 pi m + 50 e) / g.                                  (4.1)

This theorem has no moment, support, log-concavity, iid, diagonal-basis, or post-rotation-independence assumption. Continuity is separate from the stability argument.

## 5. Equation-level use of the latest account03/B12 result

The latest compatible account03/B12 report (`r44`) proves a multi-packet fixed-physical-core density theorem. Applied to the **actual final block C** (equivalently, with the final matrix as baseline and zero additional packets), its receiver gives exactly

||p_Q||_(infinity,ess) <= 2 sqrt(6 pi m)/s_3(C).                (5.1)

Thus the self branch in Section 4 is a direct use of the completed partner theorem, not an assumed coarea inequality for an arbitrary rotated joint density.

The same partner report also proves the global column-square packet budget

sqrt(lambda_k((A^2)[H,H]))
 >= [sqrt(lambda_{k+Q}((A_0^2)[H,H]))-Delta]_+,

with Delta=sum s_{q_l+1}(E_l). Section 2 sharpens precisely this step for a fixed physical carrier by replacing each global packet tail with the smaller local tail s_{q_l+1}(E_l P_H).

As a separate concrete r44 application, take an ORIGINAL six-coordinate core with baseline C_0=2I_6, one arbitrary symmetric packet E with q=3 and s_4(E)<=1/4, and a dense symmetric tail ||T||<=1/4. Spending q=3 on E and q=0 on T gives

s_3(C_final) >= s_6(C_0)-1/4-1/4 = 3/2,

so the partner theorem yields the real inequality

boxed:
||p_Q||_(infinity,ess) <= 2 sqrt(36 pi)/(3/2) = 8 sqrt(pi).

The first three signed eigenmodes of E may be arbitrarily large.

## 6. Required pinned e5f result applied at a real inequality

The pinned `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` Fourier route records the fifth-volume extension

||p_Q||_infinity <= 5 sqrt(2e) e_5(B^T B)^(-1/10)              (6.1)

for an actual original-coordinate cross block B, with no marginal condition.

In the cross branch of (3.2),

s_5(B)>=sqrt(1-theta_*^2) g,

and therefore

e_5(B^T B) >= s_5(B)^10
             >= (1-theta_*^2)^5 g^10.

Substituting in (6.1) gives

||p_Q||_infinity
 <= B_5/[sqrt(1-theta_*^2) g]
 = sqrt(24 pi m+50e)/g,

which is exactly the cross half of (4.1). This is an application to the actual final coefficient matrix, not to a rotated product law.

## 7. Exact-target stress family with arbitrary extra spectrum

Take |H|=7 and |J|=4. On H let

C_0=diag(2,2,2,0,0,0,0),

and let B_0 be the 7x4 matrix whose first three rows vanish and whose last four rows form 2I_4. Take D_0=0 on J. Then

C_0^2+B_0B_0^T=4I_7,

so

s_7(A_0P_H)=2.

The carrier spectrum consists of three decoupled +2 modes and four hyperbolic blocks with eigenvalues (+2,-2), hence it has seven +2 eigenvalues and four -2 eigenvalues.

Now append N spectator coordinates with baseline 2I_N and replace that entire degenerate eigenspace by an **arbitrary symmetric matrix Theta**. Equivalently add

S_spec = 0_(H union J) direct-sum (Theta-2I_N).

The number N is arbitrary, Theta may have arbitrary internal mixing, signs and eigenvalue magnitudes, and yet

S_spec P_H=0.

Thus its local packet cost is exactly zero. Finally add any globally dense symmetric T with

||T||_op <= 1/4.

The local theorem gives

g>=2-1/4=7/4.

Therefore every such final form satisfies

boxed:
||p_Q||_(infinity,ess)
 <= sqrt(168 pi+50e)/(7/4)
 = 14.721375903154279....                                      (7.1)

This family remains in the exact owner target class uniformly over N and Theta: before T there are seven +2 carrier eigenvalues, so Weyl leaves at least three final eigenvalues >=7/4>1.

At T=0 the carrier cross block has rank exactly four, so

e_5(B_0^T B_0)=0.

Thus a D5-only proof has no certificate on this family. The three-dimensional physical self block supplies the missing smoothing resource.

A complementary sibling takes

C_0=diag(2,2,0,0,0,0,0)

and puts five orthogonal cross rows of size 2 on rows 3,...,7. It still has carrier square Gram 4I_7, but now s_3(C_0)=0 and s_5(B_0)=2, so the pinned D5 branch—not the three-mode physical core—closes the endpoint. The two receivers are genuinely complementary.

## 8. Seven modes are sharp for the pure two-receiver dichotomy

The number seven in (3.1) cannot be reduced to six if the only exits are `s_3(C)>0` and `s_5(B)>0`.

Indeed, on a six-coordinate H take

C=diag(1,1,0,0,0,0)

and let B have four orthogonal unit cross rows supported on rows 3,...,6. Then

C^2+BB^T=I_6,

so

lambda_6((A^2)[H,H])=1,

but

s_3(C)=0,
s_5(B)=0.

Hence no implication of the form

lambda_6((A^2)[H,H])>0 => [s_3(C)>0 or s_5(B)>0]

can hold. Six modes require a third receiver (for example the physical-pair route developed in earlier B12 work); seven modes are exactly sufficient for the clean core-vs-D5 compiler proved here.

## 9. Dense-tail and provenance controls

The dense tail appears only through

||TP_H||_op<=||T||_op.

There is no assertion that small ||T|| makes X^T T X uniformly small for unbounded inputs. All conditioning is on ORIGINAL coordinates. Matrix SVDs and projections are deterministic coefficient manipulations only; no rotated random coordinate is treated as independent.

The pinned counterexample search reports no counterexample and explicitly warns that arbitrary three-dimensional density coarea is false; the proof above never uses such a statement. Its unresolved configurations include delocalized higher-rank geometry, consistent with the remaining extraction debt here.

## 10. Status

`QFORM-LOCAL-COLUMN-PACKET-SEVEN-MODE-HYBRID-v1` is proved as a supporting theorem. The unrestricted universal conjecture remains OPEN / NOT PROVED / NOT DISPROVED.

The next useful step is structural: show that every exact-target matrix either admits a bounded original-coordinate H with a positive local seven-mode reserve after spending hostile column-packet ranks, or triggers an already-paid volume / projected-crossing / grouped-bank / hub / ridge / physical-pair / Schur exit. The live g-star correction forbids assuming this extraction for free.
