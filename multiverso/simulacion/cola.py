class Cola:
    def __init__(self) -> None:
        self.elementos = []

    def push(self, elemento )-> None:
        """Añade un elemento al final de la cola."""
        self.elementos.append(elemento)

    def pop(self) -> any:
        """Elimina y devuelve el primer elemento de la cola."""
        if not self.elementos:
            raise IndexError("La cola está vacía.")
        return self.elementos.pop(0)
    
    def is_empty(self) -> bool:
        """Verifica si la cola está vacía."""
        return len(self.elementos) == 0
    
    def __str__(self) -> str:
        """Representación en cadena de la cola."""
        return f"Cola({self.elementos})"