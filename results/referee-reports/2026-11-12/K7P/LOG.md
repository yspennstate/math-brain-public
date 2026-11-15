# K(7) research log

2026-11-12, task start (Asia/Tbilisi; exact receipt time unavailable). Read K5P_REPORT.md before K6P_REPORT.md, then q1_core.py and the relevant q2 programs. The established universal bound remains 4; rank-two singleton entries with independent boundary vectors are the only missing factor-3 case. Work is restricted to this directory; external brain/mesh/checklist programs are not invoked because they write outside it. No web, agents, pushes, or visible windows. Programs will run sequentially with one numerical-library thread and a wall-time limit below five minutes.

Initial algebra observation: for every state, a_i = Fhat_ii - F_ii <= -F_ii because Fhat_ii <= 0. This is an upper bound, not equality, and is not useful without controlling the possibly large negative original diagonal. For an untouched singleton, Q phi_i is harmonic outside the merged vertices, by the original and quotient source equations. Whether this yields a bound in terms of t_i and T remains to be tested.

Orthogonal-decomposition refinement (derived before testing): write q_i=Q phi_i, a_i=E(q_i,q_i)/W, c=E(q_i,q_j)/W>0, lambda=c/a_i, gamma=q_j-lambda q_i (centered), k=phi_j-gamma, g=lambda phi_i, m=min(g,k). Then Qg=Qk, so m-k is block constant and E(gamma,m)=E(gamma,k)=0. Also gamma(i)=0. The same disjoint-support energy argument as K5P, which does not require m>=0, gives Fhat_ij <= t_i+t_j-(1+1/lambda) E_pi m. Thus a lower bound E_pi m >= -lambda*T/(1+lambda) would suffice. A weaker sufficient condition bounds (1+1/lambda)E_pi(k_-)/T by 1. Neither bound is yet proved; k need not be nonnegative. This is an exact reduction, not a resolution.

Padding the diagonal obstruction: singleton-cloning a leaves the correction a_a unchanged because the original and quotient diagonal shifts are identical. The possible new original off-diagonal is 2M-mu-W(1-1/t+1/t^2), at most T since M <= (9/4)t and W(1-1/t+1/t^2) >= (3/4)t^6. The quotient off-diagonal is at most its old maximum. Thus a_i/T is unbounded for each fixed n >= 5 (triple) or n >= 6 (two pairs), including n=7 in both shapes. This is a proved obstruction, not a counterexample to factor 3.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_triple = 56066361677495235/2551659699161; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_triple = 56066361677495235/8035647248653; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_pairs = 26822922928731/12641900175124; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_pairs = 5785391432562876/255267221789; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_pairs = 5785391432562876/803883585697; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_triple = 71423163691731/3150058268; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_triple = 71423163691731/9920114764; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_triple = 27930528323386965/98044925326; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_triple = 27930528323386965/196089850652; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_pairs = 137588798390031/483575464; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_pairs = 137588798390031/967150928; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_pairs = 25140919445506989/88252522180; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_pairs = 25140919445506989/176505044360; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_triple = 17219807844975/60446933; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_triple = 17219807844975/120893866; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_triple = 2272530219176069619736181802500000/1608349659052500017188533; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_triple = 4545060438352139239472363605000000/21598559317931731824864187; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_pairs = 22522554168941135423581052500000/15924255625108484188533; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_pairs = 45045108337882270847162105000000/213847143111550637864187; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_triple = 2252255416654113381807550250/1592425403427391533; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_triple = 4504510833308226763615100500/21384712174820181187; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_triple = 4545015438652438885784445205000000/18363514666839580487121; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_triple = 2272507719326219442892222602500000/18363514666839580487121; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_pairs = 454500643863830854746332210500/1836349648515989221; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_pairs = 227250321931915427373166105250/1836349648515989221; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_pairs = 4500015330349056622826272500000000/18181697869956809277121; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_pairs = 2250007665174528311413136250000000/18181697869956809277121; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_triple = 4500010830338226284716160500/18181679688277121; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_triple = 2250005415169113142358080250/18181679688277121; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_triple = 4500004500000004515003013503003003021505013503507002514004007002003501003501000500000000000000000000/3001506006006009008507010512009514509009009009504508004003502502000501501; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_triple = 2250002250000002257501506751501501510752506751753501257002003501001750501750500250000000000000000000/753002256756006759508757762012760515509760010510255758254504003002000751751; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_pairs = 4500000004500000010503003003007503008002002501505503004502001501002001000500000000000000000000/3001503004503004505505506509504506506006504006503003502502000501501; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_pairs = 2250000002250000005251501501503751504001001250752751502251000750501000500250000000000000000000/753001503754503005006505757010005007006757255006503504003002000751751; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_triple = 642857143500000001500429000429000001143143214500357286214428785714428571500000000/428786143500429215071786429500429286357500429000071643; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_triple = 321428571750000000750214500214500000571571607250178643107214392857214285750000000/107571643393500429286536107929571929357821857679000107393; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_triple = 4500004500000000015003013503006003021508013503008007015007008004004004005002000500000000000000000000/1503003006003004505509005511006007508009005007505004503502001002001; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_triple = 2250002250000000007501506751503001510754006751504003507503504002002002002501000250000000000000000000/1503003006003004505509005511006007508009005007505004503502001002001; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_pairs = 4500004500000000006003013503006003008002010503005004007004006003003002002001000500000000/1503003006003004504006004008004506005504503504002002001; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_pairs = 2250002250000000003001506751503001504001005251502502003502003001501501001000500250000000/1503003006003004504006004008004506005504503504002002001; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_pairs = 4500000000000000015003003000003003018505005501005506012503002501002502002500000000000000000000000000/1503001503001501504007503006504504005006502505504002502502001002001; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_pairs = 2250000000000000007501501500001501509252502750502753006251501250501251001250000000000000000000000000/1503001503001501504007503006504504005006502505504002502502001002001; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_triple = 4500000000000000010503003000003003008002002501002503004502001501001501000500000000/1503001503001501502504501503503002502502001002001; exact witness saved.

2026-11-12 22:32:16 Initial probe: reject_a_le_ti_plus_T_triple = 2250000000000000005251501500001501504001001250501251502251000750500750500250000000/1503001503001501502504501503503002502502001002001; exact witness saved.

2026-11-12 22:32:18 Initial exact probes complete: 5321 rank-two partitions in 1.988s; peak RSS 29523968 bytes. Details in k7_probe_results.json.

2026-11-12 22:34:13 Adversarial n=7, pairs_ratio: exact incumbent 2.999991000024, evaluation 1; witness in k7_search_7_results.json.

2026-11-12 22:34:53 Adversarial phase n=7 pairs ratio finished; 26611 exact evaluations.

2026-11-12 22:34:53 Adversarial n=7, pairs_excess: exact incumbent 0.999992000021, evaluation 26612; witness in k7_search_7_results.json.

2026-11-12 22:34:54 Adversarial n=7, pairs_excess: exact incumbent 0.999999486004184, evaluation 27440; witness in k7_search_7_results.json.

2026-11-12 22:34:54 Adversarial n=7, pairs_excess: exact incumbent 0.999999690842536, evaluation 27441; witness in k7_search_7_results.json.

2026-11-12 22:34:54 Adversarial n=7, pairs_excess: exact incumbent 0.99999988884241, evaluation 27446; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial phase n=7 pairs excess finished; 29213 exact evaluations.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.60048247035638, evaluation 55825; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.60048247035638, evaluation 55832; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.60115330909228, evaluation 55845; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.73322938792986, evaluation 55846; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.73330864244845, evaluation 55850; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.7489152229128, evaluation 55866; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.74899585828395, evaluation 55887; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.74899585828395, evaluation 55888; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.74899603764049, evaluation 55889; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.74927179562043, evaluation 55896; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.74953520128472, evaluation 55916; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.74953521489115, evaluation 55918; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.74953521489115, evaluation 55919; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.74953521489679, evaluation 55924; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.74954271278111, evaluation 55926; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.74954353755663, evaluation 55927; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.74956975359307, evaluation 55930; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.74959199121526, evaluation 55931; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.76747451031871, evaluation 56188; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.76748315852095, evaluation 56189; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.76748316669225, evaluation 56190; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.76907131963131, evaluation 56195; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.76966357843077, evaluation 56249; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.77208940958906, evaluation 56272; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.77208984463732, evaluation 56273; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.7770588474, evaluation 56281; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.77705884740347, evaluation 56282; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.77705918596499, evaluation 56284; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.79925386942643, evaluation 56285; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.86879161128854, evaluation 56287; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.86884642429617, evaluation 56305; witness in k7_search_7_results.json.

2026-11-12 22:35:33 Adversarial n=7, triple_ratio: exact incumbent 1.86884643098341, evaluation 56307; witness in k7_search_7_results.json.

2026-11-12 22:35:36 Adversarial n=7, triple_ratio: exact incumbent 1.86906758710549, evaluation 58446; witness in k7_search_7_results.json.

2026-11-12 22:35:37 Adversarial n=7, triple_ratio: exact incumbent 1.87331008340999, evaluation 59676; witness in k7_search_7_results.json.

2026-11-12 22:35:37 Adversarial n=7, triple_ratio: exact incumbent 1.87352376773557, evaluation 59678; witness in k7_search_7_results.json.

2026-11-12 22:35:37 Adversarial n=7, triple_ratio: exact incumbent 1.87353474634742, evaluation 59679; witness in k7_search_7_results.json.

2026-11-12 22:35:37 Adversarial n=7, triple_ratio: exact incumbent 1.87889354710825, evaluation 59691; witness in k7_search_7_results.json.

2026-11-12 22:35:39 Adversarial n=7, triple_ratio: exact incumbent 1.89401931611731, evaluation 61618; witness in k7_search_7_results.json.

2026-11-12 22:35:39 Adversarial n=7, triple_ratio: exact incumbent 1.89418894024859, evaluation 61630; witness in k7_search_7_results.json.

2026-11-12 22:35:39 Adversarial n=7, triple_ratio: exact incumbent 1.89425493566744, evaluation 61631; witness in k7_search_7_results.json.

2026-11-12 22:36:13 Adversarial phase n=7 triple ratio finished; 37408 exact evaluations.

2026-11-12 22:36:13 Adversarial n=7, triple_excess: exact incumbent -0.322466129082961, evaluation 93233; witness in k7_search_7_results.json.

2026-11-12 22:36:13 Adversarial n=7, triple_excess: exact incumbent -0.0450669898827129, evaluation 93238; witness in k7_search_7_results.json.

2026-11-12 22:36:13 Adversarial n=7, triple_excess: exact incumbent -0.0238389777962434, evaluation 93239; witness in k7_search_7_results.json.

2026-11-12 22:36:13 Adversarial n=7, triple_excess: exact incumbent -0.00800660610233474, evaluation 93260; witness in k7_search_7_results.json.

2026-11-12 22:36:13 Adversarial n=7, triple_excess: exact incumbent -0.00364184498457388, evaluation 93270; witness in k7_search_7_results.json.

2026-11-12 22:36:13 Adversarial n=7, triple_excess: exact incumbent -0.00361500353640005, evaluation 93271; witness in k7_search_7_results.json.

2026-11-12 22:36:13 Adversarial n=7, triple_excess: exact incumbent -0.00286276273675256, evaluation 93326; witness in k7_search_7_results.json.

2026-11-12 22:36:13 Adversarial n=7, triple_excess: exact incumbent -0.00278007735685637, evaluation 93332; witness in k7_search_7_results.json.

2026-11-12 22:36:13 Adversarial n=7, triple_excess: exact incumbent -0.00154699061369513, evaluation 93334; witness in k7_search_7_results.json.

2026-11-12 22:36:13 Adversarial n=7, triple_excess: exact incumbent -0.00154042327982892, evaluation 93335; witness in k7_search_7_results.json.

2026-11-12 22:36:13 Adversarial n=7, triple_excess: exact incumbent -0.0015404232703658, evaluation 93336; witness in k7_search_7_results.json.

2026-11-12 22:36:13 Adversarial n=7, triple_excess: exact incumbent -0.000804343595490624, evaluation 93337; witness in k7_search_7_results.json.

2026-11-12 22:36:13 Adversarial n=7, triple_excess: exact incumbent -8.06164473105118e-05, evaluation 93340; witness in k7_search_7_results.json.

2026-11-12 22:36:13 Adversarial n=7, triple_excess: exact incumbent -5.11052468728238e-05, evaluation 93346; witness in k7_search_7_results.json.

2026-11-12 22:36:13 Adversarial n=7, triple_excess: exact incumbent -4.83733189361071e-05, evaluation 93350; witness in k7_search_7_results.json.

2026-11-12 22:36:15 Adversarial n=7, triple_excess: exact incumbent -1.72906173492214e-05, evaluation 94636; witness in k7_search_7_results.json.

2026-11-12 22:36:15 Adversarial n=7, triple_excess: exact incumbent -1.22456562443749e-05, evaluation 94642; witness in k7_search_7_results.json.

2026-11-12 22:36:15 Adversarial n=7, triple_excess: exact incumbent -9.08486257562559e-06, evaluation 95125; witness in k7_search_7_results.json.

2026-11-12 22:36:15 Adversarial n=7, triple_excess: exact incumbent -8.195621128487e-06, evaluation 95132; witness in k7_search_7_results.json.

2026-11-12 22:36:15 Adversarial n=7, triple_excess: exact incumbent -8.16852186171863e-06, evaluation 95133; witness in k7_search_7_results.json.

2026-11-12 22:36:15 Adversarial n=7, triple_excess: exact incumbent -8.15278490539502e-06, evaluation 95134; witness in k7_search_7_results.json.

2026-11-12 22:36:15 Adversarial n=7, triple_excess: exact incumbent -8.121600575283e-06, evaluation 95135; witness in k7_search_7_results.json.

2026-11-12 22:36:37 Adversarial n=7, triple_excess: exact incumbent -9.96696589619249e-07, evaluation 114260; witness in k7_search_7_results.json.

2026-11-12 22:36:37 Adversarial n=7, triple_excess: exact incumbent -9.96696521811263e-07, evaluation 114261; witness in k7_search_7_results.json.

2026-11-12 22:36:37 Adversarial n=7, triple_excess: exact incumbent -9.86867913257426e-07, evaluation 114263; witness in k7_search_7_results.json.

2026-11-12 22:36:37 Adversarial n=7, triple_excess: exact incumbent -9.78021894522387e-07, evaluation 114265; witness in k7_search_7_results.json.

2026-11-12 22:36:41 Adversarial n=6, pairs_ratio: exact incumbent 2.999994000009, evaluation 1; witness in k7_search_6_results.json.

2026-11-12 22:36:53 Adversarial phase n=7 triple excess finished; 33504 exact evaluations.

2026-11-12 22:36:53 Adversarial n=7 complete: 126736 exact evaluations, 88272 accepted, 160.002s, peak RSS 29196288 bytes.

2026-11-12 22:37:21 Adversarial phase n=6 pairs ratio finished; 41175 exact evaluations.

2026-11-12 22:37:21 Adversarial n=6, pairs_excess: exact incumbent 0.999995000007, evaluation 41176; witness in k7_search_6_results.json.

2026-11-12 22:37:21 Adversarial n=6, pairs_excess: exact incumbent 0.999995947838098, evaluation 41849; witness in k7_search_6_results.json.

2026-11-12 22:37:21 Adversarial n=6, pairs_excess: exact incumbent 0.999995947918098, evaluation 41850; witness in k7_search_6_results.json.

2026-11-12 22:37:21 Adversarial n=6, pairs_excess: exact incumbent 0.999995951878107, evaluation 41853; witness in k7_search_6_results.json.

2026-11-12 22:37:21 Adversarial n=6, pairs_excess: exact incumbent 0.999995959078084, evaluation 41855; witness in k7_search_6_results.json.

2026-11-12 22:37:21 Adversarial n=6, pairs_excess: exact incumbent 0.999995959078084, evaluation 41857; witness in k7_search_6_results.json.

2026-11-12 22:37:21 Adversarial n=6, pairs_excess: exact incumbent 0.999995959083084, evaluation 41858; witness in k7_search_6_results.json.

2026-11-12 22:37:21 Adversarial n=6, pairs_excess: exact incumbent 0.999995959875082, evaluation 41862; witness in k7_search_6_results.json.

2026-11-12 22:37:21 Adversarial n=6, pairs_excess: exact incumbent 0.999999919490803, evaluation 41864; witness in k7_search_6_results.json.

2026-11-12 22:37:21 Adversarial n=6, pairs_excess: exact incumbent 0.999999955498001, evaluation 41868; witness in k7_search_6_results.json.

2026-11-12 22:37:30 Adversarial n=6, pairs_excess: exact incumbent 0.9999999981925, evaluation 51581; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial phase n=6 pairs excess finished; 46941 exact evaluations.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.73252337280837, evaluation 88117; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.73252337309739, evaluation 88121; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.77498556502997, evaluation 88173; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.7749855679492, evaluation 88174; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.77510694270768, evaluation 88184; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.83827755067196, evaluation 88359; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.85622816738315, evaluation 88560; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.87428037287297, evaluation 88561; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.87465954108998, evaluation 88566; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.87478475163633, evaluation 88572; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.87569979555586, evaluation 88579; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.87569979798145, evaluation 88583; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.87856564631819, evaluation 88585; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.87862060265864, evaluation 88586; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.8786353931549, evaluation 88588; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.87867314097957, evaluation 88600; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.9103836512026, evaluation 88866; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.91038365686636, evaluation 88867; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.95253134168719, evaluation 88868; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.95253134798706, evaluation 88869; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.95253134799057, evaluation 88875; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.95253134799409, evaluation 88877; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.95253134805739, evaluation 88880; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.95253134805743, evaluation 88882; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.96075649508461, evaluation 88889; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.96305606186495, evaluation 88906; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.96306787580039, evaluation 88907; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.96306787581306, evaluation 88909; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.96593315443797, evaluation 88945; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.96593316046687, evaluation 88946; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.96609624565848, evaluation 88947; witness in k7_search_6_results.json.

