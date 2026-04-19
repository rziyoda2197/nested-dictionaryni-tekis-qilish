def flatten(nested_dict):
    flat_dict = {}
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            for subkey, subvalue in flatten(value).items():
                flat_dict[f"{key}.{subkey}"] = subvalue
        else:
            flat_dict[key] = value
    return flat_dict

nested_dict = {
    "a": 1,
    "b": 2,
    "c": {
        "d": 3,
        "e": 4,
        "f": {
            "g": 5,
            "h": 6
        }
    }
}

print(flatten(nested_dict))
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. `nested_dict` deb nomlangan dictionaryni yaratib, uni quyidagilar bilan to'ldiring:
   - "a" kaliti uchun qiymat 1
   - "b" kaliti uchun qiymat 2
   - "c" kaliti uchun dictionary:
     - "d" kaliti uchun qiymat 3
     - "e" kaliti uchun qiymat 4
     - "f" kaliti uchun dictionary:
       - "g" kaliti uchun qiymat 5
       - "h" kaliti uchun qiymat 6

2. `flatten(nested_dict)` funksiyasini chaqiring.

3. Natija quyidagilar bo'lishi kerak:
   - "a": 1
   - "b": 2
   - "c.d": 3
   - "c.e": 4
   - "c.f.g": 5
   - "c.f.h": 6
