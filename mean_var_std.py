import numpy as np

def calculate(list) -> dict:
    if len(list) != 9: raise ValueError("List must contain nine numbers.")

    matrix_reshaped = np.reshape(list, (3,3))

    calculations = {'mean': [np.mean(matrix_reshaped,axis=0).tolist(), np.mean(matrix_reshaped,axis=1).tolist(), np.mean(matrix_reshaped)],
                    'variance': [np.var(matrix_reshaped,axis=0).tolist(), np.var(matrix_reshaped,axis=1).tolist(), np.var(matrix_reshaped)],
                    'standard deviation': [np.std(matrix_reshaped,axis=0).tolist(), np.std(matrix_reshaped,axis=1).tolist(), np.std(matrix_reshaped)],
                    'max': [np.max(matrix_reshaped,axis=0).tolist(), np.max(matrix_reshaped, axis=1).tolist(), np.max(matrix_reshaped)],
                    'min': [np.min(matrix_reshaped, axis=0).tolist(), np.min(matrix_reshaped, axis=1).tolist(), np.min(matrix_reshaped)],
                    'sum': [np.sum(matrix_reshaped, axis=0).tolist(), np.sum(matrix_reshaped, axis=1).tolist(), np.sum(matrix_reshaped)],}

    return calculations