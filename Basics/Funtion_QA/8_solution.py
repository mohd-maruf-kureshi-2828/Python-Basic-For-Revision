def print_key_value(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')

print_key_value(name="maruf",course="BCA")
print_key_value(name="maruf",course="BCA",speciality="Web Dev")