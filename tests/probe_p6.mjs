import {p6_js_add} from '../p6_node_cli.mjs';
if (p6_js_add(2,3)!==5) {console.log('TARGET_BUG');process.exit(1);} console.log('TARGET_OK');
