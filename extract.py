from pathlib import Path
from zipfile import ZipFile
import rarfile

rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\UnRAR.exe"

import shutil


def unique_path(path: Path) -> Path:
    """Return a unique filename by appending _1, _2, etc."""
    if not path.exists():
        return path

    stem = path.stem
    suffix = path.suffix
    counter = 1

    while True:
        candidate = path.with_name(f"{stem}_{counter}{suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def extract_archive(archive_path: Path, output_dir: Path):
    output_dir.mkdir(exist_ok=True)

    if archive_path.suffix.lower() == ".zip":
        archive = ZipFile(archive_path, "r")
    elif archive_path.suffix.lower() == ".rar":
        archive = rarfile.RarFile(archive_path)
    else:
        raise ValueError("Unsupported archive format.")

    extracted = 0

    with archive:
        for member in archive.infolist():

            # Ignore folders
            if member.is_dir():
                continue

            filename = Path(member.filename).name

            # Ignore empty names
            if not filename:
                continue

            destination = unique_path(output_dir / filename)

            with archive.open(member) as src, open(destination, "wb") as dst:
                shutil.copyfileobj(src, dst)

            extracted += 1
            print(f"[{extracted}] {destination.name}")

    print(f"\nDone! Extracted {extracted} files.")


if __name__ == "__main__":
    current_folder = Path(__file__).parent

    # Find the first ZIP/RAR in the current folder
    archives = list(current_folder.glob("*.rar")) + list(current_folder.glob("*.zip"))

    if not archives:
        print("No ZIP or RAR archive found in this folder.")
        exit()

    archive = archives[0]
    output = current_folder / "output"

    print(f"Archive : {archive.name}")
    print(f"Output  : {output}")

    extract_archive(archive, output)