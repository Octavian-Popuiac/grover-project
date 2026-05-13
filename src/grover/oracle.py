def build_oracle(marked_state: list): # verificar a cena do marked_state ser uma lista ou um str
  if not isinstance(marked_state, list):
    marked_state = [marked_state]

  num_qubits = len(marked_state[0])
