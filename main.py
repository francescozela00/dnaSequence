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
from keras.models import Sequential
from keras.layers import Dense, Activation



# Use numpy arrays to store inputs (x) and outputs (y):
x = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]]) 

number_of_sequence = randint(5,10)
lenghts = [randint(5,10) for i in range(number_of_sequence)]
def generate_sequence(length=10):
    bases=["A","G","C","T","U","D"]
    sequence=[choice(bases) for i in range(length)]
    sequence=''.join(sequence)
    return sequence




if __name__ == "__main__":

    i = 1

    while i<100: 
        sequences = [generate_sequence(lenght) for lenght in lenghts]
        sequences = ''.join(sequences)


        # Transcrizione da DNA a RNA 
        rnaTransctiption = sequences.maketrans("AGCTUD", "UCGADU")
        result = CurvedDNA(sequences * 5 , 'trifonov', name="DNAGeneratedwithPython")
        result.curvature[:, 18:22]
        result.save_csv('ArtificialDna.csv')
        result.save_pdb('ArtificialDna.pdb')
        result.plot('gif/ArtificialDna-'+str(i)+'.png', dpi=185)
        
        model = Sequential()
        model.add(Dense(2, input_shape=(2,)))
        model.add(Activation('sigmoid'))
        model.add(Dense(1))
        model.add(Activation('sigmoid')) 
        model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy']) 

        # Print a summary of the Keras model:
        model.summary()
        print("DNA:")
        print(sequences)
        print("RNA:")
        print(sequences.translate(rnaTransctiption))
        i+=1




