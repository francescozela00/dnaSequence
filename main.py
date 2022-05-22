"""
    Name: RNAAI 
    Description: Gnerate genome sequence with Nerual Artificial 
    Author: Francesco Zela 
    
"""

import random 
import numpy as np

from numpy import exp, array, random, dot, zeros
from random import randint, choice
from dnacurve import CurvedDNA
from scipy.special import expit as activation_function
from scipy.stats import truncnorm



number_of_sequence = randint(5,10)
lenghts = [randint(5,10) for i in range(number_of_sequence)]
def generate_sequence(length=10):
    bases=["A","G","C","T","U","D"]
    sequence=[choice(bases) for i in range(length)]
    sequence=''.join(sequence)
    return sequence



class NeuralNetwork():
    """
     That Nerual network i want to be contected to gnerate a good sequence of 
     dna to generate more complex rna structures.
    """
    def __init__(self, 
                 no_of_in_nodes, 
                 no_of_out_nodes, 
                 no_of_hidden_nodes,
                 learning_rate):
        self.no_of_in_nodes = no_of_in_nodes
        self.no_of_out_nodes = no_of_out_nodes
        self.no_of_hidden_nodes = no_of_hidden_nodes
        self.learning_rate = learning_rate 
        self.create_weight_matrices()
        
    def create_weight_matrices(self):
        """ A method to initialize the weight matrices of the neural network"""
        rad = 1 / np.sqrt(self.no_of_in_nodes)
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_in_hidden = X.rvs((self.no_of_hidden_nodes, 
                                       self.no_of_in_nodes))
        rad = 1 / np.sqrt(self.no_of_hidden_nodes)
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_hidden_out = X.rvs((self.no_of_out_nodes, 
                                        self.no_of_hidden_nodes))

    def train(self, input_vector, target_vector):
        pass # More work is needed to train the network
            
    def run(self, input_vector):
        """
        running the network with an input vector 'input_vector'. 
        'input_vector' can be tuple, list or ndarray
        """
        # Turn the input vector into a column vector:
        input_vector = np.array(input_vector, ndmin=2).T
        # activation_function() implements the expit function,
        # which is an implementation of the sigmoid function:
        input_hidden = activation_function(self.weights_in_hidden @   input_vector)
        output_vector = activation_function(self.weights_hidden_out @ input_hidden)
        return output_vector     



if __name__ == "__main__":
    # Inizialize  Nerual Network 


    sequences = [generate_sequence(lenght) for lenght in lenghts]
    sequences = ''.join(sequences)
    print("DNA:")
    print(sequences)
    # Transcrizione da DNA a RNA 
    rnaTransctiption = sequences.maketrans("AGCTUD", "UCGADU")
    print("RNA:")
    print(sequences.translate(rnaTransctiption))
    result = CurvedDNA(sequences * 5 , 'trifonov', name="DNAGeneratedwithPython")
    result.curvature[:, 18:22]
    result.save_csv('3_test.csv')
    result.save_pdb('3_test.pdb')
    result.plot('3_test.png', dpi=185)

    simple_network = NeuralNetwork(no_of_in_nodes=sequences, 
                                no_of_out_nodes=sequences.translate(rnaTransctiption), 
                                no_of_hidden_nodes=4,
                                learning_rate=0.6)
    
    simple_network.run([(3,4)])
