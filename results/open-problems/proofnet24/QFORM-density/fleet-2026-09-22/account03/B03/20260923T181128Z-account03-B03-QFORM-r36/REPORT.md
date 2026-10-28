SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T18:11:28Z.
attacking: switch from the repeated near-coloop physical-pivot mechanism to the fresh arbitrary-internal-function crossing theorem; derive a dependence-safe effective-dimension Riesz integral, apply it to the actual square-plus-hyperbola survivor, and identify exactly why the new projected-crossing extension remains at the critical dimension two there.

# account03/B03 r36 — effective-dimension Riesz compiler and exact rank-two crossing of the angular packet

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Status:** `NEW SUPPORTING THEOREM / MECHANISM SWITCH / WHOLE ANGULAR PACKET GETS A LEVERAGE-FREE L2 + HALF-RIESZ CERTIFICATE / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem remains open. The full continuity conclusion remains open. This run deliberately changes mechanism after the sequence of physical-pivot/near-coloop runs: it treats the relevant packet as a literal original-coordinate crossing with arbitrary internal functions and extracts the exact effective-time dimension before selecting any fragile physical minor.

No law-uniform pointwise quadratic van-der-Corput estimate, no post-rotation independence, no conditional cap for a conjugate sum/difference, no arbitrary-joint coarea lemma, and no deletion of a small random quadratic tail is used.

## 1. Fresh sources actually consumed


2. Fresh projected crossing source:

`yspennstate/math-open-problems:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

The exact-rank crossing theorem used below allows arbitrary measurable internal functions on both physical sides. If a physical cross block has exact rank `r`, nonzero singular values `s_1,...,s_r`, and the corresponding orthogonal product projections have density caps `M_X,M_Y`, then

`|phi(t)| <= min{1, (pi/|t|)^(r/2) (M_X M_Y)^(1/2) (s_1...s_r)^(-1/2)}.`       (1.1)

The same source supplies the grouped projected-crossing theorem with effective dimension `d=k+ell` and explicitly records that `d>2` is the one-copy Fourier-inversion threshold.

3. Incoming exact packet and preceding endpoint work are account03/B03 r27, r34, and the two r35 reports. The packet retained here is

`Q = a^(-1) H^2 + 2 sigma U V`,                                     (1.2)

`H = a X_i + h_L.X_L + h_R.X_R + h_K.X_K`,
`U=u.X_L`, `V=v.X_R`,                                                (1.3)

`h_R=beta v+m q`, `q perpendicular v`, `||q||=||v||=1`, `m>0`.      (1.4)

The banks are disjoint original-coordinate product banks and `u` is unit. The source packet also has

`m=rho y`, `y^2>1/2`, and `|sigma| rho^2/|a| >= s_3(A)^2`,           (1.5)

but the first theorem below does not need the heavy-row or angular-cancellation hypotheses at all.

4. Designated partner `account04/B03`, canonical source

`yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260922T193150Z-account04-B03-collision-l2-r1/REPORT.md`.

Only its elementary valid implication

`P(|Y-Y'|<=eps) <= 2 eps ||p_Y||_2^2`                               (1.6)

is used. Its later-challenged weighted-L2 compiler is not used.

## 2. General effective-dimension squared-time lemma

The following elementary compiler is useful whenever a source-valid Fourier argument gives a joint envelope rather than a false coordinatewise pointwise estimate.

### Lemma 2.1 — `QFORM-EFFECTIVE-DIMENSION-RIESZ-v1`

Let `Y` be real and assume

`|phi_Y(t)| <= min{1, K |t|^(-d/2)}`                               (2.1)

for some `K>0`, `d>0`. Then for every `0<gamma<d`,

`boxed:
 int_R |t|^(gamma-1)|phi_Y(t)|^2 dt
 <= [2d/(gamma(d-gamma))] K^(2gamma/d).
}`                                                                   (2.2)

In particular, for `d>1/2`,

`boxed:
 int_R |t|^(-1/2)|phi_Y(t)|^2 dt
 <= [8d/(2d-1)] K^(1/d).
}`                                                                   (2.3)

If `Y'` is an independent copy, then the exact independent-copy/Riesz identity gives

`int_R |t|^(-1/2)|phi_Y(t)|^2 dt
 = sqrt(2pi) E|Y-Y'|^(-1/2).`                                      (2.4)

No coordinate difference is separated from its conjugate sum in (2.4); it is an identity for the whole copy difference.

