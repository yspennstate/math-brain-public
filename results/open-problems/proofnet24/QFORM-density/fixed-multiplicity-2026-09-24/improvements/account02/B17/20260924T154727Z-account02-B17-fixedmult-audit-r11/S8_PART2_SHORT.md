# S8 closure

From Part I, g=det(CC^T)>8/25. Normalize C to the rank-two projection Q. Its determinantal two-set weights imply that two leverage scores >2/3 would force a physical 2x2 cross minor squared >8/75, impossible under the no-pivot entry cap.

Thus at most one high-leverage complement coordinate exists. With P=I-Q, the exact three-row Gram identity and diagonal cancellation give a zero-diagonal error E satisfying ||E||_F^2<=3 W_dis/g. If W_dis<=g/48, then ||E||<=1/4. The residual has global rank <=5 and restricted low-low rank <=2. From s8(A)>=1, three low diagonal coefficients have modulus >=3/4; the no-pivot entry cap makes their 3x3 restricted block strictly diagonally dominant, contradiction.

Hence W_dis>g/48>1/150. Since W_dis is part of V3, this contradicts Part I's V3<1/6400^3. Therefore the small-V3 chamber is empty and s8 implies essential density <2371 K^2/s.
