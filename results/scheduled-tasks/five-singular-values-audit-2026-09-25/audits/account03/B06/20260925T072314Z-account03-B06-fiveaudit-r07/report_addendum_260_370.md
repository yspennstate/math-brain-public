# account03/B06 r07 addendum

P2 also audited pinned source lines 260-370 in this invocation.

Lemma 4.2 entropy proof passes independently: zero marginals are excluded from positive-weight logarithms/divisions; Jensen is applied on the support; each squarefree degree-m monomial occurs exactly m! times; and sum_i alpha_i=m.

Lemma 4.3's internal proof passes: complex-measure domination, mollification and L2 convergence, Holder exponents, zero marginals, Gram factors, Fourier-power scaling, and entropy collapse were reconstructed. C02 at line 319 was reproduced: the source omits the outer Jensen/Cauchy-Schwarz inequality |E F|^2 <= E|F|^2 before (4.5). The one-line repair is valid with no constant loss.

End-to-end P2 closure of Lemma 4.3 remains UNCHECKED pending fresh P2 reconstruction of Lemma 2.1(a), Lemma 3.2 and Lemma 3.3. Direct P2 coverage after this run is 260-638. Next cursor: 175-241, then 83-138.
