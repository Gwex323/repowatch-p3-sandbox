import {execFileSync} from 'node:child_process';
import {mkdirSync, writeFileSync} from 'node:fs';
execFileSync(process.execPath, ['/opt/repowatch/typescript/lib/tsc.js', '--project', 'tsconfig.json'], {stdio:'inherit'});
mkdirSync('dist', {recursive:true});
writeFileSync('dist/index.html', '<!doctype html><html><head><title>P6 TypeScript Web</title></head><body><h1>P6 TypeScript Web</h1><output id="result">Loading</output><script type="module" src="/app.js"></script></body></html>');
writeFileSync('dist/app.js', "fetch('/api/result').then(r=>r.json()).then(r=>document.getElementById('result').textContent=String(r.value));");
console.log('P6_TYPESCRIPT_BUILD_OK');
