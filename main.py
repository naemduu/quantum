import quantum as q
import numpy as np

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


    # 양자 상태 벡터 생성
    state_0 = q.State(np.array([1, 0]))  # |0> 상태
    state_1 = q.State(np.array([0, 1]))  # |1> 상태

    # 상태 정규화
    state_0.normalize()
    state_1.normalize()

    # 내적 계산
    print("내적:", state_0.inner_product(state_1))

    # 확률 밀도 계산
    print("확률 밀도:", state_0.probability(state_1))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
