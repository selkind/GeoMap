import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import src.build_bibliography
import src.build_faults_field_glossary
import src.build_field_value_files
import src.build_field_glossary
import src.build_qualityinfo_field_glossary
import src.build_source_field_glossary
from src.build_utils import download_data


def main():
    os.system('make clean')
    download_data()
    src.build_bibliography.main()
    src.build_faults_field_glossary.main()

    # order matters here, field_glossary depends on field value file existence
    src.build_field_value_files.main()
    src.build_field_glossary.main()

    src.build_qualityinfo_field_glossary.main()
    src.build_source_field_glossary.main()

    os.system('make html')
    os.system('make latexpdf')


if __name__ == '__main__':
    main()
