def analyze_relation(set_elements, relation):
    """
    Analyze a relation to determine its properties and compute closures.

    :param set_elements: A set of elements, e.g., {'a', 'b', 'c'}
    :param relation: A set of tuples representing the relation, e.g., {('a', 'a'), ('a', 'b')}
    """
    # Check Reflexive
    reflexive = all((x, x) in relation for x in set_elements)
    antireflexive = all((x, x) not in relation for x in set_elements)

    # Check Symmetric
    symmetric = all((b, a) in relation for (a, b) in relation)
    antisymmetric = all((b, a) not in relation or a == b for (a, b) in relation)

    # Check Transitive
    transitive = all((a, c) in relation for (a, b) in relation for (x, c) in relation if b == x)

    # Reflexive closure
    reflexive_closure = relation | {(x, x) for x in set_elements}

    # Symmetric closure
    symmetric_closure = relation | {(b, a) for (a, b) in relation}

    # Transitive closure (using Warshall's algorithm-like approach)
    transitive_closure = set(relation)
    for a in set_elements:
        for b in set_elements:
            for c in set_elements:
                if (a, b) in transitive_closure and (b, c) in transitive_closure:
                    transitive_closure.add((a, c))

    # Print results
    print("Relation:", relation)
    print("Reflexive:", reflexive)
    print("Antireflexive:", antireflexive)
    print("Symmetric:", symmetric)
    print("Antisymmetric:", antisymmetric)
    print("Transitive:", transitive)
    print("Reflexive Closure:", reflexive_closure)
    print("Symmetric Closure:", symmetric_closure)
    print("Transitive Closure:", transitive_closure)


# Example usage
set_elements = {'a', 'b', 'c'}
relation = {('a', 'b'),("b","b"), ('a', 'a'), ('a', 'c'), ("b","c"),("c","b"),("c","c")}  # Replace with your relation
analyze_relation(set_elements, relation)
