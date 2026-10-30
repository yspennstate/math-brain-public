SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B01, 2026-09-23T18:09:36Z.
attacking: the critical two-original-hub rank-two cross packet at zero hub self-curvature by a direct distribution-function estimate rather than an L1 Fourier bound.

# fleet01/B01 — direct slicing at the critical two-hub Fourier endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T180936Z-fleet01-B01-qform-auto11`  
Status: **PROVED SUPPORTING TARGET-LEVEL THEOREM; FULL QFORM OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The target remains the unrestricted product-law theorem for every symmetric A with at least three eigenvalues of modulus at least one. The phase-aligned fragmented-support construction still refutes every proposed law-uniform scalar pointwise quadratic Fresnel power decay. Nothing below uses such a bound, independence after rotation, an arbitrary-joint coarea estimate, a conditional projected-density cap, moments, compact support, or log-concavity.

## 1. Source inputs actually used

The current grouped-crossing theorem in

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`

proves the product-projection density bound needed below: if C is rank two and W has independent scalar coordinates with densities at most one, then for L=CW+d,

`||p_L||_infinity <= 2/[s1(C)s2(C)]`.

The same source shows why the ordinary Fourier receiver is critical here: an exact rank-two cross packet supplies only a `|t|^-1` characteristic-function envelope, which is not L1 by itself.

The newest completed designated partner report available before publication is fleet02/B01 run `20260923T170428Z-fleet02-B01-QFORM-auto11`, proving `QFORM-ONE-HUB-ONE-CROSS-HALFRIESZ-PEEL-v1`. Its exact application is given in Section 5.

## 2. Main theorem

### Theorem — `QFORM-TWOHUB-ZEROSELFBLOCK-SLICING-v1`

Let H=(H1,H2) be two ORIGINAL coordinates, independent of each other and of a disjoint tuple W of ORIGINAL coordinates. Assume every scalar coordinate has a probability density bounded by one. Let C be a rank-two real 2xm matrix, d in R^2, and let R(W) be an arbitrary measurable real function. Put

`L=CW+d`

and

`Q = 2 H^T L + R(W)`.                                           (2.1)

Thus the quadratic self-block on the two physical hubs is exactly zero; arbitrary affine hub terms are included in d, and R may contain arbitrary nonseparable same-bank quadratic curvature and affine terms.

Write

`S=s1(C)s2(C)=sqrt(det(CC^T))>0`.

Then Q has a continuous C0 density and

`boxed: ||p_Q||_infinity <= 2 sqrt(pi) S^(-1/2)
                              =2 sqrt(pi) det(CC^T)^(-1/4).`      (2.2)

Numerically `2 sqrt(pi)=3.5449077018110318...`.

### Proof

Fix W=w and write `l=L(w)`, `r=R(w)`. Except on a W-null set, l is nonzero because L has a two-dimensional density. Conditional on W=w,

`Q-r = 2 l1 H1 + 2 l2 H2`.                                      (2.3)

If both coordinates of l are nonzero, the two summands in (2.3) are independent and have density caps `1/(2|l1|)` and `1/(2|l2|)`. Convolution with a probability density cannot increase an L-infinity norm, so the conditional density k_l obeys

`||k_l||_infinity <= 1/[2 max(|l1|,|l2|)]
                   <= 1/[sqrt(2)|l|]`.                          (2.4)

The same first inequality is valid when exactly one coordinate of l vanishes, using the other scaled variable. Therefore the mixture over W is absolutely continuous and

`||p_Q||_infinity <= (1/sqrt(2)) E |L|^(-1)`.                   (2.5)

Let g be the density of L and put `M=||g||_infinity`. Layer cake gives

`E |L|^(-1)
 = integral_0^infinity P(|L|<1/t) dt`.                          (2.6)

The two-dimensional density cap gives

`P(|L|<r) <= min(1, pi M r^2)`.                                 (2.7)

With `T=sqrt(pi M)`, split (2.6) at T:

`E |L|^(-1)
 <= integral_0^T 1 dt + integral_T^infinity pi M t^(-2)dt
 = 2 sqrt(pi M)`.                                                (2.8)

Substitution into (2.5) yields

`||p_Q||_infinity <= sqrt(2 pi M)`.                              (2.9)

Now write an SVD `C=U diag(s1,s2) V^T`. The current source-valid product-projection theorem bounds the density of `V^T W` by `2`; scaling by the two singular values gives

`M <= 2/(s1 s2)=2/S`.                                           (2.10)

Combining (2.9) and (2.10) is exactly (2.2).

For regularity, the axes in R^2 have L-probability zero. For almost every l, both coefficients in (2.3) are nonzero, and k_l is a convolution of two L1 densities, hence belongs to C0(R). The dominating envelope in (2.4) is integrable by (2.8). Dominated convergence therefore gives continuity of `p_Q(s)=E k_L(s-R(W))`; applying the same argument as |s| tends to infinity gives `p_Q(s)->0`. QED.

## 3. Why this is an oscillatory replacement rather than the refuted pointwise claim

The grouped-crossing Fourier theorem sees rank two as the critical envelope `|phi_Q(t)| <= const/|t|`; direct absolute Fourier inversion is logarithmically divergent. The theorem above does not try to improve this to a false law-uniform pointwise decay. It instead integrates the conditional density singularity `1/|L|` against the actual two-dimensional slope distribution. The only singular integral is

`integral_R2 |l|^-1 g(l) dl`,

and its dimension-two distribution-function estimate is finite uniformly under a density cap. Thus the missing gain occurs in slope space, not pointwise in frequency.

The original phase-aligned counterexample remains valid without modification.

## 4. Target-valid pivot-resistant stress family

Let m>=2 and let u,v in R^m be flat unit vectors. On ORIGINAL coordinates

`H1,H2,Z,U_1,...,U_m,V_1,...,V_m`

choose k>=1 and eta real and define a symmetric matrix with the only nonzero entries

`A_(H1,Z)=eta`,
`A_(H1,U)=k u^T`,
`A_(H2,V)=k v^T`,                                                (4.1)

plus their symmetric transposes. Its two-by-(1+2m) cross matrix is

`C=[ eta   k u^T   0
     0      0      k v^T ]`,                                    (4.2)

so

`CC^T=diag(k^2+eta^2,k^2)`.                                    (4.3)

The nonzero spectrum of the full symmetric matrix is therefore exactly

`+sqrt(k^2+eta^2), -sqrt(k^2+eta^2), +k, -k`.                  (4.4)

Hence it satisfies the full target spectral hypothesis, in fact with four large eigenvalues, for every k>=1.

At the same time every physical diagonal is zero. Every nonzero physical 2x2 principal determinant is either `-eta^2` or `-k^2/m`. Given any fixed threshold tau>0, choose `eta^2<tau` and then `m>k^2/tau`; all such physical pair determinants are below tau although the four large eigenvalues remain.

The new theorem gives, for every admissible product input law,

`||p_Q||_infinity
 <=2 sqrt(pi) [k sqrt(k^2+eta^2)]^(-1/2)
 <=2 sqrt(pi)/k
 <=2 sqrt(pi)=3.5449077018110318...`.                           (4.5)

The density is continuous. This is a genuine aggregate rank-two slope payment: no individual small physical edge or principal pair is inverted.

## 5. Required designated-partner application at an actual inequality

Use the newest completed fleet02/B01 theorem `QFORM-ONE-HUB-ONE-CROSS-HALFRIESZ-PEEL-v1` on the following explicit target-valid form. Let e=(1,1)/sqrt(2), q=(1,-1)/sqrt(2), w=(1,1)/sqrt(2), and use six ORIGINAL independent cap-one coordinates

`X,Y,U1,U2,V1,V2`.

Set

`Q_partner = X^2 + 2Y <e,V> + 2<w,U><q,V>`.                     (5.1)

Complete the original coordinate X. The outer coefficient is `a=1`. In the residual, Y is the partner theorem's original hub, its J=V slope is `ell_J=e`, and the I=U to J=V crossing is

`C=w q^T`.                                                       (5.2)

Because q is orthogonal to e, the projected crossing remains exactly C. Moreover

`||ell_J||_2=1`, `||C||_F=1`,

and its two row weights are `w_1^2=w_2^2=1/2`, exactly satisfying the partner gate. Therefore the partner theorem gives the actual equation

`boxed: ||p_(Q_partner)||_infinity
       <=8*1^(-1/2)*(1*1)^(-1/4)=8.`                            (5.3)

This form really lies in the target class. The residual bipartite cross matrix has two singular values equal to one because e,q are orthonormal and ||w||=1, so its symmetric spectrum is `{+1,+1,-1,-1}`; the independent X^2 direction contributes another `+1`. Thus the full spectrum is `{1,1,1,-1,-1,0}`.

The partner result is complementary to the theorem of this run: (5.3) spends an OUTER scalar square to turn a one-hub/one-cross critical Fourier estimate into a half-Riesz estimate, whereas Theorem 2.1 directly closes the exact two-hub zero-self-block critical packet by integrating the slope singularity.

## 6. Sharp scope obstruction: arbitrary hub bilinear curvature cannot be added for free

The zero hub self-block hypothesis in Theorem 2.1 cannot simply be discarded while keeping only a two-dimensional slope-density cap. Take independent

`H1,H2,Y1,Y2 ~ Uniform[-1/2,1/2]`

and

`Q_0=2H1H2+2H1Y1+2H2Y2+2Y1Y2
    =2(H1+Y2)(H2+Y1)`.                                         (6.1)

The two factors on the right are independent triangular-density variables whose densities are positive at zero. Their product has a logarithmically divergent density at zero. Thus Q_0 has no bounded density.

Its symmetric coefficient matrix nevertheless has rank exactly two and nonzero eigenvalues `+2,-2`; hence (6.1) is NOT a counterexample to the three-large-eigenvalue conjecture. It is the exact rank-two logarithmic control that any proposed extension across arbitrary internal hub bilinear curvature must respect.

## 7. What is now paid and what remains open

This run pays the exact two-original-hub, rank-two slope packet whenever the physical hub self-block vanishes, while allowing arbitrary same-bank remainder curvature. It also gives C0 regularity in this scope.

The first unpaid implication for this mechanism is

`QFORM-TWOHUB-INTERNAL-CURVATURE-THIRD-RESOURCE-ROUTING-v1`:

in the remaining full-target configurations with a rank-two two-hub slope packet and nonzero internal hub quadratic block, quantitatively force the third spectral resource into (i) an outer scalar-square / half-Riesz peel, (ii) a projected crossing satisfying a volume-marginal gate, (iii) a definite or otherwise already-paid physical pair, or (iv) another proved grouped/ridge/volume receiver. The rank-two example (6.1) shows that no theorem depending only on the slope density can pay arbitrary hub bilinear curvature.

The unrestricted QFORM conjecture remains OPEN. Full-target continuity remains OPEN. No full proof or counterexample is claimed here.

## 8. Source pins


Analytic source used for (2.10):
`yspennstate/math-open-problems`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Designated partner used in Section 5:
`yspennstate/math-open-problems`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260923T170428Z-fleet02-B01-QFORM-auto11/REPORT.md`.

This run's canonical report is this file under
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260923T180936Z-fleet01-B01-qform-auto11/REPORT.md`.
