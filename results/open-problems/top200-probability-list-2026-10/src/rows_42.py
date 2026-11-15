# Famous-list addition, 15 Nov 2026 (an agent), from a fresh screen of classical constants of interacting
# particle systems; sources read from Crossref records and abstracts on 15 Nov 2026.
ROWS = [
 {'id': 'T475',
  'd': 'IPS',
  't': 'The critical value of the one-dimensional contact process',
  's': 'In the basic contact process on Z each infected site recovers at rate 1 and infects each of its two '
       'neighbours at rate lambda. Let lambda_c be the infimum of the rates at which the process started from one '
       'infected site survives with positive probability. Determine lambda_c, or prove upper and lower bounds on it '
       'much closer together than the present ones.',
  'c': 'The process dies out at lambda_c itself (Bezuidenhout and Grimmett 1990). The upper bound 2 was lowered to 1.942 by Liggett (1995), who devised a method that, unlike the '
       'earlier argument for 2, can be pushed further. Lower bounds come from computer calculations on processes '
       'that only change sites within m places of the left-most infected one (Ziezold and Grillenberger 1988, m up to '
       '14). No closed form is known. In d >= 3, Xue '
       '(2018) shows lambda_c(Z^3) <= 0.34. T099 asks for the critical exponents at lambda_c; T473 and T474 are '
       'other constants known far better from computation than from proof.',
  'src': 'T. M. Liggett, Improved upper bounds for the contact process critical value, Ann. Probab. 23 (1995), '
         '697-723, doi:10.1214/aop/1176988285. J. Ziezold and C. Grillenberger, On the critical infection rate of the '
         'one-dimensional basic contact process: numerical results, J. Appl. Probab. 25 (1988), 1-8, '
         'doi:10.1017/S0021900200040584. C. Bezuidenhout and G. Grimmett, The critical contact process dies out, '
         'Ann. Probab. 18 (1990), 1462-1482, doi:10.1214/aop/1176990627. X. Xue, An improved upper bound for the '
         'critical value of the contact process on Z^d with d >= 3, Electron. Commun. Probab. 23 (2018), 1-11, '
         'doi:10.1214/18-ECP177.',
  'loc': 'Liggett 1995, abstract (Crossref, read 15 Nov 2026): the best known upper bound "is 2", and the method gives '
         '"lambda_c <= 1.942". Ziezold-Grillenberger, abstract: for m = 0, 1, ..., 14 "direct computations give '
         'critical values which are lower bounds". Xue 2018, abstract: the three-dimensional critical value "is '
         'shown to be at most 0.34". The numerical lower bound of Ziezold-Grillenberger and the simulated value '
         'were not read and are not given here.',
  'url': 'https://doi.org/10.1214/aop/1176988285',
  'why': 'The contact process is the basic model of the spread of an infection and the continuous-time form of '
         'oriented percolation; lambda_c is its first number. Every known rigorous route to it (comparison, '
         'renormalisation, truncated processes) loses a fixed factor, so the gap between proof and simulation '
         'measures what the methods of the field cannot yet do.',
  'st': 'Open: Liggett\'s 1.942 is the upper bound in his 1995 paper; later work on the one-dimensional bound has not '
        'been checked here. Read the papers citing Liggett (1995) and the 1999 book before quoting a current interval.',
  'n': 'Added 15 Nov 2026 by an agent from a fresh screen after the earlier candidate pool was spent; it takes '
       'one of the famous places freed by the retirements.'},
]
