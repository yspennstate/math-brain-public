# FEI loop - STATE (agent an agent, 10-20 Nov 2026)

ADDED 12 Nov 04:30 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): dg_5 (m 20, 9608 classes, last line BEST) -0.480653478; k33cx1 (m 19, 8960 classes, last line BEST) +0.000000000; 
Read at write time. 06:30 Mac mini 2 clock: ncpu=12 load=13.65 free_cores=-1 avail=9067MB pressure=1; mine queued 263 running sy_ap_9c sy_ec_k2x4 sy_gv_dodec sy_sub_7_2 cq_gs5_304 cq_gs6_305 cq_gs6_306 cq_gs6_307 ; flagged files 0

ADDED 12 Nov 04:26 laptop clock (newest block; the NEXT line in the 07:46 block stands):

## 12 Nov 04:31 laptop: correction - ap_9c does contain the record (its group is an index-2 subgroup of the k33c group)

- The 04:23 block called ap_9c "a structure that does not contain the record". That is wrong. Writing GF(9) = F_3[i], the 9 points are the 9 cells of the 3 x 3 grid (the edges of K_{3,3}); translations permute rows and columns, and multiplication by i sends (x, y) to (-y, x), a swap of the two sides with a sign. So the ap_9c group (order 36) lies inside the k33c group (order 72), and every k33c function, the record included, is an ap_9c function.
- Checked by machine (code/ap9_in_k33.py, run on Mac mini 2): closure orders 36, 72 and 36 (k33cs); of the 40320 relabellings of the points fixing point 0, 16 carry the ap_9c generators into the k33c group, the identity labelling among them; none of the 16 carries them into the k33cs group (S_3 x S_3). So ap_9c is a second index-2 subgroup, a space around the record different from the k33cs one, which ended at slack exactly 0.
- Reading of the -0.049953176 line: a random start in a space that holds the record climbed to within 0.05 of the record's level. It says the anneal works there; it is not a sign of a new function. What matters is whether any later run passes 0. No further run line yet at 06:24 Mac mini 2 clock; the other four files are unchanged (gv_dodec -0.276516984, dg_5 -0.480653478, ec_k2x4 -0.208315180, sub_7_2 -1.480246822).
- The ap_9c job has no graph seeds (struct returns no edge list for it), so it does not start from the record. A seeded run of this space needs the record written in the GF(9) labelling; that is the useful follow-up, not more random seeds.
- Record lower bound unchanged: 6.521845710923. Conjecture open.

NEXT: (1) read sy_ap_9c, sy_gv_dodec, sy_dg_5, sy_sub_7_2, sy_ec_k2x4 and the eleven small ones as they end; (2) ap_9c from the record: give struct("ap_9c") the K_{3,3} edge list in the identity labelling (checked above) so the k33c seeds apply, test that the seeded start reproduces slack 0, then queue single flips and pairs from the record in this space, as was done for k33cs; (3) when sy_gv_dodec and sy_dg_5 have ended and 9000 MB is available: mv ~/fei_agent/parked/30_agent_sy_k33cx2.job ~/fillq/queue/24_agent_sy_k33cx2.job; (4) read cq_gs23*, cq_gs5*, cq_gs6*, the remaining library starts on Mac mini 1 as they end; a line above 0 is rebuilt from the explicit truth table before a word is said; (5) new families in struct() (Heawood edges = the 21 flags of the Fano plane; Petersen vertices with coins; arcs and vertices of K_4), under 10,000 classes; the fixed names not covered by missing_names.py (pet, q3e, octa, the small graphs with coins, k3c5, k4c2, agl/pgl) are checked against the result files first; (6) loop job 49a7ba01 expires about 17 Nov 21:4x: re-create it.

ADDED 12 Nov 04:22 laptop clock (newest block; the NEXT line in the 07:46 block stands):

## 12 Nov 04:23 laptop: first run lines of the five searches on Mac mini 2; ap_9c is at -0.05 from a random start

- 06:22 Mac mini 2 clock, all still running, best line so far in each file (each with its explicit rebuild equal):
  - sy_ap_9c (7584 classes): run 0, random start, slack -0.049953176, G 6.841525890, J 2.056680343, p' 0.502197266.
  - sy_ec_k2x4 (1996): run 1, pm+coins start, slack -0.208315180, G 5.785835125, J 1.956615224.
  - sy_gv_dodec (9436): run 0, random start, slack -0.276516984, G 10.550277698, J 2.660274925.
  - sy_dg_5 (9608): run 2, random start, slack -0.480653478, G 10.425657778, J 2.672307883.
  - sy_sub_7_2 (1044): run 3, random start, slack -1.480246822.
- None above 0. ap_9c is the nearest any random start has come on a structure that does not contain the record (the others near 0 were seeded: k33cx1 0, library start 21 at 0, library start 5 at -0.023); its later runs are the ones to read.
- k33cx2 still parked: 8289 MB available and the two large jobs running (the gate wants 9000 MB and both ended).
- Mac mini 1 at 06:20 its clock: load 22 on 10 cores, 73 of mine queued and none running (other work holds the cores), 176 done, 0 failed.

NEXT: (1) read sy_ap_9c first, then sy_gv_dodec, sy_dg_5, sy_sub_7_2, sy_ec_k2x4 and the eleven small ones as they end; if ap_9c ends within 0.05 of 0, queue it again with other seeds and a longer run, and queue its relatives (ap_9c with --pairs, ap_7c and ap_13 again with new seeds); (2) when sy_gv_dodec and sy_dg_5 have ended and 9000 MB is available: mv ~/fei_agent/parked/30_agent_sy_k33cx2.job ~/fillq/queue/24_agent_sy_k33cx2.job; (3) read cq_gs23*, cq_gs5*, cq_gs6*, the remaining library starts on Mac mini 1 as they end; a line above 0 is rebuilt from the explicit truth table before a word is said; (4) new families in struct() (Heawood edges = the 21 flags of the Fano plane; Petersen vertices with coins; arcs and vertices of K_4), each tested against a brute-force group, under 10,000 classes; (5) loop job 49a7ba01 expires about 17 Nov 21:4x: re-create it.

ADDED 12 Nov 04:14 laptop clock (newest block; the NEXT line in the 07:46 block stands):

## 12 Nov 04:16 laptop: the 04:10 block overstated the coverage; full list of unsearched structures, eleven more queued, k33cx2 parked

- Correction to the 04:10 block: "every other structure the script can name on 16 to 21 inputs already has a result" rested on thirteen names checked by hand. The full enumeration (code/missing_names.py: 443 names over wr_, wn_, pr_, ev_, ec_, eh_, sub_, dg_, g3_, the field families and the fixed names, each tested against the result files in ~/fei_agent) finds 348 names with 16 to 21 inputs and no result file.
- 319 of the 348 are pr_ block structures with unequal blocks (45 to about 1,300 classes each). The sixteen pr_ structures that were run all ended far below 0 (pr_3_6_9 -1.260922855, pr_5_5_5_5 -2.381239217, pr_6_6_6 -2.529825610, pr_9_9 -3.996722769), so these are not queued one by one.
- Of the other 29: ec_k3x3 and ec_k5 are k33c and k5c under another name (both run); psl_8c, psl_16, ap_8c, ap_16 are pl_8c, pl_16, al_8c, al_16 (the groups coincide in characteristic 2; all run); plf_7c, pl_17, plf_17, al_17, alf_17, pl_19, plf_19, al_19, alf_19 are groups containing one already searched (pl_7c, psl_17, ap_17, psl_19, ap_19), so their functions lay inside those searches; ap_9c, sub_7_2, ec_k2x4 were queued at 04:10 (ap_9c and ec_k2x4 are running, 945 MB and 104 MB resident).
- Queued 06:14:02 Mac mini 2 clock at 8287 MB available, 84 pct free, load 12.6: 26_agent_sy_<name>.job for wr_8_2 (45 classes), wr_9_2 (55), wr_10_2 (66), wr_3_7 (120), wr_7_3 (120), eh_k2x7 (260), eh_k2x8 (355), eh_k2x9 (470), eh_k3x6 (2676), eh_k7x2 (1870), s8c (165); 1500 s each, seeds 71 to 91, mem_mb 400 to 900. 266 of mine queued.
- k33cx2 (20 inputs, 13440 classes: the structure of the record with two further inputs; k33cx1 with one further input ended at slack exactly 0): matrices 2756 MB. Measured on the running jobs, resident memory is about 1.1 times the two matrices (gv_dodec 1489 MB for 1358 MB of matrices, dg_5 1510 MB for 1408 MB), so about 3.1 GB. Written as ~/fei_agent/parked/30_agent_sy_k33cx2.job (mem_mb 4800, 5400 s, seed 97, batch 32), not queued: it moves to the queue when 9000 MB is available and sy_gv_dodec and sy_dg_5 have ended (scratchpad unpark_k33cx2.sh does the check and the move).
- Record lower bound unchanged: 6.521845710923. Conjecture open.

NEXT: (1) read sy_gv_dodec, sy_dg_5, sy_ap_9c, sy_sub_7_2, sy_ec_k2x4 and the eleven small ones as they end; (2) when sy_gv_dodec and sy_dg_5 have ended and 9000 MB is available: mv ~/fei_agent/parked/30_agent_sy_k33cx2.job ~/fillq/queue/24_agent_sy_k33cx2.job; (3) read cq_gs23*, cq_gs5*, the remaining library starts on Mac mini 1 as they end; a line above 0 is rebuilt from the explicit truth table before a word is said; (4) new families in struct() (edges of a named graph under its automorphisms: Heawood edges are the 21 flags of the Fano plane; Petersen vertices with coins; arcs and vertices of K_4), each tested against a brute-force group, under 10,000 classes; (5) loop job 49a7ba01 expires about 17 Nov 21:4x: re-create it.

ADDED 12 Nov 04:09 laptop clock (newest block; the NEXT line in the 07:46 block stands):

## 12 Nov 04:10 laptop: three structures not searched before queued on Mac mini 2 (ap_9c, sub_7_2, ec_k2x4)

- Read against the result files in ~/fei_agent: every other structure the script can name on 16 to 21 inputs already has a result (ap_17 best -0.705515042, ap_13 -0.660509954, psl_7c -2.042285583, psl_13 -2.628191135, psl_5c -0.491254730, m11c -3.376198938; the pl_, al_ groups contain the psl_, ap_ groups, so their functions were already inside those searches). Three had no file.
- Class counts, by the script's orbit pass and by Burnside over the closure of the generators (code/cls_count.py, both agree, class sizes sum to 2^m):
  - ap_9c: 18 inputs (GF(9) and one coin per point), group of order 36, 7584 classes, two matrices 877 MB.
  - sub_7_2: 21 inputs (the edges of K_7 under S_7), order 5040, 1044 classes (the number of graphs on 7 vertices), 16 MB.
  - ec_k2x4: 16 inputs (the edges of K_{2,4} and one coin per edge), order 48, 1996 classes, 60 MB.
- Queued 06:08:45 Mac mini 2 clock at 10002 MB available, 84 pct free, load 12.9 on 12 cores: 24_agent_sy_ap_9c.job (mem_mb 1600, 3000 s, seed 53, batch 16), 24_agent_sy_sub_7_2.job (mem_mb 900, 3000 s, seed 59, batch 16), 24_agent_sy_ec_k2x4.job (mem_mb 400, 1500 s, seed 67, batch 64). 258 of mine queued.
- Running: sy_gv_dodec (9436 classes, setup 287 s) and sy_dg_5 (9608 classes, setup 298 s), no result line yet; cq_gs5_302, cq_gs5_303.
- Memory rule for the next groups: the two class matrices take 2 K^2 8 bytes (K classes), and the declared peak has been about 1.7 times that; 10,000 classes is about 2.6 GB declared, 20,000 would be about 10 GB and does not fit, so new groups stay under about 10,000 classes.
- Record lower bound unchanged: 6.521845710923. Conjecture open.

NEXT: (1) read sy_gv_dodec, sy_dg_5, sy_ap_9c, sy_sub_7_2, sy_ec_k2x4 as they end; (2) read cq_gs23*, cq_gs5*, the remaining library starts on Mac mini 1 as they end; a line above 0 is rebuilt from the explicit truth table before a word is said; (3) the script's named structures on 16 to 21 inputs are now used up: add new families to struct() (edges of a named graph under its automorphisms: Heawood edges are the 21 flags of the Fano plane, order 336; Petersen vertices with coins, 20 inputs, order 120; arcs and vertices of K_4, 16 inputs), test each with a brute-force group as in test_grp3.py, keep under 10,000 classes, then queue; (4) loop job 49a7ba01 expires about 17 Nov 21:4x: re-create it.

ADDED 12 Nov 04:02 laptop clock (newest block; the NEXT line in the 07:46 block stands):

## 12 Nov 04:02 laptop: sy_gv_dodec running, sy_dg_5 queued; nothing parked any more

- 06:01 Mac mini 2 clock: sy_gv_dodec is running with cq_gs5_301..303; avail 11611 MB by the tick's own figure (the H3 film work is off this machine since his 03:51 order), load 13 on 12 cores, 256 of mine queued.
- 06:01:52: parked/30_agent_sy_dg_5.job moved to ~/fillq/queue/24_agent_sy_dg_5.job (peak 1761 MB) at avail 11518 MB, 84 pct free; with sy_gv_dodec at its 2300 MB peak that leaves about 7 GB.

NEXT: (1) read sy_gv_dodec and sy_dg_5 as they run and end; (2) read cq_gs23*, cq_gs5*, the remaining 60 library starts on Mac mini 1 as they end; a line above 0 is rebuilt from the explicit truth table before a word is said; (3) Mac mini 2 now has about 11 GB free: prepare further groups on 16 to 20 inputs with under 20,000 classes and queue them; (4) loop job 49a7ba01 expires about 17 Nov 21:4x: re-create it.

ADDED 12 Nov 03:59 laptop clock (newest block; the NEXT line in the 07:46 block stands):

## 12 Nov 03:59 laptop: sy_gv_dodec moved into the Mac mini 2 queue

- 05:59:30 Mac mini 2 clock: parked/30_agent_sy_gv_dodec.job moved to ~/fillq/queue/24_agent_sy_gv_dodec.job (peak 2300 MB). Reading at the move: memory_pressure 84 pct free, free+inactive+purgeable 11185 MB, load 12.44 on 12 cores. The tick's stricter avail figure read 3568 MB a few seconds earlier; the job's peak is under both. sy_k33cx1 had ended, so its memory is back.
- The tick's result line for k33cx1: classes 8960, m 19, best +0.000000000, kind BEST, flags 0.
- sy_dg_5 (1761 MB) stays parked until sy_gv_dodec has ended.

NEXT: (1) read sy_gv_dodec as it runs and ends; then mv ~/fei_agent/parked/30_agent_sy_dg_5.job ~/fillq/queue/24_agent_sy_dg_5.job; (2) read cq_gs23*, cq_gs5*, the remaining 60 library starts on Mac mini 1 as they end; a line above 0 is rebuilt from the explicit truth table before a word is said; (3) further groups on 16 to 20 inputs with under 20,000 classes; (4) loop job 49a7ba01 expires about 17 Nov 21:4x: re-create it.

ADDED 12 Nov 03:57 laptop clock (newest block; the NEXT line in the 07:46 block stands):

## 12 Nov 03:57 laptop: sy_k33cx1 ended on Mac mini 2, best slack exactly 0, nothing above

- sy_k33cx1 (8960 sign classes): BEST of 28 runs slack +0.000000000, G 6.776605309, J 2.039062500, p' 0.500000000; the explicit rebuild gives the same three numbers. Earlier runs of the same job sat at -0.483245065 (run 7) and -1.264402025 (run 20). A slack of 0 is the boundary case, not a gain: no line above 0, so nothing to rebuild from a truth table and no claim.
- Mac mini 1 library starts: 110 done, 60 queued, 0 failed; best three unchanged (0 lib 21, -0.023143487707 lib 5, -0.066370796906 lib 81); none above 0.
- Mac mini 2 at 05:56 its clock: load 17 to 21 on 12 cores, avail 3921 to 4807 MB, 256 of mine queued, cq_gs23_318..320 and cq_gs5_301..303 running. The parked sy_gv_dodec (2300 MB) and sy_dg_5 (1761 MB) stay parked until avail is above 5000 MB.
- Record lower bound unchanged: 6.521845710923. Conjecture open.

NEXT: (1) when avail on Mac mini 2 is above 5000 MB: mv ~/fei_agent/parked/30_agent_sy_gv_dodec.job ~/fillq/queue/24_agent_sy_gv_dodec.job, then sy_dg_5 the same way after it ends; (2) read cq_gs23*, cq_gs5*, the remaining 60 library starts on Mac mini 1 as they end; a line above 0 is rebuilt from the explicit truth table before a word is said; (3) further groups on 16 to 20 inputs with under 20,000 classes; (4) loop job 49a7ba01 expires about 17 Nov 21:4x: re-create it.

ADDED 12 Nov 02:43 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): wr_6_3 (m 18, 84 classes, last line BEST) -2.886121946; 
Read at write time. 04:43 Mac mini 2 clock: ncpu=12 load=13.12 free_cores=-1 avail=4515MB pressure=1; mine queued 262 running sy_k33cx1 cq_gs19_313 cq_gs19_314 cq_gs19_315 cq_gs19_316 cq_gs23_317 ; flagged files 0

ADDED 12 Nov 02:39 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): wr_5_3 (m 15, 56 classes, last line BEST) -2.211205751; wr_5_4 (m 20, 126 classes, last line BEST) -2.247040593; 
Read at write time. 04:39 Mac mini 2 clock: ncpu=12 load=13.77 free_cores=0 avail=4885MB pressure=1; mine queued 264 running sy_k33cx1 sy_wr_6_3 cq_gs19_313 cq_gs19_314 cq_gs19_315 ; flagged files 0

ADDED 12 Nov 02:34 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): wr_4_4 (m 16, 70 classes, last line BEST) -1.366981042; wr_4_5 (m 20, 126 classes, last line BEST) -1.407709855; 
Read at write time. 04:34 Mac mini 2 clock: ncpu=12 load=13.60 free_cores=0 avail=4035MB pressure=1; mine queued 264 running sy_k33cx1 sy_wr_5_3 sy_wr_5_4 sy_wr_6_3 cq_gs19_313 cq_gs19_314 cq_gs19_315 ; flagged files 0

ADDED 12 Nov 02:32 laptop clock (newest block; the NEXT line in the 07:46 block stands):
sy_k33cx1 started on Mac mini 2 between 04:14 and 04:27 its clock (02:14 to 02:27 laptop clock) after the rename to
24_agent_sy_k33cx1.job; it runs 5400 s (--seed 11 --batch 32) and writes sy_k33cx1.txt; first lines so far are flip2
pair scans far below 0 (best pair among 150: -7.68228), no BEST line yet.
Still parked (one at a time, avail above 5000 MB, low prefix so it is the queue head): 30_agent_sy_gv_dodec.job (2300),
then 30_agent_sy_dg_5.job (1761). Mac mini 2 at 04:32 its clock: avail 3753 to 4792 MB, load 13 to 16.
Mac mini 1 at 04:32 its clock: load 18.77, avail 10126 MB; mine queued 73, running 3, done 173, failed 0; library starts
done 110, queued 60 (the n 14 to 16 ones, none begun), none above 0, best three unchanged (0 lib 21, -0.023143487707 lib 5,
-0.066370796906 lib 81).

