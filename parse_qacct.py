"""
Parse a given qacct file and load it into the database.
"""
import argparse
import pprint

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sge_dashboard.settings")

from dashboard.models import Job


def parse_qacct(qacct_filename):
    """

    """
    jobs = []
    job = None

    with open(qacct_filename, "r") as qacct_fh:
        for line in qacct_fh:
            if line.startswith("Total System Usage"):
                # The last record is followed by a summary of all usage.
                break
            elif line.startswith("="):
                # New records start with a full line of =.
                if job is not None:
                    jobs.append(job)

                job = Job()
            else:
                pieces = line.strip().split(" ")

                # Ignore empty keys.
                if pieces[0] != "":
                    try:
                        # Cast all values to integers if possible.
                        setattr(job, pieces[0], int(pieces[-1]))
                    except ValueError:
                        # Otherwise, keep values as strings.
                        setattr(job, pieces[0], pieces[-1])

    Job.objects.bulk_create(jobs)
    pprint.pprint(jobs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("qacct_filename")
    args = parser.parse_args()

    parse_qacct(args.qacct_filename)
