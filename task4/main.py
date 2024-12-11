import numpy as np


def calculate_entropy(probabilities):
    return -sum(p * np.log2(p) for p in np.nditer(probabilities))

def main(input_matrix):
    matrix = np.array(input_matrix)
    total = matrix.sum()
    
    joint_probs = matrix / total
    p_y = joint_probs.sum(axis=1)
    p_x = joint_probs.sum(axis=0)
    
    h_y = calculate_entropy(p_y)
    h_x = calculate_entropy(p_x)
    
    cond_probs = joint_probs / p_y[:, np.newaxis]
    cond_h = sum(p_y[i] * calculate_entropy(cond_probs[i]) for i in range(len(joint_probs)))
    
    info = h_x - cond_h
    h_xy_sum = h_y + cond_h

    print(f"Информация:          {info:.3f}")
    print(f"Совместная энтропия: {h_xy_sum:.3f}")


test_matrix = [[20, 15, 10, 5],
               [30, 20, 15, 10],
               [25, 25, 20, 15],
               [20, 20, 25, 20],
               [15, 15, 30, 25]]

main(test_matrix)
