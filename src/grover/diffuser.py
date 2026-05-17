from qiskit import QuantumCircuit

class Diffuser:
  def __init__(self) -> None:
    pass

  def build(self):
    qc = QuantumCircuit(2, name="Diffuser")

    qc.h([0, 1])

    qc.x([0, 1])

    qc.h(1)
    qc.cx(0, 1)
    qc.h(1)

    qc.x([0, 1])

    qc.h([0, 1])
    return qc

    