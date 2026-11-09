import {pathToFileURL} from 'node:url';
export function p6_js_add(left, right) {
  return left - right; // P6_JAVASCRIPT_CLI_BUG
}
if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  console.log(p6_js_add(Number(process.argv[2]), Number(process.argv[3])));
}