ADDED 12 Nov 02:31 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): wr_3_6 (m 18, 84 classes, last line BEST) -0.740816898; wr_4_3 (m 12, 35 classes, last line BEST) -1.325180869; 
Read at write time. 04:31 Mac mini 2 clock: ncpu=12 load=13.37 free_cores=1 avail=3856MB pressure=1; mine queued 264 running sy_k33cx1 sy_wr_4_4 sy_wr_4_5 sy_wr_5_3 sy_wr_5_4 sy_wr_6_3 cq_gs19_313 cq_gs19_314 cq_gs19_315 ; flagged files 0

ADDED 12 Nov 02:28 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): wr_2_9 (m 18, 55 classes, last line BEST) -1.306611693; wr_3_4 (m 12, 35 classes, last line BEST) -0.665201147; wr_3_5 (m 15, 56 classes, last line BEST) -0.693178861; 
Read at write time. 04:28 Mac mini 2 clock: ncpu=12 load=15.68 free_cores=-1 avail=3870MB pressure=1; mine queued 264 running sy_k33cx1 sy_wr_3_6 sy_wr_4_3 sy_wr_4_4 sy_wr_4_5 sy_wr_5_3 sy_wr_5_4 sy_wr_6_3 cq_gs19_313 cq_gs19_314 cq_gs19_315 ; flagged files 0

ADDED 12 Nov 02:21 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): wr_2_10 (m 20, 66 classes, last line BEST) -1.663370505; wr_2_7 (m 14, 36 classes, last line BEST) -0.713489509; wr_2_8 (m 16, 45 classes, last line BEST) -0.988873386; 
Read at write time. 04:22 Mac mini 2 clock: ncpu=12 load=16.87 free_cores=-1 avail=4143MB pressure=1; mine queued 266 running sy_wr_2_9 sy_wr_3_4 sy_wr_3_5 sy_wr_3_6 sy_wr_4_3 sy_wr_4_4 sy_wr_4_5 sy_wr_5_3 sy_wr_5_4 sy_wr_6_3 cq_gs19_313 cq_gs19_314 ; flagged files 0

ADDED 12 Nov 02:14 laptop clock (newest block; the NEXT line in the 07:46 block stands):
The parked job released at 01:40 had not started by 02:14 laptop clock: the runner admits it only with avail at or above 4800 MB
(mem_mb 2400) and avail stayed at 4100 to 4600 MB while smaller jobs went past it. It was renamed in the Mac mini 2 queue to
24_agent_sy_k33cx1.job so that it is the head of the queue. The queue aging helper ~/fillq/aging.sh (an agent's; it had
not come back after the Mac mini 2 restart of 11 Nov, uptime 9 h 24 min at the read) was started again at 04:14 its clock, pid 96818
in ~/fillq/aging.pid, stop file ~/fillq/STOP_AGING: after 30 min with the same head it holds the other queued jobs in
~/fillq/queue_hold until the head starts or 45 min pass, then puts them back. My 12 running searches hold 844 MB together.
Structure search that has ended on Mac mini 2: wn_5_2_2 (m 20, 231 classes, last line BEST) -2.247040593.
wn_3_2_3 (220 classes) and wn_3_3_2 (210 classes) end at the same value -0.740816898.

ADDED 12 Nov 02:10 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): wn_3_2_3 (m 18, 220 classes, last line BEST) -0.740816898; wn_3_3_2 (m 18, 210 classes, last line BEST) -0.740816898; wn_4_2_2 (m 16, 120 classes, last line BEST) -1.366981042; 
Read at write time. 04:10 Mac mini 2 clock: ncpu=12 load=13.66 free_cores=-1 avail=4185MB pressure=1; mine queued 271 running sy_wn_5_2_2 sy_wr_2_10 sy_wr_2_7 sy_wr_2_8 sy_wr_2_9 sy_wr_3_4 sy_wr_3_5 sy_wr_3_6 sy_wr_4_3 sy_wr_4_4 sy_wr_4_5 ; flagged files 0

ADDED 12 Nov 02:03 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): wn_2_5_2 (m 20, 231 classes, last line BEST) -0.371599232; wn_3_2_2 (m 12, 55 classes, last line BEST) -0.665201147; 
Read at write time. 04:03 Mac mini 2 clock: ncpu=12 load=12.40 free_cores=0 avail=3019MB pressure=1; mine queued 275 running sy_wn_3_2_3 sy_wn_3_3_2 sy_wn_4_2_2 sy_wn_5_2_2 sy_wr_2_10 sy_wr_2_7 sy_wr_2_8 sy_wr_2_9 sy_wr_3_4 sy_wr_3_5 ; flagged files 0

ADDED 12 Nov 02:00 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): wn_2_3_3 (m 18, 220 classes, last line BEST) -0.469283994; wn_2_4_2 (m 16, 120 classes, last line BEST) -0.245967089; wr_3_3 (m 9, 20 classes, last line exh) -0.618552686; 
Read at write time. 04:00 Mac mini 2 clock: ncpu=12 load=13.54 free_cores=0 avail=3882MB pressure=1; mine queued 276 running sy_wn_2_5_2 sy_wn_3_2_2 sy_wn_3_2_3 sy_wn_3_3_2 sy_wn_4_2_2 sy_wn_5_2_2 sy_wr_2_10 sy_wr_2_7 sy_wr_2_8 sy_wr_2_9 sy_wr_3_4 ; flagged files 0

ADDED 12 Nov 01:57 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): wn_2_2_5 (m 20, 252 classes, last line BEST) -1.407709855; wn_2_3_2 (m 12, 55 classes, last line BEST) -0.224587389; 
Read at write time. 03:57 Mac mini 2 clock: ncpu=12 load=15.00 free_cores=0 avail=4159MB pressure=1; mine queued 279 running sy_wn_2_4_2 sy_wn_2_5_2 sy_wn_3_2_2 sy_wn_3_2_3 sy_wn_3_3_2 sy_wn_4_2_2 sy_wn_5_2_2 sy_wr_2_10 sy_wr_2_7 sy_wr_2_8 ; flagged files 0

ADDED 12 Nov 01:54 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): ev_k6 (m 21, 5096 classes, last line BEST) -0.534546704; ev_octa (m 18, 6456 classes, last line BEST) -0.160154561; wr_2_6 (m 12, 28 classes, last line exh) -0.491254730; 
Read at write time. 03:54 Mac mini 2 clock: ncpu=12 load=14.47 free_cores=1 avail=4773MB pressure=1; mine queued 280 running sy_wn_2_2_5 sy_wn_2_3_2 sy_wn_2_3_3 sy_wn_2_4_2 sy_wn_2_5_2 sy_wn_3_2_2 sy_wn_3_2_3 sy_wn_3_3_2 sy_wn_4_2_2 sy_wn_5_2_2 sy_wr_2_10 sy_wr_2_7 ; flagged files 0

ADDED 12 Nov 01:45 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): ev_k4 (m 10, 90 classes, last line BEST) -0.159675860; ev_k5 (m 15, 544 classes, last line BEST) -0.430803580; 
Read at write time. 03:45 Mac mini 2 clock: ncpu=12 load=15.58 free_cores=0 avail=4251MB pressure=1; mine queued 284 running sy_ev_k6 sy_ev_octa sy_wn_2_2_5 sy_wn_2_3_2 sy_wn_2_3_3 sy_wn_2_4_2 sy_wn_2_5_2 sy_wn_3_2_2 sy_wn_3_2_3 sy_wn_3_3_2 sy_wn_4_2_2 ; flagged files 0

ADDED 12 Nov 01:40 laptop clock (newest block; the NEXT line in the 07:46 block stands):
Parked job moved into the Mac mini 2 queue at 01:40 laptop clock (status line 03:39 its clock: avail 5597 MB, load 12.52):
30_agent_sy_k33cx1.job (mem_mb 2400; sym_search.py k33cx1 W_cur.txt sy_k33cx1.txt --secs 5400 --seed 11 --batch 32).
Still parked, one at a time when avail is above 5000 MB: 30_agent_sy_gv_dodec.job (2300), 30_agent_sy_dg_5.job (1761).
Structure search that has ended on Mac mini 2: ev_k3x4 (m 19, 6170 classes, last line BEST) -0.604970091.
The ev_k2x<b> line so far: ev_k2x2 -0.135432834, ev_k2x3 -0.060092993, ev_k2x4 -0.173096831, ev_k2x5 -0.236734873,
ev_k2x6 -0.586459106; ev_k2x3 sits next to eh_k3x3 -0.056051752 among the nearest neighbours of the record structure.

ADDED 12 Nov 01:36 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): ev_k2x5 (m 17, 1692 classes, last line BEST) -0.236734873; ev_k2x6 (m 20, 3620 classes, last line BEST) -0.586459106; 
Read at write time. 03:36 Mac mini 2 clock: ncpu=12 load=12.44 free_cores=0 avail=3039MB pressure=1; mine queued 287 running sy_ev_k3x4 sy_ev_k4 sy_ev_k5 sy_ev_k6 sy_ev_octa sy_wn_2_2_5 sy_wn_2_3_2 sy_wn_2_3_3 sy_wn_2_4_2 sy_wn_2_5_2 ; flagged files 0

ADDED 12 Nov 01:33 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): ev_k2x3 (m 11, 268 classes, last line BEST) -0.060092993; ev_k2x4 (m 14, 718 classes, last line BEST) -0.173096831; 
Read at write time. 03:33 Mac mini 2 clock: ncpu=12 load=11.72 free_cores=0 avail=3943MB pressure=1; mine queued 289 running sy_ev_k2x5 sy_ev_k2x6 sy_ev_k3x4 sy_ev_k4 sy_ev_k5 sy_ev_k6 sy_ev_octa sy_wn_2_2_5 sy_wn_2_3_2 sy_wn_2_3_3 ; flagged files 0

ADDED 12 Nov 01:28 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): eh_k5x3 (m 20, 3292 classes, last line BEST) -0.550582772; eh_k6x2 (m 18, 952 classes, last line BEST) -0.695945208; ev_k2x2 (m 8, 51 classes, last line BEST) -0.135432834; 
Read at write time. 03:29 Mac mini 2 clock: ncpu=12 load=13.22 free_cores=1 avail=3595MB pressure=2; mine queued 292 running sy_ev_k2x3 sy_ev_k2x4 sy_ev_k2x5 sy_ev_k2x6 sy_ev_k3x4 sy_ev_k4 sy_ev_k5 sy_ev_k6 sy_ev_octa ; flagged files 0

ADDED 12 Nov 01:24 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): eh_k4x2 (m 12, 194 classes, last line BEST) -0.207054154; eh_k4x3 (m 16, 905 classes, last line BEST) -0.252671696; eh_k4x4 (m 20, 3684 classes, last line BEST) -0.252671696; eh_k5x2 (m 15, 450 classes, last line BEST) -0.553465343; 
Read at write time. 03:24 Mac mini 2 clock: ncpu=12 load=15.85 free_cores=-1 avail=3449MB pressure=2; mine queued 293 running sy_eh_k5x3 sy_eh_k6x2 sy_ev_k2x2 sy_ev_k2x3 sy_ev_k2x4 sy_ev_k2x5 sy_ev_k2x6 sy_ev_k3x4 sy_ev_k4 sy_ev_k5 sy_ev_k6 ; flagged files 0

ADDED 12 Nov 01:15 laptop clock (newest block; the NEXT line in the 07:46 block stands):
Mac mini 1 queue refilled at 01:14 laptop clock (its queue was down to 27): 47 jobs 46_agent_co_zoo_lib_<i>_n<n>_<3202+i>,
the library gates with 14, 15 and 16 inputs (14, 28 and 5 lines of zoo_lib.txt) as bases for fei_coin with 24 coins free,
1800 s each, 1500000 steps a run, T 0.03 to 0.00002, obj 1, jmin 1.2, qbal 0.9, table W_cur.txt, mem_mb 80. The 104
lines with 6 to 13 inputs ran before (none above 0; best three 0 (lib 21, the record tie), -0.023143487707 (lib 5),
-0.066370796906 (lib 81)). A 6 s test of line 8 (16 inputs) wrote three runs before queueing. Script: m1_queue_big.sh in
the session scratchpad; the loop is the lib mode of queue_coin_hot.sh on Mac mini 1 with the range 14..16.
Structure search that has ended on Mac mini 2: eh_k3x5 (m 18, 1280 classes, last line BEST) -0.551269057.
Neighbours of the record structure so far (eh_k<a>x<b>: edges of K_{a,b} plus the a side vertices): eh_k3x3 -0.056051752
and eh_k3x2 -0.071099786 sit between k33v -0.049887206 and diac -0.098844446; the eh_k2x<b> all stop at -0.118503715.

ADDED 12 Nov 01:10 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): eh_k3x3 (m 12, 220 classes, last line BEST) -0.056051752; eh_k3x4 (m 15, 562 classes, last line BEST) -0.275173185; 
Read at write time. 03:10 Mac mini 2 clock: ncpu=12 load=13.19 free_cores=0 avail=4388MB pressure=1; mine queued 298 running sy_eh_k3x5 sy_eh_k4x2 sy_eh_k4x3 sy_eh_k4x4 sy_eh_k5x2 sy_eh_k5x3 sy_eh_k6x2 sy_ev_k2x2 sy_ev_k2x3 sy_ev_k2x4 sy_ev_k2x5 ; flagged files 0

ADDED 12 Nov 01:07 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): eh_k2x6 (m 14, 184 classes, last line BEST) -0.118503715; eh_k3x2 (m 9, 74 classes, last line BEST) -0.071099786; q4v (m 16, 402 classes, last line BEST) -0.245967089; 
Read at write time. 03:07 Mac mini 2 clock: ncpu=12 load=12.98 free_cores=0 avail=3999MB pressure=1; mine queued 300 running sy_eh_k3x4 sy_eh_k3x5 sy_eh_k4x2 sy_eh_k4x3 sy_eh_k4x4 sy_eh_k5x2 sy_eh_k5x3 sy_eh_k6x2 sy_ev_k2x2 sy_ev_k2x3 ; flagged files 0

ADDED 12 Nov 01:01 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): eh_k2x4 (m 10, 79 classes, last line BEST) -0.118503715; eh_k2x5 (m 12, 124 classes, last line BEST) -0.118503715; 
Read at write time. 03:01 Mac mini 2 clock: ncpu=12 load=15.46 free_cores=-1 avail=4094MB pressure=1; mine queued 303 running sy_eh_k2x6 sy_eh_k3x2 sy_eh_k3x3 sy_eh_k3x4 sy_eh_k3x5 sy_eh_k4x2 sy_eh_k4x3 sy_eh_k4x4 sy_eh_k5x2 sy_eh_k5x3 sy_q4v ; flagged files 0

ADDED 12 Nov 00:58 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): ec_k2x5 (m 20, 7882 classes, last line BEST) -0.986901970; eh_k2x3 (m 8, 46 classes, last line BEST) -0.118503715; 
Read at write time. 02:58 Mac mini 2 clock: ncpu=12 load=19.81 free_cores=-1 avail=4269MB pressure=1; mine queued 304 running sy_eh_k2x4 sy_eh_k2x5 sy_eh_k2x6 sy_eh_k3x2 sy_eh_k3x3 sy_eh_k3x4 sy_eh_k3x5 sy_eh_k4x2 sy_eh_k4x3 sy_eh_k4x4 sy_eh_k5x2 sy_q4v ; flagged files 0

ADDED 12 Nov 00:52 laptop clock (newest block; item (7) of the NEXT list in the 00:01 block; the NEXT line in the 07:46 block stands):
Cube edits of the record gate with d=6 have ended (k33c seed pm+coins, m 18; a subcube fixes 6 inputs and the gate is
set to one sign on it): 1188096 subcubes, one per orbit 17748, 478294 gates scored, none above 0, none equal to the
seed, best slack -0.002718274 (G 6.780266213, J 2.040041008), the top eight rescored from the truth table; 5647 s.
With d=3, 4, 5 (-0.105819030, -0.007644592, -0.005366807) the best edit comes nearer 0 from below as the subcube
shrinks, which a smaller edit must do; no edit of this kind beats the record gate. Output sy_cube_k33c_d6.txt.
Structure search that has ended: wn_2_2_4 (m 16, 126 classes, last line BEST) -1.366981042.
Read at write time. 02:51 Mac mini 2 clock: ncpu=12 load=14.08 free_cores=-1 avail=3247MB pressure=1; mine queued 307 running sy_ec_k2x5 sy_eh_k2x3 sy_eh_k2x4 sy_eh_k2x5 sy_eh_k2x6 sy_eh_k3x2 sy_eh_k3x3 sy_eh_k3x4 sy_eh_k3x5 sy_eh_k4x2 sy_q4v ; flagged files 0

ADDED 12 Nov 00:45 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): sub_6_3 (m 20, 2136 classes, last line BEST) -0.784411885; wn_2_2_2_2 (m 16, 231 classes, last line BEST) -0.245967089; wn_2_2_3 (m 12, 56 classes, last line BEST) -0.491254730; 
Read at write time. 02:46 Mac mini 2 clock: ncpu=12 load=14.98 free_cores=0 avail=3702MB pressure=1; mine queued 309 running sy_ec_k2x5 sy_eh_k2x3 sy_eh_k2x4 sy_eh_k2x5 sy_eh_k2x6 sy_eh_k3x2 sy_eh_k3x3 sy_eh_k3x4 sy_cube_k33c_d6 sy_q4v sy_wn_2_2_4 ; flagged files 0

ADDED 12 Nov 00:38 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): psl_19 (m 20, 396 classes, last line BEST) -3.904511506; psl_9c (m 20, 3552 classes, last line BEST) -2.238145843; 
Read at write time. 02:38 Mac mini 2 clock: ncpu=12 load=13.64 free_cores=0 avail=3846MB pressure=1; mine queued 312 running sy_ec_k2x5 sy_eh_k2x3 sy_eh_k2x4 sy_eh_k2x5 sy_eh_k2x6 sy_cube_k33c_d6 sy_q4v sy_sub_6_3 sy_wn_2_2_2_2 sy_wn_2_2_3 sy_wn_2_2_4 ; flagged files 0

ADDED 12 Nov 00:35 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): pr_9_9 (m 18, 100 classes, last line BEST) -3.996722769; psl_17 (m 18, 192 classes, last line BEST) -3.518116907; 
Read at write time. 02:35 Mac mini 2 clock: ncpu=12 load=13.77 free_cores=1 avail=3719MB pressure=1; mine queued 313 running sy_ec_k2x5 sy_eh_k2x3 sy_eh_k2x4 sy_eh_k2x5 sy_cube_k33c_d6 sy_psl_19 sy_psl_9c sy_q4v sy_sub_6_3 sy_wn_2_2_2_2 sy_wn_2_2_3 sy_wn_2_2_4 ; flagged files 0

ADDED 12 Nov 00:31 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): pr_6_6 (m 12, 49 classes, last line BEST) -2.529825610; pr_6_6_6 (m 18, 343 classes, last line BEST) -2.529825610; pr_7_7 (m 14, 64 classes, last line BEST) -3.053488977; pr_8_8 (m 16, 81 classes, last line BEST) -3.509965028; 
Read at write time. 02:31 Mac mini 2 clock: ncpu=12 load=18.13 free_cores=1 avail=3834MB pressure=1; mine queued 315 running sy_ec_k2x5 sy_eh_k2x3 sy_cube_k33c_d6 sy_pr_9_9 sy_psl_17 sy_psl_19 sy_psl_9c sy_q4v sy_sub_6_3 sy_wn_2_2_2_2 sy_wn_2_2_3 sy_wn_2_2_4 ; flagged files 0

