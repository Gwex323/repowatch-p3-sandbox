import test from 'node:test';
import assert from 'node:assert/strict';
import {createServer} from '../server.mjs';
test('compiled TypeScript serves a correct HTTP response', async () => {
  const server = createServer();
  await new Promise(done => server.listen(0, '127.0.0.1', done));
  try {
    const base = 'http://127.0.0.1:' + server.address().port;
    assert.match(await (await fetch(base + '/')).text(), /P6 TypeScript Web/);
    assert.equal((await (await fetch(base + '/api/result')).json()).value, 5);
  } finally { await new Promise(done => server.close(done)); }
});
