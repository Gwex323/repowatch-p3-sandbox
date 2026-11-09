import {p6_ts_add} from '../p6_calc.ts';
if (p6_ts_add(2,3)!==5) {console.log('TARGET_BUG');process.exit(1);} console.log('TARGET_OK');
