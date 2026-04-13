from npc.types import CNF, Assignment, Clause
import logging

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

def _get_variables(cnf: CNF) -> set[str]:
    variables = set()
    for clause in cnf:
        for v in clause:
            if v.startswith('!'):
                variables.add(v[1:])
            else:
                variables.add(v)
    return variables

def verify_solution(cnf: CNF, variables: Assignment, K: int) -> bool:
    cnt = 0
    # logging.info(f"Verifying assignment: {variables}")
    vars = _get_variables(cnf)
    values = _evaluate_assignment(variables)
    if len(values) != len(variables):
        # logging("Invalid assignment: duplicate variables with different values")
        return False
    if set(values.keys()) != vars:
        # logging.warning("Invalid assignment: missing variables")
        return False
    for clause in cnf:
        if not (val := _evaluate_clause(clause, values)):
            # logging.info(f"{clause} is unsatisfied")
            cnt += 1
            if cnt > K: return False
    return cnt == K


def input_transformation(cnf: CNF) -> tuple[CNF, int]:
    # SAT input to k-SAT input transformation
    literal1 = 'AUX'
    literal2 = '!AUX'
    out = [*cnf, {literal1}, {literal2}]
    return out, 1


def output_transformation(variables: Assignment | None) -> Assignment | None:
    # k-SAT output to SAT output transformation
    return variables.difference({'AUX', '!AUX'}) if variables is not None else None
