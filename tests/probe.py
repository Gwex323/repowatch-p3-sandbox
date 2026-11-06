from mul import mul
value = mul(2, 3)
if value != 6:
    print('TARGET_BUG')
    raise SystemExit(1)
print('TARGET_OK')
