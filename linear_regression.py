from math import pi
from qiskit import Aer, execute, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.tools.visualization import plot_histogram


backend = Aer.get_backend('qasm_simulator')

qr = QuantumRegister(4, "qr")
cr = ClassicalRegister(4, "cr")

qc = QuantumCircuit(qr, cr,name="linear_model")

n0 = 0
n1 = 0

for i in range(10):
    qc.x(qr[2])

    qc.h(qr[0])
    qc.h(qr[1])

    qc.u1(pi, qr[0])
    qc.u1(pi/2, qr[1])
    qc.cx(qr[1], qr[2])

    qc.h(qr[0])
    qc.cu1(-pi/2, qr[0], qr[1])
    qc.h(qr[1])

    qc.x(qr[1])
    qc.cu3(pi/16, 0, 0, qr[0], qr[3])
    qc.cu3(pi/8, 0, 0, qr[0], qr[3])

    qc.x(qr[1])
    qc.h(qr[1])
    qc.cu1(pi/2, qr[0], qr[1])
    qc.h(qr[0])

    qc.cx(qr[1], qr[2])
    qc.u1(-pi/2, qr[0])
    qc.u1(-pi, qr[0])

    qc.h(qr[1])
    qc.h(qr[0])

    qc.measure(qr[0], cr[0])
    qc.measure(qr[1], cr[1])
    qc.measure(qr[2], cr[2])
    qc.measure(qr[3], cr[3])

    job = execute(qc, backend, shots=8192)
    result = job.result()

    n0 = n0 + result.get_data("linear_model")['counts']['1000']
    n1 = n1 + result.get_data("linear_model")['counts']['1100']

    print(result)
    print(result.get_data(qc))

    plot_histogram(result.get_counts())

    qc.reset(qr)

    p = n0/n1
    print(n0)
    print(n1)
    print(p)
