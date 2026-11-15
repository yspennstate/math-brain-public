Result: partial

The question remains unresolved: this run proves neither $K(7)=3$ nor a counterexample. The established bounds remain $3\le K(7)\le4$. In particular, no finite search below is a universal inequality.

The work isolates failures of all three proposed shortcuts and gives exact adversarial evidence for the remaining inequality. The new proved statement is that the diagonal projection cost at an untouched singleton cannot be bounded by any constant multiple of $T$, or of $t_i+T$. This holds for both rank-two shapes.

## 1. Notation and what remains open

Use the definitions and identities in K5P_REPORT.md and K6P_REPORT.md. In particular, $T=\max_{i,j}F_{ij}$, $\phi_i=t_i-F_{i\cdot}$, $\mathcal E(\phi_i,z)=W(z_i-E_\pi z)$, and $\mathcal E(\phi_i,\phi_j)=-WF_{ij}$. Let $P$ be energy projection onto block-constant functions and $Q=I-P$, with representatives centered to have stationary mean zero. Write $q_i=Q\phi_i$. Then

$$\widehat F_{ij}=F_{ij}+\mathcal E(q_i,q_j)/W,\qquad a_i=\mathcal E(q_i,q_i)/W=\widehat F_{ii}-F_{ii}.$$

The previous proofs give an upper bound $T$ on entries incident to the triple and $2T$ on entries incident to either of two merged pairs. Proportional boundary vectors give $\widehat F_{ij}\le t_i+t_j$. The missing case is still two untouched singletons with independent boundary vectors. None of the arguments here bounds every such entry by $3T$.

## 2. A proved obstruction to diagonal bounds

Take the four-state family $(a,b,u,v)$ with $w_{au}=w_{bu}=1$, $w_{uv}=t^2$, $w_{aa}=w_{bb}=t-1$, $w_{vv}=t^6$, and all other conductances zero except symmetry, for integers $t\ge2$. Put

$$W=t^6+2t^2+2t+2,\quad S=t^2+2t+2,\quad N=t^7+t^6+2t^5+2t^4+2t^3+t^2+4t+2.$$

K5P proves $T=t_a=t_b=N/W$. For the merge $\{u,v\}$, its equilibrium potential has $h_a=h_b=h_u=1$, $h_v=0$, effective resistance $R=t^{-2}$, and stationary mean $p=S/W$. Therefore

$$a_a=WR(1-p)^2=\frac{(W-S)^2}{t^2W}=\frac{t^2(t^4+1)^2}{W},\qquad \frac{a_a}{T}=\frac{t^2(t^4+1)^2}{N}\sim t^3.$$

Thus $a_a/T$ and $a_a/(t_a+T)$ are unbounded. At $t=10$ the first ratio is exactly $5001000050/5611071>891$. The bound $a_i\le-F_{ii}$ is valid, since $\widehat F_{ii}\le0$, but supplies no bound in terms of $T$.

To obtain the triple shape, split $v$ into two equal clones and merge $\{u,v_1,v_2\}$. To obtain two disjoint pairs, split both $u$ and $v$ into two equal clones, and merge $\{u_1,v_1\}$ and $\{u_2,v_2\}$. A clone-to-unsplit weight is half the original weight and a clone-to-clone weight, including its loop, is one quarter. These are respectively five- and six-state examples with $a,b$ untouched. Their quotients are the four-state quotient, or its equal-root clone. In both constructions $F_{aa}$ and $\widehat F_{aa}$ stay unchanged, as does $T$.

Here is a check that cloning does not create a larger original maximum. Splitting a state $c$ adds only the possible off-diagonal value $F_{cc}+1/\pi_c$, while entries from distinct original states stay fixed. Write $C=S/t^2$, $M=t+C$, and $\mu=(2t^2+S^2/t^2)/W$. For $u$, this extra value is $2C-\mu-2W/[t^2(t^2+2)]\le2C-\mu\le M-\mu=T$, since $C\le t$ for $t\ge3$; at $t=2$ it is $-3/2-\mu\le9/2-\mu=T$. For $v$, the extra value is $-\mu+W/(t^6+t^2)\le M-\mu$, since $W/(t^6+t^2)<2<M$. The quotient clones only its root: its extra value is $-2t^2/W+W/(t^6+2t^2+2)\le 2t-2t^2/W=\widehat T$. This verifies the asserted maxima.

