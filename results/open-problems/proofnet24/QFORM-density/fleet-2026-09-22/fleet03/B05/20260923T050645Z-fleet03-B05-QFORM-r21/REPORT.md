SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B05, 2026-09-23T05:06:45Z.
attacking: QFORM-INTERPACKET-CURVATURE-COAREA-v1 — identify the exact global curvature that survives three locally good physical quadratic packets after arbitrary bilinear interpacket coupling.

# fleet03/B05 r21 — interpacket curvature can cancel; third global curvature is the missing coarea factor

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Status: **EXACT_INTERMEDIATE_OBSTRUCTION + STRUCTURAL_ESCAPE_LEMMA + SCOPED_GLOBAL-CURVATURE EXIT / FULL QFORM OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.  
Continuity: proved for the explicit target-valid stress family; not proved for the full target.

## 1. Fresh source state and exact predecessor


The immediately preceding B05 theorem is

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260923T044412Z-fleet03-B05-QFORM-r21/REPORT.md`.

It proves that every two-original-coordinate quadratic packet

`F=aX^2+2bXY+cY^2+alpha X+beta Y+gamma`

with independent cap-one `X,Y` has

`||p_F||_(3/2) <= 20 m^(-1/3),   m=max(|a|,|b|,|c|)>0`,

and hence three **disjoint** two-coordinate packets with no live quadratic coupling between the packets give an `L^infinity` output bound by three-factor Young. Its exact remaining debt was whether this endpoint survives arbitrary interpacket bilinear curvature.

It does not. The first essential implication fails in a sharp way even inside a matrix satisfying the full three-large-eigenvalue spectral hypothesis.

## 2. Exact cancellation example: three perfect local indefinite packets collapse to global rank two

Let

`x_1,x_2,x_3,y_1,y_2,y_3,z`

be mutually independent `Uniform[-1/2,1/2]`, and group the first six coordinates into three physical packets

`P_j=(x_j,y_j),  j=1,2,3`.

Define

`S=x_1+x_2+x_3`,  `T=y_1+y_2+y_3`,

and first consider

`Q_0=S^2-T^2`.                                                    (2.1)

In the packet ordering `(x_1,y_1,x_2,y_2,x_3,y_3)`, every diagonal `2 x 2` packet block is exactly

`B_j=diag(1,-1)`.                                                   (2.2)

Thus for **every** packet

`|det B_j|=1`, `sigma_min(B_j)=1`, and `max_{a,b in P_j}|A_ab|=1`. (2.3)

The off-diagonal packet-packet blocks are also `diag(1,-1)`. In the equivalent ordering `(x_1,x_2,x_3,y_1,y_2,y_3)`, the full active matrix is

`M_0 = J_3 direct_sum (-J_3)`,                                     (2.4)

where `J_3` is the all-ones `3 x 3` matrix. Therefore

`spectrum(M_0)={3,-3,0,0,0,0}`.                                   (2.5)

So three perfectly conditioned local rank-two indefinite curvature packets can be cancelled by interpacket couplings until only **two global quadratic directions** remain.

This already proves that no extension of the preceding three-packet theorem can depend only on the three local quantities `(m_j, |det B_j|, sigma_min(B_j))` while allowing arbitrary interpacket bilinear blocks.

## 3. The resulting global density is genuinely unbounded

The sum of three independent `Uniform[-1/2,1/2]` variables has density

`h(s)=3/4-s^2,   |s|<=1/2`.                                        (3.1)

In particular,

`h(s)>=1/2` on `[-1/2,1/2]`.                                       (3.2)

The variables `S,T` are independent. Introduce

`u=S+T`, `v=S-T`.

Their joint density is

`k(u,v)=1/2 h((u+v)/2) h((u-v)/2)`.                                (3.3)

If `|u|<=1/2` and `|v|<=1/2`, then both arguments in (3.3) have modulus at most `1/2`, hence

`k(u,v)>=1/8`.                                                       (3.4)

Since

`Q_0=(S+T)(S-T)=uv`,                                                (3.5)

the standard product coarea formula gives, for a.e. `q != 0`,

`p_{Q_0}(q)= integral_R k(u,q/u) du/|u|`.                            (3.6)

For `0<|q|<1/4`, restrict (3.6) to the one-sided interval

`2|q| <= u <= 1/2`.

Then `|u|<=1/2` and `|q/u|<=1/2`, so (3.4) applies. Therefore

`p_{Q_0}(q)
 >= (1/8) integral_{2|q|}^{1/2} du/u
 = (1/8) log(1/(4|q|)).`                                           (3.7)

Consequently

`boxed( ||p_{Q_0}||_infinity = infinity ).`                         (3.8)

This is the exact rank-two hyperbolic logarithm. It arises even though every one of the three physical packet blocks in (2.2) is maximally well conditioned.

A useful analytic corollary is that **uniform conditional packet smoothing does not tensorize through arbitrary bilinear interpacket couplings**. Conditional on all coordinates outside any one `P_j`, the quadratic coefficient on that packet is still exactly `diag(1,-1)`, so the preceding B05 packet theorem gives the same uniform `L^(3/2)` conditional bound. Nevertheless (3.8) holds. The missing resource is therefore not repaired by applying the same local finite-`p` packet estimate three times while retaining the couplings.

## 4. Target-valid embedding: conditioning away the outside third direction destroys the theorem

Now restore the seventh independent coordinate and set

`Q=Q_0+z^2 = S^2-T^2+z^2`.                                        (4.1)

The full quadratic matrix is

`A = J_3 direct_sum (-J_3) direct_sum [1]`,                         (4.2)

so

`spectrum(A)={3,-3,1,0,0,0,0}`.                                   (4.3)

Thus (4.1) satisfies the **exact full spectral hypothesis**: it has three eigenvalues of absolute value at least one.

However, conditioning on the outside coordinate `z` leaves the translate `Q_0+z^2`, whose conditional density is logarithmically unbounded by (3.7) for every fixed `z`. Hence the following proof interface is false even on a target-valid matrix:

> select three locally good physical quadratic packets, condition every remaining original coordinate, and then bound the conditional output using only the local packet curvature parameters.

The third large spectral direction can live precisely in the variables that this conditioning discards.

This is **not** a counterexample to QFORM. In fact the same family is uniformly easy once the outside resource is kept. The aggregate scalars `S,T,z` are independent and

`||p_S||_infinity=3/4`, `||p_z||_infinity=1`.                       (4.4)

The usual square-density envelope gives

`p_{S^2}(r)<= (3/4) r^(-1/2)`, `p_{z^2}(r)<=r^(-1/2)`, `r>0`.       (4.5)

Therefore the beta integral gives

`||p_{S^2+z^2}||_infinity <= 3 pi/4`.                              (4.6)

Convolution with the independent `-T^2` cannot increase the supremum, so

`boxed( ||p_Q||_infinity <= 3 pi/4 ).`                              (4.7)

Moreover each of the three square outputs has an `L^(3/2)` density; convolving two gives an `L^3` density and convolving the third gives a `C_0` representative by the standard `L^3 * L^(3/2)` translation-continuity theorem. Thus this particular target-valid stress family has a continuous bounded density even though every conditional density after freezing `z` is unbounded.

This is a concrete instance where **averaging an unbounded moving conditional singularity is essential**.

## 5. Global packet-union curvature is a complete scoped exit

The obstruction suggests the right quantity immediately: do not pay the three diagonal packet blocks separately; pay the third singular direction of their **entire union after all interpacket couplings are included**.

### Proposition 5.1 — six-coordinate global-curvature gate

Let `P` be any set of six original coordinates and let

`M=A_{P,P}`.

Assume

`s_3(M)>=s>0`.                                                       (5.1)

Then, for arbitrary coefficients on the complementary coordinates and arbitrary cross couplings between `P` and its complement,

`boxed(
 ||p_{X^T A X}||_infinity
 <= [1500(8+log 6)]/s.
)`                                                                    (5.2)

Only essential boundedness is asserted here.

### Proof

Condition on all original coordinates outside `P`. The six coordinates in `P` remain independent and cap one; every outside cross term becomes only an affine term in those six coordinates. Their homogeneous quadratic matrix remains exactly `M`.

The completed fixed-dimensional geometric theorem in

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/GEOMETRIC_ROUTE_REPORT.md`