If `d>1`, Plancherel gives an `L2` density with

`boxed:
 ||p_Y||_2^2 <= [d/(pi(d-1))] K^(2/d).
}`                                                                   (2.5)

Applying the valid account04/B03 lemma (1.6) therefore yields the actual partner-consumed inequality

`boxed:
 P(|Y-Y'|<=eps)
 <= [2d/(pi(d-1))] K^(2/d) eps.
}`                                                                   (2.6)

Finally, if `d>2`, the one-copy characteristic function is integrable and Fourier inversion gives a continuous `C_0` density satisfying

`boxed:
 ||p_Y||_infinity <= [d/(pi(d-2))] K^(2/d).
}`                                                                   (2.7)

Thus `d>2` directly gives one-copy linear small-ball scaling, whereas the critical `d=2` gives full `L2`, collision-linear scaling and half-Riesz energy but not one-copy `L-infinity` from this envelope alone.

### Proof

The crossover in (2.1) is `T=K^(2/d)`. Squaring (2.1) and integrating gives

`2[ int_0^T t^(gamma-1)dt + K^2 int_T^infinity t^(gamma-d-1)dt ]`

`=2 K^(2gamma/d)[1/gamma+1/(d-gamma)]`

`=[2d/(gamma(d-gamma))]K^(2gamma/d)`,                               (2.8)

which proves (2.2). Setting `gamma=1/2` proves (2.3). The identity

`int_R |t|^(-1/2) exp(itx) dt = sqrt(2pi)|x|^(-1/2)`                (2.9)

in the positive-kernel/Riesz sense gives (2.4) by monotone regularization.

For (2.5), use (2.2) with `gamma=1` and Plancherel:

`||p_Y||_2^2=(2pi)^(-1)int|phi_Y|^2
 <= d/[pi(d-1)] K^(2/d).`                                          (2.10)

Equation (2.6) is exactly (1.6) applied to (2.10). For `d>2`, direct integration of (2.1) gives

`int_R |phi_Y(t)|dt <= [2d/(d-2)]K^(2/d)`,                          (2.11)

and (2.7) follows from Fourier inversion. QED.

## 3. Immediate B03 corollary for the fresh grouped projected-crossing theorem

In the fresh grouped-hub theorem, let `k` be the hub-projection dimension, `ell` the projected-crossing volume degree and `d=k+ell`. Its source-valid envelope has

`K_GC = M_H^(1/2)
        2^((k+3ell)/4) pi^(d/2) exp(ell/4)
        S^(-1/2) Z_ell^(-1/4)`,                                    (3.1)

with the exponential factor omitted for `ell=1`. Here `S` is the singular-value product of the rank-`k` hub crossing and `Z_ell` is the projected crossing volume; all row-volume marginals must obey the source gate `alpha_i<=1/2`.

Lemma 2.1 gives, without any new independence assertion,

`boxed:
 int |t|^(-1/2)|phi_Q(t)|^2 dt
 <= [8d/(2d-1)] sqrt(pi)
    M_H^(1/(2d)) 2^((k+3ell)/(4d)) exp(ell/(4d))
    S^(-1/(2d)) Z_ell^(-1/(4d)).
}`                                                                   (3.2)

Again omit the exponential for `ell=1`.

For `d>1`, applying the designated account04/B03 collision lemma at the exact new `L2` value gives

`boxed:
 P(|Q-Q'|<=eps)
 <= [2d/(d-1)]
    2^((k+3ell)/(2d)) exp(ell/(2d))
    M_H^(1/d) S^(-1/d) Z_ell^(-1/(2d)) eps.
}`                                                                   (3.3)

For `d>2`, the same parameters give the already source-compatible one-copy density coefficient

`[d/(d-2)]2^((k+3ell)/(2d)) exp(ell/(2d))
 M_H^(1/d)S^(-1/d)Z_ell^(-1/(2d))`.                                (3.4)

So the fresh crossing theorem automatically supplies exactly the integrated independent-copy estimate B03 needs; the threshold `d=3` simultaneously produces one-copy linear small-ball.

For example, in the source's one-hub/two-projected-crossing case `(k,ell,d)=(1,2,3)`,

`int |t|^(-1/2)|phi_Q|^2
 <= (24/5) 2^(7/12) sqrt(pi) e^(1/6)
    M_H^(1/6) S^(-1/6) Z_2^(-1/12),`                               (3.5)