These examples pad to any $n\ge5$ for a triple, or $n\ge6$ for two pairs, by splitting $a$ into singleton clones. The new original off-diagonal value is $2M-\mu-W(1-1/t+1/t^2)\le T$, since $M\le(9/4)t$ and $W(1-1/t+1/t^2)\ge(3/4)t^6\ge(9/4)t$. In the quotient the new off-diagonal value is $2t-2t^2/W-W(1-1/t)\le\widehat T$. The diagonal shifts by the same amount in both chains, since the mass of the untouched state is preserved, so $a_a$ is unchanged. Thus the obstruction holds specifically on seven states as well.

The exact family checks at $t=2,10,1000$, with conductances, times, and projection costs, are in k7_leads_results.json. The asymptotic formulas above, rather than those tests, establish unboundedness.

## 3. Why the other shortcuts do not close the gap

Cauchy--Schwarz gives $\widehat F_{ij}\le F_{ij}+\sqrt{a_i a_j}$. The exact witness `cauchy_schwarz_bound_exceeds_3T` in k7_leads_results.json satisfies $\mathcal E(q_i,q_j)>0$ and $a_i a_j>(3T-F_{ij})^2$, with $3T-F_{ij}>0$. Thus this upper bound exceeds $3T$, although the actual quotient entry is below $3T$. It cannot serve as a universal factor-3 certificate.

The sequential row-maxima budget also fails. Start with the four-state family at $t=10$, add states $x,y$ each attached only to $v$ by conductance $10^{-6}$, and merge $\{u,v\}$ first and $\{x,y\}$ second. Both $a,b$ remain singleton. Exact hitting solves give

$$t_a^{(1)}+t_b^{(1)}=\frac{10002120000039}{250055500001}>\frac{229169325000879}{6251387500025}=t_a+t_b+T.$$

This rejects bounding the sum of intermediate row maxima by the desired budget. It does not reject the proposed final-entry inequality. The full conductance matrix and final entry are in `intermediate_row_sum_exceeds_proposed_budget`.

## 4. Exact orthogonal-minimum refinement, and its gap

For a pair with $c=\mathcal E(q_i,q_j)/W>0$, let $\lambda=c/a_i>0$ and $\gamma=q_j-\lambda q_i$. Then $\mathcal E(\gamma,q_i)=0$, $E_\pi\gamma=0$, and $\gamma(i)=\mathcal E(\phi_i,\gamma)/W=0$. Set

$$g=\lambda\phi_i,\quad k=\phi_j-\gamma,\quad m=\min(g,k).$$

Here $Qg=Qk=\lambda q_i$. Consequently $g-k$ and $m-k$ are block constant. It follows that $\mathcal E(\gamma,m)=\mathcal E(\gamma,k)=0$, because $Qk=\lambda q_i$. Dirichlet minimization and the disjoint-support argument therefore give

$$\lambda^2Wa_i\le\mathcal E(m,m)\le\mathcal E(g,m)+\mathcal E(k,m)-\mathcal E(g,k).$$

For the upper inequality, $g-m$ and $k-m$ are nonnegative and have disjoint supports, regardless of the sign of $m$, so their cross-energy is nonpositive. The source identities, orthogonality, and $\gamma(i)=0$ give

$$\mathcal E(g,m)=\lambda W(m_i-\bar m),\quad \mathcal E(k,m)=W(m_j-\bar m),\quad \mathcal E(g,k)=-\lambda WF_{ij},$$

where $\bar m=E_\pi m$. Also $m_i\le t_j-F_{ij}$ and $m_j\le\lambda(t_i-F_{ij})$. Dividing by $\lambda W$ proves the exact inequality

