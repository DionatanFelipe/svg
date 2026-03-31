import os

# entrada via terminal
input_folder = input("Pasta com SVGs: ").strip()
output_folder = input("Pasta de saída: ").strip()
old_color = input("Cor a substituir (ex: #ffffff): ").strip()
target_color = input("Nova cor (ex: #00ff9c): ").strip()

# validações básicas
if not os.path.isdir(input_folder):
    print("❌ Pasta de entrada inválida.")
    exit()

os.makedirs(output_folder, exist_ok=True)

def process_svg(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content_new = content.replace(old_color, target_color)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content_new)

# processamento
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

print("✅ Concluído!")