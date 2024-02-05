# Utiliza una imagen base de Python
FROM python:3.9.12

# Establece el directorio de trabajo en el contenedor
WORKDIR /app                                    

# Copia los archivos de requerimientos y luego instala las dependencias
COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
#RUN pip install --no-cache-dir --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host=files.pythonhosted.org -r requirements.txt

# Copia el código de la aplicación al contenedor
COPY . .

# Configura las variables de entorno (si es necesario)
# ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
