from npc.types import CNF, Assignment, Clause


def verify_solution(cnf: CNF, variables: Assignment, K: int) -> bool:
    # Validate: no conflicting assignments (e.g. both 'x1' and '!x1')
    var_names = set()
    for v in variables:
        name = v[1:] if v[0] == '!' else v
        if name in var_names:
            return False
        var_names.add(name)

    # Check assignment covers exactly the variables in the CNF
    cnf_vars = set()
    for clause in cnf:
        for lit in clause:
            cnf_vars.add(lit[1:] if lit[0] == '!' else lit)
    if var_names != cnf_vars:
        return False

    # Count unsatisfied clauses using fast C-level set operation.
    # A clause is satisfied iff it shares a literal with the assignment.
    # isdisjoint() == True means no shared literals → clause is unsatisfied
    cnt = 0
    for clause in cnf:
        if clause.isdisjoint(variables):
            cnt += 1
            if cnt > K:
                return False
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
