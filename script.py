def inventory_summary(my_dict):
    sum1=0
    for(key, value) in my_dict.items():
        sum1 = sum1 + value[1]
    return sum1




my_dict={ "milk":(3,3),"candy":(2,5),"chips":(4,6)}
print(inventory_summary(my_dict))
def print_args_kwargs(*args,**kwargs):
 print(*args)
 print(**kwargs)



print_args_kwargs(2,3,4,5,"milk","candy","chips")
