import test from 'node:test';
import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';
test('actual CLI returns the sum', () => {
  const result = spawnSync(process.execPath, ['p6_node_cli.mjs', '2', '3'], {encoding:'utf8'});
  assert.equal(result.status, 0);
  assert.equal(result.stdout.trim(), '5');
});
test('CLI zero argument', () => {
  const result = spawnSync(process.execPath, ['p6_node_cli.mjs', '2', '0'], {encoding:'utf8'});
  assert.equal(result.status, 0);
  assert.equal(result.stdout.trim(), '2');
});
