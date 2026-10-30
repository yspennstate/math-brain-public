from pathlib import Path
import time,json,hashlib
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter()
left=31**491071
right=481**231361*15**27900*(1<<262144)
assert left>right
assert 1924**2+124**2+124*60**2+1922*4**2==2048**2
assert 961*511==491071
elapsed=time.perf_counter()-start;assert elapsed<60
record={'status':'PASS','checks':3,'elapsed_seconds':elapsed,'claim':'H(F)>2H(f) for the actual eleven-bit shared point-defect product','gap_natural':'(491071 ln31-231361 ln481-27900 ln15-262144 ln2)/131072','integer_comparison':'31^491071 > 481^231361 * 15^27900 * 2^262144','left_bit_length':left.bit_length(),'right_bit_length':right.bit_length(),'left_sha256':hashlib.sha256(left.to_bytes((left.bit_length()+7)//8,'big')).hexdigest(),'right_sha256':hashlib.sha256(right.to_bytes((right.bit_length()+7)//8,'big')).hexdigest(),'certificate_regeneration':'python -X utf8 code/verify_integer_witness.py','floating_arithmetic':False}
(ROOT/'out/INTEGER_WITNESS.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(json.dumps(record))
