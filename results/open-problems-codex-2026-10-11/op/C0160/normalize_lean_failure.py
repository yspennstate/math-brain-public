from pathlib import Path
p=Path(__file__).parent/'lean_check_failed_decidability.txt'
raw=p.read_bytes()
if raw.startswith(b'\xff\xfe'):
 marker=raw.rfind(b'Exit code: ')
 if marker>=0:
  text=raw[:marker].decode('utf-16',errors='replace')+raw[marker:].decode('utf-8-sig',errors='replace')
 else:
  text=raw.decode('utf-16',errors='replace')
else:
 text=raw.decode('utf-8-sig')
assert 'Exit code: 1' in text
p.write_text(text,encoding='utf-8')
print('Failed run preserved as UTF-8, exit 1.')
