import os

def generate_readme():
    readme_content = "# Wallpapers Repository\n\n"
    readme_content += "This repository contains the following images:\n\n"
    
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                # Get the relative path of the image
                image_path = os.path.join(root, file).replace("\\", "/")
                readme_content += f"![{file}]({image_path})\n\n"
    
    # Write the content to README.md
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    generate_readme()

