# Independent global colored-transfer audit and route boundary

Date: 3 October 2026. Scope: the ten-vertex Möbius ladder, Boolean convolution hosts, the colored fourth-order coefficient, and the proposed positivity of every colored coefficient. This is an independent analytic and exact-computation audit; no author checker or flow list is imported.

## Verdict

The C4 transfer and reflection identities pass. A useful Walsh-translation block reduction also passes exact checks. None of the available reductions proves global C4 positivity. In particular, neither the reflected trace nor the individual character contributions are automatically nonnegative.

The broader assertion that every colored coefficient is nonnegative is **false**, already for a strictly positive 16-state Boolean convolution kernel. An exact negative C6 example is given below and independently verified by three computations. This is a failed-route checkpoint, not a counterexample to Sidorenko's conjecture. The narrower global C4 inequality remains unproved here.

## 1. Literal graph and normalization

Use vertices `(i,t)`, with `i` modulo five and `t` in `{0,1}`. Its fifteen edges are the five rungs `(i,0)(i,1)` and the ten crossings `(i,0)(i+1,1)`, `(i,1)(i+1,0)`. The crossings form a ten-cycle and the rungs are its antipodal matching.

Let the quotient group be `K=F_2^d`, of size q. Write a host point as `(t,x)` and set

\[
 W((t,x),(s,y))=q\,[a_{x+y}+(-1)^{t+s}b_{x+y}],
 \qquad a_g\ge |b_g|,\quad \sum_g a_g=1.
\]

The kernel is symmetric, nonnegative, and has edge density one. On expanding the product of its fifteen edge kernels and averaging the first coordinate, a set of B-colored edges survives precisely when every graph vertex has even B-degree. There are 64 such sets. Their sizes have multiplicities

\[
 (0,4,6,8,10)\longmapsto(1,5,15,30,13).
\]

For a fixed surviving set, there are ten quotient vertices and fifteen factors q. Consequently the raw profile transfer trace has multiplier q^5. This explains the normalization without relying on the author's transfer-word enumeration.

## 2. C4 transfer and reflection

Index pair states by `(x,y)` and `(k,l)`. The three matrices for the unique four-edge cycle type are

\[
 X_{xy,kl}=b_{x+y}b_{x+l}b_{k+y},\quad
 Y_{xy,kl}=b_{x+y}a_{x+l}a_{k+y},\quad
 Z_{xy,kl}=a_{x+y}a_{x+l}a_{k+y}.
\]

The five four-edge cycles are rotations of the same transfer word, so

\[
 C_4=5q^5\operatorname{tr}(XYZ^3).
\]

For actual kernel matrices `A_{xy}=q a_{x+y}` and `B_{xy}=q b_{x+y}`, put

\[
 D_z=\operatorname{diag}A(z,\cdot),\qquad
 F_{zw}=B\circ(A D_z A D_w A).
\]

Then the literal reflected expansion is

\[
 C_4=\frac5{q^{10}}\sum_{z,w} A(z,w)
          \operatorname{tr}(F_{zw}B F_{zw}B).
\]

The same identity on raw matrices removes the powers q. Nine independently generated integer cases, three at each q=2,4,8, agree exactly between the full pair transfer, this reflected sum, and the translation blocks below. They also agree when b is an arbitrary signed profile rather than satisfying the host inequality.

The generic implication `F,B symmetric => tr(FBFB)>=0` is invalid: `F=diag(1,-1)` and `B=[[0,1],[1,0]]` give trace -2. This is a warning about the algebraic step, not an actual convolution-host counterexample. A proof using the reflected formula must retain its special dependence between F, A, and B, or exploit the sum over z,w.

## 3. Exact translation-block reduction

For any rung color triple `(c0,c1,c2)`, change pair coordinates to `(x,g=x+y)` and `(k,h=k+l)`, and write `t=x+k`. The corresponding transfer kernel is

\[
 c_0(g)c_1(t+h)c_2(t+g).
\]

Taking the Walsh transform in the simultaneous translation coordinate x therefore gives q blocks

\[
 T_\chi[g,h]=c_0(g)\sum_t\chi(t)c_1(t+h)c_2(t+g).
\]

No factor q occurs in this unitary change of coordinates: the full trace is the sum of the block traces.

When the cross profiles agree, define

\[
 R_p^\chi(d)=\sum_u\chi(u)p_u p_{u+d}.
\]

The C4 blocks become

\[
 X_\chi[g,h]=b_g\chi(g)R_b^\chi(g+h),\quad
 Y_\chi[g,h]=b_g\chi(g)R_a^\chi(g+h),\quad
 Z_\chi[g,h]=a_g\chi(g)R_a^\chi(g+h),
\]

and `tr(XYZ^3)=sum_chi tr(X_chi Y_chi Z_chi^3)`. Changing u to u+d proves `R_p^chi(d)=chi(d)R_p^chi(d)`. Thus it vanishes if `chi(d)=-1`; the nontrivial-character blocks split into two parity subblocks.

For strictly positive a, let `E_chi=diag(chi)`, `D_a=diag(a)`, and

