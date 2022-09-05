import os
import mdutils
import csv
import itertools

import file_paths as fp
from build_utils import configure_logger

logger = configure_logger(__name__)


def build_restricted_lists() -> None:
    restricted_value_files = [
        i
        for i in os.listdir(fp.RESTRICTED_VALS_SOURCE_DIR)
        if os.path.isfile(os.path.join(fp.RESTRICTED_VALS_SOURCE_DIR, i))
        and os.path.splitext(os.path.join(fp.RESTRICTED_VALS_SOURCE_DIR, i))[1]
        == ".csv"
    ]

    logger.info(f"restricted value files found: {len(restricted_value_files)}")

    mdfile = mdutils.MdUtils(file_name=fp.RESTRICTED_VALS_PATH, author="Samuel Elkind")
    mdfile.new_header(1, title="Restricted Values")

    for file_name in restricted_value_files:
        mdfile.new_line("")
        with open(os.path.join(fp.RESTRICTED_VALS_SOURCE_DIR, file_name), "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            field_name = header[0]

            mdfile.new_header(2, title=field_name)

            col_count = len(header)
            fields = header
            fields.extend(itertools.chain.from_iterable(reader))

            mdfile.new_table(
                columns=col_count,
                rows=int(len(fields) / col_count),
                text=fields,
                text_align="left",
            )

    mdfile.create_md_file()


def main():
    build_restricted_lists()


if __name__ == "__main__":
    main()