ADDED 12 Nov 00:23 laptop clock (newest block; item (3) of the NEXT line in the 07:46 block, continued; that NEXT line stands):
Ranking of the 109 structure searches finished on Mac mini 2 by 00:15: the record structure k33c stands alone at 0
(k33cs holds the same gate, bs_3 is the one-input gate); next come k33v (the edges of K33 and one input per vertex,
-0.049887206) and diac (-0.098844446); every other finished structure is below -0.13. So the next family is the
record's own neighbourhood. sym_search.py takes ev_<g> (the edges of a graph and one input per vertex), ec_<g> (the
edges and one coin per edge) and eh_k<a>x<b> (the edges of K_{a,b} and one input per vertex of the a side, the sides
not exchanged); <g> is k<n>, k<a>x<b> or octa. Tested on Mac mini 2 without the transform (code/test_grp3.py): the
group is listed apart from the script's generators, as every vertex permutation that keeps the edge set, by brute
force; every generator is a permutation and lies in it, the closure of the generators has the same order, the class
sizes sum to 2^m, and the class count equals a Burnside count over every element. ev_k3x3, ec_k3x3, ec_k2x3, ec_k2x4,
ec_k4 and ec_k5 give the class counts of k33v, k33c, k23c, k24c, k4c and k5c (756, 4480, 430, 1996, 276, 10688).
The old structures return the same generators as before (14 of 14 compared).
Classes: ev_k2x2 51 (m 8, order 8); ev_k2x3 268 (m 11, order 12); ev_k2x4 718 (m 14, order 48); ev_k2x5 1692 (m 17, order 240); ev_k2x6 3620 (m 20, order 1440); ev_k3x4 6170 (m 19, order 144); ev_k4 90 (m 10, order 24); ev_k5 544 (m 15, order 120); ev_k6 5096 (m 21, order 720); ev_octa 6456 (m 18, order 48); ec_k2x5 7882 (m 20, order 240); eh_k2x3 46 (m 8, order 12); eh_k3x2 74 (m 9, order 12); eh_k2x4 79 (m 10, order 48); eh_k4x2 194 (m 12, order 48); eh_k2x5 124 (m 12, order 240); eh_k5x2 450 (m 15, order 240); eh_k2x6 184 (m 14, order 1440); eh_k6x2 952 (m 18, order 1440); eh_k3x3 220 (m 12, order 36); eh_k3x4 562 (m 15, order 144); eh_k4x3 905 (m 16, order 144); eh_k3x5 1280 (m 18, order 720); eh_k5x3 3292 (m 20, order 720); eh_k4x4 3684 (m 20, order 576); 
Queued: 24_agent_sy_<name>.job for 25 of them, 1500 s, seed 61, output sy_<name>.txt. Not queued: none
Mac mini 1: 20 of my 40 queued jobs were moved from prefixes 31, 33 and 35 to prefix 46, behind the
jobs of another agent (that queue starts jobs in name order and theirs had not started since 22:04 Mac time).
Read at write time. 02:24 Mac mini 2 clock: ncpu=12 load=19.97 free_cores=0 avail=3395MB pressure=1; mine queued 317

ADDED 11 Nov 00:16 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
CORRECTION 12 Nov 00:23 laptop clock: the heading above should read 12 Nov, not 11 Nov (written on 12 Nov; the script had the day fixed).
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): pr_5_5_5 (m 15, 216 classes, last line BEST) -2.212804203; pr_5_5_5_5 (m 20, 1296 classes, last line BEST) -2.381239217; pr_6_12 (m 18, 91 classes, last line BEST) -2.529825610; 
Read at write time. 02:16 Mac mini 2 clock: ncpu=12 load=11.69 free_cores=2 avail=3727MB pressure=1; mine queued 295 running sy_cube_k33c_d6 sy_pr_6_6_6 sy_pr_7_7 sy_pr_8_8 sy_pr_9_9 sy_psl_17 sy_psl_19 sy_psl_9c sy_q4v sy_sub_6_3 ; flagged files 0

ADDED 11 Nov 00:11 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
CORRECTION 12 Nov 00:23 laptop clock: the heading above should read 12 Nov, not 11 Nov (written on 12 Nov; the script had the day fixed).
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): pr_10_10 (m 20, 121 classes, last line BEST) -4.395468321; pr_3_3_3_3 (m 12, 256 classes, last line BEST) -0.580752762; pr_3_3_3_3_3 (m 15, 1024 classes, last line BEST) -0.665201147; pr_3_3_3_3_3_3 (m 18, 4096 classes, last line BEST) -0.693178861; pr_3_6_9 (m 18, 280 classes, last line BEST) -1.260922855; pr_4_4_4 (m 12, 125 classes, last line BEST) -1.418974843; pr_4_4_4_4 (m 16, 625 classes, last line BEST) -1.477988713; pr_4_4_4_4_4 (m 20, 3125 classes, last line BEST) -1.681747860; 
Read at write time. 02:11 Mac mini 2 clock: ncpu=12 load=13.45 free_cores=-1 avail=4118MB pressure=1; mine queued 298 running sy_cube_k33c_d6 sy_pr_5_5_5 sy_pr_5_5_5_5 sy_pr_6_12 sy_pr_6_6 sy_pr_6_6_6 sy_pr_7_7 sy_pr_8_8 sy_pr_9_9 sy_psl_17 sy_psl_19 ; flagged files 0

ADDED 12 Nov 00:01 laptop clock (newest block; items (1) and (3) of the NEXT line in the 07:46 block; that NEXT line stands, with the
additions at the end of this block):
Outage: the laptop lost the network at 11:09 on 11 Nov and both Macs were off the tailnet from about 11:30 to 16:50;
Mac mini 2 restarted at 18:52 its clock (16:52 laptop). Nothing on GitHub was lost. Seven searches died at the restart
(sy_ap_19, sy_ap_7c, sy_bs_3, sy_bs_4, sy_dg_4, sy_cube_k33c_d5, sy_cube_k33c_d6; exit codes 99 and 143). Their partial
outputs were renamed *.pre_reboot and the jobs went back into the queue at 20:01 laptop clock. The other 13 entries
of mine in failed/ on Mac mini 2 (co_k33_807, het_a, het_b, ms_n8_*, ms_n10_*) are from before the outage.
Reader fault in fei_coin.c and fei_coinp.c, fixed in code/ in the same commit: getline_k read library lines with
fgets into a buffer sized for the job's own input count, so a longer line earlier in zoo_lib.txt came back in pieces
and each piece was counted as a line. Of the 104 co_zoo_lib jobs on Mac mini 1, 78 stopped at once with
'hex line has n = ...', and 19 of the 26 that ran had started from an earlier library line with the same input count,
not the line their name gives (the job named line 70 started from line 49; checked by replaying the old reader on the
file, scratch sim_reader.py). Those 19 results are valid searches from a library gate; only the label is wrong. The
fixed reader skips the tail of an over-long line. On Mac mini 1 it was rebuilt and tested (lines 5, 94, 70 and 49 load;
a 15-input line asked for as 6 inputs is refused), the 78 jobs were put back in the queue and 19 jobs were added for
the lines never started (output names end in r). fei_coinp on the Macs is still the old build.
Subcube edits of the record, continued (code/cube1.py; outputs sy_cube_k33c_d<d>.txt on Mac mini 2), none above 0,
top eight rescored from the truth table each time: d=3 best -0.105819030 (5014 gates); d=4 best -0.007644592 (27081 gates); d=5 best -0.005366807 (125854 gates).
Structure searches that have ended since the 10:27 block of 11 Nov, best slack each, all below 0 (at most 34
classes means every invariant function was scored; more means seeds, flip scans and anneals for 1500 s):
af_4 (m 16, 32 classes, last line exh) -3.731093717; al_9c (m 18, 3800 classes, last line BEST) -1.991877917; alf_16 (m 16, 118 classes, last line BEST) -1.899402208; alf_8c (m 16, 496 classes, last line BEST) -2.042285583; alf_9c (m 18, 2260 classes, last line BEST) -1.816014978; ap_11 (m 11, 44 classes, last line BEST) -1.804716017; ap_13 (m 13, 140 classes, last line BEST) -0.660509954; ap_17 (m 17, 1040 classes, last line BEST) -0.705515042; ap_19 (m 19, 3100 classes, last line BEST) -2.493704406; ap_7c (m 14, 824 classes, last line BEST) -0.382829597; bs_3 (m 8, 80 classes, last line BEST) +0.000000000; bs_4 (m 16, 3984 classes, last line BEST) -0.163068437; dg_4 (m 12, 218 classes, last line BEST) -0.160154561; dih18 (m 18, 7685 classes, last line BEST) -0.532855736; g3_2_2_2 (m 8, 46 classes, last line BEST) -0.207054154; g3_2_2_3 (m 12, 237 classes, last line BEST) -0.224587389; g3_2_2_4 (m 16, 1056 classes, last line BEST) -0.245967089; g3_2_2_5 (m 20, 4071 classes, last line BEST) -0.371599232; g3_2_3_3 (m 18, 4236 classes, last line BEST) -0.439318784; gl_4 (m 15, 46 classes, last line BEST) -2.926323324; gr_2_10 (m 20, 161 classes, last line BEST) -2.356942034; gr_2_6 (m 12, 50 classes, last line BEST) -0.491254730; gr_2_7 (m 14, 70 classes, last line BEST) -0.713489509; gr_2_8 (m 16, 95 classes, last line BEST) -0.988873386; gr_2_9 (m 18, 125 classes, last line BEST) -2.200141978; gr_3_5 (m 15, 190 classes, last line BEST) -0.553465343; gr_3_6 (m 18, 386 classes, last line BEST) -0.695945208; gr_4_5 (m 20, 1053 classes, last line BEST) -0.728168968; gv_clebsch (m 16, 151 classes, last line BEST) -0.559631852; gv_desarg (m 20, 5466 classes, last line BEST) -0.447927675; gv_heawood (m 14, 146 classes, last line BEST) -0.382829597; gv_mobkan (m 16, 887 classes, last line BEST) -0.245967089; gv_pappus (m 18, 1630 classes, last line BEST) -0.405908793; gv_shrik (m 16, 528 classes, last line BEST) -0.368916638; k33k33 (m 18, 351 classes, last line BEST) -0.182347505; k5c (m 20, 10688 classes, last line BEST) -0.331418287; m11c (m 22, 1096 classes, last line BEST) -3.376198938; pg24 (m 21, 160 classes, last line BEST) -1.793407593; pgl19 (m 20, 260 classes, last line BEST) -3.904511506; pl_16 (m 17, 80 classes, last line BEST) -3.532539464; pl_5c (m 12, 94 classes, last line BEST) -0.491254730; pl_7c (m 16, 355 classes, last line BEST) -2.099610792; pl_8c (m 18, 684 classes, last line BEST) -2.855791438; pl_9c (m 20, 1844 classes, last line BEST) -2.931249042; plf_16 (m 17, 48 classes, last line BEST) -3.532539464; plf_8c (m 18, 364 classes, last line BEST) -2.200141978; plf_9c (m 20, 1312 classes, last line BEST) -2.801767006; pr_10_10 (m 20, 121 classes, last line BEST) -4.395468321; pr_3_3_3_3 (m 12, 256 classes, last line BEST) -0.580752762; pr_3_3_3_3_3 (m 15, 1024 classes, last line BEST) -0.665201147; psl_13 (m 14, 52 classes, last line BEST) -2.628191135; psl_5c (m 12, 144 classes, last line BEST) -0.491254730; psl_7c (m 16, 516 classes, last line BEST) -2.042285583; ag23c (m 18, 1060 classes, last line BEST) -1.778614160; agl11 (m 11, 30 classes, last line exh) -2.159382952; agl13 (m 13, 74 classes, last line BEST) -2.335783714; agl17 (m 17, 522 classes, last line BEST) -2.258286783; c6c (m 12, 430 classes, last line BEST) -0.142954969; c7c (m 14, 1300 classes, last line BEST) -0.223475253; c8c (m 16, 4435 classes, last line BEST) -0.137347878; dih12 (m 12, 224 classes, last line BEST) -0.224587389; dih14 (m 14, 687 classes, last line BEST) -0.300015211; dih16 (m 16, 2250 classes, last line BEST) -0.183692121; fanoc (m 14, 264 classes, last line BEST) -1.402139745; fanoc2 (m 21, 2766 classes, last line BEST) -0.801286665; k113c (m 14, 1720 classes, last line BEST) -0.152026160; k23c (m 12, 430 classes, last line BEST) -0.142954969; k33mc (m 16, 8740 classes, last line BEST) -0.162606579; k34 (m 12, 87 classes, last line BEST) -0.277684672; k3c2 (m 9, 56 classes, last line BEST) -0.159675860; k3c3 (m 12, 120 classes, last line BEST) -0.480998026; k3c4 (m 15, 220 classes, last line BEST) -0.540225656; k3c5 (m 18, 364 classes, last line BEST) -0.540225656; k44 (m 16, 192 classes, last line BEST) -0.252671696; k4c (m 12, 276 classes, last line BEST) -0.159675860; k4c2 (m 18, 2451 classes, last line BEST) -0.159675860; k5 (m 10, 34 classes, last line exh) -0.574258328; k6 (m 15, 156 classes, last line BEST) -0.534546704; octa (m 12, 144 classes, last line BEST) -0.160154561; pet (m 15, 396 classes, last line BEST) -0.328817600; pgl11 (m 12, 20 classes, last line exh) -2.666091799; pgl13 (m 14, 35 classes, last line BEST) -2.628191135; pgl17 (m 18, 113 classes, last line BEST) -3.518116907; q3e (m 12, 144 classes, last line BEST) -0.160154561; q3vc (m 16, 1996 classes, last line BEST) -0.320090292; s10c (m 20, 286 classes, last line BEST) -2.356942034; s9c (m 18, 220 classes, last line BEST) -2.200141978; w33c (m 18, 1540 classes, last line BEST) -0.522479521; w4c (m 16, 8740 classes, last line BEST) -0.162606579.
Library starts on Mac mini 1 (fei_coin, 900 s each): 90 output files, none above 0. Best: co_zoo_lib_21_n10_3223r +0.000000000000 (a tie with the
record at twelve places; not yet checked whether it is the record gate itself on a padded base), then co_zoo_lib_5_n9_3207 -0.023143487707.
CORRECTION 12 Nov 00:06 laptop clock, to the two lines above and to the structure list in this block: both values that read
+0.000000000 were opened. (a) co_zoo_lib_21_n10_3223r is the record gate itself: G 6.776605309006, J 2.039062500000
= 261/128, a 10-input base with eight coin labels, reached from library line 21 in runs 199 to 203 of 206. A tie, not
a new gate. (b) bs_3 is not below 0 as the list's heading says: its BEST is the one-input gate (G 0, J 1), which sits
at exactly 0 in this frame by construction and says nothing. Of its 300 anneals only five ended on a gate with J above
1, best -0.101186821 (G 3.359482744, J 1.551515152), so bs_3 was barely searched. No other sy_ file on Mac mini 2 has
a J = 1 gate on its last line (212 finished, checked 12 Nov 00:05). Items (5) and (6) of the NEXT list below are done:
fei_coinp was rebuilt on Mac mini 1 from the fixed source and loads lines 5, 94 and 70 (line 5 on 9 inputs starts at
-0.071099785797, the same as fei_coin); no queued or running job of mine uses it.
ADDED 12 Nov 00:09 laptop clock, inside the correction above: code/sym_search.py takes --jmin X; score() then returns -1e9 for a gate with J below X, so
anneals and flip scans cannot settle on the one-input gate. The default 0 leaves every earlier and queued run as it
was. bs_3 is queued again on Mac mini 2 as sy_bs_3j with --jmin 1.2 (output sy_bs_3j.txt).
Read at write time. 01:59 Mac mini 2 clock: ncpu=12 load=25.41 free_cores=0 avail=3757MB pressure=1; mine queued 302 running sy_cube_k33c_d6 sy_pr_3_3_3_3_3_3 sy_pr_3_6_9 sy_pr_4_4_4 sy_pr_4_4_4_4 sy_pr_4_4_4_4_4 sy_pr_5_5_5 sy_pr_5_5_5_5 sy_pr_6_12 sy_pr_6_6 sy_pr_6_6_6 ; flagged files 0
Read at write time. 01:59 Mac mini 1 clock: ncpu=10 load=11.42 free_cores=0 avail=7721MB pressure=1; mine queued 53 running 6 done 143 failed 0; flagged files 0
NEXT, added to the 07:46 list: (5) open the tie above and say whether it is the record gate; (6) rebuild fei_coinp on
Mac mini 1 with the fixed reader before any hex-start run of it; (7) read cube d=6 and the pr_* family as they end.

ADDED 11 Nov 10:27 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): ag24 (m 16, 77 classes, last line BEST) -1.899402208; al_8c (m 16, 1216 classes, last line BEST) -1.874203306; 
Read at write time. 12:27 Mac mini 2 clock: ncpu=12 load=10.08 free_cores=-1 avail=6163MB pressure=1; mine queued 364 running sy_al_9c sy_alf_16 sy_alf_8c sy_alf_9c sy_ap_11 ; flagged files 0

ADDED 11 Nov 10:22 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): al_16 (m 16, 304 classes, last line BEST) -1.899402208; 
Read at write time. 12:22 Mac mini 2 clock: ncpu=12 load=10.49 free_cores=0 avail=7991MB pressure=1; mine queued 367 running sy_al_8c sy_al_9c sy_alf_16 ; flagged files 0

ADDED 11 Nov 10:19 laptop clock (newest block; a second test beside the NEXT line in the 07:46 block; that NEXT line stands):
Subcube edits of the record gate, no symmetry kept in the result (code/cube1.py; on Mac mini 2 cube1.py): fix d of the
18 inputs to given values and, on that subcube only, replace the gate by its negation, by a constant, or by one of the
free inputs or its negation. One subcube per orbit of the K33 group is tried; each edited gate is scored from its full
transform and the best eight again from a rebuilt truth table (they agree).
summary d=1 subcubes 36, one per orbit 4, gates scored 148, the seed again 0, above 0: 0, best below the seed slack -0.099838241
summary d=2 subcubes 612, one per orbit 24, gates scored 840, the seed again 0, above 0: 0, best below the seed slack -0.098118237
reduction check d=1 (all edits): distinct scores one-per-orbit 23, every subcube 23, same set True
reduction check d=2 (negation only): distinct scores one-per-orbit 11, every subcube 11, same set True
Queued on Mac mini 2 as 25_agent_sy_cube_k33c_d3.job .. _d6.job (mem_mb 500 each), outputs sy_cube_k33c_d<d>.txt;
read them with: grep -v progress sy_cube_k33c_d<d>.txt. A line with !!! is rebuilt from the truth table before a word
is said. The .out files carry matmul warnings from the Mac's numpy; the explicit re-scoring agrees to nine places.
Read at write time. 12:19 Mac mini 2 clock: ncpu=12 load=10.77 free_cores=-1 avail=7500MB pressure=1; mine queued 368 running sy_ag24 sy_al_16 sy_al_8c sy_al_9c ; flagged files 0

