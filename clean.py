import os
import shutil


def clear_folder(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(e)
        shutil.rmtree(folder_path)


def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f'Failed to delete {file_path}. Reason: {e}')

def process(base_path):
    for prod_path in os.listdir(base_path):
        full_path = os.path.join(base_path, prod_path)
        if prod_path[0] != "_" and os.path.isdir(full_path):
            for ver_path in os.listdir(full_path):
                full_path = os.path.join(base_path, prod_path, ver_path)
                if os.path.isdir(full_path):
                    templates_folder = os.path.join(full_path, '_templates')
                    static_folder = os.path.join(full_path, '_static')
                    conf_path = os.path.join(full_path, 'conf.py')
                    clear_folder(templates_folder)
                    clear_folder(static_folder)
                    delete_file(conf_path)

if __name__ == "__main__":
    doc_folder = './doc'
    process(doc_folder)
    clear_folder(os.path.join(doc_folder, '_build'))
