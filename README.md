<div align="center">

# Awesome Weight-Space Programming [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**Language models that read, edit and write the weights of other neural networks directly, without gradient descent.**

[![Last commit](https://img.shields.io/github/last-commit/SajjadPSavoji/awesome-weight-space-programming?color=green)](https://github.com/SajjadPSavoji/awesome-weight-space-programming/commits/main)
![Entries](https://img.shields.io/badge/entries-31-blue)
![Updated](https://img.shields.io/badge/updated-daily-orange)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)

</div>

*Weight-space programming* was named in the MIT CSAIL report [Sparks of Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/) (2026-11-02). A general LLM is given another network's weights, sometimes with code and a budget of forward passes, and changes the numbers to explain, repair or build behavior. This list tracks the papers, code, benchmarks and critiques that follow, grouped by the kind of network being programmed. It is rebuilt from [`data/entries.json`](data/entries.json).

## 🔥 Recently Added

- **2026-11-04** · [Astra weight edits on a VLA, a world action model and humanoid control](https://x.com/Lingxiao234/status/2118048171649806424) (Vision-language-action models)
- **2026-11-04** · [Weight-Space Programming for VLAs](https://github.com/Geeksongs/Weight-Space-Programming-VLA) (Vision-language-action models)
- **2026-11-04** · [weights_editing: replicating Sparks of Weight-Space Programming across LLMs](https://github.com/alan-turing-institute/weights_editing) (Repairing behavior)
- **2026-11-04** · [OpenWSP](https://github.com/openwsp/openwsp) (Repairing behavior)
- **2026-11-04** · [WSPBench](https://github.com/alexcarterhq/wspbench) (Benchmarks and Evaluations)
- **2026-11-04** · [weightspace](https://github.com/leofmarciano/weightspace) (Tools, Harnesses and Agent Skills)
- **2026-11-04** · [weight-space-programming-skill](https://github.com/di37/weight-space-programming-skill) (Tools, Harnesses and Agent Skills)
- **2026-11-04** · [weights-lab](https://github.com/oumi-ai/weights-lab) (Tools, Harnesses and Agent Skills)
- **2026-11-04** · [pi-weight-space-programming](https://github.com/felipepenha/pi-weight-space-programming) (Tools, Harnesses and Agent Skills)
- **2026-11-04** · [The 'Astra can read and write weights to improve Qwen' post is misleading](https://honnibal.dev/blog/astra-read-write-misleading) (Analyses and Critiques)
- **2026-11-04** · [MIT team says GPT-6 Astra can improve other AI models by editing their weights. Critics say its biggest result relied on standard ML engineering.](https://www.rdworldonline.com/mit-team-says-gpt-6-astra-can-fix-an-ai-model-by-editing-its-weights-critics-say-the-method-was-standard-ml-engineering/) (Analyses and Critiques)
- **2026-11-04** · [Weight-space programming for auditing clinical decision networks](https://arxiv.org/abs/2611.05341) (Other Domains)

## 🧭 Milestones

| Date | Milestone | Who | Work |
|:--|:--|:--|:--|
| 2026-11-02 | Term coined | MIT CSAIL | [Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights](https://rikiyat.github.io/blog/weight-space-programming/) |
| 2026-11-04 | First robot policies | Lingxiao Guo, Angchen Xie | [Astra weight edits on a VLA, a world action model and humanoid control](https://x.com/Lingxiao234/status/2118048171649806424) |

## Contents

- [🌟 The Original Report](#-the-original-report) (1)
- [💬 Language Models](#-language-models) (3)
  - [Repairing behavior](#repairing-behavior) (2)
  - [Reading and predicting from weights](#reading-and-predicting-from-weights) (1)
- [🦾 Robotics and Control](#-robotics-and-control) (3)
  - [Vision-language-action models](#vision-language-action-models) (2)
  - [RL control policies](#rl-control-policies) (1)
- [🧩 Other Domains](#-other-domains) (1)
- [📊 Benchmarks and Evaluations](#-benchmarks-and-evaluations) (1)
- [🛠️ Tools, Harnesses and Agent Skills](#-tools-harnesses-and-agent-skills) (6)
- [🔍 Analyses and Critiques](#-analyses-and-critiques) (2)
- [📚 Foundations and Related Fields](#-foundations-and-related-fields) (14)
  - [Model editing and weight arithmetic](#model-editing-and-weight-arithmetic) (3)
  - [Activation steering and representation engineering](#activation-steering-and-representation-engineering) (4)
  - [Compiled and hand-written weights](#compiled-and-hand-written-weights) (1)
  - [Weight-space learning](#weight-space-learning) (1)
  - [Steering and adapting robot policies](#steering-and-adapting-robot-policies) (5)
- [Legend](#legend)
- [How This List Is Maintained](#how-this-list-is-maintained)
- [Related Lists](#related-lists)
- [Contributing](#contributing)
- [Citation](#citation)

## 🌟 The Original Report

*Where the term comes from.*

- **[Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights](https://rikiyat.github.io/blog/weight-space-programming/)**  
  MIT CSAIL · *Blog report* · 2026-11-02 · `💻 code / results`  
  [[Post](https://rikiyat.github.io/blog/weight-space-programming/)] [[Thread](https://x.com/rikiyatakehi/status/2117313742891327994)] [[Code](https://github.com/RikiyaT/lm_understand-logs)] ![GitHub stars](https://img.shields.io/github/stars/RikiyaT/lm_understand-logs?style=social)  
  GPT-6 Astra names what networks were trained on from their weights alone, repairs a stuck Kinetix car policy (0% to 100%, 3.5% of weights, one reply, no tools), writes MinAtar and 9x9 Go networks from zero, and lifts Qwen3.5-0.8B on MATH-500 from 7.9% to 48.1% by removing a loop direction (0.016% of weights). Edits removed a blocker; they did not add a missing ability (Gemma 3 270M: no gain).

## 💬 Language Models

*Reading, repairing and writing the weights of language models.*

### Repairing behavior

- **[weights_editing: replicating Sparks of Weight-Space Programming across LLMs](https://github.com/alan-turing-institute/weights_editing)**  
  The Alan Turing Institute · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/alan-turing-institute/weights_editing)] ![GitHub stars](https://img.shields.io/github/stars/alan-turing-institute/weights_editing?style=social)  
  Replicates the weight-editing experiments with several LLMs as the editor.

- **[OpenWSP](https://github.com/openwsp/openwsp)**  
  OpenWSP · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/openwsp/openwsp)] ![GitHub stars](https://img.shields.io/github/stars/openwsp/openwsp?style=social)  
  An open replication with a Python kernel over weights, a forward-pass service and a versioned edit format (CLI, SDK and MCP server). The math replication was in progress when checked, and its one-shot car repair with an open model failed.

### Reading and predicting from weights

- **[Weight-space programming autoresearch](https://github.com/csinva/weight-space-programming-autoresearch)**  
  csinva · *GitHub* · 2026-11 · `💻 code / results`  
  [[Code](https://github.com/csinva/weight-space-programming-autoresearch)] ![GitHub stars](https://img.shields.io/github/stars/csinva/weight-space-programming-autoresearch?style=social)  
  Claude, running as a coding agent, hand-writes transformer weights: 959 programs, and all 10 algorithmic tasks reach 100% within three attempts. A second test is mostly negative: Claude Opus 5.5 reading Qwen3.5-0.8B weights predicts the effects of 420 edits only slightly better than without the numbers (+0.06 correlation).

## 🦾 Robotics and Control

*Weight edits on robot policies, VLAs, world action models and controllers.*

### Vision-language-action models

- **[Astra weight edits on a VLA, a world action model and humanoid control](https://x.com/Lingxiao234/status/2118048171649806424)**  
  Lingxiao Guo, Angchen Xie · *X thread* · 2026-11-04 · `💬 post only`  
  [[Thread](https://x.com/Lingxiao234/status/2118048171649806424)]  
  π0.5 on 5 RoboTwin 2.0 tasks: 27% to 65% with about 4 edits on held-out episodes; on one task 4 of 3.6B parameters took success from 28/92 to 82/92. FastWAM gains 8.7 points. Unitree G1 policies adapt to a hidden payload by rewiring waist and knee gains. Candidates are found by probing saved inputs offline, then checked with rollouts.

- **[Weight-Space Programming for VLAs](https://github.com/Geeksongs/Weight-Space-Programming-VLA)**  
  Geeksongs · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/Geeksongs/Weight-Space-Programming-VLA)] [[Model](https://huggingface.co/pythonsong/smolvla-libero-wsp-B35)] ![GitHub stars](https://img.shields.io/github/stars/Geeksongs/Weight-Space-Programming-VLA?style=social)  
  Changing one number in SmolVLA (the x-action output bias) lifts a LIBERO-Spatial task from 42/100 to 64/100 on unseen initial states (Fisher p = 0.003). The fault was read off rollouts: the gripper closed too far along x and regrasped.

### RL control policies

- **[Policy Surgery](https://github.com/latentpaths/policy-surgery)**  
  latentpaths · *GitHub* · 2026-11-02 · `💻 code / results`  
  [[Code](https://github.com/latentpaths/policy-surgery)] [[Project](https://www.latentpaths.com/projects/policy-surgery)] ![GitHub stars](https://img.shields.io/github/stars/latentpaths/policy-surgery?style=social)  
  GPT-OSS-120B edits a 4,996-parameter LunarLander PPO actor after its dynamics change. Reversed thrusters: 0 to 226 of 256 held-out episodes. Crosswind and reduced thrust gain 3 to 6 points, and only one of those intervals excludes zero. Separate selection, approval and test seeds, with every failure kept.

## 🧩 Other Domains

*Classifiers, small decision networks and anything else.*

- **[Weight-space programming for auditing clinical decision networks](https://arxiv.org/abs/2611.05341)**  
  Henry Ford Health · *Preprint* · 2026-11-03 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.05341)] ![GitHub stars](https://img.shields.io/github/stars/hnusrat1/weightspace-rt?style=social)  
  Claude Opus 5.5 audited small head-and-neck planning-request screening networks (433 to 4,801 parameters) blind, without tools, data or code execution. It named the broken rule in 16 of 18 flawed networks and repaired each of the 16 by changing a median of 3 parameters. Checks used about 420,000 requests.

## 📊 Benchmarks and Evaluations

*Controlled tests of whether weight access helps.*

- **[WSPBench](https://github.com/alexcarterhq/wspbench)**  
  alexcarterhq · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/alexcarterhq/wspbench)] [[Project](https://wspbench.com)] ![GitHub stars](https://img.shields.io/github/stars/alexcarterhq/wspbench?style=social)  
  Does weight access help an agent diagnose and repair a model? GPT-6.1 Sol repaired 30/32 faults with behavior probes plus weights, against 14/32 with probes alone and 5/32 for a scripted solver at the same probe budget. All three kept 8 clean controls intact.

## 🛠️ Tools, Harnesses and Agent Skills

*Libraries and agent skills for reading and editing weights.*

- **[weightspace](https://github.com/leofmarciano/weightspace)**  
  Leo Marciano · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/leofmarciano/weightspace)] ![GitHub stars](https://img.shields.io/github/stars/leofmarciano/weightspace?style=social)  
  Apache-2.0 Python library: read, fix, write and improve any torch.nn.Module with an LLM, using budgeted probes, tracked edits and sparse patches. Its own rerun of the Qwen experiment did not beat the original edit.

- **[weight-space-programming-skill](https://github.com/di37/weight-space-programming-skill)**  
  di37 · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/di37/weight-space-programming-skill)] ![GitHub stars](https://img.shields.io/github/stars/di37/weight-space-programming-skill?style=social)  
  Claude Code skill for improving a small open LLM by editing its weights directly, with no training.

- **[weights-lab](https://github.com/oumi-ai/weights-lab)**  
  Oumi · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/oumi-ai/weights-lab)] ![GitHub stars](https://img.shields.io/github/stars/oumi-ai/weights-lab?style=social)  
  Agent skill for editing LLM weights.

- **[pi-weight-space-programming](https://github.com/felipepenha/pi-weight-space-programming)**  
  Felipe Penha · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/felipepenha/pi-weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/felipepenha/pi-weight-space-programming?style=social)  
  Extension for the Pi coding agent with skills for reading and editing weights.

- **[weight-surgery](https://github.com/lorenzofamiglini/weight-surgery)**  
  Lorenzo Famiglini · *GitHub* · 2026-11-02 · `💻 code / results`  
  [[Code](https://github.com/lorenzofamiglini/weight-surgery)] ![GitHub stars](https://img.shields.io/github/stars/lorenzofamiglini/weight-surgery?style=social)  
  Open agent skill that reads weights first, keeps a fixed forward-pass budget and proves fixes on held-out data. On a BERT NER model, a fitted control beat the hand edit (+0.109 vs +0.032 F1).

- **[weight-space-programming (agent skill)](https://github.com/xero00000/weight-space-programming)**  
  xero00000 · *GitHub* · 2026-11-02 · `💻 code / results`  
  [[Code](https://github.com/xero00000/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/xero00000/weight-space-programming?style=social)  
  Agent skill for reasoning-driven weight inspection, targeted edits and small-network construction.

## 🔍 Analyses and Critiques

*Audits, replications of claims and critical takes.*

- **[The 'Astra can read and write weights to improve Qwen' post is misleading](https://honnibal.dev/blog/astra-read-write-misleading)**  
  Matthew Honnibal · *Blog* · 2026-11-03 · `💬 post only`  
  [[Post](https://honnibal.dev/blog/astra-read-write-misleading)]  
  Separates reading weights directly from repairing a model with code and practice feedback: raw-weight reading without tools appears only on the smallest networks, and the language-model results used Python and forward passes.

- **[MIT team says GPT-6 Astra can improve other AI models by editing their weights. Critics say its biggest result relied on standard ML engineering.](https://www.rdworldonline.com/mit-team-says-gpt-6-astra-can-fix-an-ai-model-by-editing-its-weights-critics-say-the-method-was-standard-ml-engineering/)**  
  R&D World · *News* · 2026-11-03 · `💬 post only`  
  [[Post](https://www.rdworldonline.com/mit-team-says-gpt-6-astra-can-fix-an-ai-model-by-editing-its-weights-critics-say-the-method-was-standard-ml-engineering/)]  
  News coverage of the claims and the methodological pushback.

## 📚 Foundations and Related Fields

*Earlier work the field builds on.*

### Model editing and weight arithmetic

- **[Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089)**  
  Gabriel Ilharco et al. · *ICLR 2023* · 2022-12-08 · `📄 peer-reviewed`  
  [[Paper](https://arxiv.org/abs/2212.04089)] [[Code](https://github.com/mlfoundations/task_vectors)] ![GitHub stars](https://img.shields.io/github/stars/mlfoundations/task_vectors?style=social)  
  Adding and subtracting fine-tuning weight differences (task vectors) steers a model's behavior.

- **[Mass-Editing Memory in a Transformer (MEMIT)](https://arxiv.org/abs/2210.07229)**  
  Kevin Meng, Arnab Sen Sharma, Alex Andonian, Yonatan Belinkov, David Bau · *ICLR 2023* · 2022-10-13 · `📄 peer-reviewed`  
  [[Paper](https://arxiv.org/abs/2210.07229)] [[Code](https://github.com/kmeng01/memit)] [[Project](https://memit.baulab.info/)] ![GitHub stars](https://img.shields.io/github/stars/kmeng01/memit?style=social)  
  Extends ROME to thousands of edits at once across several layers.

- **[Locating and Editing Factual Associations in GPT (ROME)](https://arxiv.org/abs/2202.05262)**  
  Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov · *NeurIPS 2022* · 2022-02-10 · `📄 peer-reviewed`  
  [[Paper](https://arxiv.org/abs/2202.05262)] [[Code](https://github.com/kmeng01/rome)] [[Project](https://rome.baulab.info/)] ![GitHub stars](https://img.shields.io/github/stars/kmeng01/rome?style=social)  
  Rank-one edits to a single MLP layer rewrite a stored fact.

### Activation steering and representation engineering

- **[Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717)**  
  Andy Arditi et al. · *NeurIPS 2024* · 2024-06-17 · `📄 peer-reviewed`  
  [[Paper](https://arxiv.org/abs/2406.11717)]  
  Orthogonalizing weights against one direction removes refusal. It is the same kind of edit as the Qwen loop fix.

- **[Steering Llama 2 via Contrastive Activation Addition (CAA)](https://arxiv.org/abs/2312.06681)**  
  Nina Rimsky et al. · *ACL 2024* · 2023-12-09 · `📄 peer-reviewed`  
  [[Paper](https://arxiv.org/abs/2312.06681)]  
  Steering vectors from paired positive and negative examples shift behaviors such as sycophancy.

- **[Representation Engineering: A Top-Down Approach to AI Transparency](https://arxiv.org/abs/2310.01405)**  
  Andy Zou et al. · *Preprint* · 2023-10-02 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2310.01405)] [[Code](https://github.com/andyzoujm/representation-engineering)] ![GitHub stars](https://img.shields.io/github/stars/andyzoujm/representation-engineering?style=social)  
  Reads and controls high-level concepts through population-level directions in representations.

- **[Steering Language Models With Activation Engineering (ActAdd)](https://arxiv.org/abs/2308.10248)**  
  Alexander Matt Turner et al. · *Preprint* · 2023-08-20 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2308.10248)]  
  Adds a direction computed from contrasting prompts to the residual stream at inference.

### Compiled and hand-written weights

- **[Tracr: Compiled Transformers as a Laboratory for Interpretability](https://arxiv.org/abs/2301.05062)**  
  David Lindner et al. · *NeurIPS 2023* · 2023-01-12 · `📄 peer-reviewed`  
  [[Paper](https://arxiv.org/abs/2301.05062)] [[Code](https://github.com/google-deepmind/tracr)] ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/tracr?style=social)  
  Compiles RASP programs into transformer weights with known structure.

### Weight-space learning

- **[A Survey of Weight Space Learning: Understanding, Representation, and Generation](https://arxiv.org/abs/2603.10090)**  
  Xiaolong Han et al. · *Preprint* · 2026-03-10 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2603.10090)]  
  Taxonomy of learning on weights: geometry and symmetries, weight embeddings, and weight generation.

### Steering and adapting robot policies

- **[Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts (DART)](https://arxiv.org/abs/2607.00666)**  
  Taewook Kang, Taeheon Kim, Donghyun Shin, Jonghyun Choi · *Preprint* · 2026-07-01 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2607.00666)]  
  Adapts a VLA to camera and embodiment shifts from one demonstration through weight-vector arithmetic with subspace alignment.

- **[Steering Robustness into World Action Models via Mechanistic Interpretability and Optimal Control (WA-LQR)](https://arxiv.org/abs/2607.14943)**  
  *Preprint* · 2026-07 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2607.14943)]  
  Closed-loop LQR activation steering of Cosmos-Policy, DiT4DiT and LingBot-VA under camera, gripper and noise perturbations. Linear separability predicts which models can be steered.

- **[DiMaS: Distribution Matching for Steering Vision-Language-Action Models](https://arxiv.org/abs/2607.14280)**  
  Khayatan, Meziane, Parekh, Cord · *Preprint* · 2026-07 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2607.14280)] [[Code](https://github.com/pegah-kh/dimas)] ![GitHub stars](https://img.shields.io/github/stars/pegah-kh/dimas?style=social)  
  In flow-matching VLAs, behavioral features are linearly decodable but not linearly steerable, which motivates distribution matching instead.

- **[Robotic Policy Adaptation via Weight-Space Meta-Learning (WIZARD)](https://arxiv.org/abs/2606.07217)**  
  Christian Bianchi et al. · *Preprint* · 2026-06 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2606.07217)]  
  A meta-network turns language and video into LoRA weights for a frozen VLA, with no test-time optimization.

- **[Contrastive Conceptor Activation Steering (COAST): Unlocking Vision-Language-Action Models through Hidden States](https://arxiv.org/abs/2605.17144)**  
  Miranda Muqing Miao, Subin Kim, Brandon Yang, Lyle Ungar · *Preprint* · 2026-05 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2605.17144)]  
  Training-free conceptor steering of a VLA's action-expert residual stream (GR00T N1.5), learned from a few success and failure rollouts.

## Legend

`📄 peer-reviewed` · `📝 preprint` · `💻 code / results` · `💬 post only`

Entries are newest first within each section. Summaries report the source's own numbers and settings. Evidence labels say what kind of source backs an entry, not whether its claims hold.

## How This List Is Maintained

An automated sweep (daily) checks arXiv, GitHub and the Hugging Face Hub for new work. Entries need to do weight-space programming or be direct groundwork for it. On-topic papers are listed whatever their traction; repositories are listed once they show traction or come from an organization, and young ones are kept on a watch list and re-checked. Categories grow as the field does: a new section opens when work no longer fits the existing ones. Corrections are welcome as issues or pull requests.

## Related Lists

- [Awesome Weight Space Learning](https://github.com/Zehong-Wang/Awesome-Weight-Space-Learning): learning on and generating weights.
- [Awesome Weight-Space Learning (ege-erdogan)](https://github.com/ege-erdogan/awesome-weight-space-learning)
- [Knowledge Editing Papers](https://github.com/zjunlp/KnowledgeEditingPapers): editing facts in LLMs.
- [Awesome LLM Interpretability](https://github.com/JShollaj/awesome-llm-interpretability)
- [Awesome VLA & WAM](https://github.com/DravenALG/awesome-vla-wam): robot foundation models.
- [awesome-weight-space-programming (brighterr)](https://github.com/brighterr/awesome-weight-space-programming): another list on the same topic.

## Contributing

Add an object to [`data/entries.json`](data/entries.json), run `python3 scripts/build.py`, and open a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) for the fields and inclusion rules.

## Citation

```bibtex
@misc{awesome-weight-space-programming,
  author       = {Pakdamansavoji, Sajjad},
  title        = {Awesome Weight-Space Programming},
  year         = {2026},
  howpublished = {\url{https://github.com/SajjadPSavoji/awesome-weight-space-programming}}
}
```

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=SajjadPSavoji/awesome-weight-space-programming&type=Date)](https://star-history.com/#SajjadPSavoji/awesome-weight-space-programming&Date)
