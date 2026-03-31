import os

# entrada por terminal
input_folder = input("Carpeta con SVGs: ").strip()
output_folder = input("Carpeta de salida: ").strip()
old_color = input("Color a reemplazar (ej: #ffffff): ").strip()
target_color = input("Nuevo color (ej: #00ff9c): ").strip()

# validaciones básicas
if not os.path.isdir(input_folder):
    print("❌ Carpeta de entrada inválida.")
    exit()

os.makedirs(output_folder, exist_ok=True)

def process_svg(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content_new = content.replace(old_color, target_color)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content_new)

# procesamiento
for root_dir, dirs, files in os.walk(input_folder):
    rel_path = os.path.relpath(root_dir, input_folder)
    output_subfolder = os.path.join(output_folder, rel_path)
    os.makedirs(output_subfolder, exist_ok=True)

    for file in files:
        if file.lower().endswith('.svg'):
            input_file = os.path.join(root_dir, file)
            output_file = os.path.join(output_subfolder, file)
            process_svg(input_file, output_file)
            print(f"✔ {output_file}")

print("✅ ¡Proceso completado!")