import os
import subprocess
from datetime import datetime, timedelta

# Configuración inicial
start_date = datetime(2016, 1, 1)
end_date = datetime.today()
repo_path = "/ruta/a/tu/repositorio"  # Cambia esta ruta al repositorio local

# Cambiar al directorio del repositorio
os.chdir(repo_path)

# Asegúrate de que el repositorio esté inicializado
subprocess.run(["git", "init"], check=True)

# Crear un archivo para simular actividad
file_path = os.path.join(repo_path, "activity_log.txt")

# Generar commits para cada día
current_date = start_date
commit_count = 0

while current_date <= end_date:
    # Escribir algo en el archivo
    with open(file_path, "a") as file:
        file.write(f"Commit del día {current_date.strftime('%Y-%m-%d')}\n")

    # Configurar las fechas de los commits
    date_str = current_date.strftime("%Y-%m-%dT%H:%M:%S")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str

    # Realizar el commit
    subprocess.run(["git", "add", "activity_log.txt"], check=True)
    subprocess.run(
        ["git", "commit", "-m", f"Commit del día {current_date.strftime('%Y-%m-%d')}"],
        env=env,
        check=True,
    )

    # Incrementar la fecha
    current_date += timedelta(days=1)
    commit_count += 1

print(f"Se realizaron {commit_count} commits en el repositorio.")

# Opcional: hacer push al repositorio remoto
remote_repo = "https://github.com/usuario/repositorio.git"  # Cambia esta URL
subprocess.run(["git", "remote", "add", "origin", remote_repo], check=True)
subprocess.run(["git", "branch", "-M", "main"], check=True)
subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
