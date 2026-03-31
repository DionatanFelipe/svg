
## Objetivo

Este projeto permite **alterar cores de arquivos SVG em múltiplas pastas de forma otimizada**.
São dois scripts disponíveis:

1. **MudarCorSVG.ipynb** – Para ser rodado no **modo Jupyter Notebook**, com instruções internas.
2. **Mudarsvg.py** – Para ser rodado via terminal com `python3 Mudarsvg.py`, solicitando interativamente:

   * Pasta com os arquivos SVG
   * Cor que deseja substituir
   * Cor de substituição

---

##  Requisitos

* Python 3 instalado
* Editor de código ou Jupyter Notebook (se for usar o `.ipynb`)
* Pastas com arquivos `.svg` organizadas

Como usar

### **Modo Notebook**

1. Abra **MudarCorSVG.ipynb** no Jupyter Notebook.
2. Siga as instruções dentro do notebook para configurar as pastas e cores.
3. Execute as células e veja os arquivos modificados na pasta de saída.

### **Modo Terminal**

1. Abra o terminal ou prompt de comando.
2. Execute:

   ```bash
   python3 Mudarsvg.py
   ```
3. Informe os dados solicitados:

   * Caminho da pasta com SVGs
   * Cor que deseja substituir
   * Cor de substituição

O script processará todas as pastas e arquivos, criando subpastas equivalentes na pasta de saída.

---
Observações

* O script **não altera os arquivos originais**, ele cria uma cópia modificada na pasta de saída.
* Você pode adicionar mais cores a substituir modificando a linha:

  ```python
  content_new = content.replace('#ffffff', target_color).replace('#000000', target_color)
  ```
* Ideal para **lotes grandes de SVGs**, mantendo a organização das pastas.

------------------------------------------------------------------------------------------------------------




## Detailed Guide – Change Color of SVG Files in Multiple Folders (Python)**
 Purpose

This project allows you to **change colors in SVG files across multiple folders efficiently**.
Two scripts are available:

1. **MudarCorSVG.ipynb** – Run in **Jupyter Notebook** mode with internal instructions.
2. **Mudarsvg.py** – Run via terminal with `python3 Mudarsvg.py`, asking for:

   * Folder containing SVG files
   * Color to replace
   * Replacement color

---
Requirements

* Python 3 installed
* Code editor or Jupyter Notebook (if using `.ipynb`)
* Folders containing `.svg` files

---
How to Use

### **Notebook Mode**

1. Open **MudarCorSVG.ipynb** in Jupyter Notebook.
2. Follow instructions inside the notebook to set folders and colors.
3. Run the cells and check the modified files in the output folder.

### **Terminal Mode**

1. Open terminal/command prompt.
2. Run:

   ```bash
   python3 Mudarsvg.py
   ```
3. Enter requested information:

   * Folder with SVG files
   * Color to replace
   * Replacement color

The script will process all folders and files, creating matching subfolders in the output folder.

---
 Notes

* The script **does not modify original files**, it saves a copy in the output folder.
* You can replace multiple colors by modifying:

  ```python
  content_new = content.replace('#ffffff', target_color).replace('#000000', target_color)
  ```
* Ideal for **large batches of SVGs**, keeping folder structure intact.

------------------------------------------------------------------------------------------------------------





## Guía Detallada – Cambiar Color de Archivos SVG en Múltiples Carpetas (Python)**

 Objetivo

Este proyecto permite **cambiar colores de archivos SVG en múltiples carpetas de manera eficiente**.
Hay dos scripts disponibles:

1. **MudarCorSVG.ipynb** – Ejecutar en **modo Jupyter Notebook**, con instrucciones internas.
2. **Mudarsvg.py** – Ejecutar desde terminal con `python3 Mudarsvg.py`, solicitando:

   * Carpeta con archivos SVG
   * Color a reemplazar
   * Color de reemplazo

---

Requisitos

* Python 3 instalado
* Editor de código o Jupyter Notebook (si usa `.ipynb`)
* Carpetas con archivos `.svg` organizadas

