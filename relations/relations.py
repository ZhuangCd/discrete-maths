# Define the set of elements and the set of relations as inputs.
base_set = {"a", "b", "c", "d"}
relations = {
    ("1","2"),
    ("2", "1"),
    ("2","3"),
    ("2", "4"),
    ("3","2"),
}  # Sample relation set


def is_reflexive(base_set: set[int], relations: set[tuple[int, int]]) -> bool:
    """Check if a relation relations on set base_set is reflexive."""
    for a in base_set:
        if (a, a) not in relations:
            return False
    return True


def is_symmetric(relations: set[tuple[int, int]]) -> bool:
    """Check if a relation relations is symmetric."""
    for a, b in relations:
        if (b, a) not in relations:
            return False
    return True


def is_antisymmetric(relations: set[tuple[int, int]]) -> bool:
    """Check if a relation relations is antisymmetric."""
    for a, b in relations:
        if (a != b) and ((b, a) in relations):
            return False
    return True


def is_transitive(relations: set[tuple[int, int]]) -> bool:
    """Check if a relation relations is transitive."""
    for a, b in relations:
        for c, d in relations:
            if b == c and (a, d) not in relations:
                return False
    return True

#reflexive, symmetric, and transitive Equivalence relations

def is_equivalence(base_set,relations) -> bool:
    if is_reflexive(base_set,relations) and is_symmetric(relations) and (is_transitive(relations)):
        return True
    return False

def is_partial_order(base_set, relations) -> bool:
    return (
        is_reflexive(base_set, relations)
        and is_antisymmetric(relations)
        and is_transitive(relations)
    )


def is_comparable(base_set, relations):
    # Check all pairs (a, b) in the base_set
    for a in base_set:
        for b in base_set:
            if a != b:
                # Check if either (a, b) or (b, a) is in relations
                if (a, b) not in relations and (b, a) not in relations:
                    # If neither pair is present, a and b are not comparable
                    return False

    # If all pairs are comparable, return True
    return True


def is_total_ordered(base_set, relations) -> bool:
    is_partial_ordered = is_partial_order(base_set, relations)
    is_every_pair_comparable = is_comparable(base_set, relations)
    return is_every_pair_comparable and is_partial_ordered


def reflexsive_closure(
    base_set, relations: set[tuple[int, int]]
) -> set[tuple[int, int]]:
    missing_relations = set()
    for a in base_set:
        if (a, a) not in relations:
            missing_relations.add((a, a))

    print(f"The missing relations added are: {missing_relations}")
    return missing_relations.union(relations)


def symmetric_closure(relations: set[tuple[int, int]]) -> set[tuple[int, int]]:
    missing_relations = set()
    for a, b in relations:
        if (a, b) in relations and (b, a) not in relations:
            missing_relations.add((b, a))

    print(f"The missing relations added are: {missing_relations}")
    return missing_relations.union(relations)


def antisymmetric_closure(relations: set[tuple[int, int]]) -> set[tuple[int, int]]:
    # note that antisymmetric closures only work by subtraction
    # antisymmetric closures cannot be additive closures like the other closure types
    antisymmetric_relations = relations.copy()
    # Iterate over each pair in the set of relations
    for a, b in antisymmetric_relations:
        # Check if both (a, b) and (b, a) exist, and a != b
        if (b, a) in antisymmetric_relations and a != b:
            # Remove one of the symmetric pairs; here we remove (b, a)
            antisymmetric_relations.remove((b, a))

    print(
        f"The relations removed in order to make the set antisymmetric are: {
    relations.difference(antisymmetric_relations)}"
    )
    return antisymmetric_relations


def transitive_closure(relations: set[tuple[int, int]]) -> set[tuple[int, int]]:
    missing_relations = set()
    for a, b in relations:
        for b, c in relations:
            if (a, b) in relations and (b, c) in relations and (a, c) not in relations:
                missing_relations.add((a, c))

    print(f"The missing relations added are: {missing_relations}")
    return missing_relations.union(relations)

# with it self, fx R^2 or R^3
def relation_composition_with_it_self(relation, n):
    """
    Calculate the n-th composition of a relation with itself fx R^2 or R^3
    Just adjust n to be the exponent

    Args:
        relation (set of tuple): A set of ordered pairs representing the relation.
        n (int): The number of compositions.

    Returns:
        set of tuple: The resulting set of ordered pairs after n compositions.
    """
    composed_relation = relation  # Start with the base relation
    for _ in range(n - 1):  # Perform n-1 compositions
        new_composed_relation = set()
        for (a, b) in composed_relation:
            for (c, d) in relation:
                if b == c:
                    new_composed_relation.add((a, d))
        composed_relation = new_composed_relation
    return composed_relation


# Fx R1 o R2
def relation_composition_with_another(R1, R2):
    """
    Calculate the composition of two relations, R1 and R2.

    Args:
        R1 (set of tuple): The first relation (a set of ordered pairs).
        R2 (set of tuple): The second relation (a set of ordered pairs).

    Returns:
        set of tuple: The resulting set of ordered pairs after composition.
    """
    composed_relation = set()
    for (a, b) in R1:
        for (c, d) in R2:
            if b == c:
                composed_relation.add((a, d))
    return composed_relation

print(relation_composition_with_another(relations, relations))