$$\boxed{\widehat F_{ij}\le t_i+t_j-(1+1/\lambda)E_\pi m.}$$

This does not prove factor 3. The function $k$ can be negative; an exact example is saved as `removing_orthogonal_boundary_part_loses_nonnegativity`. More decisively, the tempting sufficient bound $-(1+1/\lambda)E_\pi m\le T$ fails even if the better of the two orientations $(i,j)$ and $(j,i)$ is chosen. The initial finite scan did not find this failure; the adversarial test did. This is why the scan is not evidence of a theorem.

For `k7_min_search_results.json`, the smaller of the two normalized error terms is 200370.630809, while the actual entry ratio is 0.941885243514. Both error terms exceed 1 exactly; the explicit rational values, chain, and partition are in that file and independently audited in k7_final_results.json.

For `k7_min_search_above2_results.json`, the smaller of the two normalized error terms is 1853.05426, while the actual entry ratio is 2.0334909032. Both error terms exceed 1 exactly; the explicit rational values, chain, and partition are in that file and independently audited in k7_final_results.json.

The second test explicitly restricts to $\widehat F_{ij}\ge2T$. Thus restricting to entries above $2T$ does not repair this sufficient bound. No bound on the actual entry follows from the large error term.

Gap: a different estimate exploiting the rank-two structure is still needed. Neither this refinement, the diagonal estimates, nor the sequential row bounds establishes $\widehat F_{ij}\le t_i+t_j+T$. The claimed constant 2 for a triple remains a conjecture.

## 5. Exact best values and the search evidence

The following table reports the largest values among the new searches, the fork prequotient scans, and explicitly audited baselines at parameter $10^{12}$. Every entry is an exact rational in k7_final_results.json; decimal values are only for readability. All pairs in the table are untouched singletons.

| States | Shape | Best $\widehat F_{ij}/T$ | Best $(\widehat F_{ij}-t_i-t_j)/T$ |
|---:|---|---:|---:|
| 6 | pairs | 2.999999999994 | 0.999999999995 |
| 6 | triple | 1.999999999998 | -1.9999999799998e-16 |
| 7 | pairs | 2.999999999994 | 0.999999999995 |
| 7 | triple | 1.999999999998 | -1.9999000099956e-16 |
| 8 | pairs | 2.999999999994 | 0.999999999995 |
| 8 | triple | 1.999999999998 | -2.000000000002e-12 |

The ratio winners for two pairs are the exact $R_3$ family in K6P_REPORT.md, equation (12), at $M=10^{12}$; the triple ratio winners are $R_2$ in its equation (11), with the padding described below. In particular the two-pair ratio approaches 3, and the triple ratio approaches 2. These are lower bounds only.

For completeness, the following list gives every best value exactly. A record identifies the conductances, partition, pair, $T,t_i,t_j$, and quotient entry in k7_final_results.json.

