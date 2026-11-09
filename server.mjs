import {createServer as createHttpServer} from 'node:http';
import {readFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {p6_ts_add} from './dist/p6_calc.js';
export function createServer() {
  return createHttpServer((req,res) => {
    if (req.url === '/api/result') {
      res.writeHead(200, {'Content-Type':'application/json'});
      res.end(JSON.stringify({value:p6_ts_add(2,3)}));
    } else if (req.url === '/' || req.url === '/app.js') {
      res.writeHead(200, {'Content-Type':req.url === '/' ? 'text/html' : 'text/javascript'});
      res.end(readFileSync(req.url === '/' ? 'dist/index.html' : 'dist/app.js'));
    } else { res.writeHead(404); res.end(); }
  });
}
if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  createServer().listen(Number(process.env.PORT || 8080), '0.0.0.0');
}