2026-11-12 22:38:01 Adversarial n=6, triple_ratio: exact incumbent 1.96998304315265, evaluation 88949; witness in k7_search_6_results.json.

2026-11-12 22:38:02 Adversarial n=6, triple_ratio: exact incumbent 1.97585370721519, evaluation 89341; witness in k7_search_6_results.json.

2026-11-12 22:38:02 Adversarial n=6, triple_ratio: exact incumbent 1.9788729779401, evaluation 89344; witness in k7_search_6_results.json.

2026-11-12 22:38:02 Adversarial n=6, triple_ratio: exact incumbent 1.97901906924441, evaluation 89427; witness in k7_search_6_results.json.

2026-11-12 22:38:02 Adversarial n=6, triple_ratio: exact incumbent 1.9799548699867, evaluation 89439; witness in k7_search_6_results.json.

2026-11-12 22:38:02 Adversarial n=6, triple_ratio: exact incumbent 1.98157987322123, evaluation 89441; witness in k7_search_6_results.json.

2026-11-12 22:38:02 Adversarial n=6, triple_ratio: exact incumbent 1.98163919627123, evaluation 89446; witness in k7_search_6_results.json.

2026-11-12 22:38:03 Adversarial n=6, triple_ratio: exact incumbent 1.98248779991235, evaluation 91397; witness in k7_search_6_results.json.

2026-11-12 22:38:03 Adversarial n=6, triple_ratio: exact incumbent 1.98248779991987, evaluation 91399; witness in k7_search_6_results.json.

2026-11-12 22:38:03 Adversarial n=6, triple_ratio: exact incumbent 1.98253839236173, evaluation 91401; witness in k7_search_6_results.json.

2026-11-12 22:38:03 Adversarial n=6, triple_ratio: exact incumbent 1.98255601939407, evaluation 91404; witness in k7_search_6_results.json.

2026-11-12 22:38:03 Adversarial n=6, triple_ratio: exact incumbent 1.98255601939486, evaluation 91405; witness in k7_search_6_results.json.

2026-11-12 22:38:03 Adversarial n=6, triple_ratio: exact incumbent 1.98255606356177, evaluation 91406; witness in k7_search_6_results.json.

2026-11-12 22:38:04 Adversarial n=6, triple_ratio: exact incumbent 1.9852893399231, evaluation 92740; witness in k7_search_6_results.json.

2026-11-12 22:38:04 Adversarial n=6, triple_ratio: exact incumbent 1.98529094604092, evaluation 92742; witness in k7_search_6_results.json.

2026-11-12 22:38:05 Adversarial n=6, triple_ratio: exact incumbent 1.98614402579314, evaluation 93921; witness in k7_search_6_results.json.

2026-11-12 22:38:07 Adversarial n=6, triple_ratio: exact incumbent 1.98740674176056, evaluation 98169; witness in k7_search_6_results.json.

2026-11-12 22:38:07 Adversarial n=6, triple_ratio: exact incumbent 1.9875080753587, evaluation 98170; witness in k7_search_6_results.json.

2026-11-12 22:38:13 Adversarial n=6, triple_ratio: exact incumbent 1.98791876288841, evaluation 106813; witness in k7_search_6_results.json.

2026-11-12 22:38:13 Adversarial n=6, triple_ratio: exact incumbent 1.98795973737782, evaluation 106823; witness in k7_search_6_results.json.

2026-11-12 22:38:13 Adversarial n=6, triple_ratio: exact incumbent 1.99187150268389, evaluation 106850; witness in k7_search_6_results.json.

2026-11-12 22:38:13 Adversarial n=6, triple_ratio: exact incumbent 1.99187224488299, evaluation 106853; witness in k7_search_6_results.json.

2026-11-12 22:38:13 Adversarial n=6, triple_ratio: exact incumbent 1.99187225441166, evaluation 106855; witness in k7_search_6_results.json.

2026-11-12 22:38:13 Adversarial n=6, triple_ratio: exact incumbent 1.99187225564916, evaluation 106858; witness in k7_search_6_results.json.

2026-11-12 22:38:14 Adversarial n=6, triple_ratio: exact incumbent 1.99704047909269, evaluation 108715; witness in k7_search_6_results.json.

2026-11-12 22:38:41 Adversarial phase n=6 triple ratio finished; 60175 exact evaluations.

2026-11-12 22:38:41 Adversarial n=6, triple_excess: exact incumbent -0.184068433192951, evaluation 148292; witness in k7_search_6_results.json.

2026-11-12 22:38:41 Adversarial n=6, triple_excess: exact incumbent -0.00246826124955125, evaluation 148293; witness in k7_search_6_results.json.

2026-11-12 22:38:41 Adversarial n=6, triple_excess: exact incumbent -0.00242236297018782, evaluation 148304; witness in k7_search_6_results.json.

2026-11-12 22:38:41 Adversarial n=6, triple_excess: exact incumbent -0.00242206251650477, evaluation 148305; witness in k7_search_6_results.json.

2026-11-12 22:38:41 Adversarial n=6, triple_excess: exact incumbent -0.00225892285833845, evaluation 148312; witness in k7_search_6_results.json.

2026-11-12 22:38:41 Adversarial n=6, triple_excess: exact incumbent -0.00116746448784064, evaluation 148316; witness in k7_search_6_results.json.

2026-11-12 22:38:41 Adversarial n=6, triple_excess: exact incumbent -0.00116746444339567, evaluation 148317; witness in k7_search_6_results.json.

2026-11-12 22:38:41 Adversarial n=6, triple_excess: exact incumbent -0.00113515133603402, evaluation 148318; witness in k7_search_6_results.json.

2026-11-12 22:38:41 Adversarial n=6, triple_excess: exact incumbent -0.0011246598952416, evaluation 148319; witness in k7_search_6_results.json.

2026-11-12 22:38:41 Adversarial n=6, triple_excess: exact incumbent -9.17079813445709e-05, evaluation 148339; witness in k7_search_6_results.json.

2026-11-12 22:38:41 Adversarial n=6, triple_excess: exact incumbent -5.65843766537642e-05, evaluation 148340; witness in k7_search_6_results.json.

2026-11-12 22:38:41 Adversarial n=6, triple_excess: exact incumbent -5.65843766536775e-05, evaluation 148341; witness in k7_search_6_results.json.

2026-11-12 22:38:41 Adversarial n=6, triple_excess: exact incumbent -5.65841632467905e-05, evaluation 148344; witness in k7_search_6_results.json.

2026-11-12 22:38:41 Adversarial n=6, triple_excess: exact incumbent -5.58733468682586e-05, evaluation 148348; witness in k7_search_6_results.json.

2026-11-12 22:38:41 Adversarial n=6, triple_excess: exact incumbent -5.58508188749462e-05, evaluation 148349; witness in k7_search_6_results.json.

2026-11-12 22:38:41 Adversarial n=6, triple_excess: exact incumbent -5.74328278265731e-07, evaluation 148358; witness in k7_search_6_results.json.

2026-11-12 22:38:43 Adversarial n=6, triple_excess: exact incumbent -3.11097978346263e-07, evaluation 151967; witness in k7_search_6_results.json.

2026-11-12 22:38:43 Adversarial n=6, triple_excess: exact incumbent -1.07005852911711e-07, evaluation 152037; witness in k7_search_6_results.json.

2026-11-12 22:38:43 Adversarial n=6, triple_excess: exact incumbent -1.07005841401432e-07, evaluation 152038; witness in k7_search_6_results.json.

2026-11-12 22:38:43 Adversarial n=6, triple_excess: exact incumbent -7.59176360288786e-08, evaluation 152039; witness in k7_search_6_results.json.

2026-11-12 22:38:45 Adversarial n=6, triple_excess: exact incumbent -7.18119491027262e-08, evaluation 154950; witness in k7_search_6_results.json.

2026-11-12 22:38:50 Adversarial n=6, triple_excess: exact incumbent -6.34543746162233e-08, evaluation 161492; witness in k7_search_6_results.json.

2026-11-12 22:38:50 Adversarial n=6, triple_excess: exact incumbent -6.22147880241477e-08, evaluation 161493; witness in k7_search_6_results.json.

2026-11-12 22:38:50 Adversarial n=6, triple_excess: exact incumbent -6.22070391669634e-08, evaluation 161494; witness in k7_search_6_results.json.

2026-11-12 22:38:50 Adversarial n=6, triple_excess: exact incumbent -6.13503543732565e-08, evaluation 161496; witness in k7_search_6_results.json.

2026-11-12 22:38:50 Adversarial n=6, triple_excess: exact incumbent -6.09238526086737e-08, evaluation 161500; witness in k7_search_6_results.json.

2026-11-12 22:38:50 Adversarial n=6, triple_excess: exact incumbent -4.19647831951526e-08, evaluation 161502; witness in k7_search_6_results.json.

2026-11-12 22:38:50 Adversarial n=6, triple_excess: exact incumbent -3.56357350480375e-08, evaluation 161503; witness in k7_search_6_results.json.

2026-11-12 22:39:13 Adversarial n=6, triple_excess: exact incumbent -1.3882571805606e-08, evaluation 185764; witness in k7_search_6_results.json.

2026-11-12 22:39:13 Adversarial n=6, triple_excess: exact incumbent -1.3834120362184e-08, evaluation 185766; witness in k7_search_6_results.json.

2026-11-12 22:39:13 Adversarial n=6, triple_excess: exact incumbent -1.35821296935262e-08, evaluation 185767; witness in k7_search_6_results.json.

2026-11-12 22:39:13 Adversarial n=6, triple_excess: exact incumbent -1.18686587576401e-08, evaluation 185768; witness in k7_search_6_results.json.

2026-11-12 22:39:21 Adversarial phase n=6 triple excess finished; 46919 exact evaluations.

2026-11-12 22:39:21 Adversarial n=6 complete: 195210 exact evaluations, 129301 accepted, 160.004s, peak RSS 29786112 bytes.

2026-11-12 22:39:53 Adversarial n=8, pairs_ratio: exact incumbent 2.999991000024, evaluation 1; witness in k7_search_8_results.json.

2026-11-12 22:40:33 Adversarial phase n=8 pairs ratio finished; 14865 exact evaluations.

2026-11-12 22:40:33 Adversarial n=8, pairs_excess: exact incumbent 0.999992000021, evaluation 14866; witness in k7_search_8_results.json.

2026-11-12 22:40:34 Adversarial n=8, pairs_excess: exact incumbent 0.999996917389335, evaluation 15311; witness in k7_search_8_results.json.

2026-11-12 22:40:46 Adversarial n=8, pairs_excess: exact incumbent 0.999998631987815, evaluation 19175; witness in k7_search_8_results.json.

2026-11-12 22:40:46 Adversarial n=8, pairs_excess: exact incumbent 0.999999298777643, evaluation 19207; witness in k7_search_8_results.json.

2026-11-12 22:40:46 Adversarial n=8, pairs_excess: exact incumbent 0.999999298781604, evaluation 19208; witness in k7_search_8_results.json.

2026-11-12 22:40:46 Adversarial n=8, pairs_excess: exact incumbent 0.999999315017591, evaluation 19209; witness in k7_search_8_results.json.

2026-11-12 22:40:46 Adversarial n=8, pairs_excess: exact incumbent 0.999999388732027, evaluation 19214; witness in k7_search_8_results.json.

2026-11-12 22:40:46 Adversarial n=8, pairs_excess: exact incumbent 0.999999389271296, evaluation 19216; witness in k7_search_8_results.json.

2026-11-12 22:41:13 Adversarial phase n=8 pairs excess finished; 14156 exact evaluations.

2026-11-12 22:41:13 Adversarial n=8, triple_ratio: exact incumbent 1.60048247035638, evaluation 29022; witness in k7_search_8_results.json.

2026-11-12 22:41:13 Adversarial n=8, triple_ratio: exact incumbent 1.67706945253669, evaluation 29024; witness in k7_search_8_results.json.

2026-11-12 22:41:13 Adversarial n=8, triple_ratio: exact incumbent 1.6770694531657, evaluation 29031; witness in k7_search_8_results.json.

2026-11-12 22:41:13 Adversarial n=8, triple_ratio: exact incumbent 1.68873802506218, evaluation 29037; witness in k7_search_8_results.json.

2026-11-12 22:41:13 Adversarial n=8, triple_ratio: exact incumbent 1.8235295167134, evaluation 29055; witness in k7_search_8_results.json.

2026-11-12 22:41:13 Adversarial n=8, triple_ratio: exact incumbent 1.82352955644482, evaluation 29058; witness in k7_search_8_results.json.

2026-11-12 22:41:13 Adversarial n=8, triple_ratio: exact incumbent 1.82353622775387, evaluation 29064; witness in k7_search_8_results.json.

2026-11-12 22:41:13 Adversarial n=8, triple_ratio: exact incumbent 1.82421089914029, evaluation 29065; witness in k7_search_8_results.json.

2026-11-12 22:41:13 Adversarial n=8, triple_ratio: exact incumbent 1.8255114191044, evaluation 29082; witness in k7_search_8_results.json.

2026-11-12 22:41:14 Adversarial n=8, triple_ratio: exact incumbent 1.82676588967536, evaluation 29476; witness in k7_search_8_results.json.

2026-11-12 22:41:14 Adversarial n=8, triple_ratio: exact incumbent 1.83766802319324, evaluation 29490; witness in k7_search_8_results.json.

2026-11-12 22:41:14 Adversarial n=8, triple_ratio: exact incumbent 1.83852312716211, evaluation 29494; witness in k7_search_8_results.json.

2026-11-12 22:41:17 Adversarial n=8, triple_ratio: exact incumbent 1.84742263063143, evaluation 30888; witness in k7_search_8_results.json.

2026-11-12 22:41:17 Adversarial n=8, triple_ratio: exact incumbent 1.84743267969439, evaluation 30891; witness in k7_search_8_results.json.

2026-11-12 22:41:17 Adversarial n=8, triple_ratio: exact incumbent 1.8474326924844, evaluation 30892; witness in k7_search_8_results.json.

2026-11-12 22:41:17 Adversarial n=8, triple_ratio: exact incumbent 1.84743605658159, evaluation 30893; witness in k7_search_8_results.json.

2026-11-12 22:41:17 Adversarial n=8, triple_ratio: exact incumbent 1.84752420662677, evaluation 30897; witness in k7_search_8_results.json.

2026-11-12 22:41:17 Adversarial n=8, triple_ratio: exact incumbent 1.84839828539941, evaluation 30905; witness in k7_search_8_results.json.

2026-11-12 22:41:17 Adversarial n=8, triple_ratio: exact incumbent 1.84889868758963, evaluation 30908; witness in k7_search_8_results.json.

2026-11-12 22:41:17 Adversarial n=8, triple_ratio: exact incumbent 1.85172466888524, evaluation 30916; witness in k7_search_8_results.json.

2026-11-12 22:41:17 Adversarial n=8, triple_ratio: exact incumbent 1.85172466920259, evaluation 30923; witness in k7_search_8_results.json.

2026-11-12 22:41:17 Adversarial n=8, triple_ratio: exact incumbent 1.8517453690183, evaluation 30924; witness in k7_search_8_results.json.

2026-11-12 22:41:17 Adversarial n=8, triple_ratio: exact incumbent 1.85174536901831, evaluation 30925; witness in k7_search_8_results.json.

2026-11-12 22:41:17 Adversarial n=8, triple_ratio: exact incumbent 1.85174540498559, evaluation 30933; witness in k7_search_8_results.json.

2026-11-12 22:41:17 Adversarial n=8, triple_ratio: exact incumbent 1.85183229065479, evaluation 30935; witness in k7_search_8_results.json.

2026-11-12 22:41:17 Adversarial n=8, triple_ratio: exact incumbent 1.85296743190409, evaluation 30950; witness in k7_search_8_results.json.

2026-11-12 22:41:25 Adversarial n=8, triple_ratio: exact incumbent 1.85318275911423, evaluation 34813; witness in k7_search_8_results.json.

2026-11-12 22:41:25 Adversarial n=8, triple_ratio: exact incumbent 1.85318275911423, evaluation 34816; witness in k7_search_8_results.json.

2026-11-12 22:41:25 Adversarial n=8, triple_ratio: exact incumbent 1.85318286202414, evaluation 34825; witness in k7_search_8_results.json.

2026-11-12 22:41:25 Adversarial n=8, triple_ratio: exact incumbent 1.85325391144889, evaluation 34826; witness in k7_search_8_results.json.

2026-11-12 22:41:25 Adversarial n=8, triple_ratio: exact incumbent 1.85327895912645, evaluation 34827; witness in k7_search_8_results.json.

2026-11-12 22:41:25 Adversarial n=8, triple_ratio: exact incumbent 1.85328052729161, evaluation 34829; witness in k7_search_8_results.json.

2026-11-12 22:41:33 Adversarial n=8, triple_ratio: exact incumbent 1.91112171328196, evaluation 38742; witness in k7_search_8_results.json.

2026-11-12 22:41:33 Adversarial n=8, triple_ratio: exact incumbent 1.91629096125775, evaluation 38743; witness in k7_search_8_results.json.

2026-11-12 22:41:33 Adversarial n=8, triple_ratio: exact incumbent 1.91646330336232, evaluation 38747; witness in k7_search_8_results.json.

2026-11-12 22:41:33 Adversarial n=8, triple_ratio: exact incumbent 1.91646332382354, evaluation 38748; witness in k7_search_8_results.json.

