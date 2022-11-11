"""SfBizzaboETL tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
# TODO: Import your custom stream types here:
from tap_sfbizzaboetl.stream_events import (SfBizzaboETLStream,EventsStream)
from tap_sfbizzaboetl.stream_reg import RegStream

# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [EventsStream, RegStream]


class TapSfBizzaboETL(Tap):
    """SfBizzaboETL tap class."""
    name = "tap-sfbizzaboetl"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            default="81edf834-f0dc-4754-89a9-99d44ab1b9fa",
            description="The token to authenticate against the API service"
        ),

        th.Property(
            "api_url",
            th.StringType,
            default="https://api.bizzabo.com/api",
            description="The base url for Bizzabo API"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
