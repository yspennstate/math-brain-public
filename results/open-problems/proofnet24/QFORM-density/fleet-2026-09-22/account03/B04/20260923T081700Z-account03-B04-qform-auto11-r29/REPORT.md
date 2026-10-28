SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-23T08:17:00Z.
attacking: third-compound random-cut product Fourier routing: turn disjoint 3x3 compound mass into an aggregate original-coordinate cross block, then quantify the finite triple-hub complement.

# account03/B04 r29 — third-compound random-cut gate and six-coordinate compound-hub alternative

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Product Fourier rearrangement  
Status: `NEW SUPPORTING THEOREM / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN`.

The full conjecture is not proved here. The result below supplies a dimension-free product-Fourier exit whenever a positive fraction of the global third compound of the full symmetric matrix is carried by disjoint physical row/column triples. If that exit fails, the failure is converted into a concrete finite physical obstruction: either global third-compound mass is concentrated on overlapping row/column triples, or a selected cross cut has more than `1-2 tau` of its third-volume mass forced to meet one fixed row triple and one fixed column triple.

No pointwise law-uniform quadratic-phase decay, arbitrary-joint coarea estimate, post-rotation independence, moment hypothesis, compact support, connected support, log-concavity, selected-small-minor reciprocal, or Monte Carlo evidence is used.

## 1. Completed peer result actually applied

The designated partner is `account04/B04`. A fresh lookup found no completed current-QFORM canonical report or shared handoff for that slot, so no designated-partner theorem is invented.

The completed peer result actually applied is the global third-volume product-Fourier theorem of account03/B02 together with the exact KL-halving improvement recorded by account01/B04. An immutable source snapshot containing both is:

- repository `yspennstate/math-open-problems`, commit `00c845c9d1dad964da3c22f7e516db277a516db3`;
- B02 path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T043653Z-account03-B02-qform-r20/REPORT.md`;
- B04 improvement path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260923T055035Z-account01-B04-QFORM-auto13/REPORT.md`.

Its scope is the following. Let `I,J` be disjoint ORIGINAL-coordinate banks, condition arbitrary outside original coordinates, and write

`Q=F(X_I)+2 X_I^T M X_J+G(X_J)`,

with arbitrary within-bank quadratic/affine terms retained. Put

`Z=E_3(M)=e_3(M^T M)=sum_{|S|=|T|=3} det(M[S,T])^2`.

Let the canonical row-triple law have weights proportional to the squared minors, and let `delta_r` be the probability that two iid row triples from that law are disjoint. Define `delta_c` analogously after transposition. If `delta=max(delta_r,delta_c)>0`, the completed Fourier argument plus the KL-halving identity gives a continuous `C_0` density with

`||p_Q||_infinity <= 3 e delta^(-1/12) Z^(-1/6)`.              (1.1)

The same source proves the exact residual-volume identity

`delta_r = E_{S}[ E_3(M[S^c,J])/Z ]`,                           (1.2)

and its column-transposed analogue. Equation (1.1) is the peer inequality used below.

## 2. Global third compound and disjoint physical mass

For an arbitrary real symmetric `n x n` matrix `A`, define

`E_3(A)=e_3(A^T A)
      =sum_{|I|=|J|=3} det(A[I,J])^2`.                          (2.1)

Because `A` is symmetric, its singular values are the absolute eigenvalues. Hence the target hypothesis that at least three eigenvalues have modulus at least one implies immediately

`E_3(A)>=1`.                                                     (2.2)

Define the **disjoint third-compound mass**

`D_0(A)=sum_{|I|=|J|=3, I cap J=empty} det(A[I,J])^2`,          (2.3)

and its normalized fraction

`omega(A)=D_0(A)/E_3(A) in [0,1]`.                              (2.4)

This quantity is basis-physical: the triples are subsets of the original independent coordinates. No spectral rotation is performed.

## 3. Random-cut identity

Choose a random bipartition `[n]=L sqcup R` by independent fair coins and let

`M_L=A[L,R]`.                                                    (3.1)

### Lemma 3.1 — exact third-compound cut average

`E_L E_3(M_L)=D_0(A)/64`.                                       (3.2)

### Proof

Expand

`E_3(M_L)=sum_{I subset L, J subset R, |I|=|J|=3}
             det(A[I,J])^2`.

For fixed physical triples `(I,J)`, the event `I subset L` and `J subset R` is impossible if `I cap J` is nonempty. If they are disjoint, it fixes the side of six distinct coordinates and has probability `2^(-6)=1/64`. Taking expectation termwise gives (3.2). QED.

Therefore there exists an actual physical cut `L|R` satisfying

`Z_L:=E_3(A[L,R])
 >=D_0(A)/64
 =omega(A) E_3(A)/64`.                                         (3.3)

No local minor is selected or inverted.

