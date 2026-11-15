from pathlib import Path
from datetime import datetime
import hashlib,json
from playwright.sync_api import sync_playwright
H=Path(__file__).resolve().parent;report=Path('~/Downloads/frontier_layer_report_2026-10-15.html')
with sync_playwright() as p:
 browser=p.chromium.launch(channel='chrome',headless=True,args=['--disable-gpu'])
 try:
  page=browser.new_page(viewport={'width':1600,'height':1000});page.goto(report.as_uri(),wait_until='load')
  for d in [14,15]:
   row=page.locator(f'#recovery-t170-d{d}');assert row.count()==1;row.scroll_into_view_if_needed();row.screenshot(path=str(H/f'report_review_d{d}.png'));assert 'distinct actual accounts' in row.inner_text()
  widths=page.evaluate('({scroll:document.documentElement.scrollWidth,viewport:innerWidth})');assert widths['scroll']<=widths['viewport']
  (H/'T170_ROLLING_REPORT_RECEIPT.json').write_text(json.dumps({'at':datetime.now().astimezone().isoformat(),'report_sha256':hashlib.sha256(report.read_bytes()).hexdigest(),'widths':widths,'status':'Rendered; visual review pending'},indent=2)+'\n',encoding='utf-8')
 finally:browser.close()
print('Rendered dimension14 and15 rows; no overflow')
