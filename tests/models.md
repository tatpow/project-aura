# Testing AI models of ASR format for quality, speed and other parameters (November 2025)

- #### Last update: 16.11.25

## Data

I tested nearly 80 ASR models from HF. All tests were on laptop. Here are the parameters:

- CPU: 12th Gen Intel Core i5-12500H, 2500 MGZ
- GPU: NVIDIA GeForce RTX 3050 Laptop / Intel Iris Xe Graphics
- Ram: 16 GB

I had tree audio files in MP3 format: first is 60 seconds prepared audio with low-middle background noise, second is ~ 3 minutes not prepared audio with middle-high background noise and third is ~ 20 minutes not prepared audio with middle-high background noise. 
(Prepared - recorded on a speciac microphone; Not Prepared - recorded in 'real' production, for example, on real lectures).
All tests were on Russian language.

About table: 
- Test 1 - prepared audio
- Test 2 - NOT prepared audio 3 minutes
- Test 3 - NOT prepared audio ~ 21 minutes
- Spec. info 'test_id' - some of my notes may be useful

I have a lot of table, here list of them:

- 

### Final table (top 5 model):

### Finan table for Test 1:

| Model | Test 1 - Speed | Test 1 - Quality | Spec. info Test 1 |
|---|---|---|---|
| openai/whisper-large-v3-turbo | 15 | 95.00% |  |
| unsloth/whisper-large-v3-turbo | 25 | 70.00% |  |
| BorisFaj/whisperL-v3-turbo | 20 | 70.00% |  |
| brahmairesearch/vaani-opt | 25 | 70.00% |  |
| Quantumhash/Quantum_STT | 30 | 80.00% | partially understood |
| Compumacy/whisper_turbo | 22 | 70.00% |  |
| chaitnya26/whisper-large-v3-turbo-fork | 25 | 80.00% |  |
| IdoMachlev/ido-whisper-turbo | 16 | 65.00% |  |
| richiebailey/whisper-large-v3-turbo | 16 | 65.00% | missed parts |
| openai/whisper-large-v2 | 185 | 65.00% | skipped parts |
| openai/whisper-large-v3 | 30 | 100.00% |  |
| spellingdragon/whisper-large-v3-handler | 60 | 65.00% | garbage output |
| dvislobokov/whisper-large-v3-turbo-russian | 6 | 65.00% |  |
| Apel-sin/whisper-large-v3-russian-ties-podlodka-v1.2 | 20 | 100.00% |  |
| MonsterVen/whisper-small-ru | 15 | 80.00% | partially understood |
| bond005/whisper-podlodka-turbo | 15 | 100.00% |  |
| thucdangvan020999/whisper_v3_turbo_noise_dataset_2_7_200_step | 25 | 65.00% | partially understood |
| antony66/whisper-large-v3-russian | 60 | 80.00% | skipped parts |
| ElderlyDed/whisper-small-ruV4 | 4 | 70.00% | missed parts |
| Apel-sin/whisper-large-v3-russian-ties-podlodka-v1.0 | 60 | 90.00% |  |

### Finan table for Test 2:



### Finan table for Test 3:



## Full unsorted tables iterations
<details> 

---
  
### Full Table 1 Iteration
  
<details>
  
