

from loadandprepared import load_and_prepare_data
import numpy as np

def ann (hidden_neurons, epochs, lerning_rate):

    file_path = "assignment5.csv"
    
    X_train, y_train, X_val, y_val, X_test, y_test = load_and_prepare_data(file_path)


    input_size = X_train.shape[1]   # 784 för 28*28 pixlar
    output_size = y_train.shape[1]  # 10 (eftersom vi har one-hot encoding)


    #Vikt och vikt "noll" för första lagret
    weights_1 = np.random.randn(input_size, hidden_neurons) * 0.01
    weights_zero_1 = np.zeros((1, hidden_neurons))

    weights_2 = np.random.randn(hidden_neurons, output_size) * 0.01
    weights_zero_2 = np.zeros((1, output_size))



    printinfo(hidden_neurons, epochs, lerning_rate)


    for epoch in range(epochs):

        # Forward pass
        first_matrix_multi, relu_value, Y_hat = forwardpass(X_train, weights_1, weights_zero_1, weights_2, weights_zero_2)

        # Loss, hur fel nätverket har gjort, ju lägre desto bättre
        loss = compute_loss(Y_hat, y_train)

        # Backprop
        weights_1, weights_zero_1, weights_2, weights_zero_2 = backwardpass(
            X_train, y_train, first_matrix_multi, relu_value, weights_1, weights_zero_1, weights_2, weights_zero_2, lerning_rate
        )

        # Accuracy
        train_acc = accuracy(Y_hat, y_train)

        # Validation
        _, _, Y_val_hat = forwardpass(X_val, weights_1, weights_zero_1, weights_2, weights_zero_2)
        val_acc = accuracy(Y_val_hat, y_val)

        print(f"Epoch {epoch+1:02d}: Loss={loss:.4f} Train Acc={train_acc*100:.2f}%  Val Acc={val_acc*100:.2f}%")

    #Test
    _, _, Y_test_hat = forwardpass(X_test, weights_1, weights_zero_1, weights_2, weights_zero_2)
    test_acc = accuracy(Y_test_hat, y_test)

    printline()
    print(f"\nTest accuracy: {test_acc*100:.2f}%\n")
    printline()



def forwardpass(X, weights_1, weights_zero_1, weights_2, weights_zero_2):

    first_matrix_multi, relu_value = hidden_layer_one(X, weights_1, weights_zero_1)
    Y_hat = output_layer(relu_value, weights_2, weights_zero_2)

    return first_matrix_multi, relu_value, Y_hat

def backwardpass(X, Y, first_matrix_multi, relu_value, weights_1, weights_zero_1, weights_2, weights_zero_2, lerning_rate):
    m = X.shape[0]  # antal tränings exempel

    # Output layer, beräkna fel och uppdatera vikter
    Z2 = relu_value @ weights_2 + weights_zero_2
    Y_hat = softmax(Z2)
    error_output = Y_hat - Y  
    uppdate_weights2 = relu_value.T @ error_output / m
    uppdate_weights2_0 = np.sum(error_output, axis=0, keepdims=True) / m

    # Hidden layer
    error_hidden_layer = error_output @ weights_2.T
    error_before_relu = error_hidden_layer * (first_matrix_multi > 0)  # ReLU derivata
    uppdate_weights_1 = X.T @ error_before_relu / m
    uppdate_weights_1_0 = np.sum(error_before_relu, axis=0, keepdims=True) / m

    # Uppdatera vikter
    weights_1 -= lerning_rate * uppdate_weights_1
    weights_zero_1 -= lerning_rate * uppdate_weights_1_0
    weights_2 -= lerning_rate * uppdate_weights2
    weights_zero_2 -= lerning_rate * uppdate_weights2_0

    return weights_1, weights_zero_1, weights_2, weights_zero_2

def relu(z):
    #släpper igenom positiva värden och nollställer negativa värden
    return np.maximum(0, z)

def sigmoid(x):   #Omvandlar tal x till ett värde mellan 0 och 1
    return 1 / (1 + np.exp(-x))

def softmax(z):
    #omvandla nätverkets utsignaler till sannolikheter för de tio siffrorna (0–9)
    exp_z = np.exp(z - np.max(z, axis=1, keepdims=True)) 
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

def hidden_layer_one(X, weights, bias):
    #matrix multi, skickar bara posetiva tal 
    z = np.dot(X, weights) + bias
    a = relu(z)
    #a = sigmoid(z)
    return z,a

def output_layer(X, weights, bias):
    #Alla 0-9 siffror får sanloikheten att vara den rätta siffran, softmax gör så att alla sannolikheter summerar till 1
    z = np.dot(X, weights) + bias
    #a = sigmoid(z)
    a = softmax(z)
    return a    

#Räkna ut förlusten (loss) med hjälp av cross-entropy loss
def compute_loss(Y_hat, Y):
    m = Y.shape[0]
    return -np.sum(Y * np.log(Y_hat + 1e-8)) / m

#Hur många av nätverkets gissningar som är korrekta, jämför nätverkets gissningar (Y_hat) 
# med de faktiska etiketterna (Y) och räkna ut andelen korrekta gissningar.
def accuracy(Y_hat, Y):
    pred_labels = np.argmax(Y_hat, axis=1)
    true_labels = np.argmax(Y, axis=1)
    return np.mean(pred_labels == true_labels)

def printline():
    print("-" * 55)

def printinfo(hidden_neurons, epochs, lerning_rate):

    printline()
    print("      Neural Network Training: Lab 5") 
    printline()
    
    print(f"Settings: Neurons={hidden_neurons}, Epochs={epochs}, Learning Rate={lerning_rate}")
    print("\nTerminology:")
    print("- Loss: The error of the network (Goal: close to 0)")
    print("- Train Accuracy: Accuracy on the training data (Learning)")
    print("- Validation Accuracy: Accuracy on unseen validation data (Generalization)")
    printline()