2026-11-12 22:41:33 Adversarial n=8, triple_ratio: exact incumbent 1.9336988438965, evaluation 38752; witness in k7_search_8_results.json.

2026-11-12 22:41:33 Adversarial n=8, triple_ratio: exact incumbent 1.94247670264099, evaluation 38775; witness in k7_search_8_results.json.

2026-11-12 22:41:33 Adversarial n=8, triple_ratio: exact incumbent 1.95176011602693, evaluation 38777; witness in k7_search_8_results.json.

2026-11-12 22:41:33 Adversarial n=8, triple_ratio: exact incumbent 1.95984156092869, evaluation 38778; witness in k7_search_8_results.json.

2026-11-12 22:41:33 Adversarial n=8, triple_ratio: exact incumbent 1.95984156125522, evaluation 38781; witness in k7_search_8_results.json.

2026-11-12 22:41:33 Adversarial n=8, triple_ratio: exact incumbent 1.95984202749498, evaluation 38782; witness in k7_search_8_results.json.

2026-11-12 22:41:33 Adversarial n=8, triple_ratio: exact incumbent 1.95993434270979, evaluation 38783; witness in k7_search_8_results.json.

2026-11-12 22:41:33 Adversarial n=8, triple_ratio: exact incumbent 1.96834372535806, evaluation 38787; witness in k7_search_8_results.json.

2026-11-12 22:41:48 Adversarial n=8, triple_ratio: exact incumbent 1.96953356294492, evaluation 46196; witness in k7_search_8_results.json.

2026-11-12 22:41:53 Adversarial phase n=8 triple ratio finished; 19608 exact evaluations.

2026-11-12 22:41:53 Adversarial n=8, triple_excess: exact incumbent -0.322466129082961, evaluation 48630; witness in k7_search_8_results.json.

2026-11-12 22:41:53 Adversarial n=8, triple_excess: exact incumbent -0.185307624979487, evaluation 48637; witness in k7_search_8_results.json.

2026-11-12 22:41:53 Adversarial n=8, triple_excess: exact incumbent -0.182762197091734, evaluation 48638; witness in k7_search_8_results.json.

2026-11-12 22:41:53 Adversarial n=8, triple_excess: exact incumbent -0.00161123019075143, evaluation 48643; witness in k7_search_8_results.json.

2026-11-12 22:41:55 Adversarial n=8, triple_excess: exact incumbent -0.00144226247907157, evaluation 49211; witness in k7_search_8_results.json.

2026-11-12 22:41:55 Adversarial n=8, triple_excess: exact incumbent -0.00120393863728743, evaluation 49212; witness in k7_search_8_results.json.

2026-11-12 22:41:55 Adversarial n=8, triple_excess: exact incumbent -0.00120393858462094, evaluation 49213; witness in k7_search_8_results.json.

2026-11-12 22:41:55 Adversarial n=8, triple_excess: exact incumbent -0.00111732043209505, evaluation 49220; witness in k7_search_8_results.json.

2026-11-12 22:41:55 Adversarial n=8, triple_excess: exact incumbent -0.000454321534139701, evaluation 49276; witness in k7_search_8_results.json.

2026-11-12 22:41:55 Adversarial n=8, triple_excess: exact incumbent -0.000408074790361838, evaluation 49277; witness in k7_search_8_results.json.

2026-11-12 22:41:55 Adversarial n=8, triple_excess: exact incumbent -0.000361024183861617, evaluation 49285; witness in k7_search_8_results.json.

2026-11-12 22:41:55 Adversarial n=8, triple_excess: exact incumbent -0.000361024183394962, evaluation 49287; witness in k7_search_8_results.json.

2026-11-12 22:41:55 Adversarial n=8, triple_excess: exact incumbent -0.000361024148154989, evaluation 49288; witness in k7_search_8_results.json.

2026-11-12 22:41:55 Adversarial n=8, triple_excess: exact incumbent -0.000302946397319386, evaluation 49298; witness in k7_search_8_results.json.

2026-11-12 22:41:57 Adversarial n=8, triple_excess: exact incumbent -0.000296247114829446, evaluation 50195; witness in k7_search_8_results.json.

2026-11-12 22:41:57 Adversarial n=8, triple_excess: exact incumbent -0.000296246881150592, evaluation 50197; witness in k7_search_8_results.json.

2026-11-12 22:41:57 Adversarial n=8, triple_excess: exact incumbent -0.000247647473410634, evaluation 50201; witness in k7_search_8_results.json.

2026-11-12 22:41:57 Adversarial n=8, triple_excess: exact incumbent -0.000208548729227457, evaluation 50202; witness in k7_search_8_results.json.

2026-11-12 22:41:58 Adversarial n=8, triple_excess: exact incumbent -0.000119724018829958, evaluation 50647; witness in k7_search_8_results.json.

2026-11-12 22:41:58 Adversarial n=8, triple_excess: exact incumbent -0.000115483496461754, evaluation 50652; witness in k7_search_8_results.json.

2026-11-12 22:41:58 Adversarial n=8, triple_excess: exact incumbent -0.000114833626616555, evaluation 50653; witness in k7_search_8_results.json.

2026-11-12 22:41:58 Adversarial n=8, triple_excess: exact incumbent -0.000114016962336826, evaluation 50655; witness in k7_search_8_results.json.

2026-11-12 22:41:58 Adversarial n=8, triple_excess: exact incumbent -7.67043545494393e-06, evaluation 50656; witness in k7_search_8_results.json.

2026-11-12 22:41:58 Adversarial n=8, triple_excess: exact incumbent -6.88103298655095e-06, evaluation 50664; witness in k7_search_8_results.json.

2026-11-12 22:41:58 Adversarial n=8, triple_excess: exact incumbent -6.82947786492878e-06, evaluation 50666; witness in k7_search_8_results.json.

2026-11-12 22:41:58 Adversarial n=8, triple_excess: exact incumbent -6.29144229311212e-06, evaluation 50682; witness in k7_search_8_results.json.

2026-11-12 22:41:58 Adversarial n=8, triple_excess: exact incumbent -7.72624094359091e-07, evaluation 50686; witness in k7_search_8_results.json.

2026-11-12 22:42:09 Adversarial n=8, triple_excess: exact incumbent -2.37820556253123e-07, evaluation 56094; witness in k7_search_8_results.json.

2026-11-12 22:42:09 Adversarial n=8, triple_excess: exact incumbent -2.00664762166908e-07, evaluation 56095; witness in k7_search_8_results.json.

2026-11-12 22:42:09 Adversarial n=8, triple_excess: exact incumbent -2.00664742291447e-07, evaluation 56096; witness in k7_search_8_results.json.

2026-11-12 22:42:33 Adversarial phase n=8 triple excess finished; 18618 exact evaluations.

2026-11-12 22:42:33 Adversarial n=8 complete: 67247 exact evaluations, 46573 accepted, 160.003s, peak RSS 28508160 bytes.

2026-11-12 22:42:45 Exact lead audit: diagonal_family; details saved in k7_leads_results.json.

2026-11-12 22:42:45 Exact lead audit: intermediate_row_sum_exceeds_proposed_budget; details saved in k7_leads_results.json.

2026-11-12 22:42:45 Exact lead audit: removing_orthogonal_boundary_part_loses_nonnegativity; details saved in k7_leads_results.json.

2026-11-12 22:42:46 Exact lead audit: cauchy_schwarz_bound_exceeds_3T; details saved in k7_leads_results.json.

2026-11-12 22:42:50 Lead audit complete: 29400 singleton-pair tests, 4.660s, peak RSS 28868608 bytes.

2026-11-12 22:44:56 Orthogonal minimum refinement audit passed: 65600 orientations, 16.477s, peak RSS 29229056 bytes. This audits a conditional inequality, not factor 3.

2026-11-12 22:45:22 Fork prequotient 7_triple_ratio: 0.909016515804423; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_triple_excess: -0.181811549569214; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_triple_ratio: 1.7272051480466; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_triple_excess: -0.181656151239833; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_ratio: -327273.807182803; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_excess: -327275.716199501; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_ratio: -327273.807150076; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_excess: -327275.716166773; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_excess: -327275.625183471; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_ratio: -326950.828879911; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_excess: -326951.919707976; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_ratio: -326950.828847215; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_excess: -326951.919675281; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_ratio: -326947.585943318; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_excess: -326948.676771383; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_ratio: -326946.767754686; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_triple_excess: -0.181656151231544; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_ratio: 1.72720514803859; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_excess: -0.181811549577232; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_ratio: 1.72720514806633; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_excess: -0.181811549566839; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_ratio: 1.72720516850221; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_excess: -0.181811529113609; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_ratio: 1.7273606289386; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_excess: -0.18165606867722; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_triple_excess: -0.181656151223354; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_triple_ratio: 1.7273597494776; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_excess: -0.181012135314988; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_ratio: 1.72800456230083; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_excess: 0.544749986541803; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_ratio: 2.45449316300865; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_excess: 0.545476465392827; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_ratio: 2.45449539178582; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_pairs_excess: 0.545477868684262; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_triple_excess: -0.181565467626494; exact witness saved.

2026-11-12 22:45:22 Fork prequotient 7_triple_ratio: 1.72736131810963; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.161784968620232; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.1609467534295; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.1609467534295; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.153343429709011; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.152420563318484; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.105636295784793; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.105173458449837; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.101319615888207; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.100370750123425; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_ratio: 1.72743198601231; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_ratio: 1.72750462010064; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_pairs_ratio: 2.45491864606596; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_pairs_excess: 0.545744338275112; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_ratio: 1.73252351108251; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_ratio: 1.733421881872; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_ratio: 1.74159857875217; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_ratio: 1.74159857882618; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_pairs_ratio: 2.47502043999894; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_pairs_excess: 0.558428632021853; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_ratio: 1.74159864357107; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.001998001998001; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_ratio: 1.997002997002; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.001998001996006; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.001998001996006; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.001998001996006; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_ratio: 1.997002997004; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_pairs_excess: 0.995004994007995; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_pairs_ratio: 2.994005994005; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_pairs_excess: 0.995004995004998; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_pairs_ratio: 2.994005994005; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_pairs_excess: 0.995004995004998; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.00199800199500699; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_ratio: 1.997002997004; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.00199501495911269; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.0019950139611077; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.0019950139611077; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.00199401695313263; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.00199401595412964; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.00100050074887494; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.00100050024912606; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.00100000149800225; exact witness saved.

2026-11-12 22:45:23 Fork prequotient 7_triple_excess: -0.00100000049850225; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_triple_ratio: 1.99700299700499; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_triple_ratio: 1.99700299700599; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_pairs_ratio: 2.99400599401098; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_pairs_excess: 0.995004995008982; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_triple_ratio: 1.99700399101797; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_triple_ratio: 1.99700399201697; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_triple_ratio: 1.99700499001896; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_triple_ratio: 1.99700499001896; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_pairs_ratio: 2.99400898203593; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_pairs_excess: 0.995006986028944; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_triple_ratio: 1.99700499001896; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_triple_excess: -1.999998000002e-06; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_triple_ratio: 1.999997000003; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_triple_excess: -1.999998000002e-06; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_triple_excess: -1.999998000002e-06; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_triple_excess: -1.999998000002e-06; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_triple_ratio: 1.999997000003; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_pairs_excess: 0.999995000005; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_pairs_ratio: 2.999994000006; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_pairs_excess: 0.999995000005; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_pairs_ratio: 2.999994000006; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_pairs_excess: 0.999995000005; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_triple_excess: -1.999998000002e-06; exact witness saved.

2026-11-12 22:45:24 Fork prequotient 7_triple_ratio: 1.999997000003; exact witness saved.

2026-11-12 22:45:25 Fork prequotient 7_triple_excess: -1.999995000015e-06; exact witness saved.

2026-11-12 22:45:25 Fork prequotient 7_triple_excess: -1.999995000014e-06; exact witness saved.

2026-11-12 22:45:25 Fork prequotient 7_triple_excess: -1.999995000014e-06; exact witness saved.

2026-11-12 22:45:25 Fork prequotient 7_triple_excess: -1.999994000017e-06; exact witness saved.

2026-11-12 22:45:25 Fork prequotient 7_triple_excess: -1.999994000016e-06; exact witness saved.

2026-11-12 22:45:25 Fork prequotient 7_triple_excess: -1.00000050000075e-06; exact witness saved.

2026-11-12 22:45:25 Fork prequotient 7_triple_excess: -1.00000050000025e-06; exact witness saved.

2026-11-12 22:45:25 Fork prequotient 7_triple_excess: -1.0000000000015e-06; exact witness saved.

2026-11-12 22:45:25 Fork prequotient 7_triple_excess: -1.0000000000005e-06; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 7_triple_ratio: 1.999997000003; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 7_triple_ratio: 1.999997000003; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 7_pairs_ratio: 2.999994000006; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 7_pairs_excess: 0.999995000005; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 7_triple_ratio: 1.999997000004; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 7_triple_ratio: 1.999997000004; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 7_triple_ratio: 1.999997000005; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 7_triple_ratio: 1.999997000005; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 7_pairs_ratio: 2.999994000009; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 7_pairs_excess: 0.999995000007; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 7_triple_ratio: 1.999997000005; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_triple_ratio: 0.090414987288682; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_triple_excess: -0.507695386536864; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_triple_ratio: 0.497282481455356; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_triple_excess: -0.507198104043993; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_triple_ratio: 0.954295218155277; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_pairs_ratio: -180829.070057535; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_pairs_excess: -180830.074538121; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_pairs_ratio: 0.954295168436015; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_pairs_excess: -1.00000004971926; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_pairs_excess: -0.999999999999999; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_pairs_excess: -0.507198104043993; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_triple_excess: -0.507198104043993; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_triple_excess: -0.507198104043982; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_pairs_excess: -0.13777063888599; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_pairs_ratio: 0.954295218064965; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_triple_ratio: 0.954295218155288; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_pairs_ratio: 0.954335365597526; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_triple_ratio: 1.35618478329816; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_triple_ratio: 6.66655555185062e-05; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_triple_excess: -0.999966668888963; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_triple_ratio: 0.333344444814938; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_triple_ratio: 0.333377775925975; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_triple_ratio: 0.666655555185395; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_triple_ratio: 0.666688886296432; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_pairs_ratio: 0.333344444814938; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_pairs_excess: -1; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_pairs_ratio: 0.999966665555852; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_pairs_excess: -0.666688889629876; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_triple_ratio: 0.666688889629543; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_triple_ratio: 0.666688889629543; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_triple_ratio: 0.999966665555852; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_triple_excess: -0.666688889629877; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_triple_excess: -0.666688889629876; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_triple_ratio: 0.999966665555852; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_pairs_ratio: 0.999966665555852; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_pairs_ratio: 0.999966665555852; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_triple_ratio: 0.999966665555852; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_triple_ratio: 0.999966665555852; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_pairs_ratio: 0.999966665555852; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_pairs_excess: -0.666688889629876; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_pairs_ratio: 1.33321111703668; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_pairs_excess: -0.333444438148716; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_triple_ratio: 1; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 8_pairs_ratio: 1.33324445148116; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_triple_excess: -0.000199960010997201; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_triple_excess: -0.000199960009997401; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_pairs_ratio: 0.999800049987003; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_pairs_excess: -0.000199960009997401; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_pairs_ratio: 0.999800049987003; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_triple_ratio: 1.99940013996401; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_triple_excess: -0.000199960009997401; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_triple_ratio: 1.99950011996901; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_pairs_ratio: 1.99950011996901; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_triple_excess: -0.000199960009997401; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_pairs_excess: 0.999300189949013; exact witness saved.

2026-11-12 22:45:26 Fork prequotient 6_pairs_ratio: 2.38879451451937; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_triple_excess: -0.0003999600019999; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_triple_excess: -0.0003999600019999; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_triple_excess: -0.0001999900009998; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_triple_ratio: 1.999700019998; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_triple_ratio: 1.999700029997; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_pairs_excess: -0.0003999600010001; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_pairs_excess: -0.0001999800019998; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_pairs_ratio: 1.999700029997; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_triple_ratio: 1.999700029997; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_triple_excess: -0.0001999800019998; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_triple_excess: -0.0001999800019996; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_triple_excess: -0.0001999800019996; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_triple_ratio: 1.999700029997; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_pairs_ratio: 1.999800009998; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_pairs_excess: 0.999400059995; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_pairs_excess: 0.999400059995001; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_pairs_excess: 0.999400079991001; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_pairs_ratio: 2.999300099987; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_pairs_excess: 0.999400089988002; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_pairs_excess: 0.999400089988002; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_triple_excess: -0.00010000000000005; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_triple_excess: -9.99999990001e-05; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_triple_excess: -9.99999990001e-05; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_triple_excess: -9.99999990001e-05; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_triple_excess: -9.99999990001e-05; exact witness saved.

2026-11-12 22:45:27 Fork prequotient 8_pairs_excess: 0.999400129967008; exact witness saved.

2026-11-12 22:45:28 Fork prequotient 6_pairs_ratio: 2.93156379277102; exact witness saved.

2026-11-12 22:45:28 Fork prequotient 6_pairs_ratio: 2.94117354825259; exact witness saved.

2026-11-12 22:45:28 Fork prequotient 6_triple_ratio: 1.9998; exact witness saved.

2026-11-12 22:45:28 Fork prequotient 6_triple_ratio: 1.9998; exact witness saved.

2026-11-12 22:45:28 Fork prequotient 6_pairs_excess: 0.999599999999; exact witness saved.

2026-11-12 22:45:29 Fork prequotient 6_triple_excess: -0.000198169150521273; exact witness saved.

2026-11-12 22:45:29 Fork prequotient 6_triple_excess: -0.000100005000249913; exact witness saved.

