from zipfile import ZipFile, ZIP_DEFLATED
import os
def test_zip_archive():
    path = "tmp_files"   # папка, откуда берём файлы
    files = os.listdir(path)
    archive_path = os.path.join("resources", "files_arc.zip")

    # создаем папку, если ее нет
    if not os.path.exists("resources"):
            os.mkdir("resources")

    with ZipFile(archive_path, "w", compression=ZIP_DEFLATED) as archive:
        for item in files:
            file_path = os.path.join(path, item)
            archive.write(file_path, arcname=item)
