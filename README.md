# Archive Flattener

A lightweight Python utility that extracts all files from ZIP and RAR archives into a single output directory while automatically preserving duplicate filenames.

Instead of recreating the original folder structure, this tool flattens the archive and renames duplicate files so that nothing is overwritten.

## Features

- Supports both ZIP and RAR archives
- Flattens nested directory structures
- Automatically renames duplicate filenames
- Preserves every file without overwriting
- Streams file extraction for efficient memory usage
- Automatically creates the output directory

## Example

### Archive Structure

```
Archive.rar
├── Folder A
│   ├── image.png
│   └── report.pdf
├── Folder B
│   ├── image.png
│   └── report.pdf
└── Folder C
    └── image.png
```

### Output

```
output/
├── image.png
├── image_1.png
├── image_2.png
├── report.pdf
└── report_1.pdf
```

No files are overwritten.

---

## Requirements

- Python 3.8+
- `rarfile`

Install the dependency:

```bash
pip install rarfile
```

---

## WinRAR Configuration (RAR Only)

If you're extracting RAR archives, the `rarfile` package requires an extraction backend.

If WinRAR is installed at:

```
C:\Program Files\WinRAR
```

add the following after importing `rarfile`:

```python
import rarfile

rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\UnRAR.exe"
```

---

## Project Structure

```
root/
│
├── demo.rar
├── extract.py
└── output/
```

The script automatically detects the first ZIP or RAR archive located in the same directory.

---

## Usage

Run the script:

```bash
python extract.py
```

or

```bash
py extract.py
```

The script will:

1. Detect the archive
2. Create an `output` directory
3. Extract every file
4. Ignore all folders
5. Rename duplicate filenames automatically

---

## Duplicate File Handling

If multiple files share the same filename, they are renamed automatically.

Example:

```
resume.pdf
resume_1.pdf
resume_2.pdf
```

This ensures that every file from the archive is preserved.

---

## Supported Formats

- ZIP
- RAR

---

## License

MIT License
