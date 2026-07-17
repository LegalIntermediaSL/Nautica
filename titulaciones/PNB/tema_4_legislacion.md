---
title: "Tema 4: Legislación Marítima y Análisis Jurídico"
description: "Marco normativo, teoría del derecho marítimo y responsabilidades legales para embarcaciones de recreo."
---

# Tema 4: Legislación Marítima y Análisis Jurídico

El marco legal que rige las atribuciones del Patrón de Navegación Básica se inscribe en el ámbito del Derecho Administrativo Sancionador y del Derecho Marítimo Internacional. El análisis de estas normas se aborda desde la lógica de la teoría de conjuntos y la teoría de decisiones.

## Dominio de Aplicación Normativa

Definamos el conjunto de embarcaciones $E$ y el conjunto de atribuciones $A$. Para la titulación PNB, el dominio de atribuciones se define como:

$$
A_{PNB} = \{ x \in E \mid L(x) \le 8\text{ m} \land \text{Dist}(x) \le 5\text{ millas} \}
$$

Donde $L(x)$ es la eslora de la embarcación y $\text{Dist}(x)$ la distancia a un puerto, marina o lugar de abrigo. 
Cualquier evento de navegación $N$ que verifique $N \notin A_{PNB}$ incurre en una infracción grave según el régimen sancionador de la Ley de Puertos del Estado y de la Marina Mercante.

### Jerarquía Normativa

```mermaid
graph TD;
    CNUDM[Convención de las Naciones Unidas sobre el Derecho del Mar] --> Ley_Navegacion[Ley de Navegación Marítima 14/2014];
    Ley_Navegacion --> RD_875[RD 875/2014 Titulaciones de Recreo];
    RD_875 --> Resoluciones[Resoluciones de la DGMM];
```

## Prevención de Contaminación (MARPOL)

La ecuación de la dilución de efluentes en el medio marino para la zona de descargas permitidas se puede modelizar estocásticamente, pero el anexo V de MARPOL establece un régimen absoluto de "cero vertidos" de plásticos:

$$
\forall t, V_{plastico}(t) = 0
$$

La probabilidad $P$ de una sanción por contaminación accidental frente a negligencia se evalúa mediante la carga de la prueba, donde el patrón asume responsabilidad objetiva por el buque.

## Ejemplos Prácticos

### Problema 1: Inferencia Lógica de Sanciones
Un patrón de PNB es avistado navegando en un buque a motor a una distancia rectilínea $D_p = \sqrt{x^2 + y^2}$ desde un refugio. Las coordenadas de la embarcación respecto al refugio son $(x=4\text{ millas}, y=3.5\text{ millas})$.
1. Determine matemáticamente si existe infracción de las atribuciones del PNB.

**Solución:**
1. Cálculo de la distancia euclídea al lugar de abrigo:
$$
D_p = \sqrt{4^2 + 3.5^2} = \sqrt{16 + 12.25} = \sqrt{28.25} \approx 5.315\text{ millas}
$$
2. Verificación de la condición de atribución:
Condición: $D_p \le 5\text{ millas}$.
Evaluación: $5.315 \le 5$ es FALSO.
Conclusión: $\exists$ Infracción administrativa por superar la distancia de 5 millas de un abrigo, violando las atribuciones conferidas por el RD 875/2014.

## Referencias Bibliográficas y Jurisprudencia

- Ley 14/2014, de 24 de julio, de Navegación Marítima.
- Real Decreto 875/2014, de 10 de octubre, de titulaciones náuticas para embarcaciones de recreo.
- Convenio Internacional para prevenir la contaminación por los buques (MARPOL 73/78).
- Texto Refundido de la Ley de Puertos del Estado y de la Marina Mercante (TRLPEMM, RDL 2/2011).