ADDED 11 Nov 10:11 laptop clock (newest block; a test beside the NEXT line in the 07:46 block; that NEXT line stands):
Single-point flips of the record gate, no symmetry kept (code/flip1.py; on Mac mini 2 flip1.py, output flip1_k33c.txt):
for one point from each of the 4480 orbits of the K33 group on the 18 inputs, the gate's value at that point alone was
flipped and the result scored from its full transform. All 4480 changes of the slack are below 0, between -4.288e-04
and -1.041e-04 (the W term adds +1.95e-08 to each). The six best were scored again from the explicit flipped truth
table and agree. The orbit searches flip whole orbits, so they had not tested this. Cross-check (chk_flip1.py): the four
orbits of size 1 give -0.000335744 -0.000335744 -0.000335744 -0.000335744, and the best of them equals the best one-orbit flip
sy_k33c reported (-0.000335744). So the record is a strict local best under any one-point change among all gates on 18
inputs, and no such change gives a new lower bound. Rough count of why: one flipped point moves weight 4/2^18 onto all
sets evenly, which buys about 2m - 2 = 34 bits of entropy per unit of weight and costs c(m/2 - J) = about 45 per unit.
Read at write time. 12:11 Mac mini 2 clock: ncpu=12 load=11.46 free_cores=-2 avail=8621MB pressure=1; mine queued 364 running sy_ag24 sy_al_16 sy_al_8c sy_al_9c ; flagged files 0

ADDED 11 Nov 10:00 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
Structure searches that have ended, best slack each, all below 0 (at most 34 classes means every invariant function
was scored; more means seeds, flip scans and anneals for 1500 s): al_11 (m 11, 30 classes, last line exh) -2.159382952; af_3c (m 16, 271 classes, last line BEST) -2.042285583; agl19 (m 19, 1610 classes, last line BEST) -2.493704406; 
Read at write time. 12:01 Mac mini 2 clock: ncpu=12 load=10.55 free_cores=-1 avail=7604MB pressure=1; mine queued 365 running sy_ag24 sy_al_16 sy_al_8c ; flagged files 0

ADDED 11 Nov 09:55 laptop clock (newest block; item (3) of the NEXT line in the 07:46 block, continued; that NEXT line stands):
sym_search.py takes m11t: the 12 points under the Mathieu group M11 in its 3-transitive action, as a subgroup of the
m12 group. Its two generators are words in the m12 generators found by a seeded search (find_m11t.py on Mac mini 2):
[9,1,0,7,2,4,5,11,10,6,8,3] and [2,11,4,0,6,1,10,9,8,5,7,3]. Tested: their closure has order 7920, gives 1320 distinct
images of the first three points, lies inside the closure of the m12 generators (order 95040), and the class count
(19) equals the Burnside count over every element. Twelve old structures return the same generators as before.
m11t: every invariant function was scored (exhaustive branch, reported states re-scored from the explicit truth table), best slack -3.039034946.
Read at write time. 11:55 Mac mini 2 clock: ncpu=12 load=10.42 free_cores=0 avail=8065MB pressure=1; mine queued 367 running sy_ag24 sy_agl19 sy_al_11 ; flagged files 0

ADDED 11 Nov 09:49 laptop clock (correction to the 09:27 block below; the NEXT line in the 07:46 block stands):
In the Classes line of the 09:27 block the words "order True" stand where the group orders belong. The orders, from
the same test output (tnew/test8.txt on Mac mini 2): af_4 322560; af_3c 1344; m12 95040; plf_8c 1512; pl_8c 504; plf_9c 1440; pl_9c 720; plf_16 16320; pl_16 4080; alf_9c 144; al_9c 72; alf_8c 168; al_8c 56; alf_16 960; al_16 240; pl_7c 336; pl_5c 120; 
The class counts and m in that line are right as printed.

ADDED 11 Nov 09:47 laptop clock (newest block; item (3) of the NEXT line in the 07:46 block, continued; that NEXT line stands):
sy_af_4 has ended: all 2^32 functions on 16 points invariant under AGL(4,2) were scored, best slack -3.731093717.
sym_search.py takes three more families and one group, none with seeds: psl_<q> (the q + 1 points of the projective
line over GF(q) under PSL(2,q), q odd), ap_<q> (the q points of GF(q) under the maps x -> s x + b with s a nonzero
square, q odd), gl_<n> (the 2^n - 1 nonzero vectors over GF(2) under GL(n,2)), each with an optional trailing c for
one coin per point, and m11 / m11c (11 points under the Mathieu group M11, generated by an 11-cycle and
(2 6 10 7)(3 9 4 5) on the points 0..10). Tested on Mac mini 2 without the transform: every generator is a
permutation and lies in the group, the group has the expected order, the class sizes sum to 2^m, and the class count
equals a Burnside count over every element, where the group is listed apart from the script's generators (all Moebius
maps with square determinant and all maps s x + b with the field arithmetic written a second time, all invertible
matrices over GF(2)). M11 is the closure of its two generators, identified by order 7920 and sharp 4-transitivity.
The old structures return the same generators as before (26 of 26 compared).
Classes: ap_7 12 (m 7, order 21); ap_11 44 (m 11, order 55); ap_13 140 (m 13, order 78); ap_17 1040 (m 17, order 136); ap_19 3100 (m 19, order 171); ap_7c 824 (m 14, order 21); psl_7 11 (m 8, order 168); psl_9 20 (m 10, order 360); psl_11 22 (m 12, order 660); psl_13 52 (m 14, order 1092); psl_17 192 (m 18, order 2448); psl_19 396 (m 20, order 3420); psl_5c 144 (m 12, order 60); psl_7c 516 (m 16, order 168); psl_9c 3552 (m 20, order 360); gl_4 46 (m 15, order 20160); m11 14 (m 11, order 7920); m11c 1096 (m 22, order 7920); 
At most 22 classes, every invariant function scored at once (exhaustive branch, each reported state re-scored from
its explicit truth table), best slack per structure: ap_7 (m 7, 12 classes) -1.430069488; psl_7 (m 8, 11 classes) -2.099610792; psl_9 (m 10, 20 classes) -2.242605903; psl_11 (m 12, 22 classes) -2.666091799; m11 (m 11, 14 classes) -4.041418247; 
Queued: 25_agent_sy_<name>.job for 13 of them, 1500 s, seed 53, output sy_<name>.txt. Not queued: none
Read at write time. 11:47 Mac mini 2 clock: ncpu=12 load=11.54 free_cores=-2 avail=8727MB pressure=1; mine queued 368 running sy_af_3c sy_ag24 sy_agl19 ; flagged files 0

ADDED 11 Nov 09:30 laptop clock (newest block; first results from the groups of the block below; the NEXT line in the 07:46 block stands):
The same groups without coins, on at most 13 points. Where the group has at most 22 classes of points every invariant
function was scored (sym_search.py, exhaustive branch, each reported state re-scored from its explicit truth table).
Best slack per structure, all below 0: m12 (m 12, 14 classes) -4.657721601; af_3 (m 8, 10 classes) -2.500836039; pl_5 (m 6, 7 classes) -2.529825610; pl_7 (m 8, 10 classes) -2.099610792; pl_8 (m 9, 10 classes) -3.996722769; plf_8 (m 9, 10 classes) -3.996722769; pl_9 (m 10, 14 classes) -2.945995106; plf_9 (m 10, 14 classes) -2.945995106; al_7 (m 7, 10 classes) -1.618027336; al_8 (m 8, 10 classes) -2.500836039; alf_8 (m 8, 10 classes) -2.500836039; al_9 (m 9, 16 classes) -1.859388773; alf_9 (m 9, 16 classes) -1.859388773; 
Queued for the exhaustive branch (23 to 34 classes): al_11 (30 classes); 
More than 34 classes, not run without coins: al_13 (74 classes); 
Outputs sy_<name>.txt in ~/fei_agent on Mac mini 2. Read at write time. 11:30 Mac mini 2 clock: ncpu=12 load=10.75 free_cores=1 avail=7874MB pressure=1; mine queued 357 running sy_af_3c sy_af_4 cq_grow2_220 cq_grow2_221 cq_grow2_222 ; flagged files 0

ADDED 11 Nov 09:27 laptop clock (newest block; item (3) of the NEXT line in the 07:46 block, continued; that NEXT line stands):
sym_search.py takes five more families and one group, none with seeds: pl_<q> and plf_<q> (the q + 1 points of the
projective line over GF(q) under PGL(2,q) and under PGammaL(2,q)), al_<q> and alf_<q> (the q points of GF(q) under
AGL(1,q) and AGammaL(1,q)), af_<n> (the 2^n points of affine space over GF(2) under AGL(n,2)), each with an optional
trailing c for one coin per point, and m12 (12 points under the Mathieu group M12). GF(8), GF(9), GF(16) come from
x^3+x+1, x^2+1 over GF(3), x^4+x+1. Tested on Mac mini 2 without the transform: every generator is a permutation and
lies in the group, the group has the expected order, the class sizes sum to 2^m, and the class count equals a Burnside
count over every element, where the group is listed apart from the script's generators (all Moebius or affine maps
with the field arithmetic written a second time, all invertible matrices over GF(2) with all translations). M12 is
the closure of its four generators, identified by order 95040 and sharp 5-transitivity; its 14 classes agree with the
known count of its orbits on subsets. The old structures return the same generators as before (21 of 21 compared).
Classes: af_4 32 (m 16, order True); af_3c 271 (m 16, order True); m12 14 (m 12, order True); plf_8c 364 (m 18, order True); pl_8c 684 (m 18, order True); plf_9c 1312 (m 20, order True); pl_9c 1844 (m 20, order True); plf_16 48 (m 17, order True); pl_16 80 (m 17, order True); alf_9c 2260 (m 18, order True); al_9c 3800 (m 18, order True); alf_8c 496 (m 16, order True); al_8c 1216 (m 16, order True); alf_16 118 (m 16, order True); al_16 304 (m 16, order True); pl_7c 355 (m 16, order True); pl_5c 94 (m 12, order True); 
(Corrected 11 Nov 09:51: for "order True" in the line above read the group orders af_4 322560; af_3c 1344; m12 95040; plf_8c 1512; pl_8c 504; plf_9c 1440; pl_9c 720; plf_16 16320; pl_16 4080; alf_9c 144; al_9c 72; alf_8c 168; al_8c 56; alf_16 960; al_16 240; pl_7c 336; pl_5c 120; )
Queued: 25_agent_sy_<name>.job for 17 of them, 1500 s, seed 53, output sy_<name>.txt. Not queued: none
Read at write time. 11:27 Mac mini 2 clock: ncpu=12 load=10.95 free_cores=-1 avail=8504MB pressure=1; mine queued 359 running 3; grow files 22 with 47 finished anneals, best +0.000000000000; flagged files 0

ADDED 11 Nov 09:03 laptop clock (newest block; queue order on Mac mini 2 changed; the NEXT line in the 07:46 block stands):
The base-growing anneals keep returning to slack 0 and none passes it, so another 14 of them tell less than the first
result from each structure not yet searched. My queued jobs now run in this order: 25_agent_sy_<name>.job (the 76
structure searches, renamed from 29_), then 26_agent_cq_gs*.job (the 20 label searches, renamed from 27_), then the
remaining 27_agent_cq_grow*.job, then 31_agent_co_zoo_lib_*. Only the job file names changed; outputs keep their
names (sy_<name>.txt, cq_gs*.txt). No other agent's job was passed. Where an older block says 29_agent_sy_, read 25_.
Read at write time. 11:03 Mac mini 2 clock: ncpu=12 load=11.73 free_cores=-1 avail=8061MB pressure=1; mine queued 342 running 4; grow files 22 with 43 finished anneals, best +0.000000000000; flagged files 0
Mac mini 1 at the same time: 11-11 11:02:58 ncpu=10 load=24.63 free_cores=0 avail=2806MB pressure=2 queued=424 running=3 done=138 failed=0 11:03 Mac mini 1 clock: mine queued 172 hold 0 running 0 done 11 failed 0 flagged files 0 

ADDED 11 Nov 09:00 laptop clock (newest block; item (3) of the NEXT line in the 07:46 block, continued; that NEXT line stands):
sym_search.py takes four more families, none with seeds: sub_<n>_<k> (the k-subsets of an n-set under S_n; sub_n_2 is
the edge set of K_n), dg_<n> (the ordered pairs of an n-set, the arcs of the complete digraph, under S_n), g3_<a>_<b>_<c>
(the cells of an a x b x c box under any permutation of each axis, no exchange of axes) and bs_<n> (the 2^n subsets of
an n-set under S_n permuting the coordinates). Tested on Mac mini 2 without the transform: every generator is a
permutation and lies in the intended group, the class sizes sum to 2^m, and the class count equals a Burnside count
taken over every element of the group, listed from all permutations of the underlying set and not from the script's
generators (sub_5_2 gives 34 = k5, sub_6_2 gives 156 = k6). Classes: sub_6_3 2136 (m 20); dg_4 218 (m 12); dg_5 9608 (m 20); g3_2_2_2 46 (m 8); g3_2_2_3 237 (m 12); g3_2_2_4 1056 (m 16); g3_2_3_3 4236 (m 18); g3_2_2_5 4071 (m 20); bs_3 80 (m 8); bs_4 3984 (m 16); 
Queued: 29_agent_sy_<name>.job for nine of them, 1500 s, seed 47, output sy_<name>.txt. dg_5 holds two 9608 x 9608
matrices (about 1.5 GB), so it is parked beside k33cx1 and gv_dodec: ~/fei_agent/parked/30_agent_sy_dg_5.job,
same rule as in the 07:46 and 07:53 blocks, one parked job at a time.
The queued dih18 job (7685 classes, two matrices of 472 MB each) declared mem_mb 700; the declaration is now 1100.
The brain memory named in the 08:40 block was filed at 08:42:
fei_record_gate_is_k33_perfect_matching_local_best_k5_exhaustive_2026_11_11.
Read at write time. 11:00 Mac mini 2 clock: mine queued 342 running 4; grow files 22 with 42 finished anneals, best +0.000000000000; gs files 0; flagged files 0

ADDED 11 Nov 08:40 laptop clock (newest block; item (3) of the NEXT line in the 07:46 block, continued; that NEXT line stands):
sym_search.py takes gr_<a>_<b>: the a*b cells of a grid (the edges of K_{a,b}) under any permutation of the rows and any
of the columns (and the transpose when a = b; gr_3_3, gr_3_4, gr_4_4 give the class counts of k33, k34, k44). No seeds.
Tested on Mac mini 2 without the transform: every generator is a permutation, the class sizes sum to 2^m, and the class
count equals the Burnside count of a x b 0/1 matrices up to row and column permutations. With them go three structures
the script already had and that were never queued: agl19, pgl19, dih18. Classes: gr_2_6 50 (m 12); gr_2_7 70 (m 14); gr_2_8 95 (m 16); gr_2_9 125 (m 18); gr_2_10 161 (m 20); gr_3_5 190 (m 15); gr_3_6 386 (m 18); gr_4_5 1053 (m 20); agl19 1610 (m 19); pgl19 260 (m 20); dih18 7685 (m 18); 
Queued: 29_agent_sy_<name>.job for the 11 structures above, 1500 s, seed 47, output sy_<name>.txt (m 20 and any
with over 3000 classes run --batch 16). All have more than 34 classes, so all anneal from random starts.
A brain memory for the record's rule, the K33 local-best check and the K5 exhaustive search is written
(scratchpad mem_k33_k5.md) and not yet filed: the index claim was held by another agent at 08:40; file it with
brain.py remember fei_record_gate_is_k33_perfect_matching_local_best_k5_exhaustive_2026_11_11 once the claim is free.
Read at write time. 10:40 Mac mini 2 clock: mine queued 333 running 9; grow files 22 with 32 finished anneals, best +0.000000000000; gs files 0; flagged files 0

ADDED 11 Nov 08:23 laptop clock (newest block; item (1) of the NEXT line in the 07:46 block; that NEXT line stands):
sy_k5 ended (file sy_k5.txt on Mac mini 2): the ten edges of K5 as inputs, 34 classes of graphs on five vertices, every
one of the 2^33 graph properties (up to a global sign) scored, 10828 s. Best slack -0.574258328 (G 7.040555983, J 2.236784622,
p' 0.745117188, signs 0000000001110011111101111111111111 and its mirror at p' 0.254882812); the explicit truth table gives the
same three numbers. Next: -0.642313841, -0.650287854, -0.661732745. So no graph property on five vertices, used as the base
gate of the tower, reaches slack 0; the record 6.521845711 stands. (K4 with coins and K33 are in earlier blocks; sy_k5c, K5
with one coin per edge, is queued.)
Read at write time. 10:23 Mac mini 2 clock: mine queued 325 running 7; grow files 19 with 25 finished anneals, best +0.000000000000; gs files 0; flagged files 0

ADDED 11 Nov 08:17 laptop clock (newest block; item (3) of the NEXT line in the 07:46 block, continued; that NEXT line stands):
sym_search.py takes pr_<a>_<b>_...: consecutive blocks of a, b, ... inputs with any permutation inside a block and none
between blocks, and wn_<a>_<b>_<c>...: nested blocks, innermost first, every level under its full symmetric group (wn_a_b is
wr_a_b; recursive majority and read-once trees with equal fan-in live here). Tested on Mac mini 2 without the transform: the
class count and the class sizes equal the direct count (product of binomials for pr, nested multisets for wn) and the sizes
sum to 2^m. Classes: wn_2_2_3 56 (m 12); wn_2_3_2 55 (m 12); wn_3_2_2 55 (m 12); wn_2_2_4 126 (m 16); wn_2_4_2 120 (m 16); wn_4_2_2 120 (m 16); wn_2_2_2_2 231 (m 16); wn_2_3_3 220 (m 18); wn_3_2_3 220 (m 18); wn_3_3_2 210 (m 18); wn_2_2_5 252 (m 20); wn_2_5_2 231 (m 20); wn_5_2_2 231 (m 20); pr_6_6 49 (m 12); pr_4_4_4 125 (m 12); pr_3_3_3_3 256 (m 12); pr_7_7 64 (m 14); pr_5_5_5 216 (m 15); pr_3_3_3_3_3 1024 (m 15); pr_8_8 81 (m 16); pr_4_4_4_4 625 (m 16); pr_6_12 91 (m 18); pr_9_9 100 (m 18); pr_6_6_6 343 (m 18); pr_3_6_9 280 (m 18); pr_3_3_3_3_3_3 4096 (m 18); pr_10_10 121 (m 20); pr_5_5_5_5 1296 (m 20); pr_4_4_4_4_4 3125 (m 20); 
Queued: 29_agent_sy_<name>.job for the 29 structures above, 1500 s, seed 43, output sy_<name>.txt (m 20 and the two
with over 3000 classes run --batch 16). All have more than 34 classes, so all anneal from random starts.
Read at write time. 10:17 Mac mini 2 clock: mine queued 325 running 8; grow files 19 with 24 finished anneals, best +0.000000000000; gs files 0; flagged files 0

ADDED 11 Nov 08:03 laptop clock (newest block; item (3) of the NEXT line in the 07:46 block, continued; that NEXT line stands):
sym_search.py takes wr_<a>_<b>: b blocks of a inputs under S_a wr S_b (any permutation inside a block, any permutation of
the blocks), the family that holds tribes and majority of majorities. Tested on Mac mini 2 without the transform: the class
count equals the number of multisets C(a+b, b), the class sizes equal the direct count and sum to 2^m. Classes: wr_3_3 20 (m 9); wr_2_6 28 (m 12); wr_3_4 35 (m 12); wr_4_3 35 (m 12); wr_2_7 36 (m 14); wr_3_5 56 (m 15); wr_5_3 56 (m 15); wr_2_8 45 (m 16); wr_4_4 70 (m 16); wr_2_9 55 (m 18); wr_3_6 84 (m 18); wr_6_3 84 (m 18); wr_2_10 66 (m 20); wr_4_5 126 (m 20); wr_5_4 126 (m 20); 
Queued: 29_agent_sy_wr_<a>_<b>.job for the 15 structures above, 1500 s, seed 41, output sy_wr_<a>_<b>.txt (m 20 with
--batch 16). A structure with at most 34 classes is scored exhaustively, the others anneal from random starts.
Read at write time. 10:03 Mac mini 2 clock: mine queued 297 running 7; grow files 18 with 20 finished anneals, best +0.000000000000; gs files 0; flagged files 0

