global_num = 10

def local_scope(local_num):
    sum = local_num + global_num
    return sum

sum_of_both = local_scope(5)

print(f"\n\nGLOBAL NUMBER: {global_num}")
print(f"lOCAL NUMBER: {sum_of_both - global_num}")
print(f"SUM: {sum_of_both}")