import os
import shutil
import subprocess


def copy_file(src, dest):
    if os.path.exists(dest):
        os.remove(dest)
    shutil.copy(src, dest)


def copy_folders(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def process(doc_folder, config_folder):
    templates_folder = os.path.join(config_folder, '_templates')
    static_folder = os.path.join(config_folder, '_static')
    conf_path = os.path.join(config_folder, 'conf.py')
    for prod_path in os.listdir(doc_folder): # traverse products
        full_path = os.path.join(doc_folder, prod_path)
        if prod_path[0] != "_" and os.path.isdir(full_path):
            for ver_path in os.listdir(full_path): # traverse versions
                full_path = os.path.join(doc_folder, prod_path, ver_path)
                if os.path.isdir(full_path):
                    copy_folders(templates_folder, os.path.join(full_path, '_templates'))
                    copy_folders(static_folder, os.path.join(full_path, '_static'))
                    copy_file(conf_path, os.path.join(full_path, 'conf.py'))
                pv_path = str(os.path.join(prod_path, ver_path))
                command = f'cd .\doc && sphinx-build -b html {pv_path} _build\html\{pv_path}'
                subprocess.run(command, shell=True)
              

if __name__ == "__main__":
    doc_folder = './doc'
    config_folder = './config'
    process(doc_folder, config_folder)