- `6_pairs_excess`: `2999999999990999999999993999999999990999999999996999999999987999999999989999999999979999999999997999999999982999999999986999999999983999999999993999999999986999999999992999999999994999999999996999999999998000000000003000000000001000000000000000000000001000000000002000000000001/3000000000006000000000003000000000006000000000006000000000009000000000008000000000015000000000006000000000010000000000011000000000014000000000008000000000011000000000008000000000009000000000007000000000004000000000002000000000004000000000002000000000000000000000000000000000000` (source `R3_M10pow12_padded_to_6`).
- `6_pairs_ratio`: `9000000000000000000000000000000000000000000000006000000000003000000000006000000000005000000000006000000000000000000000006000000000007000000000007000000000003000000000004000000000006000000000006000000000002000000000003000000000004000000000001/3000000000006000000000003000000000006000000000006000000000009000000000008000000000015000000000006000000000010000000000011000000000014000000000008000000000011000000000008000000000009000000000007000000000004000000000002000000000004000000000002` (source `R3_M10pow12_padded_to_6`).
- `6_triple_excess`: `-3333333366672999866743339666733410016333833493357334033516683333633356676333500000013667533420014667833416672666999986664999666616662666466633331333299993333/16666667000033338334000073343334033480007000966803346334333510016334766833349334633443346667866753345667800100007667500049999333433303328332966613328666466633331333299993333` (source `k7_prequotient:6_triple_ratio`).
- `6_triple_ratio`: `333333333333333333333333333333333333333333333334000000000000333333333334000000000000/166666666666833333333333666666666667000000000000333333333333500000000000666666666667` (source `R2_M10pow12_padded_to_6`).
- `7_pairs_excess`: `2999999999990999999999993999999999990999999999996999999999987999999999989999999999979999999999997999999999982999999999986999999999983999999999993999999999986999999999992999999999994999999999996999999999998000000000003000000000001000000000000000000000001000000000002000000000001/3000000000006000000000003000000000006000000000006000000000009000000000008000000000015000000000006000000000010000000000011000000000014000000000008000000000011000000000008000000000009000000000007000000000004000000000002000000000004000000000002000000000000000000000000000000000000` (source `R3_M10pow12_padded_to_7`).
- `7_pairs_ratio`: `9000000000000000000000000000000000000000000000006000000000003000000000006000000000005000000000006000000000000000000000006000000000007000000000007000000000003000000000004000000000006000000000006000000000002000000000003000000000004000000000001/3000000000006000000000003000000000006000000000006000000000009000000000008000000000015000000000006000000000010000000000011000000000014000000000008000000000011000000000008000000000009000000000007000000000004000000000002000000000004000000000002` (source `R3_M10pow12_padded_to_7`).
- `7_triple_excess`: `-111127779444755603338556489013345334844623351446278004465890533466680000344468886998888727758108333053301774244128857885633044417664099805540442955443324554666595550443999973331221911078885999755541110111011102221333255551111/555666677780555833366673556366766681779489067801780411406702892755947822004533775604893789365606115867124491115500434489448689306708448455932261003833697813669955856695447011341132001766814457334355626672111544474446666822228889000000000000` (source `k7_prequotient:7_triple_excess`).
- `7_triple_ratio`: `333333333333333333333333333333333333333333333334000000000000333333333334000000000000/166666666666833333333333666666666667000000000000333333333333500000000000666666666667` (source `R2_M10pow12_padded_to_7`).
- `8_pairs_excess`: `2999999999990999999999993999999999990999999999996999999999987999999999989999999999979999999999997999999999982999999999986999999999983999999999993999999999986999999999992999999999994999999999996999999999998000000000003000000000001000000000000000000000001000000000002000000000001/3000000000006000000000003000000000006000000000006000000000009000000000008000000000015000000000006000000000010000000000011000000000014000000000008000000000011000000000008000000000009000000000007000000000004000000000002000000000004000000000002000000000000000000000000000000000000` (source `R3_M10pow12_padded_to_8`).
- `8_pairs_ratio`: `9000000000000000000000000000000000000000000000006000000000003000000000006000000000005000000000006000000000000000000000006000000000007000000000007000000000003000000000004000000000006000000000006000000000002000000000003000000000004000000000001/3000000000006000000000003000000000006000000000006000000000009000000000008000000000015000000000006000000000010000000000011000000000014000000000008000000000011000000000008000000000009000000000007000000000004000000000002000000000004000000000002` (source `R3_M10pow12_padded_to_8`).
- `8_triple_excess`: `-333333333334000000000000666666666666666666666666666666666667333333333334/166666666666833333333333666666666667000000000000333333333333500000000000666666666667` (source `R2_M10pow12_padded_to_8`).
- `8_triple_ratio`: `333333333333333333333333333333333333333333333334000000000000333333333334000000000000/166666666666833333333333666666666667000000000000333333333333500000000000666666666667` (source `R2_M10pow12_padded_to_8`).