2026-11-12 22:45:29 Fork prequotient 6_triple_excess: -0.000100005000249913; exact witness saved.

2026-11-12 22:45:29 Fork prequotient 6_triple_excess: -0.000100005000249913; exact witness saved.

2026-11-12 22:45:30 Fork prequotient 8_pairs_excess: 0.999500049995; exact witness saved.

2026-11-12 22:45:30 Fork prequotient 8_pairs_ratio: 2.999400059994; exact witness saved.

2026-11-12 22:45:30 Fork prequotient 8_triple_ratio: 1.999700029997; exact witness saved.

2026-11-12 22:45:30 Fork prequotient 8_pairs_ratio: 2.999400059994; exact witness saved.

2026-11-12 22:45:30 Fork prequotient 8_pairs_excess: 0.999500049995001; exact witness saved.

2026-11-12 22:45:33 Fork prequotient 6_pairs_ratio: 2.95941991471107; exact witness saved.

2026-11-12 22:45:33 Fork prequotient 6_pairs_ratio: 2.999400059994; exact witness saved.

2026-11-12 22:45:34 Fork prequotient 8_triple_ratio: 1.999700029997; exact witness saved.

2026-11-12 22:45:34 Fork prequotient 8_pairs_ratio: 2.999400059994; exact witness saved.

2026-11-12 22:45:34 Fork prequotient 8_pairs_excess: 0.999500049995001; exact witness saved.

2026-11-12 22:45:34 Fork prequotient 8_triple_ratio: 1.999700029997; exact witness saved.

2026-11-12 22:45:34 Fork prequotient 8_triple_ratio: 1.999700029997; exact witness saved.

2026-11-12 22:45:36 Fork prequotient 6_triple_excess: -0.000100005000249863; exact witness saved.

2026-11-12 22:45:36 Fork prequotient 6_triple_excess: -0.000100005000249863; exact witness saved.

2026-11-12 22:45:36 Fork prequotient 6_triple_excess: -0.000100005000249863; exact witness saved.

2026-11-12 22:45:37 Fork prequotient 6_pairs_ratio: 2.99940011997301; exact witness saved.

2026-11-12 22:45:39 Fork prequotient 6_triple_ratio: 1.9998; exact witness saved.

2026-11-12 22:45:40 Fork prequotient 6_triple_ratio: 1.9998; exact witness saved.

2026-11-12 22:45:42 Fork prequotient 6_triple_excess: -0.000100005000249862; exact witness saved.

2026-11-12 22:45:42 Fork prequotient 6_triple_excess: -0.000100005000249862; exact witness saved.

2026-11-12 22:45:43 Fork prequotient 6_pairs_excess: 0.9996; exact witness saved.

2026-11-12 22:45:44 Fork prequotient 6_triple_excess: -0.00010000000099995; exact witness saved.

2026-11-12 22:45:44 Fork prequotient 8_triple_excess: -9.9999999e-05; exact witness saved.

2026-11-12 22:45:44 Fork prequotient 8_triple_excess: -9.9999999e-05; exact witness saved.

2026-11-12 22:45:44 Fork prequotient 8_triple_ratio: 1.999700029997; exact witness saved.

2026-11-12 22:45:44 Fork prequotient 8_triple_ratio: 1.999700029997; exact witness saved.

2026-11-12 22:45:44 Fork prequotient 8_triple_ratio: 1.999700029997; exact witness saved.

2026-11-12 22:45:44 Fork prequotient 8_pairs_ratio: 2.999400059994; exact witness saved.

2026-11-12 22:45:44 Fork prequotient 8_pairs_excess: 0.999500049995001; exact witness saved.

2026-11-12 22:45:48 Fork prequotient 6_triple_excess: -1.999999999998e-08; exact witness saved.

2026-11-12 22:45:48 Fork prequotient 6_triple_excess: -1.999999980001e-08; exact witness saved.

2026-11-12 22:45:48 Fork prequotient 6_triple_ratio: 1.9998; exact witness saved.

2026-11-12 22:45:48 Fork prequotient 6_pairs_excess: 0.999699999999; exact witness saved.

2026-11-12 22:45:55 Fork prequotient 7_triple_excess: -5.40653128040693e-07; exact witness saved.

2026-11-12 22:45:55 Fork prequotient 7_triple_excess: -5.40653128040685e-07; exact witness saved.

2026-11-12 22:45:57 Fork prequotient 8_triple_excess: -6.66733326666556e-05; exact witness saved.

2026-11-12 22:45:57 Fork prequotient 8_triple_excess: -6.66733326665556e-05; exact witness saved.

2026-11-12 22:45:57 Fork prequotient 8_triple_excess: -6.66733326665556e-05; exact witness saved.

2026-11-12 22:45:59 Fork prequotient 7_triple_excess: -1.999999979999e-08; exact witness saved.

2026-11-12 22:45:59 Fork prequotient 7_triple_excess: -1e-08; exact witness saved.

2026-11-12 22:45:59 Fork prequotient 7_triple_excess: -1e-08; exact witness saved.

2026-11-12 22:45:59 Fork prequotient 7_triple_excess: -9.99999999999e-13; exact witness saved.

2026-11-12 22:45:59 Fork prequotient 7_triple_excess: -9.99999999999e-13; exact witness saved.

2026-11-12 22:45:59 Fork prequotient 7_triple_excess: -1.9999000099956e-16; exact witness saved.

2026-11-12 22:46:02 Fork prequotient 6_pairs_ratio: 2.99959994002; exact witness saved.

2026-11-12 22:46:06 Fork prequotient 6_triple_excess: -1.98029093229111e-08; exact witness saved.

2026-11-12 22:46:14 Fork prequotient 6_pairs_ratio: 2.999599940022; exact witness saved.

2026-11-12 22:46:24 Fork prequotient 8_triple_ratio: 1.999800009999; exact witness saved.

2026-11-12 22:46:24 Fork prequotient 8_triple_ratio: 1.99980001; exact witness saved.

2026-11-12 22:46:24 Fork prequotient 8_pairs_ratio: 2.999500049995; exact witness saved.

2026-11-12 22:46:24 Fork prequotient 8_pairs_excess: 0.999500059993001; exact witness saved.

2026-11-12 22:46:24 Fork prequotient 8_triple_ratio: 1.999800019998; exact witness saved.

2026-11-12 22:46:25 Fork prequotient 8_pairs_excess: 0.999600049994001; exact witness saved.

2026-11-12 22:46:28 Fork prequotient 8_pairs_excess: 0.999799985001; exact witness saved.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 0.674385633735628; exact witness saved.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 0.894126188240038; exact witness saved.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 0.972738343546542; exact witness saved.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.04604269972566; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.07091644640696; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.08119994266894; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.08119994940517; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.08122599091606; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.08122599091674; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.08122599091734; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.26289967341949; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.2631615017176; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.26316181550716; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.69668861870672; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.74086015742576; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.74086026042792; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.74086026044716; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.74112162082595; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.98123636378786; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.98123681535104; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.98140690269572; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.98140690269732; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:39 Orthogonal minimum adversary: best-orientation error 1.98140730913891; exact witness saved.

2026-11-12 22:46:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:40 Orthogonal minimum adversary: best-orientation error 1.98220794990075; exact witness saved.

2026-11-12 22:46:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:40 Orthogonal minimum adversary: best-orientation error 1.98221773549687; exact witness saved.

2026-11-12 22:46:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:40 Orthogonal minimum adversary: best-orientation error 1.98266289415039; exact witness saved.

2026-11-12 22:46:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:40 Orthogonal minimum adversary: best-orientation error 1.98619647811661; exact witness saved.

2026-11-12 22:46:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:40 Orthogonal minimum adversary: best-orientation error 1.98622220486006; exact witness saved.

2026-11-12 22:46:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:40 Orthogonal minimum adversary: best-orientation error 1.98625974692545; exact witness saved.

2026-11-12 22:46:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:40 Orthogonal minimum adversary: best-orientation error 1.98625974692546; exact witness saved.

2026-11-12 22:46:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:40 Fork prequotient 8_triple_ratio: 1.999800029995; exact witness saved.

2026-11-12 22:46:40 Fork prequotient 8_pairs_ratio: 2.999500069988; exact witness saved.

2026-11-12 22:46:40 Fork prequotient 8_triple_ratio: 1.999800029996; exact witness saved.

2026-11-12 22:46:40 Fork prequotient 8_pairs_ratio: 2.999500079987; exact witness saved.

2026-11-12 22:46:40 Fork prequotient 8_triple_ratio: 1.999800029996; exact witness saved.

2026-11-12 22:46:40 Fork prequotient 8_pairs_ratio: 2.999500079987; exact witness saved.

2026-11-12 22:46:40 Orthogonal minimum adversary: best-orientation error 1.98637145548924; exact witness saved.

2026-11-12 22:46:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:40 Orthogonal minimum adversary: best-orientation error 1.98637416923546; exact witness saved.

2026-11-12 22:46:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:40 Orthogonal minimum adversary: best-orientation error 1.98637417102158; exact witness saved.

2026-11-12 22:46:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.98646466188089; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.9864649263683; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.98830507020828; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.98830521347795; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.98830699920339; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.98859653878374; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.98887508981825; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.98893102829052; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.98896505740845; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.98925970103536; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.98996588655302; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.9900799300128; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.99007993002456; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.99173153552854; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.9935186988828; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.9935194303514; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.99352198777352; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.99352759336882; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:41 Orthogonal minimum adversary: best-orientation error 1.99356519348208; exact witness saved.

2026-11-12 22:46:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 1.99369631367016; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 1.99369666335471; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 1.99536684044754; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 1.99585403452556; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 1.99609099404083; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 1.99609103005835; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 1.99654464532616; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 1.99654506078527; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 1.99654543469862; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 1.99654547208997; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 1.99668591983558; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 1.99781667947117; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 2.06902712840421; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 2.06906722977986; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 2.06923440445782; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 2.07177366596646; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 2.07183137469224; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 2.07184918147232; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 2.07192628291636; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:42 Orthogonal minimum adversary: best-orientation error 2.07198583233531; exact witness saved.

2026-11-12 22:46:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 2.07719918662052; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 2.0775482541223; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 2.07759366890257; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 2.07759402988808; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 2.79538203220059; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 2.79538203220323; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 2.7954406340826; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 3.32983872620757; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 3.32983872999613; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 3.32983882151289; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 3.33432444534588; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 3.33433452178002; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 3.33433938669309; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 3.33450015345722; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 3.33694627969119; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 24.24465806927; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 24.2492721498456; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 24.2492721498718; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 24.2492769391135; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 24.2492778768273; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 24.249312184235; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 24.2493503671635; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 24.2532104218617; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 24.2540799828982; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 24.2541407019385; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 24.2541407160037; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 221.549785123896; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 221.549791432086; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 221.549791432125; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 222.236512706535; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:43 Orthogonal minimum adversary: best-orientation error 222.236553892372; exact witness saved.

2026-11-12 22:46:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 222.236553892914; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 262.555339164261; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 262.555339164299; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 262.555339173612; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 262.555339173613; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 315.906701699419; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 315.906701699433; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 315.906701714484; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 315.915846520665; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 349.683697282099; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 349.684337252905; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 349.792792356918; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 349.806663279196; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 349.808047452548; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 349.809788322961; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 365.865838768939; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 365.865842073826; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 365.867328479493; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 365.867328483131; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 366.171283644738; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 366.198085577187; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 366.606442547008; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 366.94640705556; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 368.89459569133; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 368.960936836616; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 368.963270107535; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 369.151847240916; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 369.18598058126; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 374.441760061824; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 374.461998861842; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 374.461998865832; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 374.632090930674; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 528.654403120586; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 528.654448650135; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 528.963698441194; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 532.802479498631; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 533.246181806456; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 533.246181806456; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 533.24620893154; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 533.426996943602; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 533.968998940314; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Fork prequotient 6_triple_excess: -5.00025001249563e-13; exact witness saved.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 534.013520095217; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:44 Orthogonal minimum adversary: best-orientation error 534.080903203437; exact witness saved.

2026-11-12 22:46:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 534.081288347204; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 534.104101680562; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 534.104101680685; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 534.137801527389; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 534.465278508922; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 565.444833605375; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 565.444838859224; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 566.588241261048; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 566.588245497174; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 566.588245497198; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 566.588384280469; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 566.691532150786; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 567.359267043398; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 567.546551865413; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 567.546551865458; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 568.888078314192; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 568.888078314192; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 667.012710284307; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 672.741347550155; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 672.84468872403; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 690.785278984116; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 690.829240174821; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 690.829279859287; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 690.829279919663; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 690.829279919748; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 690.967640428295; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 690.967640429154; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 690.96764045824; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 690.967640458826; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 719.375907217294; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 719.49064958621; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 720.517652950607; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 720.626488860621; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 720.626488860634; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 720.626489821429; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 720.62648982143; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 720.628664776864; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:45 Orthogonal minimum adversary: best-orientation error 720.631420806353; exact witness saved.

2026-11-12 22:46:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 721.024755173722; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 723.027479399852; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 775.856457358242; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 775.856612708041; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 775.857158824014; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 775.857359439315; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 788.500526823028; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 788.580636659422; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 942.310144280145; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 948.150742817933; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 959.889119968099; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 959.891551514414; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 959.891551514414; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2467.65830217745; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2467.70352936524; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2467.71014265592; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2467.71014265593; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2467.71019297133; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2470.38417551247; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2470.38417697887; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2470.38417717226; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2470.9043446946; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2472.38325672869; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2472.48796806091; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2478.32632646402; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2513.16604070069; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2513.16856998746; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2513.74039245056; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2517.5007568712; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2517.5007568712; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2517.6256340843; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2517.6574591113; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2517.65745911211; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2518.72699724046; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2518.72699724119; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2520.54713962175; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2520.54713962176; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2524.48240816069; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2525.84481425064; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2525.88661325598; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2525.8866132573; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2529.06357148691; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2533.87317654463; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2533.87317655256; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2533.87317655335; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2533.8731765785; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2533.87317657966; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2573.50407383724; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2576.29019810581; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2576.29019810581; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:46 Orthogonal minimum adversary: best-orientation error 2576.29019810581; exact witness saved.

2026-11-12 22:46:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2576.29020248901; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2655.59423938897; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2655.59424235396; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2658.27801673956; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2658.2783178612; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2658.27887511416; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2658.27887511417; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2658.27887523473; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2658.27927517768; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2658.28720642407; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2658.28748556987; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2658.2876251428; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2658.29194651654; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2658.95360487356; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2659.02616921905; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2659.02629498614; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2659.02652201135; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 2659.02652680583; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 4091.84183882391; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 4091.84201806668; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 4092.07104835287; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 4092.07105841439; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:47 Orthogonal minimum adversary: best-orientation error 4092.09330981287; exact witness saved.

2026-11-12 22:46:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 4092.12932462401; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 4092.12932579606; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 4092.12932579606; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 4092.12932586117; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 4092.12932586117; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 4092.13108215705; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 4092.13108299676; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 4092.13124036481; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 4092.13189048596; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 5678.93711439724; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 5678.95447362149; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 5678.95447379863; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 5678.95469147577; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 8736.10152494073; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 8747.10498170825; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 8747.10503817606; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 8834.42217945889; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 8835.91985592359; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 8866.81781457808; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 8866.81792509135; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 14300.3674688437; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 14300.3674688437; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:48 Orthogonal minimum adversary: best-orientation error 14300.3674688598; exact witness saved.

2026-11-12 22:46:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 14322.1088102811; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 14324.8912395289; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 14911.6912383822; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 14917.7429148681; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 15005.2666655177; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 15147.2126470774; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 15158.4554647625; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 17712.7748222875; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22688.0659232214; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22688.065968973; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22688.065968973; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22714.9449834338; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22714.9449834348; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.6955735933; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.7146364469; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.7146640764; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.7146640764; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.7146681442; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.7146681766; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.7151869421; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.726583986; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.726583987; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.7272970976; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.7531790995; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.7531790995; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.772801806; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.7736128769; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.7736143183; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.7736954407; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.7736954407; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.773696737; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.8805383893; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.8805383893; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22716.8806926366; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22717.7597783214; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:49 Orthogonal minimum adversary: best-orientation error 22717.7667740663; exact witness saved.

2026-11-12 22:46:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 22717.7667742968; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 26390.9792529784; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 26404.8193292195; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 26404.8193292195; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 26404.8753684005; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 27960.3393953333; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 28052.1450580592; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 28052.1450585771; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 28453.9142577573; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 28477.8865118138; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 28477.8865118138; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32673.0719419838; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32678.2331358059; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32678.2331359466; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32678.2331359466; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32678.2331359466; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32680.8137867681; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32680.8140603263; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32680.8140603263; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32680.8144320904; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32680.8144545648; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32680.8144620127; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32680.8144657366; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32680.8146558526; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32680.8146558526; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32681.5401192184; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32681.5404493784; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32681.5404497433; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32682.8221386332; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32682.9086074266; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32683.759186469; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32684.0074229482; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32684.007661; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:50 Orthogonal minimum adversary: best-orientation error 32684.0076613702; exact witness saved.

2026-11-12 22:46:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32684.0375013244; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32685.9352420635; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32692.7520727745; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32692.7520727836; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32692.7520727842; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32692.7872483179; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32692.9072780732; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32692.9072782329; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32766.2299925191; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32766.2300144131; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32772.8021142465; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32783.9788160391; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32790.5256836744; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32790.5315722107; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32790.5321610956; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32790.711889099; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32790.7118894763; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32790.72957898; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:51 Orthogonal minimum adversary: best-orientation error 32792.5110924857; exact witness saved.