ADDED 11 Nov 07:53 laptop clock (newest block; item (3) of the NEXT line in the block below, continued; that NEXT line stands):
sym_search.py takes gv_<graph>: the vertices of a named graph as inputs under its full automorphism group, found by
backtracking (cubic graphs by LCF code; Clebsch; Shrikhande). Tested on Mac mini 2 without the transform: group order and class
count agree with the Burnside count, class sizes sum to 2^m. Group order / classes: gv_heawood (m 14) 336 / 146; gv_mobkan
(m 16) 96 / 887; gv_pappus (m 18) 216 / 1630; gv_clebsch (m 16) 1920 / 151; gv_shrik (m 16) 192 / 528; gv_desarg (m 20)
240 / 5466; gv_dodec (m 20) 120 / 9436. Queued: 29_agent_sy_gv_{heawood,mobkan,pappus,clebsch,shrik,desarg}.job, 3000 s,
seed 31, output sy_gv_<graph>.txt (desarg --batch 16, mem_mb 1000). Parked for memory beside k33cx1:
~/fei_agent/parked/30_agent_sy_gv_dodec.job (mem_mb 2300); move it to ~/fillq/queue/ under the same rule as k33cx1,
one of the two at a time. These have no graph seeds; they anneal from random starts.
Read at write time. 09:53 Mac mini 2 clock: mine queued 284 running 7; grow files 16 with 19 finished anneals, best +0.000000000000; gs files 0; flagged files 0

ADDED 11 Nov 07:46 laptop clock (newest block; the 07:22 NEXT line stands, with item (3) done and item (4) begun):
A stamp below is wrong: the block headed 07:45 was written at 07:40 laptop clock and its four jobs were queued at 09:36 Mac clock.
sy_k33c ended at 09:42 Mac clock (sy_k33c.txt, 59 lines; group of K33 on the 9 cells and the 9 coins, 4480 classes). The record's
function (seed pm+coins, slack 0) loses under every flip of one class (best -0.000335744, the classes of the all-0 and all-1
points and their two mixed forms) and under every flip of two classes (file line: best pair among 4480, classes 0 and 4454,
-0.000727753). The bare gate (seed pm, -0.071099786) also loses under every one-class flip (best -0.071432601). The run ended
in the pair scans, so no anneal ran in this structure. co_rec_805 ended with its last runs (to run 179) at the record's labels.
The queue's aging rule released its 281 held jobs (all mine) at 09:45 Mac clock when cq_grow2_213 started.
Read at write time. 09:46 Mac mini 2 clock: mine queued 280 running 5; grow files 14 with 18 finished anneals, best +0.000000000000; gs files 0; flagged files 0
09:46 Mac mini 1 clock: mine queued 172 running 3 done 8 failed 0
NEXT: (1) read sy_k33cs, sy_k33k33, sy_q4v, sy_ag24, sy_pg24, cq_gs*, cq_grow2*/grow3* as they end (compact read:
$TEMP/fei_m2ak.sh on the laptop, or tick44.sh); a line above 0 is rebuilt from the explicit truth table before a word is said;
(2) when sy_k33cs has ended and avail is above 5000 MB: mv ~/fei_agent/parked/30_agent_sy_k33cx1.job ~/fillq/queue/ ;
(3) further groups on 16 to 20 inputs with under 20,000 classes; (4) loop job 49a7ba01 expires about 17 Nov 21:4x: re-create it.

ADDED 11 Nov 07:45 laptop clock (newest block; this is item (4) of the 07:22 NEXT line begun, the rest of that line stands):
sym_search.py has four more structures, tested on Mac mini 2 without the transform (class sizes sum to 2^m): k33k33 = two
3x3 grids, each under the group of K33, with the swap of the two grids (order 10368); q4v = the 16 vertices of the 4-cube
under its group of order 384; ag24 = the 16 points of the affine plane over GF(4) under AGL(2,4); pg24 = the 21 points of the
projective plane over GF(4) under PGL(3,4). Classes: k33k33 351 (m 18); q4v 402 (m 16); ag24 77 (m 16); pg24 160 (m 21); 
Queued on Mac mini 2 at about 09:45 Mac clock: 29_agent_sy_{k33k33,q4v,ag24,pg24}.job, 3000 s, seed 21, output
sy_<name>.txt (pg24 with --batch 8, mem_mb 900). These have no graph seeds: a structure with at most 34 classes is scored
exhaustively, the others anneal from random starts.
Read at 09:34 Mac clock: 12 grow files, 6 finished anneals on the fast cores, all at slack 0 with the record's labels; no
file carries a positive-slack line; the 20 cq_gs jobs had not started.

ADDED 11 Nov 07:32 laptop clock (newest block; item (3) of the 07:22 NEXT line is done, the rest of it stands):
20 label searches queued on Mac mini 2 at 09:26 Mac clock from five bare graph gates: 27_agent_cq_gs<line>_<seed>.job,
gseeds.txt lines 5 (pm_k4, m 6), 6 (star_q3, m 12), 7 (pm_q3, m 12), 19 (star_mob8, m 12), 23 (star_k24, m 8), seeds 301 to 320,
pools 1:6,2:6,3:4 and 1:10, T0 0.002 and 0.008, --pcube 0.1, 22,480,000 steps an anneal for m 6 and 8, 13,600,000 for m 12;
output cq_gs<line>_<seed>.txt, read by tick44.sh with the other cq_ files.
Read at write time. 09:27 Mac mini 2 clock: mine queued 278 running 24; grow files 12 with 3 finished anneals, best +0.000000000000; gs files 0; flagged files 0
09:27 Mac mini 1 clock: 11-11 09:27:16 ncpu=10 load=19.38 free_cores=0 avail=3175MB pressure=2; mine queued 173 running 2 done 16 failed 0

ADDED 11 Nov 07:22 laptop clock (newest block; NEXT below replaces the 07:12 NEXT line):
sym_search.py has two new structures: k33cx1 and k33cx2 = k33c (9 cells, 9 coins, group of order 72) plus 1 or 2
further inputs that the group leaves in place (two further inputs may be swapped). Tested on Mac mini 2 without the
transform: k33c 4480 classes, k33cx1 8960 (m 19), k33cx2 13440 (m 20); class sizes sum to 2^m; all eight seeds
(pm, pm+coins, ham, ham+coins, det2, det2+coin, detR, detR+coin) are invariant and ignore the further inputs.
Memory: the search holds two K x K float64 matrices, so k33cx1 needs about 1.3 GB for them and about 1.8 GB at peak
with --batch 32; k33cx2 needs 2.9 GB for the matrices alone and is not queued on a 16 GB shared machine.
Queue on Mac mini 2: 29_agent_sy_k33cs.job went back at 09:16 Mac clock (avail 5513 MB). The k33cx1 job is
written but parked (~/fei_agent/parked/30_agent_sy_k33cx1.job, mem_mb 2400): the two together would take
more than half of the free memory.
NEXT: (1) read cq_grow*.txt and sy_k33cs.txt with tick44.sh; a line above 0 is rebuilt from the explicit truth
table before a word is said; (2) when sy_k33cs has ended and avail is above 5000 MB:
mv ~/fei_agent/parked/30_agent_sy_k33cx1.job ~/fillq/queue/ ; (3) coinq anneals from the three best bare
graph gates other than K33 (pm_k4, star_q3, star_mob8: gseeds.txt lines by name) with pools 1:6,2:6,3:4;
(4) groups on 16 to 20 inputs with under 20,000 classes. Loop job 49a7ba01 expires about 17 Nov 21:4x: re-create it.

ADDED 11 Nov 07:12 laptop clock (newest block; NEXT below replaces items (1)-(2) of the 06:43 NEXT line; (3)-(4) of 06:20 stand):
The record's rule (read from results/seeds/rec18.lab). Base: the 9 cells of a 3x3 grid (edges of K33). The gate is
true where the present cells contain a transversal (a perfect matching of K33). The nine coins sit on 18 base points
with no transversal and exactly 4 pivotal cells: for each cell (r,c) the cross (row r with column c) with and without
its centre, both carrying coin (r,c) with the same sign. Every other base point is a constant. The six transversals and
the six lines (rows and columns) of the grid are isomorphic set systems (rows <-> even permutations, columns <-> odd),
so "some line full" is the same gate up to renaming cells.
Bare graph gates (no coins), slack in the tower frame, code/graph_seeds.py ('star' = some vertex has all its edges
present, 'pm' = a perfect matching is present; k34, k24, k23: a matching covering the small side), 31 gates on Mac
mini 2 (gseeds.txt, ev_<name>.txt):
  star_k33 = pm_k33                 -0.071099785797   (value 6.486408968726)
  pm_k4                             -0.159675859909
  star_q3 = pm_octa = star_k4m      -0.160154561050
  star_mob8                         -0.205808915742
  star_b5c                          -0.230163894040
  pm_q3 = pm_k4m                    -0.230381837107
  pm_k44                            -0.252671696220
  star_k24                          -0.270490146387
  star_k23                          -0.289478212042
  star_k34                          -0.290122978441
  star_prism                        -0.325226366512
  star_pet                          -0.328817600454
  pm_mob8                           -0.343832160082
  pm_prism                          -0.358747359591
  star_k4                           -0.428107369605
  star_k44                          -0.457676252547
  pm_b5c                            -0.460486473517
  pm_k23 = star_c6k                 -0.518993499408
  pm_k6                             -0.534546704442
  star_octa                         -0.577705975110
  pm_c6k                            -0.580752761614
  star_k5                           -0.642313841408
  pm_k34                            -0.952104684719
  pm_k24                            -1.196949811376
  pm_pet = star_k6                  -1.351590584688
