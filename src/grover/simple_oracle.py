from qiskit import QuantumCircuit

def build_simple_oracle():
  """
  Simple Grover oracle for 2 qubits.

  Marks the state |11> by applying a phase flip:
    |11> -> -|11>
  
  Returns:
    QuantumCircuit: Oracle Circuit.
  """
  qc = QuantumCircuit(2, name="Manual Oracle")

  # Apply controlled-Z gate 
  # This flips the phase of the |11> state
  qc.cz(0, 1)
  return qc