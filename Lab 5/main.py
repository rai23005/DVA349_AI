
from ann import ann

def main():


    hidden_neurons = 64
    epochs=70
    learning_rate=0.2

    ann(hidden_neurons, epochs, learning_rate)


if __name__ == "__main__":

    main()