from npc.types import CNF, Assignment, Clause

def _evaluate_assignment(variables: Assignment) -> dict[str, bool]:
    values = {}
    for v in variables:
        if v.startswith('!'):
            values[v[1:]] = False
        else:
            values[v] = True
    return values

def _evaluate_clause(clause: Clause, values: dict[str, bool]) -> bool:
    res = False
    for v in clause:
        if v.startswith('!'):
            val = not values[v[1:]]
        else:
            val = values[v]
        res = res or val
        if res == True: return True
    return res

def verify_solution(cnf: CNF, variables: Assignment, K: int) -> bool:
    cnt = 0
    print(f"Verifying assignment: {variables}")
    values = _evaluate_assignment(variables)
    for clause in cnf:
        if not (val := _evaluate_clause(clause, values)):
            print(f"{clause} is unsatisfied")
            cnt += 1
            if cnt > K: return False
    return cnt == K


def input_transformation(cnf: CNF) -> tuple[CNF, int]:
    # SAT input to k-SAT input transformation
    return cnf, 0


def output_transformation(variables: Assignment | None) -> Assignment | None:
    # k-SAT output to SAT output transformation
    return variables
