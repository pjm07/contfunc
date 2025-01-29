from fitting_fns import *
import sys

if len(sys.argv) > 1:
    iteration_i = int(sys.argv[1])
else:
    iteration_i = 8

constant_str = "pi"

iteration_idx, Upsilon_list, Upsilon_error_list = \
                fit_loop(constant_str = constant_str, 
                        iteration_i = iteration_i,
                        iteration_f = iteration_i + 1)

print(Upsilon_list)
print(Upsilon_error_list)

if iteration_idx < 11:
    np.savetxt(constant_str + "_fit_" + "it0" + str(iteration_idx - 1) + ".txt", 
                    Upsilon_list + Upsilon_error_list, 
                    delimiter = ', ')
else:
    np.savetxt(constant_str + "_fit_" + "it" + str(iteration_idx - 1) + ".txt", 
                    Upsilon_list + Upsilon_error_list, 
                    delimiter = ', ')
