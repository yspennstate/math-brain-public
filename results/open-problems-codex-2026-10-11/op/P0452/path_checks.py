from fractions import Fraction
from itertools import permutations
from pathlib import Path
import json,math
rows=[]
for length in range(3,9):
 total=Fraction(0)
 for order in permutations(range(length)):
  ranks=[0]*length
  for rank,index in enumerate(order):ranks[index]=rank
  counts=[0]*length
  for index in range(length-1):counts[max(ranks[index],ranks[index+1])]+=1
  term=Fraction(1);tail=0
  for count in reversed(counts):
   tail+=count
   term/=tail
  total+=term
 square_bound=Fraction(25,16)*Fraction(1,2)**(length-3)
 assert total**2<=square_bound
 rows.append({'l':length,'integral_exact':str(total),'HS_bound':1.25*(1/math.sqrt(2))**(length-3),'passed':True})
Path('path_integral_checks.json').write_text(json.dumps(rows,indent=2))
print('Exact integration inequalities passed for lengths 3 through 8.')