2026-11-12 22:46:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 32793.4215163499; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 32793.4215163499; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 32793.4803069957; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 32794.1567427328; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 32794.1801316493; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 32797.9498471674; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 32797.9514202759; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 32797.9522068445; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 32797.9522068445; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 32799.9230852545; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 32799.923085692; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 32799.9266892419; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 32799.9285344545; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 33531.5897510345; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 33531.5897511412; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 33600.1779024782; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 33600.1895156101; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 33600.1895156349; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 33674.9910990958; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 33674.991099096; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 33737.4700046165; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 33737.4938952021; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 33771.7400325424; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 33771.7400325424; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 33771.7400325765; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 33771.7400961557; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 33789.7001952657; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:52 Orthogonal minimum adversary: best-orientation error 33789.7001952661; exact witness saved.

2026-11-12 22:46:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:53 Orthogonal minimum adversary: best-orientation error 33789.7055735959; exact witness saved.

2026-11-12 22:46:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:53 Orthogonal minimum adversary: best-orientation error 33789.7055800616; exact witness saved.

2026-11-12 22:46:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:53 Orthogonal minimum adversary: best-orientation error 33789.7056087426; exact witness saved.

2026-11-12 22:46:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:53 Orthogonal minimum adversary: best-orientation error 33789.7078230786; exact witness saved.

2026-11-12 22:46:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:53 Orthogonal minimum adversary: best-orientation error 33789.7143172974; exact witness saved.

2026-11-12 22:46:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:53 Orthogonal minimum adversary: best-orientation error 33789.7143172974; exact witness saved.

2026-11-12 22:46:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:53 Orthogonal minimum adversary: best-orientation error 33789.7143172974; exact witness saved.

2026-11-12 22:46:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:53 Orthogonal minimum adversary: best-orientation error 33789.7143172974; exact witness saved.

2026-11-12 22:46:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:53 Orthogonal minimum adversary: best-orientation error 33789.7143189397; exact witness saved.

2026-11-12 22:46:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:53 Orthogonal minimum adversary: best-orientation error 33789.7143190309; exact witness saved.

2026-11-12 22:46:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:53 Orthogonal minimum adversary: best-orientation error 33789.7192782005; exact witness saved.

2026-11-12 22:46:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:54 Orthogonal minimum adversary: best-orientation error 33789.7192782008; exact witness saved.

2026-11-12 22:46:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:54 Orthogonal minimum adversary: best-orientation error 33789.719278362; exact witness saved.

2026-11-12 22:46:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:54 Orthogonal minimum adversary: best-orientation error 33789.7365162673; exact witness saved.

2026-11-12 22:46:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:54 Orthogonal minimum adversary: best-orientation error 33789.7365163494; exact witness saved.

2026-11-12 22:46:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:54 Orthogonal minimum adversary: best-orientation error 33789.7411660163; exact witness saved.

2026-11-12 22:46:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:54 Orthogonal minimum adversary: best-orientation error 33789.7411660245; exact witness saved.

2026-11-12 22:46:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:54 Orthogonal minimum adversary: best-orientation error 33806.4064507059; exact witness saved.

2026-11-12 22:46:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:54 Orthogonal minimum adversary: best-orientation error 33806.4092206261; exact witness saved.

2026-11-12 22:46:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:54 Orthogonal minimum adversary: best-orientation error 33806.4093580977; exact witness saved.

2026-11-12 22:46:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:54 Orthogonal minimum adversary: best-orientation error 33806.4097116324; exact witness saved.

2026-11-12 22:46:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:54 Orthogonal minimum adversary: best-orientation error 33806.409713512; exact witness saved.

2026-11-12 22:46:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:54 Orthogonal minimum adversary: best-orientation error 33806.409990505; exact witness saved.

2026-11-12 22:46:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:54 Orthogonal minimum adversary: best-orientation error 33808.1046353388; exact witness saved.

2026-11-12 22:46:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.1902819503; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.1932656669; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.1932948975; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.2019857617; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.2034946179; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.2506483887; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.2508148996; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.2508412085; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.2508438394; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.4566539516; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.4566542147; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.4991112961; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.4991301605; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.5069561032; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.5069561032; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.5073908826; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:55 Orthogonal minimum adversary: best-orientation error 33808.5073908826; exact witness saved.

2026-11-12 22:46:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:56 Orthogonal minimum adversary: best-orientation error 33808.5080100426; exact witness saved.

2026-11-12 22:46:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:56 Orthogonal minimum adversary: best-orientation error 33808.5085997543; exact witness saved.

2026-11-12 22:46:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:56 Orthogonal minimum adversary: best-orientation error 33808.5096251356; exact witness saved.

2026-11-12 22:46:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:56 Orthogonal minimum adversary: best-orientation error 33810.5721681032; exact witness saved.

2026-11-12 22:46:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:56 Orthogonal minimum adversary: best-orientation error 33810.5722627688; exact witness saved.

2026-11-12 22:46:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:56 Orthogonal minimum adversary: best-orientation error 33810.5723100753; exact witness saved.

2026-11-12 22:46:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:56 Orthogonal minimum adversary: best-orientation error 33810.5742736832; exact witness saved.

2026-11-12 22:46:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:56 Orthogonal minimum adversary: best-orientation error 33810.5757538754; exact witness saved.

2026-11-12 22:46:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:56 Orthogonal minimum adversary: best-orientation error 33831.6332260874; exact witness saved.

2026-11-12 22:46:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:56 Orthogonal minimum adversary: best-orientation error 33831.633533032; exact witness saved.

2026-11-12 22:46:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:57 Orthogonal minimum adversary: best-orientation error 33831.6335330335; exact witness saved.

2026-11-12 22:46:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:57 Orthogonal minimum adversary: best-orientation error 33831.6346645462; exact witness saved.

2026-11-12 22:46:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:57 Orthogonal minimum adversary: best-orientation error 33831.6346645462; exact witness saved.

2026-11-12 22:46:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:57 Orthogonal minimum adversary: best-orientation error 33831.6348513694; exact witness saved.

2026-11-12 22:46:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:57 Orthogonal minimum adversary: best-orientation error 33831.6348545851; exact witness saved.

2026-11-12 22:46:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:57 Orthogonal minimum adversary: best-orientation error 33831.6348590036; exact witness saved.

2026-11-12 22:46:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:57 Orthogonal minimum adversary: best-orientation error 33831.6369999762; exact witness saved.

2026-11-12 22:46:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:57 Orthogonal minimum adversary: best-orientation error 33831.6369999795; exact witness saved.

2026-11-12 22:46:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:57 Orthogonal minimum adversary: best-orientation error 33831.6372762313; exact witness saved.

2026-11-12 22:46:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:57 Orthogonal minimum adversary: best-orientation error 33831.6372818889; exact witness saved.

2026-11-12 22:46:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:57 Orthogonal minimum adversary: best-orientation error 33831.6374004916; exact witness saved.

2026-11-12 22:46:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:58 Orthogonal minimum adversary: best-orientation error 33831.6374033857; exact witness saved.

2026-11-12 22:46:58 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:58 Orthogonal minimum adversary: best-orientation error 33831.6404434014; exact witness saved.

2026-11-12 22:46:58 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:58 Orthogonal minimum adversary: best-orientation error 33855.9704031495; exact witness saved.

2026-11-12 22:46:58 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:58 Orthogonal minimum adversary: best-orientation error 33855.9704031495; exact witness saved.

2026-11-12 22:46:58 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:58 Orthogonal minimum adversary: best-orientation error 33855.9705838363; exact witness saved.

2026-11-12 22:46:58 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:58 Orthogonal minimum adversary: best-orientation error 33855.9705838363; exact witness saved.

2026-11-12 22:46:58 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:58 Orthogonal minimum adversary: best-orientation error 33855.9705838365; exact witness saved.

2026-11-12 22:46:58 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:58 Orthogonal minimum adversary: best-orientation error 33855.9707256309; exact witness saved.

2026-11-12 22:46:58 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:58 Orthogonal minimum adversary: best-orientation error 33855.9708368801; exact witness saved.

2026-11-12 22:46:58 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:58 Orthogonal minimum adversary: best-orientation error 33855.9708394386; exact witness saved.

2026-11-12 22:46:58 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:58 Orthogonal minimum adversary: best-orientation error 33855.9708456195; exact witness saved.

2026-11-12 22:46:58 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:58 Orthogonal minimum adversary: best-orientation error 33855.9708481951; exact witness saved.

2026-11-12 22:46:58 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:59 Orthogonal minimum adversary: best-orientation error 33855.9711501316; exact witness saved.

2026-11-12 22:46:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:59 Orthogonal minimum adversary: best-orientation error 33855.9716218867; exact witness saved.

2026-11-12 22:46:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:59 Orthogonal minimum adversary: best-orientation error 33855.9716224626; exact witness saved.

2026-11-12 22:46:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:59 Orthogonal minimum adversary: best-orientation error 33855.9716552233; exact witness saved.

2026-11-12 22:46:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:59 Orthogonal minimum adversary: best-orientation error 33855.9716552553; exact witness saved.

2026-11-12 22:46:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:59 Orthogonal minimum adversary: best-orientation error 33855.9716552557; exact witness saved.

2026-11-12 22:46:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:59 Orthogonal minimum adversary: best-orientation error 33855.971671636; exact witness saved.

2026-11-12 22:46:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:59 Orthogonal minimum adversary: best-orientation error 33855.9718839239; exact witness saved.

2026-11-12 22:46:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:59 Orthogonal minimum adversary: best-orientation error 33855.9719051527; exact witness saved.

2026-11-12 22:46:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:59 Orthogonal minimum adversary: best-orientation error 33855.9719068285; exact witness saved.

2026-11-12 22:46:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:59 Orthogonal minimum adversary: best-orientation error 33855.9719068445; exact witness saved.

2026-11-12 22:46:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:59 Orthogonal minimum adversary: best-orientation error 33855.9719068445; exact witness saved.

2026-11-12 22:46:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:59 Orthogonal minimum adversary: best-orientation error 33855.9791343818; exact witness saved.

2026-11-12 22:46:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:59 Orthogonal minimum adversary: best-orientation error 33855.9791360398; exact witness saved.

2026-11-12 22:46:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:46:59 Orthogonal minimum adversary: best-orientation error 33855.9791999548; exact witness saved.

2026-11-12 22:46:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 33855.9791999868; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 33855.9791999868; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 33855.9872306967; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 33907.8366342735; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 33907.8366342735; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 33907.8366969766; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 38463.7245928505; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 38463.7281869736; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 38463.728206491; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 38463.7366575726; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 38463.7366682767; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 38463.7367444183; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 38463.7367444183; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 38463.8888680975; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 38463.8888680991; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 38463.8891191046; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 38464.0573528463; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:00 Orthogonal minimum adversary: best-orientation error 38464.0576058183; exact witness saved.

2026-11-12 22:47:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:01 Orthogonal minimum adversary: best-orientation error 38464.0576058183; exact witness saved.

2026-11-12 22:47:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:01 Orthogonal minimum adversary: best-orientation error 38464.0578055145; exact witness saved.

2026-11-12 22:47:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:01 Orthogonal minimum adversary: best-orientation error 38464.0578055145; exact witness saved.

2026-11-12 22:47:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:01 Orthogonal minimum adversary: best-orientation error 104002.434195841; exact witness saved.

2026-11-12 22:47:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:01 Orthogonal minimum adversary: best-orientation error 104002.533206373; exact witness saved.

2026-11-12 22:47:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:01 Orthogonal minimum adversary: best-orientation error 104002.533738896; exact witness saved.

2026-11-12 22:47:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:02 Orthogonal minimum adversary: best-orientation error 104002.534316721; exact witness saved.

2026-11-12 22:47:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:02 Orthogonal minimum adversary: best-orientation error 104002.541984999; exact witness saved.

2026-11-12 22:47:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:02 Orthogonal minimum adversary: best-orientation error 104028.130743574; exact witness saved.

2026-11-12 22:47:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:03 Orthogonal minimum adversary: best-orientation error 104028.138683084; exact witness saved.

2026-11-12 22:47:03 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:03 Orthogonal minimum adversary: best-orientation error 104028.140061285; exact witness saved.

2026-11-12 22:47:03 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 104028.144157819; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 104491.985221991; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 104491.985221991; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 104491.989871119; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 104491.99764498; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 104491.99764498; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 104491.99764498; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 104491.997714789; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 104521.125434785; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 104521.125438666; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 104521.125665192; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 104521.125666364; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 104521.125870237; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 104521.125870237; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 104521.125871292; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 105044.045905781; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 105044.046782871; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:04 Orthogonal minimum adversary: best-orientation error 105044.046828838; exact witness saved.

2026-11-12 22:47:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:05 Orthogonal minimum adversary: best-orientation error 115954.207846663; exact witness saved.

2026-11-12 22:47:05 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:05 Orthogonal minimum adversary: best-orientation error 115954.222002582; exact witness saved.

2026-11-12 22:47:05 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:05 Orthogonal minimum adversary: best-orientation error 115954.223418174; exact witness saved.

2026-11-12 22:47:05 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:06 Orthogonal minimum adversary: best-orientation error 116032.581905233; exact witness saved.

2026-11-12 22:47:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:06 Orthogonal minimum adversary: best-orientation error 116032.585842503; exact witness saved.

2026-11-12 22:47:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:06 Orthogonal minimum adversary: best-orientation error 116032.586477003; exact witness saved.

2026-11-12 22:47:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:06 Orthogonal minimum adversary: best-orientation error 116032.58648224; exact witness saved.

2026-11-12 22:47:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:06 Orthogonal minimum adversary: best-orientation error 116032.586691223; exact witness saved.

2026-11-12 22:47:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:06 Orthogonal minimum adversary: best-orientation error 132822.716596986; exact witness saved.

2026-11-12 22:47:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:07 Orthogonal minimum adversary: best-orientation error 132822.721982474; exact witness saved.

2026-11-12 22:47:07 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:07 Orthogonal minimum adversary: best-orientation error 132822.726488789; exact witness saved.

2026-11-12 22:47:07 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:07 Orthogonal minimum adversary: best-orientation error 200370.620565554; exact witness saved.

2026-11-12 22:47:07 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:07 Orthogonal minimum adversary: best-orientation error 200370.620565554; exact witness saved.

2026-11-12 22:47:07 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:07 Orthogonal minimum adversary: best-orientation error 200370.620571914; exact witness saved.

2026-11-12 22:47:07 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:08 Orthogonal minimum adversary: best-orientation error 200370.620575107; exact witness saved.

2026-11-12 22:47:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:08 Orthogonal minimum adversary: best-orientation error 200370.620577981; exact witness saved.

2026-11-12 22:47:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:08 Orthogonal minimum adversary: best-orientation error 200370.623184116; exact witness saved.

2026-11-12 22:47:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:08 Orthogonal minimum adversary: best-orientation error 200370.623184668; exact witness saved.

2026-11-12 22:47:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:08 Orthogonal minimum adversary: best-orientation error 200370.624492641; exact witness saved.

2026-11-12 22:47:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:08 Orthogonal minimum adversary: best-orientation error 200370.627518156; exact witness saved.

2026-11-12 22:47:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:08 Orthogonal minimum adversary: best-orientation error 200370.6275183; exact witness saved.

2026-11-12 22:47:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:08 Orthogonal minimum adversary: best-orientation error 200370.627552202; exact witness saved.

2026-11-12 22:47:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:09 Orthogonal minimum adversary: best-orientation error 200370.627571179; exact witness saved.

2026-11-12 22:47:09 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:09 Orthogonal minimum adversary: best-orientation error 200370.627571198; exact witness saved.

2026-11-12 22:47:09 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:09 Orthogonal minimum adversary: best-orientation error 200370.627571227; exact witness saved.

2026-11-12 22:47:09 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:09 Orthogonal minimum adversary: best-orientation error 200370.627584307; exact witness saved.

2026-11-12 22:47:09 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:09 Orthogonal minimum adversary: best-orientation error 200370.629165451; exact witness saved.

2026-11-12 22:47:09 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:10 Orthogonal minimum adversary: best-orientation error 200370.629179537; exact witness saved.

2026-11-12 22:47:10 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:10 Orthogonal minimum adversary: best-orientation error 200370.629179539; exact witness saved.

2026-11-12 22:47:10 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:10 Orthogonal minimum adversary: best-orientation error 200370.629181879; exact witness saved.

2026-11-12 22:47:10 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:11 Fork prequotient 6_triple_excess: -1.9999999799998e-16; exact witness saved.

2026-11-12 22:47:11 Fork prequotient 6_triple_ratio: 1.9999; exact witness saved.

2026-11-12 22:47:12 Orthogonal minimum adversary: best-orientation error 200370.629978975; exact witness saved.

2026-11-12 22:47:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:12 Orthogonal minimum adversary: best-orientation error 200370.630006673; exact witness saved.

2026-11-12 22:47:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:12 Orthogonal minimum adversary: best-orientation error 200370.630405221; exact witness saved.

2026-11-12 22:47:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:12 Orthogonal minimum adversary: best-orientation error 200370.630763915; exact witness saved.

2026-11-12 22:47:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:12 Orthogonal minimum adversary: best-orientation error 200370.630799784; exact witness saved.

2026-11-12 22:47:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:12 Orthogonal minimum adversary: best-orientation error 200370.630799786; exact witness saved.

2026-11-12 22:47:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:12 Orthogonal minimum adversary: best-orientation error 200370.630799795; exact witness saved.

2026-11-12 22:47:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:12 Orthogonal minimum adversary: best-orientation error 200370.630799796; exact witness saved.

2026-11-12 22:47:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:12 Orthogonal minimum adversary: best-orientation error 200370.630799797; exact witness saved.

2026-11-12 22:47:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:12 Orthogonal minimum adversary: best-orientation error 200370.630799916; exact witness saved.

2026-11-12 22:47:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:12 Orthogonal minimum adversary: best-orientation error 200370.630799916; exact witness saved.

