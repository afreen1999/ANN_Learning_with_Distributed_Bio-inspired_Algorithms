class StrassensMult():
    # credits - https://github.com/stanislavkozlovski/Algorithms/blob/master/Coursera/algorithms_stanford/Strassen%20Matrix%20Multiplication/python/strassen.py

    def __init__(self, matrix_a=[[1,2,3,4],[3,4,5,6],[1,2,6,7],[3,4,3,4]], matrix_b=[[1,2,6,7],[3,4,3,4],[1,2,6,7],[3,4,3,4]]):
        self.matrix_a = matrix_a 
        self.matrix_b = matrix_b
        
    def default_matrix_multiplication(self, a, b):
        """
        Only for 2x2 matrices
        """
        if len(a) != 2 or len(a[0]) != 2 or len(b) != 2 or len(b[0]) != 2:
            raise Exception('Matrices should be 2x2!')
        # print(a[0][0] * b[0][1] + a[0][1] * b[1][1])
        new_matrix = [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                      [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

        return new_matrix


    def matrix_addition(self, matrix_a, matrix_b):
        return [[matrix_a[row][col] + matrix_b[row][col]
                 for col in range(len(matrix_a[row]))] for row in range(len(matrix_a))]


    def matrix_subtraction(self, matrix_a, matrix_b):
        return [[matrix_a[row][col] - matrix_b[row][col]
                 for col in range(len(matrix_a[row]))] for row in range(len(matrix_a))]


    def split_matrix(self,a):
        """
        Given a matrix, return the TOP_LEFT, TOP_RIGHT, BOT_LEFT and BOT_RIGHT quadrant
        """
        if len(a) % 2 != 0 or len(a[0]) % 2 != 0:
            raise Exception('Odd matrices are not supported!')

        matrix_length = len(a)
        mid = matrix_length // 2
        top_left = [[a[i][j] for j in range(mid)] for i in range(mid)]
        bot_left = [[a[i][j] for j in range(mid)] for i in range(mid, matrix_length)]

        top_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid)]
        bot_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid, matrix_length)]

        return top_left, top_right, bot_left, bot_right


    def get_matrix_dimensions(self, matrix):
        return len(matrix), len(matrix[0])


    def strassen(self):
        """
        Recursive function to calculate the product of two matrices, using the Strassen Algorithm.
        Currently only works for matrices of even length (2x2, 4x4, 6x6...etc)
        """
        matrix_a = self.matrix_a
        matrix_b = self.matrix_b
        if self.get_matrix_dimensions(matrix_a) != self.get_matrix_dimensions(matrix_b):
            raise Exception(f'Both matrices are not the same dimension! \nMatrix A:{matrix_a} \nMatrix B:{matrix_b}')
        if self.get_matrix_dimensions(matrix_a) == (2, 2):
            return self.default_matrix_multiplication(matrix_a, matrix_b)

        A, B, C, D = self.split_matrix(matrix_a)
        E, F, G, H = self.split_matrix(matrix_b)

        p1 = self.strassen(A, self.matrix_subtraction(F, H))
        p2 = self.strassen(self.matrix_addition(A, B), H)
        p3 = self.strassen(self.matrix_addition(C, D), E)
        p4 = self.strassen(D, self.matrix_subtraction(G, E))
        p5 = self.strassen(self.matrix_addition(A, D), self.matrix_addition(E, H))
        p6 = self.strassen(self.matrix_subtraction(B, D), self.matrix_addition(G, H))
        p7 = self.strassen(self.matrix_subtraction(A, C), self.matrix_addition(E, F))

        top_left = self.matrix_addition(self.matrix_subtraction(self.matrix_addition(p5, p4), p2), p6)
        top_right = self.matrix_addition(p1, p2)
        bot_left = self.matrix_addition(p3, p4)
        bot_right = self.matrix_subtraction(self.matrix_subtraction(self.matrix_addition(p1, p5), p3), p7)

        # construct the new matrix from our 4 quadrants
        new_matrix = []
        for i in range(len(top_right)):
            new_matrix.append(top_left[i] + top_right[i])
        for i in range(len(bot_right)):
            new_matrix.append(bot_left[i] + bot_right[i])
        return new_matrix

s = StrassensMult([[1,2],[3,4]], [[6,7],[8,9]])
s.strassen()
