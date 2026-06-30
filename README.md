<div align="center">

<img src="./terminal_header.svg" alt="Brayan Clavijo — Terminal Profile" width="680"/>

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/brayan-camilo-clavijo-gomez-07538a152/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:bclavijogomez@gmail.com)
[![Portafolio](https://img.shields.io/badge/Portafolio-111827?style=flat-square&logo=vercel&logoColor=white)](https://brayan-clavijo.vercel.app)
![Visitas](https://komarev.com/ghpvc/?username=BrayanClavijo&style=flat-square&color=3fb950&label=visitas)

</div>

---

## whoami

```bash
$ cat dev.profile
```

```
nombre     : Brayan Camilo Clavijo Gómez
rol        : Mobile & Backend Developer
exp        : +2 años en producción
stack      : Flutter · Django · PostgreSQL · AWS
base       : Villavicencio, Colombia 🇨🇴
docencia   : Arquitectura de Software con Microservicios @ universidad
enfoque    : código que escala, no solo que funciona en el demo
```

Construyo aplicaciones reales — sincronización offline, notificaciones en tiempo real, autenticación robusta, dashboards con datos reales. No prototipos de presentación.

```
filosofía:
  → código mantenible > código inteligente
  → arquitecturas que escalan sin romper
  → documentación como parte del código, no como extra
```

---

## stack

### mobile
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white)
![Dart](https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=dart&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black)
![Provider](https://img.shields.io/badge/Provider-607D8B?style=flat-square&logoColor=white)
![BLoC](https://img.shields.io/badge/BLoC-13B9FD?style=flat-square&logoColor=white)
![GetX](https://img.shields.io/badge/GetX-8B0000?style=flat-square&logoColor=white)
![Google Maps](https://img.shields.io/badge/Google_Maps-4285F4?style=flat-square&logo=googlemaps&logoColor=white)

### backend
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-ff1709?style=flat-square&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=celery&logoColor=white)

### infra & devops
![AWS](https://img.shields.io/badge/AWS-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white)

---

## arquitectura que manejo

```
Mobile (Flutter)                    Backend (Django)
────────────────────────            ──────────────────────────
Clean Architecture          ←→      REST API + DRF
BLoC / GetX / Provider              JWT + refresh token rotation
Offline-first (SQLite)              PostgreSQL + migrations
Push Notifications                  Celery (tareas async + beat)
Google Maps SDK                     AWS S3 + EC2
Firebase Auth / Storage             Nginx + Gunicorn

CI/CD                               Observabilidad
────────────────────────            ──────────────────────────
GitHub Actions                      Logs estructurados
Docker multi-stage builds           Health checks por servicio
Deploy automatizado en push         Variables de entorno por env
```

---

## proyectos en producción

### Chilasi — reporte de emergencias en tiempo real

App móvil para reporte y gestión de emergencias. Diseñada para funcionar en zonas sin conexión.

```
problema   : coordinación lenta en emergencias por dependencia de señal
solución   : app offline-first con sincronización automática al reconectar
resultado  : reportes en < 3 taps · actualizaciones en vivo para coordinadores
```

**decisiones técnicas relevantes:**
- SQLite local con cola de sincronización priorizada por criticidad
- WebSocket para actualizaciones en tiempo real cuando hay señal
- Google Maps con tiles cacheados para zonas sin internet
- Push notifications segmentadas por rol (coordinador / campo)

`Flutter` `Dart` `Firebase` `Google Maps` `SQLite` `Provider` `WebSocket`

---

### AFI Asesorías Plus — gestión de calidad en salud

Plataforma para el sector salud y farmacéutico. Automatiza seguimiento regulatorio, riesgo farmacéutico y planes de mejoramiento.

```
problema   : seguimiento manual de registros INVIMA y permisos sanitarios
solución   : sistema automatizado con alertas, dashboards y app companion
resultado  : reducción de tareas manuales en gestión de calidad institucional
```

**decisiones técnicas relevantes:**
- Celery Beat para alertas programadas de vencimientos regulatorios
- DRF con permisos por módulo (calidad / riesgo / mejoramiento)
- Dashboard con reportes exportables en PDF y Excel
- App Flutter companion para acceso en campo sin abrir el navegador
- AWS S3 para almacenamiento de documentos regulatorios

`Django` `DRF` `PostgreSQL` `Flutter` `Celery` `AWS` `Push Notifications`

---

## repos con estrella

<!-- STARRED_START -->
| repositorio | descripción | lenguaje | stats |
|-------------|-------------|----------|-------|
| [Api-Rest-Spring-boot](https://github.com/clavijo99/Api-Rest-Spring-boot) |  | ![Java](https://img.shields.io/badge/-Java-B07219?style=flat-square&logoColor=white) | ⭐ 1 |
| [POO-ParcialF-project](https://github.com/YefrxxJPG/POO-ParcialF-project) |  | ![Java](https://img.shields.io/badge/-Java-B07219?style=flat-square&logoColor=white) | ⭐ 1 |
| [Project](https://github.com/yesicablum/Project) |  | ![JavaScript](https://img.shields.io/badge/-JavaScript-F1E05A?style=flat-square&logoColor=white) | ⭐ 2 |
| [sample_application_flutter](https://github.com/JeanmartinPV/sample_application_flutter) |  | ![Dart](https://img.shields.io/badge/-Dart-00B4AB?style=flat-square&logoColor=white) | ⭐ 78 · 🍴 26 |
| [flutter-samples](https://github.com/diegoveloper/flutter-samples) | Flutter Samples | ![Dart](https://img.shields.io/badge/-Dart-00B4AB?style=flat-square&logoColor=white) | ⭐ 3211 · 🍴 739 |
| [flutter_side_menu_animation](https://github.com/diegoveloper/flutter_side_menu_animation) |  | ![Dart](https://img.shields.io/badge/-Dart-00B4AB?style=flat-square&logoColor=white) | ⭐ 56 · 🍴 15 |
| [portfolio](https://github.com/diegobrice/portfolio) |  | ![HTML](https://img.shields.io/badge/-HTML-E34C26?style=flat-square&logoColor=white) | ⭐ 6 |
| [emmanuel-mendez-react](https://github.com/emmanuel-mendez/emmanuel-mendez-react) | Emmanuel Méndez portfolio | ![SCSS](https://img.shields.io/badge/-SCSS-888888?style=flat-square&logoColor=white) | ⭐ 2 |
| [flutter_network_layer](https://github.com/Richa0305/flutter_network_layer) |  | ![Dart](https://img.shields.io/badge/-Dart-00B4AB?style=flat-square&logoColor=white) | ⭐ 23 · 🍴 8 |
| [Welcome-Login-Signup-Page-Flutter](https://github.com/abuanwar072/Welcome-Login-Signup-Page-Flutter) | Mobile app onboarding, Login, Signup page with #flutter. | ![Dart](https://img.shields.io/badge/-Dart-00B4AB?style=flat-square&logoColor=white) | ⭐ 1338 · 🍴 862 |
<!-- STARRED_END -->

---

## stats

<div align="center">

<img height="180em" src="https://github-readme-stats.vercel.app/api?username=BrayanClavijo&show_icons=true&theme=github_dark&hide_border=true&include_all_commits=true&count_private=true&bg_color=0d1117&title_color=58a6ff&icon_color=3fb950&text_color=c9d1d9" />
<img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=BrayanClavijo&layout=compact&theme=github_dark&hide_border=true&langs_count=8&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9" />

</div>

<div align="center">

<img src="https://github-readme-streak-stats.herokuapp.com/?user=BrayanClavijo&theme=github-dark-blue&hide_border=true&background=0d1117&ring=58a6ff&fire=3fb950&currStreakLabel=58a6ff" />

</div>

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=BrayanClavijo&theme=github-compact&hide_border=true&bg_color=0d1117&color=58a6ff&line=3fb950&point=ffffff&area=true&area_color=3fb95020" />

</div>

---

## aprendiendo ahora

```bash
$ git log --oneline --learning
```

```
[en curso]  FastAPI       → microservicios más rápidos que DRF para endpoints de alta carga
[en curso]  Riverpod      → reemplazo de Provider con mejor manejo de estado reactivo
[explorando] Kafka        → event streaming para arquitecturas desacopladas
[explorando] Kubernetes   → orquestación cuando Docker Compose no escala
```

---

## contacto

Si tienes un proyecto en mente, buscas dev para tu equipo o quieres hablar de arquitectura:

<div align="center">

[![LinkedIn](https://img.shields.io/badge/Conectemos_en_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/brayan-camilo-clavijo-gomez-07538a152/)
[![Portafolio](https://img.shields.io/badge/Ver_Portafolio-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://brayan-clavijo.vercel.app)
[![Email](https://img.shields.io/badge/Enviar_Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:bclavijogomez@gmail.com)

</div>

<div align="center">

*disponible para proyectos freelance · remoto · Colombia*

</div>