The ratio baseline for two pairs is the six-state fork $N=1$, cloned at the untouched $a$ to reach seven or eight states, keeping each clone singleton. Its maximizing pair is $a,y_0$. Writing $U=M^3+M+1$, the original row maxima are $t_a=T_3$ and $t_{y_0}=T_3-U/M^3$. This gives the exact baseline excess $R_3-2+U/(M^3T_3)$, independently checked by hitting solves. The triple baseline splits the four-state family root $v$ into two equal clones, merges $\{u,v_1,v_2\}$, and then splits $a$ into $n-4$ equal singleton clones. It retains the original and quotient times. All conductances and the maximum checks are saved.

The main optimizer used exact rational objectives on every proposal, including rejected proposals. It separately maximized the entry ratio and the excess for each shape at each size, starting from both the fork and the independent-vector obstacle witness. Conductances include powers of ten, multiplicative heavy-tailed perturbations, zero edges, extra edges, and loops. Proposal acceptance uses floating-point probabilities; all objective comparisons and saved values use Fraction.

| Run | Exact objective evaluations | Seconds | Peak RSS, bytes |
|---|---:|---:|---:|
| n=6 | 195210 | 160.003 | 29786112 |
| n=7 | 126736 | 160.002 | 29196288 |
| n=8 | 67247 | 160.003 | 28508160 |

The main runs total 389,193 exact objectives. The separate prequotient scan checked 2,894 chains and 447,028 rank-two partitions in 165.054 seconds. It starts with larger fork combs (eight or ten states), prequotients them to six, seven, or eight states, and then scans every rank-two partition. This tests a different family of adversarial starts; it found no counterexample.

The independent final audit recomputed 36 saved witnesses with target-by-target killed hitting systems, compared every quotient matrix against the low-rank update, verified all saved objective values, checked the baseline formulas, and confirmed the two failures of the orthogonal-minimum sufficient bound. The conditional energy argument was separately audited in k7_minimum.py, including its Dirichlet, source, and disjoint-support steps. None of these checks establishes the missing universal bound.

## 6. Programs and outputs

| Program | Output and data | Purpose |
|---|---|---|
| k7_probe.py | k7_probe_output.txt; k7_probe_results.json | Initial exact all-partition probes |
| k7_search.py | k7_search_6_output.txt, k7_search_7_output.txt, k7_search_8_output.txt; matching results JSON | Exact singleton ratio and excess optimization |
| k7_leads.py | k7_leads_output.txt; k7_leads_results.json | Diagonal family and shortcut obstructions |
| k7_minimum.py | k7_minimum_output.txt; k7_minimum_results.json | Exact audit of the orthogonal-minimum inequality |
| k7_min_search.py | k7_min_search_output.txt and k7_min_search_above2_output.txt; matching results JSON | Adversarial rejection of the sufficient mean bound |
| k7_prequotient.py | k7_prequotient_output.txt; k7_prequotient_results.json | Larger-fork prequotient scans |
| k7_summary.py | k7_summary_output.txt | Readable intermediate summaries |
| k7_finalize.py | k7_finalize_output.txt; k7_final_results.json; REPORT.md | Independent exact recomputation and report |
| k7_check_report.py | k7_check_report_output.txt | Final report and artifact checks |

The reused libraries are q1_core.py, q2_search.py, and q2_families.py. No old search results were overwritten. All new findings were appended to LOG.md when obtained. Programs were saved before execution. Each task computation used one numerical-library thread; at most two computations overlapped. All measured runs were below five minutes and far below 1 GB. Python bytecode writes were disabled. No web, other agents, git pushes, visible windows, or writes outside this directory were used. External brain/checklist/mesh tools were not invoked because they write outside the authorized directory.

Reproduce each program separately, for example:

```sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 k7_search.py 7 160 > k7_search_7_output.txt 2>&1
```

Use n=6 and n=8 for the other main runs. Run k7_min_search.py without arguments for the unrestricted error search, and with argument 2 for the restricted one. Run k7_finalize.py after the searches and k7_check_report.py last. Searches append to LOG.md; reruns can change their time-limited incumbents.

Task: “settle K(7)” — 12 November 2026, 22:32:16 +0400 (first local work recorded; exact receipt time unavailable).