whose outer constant is `15.0591139026...`; and the partner-consumed collision coefficient is

`3*2^(7/6)e^(1/3)=9.39913188785...`                                (3.6)

multiplying `M_H^(1/3)S^(-1/3)Z_2^(-1/6) eps`.

These are not new structural hypotheses; they are the exact time/collision consequences of the fresh proved crossing theorem.

## 4. The actual angular packet is a literal exact-rank-two physical crossing

Now return to (1.2)-(1.4), with no heavy-row assumption. Let `O={i} union L union K` be the physical complement of the right bank and define the physical vector `r` on `O` by

`H_0:=aX_i+h_L.X_L+h_K.X_K = a r.X_O.`                              (4.1)

Thus the coefficient of the original pivot `i` in `r` is exactly one. Extend `u` by zero outside `L`; then

`||u||=1`, `u_i=0`, and therefore `||P_(u^perp)r||>=1`.             (4.2)

Expanding Q gives

`Q = F(X_R) + 2 X_R^T B X_O + G(X_O)`,                              (4.3)

where

`F(X_R)=a^(-1)[(beta v+m q).X_R]^2`,
`G(X_O)=a(r.X_O)^2`,                                                 (4.4)

and the literal physical cross block is

`B = v (beta r+sigma u)^T + q (m r)^T.`                             (4.5)

This is exactly the setup of the fresh theorem: arbitrary internal functions are permitted, so neither square in (4.4) is discarded.

Because `v,q` are orthonormal, the product of the two nonzero singular values of `B` is the square root of the Gram determinant of its two coefficient rows:

`(s_1(B)s_2(B))^2`
`= det Gram(beta r+sigma u, m r)`
`= m^2[ ||r||^2||beta r+sigma u||^2
        - <r,beta r+sigma u>^2 ]`
`= m^2 sigma^2 (||r||^2-<r,u>^2)`
`= m^2 sigma^2 ||P_(u^perp)r||^2`
`>= m^2 sigma^2.`                                                    (4.6)

In particular `B` has exact rank two and

`boxed: s_1(B)s_2(B) >= m|sigma|.`                                  (4.7)

This is an aggregate determinant identity before any physical minor is selected.

The orthogonal two-dimensional product projections associated with the SVD on the right and left physical banks each have density cap at most `2` by the source's product-projection theorem. Hence (1.1), `r=2`, and (4.7) give the new whole-packet estimate

### Theorem 4.1 — `QFORM-ANGULAR-PACKET-RANK2-CROSSING-RIESZ-v1`

For every packet (1.2)-(1.4), with arbitrary angular coefficient `beta`, arbitrary row leverage pattern and all signs,

`boxed:
 |phi_Q(t)|
 <= min{1, 2pi (m|sigma|)^(-1/2)|t|^(-1)}.
}`                                                                   (4.8)

Therefore

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <= (16/3)sqrt(2pi)(m|sigma|)^(-1/4)
 =13.3686841314...(m|sigma|)^(-1/4).
}`                                                                   (4.9)

Equivalently, for an independent copy `Q'`,

`boxed:
 E|Q-Q'|^(-1/2)
 <= (16/3)(m|sigma|)^(-1/4).
}`                                                                   (4.10)

Moreover Q has an `L2` density and

`boxed:
 ||p_Q||_2^2 <=4(m|sigma|)^(-1/2).
}`                                                                   (4.11)

Applying the designated account04/B03 result (1.6) to this actual new inequality gives

`boxed:
 P(|Q-Q'|<=eps)
 <=8(m|sigma|)^(-1/2) eps.
}`                                                                   (4.12)

This is genuine linear collision small-ball scaling and retains the complete dependence in the copy difference.

Unlike the earlier heavy-row estimates, (4.8)-(4.12) are independent of `eta_r`, `h_r=beta v_r+m q_r`, and the coloop defect. They therefore remain finite through exact angular cancellation and through every leverage configuration inside this packet.

## 5. Translation-uniform one-copy half-Riesz receiver at the critical dimension

Although (4.8) is only the critical `1/|t|` one-copy envelope, it still gives every finite density norm. The same Hausdorff-Young calculation as in the earlier B03 Fresnel endpoint gives, if `K_2` is the coefficient in (4.8),

`||p_Q||_4 <= [4K_2/pi]^(3/4).`                                    (5.1)

For every shift `z` and cutoff `R`, Holder near z and unit mass outside give