2026-11-12 22:47:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:12 Orthogonal minimum adversary: best-orientation error 200370.630799929; exact witness saved.

2026-11-12 22:47:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:12 Orthogonal minimum adversary: best-orientation error 200370.630799936; exact witness saved.

2026-11-12 22:47:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:13 Orthogonal minimum adversary: best-orientation error 200370.630799936; exact witness saved.

2026-11-12 22:47:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:13 Orthogonal minimum adversary: best-orientation error 200370.630799942; exact witness saved.

2026-11-12 22:47:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:13 Orthogonal minimum adversary: best-orientation error 200370.630800787; exact witness saved.

2026-11-12 22:47:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:14 Orthogonal minimum adversary: best-orientation error 200370.630800787; exact witness saved.

2026-11-12 22:47:14 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:14 Orthogonal minimum adversary: best-orientation error 200370.630800787; exact witness saved.

2026-11-12 22:47:14 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:14 Orthogonal minimum adversary: best-orientation error 200370.630800787; exact witness saved.

2026-11-12 22:47:14 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:14 Orthogonal minimum adversary: best-orientation error 200370.630800849; exact witness saved.

2026-11-12 22:47:14 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:17 Orthogonal minimum adversary: best-orientation error 200370.630803545; exact witness saved.

2026-11-12 22:47:17 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:17 Orthogonal minimum adversary: best-orientation error 200370.630803545; exact witness saved.

2026-11-12 22:47:17 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:17 Orthogonal minimum adversary: best-orientation error 200370.630803545; exact witness saved.

2026-11-12 22:47:17 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:17 Orthogonal minimum adversary: best-orientation error 200370.630803792; exact witness saved.

2026-11-12 22:47:17 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:17 Orthogonal minimum adversary: best-orientation error 200370.630804154; exact witness saved.

2026-11-12 22:47:17 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:18 Orthogonal minimum adversary: best-orientation error 200370.630804298; exact witness saved.

2026-11-12 22:47:18 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:18 Orthogonal minimum adversary: best-orientation error 200370.630804298; exact witness saved.

2026-11-12 22:47:18 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:18 Orthogonal minimum adversary: best-orientation error 200370.630804299; exact witness saved.

2026-11-12 22:47:18 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:18 Orthogonal minimum adversary: best-orientation error 200370.630804299; exact witness saved.

2026-11-12 22:47:18 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:18 Orthogonal minimum adversary: best-orientation error 200370.630804307; exact witness saved.

2026-11-12 22:47:18 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:18 Orthogonal minimum adversary: best-orientation error 200370.6308063; exact witness saved.

2026-11-12 22:47:18 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:18 Orthogonal minimum adversary: best-orientation error 200370.630806511; exact witness saved.

2026-11-12 22:47:18 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:18 Orthogonal minimum adversary: best-orientation error 200370.630806616; exact witness saved.

2026-11-12 22:47:18 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:18 Orthogonal minimum adversary: best-orientation error 200370.630806616; exact witness saved.

2026-11-12 22:47:18 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:19 Orthogonal minimum adversary: best-orientation error 200370.630806656; exact witness saved.

2026-11-12 22:47:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:19 Orthogonal minimum adversary: best-orientation error 200370.630806725; exact witness saved.

2026-11-12 22:47:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:19 Orthogonal minimum adversary: best-orientation error 200370.630806734; exact witness saved.

2026-11-12 22:47:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:20 Orthogonal minimum adversary: best-orientation error 200370.630806734; exact witness saved.

2026-11-12 22:47:20 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:20 Orthogonal minimum adversary: best-orientation error 200370.630806748; exact witness saved.

2026-11-12 22:47:20 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:20 Orthogonal minimum adversary: best-orientation error 200370.630806754; exact witness saved.

2026-11-12 22:47:20 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:20 Orthogonal minimum adversary: best-orientation error 200370.630806754; exact witness saved.

2026-11-12 22:47:20 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:20 Orthogonal minimum adversary: best-orientation error 200370.630806754; exact witness saved.

2026-11-12 22:47:20 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:21 Orthogonal minimum adversary: best-orientation error 200370.630806772; exact witness saved.

2026-11-12 22:47:21 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:21 Orthogonal minimum adversary: best-orientation error 200370.630806772; exact witness saved.

2026-11-12 22:47:21 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:21 Orthogonal minimum adversary: best-orientation error 200370.630806828; exact witness saved.

2026-11-12 22:47:21 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:21 Orthogonal minimum adversary: best-orientation error 200370.630806834; exact witness saved.

2026-11-12 22:47:21 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:21 Orthogonal minimum adversary: best-orientation error 200370.630806836; exact witness saved.

2026-11-12 22:47:21 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:23 Orthogonal minimum adversary: best-orientation error 200370.630806836; exact witness saved.

2026-11-12 22:47:23 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:23 Orthogonal minimum adversary: best-orientation error 200370.630806836; exact witness saved.

2026-11-12 22:47:23 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:23 Orthogonal minimum adversary: best-orientation error 200370.630806836; exact witness saved.

2026-11-12 22:47:23 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:24 Orthogonal minimum adversary: best-orientation error 200370.630808535; exact witness saved.

2026-11-12 22:47:24 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:25 Orthogonal minimum adversary: best-orientation error 200370.630808714; exact witness saved.

2026-11-12 22:47:25 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:25 Orthogonal minimum adversary: best-orientation error 200370.630808724; exact witness saved.

2026-11-12 22:47:25 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:25 Orthogonal minimum adversary: best-orientation error 200370.630808777; exact witness saved.

2026-11-12 22:47:25 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:25 Orthogonal minimum adversary: best-orientation error 200370.630808803; exact witness saved.

2026-11-12 22:47:25 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:26 Orthogonal minimum adversary: best-orientation error 200370.630808827; exact witness saved.

2026-11-12 22:47:26 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:26 Orthogonal minimum adversary: best-orientation error 200370.630808836; exact witness saved.

2026-11-12 22:47:26 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:26 Orthogonal minimum adversary: best-orientation error 200370.630808837; exact witness saved.

2026-11-12 22:47:26 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:26 Orthogonal minimum adversary: best-orientation error 200370.630808867; exact witness saved.

2026-11-12 22:47:26 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:26 Orthogonal minimum adversary: best-orientation error 200370.630808892; exact witness saved.

2026-11-12 22:47:26 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:29 Orthogonal minimum adversary: best-orientation error 200370.630808895; exact witness saved.

2026-11-12 22:47:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:29 Orthogonal minimum adversary: best-orientation error 200370.630808895; exact witness saved.

2026-11-12 22:47:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:29 Orthogonal minimum adversary: best-orientation error 200370.630808895; exact witness saved.

2026-11-12 22:47:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:33 Orthogonal minimum adversary: best-orientation error 200370.630808898; exact witness saved.

2026-11-12 22:47:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:35 Orthogonal minimum adversary: best-orientation error 200370.630808899; exact witness saved.

2026-11-12 22:47:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:35 Orthogonal minimum adversary: best-orientation error 200370.630808899; exact witness saved.

2026-11-12 22:47:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:35 Orthogonal minimum adversary: best-orientation error 200370.630808903; exact witness saved.

2026-11-12 22:47:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:36 Orthogonal minimum adversary: best-orientation error 200370.630808904; exact witness saved.

2026-11-12 22:47:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:36 Orthogonal minimum adversary: best-orientation error 200370.630808905; exact witness saved.

2026-11-12 22:47:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:37 Orthogonal minimum adversary: best-orientation error 200370.630808906; exact witness saved.

2026-11-12 22:47:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:37 Orthogonal minimum adversary: best-orientation error 200370.630808906; exact witness saved.

2026-11-12 22:47:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:37 Orthogonal minimum adversary: best-orientation error 200370.630808906; exact witness saved.

2026-11-12 22:47:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:37 Orthogonal minimum adversary: best-orientation error 200370.630808907; exact witness saved.

2026-11-12 22:47:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:37 Orthogonal minimum adversary: best-orientation error 200370.630808907; exact witness saved.

2026-11-12 22:47:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:37 Orthogonal minimum adversary: best-orientation error 200370.630808907; exact witness saved.

2026-11-12 22:47:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:37 Orthogonal minimum adversary: best-orientation error 200370.630808907; exact witness saved.

2026-11-12 22:47:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:38 Orthogonal minimum adversary: best-orientation error 200370.630808907; exact witness saved.

2026-11-12 22:47:38 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:40 Orthogonal minimum adversary: best-orientation error 200370.630808908; exact witness saved.

2026-11-12 22:47:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:40 Orthogonal minimum adversary: best-orientation error 200370.630808908; exact witness saved.

2026-11-12 22:47:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:41 Orthogonal minimum adversary: best-orientation error 200370.630808908; exact witness saved.

2026-11-12 22:47:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:41 Orthogonal minimum adversary: best-orientation error 200370.630808908; exact witness saved.

2026-11-12 22:47:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:41 Orthogonal minimum adversary: best-orientation error 200370.630808908; exact witness saved.

2026-11-12 22:47:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:42 Orthogonal minimum adversary: best-orientation error 200370.630808908; exact witness saved.

2026-11-12 22:47:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:42 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:42 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:42 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:43 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:43 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:43 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:45 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:46 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:46 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:47 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:47 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:47 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:47 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:47 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:47 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:48 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:48 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:48 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:48 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:48 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:48 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:48 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:48 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:48 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:48 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:48 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:49 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:50 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:50 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:50 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:50 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:50 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:50 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:50 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:50 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:50 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:50 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:51 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:53 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:53 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:53 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:54 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:54 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:54 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:55 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:55 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:55 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:55 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:56 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:56 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:56 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:56 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:57 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:57 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:57 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:57 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:47:59 Fork prequotient 6_pairs_ratio: 2.999699999997; exact witness saved.

2026-11-12 22:47:59 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:47:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:01 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:02 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:03 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:03 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:04 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:05 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:05 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:05 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:05 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:05 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:05 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:07 Fork prequotient scan finished: 2894 networks, 447028 rank-two partitions, 165.056s, peak RSS 29589504 bytes.

2026-11-12 22:48:09 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:09 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:10 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:10 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:10 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:10 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:12 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:12 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:12 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:12 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:13 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:14 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:14 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:16 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:16 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:16 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:16 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:16 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:16 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:16 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:16 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:17 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:17 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:17 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:17 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:18 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:18 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:21 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:21 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:22 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:22 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:22 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:22 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:23 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:23 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:23 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:23 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:23 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:23 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:23 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:23 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:24 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:24 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:24 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:24 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:24 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:24 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:25 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:25 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:25 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:25 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:25 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:25 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:26 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:26 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:26 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:26 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:26 Orthogonal minimum adversary: best-orientation error 0.674385633735628; exact witness saved.

2026-11-12 22:48:26 Orthogonal minimum adversary: best-orientation error 0.895612475378087; exact witness saved.

2026-11-12 22:48:26 Orthogonal minimum adversary: best-orientation error 0.895613318140911; exact witness saved.

2026-11-12 22:48:26 Orthogonal minimum adversary: best-orientation error 0.907402733503021; exact witness saved.

2026-11-12 22:48:26 Orthogonal minimum adversary: best-orientation error 1.26916134206471; exact witness saved.

2026-11-12 22:48:26 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.28098322919262; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.28098323200436; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.28102887186663; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.29669383662752; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.29669383663043; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.29669699081085; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.29692998036499; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.29693012336554; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.29693013551985; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.29693029440651; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.4248302750673; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.43283150678084; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.43283150755968; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.43331765833904; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.4369463280118; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.43714839832245; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.43856323025293; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.43936864193146; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.43937088656973; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.43937088721383; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.43940097978686; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.43970933011098; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:27 Orthogonal minimum adversary: best-orientation error 1.43970933014508; exact witness saved.

2026-11-12 22:48:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:28 Orthogonal minimum adversary: best-orientation error 1.44188460853304; exact witness saved.

2026-11-12 22:48:28 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:28 Orthogonal minimum adversary: best-orientation error 1.44229039026843; exact witness saved.

2026-11-12 22:48:28 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:28 Orthogonal minimum adversary: best-orientation error 1.44334747200516; exact witness saved.

2026-11-12 22:48:28 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:28 Orthogonal minimum adversary: best-orientation error 1.44344930331674; exact witness saved.

2026-11-12 22:48:28 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:28 Orthogonal minimum adversary: best-orientation error 1.443449303641; exact witness saved.

2026-11-12 22:48:28 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:28 Orthogonal minimum adversary: best-orientation error 1.44345088242373; exact witness saved.

2026-11-12 22:48:28 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:28 Orthogonal minimum adversary: best-orientation error 1.44391916449177; exact witness saved.

2026-11-12 22:48:28 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:28 Orthogonal minimum adversary: best-orientation error 1.44391916450891; exact witness saved.

2026-11-12 22:48:28 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:28 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:28 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:28 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:28 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:28 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:28 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:28 Orthogonal minimum adversary: best-orientation error 200370.630808909; exact witness saved.

2026-11-12 22:48:28 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:29 Orthogonal minimum adversary: best-orientation error 1.44473706598624; exact witness saved.

2026-11-12 22:48:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:29 Orthogonal minimum adversary: best-orientation error 1.44473740611616; exact witness saved.

2026-11-12 22:48:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:29 Orthogonal minimum adversary: best-orientation error 1.44473808637696; exact witness saved.

2026-11-12 22:48:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:29 Orthogonal minimum adversary: best-orientation error 1.4479750904642; exact witness saved.

2026-11-12 22:48:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:29 Orthogonal minimum adversary: best-orientation error 1.44828387481998; exact witness saved.

2026-11-12 22:48:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:29 Orthogonal minimum adversary: best-orientation error 1.44837487694262; exact witness saved.

2026-11-12 22:48:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:29 Orthogonal minimum adversary: best-orientation error 1.4483840463641; exact witness saved.

2026-11-12 22:48:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:29 Orthogonal minimum adversary: best-orientation error 1.44841494332877; exact witness saved.

2026-11-12 22:48:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:29 Orthogonal minimum adversary finished: 14609 exact objectives, 110.010s, best 200370.630808909, peak RSS 29573120 bytes.

2026-11-12 22:48:29 Orthogonal minimum adversary: best-orientation error 1.44853907029794; exact witness saved.

2026-11-12 22:48:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:29 Orthogonal minimum adversary: best-orientation error 1.4498773081455; exact witness saved.

2026-11-12 22:48:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:29 Orthogonal minimum adversary: best-orientation error 1.45057316542147; exact witness saved.

2026-11-12 22:48:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:29 Orthogonal minimum adversary: best-orientation error 1.45057599472985; exact witness saved.

2026-11-12 22:48:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:29 Orthogonal minimum adversary: best-orientation error 1.45071426546394; exact witness saved.

2026-11-12 22:48:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:29 Orthogonal minimum adversary: best-orientation error 1.45071630614567; exact witness saved.

2026-11-12 22:48:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:31 Orthogonal minimum adversary: best-orientation error 1.45072196472171; exact witness saved.

2026-11-12 22:48:31 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:32 Orthogonal minimum adversary: best-orientation error 1.45138393067758; exact witness saved.

2026-11-12 22:48:32 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:32 Orthogonal minimum adversary: best-orientation error 1.45251502577572; exact witness saved.

2026-11-12 22:48:32 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:32 Orthogonal minimum adversary: best-orientation error 1.45251908974113; exact witness saved.

2026-11-12 22:48:32 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:32 Orthogonal minimum adversary: best-orientation error 1.45477120793048; exact witness saved.

2026-11-12 22:48:32 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:32 Orthogonal minimum adversary: best-orientation error 1.4547712130272; exact witness saved.

2026-11-12 22:48:32 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:32 Orthogonal minimum adversary: best-orientation error 1.46504027326925; exact witness saved.

2026-11-12 22:48:32 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:32 Orthogonal minimum adversary: best-orientation error 1.46863178453009; exact witness saved.

2026-11-12 22:48:32 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 1.46863335844071; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 1.46866673779; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 1.47199908621702; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 1.49133846487628; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 1.83083813935213; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 1.83627291439048; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 1.83627566452658; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 5.53770749320086; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 5.5443700746488; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 5.54504170681732; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 5.56234964907571; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 5.56267575478145; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 5.56267591542815; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 5.56267741594054; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 5.56267741858147; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 9.63973543895739; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 17.6962267995787; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 17.6962268000505; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 17.6982368228027; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 17.7318697656702; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 33.9604870673574; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 33.9604940134194; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 33.9612597556449; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 33.96782116207; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 33.9820681560817; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 34.0137007088667; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 34.0137007093756; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 34.0137007096332; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 34.0302544157659; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 318.346705048888; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 318.346705486297; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 318.424198773267; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:33 Orthogonal minimum adversary: best-orientation error 318.424198773829; exact witness saved.

2026-11-12 22:48:33 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 318.424198775677; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 318.427613789802; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 318.431476200059; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 318.431476223952; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 318.494122598176; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 320.557292943181; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 320.596547506607; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 321.380891337772; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 321.380892519593; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 321.412455148176; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 321.422489067024; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 321.992069301393; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 365.56262872263; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 365.567046373502; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 372.695928968392; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 381.35176998546; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 381.351774990485; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 381.425692758296; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 449.703484832843; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 449.703484835621; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 460.353872696642; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 460.354096644739; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 460.394594286424; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 460.396770365147; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 483.101962924383; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 598.374163574114; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 599.105652459843; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 599.105825392847; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 599.109282044283; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 599.109285301304; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 599.648997800025; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 599.649153601132; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 600.769166986128; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 1117.24732392387; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 1117.24736018646; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 1117.25337433487; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 1119.47928379868; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 1119.60020333848; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 1158.93364085736; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 1160.80026789358; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 1160.80530755227; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 1234.22384118153; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 1234.22446612078; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 1234.94554931318; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 1234.94558451158; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:34 Orthogonal minimum adversary: best-orientation error 1470.91232656942; exact witness saved.

