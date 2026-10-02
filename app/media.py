import os
import shutil
import subprocess

from app.data.utils import resource_path


def get_ffmpeg_path() -> str:
    executable = "ffmpeg.exe" if os.name == "nt" else "ffmpeg"
    bundled_path = resource_path(os.path.join("ffmpeg", executable))
    if os.path.isfile(bundled_path):
        return bundled_path

    system_path = shutil.which("ffmpeg")
    if system_path:
        return system_path

    raise FileNotFoundError(
        "FFmpeg не найден. Переустановите приложение или установите FFmpeg."
    )


def extract_audio(input_path: str, output_path: str) -> None:
    result = subprocess.run(
        [
            get_ffmpeg_path(),
            "-nostdin",
            "-y",
            "-i",
            input_path,
            "-map",
            "0:a:0",
            "-vn",
            "-ac",
            "1",
            "-ar",
            "16000",
            "-c:a",
            "pcm_s16le",
            output_path,
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode != 0:
        details = result.stderr.strip()[-2000:]
        raise RuntimeError(
            f"Не удалось извлечь аудио с помощью FFmpeg:\n{details or 'неизвестная ошибка'}"
        )
