```mermaid
flowchart TD
    A([Inicio]) --> B[Entradas:<br>200 CV<br>Perfiles de candidatos]
    
    subgraph C [Caja Negra - Proceso Interno]
        D[Revisión curricular] --> E{Aprobado?}
        E -->|No| F[Descarte]
        E -->|Sí| G[Pruebas técnicas]
        G --> H{Aprobado?}
        H -->|No| F
        H -->|Sí| I[Entrevistas]
        I --> J{Aprobado?}
        J -->|No| F
        J -->|Sí| K[Deliberación del comité]
    end
    
    B --> C
    K --> L[Salidas:<br>10 candidatos seleccionados<br>Evaluación de desempeño]
    L --> M([Fin])
    F --> M
