from fccf.fitting_fns import *

# import numpy as np
# from scipy.optimize import curve_fit

# def func_power(x, P, t):
#     return P * x**(-t)

# def func_quad(x, C, b, a):
#     return C * x**(b) * x**(a * np.log(x))

# def func_exp(x, A, B):
#     return np.exp(A * x**(B))

# # factor = 3
# # factor_max_power = 18

# # digits = []
# # iteration_idx = 2
# # while factor**(factor_max_power) >= len(digits):
# #     try:
# #         digits.extend(list(map(int, open("gamma_data/iteration" + str(iteration_idx) + ".txt").read().splitlines()))[1:])
# #         iteration_idx += 1
# #     except:
# #         break

# # # fit_limit = 250000

# # # hist, bins = np.histogram(digits[:fit_limit], bins = max(digits[:fit_limit]) - 1)
# # # bins = bins[:-1]
# # # # print("bins has shape " + str(np.shape(bins)))
# # # # print("bins = " + str(bins))
# # # # print("hist has shape " + str(np.shape(hist)))
# # # # print("hist = " + str(hist))

# # # popt_power, pcov_power = curve_fit(func_power, bins, hist)

# # # print(popt_power)

# # Upsilon_array = np.array([])
# # Upsilon_error_array = np.array([])

# # for i in range(2, factor_max_power):
# #     try:
# #         fit_limit = int(factor**(i))
# #         hist, bins = np.histogram(digits[:fit_limit], bins = max(digits[:fit_limit]) - 1)
# #         bins = bins[:-1]
        
# #         popt_power, pcov_power = curve_fit(func_power, bins, hist)
# #         Upsilon_array = np.append(Upsilon_array, popt_power[1])
# #         Upsilon_error_array = np.append(Upsilon_error_array, np.sqrt(np.diag(pcov_power))[1])
# #     except:
# #         break

# # print(Upsilon_array)
# # print(Upsilon_error_array)

# # np.savetxt("gamma_data_" + str(fit_limit) + "_2.txt", np.append(bins, hist), delimiter = ', ')

# Upsilon_list = []
# Upsilon_error_list = []

# iteration_idx = 1

# # input to this function: iteration_i = 1, iteration_f = None, constant_str, Upsilon_list [], Upsilon_error_list = [], delimiter = ", "
# while iteration_idx < 12:
#     print(iteration_idx)
    
#     try:
#         file = open("gamma_data/iteration" + str(iteration_idx) + ".txt")
#         if iteration_idx == 1:
#             digits = list(map(int, file.read().splitlines()))[1:]
#         else:
#             digits = list(map(int, file.read().splitlines()))
#         file.close()
#         print("Successfully read data. Now incrementing iteration_idx.")
#         iteration_idx += 1
#     except Exception as e:
#         print(e)
#         break

#     try:
#         fit_limit = len(digits) // 2
        
#         hist, bins = np.histogram(digits[:fit_limit], bins = max(digits[:fit_limit]) - 1)
#         bins = bins[:-1]
#         print("hist has shape " + str(np.shape(hist)))
#         print("hist = " + str(hist))
#         print("bins has shape " + str(np.shape(bins)))
#         print("bins = " + str(bins))
        
#         popt_power, pcov_power = curve_fit(func_power, bins, hist, 
#                                     p0 = [hist[0], 1], 
#                                     method = 'trf', 
#                                     x_scale = [hist[0], 1])
#         print("popt_power = " + str(popt_power))
#         print("pcov_power = " + str(pcov_power))
#         Upsilon_list.append(popt_power[1])
#         Upsilon_error_list.append(np.sqrt(np.diag(pcov_power)[1]))
        
#         del hist, bins
        
#         hist, bins = np.histogram(digits[fit_limit:], bins = max(digits[fit_limit:]) - 1)
#         bins = bins[:-1]
#         print("hist has shape " + str(np.shape(hist)))
#         print("hist = " + str(hist))
#         print("bins has shape " + str(np.shape(bins)))
#         print("bins = " + str(bins))
        
#         popt_power, pcov_power = curve_fit(func_power, bins, hist, 
#                                     p0 = [hist[0], 1], 
#                                     method = 'trf', 
#                                     x_scale = [hist[0], 1])
#         print("popt_power = " + str(popt_power))
#         print("pcov_power = " + str(pcov_power))
        
#         print("Successfully performed fit and extracted Upsilon values.")
        
#         Upsilon_list.append(popt_power[1])
#         Upsilon_error_list.append(np.sqrt(np.diag(pcov_power)[1]))
#     except Exception as e:
#         print(e)
#         break
    
#     del file, digits, hist, bins

# print(Upsilon_list)
# print(Upsilon_error_list)

# np.savetxt("gamma_fit_" + str(iteration_idx - 1) + "its.txt", Upsilon_list + Upsilon_error_list, delimiter = ', ')

constant_str = "gamma"

iteration_idx, Upsilon_list, Upsilon_error_list = \
                fit_loop(constant_str = constant_str, 
                        iteration_f = 11)

print(Upsilon_list)
print(Upsilon_error_list)

np.savetxt(constant_str + "_fit_" + str(iteration_idx - 1) + "its.txt", 
                Upsilon_list + Upsilon_error_list, 
                delimiter = ', ')