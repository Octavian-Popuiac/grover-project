from qiskit import QuantumCircuit

class SimpleOracle:
  def __init__(self, marked_state):
    self.marked_state = marked_state
    self.num_qubits = len(marked_state)

    self.qc = QuantumCircuit(
      self.num_qubits,
      name=f"Oracle {self.marked_state}"
    )

  def build(self):
    reversed_state = self.marked_state[::-1]

    for qubit, bit in enumerate(reversed_state):
      if bit == "0":
        self.qc.x(qubit)

    self.qc.cz(0, 1)

    for qubit, bit in enumerate(reversed_state):
      if bit == "0":
        self.qc.x(qubit)
        
    return self.qc

  def draw(self, output="mpl"):
    return self.qc.draw(output=output)
