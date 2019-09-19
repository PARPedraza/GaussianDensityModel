====================
Gaussian Density Model
====================

We proposes a novel and robust 3D object segmentation method,  the Gaussian Density Model (GDM) algorithm. The algorithm works with point clouds scanned in the urban environment using the density metrics, based on existing quantity of features in the neighborhood. The LiDAR Velodyne 64E was used to scan urban environment.
==============================================================

Versión 1
  * Login
  * Importación de CSV a MySQL
  * Exportación de MySQL a CSV
  * Alta de nuevos registros y evaluaciones
  * Administración de Usuarios
  * Reporte General
  * Reporte Individual
  * Exportación de Reportes a PDF

Versión 2
  * Optimización y validación de código
  * Catálogos

Módulos requeridos:
====================

  * MySQL-Workbench
  * MySQL-Server
  * Sublimetext    : https://www.sublimetext.com/3
  * XAMPP          : https://www.apachefriends.org/download.html

Instalación XAMPP y MySQL:
==============================
XAMPP

1.- Descargar la versión 5.6.36 (Probada)

2.- 
``$ cd al archivo``

3.- 
``$ chmod 755 xampp-linux-x64-5.6.36-0-installer.run``

4.- 
``$ sudo ./xampp-linux-x64-5.6.36-0-installer.run``

5.- Instalar siguiente, siguiente, finalizar y se abrirá XAMPP.

Ejecutar/Parar Servidor Apache

1.- 
``$ sudo /opt/lampp/lampp start``

2.- 
``$ sudo /opt/lampp/lampp stop``

Abrir Xampp IDE

1.- 
``$ cd /opt/lampp``

2.- 
``$ sudo ./manager-linux-x64.run``

Copiar Carpetas a /opt/lampp/htdocs

1.- 
``$ sudo su``

2.- 
``$ sudo cp -r Documentos/Base_De_Datos/csv /opt/lampp/htdocs``

Listo! Ejecutar tu servidor

Puertos en uso:

 * Puerto 80
 * HTTP 443

Instalación MySQL

1.- 
``$ sudo apt-get install mysql-workbench``

2.- 
``$ sudo apt-get install mysql-server``

3.- Al abrir workbench el signo + te permitirá agregar una nueva conexión, coloca el nombre de tu conexión y da clic en administración de la configuración del servidor.

5.- Next, ingresas la contraseña que deseas tenga el servidor, Next, seleccionas el OS Linux Ubuntu Linux (Vendor Package), Next, Next, Finalizar y clic en OK. 

Listo carga o diseña tu base de datos!!!

CARGAR LA BASE DE DATOS

1.- En Management -> Data Import/Restore -> Import from Self-Contained File (buscr tu .sql) -> en el Default target schema da clic en New y coloca el nombre de tu esquema -> Finalmente da clic en Stt Import.

¡Listo!  haz importado tú .sql de manera correcta.


Ejemplo:
========

Abre explorador preferentemente chrome

``> localhost/biopsicosocial``

  .. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3
