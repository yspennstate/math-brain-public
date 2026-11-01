# B12 source-bound handoff — zero-credit MUX collar

Full FEI remains **OPEN / NOT PROVED**.

Live candidate:
\[
\Gamma^\dagger=\Gamma_0+0.268204856\,p(1-p),
\qquad \Gamma^\dagger(1/2)=6.521851214.
\]

Consumed completed other-account theorem: `fleet01/B18/20260922T052537Z-zero-credit-mux-line/REPORT.md`, commit `c9794c46ea6b09c45e042290c99e53bec364dcdc`, which gives the uniform exact-line reserve
\[
D_{\Gamma^\dagger}(M;1/2,1/2,s)=Z(s)>1/64\quad(0\le s\le1).
\]
The actual-Boolean six-mass MUX law and exact selector information identities are from `fleet04/B18/20260922T045533Z-mux-joint-credit-collapse/REPORT.md` and `fleet01/B15/20260922T050419Z-mux-negative-posterior-credit/REPORT.md` (commit `9ff5ab66db321bb07f8c0667f702b2c15f97fe67`).

New theorem in this folder: if
\[
|t-1/2|\le2^{-15},\qquad |q_0-1/2|\le2^{-15},\qquad 0\le q_1\le1,
\]
then
\[
\boxed{D_{\Gamma^\dagger}(M;t,q_0,q_1)>1/128.}
\]
By swapping data labels, the same holds with `q_0,q_1` exchanged. The proof perturbs the complete six-atom Shannon law, so no negative posterior-information credit is dropped. The total perturbation debit is bounded by
\[
160/32768+165/65536+2^{-22}
=31041/4194304<1/128.
\]

This completes the quantitative-collar step explicitly left open by the consumed fleet01/B18 report. It is transverse to fleet02/B14's balanced-address equal-data relative collar and fleet04/B18's complementary-data joint tube. The next MUX task is the compact remainder away from the two zero-credit lines, the equal-data collar, and the complementary-data tubes; after full MUX, arbitrary composition-prime gates remain.

Scientific report: `REPORT.md` in this folder. Arithmetic checker: `check_zero_credit_mux_collar.py`; recorded output: `CHECK_OUTPUT.txt`.