Reading: K33 stands alone, 0.089 ahead of the next graph. The orbit searches with coins on K4, Q3 and the octahedron
ended at exactly their bare values (-0.1597, -0.1602), so coins gained nothing there; the 4x4 grid (pm_k44) is far
behind the 3x3. The record's gate is not the first member of a family over these graphs.
Grow search (record padded to 10 to 12 base inputs, 36 jobs): at 09:08 Mac clock 12 started, two finished a first
anneal (cq_grow1_209, cq_grow1_211, T0 0.008), both back at slack 0 with the record's labels. Jobs started before
08:47 Mac clock run on the slow cores (17 pct of a core: peer note msg-4ef1ad23dc from an agent, the queue
service gives fast cores only to jobs started after 08:47); on a fast core one anneal of 22,480,000 steps takes
about 18 minutes, so a 3300 s job does three.
NEXT: (1) read cq_grow*.txt with tick44.sh; a line above 0 is rebuilt from the explicit truth table before a word is
said; (2) k33cs goes back into the queue (avail was 7130 MB at 09:08 Mac clock); (3) write the K33-plus-extra-inputs
orbit structures for sym_search.py (9 cells plus 1 to 3 inputs fixed by the grid's group, coins on the crosses);
(4) groups on 16 to 20 inputs with under 20,000 classes. Loop job 49a7ba01 expires about 17 Nov 21:4x: re-create it.

ADDED 11 Nov 06:43 laptop clock (newest block; NEXT below replaces items (1)-(2) of the 06:20 NEXT line, (3)-(4) stand):
Pair scan at the record finished: all 4480 classes, best pair of class flips gives slack -0.000727753, so no single or
pair flip of the 18-input record improves it (sy_k33c.txt, line "flip2 pm+coins best pair among 4480"). coinq at
08:37 Mac clock: 52 files, no !!!; the nine runs from the record are still at slack 0 after 7 to 11 anneals each; best
start that is not the matching gate: zoo_lib line 34 (9 inputs) from -1.5105 to -0.004768.
New in coinq.py: --pad k adds k base inputs that the start function ignores (same G, J, slack), so the search can
grow the record's 9-input base to 10, 11 or 12 inputs; --pcube p is a move that writes one label on a subcube of
dimension 1 to 3 or copies a subcube from its mirror image. Tested on Mac mini 2: selftest worst diff 1.78e-15, the
padded record prints 6.521845710923, slack 0, G 6.776605309006, J 2.0390625 for pad 1, 2, 3. Queued 36 jobs
27_agent_cq_grow{1,2,3}_201..236 (pad 1-3, T0 0.0005/0.002/0.008, pools 1:6,2:6,3:4 and 1:10, pcube 0 and 0.25,
3300 s, mem 300 MB each); outputs cq_grow<pad>_<seed>.txt. The iteration count per anneal was sized from a 20 s test
(13.6 to 22.5 million); if a job's file shows no "# run 0 end" line after 20 minutes the rate under load is lower
than the test's and the jobs should be queued again with fewer iterations.
NEXT: (1) read cq_grow*.txt with tick44.sh (they match its cq_ pattern); a line above 0 is rebuilt from the explicit
truth table before a word is said; (2) check the first grow job reaches "# run 0 end" within 20 minutes.

ADDED 11 Nov 06:32 laptop clock (newest; the NEXT line is in the 06:20 block below):
coinq results at 08:26 Mac clock (34 files, no !!!): the nine runs from the record stay at the record (slack 0, nine
plain coins, no AND label taken up) after 3 to 6 anneals each; from the bare matching gate the search now reaches the
record itself (cq_k33_110, slack +0.000000000000, G 6.776605309006, J 2.0390625). A line with slack 0, G 0, J 1 in
cq_keep5_183_n7_116.txt is the one-bit function, not a result. coinq.py now penalises states with J below --jmin
(default 1.2), as fei_coin does; jobs that start after 08:3x Mac clock use it. Pair scan at the record: 3000 of
4480 classes, best pair still -0.000727753.

ADDED 11 Nov 06:20 laptop clock (newest):
First coinq results (Mac mini 2, 08:13 Mac clock, 13 files, all still running, no file contains !!!). From the bare
K33 matching gate (start slack -0.071099786): best -0.002307878 with eight plain coins and one double coin (G
6.774342186, J 2.039070278, mean -1/512), and -0.020969886 with nine double coins when the pool has no plain coin.
So an AND-of-two label in place of a plain coin costs about 0.002 per label at the record's shape; nothing above 0.
Library bases with 7 to 10 inputs: best -0.0126 (keep5 line 186, which is the matching gate itself), the others
-0.066 or worse. The nine runs from the record (cq_rec_101..109) and the zoo_lib bases had not started.
The line "-0.000000000" that a ranking of sy_k24c.txt shows is its degenerate start line (G -0.000000000 of a
constant function), not a result: k24c's best is -0.245967089. Rank sy_ files by their BEST line only.
Pair scan at the record: 2000 of 4480 classes, best pair still -0.000727753.
NEXT (this line replaces the 04:14 one): (1) read cq_*.txt (the loop in scratchpad tick44.sh; field 4 of a line is
the slack) and sy_*.txt BEST lines on Mac mini 2; anything above 0 is rebuilt from the explicit truth table before a
word is said; (2) when the pair scan at the record ends (grep "flip2 pm+coins" sy_k33c.txt), record its best pair;
(3) put k33cs back when avail is above 5000 MB (see the 06:05 block); (4) next families to write: labels that are
OR / XOR of two fresh bits and a label shared by the two ends of an edge with opposite signs; groups on 16 to 20
inputs with under 20,000 classes. Loop job 49a7ba01 expires about 17 Nov 21:4x: re-create it then. My usage window
ran out at 06:15 (resets 10:50 laptop clock), so ticks before then may do nothing; the Mac jobs keep running.

ADDED 11 Nov 06:05 laptop clock (newest; the 05:56 block below describes coinq.py):
The queue's aging rule (~/fillq/aging.sh: a job first in the queue for 30 min puts every other waiting job into
~/fillq/queue_hold until it starts, 45 min at most) had held my 297 waiting jobs, the 52 cq_ jobs among them,
behind my own 29_agent_sy_k33cs.job (mem_mb 2500), which could not start with 2.6 to 3.1 GB available. I moved
that job file to ~/fei_agent/parked/ at 08:02 Mac clock; the 297 jobs were back in the queue at 08:02:19 with
the cq_ jobs first. Put k33cs back (mv ~/fei_agent/parked/29_agent_sy_k33cs.job ~/fillq/queue/) only when
the status line (head -1 ~/fillq/status.txt) shows avail above 5000 MB. Mac mini 2 at 08:02: load 54 on 12 cores,
36 jobs running (13 mine, 22 of another session's n6_holding_search, and the film render), so each job gets about a
fifth of a core and results come slowly. Commit cbccb0c42d2461703f8cb94b33702ade23b0cd66 (coinq.py and the 05:56
block) is confirmed on origin main. Pair scan at the record: 1500 of 4480 classes, best pair still -0.000727753.

ADDED 11 Nov 05:56 laptop clock (newer than the 05:20 block below; the 04:14 NEXT line further down still holds):
New search code/coinq.py: every point of the base cube carries a label +1, -1, Y_j or -Y_j, where Y_j is the AND
of k_j fresh bits (k_j = 1 is a plain coin, the fei_coin family; k_j = 2, 3, 4 give labels of mean 1/2, 3/4, 7/8,
which no earlier search could express). Weights in closed form, one evaluation costs (coins + 1) 2^m; the built-in
self-test agrees with explicit truth tables on six random functions to 2e-15, and the record's label file gives
6.521845710923, slack 0. First run from the record (60 s, ten anneals, pool of 4 plain, 8 double, 4 triple coins):
nothing above slack 0. Queued on Mac mini 2 at 07:53 Mac clock, prefix 28 (ahead of the sy_ and co_ jobs), 52 jobs
28_agent_cq_<tag>_<seed>.job, mem_mb 250 (measured peak 32 MB at m = 9): nine from the record (three pools,
T0 .003 / .01 / .03, 3000 s), four from the bare matching gate, the rest on library bases with 7 to 10 inputs
(keep5.txt, zoo_lib.txt, 1500 s). Outputs cq_*.txt in ~/fei_agent; read with
grep -h "^BEST" cq_*.txt | sort -k5,5 -g -r | head (field 5 is the slack), and grep -l '!!!' cq_*.txt.
Other results at 05:54: no file contains !!!; ranking unchanged (k33c +0.000000000 = the record, k33v -0.049887206,
diac -0.098844446); the record's full pair scan is at 1000 of 4480 classes, best pair still -0.000727753.
Mac mini 1: none of my 175 jobs has started (load 21 from another session's work; left as is).

ADDED 11 Nov 05:20 laptop clock (this block is the newest one; the 04:14 NEXT line further down still holds):
Commit 2f32995c62fe is confirmed on origin main. Results at 05:11: ag23c -1.779, fanoc -1.402, c6c -0.143,
c7c -0.223, c8c -0.137, diac -0.099, k113c -0.152, dih14 -0.300, dih16 -0.184; no '!!!' in any file.
New in sym_search.py: struct k33cs (K33 with a coin per edge under S3 x S3 only, no swap of the two sides:
8240 classes, peak memory 1.56 GB measured, setup 67 s) and, for any struct on the nine K33 edges, the seeds
det2 / detR (3x3 determinant of the edge bits mod 2 / over the reals) and det2+coin / detR+coin (same coin rule
as the record). Test on Mac mini 2 (200 s): k33cs reproduces the record from the explicit table (pm+coins
+0.000000000, G 6.776605309, J 2.039062500); det2 -9.959, det2+coin -9.407, detR -8.168, detR+coin -7.689, so the
determinant is no start. Queued 29_agent_sy_k33cs.job (5400 s, mem_mb 2500): single flips and the top-150
pair scan at the record in the larger space, then annealing. 20 sy_ jobs wait behind seven running.
Mac mini 1 at 05:11: still 0 of 175 started, load 14.

ADDED 11 Nov 05:02 laptop clock (newest; the blocks below are older, the 04:14 NEXT line still holds):
Commit 03be6cee00b3 is confirmed on origin main. Small graphs with a coin per edge, results at 04:55: diac -0.109,
c6c -0.143, c7c -0.402, c8c -1.282 (anneals still running), agl13 -2.336, agl17 -2.258, dih12 -0.225 finished.
sym_search.py has point structures now (function point_struct): fanoc, fanoc2 (Fano plane, one or two coins a point;
fanoc2 needs --batch 16), ag23c (the nine points of AG(2,3) under the full affine group, a coin a point: 1060 classes,
a symmetric subspace of the k33c space), q3vc (cube vertices), w33c (S3 wr S3 on nine points), s9c, s10c (symmetric
group with a coin a point), pg23 (the thirteen points of PG(2,3), bare: 30 classes, exhaustive best -1.654889012).
All tested on Mac mini 2 for 12 s each and queued (29_agent_sy_<name>.job); 31 sy_ jobs wait. No '!!!' anywhere.
Mac mini 1 at 04:55: still 0 of 175 started, load 15.

ADDED 11 Nov 04:41 laptop clock (read this first, then the 04:27 and 04:14 blocks below; the 04:14 NEXT line still holds):
Commit ac8ea3268481 is confirmed on origin main (fetch rc 0, ancestry rc 0). sym_search.py has a new family: a small
graph with one coin per edge, group = the whole automorphism group found by brute force (c6c c7c c8c k23c k24c k33mc
w4c diac k113c). Tested on Mac mini 2 (diac: best -0.109; k23c: best -0.354 in 25 s; both paths agree) and queued there
as 29_agent_sy_<name>.job together with k5c (20 inputs, mem 2500 MB). 28 sy_ jobs wait in the queue. Results at
04:35: agl13 -2.336, agl17 -2.258, dih12 -0.225, dih14 -0.300, dih16 -0.184 (all still running), six coin searches
returned the record itself, no file contains '!!!'. Mac mini 1: still 0 of 175 started, load 21-23.
Note on NEXT item (4): an invariant AND / OR of coins is inside the k33c search space (every invariant function of
edges and coins), so the queued k33c anneal from the record covers it; fei_coin itself is unchanged.

ADDED 11 Nov 04:27 laptop clock (read this first, then the 04:14 block below, whose NEXT line still holds):
- The 04:14 state landed on GitHub as 1bae792ec76eae903f268fadbbc19a3cc4054c9b (read back from origin main, five files).
- sym_search.py has a new family: K3 / K4 with r interchangeable coins per edge (names k3c2..k3c5, k4c2; k4c2 and k3c5
  have 18 inputs). Queued on Mac mini 2: k4c2, k3c5, k3c4, k3c3, k3c2 (29_agent_sy_*). k4c3 is too large (about
  11,500 classes at 2^24 points); do not queue it there.
- Results so far (slack; all below 0): agl11 exhaustive over 2^29 functions -2.159; running: agl13 -2.336, agl17 -2.258,
  dih12 -0.225, dih14 -0.300, dih16 -0.807. Six coin searches finished: best is the record itself, slack 0.
- Mac mini 1: none of my 175 queued jobs has started (load 21, another session's jobs). Left as is.
- Mac mini 2 admits about five of my jobs at a time (the runner keeps cores for the film work); about 296 queued.

NEXT, NEWEST (written 11 Nov 04:14 laptop clock; the 03:20 block below is older) - FIVE-INPUT GATES AT EVERY BIAS CLOSED; SEARCH OVER ALL INVARIANT FUNCTIONS STARTED

Status: the conjecture is open; no new lower bound; the record 6.521845710923 stands.

Done since 03:20 (each number was reached two ways unless said otherwise):
- GitHub: the 03:20 state landed as 382f45465dcd4bb0514e3c1c50bd2d28a7b36341.
- Table round 9: W_run9 - W_run8 at most 0.000146 over the grid. The table is settled; the round loop is stopped.
  W_cur.txt = W_run9 on both Macs (results/tower/W_run9.txt here).
- Read-once formulas, my own Bellman iteration (code/ro_vi.py): the read-once constant lies between 6.454662323 and
  6.454667091 with AND/OR/NOT, and the same with XOR allowed. Agrees with the known 6.4548 and the store card
  claim_415d9ba1b7f745a2a442da84ef6836ef. Below the record: read-once gives nothing new.
- Every five-input gate at every bias (code/fei_gate5.c, all tables up to input order and complement, biases
  p = j/96 for j = 2..48, against W_run9; outputs g5_0..15.txt in ~/fei_agent on Mac mini 2): largest slack 4.9e-07,
  which is interpolation noise; the tables at slack 0 are the policy's own gates (dictator, AND/OR type). No
  five-input gate beats the settled table at any tested bias.
- code/sym_search.py: search over ALL functions invariant under a permutation group of the inputs (a sign per orbit of
  points; one evaluation costs the number of orbits K). Every reported state is re-scored from its explicit truth table.
  * Bare K33 (9 edge inputs, K = 26): all 2^25 invariant functions scored. The best is the perfect-matching function and
    its dual, slack -0.071099786 (G 6.490807250, J 2.006386067). Nothing on bare K33 reaches the record.
  * K33 edges + one coin per edge (18 inputs, K = 4480): the record is reproduced exactly (slack +0.000000000,
    G 6.776605309, J 2.039062500, both paths); the best single orbit flip gives -0.000335744 (the all-zero / all-one
    points). The record is a strict local maximum under single flips. The pair-flip line of the test run was cut off
    in my printout and has NOT been read; the queued k33c job runs the full pair scan and writes it to sy_k33c.txt.
  * Queued on Mac mini 2, prefix 29_agent_sy_: k5 (exhaustive, K = 34), k33c with the full pair scan, k4c, k33v,
    k6, k34, k44, pet, q3e, octa, agl11/13/17, pgl11/13/17, dih12/14/16. Outputs sy_<name>.txt; a line starting
    "!!! POSITIVE SLACK" is checked from the truth table before a word is said.
- Queue changes: I removed my queued cp_ jobs (coin searches at biased inputs) from both Macs so the co_ jobs start;
  only the cube ones had finished (best -0.038). They can be recreated with code/queue_coinp.sh. The two het runs on the
  old table W_run6 were stopped by me; het_c on W_cur is queued (40_agent_het_c.job).
- Coin searches finished so far on Mac mini 2 (6 files): best slack +0.000000000000, which is the record itself
  (G 6.776605309006, J 2.0390625). Nothing above it.

NEXT: (1) read sy_*.txt on Mac mini 2 (grep -E "^(exh0|seed|BEST|!!!|  flip2)" sy_*.txt); if k33c's pair scan finds no
improving pair, the record is a local maximum under pair flips too, and the next step in that space is annealing from the
record with the coin orbits only (already in the k33c job); (2) coin searches on bases with 12 to 16 inputs keep running
(co_ jobs on both Macs): grep -hv '^#' co_*.txt | sort -t' ' -k4,4 -g -r | head (field 4 is the slack); (3) new
structures for sym_search with two coins per edge or a coin per vertex pair (k4 with 2 coins per edge is 18 inputs),
and groups acting on 16 to 20 inputs with K under about 20,000 (memory: K^2 * 16 bytes); (4) labels that are AND / OR of
two coins in fei_coin (never done); (5) anything above slack 0 is checked from the explicit truth table before a word
is said. Not yet fetched: g5_*.txt. Loop job 49a7ba01 expires about 17 Nov 21:4x: re-create it then.

NEXT, NEWEST (written 11 Nov 03:20 laptop clock) - THE TABLE WITH NEGATIONS HAS SETTLED; THREE MORE NEGATIVE RESULTS

Still no new lower bound (6.521845710923 stands).
- ROUND 8 (Mac mini 2, 05:08 its clock): the screen against W_run7 found slack at most +0.0021 (record gate, p .381);
  W_run8 - W_run7 is at most 0.00115 (at p .378): .25 6.992328, 11/32 6.688385, 12/32 6.610820, 13/32 6.569524,
  14/32 6.542416, 15/32 6.526872, .4824 6.523437, .498 6.521868, 1/2 6.521845711 unchanged. The table with negated
  inputs has settled. Rounds 9 and 10 still run (pid 99709, neg_loop.sh); read them only to confirm.
- FIVE-INPUT ENTRY GATES, EXHAUSTIVE (code/fei_entry5.c, all 2^32 tables against W_run7, Mac mini 1, e5_0..15.txt):
  no positive slack. Best per output bias k/32: 8: -0.118662 (0000aaaa), 10: -0.076419 (0000aaee), 11: -0.069734
  (0000aafe and its 13 relatives, G 2.728404620 J 1.454545455), 12: -0.080718 (0000eeee), 15: -0.095730, 16:
  -0.260923 (00aaeeee). The Mac mini 1 queue admitted nothing for 25 minutes (its gate reads the load average), so
  the scan was run directly: two processes at nice 19, about one minute.
- BIASED COINS (code/coin_bias.py, Mac mini 2): the record gate with uniform main inputs and every coin replaced by
  a small function of bias q. Phi(f) = U_F(1/2..; q..) + sum_j Inf_j Phi(h_j). U alone: +0.000012 at q .45/.55,
  -0.00038 at .40, -0.0067 at .25 (symmetric in q -> 1-q); best Phi of a function of at most 4 inputs by bias:
  7/16 -0.1496 (007f), 6/16 -0.1690 (030f), 5/16 -0.3314, 4/16 -0.5890 (AND2). Totals Phi(f) + D(p_f): 7/16 -0.0052,
  6/16 -0.0063, 5/16 -0.0127, 4/16 -0.0219; mixed patterns q / 1-q no better. The gain is second order and tiny,
  the cost first order. Dead.
- WHY the table says it all: for f = F(h,..,h) with h of bias q, Phi(f) + D(p_f) = [U_F - J_F D(q) + D(p_f)] +
  J_F (Phi(h) + D(q)); the first bracket is <= 0 by the Bellman table, the second is the entry shortfall of h.
  So only two levers exist: gates that raise W at a bias q, and entry functions h with Phi(h) + D(q) nearer 0.
  Entries near the record pay about 3.8 |q - 1/2| against D about 5.5 (q - 1/2)^2.
- Also note C* = sup over balanced g of H(g)/(I(g) - 1) exactly (g = y f for a fresh bit y is balanced with
  H(g)/(I(g) - 1) = H(f)/I(f)), so the G/(J - 1) frame loses nothing.
- Finished coin searches at biased p on the cube base (cp_cube_*, against W_run6): best slack -0.038 (p 11/32),
  elsewhere -0.08 to -0.24. Nothing gains there.
- NEXT: (1) the coin searches on bases with 12 to 16 inputs (co_ jobs, 43 on Mac mini 2 with seeds 5001.., and the
  library pass) are the open lever at p = 1/2: move them ahead of the cp_ jobs in both queues and read
  `grep -v '^#' co_*.txt | sort -t' ' -k4,4 -g -r | head`; (2) labels that are AND / OR of two coins and coins
  shared by a 2-face in fei_coin (never done); (3) new bases outside the zoo: per(4x4) > 0, matchings of K6, det
  over GF(2), with coins; (4) anything above slack 0 is checked from the explicit truth table before a word is said.
- GitHub: the 02:58 push was refused (this file "would lose 1 line that origin has": my own rewrite of the top
  block); sent again at 03:2x with ALLOW_REMOVALS=1 together with coin_bias.py, W_run8.txt, keep8.txt(.coin).

EARLIER (written 11 Nov 02:35 laptop clock) - NEGATED INPUTS: THE TABLE W_run6 IS TOO LOW AROUND 1/2

Still no new lower bound (6.521845710923 stands). What changed: a tower may feed a gate the state g or its negation
(same G and J, bias p or 1 - p). For a gate F that is F(x xor mask) at the homogeneous bias p. No library above four
inputs ever held such variants, and they beat W_run6 almost everywhere near 1/2.
- The record gate with every input at bias 1/2 + e: U = G_p - c J_p + c = -38.7 e^2 (even in e, no linear term), and
  p' - 1/2 = 2.039 e, the bias runs away (code/rec_lambda.py). That gave the table its downward cusp at 1/2
  (W - c about -1.6 |e|).
- The record gate with main inputs 0, 2, 3, 6 and all nine coins negated (mask 101100100111111111, input i = character
  i): U = +10.25 e^2 at e = 0.01, +10.79 e^2 at 0.001 (Hessian value 11.02), +0.0250 at e = 0.05, +0.0997 at e = 0.1,
  and p' - 1/2 = 0.19 e, the bias contracts. Two computations agree to the printed digits: the coin decomposition
  with one bias per input (code/rec_hess.py) and the explicit 2^18 truth table (code/neg_check.py). So the true value
  satisfies W(1/2 + e) >= c + 5.5 e^2 near 1/2: a minimum at 1/2, not a cusp peak.
- Screen of every input negation against W_run6 on 121 biases (code/neg_screen.py; keep5 gates with at most 10
  inputs, and the record gate with all 512 x 512 main and coin patterns): 397 distinct variants with positive slack,
  the largest +0.0896 at p = 0.560 (record gate, main mask 27, all coins negated); explicit gates gain too (a
  nine-input keep5 gate +0.0336 at 0.560, a seven-input one +0.0238 at 0.816).
- What a new bound needs is unchanged: an entry gate on uniform bits with G - c J + W(p') > 0. Shortfalls against
  W_run6 were -0.0107 (K33 + 8 coins, p' = .498), -0.0946 (bare K33, p' = .4824), -0.103 (a8a8a888, p' = 11/32).
  Every rise of the table at those biases is worth the same amount of slack.
ROUND 7 DONE 04:46 Mac clock (results/tower/W_run7.txt, keep7.txt, keep7.txt.coin; 60 negated variants added, top 3
  per bias of the screen; neg1_all.* on Mac mini 2 hold all 3260): W(1/2) = 6.521845711 unchanged, rollout value
  6.521845711, and 1/2 is now the minimum of the table. W7 (rise over W6): .25 6.992170 (+.0131), .30 6.815459,
  11/32 6.688182 (+.0334), .40 6.575784, .45 6.534783 (+.0483), .4824 6.523435 (+.0235), .49 6.522362,
  .498 6.521868 (+.0032), .56 6.540603 (+.0497), .90 8.125792. Largest rise +0.0508 at p = .4422.
  Entry shortfalls against W7: K33 + 8 coins -0.0075, bare K33 -0.0711, a8a8a888 -0.0696, AND2 (p' = 1/4) -0.1187.
RUNNING on Mac mini 2 since 04:50 its clock: pid 99709 `bash neg_loop.sh 8 10` (code/neg_loop.sh): three more rounds
  of screen + value iteration, about 16 minutes each; logs neg<r>.log, vi_run<r>.txt; each round refreshes W_cur.txt.
  My queued co_ and cp_ jobs on both Macs now read W_cur.txt (230 and 179 job files rewritten; Mac mini 1's W_cur.txt
  is W_run7 and must be copied again by hand after each round, it has no numpy).
QUEUED on Mac mini 1 at 04:51 its clock: 16 jobs 29_agent_e5_<i> (code/fei_entry5.c, about 3 minutes each):
  every function of five uniform inputs as an entry gate against W_e5.txt (= W_run7), outputs e5_<i>.txt with the
  best slack per output bias and the 40 best tables. Read with
  `cat e5_*.txt | grep "^bias" | sort -k2,2 -k7,7gr | awk '!s[$2]++'` (best per bias) and `grep -h "^top" | sort -k2gr`.
  First 1/4096 of the tables already gives, per output bias k/32: 8: -0.1187 (AND2 type), 10: -0.0764, 11: -0.0697
  (the a8a8a888 class), 12: -0.0807, 15: -0.0957, 16: -0.544. A new bound needs one of these above zero; the table at
  p' = 10/32 .. 12/32 has to rise by about 0.07 more, or a larger entry gate has to do better (the co_ jobs search
  those against W_cur.txt).
WHY NEAR 1/2 CANNOT WORK (second-order argument, record gate only): with e = bias - 1/2, Phi = G - c(J - 1) of a state
  and Psi = Phi + a e^2, one record-gate step with any signs, some inputs left at exact 1/2, gives
  Psi' <= sum_i Inf_i Psi_i for every a between about 5.5 and 18.2 (the matrix Q/2 + a Inf Inf' - a diag(Inf) is
  negative semidefinite there; Q from code/rec_hess.py, saved as rec18.lab.Q.npy on Mac mini 2). An entry needs
  Phi + 5.5 e^2 > 0, entries near the record have Phi about -0.0077 at e = .002, so the gain must come from entries
  far from 1/2 (biases .30 to .40), where the table still moves.
GitHub: merge commit 2421f4b0572b84f1925f843b10d036c112ce8bd5 holds this file as of 02:35 and the code up to
  neg_screen.py; a push of this file, neg_loop.sh, fei_entry5.c, results/tower/W_run7.txt, keep7.txt, keep7.txt.coin
  was started at 02:58 (background job; its log is %TEMP%/fei_push4.txt).
THE LOOP NOW: (1) read vi_run7.txt: W at .498, .4824, 11/32, the rollout value; (2) screen again against W_run7
  (`python3 neg_screen.py W_run7.txt neg2 --lib keep7.txt --coin rec18.lab --coin keep7.txt.coin --topk 3`), value
  iteration again with --init W_run7.txt, until the table stops moving; (3) search entry gates on uniform bits against
  the new table (queue_coin.sh with the new W; add `nice -n 10` to its mk first) and biased gates with fei_coinp
  started from negated variants (init lab:FILE:LINE); (4) anything that lifts W(1/2) or the rollout above
  6.521845711 is checked by explicit truth tables and an explicit rollout before a word is said. Linear interpolation
  of a convex table overestimates by about 1e-6 near 1/2, so a rise of that size on the grid is not a result.
Stopped (mine): co_k33_807 on Mac mini 2 (it returned the record in every run), and the first oversized value
  iteration pid 93286.

EARLIER (written 11 Nov 02:11 laptop clock) - COIN GATES AT BIASED INPUTS BEAT THE TABLE AWAY FROM 1/2
- STILL NO NEW LOWER BOUND.  What is new: at input bias p = 0.55 the nine-edge matching gate with nine coins
  (all 18 inputs of bias 0.55) has value 6.490833518 against the table's W(0.55) = 6.486504744, slack
  +0.008873596, p' = 0.59769; the explicit 18-input truth table gives the same numbers (code/coinp_check.py).
  So the table W_run6 can be raised at biased p by coin gates.  A new bound needs the gain to reach p = 1/2 through
  an entry gate (the five-input entry needs W(11/32) up by 0.103; the bare matching gate needs W(0.4824) up by 0.095).
- code/fei_coinp.c = fei_coin at input bias p (usage: fei_coinp p m k seconds seed outfile wfile init [iters] [T0]
  [T1] [jmin] [qbal] [pedge]; slack = G - W(p) J + W(p'); at p = 1/2 it returns the record, slack 0, checked).
  code/coinp_check.py re-evaluates from the explicit truth table.  code/tower_vi2.py = tower_vi.py that also takes
  coin gates (--coinfile, lines "m k labels") and rolls the policy out with exact quantities; --keep writes
  KEEP.txt and KEEP.txt.coin.  code/make_hot.py + code/queue_coinp.sh (modes hot, lib) queue the searches.
- QUEUED 04:10 Mac clock on BOTH Macs: 30 jobs 30_agent_cp_<tag>_{lo,hi}_<seed> (seeds 7001.. on Mac mini 2,
  7501.. on Mac mini 1): bases k33, k33 padded by 1 and 2 idle inputs, pmk4 padded 2/3/4, cube, octa, entry5 padded
  3/5, nor2 and nand2 padded 6/8, and the record's labels; biases lo = .30 .34375 .381966 .42 .45 .47 .49,
  hi = .51 .53 .55 .58 .618034 .65625 .70; 24 coins; output one file per bias cp_<tag>_p<bias>_<seed>.txt.
  They sit ahead of the uniform co_ jobs.  New waiting jobs on the Macs start with `nice -n 10` (peer
  an agent measured the film render 10% slower; all my waiting Mac mini 2 jobs were rewritten that way).
- LOOP TO RUN: (1) read `grep -v '^#' cp_*.txt | sort -t' ' -k4,4 -g -r` per file (best slack > 0 is a gain at that
  bias); (2) put the best line of every gaining file into a coin file ("m 24 labels"), run
  `python3 tower_vi2.py --nobase --grid 9601 --span 24 --sweeps 4000 --libfile keep5.txt --libfile rec18.txt
  --coinfile COINS.txt --dump W_run7.txt --keep keep7.txt` on Mac mini 2; (3) if W(1/2) or the rollout value rises
  above 6.521845711: stop and verify (explicit truth tables, second transform in high precision); otherwise requeue
  the biased and the uniform searches against W_run7.txt (third argument of queue_coinp.sh; queue_coin.sh has W
  inside) and repeat.  A first test of step (2) with the one gate above runs on Mac mini 2 as pid 84660
  (vi_t0.txt, W_t0.txt).
- Then `bash queue_coinp.sh lib SEED0` (every keep5/zoo gate with 7..13 inputs at the 14 biases, 286 jobs named
  31_agent_cl_*, ahead of the co_ jobs) once the hot pass shows which biases gain.
- GitHub: commit b4a41b9dd031a1d6fd80378024aa2140dafc1d23 holds the coin code, rec18.lab, the memory body and this
  file as of 01:42.

OLDER (written 11 Nov 01:42 laptop clock) - THE RECORD IS AFFINE IN ITS COINS; COIN SEARCH QUEUED ON BOTH MACS
- Anatomy of the record (code/rec_anatomy.py, code/rec_coins.py on results/rec18.txt): nine inputs of influence
  57/256 (the edges of K33) and nine coins of influence 1/256.  With all coins 0 it is the matching function (247
  ones, six minterms).  Coin e adds one minterm: the four edges that share a vertex with e (two settings of x: with
  and without e itself); nothing else depends on a coin.  No pair of inputs is a module, so it is not a read-once
  tree and het_search can only use it as a ready gate.
- So g(x, y) = a(x) + sum_j b_j(x) Y_j with every x labelled +1, -1, Y_j or -Y_j.  The spectrum is the union of
  the spectra of a and the b_j: one evaluation costs (k+1) 2^m, any m <= 16 and k <= 38 coins (up to 54 inputs).
  code/fei_coin.c anneals over the labels (boundary moves, paired moves that keep the mean), objective slack =
  G - cJ + W(p') on W_run6.txt; code/coin_check.py re-evaluates a line from the explicit truth table.  Both give
  the record 6.521845710923, slack 0, from results/seeds/rec18.lab (difference 2.4e-14).
- First test (Mac mini 2, 94 runs, T0 2e-3): no state above slack 0 from the record.
- QUEUED 03:37-03:40 Mac clock.  Mac mini 2: 31_agent_co_rec_801..806 (record, T0 .005/.02/.05, 24 coins,
  1 h each), co_k33_807/808 (bare matching gate), 143 jobs co_<lib>_<line>_n<n>_<seed> (every keep5.txt and
  zoo_lib.txt gate with 6..13 inputs as base, T0 .01).  Mac mini 1: the same with seeds 901.. and the library
  pass at T0 .03 (seeds 3001..).  Outputs co_*.txt in ~/fei_agent.
  READ: `grep -v '^#' co_*.txt | sort -t' ' -k4,4 -g -r | head` (field 4 = slack; run -1 is the start state), then
  `python3 coin_check.py W_run6.txt <file>` on Mac mini 2 (numpy) for anything with slack > 0.
- First coin result (co_k33_807, 03:45 Mac clock, 5 runs): from the bare matching gate (slack -0.0946) the search
  reaches slack -0.0107 with 8 coins, mean 1/256.  The start line of each file is run -1.
- EDGE MOVES (03:48 Mac clock): fei_coin got a move that gives both ends of a cube edge one coin label.  With it
  the search goes from the bare matching gate to the record itself (slack 0, same G and J) in every run, about 3 s
  each, on both Macs; nothing above 0 at m = 9.  The new binary is in place on both Macs (built as fei_coin.new,
  then renamed, so running jobs kept theirs); all waiting co_ jobs use it.  Mac mini 2 also has 43 jobs on the
  14..16-input bases (queue_coin.sh big, seeds 5001.., 1 h each): 201 co_ jobs waiting there, 151 on Mac mini 1.
  The 01:46 push was refused (fei_coin.c changed during it); sent again as a background job, output
  $TEMP/push3.out.
- NEXT IDEAS if single coins saturate: labels that are AND / OR of two coins (a(x) = +-1/2), coins shared by a
  2-dimensional face, and feeding the best coin gates to het_search as library lines (coin_check.py --emit).
- GitHub: commit 3701197a1b00e0f472551777ca27a2fa8ca982b0 holds the fine table, keep5, the n = 7 merge and
  het_search.  The coin code, this file, read_bell.py, the memory body and rec18.lab went out at 01:46 laptop clock
  as background job beoorhfsl (output $TEMP/push2.out).  Brain memory filed 01:44:
  fei_towers_drifting_and_unequal_bias_do_not_beat_6_5218_2026_11_11 (provisional).
- On Mac mini 1 the first number in a fillq .pid file is the RUNNER's pid (23533), not the job's: never kill by it.
- het_a and het_b started 03:27 Mac clock on Mac mini 2 (all slack <= 0 through round 4 / round 2); the three
  bw_k10 jobs ended by themselves.
- Mac mini 1's waiting bw jobs were switched to W_run6.txt on 11 Nov; its running bw_k11_half_405 still uses the
  coarse table and is a near-dictator (useless).

OLDER (written 11 Nov 01:16 laptop clock) - UNEQUAL-BIAS COMPOSITIONS QUEUED; FINE TABLE IN USE; n = 7 SENT
- The record 6.521845711 is the PUBLISHED lower bound (PM(K33) with nine coins; main loop's store card
  claim_dc791b32), not ours; Hod's is 6.4548.  A gate or tree with positive slack would be a new lower bound, not a
  proof of the conjecture.
- results/tower/W_run6.txt (9601-point grid, from Mac mini 2) resolves the cusp: W(1/2) = 6.521845710923, W at
  log-odds +-0.005 = 6.520454674, +-0.010 = 6.519087861.  Every waiting bw_/bs_ job on Mac mini 2 was switched to it
  (41 job files), the nine p = 1/2 seeded jobs were released, and two record-seeded jobs added
  (33_agent_bs_rec18_k18_phalf_601/602).  Mac mini 1's 35_ bw jobs still use W_run2.txt (fine away from 1/2;
  distrust a k = 9/11/13 "half" value there unless its mean is exactly 0).
- n = 7 monotone census v4 merged (results/merged7_v4.txt, weighted count 2,414,682,040,998 = Dedekind): overall sup
  sum_i E_i / I = 3.164564560463, balanced 1.901840492556, |mean| <= 1/8 2.222283760112, balanced max min E/Inf
  1.778965422289.  Sent to an agent (msg-88e09c2ba3); it recomputed the four leaders with its own code and
  agrees to 5e-13.  Nothing more owed there.
- NEW LINE: gates whose inputs are DIFFERENT functions.  For independent inputs g_j of biases p_j,
  G(F(g)) = G_pvec(F) + sum_j J^(j) G(g_j), J(F(g)) = sum_j J^(j) J(g_j) (checked against explicit truth tables to
  4e-15, code/het_test.py).  Potential U(g) = G - cJ, slack(g) = U(g) + W(p_g); slack > 0 is a new bound; a bit and
  the record gate have slack 0.  code/het_search.py keeps, per bias bin, the explicit tree with the largest U and
  grows it by AND/XOR of all pairs and by coordinate ascent over which menu entry feeds each input of each library
  gate.  First test (149 gates of <= 5 inputs, 3 rounds): every slack <= 0, the largest away from the bit
  -0.0345 at p = 0.5013.
  QUEUED on Mac mini 2: 32_agent_het_{a,b,c,d} (a: keep5 + zoo gates to 12 inputs, 40 rounds; b: all 16181
  six-input monotone classes; c: gates to 18 inputs incl. the record; d: 3600 bins, span 12).  Outputs
  ~/fei_agent/het_<x>.log (one line a round, "!!! POSITIVE SLACK" plus the tree if any), het_<x>.menu.
  READ: `tail -2 het_?.log | cut -c1-300`.  A positive slack is believed only after the tree is expanded to an
  explicit truth table (or its G, J recomputed in high precision) and the tower above it rolled out.
- code/het_record.py (the record gate with two input classes on a 601-point table) was stopped unfinished on the
  laptop; het job c covers it.

OLDER (written 11 Nov 00:31 laptop clock) - STRUCTURED GATES DO NOT HELP; SEEDED SEARCHES QUEUED
Since the block below (all numbers against results/tower/W_run2.txt, record 6.521846):
- 211 structured functions of the main campaign (FEIB11 families.json, 7-18 inputs; code/gen_famlib.py ->
  results/tower/fam.txt + .names) added as gates: value iteration run 4 gives the same W(1/2) = 6.521845711, rollout =
  the record gate for ever.  No gain.
- 153 more structured monotone gates (code/zoo.py: bipartite and graph matchings, connectivity, triangles, Hamilton
  cycles, cube/octahedron/Petersen/prism/wheel matchings, Hex, Y, bond crossing, Fano/AG(2,3)/PG(2,3) lines, all
  thresholds on 7-15 inputs) scored at 101 biases: every Bellman excess B_F(p) - W(p) is NEGATIVE
  (results/zoo/zoo_run1.txt).  Closest: pm_K4 -0.0066 (p .58), match_K3,3 -0.018 (p .55), pm_cube -0.021 (p .57),
  match_K4,4 -0.021 (p .45), pm_wheel5 -0.044, pm_octa -0.051.  At p = 1/2 the best is match_K3,3 (the record's
  nine-edge core): B = 6.4747 with p' = 0.4824.  So the matching gates are the right cores and the record's "coins"
  are worth about +0.047 on top of the core.
- What a new bound needs, in one line: a gate F on uniform bits with G(F) + W(p') > 6.5218 J(F).  Shortfalls J(B - c):
  five-input entry gate a8a8a888 (p' = 11/32) -0.103; match_K3,3 (p' = .4824) -0.095; the record 0 by definition.
- W near 1/2 is a cusp: with the record gate, W(1/2 + e) = 6.5218 - O(e log 1/e) (the bias drifts by the factor I per
  level and the discount is 1/J = 1/I at 1/2).  The 601-point table interpolates linearly across it, so a search at
  p = 1/2 that lands near but not at 1/2 is flattered.  FIX IN FLIGHT on Mac mini 2 (vi_chain.sh): run 5 = all
  libraries + --keep keep5.txt (gates in the top 3 somewhere), run 6 = keep5 + record on a 9601-point grid ->
  W_run6.txt.  Use W_run6.txt for every search at p = 1/2.
- code/fei_bias.c now takes a seed file (argv[20], "n0 hex"; every run starts from that gate on the low inputs, the
  other inputs free), k <= 18, and its monotone move walks from a random point to the boundary (the old 8192 random
  tries found no legal move on the 18-input record).  Controls on Mac mini 2: k = 6 unseeded 6.454623321607; the
  record seed scores 6.521845710923; match_K3,3 seed with 3 free inputs at p = .55 runs 3000 moves a run.
- QUEUED on Mac mini 2 (code/queue_batch4.sh, seeds results/seeds/ = ~/fei_agent/seed_*.txt): 20 jobs
  33_agent_bs_<seed>_k<k>_p<tag>_<n> at biased p (k33 at .55/.45, cube .57, octa .46, k44 .45, pmk4 .58, nor2 at
  the golden bias, nand2 at its complement, entry5 at 11/32), outputs bs_*.txt.  Nine p = 1/2 jobs wait in
  ~/fei_agent/hold_half/ and seed_rec18.hold is not yet named seed_rec18.txt: when W_run6.txt exists, delete
  hold_half, `mv seed_rec18.hold seed_rec18.txt`, and rerun `bash queue_batch4.sh W_run6.txt 600` after deleting its
  non-half lines (or queue only the half ones by hand).
- QUEUED on Mac mini 1 (fei_bias built there, W_run2.txt): 12 jobs 35_agent_bw_k{9,11,13}_{half,entry,gold,goldc}
  _4xx, behind a 229-job queue.  Mac mini 1 has no numpy: value iteration runs only on Mac mini 2.
- Mac mini 2 at 00:28: I stopped my own ten ms_n8/n10 searches (converged on the known read-once leaders; they show as
  rc=143 in fillq/failed) to free cores; the six census parts 30_agent_mono7v4_p0..p5 and the first bw jobs
  started at once.  The n = 7 balanced slice owed to an agent comes from out7v4_0..5.txt (see below).
READ NEXT: bw_k*.txt and bs_*.txt (column 3 = Bellman value; compare with W(p) of the table the job used: W(.5) 6.521846,
W(.34375) 6.655472, W(golden) 6.576709, W(.55), W(.45), W(.57), W(.46), W(.58) from W_run2.txt by interpolation).
Anything above its W(p): recompute with bias_check.biased, add to a library file, rerun the value iteration, and
believe only an explicit rollout above 6.5218 that survives a second transform in high precision.

NEXT (written 11 Nov 00:05 laptop clock) - THE LOWER-BOUND LINE: TOWERS WITH DRIFTING BIAS
What it is. For a Boolean g on uniform bits put p = Pr[g = -1], G(g) = entropy of the spectrum off the constant,
normalised by the variance, J(g) = I(g)/Var(g).  Then H(g)/I(g) >= G(g)/J(g), and composing a gate F with independent
copies of g gives  p' = Pr_p[F = -1],  G' = G_p(F) + J_p(F) G,  J' = J_p(F) J  (p-biased Fourier quantities of F).
CHECKED numerically against explicit truth tables to 4e-15 (code/bias_check.py --law).  So every tower of gates gives
a lower bound on the FEI constant, and the best tower from bias p solves W(p) = max_F [G_p(F) + W(p')]/J_p(F).  The
balanced score H/(I-1) is the special case "stay at p = 1/2 for ever".
Measured (code/tower_vi.py, Mac mini 2, results/tower/):
  gates on <= 5 inputs (all functions on <= 4, monotone on 5):        W(1/2) = 6.4512, rollout 6.450935
  + all 16,181 classes of monotone gates on 6 inputs (code/gen_lib6.py): W(1/2) = 6.4514 (no gain from 6 inputs)
  + the 18-variable record gate (results/rec18.txt, H/(I-1) = 6.521845710923 recomputed): W(1/2) = 6.521845711,
    policy = the record gate for ever.  So NO NEW LOWER BOUND YET.
  The small-gate optimum is the 2-input NOR/NAND tree at the golden-ratio bias (p = 0.381966 or 0.618034), where
  W = 6.5767 > 6.5218; what it loses is the entry from one uniform bit (best entry: a gate to p = 11/32 with
  G = 2.728405, J = 1.454545; W(11/32) = 6.6555 and (2.728405 + 6.6555)/1.454545 = 6.4514).  To beat 6.5218 through
  that entry W(11/32) must reach 6.758, i.e. the biased regime needs gates about 0.10 better than 2-input ones, or a
  cheaper entry gate.  The main campaign's read-once bound 6.4573 is the same regime (a NOR tree is read-once).
Queued to find such gates (Mac mini 2, code/queue_batch3.sh, 16 jobs 35_agent_bw_k{8,10,12,14}_{half,entry,
gold,goldc}_<seed>.job, 1 h each, program code/fei_bias.c in Bellman mode with W table ~/fei_agent/W_run2.txt):
each maximises (G_p(F) + W(p'))/J_p(F) over monotone F on k inputs at p = 0.5, 0.34375, 0.381966, 0.618034.
READ THEM: scp ~/fei_agent/bw_k*.txt into results/bw/, sort by column 3.  A value above the table's
W(0.5) = 6.521846, W(0.34375) = 6.655472, W(0.381966) = W(0.618034) = 6.576709 is an improving gate: recompute it
with bias_check.biased, append "k hex" to a library file, rerun `python3 tower_vi.py --grid 601 --span 24 --libfile
lib6.txt --libfile rec18.txt --libfile NEW.txt --dump W_run4.txt`, and if W(1/2) or the rollout passes 6.5218,
verify the rollout with high-precision arithmetic and a second transform BEFORE saying anything.  Validation done:
Bellman mode at k = 6 returns 6.454623 at p = 1/2 (= (3.966917 + 6.521846)/1.625, the census leader) and 6.576564 at
the golden bias.  Fixed-point mode of fei_bias (exact dyadic mass, monotone) found only dictators at p = 1/4 and 1/8:
the mass equation is 3-adic and the walk rarely lands on it; the drifting-bias formulation makes it unnecessary.
The grid (log-odds step 0.08) is coarse near p = 1/2, where W has a cusp at the record gate; refine there (keep the
few hundred useful gates, grid 4801) before trusting any "entry" comparison at p = 1/2.
Pushed: d2e830baa266946df42723ccd8d3a8cbe9962d28 (10 Nov 23:43, fei_search.c and batch 2) and
5131d3834afd847b1d0732ca33df80dc5597c859 (11 Nov 00:10, everything in this block).  Told an agent (topic
fei-fronts, key towers-20261111) and answered an agent (fei-p5: nothing of mine overlaps its paper).
MAC MINI 2 IS SATURATED (load 17-20 on 12 cores, other agents' film work): fillq admits a job only when cores are
free, and its ageing rule moved 59 of my jobs to ~/fillq/queue_hold until the head job (30_agent_mono7v4_p0)
starts; they come back by themselves in name order (30 census, 35 bw, 40, 45, 50).  My ten 40_ searches started
00:54-01:01 MAC clock and end 02:54-03:01 MAC clock (00:54-01:01 laptop clock).

NEXT (written 10 Nov 23:33 laptop clock; the Mac clocks run 2 h ahead):
(a) About 01:15 laptop clock the six census parts ~/fei_agent/out7v4_0..5.txt on Mac mini 2 should exist (they wait
    behind ten 2 h searches that end 00:52). Then: scp into results/v4n7/, `cd code && python -X utf8 merge_census.py
    ../results/v4n7 out7v4_ 3 > ../results/merged7_v4.txt`, check weighted sum 2,414,682,040,998, and send
    an agent (mesh topic fei-fronts) the n = 7 values of balQ0, nbQ0, balMinE with the leaders' hex. That is the
    only thing owed to a peer.
(b) Batch 2 on Mac mini 2 (queued about 23:25, runs after the 40_ and 45_ jobs, about 03:00-09:00 laptop clock): 26 jobs
    ~/fillq/queue/50_agent_fs_n<n>_o<obj>_<m|g>_<seed>.job from code/queue_batch2.sh, program code/fei_search.c
    (table-free, n <= 14, objective 4 = H/(I-1) on balanced functions), outputs ~/fei_agent/fs_n*_o*_*.txt:
    objective 4 monotone n = 8..14 (two seeds each), objective 4 general n = 7..10, objective 0 monotone n = 11..13,
    objective 2 monotone n = 11, 12. Read with scp into results/fs/ and `python -X utf8 check_search.py
    ../results/fs/fs_*.txt --top 1`. THE POINT of objective 4: a balanced function with H/(I-1) above 6.5218 would raise
    the known lower bound on the FEI constant (the record is the 18-variable PM(K33) host with nine coins). Any such
    value is recomputed with merge_census.stats and a third way before a word is said about it.
(c) Read the first batch when done (ms_n9_*, ms_n8_o2_*, gs_n9/10 on mini 2; gs_n6/7/8 on mini 1, long queue):
    do NOT scp into results/ms while a push of that folder is in flight (the 23:1x push was refused for that).
(d) Refill mini 2 from what (b) shows; an agent wants about three days queued there.
(e) Checklist T-20261110-114 note after (a). Loop cron 49a7ba01 expires about 17 Nov 21:4x: re-create it then.
Pushed so far: 2a9b391eff69, 89283c5f81ed, a1c76972e7ea1c523b7a8353c0aa79194e75b5db (10 Nov 23:3x: full n = 7
statistics, n = 6 balanced slice, search code, first search files). Not yet pushed: code/fei_search.c,
code/validate_search.sh, code/queue_batch2.sh, the check_search.py edit, this file.
Search results read at 23:15 (first 20 minutes of the 2 h jobs; each leader recomputed, monotone checked):
  n = 8  min_i E_i/Inf_i >= 3.304701322452   (x0 x7 OR x1 x4) AND (x2 x6 OR x3 x5)                 read-once
  n = 10 min_i E_i/Inf_i >= 3.401069972510   (x0 x1 OR x2 x6) AND (x3 OR x7) AND (x4 x8 OR x5 x9)  read-once
  n = 10 sum_i E_i / I   >= 3.433874258511   (x0 x5 OR x2 x6) AND (x1 OR x9) AND (x3 OR x8) AND (x4 OR x7)  read-once
  The exhaustive leaders are not read-once: n = 6 (2.944495) is Maj_3(x0 x1, x2 x3, x4 x5); n = 7 (2.954684) is the
  CNF (x2+x3+x4+x5)(x0+x1+x2+x3+x6)(x0+x1+x4+x5+x6). Read-once leaves are bounded by pi/ln 2 = 4.5324 (FEIB31,
  proved), so nothing at n <= 10 goes beyond what the main campaign has. Sent to an agent (msg-40688030e9).
  fei_search validation (Mac mini 2, code/validate_search.sh): n = 6 objective 4 gives 6.347067498702 in monotone and
  in general mode (the census value); n = 7 objective 0 gives 2.954683814183.
Refereed by a peer: an agent recomputed the n = 6 and n = 7 census leaders with its own transform
(../fei_solve_2026_11_09/audit_agent/N7_CENSUS_REFEREE_2026_11_10.md); maximality rests on my enumeration.

OLDER NEXT TEXT (superseded by the block above; kept for the job names). FIRST (owed to an agent, its ask 10 Nov 21:06Z): the n = 7 census v4 (adds balQ0, nbQ0, balMinE) is
queued on Mac mini 2, ~/fillq/queue/30_agent_mono7v4_p0..5.job -> ~/fei_agent/out7v4_0..5.txt (about 25 min a
part once admitted). When all six exist: scp into results/v4n7/, `cd code && python -X utf8 merge_census.py
../results/v4n7 out7v4_ 3 > ../results/merged7_v4.txt`, check the weighted sum, send it sup Q0 over balanced, over
|fhat(0)| <= 1/8 and over all, and balanced max min E/Inf, with the leaders' hex (n = 6 already sent: 1.784287864955,
2.012892400868, 3.030964070213, 1.598835983108; results/merged6_v4.txt).
ALSO RUNNING: general-function annealing (gen_search = mono_search.c with last argument 1): Mac mini 1
(a worker machine) ~/fillq/queue/45_agent_gs_n{6,7,8}_o{0,2}.job -> ~/fei_agent/gs_n*_o*.txt
(its queue held 249 jobs, so these may wait hours); Mac mini 2 45_agent_gs_n{9,10}_o{0,2}.job. Read them with
check_search.py as below (monotone=False is expected there). Validation so far: general mode at n = 5 gives
min_i E_i/Inf_i >= 2.695887520153 on every run (compare with the n = 5 NPN census of the main loop before quoting).
(1) F4 search is running on Mac mini 2: 18 jobs ~/fillq/queue/40_agent_ms_n{10,9,8}_o{0,1,2}_{a,b}.job
(2 h each, single core, mem_mb 60; started Mac clock 00:52, n = 10 first), outputs ~/fei_agent/ms_n*_o*_*.txt, one
line per annealing run, flushed as it goes. Read with: scp the ms_n*.txt into results/ms/, then
`cd code && python -X utf8 check_search.py ../results/ms/ms_n*.txt --top 1` (recomputes each leader with the separate
transform and checks monotonicity). All done about Mac clock 04:00-05:00 (laptop clock is 2 h behind the Mac's).
(2) Identify the leaders structurally (the n = 8 leader 3.3047 has eight equal influences - a depth-3 read-once tree?;
the n = 10 leaders 3.3892 transitive and 3.4011 not) and compare with the tower gate values in ../fei_solve_2026_11_09.
(3) File the n = 7 census as a brain memory (claim memory:brain/index first). (4) Queue the next batch on mini 2 from
what the search shows (longer runs at the n where the largest-influence rule and the best coordinate separate; n = 11,
12 need the table-free build). (5) Checklist T-20261110-114: note progress. Loop cron job 49a7ba01 (every 3 min,
session-only) auto-expires about 17 Nov 21:4x: re-create it then.
The Q/HB lines in results/merged7_first_pass.txt come from part 5 ALONE; the n = 7 Q and HB maxima are in
results/merged7_full.txt.


## Where the campaign stands (read 10 Nov from ../fei_solve_2026_11_09/STATE.md and FLOW.md)
- Main loop: an agent -> taken over by an agent (STATE/FLOW there; live). Papers: an agent (P2 posted,
  github.com/yspennstate/fei-good-coordinates). Older loop: an agent (host+coins search).
- Reduction in force: FEI <=> erasure form sum_i H(1[i in U] | U - i) <= C I <=> every nonconstant Boolean g has a
  coordinate with E_i(g) <= C Inf_i(g) (FLOW 7(d),(g)); half of it is in Gonzalez-MacManus-Pereyra arXiv 2606.00246.
  A restriction-closed class (monotone functions) with a good coordinate at constant C has FEI with C + 2/ln 2.
- Lower bound 6.5218 general; monotone tower record 4.506428465445; G* >= 4.50505 (transitive towers of PM(K33)).
- agent's item 12(gg): slowly varying weights g(Inf_i) are no easier than the unweighted statement (uses the n = 6
  census below: sup Q1 2.9733 < sup Q0 3.0310).
- Monotone FEI itself is open (memory fei_monotone_case_open_three_failed_routes_exact_data_2026_09_24).

## Results of this loop (each number computed two ways: C integer-table census, and numpy float recompute of the
## leading function from its truth table, code/merge_census.py; differences <= 6e-13)
Monotone n = 6, all 7,828,354 functions (weighted count = Dedekind number):
  max H/I 3.739764017898; max min_i E_i/Inf_i 2.944495303872 (f1 f8888000, f0 80008000; FEIB24's value);
  max min_i D_i/Inf_i 5.194871623379; rule "smallest positive influence" max 5.019930166880;
  balanced max H/(I-1) 6.347067498702 (f1 ffccff88, f0 a888a888; H 3.966917, I 1.625; equals agent's 6-variable
  host+coins value); max Q0 3.030964070213, Q05 3.001767947940, Q1 2.973303001503 (f1 ffffffee, f0 fefefeee);
  max Q1-Q0 0.117726646858; max H/B_var 0.473511279114; max H/B_han 0.386989089253.
Monotone n = 7, all 2,414,682,040,998 functions (six parts, weighted sum equals the Dedekind number; 6,031,580,181
evaluations; results/out7_0..5.txt, merged in results/merged7_first_pass.txt):
  max H/I 3.804357069772 (AND_7 / OR_7);
  max min_i E_i/Inf_i 2.954683814183 (f1 fffffffffffffff0, f0 fffefffefffeeee0; H 3.205207162, I 0.90625; influences
    0.09375 x3 and 0.15625 x4; E/Inf 3.031637 and 2.954684);
  rule "largest influence": max 2.954683814183, the same function - at n = 7 the coordinate of largest influence is
    never worse than the worst case of the best coordinate;
  max min_i D_i/Inf_i 5.215460422981 (f1 fffffffffffffffc, f0 fefefefefefefea8);
  rule "smallest positive influence": max 6.242539088548 (f1 fcf8ec00fcf8ec00, f0 e8a8a800e888a800; the bad coordinate
    has influence 0.015625) - that rule is bad, as expected;
  balanced max H/(I-1) 6.347067498702, attained by the 6-variable maximiser with a dummy variable: no 7-variable
    monotone balanced function beats it.
  Growth of max min_i E_i/Inf_i: 2.944495 (n = 6) -> 2.954684 (n = 7).
  Full-statistics pass (results/q7/, merged in results/merged7_full.txt, same weighted sum):
  max Q0 3.164564560463, Q05 3.124590660064, Q1 3.082273853464, all at f1 fca8f0a0cc880000, f0 0 (H 3.871583624,
    I 1.109375); sup Q1 < sup Q0 as at n = 6; max Q1-Q0 0.122307032088 (f1 fffffffffffffffe, f0 eaaaaaaaaaaaaaaa);
  max H/B_var 0.481228303877 (AND_7); max H/B_han 0.393531663695 (f1 ffffffffffffffff, f0 feeefeeefeeef000).
  Sent to an agent and an agent (mesh topic fei-fronts, 10 Nov 22:5x).

F4 annealing over monotone functions (code/mono_search.c; reproduces the census maxima 2.944495303872 at n = 6 and
2.954683814183 at n = 7 for both min E/Inf and the largest-influence rule, every run). FIRST MINUTES ONLY, lower
bounds, each leader recomputed with the separate transform (code/check_search.py) and checked monotone:
  n = 8:  min_i E_i/Inf_i >= 3.304701322452 (all eight influences 0.1640625; H 4.741429279, I 1.3125;
          table eee0aaa0e0e0a0a0ee00aa0000000000ccc00000c0c00000cc00000000000000) - a jump from 2.9547 at n = 7;
  n = 10: min_i E_i/Inf_i >= 3.401069972510 (eight coordinates at 3.401070, two at 3.589954; H 4.593938732,
          I 1.17578125); a function with ten equal influences gives 3.389192093441 (H 5.830604224, I 1.58203125);
  n = 10: largest-influence rule >= 3.388313072760 (that function's best coordinate has 2.541918) - so far the rule's
          worst case stays below the best-coordinate worst case;
  n = 10: sum_i E_i / I >= 3.346913333348.
  Leaders read as formulas (code/minterms.py): the n = 8 leader is the read-once tree (x0 x7 OR x1 x4) AND
  (x2 x6 OR x3 x5); the n = 10 transitive one is the 5 x 2 tribes function (AND of five ORs of two). So the small-n
  extremes of min_i E_i/Inf_i are read-once trees, which the towers of the main campaign already cover (4.505).
  READ BEFORE BUILDING ON THE n = 7 COINCIDENCE: the largest-influence rule is already refuted for monotone functions,
  FLOW 12(u) fact 3 and Prop 7.2 of the 24 Sep paper FEI_monotone_width (Maj_k(y) OR (x AND [y >= y0]) with each y_j
  replaced by a large majority: E_x/Inf_x ~ k/2 at the unique largest-influence coordinate, n about k 4^k). The
  agreement of the two maxima at n <= 10 is a small-n fact, not a route. The o1 jobs are therefore of low value.
  Odd (self-dual) functions have E_i = 0 at every coordinate (a b = 0 on every pair T, T+i by parity), so
  agent's test "Q1 on Maj_3 o psi, psi balanced monotone on 3-4 variables" is degenerate: every such psi but one
  (table eac8) is self-dual; for eac8 Q0 = 1.268273 and Q1 = 1.201205, and on Maj_3 o eac8 (12 variables) Q0 = 1.268273
  (unchanged, the composition identity) and Q1 = 1.219496 (results/maj3_lift.txt, code/maj3_lift.py).

## Fronts for this loop (disjoint from agent's weights item)
F1 monotone n = 7 census: first pass DONE; full-statistics pass running.
F4 local search over monotone functions on n = 8, 9, 10 (code/mono_search.c): objectives min_i E_i/Inf_i, E/Inf at the
   largest influence (does the n = 7 coincidence persist, or can the largest-influence coordinate be made bad?),
   sum_i E_i / I, balanced H/(I-1). Validated against the census at n = 6, 7 before any n >= 8 number is quoted.
F2 (to design) pair form 9(b): f = (u, B); all-coordinates-bad search under a transitive group beyond 21 variables.
F3 proof side, monotone case. Notes so far (not checked beyond hand algebra): for monotone f and coordinate i with
   g = E_i f, h = D_i f = 1_B (B the pivotal set), a = ghat(T), b = hhat(T); a private term (f = x_i OR F) gives
   a^2 = b^2 on every pair and E_i = 2 Inf_i; majority has E_i = 0 for T != empty by self-duality; the per-vertex
   inequality sum_i b_i^2 log2(1 + a^2/b_i^2) <= C (a^2 I(g) + W_1(g)) is FALSE (near-balanced thresholds: left side
   ~ log n, right side O(1)), so any proof must move mass across vertices.

## Log
- 10 Nov 21:40 on: cron 49a7ba01 created; campaign record read; both Macs probed; F1 written.
- 10 Nov about 22:00: mono_census.c compiled on Mac mini 2, validated on n = 6; six n = 7 jobs queued through fillq.
- 10 Nov 22:1x: first push, commit 2a9b391eff69052af9d2105ae0fbfe0699fd74b9 (STATE.md, code/mono_census.c).
- 10 Nov 22:2x-22:40: parts 0-5 fetched (about 21 min a part), merge_census.py written, every n = 6 and n = 7 leader
  recomputed independently; full-statistics pass (out7q_0..4) started on mini 2.

## 12 Nov 04:34 laptop: sy_dg_5 ended at -0.48; ap_9ck (the ap_9c space started from the record) added, tested, queued

- sy_dg_5 (9608 classes) ended: best -0.480653478, nothing above 0. sy_ap_9c still shows only its run 0 line (-0.049953176).
- New name in sym_search.py: ap_9ck = ap_9c with the K_{3,3} edge list attached, so the k33c seeds start the search (six added lines, nothing else changed; laptop copy and Mac mini 2 copy 697987357f074274, the previous Mac copy kept as sym_search_before_ap9ck.py, sha 2cef27d942cdef17).
- Test on Mac mini 2 before install (code/test_ap9ck.py): same inputs and generators as ap_9c; edge list equal to k33c's; 7584 classes against 4480 for k33c; every one of the 7584 classes lies inside a single k33c class, so every k33c function, the record included, is constant on ap_9ck classes.
- Queued 06:33:09 Mac mini 2 clock at 8568 MB available, 84 pct free, load 13.9: 23_agent_sy_ap_9ck.job (mem_mb 1600, 5400 s, seed 13), the same form as the k33cs run that ended at slack exactly 0 over 8240 classes. 264 of mine queued.
- What this run can show: the k33c group has the index-2 subgroups k33cs (S_3 x S_3) and this one; k33cs gave nothing above the record. If ap_9ck also ends at exactly 0, the record is a local optimum in both half-symmetric spaces around it.
- Record lower bound unchanged: 6.521845710923. Conjecture open.

NEXT: (1) read sy_ap_9ck first (expected first line: a seeded start at slack 0; anything above 0 is rebuilt from the explicit truth table before a word is said), then sy_ap_9c, sy_gv_dodec, sy_sub_7_2, sy_ec_k2x4 and the eleven small ones; (2) when sy_gv_dodec has ended and 9000 MB is available: mv ~/fei_agent/parked/30_agent_sy_k33cx2.job ~/fillq/queue/24_agent_sy_k33cx2.job; (3) the third index-2 subgroup of the k33c group, if there is one (the group of order 72 has up to three): list the index-2 subgroups, name the one not yet searched, add it the same way; (4) read cq_gs23*, cq_gs5*, cq_gs6*, the remaining library starts on Mac mini 1 as they end; (5) new families in struct() (Heawood edges = the 21 flags of the Fano plane; Petersen vertices with coins; arcs and vertices of K_4), under 10,000 classes; fixed names not covered by missing_names.py are checked against the result files first; (6) loop job 49a7ba01 expires about 17 Nov 21:4x: re-create it.

## 12 Nov 04:37 laptop: the k33c group has exactly three index-2 subgroups; the third (k33ce) added, tested, queued

- The subgroup of the k33c group (order 72 on the 9 edges) generated by all squares has order 18, so the quotient is of order 4 and exponent 2 and there are exactly three subgroups of index 2. They are: k33cs (S_3 x S_3, no swap of the sides; run, ended at slack exactly 0 over 8240 classes), ap_9ck (running since 06:34 Mac mini 2 clock, 7584 classes) and k33ce: the vertex permutations whose two sides carry the same sign, with or without the swap.
- k33ce added to sym_search.py (six lines; generators (0 1 2), (3 4 5), (0 1)(3 4), the swap; laptop and Mac mini 2 copy 229622268c12a482, previous Mac copy kept as sym_search_before_k33ce.py).
- Test before install (code/test_k33ce.py, Mac mini 2): the three groups each have order 36, each lies in the k33c group, the three are pairwise different, each carries the k33c edge list; k33ce has 8240 classes, each inside a single k33c class, class sizes sum to 2^18.
- Queued 06:36:14 Mac mini 2 clock at 8186 MB available, 84 pct free: 24_agent_sy_k33ce.job (mem_mb 1800, 5400 s, seed 17). 264 of mine queued.
- sy_ap_9ck is writing its flip lines from the record (single flips and the best pairs among 150); no summary line yet. sy_ap_9c and sy_gv_dodec unchanged.
- With k33cs done and these two queued or running, every space of functions invariant under half of the record's symmetry group gets searched from the record.
- Record lower bound unchanged: 6.521845710923. Conjecture open.

NEXT: (1) read sy_ap_9ck and sy_k33ce (anything above 0 is rebuilt from the explicit truth table before a word is said), then sy_ap_9c, sy_gv_dodec, sy_sub_7_2, sy_ec_k2x4 and the eleven small ones; (2) when sy_gv_dodec has ended and 9000 MB is available: mv ~/fei_agent/parked/30_agent_sy_k33cx2.job ~/fillq/queue/24_agent_sy_k33cx2.job; (3) if the three index-2 spaces all end at 0: the index-4 subgroup (order 18, generated by the squares) is the common refinement, about 15,000 classes, 3.6 GB of matrices, to be sized against free memory before it is written; (4) read cq_gs23*, cq_gs5*, cq_gs6*, the remaining library starts on Mac mini 1 as they end; (5) new families in struct() (Heawood edges = the 21 flags of the Fano plane; Petersen vertices with coins; arcs and vertices of K_4), under 10,000 classes; (6) loop job 49a7ba01 expires about 17 Nov 21:4x: re-create it.
