import shutil
import os
import sys

def main(file_path, extract_dir, verbose):
  if file_path == '':
    print('filename must be set.')
    sys.exit(1)
  if extract_dir == '':
    extract_dir = '.'
  verbose = verbose.lower() == 'true'

  if verbose:
    print('Inputs => file_path:{}, extract_dir:{}, verbose:{}'.format(file_path, extract_dir, verbose))

  try:
    shutil.unpack_archive(file_path, extract_dir)
    print('Sucessfully unpacked.')
  except Exception as error:
    print('Failed to unpack file: {0}. {1}.'.format(file_path, error))
    sys.exit(2)


if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2], sys.argv[3])
