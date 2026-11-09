from p6_python_cli import p6_cli_add
if p6_cli_add(2, 3) != 5:
    print('TARGET_BUG')
    raise SystemExit(1)
print('TARGET_OK')
