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
Convert any* audio file into a txt file, with decoding of the recording.

*-I use [Librosa](https://librosa.org/) and [FFmpeg](https://ffmpeg.org/) ([gyan.dev build essential version: 2025-11-12-git-6cdd2cbe32](https://www.gyan.dev/ffmpeg/builds/)) for work with audio files. That mean, program maybe will be work with ANY audio type.


- [Important notes](#important-notes)
- [CUDA](#cuda)
- [AI Examples](#ai-examples)
- [AI Description](#ai-description)
- [Modify of JSON files](#modify-of-json-files)
- [License](#license)

## Important notes
> [!WARNING]
> All neural networks that are presented below or in the project (file settings.json) are only an EXAMPLE. By using these neural networks, you automatically agree to their license agreement, if any. If you want to read information about the neural networks that are used here, go to the AI ​​column.

## CUDA 
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

## AI Examples
> [!WARNING]
> All URL will be entered into the [Hugging Face website](https://huggingface.co/). The AI ​​work in the program is done using their [Transformers library](https://huggingface.co/docs/transformers/index).
- [openai/whisper-large-v3 (Apache 2.0)](https://huggingface.co/openai/whisper-large-v3)
- [openai/whisper-large-v3-turbo (MIT)](https://huggingface.co/openai/whisper-large-v3-turbo)
- [openai/whisper-small (Apache 2.0)](https://huggingface.co/openai/whisper-small)
- [bond005/whisper-podlodka-turbo (Apache 2.0)](https://huggingface.co/bond005/whisper-podlodka-turbo)
- [Quantumhash/Quantum_STT (Apache 2.0)](https://huggingface.co/Quantumhash/Quantum_STT)
- [Apel-sin/whisper-large-v3-russian-ties-podlodka-v1.2 (No license?)](https://huggingface.co/Apel-sin/whisper-large-v3-russian-ties-podlodka-v1.2)

## AI Description

Aboit it you can read right [here](https://github.com/tatpow/project-aura/blob/91b026c81fc87a1210911549d4f5999d2ed75ac2/tests/models.md).

## Modify of JSON files
If you want to modify, for example, list of all models, just update JSON file. All files you can find:
> _internal\app\json (BUILD)

>  app/json (SOURCE CODE)

## License

MIT © [tatpow](https://github.com/tatpow)
