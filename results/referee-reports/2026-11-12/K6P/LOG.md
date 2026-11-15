# Q2 research log

2026-11-12 (local session). Task: determine whether an r-merge lumping satisfies tmix(quotient) <= (r+1) tmix(original), especially r=2; exact searches on 4–8 states and a proof attempt.

Read K5P_REPORT.md and q1_core.py first. The supplied report proves the entrywise one-pair bound Fhat <= t_i+t_j and the separate (q-1) bound. The fork-comb constructor uses n=2N+4, q=N+3, r=N+1 and approaches ratio N+2. Its script has top-level computations, so its constructor will be copied locally rather than imported.

All task work is confined to this directory. No external brain/checklist/mesh commands are run: they mutate files outside the explicitly authorized directory. No agents, web, git push, or visible windows. Computations will run sequentially with numerical-library thread counts fixed at one, with each run limited to less than five minutes. Programs are saved before execution.

2026-11-12 21:59:47 Exact random n=4: 20 networks, 160 partitions; elapsed 0.014s, peak RSS 27754496 bytes.

2026-11-12 22:00:02 Exact random n=8: 20 networks, 26320 partitions; elapsed 11.341s, peak RSS 27918336 bytes.

2026-11-12 22:01:07 Exact structured n=8: 24 networks, 31584 partitions; elapsed 9.950s, peak RSS 28950528 bytes.

2026-11-12 22:02:02 Exact random n=5: 20 networks, 800 partitions; elapsed 0.081s, peak RSS 28164096 bytes.

2026-11-12 22:02:02 Exact random n=6: 20 networks, 3100 partitions; elapsed 0.587s, peak RSS 28573696 bytes.

2026-11-12 22:02:05 Exact random n=7: 20 networks, 9800 partitions; elapsed 2.841s, peak RSS 28803072 bytes.

2026-11-12 22:02:05 Exact structured n=4: 16 networks, 128 partitions; elapsed 0.010s, peak RSS 28803072 bytes.

2026-11-12 22:02:05 Exact structured n=5: 16 networks, 640 partitions; elapsed 0.077s, peak RSS 28803072 bytes.

2026-11-12 22:02:06 Exact structured n=6: 20 networks, 3100 partitions; elapsed 0.476s, peak RSS 28803072 bytes.

2026-11-12 22:02:08 Exact structured n=7: 20 networks, 9800 partitions; elapsed 2.214s, peak RSS 28803072 bytes.

2026-11-12 22:02:15 Optimized n=7, r=2, seed=1121: 27458 numerical evaluations; 6 rounded candidates scanned over every r-merge partition exactly; elapsed 3.935s, peak RSS 74629120 bytes.

2026-11-12 22:04:37 Exact shape scan n=4 complete, 26 networks; cumulative entrywise checks 2704.

2026-11-12 22:04:38 Exact shape scan n=5 complete, 26 networks; cumulative entrywise checks 21684.

2026-11-12 22:04:40 Exact shape scan n=6 complete, 30 networks; cumulative entrywise checks 135084.

2026-11-12 22:04:50 Exact shape scan n=7 complete, 30 networks; cumulative entrywise checks 597084.

2026-11-12 22:05:18 Exact shape scan n=8 complete, 34 networks; cumulative entrywise checks 2361140.

2026-11-12 22:05:26 Optimized n=4, r=2, seed=11262: 3396 numerical evaluations; 6 rounded candidates scanned over every r-merge partition exactly; elapsed 0.745s, peak RSS 73531392 bytes.

2026-11-12 22:05:26 Optimized n=4, r=3, seed=11263: 0 numerical evaluations; 0 rounded candidates scanned over every r-merge partition exactly; elapsed 0.000s, peak RSS 73531392 bytes.

2026-11-12 22:05:27 Optimized n=5, r=2, seed=11272: 17754 numerical evaluations; 6 rounded candidates scanned over every r-merge partition exactly; elapsed 1.237s, peak RSS 73531392 bytes.

2026-11-12 22:05:27 Optimized n=5, r=3, seed=11273: 4897 numerical evaluations; 6 rounded candidates scanned over every r-merge partition exactly; elapsed 0.322s, peak RSS 73547776 bytes.

2026-11-12 22:05:29 Optimized n=6, r=2, seed=11282: 23101 numerical evaluations; 6 rounded candidates scanned over every r-merge partition exactly; elapsed 1.782s, peak RSS 73760768 bytes.

2026-11-12 22:05:32 Optimized n=6, r=3, seed=11283: 38886 numerical evaluations; 9 rounded candidates scanned over every r-merge partition exactly; elapsed 3.178s, peak RSS 73924608 bytes.

2026-11-12 22:05:35 Optimized n=7, r=2, seed=11292: 34218 numerical evaluations; 6 rounded candidates scanned over every r-merge partition exactly; elapsed 3.220s, peak RSS 74186752 bytes.

2026-11-12 22:05:41 Optimized n=7, r=3, seed=11293: 47224 numerical evaluations; 9 rounded candidates scanned over every r-merge partition exactly; elapsed 5.267s, peak RSS 74891264 bytes.

2026-11-12 22:05:45 Optimized n=8, r=2, seed=11302: 39360 numerical evaluations; 6 rounded candidates scanned over every r-merge partition exactly; elapsed 4.523s, peak RSS 75218944 bytes.

2026-11-12 22:05:57 Optimized n=8, r=3, seed=11303: 60082 numerical evaluations; 9 rounded candidates scanned over every r-merge partition exactly; elapsed 11.984s, peak RSS 75612160 bytes.

2026-11-12 22:10:23 Exact optimizer n=7, shape=(3,), improved to 1.9999969600052; exact witness saved (evaluation 209).

2026-11-12 22:10:23 Exact optimizer n=7, shape=(3,), improved to 1.9999969600052; exact witness saved (evaluation 211).

2026-11-12 22:10:23 Exact optimizer n=7, shape=(3,), improved to 1.9999969600052; exact witness saved (evaluation 218).

2026-11-12 22:10:23 Exact optimizer n=7, shape=(3,), improved to 1.9999969600052; exact witness saved (evaluation 220).

2026-11-12 22:10:23 Exact optimizer n=7, shape=(3,), improved to 1.9999969600052; exact witness saved (evaluation 222).

2026-11-12 22:10:23 Exact optimizer n=7, shape=(3,), improved to 1.9999969600052; exact witness saved (evaluation 223).

2026-11-12 22:10:23 Exact optimizer n=7, shape=(3,), improved to 1.9999969600052; exact witness saved (evaluation 225).

2026-11-12 22:10:24 Exact optimizer n=7, shape=(3,), improved to 1.99999697800511; exact witness saved (evaluation 414).

2026-11-12 22:10:24 Exact optimizer n=7, shape=(3,), improved to 1.99999697800511; exact witness saved (evaluation 425).

2026-11-12 22:10:24 Exact optimizer n=7, shape=(3,), improved to 1.99999697800512; exact witness saved (evaluation 426).

2026-11-12 22:10:24 Exact optimizer n=7, shape=(3,), improved to 1.99999697980511; exact witness saved (evaluation 430).

2026-11-12 22:10:25 Exact optimizer n=7, shape=(3,), improved to 1.99999699596522; exact witness saved (evaluation 467).

