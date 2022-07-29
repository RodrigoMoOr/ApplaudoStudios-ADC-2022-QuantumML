from math import pi
from qiskit import Aer, IBMQ, execute, QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.tools.visualization import plot_histogram

backend = Aer.get_backend('qasm_simulator')
theta_list = [0.01, 0.02, 0.03, 0.04, 0.05, 1.31, 1.32, 1.33, 1.34, 1.35]

qr = QuantumRegister(5, "qr")
cr = ClassicalRegister(5, "cr")

qc = QuantumCircuit(qr, cr, name="k-means")

for i in range(9):
    for j in range(1, 10-i):
        theta_1 = theta_list[i]
        theta_2 = theta_list[i+j]

        qc.h(qr[2])
        qc.h(qr[1])
        qc.h(qr[4])

        qc.u3(theta_1, pi, pi, qr[1])
        qc.u3(theta_1, pi, pi, qr[1])

        qc.cswap(qr[2], qr[1], qr[4])
        qc.h(qr[2])

        qc.measure(qr[2], cr[2])
        qc.reset(qr)

        job = execute(qc, backend, shots=1024)
        result = job.result()

        print(result)
        print('Theta 1: ', str(theta_1))
        print('Theta 2: ', str(theta_2))
        print(result.get_data(qc))

        plot_histogram(result.get_counts())