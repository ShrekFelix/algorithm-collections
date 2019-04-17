from collections import deque
class Monoqueue:
    def __init__(self):
        self.q = deque()
    def __repr__(self):
        return str([p for p in self.q])
    def get_best(self):
        if not self.q:
            return None
        return self.q[0][0]
    def push(self, val):
        count = 0
        while self.q and val>self.q[-1][0]:
            count += 1 + self.q[-1][1]
            self.q.pop()
        self.q.append([val, count])
    def pop(self):
        if not self.q:
            return None
        if self.q[0][1] > 0:
            self.q[0][1] -= 1
        else:
            self.q.popleft()