---
 Cómo Usar

### **Modo Notebook**

1. Abre **MudarCorSVG.ipynb** en Jupyter Notebook.
2. Sigue las instrucciones internas para configurar carpetas y colores.
3. Ejecuta las celdas y revisa los archivos modificados en la carpeta de salida.

### **Modo Terminal**

1. Abre terminal o símbolo del sistema.
2. Ejecuta:

   ```bash
   python3 Mudarsvg.py
   ```
3. Ingresa la información solicitada:

   * Carpeta con archivos SVG
   * Color a reemplazar
   * Color de reemplazo

El script procesará todas las carpetas y archivos, creando subcarpetas equivalentes en la carpeta de salida.

---
 Observaciones

* El script **no modifica los archivos originales**, guarda una copia modificada en la carpeta de salida.
* Se pueden reemplazar múltiples colores agregando más `.replace()`:

  ```python
  content_new = content.replace('#ffffff', target_color).replace('#000000', target_color)
  ```
* Ideal para **lotes grandes de SVGs**, manteniendo la estructura de carpetas.

-------------------------------------------------------------------------------------------

PS: WINDOS TERMINAL

Introdução ao Terminal/Prompt de Comando (Windows)**

Se você nunca usou o terminal no Windows, ele é chamado **Prompt de Comando** ou **PowerShell** e serve para executar comandos como rodar scripts Python.

### Como abrir:

1. Pressione `Win + R`, digite `cmd` e pressione Enter → abre o **Prompt de Comando**.
   Ou digite `PowerShell` para abrir o PowerShell.

2. Navegue até a pasta onde está o script usando o comando `cd`.
   Exemplo:

   ```bat
   cd C:\Users\SeuUsuario\Documentos\ProjetosSVG
   ```

3. Rode o script com Python:

   ```bat
   python Mudarsvg.py
   ```

   ou, se estiver usando Python 3:

   ```bat
   python3 Mudarsvg.py
   ```

> ⚠️ Dica: Se aparecer um erro dizendo que `python` não é reconhecido, significa que o Python não está adicionado ao PATH. Neste caso, instale Python 3 e marque a opção **“Add Python to PATH”** na instalação.

---

Introduction to Terminal / Command Prompt (Windows)**

If you have never used the terminal on Windows, it is called **Command Prompt** or **PowerShell**. It is used to run commands, like executing Python scripts.

### How to open:

1. Press `Win + R`, type `cmd` and hit Enter → opens **Command Prompt**.
   Or type `PowerShell` to open PowerShell.

2. Navigate to the folder where your script is using `cd`:

   ```bat
   cd C:\Users\YourUser\Documents\SVGProjects
   ```

3. Run the script with Python:

   ```bat
   python Mudarsvg.py
   ```

   or if using Python 3:

   ```bat
   python3 Mudarsvg.py
   ```

> ⚠️ Tip: If you see an error saying `python` is not recognized, Python is not added to PATH. Install Python 3 and check **“Add Python to PATH”** during installation.

---

Introducción al Terminal / Símbolo del Sistema (Windows)**

Si nunca has usado el terminal en Windows, se llama **Símbolo del Sistema** o **PowerShell** y se usa para ejecutar comandos, como correr scripts de Python.

### Cómo abrir:

1. Presiona `Win + R`, escribe `cmd` y presiona Enter → abre el **Símbolo del Sistema**.
   O escribe `PowerShell` para abrir PowerShell.

2. Navega a la carpeta donde está tu script usando `cd`:

   ```bat
   cd C:\Users\TuUsuario\Documentos\ProyectosSVG
   ```

3. Ejecuta el script con Python:

   ```bat
   python Mudarsvg.py
   ```

   o si usas Python 3:

   ```bat
   python3 Mudarsvg.py
   ```

> ⚠️ Consejo: Si aparece un error que dice `python` no reconocido, significa que Python no está agregado al PATH. Instala Python 3 y marca la opción **“Add Python to PATH”** durante la instalación.
