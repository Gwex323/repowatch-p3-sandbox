from pathlib import Path
import runpy
import unittest
path = Path('tests/test_mul_regression.py')
if not path.is_file():
    print('TARGET_BUG: missing permanent regression tests')
    raise SystemExit(1)
namespace = runpy.run_path(str(path))
suite = unittest.defaultTestLoader.loadTestsFromTestCase(namespace['MulRegression'])
result = unittest.TextTestRunner(verbosity=2).run(suite)
if not result.wasSuccessful():
    print('TARGET_BUG: regression failed')
    raise SystemExit(1)
print('TARGET_OK')
