from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Operator
from qiskit import Aer

unknownnumber = '001010'

circuit = QuantumCircuit(6+1,6)

q_sim = Aer.get_backend('q_simulator')

circuit.h([0,1,2,3,4,5])

#turning 6th qubit into superposed
circuit.h(6)

#switching 6th qubit
circuit.x(6)

circuit.cx(3, 6)

circuit.cx(1, 6)

circuit.measure([0,1,2,3,4,5], [0,1,2,3,4,5])



estimation = q_sim.run(circuit)

results = estimation.result()

sol_counts = results.get_counts()


print(sol_counts)

if sol_counts == '01010':
    print("bruh the unknown number got solved aint no way")

    matrice = Operator(circuit(3,1))


    #Printing out the matrice data for the qubits

    print(matrice.data)



