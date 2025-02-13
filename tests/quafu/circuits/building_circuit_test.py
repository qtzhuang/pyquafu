import quafu.elements.element_gates as qeg
from quafu.circuits import QuantumCircuit


class TestBuildingCircuit:
    def test_add(self):
        q = QuantumCircuit(3)
        q << (qeg.XGate(1))
        q << (qeg.CXGate(0, 2))
        q << (qeg.RXGate(0, 0.1))
        q << (qeg.XGate(2)).ctrl_by([0])
        q << qeg.RZZGate(0, 2, 0.26)
        try:
            nq = q.add_controls(2)
        except NotImplementedError:
            nq = q
        nq.draw_circuit()
        nq.to_openqasm()


if __name__ == '__main__':
    test = TestBuildingCircuit()
    test.test_add()
