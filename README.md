# Acessible-Lliure


# 1. **Introducción**
Acessible Lliure es una plataforma de herramientas libres y descentralizadas diseñadas específicamente para personas neurodivergente (Autistas, TDAH o divergentes atencionales, down, dislexia...), discapacidad visual y cognitiva, física, movilidad reducida o condición de cualquier tipo. 

Actualmente, estas personas dependen de herramientas propietarias (ecosistemas cerrados de Big Tech) para gestionar aspectos críticos de su autonomía diaria, como la medicación, las rutinas o la lectura. Esta dependencia implica una cesión masiva de datos sensibles de salud y hábitos personales a corporaciones cuyo modelo de negocio se basa en la extracción y monetización de información.
Nuestra propuesta: Una alternativa Open Source, Local-First (los datos viven en el dispositivo del usuario) y accesible radicalmente (WCAG 2.2 AA). Devolvemos la soberanía digital a quienes más lo necesitan, eliminando la vigilancia algorítmica y garantizando la continuidad del servicio independientemente de las decisiones comerciales de grandes tecnológicas.

#2. **La Vulnerabilidad Doble**
Las personas con las problemáticas planteadas enfrentan una doble brecha:
Brecha de Accesibilidad: Necesitan tecnología asistencial para participar plenamente en sociedad.
Brecha de Privacidad: Al usar las pocas herramientas disponibles (suelen ser apps móviles populares), entregan datos extremadamente sensibles (ubicación exacta, horarios médicos, estado emocional, interacciones sociales) a servidores opacos.
Para una persona de estas características estos datos son aún más delicados, ya que revelan patrones de comportamiento y necesidades de apoyo constantes. En manos de terceros comerciales, esto representa un riesgo de discriminación, profilaxis indebida o simplemente explotación publicitaria.

##2.1 **Falta de Alternativas Éticas**
Existen lectores de pantalla y recordatorios, pero casi todos están integrados en sistemas operativos propietarios o requieren cuentas en la nube centralizada. No existe en el mercado hispanohablante una solución integral, gratuita, auditable y sin rastreo, pensada desde el diseño inclusivo (Design for Accessibility).

#3. **Herramienta de punto de partida**
Tamagochi retro. Funcionalidades Principales:
- Autenticación Local: La autenticación será local, almacenando los datos del usuario en el dispositivo del usuario, asegurando la privacidad y la seguridad de los datos personales.
- Recompensa Gamificada: El usuario puede ganar estrellas por realizar tareas diarias, lo que puede traducirse en decoraciones o bonificaciones dentro de la plataforma.
- Interfaz Retro: La interfaz de usuario será inspirada en los Tamagochis retro, lo que puede ser más accesible y familiar para algunas personas neurodivergentes.
- Accesibilidad Avanzada:Cumplir con estándares WCAG 2.2 AA para garantizar la accesibilidad total, lo que incluye alternativas de texto para los sonidos y opciones de tamaño de fuente.

(Funcionalidad futura) Lector de Texto Offline: Motor de síntesis de voz local (sin enviar audio a la nube).
(Funcionalidad futura) Organizador Visual de Tareas: Interfaz simplificada, baja carga sensorial, compatible con lectores de pantalla.
(Funcionalidad futura): A medida que avance el proyecto, iremos proponiendo de forma constante con la colaboración de stake-holders de colaboración voluntaria que testearán la plataforma y nos darán ideas sobre necesidades reales que se vayan descubriendo, así como las mismas que durante el proyecto vayan surgiendo. 
Arquitectura Local-First: Implementar bases de datos locales cifradas. La sincronización entre dispositivos (si se activa) será End-to-End Encrypted (E2EE) y opcional.

- Accesibilidad Radical: Cumplir WCAG 2.2 nivel AA desde la primera línea de código. Realizar pruebas de usabilidad con colectivos reales de discapacidad.
- Soberanía Lingüística: Diseñar la arquitectura para facilitar la localización inmediata en catalán y castellano, y más adelante en gallego y euskera, promoviendo la diversidad lingüística en el entorno digital.


4. # Mapeo de testeo ético #

Realizaremos un Análisis Competitivo Ético:
- Entrevistaremos a usuarios actuales para saber qué apps usan realmente.
- Analizaremos los permisos de acceso de dichas apps (qué datos piden y para qué).
- Publicaremos un informe abierto ("Informe de Vigilancia en Herramientas Asistenciales") que servirá como justificación técnica de por qué necesitamos construir alternativas.
Ese informe alimentará directamente el Product Backlog inicial: las funciones más críticas y con mayor riesgo de privacidad pasarán a ser los primeros Sprints.