2026-11-12 22:48:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1470.91259174295; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1471.02390869202; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1528.2816489225; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1772.46766663123; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1772.46863761736; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1772.48559576665; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1772.4855957873; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1772.70255352028; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1772.70265063521; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1772.72362485909; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1772.72362497675; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1772.8742890742; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1775.04736757848; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1775.04811228524; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1775.18419760145; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1775.18456433462; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1775.18466163348; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1775.18466703897; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1775.18602717979; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1775.18711544934; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1775.18711999071; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1775.18772441977; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1782.68350653188; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:35 Orthogonal minimum adversary: best-orientation error 1782.68405512412; exact witness saved.

2026-11-12 22:48:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1782.68405521819; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1782.68413142156; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1782.69175637834; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1782.77960057443; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1782.7808201345; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1782.78960449881; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1782.79593710264; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1782.79662234486; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1782.79670847228; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1783.55993494256; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1783.5599763622; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1783.60335706729; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1783.60335706964; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1783.60336470265; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1783.61949842996; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1783.61949990428; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1783.61949990668; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1783.63902937093; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1783.64335751151; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1783.6433575231; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1783.67319517346; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:36 Orthogonal minimum adversary: best-orientation error 1783.67363484687; exact witness saved.

2026-11-12 22:48:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:37 Orthogonal minimum adversary: best-orientation error 1783.67365047236; exact witness saved.

2026-11-12 22:48:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:37 Orthogonal minimum adversary: best-orientation error 1783.67367221213; exact witness saved.

2026-11-12 22:48:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:37 Orthogonal minimum adversary: best-orientation error 1783.67371617949; exact witness saved.

2026-11-12 22:48:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:37 Orthogonal minimum adversary: best-orientation error 1783.67373576433; exact witness saved.

2026-11-12 22:48:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:37 Orthogonal minimum adversary: best-orientation error 1783.67482086816; exact witness saved.

2026-11-12 22:48:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:37 Orthogonal minimum adversary: best-orientation error 1783.67498382821; exact witness saved.

2026-11-12 22:48:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:37 Orthogonal minimum adversary: best-orientation error 1783.67517914931; exact witness saved.

2026-11-12 22:48:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:37 Orthogonal minimum adversary: best-orientation error 1783.67556058151; exact witness saved.

2026-11-12 22:48:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:37 Orthogonal minimum adversary: best-orientation error 1783.6755692625; exact witness saved.

2026-11-12 22:48:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:37 Orthogonal minimum adversary: best-orientation error 1783.67556926467; exact witness saved.

2026-11-12 22:48:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:37 Orthogonal minimum adversary: best-orientation error 1783.67557360492; exact witness saved.

2026-11-12 22:48:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:38 Orthogonal minimum adversary: best-orientation error 1783.67558239841; exact witness saved.

2026-11-12 22:48:38 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:38 Orthogonal minimum adversary: best-orientation error 1783.67573053536; exact witness saved.

2026-11-12 22:48:38 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:38 Orthogonal minimum adversary: best-orientation error 1783.67577401546; exact witness saved.

2026-11-12 22:48:38 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:38 Orthogonal minimum adversary: best-orientation error 1783.67661875087; exact witness saved.

2026-11-12 22:48:38 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:38 Orthogonal minimum adversary: best-orientation error 1783.6766210319; exact witness saved.

2026-11-12 22:48:38 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:39 Orthogonal minimum adversary: best-orientation error 1783.68077165467; exact witness saved.

2026-11-12 22:48:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:39 Orthogonal minimum adversary: best-orientation error 1783.6837573611; exact witness saved.

2026-11-12 22:48:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:39 Orthogonal minimum adversary: best-orientation error 1783.68571147996; exact witness saved.

2026-11-12 22:48:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:39 Orthogonal minimum adversary: best-orientation error 1783.68571453104; exact witness saved.

2026-11-12 22:48:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:39 Orthogonal minimum adversary: best-orientation error 1783.68571605658; exact witness saved.

2026-11-12 22:48:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:39 Orthogonal minimum adversary: best-orientation error 1783.68571606946; exact witness saved.

2026-11-12 22:48:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:39 Orthogonal minimum adversary: best-orientation error 1783.68732890247; exact witness saved.

2026-11-12 22:48:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:39 Orthogonal minimum adversary: best-orientation error 1783.68732900039; exact witness saved.

2026-11-12 22:48:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:39 Orthogonal minimum adversary: best-orientation error 1783.79339890944; exact witness saved.

2026-11-12 22:48:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:39 Orthogonal minimum adversary: best-orientation error 1783.79339928864; exact witness saved.

2026-11-12 22:48:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:39 Orthogonal minimum adversary: best-orientation error 1783.79347742622; exact witness saved.

2026-11-12 22:48:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:39 Orthogonal minimum adversary: best-orientation error 1783.79347743357; exact witness saved.

2026-11-12 22:48:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:39 Orthogonal minimum adversary: best-orientation error 1783.79347747062; exact witness saved.

2026-11-12 22:48:39 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:40 Orthogonal minimum adversary: best-orientation error 1784.88905809834; exact witness saved.

2026-11-12 22:48:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:40 Orthogonal minimum adversary: best-orientation error 1784.89296170109; exact witness saved.

2026-11-12 22:48:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:40 Orthogonal minimum adversary: best-orientation error 1784.8929620772; exact witness saved.

2026-11-12 22:48:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:40 Orthogonal minimum adversary: best-orientation error 1784.89296241111; exact witness saved.

2026-11-12 22:48:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:40 Orthogonal minimum adversary: best-orientation error 1784.89296790138; exact witness saved.

2026-11-12 22:48:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:40 Orthogonal minimum adversary: best-orientation error 1784.89298354818; exact witness saved.

2026-11-12 22:48:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:40 Orthogonal minimum adversary: best-orientation error 1784.89490729327; exact witness saved.

2026-11-12 22:48:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:40 Orthogonal minimum adversary: best-orientation error 1784.89654420622; exact witness saved.

2026-11-12 22:48:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:40 Orthogonal minimum adversary: best-orientation error 1784.89655015094; exact witness saved.

2026-11-12 22:48:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:40 Orthogonal minimum adversary: best-orientation error 1795.96664205481; exact witness saved.

2026-11-12 22:48:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:40 Orthogonal minimum adversary: best-orientation error 1795.96697138683; exact witness saved.

2026-11-12 22:48:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:40 Orthogonal minimum adversary: best-orientation error 1795.96697187051; exact witness saved.

2026-11-12 22:48:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:40 Orthogonal minimum adversary: best-orientation error 1795.96697188039; exact witness saved.

2026-11-12 22:48:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:40 Orthogonal minimum adversary: best-orientation error 1795.96697194999; exact witness saved.

2026-11-12 22:48:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:41 Orthogonal minimum adversary: best-orientation error 1795.96697730858; exact witness saved.

2026-11-12 22:48:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:41 Orthogonal minimum adversary: best-orientation error 1795.9679678763; exact witness saved.

2026-11-12 22:48:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:41 Orthogonal minimum adversary: best-orientation error 1795.96807788867; exact witness saved.

2026-11-12 22:48:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:41 Orthogonal minimum adversary: best-orientation error 1795.96825381001; exact witness saved.

2026-11-12 22:48:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:41 Orthogonal minimum adversary: best-orientation error 1795.96874908768; exact witness saved.

2026-11-12 22:48:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:41 Orthogonal minimum adversary: best-orientation error 1795.96904548695; exact witness saved.

2026-11-12 22:48:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:41 Orthogonal minimum adversary: best-orientation error 1795.9691494912; exact witness saved.

2026-11-12 22:48:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:41 Orthogonal minimum adversary: best-orientation error 1808.43151042192; exact witness saved.

2026-11-12 22:48:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:41 Orthogonal minimum adversary: best-orientation error 1808.43196238837; exact witness saved.

2026-11-12 22:48:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:42 Orthogonal minimum adversary: best-orientation error 1808.43196426816; exact witness saved.

2026-11-12 22:48:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:42 Orthogonal minimum adversary: best-orientation error 1808.43196470953; exact witness saved.

2026-11-12 22:48:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:43 Orthogonal minimum adversary: best-orientation error 1808.4319647132; exact witness saved.

2026-11-12 22:48:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:43 Orthogonal minimum adversary: best-orientation error 1808.43196473772; exact witness saved.

2026-11-12 22:48:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:43 Orthogonal minimum adversary: best-orientation error 1808.43196473996; exact witness saved.

2026-11-12 22:48:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:43 Orthogonal minimum adversary: best-orientation error 1808.43196501565; exact witness saved.

2026-11-12 22:48:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:43 Orthogonal minimum adversary: best-orientation error 1808.43200456802; exact witness saved.

2026-11-12 22:48:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:43 Orthogonal minimum adversary: best-orientation error 1808.43202244024; exact witness saved.

2026-11-12 22:48:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:43 Orthogonal minimum adversary: best-orientation error 1808.43202247552; exact witness saved.

2026-11-12 22:48:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:43 Orthogonal minimum adversary: best-orientation error 1808.43202270151; exact witness saved.

2026-11-12 22:48:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:43 Orthogonal minimum adversary: best-orientation error 1808.43216976801; exact witness saved.

2026-11-12 22:48:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:43 Orthogonal minimum adversary: best-orientation error 1808.43216977696; exact witness saved.

2026-11-12 22:48:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:43 Orthogonal minimum adversary: best-orientation error 1808.43217002216; exact witness saved.

2026-11-12 22:48:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:43 Orthogonal minimum adversary: best-orientation error 1808.43217011966; exact witness saved.

2026-11-12 22:48:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:43 Orthogonal minimum adversary: best-orientation error 1808.43219007143; exact witness saved.

2026-11-12 22:48:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:44 Orthogonal minimum adversary: best-orientation error 1808.43219117986; exact witness saved.

2026-11-12 22:48:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:44 Orthogonal minimum adversary: best-orientation error 1808.43219435889; exact witness saved.

2026-11-12 22:48:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:44 Orthogonal minimum adversary: best-orientation error 1808.43219455505; exact witness saved.

2026-11-12 22:48:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:44 Orthogonal minimum adversary: best-orientation error 1808.4322047089; exact witness saved.

2026-11-12 22:48:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:44 Orthogonal minimum adversary: best-orientation error 1808.43220508256; exact witness saved.

2026-11-12 22:48:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:44 Orthogonal minimum adversary: best-orientation error 1808.43220553453; exact witness saved.

2026-11-12 22:48:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:44 Orthogonal minimum adversary: best-orientation error 1808.43220822036; exact witness saved.

2026-11-12 22:48:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:44 Orthogonal minimum adversary: best-orientation error 1808.43220826555; exact witness saved.

2026-11-12 22:48:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:44 Orthogonal minimum adversary: best-orientation error 1808.43220830969; exact witness saved.

2026-11-12 22:48:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:44 Orthogonal minimum adversary: best-orientation error 1808.43220919214; exact witness saved.

2026-11-12 22:48:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:45 Orthogonal minimum adversary: best-orientation error 1808.43220920096; exact witness saved.

2026-11-12 22:48:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:45 Orthogonal minimum adversary: best-orientation error 1808.43220920185; exact witness saved.

2026-11-12 22:48:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:46 Orthogonal minimum adversary: best-orientation error 1808.43221020576; exact witness saved.

2026-11-12 22:48:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:46 Orthogonal minimum adversary: best-orientation error 1808.43221429094; exact witness saved.

2026-11-12 22:48:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:46 Orthogonal minimum adversary: best-orientation error 1808.4322164174; exact witness saved.

2026-11-12 22:48:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:46 Orthogonal minimum adversary: best-orientation error 1808.43221835729; exact witness saved.

2026-11-12 22:48:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:46 Orthogonal minimum adversary: best-orientation error 1808.43221851045; exact witness saved.

2026-11-12 22:48:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:46 Orthogonal minimum adversary: best-orientation error 1808.4322186483; exact witness saved.

2026-11-12 22:48:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:46 Orthogonal minimum adversary: best-orientation error 1808.43221963065; exact witness saved.

2026-11-12 22:48:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:46 Orthogonal minimum adversary: best-orientation error 1808.43221963065; exact witness saved.

2026-11-12 22:48:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:46 Orthogonal minimum adversary: best-orientation error 1808.43221963068; exact witness saved.

2026-11-12 22:48:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:46 Orthogonal minimum adversary: best-orientation error 1808.43222867001; exact witness saved.

2026-11-12 22:48:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:47 Orthogonal minimum adversary: best-orientation error 1808.43222867229; exact witness saved.

2026-11-12 22:48:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:47 Orthogonal minimum adversary: best-orientation error 1808.43222867474; exact witness saved.

2026-11-12 22:48:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:47 Orthogonal minimum adversary: best-orientation error 1808.43222867597; exact witness saved.

2026-11-12 22:48:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:47 Orthogonal minimum adversary: best-orientation error 1808.43222878537; exact witness saved.

2026-11-12 22:48:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:47 Orthogonal minimum adversary: best-orientation error 1808.43223020641; exact witness saved.

2026-11-12 22:48:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:47 Orthogonal minimum adversary: best-orientation error 1808.4322302068; exact witness saved.

2026-11-12 22:48:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:47 Orthogonal minimum adversary: best-orientation error 1808.43223020881; exact witness saved.

2026-11-12 22:48:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:47 Orthogonal minimum adversary: best-orientation error 1808.432230711; exact witness saved.

2026-11-12 22:48:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:47 Orthogonal minimum adversary: best-orientation error 1808.43223071113; exact witness saved.

2026-11-12 22:48:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:48 Orthogonal minimum adversary: best-orientation error 1808.43223081089; exact witness saved.

2026-11-12 22:48:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:48 Orthogonal minimum adversary: best-orientation error 1808.43223081229; exact witness saved.

2026-11-12 22:48:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:48 Orthogonal minimum adversary: best-orientation error 1808.43223082032; exact witness saved.

2026-11-12 22:48:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:49 Orthogonal minimum adversary: best-orientation error 1808.43223107277; exact witness saved.

2026-11-12 22:48:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:49 Orthogonal minimum adversary: best-orientation error 1808.43223127229; exact witness saved.

2026-11-12 22:48:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:49 Orthogonal minimum adversary: best-orientation error 1808.43223127229; exact witness saved.

2026-11-12 22:48:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:49 Orthogonal minimum adversary: best-orientation error 1808.43223131749; exact witness saved.

2026-11-12 22:48:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:49 Orthogonal minimum adversary: best-orientation error 1808.43223131749; exact witness saved.

2026-11-12 22:48:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:49 Orthogonal minimum adversary: best-orientation error 1808.43223132867; exact witness saved.

2026-11-12 22:48:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:49 Orthogonal minimum adversary: best-orientation error 1808.43223133976; exact witness saved.

2026-11-12 22:48:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:49 Orthogonal minimum adversary: best-orientation error 1808.4322313453; exact witness saved.

2026-11-12 22:48:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:50 Orthogonal minimum adversary: best-orientation error 1808.43223135003; exact witness saved.

2026-11-12 22:48:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:50 Orthogonal minimum adversary: best-orientation error 1808.43223138266; exact witness saved.

2026-11-12 22:48:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:51 Orthogonal minimum adversary: best-orientation error 1808.43223138517; exact witness saved.

2026-11-12 22:48:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:51 Orthogonal minimum adversary: best-orientation error 1808.43223138517; exact witness saved.

2026-11-12 22:48:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:51 Orthogonal minimum adversary: best-orientation error 1808.43223141237; exact witness saved.

2026-11-12 22:48:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:51 Orthogonal minimum adversary: best-orientation error 1808.43223141454; exact witness saved.

2026-11-12 22:48:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:51 Orthogonal minimum adversary: best-orientation error 1808.43223141477; exact witness saved.

2026-11-12 22:48:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:51 Orthogonal minimum adversary: best-orientation error 1808.43223141512; exact witness saved.

2026-11-12 22:48:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:51 Orthogonal minimum adversary: best-orientation error 1808.43223142003; exact witness saved.

2026-11-12 22:48:51 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:52 Orthogonal minimum adversary: best-orientation error 1808.43223142064; exact witness saved.

2026-11-12 22:48:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:52 Orthogonal minimum adversary: best-orientation error 1808.43223143414; exact witness saved.

2026-11-12 22:48:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:52 Orthogonal minimum adversary: best-orientation error 1808.43223144591; exact witness saved.

2026-11-12 22:48:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:52 Orthogonal minimum adversary: best-orientation error 1808.43223144653; exact witness saved.

2026-11-12 22:48:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:52 Orthogonal minimum adversary: best-orientation error 1808.43223144653; exact witness saved.

2026-11-12 22:48:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:52 Orthogonal minimum adversary: best-orientation error 1808.43223144653; exact witness saved.

2026-11-12 22:48:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:52 Orthogonal minimum adversary: best-orientation error 1808.43223144723; exact witness saved.

2026-11-12 22:48:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:52 Orthogonal minimum adversary: best-orientation error 1808.43223144726; exact witness saved.

2026-11-12 22:48:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:52 Orthogonal minimum adversary: best-orientation error 1808.4322314476; exact witness saved.

2026-11-12 22:48:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:52 Orthogonal minimum adversary: best-orientation error 1808.43223144801; exact witness saved.

2026-11-12 22:48:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:52 Orthogonal minimum adversary: best-orientation error 1808.43223144815; exact witness saved.

2026-11-12 22:48:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:53 Orthogonal minimum adversary: best-orientation error 1808.4322314482; exact witness saved.

2026-11-12 22:48:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:54 Orthogonal minimum adversary: best-orientation error 1808.43223149612; exact witness saved.

