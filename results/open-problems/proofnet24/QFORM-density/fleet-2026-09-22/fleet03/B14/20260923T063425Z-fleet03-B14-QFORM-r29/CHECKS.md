# Quantitative checks for QFORM-ARBITRARY-BANK-SQUARE-v1

Run: `20260923T063425Z-fleet03-B14-QFORM-r29`.

1. At `theta=1/64`, the two formulas for `H` agree:
   `8 sqrt(2) (1/64)^(1/4)=4` and `4+2 log(8 sqrt(1/64))=4`.
2. For `theta>0`, both branches of `H` are increasing.
3. Under the target conditions `|c|>=1` and `(|d|/2)||a||_2^2>=1`,
   `theta=2|c|/(|d|||a||_2^2)<=|c|`.
4. For `s>=1`,
   `F(s)=[4+2log8+log s]/s`,
   `F'(s)=-[3+2log8+log s]/s^2<0`,
   so `F(s)<=F(1)=4+2log8=8.158883083359672...`.
5. Diffuse-bank stress family: with `a_N=sqrt(2/N)(1,...,1)`, `c=d=1`, the active homogeneous matrix has nonzero eigenvalues exactly `{1,-1,1}` because the rank-one bank eigenvalue is `(1/2)||a_N||_2^2=1`; every individual bank coefficient tends to zero.

No numerical item here is used in place of the analytic proof in `REPORT.md`.
