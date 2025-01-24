# import pdb

def buggy_function(x):
    # pdb.set_trace()
    y = x + 10
    z = y * 2
    return z

print(buggy_function(5))
