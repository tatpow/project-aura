> [!WARNING]
> # PROJECT CLOSED. IN THE FUTURE LOOK FOR US AT [Melofixus](https://github.com/dotcoord/Melofixus)

---

<h1 align="center">
  <img src="https://github.com/tatpow/project-aura/blob/main/banner.png" alt="Project Aura Logo" width="1000">
  <br>
  Project Aura - Audio in Analysis
  <br>
</h1>

![GitHub Release](https://img.shields.io/github/v/release/tatpow/project-aura)
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/tatpow/project-aura/total)
![GitHub License](https://img.shields.io/github/license/tatpow/project-aura)

## About this project
This project was created to make life easier for schoolers or students.
All UI in program is in Russian. Maybe later I add English version.
Transcribe audio and video recordings into a text file. Video files are processed by extracting their first audio track with FFmpeg.

The file picker supports common audio formats (MP3, WAV, FLAC, OGG, M4A, AAC, WMA, AIFF, and OPUS) and video containers (MP4, MKV, MOV, AVI, WebM, FLV, WMV, M4V, MPEG, 3GP, TS, MTS, M2TS, OGV, VOB, and ASF). Decodable codecs depend on the media file and the bundled FFmpeg build. Windows builds include FFmpeg and ffprobe.

- [Build](#build)
- [Models and languages](#models-and-languages)
- [Historical CUDA benchmark](#historical-cuda-benchmark)
- [Important notes](#important-notes)
- [AI model list](#ai-model-list)
- [Model comparisons](#model-comparisons)
- [Modify model list](#modify-model-list)
- [License](#license)

## Build

Use Python 3.13 and install the matching dependencies from the repository root:

```powershell
py -3.13 -m venv .venv_gpu
.\.venv_gpu\Scripts\Activate.ps1
python -m pip install -r requirements\requirements_gpu.txt
pyinstaller --noconfirm --clean --distpath dist\gpu --workpath build\gpu spec\gpu.spec
```

For the CPU build:

```powershell
py -3.13 -m venv .venv_cpu
.\.venv_cpu\Scripts\Activate.ps1
python -m pip install -r requirements\requirements_cpu.txt
pyinstaller --noconfirm --clean --distpath dist\cpu --workpath build\cpu spec\cpu.spec
```

Both builds bundle the application and FFmpeg. The GPU build uses the CUDA 13.0 PyTorch wheel for recent NVIDIA GPUs, including GeForce RTX 50-series cards; the CPU build installs PyTorch without CUDA.

## Models and languages

The model picker includes NVIDIA [Parakeet TDT 0.6B v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3), a multilingual ASR model that supports Russian and 24 other languages. It runs through the Transformers 5.18 automatic-speech-recognition pipeline. Models download from Hugging Face on first use.

Parakeet includes punctuation and capitalization, while recognition quality and speed depend on language, audio, hardware, and settings. Its quality has not been compared against the Whisper models on the Russian recordings documented in [the model tests](tests/models.md); try both on the same recording before choosing a default.

The model repository is licensed under CC BY 4.0. Each model has its own license and terms; review them before use.

## Historical CUDA benchmark

The benchmark below is a historical result for Whisper from a different project setup and a GeForce RTX 3050 Laptop. It does not measure Parakeet or predict performance on newer hardware.

I ran my 'banchmark'. I used model [bond005/whisper-podlodka-turbo (Apache 2.0)](https://huggingface.co/bond005/whisper-podlodka-turbo) (it's the fastest). Audio file len is 2780 seconds.

I have the following components in my PC:
- CPU: 12th Gen Intel Core i5-12500H, 2500 MHz
- GPU (from CPU): Irix Xe Graphics
- GPU: GeForce RTX 3050 Laptop
- Ram: 16GB

The laptop was on charge all the time. No third party programs were opened. Only one file in ogg.

Also, through my setup program, you can select the type of operation: 
- Quiet (uses the processor video card)
- Efficiency (according to the manufacturers, this mode “balances” between video cards)
- Turbo (everything is at maximum)

Table of banchmark:
| **Device Type** | **Time (sec)** | **Laptop Mod** |
|---|---|---|
| GPU | 330 | Q |
| GPU | 170 | E |
| GPU | 165 | T |
| CPU | > ~2100 | Q |
| CPU | > ~2100 | E |
| CPU | > ~2100 | T |

I don't believe this kind of performance on a CPU, it was faster on my PC rather than a laptop. Perhaps the problem is in the ogg file extension.

## Important notes

The listed models are examples. Check each model's license and terms before using it.

## AI model list
> [!WARNING]
> The models are downloaded from [Hugging Face](https://huggingface.co/) and run locally using the [Transformers library](https://huggingface.co/docs/transformers/index).

- [WhisperL3-T (openai/whisper-large-v3-turbo)](https://huggingface.co/openai/whisper-large-v3-turbo)
- [WhisperL3-T-Fork (chaitnya26/whisper-large-v3-turbo-fork)](https://huggingface.co/chaitnya26/whisper-large-v3-turbo-fork)
- [WhisperL3 (openai/whisper-large-v3)](https://huggingface.co/openai/whisper-large-v3)
- [WhisperS-ruV4 (ElderlyDed/whisper-small-ruV4)](https://huggingface.co/ElderlyDed/whisper-small-ruV4)
- [Parakeet TDT 0.6B v3 (nvidia/parakeet-tdt-0.6b-v3)](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3)

## Model comparisons

Historical Russian Whisper model comparisons and their test setup are documented in [tests/models.md](tests/models.md). Parakeet is listed there as not yet benchmarked on those recordings.

## Modify model list

To add or remove a model in source, update `app/json/models.json`. Packaged builds include that file under `_internal/app/json`.

## License

MIT © [tatpow](https://github.com/tatpow)
