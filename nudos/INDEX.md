# Nudos Náuticos

En la mar, un nudo mal hecho no solo es un inconveniente, puede ser un peligro mortal. Un buen nudo náutico se define por tres características: es fácil de hacer, cumple su función a la perfección sin escurrirse, y **es fácil de deshacer incluso después de haber estado sometido a gran tensión**.

```mermaid
flowchart TD
    Nudos(Tipos de Nudos Náuticos) --> Amarre
    Nudos --> Union
    Nudos --> Tope
    Nudos --> Otros
    
    Amarre(De Amarre<br>Fijar a un objeto)
    Amarre --> As(As de Guía)
    Amarre --> Ballestrinque(Ballestrinque)
    Amarre --> Cornamusa(Vuelta de Cornamusa)
    Amarre --> Rezon(Vuelta de Rezón)
    Amarre --> Braza(Vuelta de Braza)
    
    Union(De Unión / Ayuste<br>Unir dos cabos)
    Union --> Llano(Nudo Llano)
    Union --> Escota(Nudo de Escota)
    Union --> Pescador(Pescador)
    Union --> Carrick(Carrick)
    
    Tope(De Tope<br>Evitar que un cabo escape)
    Tope --> Ocho(Nudo en Ocho)
    
    Otros(Especiales<br>Acortar o tensar)
    Otros --> Margarita(Margarita)
    
    style Nudos fill:#bbdefb,stroke:#1976d2,stroke-width:2px
    style Amarre fill:#c8e6c9,stroke:#388e3c
    style Union fill:#ffecb3,stroke:#fbc02d
    style Tope fill:#ffcdd2,stroke:#d32f2f
    style Otros fill:#e1bee7,stroke:#8e24aa
```

## Clasificación Principal

Hemos dividido los nudos en cuatro categorías principales para facilitar su estudio:

1.  **[Nudos de Amarre](AMARRE.md)**: Sirven para hacer firme un cabo a un objeto (cornamusa, noray, argolla, mástil). *Ej: As de Guía, Ballestrinque.*
2.  **[Nudos de Unión (Ayustes)](UNION.md)**: Sirven para unir dos cabos entre sí, ya sean del mismo o de distinto grosor. *Ej: Nudo Llano, Nudo de Escota.*
3.  **[Nudos de Tope](TOPE.md)**: Se hacen al final del cabo para evitar que se escape por una polea o pasacabos. *Ej: Nudo en Ocho.*
4.  **[Nudos Especiales (Otros)](OTROS.md)**: Nudos para acortar cabos, hacer tensores o aislar zonas dañadas. *Ej: Nudo de Margarita.*
