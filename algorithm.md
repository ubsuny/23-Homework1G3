# Algorithm to implement division function using qiskit.
1. Import qiskit library into our program to create and run quantam program.
 
3. Create new quantum circuit with 3 qubits to provide a variety of methods for adding quantam gates and measurements to the circuits.

4. Apply Hardamard gate to qubit 0 of the quantum circuit which is a single qubit gate that puts the qubit into an equal superposition of states |0> 
and |1>.

5. Apply Hardmard gate to qubit 1 of the quantum circuit.

6. Apply Hardmard gate to qubit 2 of the quantum circuit.

7. Apply the Controlled Xgate to qubits 1 and 2 of the quantum circuit such that it flips the target qubit if and only if the control qubit is in the state |1>.

8. Apply the controlled Xgate also known as CNOT gate to qubits o and 2 of the quantum circuit qc.

9. Measure the qubits 2,1 and 0 of the quantum circuit and store the results in classical bits 2, 1 and 0 respectively.

10. Visualize the circuit

...
11. Test the rest in your local computer and assign job to server qunatum computer.

