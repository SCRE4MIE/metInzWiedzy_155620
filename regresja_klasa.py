class RegresjaWektory:

    def __init__(self, vector_x, vector_y):
        import numpy as np
        from numpy.linalg import inv

        self.vector_x = np.array(vector_x).reshape(len(vector_x), 1)
        self.vector_y = np.array(vector_y).reshape(len(vector_y), 1)
        self.vector_X = np.append(np.ones((len(self.vector_x), 1)), self.vector_x, axis=1)
        self.vector_B = inv(np.transpose(self.vector_X) @ self.vector_X) @ np.transpose(self.vector_X) @ self.vector_y
        self.B_0 = self.vector_B[0][0]
        self.B_1 = self.vector_B[1][0]
        self.predict = [(q * self.B_1) + self.B_0 for q in x]

    def wykres(self):
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 6))
        plt.scatter(self.vector_x, self.vector_y, alpha=1)
        plt.plot(self.vector_x, self.predict, color='red')
        plt.title('Regresja liniowa')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()


x = [2,5,7,8]
y = [1,2,3,3]
regresja = RegresjaWektory(x, y)
regresja.wykres()