2026-11-12 22:10:25 Exact optimizer n=7, shape=(3,), improved to 1.99999699596522; exact witness saved (evaluation 468).

2026-11-12 22:10:26 Exact optimizer n=7, shape=(3,), improved to 1.99999699596522; exact witness saved (evaluation 798).

2026-11-12 22:10:26 Exact optimizer n=7, shape=(3,), improved to 1.99999699776521; exact witness saved (evaluation 799).

2026-11-12 22:10:26 Exact optimizer n=7, shape=(3,), improved to 1.99999699778421; exact witness saved (evaluation 808).

2026-11-12 22:10:26 Exact optimizer n=7, shape=(3,), improved to 1.99999699778421; exact witness saved (evaluation 810).

2026-11-12 22:10:26 Exact optimizer n=7, shape=(3,), improved to 1.99999699780221; exact witness saved (evaluation 812).

2026-11-12 22:10:26 Exact optimizer n=7, shape=(3,), improved to 1.999996999604; exact witness saved (evaluation 813).

2026-11-12 22:10:26 Exact optimizer n=7, shape=(3,), improved to 1.999996999604; exact witness saved (evaluation 816).

2026-11-12 22:10:28 Exact optimizer n=7, shape=(3,), improved to 1.999996999604; exact witness saved (evaluation 997).

2026-11-12 22:10:28 Exact optimizer n=7, shape=(3,), improved to 1.999996999606; exact witness saved (evaluation 998).

2026-11-12 22:10:28 Exact optimizer n=7, shape=(3,), improved to 1.999996999606; exact witness saved (evaluation 999).

2026-11-12 22:10:28 Exact optimizer n=7, shape=(3,), improved to 1.999996999606; exact witness saved (evaluation 1001).

2026-11-12 22:10:28 Exact optimizer n=7, shape=(3,), improved to 1.999996999606; exact witness saved (evaluation 1003).

2026-11-12 22:10:28 Exact optimizer n=7, shape=(3,), improved to 1.999996999606; exact witness saved (evaluation 1005).

2026-11-12 22:10:29 Exact optimizer n=7, shape=(3,), improved to 1.99999699966281; exact witness saved (evaluation 1138).

2026-11-12 22:10:29 Exact optimizer n=7, shape=(3,), improved to 1.99999699968585; exact witness saved (evaluation 1143).

2026-11-12 22:10:30 Exact optimizer n=7, shape=(3,), improved to 1.99999699968586; exact witness saved (evaluation 1397).

2026-11-12 22:10:30 Exact optimizer n=7, shape=(3,), improved to 1.99999701116984; exact witness saved (evaluation 1400).

2026-11-12 22:10:33 Exact optimizer n=7, shape=(3,), improved to 1.99999701542997; exact witness saved (evaluation 1721).

2026-11-12 22:10:33 Exact optimizer n=7, shape=(3,), improved to 1.99999701542997; exact witness saved (evaluation 1722).

2026-11-12 22:10:33 Exact optimizer n=7, shape=(3,), improved to 1.99999701548757; exact witness saved (evaluation 1723).

2026-11-12 22:10:33 Exact optimizer n=7, shape=(3,), improved to 1.99999701548757; exact witness saved (evaluation 1725).

2026-11-12 22:10:33 Exact optimizer n=7, shape=(3,), improved to 1.9999970795924; exact witness saved (evaluation 1738).

2026-11-12 22:10:34 Exact optimizer n=7, shape=(3,), improved to 1.99999780532755; exact witness saved (evaluation 1990).

2026-11-12 22:10:34 Exact optimizer n=7, shape=(3,), improved to 1.999998999626; exact witness saved (evaluation 2004).

2026-11-12 22:10:34 Exact optimizer n=7, shape=(3,), improved to 1.999998999626; exact witness saved (evaluation 2005).

2026-11-12 22:10:36 Exact optimizer n=7, shape=(3,), improved to 1.99999899962602; exact witness saved (evaluation 2191).

2026-11-12 22:10:36 Exact optimizer n=7, shape=(3,), improved to 1.99999899962602; exact witness saved (evaluation 2192).

2026-11-12 22:10:37 Exact optimizer n=7, shape=(3,), improved to 1.99999899963873; exact witness saved (evaluation 2230).

2026-11-12 22:10:37 Exact optimizer n=7, shape=(3,), improved to 1.99999899965873; exact witness saved (evaluation 2231).

2026-11-12 22:10:37 Exact optimizer n=7, shape=(3,), improved to 1.99999899986366; exact witness saved (evaluation 2233).

2026-11-12 22:10:37 Exact optimizer n=7, shape=(3,), improved to 1.99999899987587; exact witness saved (evaluation 2236).

2026-11-12 22:10:37 Exact optimizer n=7, shape=(3,), improved to 1.99999899987627; exact witness saved (evaluation 2238).

2026-11-12 22:10:37 Exact optimizer n=7, shape=(3,), improved to 1.99999899989281; exact witness saved (evaluation 2250).

2026-11-12 22:10:39 Exact optimizer n=7, shape=(3,), improved to 1.99999899989298; exact witness saved (evaluation 2586).

2026-11-12 22:10:39 Exact optimizer n=7, shape=(3,), improved to 1.99999899989298; exact witness saved (evaluation 2587).

2026-11-12 22:10:39 Exact optimizer n=7, shape=(3,), improved to 1.99999899989315; exact witness saved (evaluation 2597).

2026-11-12 22:10:39 Exact optimizer n=7, shape=(3,), improved to 1.99999899989511; exact witness saved (evaluation 2607).

2026-11-12 22:10:39 Exact optimizer n=7, shape=(3,), improved to 1.99999899989511; exact witness saved (evaluation 2608).

2026-11-12 22:10:39 Exact optimizer n=7, shape=(3,), improved to 1.99999899989519; exact witness saved (evaluation 2609).

2026-11-12 22:10:39 Exact optimizer n=7, shape=(3,), improved to 1.99999899989519; exact witness saved (evaluation 2611).

2026-11-12 22:10:40 Exact optimizer n=7, shape=(3,), improved to 1.99999899995459; exact witness saved (evaluation 2674).

2026-11-12 22:10:40 Exact optimizer n=7, shape=(3,), improved to 1.99999899995459; exact witness saved (evaluation 2677).

2026-11-12 22:10:40 Exact optimizer n=7, shape=(3,), improved to 1.99999899996168; exact witness saved (evaluation 2684).

2026-11-12 22:10:40 Exact optimizer n=7, shape=(3,), improved to 1.99999899996168; exact witness saved (evaluation 2685).

2026-11-12 22:10:40 Exact optimizer n=7, shape=(3,), improved to 1.99999899997418; exact witness saved (evaluation 2686).

2026-11-12 22:10:40 Exact optimizer n=7, shape=(3,), improved to 1.99999899997418; exact witness saved (evaluation 2687).

2026-11-12 22:10:40 Exact optimizer n=7, shape=(3,), improved to 1.99999899997424; exact witness saved (evaluation 2688).

2026-11-12 22:10:40 Exact optimizer n=7, shape=(3,), improved to 1.99999899998549; exact witness saved (evaluation 2691).

2026-11-12 22:10:40 Exact optimizer n=7, shape=(3,), improved to 1.99999899998561; exact witness saved (evaluation 2693).

2026-11-12 22:10:40 Exact optimizer n=7, shape=(3,), improved to 1.99999899998773; exact witness saved (evaluation 2705).

