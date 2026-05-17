from qiskit import QuantumCircuit
from qiskit.circuit.library import grover_operator, MCMTGate, ZGate
from qiskit_aer import AerSimulator
from qiskit import transpile

from simple_oracle import SimpleOracle
from diffuser import Diffuser

import matplotlib.pyplot as plt

def simulate_circuit(qc):
  simulator = AerSimulator()
  compiled_circuit = transpile(qc, simulator)
  result = simulator.run(compiled_circuit, shots=1024).result()
  counts = result.get_counts()
  print(counts)

def apply_hadamard(qc, qubits):
  for qubit in qubits:
    qc.h(qubit)

def build_grover_circuit(marked_state):
  qc = QuantumCircuit(2)

  # Step 1: Superposition
  apply_hadamard(qc, [0, 1])

  # Step 2: Oracle
  oracle = SimpleOracle(marked_state=marked_state)
  qc.compose(oracle.build(), inplace=True)
  # oracle.draw(output="mpl")

  # Step 3: Diffuser
  diffuser = Diffuser()
  qc.compose(diffuser.build(), inplace=True)

  # Step 4: Measurement
  qc.measure_all()
  return qc

if __name__ == "__main__":
  marked_state = "01"
  circuit = build_grover_circuit(marked_state=marked_state)
  
  circuit.draw(output="mpl", style="iqp")
  plt.show()

  simulate_circuit(circuit)