| Model | Test 1 - Speed | Test 1 - Quality | Spec. info Test 1 |
|---|---|---|---|
| openai/whisper-large-v3 | 30 | 100.00% |  |
| openai/whisper-large-v3-turbo | 15 | 95.00% |  |
| microsoft/Phi-4-multimodal-instruct | - |  | requires trust_remote |
| openai/whisper-tiny | 17 | 50.00% | recognized Arabic |
| facebook/seamless-m4t-v2-large | - |  | large model size |
| openai/whisper-small | 45 | 60.00% | recognized Arabic |
| facebook/mms-1b-all | - |  | large model size |
| bond005/whisper-podlodka-turbo | 15 | 100.00% |  |
| Darveht/ZenVision-AI-Subtitle-Generator | - |  | not working yet (waiting for DB update) |
| Apel-sin/whisper-large-v3-russian-ties-podlodka-v1.2 | 20 | 100.00% |  |
| jonatasgrosman/wav2vec2-xls-r-1b-russian | - |  |  |
| openai/whisper-base | 5 | 50.00% | partially understood |
| MahmoudAshraf/mms-300m-1130-forced-aligner | 0 | 0.00% |  |
| openai/whisper-large-v2 | 185 | 65.00% | skipped parts |
| antony66/whisper-large-v3-russian | 60 | 80.00% | skipped parts |
| xkeyC/whisper-large-v3-turbo-gguf | - |  | failed to launch |
| Edresson/wav2vec2-large-100k-voxpopuli-ft-Common-Voice_plus_TTS-Dataset-russian | - |  | failed to launch |
| RASMUS/wav2vec2-xlsr-1b-ru | - |  | failed to launch |
| emre/wav2vec2-xls-r-300m-Russian-small | - |  | failed to launch |
| anton-l/wav2vec2-large-xls-r-53-russian | - |  | failed to launch |
| facebook/s2t-small-mustc-en-ru-st | - |  | failed to launch |
| facebook/s2t-medium-mustc-multilingual-st | - |  | failed to launch |
| facebook/wav2vec2-xls-r-2b-21-to-en | - |  | failed to launch |
| facebook/wav2vec2-xls-r-1b-21-to-en | - |  | failed to launch |
| facebook/wav2vec2-xls-r-2b-22-to-16 | - |  | failed to launch |
| facebook/wav2vec2-xls-r-300m-21-to-en | - |  | failed to launch |
| mobedkova/wav2vec2-large-xls-r-300m-ru | - |  | failed to launch |
| jonatasgrosman/wav2vec2-large-xlsr-53-russian | - |  | failed to launch |
| voidful/wav2vec2-xlsr-multilingual-56 | - |  | failed to launch |
| bond005/wav2vec2-large-ru-golos | - |  | failed to launch |
| juasker/whisper-ct2-podlodka-turbo | - |  | failed to launch |
| FriendliAI/Phi-4-multimodal-instruct | - |  | requires trust_remote |
| FastFlowLM/Whisper-V3-Turbo-NPU2 | - |  | failed to launch |
| pklumpp/Wav2Vec2_CommonPhone | - |  | failed to launch |
| kumapo/Phi-4-multimodal-instruct | - |  | requires trust_remote |
| chaitnya26/whisper-large-v3-turbo-fork | 25 | 80.00% |  |
| Vikhrmodels/Borealis | - |  | requires trust_remote |
| feelmadrain/whisper-small-ru | 35 | 20.00% | output not in Russian (appeared in Ukrainian) |
| shunyalabs/pingala-v1-universal | - |  | requires authentication |
| bzikst/faster-whisper-large-v3-russian | - |  | failed to launch |
| lakshmi97/Phi-4-multimodal-instruct | - |  | requires trust_remote |
| waveletdeboshir/gigaam-rnnt | - |  | requires trust_remote |
| waveletdeboshir/gigaam-ctc-with-lm | - |  | requires trust_remote |
| waveletdeboshir/gigaam-ctc | - |  | requires trust_remote |
| johntsi/ZeroSwot-Large_asr-mustc_en-to-200 | - |  | requires trust_remote |
| johntsi/ZeroSwot-Large_asr-mustc_mt-mustc_en-to-8 | - |  | requires trust_remote |
| johntsi/ZeroSwot-Medium_asr-mustc_en-to-200 | - |  | requires trust_remote |
| johntsi/ZeroSwot-Medium_asr-mustc_mt-mustc_en-to-8 | - |  | requires trust_remote |
| Den4ikAI/gigaam-ctc-whisperx | - |  | requires trust_remote |
| waveletdeboshir/whisper-large-v3-no-numbers | - |  | Error |
| waveletdeboshir/whisper-large-v3-turbo-no-numbers | - |  | Error |
| spellingdragon/whisper-large-v3-handler | 60 | 65.00% | garbage output |
| internalhell/whisper_small_ru_model_trainer_3ep | 15 | 60.00% | garbage output |
| internalhell/wav2vec2-large-ru-5ep | 3 | 10.00% | garbage output |
| MonsterVen/whisper-small-ru | 15 | 80.00% | partially understood |
| ShadowBunting/whisper-small-ru-my-2 | - |  | requires protobuf |
| Sh1man/whisper-large-v3-russian-ties-podlodka-v1.2-ct | - |  | Error |
| Lexius/Phi-4-multimodal-instruct | - |  | requires trust_remote |
| thucdangvan020999/whisper_v3_turbo_noise_dataset_2_7_200_step | 25 | 65.00% | partially understood |
| shadow-bunting-1/whisper-small-ru-my | - |  | requires protobuf |
| Quantumhash/Quantum_STT | 30 | 80.00% | partially understood |
| internalhell/whisper_small_ru_model_trainer_2 | - |  | requires protobuf |
| unsloth/whisper-large-v3-turbo | 25 | 70.00% |  |
| artyomboyko/whisper-small-ru-v4 | - |  | requires authentication |
| realitisoft/ai-bot-test | - |  | Error |
| IronWolfAI/GoldenCrow | - |  | requires trust_remote |
| Apel-sin/whisper-large-v3-russian-ties-podlodka-v1.0 | 60 | 90.00% |  |
| Sh1man/whisper-large-v3-russian-ties-podlodka-v1.0-ct | - |  | Error |
| Compumacy/whisper_turbo | 22 | 70.00% |  |
| BorisFaj/whisperL-v3-turbo | 20 | 70.00% |  |
| Auttar/whisper-finetuned-shortened |  | 0.00% | nonsense |
| huihui-ai/Phi-4-multimodal-instruct-abliterated | - |  | requires trust_remote |
| BobV33/Phi-4-multimodal-instruct | 15 | 80.00% |  |
| mjtechguy/phi-4-multimodal-instruct | - |  | requires trust_remote |
| brahmairesearch/vaani-opt | 25 | 70.00% |  |
| dvislobokov/whisper-large-v3-turbo-russian | 6 | 65.00% |  |
| ctranslate2-4you/whisper-large-v3-ct2-float32 | - |  | Error |
| felarof01/whisper-large-v3-turbo | - |  | Error |
| Qwzerty/whisper-large-v3-ru | - |  | requires protobuf |
| IdoMachlev/ido-whisper-turbo | 16 | 65.00% |  |
| Ailurus/whisper-tiny-finetuned-ru | 6 | 30.00% | skipped a lot |
| ElderlyDed/whisper-small-ruV4 | 4 | 70.00% | missed parts |
| richiebailey/whisper-large-v3-turbo | 16 | 65.00% | missed parts |