2026-11-12 22:10:40 Exact optimizer n=7, shape=(3,), improved to 1.99999899998773; exact witness saved (evaluation 2706).

2026-11-12 22:10:40 Exact optimizer n=7, shape=(3,), improved to 1.99999899998773; exact witness saved (evaluation 2708).

2026-11-12 22:10:40 Exact optimizer n=7, shape=(3,), improved to 1.99999899998773; exact witness saved (evaluation 2709).

2026-11-12 22:10:40 Exact optimizer n=7, shape=(3,), improved to 1.99999899998774; exact witness saved (evaluation 2710).

2026-11-12 22:10:40 Exact optimizer n=7, shape=(3,), improved to 1.99999899999024; exact witness saved (evaluation 2711).

2026-11-12 22:10:41 Exact optimizer n=7, shape=(3,), improved to 1.99999899999384; exact witness saved (evaluation 2784).

2026-11-12 22:10:41 Exact optimizer n=7, shape=(3,), improved to 1.99999899999609; exact witness saved (evaluation 2785).

2026-11-12 22:10:41 Exact optimizer n=7, shape=(3,), improved to 1.99999899999834; exact witness saved (evaluation 2786).

2026-11-12 22:10:41 Exact optimizer n=7, shape=(3,), improved to 1.99999899999834; exact witness saved (evaluation 2787).

2026-11-12 22:10:41 Exact optimizer n=7, shape=(3,), improved to 1.9999989999987; exact witness saved (evaluation 2788).

2026-11-12 22:10:43 Exact optimizer n=7, shape=(3,), improved to 1.9999989999987; exact witness saved (evaluation 3184).

2026-11-12 22:10:43 Exact optimizer n=7, shape=(3,), improved to 1.9999989999987; exact witness saved (evaluation 3187).

2026-11-12 22:10:45 Exact optimizer n=7, shape=(3,), improved to 1.99999899999882; exact witness saved (evaluation 3378).

2026-11-12 22:10:48 Exact optimizer n=7, shape=(3,), improved to 1.99999899999882; exact witness saved (evaluation 3774).

2026-11-12 22:10:48 Exact optimizer n=7, shape=(3,), improved to 1.99999899999885; exact witness saved (evaluation 3778).

2026-11-12 22:10:48 Exact optimizer n=7, shape=(3,), improved to 1.99999899999885; exact witness saved (evaluation 3779).

2026-11-12 22:10:48 Exact optimizer n=7, shape=(3,), improved to 1.99999899999892; exact witness saved (evaluation 3780).

2026-11-12 22:10:48 Exact optimizer n=7, shape=(3,), improved to 1.99999899999892; exact witness saved (evaluation 3781).

2026-11-12 22:10:48 Exact optimizer n=7, shape=(3,), improved to 1.99999899999964; exact witness saved (evaluation 3787).

2026-11-12 22:10:48 Exact optimizer n=7, shape=(3,), improved to 1.99999900000036; exact witness saved (evaluation 3790).

2026-11-12 22:10:48 Exact optimizer n=7, shape=(3,), improved to 1.99999900000036; exact witness saved (evaluation 3791).

2026-11-12 22:10:48 Exact optimizer n=7, shape=(3,), improved to 1.99999900000036; exact witness saved (evaluation 3792).

2026-11-12 22:10:48 Exact optimizer n=7, shape=(3,), improved to 1.99999900000036; exact witness saved (evaluation 3793).

2026-11-12 22:10:52 Exact optimizer n=7, shape=(3,), improved to 1.99999900000037; exact witness saved (evaluation 4378).

2026-11-12 22:11:01 Exact optimizer n=7, shape=(3,), improved to 1.99999900000037; exact witness saved (evaluation 5568).

2026-11-12 22:11:01 Exact optimizer n=7, shape=(3,), improved to 1.9999990000005; exact witness saved (evaluation 5569).

2026-11-12 22:11:01 Exact optimizer n=7, shape=(3,), improved to 1.9999990000005; exact witness saved (evaluation 5574).

2026-11-12 22:11:02 Exact optimizer n=7, shape=(3,), improved to 1.99999900000084; exact witness saved (evaluation 5645).

2026-11-12 22:11:02 Exact optimizer n=7, shape=(3,), improved to 1.99999900000084; exact witness saved (evaluation 5647).

2026-11-12 22:11:02 Exact optimizer n=7, shape=(3,), improved to 1.99999900000084; exact witness saved (evaluation 5648).

2026-11-12 22:11:02 Exact optimizer n=7, shape=(3,), improved to 1.99999900000086; exact witness saved (evaluation 5654).

2026-11-12 22:11:02 Exact optimizer n=7, shape=(3,), improved to 1.99999900000086; exact witness saved (evaluation 5655).

2026-11-12 22:11:02 Exact optimizer n=7, shape=(3,), improved to 1.99999900000086; exact witness saved (evaluation 5657).

2026-11-12 22:11:02 Exact optimizer n=7, shape=(3,), improved to 1.99999900000087; exact witness saved (evaluation 5658).

2026-11-12 22:11:06 Exact optimizer n=7, shape=(3,), improved to 1.99999900000088; exact witness saved (evaluation 6161).

2026-11-12 22:11:10 Exact optimizer n=7, shape=(3,), improved to 1.99999900000088; exact witness saved (evaluation 6755).

2026-11-12 22:11:10 Exact optimizer n=7, shape=(3,), improved to 1.99999900000088; exact witness saved (evaluation 6756).

2026-11-12 22:11:10 Exact optimizer n=7, shape=(3,), improved to 1.99999900000088; exact witness saved (evaluation 6757).

2026-11-12 22:11:12 Exact optimizer n=7, shape=(3,), improved to 1.99999900000088; exact witness saved (evaluation 6951).

2026-11-12 22:11:15 Exact optimizer n=7, shape=(3,), improved to 1.99999900000088; exact witness saved (evaluation 7345).

2026-11-12 22:11:15 Exact optimizer n=7, shape=(3,), improved to 1.99999900000088; exact witness saved (evaluation 7348).

2026-11-12 22:11:17 Exact optimizer n=7, shape=(3,), improved to 1.99999900000088; exact witness saved (evaluation 7544).

2026-11-12 22:11:17 Exact optimizer n=7, shape=(3,), improved to 1.99999900000088; exact witness saved (evaluation 7545).

2026-11-12 22:11:18 Exact optimizer n=7, shape=(3,), improved to 1.99999900000098; exact witness saved (evaluation 7610).

2026-11-12 22:11:18 Exact optimizer n=7, shape=(3,), improved to 1.99999900000098; exact witness saved (evaluation 7615).

2026-11-12 22:11:18 Exact optimizer n=7, shape=(3,), improved to 1.99999900000098; exact witness saved (evaluation 7616).

2026-11-12 22:11:18 Exact optimizer n=7, shape=(3,), improved to 1.99999900000098; exact witness saved (evaluation 7617).

2026-11-12 22:11:18 Exact optimizer n=7, shape=(3,), improved to 1.99999900000098; exact witness saved (evaluation 7620).

2026-11-12 22:11:18 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 7640).

2026-11-12 22:11:18 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 7644).

2026-11-12 22:11:22 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 8149).

2026-11-12 22:11:25 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 8537).

2026-11-12 22:11:27 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 8740).

