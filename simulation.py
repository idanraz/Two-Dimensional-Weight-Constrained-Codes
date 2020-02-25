import IterativeEncoder as Encoder
from time import time
import numpy as np


"""
this module is used to perform simulations of the encoder on differnt sized inputs
p - probability of 1 in the input matrix
c - ratio of  n/m in the input matrix
start - the initial size to check from
end - the size to check up to
steps - the increment in size between iterations
num_iterations - the nubmer of runs to perform on each size
"""

if __name__ == "__main__":
    p = 0.5
    c = 0.5
    start = 0
    end = 10000
    steps = 200
    num_iterations = 10


    name = "results_{}_{}.csv".format(p,c)
    res_file = open(name,"a+")
    res_file.write("n,m,encode_time,decode_time,count_flips\n")
    res_file.close()
    x = [i for i in range(start, end, steps)]
    for i in x:
        with open(name,"a+") as res_file:
            total_steps_count = 0
            total_enc_time = 0
            total_dec_time = 0
            for _ in range(num_iterations):
                mat = np.random.choice(a=[1,0],size=(i,int(i//c)),p=[p,1-p])
                start = time()
                res = Encoder.endoce(mat)
                endcode_time = time() - start
                start = time()
                dec = Encoder.decode(res)
                dec_time = time() - start
                # check_correctness(mat, res, dec)
                total_enc_time += endcode_time
                total_dec_time += dec_time
                total_steps_count += Encoder.get_num_steps()

            enc_time = total_enc_time / num_iterations
            dec_time = total_dec_time / num_iterations
            flip_num = total_steps_count // num_iterations

            results = "{},{},{},{},{}\n".format(i,i//c,enc_time,dec_time,flip_num)
            res_file.write(results)
            print("size {} finished".format(i))
