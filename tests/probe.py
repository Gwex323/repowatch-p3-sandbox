from sub import sub
value = sub(5, 2)
if value != 3:
    print('TARGET_BUG')
    raise SystemExit(1)
print('TARGET_OK')