</details>
  
---

### Full Table 2 Iteration
  
<details>
  
| Model | Test 1 - Speed | Test 1 - Quality | Spec. info Test 1 |
|---|---|---|---|
| openai/whisper-large-v2 | 185 | 65.00% | skipped parts |
| spellingdragon/whisper-large-v3-handler | 60 | 65.00% | garbage output |
| thucdangvan020999/whisper_v3_turbo_noise_dataset_2_7_200_step | 25 | 65.00% | partially understood |
| dvislobokov/whisper-large-v3-turbo-russian | 6 | 65.00% |  |
| IdoMachlev/ido-whisper-turbo | 16 | 65.00% |  |
| richiebailey/whisper-large-v3-turbo | 16 | 65.00% | missed parts |
| unsloth/whisper-large-v3-turbo | 25 | 70.00% |  |
| Compumacy/whisper_turbo | 22 | 70.00% |  |
| BorisFaj/whisperL-v3-turbo | 20 | 70.00% |  |
| brahmairesearch/vaani-opt | 25 | 70.00% |  |
| ElderlyDed/whisper-small-ruV4 | 4 | 70.00% | missed parts |
| antony66/whisper-large-v3-russian | 60 | 80.00% | skipped parts |
| chaitnya26/whisper-large-v3-turbo-fork | 25 | 80.00% |  |
| MonsterVen/whisper-small-ru | 15 | 80.00% | partially understood |
| Quantumhash/Quantum_STT | 30 | 80.00% | partially understood |
| BobV33/Phi-4-multimodal-instruct | 15 | 80.00% |  |
| Apel-sin/whisper-large-v3-russian-ties-podlodka-v1.0 | 60 | 90.00% |  |
| openai/whisper-large-v3-turbo | 15 | 95.00% |  |
| openai/whisper-large-v3 | 30 | 100.00% |  |
| bond005/whisper-podlodka-turbo | 15 | 100.00% |  |
| Apel-sin/whisper-large-v3-russian-ties-podlodka-v1.2 | 20 | 100.00% |  |
| microsoft/Phi-4-multimodal-instruct | - |  | error: this is a multimodal LLM |
| jonatasgrosman/wav2vec2-xls-r-1b-russian | - |  | error: requires torch > 2.6 |
| FriendliAI/Phi-4-multimodal-instruct | - |  | error: this is a multimodal LLM |
| kumapo/Phi-4-multimodal-instruct | - |  | error: this is a multimodal LLM |
| Vikhrmodels/Borealis | - |  | error: requires specific launch setup |
| lakshmi97/Phi-4-multimodal-instruct | - |  | error: this is a multimodal LLM |
| waveletdeboshir/gigaam-rnnt | - |  | error: requires torchaudio |
| waveletdeboshir/gigaam-ctc-with-lm | - |  | error: requires torchaudio |
| waveletdeboshir/gigaam-ctc | - |  | error: requires torchaudio |
| johntsi/ZeroSwot-Large_asr-mustc_en-to-200 | - |  | error: this is a multimodal LLM |
| johntsi/ZeroSwot-Large_asr-mustc_mt-mustc_en-to-8 | - |  | error: this is a multimodal LLM |
| johntsi/ZeroSwot-Medium_asr-mustc_en-to-200 | - |  | error: this is a multimodal LLM |
| johntsi/ZeroSwot-Medium_asr-mustc_mt-mustc_en-to-8 | - |  | error: this is a multimodal LLM |
| Den4ikAI/gigaam-ctc-whisperx | - |  | error: requires torchaudio |
| ShadowBunting/whisper-small-ru-my-2 | - |  | error: expected str, bytes or os.PathLike object, not NoneType |
| Lexius/Phi-4-multimodal-instruct | - |  | error: this is a multimodal LLM |
| shadow-bunting-1/whisper-small-ru-my | - |  | error: expected str, bytes or os.PathLike object, not NoneType |
| internalhell/whisper_small_ru_model_trainer_2 | - |  | error: expected str, bytes or os.PathLike object, not NoneType |
| IronWolfAI/GoldenCrow | - |  | error: this is a multimodal LLM |
| huihui-ai/Phi-4-multimodal-instruct-abliterated | - |  | error: this is a multimodal LLM |
| mjtechguy/phi-4-multimodal-instruct | - |  | error: this is a multimodal LLM |
| Qwzerty/whisper-large-v3-ru | - |  | error: expected str, bytes or os.PathLike object, not NoneType |
  
