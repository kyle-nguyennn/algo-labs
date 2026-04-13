from npc.types import CNF, Assignment, Clause

def _evaluate_assignment(variables: Assignment) -> dict[str, bool]:
    values = {}
    for v in variables:
        if v.startsWith('!'):
            values[v] = False
        else:
            values[v] = True
    return values

def _evaluate_clause(clause: Clause, values: dict[str, bool]) -> bool:
    res = False
    for v in clause:
        if v.startsWith('!'):
            val = not values[v]
        else:
            val = values[v]
        res = res or val
        if res == True: return True
    return res

def verify_solution(cnf: CNF, variables: Assignment, K: int) -> bool:
    cnt = 0
    values = _evaluate_assignment(variables)
    for clause in cnf:
        if _evaluate_clause(clause, values):
            cnt += 1
            if cnt > K: return False
    return cnt == K


def input_transformation(cnf: CNF) -> tuple[CNF, int]:
    pass


def output_transformation(variables: Assignment | None) -> Assignment | None:
    pass
