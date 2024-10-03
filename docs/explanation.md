# Explicación del método

El método RK4 se utiliza para aproximar la solución a un paso temporal $h$ en el futuro, denotada por $y_{n+1}$, como función de la solución en el tiempo anterior $y_n$. Tenemos:

\begin{equation}
    y_{n+1} \rightarrow y_n + \dfrac{1}{6}(k_1 + 2k_2 + 2k_3  + k_4)
\end{equation}

donde

$$k_1 = h f\left(t_n,y_n\right)$$

$$k_2 = h f\left(t_n+\dfrac{h}{2},y_n+k_1\right)$$

$$k_3 = h f\left(t_n+\dfrac{h}{2},y_n+k_2\right)$$

$$k_4 = h f\left(t_n+\dfrac{h}{2},y_n+k_3\right)$$

y $t_n$ corresponde al tiempo en el punto donde la solución es $y_n$.