\[
 T_\chi=D_a^{1/2}E_\chi R_a^\chi D_a^{1/2},\qquad
 S_\chi=D_{b/\sqrt a}E_\chi R_b^\chi D_{b/\sqrt a}.
\]

These matrices are symmetric, and the character contribution is exactly

\[
 \operatorname{tr}(X_\chi Y_\chi Z_\chi^3)
   =\operatorname{tr}(S_\chi T_\chi^4).
\]

For the trivial character, the autocorrelation matrix `R_b` is positive semidefinite, hence so is S, and that contribution is nonnegative. This implication does not extend to the other characters. In fact the actual admissible raw profiles

\[
 q=4,\quad a=(3,1,4,5),\quad b=(0,1,-2,-5)
\]

have the exact character trace contributions

\[
 (11760667978484,\;-5649532,\;977926308656,\;33153277200).
\]

The total `12771741914808` is positive, but the character indexed by 1 is negative. Here `|b|<=a` already holds, and division by 13 gives a mean-one host. Therefore a termwise character-positivity argument is ruled out in the actual host class. This does not rule out a valid inequality coupling different characters.

## 4. Why arbitrary signed-b searches are legitimate

C4 has degree eleven in a and degree four in b. Suppose `a>=0` and arbitrary real b gave a strictly negative value. First perturb a by a small positive constant if it has zeros; continuity preserves strict negativity. Then scale b by a sufficiently small positive factor so that `|b|<=a`. Normalize both profiles by `sum a`; neither operation changes the sign. Thus global sign positivity over actual nonnegative hosts is equivalent to sign positivity for all nonnegative a and all real b.

The same argument applies separately to C6, C8, and C10, whose b-degrees are six, eight, and ten. It does not say these coefficients are positive. Separately normalizing b to a sphere prevents a numerical optimizer from obtaining small values merely by taking b almost zero.

## 5. Independent larger-group C4 searches

`global_C4_ant_translation_block_search.py` uses the preceding blocks, analytic matrix gradients, a positive softmax a with sum one, and an independently sphere-normalized signed b of Euclidean norm `1/sqrt(q)`. It includes positive, mixed-sign, and sparse starting b profiles, and independently checks its gradients by finite differences.

| Quotient q | Actual host states | Starts | Iteration cap | Smallest value found | Gradient check error |
|---:|---:|---:|---:|---:|---:|
| 32 | 64 | 32 | 200 | 1.302839302114202e-13 | 1.044411761935704e-10 |
| 64 | 128 | 32 | 200 | 1.9662567005545228e-13 | 1.510157567573278e-10 |

The output files are `global_C4_ant_translation_blocks_q32_checks.json` and `global_C4_ant_translation_blocks_q64_checks.json`. The final q32 start was replayed from the deterministic seed after its initial persisted report ended at start 30; the completed report records this fact. No substantial negative value was found. Some runs terminate at an iteration limit, and these are finite floating-point searches, not an exhaustive check or proof.

## 6. Exact strictly positive actual-host C6 obstruction

Take quotient q=8, and the integer profiles

\[
 a=(3,3,503,3,3,503,3,503),\qquad
 b=(-1,2,0,2,2,0,-2,0).
\]

Their sum is 1524, and `a_g>|b_g|` in every coordinate. Divide both by 1524 in the kernel of Section 1. This is a strictly positive 16-state kernel with mean one; its smallest value is `8/1524`.

Its exact C6 coefficient is

\[
 \boxed{\displaystyle
 C_6=\frac{-809116997184077332220240713482240}{1524^{15}}<0.}
\]

The new checker `global_colored_ant_exact_obstruction_check.py` obtains this integer in three independent ways:

1. It enumerates all `2^15` subsets of the literal graph, retains exactly the 64 even-degree subsets, and multiplies the resulting full 64-by-64 integer pair transfers.
2. It constructs general-color translation blocks directly from the displayed sum over t, and sums the exact 8-by-8 block traces for each literal subset. All five colored coefficient groups match the full transfer.
3. It evaluates the Kirchhoff Fourier-flow formula without transfer matrices. Each of the three quotient frequency bits is one of the 64 literal even subsets. For each of the fifteen six-edge color sets, it sums all `64^3` quotient flows, for 3,932,160 exact fifteen-factor terms. The result is the same negative integer.

No author matrix generator, orbit list, Fourier-polynomial table, or checker is imported. The saved report is `global_colored_ant_exact_obstruction_checks.json`.

The full homomorphism density in this example is approximately 70.60856797840013, well above its mean-density lower bound one. Therefore the example is explicitly not a Sidorenko counterexample. It obstructs an intermediate coefficient-positivity assertion. The negative normalized coefficient is small (about -1.45625e-15), but its sign is certified by exact integers and does not rely on floating-point subtraction.

## 7. Remaining gap and preserved conclusions

The complete colored-coefficient positivity route has a genuine actual-host obstruction. A global C4 proof remains an independent question: its transfer identity, reflection identity, translation decomposition, and signed-profile reduction all pass, but the necessary global inequality has not been established by this audit. The completed finite-host cube8 results and the regular three-state theorem are not contradicted. No claim about unrestricted Sidorenko, general Boolean FEI, or a new solution of a famous open conjecture follows from this checkpoint.
