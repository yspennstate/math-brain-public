# A005 signed-child review, with contributor conflict retained

Source: A005-POINT-EDIT-CHILD-ELIGIBILITY-OBSTRUCTION@1, statement hash fe35bf07b99937d1c09d5ac1cb5287c3696ccc6aa80995f3d3b29de935fb17c4. Entropy is in bits. Write delta_C=H-CI and sigma_i=-average delta_C(child). We review the new implication and finite obstruction; A061 authored the admission dependency and cannot independently accept that full chain.

## Physical-child reconstruction

Fix a finite nonconstant seed f with only relevant inputs and delta_C(f)>0. Let F_N be its padded one-vertex flip at zero. For a fresh coordinate, the + physical child is either clean padded f or its one-vertex flip F_(N-1), and the - child is the other. Hence sigma_j(F_N)=-(delta_C(f)+delta_C(F_(N-1)))/2. This equality uses physical truth tables, not a spectral coupling or a postselected restriction. For an old coordinate one child is clean f restricted at 1, and one is its restriction at 0 with the single edit, padded. Both converge to the corresponding seed children.

Here is a reconstruction of the continuity needed for this implication, not an independent acceptance of A061's broader lambda/D theorem. The disagreement mass is 2^-N. Parseval and Cauchy--Schwarz give spectral TV at most 2*2^(-N/2). Maximal coupling gives |Delta H| <= h2(TV)+N*TV for sufficiently large N. Each physical coordinate influence changes by at most 2^(1-N), so |Delta I|<=N*2^(1-N). These errors vanish. A seed child is treated in the same way in dimension N-1. Thus fresh sigma tends to -delta_C(f)<0 and old sigma tends to its seed value. Strictly positive old sigmas imply that exactly the old coordinates are eventually average-child eligible. No conclusion at a zero boundary follows from continuity alone.

For completeness, B_i=H(S)-H(S_-i) is continuous by marginal TV contraction and the same entropy estimate. A fresh erasure is a sum of Phi(x,y)=(x+y)log2(x+y)-xlog2x-ylog2y. Put alpha=2^(1-N), v=alpha^2. All but 2^n fresh packets have equal masses v,v. Since Phi(x,v)<=v log2(e(1+x/v)), the finitely many exceptional packets contribute O_f(N alpha^2). Consequently B_j/alpha->2. Old B_i/d_i converge to their seed ratios, with strictly positive denominators. This verifies the exact hypotheses for A005's eligible-minimum conclusion without invoking a new universal bound.

## Corrected selection

Set q_i=(B_i+max(-sigma_i,0))/d_i and Q_C=min_i q_i. Old prices converge, because max(x,0) is continuous. Fresh prices satisfy alpha*q_j -> delta_C(f)>0, so q_j is asymptotic to delta_C(f)*2^(N-1) and diverges. There are finitely many old coordinates and all fresh coordinates are symmetric. Therefore Q_C(F_N)->Q_C(f), including when an old seed sigma is zero. This is transport, not an independent deficit payment.

The exact node identity, used here to audit that distinction, gives

    q_i = max(B_i/d_i, C+(delta_C-J_i)/d_i).

Replacing B_i by D_i yields max(D_i/d_i,C+delta_C/d_i). Thus the corrected price explicitly contains the root deficit. Using the already-established J_i<=(2/ln2)d_i gives q_i>=C-2/ln2+delta_C/d_i. For a violating root this is at least C-2/ln2+delta_C/I. A universal bound Q_C<=C-2/ln2 would force delta_C<=0; restating that bound is not new structural payment. On fresh queries the unpaid numerator stays near delta_C(f), while the actual influence debit is alpha.

## Finite witness and scope

The witness is f=-1 at seed vertex zero and +1 elsewhere on three bits, padded by nine bits and then flipped at the single 12-bit zero vertex. Equivalently its negative physical vertices are precisely those with the first three bits zero except the all-zero 12-bit vertex. Its Walsh classes are 1537/2048 once, -511/2048 seven times, and 1/2048 4088 times. All coefficients are nonzero. Old influences are 511/2048; fresh influences 1/2048; I=771/1024.

The checker reconstructs the entire truth table, all Walsh coefficients, all physical edge influences, and all 24 complete physical children. At C=8/3 it must certify positive root deficit, positive old average slack with individual child slacks zero and positive, negative fresh average slack with both child slacks negative, old B_i/d_i>5/2 and fresh B_i/d_i<5/2. These signs refute exactly the quantified endpoint stated by A005. This root is not a minimal violator, because its fresh children violate the same C.

Verdict after the executed certificate passes: HOLDS for the new signed-child implication, corrected-price transport, and finite endpoint obstruction, conditional on the source-owned admission premise where invoked. INDEPENDENT_FULL_CHAIN_ACCEPTANCE_WITHHELD: A061 is the author of A061-ARBITRARY-CORE-EDIT-ADMISSION@1. No substantive repair supplied to A005 and no new broad pending candidate opened.

First unsupported universal line: select a physical query or block whose erasure and negative descendant slack have an independently owned payment, retaining both actual child deficits or terminal core deficit. Neither the local fresh price two nor the corrected-price identity proves that payment.
