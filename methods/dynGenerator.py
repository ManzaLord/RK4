def dyn_generator(oper, state):
    """Evalúa la función que representa al sistema dinámico a partir de una matriz de estado y un operador lineal definidos.
    
    Examples:
        >>> oper = np.array([[0, 1], [1, 0]])
        >>> state = np.array([[1, 0], [0, 0]])
        >>> result = dyn_generator(oper, state)
        array([[0. - 0.j, 0. + 1.j],[0. - 1.j, 0. - 0.j]])

    Args:
        oper (numpy.ndarray): Operador lineal que modifica el estado.
        state (numpy.ndarray): Matriz que representa cantidades físicas en el sistema.

    Returns:
        (numpy.ndarray): Resultado de la conmutación entre el operador y el estado, multiplicado por -i.
    
    """
    result = -1.0j * (np.dot(oper,state) - np.dot(state,oper))

    return result