2026-11-12 22:11:27 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 8742).

2026-11-12 22:11:30 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 9135).

2026-11-12 22:11:30 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 9173).

2026-11-12 22:11:34 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 9735).

2026-11-12 22:11:35 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 9780).

2026-11-12 22:11:35 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 9783).

2026-11-12 22:11:35 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 9784).

2026-11-12 22:11:35 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 9797).

2026-11-12 22:11:35 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 9798).

2026-11-12 22:11:35 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 9809).

2026-11-12 22:11:36 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 9926).

2026-11-12 22:11:36 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 9927).

2026-11-12 22:11:39 Exact optimizer n=7, shape=(3,), improved to 1.99999900000099; exact witness saved (evaluation 10315).

2026-11-12 22:11:44 Exact optimizer completed n=7, shape=(3,), best 1.99999900000099, 10737 cumulative exact evaluations.

2026-11-12 22:11:45 Exact optimizer n=7, shape=(2, 2), improved to 2.9999937272853; exact witness saved (evaluation 10944).

2026-11-12 22:11:45 Exact optimizer n=7, shape=(2, 2), improved to 2.99999385714972; exact witness saved (evaluation 10950).

2026-11-12 22:11:45 Exact optimizer n=7, shape=(2, 2), improved to 2.99999684285475; exact witness saved (evaluation 10954).

2026-11-12 22:11:45 Exact optimizer n=7, shape=(2, 2), improved to 2.99999696732861; exact witness saved (evaluation 10961).

2026-11-12 22:11:50 Exact optimizer n=7, shape=(2, 2), improved to 2.9999969673292; exact witness saved (evaluation 11535).

2026-11-12 22:11:52 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699371499; exact witness saved (evaluation 11755).

2026-11-12 22:11:52 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699937307; exact witness saved (evaluation 11759).

2026-11-12 22:11:56 Exact optimizer n=7, shape=(2, 2), improved to 2.9999969993731; exact witness saved (evaluation 12323).

2026-11-12 22:11:58 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699940309; exact witness saved (evaluation 12721).

2026-11-12 22:11:58 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699970302; exact witness saved (evaluation 12731).

2026-11-12 22:11:58 Exact optimizer n=7, shape=(2, 2), improved to 2.999996999853; exact witness saved (evaluation 12732).

2026-11-12 22:11:59 Exact optimizer n=7, shape=(2, 2), improved to 2.999996999913; exact witness saved (evaluation 12838).

2026-11-12 22:11:59 Exact optimizer n=7, shape=(2, 2), improved to 2.999996999913; exact witness saved (evaluation 12840).

2026-11-12 22:11:59 Exact optimizer n=7, shape=(2, 2), improved to 2.999996999918; exact witness saved (evaluation 12848).

2026-11-12 22:11:59 Exact optimizer n=7, shape=(2, 2), improved to 2.999996999918; exact witness saved (evaluation 12851).

2026-11-12 22:11:59 Exact optimizer n=7, shape=(2, 2), improved to 2.999996999918; exact witness saved (evaluation 12864).

2026-11-12 22:11:59 Exact optimizer n=7, shape=(2, 2), improved to 2.9999969999225; exact witness saved (evaluation 12871).

2026-11-12 22:11:59 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699999; exact witness saved (evaluation 12923).

2026-11-12 22:11:59 Exact optimizer n=7, shape=(2, 2), improved to 2.9999969999925; exact witness saved (evaluation 12929).

2026-11-12 22:11:59 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699999275; exact witness saved (evaluation 12930).

2026-11-12 22:11:59 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699999275; exact witness saved (evaluation 12931).

2026-11-12 22:11:59 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699999275; exact witness saved (evaluation 12936).

2026-11-12 22:12:00 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699999625; exact witness saved (evaluation 12969).

2026-11-12 22:12:00 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699999647; exact witness saved (evaluation 12970).

2026-11-12 22:12:01 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699999888; exact witness saved (evaluation 13082).

2026-11-12 22:12:01 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699999888; exact witness saved (evaluation 13084).

2026-11-12 22:12:01 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699999969; exact witness saved (evaluation 13108).

2026-11-12 22:12:01 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699999969; exact witness saved (evaluation 13110).

2026-11-12 22:12:01 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699999969; exact witness saved (evaluation 13111).

2026-11-12 22:12:01 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699999975; exact witness saved (evaluation 13113).

2026-11-12 22:12:02 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699999975; exact witness saved (evaluation 13318).

2026-11-12 22:12:03 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699999975; exact witness saved (evaluation 13517).

2026-11-12 22:12:03 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699999975; exact witness saved (evaluation 13518).

2026-11-12 22:12:03 Exact optimizer n=7, shape=(2, 2), improved to 2.99999699999978; exact witness saved (evaluation 13519).

2026-11-12 22:12:03 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000103; exact witness saved (evaluation 13533).

2026-11-12 22:12:03 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000103; exact witness saved (evaluation 13534).

2026-11-12 22:12:03 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000103; exact witness saved (evaluation 13541).

2026-11-12 22:12:03 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000106; exact witness saved (evaluation 13548).

2026-11-12 22:12:09 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000106; exact witness saved (evaluation 14510).

2026-11-12 22:12:11 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000124; exact witness saved (evaluation 14710).

2026-11-12 22:12:11 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000124; exact witness saved (evaluation 14711).

2026-11-12 22:12:15 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000124; exact witness saved (evaluation 15304).

2026-11-12 22:12:17 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000124; exact witness saved (evaluation 15703).

2026-11-12 22:12:17 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000124; exact witness saved (evaluation 15706).

2026-11-12 22:12:17 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000125; exact witness saved (evaluation 15707).

2026-11-12 22:12:17 Exact optimizer n=7, shape=(2, 2), improved to 2.9999970000014; exact witness saved (evaluation 15710).

2026-11-12 22:12:17 Exact optimizer n=7, shape=(2, 2), improved to 2.9999970000014; exact witness saved (evaluation 15711).

2026-11-12 22:12:19 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000173; exact witness saved (evaluation 15897).

2026-11-12 22:12:19 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000173; exact witness saved (evaluation 15898).

2026-11-12 22:12:21 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000178; exact witness saved (evaluation 16302).

2026-11-12 22:12:21 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000178; exact witness saved (evaluation 16306).

2026-11-12 22:12:21 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000188; exact witness saved (evaluation 16311).

2026-11-12 22:12:21 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000188; exact witness saved (evaluation 16316).

2026-11-12 22:12:22 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000219; exact witness saved (evaluation 16498).

2026-11-12 22:12:23 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000219; exact witness saved (evaluation 16517).

2026-11-12 22:12:23 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000235; exact witness saved (evaluation 16522).

2026-11-12 22:12:26 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000254; exact witness saved (evaluation 17090).

2026-11-12 22:12:26 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000254; exact witness saved (evaluation 17092).

2026-11-12 22:12:28 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000254; exact witness saved (evaluation 17488).

2026-11-12 22:12:28 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000269; exact witness saved (evaluation 17518).

2026-11-12 22:12:28 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000269; exact witness saved (evaluation 17519).

2026-11-12 22:12:28 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000269; exact witness saved (evaluation 17522).

2026-11-12 22:12:28 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000269; exact witness saved (evaluation 17526).

2026-11-12 22:12:28 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000269; exact witness saved (evaluation 17528).

