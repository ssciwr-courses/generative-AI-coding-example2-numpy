# for example, interpolate between the points
# for example, numerical integration
# for example, matrix diagonalization
# for example, particle in a box hamiltonian
# write a class that does different operations on the numpy array
class OperateArray:
    def __init__(self, array):
        self.array = array

    def sum(self):
        return self.array.sum()

    def mean(self):
        return self.array.mean()

    def std(self):
        return self.array.std()

    # multiply the array by a scalar
    def multiply(self, scalar):
        return self.array * scalar

    # multiply the array by another array element-wise (Hadamard product)
    def multiply_array(self, array):
        return self.array * array

    # perform matrix multiplication
    def matrix_multiply(self, array):
        return self.array @ array
