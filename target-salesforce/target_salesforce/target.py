"""Salesforce target class."""

from __future__ import annotations

from singer_sdk.target_base import Target
from singer_sdk import typing as th

from target_salesforce.sinks import (
    SalesforceSink,
)


class TargetSalesforce(Target):
    """Sample target for Salesforce."""

    name = "target-salesforce"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "filepath",
            th.StringType,
            description="The path to the target output file"
        ),
        th.Property(
            "file_naming_scheme",
            th.StringType,
            description="The scheme with which output files will be named"
        ),
        th.Property(
            "auth_token",
            th.StringType,
            secret=True,  # Flag config as protected.
            description="The path to the target output file"
        ),
    ).to_dict()

    default_sink_class = SalesforceSink


if __name__ == "__main__":
    TargetSalesforce.cli()
