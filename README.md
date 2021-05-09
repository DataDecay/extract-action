# extract-action

Github Action to extract a various format archive file, and it works on any platform. This action is powered by python's `shutil.unpack_archive`, and probably lightweight because it works without docker build.

## Supported format

- zip
- tar
- tar.gz (tgz)
- tar.bz2 (tbz2)
- tar.xz (txz)

## Usage

```yaml
      - name: Extract tgz
        uses: ihiroky/extract-action@v1
        with:
          file_path: path_to_archive_file
          extract_dir: path_to_extract_directory
```

If you set like [this](https://github.com/ihiroky/extract-action/blob/main/.github/workflows/test.yml), `tmp/zip/hoge/fuga/file` and `tmp/zip/file` is extracted from `tmp/a.zip` for example.

### Arguments

- file_path (required)

  File path to extract.

- extract_dir (optional, default: `'.'`)

  Directory path to extract archive.

- verbose: (optional, default: `false`)

  Shows details about the result of running this action.
