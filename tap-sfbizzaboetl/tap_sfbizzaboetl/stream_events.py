"""Stream type classes for tap-sfbizzaboetl."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_sfbizzaboetl.client import SfBizzaboETLStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class EventsStream(SfBizzaboETLStream):
    """Define custom stream."""
    name = "events"
    path = "/events"
    primary_keys = ["id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
            description="The events ID"
        ),
        th.Property(
            "status",
            th.StringType,
            description="The event status e.g : live or draft"
        ),
        th.Property(
            "name",
            th.StringType,
            description="The event name"
        ),

        th.Property(
            "startDate",
            th.IntegerType,
            description="The event start date"
        ),
        th.Property(
            "endDate",
            th.StringType,
            description="The event end date"
        ),
        th.Property(
            "timezone",
            th.StringType,
            description="The time zone of the event"
        ),
        th.Property(
            "created",
            th.StringType,
            description="The date of the event creation in the Bizzabo platform"
        ),
        th.Property(
            "modified",
            th.StringType,
            description="The last modified date of one of the event properties"
        ),

    ).to_dict()


# class GroupsStream(SfBizzaboETLStream):
#     """Define custom stream."""
#     name = "groups"
#     path = "/groups"
#     primary_keys = ["id"]
#     replication_key = "modified"
#     schema = th.PropertiesList(
#         th.Property("name", th.StringType),
#         th.Property("id", th.StringType),
#         th.Property("modified", th.DateTimeType),
#     ).to_dict()
