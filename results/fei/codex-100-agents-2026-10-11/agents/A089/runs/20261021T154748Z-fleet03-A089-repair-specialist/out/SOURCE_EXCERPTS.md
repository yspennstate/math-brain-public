
SOURCE math-open-problems/reports\fei-2026-10-11\FEI_100_agent_research_plan.tex
169: \end{align*}
170: A successful stopping-tree theorem must bound the \emph{entire expected path cost} and the terminal entropy. The recovered threshold and formula classes provide useful terminal classes. The structural theorem guaranteeing cheap access to those terminals remains to be proved.
171: 
172: 
173: For a fixed block $W$, the recovered block identity is
174: \begin{align}
175:  \Delta_W\HH(f)
176:  &:=
177:  \HH(f)-\E_y\HH(f|_{W=y})\notag\\
178:  &=H(\mathcal S\cap W\mid\mathcal S\cap W^c)+M_W(f),
179:  \label{eq:block-erasure}\\
180:  0&\le M_W(f)\le\frac2{\ln2}\sum_{i\in W}\I_i(f),\notag\\
181:  \I(f)-\E_y\I(f|_{W=y})&=\sum_{i\in W}\I_i(f).\label{eq:block-influence}
220: \]
221: together with terminal entropy. Bounding this complete quantity
222: by a universal multiple of root influence remains open.
223: The mismatch mass $\mu_i^{\rm mis}$ is different from the
224: influence-variation refund denoted $M$ in the B05 report.
225: 
226: \paragraph{A newly verified local refund obstruction.}
227: \label{par:b05-refund}
228: For the B05 packet statistics, let $G,H$ be the actual Boolean
229: children, $a_T=\wh G(T)$, $b_T=\wh H(T)$,
230: $q_T=(a_T^2+b_T^2)/2$, $e_T=(a_T-b_T)^2/4$ and
231: $\theta_T=e_T/q_T$, omitting $q_T=0$. Define
232: \[

SOURCE context\percolation_spectral_pivotal_entropy_30pp.txt

SOURCE context\percolation_spectral_pivotal_entropy_31pp_other_version.txt

SOURCE context\threshold_paper_29pp_earlier_version.txt
1678: 
1679: Proposition 7.1 (Exact composition identities).
1680: 
1681: (64)      Eµ(F ) = E(g) + aiEµi(fi),
1682: 
1683:                                                          i
1684: 
1685: (65)  Iµ(F ) = aiIµi(fi), Varµ(F ) = Var(g),
1686: 
1687:           i
1688: 
1689: (66)      µ(F ) = (g) + aiµi(fi).
1690: 
1990: symmetric thresholds. A positive answer for arbitrary weights would remove the balance assumption
1991: on weighted internal gates in Corollary 7.4, by the same exact composition identities.
1992: 
1993:    The antichain argument raises a second question. Can a spectral reference measure control the
1994: cost of many incomparable coordinate orders without a factor depending on their number? The
1995: width bound of Theorem 4.2 and the overlap bound of Theorem C provide two ways to limit that
1996: cost. The unrestricted FEI conjecture requires an argument without either restriction.
1997: 
1998:                                         Acknowledgements and funding
1999: 
2000:    The research presented in this paper was supported by the European Research Council (ERC)
2001: under the European Union's Horizon Europe research and innovation programme (grant agreement
2002: No. 101041711), by the Simons Foundation as part of the Collaboration on the Mathematical and

SOURCE context\threshold_paper_38pp.txt
12:      joint description of each Fourier set refines the overlap estimate and recovers constant bounds for
13:      addressing. Exact selector identities extend the bound to orthogonal multiplexers with shared data.
14:      Rare activation preserves the optimal constant of unrestricted FEI. The proofs combine pivotal
15:      antichains, spectral reference measures, and product-measure composition.
16: 
17:                                        1. Introduction
18: 
19: For a Boolean function f : {-1, 1}n  {-1, 1}, write
20: 
21:                         f (x) = f (S)S(x),           S(x) = xi,
22: 
23:                                      S[n]                            iS
24: 
1961: 
1962: Proposition 7.1 (Exact composition identities).
1963: 
1964: (67)                           Eµ(F ) = E(g) + aiEµi(fi),
1965: 
1966:                                                              i
1967: 
1968: (68)                        Iµ(F ) = aiIµi(fi), Varµ(F ) = Var(g),
1969: 
1970:                                        i
1971: 
1972:                FOURIER ENTROPY OF THRESHOLD FUNCTIONS                                  27
1973: 
