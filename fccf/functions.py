import mpmath as mp

class ContFunc:
    def __init__(self, exp_func, inv_exp_func, func_kwargs = {}, inv_func_kwargs = {}):
        self.func = exp_func
        self.func_kwargs = func_kwargs
        self.inv_func = inv_exp_func
        self.inv_func_kwargs = inv_func_kwargs
        
    def func(self, x):
        return self.exp_func(x, **self.func_kwargs)
    
    def inv_func(self, x):
        return self.inv_exp_func(x, **self.inv_func_kwargs)
    
def exp_neg(x):
    return mp.exp(-x)

def neg_log(x):
    return -mp.log(x)
    
TanhCF = ContFunc(mp.tanh, mp.atanh)

ExpNegCF = ContFunc(exp_neg, neg_log)