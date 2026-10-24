# B18 s8/291 audit

Verdict: PASS_AFTER_LOCAL_HYPERBOLIC_REPAIR.

The reviewed statement is: if the independent real coordinate densities are bounded by K, A is real symmetric, b,c are arbitrary, and s8(A)>=s>0, then the output density of X^T A X+b^T X+c has essential supremum <291 K^2/s.

Pinned analytic source: eeb752c8943536541b34b42b8bf48e924f4d3d2f, paper blob 19fb119877426b640b2c0dae19ec2f78a399fe11. Candidate retuning: account03/B15 blob 9d0ec11f16ecb6201668a74649c831b0f132f742.

I reread the complete 955-line pinned source. The known local repair is required in the hyperbolic-pair proof: the negative exponential tail chooses its own large original coordinate from its tail vector. Equal tail-vector norms preserve every constant.

Exact retuning certificates checked:
7/125000; 3/500; 308449/648375; 8179/8312500; 20726611/202759667208; 563/5306700; 4437/52; and
291^6-2^6*6^8*178^3=989059098393>0.

The large-third-volume branch is 2*6^(4/3)*sqrt(178)=290.9209501628...<291. The scalar-pivot branch is (105/2)*sqrt(399/13)=290.8533532...<291. The other pivot and small-third-volume branches are below these.

account02/B10 independently recorded PASS for the same retuning at 5d2364175bb6cd9e01130ed9cd43fddf72c02998, with line ledger da8db39799454285bf505769eea1d31b29308847. This is a second independent end-to-end B18 review. No owner release flag is changed.

This audit certifies essential boundedness. Continuity is recorded separately. Full s3 and s7 remain open.
