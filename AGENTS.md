# Agent instructions

## Project layout

- `app/asr.py` runs the Hugging Face automatic-speech-recognition pipeline and
  processes audio in resumable chunks.
- `app/json/models.json` maps the model names shown in the UI to Hugging Face
  model IDs. Add compatible models there rather than hard-coding them in the UI.
- `app/media.py` extracts a mono 16 kHz WAV audio track with FFmpeg before ASR.
  Keep the bundled executable paths in both `spec/gpu.spec` and `spec/cpu.spec`
  in sync with changes to media handling.
- `requirements/requirements_gpu.txt` and
  `requirements/requirements_cpu.txt` pin the Windows GPU and CPU environments.
  Keep shared AI-library versions compatible between both files. The GPU
  PyTorch wheel uses the CUDA 13.0 index.

## Model changes

- Confirm that a model is supported by the pinned Transformers release and by
  the existing ASR pipeline before adding it to `app/json/models.json`.
- The model list includes Parakeet TDT. Keep Transformers and its pinned
  dependencies at versions that include the Parakeet TDT architecture.
- Do not describe a model as more accurate or faster without benchmarking it
  against the same audio and settings as the existing models.
- Keep the model notes in `tests/models.md` clear about which results are
  measured locally and which are published by model authors.

## Validation and builds

- Use Python 3.13 on Windows.
- Run unit tests with `python -m unittest discover -s tests -v`.
- Check Python syntax with `python -m compileall -q app main.py tests`.
- Build the GPU app with `.venv_gpu` and `spec/gpu.spec`; build the CPU app
  with `.venv_cpu` and `spec/cpu.spec`.
- Both builds must include the FFmpeg binaries used for media extraction.
