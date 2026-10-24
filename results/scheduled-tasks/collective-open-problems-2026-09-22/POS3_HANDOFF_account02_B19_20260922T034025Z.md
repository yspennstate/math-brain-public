# POS3 source-bound handoff — account02/B19

Run: `20260922T034025Z-account02-B19-pos3-r11-c4d1b3b8`  
Outcome: `CANDIDATE_REFUTED` (intermediate selector only; POS3 remains open)  
Brain status: `WITHOUT_VERIFIED_BRAIN`

Canonical science commit: `8f46621bd5dc29d985e453ab6d528a4eaca7476e`  
Report blob: `ebdc70ff7dfa0a07ac01c29ce60027e2aff4df25`  
Checker blob: `b73561b042a9f084790daed7e30f6232b9e7a5b3`, SHA-256 `89bb329a335fe78a0ea137ab633652525e3b936052778be5cc0e7b24a77d2d69`  
Output blob: `ccf89f1b71dfadc00539e85fc8a7e633be64a959`, SHA-256 `5cdee105a19f699b092ca06b15d924c5be89f780b3d815b871a82703f7a081e7`

Consumed current lead: account04/B10 `20260922T031005Z-B10-POS3-r11`, report blob `fb5b7e5f9b8e596f4b6bafff4d56164094336361`.  
Consumed named partner: account03/B10 `20260922T031643Z-a03-b10-pos3-r11`, report blob `e39ea9f7c820637f16470822d2979f2bbe494e0c`.

Exact witness `P` has covers

`d<a, d<r1, r1<r2, r2<u, b<u`.

It has width exactly three and 19 uniform linear extensions. For the current majority-late strict-corridor local geometry,

`Pred(b)=empty`, `Pred(a)={d}`, `D={d}`,

`Pr_P(a<b)=6/19<1/3`, `Pr_P(d<b)=15/19>2/3`, `Pr_P(a<u)=15/19>2/3`.

Conditioning on `d<b` gives a genuine uniform child `P+` with equal predecessor sets and

`e(P+)=15`, `Pr_{P+}(a<b)=2/5`.

The opposite child has `e(P-)=4` and forces `b<a`, hence

`Pr_P(a<b)=(15/19)(2/5)=6/19`.

So a balanced same pair in the equal-predecessor child does **not** lift to a balanced same pair in the original law. The original balance migrates to side-corridor pairs: `Pr(b<r1)=9/19` and `Pr(a<r2)=10/19`. Ordinal prefix/suffix chains preserve all internal probabilities, so the obstruction persists at arbitrarily large finite orders.

Next essential implication: prove a **majority-late side-channel transport lemma** under the full hypothetical-counterexample hypotheses: if exact `d<b` conditioning reaches a balanced equal-predecessor child event, the mass lost to the opposite child must force some possibly different original incomparable pair into `[1/3,2/3]`, using the width-three side-corridor/fork geometry. Same-pair scalar scaling alone is insufficient.
