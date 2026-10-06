// Captures real screenshots of the live products into assets/shots/. Run by .github/workflows/screenshots.yml
import { chromium } from 'playwright';
import { mkdirSync } from 'node:fs';
const sites = { casora: 'https://casora-nine.vercel.app/', splitmate: 'https://splitmate-two-iota.vercel.app/', laya: 'https://layameme.vercel.app/' };
mkdirSync('assets/shots', { recursive: true });
const b = await chromium.launch();
for (const [slug, url] of Object.entries(sites)) {
  try {
    const p = await b.newPage({ viewport: { width: 1440, height: 960 }, deviceScaleFactor: 1 });
    await p.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
    await p.waitForTimeout(2500);
    await p.screenshot({ path: `assets/shots/${slug}.jpg`, type: 'jpeg', quality: 82, clip: { x: 0, y: 0, width: 1440, height: 960 } });
    console.log('captured', slug);
  } catch (e) { console.log('skipped', slug, e.message.split('\n')[0]); }
}
await b.close();
