inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]


weight2 = [[6, 9, 10],
           [3, 4, 0.5]]
biases2 = [2, 0.4]

weight3 = [[1.3], [3.9]]
bias3 = [3]

# Output of current layer
layer1_outputs = []
layer2_outputs = []
final_output = []
prediction = 90
# For each neuron
for neuron_weights, neuron_bias in zip(weights, biases):
    # Zeroed output of given neuron
    neuron_output = 0
    # For each input and weight to the neuron
    for n_input, weight in zip(inputs, neuron_weights):
        # Multiply this input by associated weight
        # and add to the neuron's output variable
        neuron_output += n_input * weight
    # Add bias (once per neuron)
    neuron_output += neuron_bias
    # Put neuron's result into the layer's output list
    layer1_outputs.append(neuron_output)

for neuron2_weights, neuron2_biases in zip(weight2, biases2):
    neuron2_output = 0
    for n_weights2, n_input2 in zip(neuron2_weights, layer1_outputs):
        neuron2_output += n_weights2*n_input2
    neuron2_output += neuron2_biases
    layer2_outputs.append(neuron2_output)

for neuron3_weight, neuron3_bias in zip(weight3, bias3):
    neuron_last = 0
    for n_input_last, n_last_weight in zip(layer2_outputs, neuron3_weight):
        neuron_last += n_input_last*n_last_weight
    neuron_last += neuron3_bias

print("The prediction is: ", prediction ,"\nAnd the output is: " , neuron_last, "Accuracy: ", neuron_last/prediction*100, "%")
