import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import GeomapDocs.build_bibliography
import GeomapDocs.build_faults_field_glossary
import GeomapDocs.build_field_value_files
import GeomapDocs.build_field_glossary
import GeomapDocs.build_qualityinfo_field_glossary
import GeomapDocs.build_source_field_glossary
from GeomapDocs.build_utils import download_data


def main():
    os.system('make clean')
    download_data()
    GeomapDocs.build_bibliography.main()
    GeomapDocs.build_faults_field_glossary.main()

    # order matters here, field_glossary depends on field value file existence
    GeomapDocs.build_field_value_files.main()
    GeomapDocs.build_field_glossary.main()

    GeomapDocs.build_qualityinfo_field_glossary.main()
    GeomapDocs.build_source_field_glossary.main()

    os.system('make html')
    os.system('make latexpdf')


if __name__ == '__main__':
    main()