2026-11-12 22:48:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:54 Orthogonal minimum adversary: best-orientation error 1808.43223149612; exact witness saved.

2026-11-12 22:48:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.43223149723; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.43223149896; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.43223149898; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.43223149909; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.43223149909; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.43223149932; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.43223149934; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.4322315009; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.43223151332; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.43223152451; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.43223152859; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.43223152875; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.43223153074; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.43223153137; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.43223153137; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.43223153137; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:55 Orthogonal minimum adversary: best-orientation error 1808.43223153321; exact witness saved.

2026-11-12 22:48:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:56 Orthogonal minimum adversary: best-orientation error 1808.43223153323; exact witness saved.

2026-11-12 22:48:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:57 Orthogonal minimum adversary: best-orientation error 1808.43223153323; exact witness saved.

2026-11-12 22:48:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:57 Orthogonal minimum adversary: best-orientation error 1808.43223153333; exact witness saved.

2026-11-12 22:48:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:57 Orthogonal minimum adversary: best-orientation error 1808.43223153377; exact witness saved.

2026-11-12 22:48:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:59 Orthogonal minimum adversary: best-orientation error 1808.43223153383; exact witness saved.

2026-11-12 22:48:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:59 Orthogonal minimum adversary: best-orientation error 1808.43223153383; exact witness saved.

2026-11-12 22:48:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:59 Orthogonal minimum adversary: best-orientation error 1808.43223153394; exact witness saved.

2026-11-12 22:48:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:48:59 Orthogonal minimum adversary: best-orientation error 1808.43223153394; exact witness saved.

2026-11-12 22:48:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:00 Orthogonal minimum adversary: best-orientation error 1808.43223153397; exact witness saved.

2026-11-12 22:49:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:02 Orthogonal minimum adversary: best-orientation error 1808.43223153398; exact witness saved.

2026-11-12 22:49:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:02 Orthogonal minimum adversary: best-orientation error 1808.43223153401; exact witness saved.

2026-11-12 22:49:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:02 Orthogonal minimum adversary: best-orientation error 1808.43223153406; exact witness saved.

2026-11-12 22:49:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:02 Orthogonal minimum adversary: best-orientation error 1808.4322315341; exact witness saved.

2026-11-12 22:49:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:02 Orthogonal minimum adversary: best-orientation error 1808.43223153411; exact witness saved.

2026-11-12 22:49:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:03 Orthogonal minimum adversary: best-orientation error 1808.43223153411; exact witness saved.

2026-11-12 22:49:03 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:03 Orthogonal minimum adversary: best-orientation error 1808.43223153411; exact witness saved.

2026-11-12 22:49:03 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:03 Orthogonal minimum adversary: best-orientation error 1808.43223153411; exact witness saved.

2026-11-12 22:49:03 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:03 Orthogonal minimum adversary: best-orientation error 1808.43223153411; exact witness saved.

2026-11-12 22:49:03 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:04 Orthogonal minimum adversary: best-orientation error 1808.43223153411; exact witness saved.

2026-11-12 22:49:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:04 Orthogonal minimum adversary: best-orientation error 1808.43223153412; exact witness saved.

2026-11-12 22:49:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:05 Orthogonal minimum adversary: best-orientation error 1808.43223153413; exact witness saved.

2026-11-12 22:49:05 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:05 Orthogonal minimum adversary: best-orientation error 1808.43223153413; exact witness saved.

2026-11-12 22:49:05 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:05 Orthogonal minimum adversary: best-orientation error 1808.43223153413; exact witness saved.

2026-11-12 22:49:05 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:05 Orthogonal minimum adversary: best-orientation error 1808.43223153413; exact witness saved.

2026-11-12 22:49:05 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:05 Orthogonal minimum adversary: best-orientation error 1808.43223153413; exact witness saved.

2026-11-12 22:49:05 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:05 Orthogonal minimum adversary: best-orientation error 1808.43223153413; exact witness saved.

2026-11-12 22:49:05 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:05 Orthogonal minimum adversary: best-orientation error 1808.43223153417; exact witness saved.

2026-11-12 22:49:05 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:06 Orthogonal minimum adversary: best-orientation error 1808.43223153417; exact witness saved.

2026-11-12 22:49:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:06 Orthogonal minimum adversary: best-orientation error 1808.43223153421; exact witness saved.

2026-11-12 22:49:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:06 Orthogonal minimum adversary: best-orientation error 1808.43223153421; exact witness saved.

2026-11-12 22:49:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:06 Orthogonal minimum adversary: best-orientation error 1808.43223153421; exact witness saved.

2026-11-12 22:49:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:07 Orthogonal minimum adversary: best-orientation error 1808.43223153421; exact witness saved.

2026-11-12 22:49:07 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:07 Orthogonal minimum adversary: best-orientation error 1808.43223153421; exact witness saved.

2026-11-12 22:49:07 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:07 Orthogonal minimum adversary: best-orientation error 1808.43223153421; exact witness saved.

2026-11-12 22:49:07 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:07 Orthogonal minimum adversary: best-orientation error 1808.43223153423; exact witness saved.

2026-11-12 22:49:07 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:07 Orthogonal minimum adversary: best-orientation error 1808.43223153423; exact witness saved.

2026-11-12 22:49:07 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:08 Orthogonal minimum adversary: best-orientation error 1808.43223153423; exact witness saved.

2026-11-12 22:49:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:08 Orthogonal minimum adversary: best-orientation error 1808.43223153423; exact witness saved.

2026-11-12 22:49:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:08 Orthogonal minimum adversary: best-orientation error 1808.43223153423; exact witness saved.

2026-11-12 22:49:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:08 Orthogonal minimum adversary: best-orientation error 1808.43223153423; exact witness saved.

2026-11-12 22:49:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:08 Orthogonal minimum adversary: best-orientation error 1808.43223153423; exact witness saved.

2026-11-12 22:49:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:08 Orthogonal minimum adversary: best-orientation error 1808.43223153423; exact witness saved.

2026-11-12 22:49:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:08 Orthogonal minimum adversary: best-orientation error 1808.43223153423; exact witness saved.

2026-11-12 22:49:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:09 Orthogonal minimum adversary: best-orientation error 1808.43223153423; exact witness saved.

2026-11-12 22:49:09 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:10 Orthogonal minimum adversary: best-orientation error 1808.43223153423; exact witness saved.

2026-11-12 22:49:10 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:12 Orthogonal minimum adversary: best-orientation error 1808.43223153423; exact witness saved.

2026-11-12 22:49:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:12 Orthogonal minimum adversary: best-orientation error 1808.43223153423; exact witness saved.

2026-11-12 22:49:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:12 Orthogonal minimum adversary: best-orientation error 1808.43223153423; exact witness saved.

2026-11-12 22:49:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:12 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:12 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:12 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:12 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:12 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:12 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:13 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:13 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:13 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:13 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:14 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:14 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:14 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:14 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:14 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:14 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:14 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:14 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:15 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:15 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:15 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:15 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:15 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:16 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:16 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:18 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:18 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:18 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:18 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:19 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:19 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:20 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:20 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:20 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:20 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:20 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:20 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:20 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:20 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:20 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:20 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:21 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:21 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:21 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:21 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:21 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:21 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:21 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:21 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:21 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:21 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:21 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:21 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:21 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:21 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:21 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:21 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:24 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:24 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:24 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:24 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:24 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:24 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:24 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:24 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:24 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:24 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:24 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:24 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:27 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:27 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:27 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:27 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:27 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:29 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:29 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:29 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:29 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:30 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:30 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:30 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:30 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:31 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:31 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:32 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:32 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:32 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:32 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:32 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:32 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:32 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:32 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:32 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:32 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:32 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:32 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:32 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:32 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:34 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:34 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:34 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:35 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:35 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:35 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:35 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:36 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:36 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:37 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:37 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:37 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:38 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:38 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:38 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:38 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:38 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:38 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:38 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:38 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:38 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:38 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:40 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:40 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:40 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:41 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:41 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:42 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:42 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:42 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:42 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:42 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:42 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:42 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:43 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:43 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:43 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:43 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:43 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:43 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:43 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:43 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:43 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:43 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:44 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:44 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:44 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:44 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:44 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:45 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:45 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:45 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:45 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:45 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:45 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:45 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:45 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:45 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:45 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:45 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:46 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:46 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:46 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:47 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:47 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:47 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:47 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:47 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:47 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:48 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:48 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:48 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:49 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:49 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:49 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:50 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:50 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:50 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:50 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:50 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:50 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:50 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:52 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:52 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:52 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:52 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:52 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:52 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:53 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:53 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:53 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:53 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:53 Orthogonal minimum adversary: best-orientation error 1808.43223153424; exact witness saved.

2026-11-12 22:49:53 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:54 Orthogonal minimum adversary: best-orientation error 1808.43223153427; exact witness saved.

2026-11-12 22:49:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:54 Orthogonal minimum adversary: best-orientation error 1808.43223153427; exact witness saved.

2026-11-12 22:49:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:54 Orthogonal minimum adversary: best-orientation error 1808.4322315344; exact witness saved.

2026-11-12 22:49:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:54 Orthogonal minimum adversary: best-orientation error 1808.4322315344; exact witness saved.

2026-11-12 22:49:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:54 Orthogonal minimum adversary: best-orientation error 1808.4322315344; exact witness saved.

2026-11-12 22:49:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:54 Orthogonal minimum adversary: best-orientation error 1808.43223153582; exact witness saved.

2026-11-12 22:49:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:54 Orthogonal minimum adversary: best-orientation error 1808.43223153582; exact witness saved.

2026-11-12 22:49:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:54 Orthogonal minimum adversary: best-orientation error 1808.43223153582; exact witness saved.

2026-11-12 22:49:54 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:55 Orthogonal minimum adversary: best-orientation error 1808.43223155007; exact witness saved.

2026-11-12 22:49:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:55 Orthogonal minimum adversary: best-orientation error 1808.43223169256; exact witness saved.

2026-11-12 22:49:55 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:56 Orthogonal minimum adversary: best-orientation error 1808.43223169256; exact witness saved.

2026-11-12 22:49:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:56 Orthogonal minimum adversary: best-orientation error 1808.43223311749; exact witness saved.

2026-11-12 22:49:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:56 Orthogonal minimum adversary: best-orientation error 1808.43223311749; exact witness saved.

2026-11-12 22:49:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:56 Orthogonal minimum adversary: best-orientation error 1808.4322473667; exact witness saved.

2026-11-12 22:49:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:56 Orthogonal minimum adversary: best-orientation error 1808.4322473667; exact witness saved.

2026-11-12 22:49:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:56 Orthogonal minimum adversary: best-orientation error 1808.4322473667; exact witness saved.

2026-11-12 22:49:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:56 Orthogonal minimum adversary: best-orientation error 1808.4322473667; exact witness saved.

2026-11-12 22:49:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:56 Orthogonal minimum adversary: best-orientation error 1808.4322473667; exact witness saved.

2026-11-12 22:49:56 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:57 Orthogonal minimum adversary: best-orientation error 1808.43226319915; exact witness saved.

2026-11-12 22:49:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:57 Orthogonal minimum adversary: best-orientation error 1808.43226319915; exact witness saved.

2026-11-12 22:49:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:57 Orthogonal minimum adversary: best-orientation error 1808.43226319915; exact witness saved.

2026-11-12 22:49:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:57 Orthogonal minimum adversary: best-orientation error 1808.43226319915; exact witness saved.

2026-11-12 22:49:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:57 Orthogonal minimum adversary: best-orientation error 1808.43226319915; exact witness saved.

2026-11-12 22:49:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:57 Orthogonal minimum adversary: best-orientation error 1808.4325481832; exact witness saved.

2026-11-12 22:49:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:57 Orthogonal minimum adversary: best-orientation error 1808.43539800741; exact witness saved.

2026-11-12 22:49:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:57 Orthogonal minimum adversary: best-orientation error 1808.43539800741; exact witness saved.

2026-11-12 22:49:57 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:58 Orthogonal minimum adversary: best-orientation error 1808.43539800741; exact witness saved.

2026-11-12 22:49:58 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:59 Orthogonal minimum adversary: best-orientation error 1808.43856444398; exact witness saved.

2026-11-12 22:49:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:59 Orthogonal minimum adversary: best-orientation error 1808.44489720732; exact witness saved.

2026-11-12 22:49:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:59 Orthogonal minimum adversary: best-orientation error 1808.44489720732; exact witness saved.

2026-11-12 22:49:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:59 Orthogonal minimum adversary: best-orientation error 1808.44489720732; exact witness saved.

2026-11-12 22:49:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:59 Orthogonal minimum adversary: best-orientation error 1808.44489720732; exact witness saved.

2026-11-12 22:49:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:59 Orthogonal minimum adversary: best-orientation error 1808.44489720732; exact witness saved.

2026-11-12 22:49:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:59 Orthogonal minimum adversary: best-orientation error 1808.55886191946; exact witness saved.

2026-11-12 22:49:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:59 Orthogonal minimum adversary: best-orientation error 1808.55886191946; exact witness saved.

2026-11-12 22:49:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:49:59 Orthogonal minimum adversary: best-orientation error 1808.55886191946; exact witness saved.

2026-11-12 22:49:59 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:00 Orthogonal minimum adversary: best-orientation error 1808.55886191946; exact witness saved.

2026-11-12 22:50:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:00 Orthogonal minimum adversary: best-orientation error 1808.55886191946; exact witness saved.

2026-11-12 22:50:00 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.55886191946; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.55886191946; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.55886191946; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.55886191946; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.68543377712; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.68543377712; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:01 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:01 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:02 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:02 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:02 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:02 Orthogonal minimum adversary: best-orientation error 1808.9384020251; exact witness saved.

2026-11-12 22:50:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:02 Orthogonal minimum adversary: best-orientation error 1809.44363745839; exact witness saved.

2026-11-12 22:50:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:02 Orthogonal minimum adversary: best-orientation error 1809.44363745839; exact witness saved.

2026-11-12 22:50:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:02 Orthogonal minimum adversary: best-orientation error 1809.44363745839; exact witness saved.

2026-11-12 22:50:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:02 Orthogonal minimum adversary: best-orientation error 1818.38005697771; exact witness saved.

2026-11-12 22:50:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:02 Orthogonal minimum adversary: best-orientation error 1818.38005697771; exact witness saved.

2026-11-12 22:50:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:02 Orthogonal minimum adversary: best-orientation error 1818.38005697771; exact witness saved.

2026-11-12 22:50:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:02 Orthogonal minimum adversary: best-orientation error 1827.96748109485; exact witness saved.

2026-11-12 22:50:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:02 Orthogonal minimum adversary: best-orientation error 1827.96748109485; exact witness saved.

2026-11-12 22:50:02 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:03 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:03 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:03 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:03 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:03 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:03 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:03 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:03 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:04 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:04 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:04 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:04 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:04 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:04 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:04 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:04 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:04 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:05 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:05 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:06 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:06 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:06 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:06 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:06 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:06 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:06 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:06 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:08 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:08 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:08 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:08 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:08 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:08 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:08 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:09 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:09 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:09 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:09 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:09 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:09 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:09 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:09 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:10 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:10 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:10 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:10 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:10 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:10 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:10 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:10 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:13 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:13 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:13 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:13 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:13 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:13 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:13 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:13 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:13 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:13 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:14 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:14 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:14 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:14 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:14 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:14 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:14 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:14 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:14 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:14 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:15 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:15 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:15 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:15 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:15 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:15 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:15 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:15 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:15 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:15 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:15 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:15 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:15 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:15 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:15 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:15 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:15 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:16 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:16 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:16 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:16 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:16 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:16 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:16 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:16 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:16 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:16 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:16 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:16 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:16 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:16 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:16 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:16 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:16 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:16 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:16 Orthogonal minimum adversary: best-orientation error 1853.05426000316; exact witness saved.

2026-11-12 22:50:16 The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.

2026-11-12 22:50:16 Orthogonal minimum adversary finished: 21428 exact objectives, 110.002s, best 1853.05426000316, peak RSS 29966336 bytes.

2026-11-12 22:52:46 Orthogonal minimum refinement audit passed: 65600 orientations, 16.413s, peak RSS 29294592 bytes. This audits a conditional inequality, not factor 3.

2026-11-12 22:53:22 Final independent hitting-solve audit passed for 36 exact witnesses, including all search incumbents, near-sharp baselines, and both orthogonal-minimum obstructions. All tested singleton ratios <=3. 0.189s; peak RSS 29360128 bytes. No universal upper bound has been proved.

2026-11-12 22:54:12 Exact lead audit: diagonal_family; details saved in k7_leads_results.json.

2026-11-12 22:54:12 Exact lead audit: intermediate_row_sum_exceeds_proposed_budget; details saved in k7_leads_results.json.

2026-11-12 22:54:12 Exact lead audit: removing_orthogonal_boundary_part_loses_nonnegativity; details saved in k7_leads_results.json.

2026-11-12 22:54:12 Exact lead audit: cauchy_schwarz_bound_exceeds_3T; details saved in k7_leads_results.json.

2026-11-12 22:54:15 Lead audit complete: 29400 singleton-pair tests, 3.549s, peak RSS 28737536 bytes.

2026-11-12 22:54:58 Final independent hitting-solve audit passed for 36 exact witnesses, including all search incumbents, near-sharp baselines, and both orthogonal-minimum obstructions. All tested singleton ratios <=3. 0.195s; peak RSS 29900800 bytes. No universal upper bound has been proved.

2026-11-12 22:54:59 REPORT CHECK PASSED: exact fractions, all referenced artifacts, 36 independent winner audits, 24 diagonal family checks, shortcut obstructions, resource metadata, and explicit unresolved K(7) statement. 0.044s; peak RSS 28033024 bytes.
