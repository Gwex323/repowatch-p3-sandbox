from p6_python_web import p6_web_add
if p6_web_add(2, 3) != 5:
    print('TARGET_BUG')
    raise SystemExit(1)
print('TARGET_OK')