2026-11-12 22:12:28 Exact optimizer n=7, shape=(2, 2), improved to 2.9999970000027; exact witness saved (evaluation 17530).

2026-11-12 22:12:28 Exact optimizer n=7, shape=(2, 2), improved to 2.9999970000027; exact witness saved (evaluation 17531).

2026-11-12 22:12:30 Exact optimizer n=7, shape=(2, 2), improved to 2.9999970000027; exact witness saved (evaluation 17690).

2026-11-12 22:12:30 Exact optimizer n=7, shape=(2, 2), improved to 2.9999970000027; exact witness saved (evaluation 17694).

2026-11-12 22:12:30 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000271; exact witness saved (evaluation 17700).

2026-11-12 22:12:30 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000271; exact witness saved (evaluation 17702).

2026-11-12 22:12:30 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000271; exact witness saved (evaluation 17703).

2026-11-12 22:12:30 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000271; exact witness saved (evaluation 17704).

2026-11-12 22:12:30 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000271; exact witness saved (evaluation 17705).

2026-11-12 22:12:30 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000271; exact witness saved (evaluation 17709).

2026-11-12 22:12:30 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000271; exact witness saved (evaluation 17710).

2026-11-12 22:12:30 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000271; exact witness saved (evaluation 17713).

2026-11-12 22:12:30 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000271; exact witness saved (evaluation 17717).

2026-11-12 22:12:30 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000271; exact witness saved (evaluation 17719).

2026-11-12 22:12:30 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000279; exact witness saved (evaluation 17747).

2026-11-12 22:12:30 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000279; exact witness saved (evaluation 17748).

2026-11-12 22:12:32 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000286; exact witness saved (evaluation 18089).

2026-11-12 22:12:32 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000286; exact witness saved (evaluation 18090).

2026-11-12 22:12:32 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000286; exact witness saved (evaluation 18091).

2026-11-12 22:12:32 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000286; exact witness saved (evaluation 18092).

2026-11-12 22:12:32 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000286; exact witness saved (evaluation 18093).

2026-11-12 22:12:32 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000288; exact witness saved (evaluation 18094).

2026-11-12 22:12:34 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000289; exact witness saved (evaluation 18284).

2026-11-12 22:12:34 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000289; exact witness saved (evaluation 18287).

2026-11-12 22:12:34 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000289; exact witness saved (evaluation 18291).

2026-11-12 22:12:34 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000291; exact witness saved (evaluation 18324).

2026-11-12 22:12:34 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000291; exact witness saved (evaluation 18326).

2026-11-12 22:12:34 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000291; exact witness saved (evaluation 18339).

2026-11-12 22:12:34 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000292; exact witness saved (evaluation 18346).

2026-11-12 22:12:34 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000297; exact witness saved (evaluation 18350).

2026-11-12 22:12:34 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000297; exact witness saved (evaluation 18356).

2026-11-12 22:12:34 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000297; exact witness saved (evaluation 18357).

2026-11-12 22:12:34 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000297; exact witness saved (evaluation 18359).

2026-11-12 22:12:34 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000297; exact witness saved (evaluation 18360).

2026-11-12 22:12:34 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000298; exact witness saved (evaluation 18368).

2026-11-12 22:12:35 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000298; exact witness saved (evaluation 18398).

2026-11-12 22:12:35 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000298; exact witness saved (evaluation 18399).

2026-11-12 22:12:35 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000298; exact witness saved (evaluation 18401).

2026-11-12 22:12:35 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000298; exact witness saved (evaluation 18404).

2026-11-12 22:12:35 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000298; exact witness saved (evaluation 18405).

2026-11-12 22:12:35 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000299; exact witness saved (evaluation 18418).

2026-11-12 22:12:35 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000299; exact witness saved (evaluation 18420).

2026-11-12 22:12:35 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000299; exact witness saved (evaluation 18422).

2026-11-12 22:12:36 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000299; exact witness saved (evaluation 18694).

2026-11-12 22:12:37 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000299; exact witness saved (evaluation 18780).

2026-11-12 22:12:37 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000299; exact witness saved (evaluation 18804).

2026-11-12 22:12:37 Exact optimizer n=7, shape=(2, 2), improved to 2.99999700000299; exact witness saved (evaluation 18805).

2026-11-12 22:12:37 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 18824).

2026-11-12 22:12:37 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 18825).

2026-11-12 22:12:38 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 18882).

2026-11-12 22:12:38 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 18888).

2026-11-12 22:12:38 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 18889).

2026-11-12 22:12:38 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 18891).

2026-11-12 22:12 +04. Proved merged-source lemma for one arbitrary block B. Let h(x)=E_x T_B and nu=(d-Lh)/W. On B, Lh<=0; outside B, Lh=d. Thus nu is a probability supported on B. From LF_.b=d-We_b and centering, h-E_pi h=sum_b nu_b F_.b. Since the quotient grounded at B has potential h, Fhat_{B,f(j)}=h(j)-E_pi h=sum_b nu_b F_jb <= t_j. The diagonal at B is -E_pi h. This is a proof, not an empirical conjecture.

Consequence for two disjoint pairs: wire pair A last. The merged-source lemma bounds entries incident to A by row maxima after wiring pair B, which Q1 bounds by t_j+T<=2T. Exchange A and B for entries incident to B. For a triple, all entries incident to the triple are <=T. Any rank-two counterexample to factor 3 therefore requires its maximizing pair to consist of two singleton blocks. This reduction does not prove their bound or settle K(7).

The exact shape scan checked 2,361,140 representative-level entry inequalities on 146 networks, including all r=2 and r=3 partitions. It found no failure of Fhat_{f(i),f(j)} <= t_i+t_j+(r-1)T, or of the stronger numerical conjecture T_hat <= (number of nonsingleton blocks+1)T. Neither is proved by these tests. Files: q2_shape_search.py, q2_shape_output.txt, q2_shape_results.json.

2026-11-12 22:12:40 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19280).

2026-11-12 22:12:40 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19282).

2026-11-12 22:12:40 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19283).

2026-11-12 22:12:40 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19286).

2026-11-12 22:12:40 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19288).

2026-11-12 22:12:40 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19289).

2026-11-12 22:12:40 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19291).

2026-11-12 22:12:40 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19294).

2026-11-12 22:12:40 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19296).

2026-11-12 22:12:40 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19298).

2026-11-12 22:12:40 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19300).

2026-11-12 22:12:40 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19301).

2026-11-12 22:12:40 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19322).

2026-11-12 22:12:41 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19349).

2026-11-12 22:12:41 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19350).

2026-11-12 22:12:41 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19352).

2026-11-12 22:12:41 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19357).

2026-11-12 22:12:41 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19359).

2026-11-12 22:12:41 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19360).

2026-11-12 22:12:41 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19378).

2026-11-12 22:12:41 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19395).

2026-11-12 22:12:41 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19398).

2026-11-12 22:12:44 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19881).

2026-11-12 22:12:44 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19885).

2026-11-12 22:12:44 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 19918).

2026-11-12 22:12:46 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20076).

2026-11-12 22:12:46 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20080).

2026-11-12 22:12:46 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20081).

2026-11-12 22:12:46 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20101).

2026-11-12 22:12:46 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20102).

2026-11-12 22:12:46 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20103).

2026-11-12 22:12:46 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20107).