states that for dimension `d`, any real symmetric quadratic matrix with three eigenvalues of modulus at least one, arbitrary affine terms, and independent cap-one inputs has density at most

`250 d (8+log d)`.

Apply it at `d=6` to `M/s`; scaling the scalar output back by `s` multiplies the density supremum by `1/s`. Thus every conditional law is bounded by (5.2), uniformly in the conditioned coordinates. Average the interval inequality over the complement. QED.

This proposition is not claimed as a new proof of the fixed-dimensional theorem. Its role here is to identify a clean **global union gate**: arbitrary interpacket curvature is already harmless whenever the union retains a dimension-free third singular value.

For the cancellation matrix (2.4), `s_3(M_0)=0`, exactly as required by the obstruction.

## 6. If the union loses the third direction, full-target curvature must escape outside it

The remaining small-`s_3(M)` regime has a deterministic structural consequence that is useful for the next coarea step.

### Lemma 6.1 — escaped third-curvature lemma

Write the full target matrix relative to the six-coordinate set `P` as

`A = [[M,C],[C^T,D]]`.                                               (6.1)

Assume

`s_3(A)>=1`, `s_3(M)=epsilon<1`.                                    (6.2)

Then

`boxed( ||C||_op + ||D||_op >= 1-epsilon )`,                         (6.3)

and hence

`boxed( max(||C||_op,||D||_op) >= (1-epsilon)/2 ).`                  (6.4)

In particular, if `epsilon<=1/2`, then at least one of the outside-coupling or outside-self resources has operator norm at least `1/4`.

### Proof

Let `M_2` be a best symmetric rank-two spectral truncation of `M`. Then

`rank(M_2)<=2`, `||M-M_2||_op=epsilon`.                              (6.5)

Set

`A_2 = diag(M_2,0)`.

Since `rank(A_2)<=2`, Eckart-Young and `s_3(A)>=1` imply