# 5. PLAN DE TRABAJO A 6 MESES (Roadmap Agile)
Este plan se divide en fases macro, pero dentro de cada fase ejecutaremos sprints 1 vez a la semana.
MES 1: FASE PUNTO DE PARTIDA
Sprint 1: Reclutamiento de usuarios testers voluntarios y firma de consentimientos éticos. Inicio de entrevistas cualitativas. (ya en marcha, personas voluntarias van entregando feedback)
Sprint 2: Reclutamiento de personas que colaboren con la idea de crear un equipo técnico consolidado con una metodología AGILE SCRUM (ya en marcha, se están realizando reuniones semanales)
MES 2: FASE DE INVESTIGACIÓN
 Análisis técnico de las apps propietarias dominantes. Documentación de permisos invasivos. Redacción del "Informe de Vigilancia".
Informe público de análisis de riesgos de privacidad en apps de accesibilidad actuales + Definición del Product Backlog prioritario.
MES 3-6: FASE DE DESARROLLO MVP (Minimum Viable Product)
Sprint 3: Arquitectura base (stack tecnológico local-first, configuración de repositorio Git, CI/CD básico).
Sprint 4: Desarrollo Autenticación Local
Sprint 5. Recompensa Gamificada.
Sprint 6: Interfaz Retro. 
Sprint 7: Accesibilidad Avanzada
Sprint 8: Creación de lector de Texto Local 
Sprint 9: Integración de funcioanlidades, pruebas de rendimiento y seguridad inicial.
Entregable MVP instalable. Código fuente publicado en GitHub/Forgejo.

*Transversal*
Redacción de documentación técnica para desarrolladores (API, arquitectura) y manual de usuario final (guías visuales y en vídeo accesibles).
Testing con personas usuarias finales reales. Registro de bugs y mejoras de UX. Corrección de fallos críticos y ajuste de interfaz según feedback (ej. tamaños de letra, contraste, flujos de navegación).
Preparación de materiales de divulgación, presentación final al financiador y apertura de canal de soporte comunitario.
Entregable Final: Plataforma operativa, documentación completa, memoria técnica del proceso Agile y reporte de impacto inicial.

# 5. METODOLOGÍA TÉCNICA Y ÉTICA
Se trabajará bajo los principios rectores de Xnet (infraestructura libre, redes comunitarias) y Accent Obert (cultura digital crítica):
Código Abierto y Auditable: Todo el código fuente estará publicado en un repositorio federado permitiendo que cualquier experto pueda auditar la seguridad y privacidad.
Zero-Knowledge by Design: No recogeremos ningún dato analítico. No habrá cookies, trackers ni perfiles de usuario.
Autosuficiencia Tecnológica: La plataforma podrá ser autoalojada (self-hosted) por entidades públicas o asociaciones.
Participación Comunitaria: Las potencionales personas usurias no son "clientela", son co-diseñadores. Su feedback en las Sprint Reviews determina el roadmap futuro.

# 6. IMPACTO Y PERSONAS BENEFICIARIAS
Personas beneficiarias directas: personas neurodivergente (Autistas, TDAH o divergentes atencionales, down, dislexia...), discapacidad visual y cognitiva, física, movilidad reducida o condición de cualquier tipo.
Personas beneficiarias indirectas: Familias, cuidadores, profesionales de la educación/salud, instituciones públicas y privadas, entidades sociales.
Impacto Social: Demostrar que la innovación tecnológica puede ser ética, humana y democrática. Romper el paradigma de que "para ser útil hay que vender datos".
Escalabilidad: Al ser software libre, otras regiones o países pueden clonar y adaptar la plataforma a sus necesidades específicas sin pagar licencias.


# 7. Estructura del Proyecto
```
accessible-lliure/
├── backend/
│   ├── controllers/
│   │   ├── authController.js
│   │   ├── taskController.js
│   │   ├── decorationController.js
│   ├── models/
│   │   ├── user.js
│   │   ├── task.js
│   │   ├── decoration.js
│   ├── routes/
│   │   ├── authRoutes.js
│   │   ├── taskRoutes.js
│   │   ├── decorationRoutes.js
│   ├── middleware/
│   │   ├── authMiddleware.js
│   ├── app.js
│   ├── config.js
│   ├── server.js
├── frontend/
│   ├── public/
│   │   ├── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── TaskList.js
│   │   │   ├── DecorationList.js
│   │   ├── pages/
│   │   │   ├── Home.js
│   │   │   ├── TaskPage.js
│   │   ├── App.js
│   │   ├── index.js
│   ├── package.json
│   ├── webpack.config.js
├── .gitignore
├── package.json
├── README.md
```