2026-11-12 22:12:46 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20108).

2026-11-12 22:12:46 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20109).

2026-11-12 22:12:46 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20112).

2026-11-12 22:12:48 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20478).

2026-11-12 22:12:48 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20479).

2026-11-12 22:12:48 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20481).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20482).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20484).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20485).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20487).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20488).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20493).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20510).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20511).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20512).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20513).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20514).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20518).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20524).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20525).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20526).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20550).

2026-11-12 22:12:49 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 20555).

2026-11-12 22:12:53 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 21069).

2026-11-12 22:12:53 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 21100).

2026-11-12 22:12:53 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 21102).

2026-11-12 22:12:54 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 21261).

2026-11-12 22:12:58 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 21858).

2026-11-12 22:12:58 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 21859).

2026-11-12 22:12:58 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 21860).

2026-11-12 22:13:01 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 22255).

2026-11-12 22:13:02 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 22461).

2026-11-12 22:13:02 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 22467).

2026-11-12 22:13:02 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 22469).

2026-11-12 22:13:06 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 23050).

2026-11-12 22:13:06 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 23053).

2026-11-12 22:13:09 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 23511).

2026-11-12 22:13:09 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 23512).

2026-11-12 22:13:09 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 23519).

2026-11-12 22:13:10 Exact optimizer n=7, shape=(2, 2), improved to 2.999997000003; exact witness saved (evaluation 23637).

2026-11-12 22:13:12 Exact optimizer completed n=7, shape=(2, 2), best 2.999997000003, 23818 cumulative exact evaluations.

2026-11-12 22:13:12 Exact optimization n=7, seed=22117: 23818 exact objectives, 15756 accepted proposals, 170.004s, peak RSS 30031872 bytes.

2026-11-12 22:20 +04. Clone-padding audit caught an incorrect shortcut before use: splitting a vertex in a block that is later merged, while leaving the new clone singleton, does not produce a cloned quotient. The intended equality of quotient times failed exactly at (n,r)=(7,2). The correction is to clone a singleton untouched by the partition (state a), or to put all clones into the same merged block when the merge deficit is meant to increase. The failed run remains in q2_family_output_failed.txt; every corrected family is independently rechecked below.

2026-11-12 22:17:41 Exact compact families at t=10^12, iid examples, and clone padding checked by independent hitting solves. Best ratios are exactly 1, 0, R2, R3, R4 as recorded in q2_family_results.json. Elapsed 1.978s; peak RSS 28114944 bytes.

2026-11-12 22:19:44 Independent exact audit PASSED: {'networks': 20, 'partitions': 8356, 'merged_source_entries': 9352, 'two_pair_entries': 22176, 'collinear_entries': 78800}; elapsed 43.917s; RSS 29065216 bytes.

2026-11-12 22:20:51 Exact obstacles saved: independent positive rank-two correction at two singleton states; and the tempting inequality T_hat <= T + (Kemeny(X)-Kemeny(quotient)) is false already for the supplied four-state family at t=10. These are not Q2 counterexamples.

2026-11-12 22:21:21 Exact optimizer n=8, shape=(3,), improved to 1.999997000005; exact witness saved (evaluation 206).

2026-11-12 22:21:25 Exact optimizer n=8, shape=(3,), improved to 1.99999702000364; exact witness saved (evaluation 409).

2026-11-12 22:21:25 Exact optimizer n=8, shape=(3,), improved to 1.99999702000364; exact witness saved (evaluation 411).

2026-11-12 22:21:25 Exact optimizer n=8, shape=(3,), improved to 1.99999704000314; exact witness saved (evaluation 421).

2026-11-12 22:21:31 Exact optimizer n=8, shape=(3,), improved to 1.99999704000314; exact witness saved (evaluation 798).

2026-11-12 22:21:34 Exact optimizer n=8, shape=(3,), improved to 1.9999972200012; exact witness saved (evaluation 998).

2026-11-12 22:21:43 Exact optimizer n=8, shape=(3,), improved to 1.99999722000174; exact witness saved (evaluation 1596).

2026-11-12 22:21:43 Exact optimizer n=8, shape=(3,), improved to 1.99999722000227; exact witness saved (evaluation 1597).

2026-11-12 22:21:48 Exact optimizer n=8, shape=(3,), improved to 1.99999749410596; exact witness saved (evaluation 2026).

2026-11-12 22:21:48 Exact optimizer n=8, shape=(3,), improved to 1.99999749410596; exact witness saved (evaluation 2027).

2026-11-12 22:21:48 Exact optimizer n=8, shape=(3,), improved to 1.99999751410589; exact witness saved (evaluation 2028).

2026-11-12 22:21:48 Exact optimizer n=8, shape=(3,), improved to 1.99999751411185; exact witness saved (evaluation 2029).

2026-11-12 22:21:48 Exact optimizer n=8, shape=(3,), improved to 1.99999751411185; exact witness saved (evaluation 2030).

2026-11-12 22:21:49 Exact optimizer n=8, shape=(3,), improved to 1.99999752411182; exact witness saved (evaluation 2031).

2026-11-12 22:21:49 Exact optimizer n=8, shape=(3,), improved to 1.99999752411182; exact witness saved (evaluation 2032).

2026-11-12 22:21:49 Exact optimizer n=8, shape=(3,), improved to 1.99999759867529; exact witness saved (evaluation 2047).

2026-11-12 22:21:49 Exact optimizer n=8, shape=(3,), improved to 1.99999764022601; exact witness saved (evaluation 2055).

2026-11-12 22:21:51 Exact optimizer n=8, shape=(3,), improved to 1.99999764026967; exact witness saved (evaluation 2195).

2026-11-12 22:21:51 Exact optimizer n=8, shape=(3,), improved to 1.99999764026967; exact witness saved (evaluation 2196).

2026-11-12 22:21:51 Exact optimizer n=8, shape=(3,), improved to 1.99999770045827; exact witness saved (evaluation 2198).

2026-11-12 22:21:52 Exact optimizer n=8, shape=(3,), improved to 1.99999771997757; exact witness saved (evaluation 2200).

2026-11-12 22:21:52 Exact optimizer n=8, shape=(3,), improved to 1.99999771997757; exact witness saved (evaluation 2201).

2026-11-12 22:21:52 Exact optimizer n=8, shape=(3,), improved to 1.99999772036514; exact witness saved (evaluation 2202).

2026-11-12 22:21:52 Exact optimizer n=8, shape=(3,), improved to 1.99999772036514; exact witness saved (evaluation 2203).

2026-11-12 22:21:52 Exact optimizer n=8, shape=(3,), improved to 1.99999772036514; exact witness saved (evaluation 2206).

2026-11-12 22:21:52 Exact optimizer n=8, shape=(3,), improved to 1.99999775636504; exact witness saved (evaluation 2207).

2026-11-12 22:21:57 Exact optimizer n=8, shape=(3,), improved to 1.99999775636506; exact witness saved (evaluation 2596).

2026-11-12 22:21:57 Exact optimizer n=8, shape=(3,), improved to 1.99999775836505; exact witness saved (evaluation 2597).

2026-11-12 22:21:57 Exact optimizer n=8, shape=(3,), improved to 1.99999775836505; exact witness saved (evaluation 2598).

2026-11-12 22:21:57 Exact optimizer n=8, shape=(3,), improved to 1.99999775836505; exact witness saved (evaluation 2602).

