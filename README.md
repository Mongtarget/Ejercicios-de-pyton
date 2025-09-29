flowchart TD
    A([🚀 Inicio]) --> B[[📥 Entradas:<br>200 CV<br>Perfiles de candidatos]]
    
    subgraph C [⚙️ Caja Negra - Proceso Interno]
        style C fill:#f2f2f2,stroke:#333,stroke-width:1px

        D([📄 Revisión curricular]) --> E{❓ ¿Aprobado?}
        E -->|❌ No| F([🗑️ Descarte])
        E -->|✔️ Sí| G([📝 Pruebas técnicas])
        G --> H{❓ ¿Aprobado?}
        H -->|❌ No| F
        H -->|✔️ Sí| I([💬 Entrevistas])
        I --> J{❓ ¿Aprobado?}
        J -->|❌ No| F
        J -->|✔️ Sí| K([👥 Deliberación del comité])
    end
    
    B --> C
    K --> L[[📤 Salidas:<br>10 candidatos seleccionados<br>Evaluación de desempeño]]
    L --> M([🏁 Fin])
    F --> M

    %% 🎨 Estilos
    classDef startEnd fill:#4CAF50,color:#fff,stroke:#2e7d32,stroke-width:2px;
    classDef inputOutput fill:#2196F3,color:#fff,stroke:#0d47a1,stroke-width:2px;
    classDef process fill:#FFEB3B,color:#000,stroke:#fbc02d,stroke-width:2px;
    classDef decision fill:#FF5722,color:#fff,stroke:#bf360c,stroke-width:2px;
    classDef discard fill:#9E9E9E,color:#fff,stroke:#424242,stroke-width:2px;

    %% Aplicación de estilos
    class A,M startEnd
    class B,L inputOutput
    class D,G,I,K process
    class E,H,J decision
    class F discard

