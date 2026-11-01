# QFORM-S7-INCIDENCE-BANK-HALFRIESZ-v1

Fix two column indices t1,t2, one row index u, and a finite set P of other row indices. For each v in P let B_v be the determinant of the two by two crossing matrix with rows u,v and columns t1,t2. Let E be the sum of B_v squared.

Let M be the rectangular matrix using rows u together with P and columns t1,t2. Since M has exactly two columns, Cauchy-Binet gives that Z_2(M) equals the sum of squares of all two-row minors of M. The B_v terms form a subfamily, hence Z_2(M) is at least E.

Using the completed marginal-free E2 half-Riesz theorem at commit 9edffa4c2a3852f42ed7e76374ac33c2ad0ff074 gives H one-half of Q at most C_E2 times E to the power minus one eighth, where C_E2 equals 9.326575926388497. The bound applies to the complete ambient quadratic polynomial.