2026-11-12 22:21:57 Exact optimizer n=8, shape=(3,), improved to 1.99999775836505; exact witness saved (evaluation 2603).

2026-11-12 22:21:57 Exact optimizer n=8, shape=(3,), improved to 1.9999977963718; exact witness saved (evaluation 2613).

2026-11-12 22:21:57 Exact optimizer n=8, shape=(3,), improved to 1.9999977963718; exact witness saved (evaluation 2615).

2026-11-12 22:21:57 Exact optimizer n=8, shape=(3,), improved to 1.9999977963718; exact witness saved (evaluation 2618).

2026-11-12 22:22:11 Exact optimizer n=8, shape=(3,), improved to 1.9999977963718; exact witness saved (evaluation 3792).

2026-11-12 22:22:11 Exact optimizer n=8, shape=(3,), improved to 1.9999977963718; exact witness saved (evaluation 3793).

2026-11-12 22:22:11 Exact optimizer n=8, shape=(3,), improved to 1.99999780219934; exact witness saved (evaluation 3798).

2026-11-12 22:22:11 Exact optimizer n=8, shape=(3,), improved to 1.99999787088652; exact witness saved (evaluation 3806).

2026-11-12 22:22:11 Exact optimizer n=8, shape=(3,), improved to 1.99999787088652; exact witness saved (evaluation 3807).

2026-11-12 22:22:11 Exact optimizer n=8, shape=(3,), improved to 1.99999787088652; exact witness saved (evaluation 3808).

2026-11-12 22:22:12 Exact optimizer n=8, shape=(3,), improved to 1.99999787205708; exact witness saved (evaluation 3818).

2026-11-12 22:22:12 Exact optimizer n=8, shape=(3,), improved to 1.99999787205708; exact witness saved (evaluation 3819).

2026-11-12 22:22:18 Exact optimizer n=8, shape=(3,), improved to 1.99999787246252; exact witness saved (evaluation 4390).

2026-11-12 22:22:18 Exact optimizer n=8, shape=(3,), improved to 1.99999787246989; exact witness saved (evaluation 4391).

2026-11-12 22:22:18 Exact optimizer n=8, shape=(3,), improved to 1.99999787247169; exact witness saved (evaluation 4394).

2026-11-12 22:22:18 Exact optimizer n=8, shape=(3,), improved to 1.9999978794446; exact witness saved (evaluation 4399).

2026-11-12 22:22:19 Exact optimizer n=8, shape=(3,), improved to 1.99999788191136; exact witness saved (evaluation 4400).

2026-11-12 22:22:19 Exact optimizer n=8, shape=(3,), improved to 1.99999788478639; exact witness saved (evaluation 4406).

2026-11-12 22:22:22 Exact optimizer n=8, shape=(3,), improved to 1.99999788478639; exact witness saved (evaluation 4589).

2026-11-12 22:22:22 Exact optimizer n=8, shape=(3,), improved to 1.99999788798916; exact witness saved (evaluation 4590).

2026-11-12 22:22:23 Exact optimizer n=8, shape=(3,), improved to 1.99999796003992; exact witness saved (evaluation 4707).

2026-11-12 22:22:23 Exact optimizer n=8, shape=(3,), improved to 1.99999796899555; exact witness saved (evaluation 4709).

2026-11-12 22:22:23 Exact optimizer n=8, shape=(3,), improved to 1.99999796899581; exact witness saved (evaluation 4710).

2026-11-12 22:22:29 Exact optimizer n=8, shape=(3,), improved to 1.99999797244182; exact witness saved (evaluation 5190).

2026-11-12 22:22:30 Exact optimizer n=8, shape=(3,), improved to 1.99999797244184; exact witness saved (evaluation 5193).

2026-11-12 22:22:30 Exact optimizer n=8, shape=(3,), improved to 1.99999798251274; exact witness saved (evaluation 5195).

2026-11-12 22:22:34 Exact optimizer n=8, shape=(3,), improved to 1.99999798251299; exact witness saved (evaluation 5588).

2026-11-12 22:22:34 Exact optimizer n=8, shape=(3,), improved to 1.99999798309237; exact witness saved (evaluation 5601).

2026-11-12 22:22:34 Exact optimizer n=8, shape=(3,), improved to 1.99999799240348; exact witness saved (evaluation 5612).

2026-11-12 22:22:34 Exact optimizer n=8, shape=(3,), improved to 1.99999799290348; exact witness saved (evaluation 5613).

2026-11-12 22:22:35 Exact optimizer n=8, shape=(3,), improved to 1.99999799638556; exact witness saved (evaluation 5650).

2026-11-12 22:22:37 Exact optimizer n=8, shape=(3,), improved to 1.99999799654516; exact witness saved (evaluation 5788).

2026-11-12 22:22:37 Exact optimizer n=8, shape=(3,), improved to 1.99999799668916; exact witness saved (evaluation 5790).

2026-11-12 22:22:37 Exact optimizer n=8, shape=(3,), improved to 1.99999799668916; exact witness saved (evaluation 5793).

2026-11-12 22:22:41 Exact optimizer completed n=8, shape=(3,), best 1.99999799668916, 5976 cumulative exact evaluations.

2026-11-12 22:22:42 Exact optimizer n=8, shape=(2, 2), improved to 2.999992000019; exact witness saved (evaluation 6179).

2026-11-12 22:22:42 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000005; exact witness saved (evaluation 6181).

2026-11-12 22:22:42 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000005; exact witness saved (evaluation 6182).

2026-11-12 22:22:45 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000005; exact witness saved (evaluation 6371).

2026-11-12 22:22:48 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000737; exact witness saved (evaluation 6781).

2026-11-12 22:22:49 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000737; exact witness saved (evaluation 6934).

2026-11-12 22:22:59 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000737; exact witness saved (evaluation 7890).

2026-11-12 22:22:59 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000737; exact witness saved (evaluation 7891).

2026-11-12 22:22:59 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000737; exact witness saved (evaluation 7892).

2026-11-12 22:22:59 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000769; exact witness saved (evaluation 7897).

2026-11-12 22:22:59 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000769; exact witness saved (evaluation 7899).

2026-11-12 22:23:02 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000769; exact witness saved (evaluation 8070).

2026-11-12 22:23:02 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000769; exact witness saved (evaluation 8071).

2026-11-12 22:23:02 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000769; exact witness saved (evaluation 8075).

2026-11-12 22:23:05 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000769; exact witness saved (evaluation 8451).

2026-11-12 22:23:08 Exact optimizer n=8, shape=(2, 2), improved to 2.9999950000077; exact witness saved (evaluation 8637).

2026-11-12 22:23:08 Exact optimizer n=8, shape=(2, 2), improved to 2.9999950000077; exact witness saved (evaluation 8639).

2026-11-12 22:23:08 Exact optimizer n=8, shape=(2, 2), improved to 2.9999950000077; exact witness saved (evaluation 8641).

2026-11-12 22:23:08 Exact optimizer n=8, shape=(2, 2), improved to 2.9999950000077; exact witness saved (evaluation 8642).

2026-11-12 22:23:12 Exact optimizer n=8, shape=(2, 2), improved to 2.9999950000077; exact witness saved (evaluation 9014).

