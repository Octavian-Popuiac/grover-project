from qiskit import QuantumCircuit
from simple_oracle import build_simple_oracle
import matplotlib.pyplot as plt

def run_simple_oracle():
  """
  Build and return the simple oracle circuit.
  """

  oracle = build_simple_oracle()
  return oracle

if __name__ == "__main__":
  oracle = run_simple_oracle()

  print(oracle)

  oracle.draw("mpl")
  plt.show()