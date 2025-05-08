import numpy as np


class State:
    def __init__(self, vector):
        if not isinstance(vector, np.ndarray):
            raise ValueError("상태 벡터는 numpy 배열이어야 합니다.")
        self.vector = vector

    def __repr__(self):
        return f"State({self.vector})"

    def normalize(self):
        norm = np.linalg.norm(self.vector)
        if norm == 0:
            raise ValueError("제로 벡터는 정규화할 수 없습니다.")
        self.vector = self.vector / norm

    def inner_product(self, other_state):
        if not isinstance(other_state, State):
            raise ValueError("다른 상태는 State 객체여야 합니다.")
        return np.vdot(self.vector, other_state.vector)

    def probability(self, other_state):
        inner_prod = self.inner_product(other_state)
        return abs(inner_prod) ** 2