</details>
  
---

### Full Table 3 Iteration
  
<details>
  
| Model | Test 1 - Speed | Test 1 - Quality | Spec. info Test 1 | Test 2 - Speed (3min) | Test 2 - Quality | Spec. info Test 2 |
|---|---|---|---|---|---|---|
| openai/whisper-large-v3 | 30 | 100.00% |  | 541 | 81.5% |  |
| bond005/whisper-podlodka-turbo | 15 | 100.00% |  | 14 | 32.5% |  |
| Apel-sin/whisper-large-v3-russian-ties-podlodka-v1.2 | 20 | 100.00% |  | 125 | 65.0% |  |
| openai/whisper-large-v3-turbo | 15 | 95.00% |  | 9 | 79.0% |  |
| Apel-sin/whisper-large-v3-russian-ties-podlodka-v1.0 | 60 | 90.00% |  | 232 | 23.0% |  |
| antony66/whisper-large-v3-russian | 60 | 80.00% | skipped parts | 268 | 52.5% |  |
| chaitnya26/whisper-large-v3-turbo-fork | 25 | 80.00% |  | 11 | 70.0% |  |
| MonsterVen/whisper-small-ru | 15 | 80.00% | partially understood | 11 | 27.5% |  |
| Quantumhash/Quantum_STT | 30 | 80.00% | partially understood | 10 | 72.5% |  |
| BobV33/Phi-4-multimodal-instruct | - | - | - | - | - |  |
| unsloth/whisper-large-v3-turbo | 25 | 70.00% |  | 8 | 72.5% |  |
| Compumacy/whisper_turbo | 22 | 70.00% |  | 10 | 72.5% |  |
| BorisFaj/whisperL-v3-turbo | 20 | 70.00% |  | 9 | 72.5% |  |
| brahmairesearch/vaani-opt | 25 | 70.00% |  | 9 | 72.5% |  |
| ElderlyDed/whisper-small-ruV4 | 4 | 70.00% | missed parts | 16 | 30.0% |  |
| openai/whisper-large-v2 | 185 | 65.00% | skipped parts | 96 | 79.0% |  |
| spellingdragon/whisper-large-v3-handler | 60 | 65.00% | garbage output | 108 | 75.0% |  |
| thucdangvan020999/whisper_v3_turbo_noise_dataset_2_7_200_step | 25 | 65.00% | partially understood | 18 | 37.5% |  |
| dvislobokov/whisper-large-v3-turbo-russian | 6 | 65.00% |  | 12 | 40.0% |  |
| IdoMachlev/ido-whisper-turbo | 16 | 65.00% |  | 13 | 72.5% |  |
| richiebailey/whisper-large-v3-turbo | 16 | 65.00% | missed parts | 13 | 72.5% |  |
  
</details>
  
---

### Full Table 4 Iteration
  
<details>
  
table
  
</details>
  
---
  
</details>



