def rk4(func, oper, state, h):
    """Aplica el método de Runge-Kutta de cuarto orden (RK4).

    Examples:
        >>> oper = np.array([[0, 1], [1, 0]])
        >>> state = np.array([[1, 0], [0, 0]])
        >>> rk4(dyn_generator, oper, state, 0.1)
        array([[0.99003333 + 0.j, 0. + 0.09933333j],[0. - 0.09933333j, 0.00996667 + 0.j]])
    
    Args:
        func (callable): Función que representa la dinámica del sistema.
        oper (numpy.ndarray): Operador lineal que modifica el estado.
        state (numpy.ndarray): Matriz que representa cantidades fisicas del sistema.
        h (float): Paso temporal del sistema.

    Returns:
        (numpy.ndarray): El nuevo estado del sistema al aplicar un paso del método RK4.

    """
    k1 = h*func(oper,state)
    k2 = h*func(oper,state + (0.5*k1))
    k3 = h*func(oper,state + (0.5*k2))
    k4 = h*func(oper,state + k3)

    return state + ((k1 + 2*k2 + 2*k3 + k4)/6)
