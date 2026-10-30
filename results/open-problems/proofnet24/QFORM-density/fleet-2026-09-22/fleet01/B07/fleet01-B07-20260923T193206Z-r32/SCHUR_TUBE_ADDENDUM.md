# r32 addendum — aggregate swapped-E3 payment or a physical four-hub Schur tube

This strengthens the main/correction dichotomy in `REPORT.md`. It uses exactly the same physical-coordinate notation and no new probabilistic premise.

## The parameterized theorem

Let `A` be real symmetric, `L,R` disjoint physical coordinate banks, `K=A[L,R]`, and

`Omega=e2(KK^T)>0`.

For the complete physical E2 determinant law

`w_(I,J)=det(K[I,J])^2/Omega`, `|I|=|J|=2`,

write row and column inclusion marginals `alpha_c`, `beta_r`. Fix `a,b>=0` with

`delta:=1-a-b>0`.

For each physical E2 anchor `(I,J)`, put

`B=K[I,J]`, `d=det B`,

`K_res=K[L\I,R\J]`,

`X=A[R\J,J]`, `Y=A[I,L\I]`.

The swapped disjoint E3 packet attached to this anchor is

`H_(I,J)
 =sum_(c in L\I,r in R\J)
   det A[I union {r},J union {c}]^2`.

As in the main report, if `d!=0`, the bordered determinant identity gives the exact factorization

`H_(I,J)
 =d^2 ||K_res-X B^(-1)Y||_F^2`.                                (A.1)

Define also

`M_(I,J)=d^2||K_res||_F^2`,
`H=sum H_(I,J)`, `M=sum M_(I,J)`.

The determinant-law exclusion identity gives

`M
 =Omega sum_(c,r)K_(c,r)^2 P_w(c notin I,r notin J)`.

Hence, if `max alpha_c<=a` and `max beta_r<=b`,

`M>=delta Omega ||K||_F^2`.                                     (A.2)

### Theorem — `QFORM-E2-DIFFUSE-CROSSPAY-OR-FOURHUB-SCHUR-TUBE-v1`

For every `0<epsilon<1`, at least one of the following holds.

1. **Physical determinant hub.** `max alpha_c>a` or `max beta_r>b`.

2. **Continuous cross-E3 payment.** The full ambient form has a continuous `C0` density satisfying

`boxed:
||p_Q||_infinity
 <= C_E3 [epsilon^2 delta Omega ||K||_F^2/64]^(-1/6),`            (A.3)

where `C_E3=3*2^(4/3)*exp(1/3)` is the completed marginal-free physical cross-E3 constant.

3. **Physical four-hub relative Schur tube.** There is one actual original-coordinate cross pivot `B=K[I,J]` with `det B!=0` and `K_res!=0` for which

`boxed:
||K_res-XB^(-1)Y||_F
 < epsilon ||K_res||_F.`                                        (A.4)

In particular the actual residual cross block lies within relative Frobenius error `epsilon` of a matrix of rank at most two whose left and right factors are the TRUE same-bank couplings to the four physical pivot coordinates. No small coefficient tail is deleted from the quadratic form.

#### Proof

Assume branch 1 fails. Then (A.2) holds.

If `H>=epsilon^2 M`, every determinant in `H` has a row triple and column triple that are disjoint physical coordinate sets. A random two-colouring of the original coordinates retains any such ordered pair of triples as opposite colour classes with probability `2^-6=1/64`. Therefore one deterministic colouring gives a literal disjoint physical cross block with complete E3 mass

`V3>=H/64>=epsilon^2 delta Omega||K||_F^2/64`.

The completed marginal-free cross-E3 theorem gives (A.3), including continuity.

Otherwise `H<epsilon^2 M`. Since `M=sum M_(I,J)>0`, some anchor with `M_(I,J)>0` obeys

`H_(I,J)<epsilon^2 M_(I,J)`.

Here `M_(I,J)>0` implies both `d!=0` and `K_res!=0`. Divide (A.1) by `d^2` to obtain (A.4). The approximant `XB^(-1)Y` has rank at most two. QED.

The role of the determinant weights is essential: the pivot is selected only after comparing the aggregate sums `H=sum d^2||Schur residual||_F^2` and `M=sum d^2||raw residual||_F^2`. No density bound is inferred from the selected pivot's reciprocal determinant.

## Symmetric 2/5 specialization

Take

`a=b=2/5`, `delta=1/5`.

Then either there is a physical E2 determinant hub of marginal `>2/5` (at most four on either side), or for every prescribed `0<epsilon<1` one has the alternative

`||p_Q||_infinity
 <= C_E3 [epsilon^2 Omega||K||_F^2/320]^(-1/6)`

continuously, or a physical four-hub Schur tube (A.4).

Using `||K||_F^2>=sqrt(2Omega)`, the payment branch becomes

`boxed:
||p_Q||_infinity
 <= C_E3 [epsilon^2 sqrt(2) Omega^(3/2)/320]^(-1/6).`            (A.5)

At `epsilon=1/2` this is the `<928335.929` partner-scale payment recorded in the main report.

## Application to the designated partner

For fleet02/B07's completed block

`Omega=Z>Z0 h^4`,
`Z0=854675.100194511`,
`h=(2sqrt(2)-1)/1572864`,

(A.5) gives, for arbitrary `epsilon`,

`||p_Q||_infinity
 < 928335.929 (2epsilon)^(-1/3)`

in the continuous-payment branch.

Otherwise the partner's actual rough-tail block has either a physical E2 determinant hub of marginal `>2/5`, or—after removing four actual original coordinates—it admits the dependence-safe coefficient identity

`K[L\I,R\J]
 =A[R\J,J] K[I,J]^(-1) A[I,L\I] + S`,

`||S||_F<epsilon ||K[L\I,R\J]||_F`.                            (A.6)

The first term has rank at most two and is built entirely from same-bank couplings to the selected physical pivot. This converts the former unstructured rough-tail obstruction into a tunably accurate four-hub rank-two coefficient tube. The true nonzero `S` remains in the quadratic form and is not treated as a small random error.

The next receiver should combine (A.6) with either (i) physical support concentration of the two hub-generated factors, feeding a finite original-coordinate core, or (ii) support diffusion, feeding the hub/Fresnel machinery. The exact-rank-at-most-one face remains separate. Full QFORM and global continuity remain open.