`E|Q-z|^(-1/2)
 <=6^(3/4)||p_Q||_4 R^(1/4)+R^(-1/2).`                             (5.2)

Optimizing R yields

`sup_z E|Q-z|^(-1/2)
 <= C_H (K_2/pi)^(1/2),
 C_H=6sqrt(6)/2^(2/3)=9.2584910653... .`                            (5.3)

Using `K_2<=2pi(m|sigma|)^(-1/2)`,

`boxed:
 sup_z E|Q-z|^(-1/2)
 <= C_H sqrt(2)(m|sigma|)^(-1/4)
 =13.0934836317...(m|sigma|)^(-1/4).
}`                                                                   (5.4)

Consequently, whenever this packet occurs as a residual beside one genuinely disjoint original cap-one square,

`T=d[Z+h]^2+Q`, `d!=0`,                                             (5.5)

with Z independent of the complete state `(h,Q)`, conditional square smoothing gives the one-copy linear small-ball estimate

`boxed:
 ||p_T||_infinity
 <= C_H sqrt(2)|d|^(-1/2)(m|sigma|)^(-1/4).
}`                                                                   (5.6)

This is a reusable linear-small-ball receiver. The present exact rank-three packet does **not** automatically furnish an unused extra square, so (5.6) is not advertised as closure of the packet or the full conjecture.

## 6. Why the fresh projected-crossing extension does not automatically supply the missing third resource here

The grouped projected-crossing theorem can promote effective dimension `k=2` to `d=2+ell>2` only if the light residual has a nonzero crossing component transverse to the row space of the hub crossing.

For the exact physical grouping (4.3), the light residual matrix is

`A_G = a r r^T.`                                                     (6.1)

Split the light coordinates `O=I disjoint_union J` and assume the restricted two-row hub crossing `M_J` has rank two, as required to keep `k=2`. In the `(v,q)` hub basis its second row is exactly

`m r_J.`                                                            (6.2)

Since `m>0`, (6.2) implies

`r_J in row(M_J).`                                                   (6.3)

Therefore the projected crossing used by the fresh theorem is

`C=(A_G)_(I,J)(I-Pi_row(M_J))`
` = a r_I r_J^T(I-Pi_row(M_J))`
` =0.`                                                               (6.4)

Hence

`Z_ell=e_ell(CC^T)=0` for every `ell>=1`.                            (6.5)

This is an exact structural calculation, not a small-parameter estimate. For the natural two-dimensional right-hub grouping of the actual survivor, the fresh arbitrary-rank extension lands **exactly at effective dimension d=2**. It explains both facts simultaneously:

- why the theorem gives the leverage-free `L2` and half-Riesz estimates (4.9)-(4.12); and
- why it does not, by itself, produce a one-copy `L-infinity` estimate for this packet.

This does not prove that every possible regrouping fails. It identifies the precise debt for this source-valid grouping: the third smoothing resource is internal to the same rank-one square/crossing geometry and is annihilated by the projected-crossing quotient. A successful next step must exploit that internal curvature **before** the transverse projection/absolute-value step, or find a different product-preserving grouping with a uniformly nonzero third resource.

## 7. Scope, target relation, and what remains

The packet scale (1.5) is retained, but (4.9)-(5.4) depend on `m|sigma|`; the spectral relation alone does not make this quantity uniformly bounded below in the way required to turn the critical d=2 certificate into the target universal `L-infinity` theorem. No such implication is asserted.

The unrestricted QFORM theorem is therefore still **OPEN**. The full continuity claim is still **OPEN**. The d>2 branches of the fresh grouped-crossing theorem have continuous `C_0` densities by Fourier inversion; Theorem 4.1 itself only establishes an `L2` density, all finite `L^p` consequences of the critical envelope, collision-linear scaling, and the translation-uniform half-Riesz receiver (5.4).

The next B03 implication is now sharply stated:

`QFORM-INTERNAL-THIRD-RESOURCE-BEFORE-PROJECTION-v1`:

> In the critical exact-rank-two crossing packet (4.3)-(4.5), exploit the internal rank-one square jointly with the crossing, before projecting the light residual into the orthogonal complement of the two crossing rows, to obtain either an effective time dimension strictly greater than two or a direct one-copy linear small-ball estimate with target-scale constant. The argument must retain arbitrary fragmented cap-one product laws and all copy-pair dependence.

This is a different mechanism from the preceding near-coloop pivot sequence and preserves the exact failure calculation (6.4) for future work.
