import numpy as np
from scipy.optimize import curve_fit

def func_power(x, P, t):
    return P * x**(-t)

def func_quad(x, C, b, a):
    return C * x**(b) * x**(a * np.log(x))

def func_exp(x, A, B):
    return np.exp(A * x**(B))
    
def fit_loop(constant_str,
                iteration_i = 1, 
                iteration_f = None,
                Upsilon_list = [], 
                Upsilon_error_list = [],
                ):
    iteration_idx = iteration_i
    
    while iteration_idx < iteration_f:
        print(iteration_idx)
        
        try:
            file = open(constant_str + "_data/iteration" + str(iteration_idx) + ".txt")
            if iteration_idx == 1:
                digits = list(map(int, file.read().splitlines()))[1:]
            else:
                digits = list(map(int, file.read().splitlines()))
            file.close()
            print("Successfully read data. Now incrementing iteration_idx.")
            iteration_idx += 1
        except Exception as e:
            print(e)
            break
    
        # try:
        hist, bins = np.histogram(digits, bins = max(digits) - 1)
        bins = bins[:-1]
        print("hist has shape " + str(np.shape(hist)))
        print("hist = " + str(hist))
        print("bins has shape " + str(np.shape(bins)))
        print("bins = " + str(bins))

        popt_power, pcov_power = curve_fit(func_power, bins, hist, 
                                    p0 = [hist[0], 1], 
                                    method = 'trf', 
                                    x_scale = [hist[0], 1])
        print("popt_power = " + str(popt_power))
        print("pcov_power = " + str(pcov_power))
        Upsilon_list.append(popt_power[1])
        Upsilon_error_list.append(np.sqrt(np.diag(pcov_power)[1]))
        # except Exception as e:
        #     print(e)
        #     break
        
        del file, digits, hist, bins
    
    return iteration_idx, Upsilon_list, Upsilon_error_list