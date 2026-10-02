import unittest
from unittest.mock import patch

from app.media import extract_audio


class ExtractAudioTests(unittest.TestCase):
    @patch("app.media.subprocess.run")
    @patch("app.media.get_ffmpeg_path", return_value="ffmpeg.exe")
    def test_extracts_first_audio_track_as_mono_16khz_pcm(
        self, _get_ffmpeg_path, run
    ):
        run.return_value.returncode = 0

        extract_audio("input video.mp4", "output.wav")

        command = run.call_args.args[0]
        self.assertEqual(command[0], "ffmpeg.exe")
        self.assertEqual(command[command.index("-i") + 1], "input video.mp4")
        self.assertEqual(command[command.index("-map") + 1], "0:a:0")
        self.assertEqual(command[command.index("-ac") + 1], "1")
        self.assertEqual(command[command.index("-ar") + 1], "16000")
        self.assertEqual(command[-1], "output.wav")
        self.assertTrue(run.call_args.kwargs["check"] is False)

    @patch("app.media.subprocess.run")
    @patch("app.media.get_ffmpeg_path", return_value="ffmpeg.exe")
    def test_reports_ffmpeg_errors(self, _get_ffmpeg_path, run):
        run.return_value.returncode = 1
        run.return_value.stderr = "No audio stream found"

        with self.assertRaisesRegex(RuntimeError, "No audio stream found"):
            extract_audio("silent.mp4", "output.wav")


if __name__ == "__main__":
    unittest.main()