## 4. Main theorem — `QFORM-THIRDCOMPOUND-RANDOMCUT-GATE-v1`

Let `A` be any real symmetric matrix and let `X` have independent one-dimensional densities bounded by one. Assume `E_3(A)>0`. Put `omega=D_0(A)/E_3(A)`. If `omega>0`, choose a physical cut `L|R` satisfying (3.3), set `M=A[L,R]`, and let `delta_r,delta_c` be its canonical determinant-weighted row/column triple disjointness probabilities. Put

`delta=max(delta_r,delta_c)`.

If `delta>0`, then `Q=X^T A X` has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= 6 e omega^(-1/6) delta^(-1/12) E_3(A)^(-1/6).`              (4.1)

Under the target hypothesis of three eigenvalues of modulus at least one, (2.2) simplifies this to

`boxed:
 ||p_Q||_infinity
 <= 6 e omega^(-1/6) delta^(-1/12).`                            (4.2)

### Proof

Condition on all original coordinates outside `L union R` (there are none for a bipartition, but this wording shows the compatibility with ambient conditioning). The full form has the exact peer-theorem shape

`Q=F(X_L)+2 X_L^T M X_R+G(X_R)`,                                (4.3)

where both same-bank quadratic blocks remain arbitrary. If `delta_r>=delta_c`, apply (1.1) to `M`; otherwise apply it to `M^T`. Thus

`||p_Q||_infinity <=3 e delta^(-1/12) Z_L^(-1/6)`.             (4.4)

From (3.3),

`Z_L^(-1/6)
 <=64^(1/6) omega^(-1/6) E_3(A)^(-1/6)
 =2 omega^(-1/6) E_3(A)^(-1/6)`.                               (4.5)

Substituting (4.5) into (4.4) gives (4.1). The peer Fourier proof has an `L^1` characteristic function, so its continuous-`C_0` conclusion is inherited. QED.

### Explicit threshold corollary

For any `eta,tau in (0,1)`, if

`omega>=eta`, `delta>=tau`,                                     (4.6)

then, in the full target scope,

`||p_Q||_infinity <=6e eta^(-1/6) tau^(-1/12)`.                (4.7)

At the concrete symmetric choice

`eta=tau=1/16`,                                                  (4.8)

one has `eta^(-1/6)tau^(-1/12)=16^(1/4)=2`, hence

`boxed: ||p_Q||_infinity <=12e
       =32.61938194150854... .`                                 (4.9)

This is a full ambient theorem under the two explicit third-compound gates; it is not the unrestricted conjecture.

## 5. Exact structural complement: a six-coordinate compound hub

The same argument gives a useful finite obstruction when the Fourier gate does not fire.

Fix `eta,tau in (0,1/2)`. Under the full target hypothesis, exactly one of the following holds:

1. **global overlap:** `omega<eta`, so more than `1-eta` of the global third-compound mass is carried by physical triple pairs `(I,J)` with `I cap J != empty`;
2. **Fourier exit:** there is a physical cut `L|R` with (3.3) and `max(delta_r,delta_c)>=tau`, hence (4.7);
3. **triple-hub residue:** there is a physical cut `L|R` with (3.3), a row triple `S subset L`, and a column triple `T subset R`, such that more than `1-2tau` of the cross third-volume `Z_L` is carried by minors whose row triple intersects `S` **and** whose column triple intersects `T`.

### Proof of the third alternative

Assume `omega>=eta`, choose the cut from (3.3), and suppose both `delta_r<tau` and `delta_c<tau`. By the exact residual identity (1.2), some row triple `S` satisfies

`E_3(M[S^c,R])<tau Z_L`.                                       (5.1)

Equivalently, under the canonical full `3x3` minor law, the probability that the row triple is disjoint from `S` is `<tau`; hence the probability it intersects `S` is `>1-tau`.

Apply the transposed identity to obtain a column triple `T` for which the canonical minor's column triple intersects `T` with probability `>1-tau`. A union bound then gives

`P{row triple intersects S AND column triple intersects T}
 >1-2tau`.                                                       (5.2)

This proves the residue claim. QED.

For `eta=tau=1/16`, failure of the `12e` Fourier gate therefore produces either

- more than `15/16` of global `E_3(A)` on overlapping physical row/column triples, or
- a cut carrying at least `E_3(A)/1024` of third volume for which more than `7/8` of that cross volume meets one fixed three-row set and one fixed three-column set.

Thus the diffuse third-compound part is now paid by a continuous-density Fourier estimate. The unpaid branch is finite-hub/overlap geometry, not a generic delocalized cloud.

## 6. Genuinely rotated indefinite family with vanishing physical coefficients

The theorem gives an explicit uniform estimate on a target-valid family in which every active physical cross coefficient tends to zero.

Let `m>=2`. Index `3m` rows by pairs `(a,r)`, with `a in {1,2,3}` and `1<=r<=m`, and define the `3m x 3` isometry `U_m` by

`row_(a,r)(U_m)=e_a^T/sqrt(m)`,                                 (6.1)

so `U_m^T U_m=I_3`.

Let

`R=I_3-(2/3) 11^T
  =(1/3) [[1,-2,-2],[-2,1,-2],[-2,-2,1]]`.                     (6.2)

`R` is a symmetric orthogonal Householder matrix, with eigenvalues `1,1,-1`; every entry is nonzero. Put

`M_m=U_m R U_m^T`,                                              (6.3)

and on two disjoint `3m`-coordinate product banks set

`A_m=[[0,M_m],[M_m^T,0]]`.                                     (6.4)

Then `M_m` has exactly three nonzero singular values, all equal to one. Therefore

`spec(A_m)={+1,+1,+1,-1,-1,-1,0,...,0}`.                       (6.5)

So `A_m` is genuinely indefinite and satisfies the exact target spectral hypothesis with six large eigenvalues. Every physical cross coefficient equals either `1/(3m)` or `-2/(3m)`, hence is nonzero and tends to zero with `m`.

Moreover

`E_3(M_m)=1`.                                                    (6.6)

A physical row triple has nonzero determinant exactly when it picks one row from each of the three `m`-element groups, and then `|det U_m[S,:]|=m^(-3/2)`. Since `|det R|=1`, every nonzero squared `3x3` minor of `M_m` equals `m^(-6)`. Consequently the canonical row and column triple laws are each uniform on the `m^3` choices selecting one coordinate from each group.

Two iid canonical triples are disjoint exactly when, independently in each group, their selected coordinates differ. Hence

`delta_r=delta_c=((m-1)/m)^3`.                                 (6.7)

Applying the completed peer inequality (1.1) at this actual matrix gives, for every admissible product input law,

`boxed:
 ||p_{X^T A_m X}||_infinity
 <=3e (1-1/m)^(-1/4).`                                         (6.8)

In particular, for every `m>=2`,

`boxed:
 ||p_{X^T A_m X}||_infinity
 <=3e 2^(1/4)
 =9.697800272958307... .`                                       (6.9)

The bound tends to

`3e=8.154845485377136...`                                       (6.10)

as `m` tends to infinity. The density is continuous and vanishes at infinity. This is aggregate-before-inversion control on a rotated indefinite family whose individual active physical coefficients are `O(1/m)`.

## 7. What is closed and what remains open

This run closes one structural/Fourier interface:

- the bare three-large-eigenvalue hypothesis always provides global third-compound currency `E_3(A)>=1`;
- a random physical coordinate cut captures exactly one sixty-fourth of the **disjoint** portion in expectation;
- a determinant-weighted triple-disjointness gate then converts that currency directly into the completed integrated product-Fourier theorem;
- simultaneous failure of row and column disjointness localizes more than `1-2tau` of the selected cross third-volume onto a fixed three-row / three-column hitting pattern.

It does **not** show that `omega` or `delta` is universally bounded below. The next precise B04 obligation is therefore

`QFORM-THIRDCOMPOUND-OVERLAP-OR-TRIPLEHUB-TO-PAID-ENDPOINT-v1`:

> Starting from either (i) global third-compound overlap `D_0/E_3<eta`, or (ii) the six-coordinate compound-hub residue of Section 5, route the matrix into an already-paid scalar/pair/star/grouped-bank/ridge/local-3block endpoint with dimension-free currency, without selecting a vanishing local minor; otherwise obtain a stronger compound-order inequality that forces the Fourier exit.

Full QFORM remains **OPEN**. Full-target continuity remains **OPEN**. The theorem in Section 4 and the family in Section 6 do prove continuity in their stated scopes.

## 8. Correction, partner, and source ledger

Consumed and respected: law-uniform pointwise quadratic-phase decay is false; arbitrary-joint rank-three coarea is false; positive conditional projection moments can diverge; rotations do not preserve independence; bounded projection density alone does not control an indefinite quadratic pushforward; naive fiber-sup integration loses dimension; local cross-rank-three or one-minor extraction is not automatic.

Designated partner `account04/B04`: no completed current-QFORM report/handoff visible at the final preproof lookup, so none was fabricated. Completed peer theorem actually applied: account03/B02 plus account01/B04's KL-halving improvement, both source-pinned in Section 1.

Native learned-memory ingestion was not authenticated or receiver-verified. Repository retrieval and writes are therefore recorded as `WITHOUT_VERIFIED_BRAIN`.

Model self-report: `GPT-5.6 Sol`.  
Configured reasoning level: `UNKNOWN_NOT_EXPOSED`.  
Provider reasoning tokens/thinking time: `NOT_EXPOSED`.
