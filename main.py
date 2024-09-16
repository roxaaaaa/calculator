def read_vectors(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        if len(lines) < 2:
            raise ValueError("File must contain at least two lines.")
        try:
            v1 = list(map(int, lines[0].strip().split(',')))
            v2 = list(map(int, lines[1].strip().split(',')))
        except ValueError:
            raise ValueError("One or both lines contain non-integer values.")
        return v1, v2

def write_vectors(file_name, content):
    with open(file_name, 'w') as f:
        f.write(','.join(map(str, content))+'\n')

def read_matrix(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        m1 = [list(map(int, row.strip().split(','))) for row in lines[:2]]
        m2 = [list(map(int, row.strip().split(','))) for row in lines[2:]]
        return m1, m2

def write_matrix(file_name, content):
    with open(file_name, 'w') as f:
        for row in content:
            f.write(','.join(map(str, content))+'\n')

def add_vector(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length.")
        return
    return [x + y for x, y in zip(v1, v2)]

def minus_vector(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length.")
        return
    return [x - y for x, y in zip(v1, v2)]

def multiply_vector(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length.")
        return
    return [x * y for x, y in zip(v1, v2)]

def devide_vector(v1, v2):
    if len(v1) != len(v2) or any(y == 0 for y in v2):
        raise ValueError("Error ")
    return [x / y for x, y in zip(v1, v2)]

def add_matrix(m1, m2):
    if len(m1) != len(m2):
        print("Error matrix must have same number of rows.")
        return
    return [m1[i][j] + m2[i][j] for j in range(len(m1[0]))for i in range(len(m1))]

def minus_matrix(m1, m2):
    if len(m1) != len(m2):
        print("Error matrix must have same number of rows.")
        return
    return [m1[i][j] - m2[i][j] for j in range (len(m1[0])) for i in range(len(m1))]

def multiply_matrix(m1, m2):
    if len(m1) != len(m2):
        print("Error matrix must have same number of rows.")
        return
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def inverse_matrix(m):
    det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    if det == 0:
        raise ValueError("Матриця невироджена")

    return [[m[1][1] / det, -m[0][1] / det], [-m[1][0] / det, m[0][0] / det]]

def divide_matrix(m1, m2):
    m2_inv = inverse_matrix(m2)
    return multiply_matrix(m1, m2_inv)

def main():
    v_file = 'input_vector.txt'
    m_file = 'input_matrix.txt'
    result_file = 'output_vector.txt'
    result_file1 = 'output_matrix.txt'

    v1, v2= read_vectors(v_file)
    m1, m2 = read_matrix(m_file)

    addition_result = add_vector(v1, v2)
    subtraction_result = minus_vector(v1, v2)
    multiplication_result = multiply_vector(v1, v2)
    division_result = devide_vector(v1, v2)

    addition_result1 = add_matrix(m1, m2)
    subtraction_result1 = minus_matrix(m1, m2)
    multiplication_result1 = multiply_matrix(m1, m2)
    division_result1 = divide_matrix(m1, m2)

    results = (
        f'({",".join(map(str, v1))}) + ({",".join(map(str, v2))}) = ({",".join(map(str, addition_result))})',
        f'({",".join(map(str, v1))}) - ({",".join(map(str, v2))}) = ({",".join(map(str, subtraction_result))})',
        f'({",".join(map(str, v1))}) * ({",".join(map(str, v2))}) = ({",".join(map(str, multiplication_result))})',
        f'({",".join(map(str, v1))}) / ({",".join(map(str, v2))}) = ({",".join(map(str, division_result))})'
    )

    with open(result_file, 'w') as f:
        f.write('\n'.join(results) + '\n')

    results1 = (
        f'({",".join(map(str, m1))}) + ({",".join(map(str, m2))}) = ({",".join(map(str, addition_result1))})',
        f'({",".join(map(str, m1))}) - ({",".join(map(str, m2))}) = ({",".join(map(str, subtraction_result1))})',
        f'({",".join(map(str, m1))}) * ({",".join(map(str, m2))}) = ({",".join(map(str, multiplication_result1))})',
        f'({",".join(map(str, m1))}) / ({",".join(map(str, m2))}) = ({",".join(map(str, division_result1))})'
    )

    with open(result_file1, 'w') as f:
        f.write('\n'.join(results1) + '\n')


if __name__ == '__main__':
    main()
