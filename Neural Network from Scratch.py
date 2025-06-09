import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)


X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])


y = np.array([[0], [1], [1], [0]])


np.random.seed(1)


input_layer_size = 2
hidden_layer_size = 4
output_layer_size = 1


W1 = 2 * np.random.random((input_layer_size, hidden_layer_size)) - 1
W2 = 2 * np.random.random((hidden_layer_size, output_layer_size)) - 1


for epoch in range(10000):
   
    hidden_input = np.dot(X, W1)
    hidden_output = sigmoid(hidden_input)
    
    final_input = np.dot(hidden_output, W2)
    predicted_output = sigmoid(final_input)

    
    error = y - predicted_output
    if epoch % 1000 == 0:
        print(f"Epoch {epoch} Error: {np.mean(np.abs(error))}")

   
    d_output = error * sigmoid_derivative(predicted_output)
    d_hidden = d_output.dot(W2.T) * sigmoid_derivative(hidden_output)

    
    W2 += hidden_output.T.dot(d_output)
    W1 += X.T.dot(d_hidden)


print("\nFinal predictions:")
print(predicted_output.round(3))

