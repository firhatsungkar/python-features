"""
Basic video exporting example
"""

from pathlib import Path
from typing import Protocol, Type
from dataclasses import dataclass


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


@dataclass
class MediaExporter:
    video: VideoExporter
    audio: AudioExporter


@dataclass
class MediaExporterFactory:
    video_class: Type[VideoExporter]
    audio_class: Type[AudioExporter]

    def __call__(self) -> MediaExporter:
        return MediaExporter(
            self.video_class(),
            self.audio_class()
        )


FACTORIES = {
    "low": MediaExporterFactory(H264BPVideoExporter, AACAudioExporter),
    "high": MediaExporterFactory(H264Hi422PVideoExporter, AACAudioExporter),
    "master": MediaExporterFactory(LosslessVideoExporter, WAVAudioExporter)
}


def read_factory() -> MediaExporterFactory:
    """Constructs an exporter factory based on the user's preference."""

    while True:
        export_quality = input(
            "Enter desired output quality (low, high, master): ")
        try:
            return FACTORIES[export_quality]
        except KeyError:
            print(f"Unknown output quality option: {export_quality}.")


def main(exporter: MediaExporter) -> None:
    """Main function."""

    # prepare the export
    exporter.video.prepare_export("placeholder_for_video_data")
    exporter.audio.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = Path("/usr/tmp/video")
    exporter.video.do_export(folder)
    exporter.audio.do_export(folder)


if __name__ == "__main__":
    # create the factory
    factory = read_factory()

    # use the factory to create the media exporter
    media_exporter = factory()

    # perform the exporting job
    main(media_exporter)
