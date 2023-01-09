"""
Basic video exporting example
"""

from pathlib import Path
from typing import Protocol


class VideoExporter(Protocol):
    """Basic representation of video exporting codec."""

    def prepare_export(self, view_data: str) -> None:
        """Prepares video data for exporting."""

    def do_export(self, folder: Path) -> None:
        """Export the video data to a folder."""


class LosslessVideoExporter:
    """Lossless video exporting codec."""

    def prepare_export(self, view_data: str) -> None:
        print("Preparing video data for lossless export.")

    def do_export(self, folder: Path) -> None:
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter:
    """H.264 video exporting codec with Baseline profile."""

    def prepare_export(self, view_data: str) -> None:
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: Path) -> None:
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter:
    """
    H.264 video exporting codec
    with Hi422P profile (10-bit, 4:2:2 chrome sampling).
    """

    def prepare_export(self, view_data: str) -> None:
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: Path) -> None:
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class AudioExporter(Protocol):
    """Basic representation of audio exporting codec."""

    def prepare_export(self, audio_data: str) -> None:
        """Prepares audio data for exporting."""

    def do_export(self, folder: Path) -> None:
        """Exports the audio data to a folder."""


class AACAudioExporter:
    """AAC Audio exporting codec."""

    def prepare_export(self, audio_data: str) -> None:
        print("Preparing audio data for AAC export.")

    def do_export(self, folder: Path) -> None:
        print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter:
    """WAV (lossless) audio exporting codec."""

    def prepare_export(self, audio_data: str) -> None:
        print("Preparing audio data for WAV export.")

    def do_export(self, folder: Path) -> None:
        print(f"Exporting audio data in WAV format to {folder}.")


class ExporterFactory(Protocol):
    """
    Factory that represents a combination of video and audio codecs.
    The factory doesn't maintain any of the instances it creates.
    """

    def get_video_exporter(self) -> VideoExporter:  # type: ignore
        """Returns a new video exporter belonging to this factory."""

    def get_audio_exporter(self) -> AudioExporter:  # type: ignore
        """Returns a new audio exporter belonging to this factory."""


FACTORIES = {
    "low": (H264BPVideoExporter, AACAudioExporter),
    "high": (H264Hi422PVideoExporter, AACAudioExporter),
    "master": (LosslessVideoExporter, WAVAudioExporter)
}


def read_factory() -> tuple[VideoExporter, AudioExporter]:
    """Constructs an exporter factory based on the user's preference."""

    while True:
        export_quality = input(
            "Enter desired output quality (low, high, master): ")
        try:
            video_class, audio_class = FACTORIES[export_quality]
            return (video_class(), audio_class())
        except KeyError:
            print(f"Unknown output quality option: {export_quality}.")


def main(fac: tuple[VideoExporter, AudioExporter]) -> None:
    """Main function."""

    # retrieve the exporters
    video_exporter, audio_exporter = fac

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    # create the factory
    factory = read_factory()

    # perform the exporting job
    main(factory)
