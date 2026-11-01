exec(open('targeted_search.py',encoding='utf-8-sig').read().split('with concurrent.futures')[0])
row=f('random_turn_hex','https://arxiv.org/pdf/math/0508580')
with (R/'search_log.jsonl').open('a',encoding='utf8') as o:o.write(json.dumps(row)+'\n')
print(row)
if 'status' in row:
 import pymupdf
 d=pymupdf.open(stream=(R/'random_turn_hex.response').read_bytes(),filetype='pdf')
 (R/'random_turn_hex.txt').write_text('\n'.join('=== PAGE '+str(i+1)+' ===\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