2026-11-12 22:23:12 Exact optimizer n=8, shape=(2, 2), improved to 2.9999950000077; exact witness saved (evaluation 9017).

2026-11-12 22:23:12 Exact optimizer n=8, shape=(2, 2), improved to 2.9999950000077; exact witness saved (evaluation 9018).

2026-11-12 22:23:12 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000785; exact witness saved (evaluation 9069).

2026-11-12 22:23:12 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000792; exact witness saved (evaluation 9078).

2026-11-12 22:23:12 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000792; exact witness saved (evaluation 9079).

2026-11-12 22:23:12 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000792; exact witness saved (evaluation 9080).

2026-11-12 22:23:12 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000792; exact witness saved (evaluation 9083).

2026-11-12 22:23:12 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000792; exact witness saved (evaluation 9084).

2026-11-12 22:23:13 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000799; exact witness saved (evaluation 9150).

2026-11-12 22:23:13 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000799; exact witness saved (evaluation 9152).

2026-11-12 22:23:13 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000799; exact witness saved (evaluation 9153).

2026-11-12 22:23:13 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000799; exact witness saved (evaluation 9164).

2026-11-12 22:23:13 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000799; exact witness saved (evaluation 9165).

2026-11-12 22:23:13 Exact optimizer n=8, shape=(2, 2), improved to 2.99999500000799; exact witness saved (evaluation 9166).

2026-11-12 22:23:13 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9172).

2026-11-12 22:23:14 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9173).

2026-11-12 22:23:14 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9182).

2026-11-12 22:23:14 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9183).

2026-11-12 22:23:14 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9184).

2026-11-12 22:23:14 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9185).

2026-11-12 22:23:14 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9186).

2026-11-12 22:23:14 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9203).

2026-11-12 22:23:14 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9230).

2026-11-12 22:23:14 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9231).

2026-11-12 22:23:14 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9232).

2026-11-12 22:23:14 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9233).

2026-11-12 22:23:14 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9239).

2026-11-12 22:23:14 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9245).

2026-11-12 22:23:14 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9247).

2026-11-12 22:23:15 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9255).

2026-11-12 22:23:15 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9266).

2026-11-12 22:23:15 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9324).

2026-11-12 22:23:15 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9325).

2026-11-12 22:23:15 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9329).

2026-11-12 22:23:16 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9334).

2026-11-12 22:23:16 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9338).

2026-11-12 22:23:16 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9339).

2026-11-12 22:23:16 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9350).

2026-11-12 22:23:16 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9351).

2026-11-12 22:23:16 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9355).

2026-11-12 22:23:16 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9357).

2026-11-12 22:23:16 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9359).

2026-11-12 22:23:16 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9363).

2026-11-12 22:23:18 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9582).

2026-11-12 22:23:18 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9630).

2026-11-12 22:23:18 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9639).

2026-11-12 22:23:19 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9654).

2026-11-12 22:23:19 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9671).

2026-11-12 22:23:19 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9673).

2026-11-12 22:23:19 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9678).

2026-11-12 22:23:19 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9679).

2026-11-12 22:23:19 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9680).

2026-11-12 22:23:19 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9681).

2026-11-12 22:23:19 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9682).

2026-11-12 22:23:19 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9683).

2026-11-12 22:23:19 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9690).

2026-11-12 22:23:20 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9767).

2026-11-12 22:23:20 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9778).

2026-11-12 22:23:20 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9782).

2026-11-12 22:23:20 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9786).

2026-11-12 22:23:20 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9787).

2026-11-12 22:23:20 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9788).

2026-11-12 22:23:20 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 9789).

2026-11-12 22:23:24 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 10149).

2026-11-12 22:23:24 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 10151).

2026-11-12 22:23:31 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 10728).

2026-11-12 22:23:38 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11300).

2026-11-12 22:23:38 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11302).

2026-11-12 22:23:41 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11484).

2026-11-12 22:23:41 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11487).

2026-11-12 22:23:41 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11489).

2026-11-12 22:23:41 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11490).

2026-11-12 22:23:45 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11869).

2026-11-12 22:23:46 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11872).

2026-11-12 22:23:46 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11875).

2026-11-12 22:23:46 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11876).

2026-11-12 22:23:46 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11880).

2026-11-12 22:23:46 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11882).

2026-11-12 22:23:46 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11885).

2026-11-12 22:23:46 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11887).

2026-11-12 22:23:46 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11893).

2026-11-12 22:23:46 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11894).

2026-11-12 22:23:46 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11896).

2026-11-12 22:23:47 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11954).

2026-11-12 22:23:47 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 11961).

2026-11-12 22:23:48 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12055).

2026-11-12 22:23:48 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12056).

2026-11-12 22:23:52 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12449).

2026-11-12 22:23:52 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12450).

2026-11-12 22:23:52 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12452).

2026-11-12 22:23:52 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12455).

2026-11-12 22:23:55 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12639).

2026-11-12 22:23:55 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12650).

2026-11-12 22:23:55 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12654).

2026-11-12 22:23:55 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12655).

2026-11-12 22:23:56 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12794).

2026-11-12 22:23:56 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12795).

2026-11-12 22:23:56 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12796).

2026-11-12 22:23:57 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12799).

2026-11-12 22:23:57 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12816).

2026-11-12 22:23:57 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12817).

2026-11-12 22:23:57 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12818).

2026-11-12 22:23:57 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 12819).

2026-11-12 22:23:58 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13024).

2026-11-12 22:23:58 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13025).

2026-11-12 22:23:58 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13028).

2026-11-12 22:23:58 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13030).

2026-11-12 22:23:58 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13036).

2026-11-12 22:23:59 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13066).

2026-11-12 22:23:59 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13067).

2026-11-12 22:23:59 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13069).

2026-11-12 22:23:59 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13075).

2026-11-12 22:23:59 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13079).

2026-11-12 22:24:01 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13209).

2026-11-12 22:24:01 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13211).

2026-11-12 22:24:01 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13212).

2026-11-12 22:24:01 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13214).

2026-11-12 22:24:01 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13216).

2026-11-12 22:24:04 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13623).

2026-11-12 22:24:05 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13625).

2026-11-12 22:24:07 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13783).

2026-11-12 22:24:07 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13784).

2026-11-12 22:24:07 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13785).

2026-11-12 22:24:07 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13786).

2026-11-12 22:24:07 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13791).

2026-11-12 22:24:07 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13793).

2026-11-12 22:24:07 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13800).

2026-11-12 22:24:07 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13806).

2026-11-12 22:24:08 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13915).

2026-11-12 22:24:08 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13917).

2026-11-12 22:24:08 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13924).

2026-11-12 22:24:09 Exact optimizer n=8, shape=(2, 2), improved to 2.999995000008; exact witness saved (evaluation 13927).

2026-11-12 22:24:09 Exact optimizer completed n=8, shape=(2, 2), best 2.999995000008, 13931 cumulative exact evaluations.

2026-11-12 22:24:09 Exact optimization n=8, seed=22118: 13931 exact objectives, 9407 accepted proposals, 170.012s, peak RSS 28639232 bytes.

2026-11-12 22:26:28 Final report validation PASSED: every best matrix and time independently recomputed; all exact ratio formulas, partition counts, run totals, partial-proof counts and report links verified. Runtime 0.036s; RSS 30228480 bytes. REPORT.md result is partial; Q2 and K(7)=3 remain unproved.
