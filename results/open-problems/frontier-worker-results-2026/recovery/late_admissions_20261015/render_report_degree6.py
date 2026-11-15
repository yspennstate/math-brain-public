from pathlib import Path
from datetime import datetime
import json,hashlib
from playwright.sync_api import sync_playwright
H=Path(__file__).resolve().parent;report=Path('~/Downloads/frontier_layer_report_2026-10-15.html')
with sync_playwright() as p:
 b=p.chromium.launch(channel='chrome',headless=True,args=['--disable-gpu'])
 try:
  page=b.new_page(viewport={'width':1600,'height':1000});page.goto(report.as_uri(),wait_until='load');row=page.locator('#recovery-t067-degree6');assert row.count()==1;row.scroll_into_view_if_needed();row.screenshot(path=str(H/'report_review_degree6.png'));text=row.inner_text();assert 'distinct actual accounts' in text
  widths=page.evaluate('({scroll:document.documentElement.scrollWidth,viewport:innerWidth})');assert widths['scroll']<=widths['viewport']
  snapshot=H/'T067_DEGREE6_REPORT_SNAPSHOT.html';snapshot.write_bytes(report.read_bytes());(H/'T067_DEGREE6_REPORT_RECEIPT.json').write_text(json.dumps({'at':datetime.now().astimezone().isoformat(),'status':'Rendered; visual review pending','report_sha256':hashlib.sha256(snapshot.read_bytes()).hexdigest(),'widths':widths,'text':text},indent=2)+'\n',encoding='utf-8')
 finally:b.close()
print('Degree6 row rendered without overflow')