`||A-A_2||_op >= 1`.                                                 (6.6)

But

`A-A_2 = diag(M-M_2,0) + E_out`,

where

`E_out=[[0,C],[C^T,D]]`.                                             (6.7)

Thus by (6.5)-(6.6),

`||E_out||_op >= 1-epsilon`.                                        (6.8)

Finally

`E_out=[[0,C],[C^T,0]] + diag(0,D)`,

and

`||[[0,C],[C^T,0]]||_op=||C||_op`.                                  (6.9)

The triangle inequality gives (6.3), then (6.4). QED.

This is only a structural lemma: for arbitrary unbounded product inputs, a large matrix operator norm cannot simply be declared a bounded random perturbation. It does, however, locate the third curvature that the local-packet proof lost. In the explicit stress family (4.2), `epsilon=0`, `C=0`, and `D=[1]`: the entire missing third direction is the outside square `z^2`, exactly matching the direct proof (4.6)-(4.7).

## 7. Required designated-partner use on the actual stress family

The designated partner `fleet04/B05` has the completed theorem at

`yspennstate/math-open-problems@59c6ff7db9aceb8b575abe0e064ebeda06f6f77f:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B05/20260923T041255Z-fleet04-B05-dominant-slope-r2/REPORT.md`.

Its exact-slope theorem gives

`||p_Q||_infinity < 51.6 (mu m_*)^(-1/3)`                           (7.1)

in its product-preserving normal form.

Apply it to (4.1) as follows. In the first original-coordinate bank `(x_1,x_2,x_3)`, take the orthonormal coefficient columns

`u=(1,1,1)/sqrt(3)`,
`t=(1,1,-2)/sqrt(6)`.                                                (7.2)

Let

`U=u dot x=S/sqrt(3)`, `R=t dot x`,
`Y=T/sqrt(3)`, `Z=z`.                                                (7.3)

The full form is

`Q=3U^2-3Y^2+Z^2`,                                                   (7.4)

so in the partner normal form the scalar-pair block on `(Y,Z)` is

`B=diag(-3,1)`, `|det B|=3`,                                        (7.5)

and the first-bank Schur remainder is exactly

`lambda e_1e_1^T`, `lambda=3`.                                      (7.6)

Hence

`mu=|det B| |lambda|=9`.                                             (7.7)

The physical ratios `t_i/u_i` are

`1/sqrt(2), 1/sqrt(2), -sqrt(2)`.                                   (7.8)

Thus the dominant exact-slope class is `{1,2}` and

`m_*=u_1^2+u_2^2=2/3`.                                               (7.9)

Substitution into the **completed partner theorem** gives the actual full-line inequality

`boxed(
 ||p_Q||_infinity
 < 51.6 (9*2/3)^(-1/3)
 = 51.6 * 6^(-1/3)
 < 28.40.
)`                                                                    (7.10)

The direct beta argument (4.7) is much sharper, but (7.10) is important structurally: once the escaped outside scalar `z` is kept rather than conditioned away, the designated partner's product-preserving exact-slope mechanism pays the same target-valid configuration without requiring independence of rotated eigen-coordinates.

## 8. What changed in the proof map

The previous debt was phrased as “retain the three `L^(3/2)` packet resources under interpacket quadratic coupling.” The example above proves that this formulation is too weak: the three local packet resources can cancel to global rank two.

The corrected B05 obligation is:

`QFORM-INTERPACKET-ESCAPED-THIRD-CURVATURE-COAREA-v1`.

A successful theorem must do one of two things **before** a reciprocal Jacobian or conditional-density supremum is taken:

1. retain a quantitative third global singular/volume direction of the full active packet union (Proposition 5.1 pays this branch); or
2. when that direction collapses, retain the quantitatively escaped outside resource supplied by Lemma 6.1 and couple it to the two surviving curved directions using original-coordinate product provenance.

The still-unpaid implication is probabilistic, not linear algebraic: from the alternative

`||C||_op >= (1-epsilon)/2` or `||D||_op >= (1-epsilon)/2`,

route the large outside resource into a physical hub/cross-bank/pivot/grouped-coordinate coarea estimate **without** treating coefficient-smallness/value-smallness as interchangeable and without conditioning away the resource. The stress family shows exactly why this must be done jointly.

No claim in this run proves N3 or the unrestricted QFORM conjecture. No counterexample to QFORM was found.

## 9. Integrity and scope checks

- Every stochastic independence assertion concerns disjoint sets of original independent coordinates.
- No Gaussianity, moments, compact support in the theorem statement, log-concavity, connected support, or diagonalization-independence assumption is introduced. Compact uniforms are used only for the explicit intermediate-mechanism counterexample.
- The obstruction is target-valid after adding `z^2`; it refutes the **conditioning/local-packet proof interface**, not the conjecture.
- The six-coordinate gate uses an already-completed fixed-dimensional theorem at its stated scope.
- Lemma 6.1 is purely spectral and makes no probabilistic conclusion from a matrix norm alone.
- The designated fleet04/B05 result is applied at equations (7.5)-(7.10), not merely cited.
- Full essential boundedness target: OPEN.
- Full continuous-density target: OPEN separately.
